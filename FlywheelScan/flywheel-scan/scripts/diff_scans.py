#!/usr/bin/env python3
"""Compare two flywheel scan outputs to show drift, score movements, and thread changes.

Usage:
    python diff_scans.py <previous_dir> <current_dir>

Produces scan-diff-report.md in the current directory.
"""

import json
import sys
from pathlib import Path


def load_events(scan_dir: Path) -> dict:
    """Load simulation-events.json from a scan directory."""
    path = scan_dir / "simulation-events.json"
    if not path.exists():
        print(f"ERROR: {path} not found", file=sys.stderr)
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def extract_triages(events: list[dict]) -> dict[str, dict]:
    """Extract repo_triage events keyed by repo."""
    return {
        e["repo"]: e
        for e in events
        if e.get("type") == "repo_triage"
    }


def extract_scores(events: list[dict]) -> dict[str, dict]:
    """Extract priority_score events keyed by bead_title."""
    return {
        e["bead_title"]: e
        for e in events
        if e.get("type") == "priority_score"
    }


def extract_threads(events: list[dict]) -> dict[str, dict]:
    """Extract thread_proposal events keyed by thread_id."""
    return {
        e["thread_id"]: e
        for e in events
        if e.get("type") == "thread_proposal"
    }


def diff_classifications(prev_triages: dict, curr_triages: dict) -> list[str]:
    """Find repos that changed classification."""
    lines = []
    all_repos = sorted(set(prev_triages) | set(curr_triages))

    for repo in all_repos:
        prev = prev_triages.get(repo)
        curr = curr_triages.get(repo)

        if prev and not curr:
            lines.append(f"| {repo} | {prev['classification']} | **removed** | Repo no longer scanned |")
        elif curr and not prev:
            lines.append(f"| {repo} | **new** | {curr['classification']} | New repo added |")
        elif prev and curr and prev["classification"] != curr["classification"]:
            lines.append(
                f"| {repo} | {prev['classification']} | {curr['classification']} | {curr.get('rationale', '')[:60]} |"
            )

    return lines


def diff_scores(prev_scores: dict, curr_scores: dict) -> list[str]:
    """Find work items with score changes."""
    lines = []
    all_items = sorted(set(prev_scores) | set(curr_scores))

    for title in all_items:
        prev = prev_scores.get(title)
        curr = curr_scores.get(title)

        if prev and not curr:
            lines.append(f"| {title} | {prev.get('total', '?')} | **dropped** | {prev.get('repo', '')} |")
        elif curr and not prev:
            lines.append(f"| {title} | **new** | {curr.get('total', '?')} | {curr.get('repo', '')} |")
        elif prev and curr:
            prev_total = prev.get("total", 0)
            curr_total = curr.get("total", 0)
            delta = curr_total - prev_total
            if delta != 0:
                arrow = "+" if delta > 0 else ""
                lines.append(f"| {title} | {prev_total} | {curr_total} ({arrow}{delta}) | {curr.get('repo', '')} |")

    return lines


def diff_threads(prev_threads: dict, curr_threads: dict) -> list[str]:
    """Find thread changes."""
    lines = []

    for tid, curr in curr_threads.items():
        if tid not in prev_threads:
            rec = next((o["label"] for o in curr.get("options", []) if o.get("recommendation")), "none")
            lines.append(f"| {curr.get('thread_title', tid)} | **new** | {rec} |")

    for tid, prev in prev_threads.items():
        if tid not in curr_threads:
            lines.append(f"| {prev.get('thread_title', tid)} | **resolved/removed** | — |")

    for tid in set(prev_threads) & set(curr_threads):
        prev_rec = next(
            (o["label"] for o in prev_threads[tid].get("options", []) if o.get("recommendation")), "none"
        )
        curr_rec = next(
            (o["label"] for o in curr_threads[tid].get("options", []) if o.get("recommendation")), "none"
        )
        if prev_rec != curr_rec:
            title = curr_threads[tid].get("thread_title", tid)
            lines.append(f"| {title} | {prev_rec} | {curr_rec} |")

    return lines


def main():
    if len(sys.argv) < 3:
        print("Usage: python diff_scans.py <previous_dir> <current_dir>", file=sys.stderr)
        sys.exit(1)

    prev_dir = Path(sys.argv[1]).expanduser()
    curr_dir = Path(sys.argv[2]).expanduser()

    prev_data = load_events(prev_dir)
    curr_data = load_events(curr_dir)

    prev_events = prev_data.get("events", [])
    curr_events = curr_data.get("events", [])

    prev_date = prev_data.get("session", {}).get("date", "unknown")
    curr_date = curr_data.get("session", {}).get("date", "unknown")

    # Extract structured data
    prev_triages = extract_triages(prev_events)
    curr_triages = extract_triages(curr_events)
    prev_scores = extract_scores(prev_events)
    curr_scores = extract_scores(curr_events)
    prev_threads = extract_threads(prev_events)
    curr_threads = extract_threads(curr_events)

    # Build report
    report = [f"# Scan Diff Report: {prev_date} → {curr_date}\n"]

    # Summary stats
    report.append("## Summary\n")
    report.append(f"| Metric | Previous ({prev_date}) | Current ({curr_date}) |")
    report.append("|--------|-----------|---------|")
    report.append(f"| Repos scanned | {len(prev_triages)} | {len(curr_triages)} |")
    report.append(f"| Total events | {len(prev_events)} | {len(curr_events)} |")
    report.append(f"| Items scored | {len(prev_scores)} | {len(curr_scores)} |")
    report.append(f"| Open threads | {len(prev_threads)} | {len(curr_threads)} |")
    report.append("")

    # Classification drift
    class_diffs = diff_classifications(prev_triages, curr_triages)
    report.append("## Classification Changes\n")
    if class_diffs:
        report.append("| Repo | Previous | Current | Rationale |")
        report.append("|------|----------|---------|-----------|")
        report.extend(class_diffs)
    else:
        report.append("No classification changes.")
    report.append("")

    # Score movements
    score_diffs = diff_scores(prev_scores, curr_scores)
    report.append("## Score Movements\n")
    if score_diffs:
        report.append("| Item | Previous | Current | Repo |")
        report.append("|------|----------|---------|------|")
        report.extend(score_diffs)
    else:
        report.append("No score changes.")
    report.append("")

    # Thread changes
    thread_diffs = diff_threads(prev_threads, curr_threads)
    report.append("## Thread Changes\n")
    if thread_diffs:
        report.append("| Thread | Previous Rec | Current Rec |")
        report.append("|--------|-------------|-------------|")
        report.extend(thread_diffs)
    else:
        report.append("No thread changes.")
    report.append("")

    # Classification distribution comparison
    report.append("## Classification Distribution\n")
    for label in ["active-invest", "maintain", "archive"]:
        prev_count = sum(1 for t in prev_triages.values() if t.get("classification") == label)
        curr_count = sum(1 for t in curr_triages.values() if t.get("classification") == label)
        delta = curr_count - prev_count
        arrow = f" (+{delta})" if delta > 0 else f" ({delta})" if delta < 0 else ""
        report.append(f"- **{label}**: {prev_count} → {curr_count}{arrow}")
    report.append("")

    # Write report
    output_path = curr_dir / "scan-diff-report.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report) + "\n")

    print(f"Diff report written to {output_path}")
    print(f"  {len(class_diffs)} classification changes")
    print(f"  {len(score_diffs)} score movements")
    print(f"  {len(thread_diffs)} thread changes")


if __name__ == "__main__":
    main()
