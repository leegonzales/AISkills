# Kata: FleetOps Journal Summarize

> **Purpose:** Compress one period of your journal (a month, a week, a themed run of wakes) into a single agent-authored narrative summary. The summary becomes a first-class entry in `fleet.db`; the wakes it covers drop out of the default render but stay in the DB for recall.
> **Rhythm:** Triggered by the compression nudge. The render emits `**N uncompressed wakes** since the last summary` as a footer when your uncompressed-wake count exceeds threshold (default 50). `fleetops journal tail --agent <you>` emits the same signal at the bottom when run with `--agent` pinned.
> **Gating condition:** None — this is a routine hygiene kata. Run it whenever the nudge fires, or proactively when you notice a coherent period has closed (end of a sprint, shipping a feature, closing an incident).

---

## Trigger

1. `fleetops journal render` emits the compression nudge footer
2. `fleetops journal tail --agent <you>` emits `# N uncompressed wakes for <you>`
3. You recognize a coherent period in your recent history that deserves a rollup (e.g., "the March 2026 agent-mail era", "the PR #20-#22 chatloop stabilization run")

## Inputs

- `~/.local/bin/fleetops` with the `journal summarize` verb (v0.1.0-dev or later)
- Your own reading of the period — this is not a mechanical transform; you are writing narrative synthesis

## The core principle

**You are preserving meaning, not metadata.** The wakes stay in `fleet.db` with their full bodies — anyone can recover the details via `fleetops journal show <id>` or `fleetops journal render --full`. Your job in the summary body is to capture what *mattered*: the arcs, the decisions, the resolutions, the patterns a future version of you would want to see at a glance.

Do not write:
> Wakes #86-#90 were cold-start storms. Wakes #91-#98 were routine. Wake #99 was a fleet roster update.

Write:
> **Cold-start storms + production hardening (#86-#113)** — daemon restarts cascaded re-wake loops until the spurious-wake fix shipped on 2026-03-18. Pattern: every restart fired unread-detection against acked mail. Six hardening items closed by end of the period (WaitDelay, lock cap, PID lockfile, shutdown timeout, exp backoff, health file) dropped previous 47.5% failure rate to 0% on the hardened instance.

The first reads like a changelog. The second reads like memory.

## Steps

### 1. Scope one period

Pick an oldest *uncovered* period. Don't try to compress everything at once — a 270-wake backlog compresses into MANY summaries, not one. Coherent unit sizes vary: a month, a week, a themed run. Typical scope: 30–80 wakes.

**Don't skip periods.** The nudge counts *any* wake not covered by a summary, so if you jump from March to January and skip February, February wakes will nudge you again forever. Compress chronologically.

**Don't overlap periods.** Two summaries covering the same days each hide the underlying wakes but render on top of each other — the reader sees redundant rollups. Pick non-overlapping ranges.

### 2. Refresh your memory of the period

```bash
# Date-bounded tail — get the stanzas in the period
~/.local/bin/fleetops journal tail --agent <you> -n 200 \
  | awk -v from="2026-03-01" -v to="2026-03-31" '$5 >= from && $5 <= to'

# Or grep for a theme across the period
~/.local/bin/fleetops journal grep "agent-mail" --agent <you>
~/.local/bin/fleetops journal grep "daemon restart" --agent <you>

# Dig into specific stanzas if you need to remember what happened
~/.local/bin/fleetops journal show 440
```

You're reading for synthesis, not duplication. Sketch on paper if it helps: what were the 3-5 major arcs? What was the texture of the period — was it mostly steady-state, mostly crisis, a ramp from chaos to stability? What decisions were made that will affect future work?

### 3. Write the narrative

Draft in a scratch file:

```bash
cat <<'BODY_EOF' > /tmp/summary-<period>.md
**<One-line title that names the period's character>**

<Opening framing — 1-2 sentences naming the period and its dominant theme.>

Key arcs:

- **<Arc 1 name — wake range>:** <2-3 sentences capturing what happened, why it mattered, and any decision or artifact that persists.>

- **<Arc 2 name — wake range>:** <same.>

- **<Arc N name — wake range>:** <same.>

<Closing paragraph if the period has an arc-level takeaway: a lesson, a shift in how you operate, a piece of doctrine that crystallized.>

Covered wakes: #<start> (YYYY-MM-DD) through #<end> (YYYY-MM-DD). Approximately <N> wakes across <time span>.
BODY_EOF
```

Guidelines:

- **Link arcs to wake ranges.** A reader should be able to reconstruct which concrete wakes fed each arc.
- **Preserve names.** Features shipped, PRs merged, beads issues closed, bugs rootcaused — keep the identifiers so the summary is cross-referenceable.
- **Don't fabricate.** If you can't remember something clearly, `fleetops journal show <id>` it. The fleet.db still has the bodies.
- **Length:** 200-600 words for most periods. Shorter is fine for quiet runs (month of routine heartbeats → one paragraph). Longer is a smell — if you're past 800 words, your period is probably two periods.

### 4. Submit it

```bash
eval "$(~/.local/bin/fleetops session-stamp cic)"
export FLEETOPS_AGENT=<YourAgentName>

~/.local/bin/fleetops journal summarize \
  --agent $FLEETOPS_AGENT \
  --from 2026-03-01 \
  --to 2026-03-31 \
  --reason "March 2026 — <one-line character>" \
  --body-file /tmp/summary-<period>.md
# Stdout: the new summary id (integer)
```

Dates can be ISO 8601 (`2026-03-01T00:00:00Z`) or plain `YYYY-MM-DD`. Date-only `--from` expands to start-of-day; `--to` expands to end-of-day. Both are inclusive.

### 5. Verify the collapse

```bash
~/.local/bin/fleetops journal render --agent $FLEETOPS_AGENT
# Your on-disk .servitor/journal.md now reflects the collapse
```

Open `.servitor/journal.md` and check:

- Your new summary appears as a stanza at its `entry_ts` position in the newest-first timeline (usually near the end of the covered period)
- Below the summary body, there's a `<!-- summary covers ... → ...; hides N entries (ids X…Y) -->` breadcrumb
- The individual wakes from the covered period are gone from the default view
- The compression-nudge footer count is smaller (or gone, if you closed out the threshold)

If any covered wake is STILL showing, it means that wake's `entry_ts` fell outside `[--from, --to]`. Either widen your range with a follow-up `fleetops journal summarize` OR accept that edge wakes stay visible (sometimes correct — an out-of-period wake genuinely doesn't belong to the period you summarized).

### 6. Commit the regenerated journal.md

```bash
git add .servitor/journal.md
git commit -m "chore(journal): compress <period> into summary #<id>"
```

The DB change was made by the CLI already — this commit captures the on-disk projection.

## When to run multiple summaries

If the nudge fires with a count like "115 uncompressed wakes", don't panic-compress all 115 into one summary. Work through your backlog one coherent period at a time:

- Session 1: summarize the oldest month (e.g., March 2026)
- Session 2 (later wake): summarize the next-oldest month (e.g., April 2026 up to the shipping event)
- And so on, until the nudge count falls below threshold

Each summary is independent. You don't need to finish the backlog in one sitting. The nudge is a standing signal, not a deadline.

## Fixing a bad summary

Two failure modes:

**Wrong range.** You covered Feb 1–Feb 15 but meant Feb 1–Feb 28. The covered wakes from Feb 16–28 are still visible; your summary renders at Feb 15. Fix: open a follow-up summary for Feb 16–Feb 28, or — if you want to merge them — delete the row via `sqlite3 ~/.fleetops/fleet.db "DELETE FROM journal_entries WHERE id=<bad-summary-id>"` and re-submit with the correct range. The covered wakes will un-hide when the summary is gone.

**Wrong narrative.** You got the story wrong. Fix: `fleetops journal update <id> --body-file /tmp/corrected.md --tag correction`. The covered wakes stay covered; the body updates; `journal_updated` event carries the before/after hash for forensics.

**Don't silently rewrite.** If you're correcting a summary that was rendered and committed, commit the new render with a message saying what you fixed and why. The history is the history.

## Delegation note

**This kata is NOT a good candidate for subagent delegation.** The value is in *your* synthesis of the period — a subagent writing a mechanical rollup defeats the purpose. The whole point of agent-authored summaries is that an agent's memory is an agent's meaning-making. If you're too drained to write a good summary, skip the kata this wake and do it on a fresher wake.

The exception: if you need to ingest external context to write the summary (reading 50 linked PRs, pulling cass search results), that mechanical ingest CAN be subagent-delegated. You still write the narrative.

## Success criteria

- New `kind=summary` row in `fleet.db` with `covers_from_ts` / `covers_to_ts` populated
- `journal_summary_created` event emitted
- `fleetops journal render` shows the summary at its `entry_ts` position with a breadcrumb listing hidden id range
- Covered wakes absent from default render, present under `fleetops journal render --full`
- `fleetops journal grep <theme>` against covered-wake bodies still returns hits (the FTS index doesn't lose anything)
- `.servitor/journal.md` committed with the new shape

## What this kata does NOT do

- Delete or modify the covered wakes — they stay in `fleet.db`, just hidden from the default view
- Compress across agents — each agent's journal is their own. Cross-agent summaries are a separate (future) primitive.
- Automate the writing — the body is yours. `fleetops journal summarize` takes what you write; it does not generate.

---

*Compression is an act of authorship, not a regex. The kata is small; the skill is in what you choose to remember.*
