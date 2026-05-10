---
name: sand-table
description: Design, scaffold, extract, and validate Sand Table simulations and event streams across domains. Meta skill that knows the protocol and all existing implementations.
---

# Sand Table — Protocol Meta Skill

Design new sand tables, scaffold project-local skills, extract agent-ops traces, and validate event streams. This skill knows the protocol and all existing implementations.

## When to Use

- `/sand-table design <use-case>` — Design a sand table for a new domain
- `/sand-table scaffold` — Generate a project-local skill + domain invariant
- `/sand-table extract <project-path>` — Extract agent-ops from Claude session logs
- `/sand-table validate <json-path>` — Check event stream against protocol
- "How should I build a sand table for X?"
- "What sand table implementations exist?"

## What This Skill Knows

1. **The Protocol** — Read `references/protocol-spec.md` for the event envelope, temporal models, normalization contract, execution tiers (Tier 1-3), multi-run comparison, and replay injection patterns.

2. **Existing Implementations** — Read `references/implementations.md` for the registry of Substack readership, AIEnablement training, and Agent-Ops implementations with their paths, event types, and temporal models.

3. **Domain Design** — Read `references/domain-invariant-template.md` for the scaffold template. Read `references/examples.md` for real annotated events from all three domains.

4. **Reusable Patterns** — Read `references/patterns.md` for the 6 battle-tested design recipes: program invariant structure, agent design, event schema enforcement (including the known LLM drift catalog), output structure, new domain creation, and multi-run comparison.

5. **Reliability** — Read `references/reliability.md` for impossible narrative detection, timeout/abort rules, module batching, and cross-session context resolution patterns.

6. **Multi-Session Continuity** — Read `references/multi-session.md` for the exit context schema, context loading chain, cohort matching, and context accumulation model.

## Commands

> All script invocations below use `<skill-root>` as a placeholder for the skill directory (`SandTable/sand-table/` in this repo). Substitute your install path or `cd` into the skill directory before running.

### `design <use-case>`

1. Read `references/protocol-spec.md`, `references/domain-invariant-template.md`, and `references/patterns.md`
2. Recommend: temporal model, persona count, event types, scoring dimensions, execution tier (Tier 1-3)
3. Identify closest existing implementation (from `references/implementations.md`) as a reference pattern
4. Output a filled domain invariant for the proposed domain
5. Flag domain-specific drift risks using the known drift catalog from `references/patterns.md`
6. Recommend reliability configuration: timeout thresholds, abort conditions, narrative integrity checks (from `references/reliability.md`)
7. If multi-session: recommend exit context schema and context loading strategy (from `references/multi-session.md`)

### `scaffold`

Generate a project-local Sand Table installation into a target project:

```bash
python <skill-root>/scripts/scaffold.py \
    --target /path/to/project \
    --domain my-sim --name "My Sim" \
    --description "What it simulates" \
    --source-type simulation --temporal-model turn \
    --tier 1 --agent-count 6 --event-types reader,section_scores \
    --register --non-interactive
```

In a TTY, omit any of those flags to be prompted interactively. Use `--dry-run` to preview without writing.

Generated files (refused if they exist; pass `--force` to overwrite):
- `.claude/skills/sand-table-{domain}.md` — project-local skill stub
- `drift-mappings.json` — seeded with the cross-domain field-rename baseline (10+ known LLM drift patterns from `references/patterns.md` §3.2) plus per-event-type `type_conditional_field_renames` stubs
- `replay/generate_replay.py` + `replay/replay_template.html` — minimal replay generator with `{{SIMULATION_DATA}}` placeholder (skipped for `--source-type extraction` or `--no-replay-stub`)
- `manifest.json` — protocol v1.1 discovery manifest
- `domain-invariant.md` — copy of `references/domain-invariant-template.md` with the Identity block lightly filled (`--no-invariant` to skip)
- `.sand-table/registry-row.md` — markdown row to paste into the meta-skill's `references/implementations.md` (only with `--register`); also printed to stdout

Atomic writes via temp + replace; refuses any planned write that would resolve outside `--target` (symlink safety).

### `extract <project-path>`

Run the shared extractor:

```bash
python <skill-root>/scripts/extract_agent_ops.py \
    --project <project-path> --since <date> -o <output.json>
```

Then validate the output:

```bash
python <skill-root>/scripts/validate_stream.py <output.json>
```

### `validate <json-path>`

Run the full validation pipeline (structural + drift + clamping + narrative):

```bash
python <skill-root>/scripts/validate_full.py <json-path> \
    [--mappings drift-mappings.json] \
    [--write-normalized <output.json>] \
    [--no-narrative]
```

The pipeline runs five stages, each with its own report section:
- **Structural** — envelope shape, required `meta` fields, agent ID cross-refs, timestamp ordering (delegates to `validate_stream.py`)
- **Drift** — applies `drift-mappings.json` to fix LLM field-name drift (delegates to `normalize.py`)
- **Score Clamping** — clamps numeric `scores` values to `mappings.score_range` or `--score-range` (default `[0, 5]`)
- **Derived Fields** — stamps `meta.event_count` and `meta.agent_count` if absent
- **Narrative** — runs impossible-narrative scan (delegates to `narrative_check.py`); advisory only, never fails the build

Exit code: `0` on pass, `1` if structural violations exist. Narrative warnings never fail.

For envelope-only checks use `validate_stream.py` directly. For legacy formats normalize first:

```bash
python <skill-root>/scripts/normalize.py --wrap-legacy <json-path> -o <output.json>
```

### `reliability <json-path>`

Run the reliability report — narrative integrity, data completeness, optional context-chain validation, and a deterministic recommendation:

```bash
python <skill-root>/scripts/reliability_report.py <json-path> \
    [--context-dir <dir>] \
    [--prior s1-run5,s2-run6]
```

Output sections (matches `references/reliability.md` format):

1. **Narrative Integrity** — CLEAN / WARNING (1-5 flags) / INTEGRITY CONCERN (6+); per-signal counts and snippets (delegates to `narrative_check.py`)
2. **Data Completeness** — NR/timeout count, affected agents and units. Only counts events with explicit NR markers (`type: timeout`, `status: NR`, `nr: true`) — never inferred from missing fields.
3. **Context Chain** — multi-session validation (only when `--context-dir`/`--prior` given). For each prior run, loads `<dir>/<run-id>/context/<agent>-exit-context.json`, validates required keys (`agent_id`, `scores` are hard-required; `growth_narrative`, `headline_quote`, `behavioral_markers` are recommended), checks cohort match against current roster.
4. **Recommendation** — deterministic rule output: `ACCEPT` / `REVIEW` / `RE-RUN` / `HALT`. Always exits `0`; callers wanting a hard gate should grep for `RECOMMENDATION: HALT`.

## Key Principle

This meta skill is a guide, not a gatekeeper. Project-local sand tables work standalone. The meta skill adds wisdom when consulted — protocol awareness, cross-domain patterns, and normalization infrastructure.
