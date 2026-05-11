#!/usr/bin/env python3
"""Scaffold a new Sand Table domain into a target project.

Generates:
  - .claude/skills/sand-table-{domain}.md     project-local skill
  - drift-mappings.json                       seeded with cross-domain baseline
  - replay/generate_replay.py                 minimal stub with {{SIMULATION_DATA}}
  - replay/replay_template.html               minimal HTML with placeholder
  - manifest.json                             discovery manifest
  - domain-invariant.md                       filled-in invariant (from template)
  - .sand-table/registry-row.md               markdown row for implementations.md

Modes:
  Interactive (TTY): prompts for missing fields.
  Non-interactive: requires all fields via flags; fails fast on missing.

Idempotent: refuses to overwrite existing files unless --force.

Usage:
    python scaffold.py --target /path/to/project \\
        --domain my-sim --name "My Simulation" \\
        --description "What it simulates" \\
        --source-type simulation --temporal-model turn \\
        --tier 1 --agent-count 6 --event-types reader,section_scores \\
        --non-interactive

    python scaffold.py --target . --dry-run    # preview without writing
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import NamedTuple


SCAFFOLD_VERSION = "1.0"

# Cross-domain drift baseline (from references/patterns.md Pattern 3.2).
DEFAULT_DRIFT_FIELD_RENAMES = {
    "module_id": "module",
    "section_id": "section",
    "unit_id": "unit",
    "persona_id": "persona",
    "agent_id": "agent",
    "planned_duration": "duration_min",
    "duration_minutes": "duration_min",
    "from_module": "from",
    "to_module": "to",
    "internal": "internal_monologue",
    "thoughts": "internal_monologue",
    "floor_deployment": "floor",
    "ceiling_deployment": "ceiling",
    "intervention": "text",
    "summary": "text",
    "response": "text",
    "timestamp_min": "time_offset",
    "time_min": "time_offset",
    "score": "scores",
    "rating": "scores",
    "participant": "persona",
    "respondent": "persona",
}

DEFAULT_EVENT_TYPES_BY_TEMPORAL = {
    "turn": ["reader", "section_scores"],
    "bracket": ["module_start", "module_end", "persona", "module_scores"],
    "timestamp": ["agent_spawn", "command", "file_change", "message"],
}

VALID_SOURCE_TYPES = {"simulation", "extraction"}
VALID_TEMPORAL_MODELS = {"turn", "bracket", "timestamp"}
VALID_TIERS = {1, 2, 3}
DOMAIN_SLUG_RE = re.compile(r"^[a-z][a-z0-9-]*$")


# ---------------------------------------------------------------------------
# Spec + planning
# ---------------------------------------------------------------------------

class PlannedWrite(NamedTuple):
    abs_path: Path
    content: str
    kind: str   # "skill" | "drift" | "replay-py" | "replay-html" | "manifest" | "invariant" | "registry"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Scaffold a new Sand Table domain into a target project.")
    p.add_argument("--target", type=Path, default=Path.cwd(), help="Target project directory (default: cwd)")
    p.add_argument("--domain", help="Domain slug ([a-z0-9-]+); default = basename of target")
    p.add_argument("--name", help="Human-readable domain name")
    p.add_argument("--description", help="One-sentence description")
    p.add_argument("--source-type", choices=sorted(VALID_SOURCE_TYPES), help="simulation | extraction")
    p.add_argument("--temporal-model", choices=sorted(VALID_TEMPORAL_MODELS), help="turn | bracket | timestamp")
    p.add_argument("--tier", type=int, choices=sorted(VALID_TIERS), help="Execution tier 1-3")
    p.add_argument("--agent-count", type=int, help="Fixed roster size (0 = dynamic for extraction)")
    p.add_argument("--event-types", help="Comma-separated event type names")
    p.add_argument("--skill-name", help="Skill filename (default: sand-table-{domain}.md)")
    p.add_argument("--no-manifest", action="store_true", help="Skip manifest.json")
    p.add_argument("--no-replay-stub", action="store_true", help="Skip replay/ files")
    p.add_argument("--no-invariant", action="store_true", help="Skip domain-invariant.md")
    p.add_argument("--register", action="store_true", help="Write .sand-table/registry-row.md (always shown to stdout too)")
    p.add_argument("--force", action="store_true", help="Overwrite existing files")
    p.add_argument("--dry-run", action="store_true", help="Print planned writes; do not touch disk")
    p.add_argument("--non-interactive", action="store_true", help="Fail fast on missing fields instead of prompting")
    return p.parse_args()


def _ask(prompt: str, default: str | None = None, validator=None, max_tries: int = 3) -> str:
    suffix = f" [{default}]" if default else ""
    for _ in range(max_tries):
        v = input(f"{prompt}{suffix}: ").strip()
        if not v and default is not None:
            v = default
        if validator and not validator(v):
            print(f"  Invalid value: {v!r}", file=sys.stderr)
            continue
        return v
    print(f"Too many invalid attempts for: {prompt}", file=sys.stderr)
    sys.exit(2)


def prompt_missing(args: argparse.Namespace) -> dict:
    spec: dict = {}
    is_tty = sys.stdin.isatty()
    if not is_tty and not args.non_interactive:
        # Auto-promote: missing fields will fail validate_spec, not hang on input().
        pass

    spec["target"] = args.target.resolve()

    default_domain = args.domain or args.target.resolve().name
    spec["domain_id"] = args.domain or (
        _ask("Domain slug (lowercase, hyphens)", default_domain, lambda v: bool(DOMAIN_SLUG_RE.match(v))) if is_tty
        else default_domain
    )
    spec["name"] = args.name or (_ask("Human-readable name", spec["domain_id"].replace("-", " ").title()) if is_tty else "")
    spec["description"] = args.description or (_ask("One-sentence description", "TODO: describe the simulation") if is_tty else "")
    spec["source_type"] = args.source_type or (
        _ask("Source type", "simulation", lambda v: v in VALID_SOURCE_TYPES) if is_tty else "simulation"
    )
    default_tm = "timestamp" if spec["source_type"] == "extraction" else "turn"
    spec["temporal_model"] = args.temporal_model or (
        _ask("Temporal model (turn|bracket|timestamp)", default_tm, lambda v: v in VALID_TEMPORAL_MODELS) if is_tty else default_tm
    )
    if spec["source_type"] == "simulation":
        spec["tier"] = args.tier if args.tier is not None else (
            int(_ask("Execution tier (1|2|3)", "1", lambda v: v.isdigit() and int(v) in VALID_TIERS)) if is_tty else 1
        )
    else:
        spec["tier"] = args.tier if args.tier is not None else 1
    spec["agent_count"] = args.agent_count if args.agent_count is not None else (
        int(_ask("Agent count (0 = dynamic)", "6", lambda v: v.isdigit())) if is_tty else 0
    )
    default_events = ",".join(DEFAULT_EVENT_TYPES_BY_TEMPORAL.get(spec["temporal_model"], []))
    raw_events = args.event_types or (_ask("Event types (comma-separated)", default_events) if is_tty else default_events)
    spec["event_types"] = [t.strip() for t in raw_events.split(",") if t.strip()]
    spec["skill_filename"] = args.skill_name or f"sand-table-{spec['domain_id']}.md"
    spec["want_manifest"] = not args.no_manifest
    spec["want_replay"] = not args.no_replay_stub and spec["source_type"] == "simulation"
    spec["want_invariant"] = not args.no_invariant
    spec["want_register"] = args.register
    spec["meta_skill_root"] = Path(__file__).resolve().parent.parent
    return spec


def validate_spec(spec: dict) -> list[str]:
    errors: list[str] = []
    if not spec.get("domain_id") or not DOMAIN_SLUG_RE.match(spec["domain_id"]):
        errors.append(f"domain_id missing or invalid (need lowercase + hyphens): {spec.get('domain_id')!r}")
    if not spec.get("name"):
        errors.append("name is required")
    if not spec.get("description"):
        errors.append("description is required")
    if spec.get("source_type") not in VALID_SOURCE_TYPES:
        errors.append(f"source_type invalid: {spec.get('source_type')!r}")
    if spec.get("temporal_model") not in VALID_TEMPORAL_MODELS:
        errors.append(f"temporal_model invalid: {spec.get('temporal_model')!r}")
    if spec.get("tier") not in VALID_TIERS:
        errors.append(f"tier invalid: {spec.get('tier')!r}")
    if not spec.get("event_types"):
        errors.append("event_types empty (provide at least one)")
    if not isinstance(spec.get("target"), Path) or not spec["target"].is_dir():
        errors.append(f"target directory does not exist: {spec.get('target')}")
    elif not os.access(spec["target"], os.W_OK):
        errors.append(f"target directory not writable: {spec['target']}")
    return errors


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------

def render_skill_md(spec: dict) -> str:
    event_lines = "\n".join(f"  - {t}" for t in spec["event_types"])
    return f"""---
name: sand-table-{spec['domain_id']}
description: Sand Table simulation for {spec['name']}. {spec['description']}
---

# Sand Table — {spec['name']}

{spec['description']}

## Domain

- **domain_id**: `{spec['domain_id']}`
- **source_type**: `{spec['source_type']}`
- **temporal_model**: `{spec['temporal_model']}`
- **execution_tier**: {spec['tier']}
- **agent_count**: {spec['agent_count']}

## Event Types

{event_lines}

## Workflow

1. Generate or extract events into a JSON file matching the Sand Table Protocol envelope.
2. Validate with the meta skill's `validate_full.py`:
   ```
   python <meta-skill>/scripts/validate_full.py events.json --mappings drift-mappings.json
   ```
3. Render with `replay/generate_replay.py`.

See `domain-invariant.md` for the full domain spec, and the meta skill at
`SandTable/sand-table/SKILL.md` for protocol details.
"""


def render_drift_mappings(spec: dict) -> dict:
    return {
        "_comment": f"Drift mappings for {spec['domain_id']}. Add domain-specific entries as initial runs surface them.",
        "field_renames": DEFAULT_DRIFT_FIELD_RENAMES,
        "type_renames": {},
        "synonyms": {},
        "valid_enums": {},
        "type_conditional_field_renames": {t: {} for t in spec["event_types"]},
        "score_range": [0, 5],
    }


def render_manifest(spec: dict) -> dict:
    return {
        "sand_table_protocol": "1.1",
        "domain": spec["domain_id"],
        "source_type": spec["source_type"],
        "temporal_model": spec["temporal_model"],
        "execution_tier": spec["tier"],
        "event_types": spec["event_types"],
        "agent_count": spec["agent_count"],
        "multi_run": False,
        "multi_session": False,
        "paths": {
            "skill": f".claude/skills/{spec['skill_filename']}",
            "replay_generator": "replay/generate_replay.py" if spec["want_replay"] else "",
            "replay_template": "replay/replay_template.html" if spec["want_replay"] else "",
            "drift_mappings": "drift-mappings.json",
        },
    }


def render_replay_py(spec: dict) -> str:
    return f'''#!/usr/bin/env python3
"""Replay generator stub for {spec['domain_id']}.

Reads validated event JSON files and injects them into the HTML template
at the {{{{SIMULATION_DATA}}}} placeholder.
"""

import argparse
import json
from pathlib import Path

PLACEHOLDER = "{{{{SIMULATION_DATA}}}}"


def main() -> None:
    p = argparse.ArgumentParser(description="Generate {spec['domain_id']} replay HTML.")
    p.add_argument("inputs", nargs="+", help="One or more validated event JSON files")
    p.add_argument("-t", "--template", default=str(Path(__file__).parent / "replay_template.html"))
    p.add_argument("-o", "--output", required=True)
    args = p.parse_args()

    sims = {{}}
    for path in args.inputs:
        data = json.loads(Path(path).read_text())
        meta = data.get("meta", {{}})
        key = f"{{meta.get('id', Path(path).stem)}}_run{{meta.get('run', 1)}}"
        sims[key] = data

    template = Path(args.template).read_text()
    payload = "const SIMULATIONS = " + json.dumps(sims, indent=2, ensure_ascii=False) + ";"
    html = template.replace(PLACEHOLDER, payload)
    Path(args.output).write_text(html)
    print(f"Wrote: {{args.output}} ({{len(sims)}} run(s))")


if __name__ == "__main__":
    main()
'''


def render_replay_html(spec: dict) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{spec['name']} — Sand Table Replay</title>
<style>
  body {{ font: 14px/1.5 -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 2rem; }}
  pre {{ background: #f4f4f4; padding: 1rem; border-radius: 4px; overflow: auto; }}
</style>
</head>
<body>
<h1>{spec['name']}</h1>
<p>Sand Table replay. Replace this stub with your domain-specific renderer.</p>
<pre id="data"></pre>
<script>
{{{{SIMULATION_DATA}}}}
document.getElementById('data').textContent = JSON.stringify(SIMULATIONS, null, 2);
</script>
</body>
</html>
"""


def render_invariant(spec: dict, template_path: Path) -> str:
    """Read the meta-skill's invariant template and lightly fill the Identity block."""
    if not template_path.exists():
        return f"# Domain Invariant — {spec['name']}\n\nTemplate not found at {template_path}; fill in manually.\n"
    body = template_path.read_text()
    # Replace the Identity yaml block placeholders in-place.
    body = re.sub(
        r"domain_id: your-domain-slug",
        f"domain_id: {spec['domain_id']}",
        body,
    )
    body = re.sub(
        r'domain_name: "Human-Readable Domain Name"',
        f'domain_name: "{spec["name"]}"',
        body,
    )
    body = re.sub(
        r'description: "One sentence: what is being simulated or extracted\?"',
        f'description: "{spec["description"]}"',
        body,
    )
    body = re.sub(
        r"source_type: simulation \| extraction",
        f"source_type: {spec['source_type']}",
        body,
    )
    body = re.sub(
        r"temporal_model: turn \| bracket \| timestamp",
        f"temporal_model: {spec['temporal_model']}",
        body,
    )
    body = re.sub(
        r"execution_tier: 1 \| 2 \| 3.*",
        f"execution_tier: {spec['tier']}",
        body,
    )
    return body


def render_registry_row(spec: dict) -> str:
    return f"""## {spec['name']}

{spec['description']}

| Attribute | Value |
|-----------|-------|
| **Project** | `{spec['target']}` |
| **Skill** | `.claude/skills/{spec['skill_filename']}` |
| **Replay Generator** | `replay/generate_replay.py` |
| **Replay Template** | `replay/replay_template.html` |
| **Source Type** | {spec['source_type'].title()} |
| **Temporal Model** | {spec['temporal_model'].title()}-based |
| **Execution Tier** | Tier {spec['tier']} |
| **Event Types** | {', '.join(f'`{t}`' for t in spec['event_types'])} |
| **Agent Count** | {spec['agent_count']} |
| **Drift Mappings** | `drift-mappings.json` |
"""


# ---------------------------------------------------------------------------
# Plan + execute
# ---------------------------------------------------------------------------

def plan_writes(spec: dict) -> list[PlannedWrite]:
    target = spec["target"]
    plan: list[PlannedWrite] = [
        PlannedWrite(target / ".claude" / "skills" / spec["skill_filename"], render_skill_md(spec), "skill"),
        PlannedWrite(target / "drift-mappings.json", json.dumps(render_drift_mappings(spec), indent=2) + "\n", "drift"),
    ]
    if spec["want_replay"]:
        plan.append(PlannedWrite(target / "replay" / "generate_replay.py", render_replay_py(spec), "replay-py"))
        plan.append(PlannedWrite(target / "replay" / "replay_template.html", render_replay_html(spec), "replay-html"))
    if spec["want_manifest"]:
        plan.append(PlannedWrite(target / "manifest.json", json.dumps(render_manifest(spec), indent=2) + "\n", "manifest"))
    if spec["want_invariant"]:
        tmpl = spec["meta_skill_root"] / "references" / "domain-invariant-template.md"
        plan.append(PlannedWrite(target / "domain-invariant.md", render_invariant(spec, tmpl), "invariant"))
    if spec["want_register"]:
        plan.append(PlannedWrite(target / ".sand-table" / "registry-row.md", render_registry_row(spec), "registry"))
    # Refuse to write outside target (symlink safety).
    target_resolved = target.resolve()
    for pw in plan:
        try:
            resolved = pw.abs_path.resolve(strict=False)
            resolved.relative_to(target_resolved)
        except ValueError:
            print(f"ERROR: planned write resolves outside target: {pw.abs_path} -> {resolved}", file=sys.stderr)
            sys.exit(5)
    return plan


def execute_plan(plan: list[PlannedWrite], force: bool, dry_run: bool) -> int:
    conflicts = [pw for pw in plan if pw.abs_path.exists()]
    if conflicts and not force:
        print(f"ERROR: {len(conflicts)} file(s) already exist (use --force to overwrite):", file=sys.stderr)
        for pw in conflicts:
            print(f"  - {pw.abs_path}", file=sys.stderr)
        return 3
    if dry_run:
        print("DRY RUN — no writes performed. Planned files:")
        for pw in plan:
            tag = " (overwrite)" if pw.abs_path.exists() else ""
            print(f"  + [{pw.kind}] {pw.abs_path}{tag}")
        return 0
    written = 0
    for pw in plan:
        pw.abs_path.parent.mkdir(parents=True, exist_ok=True)
        # Atomic write via temp + replace.
        tmp = pw.abs_path.with_suffix(pw.abs_path.suffix + ".tmp")
        tmp.write_text(pw.content)
        tmp.replace(pw.abs_path)
        action = "OVERWROTE" if pw in conflicts else "WROTE"
        print(f"  {action}: {pw.abs_path}")
        written += 1
    print(f"\nScaffold complete — {written} file(s) written.")
    return 0


def main() -> int:
    args = parse_args()
    spec = prompt_missing(args)
    errors = validate_spec(spec)
    if errors:
        print("Invalid spec:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 2

    plan = plan_writes(spec)
    rc = execute_plan(plan, force=args.force, dry_run=args.dry_run)

    if rc == 0 and not args.dry_run:
        print()
        print("Registry row (paste into <meta-skill>/references/implementations.md):")
        print()
        print(render_registry_row(spec))
    return rc


if __name__ == "__main__":
    sys.exit(main())
