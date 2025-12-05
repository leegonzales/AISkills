---
name: excel-auditor
description: "Analyze unknown or inherited Excel files to understand what they do, document their purpose, audit formulas for errors, and assess maintainability risk. Use when: (1) User uploads an Excel file asking 'what does this do?', (2) User needs to understand an inherited/legacy spreadsheet, (3) User wants formula auditing or error detection, (4) User asks about spreadsheet risk, complexity, or documentation, (5) User mentions 'inherited', 'legacy', 'undocumented', or 'someone left' regarding Excel files."
---

# Excel Auditor

> **🧪 Status: IN TESTING** - Core functionality complete, validation in progress.

Analyze unknown Excel files to understand purpose, audit formulas, detect errors, and generate documentation.

## Core Workflow

### 1. Extract Structure
Run the structure extraction script on the uploaded file:

```bash
python scripts/extract_structure.py /mnt/user-data/uploads/<filename>.xlsx
```

This produces JSON with: sheets, named ranges, tables, external links, data validation rules, conditional formatting, and VBA presence.

### 2. Extract Formulas
Run formula extraction to build dependency graph:

```bash
python scripts/extract_formulas.py /mnt/user-data/uploads/<filename>.xlsx
```

This produces JSON with: all formulas, cell dependencies, calculation chains, and formula complexity metrics.

### 3. Semantic Analysis
With structure and formula data, perform semantic analysis:

**Purpose Detection**: Infer file purpose from:
- Sheet names and structure patterns
- Named range naming conventions
- Formula patterns (financial, statistical, lookup-heavy)
- Data shapes and header labels

**Pattern Recognition**: Match against known archetypes (see references/patterns.md):
- Financial models (DCF, budget, P&L)
- Operational trackers (inventory, scheduling, CRM)
- Reporting templates (dashboards, KPI rollups)
- Data transformation pipelines

### 4. Error Detection
Identify issues in order of severity:

**Hard Errors** (file is broken):
- #REF!, #DIV/0!, #VALUE!, #N/A, #NAME?, #NULL!, #NUM!
- Circular references (unless intentional iteration)
- Broken external links

**Soft Errors** (file works but fragile):
- Hardcoded values in formulas that should be inputs
- Inconsistent formula patterns across rows/columns
- Volatile functions overuse (NOW, TODAY, RAND, INDIRECT, OFFSET)
- Missing error handling (no IFERROR wrappers on lookups)
- Implicit intersection risks

**Smells** (maintainability concerns):
- Magic numbers without documentation
- Excessive nesting depth (>3 levels)
- Very long formulas (>200 chars)
- Mixed units without labels
- Color-coded logic without legend
- Hidden sheets with active dependencies

### 5. Generate Report
Produce structured output:

```markdown
# Excel Audit Report: [filename]

## Executive Summary
[2-3 sentence plain-English description of what the file does]

## Purpose Classification
- **Primary Function**: [e.g., "Financial forecasting model"]
- **Domain**: [e.g., Finance, Operations, HR, Sales]
- **Complexity**: [Simple | Moderate | Complex | Labyrinthine]
- **Bus Factor Risk**: [Low | Medium | High | Critical]

## Structure Overview
- Sheets: [count] ([list key sheets])
- Named Ranges: [count]
- Tables: [count]
- External Links: [count] ⚠️ if any
- VBA/Macros: [Yes/No] ⚠️ if yes

## Formula Analysis
- Total Formulas: [count]
- Unique Formula Patterns: [count]
- Max Dependency Depth: [number]
- Calculation Hotspots: [cells with most dependents]

## Issues Found
### Critical [count]
[list with cell locations]

### Warnings [count]
[list with cell locations]

### Suggestions [count]
[list with recommendations]

## Key Assumptions
[List hardcoded values that appear to be model inputs]

## Dependency Map
[Describe which sheets feed into which, key formula chains]

## Recommendations
1. [Immediate fixes]
2. [Documentation needs]
3. [Refactoring suggestions]
```

## Output Formats

**Default**: Markdown report in chat
**On request**: Generate .md or .docx file with full report
**On request**: Annotated copy of Excel with comments on flagged cells

## Handling Edge Cases

**Very Large Files (>10MB)**:
- Sample analysis of first 1000 formulas
- Focus on structure and high-level patterns
- Note that full audit requires sampling

**Password Protected**:
- Cannot audit, inform user

**VBA Present**:
- Note VBA exists but cannot audit macro logic
- Flag as elevated risk for maintainability

**Binary .xls Format**:
- Attempt conversion or note limitations

## Error Response Templates

When no issues found:
> "This file appears well-structured with no formula errors detected. [summary of what it does]"

When issues found:
> "I found [N] issues requiring attention. The most critical: [top issue]. Full audit below."

When file is severely broken:
> "This file has significant structural issues that prevent complete analysis. [list blocking issues]"
