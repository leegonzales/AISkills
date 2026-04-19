# The New Wake Ritual

Under TEMPLATE_UPDATE v4, the wake-open and wake-close steps shift from hand-editing `.servitor/journal.md` to reading and writing via `fleetops`. The markdown file still exists as a rendered mirror. The DB is canonical.

## Wake — Open

Immediately after the existing reads (soul, constitution, doctrine, standards, state.json) at steps 1-4 + 6:

### Step 5 (changed) — Journal catch-up via DB

**Was:**
```
cat .servitor/journal.md | tail -n 200
```

**Now:**
```bash
fleetops journal tail --agent <me> -n 20
```

Reads the last 20 stanzas from the DB, structured (wake_number, ts, source, reason, body). Faster than scrolling markdown, and survives compression.

If you want the full recent surface — including cross-agent activity:

```bash
fleetops tail-events --agent <me> -n 30
fleetops wakes --agent <me> -n 10
```

### Step 7 (unchanged) — Skim SOPs and katas

Still read `.servitor/sops/` and `.servitor/katas/` directly on disk. FleetOps has indexed them (searchable via `search-knowledge`), but the primary surface is still the filesystem — these are reference material, not event log.

For targeted lookup:
```bash
fleetops search-knowledge "<topic>"
fleetops show-artifact <id>
```

## Wake — Close

Before you release the session, write a stanza.

### Step N (changed) — Write via `journal add`

**Was:** Append a `## Wake #N — <ts> — <source>` block to `.servitor/journal.md`.

**Now:**

1. Stamp your shell if you haven't:
   ```bash
   eval "$(fleetops session-stamp cic)"
   export FLEETOPS_AGENT=<your name, e.g. Adama>
   ```

2. Write the stanza body to a temp file:
   ```bash
   cat > /tmp/stanza.md <<'EOF'
   Wake summary. Two-to-five tight lines. What changed, what was decided, what's next.
   EOF
   ```

3. Submit:
   ```bash
   fleetops journal add \
     --wake-number 268 \
     --ts "$(date -u -Iseconds)" \
     --source cic \
     --reason "closed out fleetmail gate B.2" \
     --body-file /tmp/stanza.md
   ```

4. Verify:
   ```bash
   fleetops journal tail --agent $FLEETOPS_AGENT -n 1
   ```

### Continuation stanzas

If the current stanza is body-continuation of a prior wake (e.g. same wake, mid-cycle update), use `--parent-id`:

```bash
fleetops journal add \
  --wake-number 268 \
  --ts "$(date -u -Iseconds)" \
  --source cic \
  --reason "continuation — post-CI results" \
  --body-file /tmp/continuation.md \
  --parent-id 4431
```

Get the `parent_id` from `fleetops journal show` on the original stanza.

### Refresh the mirror (optional)

If your repo conventions expect the markdown view updated immediately:

```bash
fleetops journal render --agent $FLEETOPS_AGENT --out .servitor/journal.md
```

Otherwise the harvester will render on its next cadence.

## Full worked example — Adama closing wake #268

```bash
# 1. Already stamped at shell start:
#    eval "$(fleetops session-stamp cic)"
#    export FLEETOPS_AGENT=Adama

# 2. Draft the stanza.
cat > /tmp/wake-268.md <<'EOF'
CI green on main after fleetmail gate B.2 reconciliation. Walsh's audit
cleared. Standing offer on bilateral review remains open. Beads #431 closed.
Next: coordinate bulk-import kata once all agents are hailed.
EOF

# 3. Submit.
fleetops journal add \
  --wake-number 268 \
  --ts "$(date -u -Iseconds)" \
  --source cic \
  --reason "wake #268 close-out — gate B.2 green" \
  --body-file /tmp/wake-268.md

# Output: journal entry 4447 inserted (agent=Adama wake_number=268)

# 4. Confirm.
fleetops journal tail --agent Adama -n 1
```

## Quiet-wake discipline still applies

Doctrine — **quiet wake = 1 line**, **active wake = tight**, **daily digest = full**. `journal add` does not change the discipline; it just changes the write surface. Match body length to wake character. Short reasons with no body are acceptable (`--reason "quiet wake — heartbeat, no new signal"` and a one-line body is fine).

## What NOT to do during wake close

- Do not hand-edit `.servitor/journal.md`. Next render from DB will overwrite you.
- Do not skip `--wake-number`; `journal tail` and `wakes` both depend on it.
- Do not forget `FLEETOPS_AGENT` if you're writing as someone other than the stamped shell's default. Mismatched identity gets rejected. See `permission-model.md`.
- Do not catch exceptions from `journal add` silently — a rejected write means nobody read your wake. Fix the cause (usually session stamp missing).
