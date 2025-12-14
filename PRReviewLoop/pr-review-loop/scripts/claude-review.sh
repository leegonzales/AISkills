#!/bin/bash
# Perform a code review using Claude agent (fallback when Gemini is rate-limited)
# Usage: claude-review.sh <pr-number>
#
# This script outputs instructions for invoking a Claude agent to review the PR.
# The agent will:
#   1. Fetch PR diff and changed files
#   2. Read and analyze the code changes
#   3. Post a comprehensive review as a PR comment
#
# The review follows the same format as Gemini Code Assist but is performed by Claude.

set -euo pipefail

PR_NUMBER="${1:?Usage: claude-review.sh <pr-number>}"

# Get repo info
REPO=$(gh repo view --json nameWithOwner --jq '.nameWithOwner' 2>/dev/null || echo "")
if [[ -z "$REPO" ]]; then
    echo "Error: Could not determine repository. Run from within a git repository."
    exit 1
fi

# Get PR details for the prompt
PR_TITLE=$(gh pr view "$PR_NUMBER" --json title --jq '.title' 2>/dev/null || echo "PR #$PR_NUMBER")
PR_BRANCH=$(gh pr view "$PR_NUMBER" --json headRefName --jq '.headRefName' 2>/dev/null || echo "unknown")

echo "=============================================="
echo "Claude Code Review for PR #$PR_NUMBER"
echo "=============================================="
echo ""
echo "Repository: $REPO"
echo "Title: $PR_TITLE"
echo "Branch: $PR_BRANCH"
echo ""
echo "To perform the review, use the Task tool with subagent_type='general-purpose':"
echo ""
echo "---BEGIN AGENT PROMPT---"
cat << 'PROMPT_END'
Perform a thorough code review on PR #__PR_NUMBER__ in repository __REPO__.

## Your Task

1. **Fetch the PR diff and details:**
   ```bash
   gh pr view __PR_NUMBER__ --json title,body,files,commits
   gh api repos/__REPO__/pulls/__PR_NUMBER__/files --jq '.[] | {path: .filename, status: .status, patch: .patch}'
   ```

2. **Read the changed files in full** - Don't just look at the diff, read the complete files to understand context:
   - Use the Read tool to read each modified file
   - Understand the surrounding code and how the changes fit in

3. **Analyze the changes for:**
   - **Critical Issues**: Bugs, security vulnerabilities, logic errors, race conditions
   - **Medium Issues**: Missing validation, unclear error handling, potential edge cases
   - **Minor Issues**: Code style, naming, documentation gaps
   - **Positive Observations**: Good patterns, clean design choices

4. **Post your review as a PR comment:**
   ```bash
   gh pr review __PR_NUMBER__ --comment --body-file /tmp/claude_review.md
   ```

## Review Format

Write your review to `/tmp/claude_review.md` in this format:

```markdown
## Code Review (Claude)

I've reviewed the changes in this PR. Here's my analysis:

### Critical Issues
[List critical issues with file:line references and code snippets]

### Medium Issues
[List medium-priority issues]

### Minor Issues
[List minor issues - be selective, don't nitpick]

### Positive Observations
[Note good patterns and design choices]

### Recommendations Summary
**Must fix before merge:**
1. [Critical items]

**Should fix:**
2. [Medium items worth addressing]

**Nice to have:**
3. [Optional improvements]

### Overall Assessment
[1-2 sentence summary of the PR quality and readiness to merge]
```

## Guidelines

- **Be specific**: Include file paths, line numbers, and code snippets
- **Be constructive**: Explain WHY something is an issue and suggest fixes
- **Be selective**: Don't nitpick every minor style issue
- **Consider context**: The code might have good reasons for its patterns
- **Focus on impact**: Prioritize issues that affect correctness, security, or maintainability

After posting the review, output:
"Review posted to PR #__PR_NUMBER__. Use get-review-comments.sh to see inline comments if any were added."
PROMPT_END

echo ""
echo "---END AGENT PROMPT---"
echo ""

# Output the prompt with substitutions for easy copy
PROMPT_FILE="/tmp/claude_review_prompt_${PR_NUMBER}.txt"
cat << PROMPT_END > "$PROMPT_FILE"
Perform a thorough code review on PR #${PR_NUMBER} in repository ${REPO}.

## Your Task

1. **Fetch the PR diff and details:**
   \`\`\`bash
   gh pr view ${PR_NUMBER} --json title,body,files,commits
   gh api repos/${REPO}/pulls/${PR_NUMBER}/files --jq '.[] | {path: .filename, status: .status, patch: .patch}'
   \`\`\`

2. **Read the changed files in full** - Don't just look at the diff, read the complete files to understand context:
   - Use the Read tool to read each modified file
   - Understand the surrounding code and how the changes fit in

3. **Analyze the changes for:**
   - **Critical Issues**: Bugs, security vulnerabilities, logic errors, race conditions
   - **Medium Issues**: Missing validation, unclear error handling, potential edge cases
   - **Minor Issues**: Code style, naming, documentation gaps
   - **Positive Observations**: Good patterns, clean design choices

4. **Post your review as a PR comment:**
   \`\`\`bash
   gh pr review ${PR_NUMBER} --comment --body-file /tmp/claude_review.md
   \`\`\`

## Review Format

Write your review to \`/tmp/claude_review.md\` in this format:

\`\`\`markdown
## Code Review (Claude)

I've reviewed the changes in this PR. Here's my analysis:

### Critical Issues
[List critical issues with file:line references and code snippets]

### Medium Issues
[List medium-priority issues]

### Minor Issues
[List minor issues - be selective, don't nitpick]

### Positive Observations
[Note good patterns and design choices]

### Recommendations Summary
**Must fix before merge:**
1. [Critical items]

**Should fix:**
2. [Medium items worth addressing]

**Nice to have:**
3. [Optional improvements]

### Overall Assessment
[1-2 sentence summary of the PR quality and readiness to merge]
\`\`\`

## Guidelines

- **Be specific**: Include file paths, line numbers, and code snippets
- **Be constructive**: Explain WHY something is an issue and suggest fixes
- **Be selective**: Don't nitpick every minor style issue
- **Consider context**: The code might have good reasons for its patterns
- **Focus on impact**: Prioritize issues that affect correctness, security, or maintainability

After posting the review, output:
"Review posted to PR #${PR_NUMBER}. Use get-review-comments.sh to see inline comments if any were added."
PROMPT_END

echo "Prompt saved to: $PROMPT_FILE"
echo ""
echo "Quick invocation (copy this):"
echo ""
echo "Task tool call:"
echo "  subagent_type: general-purpose"
echo "  description: Review PR #$PR_NUMBER"
echo "  prompt: (contents of $PROMPT_FILE)"
