# Goals Graph Schema Reference

> Quick-ref for `goals_query.py` in `~/Projects/leegonzales/SiliconDoppelgangerActual/`

## Sections & Required Fields

| Section | Required Fields | Notes |
|---------|----------------|-------|
| `constraints` | `type` | |
| `streams` | `parent` | |
| `metrics` | `current`, `target`, `measures` | `as_of` auto-set on update |
| `risks` | `severity`, `likelihood` | Optional: `mitigation`, `mitigates` |
| `open_threads` | `priority` | Optional: `questions` (list), `blocks` (list) |
| `milestones` | `quarter`, `portfolio`, `parent` | |
| `actions` | `priority`, `energy` | Optional: `requires`, `resolves` |
| `objectives` | *(none)* | |

## Valid Statuses

`not_started` · `in_progress` · `done` · `blocked` · `ongoing`

## Valid Energy Levels (actions only)

`low` · `medium` · `high`

## Edge Types

| Type | Meaning |
|------|---------|
| `tensions_with` | Conflicting goals/constraints |
| `constrains` | Limits another node |
| `hedges` | Risk mitigation relationship |
| `enables` | Unlocks another node |
| `requires` | Dependency (must happen first) |
| `feeds` | Provides input/resources downstream |
| `blocks` | Prevents another from starting |
| `measures` | Metric tracks a node's progress |

## ID Conventions

| Section | Pattern | Example |
|---------|---------|---------|
| actions | `action-{slug}` | `action-lexsavvy-proposal` |
| metrics | `met-{slug}` | `met-substack-subs` |
| milestones | `ms-{quarter}-{slug}` | `ms-q2-launch` |
| risks | `risk-{slug}` | `risk-conference-budget` |
| open_threads | `thread-{slug}` | `thread-framework-priority` |
| streams | `stream-{slug}` | `stream-consulting` |
| constraints | `con-{slug}` | `con-time` |
| assets | `asset-{slug}` | `asset-framework-deck` |
| objectives | `obj-{slug}` | `obj-revenue-growth` |

## Write Commands

```
# Add a node
goals_query.py add <section> <id> <label> [--fields key=value ...]

# Add an edge
goals_query.py add-edge <from> <to> <type> [--note "..."]

# Update a field
goals_query.py update <id> <field> <value>

# Log a changelog entry
goals_query.py log <id> <note>

# Remove a node
goals_query.py remove <id> [--force]

# Remove an edge
goals_query.py remove-edge <from> <to> [type]
```

## Read Commands

```
goals_query.py status          # Dashboard overview
goals_query.py node <id>       # Single node + edges
goals_query.py next [--energy] # Ready actions
goals_query.py blocked         # Blocked nodes
goals_query.py threads         # Open threads
goals_query.py validate        # Integrity check
goals_query.py quarter <Q>     # Milestones by quarter
goals_query.py portfolio <name># Nodes by portfolio
goals_query.py tensions        # Tension edges
goals_query.py path <from> <to># Shortest path
goals_query.py impact <id>     # Forward propagation
```

## Field Type Coercion (--fields)

- `[a, b, c]` → list
- `123` → int
- `1.5` → float
- Everything else → string
