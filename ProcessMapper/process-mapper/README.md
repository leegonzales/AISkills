# Process Mapper

**Map workflows, extract SOPs, and identify automation opportunities.**

## Overview

Systematic workflow for discovering, documenting, and analyzing processes. Implements the SOP-first doctrine: "You can't automate what you can't see." Captures shadow processes and tacit knowledge, then assesses AI tractability for automation opportunities.

## Key Features

- Process discovery interviews with structured methodology
- SOP state diagnosis (Fiction, Nonexistent, Accurate)
- Shadow process and tacit knowledge capture
- AI tractability assessment for automation readiness
- Multiple output formats (flowcharts, decision trees, RACI matrices)

## Usage

Trigger with phrases like:
- "Map this workflow"
- "Document the SOP for..."
- "Where can we apply AI to this process?"
- "Interview me about how this works"

## Installation

### Claude Code
```bash
cp -r /path/to/AISkills/ProcessMapper/process-mapper ~/.claude/skills/
```

### Claude Web Chat
Upload the `.skill` file from `dist/` to claude.ai > Settings > Capabilities.

## Files

```
process-mapper/
├── SKILL.md        # Core skill definition
├── README.md       # This file
└── references/     # Discovery methodology, assessment frameworks
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
