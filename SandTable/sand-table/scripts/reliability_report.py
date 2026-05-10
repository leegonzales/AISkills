#!/usr/bin/env python3
"""Reliability report for Sand Table simulations.

Produces a four-section text report matching references/reliability.md:
  1. Narrative Integrity   (delegates to narrative_check.py)
  2. Data Completeness     (NR/timeout count, affected agents/units)
  3. Context Chain         (multi-session validation, only if --context-dir/--prior given)
  4. Recommendations       (deterministic rules: ACCEPT / REVIEW / RE-RUN / HALT)

Always exits 0 — this is a report, not a gate. Callers wanting a hard
gate should grep for "RECOMMENDATION: HALT" in the output.

Usage:
    python reliability_report.py stream.json
    python reliability_report.py stream.json --context-dir output/training-s2
    python reliability_report.py stream.json --context-dir output/ --prior s1-run5,s2-run6
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from narrative_check import scan as narrative_scan, format_report as narrative_report  # noqa: E402


# Required keys in an exit-context JSON file (per multi-session.md generic schema).
EXIT_CONTEXT_HARD_REQUIRED = {"agent_id", "scores"}
EXIT_CONTEXT_SOFT_REQUIRED = {"growth_narrative", "headline_quote", "behavioral_markers"}


def _section(title: str) -> str:
    bar = "=" * len(title)
    return f"\n{title}\n{bar}"


def data_completeness(data: dict) -> dict:
    """Count NR / timeout / null-response events. Group by agent and unit."""
    events = data.get("events", [])
    nr_events: list[tuple[int, str, str]] = []  # (idx, agent, unit)
    for idx, ev in enumerate(events):
        # Only flag explicit non-response markers — never infer from missing fields,
        # since different event types use different content field names (text, spoken, etc.).
        is_nr = (
            ev.get("type") in ("timeout", "non_responsive", "nr")
            or ev.get("status") in ("NR", "non_responsive", "timeout")
            or ev.get("nr") is True
        )
        if is_nr:
            agent = ev.get("agent") or ev.get("persona") or "?"
            unit = ev.get("unit") or ev.get("module") or ev.get("section") or "?"
            nr_events.append((idx, str(agent), str(unit)))

    by_agent: dict[str, int] = {}
    by_unit: dict[str, int] = {}
    for _, agent, unit in nr_events:
        by_agent[agent] = by_agent.get(agent, 0) + 1
        by_unit[unit] = by_unit.get(unit, 0) + 1

    return {
        "total_events": len(events),
        "nr_count": len(nr_events),
        "by_agent": by_agent,
        "by_unit": by_unit,
        "nr_events": nr_events,
    }


def format_completeness(report: dict) -> str:
    lines = ["", "Data Completeness", "-----------------"]
    pct = (report["nr_count"] / report["total_events"] * 100) if report["total_events"] else 0
    lines.append(f"Non-responsive events: {report['nr_count']} / {report['total_events']} ({pct:.1f}%)")
    if report["by_agent"]:
        lines.append("Affected agents:")
        for agent, count in sorted(report["by_agent"].items(), key=lambda x: -x[1]):
            lines.append(f"  - {agent}: {count}")
    if report["by_unit"]:
        lines.append("Affected units:")
        for unit, count in sorted(report["by_unit"].items(), key=lambda x: -x[1]):
            lines.append(f"  - {unit}: {count}")
    if report["nr_count"] == 0:
        lines.append("All agents responsive across all units.")
    return "\n".join(lines)


def validate_exit_context(path: Path) -> tuple[bool, list[str]]:
    """Validate one exit-context JSON file. Returns (hard_pass, soft_warnings)."""
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        return False, [f"could not load: {e}"]

    # Look for hard-required either at top level or under meta.
    meta = data.get("meta", {}) if isinstance(data.get("meta"), dict) else {}
    has = lambda k: k in data or k in meta
    missing_hard = [k for k in EXIT_CONTEXT_HARD_REQUIRED if not has(k)]
    if missing_hard:
        return False, [f"missing required: {', '.join(missing_hard)}"]
    missing_soft = [k for k in EXIT_CONTEXT_SOFT_REQUIRED if not has(k)]
    return True, [f"missing recommended: {k}" for k in missing_soft]


def context_chain(data: dict, context_dir: Path | None, prior_ids: list[str]) -> dict:
    """Validate exit-context files for prior runs against current roster."""
    result: dict = {"checked": False, "errors": [], "warnings": [], "valid_runs": []}
    if not context_dir or not prior_ids:
        return result
    result["checked"] = True

    roster_ids = {a.get("id") for a in data.get("agents", []) if a.get("id")}

    for run_id in prior_ids:
        run_dir = context_dir / run_id / "context"
        if not run_dir.is_dir():
            # Try alt layout: context_dir / context / per-agent files keyed by run_id.
            run_dir = context_dir / "context"
            if not run_dir.is_dir():
                result["errors"].append(f"{run_id}: context directory not found at {context_dir / run_id / 'context'}")
                continue

        # Load all *-exit-context.json files.
        ctx_files = sorted(run_dir.glob("*-exit-context.json"))
        if not ctx_files:
            result["errors"].append(f"{run_id}: no *-exit-context.json files in {run_dir}")
            continue

        ctx_agent_ids: set[str] = set()
        for f in ctx_files:
            ok, warns = validate_exit_context(f)
            if not ok:
                result["errors"].append(f"{run_id}/{f.name}: {warns[0]}")
                continue
            for w in warns:
                result["warnings"].append(f"{run_id}/{f.name}: {w}")
            # Extract agent_id (top-level or under meta).
            try:
                d = json.loads(f.read_text())
                aid = d.get("agent_id") or d.get("meta", {}).get("agent_id") or f.stem.replace("-exit-context", "")
                ctx_agent_ids.add(aid)
            except Exception:
                pass

        # Cohort match.
        missing_in_current = ctx_agent_ids - roster_ids
        missing_in_context = roster_ids - ctx_agent_ids
        if missing_in_current:
            result["errors"].append(f"{run_id}: agents in context but not in current roster: {sorted(missing_in_current)}")
        if missing_in_context:
            result["warnings"].append(f"{run_id}: current roster agents missing exit context: {sorted(missing_in_context)}")
        if not missing_in_current and not missing_in_context:
            result["valid_runs"].append(run_id)

    return result


def format_context_chain(report: dict) -> str:
    if not report["checked"]:
        return "\nContext Chain\n-------------\nSKIPPED: no --context-dir / --prior provided"
    lines = ["", "Context Chain", "-------------"]
    if report["errors"]:
        lines.append(f"ERRORS ({len(report['errors'])}):")
        for e in report["errors"]:
            lines.append(f"  ✗ {e}")
    if report["warnings"]:
        lines.append(f"Warnings ({len(report['warnings'])}):")
        for w in report["warnings"]:
            lines.append(f"  ! {w}")
    if report["valid_runs"]:
        lines.append(f"Valid runs: {', '.join(report['valid_runs'])}")
    if not report["errors"] and not report["warnings"]:
        lines.append("VALID: all prior runs validated, cohort matches")
    return "\n".join(lines)


def recommend(narrative: dict, completeness: dict, chain: dict) -> str:
    """Deterministic recommendation rules."""
    nr_pct = (completeness["nr_count"] / completeness["total_events"] * 100) if completeness["total_events"] else 0
    if chain["checked"] and chain["errors"]:
        return "HALT — context chain has hard errors; fix before re-running"
    if narrative["bucket"] == "INTEGRITY CONCERN":
        return "RE-RUN — likely single-agent execution; verify multi-agent independence"
    if nr_pct > 30:
        return "RE-RUN — over 30% non-responsive events; investigate agent connectivity"
    if narrative["bucket"] == "WARNING" or completeness["nr_count"] > 0:
        affected = sorted(completeness["by_agent"].keys())[:3]
        return f"REVIEW — minor leakage or missing data; check agents: {', '.join(affected) if affected else '(narrative flags only)'}"
    return "ACCEPT — clean narrative integrity, full data completeness"


def main() -> int:
    parser = argparse.ArgumentParser(description="Reliability report for a Sand Table event stream.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--context-dir", type=Path, default=None, help="Directory containing prior-run context dirs")
    parser.add_argument("--prior", default=None, help="Comma-separated prior run IDs (e.g., 's1-run5,s2-run6')")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: {args.input} not found", file=sys.stderr)
        return 2

    data = json.loads(args.input.read_text())

    # 1. Narrative.
    narrative = narrative_scan(data)
    print(narrative_report(narrative, max_examples=5))

    # 2. Completeness.
    completeness = data_completeness(data)
    print(format_completeness(completeness))

    # 3. Context chain.
    prior_ids = [s.strip() for s in (args.prior or "").split(",") if s.strip()]
    chain = context_chain(data, args.context_dir, prior_ids)
    print(format_context_chain(chain))

    # 4. Recommendation.
    print(_section("Recommendation"))
    print(f"RECOMMENDATION: {recommend(narrative, completeness, chain)}")

    return 0  # always advisory


if __name__ == "__main__":
    sys.exit(main())
