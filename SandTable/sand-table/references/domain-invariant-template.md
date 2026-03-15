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

## Checklist

Before using this domain invariant:

- [ ] All event types documented with field definitions
- [ ] Agent roster complete (or discovery rules defined for extraction)
- [ ] Drift mappings account for known LLM synonyms and field aliases
- [ ] Scoring dimensions defined (if applicable)
- [ ] At least one example event per type exists in `references/examples.md`
