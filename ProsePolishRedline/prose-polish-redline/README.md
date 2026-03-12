# Prose Polish Redline

**Composable agent pipeline that produces tracked-changes .docx and animated HTML replay from parallel prose-editing agents.**

## Overview

Prose Polish Redline runs 7-9 focused editing agents in parallel across two phases -- structure first (coherence, authority, claims, stakes), then style (rhythm, hedges, personality, perspective). A merge engine deduplicates, resolves conflicts, and rebases Phase 2 edits to original coordinates. Output is a Word document with tracked changes and an animated HTML replay showing edits tier-by-tier.

## Key Features

- 9 specialized kata agents across 5 editing tiers
- Genre-aware scoring and calibration (academic, technical, business, creative, personal, journalistic)
- Two-phase pipeline: structural edits before stylistic refinement
- Merge engine with deduplication, conflict resolution, and Phase 2 rebasing
- Tracked-changes `.docx` output (open in Word/Pages/Google Docs)
- Animated HTML replay with tier-by-tier visualization
- Per-agent match rate diagnostics for prompt tuning
- Three depth levels (conservative/moderate/aggressive) and dry-run mode

## Usage

```
/prose-polish-redline path/to/essay.md
/prose-polish-redline path/to/essay.md --depth aggressive
/prose-polish-redline path/to/essay.md --depth conservative --genre academic
/prose-polish-redline path/to/essay.md --dry-run
```

## Installation

### Claude Code
```bash
cp -r /path/to/AISkills/ProsePolishRedline/prose-polish-redline ~/.claude/skills/
```

### Dependencies
```bash
pip install python-docx
```

## Files

```
prose-polish-redline/
├── SKILL.md                    # Orchestrator pipeline
├── README.md                   # This file
├── agents/                     # 9 kata agents (genre-scorer + 4 Phase 1 + 4 Phase 2)
├── references/                 # Edit schema, tier mapping, genre calibration
└── scripts/                    # 5 Python scripts + HTML template
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
