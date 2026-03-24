# Sand Table Patterns — Reusable Design Recipes

> The patterns are the teacher. The invariant is the test.

Six battle-tested patterns extracted from production sand table implementations. Each pattern is domain-agnostic — customize the specifics for your domain, keep the structural recipe.

---

## Pattern 1: Program Invariant Structure

Every sand table simulation needs a **program invariant** — a single document that enumerates every valid value the simulation can produce. The invariant is the enforcement boundary: anything not listed here is a schema violation.

### What It Is

A structured specification that defines the identity, structure, agents, scoring, and valid enums for a specific simulation domain.

### Why It Matters

LLMs drift. They rename fields, invent enum values, and hallucinate module codes. The invariant gives validators a canonical reference to check against. Without it, drift detection is guesswork.

### Required Sections

**1.1 Identity**
- `domain_id`: Slug used in file paths and output directories
- `domain_name`: Human-readable name
- `session_count`: Number of sessions (1 for single-session simulations)

**1.2 Session Map** (multi-session domains)
For each session:
- Session ID (e.g., `S1`, `S2`)
- Title and duration
- Path to source materials (facilitator guide, script, scenario doc)
- Unit code range (e.g., module `CH01-CH10`, section `SEC01-SEC05`)

**1.3 Unit Enumeration**
Every valid unit code with title and session assignment. This is the hard boundary — any unit code in simulation events that does not appear here is a violation.

**1.4 Agent Roster**
Each agent has:
- `id`: lowercase slug
- `name`: display name
- `role`: archetype or descriptor
- `color`: hex color for replay rendering (optional)
- `file`: path to persona/agent definition file (simulations)

**1.5 Scoring Configuration**
- Dimensions and scale per scoring type
- Pass/flag/fail thresholds
- Aggregate computation method

**1.6 Valid Enum Values**
Exhaustive lists of valid values for every enum field in the event schema. For example, in a training simulation: energy levels, mood states, participant statuses. In a readership simulation: engagement levels, conviction states.

### What to Customize

- Section count and naming conventions
- Scoring dimensions (domain-specific)
- Enum values (audience-specific)
- Agent roster structure (fixed vs. discovered)

---

## Pattern 2: Agent Design Recipes

Multi-agent simulations use three agent roles. The separation of concerns is what makes the simulation valid — a single agent writing all voices produces creative writing, not emergent behavior.

### 2.1 Orchestrator / Facilitator Agent

The orchestrator follows the source material (script, guide, scenario) literally. It delivers content to participant agents, collects responses, and makes adaptation decisions.

**Recipe:**
- Load full source material into the agent's context
- Instruct it to follow the material literally — no improvisation
- Give it adaptation options (scaffolding for struggling participants, extensions for fast finishers)
- Define the communication format for deliveries

**Key principle:** The orchestrator is the intermediary, not the author. It sends structured briefs and receives structured responses.

### 2.2 Persona / Participant Agent

Each participant is an independent agent with its own context window, responding based only on what it receives from the orchestrator.

**Recipe:**
- Load the full persona/character definition
- Instruct it to produce actual artifacts, not summaries ("write the prompt" not "they would write a prompt about...")
- Define the response format: status fields (energy, engagement) + content fields (text, artifact)
- Quality must match the persona's skill level — not the LLM's maximum capability

**Key principle:** Independence is everything. A participant agent has NO access to other participants' responses unless the orchestrator explicitly relays them.

### 2.3 Validator Agent

Runs between simulation and replay generation. Enforces the program invariant.

**Recipe:**
- Load the event schema, drift mappings, and program invariant
- Fix field name drift (rename wrong fields to correct ones)
- Validate IDs against the invariant's enumeration (unit codes, agent IDs)
- Clamp scores to valid ranges
- Compute derived fields (averages, statuses)
- Report what it fixed and what it could not fix

**Key principle:** Fix silently fixable issues, warn on ambiguous issues, error on structural problems. Never invent content.

---

## Pattern 3: Event Schema Design

The event schema defines the structural contract between the simulation and the replay viewer. Design it once per domain, then enforce it with the validator.

### 3.1 Schema Enforcement Layers

Production simulations use three defense layers:

```
Layer 1: Prompt Hardening
  Put a WRONG-to-RIGHT field name table directly in the orchestrator prompt.
  Catches ~80% of drift at generation time.

Layer 2: Validator Agent
  Reads schema + invariant, validates every event post-simulation.
  Catches remaining drift + computes missing derived fields.

Layer 3: Replay Generator Normalization
  Python-level normalization as a belt-and-suspenders final defense.
  Last check before HTML rendering.
```

### 3.2 Known LLM Drift Patterns

These field name substitutions are reliably produced by LLMs across domains. Any simulation using structured events will encounter them:

| LLM Generates | Schema Expects | Why It Happens |
|---------------|----------------|----------------|
| `module_id` / `section_id` / `unit_id` | `module` / `section` / `unit` | Verbose naming — LLMs append `_id` to identifiers |
| `persona_id` / `agent_id` | `persona` / `agent` | Same verbose naming pattern |
| `planned_duration` / `duration_minutes` | `duration_min` | Descriptive expansion of abbreviated fields |
| `from_module` / `to_module` | `from` / `to` | Disambiguation attempt for ambiguous short names |
| `internal` / `thoughts` | `internal_monologue` | Abbreviation of long field names |
| `floor_deployment` / `ceiling_deployment` | `floor` / `ceiling` | Type name expansion — LLM uses the concept name, not the event type |
| `intervention` / `summary` / `response` | `text` | Semantic synonym — LLM picks a more "meaningful" name |
| `timestamp_min` / `time_min` | `time_offset` | Alternative naming for time-within-unit fields |
| `score` / `rating` | `scores` | Singularization of collection fields |
| `participant` / `respondent` | `persona` | Domain-specific synonym for the agent role |

**How to use this table:** Copy it into your domain's `drift-mappings.json` as `field_renames`. Add domain-specific entries as you discover them during initial runs. The first 2-3 runs of any new sand table will surface additional drift patterns — add them to the mappings and re-validate.

---

## Pattern 4: Output Structure

Standardize where simulation artifacts land. This structure works across domains:

```
output/{domain}-{session}-run{N}/
  simulation-events.json      # Validated event stream
  simulation-log.md           # Human-readable narrative log
  scoring-matrix.md           # Score tables
  agent-artifacts/            # Per-agent exercise outputs
    {agent-id}-{unit}.md
    {agent-id}-homework.md    # (if applicable)
  eval-report.md              # Structured evaluation with recommendations
  context/                    # (multi-session only) Exit context for next session
    {agent-id}-exit-context.json

output/{domain}-{session}-replay.html   # Multi-run interactive replay viewer
```

### What to Customize

- Directory naming convention (`{domain}-{session}` or `{domain}-{scenario}`)
- Agent artifact format (markdown, JSON, code files)
- Whether homework/between-session artifacts are captured
- Exit context schema (see `multi-session.md`)

---

## Pattern 5: Creating a New Sand Table

To build a sand table for a new domain:

1. **Read the source materials** — facilitator guides, scenario descriptions, system docs, whatever defines the experience being simulated
2. **Enumerate all units** (modules, sections, stages, rounds) with identifiers and sequence
3. **Define or reuse agents** — many professional simulations share archetypes (the skeptic, the eager adopter, the overwhelmed newcomer, the technical expert)
4. **Map scoring dimensions** — what does "success" look like in this domain? Define dimensions and thresholds
5. **Fill the invariant template** — use `domain-invariant-template.md` as a starting point
6. **Test with a targeted run** — simulate 1-2 units with 2-3 agents to verify paths resolve and events validate before a full run
7. **Build drift mappings** — the first 2-3 runs will reveal domain-specific LLM drift patterns. Capture them in `drift-mappings.json`
8. **Add reliability configuration** — timeout thresholds, abort conditions, narrative integrity checks (see `reliability.md`)

---

## Pattern 6: Multi-Run Comparison

The replay system supports multiple runs of the same scenario. This is where sand tables become diagnostic tools rather than one-off exercises.

### Use Cases

- **Variance analysis:** Do different LLM runs produce consistent scores? Low variance = robust design. High variance = the simulation is sensitive to LLM sampling, not the underlying material.
- **Before/after:** Run before a design change, run after, compare. The delta table shows exactly which units and dimensions changed.
- **Agent spotlight:** Run with the full roster, then run with only specific agents for deeper analysis of particular failure modes.
- **Cross-version:** Run the same agents against v1 and v2 of the source material. Which version produces better scores?

### How It Works

Runs are keyed by `meta.id` + `meta.run` (see `protocol-spec.md`). The replay generator accepts multiple run files and produces tabbed comparison views with delta tables.

### What to Watch For

- Score inflation across runs (the LLM "learns" to score higher — reset agent context between runs)
- Narrative convergence (later runs produce suspiciously similar text — reset all agent state)
- Trajectory matching (scores match the persona's predetermined arc rather than reflecting actual output quality — see `reliability.md` for impossible narrative detection)
