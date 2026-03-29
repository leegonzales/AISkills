# requesting-code-review

Dispatch three independent reviewers in parallel for multi-perspective code review. Three perspectives catch more than one.

## Installation

This is a Claude Code skill. Add it to your Claude Code configuration to invoke when completing tasks or before merging.

## Reviewers

| Reviewer | Tool | Strengths |
|----------|------|-----------|
| Claude subagent | `superpowers:code-reviewer` | Deep reasoning, plan compliance |
| Codex CLI | `codex review --base <SHA>` | Line-level bugs, concise output |
| Gemini CLI | `cat <<'EOF' \| gemini` | Holistic view, large context (1M tokens) |

## Usage

Invoke when:
- Completing a major feature implementation
- Before merging a branch
- After significant refactoring
- When you want confidence before shipping

All three reviewers run simultaneously. Results are synthesized into a unified review with deduplicated findings.
