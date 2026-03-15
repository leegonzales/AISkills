---
name: requesting-code-review
description: Use when completing tasks, implementing major features, or before merging to verify work meets requirements. Dispatches three independent reviewers in parallel.
---

# Requesting Code Review

Dispatch three independent reviewers in parallel for multi-perspective code review.

**Core principle:** Three perspectives catch more than one. Dispatch all reviewers simultaneously.

## Reviewers

| Reviewer | Skill/Tool | Strengths |
|----------|-----------|-----------|
| Claude subagent | `superpowers:code-reviewer` Task tool | Deep reasoning, plan compliance |
| Codex CLI | `codex review --base <SHA>` | Line-level bugs, concise output |
| Gemini CLI | `cat <<'EOF' \| gemini` | Holistic view, large context (1M tokens) |

## When to Request Review

**Mandatory:** After each task in subagent-driven development, after major features, before merge to main.

**Optional:** When stuck, before refactoring, after fixing complex bugs.

## The Process

### Step 1: Get git SHAs

```bash
BASE_SHA=$(git rev-parse HEAD~N)  # or origin/main, or specific commit
HEAD_SHA=$(git rev-parse HEAD)
```

### Step 2: Dispatch ALL THREE reviewers in parallel

**All three run simultaneously.** Use parallel tool calls.

#### 2a. Claude subagent

Use Task tool with `superpowers:code-reviewer` type. Fill the template from the marketplace skill's `code-reviewer.md` with:
- `{WHAT_WAS_IMPLEMENTED}` - What you built
- `{PLAN_OR_REQUIREMENTS}` - What it should do
- `{BASE_SHA}` / `{HEAD_SHA}` - Git range
- `{DESCRIPTION}` - Brief summary

#### 2b. Codex CLI

```bash
codex review --base $BASE_SHA
```

This is Codex's built-in code review command. It automatically diffs from BASE_SHA to HEAD and provides line-level feedback.

#### 2c. Gemini CLI

```bash
DIFF=$(git diff $BASE_SHA..$HEAD_SHA)
cat <<EOF | gemini
Code review request.

CONTEXT: [what was implemented and why]

REQUIREMENTS: [plan or spec reference]

DIFF:
$DIFF

Review for: code quality, architecture, error handling, security, testing gaps.
Categorize issues as Critical / Important / Minor with file:line references.
EOF
```

### Step 3: Synthesize findings

After all three return, consolidate into a single report:

1. **Agreement** — issues flagged by 2+ reviewers are high-confidence
2. **Unique findings** — issues only one reviewer caught (still valid)
3. **Disagreements** — where reviewers conflict, evaluate technically
4. **Severity** — use the highest severity assigned by any reviewer

### Step 4: Act on feedback

- Fix **Critical** issues immediately
- Fix **Important** issues before proceeding
- Note **Minor** issues for later
- Push back if reviewer is wrong (with reasoning)

## Quick Reference

| Step | Action |
|------|--------|
| Get SHAs | `git rev-parse HEAD~N` / `git rev-parse HEAD` |
| Claude | Task tool with `superpowers:code-reviewer` |
| Codex | `codex review --base $BASE_SHA` |
| Gemini | Pipe diff + context to `gemini` via heredoc |
| Synthesize | Consolidate all three, weight by agreement |

## Integration with Workflows

**Subagent-Driven Development:** Review after EACH task. All three reviewers, every time.

**Executing Plans:** Review after each batch (3 tasks).

**Ad-Hoc Development:** Review before merge.

## Red Flags

**Never:**
- Skip review because "it's simple"
- Use only one reviewer when all three are available
- Ignore Critical issues from any reviewer
- Proceed with unfixed Important issues

**If a reviewer is unavailable** (CLI not installed, API quota):
- Note which reviewer was skipped
- Proceed with remaining reviewers
- Do NOT skip review entirely
