# Excel Auditor

**Analyze unknown Excel files to understand purpose, audit formulas, and assess risk.**

## Overview

Excel Auditor reverse-engineers inherited or undocumented spreadsheets. It extracts structure and formulas, performs semantic analysis to infer purpose, detects errors and risks, and generates comprehensive documentation.

## Key Features

- Automated structure and formula extraction via Python scripts
- Purpose detection matching against known archetypes (financial models, trackers, dashboards)
- Formula error detection and dependency graph analysis
- Maintainability risk scoring
- Generated documentation and audit reports

## Usage

Trigger when:
- "What does this spreadsheet do?"
- "Audit this Excel file"
- Working with inherited/legacy spreadsheets
- Need formula error detection or risk assessment

## Installation

### Claude Code
```bash
cp -r /path/to/AISkills/ExcelAuditor/excel-auditor ~/.claude/skills/
```

### Claude Web Chat
Upload the `.skill` file from `dist/` to claude.ai > Settings > Capabilities.

## Files

```
excel-auditor/
├── SKILL.md        # Core skill definition
├── README.md       # This file
├── references/     # Pattern library, risk scoring
└── scripts/        # Python extraction scripts
```

## Part of [AISkills](https://github.com/leegonzales/AISkills)
