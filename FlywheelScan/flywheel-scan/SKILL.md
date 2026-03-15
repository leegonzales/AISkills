---
name: flywheel-scan
description: Cross-project roadmap discovery scan — 4 domain scouts + 1 strategic doppelganger review all repos, score work items, propose thread resolutions, and produce replay HTML.
---

# Flywheel Scan

## Invocation

```
Skill(skill: "flywheel-scan")                          # Full scan (default)
Skill(skill: "flywheel-scan", args: "--mode quick")    # Active-invest repos only
Skill(skill: "flywheel-scan", args: "--domain biz")    # Single domain
Skill(skill: "flywheel-scan", args: "--mode diff")     # Only repos with git activity since last scan
Skill(skill: "flywheel-scan", args: "--dry-run")       # Scouts only, no doppelganger scoring
```

## Steps

### 1. Parse Arguments

Extract from `args`:
- `--mode`: `full` (default) | `quick` | `diff` | `dry-run`
- `--domain`: `biz` | `training` | `tooling` | `personal` (default: all)
- `--date`: override scan date (default: today)

### 2. Load Config & References

```
Read config/scan-config.yaml           → repo assignments, scoring config, external paths
Read references/event-schema.md        → event type definitions
Read references/scoring-rubric.md      → 4 scoring dimensions
Read references/drift-mappings.json    → canonical field rename table (SINGLE SOURCE OF TRUTH)
Read references/scout-protocol.md      → 7-step repo scan checklist
Read references/doppelganger-protocol.md → strategic review protocol
```

### 3. Resolve Mode Filters

| Mode | Repos scanned | Doppelganger | Reports |
|------|--------------|--------------|---------|
| `full` | All repos in config | Yes | All |
| `quick` | Only repos classified `active-invest` in previous scan | Yes | All |
| `diff` | Only repos with `git log --since` activity since last scan | Yes | All |
| `dry-run` | Per domain/all | **No** | Events JSON only |

For `--domain`, filter to only that scout's repo list.

### 4. Create Output Directory

```bash
mkdir -p {output_base}/flywheel-scan-{date}
```

Where `{output_base}` comes from `config/scan-config.yaml`.

### 5. Load Goals Graph

```bash
python {goals_query_path} status
python {goals_query_path} threads
python {goals_query_path} tensions
```

Save combined output as `goals-context.md` in the output directory. This feeds the doppelganger.

### 6. Create Team

```
TeamCreate(team_name: "flywheel-scan-{date}")
```

### 7. Create Tasks

One task per active scout domain + doppelganger review + report generation. Set dependencies:
- Doppelganger task is `blockedBy` all scout tasks
- Report generation is `blockedBy` doppelganger task (or all scouts if `--dry-run`)

### 8. Spawn Scout Agents

For each active domain, spawn a scout agent using `Task` tool:

```
Task(
  subagent_type: "general-purpose",
  team_name: "flywheel-scan-{date}",
  name: "scout-{domain}",
  prompt: <scout.md template filled with domain + repo list + event schema + scout protocol>
)
```

**Spawn all scouts in parallel** (one Task call per scout, all in same message).

Each scout writes: `scout-{domain}-results.json` in the output directory.

### 9. Collect Scout Results

After all scouts complete, read their result files. Verify each produced valid JSON with the expected event types.

### 10. Spawn Doppelganger (skip if `--dry-run`)

```
Task(
  subagent_type: "general-purpose",
  team_name: "flywheel-scan-{date}",
  name: "lee-doppelganger",
  prompt: <doppelganger.md template filled with all scout results + goals context + scoring rubric + persona schema>
)
```

Doppelganger writes: `doppelganger-results.json` in the output directory.

### 11. Assemble simulation-events.json

Merge all agent result files into canonical format:

```json
{
  "session": { "id": "flywheel-scan", "title": "Cross-Project Roadmap Discovery", "date": "{date}" },
  "agents": [ ... ],
  "events": [ ... all events merged in time_offset order ... ]
}
```

Write to `simulation-events.json` in the output directory.

### 12. Run Validator

Spawn the scan-validator agent to fix schema drift:

```
Task(
  subagent_type: "general-purpose",
  name: "scan-validator",
  prompt: <scan-validator.md + path to simulation-events.json + drift-mappings.json>
)
```

Review fix count. >20 fixes = scout prompts need hardening.

### 13. Generate Reports (skip if `--dry-run`)

Using the report templates, generate:
- `flywheel-scan-report.md` — executive summary
- `master-work-queue.md` — ranked work items by tier
- `thread-proposals.md` — open decision threads with options

### 14. Generate Replay

```bash
python {skill_dir}/replay/generate_replay.py {output_dir}
```

Produces `flywheel-replay.html` — self-contained, opens in browser.

### 15. Diff Against Previous Scan

If a previous scan exists (auto-detected or from config):

```bash
python {skill_dir}/scripts/diff_scans.py {previous_dir} {current_dir}
```

Produces `scan-diff-report.md` in the output directory.

### 16. Shutdown Team

Send shutdown messages to all agents. Then `TeamDelete()`.

### 17. Report to User

Present:
- **Verdict:** repos scanned, events generated, items scored
- **Top 5 work items** with scores
- **Thread decisions needed** (count + titles)
- **Classification changes** from previous scan (if diff ran)
- **File locations:** output directory, replay HTML, reports

## Cost Notes

Full scan with 5+ agents is expensive. Preferred approach:
1. **First run:** `--dry-run --domain biz` to verify scout communication
2. **Weekly cadence:** `--mode diff` to catch only changed repos
3. **Monthly cadence:** `--mode full` for complete baseline

## FMEA

| Failure | Recovery |
|---------|----------|
| Scout can't access repo (not cloned) | Emit `repo_missing` event, continue |
| Doppelganger context too large | Summarize scout findings before passing |
| goals_query.py fails | Proceed without goals context, flag in report |
| Validator finds >20 drift fixes | Complete scan but flag prompt hardening needed |
| Previous scan not found for diff | Skip diff step, note in report |
