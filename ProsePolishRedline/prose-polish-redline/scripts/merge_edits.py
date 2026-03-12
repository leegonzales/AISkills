#!/usr/bin/env python3
"""merge_edits.py — Conflict resolution and rebasing engine for prose-polish-redline.

Merges edit JSONs from multiple agents across two phases, resolving
duplicates, overlapping edits, and rebasing Phase 2 onto Phase 1 output.

Usage:
    python merge_edits.py \
        --document text.txt \
        --phase1 coherence.json authority.json claims.json stakes.json \
        --phase2 rhythm.json hedge.json \
        -o merged.json
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import NamedTuple

# Highest priority first
TIER_ORDER = ["STRUCTURAL", "COHERENCE", "AUTHORITY", "CRAFT", "VOICE"]


class LocatedEdit(NamedTuple):
    start: int
    end: int
    original_text: str
    new_text: str
    tier: str
    severity: str
    edit_type: str
    comment: str
    kata: str
    agent: str
    phase: int
    after_text: str


# ------------------------------------------------------------------
# 1. Position detection
# ------------------------------------------------------------------

def _normalize_quotes(text: str) -> str:
    """Normalize smart quotes to straight quotes for matching.

    Only normalizes characters that map 1:1 in length so that
    character positions remain valid between original and normalized text.
    """
    return (text
            .replace("\u201c", '"').replace("\u201d", '"')   # smart double
            .replace("\u2018", "'").replace("\u2019", "'"))   # smart single


def _build_fuzzy_pattern(text: str) -> str:
    """Build a regex pattern from agent text that tolerates quote and dash variants.

    Handles the length-mismatch problem: agents may output '--' (2 chars) for
    document em dashes '\u2014' (1 char), or vice versa. Since these aren't 1:1,
    we can't use simple string replacement. Instead, build a regex where each
    dash/quote variant matches any of its counterparts.
    """
    # First normalize quotes (1:1 safe)
    text = _normalize_quotes(text)
    # Normalize spaces around em dashes: collapse ' — ', '— ', ' —' to '—'
    # so the regex builder can emit \s* uniformly without double-matching.
    text = re.sub(r'\s*(—|–)\s*', r'\1', text)
    text = re.sub(r'\s*--\s*', '--', text)
    # Escape for regex
    parts = []
    i = 0
    while i < len(text):
        ch = text[i]
        # em dash variants: --, —, – (with optional surrounding spaces)
        # Document may have ' — ' while agent outputs '—' or vice versa
        if ch == '-' and i + 1 < len(text) and text[i + 1] == '-':
            parts.append(r'\s*(?:--|—|–)\s*')
            i += 2
            continue
        if ch in ('—', '–'):
            parts.append(r'\s*(?:--|—|–)\s*')
            i += 1
            continue
        # smart/straight quote variants (already normalized to straight)
        if ch == '"':
            parts.append(r'(?:"|"|\u201c|\u201d)')
            i += 1
            continue
        if ch == "'":
            parts.append(r"(?:'|'|\u2018|\u2019)")
            i += 1
            continue
        # everything else: regex-escape
        parts.append(re.escape(ch))
        i += 1
    return ''.join(parts)


def locate_edit(document: str, edit: dict, agent: str, phase: int) -> LocatedEdit | None:
    """Find the character span of an edit's original_text in the document."""
    original = edit.get("original_text", "")
    if not original:
        return None

    # Try exact match first
    idx = document.find(original)

    # Fall back to quote-normalized match (fast, handles 1:1 quote changes)
    if idx == -1:
        norm_doc = _normalize_quotes(document)
        norm_orig = _normalize_quotes(original)
        norm_idx = norm_doc.find(norm_orig)
        if norm_idx != -1:
            idx = norm_idx

    # Fall back to fuzzy regex match (handles em dash length mismatches)
    if idx == -1:
        pattern = _build_fuzzy_pattern(original)
        m = re.search(pattern, document)
        if m:
            idx = m.start()
            original = m.group()  # use the actual document text

    if idx == -1:
        return None

    # If we matched via quote normalization, get actual document text
    if idx >= 0 and document[idx:idx + len(original)] != original:
        original = document[idx:idx + len(original)]

    return LocatedEdit(
        start=idx,
        end=idx + len(original),
        original_text=original,
        new_text=edit.get("new_text", ""),
        tier=edit.get("tier", ""),
        severity=edit.get("severity", ""),
        edit_type=edit.get("edit_type", "replace"),
        comment=edit.get("comment", ""),
        kata=edit.get("kata", ""),
        agent=agent,
        phase=phase,
        after_text=edit.get("after_text", ""),
    )


def locate_edits(
    document: str, edits_json: dict
) -> tuple[list[LocatedEdit], list[dict]]:
    """Locate all edits from one agent file.

    Returns (located_edits, unmatched_edits).
    """
    agent = edits_json.get("agent", "unknown")
    phase = edits_json.get("phase", 1)
    located = []
    unmatched = []
    for edit in edits_json.get("edits", []):
        le = locate_edit(document, edit, agent, phase)
        if le is not None:
            located.append(le)
        else:
            original = edit.get("original_text", "")
            if original:  # only track as unmatched if original_text was provided
                unmatched.append({
                    "agent": agent,
                    "original_text": original,
                    "comment": edit.get("comment", ""),
                    "kata": edit.get("kata", ""),
                    "reason": "original_text not found in document",
                })
    return located, unmatched


# ------------------------------------------------------------------
# 2. Deduplication
# ------------------------------------------------------------------

def _dedup_key(e: LocatedEdit) -> tuple:
    return (e.original_text, e.new_text)


def deduplicate(edits: list[LocatedEdit]) -> tuple[list[LocatedEdit], list[dict]]:
    """Remove identical edits (same original + new text). Keep first seen."""
    seen: dict[tuple, LocatedEdit] = {}
    kept: list[LocatedEdit] = []
    discarded: list[dict] = []
    for e in edits:
        key = _dedup_key(e)
        if key in seen:
            discarded.append({
                "edit": _edit_to_dict(e),
                "reason": f"duplicate of edit from {seen[key].agent}",
                "winner": f"{seen[key].agent}",
            })
        else:
            seen[key] = e
            kept.append(e)
    return kept, discarded


# ------------------------------------------------------------------
# 3. Conflict resolution
# ------------------------------------------------------------------

def _tier_rank(tier: str) -> int:
    """Lower number = higher priority."""
    try:
        return TIER_ORDER.index(tier.upper())
    except ValueError:
        return len(TIER_ORDER)


def _overlaps(a: LocatedEdit, b: LocatedEdit) -> bool:
    return a.start < b.end and b.start < a.end


def _contains(outer: LocatedEdit, inner: LocatedEdit) -> bool:
    return outer.start <= inner.start and inner.end <= outer.end


def _resolve_pair(a: LocatedEdit, b: LocatedEdit) -> tuple[LocatedEdit, LocatedEdit, str]:
    """Given two overlapping edits, return (winner, loser, reason)."""
    # Containment: larger span wins
    if _contains(a, b) and not _contains(b, a):
        return a, b, "conflict: contained by larger edit"
    if _contains(b, a) and not _contains(a, b):
        return b, a, "conflict: contained by larger edit"

    # Same target, different replacement — higher tier wins
    if a.original_text == b.original_text:
        rank_a = _tier_rank(a.tier)
        rank_b = _tier_rank(b.tier)
        if rank_a <= rank_b:
            return a, b, "conflict: lower tier"
        else:
            return b, a, "conflict: lower tier"

    # Partial overlap — first in document order wins
    if a.start <= b.start:
        return a, b, "conflict: partial overlap, later edit dropped"
    else:
        return b, a, "conflict: partial overlap, later edit dropped"


def resolve_conflicts(edits: list[LocatedEdit]) -> tuple[list[LocatedEdit], list[dict]]:
    """Resolve overlapping edits. Edits should already be sorted by start."""
    # Sort by start position, then by tier rank (better tier first as tiebreak)
    edits = sorted(edits, key=lambda e: (e.start, _tier_rank(e.tier)))
    survivors: list[LocatedEdit] = []
    discarded: list[dict] = []

    for edit in edits:
        conflict_found = False
        for i, existing in enumerate(survivors):
            if _overlaps(existing, edit):
                winner, loser, reason = _resolve_pair(existing, edit)
                discarded.append({
                    "edit": _edit_to_dict(loser),
                    "reason": reason,
                    "winner": f"{winner.agent}: {winner.original_text[:60]}",
                })
                # If existing lost, swap it out
                if loser is existing:
                    survivors[i] = winner
                conflict_found = True
                break
        if not conflict_found:
            survivors.append(edit)

    return sorted(survivors, key=lambda e: e.start), discarded


# ------------------------------------------------------------------
# 4. Phase 2 rebasing
# ------------------------------------------------------------------

def rebase_phase2(
    document: str,
    phase1_edits: list[LocatedEdit],
    phase2_jsons: list[dict],
) -> tuple[list[LocatedEdit], int]:
    """Rebase Phase 2 edits onto the original document.

    Phase 2 agents operated on text that already had Phase 1 edits applied.
    Their original_text may reference Phase 1 replacement text rather than
    the original document text. We detect this and create composite edits.

    Returns (rebased_edits, rebase_count).
    """
    # Build Phase 1 edit map: replacement_text -> original LocatedEdit
    p1_map: dict[str, LocatedEdit] = {}
    for e in phase1_edits:
        p1_map[e.new_text] = e

    # Build the Phase-1-edited document for locating Phase 2 originals
    p1_sorted = sorted(phase1_edits, key=lambda e: e.start)
    edited_doc = _apply_edits_to_text(document, p1_sorted)

    # Validate: edited doc should be non-empty and contain replacement text
    if not edited_doc:
        print("WARNING: Phase-1-edited document is empty — skipping Wave 2",
              file=sys.stderr)
        return [], 0
    for p1 in p1_sorted:
        if p1.new_text and p1.new_text not in edited_doc:
            print(f"WARNING: Phase 1 edit application may have failed — "
                  f"'{p1.new_text[:60]}...' not found in edited doc",
                  file=sys.stderr)

    rebased: list[LocatedEdit] = []
    rebase_count = 0

    for pj in phase2_jsons:
        agent = pj.get("agent", "unknown")
        for edit in pj.get("edits", []):
            original = edit.get("original_text", "")
            if not original:
                continue

            # Try to find in original document first (untouched text)
            idx = document.find(original)
            if idx != -1:
                le = LocatedEdit(
                    start=idx,
                    end=idx + len(original),
                    original_text=original,
                    new_text=edit.get("new_text", ""),
                    tier=edit.get("tier", ""),
                    severity=edit.get("severity", ""),
                    edit_type=edit.get("edit_type", "replace"),
                    comment=edit.get("comment", ""),
                    kata=edit.get("kata", ""),
                    agent=agent,
                    phase=2,
                    after_text=edit.get("after_text", ""),
                )
                rebased.append(le)
                continue

            # Check if original_text falls within a Phase 1 replacement
            composite = _try_composite(original, edit, agent, p1_map)
            if composite is not None:
                rebased.append(composite)
                rebase_count += 1
                continue

            # Last resort: locate in the edited document and map back
            edited_idx = edited_doc.find(original)
            if edited_idx != -1:
                # Find which Phase 1 edit this overlaps with
                mapped = _map_edited_pos_to_original(
                    edited_idx, len(original), p1_sorted, document, edit, agent
                )
                if mapped is not None:
                    rebased.append(mapped)
                    rebase_count += 1

    return rebased, rebase_count


def _try_composite(
    original: str,
    edit: dict,
    agent: str,
    p1_map: dict[str, LocatedEdit],
) -> LocatedEdit | None:
    """Check if Phase 2's original_text matches a Phase 1 replacement text.

    If so, create a composite: Phase 1's original span + Phase 2's new_text.
    Also handles substring matches within Phase 1 replacements.
    """
    # Exact match: Phase 2 edits exactly the text Phase 1 produced
    if original in p1_map:
        p1 = p1_map[original]
        return LocatedEdit(
            start=p1.start,
            end=p1.end,
            original_text=p1.original_text,
            new_text=edit.get("new_text", ""),
            tier=edit.get("tier", ""),
            severity=edit.get("severity", ""),
            edit_type=edit.get("edit_type", "replace"),
            comment=edit.get("comment", ""),
            kata=edit.get("kata", ""),
            agent=agent,
            phase=2,
            after_text=edit.get("after_text", ""),
        )

    # Substring: Phase 2 edits a portion of Phase 1's replacement text
    for p1_new_text, p1_edit in p1_map.items():
        sub_idx = p1_new_text.find(original)
        if sub_idx != -1:
            # Build composite: Phase 1's original with the substring replaced
            composite_new = p1_new_text[:sub_idx] + edit.get("new_text", "") + p1_new_text[sub_idx + len(original):]
            return LocatedEdit(
                start=p1_edit.start,
                end=p1_edit.end,
                original_text=p1_edit.original_text,
                new_text=composite_new,
                tier=edit.get("tier", ""),
                severity=edit.get("severity", ""),
                edit_type=edit.get("edit_type", "replace"),
                comment=edit.get("comment", ""),
                kata=edit.get("kata", ""),
                agent=agent,
                phase=2,
                after_text=edit.get("after_text", ""),
            )

    return None


def _map_edited_pos_to_original(
    edited_idx: int,
    length: int,
    p1_sorted: list[LocatedEdit],
    document: str,
    edit: dict,
    agent: str,
) -> LocatedEdit | None:
    """Map a position in the Phase-1-edited document back to the original."""
    # Walk through Phase 1 edits tracking offset shifts
    offset = 0
    for p1 in p1_sorted:
        delta = len(p1.new_text) - len(p1.original_text)
        # If the Phase 2 edit starts within this Phase 1 replacement zone
        orig_replacement_start = p1.start + offset
        orig_replacement_end = orig_replacement_start + len(p1.new_text)
        if orig_replacement_start <= edited_idx < orig_replacement_end:
            return LocatedEdit(
                start=p1.start,
                end=p1.end,
                original_text=p1.original_text,
                new_text=edit.get("new_text", ""),
                tier=edit.get("tier", ""),
                severity=edit.get("severity", ""),
                edit_type=edit.get("edit_type", "replace"),
                comment=edit.get("comment", ""),
                kata=edit.get("kata", ""),
                agent=agent,
                phase=2,
                after_text=edit.get("after_text", ""),
            )
        offset += delta

    # Falls on untouched text — map back by reversing offset
    original_idx = edited_idx
    offset = 0
    for p1 in p1_sorted:
        if p1.start + offset > edited_idx:
            break
        delta = len(p1.new_text) - len(p1.original_text)
        offset += delta
    original_idx = edited_idx - offset

    if 0 <= original_idx <= len(document) - length:
        return LocatedEdit(
            start=original_idx,
            end=original_idx + length,
            original_text=document[original_idx:original_idx + length],
            new_text=edit.get("new_text", ""),
            tier=edit.get("tier", ""),
            severity=edit.get("severity", ""),
            edit_type=edit.get("edit_type", "replace"),
            comment=edit.get("comment", ""),
            kata=edit.get("kata", ""),
            agent=agent,
            phase=2,
            after_text=edit.get("after_text", ""),
        )

    return None


def _apply_edits_to_text(text: str, edits: list[LocatedEdit]) -> str:
    """Apply sorted edits to text, producing edited output."""
    result = []
    cursor = 0
    for e in edits:
        if e.start < cursor:
            continue  # skip overlapping
        result.append(text[cursor:e.start])
        result.append(e.new_text)
        cursor = e.end
    result.append(text[cursor:])
    return "".join(result)


def apply_phase1_edits(
    document: str,
    phase1_jsons: list[dict],
) -> tuple[str, list[LocatedEdit]]:
    """Apply Phase 1 edits to document text, returning edited text and located edits.

    Public API for the orchestrator to generate Phase-1-edited text for Wave 2 agents.
    Validates output is sane before returning.
    """
    all_p1: list[LocatedEdit] = []
    for pj in phase1_jsons:
        located, _ = locate_edits(document, pj)
        all_p1.extend(located)

    all_p1, _ = deduplicate(all_p1)
    all_p1, _ = resolve_conflicts(all_p1)
    p1_sorted = sorted(all_p1, key=lambda e: e.start)

    edited = _apply_edits_to_text(document, p1_sorted)

    # Validate output
    if not edited:
        print("WARNING: apply_phase1_edits produced empty output — "
              "returning original document", file=sys.stderr)
        return document, all_p1

    if len(edited) < len(document) * 0.5:
        print(f"WARNING: apply_phase1_edits output is suspiciously short "
              f"({len(edited)} chars vs {len(document)} original)",
              file=sys.stderr)

    return edited, all_p1


# ------------------------------------------------------------------
# Serialization helpers
# ------------------------------------------------------------------

def _edit_to_dict(e: LocatedEdit) -> dict:
    return {
        "tier": e.tier,
        "severity": e.severity,
        "edit_type": e.edit_type,
        "original_text": e.original_text,
        "new_text": e.new_text,
        "after_text": e.after_text,
        "comment": e.comment,
        "kata": e.kata,
        "agent": e.agent,
        "phase": e.phase,
        "position": e.start,
    }


# ------------------------------------------------------------------
# Main pipeline
# ------------------------------------------------------------------

def merge(
    document: str,
    phase1_jsons: list[dict],
    phase2_jsons: list[dict] | None = None,
) -> dict:
    """Run the full merge pipeline. Returns the output dict."""
    phase2_jsons = phase2_jsons or []

    total_input = sum(len(j.get("edits", [])) for j in phase1_jsons + phase2_jsons)

    # Track per-agent stats: {agent_name: {"input": N, "matched": N, "unmatched": N}}
    per_agent: dict[str, dict[str, int]] = {}
    all_unmatched: list[dict] = []

    # 1. Locate all Phase 1 edits (with unmatched tracking)
    all_p1: list[LocatedEdit] = []
    for pj in phase1_jsons:
        agent = pj.get("agent", "unknown")
        input_count = len(pj.get("edits", []))
        located, unmatched = locate_edits(document, pj)
        all_p1.extend(located)
        all_unmatched.extend(unmatched)
        per_agent[agent] = {
            "input": input_count,
            "matched": len(located),
            "unmatched": len(unmatched),
        }

    # 2. Deduplicate Phase 1
    all_p1, dedup_discarded = deduplicate(all_p1)
    duplicates_removed = len(dedup_discarded)

    # 3. Resolve Phase 1 conflicts
    all_p1, conflict_discarded = resolve_conflicts(all_p1)
    conflicts_resolved = len(conflict_discarded)

    # 4. Rebase Phase 2 onto original document
    rebased_p2, rebase_count = rebase_phase2(document, all_p1, phase2_jsons)

    # Track Phase 2 agent stats
    for pj in phase2_jsons:
        agent = pj.get("agent", "unknown")
        input_count = len(pj.get("edits", []))
        # Phase 2 matched count comes from rebased results
        matched = sum(1 for e in rebased_p2 if e.agent == agent)
        per_agent[agent] = {
            "input": input_count,
            "matched": matched,
            "unmatched": input_count - matched,
        }

    # 5. Merge Phase 1 survivors + rebased Phase 2, then resolve again
    combined = all_p1 + rebased_p2
    combined, dedup2 = deduplicate(combined)
    duplicates_removed += len(dedup2)
    combined, conflict2 = resolve_conflicts(combined)
    conflicts_resolved += len(conflict2)

    all_discarded = dedup_discarded + conflict_discarded + dedup2 + conflict2

    # Sort final edits by document position
    final_edits = sorted(combined, key=lambda e: e.start)

    return {
        "edits": [_edit_to_dict(e) for e in final_edits],
        "stats": {
            "total_input": total_input,
            "duplicates_removed": duplicates_removed,
            "conflicts_resolved": conflicts_resolved,
            "phase2_rebased": rebase_count,
            "final_count": len(final_edits),
            "per_agent": per_agent,
        },
        "unmatched": all_unmatched,
        "discarded": all_discarded,
    }


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

def _load_json(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(
        description="Merge prose-polish-redline edit JSONs with conflict resolution."
    )
    parser.add_argument(
        "--document", required=True, help="Path to the plain text source document."
    )
    parser.add_argument(
        "--phase1", nargs="+", required=True, help="Phase 1 edit JSON files."
    )
    parser.add_argument(
        "--phase2", nargs="*", default=[], help="Phase 2 edit JSON files (optional)."
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Output path for merged JSON."
    )
    args = parser.parse_args()

    document = Path(args.document).read_text(encoding="utf-8")
    phase1_jsons = [_load_json(p) for p in args.phase1]
    phase2_jsons = [_load_json(p) for p in args.phase2]

    result = merge(document, phase1_jsons, phase2_jsons)

    Path(args.output).write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    stats = result["stats"]
    print(f"Merge complete: {stats['final_count']} edits kept", file=sys.stderr)
    print(f"  {stats['total_input']} input -> {stats['duplicates_removed']} dupes, "
          f"{stats['conflicts_resolved']} conflicts, {stats['phase2_rebased']} rebased",
          file=sys.stderr)

    # Per-agent breakdown
    per_agent = stats.get("per_agent", {})
    if per_agent:
        parts = []
        for agent, counts in per_agent.items():
            label = f"{agent} {counts['matched']}/{counts['input']}"
            if counts["unmatched"] > 0:
                label += " \u26a0\ufe0f"
            parts.append(label)
        print(f"  Per agent: {', '.join(parts)}", file=sys.stderr)

    unmatched = result.get("unmatched", [])
    if unmatched:
        print(f"  Unmatched edits: {len(unmatched)}", file=sys.stderr)


if __name__ == "__main__":
    main()
