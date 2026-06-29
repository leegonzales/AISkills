---
name: fleet-pr-review
description: Use when you want fleet personas to review a GitHub pull request and have their feedback land as line-level review comments. Orchestrates persona subagents (Pike, Thufir, Sisko, etc. embodied from their .servitor/soul.md) to review changed files, collects structured line-anchored comments, validates each against the diff, and posts them to the PR via the GitHub API attributed by persona name. Solves the problem that review subagents have no `gh` access and no GitHub identity — only the orchestrator can post.
---

# Fleet PR Review

## Overview

Fleet persona subagents have judgment but **no `gh` CLI and no GitHub identity** — they can only return comment text. This skill makes the orchestrator the single GitHub writer: fan out personas to review a PR, collect **line-anchored** comments in a fixed JSON shape, then post them as line-level review comments attributed by name (`**[Pike]** ...`) because the GitHub author is the orchestrator's token.

## When to Use

- "Have the fleet review PR #N" / "get Pike and Thufir to comment on this PR"
- You want feedback anchored to specific diff lines, not one blob PR comment
- Multiple personas, multi-file diffs, per-comment success/failure reporting

When NOT to use: a single reviewer who already has `gh` (just let them post), or non-line-anchored prose review (post one issue comment).

## Workflow

### 1. Establish the review surface
```bash
gh pr view N --repo OWNER/REPO --json headRefOid,files
gh pr diff N --repo OWNER/REPO     # the addressable lines live here
```
The **head SHA** is the `commit_id` every comment pins to. A RIGHT-side line is addressable only if it is an added (`+`) or context line in a hunk. The poster script validates this for you — but know it so you can brief reviewers on real line numbers.

### 2. Fan out persona reviewers (parallel)
Spawn each persona with the **Agent tool**, embodying them from their soul (this is the `agent` skill's pattern). **REQUIRED SUB-SKILL:** use the `agent` skill for persona resolution + the soul/journal/state load template and the fleet roster.

Add these PR-review-specific constraints to each subagent prompt:
- Paste the diff **with RIGHT-side line numbers** so the persona anchors to real lines.
- State plainly: *you have no `gh` and no GitHub identity; do not attempt to post — return text only.*
- Demand a **strict JSON array** return, nothing else:
```json
[{"agent":"Pike","path":"src/foo.py","line":42,"side":"RIGHT","comment":"..."}]
```
`agent`, `path`, `line`, `comment` required; `side` defaults RIGHT; `start_line`/`start_side` optional for a range. See `references/reviewer-prompt.md` for the full prompt template.

### 3. Collect + merge
Concatenate every persona's JSON array into one file (`/tmp/fleet-comments.json`). Keep duplicate anchors from different personas — convergence is signal, not noise.

### 4. Post (validated, per-comment, attributed)
```bash
python3 scripts/post_fleet_comments.py \
  --repo OWNER/REPO --pr N --comments /tmp/fleet-comments.json
```
The script resolves the head SHA, validates each line is in the diff (SKIPs + explains misses), prefixes `**[Agent]**`, posts each comment **independently** (one failure never blocks the rest), and prints per-comment OK/FAIL/SKIP. Always `--dry-run` first to see what would post. `--help` for all flags.

## Quick Reference

| Step | Command |
|------|---------|
| Surface | `gh pr view N --repo R --json headRefOid,files` |
| Diff | `gh pr diff N --repo R` |
| Fan out | Agent tool per persona (via `agent` skill) → JSON array |
| Dry run | `post_fleet_comments.py --repo R --pr N --comments f.json --dry-run` |
| Post | `post_fleet_comments.py --repo R --pr N --comments f.json` |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Subagent tries to post / runs `gh` | Forbid it in the prompt; only the orchestrator posts. |
| Attribution via GitHub author | Author is your token — attribution lives in the body (`**[Agent]**`, the script adds it). |
| Anchoring to a deleted/unchanged line | Use RIGHT-side `+`/context lines; the script SKIPs invalid anchors with a hint. |
| `gh api -F/-f` array typing breaks `line` | The script pipes a JSON object to `--input -` — integers stay integers. |
| One atomic `/reviews` batch | Batches are all-or-nothing; this posts per-comment so partial success is reported. |
| Posting against a moved head | `commit_id` is auto-resolved at post time; re-run after new pushes. |
| Assuming every persona repo path | `repo_path` comes from the `agent` skill's roster, not a guess — personas live in different repos (e.g. Thufir in `mentat`, not `servitor`). Resolve, don't assume. |

## Notes

- **Merged PRs:** the mechanics still work (head SHA resolves, lines validate), but line-level comments land on the merged commit rather than a live review thread, and notifications differ. Prefer reviewing while the PR is open.
- **Mixed diffs:** for new/pure-addition files `nl -ba` gives exact RIGHT-side numbers; for mixed hunks the persona reads numbers off the diff and the poster's validator is the safety net — an off-by-one anchor SKIPs (reported) rather than posting to the wrong line.

## Files
- `scripts/post_fleet_comments.py` — the poster/validator (run `--help`).
- `references/reviewer-prompt.md` — persona-subagent prompt template + JSON contract.
