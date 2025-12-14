#!/bin/bash
# Commit staged changes and push to trigger next review cycle
# Usage: commit-and-push.sh "commit message"
#
# This script is designed to be granted explicit permission for autonomous
# PR review loops. It commits and pushes, then optionally triggers a new review.

set -euo pipefail

MESSAGE="${1:?Usage: commit-and-push.sh \"commit message\" [--trigger-review]}"
TRIGGER_REVIEW=false

# Check for --trigger-review flag
for arg in "$@"; do
    if [[ "$arg" == "--trigger-review" ]]; then
        TRIGGER_REVIEW=true
    fi
done

# Run pre-commit if available
if command -v pre-commit &>/dev/null; then
    echo "Running pre-commit hooks..."
    pre-commit run --all-files || {
        echo "Pre-commit failed. Please fix issues and try again."
        exit 1
    }
fi

# Stage all changes
git add -A

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "No changes to commit."
    exit 0
fi

# Commit with standard footer
git commit -m "$(cat <<EOF
$MESSAGE

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"

# Push
echo "Pushing to origin..."
git push

# Optionally trigger new review
if [[ "$TRIGGER_REVIEW" == "true" ]]; then
    # Get PR number from current branch
    PR_NUMBER=$(gh pr view --json number --jq '.number' 2>/dev/null || echo "")
    if [[ -n "$PR_NUMBER" ]]; then
        echo "Triggering Gemini review on PR #$PR_NUMBER..."
        gh pr comment "$PR_NUMBER" --body "/gemini review"
    else
        echo "Warning: Could not determine PR number to trigger review"
    fi
fi

echo "Done."
