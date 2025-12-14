#!/bin/bash
# Resolve (minimize/hide) a PR review comment thread
# Usage: resolve-comment.sh <comment-node-id> ["reason"]
#
# Note: GitHub's GraphQL API is needed to resolve comments.
# The node_id (not numeric id) is required.

set -euo pipefail

NODE_ID="${1:?Usage: resolve-comment.sh <comment-node-id> [\"reason\"]}"
REASON="${2:-RESOLVED}"

# Valid reasons: ABUSE, OFF_TOPIC, OUTDATED, RESOLVED, SPAM
case "$REASON" in
    RESOLVED|OUTDATED|OFF_TOPIC|ABUSE|SPAM) ;;
    *)
        echo "Invalid reason. Must be: RESOLVED, OUTDATED, OFF_TOPIC, ABUSE, or SPAM"
        exit 1
        ;;
esac

echo "Resolving comment $NODE_ID as $REASON..."

gh api graphql -f query="
mutation {
    minimizeComment(input: {subjectId: \"$NODE_ID\", classifier: $REASON}) {
        minimizedComment {
            isMinimized
            minimizedReason
        }
    }
}"

echo "Comment resolved."
