# Nano Banana Pro Skill

A Claude Code skill for generating and editing high-quality AI images using Google's Gemini 3 Pro Image model (Nano Banana Pro) via MCP.

## Overview

"Nano Banana" is the community nickname for Google's Gemini image generation models:
- **Nano Banana Pro** (Gemini 3 Pro Image) - Highest quality, 4K output
- **Nano Banana** (Gemini 2.5 Flash Image) - Faster, lower cost

This skill teaches Claude how to effectively use Nano Banana MCP servers for image generation, providing prompting best practices and example workflows.

## Features

- Step-by-step MCP server setup
- Prompting framework (SCTD: Subject → Context → Technique → Details)
- Style keyword reference
- Text rendering techniques
- Character consistency across images
- 50+ example prompts by category

## Quick Start

1. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/)
2. Install MCP server:
   ```bash
   claude mcp add nano-banana --env GEMINI_API_KEY=your-key -- npx -y nanobanana-mcp
   ```
3. Install this skill:
   ```bash
   claude skill add /path/to/nano-banana
   ```

## Skill Structure

```
nano-banana/
├── SKILL.md                      # Main skill file
├── CHANGELOG.md                  # Version history
└── references/
    ├── prompting-guide.md        # Advanced prompting techniques
    └── examples.md               # Copy-paste ready prompts
```

## Use Cases

- Marketing graphics and social media content
- Product photography mockups
- UI/UX design assets
- Concept art and illustrations
- Infographics and diagrams
- Photo editing and style transfer

## Requirements

- Claude Code with MCP support
- Gemini API key (free tier available)
- Node.js 18+ (for npx)

## License

MIT

## Credits

- MCP Servers: [YCSE/nanobanana-mcp](https://github.com/YCSE/nanobanana-mcp), [ConechoAI/Nano-Banana-MCP](https://github.com/ConechoAI/Nano-Banana-MCP)
- Model: Google DeepMind Gemini 3 Pro Image
