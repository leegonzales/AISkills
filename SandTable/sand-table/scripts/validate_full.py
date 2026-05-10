#!/usr/bin/env python3
"""Full Sand Table validation — orchestrates structural + drift + clamping + narrative.

Combines:
  - validate_stream.py (structural envelope + agent-ref + timestamp ordering)
  - normalize.py       (drift mapping correction)
  - narrative_check.py (impossible-narrative scan, advisory)
  - score clamping     (clamps numeric scores to mapping-defined range)
  - derived fields     (stamps meta.event_count, meta.agent_count if absent)

Exit codes:
  0 — pass (narrative warnings never fail the build)
  1 — structural violations present

Usage:
    python validate_full.py stream.json
    python validate_full.py stream.json --mappings drift.json
    python validate_full.py stream.json --mappings drift.json --no-narrative
    python validate_full.py stream.json --mappings drift.json --write-normalized out.json
"""

import argparse
import json
import sys
from pathlib import Path

# Make sibling modules importable regardless of cwd.
sys.path.insert(0, str(Path(__file__).parent))

from validate_stream import validate as structural_validate  # noqa: E402
from normalize import load_drift_mappings, normalize_events  # noqa: E402
from narrative_check import scan as narrative_scan, format_report as narrative_report  # noqa: E402


def clamp_scores(data: dict, score_range: tuple[float, float]) -> list[str]:
    """Clamp numeric scores to [min, max]. Return list of clamp-action strings."""
    lo, hi = score_range
    actions: list[str] = []
    for idx, ev in enumerate(data.get("events", [])):
        scores = ev.get("scores")
        if not isinstance(scores, dict):
            continue
        for k, v in list(scores.items()):
            if not isinstance(v, (int, float)):
                continue
            if v < lo:
                actions.append(f"events[{idx}].scores.{k}: {v} -> {lo}")
                scores[k] = lo
            elif v > hi:
                actions.append(f"events[{idx}].scores.{k}: {v} -> {hi}")
                scores[k] = hi
    return actions


def stamp_derived(data: dict) -> list[str]:
    """Add meta.event_count and meta.agent_count if absent. Return stamp log."""
    log: list[str] = []
    meta = data.setdefault("meta", {})
    if "event_count" not in meta:
        meta["event_count"] = len(data.get("events", []))
        log.append(f"meta.event_count = {meta['event_count']}")
    if "agent_count" not in meta:
        meta["agent_count"] = len(data.get("agents", []))
        log.append(f"meta.agent_count = {meta['agent_count']}")
    return log


def _print_section(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


def main() -> int:
    parser = argparse.ArgumentParser(description="Full Sand Table validation pipeline.")
    parser.add_argument("input", type=Path)
    parser.add_argument("-m", "--mappings", type=Path, default=None, help="Path to drift-mappings.json")
    parser.add_argument("--no-narrative", action="store_true", help="Skip impossible-narrative scan")
    parser.add_argument("--write-normalized", type=Path, default=None, help="Write the normalized stream to this path")
    parser.add_argument("--score-range", default="0,5", help="Score clamp range as 'min,max' (default 0,5; overridden by mappings.score_range)")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: {args.input} not found", file=sys.stderr)
        return 2

    data = json.loads(args.input.read_text())

    # 1. Structural validation (delegates to validate_stream).
    structural_violations = structural_validate(data)
    _print_section("Structural")
    if structural_violations:
        print(f"FAIL: {len(structural_violations)} violation(s)")
        for v in structural_violations:
            print(f"  - {v}")
    else:
        print("PASS: envelope, meta, agents, events, references, ordering all valid")

    # 2. Drift correction.
    _print_section("Drift")
    mappings: dict = {}
    fix_count = 0
    if args.mappings:
        mappings = load_drift_mappings(args.mappings)
        if mappings:
            # normalize_events prints to stderr; capture nothing — the user sees it.
            before_events = json.dumps(data.get("events", []))
            normalize_events(data, mappings, source=str(args.input))
            after_events = json.dumps(data.get("events", []))
            fix_count = 0 if before_events == after_events else 1  # rough indicator; actual count printed by normalize
        else:
            print(f"SKIPPED: mappings file empty or unreadable: {args.mappings}")
    else:
        print("SKIPPED: no --mappings provided")

    # 3. Score clamping.
    _print_section("Score Clamping")
    if "score_range" in mappings:
        sr_raw = mappings["score_range"]
        if isinstance(sr_raw, list) and len(sr_raw) == 2:
            score_range = (float(sr_raw[0]), float(sr_raw[1]))
        else:
            print(f"WARN: invalid mappings.score_range, using default")
            score_range = tuple(float(x) for x in args.score_range.split(",", 1))
    else:
        score_range = tuple(float(x) for x in args.score_range.split(",", 1))
    clamps = clamp_scores(data, score_range)
    print(f"Range: [{score_range[0]}, {score_range[1]}]")
    if clamps:
        print(f"Clamped {len(clamps)} value(s):")
        for c in clamps[:10]:
            print(f"  - {c}")
        if len(clamps) > 10:
            print(f"  ... and {len(clamps) - 10} more")
    else:
        print("No values out of range")

    # 4. Derived field stamping.
    _print_section("Derived Fields")
    stamps = stamp_derived(data)
    if stamps:
        for s in stamps:
            print(f"  + {s}")
    else:
        print("No fields to stamp (already present)")

    # 5. Narrative integrity (advisory).
    if not args.no_narrative:
        _print_section("Narrative")
        report = narrative_scan(data)
        print(narrative_report(report, max_examples=3))
    else:
        _print_section("Narrative")
        print("SKIPPED: --no-narrative")

    # 6. Optional write.
    if args.write_normalized:
        args.write_normalized.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        print()
        print(f"Wrote normalized stream: {args.write_normalized}")

    # 7. Final result.
    print()
    print("=" * 60)
    if structural_violations:
        print(f"VALIDATION FAILED — {len(structural_violations)} structural violation(s)")
        return 1
    print("VALIDATION PASSED — narrative warnings (if any) are advisory only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
