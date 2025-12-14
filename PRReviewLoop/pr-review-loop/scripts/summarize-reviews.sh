#!/bin/bash
# Summarize review comments by priority and file
# Usage: summarize-reviews.sh <pr-number> [--all]
#
# Options:
#   --all    Include resolved threads (default: unresolved only)

set -euo pipefail

PR_NUMBER="${1:?Usage: summarize-reviews.sh <pr-number> [--all]}"
INCLUDE_RESOLVED=false

for arg in "$@"; do
    if [[ "$arg" == "--all" ]]; then
        INCLUDE_RESOLVED=true
    fi
done

# Get repo info
REPO=$(gh repo view --json nameWithOwner --jq '.nameWithOwner')
OWNER=$(echo "$REPO" | cut -d'/' -f1)
REPO_NAME=$(echo "$REPO" | cut -d'/' -f2)

echo "=== PR #$PR_NUMBER Review Summary ==="
echo ""

# Use GraphQL to get review threads with resolution status
QUERY='
query($owner: String!, $repo: String!, $pr: Int!) {
  repository(owner: $owner, name: $repo) {
    pullRequest(number: $pr) {
      reviewThreads(first: 100) {
        nodes {
          isResolved
          comments(first: 1) {
            nodes {
              path
              line
              originalLine
              body
            }
          }
        }
      }
    }
  }
}
'

RESULT=$(gh api graphql -f query="$QUERY" -f owner="$OWNER" -f repo="$REPO_NAME" -F pr="$PR_NUMBER" 2>/dev/null)

if [[ -z "$RESULT" ]]; then
    echo "No review comments."
    exit 0
fi

# Extract comments based on resolution filter
COMMENTS=$(echo "$RESULT" | jq --argjson resolved "$INCLUDE_RESOLVED" '
    [.data.repository.pullRequest.reviewThreads.nodes[] |
     select($resolved or .isResolved == false) |
     .comments.nodes[0] |
     select(. != null)]
')

if [[ "$COMMENTS" == "[]" ]]; then
    if [[ "$INCLUDE_RESOLVED" == "false" ]]; then
        echo "No unresolved review comments."
    else
        echo "No review comments."
    fi
    exit 0
fi

# Count by priority
echo "## By Priority"
echo "$COMMENTS" | jq -r '
    group_by(.body | capture("!\\[(?<p>high|medium|low)\\]") | .p // "unknown") |
    .[] |
    "- \(.[0].body | capture("!\\[(?<p>high|medium|low)\\]") | .p // "unknown"): \(length) comments"
'
echo ""

# Group by file
echo "## By File"
echo "$COMMENTS" | jq -r '
    group_by(.path) |
    .[] |
    "- \(.[0].path): \(length) comments"
'
echo ""

# List high priority items
echo "## High Priority Items"
echo "$COMMENTS" | jq -r '
    .[] |
    select(.body | test("!\\[high\\]")) |
    "- [\(.path):\(.line // .originalLine // "?")] \(.body | split("\n")[0] | gsub("!\\[high\\]\\([^)]+\\)"; "") | .[0:80])"
'
