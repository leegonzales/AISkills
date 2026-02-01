# Fabric Patterns Skill

A Claude Code skill for running [danielmiessler/fabric](https://github.com/danielmiessler/fabric) patterns — 240+ curated AI prompts for content analysis, extraction, summarization, writing, security analysis, and more.

## Prerequisites

- [fabric](https://github.com/danielmiessler/fabric) installed via Go:
  ```bash
  go install github.com/danielmiessler/fabric/cmd/fabric@latest
  ```
- At least one LLM provider configured (`fabric -S` to set up)
- Patterns updated: `fabric -U`

## Installation

```bash
# Symlink into Claude Code skills directory
# From within this directory, run:
ln -sf "$(pwd)" ~/.claude/skills/fabric-patterns
```

## What It Does

This skill teaches Claude Code when and how to shell out to fabric's CLI, including:

- **Pattern selection** — dual-judgment routing (Claude's pick + fabric's `suggest_pattern`)
- **Input piping** — stdin, files, URLs, YouTube, Spotify, audio transcription
- **Output handling** — streaming, file output, clipboard, pattern chaining
- **Session management** — persistent conversations and contexts

## Structure

```
fabric-patterns/
  SKILL.md              # Core skill definition
  README.md             # This file
  references/
    pattern-catalog.md  # Full pattern listing by category
    piping-idioms.md    # CLI reference and piping conventions
```

## Quick Examples

```bash
# Extract wisdom from an article
fabric -u "https://example.com/article" -p extract_wisdom

# Summarize a YouTube video
fabric -y "https://youtube.com/watch?v=..." -p summarize

# Chain patterns
cat paper.md | fabric -p extract_wisdom | fabric -p summarize

# Security threat model
cat system.md | fabric -p create_stride_threat_model
```
