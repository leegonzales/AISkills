# Sand Table Implementations Registry

Known sand table implementations and where they live.

---

## Substack Readership

Simulates 6 reader personas experiencing an essay section-by-section.

| Attribute | Value |
|-----------|-------|
| **Project** | `~/Projects/leegonzales/substack/` |
| **Skill** | `.claude/skills/sand-table.md` |
| **Replay Generator** | `tools/sandtable-replay/generate_sandtable_replay.py` |
| **Replay Template** | `tools/sandtable-replay/replay_template.html` |
| **Source Type** | Simulation (LLM-generated) |
| **Temporal Model** | Turn-based (`turn: int`) |
| **Event Types** | `reader`, `section_scores` |
| **Summary** | `session_summary` with per-persona trajectories and delta tables |
| **Agent Count** | 6 fixed personas (topic-adapted names) |
| **Drift Mappings** | Inline in generator (conviction synonyms, enum sets) |
| **Multi-Run** | Yes — Run 2 compares against Run 1 with `delta_table` |

---

## AIEnablement Training

Simulates 6-12 training participants going through coaching modules. Full multi-agent orchestration with Facilitator, Persona agents, and Validator.

| Attribute | Value |
|-----------|-------|
| **Project** | `~/Projects/leegonzales/AIEnablementTraining/` |
| **Skill** | `skills/sand-table/SKILL.md` |
| **Replay Generator** | `skills/sand-table/replay/generate_replay.py` |
| **Replay Template** | `skills/sand-table/replay/replay_template.html` |
| **Source Type** | Simulation (multi-agent orchestration) |
| **Temporal Model** | Bracket-based (`module_start`/`module_end` pairs) |
| **Event Types** | `module_start`, `module_end`, `facilitator`, `persona`, `floor`, `ceiling`, `module_scores`, `range_scores`, `observation`, `transition`, `peer_exchange`, `homework_start`, `homework_persona`, `homework_end` |
| **Summary** | Per-module scores, per-persona trajectories, range scores |
| **Agent Count** | 6-12 personas (durable files in `personas/`) |
| **Drift Mappings** | External: `references/drift-mappings.json` |
| **Multi-Run** | Yes — multi-run tabbed replay via `-r` flags |
| **Validator** | Separate validator agent (`agents/sim-events-validator.md`) |

---

## Agent-Ops (BuildTimeline)

Extracts development activity from Claude Code session logs into protocol-compliant event streams.

| Attribute | Value |
|-----------|-------|
| **Project** | `~/Projects/leegonzales/AISkills/BuildTimeline/build-timeline/` |
| **Skill** | `SKILL.md` |
| **Extractor** | `SandTable/sand-table/scripts/extract_agent_ops.py` (shared) |
| **Source Type** | Extraction (real session logs) |
| **Temporal Model** | Timestamp-based (`timestamp: ISO string`) |
| **Event Types** | `agent_spawn`, `message`, `task_event`, `command`, `file_change`, `error`, `commit` |
| **Agent Count** | Dynamic (discovered from session logs) |
| **Drift Mappings** | N/A (extraction produces clean events) |
| **Multi-Run** | No (each extraction is a single run) |

---

## Adding a New Implementation

1. Design the domain using `references/domain-invariant-template.md`
2. Create a project-local skill following the scaffold pattern
3. Register it here with the table format above
4. Optionally add a `manifest.json` to the project (see `templates/manifest.json`)
