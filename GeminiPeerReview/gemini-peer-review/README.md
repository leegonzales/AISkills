# Gemini Peer Review

**Leverage Google's Gemini CLI for AI peer review and cross-validation from Claude Code.**

## Overview

Enables Claude Code to call Google's Gemini CLI for a second AI perspective on architecture, security, and design decisions. Gemini's 1M token context window allows processing entire codebases without chunking, complementing Claude's detailed reasoning.

## Key Features

- Architecture validation via Gemini CLI
- Design decision cross-validation between Claude and Gemini
- Holistic codebase analysis using 1M token context window
- Security, performance, and testing reviews
- Multimodal analysis support (diagrams, PDFs, designs)

## Usage

Claude Code only. Invoke with:
- "Get Gemini's take on this"
- "Run a peer review with Gemini"
- `skill: gemini-peer-review`

Requires Gemini CLI installed and configured.

## Installation

### Claude Code
```bash
cp -r /path/to/AISkills/GeminiPeerReview/gemini-peer-review ~/.claude/skills/
```

Requires: Gemini CLI installed and `GEMINI_API_KEY` set.

## Files

```
gemini-peer-review/
├── SKILL.md        # Core skill definition
├── README.md       # This file
├── references/     # Additional documentation
└── LICENSE.txt     # License terms
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
