#!/usr/bin/env python3
"""Generate a self-contained HTML replay from flywheel scan events.

Usage:
    python generate_replay.py <output_dir>
    python generate_replay.py  # uses current directory

Reads simulation-events.json from the output directory and produces
flywheel-replay.html — a self-contained HTML file with embedded data.
"""

import json
import sys
from pathlib import Path


def load_template() -> str:
    """Load the HTML template from the same directory as this script."""
    template_path = Path(__file__).parent / "replay_template.html"
    if not template_path.exists():
        print(f"ERROR: Template not found at {template_path}", file=sys.stderr)
        sys.exit(1)
    return template_path.read_text(encoding="utf-8")


def load_drift_mappings() -> dict:
    """Load drift mappings for field correction."""
    drift_path = Path(__file__).parent.parent / "references" / "drift-mappings.json"
    if drift_path.exists():
        with open(drift_path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def apply_drift_corrections(data: dict, mappings: dict) -> tuple[dict, int]:
    """Apply field and type renames from drift-mappings.json. Returns (corrected_data, fix_count)."""
    if not mappings:
        return data, 0

    fix_count = 0
    field_renames = mappings.get("field_renames", {})
    type_renames = mappings.get("type_renames", {})
    type_conditional = mappings.get("type_conditional_field_renames", {})

    for event in data.get("events", []):
        # Fix type names
        if event.get("type") in type_renames:
            event["type"] = type_renames[event["type"]]
            fix_count += 1

        # Fix field names (global)
        for wrong, right in field_renames.items():
            if wrong in event and right not in event:
                event[right] = event.pop(wrong)
                fix_count += 1

        # Fix field names (type-conditional)
        evt_type = event.get("type", "")
        if evt_type in type_conditional:
            for wrong, right in type_conditional[evt_type].items():
                if wrong in event and right not in event:
                    event[right] = event.pop(wrong)
                    fix_count += 1

    return data, fix_count


def main():
    # Determine output directory
    if len(sys.argv) > 1:
        output_dir = Path(sys.argv[1]).expanduser()
    else:
        output_dir = Path.cwd()

    events_path = output_dir / "simulation-events.json"
    output_path = output_dir / "flywheel-replay.html"

    if not events_path.exists():
        print(f"ERROR: {events_path} not found", file=sys.stderr)
        sys.exit(1)

    # Load data
    with open(events_path, encoding="utf-8") as f:
        data = json.load(f)

    # Apply drift corrections
    mappings = load_drift_mappings()
    data, fix_count = apply_drift_corrections(data, mappings)

    # If corrections were made, write corrected JSON back
    if fix_count > 0:
        with open(events_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  Applied {fix_count} drift corrections to {events_path}")

    # Load template and inject data
    template = load_template()
    json_blob = json.dumps(data, indent=None)
    html = template.replace("__SIMULATION_DATA__", json_blob)

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    # Summary
    events = data.get("events", [])
    agents = data.get("agents", [])
    session = data.get("session", {})

    print(f"Replay written to {output_path}")
    print(f"  Session: {session.get('title', 'unknown')} ({session.get('date', '?')})")
    print(f"  {len(events)} events, {len(agents)} agents")

    # Event type breakdown
    type_counts: dict[str, int] = {}
    for e in events:
        t = e.get("type", "unknown")
        type_counts[t] = type_counts.get(t, 0) + 1
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"    {t}: {c}")


if __name__ == "__main__":
    main()
