# Claude Speak

High-quality text-to-speech skill for Claude using MLX-Audio (Kokoro TTS) on Apple Silicon.

## Overview

Lets Claude speak text aloud with natural-sounding AI voice synthesis. Uses a daemon architecture for instant response after initial model load.

## Prerequisites

- macOS with Apple Silicon (M1/M2/M3)
- Python 3.10+ (native ARM, not Rosetta)
- espeak-ng (`brew install espeak-ng`)

## Installation

The tool is installed at `~/Projects/claude-speak/` with:
- Virtual environment with all dependencies
- Daemon for hot model loading
- Launchd service for auto-start

## Architecture

```
┌─────────────┐     Unix Socket     ┌─────────────────┐
│   Client    │ ──────────────────▶ │     Daemon      │
│ (instant)   │                     │ (model loaded)  │
└─────────────┘                     └─────────────────┘
                                           │
                                           ▼
                                    ┌─────────────────┐
                                    │  Kokoro TTS     │
                                    │  (MLX-Audio)    │
                                    └─────────────────┘
```

## Usage

```bash
# Speak text (daemon must be running)
~/Projects/claude-speak/.venv/bin/claude-speak-client "Hello world"

# Check daemon
~/Projects/claude-speak/.venv/bin/claude-speak-daemon status
```

## Voices

Default: `bm_george` (British male, distinguished)

See SKILL.md for full voice list.

## Related

- Project source: `~/Projects/claude-speak/`
- Launchd plist: `~/Library/LaunchAgents/com.claude-speak.daemon.plist`
- Logs: `/tmp/claude-speak.log`
