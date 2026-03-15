# Scout Protocol — 7-Step Repo Scan Checklist

**Purpose:** Standardized checklist for each scout agent to follow per repo. Ensures consistent coverage and event emission.

---

## Per-Repo Steps

### Step 1: Verify Access

Check if the repo path exists and is readable.

- **If not found:** Emit a `repo_missing` event and move to the next repo.
- **If not a git repo:** Note this in a `scan_finding` with `severity: "warn"`.

### Step 2: Read Project Identity

Read in priority order (stop at first found):
1. `CLAUDE.md` — project instructions and context
2. `README.md` — project description
3. `package.json` / `Cargo.toml` / `pyproject.toml` — project metadata

Extract: project purpose, tech stack, key contacts, ecosystem relationships.

### Step 3: Check Recent Activity

```bash
git log --oneline -20
```

Assess:
- **Last commit date** — stale if >30 days
- **Commit frequency** — active if 5+ commits in last 2 weeks
- **Commit authors** — who's working here
- **Commit topics** — what's being worked on

### Step 4: Scan Plan Documents

```bash
ls docs/plans/*.md 2>/dev/null
```

Read any plan docs (skip files in `.worktrees/` paths). Extract:
- Active plans vs. completed vs. stalled
- Blockers mentioned in plans
- Dependencies on other repos

### Step 5: Check Issue Tracker

```bash
bd list --status=open 2>/dev/null
```

If beads is initialized, extract:
- Open issue count and priorities
- Blocked issues (`bd blocked`)
- In-progress work

If beads is NOT initialized, note this as a `scan_finding` with `finding_type: "gap"`.

### Step 6: Classify Repo

Based on steps 2-5, assign one classification:

| Classification | Criteria |
|---------------|----------|
| `active-invest` | Recent commits + open work + serves active goals |
| `maintain` | Working but stable — no active development needed |
| `archive` | Stale (>60 days), no open issues, no goal alignment |

### Step 7: Emit Events

For each repo, emit these events in order:

1. `scan_start` — always (marks beginning)
2. `scan_finding` — one per notable discovery (0 to N)
3. `repo_triage` — always (classification + rationale + proposed beads)

At the end of all repos:
4. `scan_end` — once, after all repos processed

---

## Event Emission Rules

- Use **short repo paths**: `catalyst/coaching` not `~/Projects/catalyst/coaching`
- Set `time_offset` to sequential integers (0, 1, 2...) per repo
- Keep `text` fields concise — 1-2 sentences max
- Include `proposed_beads` only for `active-invest` repos
- Set `severity` accurately: `info` for status, `warn` for staleness/gaps, `high` for risks/deadlines

## Output Format

Write all events to a single JSON file: `scout-{domain}-results.json`

```json
{
  "agent": "scout-{domain}",
  "events": [ ... ]
}
```

The orchestrator merges these into the final `simulation-events.json`.

## Gotchas

- Some repos aren't git repos (e.g., `fitminded`). Still scan them — use `ls` and file dates instead of `git log`.
- Skip `.worktrees/` directories when reading plan docs — those are worktree artifacts, not canonical docs.
- Don't read massive files (>500 lines). Skim CLAUDE.md/README and plan doc headers.
- If `bd` command fails, that's fine — just note "beads not initialized" and continue.
