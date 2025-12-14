# Scripts Reference

Complete reference for all PR Review Loop scripts.

## Core Scripts

### commit-and-push.sh

**CRITICAL: ALWAYS use this instead of raw `git commit` or `git push`.**

```bash
~/.claude/skills/pr-review-loop/scripts/commit-and-push.sh "fix: description"
~/.claude/skills/pr-review-loop/scripts/commit-and-push.sh "fix: description" --trigger-review
```

**What it does:**
1. Runs pre-commit hooks if available
2. Stages all changes (`git add -A`)
3. Commits with proper footer (Claude Code attribution)
4. Pushes to origin
5. Optionally triggers a new review

**Flags:**
- `--trigger-review`: Also trigger Gemini review after push

---

### reply-to-comment.sh

**CRITICAL: ALWAYS reply to every comment using this script.**

```bash
~/.claude/skills/pr-review-loop/scripts/reply-to-comment.sh <PR> <comment-id> "Fixed - description"
~/.claude/skills/pr-review-loop/scripts/reply-to-comment.sh <PR> <comment-id> "Won't fix - reason"
~/.claude/skills/pr-review-loop/scripts/reply-to-comment.sh <PR> <comment-id> "Acknowledged" --no-resolve
```

**What it does:**
1. Posts reply to the specified comment
2. Automatically resolves the thread (unless `--no-resolve`)
3. Uses GitHub GraphQL API to find and resolve thread

**Parameters:**
- `<PR>`: PR number (e.g., `42`)
- `<comment-id>`: Numeric comment ID from `get-review-comments.sh --with-ids`
- `"message"`: Reply text

**Flags:**
- `--no-resolve`: Post reply without resolving the thread

---

### get-review-comments.sh

Fetch review comments with optional filtering and polling.

```bash
~/.claude/skills/pr-review-loop/scripts/get-review-comments.sh <PR>
~/.claude/skills/pr-review-loop/scripts/get-review-comments.sh <PR> --with-ids
~/.claude/skills/pr-review-loop/scripts/get-review-comments.sh <PR> --with-ids --wait
~/.claude/skills/pr-review-loop/scripts/get-review-comments.sh <PR> --all
~/.claude/skills/pr-review-loop/scripts/get-review-comments.sh <PR> --latest
```

**Flags:**
- `--with-ids`: Include comment IDs for replying (use this!)
- `--wait`: Poll every 30s for up to 5 minutes waiting for comments
- `--all`: Include resolved threads (default: unresolved only)
- `--latest`: Only comments on latest commit

**Output format (with --with-ids):**
```
=== Comment ID: 12345 | Node ID: PRR_xxx ===
File: src/auth.py:42
Priority: high

[Comment body with suggestion]

---
```

---

### trigger-review.sh

Trigger a code review (Gemini or Claude fallback).

```bash
~/.claude/skills/pr-review-loop/scripts/trigger-review.sh <PR>
~/.claude/skills/pr-review-loop/scripts/trigger-review.sh <PR> --wait
~/.claude/skills/pr-review-loop/scripts/trigger-review.sh <PR> --claude
~/.claude/skills/pr-review-loop/scripts/trigger-review.sh --wait  # Auto-detect PR
```

**Flags:**
- `--wait`: Poll for up to 5 minutes until comments appear
- `--claude`: Skip Gemini, use Claude agent directly

**Behavior:**
1. Checks if Gemini is rate-limited first
2. If rate-limited, shows fallback instructions
3. Otherwise, posts `/gemini review` comment
4. If `--wait`, polls until comments appear

---

### summarize-reviews.sh

Summary of review comments by priority and file.

```bash
~/.claude/skills/pr-review-loop/scripts/summarize-reviews.sh <PR>
~/.claude/skills/pr-review-loop/scripts/summarize-reviews.sh <PR> --all
```

**Output:**
```
=== PR #42 Review Summary ===

## By Priority
- high: 2 comments
- medium: 5 comments
- low: 1 comments

## By File
- src/auth.py: 4 comments
- src/utils.py: 3 comments
- tests/test_auth.py: 1 comments

## High Priority Items
- [src/auth.py:42] Security: Token not validated properly
- [src/auth.py:78] Security: Missing rate limiting
```

---

## Support Scripts

### claude-review.sh

Generate Claude agent prompt for code review (Gemini fallback).

```bash
~/.claude/skills/pr-review-loop/scripts/claude-review.sh <PR>
```

**Output:**
- Displays structured prompt for Task tool
- Saves prompt to `/tmp/claude_review_prompt_<PR>.txt`

**Use with Task tool:**
```
Task tool:
  subagent_type: general-purpose
  description: Review PR #<PR>
  prompt: (contents of /tmp/claude_review_prompt_<PR>.txt)
```

---

### check-gemini-quota.sh

Check if Gemini Code Assist is rate-limited.

```bash
~/.claude/skills/pr-review-loop/scripts/check-gemini-quota.sh <PR>
```

**Exit codes:**
- `0`: Gemini available
- `1`: Gemini rate-limited

**Output (JSON):**
```json
{"status": "available", "reason": "no quota warning in last comment"}
```
or
```json
{"status": "rate-limited", "reason": "quota exceeded", "detected_at": "2025-12-14T..."}
```

---

### watch-pr.sh

Background monitor for CI checks and review comments.

```bash
~/.claude/skills/pr-review-loop/scripts/watch-pr.sh <PR>
```

**Behavior:**
- Polls every 30 seconds
- Reports CI status changes
- Detects new reviews/comments
- Alerts on Gemini quota exceeded
- Designed for background execution

---

### resolve-comment.sh

Manually resolve (minimize/hide) a comment thread.

```bash
~/.claude/skills/pr-review-loop/scripts/resolve-comment.sh <node-id> [reason]
```

**Parameters:**
- `<node-id>`: GraphQL node ID (from `get-review-comments.sh --with-ids`)
- `[reason]`: RESOLVED (default), OUTDATED, OFF_TOPIC, ABUSE, SPAM

**Note:** Prefer `reply-to-comment.sh` which auto-resolves.
