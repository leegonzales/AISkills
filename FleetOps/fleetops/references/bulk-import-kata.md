# Kata — Bulk Import of `.servitor/journal.md` into `fleet.db`

## When to run this kata

**Run this kata only when Lee hails you in Mattermost to coordinate the migration.** This is an interactive, operator-supervised event — not a heartbeat-triggered task.

- Expected posture: live Mattermost wake session, operator present.
- Adama (the fleet commander servitor) will be co-present during the migration; if anything goes sideways, ping Adama in the coordination channel.
- You run the kata once per agent. After migration, your `.servitor/journal.md` becomes a read-only archive and all future writes go through `fleetops journal add` per the new wake ritual (see `wake-ritual.md`).

Do **not** run this kata on your own initiative. Wait for the hail.

## Why

FleetOps v1 is the new single source of truth for the journal. Your agent's existing `.servitor/journal.md` needs to move into `fleet.db` so that cross-agent queries, structured wake tables, and the new wake ritual all work against a complete history.

The harvester has already done a best-effort regex pass and imported what it could parse. Your LLM comprehension fills in what the regex missed — continuation stanzas, unusual headers, and context the regex couldn't distinguish.

## Preconditions

- `fleetops` binary on PATH (`fleetops version` works).
- `~/.fleetops/fleet.db` initialized and harvester running (`fleetops doctor` reports healthy).
- You have read access to your own `.servitor/journal.md`.
- Lee has hailed you in Mattermost and Adama is available as backstop.

## Kata

### 1. Stamp the session

```bash
eval "$(fleetops session-stamp cic)"
export FLEETOPS_AGENT=<your agent name, e.g. Daystrom>
echo "$FLEETOPS_SESSION_ID $FLEETOPS_SPAWN_TYPE $FLEETOPS_AGENT"
```

Confirm agent name with `fleetops list-agents` if unsure (names are case-sensitive).

### 2. Check what's already imported

```bash
fleetops journal tail --agent $FLEETOPS_AGENT -n 3
```

Expect: a few entries, or none. The harvester's regex may have gotten some stanzas; that's fine — content-hash dedup will skip duplicates on re-insert.

Also sanity-check the current state:

```bash
fleetops wakes --agent $FLEETOPS_AGENT -n 5
```

### 3. Read your journal with comprehension

You are an LLM, not a regex engine. Open `.servitor/journal.md` in your own context and reason over it.

For each stanza, identify:

- **Stanza type** — `## Wake #N`, `## Dream #N`, or other.
- **`wake_number`** — integer.
- **`ts`** — ISO8601 if present; if the stanza has a fuzzy timestamp ("morning, 2026-04-05"), pick the best-effort ISO form (e.g. `2026-04-05T09:00:00Z`) and note the fuzz in the body.
- **`source`** — one of `cic | heartbeat | mail | dream | manual`. Infer from stanza content if the header doesn't state it.
- **`reason`** — one-line summary of why the wake happened.
- **`body`** — everything between this header and the next.
- **Is this a continuation?** If the stanza is a mid-cycle update to a previous wake (same `wake_number` or explicit "continuation" marker), prepare to pass `--parent-id <prior_id>` where `prior_id` is the DB `id` of the parent stanza.

### 4. Insert each stanza

Write body to a temp file (safer than inline for multi-line content):

```bash
cat > /tmp/stanza.md <<'EOF'
<body text here>
EOF

fleetops journal add \
  --wake-number <N> \
  --ts <ISO8601> \
  --source <cic|heartbeat|mail|dream|manual> \
  --reason "<one-line reason>" \
  --body-file /tmp/stanza.md
```

For continuations, add `--parent-id <prior_id>` where `prior_id` came from a prior `journal add` response or `journal tail` lookup.

### 5. Tail-check

After importing all stanzas:

```bash
fleetops journal tail --agent $FLEETOPS_AGENT -n 5
```

Confirm the newest entries match what you expect from the tail of your markdown.

### 6. QC check (required)

```bash
fleetops journal render --agent $FLEETOPS_AGENT --diff .servitor/journal.md
```

- Exit 0 = perfect fidelity between DB render and source markdown. You're done.
- Exit 1 = drift. Read the diff output, investigate, and reconcile before declaring done.

Common drift causes:

- Stanza the regex caught that you also inserted — dedup should have handled it, but if content differs by a character (trailing whitespace, smart-quote normalization), it'll show.
- Continuation stanzas attached with wrong `--parent-id`.
- Timezone differences in `ts` (harvester uses UTC; your source may have local).

### 7. Flip journal.md to archive

Once `--diff` returns 0:

1. Announce in the Mattermost coordination channel: "Migration complete — `<agent>` DB matches markdown, flipping to archive."
2. Wait for Adama's acknowledgment.
3. Going forward, writes go through `fleetops journal add` per `wake-ritual.md`. Your `.servitor/journal.md` is read-only; harvester's periodic `journal render --out` will keep it as a rendered mirror.

## Troubleshooting

### "my `fleetops journal add` is rejected with agent mismatch"

Session was stamped for a different agent. Restamp:
```bash
eval "$(fleetops session-stamp cic)"
export FLEETOPS_AGENT=<your correct name>
```

See `permission-model.md`.

### "I have 200+ stanzas and my context window is struggling"

Split into two sessions. After the first half, run `fleetops journal tail -n 1` to record the highest imported `wake_number`, then start the second session from there. The kata is re-runnable safely — content-hash dedup skips what's already in the DB.

### "`--diff` shows drift I don't understand"

- Write the diff to a file: `fleetops journal render --agent $FLEETOPS_AGENT --diff .servitor/journal.md > /tmp/diff.txt; echo $?`
- Ping Adama in the coordination channel with the diff attached. Do not flip to archive until the drift is reconciled.

### "harvester re-imports something I already added"

Dedup should prevent this. If it doesn't, check content hash:
```bash
fleetops journal tail --agent $FLEETOPS_AGENT --json -n 10 | jq '.[].content_hash'
```

Duplicate hashes indicate a bug — surface to Adama.

### "I'm mid-kata and `fleetops doctor` suddenly fails"

Stop. Do not insert more stanzas. Ping Adama. The harvester may be dying; rebuilding state mid-import can interleave badly.

## Success criteria

- `fleetops journal tail --agent $FLEETOPS_AGENT -n 5` returns your five most recent stanzas, correctly structured.
- `fleetops wakes --agent $FLEETOPS_AGENT -n 10` shows a consistent wake sequence.
- `fleetops journal render --agent $FLEETOPS_AGENT --diff .servitor/journal.md` exits 0.
- You've announced completion in the Mattermost coordination channel and Adama has acknowledged.

so say we all.
