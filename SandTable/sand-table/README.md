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

## Project Structure

```
sand-table/
├── SKILL.md                          # Meta skill for Claude Code
├── references/
│   ├── protocol-spec.md              # The protocol: envelope, temporal models, normalization
│   ├── implementations.md            # Registry of known sand tables
│   ├── domain-invariant-template.md  # Scaffold for new domains
│   └── examples.md                   # Annotated real events from all 3 domains
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
- Domains provide `drift-mappings.json` for LLM schema drift correction
- Multi-run comparison via `meta.id` + `meta.run`
- Replay injection via `{{SIMULATION_DATA}}` placeholder

## Design Principles

1. **Protocol, not framework** — defines the envelope, not the contents
2. **Existing implementations stay as-is** — no migration required
3. **Meta skill is a guide, not a gatekeeper** — project-local sand tables work standalone
4. **Don't get too precious** — the abstraction must reduce cognitive load, not add it
