# PR Review Loop

A Claude Code skill for managing PR review feedback loops with Gemini Code Assist and other reviewers.

## Overview

This skill streamlines the push-review-fix cycle for PRs with automated reviewers. It:

- Monitors CI checks and review comments
- Fetches and summarizes review feedback by priority
- Automates the reply-and-resolve workflow for review threads
- Detects Gemini Code Assist rate limits and falls back to Claude
- Tracks review cycles to detect diminishing returns

## Installation

Copy the `pr-review-loop` directory to your Claude skills folder:

```bash
cp -r pr-review-loop ~/.claude/skills/
```

Make scripts executable:

```bash
chmod +x ~/.claude/skills/pr-review-loop/scripts/*.sh
```

## Prerequisites

- **GitHub CLI (`gh`)**: Must be installed and authenticated
- **pre-commit**: Install globally with `pip install pre-commit`
- **Pre-commit hooks**: Configure `.pre-commit-config.yaml` in your repo

## Permission Setup

Add these to your Claude Code settings (`.claude/settings.local.json`) to enable autonomous loops:

```json
{
  "permissions": {
    "allow": [
      "Bash(~/.claude/skills/pr-review-loop/scripts/commit-and-push.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/reply-to-comment.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/trigger-review.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/get-review-comments.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/summarize-reviews.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/claude-review.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/check-gemini-quota.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/watch-pr.sh:*)",
      "Bash(~/.claude/skills/pr-review-loop/scripts/resolve-comment.sh:*)"
    ]
  }
}
```

## Usage

### Basic Workflow

1. **Push changes to your PR**
2. **Invoke the skill** by asking Claude to help with PR reviews
3. **Claude will**:
   - Fetch review comments
   - Analyze each suggestion
   - Apply fixes or explain why not
   - Reply to each comment (auto-resolving threads)
   - Push changes and trigger next review

### Scripts Reference

| Script | Purpose |
|--------|---------|
| `commit-and-push.sh "msg"` | Commit and push (runs pre-commit) |
| `reply-to-comment.sh <PR> <id> "msg"` | Reply and auto-resolve comment thread |
| `get-review-comments.sh <PR> [--with-ids] [--wait]` | Fetch comments (--wait polls 5min) |
| `trigger-review.sh [PR] [--wait] [--claude]` | Trigger review cycle |
| `summarize-reviews.sh <PR> [--all]` | Summary by priority/file |
| `watch-pr.sh <PR>` | Background monitor |
| `claude-review.sh <PR>` | Generate Claude review prompt |
| `check-gemini-quota.sh <PR>` | Check Gemini rate limit |
| `resolve-comment.sh <node-id> [reason]` | Manual thread resolve |

### Gemini Rate Limit Fallback

When Gemini Code Assist hits its daily quota, the skill automatically detects this and can use Claude as a fallback reviewer:

```bash
~/.claude/skills/pr-review-loop/scripts/trigger-review.sh <PR> --claude
```

## Key Features

### Critical Review Evaluation

The skill evaluates each review comment critically, skipping:
- Platform-specific comments not applicable to your code
- Overly defensive suggestions (excessive null checks)
- Stylistic preferences that don't match project conventions

### Diminishing Returns Detection

After 2-3 review cycles, the skill evaluates whether continuing provides value:
- Are comments addressing real issues or nitpicks?
- Are we fixing the same type of issue repeatedly?
- Is the reviewer finding fewer issues?

### One More Loop Rule

When all comments are resolved, the skill does ONE additional review cycle to catch any final feedback, then asks about merging.

## Attribution

Forked from [devonjones/skill-pr-review-loop](https://github.com/devonjones/skill-pr-review-loop).

## License

MIT
