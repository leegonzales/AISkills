# Context Continuity - Code Edition

**Transfer development context between Claude Code sessions with high fidelity.**

## Overview

Captures code state, git context, running services, and development decisions when moving work between Claude Code sessions. Designed for development workflows where preserving technical context is critical.

## Key Features

- Captures files modified, git branch/status, staged/unstaged changes
- Records technical decisions and rejected alternatives
- Tracks running services, ports, and environment state
- Documents open loops, blockers, and pending reviews
- Integrates with peer review skills (Codex/Gemini)

## Usage

Trigger when you need to:
- Continue development in a fresh Claude Code session
- Hand off work to another developer
- Resume after context window fills
- Document state before major refactoring

## Installation

### Claude Code
```bash
cp -r /path/to/AISkills/ContextContinuityCode/context-continuity-code ~/.claude/skills/
```

## Files

```
context-continuity-code/
├── SKILL.md        # Core skill definition
├── README.md       # This file
└── references/     # Transfer templates
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
