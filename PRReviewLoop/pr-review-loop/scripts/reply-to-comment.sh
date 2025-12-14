#!/bin/bash
# Reply to a PR review comment and resolve the thread
# Usage: reply-to-comment.sh <pr-number> <comment-id> "reply message" [--no-resolve]
#
# Comment IDs can be found in the output of get-review-comments.sh --with-ids
# By default, resolves the conversation after replying. Use --no-resolve to skip.

set -euo pipefail

PR_NUMBER="${1:?Usage: reply-to-comment.sh <pr-number> <comment-id> \"reply message\" [--no-resolve]}"
COMMENT_ID="${2:?Usage: reply-to-comment.sh <pr-number> <comment-id> \"reply message\" [--no-resolve]}"
REPLY="${3:?Usage: reply-to-comment.sh <pr-number> <comment-id> \"reply message\" [--no-resolve]}"
NO_RESOLVE="${4:-}"

# Get repo info
REPO=$(gh repo view --json nameWithOwner --jq '.nameWithOwner')
OWNER=$(echo "$REPO" | cut -d'/' -f1)
REPO_NAME=$(echo "$REPO" | cut -d'/' -f2)

echo "Replying to comment $COMMENT_ID on PR #$PR_NUMBER..."

# Post the reply
gh api \
    --method POST \
    "repos/$REPO/pulls/$PR_NUMBER/comments/$COMMENT_ID/replies" \
    -f body="$REPLY" > /dev/null

echo "Reply posted."

# Resolve the thread unless --no-resolve is specified
if [[ "$NO_RESOLVE" != "--no-resolve" ]]; then
    echo "Resolving thread..."

    # Get thread ID by finding the thread that contains this comment
    THREAD_ID=$(gh api graphql -f query="
        query(\$owner: String!, \$repo: String!, \$pr: Int!) {
            repository(owner: \$owner, name: \$repo) {
                pullRequest(number: \$pr) {
                    reviewThreads(first: 100) {
                        nodes {
                            id
                            comments(first: 1) {
                                nodes {
                                    databaseId
                                }
                            }
                        }
                    }
                }
            }
        }
    " -f owner="$OWNER" -f repo="$REPO_NAME" -F pr="$PR_NUMBER" \
    --jq ".data.repository.pullRequest.reviewThreads.nodes[] | select(.comments.nodes[0].databaseId == $COMMENT_ID) | .id" 2>/dev/null || echo "")

    if [[ -n "$THREAD_ID" && "$THREAD_ID" != "null" ]]; then
        gh api graphql -f query="
            mutation(\$threadId: ID!) {
                resolveReviewThread(input: {threadId: \$threadId}) {
                    thread {
                        isResolved
                    }
                }
            }
        " -f threadId="$THREAD_ID" > /dev/null 2>&1 && echo "Thread resolved." || echo "Warning: Could not resolve thread."
    else
        echo "Warning: Could not find thread ID to resolve."
    fi
fi
