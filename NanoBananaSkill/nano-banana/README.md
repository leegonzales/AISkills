# Nano Banana Pro

**Generate and edit high-quality AI images using Google's Gemini 3 Pro Image model via MCP.**

## Overview

Nano Banana Pro enables image generation up to 4K resolution, photo editing, and graphics creation with accurate text rendering. It uses Google's Gemini 3 Pro Image model through the NanoBanana MCP server.

## Key Features

- 4K image generation with multiple aspect ratios
- Photo editing with natural language instructions
- Accurate text rendering for logos, infographics, diagrams
- Consistent character generation across images
- Iterative editing with conversation history

## Usage

Trigger with phrases like:
- "Generate an image of..."
- "Edit this photo"
- "Create a logo with text"
- "Visualize this concept"

Requires a Gemini API key and NanoBanana MCP server.

## Installation

### Claude Code
```bash
# Install MCP server
claude mcp add nano-banana --env GEMINI_API_KEY=your-key -- npx -y nanobanana-mcp

# Install skill
cp -r /path/to/AISkills/NanoBananaSkill/nano-banana ~/.claude/skills/
```

## Files

```
nano-banana/
├── SKILL.md        # Core skill definition
├── README.md       # This file
└── references/     # Prompt engineering guides
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
