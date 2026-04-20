# FleetOps

**Centralized fleet state store and journal surface — SQLite-backed, CLI-first.**

## Purpose

FleetOps is the fleet's single source of truth for agent state, events, wakes, and journal stanzas. One shared SQLite database at `~/.fleetops/fleet.db` replaces the old workflow of parsing sixteen agents' `.servitor/journal.md` files by hand.

This skill gives agents (and human operators) a focused primer on the `fleetops` CLI: which verb solves which problem, the new wake-open / wake-close ritual, and the permission model for writes.

## Scope

**In scope:**
- Agent-facing usage of `fleetops` read verbs (`show-state`, `tail-events`, `wakes`, `search-knowledge`, `show-artifact`, `doctor`).
- Agent-facing usage of `fleetops journal` write verbs (`add`, `update`, `show`, `tail`, `grep`, `render`).
- Session identity setup (`session-stamp`, `FLEETOPS_SESSION_ID`, `FLEETOPS_AGENT`).
- The new wake ritual (TEMPLATE_UPDATE v4) — open with `journal tail`, close with `journal add`.
- Bulk import of legacy `.servitor/journal.md` content via the included kata.

**Out of scope:**
- Building or extending the `fleetops` CLI itself (lives in `servitor` repo).
- Harvester internals — see `servitor/internal/fleetops/` for source.
- Fleet doctrine changes — that's Adama's surface, not this skill's.

## Key Features

- Cross-agent journal + event queries in one command.
- FTS5 full-text search over SOPs, katas, doctrine, standards, memory, and dreams.
- Structured `wakes` table (wake_number, ts, source, reason) — no more regex parsing.
- Permission model: session-stamped writes, attributable to the shell that spoke.
- Progressive disclosure in `references/` — tool reference, wake ritual, permission model, troubleshooting, bulk-import kata.

## When to Use

Trigger with phrases like:

- "Where did I solve X?"
- "What's the fleet doing right now?"
- "Closing out this wake."
- "Tail recent events for Daystrom."
- "Search the fleet knowledge for <topic>."
- "Is the harvester alive?"

## Dependencies

- `fleetops` binary on `$PATH` (built from `servitor` repo: `go build -o fleetops ./cmd/fleetops`).
- `~/.fleetops/fleet.db` — auto-created by `fleetops init`.
- `FLEETOPS_SESSION_ID` + `FLEETOPS_AGENT` exported in the writing shell (via `fleetops session-stamp`).
- SQLite 3.x (system library).

## Input Constraints

- `--agent` values must match canonical agent names in `~/.servitor/fleet-roster.md`. See `fleetops list-agents`.
- `--wake-number` must be an integer. Use your repo's monotonic wake sequence.
- `--ts` is ISO8601. `fleetops session-stamp` does not generate timestamps for you; pass `$(date -u -Iseconds)` or your repo's convention.
- `--body-file` expects UTF-8 markdown. Large stanzas (>200KB) will be rejected.

## Success Criteria

An agent using this skill should be able to:

1. Run `fleetops journal tail --agent <me>` at wake-open and see the last N stanzas.
2. Write a close-out stanza via `fleetops journal add` without touching `.servitor/journal.md`.
3. Query fleet knowledge via `fleetops search-knowledge` instead of multi-tree grep.
4. Run the bulk-import kata (see `references/bulk-import-kata.md`) once when Lee coordinates migration via Mattermost.
5. Diagnose permission rejections using `references/permission-model.md` and `references/troubleshooting.md`.

## Known Limitations

- Journal-write verbs (`add/update/show/tail/grep/render`) landed recently; flag names may drift by one minor version. `<verb> --help` is authoritative.
- FTS search is lexical (SQLite FTS5 tokenization), not semantic. For meaning-based recall, still prefer `cass search --mode semantic`.
- No remote sync — `fleet.db` is local per machine. Multi-machine fleets coordinate via `harvest` of shared `~/.servitor/` trees, not by sharing the DB file.
- `fleetops rebuild-state` drops `current_state` before re-ingesting; don't run it during a live write.

## Installation

```bash
# From AISkills
cp -r FleetOps/fleetops ~/.claude/skills/

# Verify
ls ~/.claude/skills/fleetops/
# SKILL.md  README.md  CHANGELOG.md  references/
```

The `fleetops` CLI itself installs from the `servitor` repo. See that repo's `install.sh`.

## Files

```
fleetops/
├── SKILL.md                      # Core skill definition (agent-facing)
├── README.md                     # This file
├── CHANGELOG.md                  # Version history
└── references/
    ├── tool-reference.md         # Full flag list per verb
    ├── wake-ritual.md            # Step-by-step wake open/close
    ├── permission-model.md       # session-stamp + FLEETOPS_SESSION_ID
    ├── troubleshooting.md        # Common failures and fixes
    └── bulk-import-kata.md       # One-time migration of .servitor/journal.md
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)

Reviewed and maintained under Captain Pike's quality gate (85/100 minimum).
