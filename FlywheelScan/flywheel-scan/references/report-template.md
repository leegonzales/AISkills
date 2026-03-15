# Flywheel Scan Report — {{DATE}}

## Summary

| Metric | Value |
|--------|-------|
| **Repos Scanned** | {{REPO_COUNT}} |
| **Total Events** | {{EVENT_COUNT}} |
| **Agents** | {{AGENT_COUNT}} |
| **Items Scored** | {{SCORED_COUNT}} |
| **Open Threads** | {{THREAD_COUNT}} |

### Team

| Agent | Role | Events |
|-------|------|--------|
{{AGENT_TABLE}}

---

## Triage Summary

| Classification | Count | Repos |
|---------------|:-----:|-------|
| **active-invest** | {{ACTIVE_COUNT}} | {{ACTIVE_REPOS}} |
| **maintain** | {{MAINTAIN_COUNT}} | {{MAINTAIN_REPOS}} |
| **archive** | {{ARCHIVE_COUNT}} | {{ARCHIVE_REPOS}} |

---

## Tier 1: Launch-Critical (Score 17-20)

| Rank | Score | Repo | Title | Energy | Unblocks |
|:----:|:-----:|------|-------|--------|----------|
{{TIER1_TABLE}}

---

## Open Threads — Decisions Needed

{{THREAD_SUMMARIES}}

---

## Top 5 Roadmap Repos

{{ROADMAP_REPOS}}

---

## Key Strategic Observations

{{OBSERVATIONS}}

---

## Files

| File | Description |
|------|------------|
| `simulation-events.json` | {{EVENT_COUNT}} replay events |
| `flywheel-scan-report.md` | This report |
| `master-work-queue.md` | {{SCORED_COUNT}} ranked work items |
| `thread-proposals.md` | {{THREAD_COUNT}} open threads |
| `flywheel-replay.html` | Interactive timeline replay |
{{DIFF_ROW}}
