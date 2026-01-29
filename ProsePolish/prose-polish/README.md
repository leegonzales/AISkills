# Prose Polish

**Evaluate and elevate writing effectiveness through multi-dimensional quality assessment.**

## Overview

Prose Polish analyzes writing across six dimensions -- craft, coherence, authority, purpose, voice, and effectiveness -- with genre-calibrated thresholds. The goal is genuinely better writing, not just "less AI-sounding" text.

## Key Features

- Six-dimension quality scoring (0-100 each)
- Genre-aware evaluation (technical, business, academic, creative, personal, journalistic)
- Three modes: Detection/Analysis, Elevation, and Prevention
- Specific remediation strategies per dimension
- Prevention prompts for generating quality content from scratch

## Usage

Trigger with phrases like:
- "Analyze this writing"
- "Polish this draft"
- "Score this text"
- "Help me write better"
- "Evaluate my essay"

## Installation

### Claude Code
```bash
cp -r /path/to/AISkills/ProsePolish/prose-polish ~/.claude/skills/
```

### Claude Web Chat
Upload the `.skill` file from `dist/` to claude.ai > Settings > Capabilities.

## Files

```
prose-polish/
├── SKILL.md        # Core skill definition
├── README.md       # This file
└── references/     # Detection patterns, remediation strategies
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
