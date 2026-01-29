# Second Brain

**Personal intelligence system for capturing thoughts, managing knowledge, and surfacing insights.**

## Overview

Conversational interface to a personal knowledge management system. Capture thoughts naturally during Claude Code sessions without breaking flow, query past decisions and notes, and manage your inbox and task status.

## Key Features

- Natural language capture of thoughts, tasks, ideas, and references
- AI-powered classification (task, idea, reference, meeting, goal, project, value, person)
- Knowledge graph querying for past decisions and notes
- Inbox management with review queue
- Daily digest and priority surfacing

## Usage

Trigger with phrases like:
- "Remember that..."
- "Add a task to..."
- "What did I say about...?"
- "Show my inbox"
- "Mark complete"

## Installation

### Claude Code
```bash
cp -r /path/to/AISkills/SecondBrain/second-brain ~/.claude/skills/
```

### Claude Web Chat
Upload the `.skill` file from `dist/` to claude.ai > Settings > Capabilities.

## Files

```
second-brain/
├── SKILL.md        # Core skill definition
├── README.md       # This file
└── references/     # Knowledge management protocols
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
