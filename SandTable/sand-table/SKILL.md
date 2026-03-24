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

### `design <use-case>`

1. Read `references/protocol-spec.md`, `references/domain-invariant-template.md`, and `references/patterns.md`
2. Recommend: temporal model, persona count, event types, scoring dimensions, execution tier (Tier 1-3)
3. Identify closest existing implementation (from `references/implementations.md`) as a reference pattern
4. Output a filled domain invariant for the proposed domain
5. Flag domain-specific drift risks using the known drift catalog from `references/patterns.md`
6. Recommend reliability configuration: timeout thresholds, abort conditions, narrative integrity checks (from `references/reliability.md`)
7. If multi-session: recommend exit context schema and context loading strategy (from `references/multi-session.md`)

### `scaffold`

1. Ask which domain invariant to use (or design one first)
2. Generate into the current project:
   - A project-local skill (`.claude/skills/sand-table.md` or similar)
   - A `drift-mappings.json` for the domain
   - A replay generator stub
3. Register in `references/implementations.md`
4. Optionally generate a `manifest.json` for discovery

### `extract <project-path>`

Run the shared extractor:

```bash
python ~/Projects/leegonzales/AISkills/SandTable/sand-table/scripts/extract_agent_ops.py \
    --project <project-path> --since <date> -o <output.json>
```

Then validate the output:

```bash
python ~/Projects/leegonzales/AISkills/SandTable/sand-table/scripts/validate_stream.py <output.json>
```

### `validate <json-path>`

```bash
python ~/Projects/leegonzales/AISkills/SandTable/sand-table/scripts/validate_stream.py <json-path>
```

Validation includes:
- Schema compliance (required fields, valid types, enum values)
- Drift correction using domain `drift-mappings.json` (see known drift catalog in `references/patterns.md`)
- Impossible narrative detection for multi-agent simulations (see `references/reliability.md`)
- Score range clamping and derived field computation

For legacy-format files (pre-protocol), normalize first:

```bash
python ~/Projects/leegonzales/AISkills/SandTable/sand-table/scripts/normalize.py \
    --wrap-legacy <json-path> -o <output.json>
```

### `reliability <json-path>`

Run the full reliability analysis on a simulation output:

1. Read `references/reliability.md` for the detection patterns
2. Scan all agent events for impossible narrative signals (5 checks)
3. Check for timeout/NR events and assess simulation completeness
4. If multi-session: validate exit context files against schema (from `references/multi-session.md`)
5. Output a reliability report:
   - Narrative integrity status (CLEAN / N warnings / INTEGRITY CONCERN)
   - Data completeness (NR count, missing events)
   - Context chain validity (multi-session only)
   - Recommendations (re-run, accept, investigate specific agents)

## Key Principle

This meta skill is a guide, not a gatekeeper. Project-local sand tables work standalone. The meta skill adds wisdom when consulted — protocol awareness, cross-domain patterns, and normalization infrastructure.
