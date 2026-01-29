# Presentation Partner

**Collaborative presentation authoring through structured interview and voice calibration.**

## Overview

Transforms AI from slide generator into presentation collaborator. Interviews to extract real insight and story, tracks narrative threads for coherence, and drafts Talk Track v5 format with calibrated narration voice.

## Key Features

- Discovery mode: structured interview to surface core insights
- Thread tracking for narrative coherence across slides
- Talk Track v5 format output with speaker notes and narration
- Voice calibration for authentic delivery style
- Conversion of existing slides/outlines to talk tracks

## Usage

Trigger with phrases like:
- "Let's create a presentation about..."
- "Help me with my talk on..."
- "Convert this outline to a talk track"
- "Interview me about my presentation"

## Installation

### Claude Code
```bash
cp -r /path/to/AISkills/PresentationPartner/presentation-partner ~/.claude/skills/
```

### Claude Web Chat
Upload the `.skill` file from `dist/` to claude.ai > Settings > Capabilities.

## Files

```
presentation-partner/
├── SKILL.md        # Core skill definition
├── README.md       # This file
├── references/     # Talk Track format, voice profiles
└── integrations/   # External tool integrations
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
