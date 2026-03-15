# Sand Table Protocol — Annotated Examples

Real events from existing implementations. Protocol-level fields are marked with `[P]`, domain-specific fields with `[D]`.

---

## Readership Domain

**Temporal model:** Turn-based
**Source:** `~/Projects/leegonzales/substack/posts/drafts/context-is-ooda_sandtable.json`

### Reader Event

```json
{
  "type": "reader",                    // [P] event type
  "turn": 1,                          // [P] temporal field (turn-based)
  "section": "opening-and-brevity-bias", // [D] which section being read
  "persona": "sanjay",                // [D] agent ID (must exist in agents array)
  "engagement": "high",               // [D] enum: high|medium|low|lost
  "comprehension": "clear",           // [D] enum: clear|partial|confused
  "conviction": "considering",        // [D] enum: convinced|considering|skeptical|resistant
  "mood": "energized",                // [D] enum: energized|neutral|bored|annoyed|excited|curious|impressed|frustrated
  "internal_monologue": "DeepSeek-V3.1 matching GPT-4.1 on AppWorld is a bold claim...",  // [D]
  "highlight": "One rewrite erased 18,160 tokens...",  // [D] pull quote
  "objection": "The opening conflates...",             // [D] nullable
  "would_share": false,               // [D] boolean
  "share_quote": null                 // [D] nullable string
}
```

### Section Scores Event

```json
{
  "type": "section_scores",           // [P] event type
  "turn": 1,                          // [P] temporal field
  "section": "opening-and-brevity-bias", // [D]
  "scores": {                         // [D] scoring object
    "engagement": 4.2,
    "comprehension": 4.0,
    "conviction": 3.5,
    "authority_trust": 3.8,
    "so_what_factor": 3.7,
    "shareability": 3.3
  },
  "flag": "Shareability at 3.3 — only Nate would share at this stage..."  // [D] freeform observation
}
```

**Note:** Readership scores use a 1-5 scale in practice (despite 0.0-1.0 in some docs). The normalizer coerces to float but does not rescale.

---

## Training Domain

**Temporal model:** Bracket-based
**Source:** `~/Projects/leegonzales/AIEnablementTraining/`

### Module Start Event (Bracket Open)

```json
{
  "type": "module_start",             // [P] event type + bracket marker
  "module": "m1",                     // [D] module identifier
  "title": "The AI Landscape Today",  // [D]
  "subtitle": "Where We Actually Are", // [D]
  "duration_min": 15,                 // [D]
  "intensity": "full"                 // [D] enum: full|compressed|skipped
}
```

### Persona Event

```json
{
  "type": "persona",                  // [P] event type
  "module": "m1",                     // [D] current module
  "persona": "jordan",               // [D] agent ID
  "energy": "medium",                // [D] enum: low|medium|high
  "mood": "skeptical",               // [D] enum: anxious|curious|engaged|vulnerable|confident|excited|frustrated|skeptical|relieved
  "status": "building",              // [D] enum: building|stuck|finished|confused|excited|frozen|iterating|helping
  "artifact": null,                   // [D] nullable artifact reference
  "text": "I've heard this pitch before...",  // [D] spoken response
  "internal_monologue": "Let me see if this is actually different..."  // [D]
}
```

### Module Scores Event

```json
{
  "type": "module_scores",            // [P] event type
  "module": "m1",                     // [D]
  "scores": {                         // [D]
    "jordan": 3.5,
    "priya": 4.2,
    "derek": 2.8
  },
  "average": 3.5,                    // [D] computed if missing
  "status": "flag"                   // [D] derived: pass (>=4.0), flag (>=3.0), fail (<3.0)
}
```

### Module End Event (Bracket Close)

```json
{
  "type": "module_end",               // [P] event type + bracket marker
  "module": "m1"                      // [D]
}
```

### Peer Exchange Event

```json
{
  "type": "peer_exchange",            // [P] event type
  "module": "m2",                     // [D]
  "from_persona": "jordan",           // [D] sender agent ID
  "to_persona": "priya",              // [D] receiver agent ID
  "text": "Wait, you're saying that actually worked for your team?"  // [D]
}
```

### Floor/Ceiling Events

```json
{
  "type": "floor",                    // [P] event type
  "module": "m2",                     // [D]
  "persona": "derek",                // [D] who is struggling
  "text": "I don't understand how this applies to my role..."  // [D]
}
```

```json
{
  "type": "ceiling",                  // [P] event type
  "module": "m2",                     // [D]
  "persona": "priya",                // [D] who needs more challenge
  "text": "Can we go deeper on the architecture decisions?"  // [D]
}
```

---

## Agent-Ops Domain

**Temporal model:** Timestamp-based
**Source:** Extracted from Claude Code session logs

### Agent Spawn Event

```json
{
  "type": "agent_spawn",              // [P] event type
  "timestamp": "2026-03-14T10:30:15Z", // [P] temporal field (timestamp-based)
  "agent": "normalize-worker",       // [D] spawned agent name
  "prompt_excerpt": "Read and normalize the drift mappings...",  // [D] first 200 chars
  "background": false                 // [D] whether spawned in background
}
```

### Command Event

```json
{
  "type": "command",                  // [P] event type
  "timestamp": "2026-03-14T10:31:02Z", // [P]
  "command": "python scripts/validate_stream.py test.json",  // [D]
  "exit_code": 0,                     // [D]
  "output_excerpt": "All checks passed (3 events validated)"  // [D] first 500 chars
}
```

### File Change Event

```json
{
  "type": "file_change",              // [P] event type
  "timestamp": "2026-03-14T10:32:00Z", // [P]
  "operation": "write",              // [D] write|edit
  "file_path": "scripts/normalize.py" // [D]
}
```

### Task Event

```json
{
  "type": "task_event",               // [P] event type
  "timestamp": "2026-03-14T10:33:00Z", // [P]
  "action": "create",                // [D] create|update|complete
  "subject": "Implement normalizer",  // [D]
  "status": "in_progress",           // [D]
  "owner": "normalize-worker"        // [D] agent ID
}
```

### Message Event

```json
{
  "type": "message",                  // [P] event type
  "timestamp": "2026-03-14T10:35:00Z", // [P]
  "sender": "normalize-worker",      // [D]
  "recipient": "team-lead",          // [D]
  "content_excerpt": "Normalization complete, 3 fixes applied"  // [D]
}
```

### Error Event

```json
{
  "type": "error",                    // [P] event type
  "timestamp": "2026-03-14T10:36:00Z", // [P]
  "tool": "Bash",                     // [D] which tool errored
  "error_excerpt": "ModuleNotFoundError: No module named 'pandas'"  // [D]
}
```

### Commit Event

```json
{
  "type": "commit",                   // [P] event type
  "timestamp": "2026-03-14T10:40:00Z", // [P]
  "hash": "abc1234",                  // [D]
  "message": "feat: add shared normalizer",  // [D]
  "files_changed": 3                  // [D]
}
```
