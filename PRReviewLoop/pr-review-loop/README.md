# PR Review Loop

A Claude Code skill for managing PR review feedback loops with Gemini Code Assist and other automated reviewers.

## Features

- **Automated Review Cycles**: Streamline push-review-fix workflow
- **Gemini Integration**: Works with Gemini Code Assist reviews
- **Claude Fallback**: Automatic fallback when Gemini is rate-limited
- **Smart Replies**: Auto-resolve threads when replying to comments
- **Diminishing Returns**: Detects when to stop iterating
- **Safe Git Operations**: Wrapper scripts enforce proper git usage

## Installation

### 1. Copy skill to Claude skills directory

```bash
cp -r pr-review-loop ~/.claude/skills/
```

### 2. Make scripts executable

```bash
chmod +x ~/.claude/skills/pr-review-loop/scripts/*.sh
```

### 3. Add permissions to settings

Add to `.claude/settings.local.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(~/.claude/skills/pr-review-loop/scripts/commit-and-push.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/reply-to-comment.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/trigger-review.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/get-review-comments.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/summarize-reviews.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/claude-review.sh:*)"
    ]
  }
}
```

## Prerequisites

| Requirement | Install |
|-------------|---------|
| GitHub CLI | `brew install gh` then `gh auth login` |
| pre-commit | `pip install pre-commit` |
| Pre-commit hooks | `.pre-commit-config.yaml` in repo |

## Quick Start

```bash
# 1. Get review comments
~/.claude/skills/pr-review-loop/scripts/get-review-comments.sh 42 --with-ids --wait

# 2. Reply to each comment
~/.claude/skills/pr-review-loop/scripts/reply-to-comment.sh 42 12345 "Fixed - added validation"

# 3. Commit (NEVER use raw git)
~/.claude/skills/pr-review-loop/scripts/commit-and-push.sh "fix: address review feedback"

# 4. Trigger next review
~/.claude/skills/pr-review-loop/scripts/trigger-review.sh 42 --wait
```

## Scripts Reference

| Script | Purpose |
|--------|---------|
| `commit-and-push.sh "msg"` | Commit and push (runs pre-commit) |
| `reply-to-comment.sh <PR> <id> "msg"` | Reply and auto-resolve thread |
| `get-review-comments.sh <PR>` | Fetch comments (`--with-ids --wait`) |
| `trigger-review.sh <PR>` | Trigger review cycle (`--wait --claude`) |
| `summarize-reviews.sh <PR>` | Summary by priority/file |
| `claude-review.sh <PR>` | Generate Claude review prompt |
| `check-gemini-quota.sh <PR>` | Check Gemini rate limit status |
| `watch-pr.sh <PR>` | Background CI/review monitor |
| `resolve-comment.sh <id>` | Manual thread resolution |

## Usage with Claude Code

Invoke the skill by asking Claude to help with PR reviews:

- "Check for new reviews on my PR"
- "Help me address the review feedback"
- "Iterate on PR #42 until it's ready"

Claude will use the skill's workflow and scripts automatically.

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────┐
│  1. Get Comments                                            │
│     summarize-reviews.sh <PR>                               │
│     get-review-comments.sh <PR> --with-ids --wait           │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  2. For Each Comment                                        │
│     • Evaluate: Is this worthwhile?                         │
│     • Fix OR decide to skip                                 │
│     • Reply: reply-to-comment.sh <PR> <id> "message"        │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Commit & Push                                           │
│     commit-and-push.sh "fix: description"                   │
│     (NEVER use raw git commit/push)                         │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  4. Trigger Next Review                                     │
│     trigger-review.sh <PR> --wait                           │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
                    ┌──────┴──────┐
                    │ New Comments? │
                    └──────┬──────┘
                      Yes  │  No
                       ▼   │   ▼
                  Go to 1  │  One More Loop
                           │  Then ask about merge
```

## Gemini Rate Limit Fallback

When Gemini Code Assist hits its daily quota:

```bash
# Option 1: Use --claude flag
~/.claude/skills/pr-review-loop/scripts/trigger-review.sh <PR> --claude

# Option 2: Run directly
~/.claude/skills/pr-review-loop/scripts/claude-review.sh <PR>
# Then use Task tool with the generated prompt
```

## Attribution

Forked from [devonjones/skill-pr-review-loop](https://github.com/devonjones/skill-pr-review-loop).

## License

MIT - See [LICENSE](LICENSE) for details.
