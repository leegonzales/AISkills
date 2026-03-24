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

Simulates 6-18 training participants going through coaching modules across a 4-session program. Full multi-agent orchestration with Facilitator, Relay/Observer split, Persona agents, AI tool agents (Tier 3), PQE Scorer, and Validator. The most complex sand table implementation — canonical example for all protocol patterns.

| Attribute | Value |
|-----------|-------|
| **Project** | `~/Projects/leegonzales/AIEnablementTraining/` |
| **Skill** | `skills/sand-table/SKILL.md` |
| **Replay Generator** | `skills/sand-table/replay/generate_replay.py` |
| **Replay Template** | `skills/sand-table/replay/replay_template.html` |
| **Source Type** | Simulation (multi-agent orchestration) |
| **Temporal Model** | Bracket-based (`module_start`/`module_end` pairs) |
| **Execution Tier** | Tier 3 — Real AI agent interaction (personas send prompts to dedicated `-ai` agents, PQE scorer evaluates real conversations) |
| **Event Types** | `module_start`, `module_end`, `facilitator`, `persona`, `floor`, `ceiling`, `module_scores`, `range_scores`, `observation`, `transition`, `peer_exchange`, `homework_start`, `homework_persona`, `homework_end` |
| **Tier 3 Fields** | `prompt_sent`, `ai_response`, `follow_ups`, `pqe_scores`, `range_evidence`, `spoken`, `conversation` |
| **Summary** | Per-module scores, per-persona trajectories, RANGE behavioral scores, PQE evaluator scores |
| **Agent Count** | 18 personas (3 cohort versions: v1 6 personas, v2 6 personas, v3 6 personas; durable files in `personas/`) |
| **Agent Topology** | Up to 15 agents per run: facilitator + 6 personas + 6 AI tool agents + PQE scorer (+ optional relay/observer split) |
| **Drift Mappings** | External: `references/drift-mappings.json` |
| **Multi-Run** | Yes — multi-run tabbed replay via `-r` flags |
| **Multi-Session** | Yes — 4-session program with exit context per persona. `--prior` flag chains runs across sessions. Exit context schema at `references/exit-context-schema.json` |
| **Validator** | Separate validator agent (`agents/sim-events-validator.md`) with impossible narrative detection |
| **Successful Runs** | 8+ runs across S1-S2, including Tier 3 builds with real AI interaction |
| **Key Patterns Originated** | Impossible narrative detection, Tier 3 execution, exit context schema, module batching, cross-session context resolution, known LLM drift catalog |

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
