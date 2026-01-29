# Profile Builder

**Build your Claude personalization profile through guided Q&A.**

## Overview

Generates personalized Claude profile text through a structured four-mode interview process. Output is ready to paste into Claude's Settings > Profile > Personal Preferences, customizing how Claude responds across all conversations.

## Key Features

- Guided interview covering identity, communication style, frameworks, and preferences
- Four sequential modes: Discovery, Interview, Generation, Calibration
- Output formatted for direct paste into Claude settings
- Template escape hatch for quick setup
- Handles both new profiles and updates to existing ones

## Usage

Trigger with phrases like:
- "Build my Claude profile"
- "Help me write my personal preferences"
- "How do I customize Claude for me?"
- "I want Claude to know who I am"

## Installation

### Claude Code
```bash
cp -r /path/to/AISkills/ProfileBuilder/profile-builder ~/.claude/skills/
```

### Claude Web Chat
Upload the `.skill` file from `dist/` to claude.ai > Settings > Capabilities.

## Files

```
profile-builder/
├── SKILL.md        # Core skill definition
├── README.md       # This file
└── references/     # Interview guides, example profiles
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
