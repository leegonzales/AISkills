# Fleet PR Review

Orchestrate fleet AI personas to review a GitHub pull request and post their
feedback as **line-level review comments**, each attributed by persona name.

## The problem it solves

When the fleet reviews a PR, the subagents that embody fleet personas (Pike,
Thufir, Sisko, Geordi, …) have judgment but **no `gh` CLI and no GitHub
identity** — they can only return comment text. So an orchestrator (e.g. Adama)
has to collect their line-anchored comments and post them to the PR via the API,
attributed by name. This skill turns that one-off chore into a repeatable
workflow with a hardened poster.

## How it works

1. **Surface** — resolve the PR head SHA (`commit_id`) and changed files.
2. **Fan out** — spawn each persona as a subagent (via the `agent` skill's
   embodiment pattern), feed it the numbered diff, forbid `gh`/posting, and
   demand a strict JSON array of line-anchored comments.
3. **Merge** — concatenate every persona's array into one file.
4. **Post** — `scripts/post_fleet_comments.py` validates each anchor against the
   diff, prefixes `**[Agent]**`, posts each comment independently, and reports
   per-comment OK/FAIL/SKIP. Always `--dry-run` first.

## Installation

This is a Claude Code skill. With the AISkills repo on your skills path it loads
by description. To use the poster directly:

```bash
python3 scripts/post_fleet_comments.py --help
```

Requires: `gh` CLI (authenticated), Python 3.

## Usage

```bash
# Dry run — validate anchors and preview payloads, post nothing
python3 scripts/post_fleet_comments.py \
  --repo OWNER/REPO --pr 89 --comments /tmp/fleet-comments.json --dry-run

# Post for real
python3 scripts/post_fleet_comments.py \
  --repo OWNER/REPO --pr 89 --comments /tmp/fleet-comments.json
```

### Comments file shape

```json
[
  {"agent": "Pike",   "path": "src/foo.py", "line": 42, "comment": "..."},
  {"agent": "Thufir", "path": "src/foo.py", "line": 17, "side": "RIGHT",
   "start_line": 15, "comment": "multi-line anchor ..."}
]
```

`agent`, `path`, `line`, `comment` required. `side` defaults `RIGHT`.
`start_line`/`start_side` give a multi-line range.

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill definition + orchestration workflow |
| `references/reviewer-prompt.md` | Persona-subagent prompt template + JSON contract |
| `scripts/post_fleet_comments.py` | Validating, per-comment, attributed poster |

## Safety

- The poster validates every RIGHT-side anchor against the actual diff hunks and
  **skips** (with a hint) any line not addressable — an off-by-one never posts
  to the wrong place.
- Comments post independently: one failure never blocks the rest.
- `--dry-run` previews every payload without touching GitHub.

## Limitations / hardening backlog

- **Merged PRs:** mechanics work but comments land on the merged commit, not a
  live review thread. Prefer reviewing while open.
- **Mixed-diff line numbering** for personas is read off `gh pr diff`; exact only
  for new/pure-addition files via `nl -ba`. The validator is the safety net.
- **LEFT-side validation** is best-effort (RIGHT-side is strict).
- **Persona fan-out** is delegated to the `agent` skill; this skill does not
  re-implement roster resolution.

See `CHANGELOG.md` for version history.
