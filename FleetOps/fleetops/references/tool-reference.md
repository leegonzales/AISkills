# fleetops — Tool Reference

Man-page-style reference for every verb. `<verb> --help` is always authoritative; this doc tracks the current design.

## Global

- Binary: `fleetops` (from `servitor/cmd/fleetops`).
- DB path: `~/.fleetops/fleet.db`; override with `FLEETOPS_DB=<path>`.
- Exit codes: `0` success, `1` runtime error, `2` usage error.
- Most read verbs accept `--json`.

## `init`

Create `~/.fleetops/fleet.db` if it does not exist. Idempotent.

```bash
fleetops init
```

## `harvest`

Pull state and events from upstream sources into `fleet.db`.

```
fleetops harvest [--once | --watch] [--interval 30s] [--source all|servitor|state|fleetmail|journal|knowledge] [--pid-file PATH]
```

- `--once`: single pass, exit.
- `--watch`: daemon mode, polls every `--interval`.
- `--source`: restrict to one upstream.
- `--pid-file`: override the watch lockfile (default `~/.fleetops/watch.pid`).

## `show-state [agent]`

Current snapshot per agent. No argument prints the full table.

```
fleetops show-state [agent] [--raw] [--json]
```

- `--raw`: include `raw_state_json` blob in output.
- `--json`: emit JSON instead of the default table.

## `tail-events`

Recent activity from the event log.

```
fleetops tail-events [--agent X] [--type T] [--source S] [-n N] [-f]
```

- `--agent`: filter by agent name.
- `--type`: filter by event_type (e.g. `heartbeat`, `journal_add`, `ingest_warning`).
- `--source`: filter by source (e.g. `servitor`, `journal`, `fleetmail`).
- `-n`: rows to show (default 50).
- `-f`: follow mode, poll for new events every second.

## `wakes`

Structured wake log from parsed journal stanzas.

```
fleetops wakes [--agent X] [-n | --limit N]
```

Columns: `WAKE_NUM`, `AGENT`, `WAKE_TS`, `SOURCE`, `REASON`.

## `search-knowledge <query>`

FTS5 full-text search across harvested knowledge artifacts (SOPs, katas, doctrine, standards, memory, dreams).

```
fleetops search-knowledge "<query>" [--limit N] [--json] [--raw]
```

- `--limit`: max results (default 20).
- `--json`: JSON output.
- `--raw`: pass query verbatim to FTS5, skip sanitization (for advanced operators).

## `show-artifact <id>`

Print one knowledge artifact by ID.

```
fleetops show-artifact <id>
```

## `journal` subcommands

All `journal` writes require `FLEETOPS_SESSION_ID` and `FLEETOPS_AGENT`. Reads do not.

- `journal add --wake-number N --ts ISO8601 --source <cic|heartbeat|mail|dream|manual> --reason "..." --body-file PATH [--parent-id ID] [--agent NAME]` — insert a stanza. `--parent-id` attaches as continuation.
- `journal update --id N [--reason ...] [--source ...] [--body-file PATH]` — patch a stanza. Authoring session or override only. Tracks audit trail.
- `journal show <id>` — print one stanza (structured fields + body).
- `journal tail [--agent X] [-n N] [--json]` — recent stanzas (default `-n 20`).
- `journal grep "<query>" [--agent X] [--limit N] [--json]` — lexical content search (for semantic, use `cass`).
- `journal render [--agent X] [--out PATH] [--diff PATH]` — render DB as markdown. `--out` writes to file; `--diff PATH` compares DB render against PATH, exit 0 if identical, 1 if drift. The `--diff` form is the authoritative fidelity check for post-migration QC.

## `doctor`

Runtime health probes.

```
fleetops doctor [--check all|heartbeat|zero-ticks|null-sessions] [--json] [--freshness DURATION] [--zero-ticks-n N]
```

Exit 0 all passed (warnings don't fail), exit 1 at least one fail. Failed check names written to stderr.

## `session-stamp [spawn-type]`

Print shell `export` lines to stamp the current shell.

```bash
eval "$(fleetops session-stamp)"            # defaults to cic
eval "$(fleetops session-stamp heartbeat)"  # explicit
```

Valid spawn types: `cic`, `heartbeat`, `mail`, `dream`, `manual`. Unknown values warn to stderr.

Sets `FLEETOPS_SESSION_ID=<new id>` and `FLEETOPS_SPAWN_TYPE=<type>`.

## `list-agents`

Registered agents with last-seen state summary.

```
fleetops list-agents [--json]
```

## `rebuild-state`, `reparse-journals`, `migrate-fleetmail`, `version`

- `rebuild-state [--source ...]` — truncate `current_state`, re-harvest, clear state-hash cursors.
- `reparse-journals` — re-parse `journal_entries` headers into structured wake columns (use after a regex upgrade).
- `migrate-fleetmail [--from PATH] [--dry-run]` — one-shot import of `~/.fleetmail/mail.db` into `fleet.db`'s `mail_*` namespace.
- `version` — print `fleetops <semver>`.
