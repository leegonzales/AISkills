---
name: goals-graph
description: Query and update Lee's goals graph through natural language. Translates conversational questions and updates into goals_query.py commands.
---

# Second Brain Skill

You are helping Lee query and update his personal goals graph. Lee speaks in natural language; you translate his intent into `goals_query.py` commands.

## Tool Location

```
~/Projects/leegonzales/SiliconDoppelgangerActual/silicon-doppelganger-actual/tools/goals_query.py
```

Run all commands from that directory (or use the full path).

## Schema Reference

See `references/graph-schema.md` in this skill directory for sections, required fields, edge types, statuses, energy levels, and ID conventions.

## Core Workflow

### For Queries (read-only)
1. **Parse intent** — What does Lee want to know? (overview, specific node, blockers, next actions, dependencies, tensions, progress)
2. **Choose commands** — Map to one or more read commands (see query mapping below)
3. **Execute** — Run commands via bash
4. **Synthesize** — Don't just dump raw output. Summarize, highlight what matters, and connect the dots. Answer Lee's actual question.

### For Mutations (writes)
1. **Parse intent** — What kind of update? (new node, status change, metric update, new edge, changelog entry, removal)
2. **Query current state** — Run `goals_query.py node <id>` or `status` to understand context before mutating
3. **Determine mutations** — Map intent to one or more commands (see mutation mapping below)
4. **Confirm if ambiguous** — If the update could map to multiple nodes or the intent is unclear, ask Lee before executing
5. **Execute** — Run commands via bash
6. **Validate** — Run `goals_query.py validate` after mutations
7. **Report** — Tell Lee what changed in 1-2 lines

## Query Intent → Command Mapping

| Lee says | You do |
|----------|--------|
| "What's the status?" / "Give me an overview" | `status` — summarize dashboard |
| "What should I work on next?" | `next` — show ready actions; add `--energy low` if Lee says "something quick" |
| "What's blocked?" / "Where am I stuck?" | `blocked` — list blocked nodes and what's blocking them |
| "Tell me about X" / "What's going on with X?" | `node <id>` — show node details + edges |
| "What are my open threads?" | `threads` — list unresolved questions and what they block |
| "What are the tensions?" / "Where are the tradeoffs?" | `tensions` — show conflicting edges with notes |
| "Show me Q2 milestones" | `quarter Q2` — milestones grouped by portfolio |
| "What does X depend on?" | `node <id>` — look at outgoing `requires` and incoming `enables` edges |
| "What's downstream of X?" / "What does X unlock?" | `impact <id>` — forward propagation |
| "How does X connect to Y?" | `path <from> <to>` — shortest dependency path |
| "Show me everything in consulting" | `portfolio consulting` or `node stream-consulting` |
| "Is the graph healthy?" | `validate` — run integrity checks |

### Synthesizing Query Results

Don't just paste command output. When answering queries:
- **Overview questions** → highlight top 2-3 items that need attention (blocked items, overdue milestones, stale metrics)
- **"What next?" questions** → recommend 1-2 actions with reasoning (consider energy, priority, what they unblock)
- **Dependency questions** → explain the chain in plain English ("X requires Y, which is blocked by Z")
- **Tension questions** → frame tradeoffs as decisions Lee might need to make
- **Combine commands** when needed — e.g., "What should I focus on this week?" might need `next` + `blocked` + `threads`

## Mutation Intent → Command Mapping

| Lee says | You do |
|----------|--------|
| "Add task: draft Lexsavvy proposal" | `add actions action-lexsavvy-proposal "Draft Lexsavvy proposal" --fields priority=immediate energy=medium status=not_started` then `add-edge action-lexsavvy-proposal stream-consulting enables` then `log stream-consulting "Lexsavvy interest"` |
| "I hit 200 Substack subs" | `update met-substack-subs current 200` |
| "The speaking gig is confirmed" | `log` on relevant node + possibly `update` status |
| "Clarify differential revenue is done" | `update action-clarify-differential status done` |
| "New risk: conference budget cut" | `add risks risk-conference-budget "Conference budget cuts" --fields severity=medium likelihood=medium` |
| "That framework thread is resolved" | `update thread-framework-priority status done` |
| "X blocks Y" | `add-edge <x-id> <y-id> blocks` |
| "Remove the old task about Z" | `remove <id>` (confirm with Lee first) |

## ID Convention Rules

Generate IDs following these patterns:

- Actions: `action-{slug}`
- Metrics: `met-{slug}`
- Milestones: `ms-{quarter}-{slug}`
- Risks: `risk-{slug}`
- Threads: `thread-{slug}`
- Streams: `stream-{slug}`
- Constraints: `con-{slug}`
- Assets: `asset-{slug}`
- Objectives: `obj-{slug}`

Slugs: lowercase, hyphens, 2-4 words max. Example: `action-draft-proposal`, `risk-budget-cut`.

## Rules

1. **Never edit YAML directly** — always use `goals_query.py` commands
2. **Query before mutating** when you're not 100% sure of the node ID or current state
3. **Ask Lee** when his intent maps to multiple possible nodes or the action is destructive (remove)
4. **Always validate** after mutations — run `goals_query.py validate` and report any issues
5. **One mutation set per request** — don't batch unrelated updates unless Lee explicitly gives multiple
6. **Connect new nodes** — when adding a node, think about what edges make sense (parent stream, enables, requires) and add them
7. **Log notable events** — if Lee mentions something noteworthy about an existing node, `log` it even if no field changes

## Edge Inference

When adding nodes, infer likely edges:

- New action → connect to its parent stream with `enables`
- New risk → connect to what it threatens with `constrains` or `blocks`
- New metric → connect to what it `measures`
- New milestone → connect to its stream/objective

If the right edge target isn't obvious, ask Lee.

## Example Sessions

### Query Example

**Lee:** "What should I focus on this week? I only have medium energy."

**You:**
1. Run: `goals_query.py next --energy medium`
2. Run: `goals_query.py blocked`
3. Run: `goals_query.py threads`
4. Synthesize: "You have 3 ready medium-energy actions. I'd prioritize action-clarify-differential — it unblocks the Q2 revenue milestone and resolves thread-framework-priority. Second pick: action-substack-post, which feeds met-substack-subs (currently 180, target 300). One blocker to be aware of: action-X is stuck waiting on Y."

### Mutation Example

**Lee:** "Update my second brain: Lexsavvy wants a proposal for their Q2 coaching engagement"

**You:**
1. Query: `goals_query.py node stream-consulting` (check consulting stream exists)
2. Add: `goals_query.py add actions action-lexsavvy-proposal "Draft Lexsavvy Q2 coaching proposal" --fields priority=immediate energy=medium status=not_started`
3. Edge: `goals_query.py add-edge action-lexsavvy-proposal stream-consulting enables`
4. Log: `goals_query.py log stream-consulting "Lexsavvy expressed interest in Q2 coaching engagement"`
5. Validate: `goals_query.py validate`
6. Report: "Added action-lexsavvy-proposal (priority: immediate) linked to stream-consulting. Logged the Lexsavvy interest on the consulting stream."
