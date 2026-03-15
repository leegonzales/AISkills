#!/usr/bin/env python3
"""Validate a JSON file against the Sand Table Protocol.

Checks:
  1. Top-level structure: meta, agents, events
  2. meta has all required fields
  3. Every event has a 'type' field
  4. Agent IDs referenced in events exist in agents array
  5. Events are temporally ordered (for timestamp-based streams)

Usage:
    python validate_stream.py stream.json
    python validate_stream.py --lenient stream.json  # skip agent ID cross-ref
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


REQUIRED_META_FIELDS = {"domain", "id", "title", "created", "source", "run"}
VALID_SOURCES = {"simulation", "extraction"}
AGENT_REF_FIELDS = {"persona", "agent", "sender", "recipient", "from_persona", "to_persona", "owner"}


def validate(data: dict, lenient: bool = False) -> list[str]:
    """Validate a stream against the Sand Table Protocol.

    Returns a list of violation messages. Empty list = valid.
    """
    violations = []

    # 1. Top-level keys
    if not isinstance(data, dict):
        return ["Root element must be a JSON object"]

    for key in ("meta", "agents", "events"):
        if key not in data:
            violations.append(f"Missing required top-level key: '{key}'")

    if violations:
        return violations  # can't continue without structure

    # 2. meta fields
    meta = data["meta"]
    if not isinstance(meta, dict):
        violations.append("'meta' must be an object")
    else:
        for field in REQUIRED_META_FIELDS:
            if field not in meta:
                violations.append(f"Missing meta.{field}")
        if "source" in meta and meta["source"] not in VALID_SOURCES:
            violations.append(
                f"meta.source must be 'simulation' or 'extraction', "
                f"got '{meta['source']}'"
            )
        if "run" in meta and not isinstance(meta["run"], int):
            violations.append(f"meta.run must be an integer, got {type(meta['run']).__name__}")

    # 3. agents array
    agents = data["agents"]
    if not isinstance(agents, list):
        violations.append("'agents' must be an array")
        agent_ids = set()
    else:
        agent_ids = set()
        for i, agent in enumerate(agents):
            if not isinstance(agent, dict):
                violations.append(f"agents[{i}] must be an object")
                continue
            if "id" not in agent:
                violations.append(f"agents[{i}] missing 'id' field")
            else:
                agent_ids.add(agent["id"])
            if "name" not in agent:
                violations.append(f"agents[{i}] missing 'name' field")

    # 4. events array
    events = data["events"]
    if not isinstance(events, list):
        violations.append("'events' must be an array")
        return violations

    timestamps = []
    for i, ev in enumerate(events):
        if not isinstance(ev, dict):
            violations.append(f"events[{i}] must be an object")
            continue
        if "type" not in ev:
            violations.append(f"events[{i}] missing 'type' field")

        # Cross-reference agent IDs
        if not lenient:
            for field in AGENT_REF_FIELDS:
                if field in ev and ev[field] and ev[field] not in agent_ids:
                    violations.append(
                        f"events[{i}] ({ev.get('type', '?')}): "
                        f"{field}='{ev[field]}' not found in agents array"
                    )

        # Collect timestamps for ordering check
        if "timestamp" in ev:
            try:
                ts = datetime.fromisoformat(ev["timestamp"].replace("Z", "+00:00"))
                timestamps.append((i, ts))
            except (ValueError, AttributeError):
                violations.append(
                    f"events[{i}] has invalid timestamp: '{ev.get('timestamp')}'"
                )

    # 5. Temporal ordering (timestamp-based only)
    if len(timestamps) > 1:
        for j in range(1, len(timestamps)):
            idx_prev, ts_prev = timestamps[j - 1]
            idx_curr, ts_curr = timestamps[j]
            if ts_curr < ts_prev:
                violations.append(
                    f"Events out of order: events[{idx_prev}] "
                    f"({ts_prev.isoformat()}) > events[{idx_curr}] "
                    f"({ts_curr.isoformat()})"
                )

    return violations


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate a JSON file against the Sand Table Protocol."
    )
    parser.add_argument("input", type=Path, help="JSON file to validate")
    parser.add_argument(
        "--lenient", action="store_true",
        help="Skip agent ID cross-referencing"
    )
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: {args.input} not found", file=sys.stderr)
        sys.exit(1)

    try:
        data = json.loads(args.input.read_text())
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON — {e}", file=sys.stderr)
        sys.exit(1)

    violations = validate(data, lenient=args.lenient)

    if violations:
        print(f"FAIL: {len(violations)} violation(s) in {args.input}")
        for v in violations:
            print(f"  - {v}")
        sys.exit(1)
    else:
        print(f"PASS: {args.input} is protocol-compliant")
        sys.exit(0)


if __name__ == "__main__":
    main()
