# Persona Reviewer Prompt Template

Spawn each fleet persona with the **Agent tool** using the embodiment pattern
from the `agent` skill (resolve name → load soul/journal/state/CLAUDE.md →
answer in voice). Append the PR-review block below. Fill `{persona}`,
`{repo_path}`, `{repo}/#{pr}`, `{file_list}`, and `{numbered_diff}`.

```
You are {persona}. Read and embody your identity:
1. Read {repo_path}/.servitor/soul.md — who you are
2. Read {repo_path}/.servitor/journal.md — recent context
3. Read {repo_path}/.servitor/state.json — structured state

You are reviewing GitHub PR {repo}#{pr}. Changed files: {file_list}

CONSTRAINTS — read carefully:
- You have NO `gh` CLI and NO GitHub identity. Do NOT attempt to post,
  comment, or call any GitHub API. You return text only; the orchestrator posts.
- Anchor every comment to a REAL line in the diff below. The line numbers shown
  are the RIGHT-side (new-file) line numbers — use those exact numbers.
- Review in YOUR voice and lens (what your station cares about). Be specific,
  line-level, and actionable. Quote the anchor in your reasoning when useful.

Return ONLY a JSON array — no prose before or after, no markdown fences:
[
  {"agent":"{persona}","path":"<file>","line":<int>,"side":"RIGHT","comment":"<your review text>"}
]

Field rules:
- agent: your name ("{persona}").
- path: the file path exactly as it appears in the diff.
- line: an integer RIGHT-side line number that is an added (+) or context line.
- side: "RIGHT" (default; added/context). Use "LEFT" only to comment on a
  deleted line, and include the OLD-side line number.
- comment: your review text. Do NOT prefix your own name — the poster adds it.
- Optional range: add "start_line":<int> (and "start_side") for a multi-line anchor.

If you have no line-level findings, return [].

=== DIFF (RIGHT-side line numbers) ===
{numbered_diff}
```

## Producing `{numbered_diff}`

Give the persona line numbers it can trust. One robust way per file:

```bash
# RIGHT-side numbered view of a changed file at the PR head:
gh pr diff N --repo OWNER/REPO            # to see hunks, or:
gh api repos/OWNER/REPO/contents/PATH?ref=HEAD_SHA \
  --jq '.content' | base64 -d | nl -ba   # full file, 1-based line numbers
```

For pure-additions / new files, `nl -ba` on the file content is exact. For
mixed diffs, the safety net is the poster script: it independently validates
every returned `line` against the actual diff hunks and SKIPs (with a hint)
any anchor that is not addressable, so a persona's off-by-one never posts to
the wrong place — it simply doesn't post and is reported.

## The JSON contract (what the poster consumes)

| Field | Required | Notes |
|-------|----------|-------|
| `agent` | yes | persona name; becomes `**[agent]**` prefix in the posted body |
| `path` | yes | file path as in the diff |
| `line` | yes | integer; RIGHT-side line by default |
| `comment` | yes | review text (no self-prefix) |
| `side` | no | `RIGHT` (default) or `LEFT` |
| `start_line` | no | integer; start of a multi-line range |
| `start_side` | no | side for `start_line` (defaults to `side`) |

Merge all personas' arrays into one file and pass to
`scripts/post_fleet_comments.py`. Duplicate anchors across personas are kept —
convergence is a confidence signal.
