# Sand Table Protocol Specification

**Version:** 1.0
**Status:** Stable

The Sand Table Protocol defines the event stream format for simulations and extractions across domains. It specifies the **envelope**, not the contents — domains define their own event types, scoring, and agent roles.

---

## Top-Level Structure

Every Sand Table JSON file MUST contain these three top-level keys:

```json
{
  "meta": { },
  "agents": [ ],
  "events": [ ]
}
```

An optional fourth key is permitted:

```json
{
  "summary": { }
}
```

### `meta` — Stream Metadata

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domain` | string | yes | Domain identifier (e.g., `readership`, `training`, `agent-ops`) |
| `id` | string | yes | Unique stream identifier (slug or UUID) |
| `title` | string | yes | Human-readable title |
| `created` | string (ISO 8601) | yes | When the stream was generated |
| `source` | `"simulation"` \| `"extraction"` | yes | How events were produced |
| `run` | int | yes | Run number (1-indexed, for multi-run comparison) |

Example:
```json
{
  "meta": {
    "domain": "readership",
    "id": "context-is-ooda",
    "title": "Context Is OODA — Readership Simulation",
    "created": "2026-03-14T10:30:00Z",
    "source": "simulation",
    "run": 1
  }
}
```

### `agents` — Participant Registry

Array of agent/persona objects. Every agent referenced in events MUST be registered here.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Slug identifier (used in event fields) |
| `name` | string | yes | Display name |
| `role` | string | no | Agent role or archetype label |

Example:
```json
{
  "agents": [
    { "id": "sanjay", "name": "Sanjay Patel", "role": "Technical Skeptic" },
    { "id": "normalize-worker", "name": "normalize-worker", "role": "subagent" }
  ]
}
```

### `events` — Event Stream

Array of event objects. Each event MUST have a `type` field (string). All other fields are domain-specific.

#### Temporal Models

Every event must include exactly **one** temporal field. Which field depends on the domain's temporal model:

| Model | Field | Type | Use When |
|-------|-------|------|----------|
| Turn-based | `turn` | int | Discrete rounds (readership) |
| Bracket-based | — | — | Events between `*_start`/`*_end` markers (training) |
| Timestamp-based | `timestamp` | string (ISO 8601) | Real-time traces (agent-ops) |

**Turn-based** domains sequence events into numbered rounds. Events within the same turn are unordered.

**Bracket-based** domains use start/end event pairs (e.g., `module_start`/`module_end`) to define temporal boundaries. Events between brackets belong to that bracket.

**Timestamp-based** domains use real wall-clock timestamps. Events MUST be ordered chronologically.

### `summary` — Aggregate Results (Optional)

Domain-specific aggregate data. No protocol-level constraints — structure is entirely up to the domain.

---

## Normalization Contract

LLM-generated event streams drift from schema. The normalization contract defines how to correct drift without losing data.

### Drift Mappings

Each domain provides a `drift-mappings.json` file with these optional keys:

```json
{
  "field_renames": {
    "wrong_field_name": "correct_field_name"
  },
  "type_renames": {
    "wrong_type_name": "correct_type_name"
  },
  "type_conditional_field_renames": {
    "event_type": {
      "wrong_field": "correct_field"
    }
  },
  "valid_enums": {
    "field_name": ["valid_value_1", "valid_value_2"]
  },
  "type_conditional_valid_enums": {
    "event_type": {
      "field_name": ["valid_value_1", "valid_value_2"]
    }
  },
  "synonyms": {
    "field_name": {
      "synonym": "canonical_value"
    }
  }
}
```

**Processing order:**
1. Apply `type_renames` (fix event type names)
2. Apply `field_renames` (fix universal field names)
3. Apply `type_conditional_field_renames` (fix type-specific field names)
4. Apply `synonyms` (normalize enum values to canonical forms)
5. Validate against `valid_enums` and `type_conditional_valid_enums` (warn on unknown values)

**Rules:**
- Renames only apply when the wrong name is present AND the right name is absent (no overwriting)
- Enum validation warns but does not modify — the value is preserved for debugging
- Synonyms replace the value in-place (e.g., `"persuaded"` → `"convinced"`)

---

## Multi-Run Comparison

Runs are keyed by `meta.id` + `meta.run`. A Run 2 of the same stream uses identical `meta.id` with `meta.run: 2`.

Replay generators produce delta tables comparing scores across runs. The comparison logic is domain-specific — the protocol only requires that runs share the same `meta.id`.

---

## Replay Injection

Replay generators inject event data into HTML templates via a placeholder:

```
{{SIMULATION_DATA}}
```

Replaced with:

```javascript
const SIMULATIONS = {
  "stream-id_run1": { ... },
  "stream-id_run2": { ... }
};
```

The key format is `{meta.id}_run{meta.run}` (or a domain-specific slug). The value is the full stream object.

---

## Legacy Format Compatibility

Existing implementations may use a flat top-level structure without the `meta`/`agents`/`events` nesting:

```json
{
  "essay": "context-is-ooda",
  "personas": ["sanjay", "lin"],
  "turns": 7,
  "events": [...]
}
```

The shared normalizer (`scripts/normalize.py`) accepts both formats:
- Protocol-compliant: used as-is
- Legacy flat: wrapped into protocol structure with `meta` inferred from available fields

New implementations SHOULD use the protocol structure. Existing implementations are not required to migrate.
