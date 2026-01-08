# Audit Report Template

Use this template when generating the final audit report.

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
- External Links: [count] - flag if any
- VBA/Macros: [Yes/No] - flag if yes

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
