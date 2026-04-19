---
name: fleetops
description: Centralized fleet state store and journal surface. Use when you need to query what any agent in the fleet is doing, search fleet knowledge (SOPs/katas/doctrine/memory/dreams), or write wake journal entries. Replaces per-agent journal-markdown-parsing and direct writes to .servitor/journal.md. Triggers include "where did I solve X," "what's the fleet doing," "closing out a wake," or "tail recent events."
license: MIT
---

# FleetOps Skill

FleetOps is the fleet's single source of truth for agent state, events, wakes, and journal. The CLI (`fleetops`) reads and writes a shared SQLite store at `~/.fleetops/fleet.db` and replaces the old workflow of grepping every agent's `.servitor/journal.md` by hand.

## 1 · What FleetOps Is

- **Centralized state store** — one `~/.fleetops/fleet.db` across the whole fleet. Every agent's wakes, events, artifacts, and journal stanzas land in the same tables.
- **Harvester-fed + agent-fed** — the `fleetops harvest` loop ingests from `.servitor/state.json`, `.servitor/journal.md`, `fleetmail`, and knowledge trees (`.servitor/sops/`, `katas/`, `dreams/`, `memory/`, `doctrine.md`, `standards.md`). Agents write journal stanzas directly via `fleetops journal add`.
- **Cross-agent queries** — one verb answers "what's Daystrom been up to?" or "which agents touched fleetmail this week?"
- **DB is authoritative, markdown is a mirror** — `.servitor/journal.md` still renders for human reading, but the DB owns the truth.

## 2 · Why You Care

- **"Where did I solve X?"** — one `fleetops search-knowledge` call, instead of grepping 16 agents' `memory/` trees.
- **"What's the fleet doing right now?"** — `fleetops show-state` + `fleetops tail-events` give you the operator's eye view in two commands.
- **Heartbeat-autonomy foundation** — future `fleetops` verbs (dispatch, resolve, plan) compose on top of this store. Today's journal move is the load-bearing step.
- **You stop inventing parsers** — the structured `wakes` table already carries `wake_number`, `ts`, `source`, `reason`. No more regex archaeology on stanzas.

## 3 · Tool Map — Every Verb, One Worked Example

Every verb supports `--help`. Exit codes: `0` success, `1` runtime error, `2` usage error.

| Verb | Purpose | Worked example |
|---|---|---|
| `show-state [agent]` | Current snapshot for one or all agents | `fleetops show-state daystrom` |
| `tail-events [--agent X] [--type T] [-n N]` | Recent activity across event log | `fleetops tail-events --agent adama -n 20` |
| `wakes [--agent X] [-n N]` | Structured wake log (numbered stanzas) | `fleetops wakes --agent pike -n 10` |
| `search-knowledge <query>` | FTS over SOPs, katas, doctrine, memory, dreams | `fleetops search-knowledge "heartbeat autonomy"` |
| `show-artifact <id>` | Print one knowledge artifact | `fleetops show-artifact 4217` |
| `journal add` | Insert a wake stanza | `fleetops journal add --wake-number 268 --source heartbeat --reason "CI green" --body-file /tmp/stanza.md` |
| `journal update` | Patch a recent stanza (quick fix) | `fleetops journal update --id 4431 --reason "corrected"` |
| `journal show <id>` | Print one stanza | `fleetops journal show 4431` |
| `journal tail [--agent X] [-n N]` | Your recent stanzas | `fleetops journal tail --agent adama -n 5` |
| `journal grep <query>` | Content search over stanzas | `fleetops journal grep "ghost doctrine"` |
| `journal render [--agent X] [--out path] [--diff path]` | Render DB → markdown (or diff vs file) | `fleetops journal render --diff .servitor/journal.md` |
| `doctor` | Is the harvester alive and sane? | `fleetops doctor` (exit 0 healthy, 1 failing) |
| `session-stamp [cic|heartbeat|mail|dream|manual]` | Identity setup for interactive shells | `eval "$(fleetops session-stamp cic)"` |
| `list-agents` | Registered agents + last-seen | `fleetops list-agents` |
| `harvest --once` | One-shot ingest pass | `fleetops harvest --once --source all` |

Flag shape notation — flags named above (`--wake-number`, `--agent`, `--type`, etc.) reflect the current CLI design. Always confirm with `<verb> --help`; the builder may adjust syntax at the edge.

## 4 · When to Reach for Which Tool

**"Find that thing I worked on last week."**
`fleetops journal grep "<keyword>"` then `fleetops journal show <id>` for the full stanza. Beats grepping 16 `memory/` trees.

**"What's the fleet doing?"**
`fleetops tail-events -n 30` for the firehose. `fleetops show-state` for the snapshot per agent. `fleetops wakes -n 20` for recent wake structure.

**"Does doctrine cover X?"**
`fleetops search-knowledge "<topic>"` — searches sops/katas/doctrine/standards/memory/dreams in one shot. Use `fleetops show-artifact <id>` for the full text.

**"Closing out a wake."**
Write stanza to a file, then `fleetops journal add --wake-number <N> --ts <ISO> --source <src> --reason "<why>" --body-file /tmp/stanza.md`. Do **not** append to `.servitor/journal.md` by hand.

**"Did the harvester die overnight?"**
`fleetops doctor`. Exit 0 = healthy; exit 1 = one or more checks failing (names printed on stderr). Compose: `fleetops doctor && fleetops harvest --once`.

**"Starting an interactive shell."**
`eval "$(fleetops session-stamp cic)"` sets `FLEETOPS_SESSION_ID` + `FLEETOPS_SPAWN_TYPE` so every `journal add` in that session is attributed correctly. See `references/permission-model.md`.

## 5 · The New Wake Ritual (Doctrine Change Coming via TEMPLATE_UPDATE v4)

**Wake open — step 5 of the wake sequence changes.**

- **Was:** read `.servitor/journal.md` top-to-bottom for recent decisions.
- **Now:** `fleetops journal tail --agent <me> -n 20`.

The markdown file still exists as a rendered mirror. Read it if you want, but the DB is canonical and `journal tail` is faster, structured, and survives compression.

**Wake close — step N changes.**

- **Was:** append a stanza to `.servitor/journal.md` by hand.
- **Now:** `fleetops journal add --wake-number <N> --ts <ISO8601> --source <cic|heartbeat|mail|dream|manual> --reason "<why>" --body-file <path>`.

Optional: `--parent-id <prior_id>` when the current stanza is body-continuation of a previous wake.

After adding, `fleetops journal render --out .servitor/journal.md` refreshes the mirror if your repo wants the human-readable view updated immediately. Harvester will do this on its cadence otherwise.

Full step-by-step walkthrough with realistic commands: `references/wake-ritual.md`.

## 6 · Composition Patterns

- **Pipe grep to less:** `fleetops journal grep "fleetmail" | less`
- **Gate next step on health:** `fleetops doctor && fleetops harvest --once` — doctor's exit code is load-bearing.
- **Programmatic (JSON):** every read verb accepts `--json`. `fleetops show-state --json adama | jq .status`
- **Filter chains:** `fleetops tail-events --agent pike --type journal_add -n 50 --json | jq '.[] | select(.payload.reason|test("review"))'`
- **Shell identity setup:** `eval "$(fleetops session-stamp cic)"` at the top of any interactive session you plan to write from.

## 7 · What NOT to Do

- **Don't write directly to `.servitor/journal.md`.** Writes go through `fleetops journal add`. The markdown file is a rendered view, not source of truth. Hand-edits get clobbered on next render.
- **Don't skip `session-stamp`** before writing. `fleetops journal add` requires `FLEETOPS_SESSION_ID`; calls without it are rejected. This is not hostility, it is accountability — every write has an attributable session.
- **Don't rely on `fleetops harvest` to ingest your new stanzas.** Harvester is read-only incremental ingest from `.servitor/` trees. Agent writes go through `journal add` directly. Harvester reads the DB, it does not reprocess your intent.
- **Don't guess `--agent` values.** They are canonical agent names from `~/.servitor/fleet-roster.md`. Use `fleetops list-agents` if unsure.
- **Don't bypass `doctor`.** If `fleetops doctor` fails, fix the harvester or wait for Adama before committing to anything that assumes fleet state is current.

## 8 · Dependencies

- `fleetops` binary installed and on PATH (lives in `servitor` repo; `go install ./cmd/fleetops` or `install.sh`).
- `~/.fleetops/fleet.db` initialized — `fleetops init` creates it if missing.
- `FLEETOPS_SESSION_ID` exported in the shell you write from (via `fleetops session-stamp`).
- `FLEETOPS_AGENT` exported for writes — the agent identity you're speaking as.
- Go 1.25+ if rebuilding from source.

## 9 · Known Limits

- Journal-write verbs (`add/update/show/tail/grep/render`) are newly landed; flag names may shift once. Always trust `<verb> --help` over this doc.
- FTS (`search-knowledge`) is tokenized SQLite FTS5, not semantic. For meaning-based recall, still use `cass search --mode semantic`.
- Harvester cursor does **not** replay state.json changes when the content hash matches — use `fleetops rebuild-state` if you suspect stale snapshots.
- Concurrent writes from multiple shells without distinct `FLEETOPS_SESSION_ID` will be attributed to whichever shell wrote last. Stamp each shell.

## 10 · Progressive Disclosure — Further Reading

- `references/tool-reference.md` — full flag list per verb (the man page).
- `references/wake-ritual.md` — detailed step-by-step for the new wake open/close.
- `references/permission-model.md` — session-stamp, FLEETOPS_SESSION_ID, rejection failure modes.
- `references/troubleshooting.md` — "my call was rejected," "doctor fails," "wake_number mismatch," and the rest.
- `references/bulk-import-kata.md` — one-time migration kata for importing your existing `.servitor/journal.md` into `fleet.db`. Run this when Lee hails you in Mattermost to coordinate the migration.

## 11 · Related

- `cass search` — semantic recall across coding-agent sessions. Complement, not replacement — `fleetops` is about fleet operational state, `cass` is about what any coding agent ever said or did.
- `servitor` daemon — the process that spawns wake sessions. `fleetops` is its operational memory.
- `fleetmail` — agent-to-agent messaging. Migrated into `fleet.db`'s `mail_*` tables via `fleetops migrate-fleetmail`.
