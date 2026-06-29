---
name: flywheel-scan
description: Cross-project roadmap discovery scan — 4 domain scouts + 1 strategic doppelganger review all repos, score work items, propose thread resolutions, and produce replay HTML.
---

# Flywheel Scan

> **Orchestration:** This pipeline dispatches parallel domain scouts and a strategic doppelganger via the `Agent` tool (`subagent_type: "general-purpose"`). Multiple `Agent` calls issued in a single message run concurrently; use `SendMessage` to coordinate follow-up between agents when needed.

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

### 6. Plan Orchestration Ordering

No team object is created. The pipeline runs in dependency order via direct agent dispatch:
- All scout agents run first (in parallel).
- The doppelganger runs only **after** all scouts complete (it consumes their results).
- Report generation runs after the doppelganger (or after all scouts if `--dry-run`).

### 7. Dispatch Scout Agents

For each active domain, dispatch a scout via the `Agent` tool:

```
Agent(
  subagent_type: "general-purpose",
  name: "scout-{domain}",
  prompt: <scout.md template filled with domain + repo list + event schema + scout protocol>
)
```

**Dispatch all scouts in parallel** — issue one `Agent` call per scout, all in a single
message, so they run concurrently. Each scout writes `scout-{domain}-results.json` in the
output directory.

### 8. Collect Scout Results

After all scouts complete, read their result files. Verify each produced valid JSON with the expected event types. (Use `SendMessage` to a scout only if a result file is missing or malformed and the scout is still resumable.)

### 9. Dispatch Doppelganger (skip if `--dry-run`)

```
Agent(
  subagent_type: "general-purpose",
  name: "lee-doppelganger",
  prompt: <doppelganger.md template filled with all scout results + goals context + scoring rubric + persona schema>
)
```

Doppelganger writes: `doppelganger-results.json` in the output directory.

### 10. Assemble simulation-events.json

Merge all agent result files into canonical format:

```json
{
  "session": { "id": "flywheel-scan", "title": "Cross-Project Roadmap Discovery", "date": "{date}" },
  "agents": [ ... ],
  "events": [ ... all events merged in time_offset order ... ]
}
```

Write to `simulation-events.json` in the output directory.

### 11. Run Validator

Dispatch the scan-validator agent (via the `Agent` tool) to fix schema drift:

```
Agent(
  subagent_type: "general-purpose",
  name: "scan-validator",
  prompt: <scan-validator.md + path to simulation-events.json + drift-mappings.json>
)
```

Review fix count. >20 fixes = scout prompts need hardening.

### 12. Generate Reports (skip if `--dry-run`)

Using the report templates, generate:
- `flywheel-scan-report.md` — executive summary
- `master-work-queue.md` — ranked work items by tier
- `thread-proposals.md` — open decision threads with options

### 13. Generate Replay

```bash
python {skill_dir}/replay/generate_replay.py {output_dir}
```

Produces `flywheel-replay.html` — self-contained, opens in browser.

### 14. Diff Against Previous Scan

If a previous scan exists (auto-detected or from config):

```bash
python {skill_dir}/scripts/diff_scans.py {previous_dir} {current_dir}
```

Produces `scan-diff-report.md` in the output directory.

### 15. Report to User

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
