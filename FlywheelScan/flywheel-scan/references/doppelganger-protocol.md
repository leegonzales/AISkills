# Doppelganger Protocol — Strategic Review

**Purpose:** Protocol for the Lee Doppelganger agent to review all scout findings, score work items, and propose thread resolutions using Lee's goals graph and decision heuristics.

---

## Inputs

The doppelganger receives:

1. **Scout results** — all `scout-{domain}-results.json` files merged
2. **Goals context** — output of `goals_query.py status`, `threads`, `tensions`
3. **Scoring rubric** — 4 dimensions x 5 points (from `references/scoring-rubric.md`)
4. **Persona schema** — Lee's decision-making model (from silicon-doppelganger-actual)
5. **Previous scan** — prior `master-work-queue.md` and `thread-proposals.md` (if available)

## Phase 1: Situational Awareness

### 1.1 Read Goals Graph
- Load all objectives, constraints, revenue streams, and active tensions
- Identify which goals are on track vs. at risk
- Note binding constraints (time/energy budget, W-2 stability)

### 1.2 Inventory Scout Findings
- Count repos per classification (`active-invest`, `maintain`, `archive`)
- List all proposed beads across scouts
- Identify cross-repo dependencies and blockers
- Flag any `severity: "high"` findings

### 1.3 Load Thread History
If a previous scan exists, read prior thread proposals to track:
- Which threads were resolved since last scan
- Which remain open
- Any new threads that emerged

## Phase 2: Priority Scoring

For each proposed bead from the scouts:

### 2.1 Reasoning First
Write 2-3 sentences explaining:
- How this work connects to Lee's goals
- What it unblocks
- What tension it navigates
- Why the energy investment is or isn't worth it

### 2.2 Score Each Dimension
Apply the scoring rubric independently:

| Dimension | Question |
|-----------|----------|
| `goals_alignment` | How directly does this serve a 2026 objective? |
| `energy_impact_ratio` | How much output per unit of scarce time? |
| `unblocking_value` | Does completing this cascade to other work? |
| `tension_awareness` | Does this navigate or resolve a known tension? |

### 2.3 Compute Total & Rank
- Sum 4 dimensions (max 20)
- Rank all items by total (break ties by `unblocking_value`)
- Assign tier based on score range

### 2.4 Emit Events
For each scored item, emit a `priority_score` event with all fields.

After all items scored, emit a single `master_queue` event with the full ranked list.

## Phase 3: Thread Resolution

Identify open strategic threads — decisions that need Lee's input.

### 3.1 Sources of Threads
- Tensions in the goals graph
- Cross-repo conflicts (e.g., branding, revenue mechanics)
- Gaps discovered by scouts that require strategic choices
- Unresolved threads from previous scans

### 3.2 Per Thread
For each thread:

1. **Name it** — stable `thread_id` and human-readable `thread_title`
2. **Frame the decision** — what needs to be decided and why now
3. **Draft 2-3 options** — each with:
   - `label`: short name
   - `description`: what this option means
   - `trade_offs`: what you gain and lose
   - `recommendation`: boolean (exactly one should be `true`)
4. **Lee's voice** — write 1 sentence as Lee would say it (captures the felt priority)
5. **Emit** a `thread_proposal` event

### 3.3 Thread Stability
Use stable `thread_id` values so the diff engine can track threads across scans:
- Format: `thread-{slug}` (e.g., `thread-differential-mechanics`)
- Reuse IDs from previous scans for continuing threads
- New threads get new IDs

## Phase 4: Strategic Observations

Emit `observation` events for cross-cutting insights:
- Patterns across domains (e.g., "4 repos have stale beads")
- Compound effects (e.g., "training launch + content pipeline + website = visibility flywheel")
- Risk patterns (e.g., "3 repos have no version control on significant IP")

Limit to 3-5 observations. Quality over quantity.

## Output

Write all events to: `doppelganger-results.json`

```json
{
  "agent": "lee-doppelganger",
  "events": [ ... priority_score events, thread_proposal events, master_queue event, observation events ... ]
}
```

## Decision Heuristics — DO NOT DUPLICATE

**CRITICAL:** Do not hardcode Lee's decision heuristics here. Load them at runtime from the canonical source:

```
~/.claude/skills/silicon-doppelganger-actual/data/lee-gonzales-persona-schema.xml
```

The orchestrator (SKILL.md Step 10) passes the full persona schema to the doppelganger agent. The agent must use the persona's actual decision patterns, cognitive biases, and values — not a summary.

**Why:** The persona schema evolves. If we duplicate heuristics here, they drift out of sync with the actual doppelganger skill. Single source of truth = the persona schema XML.

**What to load at runtime:**
- `lee-gonzales-persona-schema.xml` — decision-making model, values, cognitive patterns
- `goals-graph.yaml` — objectives, constraints, tensions, revenue streams
- `goals_query.py status` — current goal state
- `goals_query.py threads` — open decision threads
- `goals_query.py tensions` — active tensions
