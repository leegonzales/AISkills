# Domain Invariant Template

Use this template to define a new sand table domain. Fill in each section, then use it to scaffold a project-local skill.

---

## Identity

```yaml
domain_id: your-domain-slug
name: "Human-Readable Domain Name"
description: "One sentence: what is being simulated or extracted?"
source_type: simulation | extraction
temporal_model: turn | bracket | timestamp
```

---

## Structure

How does the experience divide? Define the units that agents move through.

**Turn-based example (readership):**
```yaml
unit: section
description: "Essay sections read sequentially"
sequence: ordered
```

**Bracket-based example (training):**
```yaml
unit: module
description: "Training modules with start/end markers"
sequence: ordered
brackets:
  start: module_start
  end: module_end
```

**Timestamp-based example (agent-ops):**
```yaml
unit: phase
description: "Development phases detected from time gaps"
sequence: chronological
```

---

## Agent Roster

Define the participants. For simulations, these are synthetic personas. For extractions, they're discovered from logs.

```yaml
agents:
  - id: agent-slug
    name: "Display Name"
    role: "Role or archetype"
    # Add domain-specific fields:
    background: "Optional background/personality description"
    biases: ["Optional list of analytical biases"]
```

**Simulation domains:** Define agents in advance. Each agent gets a durable persona file.

**Extraction domains:** Agents are discovered from source data. List the expected agent types, not specific instances.

---

## Event Types

Define every event type this domain emits. For each type, specify:
- Required fields (beyond `type`)
- Optional fields
- Which fields reference agent IDs

### Template per event type:

```yaml
event_type: event-name
  description: "What this event represents"
  fields:
    - name: field_name
      type: string | int | float | bool | object | array
      required: true | false
      description: "What this field means"
      references_agent: true | false  # Does this field contain an agent ID?
  example:
    type: event-name
    field_name: "example value"
```

### Common field patterns:

| Pattern | Fields | Used In |
|---------|--------|---------|
| Agent action | `persona`/`agent`, action-specific fields | Most simulation events |
| Scores | `scores: { dim: float }`, `average`, `status` | Score/summary events |
| Bracket | no extra fields beyond `type` | `*_start`, `*_end` events |
| Extracted | `tool`, `input`, `output`, `is_error` | Extraction events |

---

## Scoring (Optional)

If the domain produces quantitative assessments, define the dimensions.

```yaml
scoring:
  scale: "0.0-1.0" | "1-5" | "L1-L4" | custom
  dimensions:
    - name: dimension_name
      description: "What this measures"
      thresholds:
        pass: ">= 4.0"
        flag: ">= 3.0"
        fail: "< 3.0"
  aggregate: "average" | "weighted" | "custom"
```

---

## Drift Mappings

Path to the domain-specific `drift-mappings.json` file, or inline the mappings here.

```yaml
drift_mappings: path/to/drift-mappings.json
```

At minimum, define:
- `type_renames`: Wrong event type names the LLM might produce
- `field_renames`: Wrong field names
- `valid_enums`: Valid values for enum fields

For simulation domains, also consider:
- `synonyms`: Value aliases (e.g., `"persuaded"` → `"convinced"`)
- `type_conditional_field_renames`: Field names that are wrong only in specific event types

Extraction domains typically don't need drift mappings (the extractor produces clean events).

---

## Replay Configuration

```yaml
replay:
  generator: path/to/generate_replay.py
  template: path/to/replay_template.html
  injection_placeholder: "{{SIMULATION_DATA}}"
  key_format: "{domain_id}_run{run}"
```

---

## Reliability Configuration

Define how the simulation handles agent failures and validates output integrity.

```yaml
reliability:
  timeout:
    max_retries: 1          # Re-pings before marking NR
    action: "mark_nr"       # mark_nr | skip | abort
  abort:
    nr_agent_threshold: 3   # Agents non-responsive to trigger abort
    consecutive_units: 2    # Consecutive units of NR to trigger abort
  narrative_integrity:
    enabled: true
    warning_threshold: 5    # Warnings before flagging INTEGRITY CONCERN
    signals:                # Which impossible narrative signals to check
      - other_agent_predictions
      - internal_state_knowledge
      - meta_commentary
      - scoring_awareness
      - synchronized_exchanges
```

**Timeout handling:** When an agent fails to respond after the orchestrator's delivery and `max_retries` re-pings, mark as non-responsive. Never fabricate missing data. See `references/reliability.md` for the full protocol.

**Abort rules:** When too many agents are non-responsive, halt the simulation rather than collecting degraded data. Thresholds depend on your agent count — 50% NR is always an abort.

**Narrative integrity:** Post-simulation validation that checks for single-author patterns in multi-agent output. Enable for any simulation using independent agents. See `references/reliability.md` for the five detection signals.

---

## Multi-Session Configuration

For simulations that span multiple sessions, define how agent context carries forward.

```yaml
multi_session:
  enabled: false            # Set true for multi-session domains
  exit_context:
    schema: path/to/exit-context-schema.json
    required_fields:
      - growth_narrative
      - headline_quote
      - behavioral_markers
    max_narrative_length: 1500
  context_loading:
    prior_flag_required: true   # --prior flag is mandatory for session 2+
    validation: strict          # strict (hard errors) | warn (warnings only)
    max_prior_sessions: null    # null = all, or integer to limit
  cohort_matching: strict       # strict | flexible (allows roster changes)
```

**Exit context schema:** Define the JSON schema for per-agent exit context files. See `references/multi-session.md` for a generic template and the AI Foundations training example.

**Context loading:** How prior session data is validated and assembled into agent spawn prompts. Strict mode (recommended) halts on any missing or invalid context.

**Cohort matching:** Whether agent IDs must exactly match across sessions. Strict mode requires all agents present in context files to exist in the current roster. Flexible mode allows roster changes with explicit handling.

See `references/multi-session.md` for the full continuity pattern.

---

## Known Drift Patterns

Reference the common LLM drift patterns from `references/patterns.md` (Pattern 3, Section 3.2) and add domain-specific entries here.

```yaml
drift_notes:
  # Common cross-domain patterns (always include these):
  - "LLMs append _id to identifier fields (module_id → module)"
  - "LLMs expand abbreviated fields (duration_min → planned_duration)"
  - "LLMs substitute semantic synonyms for 'text' (intervention, summary, response)"

  # Domain-specific patterns discovered during initial runs:
  # - "..."
  # - "..."
```

The first 2-3 runs of any new sand table will surface additional drift patterns. Add them to `drift-mappings.json` and re-validate. The known drift table in `references/patterns.md` is a good starting baseline for any domain.

---

## Checklist

Before using this domain invariant:

- [ ] All event types documented with field definitions
- [ ] Agent roster complete (or discovery rules defined for extraction)
- [ ] Drift mappings account for known LLM synonyms and field aliases
- [ ] Scoring dimensions defined (if applicable)
- [ ] At least one example event per type exists in `references/examples.md`
- [ ] Reliability configuration defined (timeout, abort, narrative integrity)
- [ ] Multi-session configuration defined (if applicable)
- [ ] Known drift patterns documented from initial test runs
