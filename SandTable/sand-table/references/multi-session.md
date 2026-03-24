# Multi-Session Simulation Pattern

How to carry agent state across simulation sessions so that session N+1 builds on actual outcomes from session N.

---

## Overview

Single-session simulations are self-contained: agents spawn, simulate, produce events, shut down. Multi-session simulations add a continuity layer: each session produces **exit context** that feeds into the next session's agent spawn prompts.

The chain looks like:

```
Session 1 → Exit Context → Session 2 → Exit Context → Session 3 → ...
```

Each link in the chain is validated before the next session launches. Missing or corrupted context is a hard error, not a graceful degradation.

---

## Exit Context Schema

At the end of each session, produce one exit context file per agent. This file captures everything the agent needs to "remember" for the next session.

### Generic Schema Template

```json
{
  "meta": {
    "agent_id": "string — matches the program invariant roster",
    "agent_name": "string — display name",
    "domain": "string — domain identifier",
    "session": "integer — session number (1-based)",
    "run": "integer — run number within this session",
    "date": "string — ISO 8601 date",
    "cohort": "string — cohort/version identifier"
  },
  "growth_narrative": "string — 2-4 sentences describing this agent's arc through the session",
  "headline_quote": "string — the agent's defining quote from this session",
  "scores": {
    "domain_specific_scoring": "object — whatever scoring your domain uses"
  },
  "behavioral_markers": {
    "engagement_trajectory": "string — overall engagement arc (declining/flat/emerging/accelerating)",
    "energy_exit": "string — energy level at session end",
    "key_moments": ["string — notable moments, breakthroughs, or friction points"],
    "artifacts_produced": ["string — notable outputs from exercises or activities"]
  },
  "facilitator_notes": "string — facilitator observations and carry-forward recommendations"
}
```

### Design Principles

- **Required fields are small.** The meta block, growth narrative, headline quote, and behavioral markers are always required. Domain-specific scores are required when they exist.
- **Narrative over numbers.** The growth narrative and headline quote carry more signal for persona continuity than raw scores. An agent that reads "I spent 20 minutes frozen at a blank screen before finally typing my first prompt" behaves differently than one that reads "engagement: 2.1".
- **Document gaps explicitly.** If homework was not simulated, if scores are partial, if a module was skipped — the `facilitator_notes` field MUST document the gap. The next session's validator checks for completeness.
- **Max length constraints.** Keep text fields bounded (e.g., 1500 chars for narrative, 300 for quote, 500 for notes). Exit context goes into spawn prompts — unbounded text bloats agent context windows.

### Example: Training Domain

The AI Foundations training implementation uses this concrete schema (from `exit-context-schema.json`):

```json
{
  "meta": { "persona_id", "persona_name", "program", "session", "run", "date", "cohort" },
  "growth_narrative": "2-4 sentences from the eval report",
  "headline_quote": "Defining quote from the session",
  "homework_pqe": { "clarity", "context", "specificity", "iteration", "average", "level" },
  "range_scores": { "R", "A", "N", "G", "E" },
  "behavioral_markers": {
    "floor_triggers": "count",
    "ceiling_triggers": "count",
    "engagement_trajectory": "declining|flat|emerging|accelerating",
    "energy_exit": "low|medium|high",
    "resistance_signals": ["notable resistance behaviors"],
    "breakthrough_moments": ["key pivot points"],
    "key_artifacts": ["notable exercise outputs"]
  },
  "convergent_findings": ["cross-persona insights this agent contributed to"],
  "facilitator_notes": "observations + data gap documentation"
}
```

---

## Context Loading for Session N+1

When launching a session that depends on prior session data, the `--prior` flag (or equivalent mechanism) specifies the run chain.

### Prior Flag Pattern

```
Session 2: --prior s1-run5
Session 3: --prior s1-run5,s2-run6
Session 4: --prior s1-run5,s2-run6,s3-run3
```

The flag is REQUIRED for sessions after the first. Omitting it is a hard error.

### Resolution Protocol

See `reliability.md` "Cross-Session Context Resolution" for the full 6-step validation protocol. Summary:

1. Locate context directory for each prior run
2. Load per-agent exit context files
3. Validate against exit context schema
4. Validate cohort match (agent IDs must align)
5. Check manifest for lineage tracking
6. Build Prior Context Block for each agent spawn prompt

Every step except manifest checking is a hard gate.

---

## Context Accumulation Model

Context accumulates across sessions. An agent in session 3 receives context from both session 1 and session 2.

### Assembly Order in Spawn Prompt

```
--- PRIOR SESSION CONTEXT ---
THIS CONTEXT TAKES PRECEDENCE over your persona file's predicted trajectory.
These are your ACTUAL experiences from previous sessions.

=== Session 1 (Run 5, 2026-03-18) ===
Growth: "{growth_narrative from S1}"
Headline: "{headline_quote from S1}"
Scores: {scores from S1}
Key Moments: {behavioral_markers from S1}

=== Session 2 (Run 6, 2026-03-20) ===
Growth: "{growth_narrative from S2}"
Headline: "{headline_quote from S2}"
Scores: {scores from S2}
Key Moments: {behavioral_markers from S2}

--- SESSION ENTRY INSTRUCTIONS ---
You are entering Session 3. Your prior experiences shape how you engage.
Reference specific artifacts and insights from previous sessions in your responses.
```

### Precedence Rule

Prior context (actual run data) always takes precedence over the static persona/character definition. The persona file defines the agent's identity and tendencies; the prior context defines what actually happened. When the two conflict, the prior context wins.

For example, if a persona file predicts "Session 2: begins to warm up to AI" but the Session 1 exit context shows the agent had a breakthrough and is already enthusiastic, the Session 2 agent should build on the actual enthusiasm, not regress to the predicted warming-up state.

---

## Cohort Matching Validation

Before loading context, verify that the agent roster matches across sessions:

- Every agent ID in the exit context files must appear in the current session's roster
- Every agent in the current roster must have a corresponding exit context file (or be explicitly marked as a new addition)
- Agent metadata (name, role) should be consistent across sessions

Mismatches indicate either a roster change between sessions (which must be explicitly handled) or context from the wrong run. Both are hard errors.

---

## Manifest and Lineage

Each run directory should contain a `manifest.json` tracking the full lineage chain:

```json
{
  "run_id": "s2-run6",
  "domain": "your-domain",
  "session": 2,
  "run": 6,
  "date": "2026-03-20",
  "prior_runs": ["s1-run5"],
  "agent_count": 6,
  "status": "complete",
  "context_files": [
    "context/agent-a-exit-context.json",
    "context/agent-b-exit-context.json"
  ]
}
```

The manifest is a tracking aid, not a data dependency. Missing manifests produce a warning, not an error.

---

## What to Customize

| Aspect | Default | Customize When |
|--------|---------|---------------|
| Exit context schema fields | Generic template above | Domain has specific scoring dimensions or artifact types |
| Number of prior sessions loaded | All | Context window constraints force truncation (load most recent N) |
| Precedence rule | Prior context wins over static definition | Domain requires blended behavior |
| Cohort matching strictness | Hard match | Domain allows agent roster changes between sessions |
| Context verification prompt | "Summarize your prior experience in 2-3 sentences" | Domain needs more specific verification |
