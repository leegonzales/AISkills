# Agent Mail Skill

Project-local Maildir-based messaging for AI agent coordination.

## Overview

When multiple AI agents (Claude, Gemini, multiple Claude instances) work on the same project in separate terminals, they need reliable communication. Agent Mail provides email-like semantics:

- Each agent has an inbox
- Messages are persistent `.eml` files
- Project isolation (each project has its own `.agent-mail/`)
- Multi-instance support (`claude-1`, `claude-2`, etc.)

## Features

- **Session rituals** - Join, check inbox, process messages before work
- **Task coordination** - Claim, complete, block, handoff
- **Priority messaging** - Normal, high, urgent
- **Broadcast** - Message all agents at once
- **Beads integration** - Works alongside task tracking

## When to Use

- Operating in tandem mode with other AI agents
- Starting a session (check for partner messages)
- Claiming tasks (notify to avoid conflicts)
- Completing work (report for handoff)
- Blocked (urgent notification)
- Long tasks (periodic status updates)

## Example Usage

**Session start:**
```bash
agent-mail join claude
agent-mail check claude
# If messages: agent-mail read claude
```

**Claiming work:**
```bash
agent-mail broadcast claude "Claiming Task" "Starting IE-34"
```

**Completion:**
```bash
agent-mail broadcast claude "Task Complete" "IE-34 done. Tests pass."
```

## Installation

The skill references the agent-mail CLI at:
```
~/Projects/leegonzales/agent-mail/src/mail.ts
```

Set up an alias:
```bash
alias agent-mail='npx tsx ~/Projects/leegonzales/agent-mail/src/mail.ts'
```

## Version

- **Version:** 1.0.0
- **Author:** Lee Gonzales
- **License:** MIT
