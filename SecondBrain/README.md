# Second Brain Skill

A Claude Code skill for the Second Brain personal intelligence system.

## Overview

This skill enables conversational capture and querying of your personal knowledge base directly from Claude Code sessions. Capture thoughts as they emerge, query past decisions, and stay on top of your priorities without breaking flow.

## Features

- **Capture**: Add thoughts, tasks, and notes naturally during conversation
- **Query**: Search your knowledge graph with natural language
- **Inbox**: Review items awaiting classification
- **Digest**: Get actionable daily summaries
- **Actions**: Mark tasks complete, update priorities

## Usage

In Claude Code, the skill activates when you:
- Say "remember this...", "add a task...", "note that..."
- Ask "what did I say about...", "show my inbox", "what's my digest"
- Request "/sb capture", "/sb inbox", "/sb digest"

## Requirements

- Second Brain CLI installed (`pip install -e /path/to/SecondBrain`)
- Anthropic API key configured
- Obsidian vault path set

## Quick Start

```bash
# In SecondBrain project directory
pip install -e .
sb init
sb capture "Test capture"
sb inbox
```

## Related

- [SecondBrain Project](../../../SecondBrain) - The core system
- [Architecture Docs](../../../SecondBrain/ARCHITECTURE.md) - Technical design

## License

MIT
