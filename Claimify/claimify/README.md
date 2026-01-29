# Claimify

**Extract and structure claims from discourse into analyzable argument maps.**

## Overview

Claimify transforms messy discourse -- conversations, documents, debates, meeting notes -- into structured claim networks. It identifies atomic claims, classifies them by type, maps logical relationships, and surfaces contradictions, assumptions, and gaps.

## Key Features

- Extracts atomic, testable claims from any text source
- Classifies claims as factual, normative, definitional, causal, or predictive
- Maps relationships: supports, opposes, assumes, contradicts
- Identifies implicit assumptions and argument gaps
- Outputs as table, graph, narrative, or JSON

## Usage

Trigger with phrases like:
- "What are the claims in this?"
- "Analyze this argument"
- "Map the logic"
- "Find contradictions"

## Installation

### Claude Code
```bash
cp -r /path/to/AISkills/Claimify/claimify ~/.claude/skills/
```

### Claude Web Chat
Upload the `.skill` file from `dist/` to claude.ai > Settings > Capabilities.

## Files

```
claimify/
├── SKILL.md        # Core skill definition
├── README.md       # This file
├── references/     # Additional documentation
└── scripts/        # Helper scripts
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
