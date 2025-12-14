#!/bin/bash
# Watch a PR for CI checks and new review comments
# Usage: watch-pr.sh <pr-number> [repo]
#
# Monitors both CI checks and review comments, outputting updates as they arrive.
# Designed to run in background with Bash tool's run_in_background option.
#
# Detects Gemini Code Assist quota limits and signals when Claude fallback is needed.

set -euo pipefail

PR_NUMBER="${1:?Usage: watch-pr.sh <pr-number> [repo]}"
REPO="${2:-}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Build repo flag if provided
REPO_FLAG=""
if [[ -n "$REPO" ]]; then
    REPO_FLAG="-R $REPO"
fi

# Track last known review count to detect new reviews
LAST_REVIEW_COUNT=0
LAST_COMMENT_COUNT=0
LAST_PR_COMMENT_COUNT=0

echo "=== Watching PR #$PR_NUMBER ==="
echo "Started at: $(date)"
echo ""

# Get initial counts
LAST_REVIEW_COUNT=$(gh api $REPO_FLAG repos/:owner/:repo/pulls/$PR_NUMBER/reviews --jq 'length' 2>/dev/null || echo 0)
LAST_COMMENT_COUNT=$(gh api $REPO_FLAG repos/:owner/:repo/pulls/$PR_NUMBER/comments --jq 'length' 2>/dev/null || echo 0)
LAST_PR_COMMENT_COUNT=$(gh pr view "$PR_NUMBER" $REPO_FLAG --json comments --jq '.comments | length' 2>/dev/null || echo 0)

echo "Initial state: $LAST_REVIEW_COUNT reviews, $LAST_COMMENT_COUNT inline comments, $LAST_PR_COMMENT_COUNT PR comments"
echo ""

while true; do
    # Check CI status
    echo "--- CI Status ($(date +%H:%M:%S)) ---"
    gh pr checks $PR_NUMBER $REPO_FLAG 2>/dev/null || echo "Failed to fetch checks"

    # Check for new reviews
    CURRENT_REVIEW_COUNT=$(gh api $REPO_FLAG repos/:owner/:repo/pulls/$PR_NUMBER/reviews --jq 'length' 2>/dev/null || echo 0)
    if [[ "$CURRENT_REVIEW_COUNT" -gt "$LAST_REVIEW_COUNT" ]]; then
        echo ""
        echo "!!! NEW REVIEWS DETECTED !!!"
        echo "Reviews: $LAST_REVIEW_COUNT -> $CURRENT_REVIEW_COUNT"
        LAST_REVIEW_COUNT=$CURRENT_REVIEW_COUNT
    fi

    # Check for new inline comments
    CURRENT_COMMENT_COUNT=$(gh api $REPO_FLAG repos/:owner/:repo/pulls/$PR_NUMBER/comments --jq 'length' 2>/dev/null || echo 0)
    if [[ "$CURRENT_COMMENT_COUNT" -gt "$LAST_COMMENT_COUNT" ]]; then
        echo ""
        echo "!!! NEW REVIEW COMMENTS DETECTED !!!"
        echo "Comments: $LAST_COMMENT_COUNT -> $CURRENT_COMMENT_COUNT"
        LAST_COMMENT_COUNT=$CURRENT_COMMENT_COUNT
    fi

    # Check for new PR comments (where Gemini posts quota warnings)
    CURRENT_PR_COMMENT_COUNT=$(gh pr view "$PR_NUMBER" $REPO_FLAG --json comments --jq '.comments | length' 2>/dev/null || echo 0)
    if [[ "$CURRENT_PR_COMMENT_COUNT" -gt "$LAST_PR_COMMENT_COUNT" ]]; then
        echo ""
        echo "--- New PR comment detected, checking for quota warning ---"
        LAST_PR_COMMENT_COUNT=$CURRENT_PR_COMMENT_COUNT

        # Check if Gemini hit quota
        if ! "$SCRIPT_DIR/check-gemini-quota.sh" "$PR_NUMBER" > /dev/null 2>&1; then
            echo ""
            echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            echo "!!! GEMINI QUOTA EXCEEDED - FALLBACK TO CLAUDE !!!"
            echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            echo ""
            echo "Gemini Code Assist has hit its daily quota limit."
            echo "Use claude-review.sh to perform code review instead:"
            echo ""
            echo "  ~/.claude/skills/pr-review-loop/scripts/claude-review.sh $PR_NUMBER"
            echo ""
        fi
    fi

    echo ""
    sleep 30
done
