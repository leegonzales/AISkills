#!/usr/bin/env python3
"""Shared Sand Table normalizer.

Loads domain-specific drift mappings and applies them to event streams.
Handles field renames, type renames, synonym resolution, and enum validation.

Generalized from:
  - substack/tools/sandtable-replay/generate_sandtable_replay.py (lines 20-107)
  - AIEnablementTraining/skills/sand-table/replay/generate_replay.py (lines 29-191)

Usage as library:
    from normalize import load_drift_mappings, normalize_events, validate_protocol

Usage as CLI:
    python normalize.py --mappings drift-mappings.json input.json -o normalized.json
"""

import argparse
import json
import sys
from pathlib import Path


def load_drift_mappings(path: Path) -> dict:
    """Load domain-specific drift mappings from a JSON file.

    Returns empty dict if file not found (allows graceful degradation).
    """
    path = Path(path)
    if not path.exists():
        print(f"Warning: {path} not found, using empty mappings", file=sys.stderr)
        return {}
    return json.loads(path.read_text())


def normalize_events(data: dict, mappings: dict, source: str = "") -> dict:
    """Apply drift mappings to normalize an event stream.

    Processing order (matches protocol-spec.md):
      1. type_renames
      2. field_renames (universal)
      3. type_conditional_field_renames
      4. synonyms
      5. valid_enums + type_conditional_valid_enums (warn only)

    Args:
        data: Event stream dict (must have "events" key)
        mappings: Drift mappings dict (from load_drift_mappings)
        source: Label for log messages

    Returns:
        The data dict with events normalized in-place.
    """
    prefix = f"[normalize {source}] " if source else "[normalize] "
    fix_count = 0
    warn_count = 0

    type_renames: dict[str, str] = mappings.get("type_renames", {})
    field_renames: dict[str, str] = mappings.get("field_renames", {})
    type_conditional: dict[str, dict[str, str]] = mappings.get(
        "type_conditional_field_renames", {}
    )
    synonyms: dict[str, dict[str, str]] = mappings.get("synonyms", {})
    valid_enums: dict[str, list[str]] = mappings.get("valid_enums", {})
    type_conditional_enums: dict[str, dict[str, list[str]]] = mappings.get(
        "type_conditional_valid_enums", {}
    )

    events = data.get("events", [])

    for ev in events:
        # 1. Fix type names
        raw_type = ev.get("type", "")
        if raw_type in type_renames:
            ev["type"] = type_renames[raw_type]
            print(
                f"{prefix}FIX: type '{raw_type}' → '{ev['type']}'",
                file=sys.stderr,
            )
            fix_count += 1

        # 2. Fix universal field names
        for wrong, right in field_renames.items():
            if wrong in ev and right not in ev:
                ev[right] = ev.pop(wrong)
                print(
                    f"{prefix}FIX: field '{wrong}' → '{right}' "
                    f"in {ev.get('type', '?')} event",
                    file=sys.stderr,
                )
                fix_count += 1

        # 3. Fix type-conditional field names
        etype = ev.get("type", "")
        if etype in type_conditional:
            for wrong, right in type_conditional[etype].items():
                if wrong in ev and right not in ev:
                    ev[right] = ev.pop(wrong)
                    print(
                        f"{prefix}FIX: field '{wrong}' → '{right}' "
                        f"in {etype} event (type-conditional)",
                        file=sys.stderr,
                    )
                    fix_count += 1

        # 4. Apply synonyms
        for field, syn_map in synonyms.items():
            if field in ev:
                val = str(ev[field]).strip().lower()
                if val in syn_map:
                    ev[field] = syn_map[val]
                    print(
                        f"{prefix}FIX: synonym '{val}' → '{syn_map[val]}' "
                        f"for {field} in {etype} event",
                        file=sys.stderr,
                    )
                    fix_count += 1

        # 5. Validate enums
        type_overrides = type_conditional_enums.get(etype, {})
        for field, valid_values in valid_enums.items():
            if field in type_overrides:
                continue  # type-specific override takes precedence
            if field in ev and ev[field] not in valid_values:
                print(
                    f"{prefix}WARN: unknown {field}='{ev[field]}' "
                    f"in {etype} event (valid: {valid_values})",
                    file=sys.stderr,
                )
                warn_count += 1

        for field, valid_values in type_overrides.items():
            if field in ev and ev[field] not in valid_values:
                print(
                    f"{prefix}WARN: unknown {field}='{ev[field]}' "
                    f"in {etype} event (valid: {valid_values})",
                    file=sys.stderr,
                )
                warn_count += 1

    # Report
    if fix_count or warn_count:
        parts = []
        if fix_count:
            parts.append(f"{fix_count} fixes")
        if warn_count:
            parts.append(f"{warn_count} enum warnings")
        print(f"{prefix}Applied {', '.join(parts)}", file=sys.stderr)
    else:
        print(f"{prefix}No normalizations needed — schema is clean", file=sys.stderr)

    return data


def validate_protocol(data: dict) -> list[str]:
    """Check protocol-level requirements. Returns list of violations."""
    violations = []

    # Check top-level keys
    if "meta" not in data:
        violations.append("Missing top-level 'meta' object")
    else:
        meta = data["meta"]
        for field in ("domain", "id", "title", "created", "source", "run"):
            if field not in meta:
                violations.append(f"Missing meta.{field}")

    if "agents" not in data:
        violations.append("Missing top-level 'agents' array")
    elif not isinstance(data["agents"], list):
        violations.append("'agents' must be an array")

    if "events" not in data:
        violations.append("Missing top-level 'events' array")
    elif not isinstance(data["events"], list):
        violations.append("'events' must be an array")

    return violations


def _wrap_legacy_format(data: dict) -> dict:
    """Wrap legacy flat-format streams into protocol structure.

    Handles Substack-style flat JSON:
        {"essay": "...", "personas": [...], "turns": N, "events": [...]}

    And AIEnablement-style:
        {"session": {...}, "personas": [...], "events": [...]}
    """
    if "meta" in data and "agents" in data:
        return data  # already protocol-compliant

    meta = {
        "domain": "unknown",
        "id": data.get("essay", data.get("session", {}).get("title", "unknown")),
        "title": data.get("essay", data.get("session", {}).get("title", "Untitled")),
        "created": data.get(
            "simulation_date",
            data.get("session", {}).get("date", ""),
        ),
        "source": "simulation",
        "run": data.get("simulation_run", 1),
    }

    # Infer domain
    if "essay" in data:
        meta["domain"] = "readership"
    elif "session" in data:
        meta["domain"] = "training"

    # Build agents array from personas
    personas = data.get("personas", [])
    agents = []
    for p in personas:
        if isinstance(p, str):
            agents.append({"id": p, "name": p})
        elif isinstance(p, dict):
            agents.append({
                "id": p.get("id", p.get("name", "")),
                "name": p.get("name", p.get("id", "")),
                "role": p.get("role", ""),
            })

    wrapped = {
        "meta": meta,
        "agents": agents,
        "events": data.get("events", []),
    }

    # Preserve summary if present
    if "session_summary" in data:
        wrapped["summary"] = data["session_summary"]

    return wrapped


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Normalize a Sand Table event stream using drift mappings."
    )
    parser.add_argument("input", type=Path, help="Input JSON file")
    parser.add_argument(
        "-m", "--mappings", type=Path, default=None,
        help="Path to drift-mappings.json (optional)"
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=None,
        help="Output path (default: stdout)"
    )
    parser.add_argument(
        "--wrap-legacy", action="store_true",
        help="Wrap legacy flat-format streams into protocol structure"
    )
    args = parser.parse_args()

    data = json.loads(args.input.read_text())

    if args.wrap_legacy:
        data = _wrap_legacy_format(data)

    mappings = load_drift_mappings(args.mappings) if args.mappings else {}
    data = normalize_events(data, mappings, source=str(args.input))

    output = json.dumps(data, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(output)
        print(f"Wrote: {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
