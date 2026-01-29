# Context Continuity

**High-fidelity context transfer protocol for moving conversations between AI agents.**

## Overview

When conversations need to transfer between AI agents or sessions, context is typically lost through naive copy-paste. This protocol creates structured artifacts that preserve decision tempo, maintain forward momentum, and gracefully degrade under truncation.

## Key Features

- Automatic mode selection (Minimal ~200 words, Full ~1000 words)
- Preserves decisions, open loops, and next actions
- Separates fact from interpretation
- Supports both human and machine parsing
- Graceful degradation under context limits

## Usage

Trigger with phrases like:
- "Transfer this conversation"
- "Continue this elsewhere"
- "Create a handoff"
- "Summarize for transfer"

Does NOT activate on general "summarize" requests without transfer intent.

## Installation

### Claude Code
```bash
cp -r /path/to/AISkills/ContextContinuity/context-continuity ~/.claude/skills/
```

### Claude Web Chat
Upload the `.skill` file from `dist/` to claude.ai > Settings > Capabilities.

## Files

```
context-continuity/
├── SKILL.md        # Core skill definition
├── README.md       # This file
├── references/     # Transfer templates and protocols
└── scripts/        # Helper scripts
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
