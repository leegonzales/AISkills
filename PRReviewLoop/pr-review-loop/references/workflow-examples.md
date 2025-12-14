# Workflow Examples

Complete examples of PR Review Loop workflows.

## Example 1: Fresh PR Review Cycle

**Scenario:** Just pushed a PR and want to address reviewer feedback.

```bash
# 1. Get summary of unresolved comments
~/.claude/skills/pr-review-loop/scripts/summarize-reviews.sh 42

# 2. Get detailed comments with IDs (wait for Gemini if just pushed)
~/.claude/skills/pr-review-loop/scripts/get-review-comments.sh 42 --with-ids --wait

# 3. For each comment:
#    - Read the suggestion
#    - Apply fix OR decide to skip
#    - Reply to the comment (auto-resolves)
~/.claude/skills/pr-review-loop/scripts/reply-to-comment.sh 42 12345 "Fixed - added input validation"
~/.claude/skills/pr-review-loop/scripts/reply-to-comment.sh 42 12346 "Won't fix - this is intentional for backwards compat"

# 4. Commit and push (NEVER use raw git)
~/.claude/skills/pr-review-loop/scripts/commit-and-push.sh "fix: address review feedback"

# 5. Trigger next review and wait
~/.claude/skills/pr-review-loop/scripts/trigger-review.sh 42 --wait

# 6. Repeat from step 1
```

---

## Example 2: Gemini Rate Limited - Claude Fallback

**Scenario:** Gemini hit daily quota, need code review.

```bash
# 1. Check quota status
~/.claude/skills/pr-review-loop/scripts/check-gemini-quota.sh 42
# Output: {"status": "rate-limited", "reason": "quota exceeded", ...}

# 2. Generate Claude review prompt
~/.claude/skills/pr-review-loop/scripts/claude-review.sh 42

# 3. Use Task tool with the generated prompt
# Task tool:
#   subagent_type: general-purpose
#   description: Review PR #42
#   prompt: (contents of /tmp/claude_review_prompt_42.txt)

# 4. After Claude posts review, continue normal workflow
~/.claude/skills/pr-review-loop/scripts/get-review-comments.sh 42 --with-ids
```

---

## Example 3: Final Verification Loop

**Scenario:** All comments resolved, doing final check.

```bash
# 1. Verify no unresolved comments
~/.claude/skills/pr-review-loop/scripts/get-review-comments.sh 42 --with-ids
# Output: No unresolved review comments.

# 2. Track in TodoWrite that we're in final verification
# Todo: "Final verification loop - if no actionable feedback, ready to merge"

# 3. Trigger one more review
~/.claude/skills/pr-review-loop/scripts/trigger-review.sh 42 --wait

# 4. Check for new comments
~/.claude/skills/pr-review-loop/scripts/get-review-comments.sh 42 --with-ids

# 5. If no new actionable feedback:
#    "We've completed the review cycles. Ready to merge, or want to address more?"

# 5b. If new feedback that requires fixes:
#     - Remove "final verification loop" todo
#     - Fix issues, reply, push
#     - Do another "one more loop" after
```

---

## Example 4: Skip Pedantic Suggestions

**Scenario:** Reviewer suggesting unnecessary changes.

```bash
# Comment: "Consider adding null check for this parameter"
# (Internal function, caller always passes valid data)

# Reply explaining why we're skipping
~/.claude/skills/pr-review-loop/scripts/reply-to-comment.sh 42 12347 \
  "Won't fix - this is an internal helper, caller guarantees valid input. Adding null checks would add noise without benefit."
```

**Guidelines for skipping:**
- Platform-specific when not applicable
- Overly defensive (excessive null checks, unlikely edge cases)
- Stylistic preferences not matching project conventions
- Documentation for self-explanatory code

---

## Example 5: Background Monitoring

**Scenario:** Long-running PR, want to monitor in background.

```bash
# Start background monitor
~/.claude/skills/pr-review-loop/scripts/watch-pr.sh 42 &

# Output example:
# === Watching PR #42 ===
# Started at: Sat Dec 14 13:45:00 MST 2025
#
# Initial state: 2 reviews, 5 inline comments, 3 PR comments
#
# --- CI Status (13:45:30) ---
# ✓ lint (1m 23s)
# ✓ test (2m 45s)
# * deploy-preview (running)
#
# !!! NEW REVIEW COMMENTS DETECTED !!!
# Comments: 5 -> 8
```

---

## Reply Templates

Standard templates for common responses:

| Situation | Template |
|-----------|----------|
| Fixed issue | `"Fixed - [description of change]"` |
| Won't fix (valid reason) | `"Won't fix - [reason: intentional, out of scope, etc.]"` |
| Deferred to issue | `"Good catch, tracking in #[issue-number]"` |
| Acknowledged info | `"Acknowledged - [explanation of understanding]"` |
| Needs discussion | `"Let's discuss - [question or concern]"` |
| Already addressed | `"Already addressed in [commit/file]"` |

---

## Critical Rules Checklist

Before each cycle, verify:

- [ ] Using `commit-and-push.sh` (never raw git)
- [ ] Replying to EVERY comment (never leave unreplied)
- [ ] Using `--wait` flag when polling for comments
- [ ] Evaluating suggestions critically (not blindly applying)
- [ ] Tracking if in "final verification loop"

---

## Diminishing Returns Signals

After 2-3 cycles, watch for:

- Same type of issue flagged repeatedly
- Comments about minor style preferences
- Fewer comments per cycle
- Lower priority issues (medium → low)
- Nitpicks rather than substantive feedback

When these appear, consider doing final verification loop.
