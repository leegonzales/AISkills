# Kata: FleetOps Journal Import

> **Purpose:** One-time migration that lifts your existing `.servitor/journal.md` history into `~/.fleetops/fleet.db`, then re-renders the on-disk file as a projection. After this kata succeeds, `fleet.db` is authoritative; `journal.md` is a rendered view.
> **Rhythm:** Run ONCE per agent, on your next wake after TEMPLATE_UPDATE v5 (the compression-ritual doctrine change) lands. Never re-run — re-running without first wiping your rows in `fleet.db` duplicates every stanza.
> **Gating condition:** Must complete before you write any new journal entries via `fleetops journal add`, or your new entries interleave with un-migrated history and the render breaks coherence.

---

## Trigger

1. TEMPLATE_UPDATE v5 lands (doctrine section "Journal as fleet-db surface" in CLAUDE_SERVITOR.md, which references THIS kata by name)
2. Your next wake reads `journal.md` (step 5 of On Wake) and notices the rendered-by comment is absent — meaning your file is not yet a projection
3. `fleetops journal tail --agent <you>` returns zero rows OR only harvester-ingested rows with empty `wake_number`/`wake_source`

## Inputs

- `~/.local/bin/fleetops` (v0.1.0-dev or later — rebuild from `servitor` main if older)
- `.servitor/journal.md` — your current journal (any shape)
- `.servitor/memory/journal-archive-*.md` — archived periods if you have them (most agents do)

## Pre-flight check

```bash
~/.local/bin/fleetops --version
# Expect: "fleetops 0.1.0-dev" or later

~/.local/bin/fleetops journal tail --agent <YourAgentName> -n 3
# Expect: zero rows OR only rows with dashed (empty) wake_number column.
# If you already see well-formed rows with wake_number/wake_source populated,
# someone has already migrated you — STOP and coordinate with Adama
# before proceeding, or you'll double-insert.
```

## Steps

### 1. Stamp this session

```bash
eval "$(~/.local/bin/fleetops session-stamp cic)"
export FLEETOPS_AGENT=<YourAgentName>
```

The stamp pins every `fleetops journal add` call in this session to your identity. Without it the CLI rejects writes for anyone other than the cwd-derived agent.

### 2. Confirm fleet.db can see you

```bash
~/.local/bin/fleetops show-state $FLEETOPS_AGENT
```

Expect: a table with your `agent_name`, `last_wake_at`, `wake_count`, etc. If you see "agent not found," your agent row needs to be seeded — escalate to Adama.

### 3. Read your existing history

Read in order, oldest first:

```bash
ls .servitor/memory/journal-archive-*.md 2>/dev/null
cat .servitor/journal.md
```

You're looking for **stanzas**: the atomic units of your journal. A stanza is one wake, one dream, one addendum, or one period summary. Typical shapes:

- `## Wake #267 — 2026-04-15 late → 2026-04-16 02:30 MDT — [source: cic] — Reason`
- `## 2026-04-04 — Wake #221: Agent-mail — Spurious Re-wake (13:33 MDT)`
- `## 2026-04-14 — Dream #3 — "The Convergence Pattern"`
- `## Archived Period Milestones (#86-#114)` (aggregated roll-up from old archives)

You are an LLM. Parse by meaning, not regex. Figure out where each stanza starts and ends (next `^## ` heading or `---` horizontal rule). Auto-journal subsections (`### Auto-Journal: ...`) stay INSIDE their parent stanza's body, not as top-level entries.

### 4. For each stanza, extract

- **wake_number** — integer from the header (0 if no number, e.g. dreams or period summaries)
- **ts** — ISO 8601 UTC (if the header gives a date-only, use `YYYY-MM-DDT00:00:00Z` for start-of-day or `23:59:59Z` for end-of-day; if MDT wall-time, add 6h to get UTC)
- **wake_ts** — verbatim human-readable timestamp from the header (for render fidelity)
- **source** — `heartbeat` | `cic` | `mail` | `dream` | `manual`. Infer from the header:
  - "Heartbeat Wake" → `heartbeat`
  - "Agent-mail" → `mail`
  - bare "Wake" or "Active Wake" or "CIC" → `cic`
  - "Dream" → `dream` (and set `--kind dream`)
  - unclear → `manual`
- **reason** — the one-line summary from the header. If no one-line, synthesize from the first sentence of the body
- **body** — full stanza content EXCLUDING the `## ` header line, stripped of leading/trailing whitespace

### 5. Insert one per stanza

```bash
# Write body to a temp file
cat <<'STANZA_EOF' > /tmp/stanza.md
<body text here>
STANZA_EOF

# Insert
~/.local/bin/fleetops journal add \
  --agent $FLEETOPS_AGENT \
  --kind wake \
  --wake-number 267 \
  --ts "2026-04-16T02:30:00Z" \
  --wake-ts "2026-04-15 late → 2026-04-16 02:30 MDT" \
  --source cic \
  --reason "one-line summary" \
  --body-file /tmp/stanza.md
# Stdout: the new entry id (integer)
```

For dreams: `--kind dream` and `--wake-number 0`.
For period summaries (e.g. "Wakes #86-#114"): `--wake-number 0`, `--source manual`, body = the summary text.

On UNIQUE constraint dedup, the CLI silently returns the existing id — don't panic, that's a stanza you already imported (or a real duplicate from your source file). Keep going.

### 6. QC — render and diff against the file you started with

```bash
# First save a copy of your current journal.md so the diff has a fixed target
cp .servitor/journal.md /tmp/pre-import-journal.md

# Now render from fleet.db over the top of journal.md
~/.local/bin/fleetops journal render --agent $FLEETOPS_AGENT

# Compare
diff -u /tmp/pre-import-journal.md .servitor/journal.md | head -100
```

The render WILL NOT byte-match your old file — ordering flips to newest-first, header synthesis kicks in for legacy bare-body entries, and preamble is added. The diff is for your eyes to sanity-check that every wake you see in the old file shows up somewhere in the new one.

Spot-check by wake number: `fleetops journal show <id>` for a handful of recent + middle + oldest wakes. Read the body to confirm fidelity.

### 7. Declare done

```bash
~/.local/bin/fleetops journal tail --agent $FLEETOPS_AGENT -n 3
```

You should see structured rows with `wake_number` and `source` populated. From here forward:

- **Never edit `.servitor/journal.md` directly again.** It's a rendered projection — edits will be overwritten on the next render.
- **Write new entries via `fleetops journal add`.** See CLAUDE_SERVITOR.md §"Journal as fleet-db surface" for the canonical form.
- **Commit the regenerated journal.md.** `git add .servitor/journal.md && git commit -m "chore(journal): migrate to fleetops-rendered projection"` so the on-disk file reflects the new shape.

### 8. Record the migration

Write a journal entry that marks the transition:

```bash
eval "$(~/.local/bin/fleetops session-stamp cic)"
~/.local/bin/fleetops journal add \
  --agent $FLEETOPS_AGENT \
  --kind addendum \
  --wake-number 0 \
  --ts "$(date -u +%Y-%m-%dT%H:%M:%S.000Z)" \
  --source manual \
  --reason "FleetOps journal-import kata complete" \
  --body "Imported <N> stanzas across <M> source files. journal.md is now a rendered projection of fleet.db. Going forward: fleetops journal add/summarize/render."
```

Then re-render so the addendum shows up on disk.

## Common gotchas

- **Mixed timestamps in source files.** Some legacy stanzas use `2026-04-19T15:55:37.982Z`, others use `2026-04-19T15:55:37Z`, others use `2026-04-19`. The CLI canonicalizes on insert — feed what you have, it'll normalize to `.000Z` millisecond form.
- **Spurious re-wake clusters.** You may see runs of near-identical stanzas ("Spurious Re-wake #14, #15, #16..."). These are real history — keep them. Don't try to dedup manually; the content-hash UNIQUE index will collapse literal duplicates automatically.
- **Dream entries.** Use `--kind dream`. They'll render as `## Dream #N` in the header synthesis.
- **Period-summary meta-entries.** Older archive files contain aggregated roll-ups like "Wakes #86-#114: Routine Noops (3 wakes)". Insert these as `--kind wake --wake-number 0 --source manual --reason "Wakes #86-#114 — Routine Noops"`. They're historical summaries, part of your narrative.

## Delegation note (optional)

This kata is mechanical and bounded — N extract-and-insert calls with a single acceptance gate. It's a legitimate candidate for subagent dispatch per doctrine §2.10 ("N ≥ 3 independent artifacts → delegate"). If your journal has >50 stanzas, brief a subagent with this kata's steps + your stanza count, and spawn it in-session to do the bulk work. You review the final render.

## Success criteria

- `fleetops journal tail --agent <you>` returns well-formed rows (non-empty `wake_number` + `source`) for every pre-migration stanza that had those in the header
- `fleetops journal render` produces a `.servitor/journal.md` whose content is the newest-first projection of all your history
- An addendum entry exists documenting the migration
- The regenerated `.servitor/journal.md` is committed to the agent's repo
- No one ever needs to run this kata again for you

## What this kata does NOT do

- Compress old history (that's the `fleetops-journal-summarize` kata, triggered by the render nudge)
- Migrate `state.json`, `memory/`, or any other `.servitor/` file — journal only
- Delete your `.servitor/memory/journal-archive-*.md` files — keep them as a fallback in case a stanza was missed

---

*This kata is load-bearing for the fleet-wide pivot to agent-authored journal state. If it fails in a way you can't debug in under 30m, escalate to Adama rather than improvising — a half-migrated journal is worse than an un-migrated one.*
