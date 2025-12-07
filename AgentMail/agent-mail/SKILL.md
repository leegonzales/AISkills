---
name: agent-mail
description: Coordinate with other AI agents via project-local Maildir messaging. Use when operating in tandem mode with Claude, Gemini, or other agents. Enables claiming tasks, reporting completion, handling blocks, and synchronizing work across terminals.
---

# Agent Mail

Project-local messaging system for multi-agent coordination. Email semantics for AI agents working together.

## When to Use

Invoke when:
- Operating in **tandem mode** with other AI agents (Claude + Gemini, multiple Claudes)
- Starting a session and need to check for messages from partners
- Claiming a task and need to notify other agents
- Completing work and need to report handoff
- Blocked and need to notify partners urgently
- Need to coordinate or synchronize work across terminals

## Pre-requisites

**Check if agent-mail is initialized:**
```bash
ls .agent-mail/  # Should exist in project root
```

**If not initialized:**
```bash
npx tsx ~/Projects/leegonzales/agent-mail/src/mail.ts init
```

## Core Rituals (MANDATORY)

### 1. Session Start

**Before ANY work**, join and check inbox:

```bash
agent-mail join claude
agent-mail check claude
```

If unread messages exist:
```bash
agent-mail read claude
```

Process all messages before proceeding.

### 2. Before Claiming Work

Notify partners before starting any task:

```bash
agent-mail broadcast claude "Claiming Task" "Claiming IE-XX. Starting now."
```

### 3. After Completing Work

Report completion immediately:

```bash
agent-mail broadcast claude "Task Complete" "IE-XX complete. Output at: path/to/result"
```

### 4. When Blocked

Notify with HIGH priority:

```bash
agent-mail send claude gemini "BLOCKED" "IE-XX blocked: reason" --priority high
```

### 5. Periodic Check-in

For long tasks (>5 minutes):

```bash
agent-mail broadcast claude "Status Update" "Still on IE-XX. 60% complete."
```

## Message Types

| Subject | Purpose |
|---------|---------|
| `Claiming Task` | Announcing you're taking a task |
| `Task Complete` | Work finished, ready for handoff |
| `BLOCKED` | Cannot proceed, need help |
| `Status Update` | Progress on long task |
| `Question` | Need clarification |
| `Answer` | Responding to question |
| `Handoff` | Explicitly passing work |
| `Sync Request` | Asking for partner status |

## Quick Reference

```bash
# Project
agent-mail init                    # Initialize in current project
agent-mail join claude             # Register as agent
agent-mail who                     # See active agents
agent-mail info                    # Project info

# Messaging
agent-mail check claude            # Peek inbox (no mark)
agent-mail read claude             # Read + mark as read
agent-mail send claude gemini "Subject" "Body"
agent-mail broadcast claude "Subject" "Body"
agent-mail reply claude <id> "Body"
agent-mail status                  # All inboxes
agent-mail history claude 10       # Message history
```

## Integration with Beads

When using beads task tracking:

1. **Claim in beads first**, then notify:
   ```bash
   bd update IE-XX --status in_progress --assignee Claude
   agent-mail broadcast claude "Claiming Task" "Claimed IE-XX in beads"
   ```

2. **Close in beads**, then notify:
   ```bash
   bd close IE-XX "Completed"
   agent-mail broadcast claude "Task Complete" "IE-XX closed"
   ```

## Examples

See `references/examples.md` for full conversation examples.
