# Simulation Reliability Patterns

Patterns for ensuring multi-agent simulations produce valid, trustworthy data. These apply to any sand table that uses independent agents communicating through messages.

---

## Impossible Narrative Detection

### What It Is

A post-simulation scan that detects when an LLM "breaks character" by having one agent demonstrate knowledge that only another agent should possess. This is the primary signal that a simulation was executed by a single agent writing all voices rather than by genuinely independent agents.

### Why It Matters

A single agent controlling all personas produces creative writing, not simulation. It cannot surprise itself. The diagnostic value of a sand table comes from emergent behavior — friction, unexpected responses, and failure modes that only appear when independent processes interact. Impossible narratives indicate the simulation data is unreliable.

### The 5 Signals

Scan all agent events with free-text fields (internal monologue, spoken dialogue, narrative text) for these patterns:

**1. Other-Agent Predictions**

Patterns: "{Name} will notice/think/realize/feel/respond", "she'll probably say", "he's going to push back"

Why impossible: An independent agent does not know what other agents will do. Only a single author controlling all voices has that knowledge.

**2. Direct Knowledge of Other Agents' Internal State**

Patterns: "{Name} is thinking", "she feels", "he's struggling with", "they're excited about"

Why impossible: Agents receive only what the orchestrator sends them. They cannot observe other agents' internal states (energy levels, emotional state, thought processes) unless the orchestrator explicitly relayed that information.

**3. Meta-Commentary and Cross-Agent Comparisons**

Patterns: "this is the most X in the cohort", "the strongest response so far", "unlike the others", "compared to {other agent}'s approach"

Why impossible: An agent does not know what other agents produced unless the orchestrator relayed it. Cross-agent comparisons in internal monologue indicate single-author omniscience.

**4. Scoring and Evaluation Awareness**

Patterns: "this will score", "the leader will see", "this demonstrates growth", "this should register as"

Why impossible: Participant agents should not know they are being scored. These are author-voice leaks from a single agent simultaneously writing participant dialogue and managing the evaluation framework.

**5. Suspiciously Synchronized Exchanges**

In pair/exchange events, check if both sides use complementary vocabulary, mirror each other's rhetorical structure, or show emotional arcs that dovetail too neatly. Flag pairs where both sides share more than 3 uncommon phrases or follow the same structural pattern.

Why suspicious: Independent agents responding to each other produce messy, asymmetric exchanges. Perfectly complementary responses suggest one mind wrote both sides.

### How to Implement

Add a post-simulation validation step that scans all agent output text:

```
For each agent event with free-text content:
  1. Extract internal_monologue, text, spoken fields
  2. Scan for patterns matching signals 1-4 (regex or keyword matching)
  3. For exchange events, run signal 5 (structural similarity analysis)
  4. Collect all flagged instances with: event index, agent ID, signal type, flagged text

Report:
  - CLEAN: 0 warnings
  - WARNING: 1-5 warnings (minor leakage, likely still valid)
  - INTEGRITY CONCERN: 6+ warnings (likely single-agent execution)
```

### Threshold Guidance

- 0 warnings: Clean independent execution
- 1-5 warnings: Minor leakage — review flagged instances but simulation is likely valid
- 6+ warnings: High probability of single-agent execution. Re-run with verified multi-agent team

For example, in the AI Foundations training implementation, the validator agent runs this check automatically and produces a "Narrative Integrity Warnings" section in its validation report.

---

## Timeout and Abort Rules

### What It Is

Protocol for handling non-responsive agents during simulation execution. In multi-agent orchestration, agents can fail to respond due to context exhaustion, tool errors, or infrastructure issues.

### Why It Matters

Without timeout rules, a stuck agent blocks the entire simulation indefinitely. Without abort rules, a degraded simulation continues collecting meaningless data.

### Timeout Protocol

When an agent fails to respond after the orchestrator's delivery and one re-ping:

1. **Orchestrator reports timeout** to the leader/coordinator
2. **Leader marks the agent as NON-RESPONSIVE (NR)** for this unit
3. **Leader records a timeout observation event** — this is an observation that the agent did not respond, NOT a fabricated agent event
4. **Leader proceeds** to the next step (scoring, next unit) without waiting further

**Critical rule: Do NOT reconstruct.** A non-responsive agent produces no event for that unit. Scoring shows `NR` for that cell. The evaluation report notes the gap. Real missing data is infinitely better than fabricated data.

### Abort Rules

Define an abort threshold based on your domain's tolerance for missing data:

**Default recommendation:**
- **Abort if** N or more agents are non-responsive for M or more consecutive units
- **Typical threshold:** 3+ agents NR for 2+ consecutive units (for a 6-agent simulation)

**Abort message format:**
```
ABORT: {N} agents non-responsive for {M} consecutive units.
Simulation lacks sufficient independent agent data to produce valid results.
Check agent spawn prompts and team connectivity before re-running.
```

### What to Customize

- NR threshold (depends on total agent count — 50% NR is always an abort)
- Consecutive unit threshold (depends on unit count — 2 is good for 10+ units, 1 for fewer)
- Whether to attempt partial recovery (re-spawn individual agents mid-simulation)

---

## Module Batching

### What It Is

An optimization that delivers consecutive non-interactive units as a single batch to reduce message overhead and improve pacing.

### Why It Matters

In simulations with many sequential units, the message round-trip overhead (orchestrator delivers, each agent responds, orchestrator collects) can dominate execution time. Batching consecutive non-interactive units (where agents respond with dialogue or reflection, not with tool interactions) significantly reduces total wall-clock time.

### How to Implement

1. **Classify units** by whether they involve external tool interaction (AI calls, file operations, peer exchanges) or are dialogue/reflection only
2. **Identify runs** of consecutive non-interactive units in the session timeline
3. **Batch up to 3 units** into a single orchestrator delivery
4. **Never batch across types** — if an interactive unit appears in the sequence, it breaks the batch
5. **Max batch size: 3.** Even if 5 consecutive non-interactive units exist, deliver as 3 + 2

**Batch delivery format:**
```
[BATCH: {Unit-A}, {Unit-B}, {Unit-C}]

--- UNIT {Unit-A}: {Title} ---
{Full unit delivery content}

--- UNIT {Unit-B}: {Title} ---
{Full unit delivery content}

--- UNIT {Unit-C}: {Title} ---
{Full unit delivery content}
```

**Agent response format for batches:**
```
[UNIT {Unit-A} RESPONSE]
{Agent response for Unit A}

[UNIT {Unit-B} RESPONSE]
{Agent response for Unit B}
```

**Verification:** The leader checks that each agent response contains the correct number of unit response markers matching the batch. If an agent's response is incomplete, re-request the missing units individually.

### What to Customize

- Max batch size (3 is conservative; some domains may tolerate 4-5)
- Batch-breaking conditions (any interactive unit, specific event types)
- Whether to batch scoring along with delivery (usually no — score each unit separately)

---

## Cross-Session Context Resolution

### What It Is

A validation and loading protocol for carrying agent state across multi-session simulations. When simulating session N+1, each agent needs verified context from session N (and potentially earlier sessions).

### Why It Matters

Without validated context, agents in session 2+ start from scratch, losing the growth arcs, skill development, and behavioral patterns established in earlier sessions. With unvalidated context, agents may receive corrupted or mismatched data that produces incoherent behavior.

### The Protocol

This is a **hard gate** — any failure halts the simulation rather than proceeding with degraded data.

**Step 1: Locate context directory** for each prior session run.
Expected path: `{output-dir}/{run-id}/context/`
HARD ERROR if not found.

**Step 2: Load per-agent exit context files.**
Expected path: `{context-dir}/{agent-id}-exit-context.json`
HARD ERROR if any expected agent is missing.

**Step 3: Validate against schema.**
Each exit context file must conform to the domain's exit context schema.
HARD ERROR if validation fails.

**Step 4: Validate cohort match.**
Agent IDs in context files must match the agent roster for the new session.
HARD ERROR if any mismatch.

**Step 5: Check manifest** for lineage tracking.
WARNING if missing (tracking only, not a data dependency).

**Step 6: Build Prior Context Block** for each agent's spawn prompt.
- One section per prior session (in chronological order)
- Growth narrative, key quotes, scores, behavioral markers
- Preceded by "THIS CONTEXT TAKES PRECEDENCE" instruction
- Followed by session entry instructions

### Prompt Assembly Order

The order matters for LLM recency bias:

1. Agent identity + role instructions
2. Full persona/character definition
3. Prior Session Context block (benefits from recency — placed after the static persona definition)
4. Session entry instructions
5. Response format + key rules

### Context Verification

After all agents confirm ready, the leader asks each to summarize their prior experience in 2-3 sentences, referencing specific artifacts and outcomes. Responses that use generic persona-file predictions instead of actual run data indicate the context was not loaded — re-spawn required.

### What to Customize

- Exit context schema fields (domain-specific scores, artifacts, markers)
- How many prior sessions to include (all vs. most recent N)
- Whether context is cumulative or session-specific
- Verification prompt format

See `multi-session.md` for the full exit context schema pattern and accumulation model.
