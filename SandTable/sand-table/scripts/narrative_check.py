#!/usr/bin/env python3
"""Impossible Narrative Detection for Sand Table simulations.

Implements the 5 signals from references/reliability.md that catch
"single-author" patterns in multi-agent output (one LLM writing all voices
instead of independent agents).

Conservative by design — flags only when a roster name appears within
~40 characters (≈8 words) of a trigger phrase, to keep false positives low.
The doc treats 1-5 warnings as "minor leakage, likely still valid";
6+ as "INTEGRITY CONCERN".

Usage as library:
    from narrative_check import scan
    report = scan(stream_dict)

Usage as CLI:
    python narrative_check.py stream.json
    python narrative_check.py stream.json --json
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import NamedTuple


# ---------------------------------------------------------------------------
# Signal patterns (hard-coded; see references/reliability.md lines 17-49)
# ---------------------------------------------------------------------------

# Signals 1-3: name-aware. {NAME} is substituted per other-roster-agent at scan time.
# Use \b{NAME}\b and require a trigger verb within ~40 chars.
# Gap pattern: up to 40 chars but no sentence terminators (.!?). Bounded to prevent backtracking blowups.
_GAP = r"[^.!?\n]{0,40}"

SIGNAL_1_OTHER_AGENT_PREDICTIONS = [
    r"\b{NAME}\b" + _GAP + r"\b(will|going to|gonna|about to)\b\W+\w+",
    r"\b(she|he|they)'?ll" + _GAP + r"probably\W+\w+",
    r"\b(she|he|they)" + _GAP + r"(is going to|will probably)\b",
]

SIGNAL_2_INTERNAL_STATE = [
    r"\b{NAME}\b" + _GAP + r"\b(is thinking|feels|is feeling|is struggling with|is excited about|is worried about)\b",
    r"\b{NAME}\b" + _GAP + r"\b(realizes|notices|understands)\b",
]

SIGNAL_3_META_COMMENTARY = [
    r"\bthe (most|strongest|weakest|best|worst)\b" + _GAP + r"\bin (the )?cohort\b",
    r"\bunlike (the )?(others|rest)\b",
    r"\bcompared to \b{NAME}\b",
    r"\b(strongest|weakest) response (so far|yet)\b",
]

# Signal 4: standalone phrases (no name dependency).
SIGNAL_4_SCORING_AWARENESS = [
    r"\bthis (will|should|would) (score|register|rate)\b",
    r"\bthe (leader|facilitator|evaluator) will (see|notice|score)\b",
    r"\bthis demonstrates (growth|progress|the)\b",
    r"\bthis should (count|register) as\b",
]

# Pre-compile signals 1-3 templates and signal 4 patterns.
_SIG4_COMPILED = [re.compile(p, re.IGNORECASE) for p in SIGNAL_4_SCORING_AWARENESS]


class Flag(NamedTuple):
    event_index: int
    agent_id: str
    signal: int          # 1-5
    phrase: str
    snippet: str         # ~100 char excerpt around the match


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Free-text fields scanned for signals 1-4 at the top level of an event.
# Nested dict/list payloads (payload.speech, content.body, message.text, etc.) are
# also scanned via _collect_text() recursion — see _NON_PROSE_KEYS denylist below.
TEXT_FIELDS = ("internal_monologue", "text", "spoken", "narrative", "reflection")

# Keys that should NOT be scanned as prose, even when they contain strings.
# Add to this set if a new structural/metadata field starts producing false flags.
_NON_PROSE_KEYS = frozenset({
    "id", "agent", "persona", "from_persona", "to_persona", "from", "to",
    "recipient", "timestamp", "time", "time_offset", "duration_min", "type",
    "status", "scores", "rating", "score", "module", "section", "unit",
    "module_id", "section_id", "unit_id", "persona_id", "agent_id", "run", "ttl",
})

_MAX_RECURSION_DEPTH = 4  # bound nested-dict walk; events should never need more

# Stopword 3-grams for signal 5 (drop these from "shared rare n-grams" count).
_STOPWORD_NGRAMS = frozenset({
    "i think that", "and i was", "this is the", "it is a", "i would like",
    "thank you for", "i am going", "we need to", "let me know", "i don't know",
    "good to see", "nice to meet", "how are you", "what do you", "i can see",
})

_MAX_TEXT_LEN = 4000  # truncate long fields to bound regex work


def _collect_text(obj, depth: int = 0) -> list[str]:
    """Recursively pull every prose string out of an event, capped depth.

    Skips structural/metadata keys (see _NON_PROSE_KEYS) so IDs, timestamps,
    and numeric scores never reach the regex scanners. Catches dialogue/prose
    nested under payload, content, message, body, and similar wrappers — closes
    the nested-payload smuggling gap where flat TEXT_FIELDS scanning misses
    the real text.
    """
    if depth > _MAX_RECURSION_DEPTH:
        return []
    if isinstance(obj, str):
        return [obj[:_MAX_TEXT_LEN]] if obj else []
    if isinstance(obj, dict):
        out: list[str] = []
        for k, v in obj.items():
            if k in _NON_PROSE_KEYS:
                continue
            out.extend(_collect_text(v, depth + 1))
        return out
    if isinstance(obj, list):
        out = []
        for v in obj:
            out.extend(_collect_text(v, depth + 1))
        return out
    return []


def _first_token(name) -> str:
    if not isinstance(name, str):
        return ""
    stripped = name.strip()
    return stripped.split()[0] if stripped else ""


def _build_other_agents_map(agents: list[dict]) -> dict[str, list[str]]:
    """Map each agent_id -> list of name tokens for OTHER agents.

    Use first-token matching (LLMs say 'Maria' not 'Maria Chen'). On first-token
    collision (two agents share a first name), fall back to including the full
    name as well so disambiguation is possible.
    """
    by_id = {a.get("id", ""): a.get("name", "") for a in agents if a.get("id")}
    first_tokens: dict[str, list[str]] = {}
    for aid, name in by_id.items():
        ft = _first_token(name).lower()
        first_tokens.setdefault(ft, []).append(aid)

    result: dict[str, list[str]] = {}
    for aid in by_id:
        own_first = _first_token(by_id[aid]).lower()
        others = []
        for other_id, other_name in by_id.items():
            if other_id == aid:
                continue
            ot = _first_token(other_name).lower()
            if ot and ot != own_first:
                others.append(other_name.split()[0])
                # If first-token collision exists for this other agent, also add full name.
                if len(first_tokens.get(ot, [])) > 1:
                    others.append(other_name)
        result[aid] = others
    return result


def _snippet(text: str, match: re.Match, width: int = 100) -> str:
    start = max(0, match.start() - width // 2)
    end = min(len(text), match.end() + width // 2)
    return ("..." if start > 0 else "") + text[start:end].strip() + ("..." if end < len(text) else "")


def _scan_signals_1_to_3(text: str, other_names: list[str], agent_id: str, idx: int) -> list[Flag]:
    flags: list[Flag] = []
    if not other_names:
        return flags
    for name in other_names:
        name_re = re.escape(name)
        for sig_id, templates in (
            (1, SIGNAL_1_OTHER_AGENT_PREDICTIONS),
            (2, SIGNAL_2_INTERNAL_STATE),
            (3, SIGNAL_3_META_COMMENTARY),
        ):
            for tmpl in templates:
                pat = tmpl.replace("{NAME}", name_re)
                try:
                    rx = re.compile(pat, re.IGNORECASE)
                except re.error:
                    continue
                for m in rx.finditer(text):
                    flags.append(Flag(idx, agent_id, sig_id, m.group(0), _snippet(text, m)))
    return flags


def _scan_signal_4(text: str, agent_id: str, idx: int) -> list[Flag]:
    flags: list[Flag] = []
    for rx in _SIG4_COMPILED:
        for m in rx.finditer(text):
            flags.append(Flag(idx, agent_id, 4, m.group(0), _snippet(text, m)))
    return flags


def _ngrams(text: str, n: int = 3) -> list[str]:
    words = re.findall(r"[a-z']+", text.lower())
    return [" ".join(words[i:i + n]) for i in range(len(words) - n + 1)]


def _scan_signal_5_pairs(events: list[dict]) -> list[Flag]:
    """Look for synchronized exchange pairs.

    A pair = consecutive events where event N+1's from/to reverses event N's.
    Flag if both texts share > 3 rare 3-grams AND combined length > 200 chars.
    """
    flags: list[Flag] = []
    for i in range(len(events) - 1):
        a, b = events[i], events[i + 1]
        a_from = a.get("from_persona") or a.get("from") or a.get("agent") or a.get("persona")
        a_to = a.get("to_persona") or a.get("to") or a.get("recipient")
        b_from = b.get("from_persona") or b.get("from") or b.get("agent") or b.get("persona")
        b_to = b.get("to_persona") or b.get("to") or b.get("recipient")
        if not (a_from and a_to and b_from and b_to):
            continue
        if not (a_from == b_to and a_to == b_from):
            continue

        a_text = " ".join(_collect_text(a))
        b_text = " ".join(_collect_text(b))
        if len(a_text) + len(b_text) < 200:
            continue

        a_ngrams = set(_ngrams(a_text)) - _STOPWORD_NGRAMS
        b_ngrams = set(_ngrams(b_text)) - _STOPWORD_NGRAMS
        shared = a_ngrams & b_ngrams
        if len(shared) > 3:
            preview = ", ".join(sorted(shared)[:3])
            flags.append(Flag(i, str(a_from), 5, f"shared {len(shared)} 3-grams", f"pair[{i},{i+1}] shares: {preview}"))
    return flags


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

SIGNAL_NAMES = {
    1: "other-agent predictions",
    2: "internal-state knowledge",
    3: "meta-commentary",
    4: "scoring awareness",
    5: "synchronized exchanges",
}


def scan(data: dict) -> dict:
    """Scan an event stream for impossible-narrative signals.

    Returns:
        {
          "total": int,
          "by_signal": {1: count, 2: count, ...},
          "bucket": "CLEAN" | "WARNING" | "INTEGRITY CONCERN",
          "flags": [Flag tuples...],
        }
    """
    agents = data.get("agents", [])
    events = data.get("events", [])
    other_names_map = _build_other_agents_map(agents)

    all_flags: list[Flag] = []

    for idx, ev in enumerate(events):
        agent_id = ev.get("agent") or ev.get("persona") or ev.get("from_persona") or ""
        if not agent_id:
            continue
        text_parts = _collect_text(ev)
        if not text_parts:
            continue
        text = "\n".join(text_parts)

        other_names = other_names_map.get(agent_id, [])
        all_flags.extend(_scan_signals_1_to_3(text, other_names, agent_id, idx))
        all_flags.extend(_scan_signal_4(text, agent_id, idx))

    all_flags.extend(_scan_signal_5_pairs(events))

    by_signal: dict[int, int] = {i: 0 for i in range(1, 6)}
    for f in all_flags:
        by_signal[f.signal] += 1

    total = len(all_flags)
    if total == 0:
        bucket = "CLEAN"
    elif total <= 5:
        bucket = "WARNING"
    else:
        bucket = "INTEGRITY CONCERN"

    return {
        "total": total,
        "by_signal": by_signal,
        "bucket": bucket,
        "flags": all_flags,
    }


def format_report(report: dict, max_examples: int = 5) -> str:
    lines = [
        "Narrative Integrity",
        "-------------------",
        f"Status: {report['bucket']} ({report['total']} flag(s))",
        "",
        "By signal:",
    ]
    for sig_id in range(1, 6):
        count = report["by_signal"][sig_id]
        marker = "•" if count else "·"
        lines.append(f"  {marker} Signal {sig_id} ({SIGNAL_NAMES[sig_id]}): {count}")
    if report["flags"]:
        lines.append("")
        lines.append(f"First {min(max_examples, len(report['flags']))} examples:")
        for f in report["flags"][:max_examples]:
            lines.append(f"  - event[{f.event_index}] agent={f.agent_id} sig{f.signal}: {f.snippet}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan a Sand Table event stream for impossible-narrative signals.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text report")
    args = parser.parse_args()

    data = json.loads(args.input.read_text())
    report = scan(data)

    if args.json:
        # Convert Flag tuples to dicts for JSON serialization.
        out = {**report, "flags": [f._asdict() for f in report["flags"]]}
        print(json.dumps(out, indent=2))
    else:
        print(format_report(report))

    # Always exit 0 — narrative check is advisory, not a gate.
    sys.exit(0)


if __name__ == "__main__":
    main()
