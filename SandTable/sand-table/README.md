# Sand Table Protocol

A protocol and shared infrastructure for building domain-specific simulations and event stream replays.

## What Is a Sand Table?

A sand table simulates participants experiencing something — readers encountering an essay, trainees going through a coaching module, agents building software. The output is a stream of events that can be replayed, compared across runs, and analyzed.

Three implementations follow this pattern today:

| Domain | Source | What It Does |
|--------|--------|--------------|
| **Readership** | LLM simulation | 6 reader personas react to essay sections |
| **Training** | Multi-agent simulation | 6-12 participants go through coaching modules |
| **Agent-Ops** | Log extraction | Claude Code sessions → development event timeline |

All three: Events → Normalize → Interactive HTML Replay → Compare runs.

## What's New in v1.1

**Reliability patterns** — Battle-tested patterns for ensuring multi-agent simulations produce valid data. Includes impossible narrative detection (5 signals that catch single-author simulations), timeout/abort rules for non-responsive agents, and module batching for pacing optimization. See `references/reliability.md`.

**Multi-session continuity** — Full pattern for carrying agent state across simulation sessions. Exit context schema captures growth narratives, scores, and behavioral markers. Context loading validates and assembles prior session data into spawn prompts with hard gates on missing data. See `references/multi-session.md`.

**Tier 3 execution** — Protocol support for real AI agent interaction, where participant agents send actual prompts to dedicated tool agents and receive real responses. Captures `prompt_sent`, `ai_response`, and `follow_ups` fields. See the Execution Tiers section in `references/protocol-spec.md`.

**Known LLM drift catalog** — A table of 10+ field name substitutions that LLMs reliably make across domains (`module_id` for `module`, `intervention` for `text`, etc.), plus guidance on building domain-specific drift mappings. See Pattern 3 in `references/patterns.md`.

**Reusable design recipes** — Six domain-agnostic patterns extracted from production implementations: program invariant structure, agent design recipes, event schema enforcement, output structure, new domain creation, and multi-run comparison. See `references/patterns.md`.

**Reliability command** — New `/sand-table reliability` command for running narrative integrity analysis, data completeness checks, and context chain validation.

The canonical complex example for all patterns is the [AI Foundations training implementation](https://github.com/leegonzales/AIEnablementTraining) (18 personas, Tier 3 execution, multi-session continuity, 8+ successful runs).

## Project Structure

```
sand-table/
├── SKILL.md                          # Meta skill for Claude Code
├── references/
│   ├── protocol-spec.md              # The protocol: envelope, temporal models, normalization
│   ├── implementations.md            # Registry of known sand tables
│   ├── domain-invariant-template.md  # Scaffold for new domains
│   ├── examples.md                   # Annotated real events from all 3 domains
│   ├── patterns.md                   # 6 reusable design recipes
│   ├── reliability.md                # Simulation reliability patterns
│   └── multi-session.md              # Multi-session continuity pattern
├── scripts/
│   ├── normalize.py                  # Shared normalizer (drift mappings → clean events)
│   ├── validate_stream.py            # Protocol compliance checker
│   └── extract_agent_ops.py          # Session logs → protocol-compliant events
└── templates/
    ├── replay-base.css               # Catalyst palette CSS variables
    └── manifest.json                 # Project discovery template
```

## Quick Start

### Validate an existing event stream

```bash
python scripts/validate_stream.py path/to/events.json
```

### Normalize a drifted stream

```bash
python scripts/normalize.py path/to/events.json \
    --mappings path/to/drift-mappings.json \
    -o normalized.json
```

### Extract agent-ops from a Claude Code session

```bash
python scripts/extract_agent_ops.py \
    --project ~/Projects/myrepo \
    --since 2026-03-14 \
    -o agent-ops.json
```

### Design a new sand table

In Claude Code:
```
/sand-table design "customer journey simulation for SaaS onboarding"
```

## The Protocol

See `references/protocol-spec.md` for the full spec. Key points:

- Every stream has `meta`, `agents`, `events` (optional `summary`)
- Events have `type` (string) + one temporal field (`turn`, bracket markers, or `timestamp`)
- Three execution tiers: narrated (Tier 1), scripted (Tier 2), real agent interaction (Tier 3)
- Domains provide `drift-mappings.json` for LLM schema drift correction
- Multi-run comparison via `meta.id` + `meta.run`
- Replay injection via `{{SIMULATION_DATA}}` placeholder
- Reliability contract: timeout handling, abort thresholds, impossible narrative detection
- Multi-session continuity: exit context, validation chain, cohort matching

## Design Principles

1. **Protocol, not framework** — defines the envelope, not the contents
2. **Existing implementations stay as-is** — no migration required
3. **Meta skill is a guide, not a gatekeeper** — project-local sand tables work standalone
4. **Don't get too precious** — the abstraction must reduce cognitive load, not add it
