# Troubleshooting

Common failure modes when using `fleetops`, what they mean, and how to fix them.

## Write rejected

### "no FLEETOPS_SESSION_ID in environment"

Shell isn't stamped.

```bash
eval "$(fleetops session-stamp cic)"
export FLEETOPS_AGENT=<your name>
```

See `permission-model.md`.

### "agent mismatch"

You passed `--agent X` but the stamped session is for agent Y. Either restamp, or — if this is an operator-supervised migration — accept the warning and proceed. Cross-agent writes during the bulk-import kata are expected.

### "wake_number already exists for this agent"

You're trying to insert a `wake_number` that's already in the DB for this agent.

Cause: (a) harvester already ingested this stanza from `.servitor/journal.md`, or (b) you re-ran the kata and are hitting content-hash dedup.

Fix:
- Check: `fleetops journal tail --agent $FLEETOPS_AGENT -n 5`
- If your content is already there, you're done. Dedup saved you.
- If the content differs, pick a new `wake_number` or use `journal update --id N` to patch.

### "body-file too large"

Stanzas over ~200KB are rejected. Split the body or move verbose content to a file reference and link it.

## `doctor` fails

### `heartbeat` check failing

```
fleetops doctor
check=heartbeat FAIL last_heartbeat_at=2026-04-19T10:14:03Z age=8m (threshold=90s)
```

Harvester hasn't ticked recently.

Diagnosis:
```bash
ps aux | grep 'fleetops harvest'
cat ~/.fleetops/watch.pid
tail -20 ~/.fleetops/harvest.log    # if configured
```

Common causes:
- `harvest --watch` process died; restart it.
- `launchd` service disabled; `launchctl list | grep fleetops`.
- PID file stale from a prior crash.

Fix: restart the harvester. For one-shot catch-up, `fleetops harvest --once` — but don't rely on one-shot in place of the watcher.

### `zero-ticks` failing

Harvester is running but processing zero events on every tick. Probably means all its sources are dead or misconfigured.

```bash
fleetops harvest --once --source servitor    # test one source
fleetops harvest --once --source journal
```

Check that `.servitor/state.json` files are readable and recent. If the fleet genuinely is quiet, bump `--zero-ticks-n` to a larger threshold.

### `null-sessions` failing

`current_state` rows exist with no attached `active_session_id`. Usually benign residue from a crashed daemon. `fleetops rebuild-state --source state` clears it.

## `fleetops` command not found

Binary not on `$PATH`.

```bash
which fleetops
ls ~/go/bin/fleetops || ls /usr/local/bin/fleetops
```

Build from `servitor`:

```bash
cd ~/Projects/leegonzales/servitor
go build -o fleetops ./cmd/fleetops
# then symlink or add to PATH
```

## `fleet.db` missing or corrupt

```
fleetops: open: unable to open database file
```

Create:
```bash
fleetops init
```

If init reports "file already exists but is unreadable":
```bash
sqlite3 ~/.fleetops/fleet.db 'PRAGMA integrity_check'
```

If corrupt, move aside and let harvester rebuild:
```bash
mv ~/.fleetops/fleet.db ~/.fleetops/fleet.db.broken.$(date +%s)
fleetops init
fleetops harvest --once --source all
```

Expect 5-20s per source on a fresh DB.

## Wake_number mismatch between DB and markdown

Symptom: `fleetops wakes --agent Adama -n 5` shows wake_number = 268, but `.servitor/journal.md` shows 271.

Cause: markdown was hand-edited or pre-dates a DB rebuild.

Fix:
```bash
fleetops journal render --agent Adama --diff .servitor/journal.md
```

Exit 0 = no drift, your read of the markdown was wrong. Exit 1 = actual drift — look at the diff and decide which is authoritative. During the bulk-import migration, DB is authority; `render --out .servitor/journal.md` to overwrite.

## `search-knowledge` returns nothing relevant

FTS5 is lexical. "heartbeat autonomy" literally matches both tokens, in any order, in any doc. If you need meaning-based recall, use `cass search --mode semantic`.

For broader FTS:
```bash
fleetops search-knowledge "heartbeat OR autonomy"
fleetops search-knowledge --raw 'heartbeat NEAR/5 autonomy'
```

## Stale, empty, or warning results

- **Stale `show-state`** — harvester content-hash says nothing changed. Fix: `fleetops rebuild-state --source state`.
- **Empty `--json`** — no rows match filters. Sanity-check without filters, then narrow.
- **`ingest_warning` events** — malformed stanza headers. `fleetops tail-events --type ingest_warning --agent $FLEETOPS_AGENT -n 20`, fix the header in the source markdown, then `fleetops reparse-journals`.

## When nothing works

Escalate to Adama (the fleet commander servitor) with:

1. Exact command and stderr output.
2. `fleetops doctor --json` output.
3. `fleetops version`.
4. Relevant `tail-events --type ingest_warning` output.

Don't wildcard-fix — FleetOps is load-bearing infrastructure. Confirm the cause first.
