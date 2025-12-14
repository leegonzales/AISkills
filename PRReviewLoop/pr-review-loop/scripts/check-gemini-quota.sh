#!/bin/bash
# Check if Gemini Code Assist has hit its daily quota on a PR
# Usage: check-gemini-quota.sh <pr-number>
#
# Checks the last comment from gemini-code-assist to see if it's a quota warning.
# This should be called after triggering a review to detect rate limiting.
#
# Returns:
#   0 (success) if Gemini is available (no quota warning detected)
#   1 if Gemini is rate-limited
#
# Output: JSON with status and details

set -euo pipefail

PR_NUMBER="${1:?Usage: check-gemini-quota.sh <pr-number>}"

# Get the most recent comment from gemini-code-assist
LAST_GEMINI_COMMENT=$(gh pr view "$PR_NUMBER" --json comments --jq '
    [.comments[] | select(.author.login == "gemini-code-assist")] |
    sort_by(.createdAt) |
    last |
    {body: .body, createdAt: .createdAt}
' 2>/dev/null || echo "{}")

if [[ -z "$LAST_GEMINI_COMMENT" || "$LAST_GEMINI_COMMENT" == "{}" || "$LAST_GEMINI_COMMENT" == "null" ]]; then
    echo '{"status": "available", "reason": "no gemini comments found"}'
    exit 0
fi

# Check if the last comment contains the quota warning
BODY=$(echo "$LAST_GEMINI_COMMENT" | jq -r '.body // ""')

if echo "$BODY" | grep -qi "reached your daily quota limit"; then
    CREATED_AT=$(echo "$LAST_GEMINI_COMMENT" | jq -r '.createdAt // "unknown"')
    echo "{\"status\": \"rate-limited\", \"reason\": \"quota exceeded\", \"detected_at\": \"$CREATED_AT\"}"
    exit 1
else
    echo '{"status": "available", "reason": "no quota warning in last comment"}'
    exit 0
fi
