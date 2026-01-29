# Codex Peer Review

**Leverage OpenAI's Codex CLI for AI peer review and cross-validation from Claude Code.**

## Overview

Enables Claude Code to call OpenAI's Codex CLI for a second AI perspective on architecture decisions, security reviews, and design trade-offs. Two AI perspectives are better than one for high-stakes decisions.

## Key Features

- Architecture validation and critique via Codex CLI
- Design decision cross-validation between Claude and Codex
- Security, performance, and testing analysis
- Alternative approach generation
- Structured review protocols (quick, standard, deep)

## Usage

Claude Code only. Invoke with:
- "Get a second opinion on this architecture"
- "Run a peer review with Codex"
- `skill: codex-peer-review`

Requires Codex CLI installed and configured.

## Installation

### Claude Code
```bash
cp -r /path/to/AISkills/CodexPeerReview/codex-peer-review ~/.claude/skills/
```

Requires: `npm install -g @openai/codex` and `OPENAI_API_KEY` set.

## Files

```
codex-peer-review/
├── SKILL.md        # Core skill definition
├── README.md       # This file
├── references/     # Additional documentation
└── LICENSE.txt     # License terms
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
