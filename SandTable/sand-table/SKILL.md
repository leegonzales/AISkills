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

1. **The Protocol** — Read `references/protocol-spec.md` for the event envelope, temporal models, normalization contract, multi-run comparison, and replay injection patterns.

2. **Existing Implementations** — Read `references/implementations.md` for the registry of Substack readership, AIEnablement training, and Agent-Ops implementations with their paths, event types, and temporal models.

3. **Domain Design** — Read `references/domain-invariant-template.md` for the scaffold template. Read `references/examples.md` for real annotated events from all three domains.

## Commands

### `design <use-case>`

1. Read `references/protocol-spec.md` and `references/domain-invariant-template.md`
2. Recommend: temporal model, persona count, event types, scoring dimensions
3. Identify closest existing implementation (from `references/implementations.md`) as a reference pattern
4. Output a filled domain invariant for the proposed domain
5. Flag domain-specific drift risks (what will the LLM get wrong?)

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

For legacy-format files (pre-protocol), normalize first:

```bash
python ~/Projects/leegonzales/AISkills/SandTable/sand-table/scripts/normalize.py \
    --wrap-legacy <json-path> -o <output.json>
```

## Key Principle

This meta skill is a guide, not a gatekeeper. Project-local sand tables work standalone. The meta skill adds wisdom when consulted — protocol awareness, cross-domain patterns, and normalization infrastructure.
