#!/usr/bin/env python3
"""Regression tests for narrative_check.py and validate_full.py score clamping.

Covers every fix from the subagent-panel hardening rounds (R1-R3) plus the
v1.5.0 additions: Signal 6 self-dissociation, quote-stripping, boolean clamp.

Run with: python3 -m unittest test_narrative_check.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from narrative_check import (
    _agent_name_variants,
    _build_other_agents_map,
    _collect_text,
    _first_token,
    _strip_quoted_speech,
    _MAX_TOTAL_TEXT,
    scan,
)
from validate_full import clamp_scores


class TestFirstToken(unittest.TestCase):
    """R1 Adversary: _first_token must not crash on non-string input."""

    def test_handles_none(self):
        self.assertEqual(_first_token(None), "")

    def test_handles_empty(self):
        self.assertEqual(_first_token(""), "")

    def test_handles_whitespace_only(self):
        self.assertEqual(_first_token("   "), "")

    def test_handles_non_string_types(self):
        self.assertEqual(_first_token(123), "")
        self.assertEqual(_first_token(["unexpected"]), "")
        self.assertEqual(_first_token({"k": "v"}), "")

    def test_returns_first_token_of_full_name(self):
        self.assertEqual(_first_token("Maria Chen"), "Maria")

    def test_strips_surrounding_whitespace(self):
        self.assertEqual(_first_token("  Alex  "), "Alex")


class TestAgentNameVariants(unittest.TestCase):
    """R3 Adversary: aliases must be collected to close nickname gap."""

    def test_name_only(self):
        self.assertEqual(_agent_name_variants({"name": "Robert Stevens"}), ["Robert"])

    def test_name_with_aliases(self):
        agent = {"name": "Robert Stevens", "aliases": ["Bob", "Bobby"]}
        variants = _agent_name_variants(agent)
        self.assertIn("Robert", variants)
        self.assertIn("Bob", variants)
        self.assertIn("Bobby", variants)

    def test_alias_first_token_reduced(self):
        agent = {"name": "Robert", "aliases": ["Bob Smith"]}
        self.assertIn("Bob", _agent_name_variants(agent))

    def test_dedupes_collisions(self):
        agent = {"name": "Bob", "aliases": ["Bob"]}
        self.assertEqual(_agent_name_variants(agent), ["Bob"])

    def test_missing_name_with_aliases(self):
        agent = {"aliases": ["Bob"]}
        self.assertEqual(_agent_name_variants(agent), ["Bob"])

    def test_none_aliases_field(self):
        # Some serializers emit explicit null
        agent = {"name": "Robert", "aliases": None}
        self.assertEqual(_agent_name_variants(agent), ["Robert"])


class TestCollectText(unittest.TestCase):
    """R2 Adversary: must walk nested payloads; R3 Adversary: must bound totals."""

    def test_picks_up_flat_text(self):
        ev = {"agent": "a", "text": "hello world"}
        self.assertEqual(_collect_text(ev), ["hello world"])

    def test_walks_nested_payload(self):
        # Smuggling regression: prose under payload.narration.speech
        ev = {"agent": "a", "payload": {"narration": {"speech": "Bob will fold."}}}
        collected = _collect_text(ev)
        self.assertIn("Bob will fold.", collected)

    def test_skips_non_prose_keys(self):
        ev = {"agent": "a", "id": "evt-1", "timestamp": "2026-01-01"}
        # Only structural keys → nothing to scan
        self.assertEqual(_collect_text(ev), [])

    def test_caps_total_bytes_against_breadth_bomb(self):
        # R3 Adversary: {"payload":[{"x":"a"*4000}]*N} should not balloon
        big_payload = [{"x": "a" * 4000}] * 1000  # ~4 MB raw
        ev = {"agent": "a", "payload": big_payload}
        collected = _collect_text(ev)
        total = sum(len(s) for s in collected)
        self.assertLessEqual(total, _MAX_TOTAL_TEXT + 4000)  # +1 chunk slack

    def test_respects_recursion_depth(self):
        # Build a 10-deep nest; only first 4 levels should be visited.
        nest = "deep"
        for _ in range(10):
            nest = {"wrap": nest}
        result = _collect_text(nest)
        self.assertEqual(result, [])  # too deep — returns empty


class TestQuoteStripping(unittest.TestCase):
    """v1.5.0: quoted speech is out-of-voice and must not feed name signals."""

    def test_strips_double_quotes(self):
        text = 'She said "Bob will fold" to the room.'
        stripped = _strip_quoted_speech(text)
        self.assertNotIn("Bob", stripped)
        # Preserve length / offsets
        self.assertEqual(len(stripped), len(text))

    def test_strips_smart_quotes(self):
        text = "She said “Bob will fold” to the room."
        stripped = _strip_quoted_speech(text)
        self.assertNotIn("Bob", stripped)

    def test_preserves_apostrophes(self):
        text = "It's Bob's turn, won't you say so?"
        stripped = _strip_quoted_speech(text)
        # Single quotes / apostrophes must NOT be stripped
        self.assertEqual(stripped, text)

    def test_no_op_when_no_quotes(self):
        text = "Maria thought about leaving."
        self.assertEqual(_strip_quoted_speech(text), text)


class TestBuildOtherAgentsMap(unittest.TestCase):
    def test_basic_two_agents(self):
        agents = [{"id": "a", "name": "Maria"}, {"id": "b", "name": "Bob"}]
        m = _build_other_agents_map(agents)
        self.assertIn("Bob", m["a"])
        self.assertIn("Maria", m["b"])

    def test_aliases_included(self):
        # R3 fix
        agents = [
            {"id": "r", "name": "Robert", "aliases": ["Bob"]},
            {"id": "m", "name": "Maria"},
        ]
        m = _build_other_agents_map(agents)
        self.assertIn("Robert", m["m"])
        self.assertIn("Bob", m["m"])

    def test_first_token_collision_includes_full_name(self):
        agents = [
            {"id": "a", "name": "Alex Anderson"},
            {"id": "b", "name": "Alex Brown"},
            {"id": "c", "name": "Carol"},
        ]
        m = _build_other_agents_map(agents)
        # Carol should see both full names because "Alex" collides
        self.assertIn("Alex Anderson", m["c"])
        self.assertIn("Alex Brown", m["c"])


class TestSignal1(unittest.TestCase):
    """Other-agent predictions."""

    def test_fires_on_basic_prediction(self):
        data = {
            "agents": [
                {"id": "m", "name": "Maria"},
                {"id": "b", "name": "Bob"},
            ],
            "events": [{"agent": "m", "text": "Bob will probably fold here."}],
        }
        report = scan(data)
        self.assertGreaterEqual(report["by_signal"][1], 1)

    def test_alias_match_fires(self):
        # R3 regression: nickname must be tracked
        data = {
            "agents": [
                {"id": "r", "name": "Robert", "aliases": ["Bob"]},
                {"id": "m", "name": "Maria"},
            ],
            "events": [{"agent": "m", "text": "Bob will probably fold."}],
        }
        report = scan(data)
        self.assertGreaterEqual(report["by_signal"][1], 1)

    def test_does_not_fire_on_own_name(self):
        # Signal 1 is about OTHER agents' predictions, not self-reference
        # (self-reference is Signal 6's job).
        data = {
            "agents": [{"id": "m", "name": "Maria"}, {"id": "b", "name": "Bob"}],
            "events": [{"agent": "m", "text": "Maria will keep going."}],
        }
        report = scan(data)
        self.assertEqual(report["by_signal"][1], 0)

    def test_quoted_prediction_no_longer_false_positives(self):
        # v1.5.0 regression: prediction inside quoted customer dialogue
        data = {
            "agents": [{"id": "m", "name": "Maria"}, {"id": "b", "name": "Bob"}],
            "events": [{"agent": "m", "text": 'The customer said "Bob will fold soon".'}],
        }
        report = scan(data)
        # Quoted speech is out-of-voice — Signal 1 should NOT fire
        self.assertEqual(report["by_signal"][1], 0)


class TestSignal6(unittest.TestCase):
    """v1.5.0: self-name third-person dissociation."""

    def test_fires_on_self_third_person_cognitive(self):
        data = {
            "agents": [{"id": "m", "name": "Maria"}, {"id": "b", "name": "Bob"}],
            "events": [
                {"agent": "m", "text": "Maria knew exactly how this would land."}
            ],
        }
        report = scan(data)
        self.assertGreaterEqual(report["by_signal"][6], 1)

    def test_does_not_fire_on_other_agent_third_person(self):
        # If MARIA narrates BOB in third person, that's Signal 1/2, not 6
        data = {
            "agents": [{"id": "m", "name": "Maria"}, {"id": "b", "name": "Bob"}],
            "events": [{"agent": "m", "text": "Bob knew exactly how this would land."}],
        }
        report = scan(data)
        self.assertEqual(report["by_signal"][6], 0)

    def test_alias_self_dissociation(self):
        # Roster Robert with alias Bob; agent narrating "Bob knew..."
        data = {
            "agents": [{"id": "r", "name": "Robert", "aliases": ["Bob"]}],
            "events": [{"agent": "r", "text": "Bob knew the room was watching."}],
        }
        report = scan(data)
        self.assertGreaterEqual(report["by_signal"][6], 1)


class TestSignal3QuoteStrip(unittest.TestCase):
    """R1 Adversary case B: 'compared to Alex' inside customer quote
    should not trip Signal 3."""

    def test_compared_to_inside_quote_clean(self):
        data = {
            "agents": [{"id": "a", "name": "Alex"}, {"id": "x", "name": "Alexandra"}],
            "events": [
                {
                    "agent": "a",
                    "text": 'The customer said, "compared to Alex, your service is slow."',
                }
            ],
        }
        report = scan(data)
        # The Signal 3 phrase "compared to Alex" was inside quoted customer
        # speech — should NOT fire against Alex (the agent's own name) or
        # Alexandra.
        self.assertEqual(report["by_signal"][3], 0)


class TestSmugglingRegression(unittest.TestCase):
    """R2 Adversary: prose nested under payload/content/body must be scanned."""

    def test_nested_payload_caught(self):
        data = {
            "agents": [{"id": "m", "name": "Maria"}, {"id": "b", "name": "Bob"}],
            "events": [
                {"agent": "m", "payload": {"narration": {"speech": "Bob will fold."}}}
            ],
        }
        report = scan(data)
        self.assertGreaterEqual(report["by_signal"][1], 1)


class TestClampScoresBooleanFix(unittest.TestCase):
    """v1.5.0: bool is a subclass of int — must be rejected, not coerced."""

    def test_bool_rejected_not_coerced(self):
        data = {"events": [{"scores": {"clarity": True, "depth": False}}]}
        actions = clamp_scores(data, (0, 5))
        self.assertEqual(actions, [])
        # Verify bools were NOT silently rewritten to 1/0
        self.assertIs(data["events"][0]["scores"]["clarity"], True)
        self.assertIs(data["events"][0]["scores"]["depth"], False)

    def test_real_numbers_still_clamped(self):
        data = {"events": [{"scores": {"clarity": 7, "depth": -1}}]}
        actions = clamp_scores(data, (0, 5))
        self.assertEqual(len(actions), 2)
        self.assertEqual(data["events"][0]["scores"]["clarity"], 5)
        self.assertEqual(data["events"][0]["scores"]["depth"], 0)


class TestScanReportShape(unittest.TestCase):
    def test_clean_run_returns_expected_keys(self):
        data = {"agents": [{"id": "a", "name": "Alex"}], "events": []}
        report = scan(data)
        self.assertEqual(report["bucket"], "CLEAN")
        self.assertEqual(report["total"], 0)
        # by_signal must cover 1-6 now (was 1-5 before v1.5.0)
        self.assertEqual(set(report["by_signal"].keys()), {1, 2, 3, 4, 5, 6})


if __name__ == "__main__":
    unittest.main(verbosity=2)
