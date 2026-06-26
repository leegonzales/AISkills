---
name: excel-auditor
description: "Analyze unknown or inherited Excel files to understand what they do, document their purpose, audit formulas for errors, and assess maintainability risk. Use when: (1) User uploads an Excel file asking 'what does this do?', (2) User needs to understand an inherited/legacy spreadsheet, (3) User wants formula auditing or error detection, (4) User asks about spreadsheet risk, complexity, or documentation, (5) User mentions 'inherited', 'legacy', 'undocumented', or 'someone left' regarding Excel files."
---

# Excel Auditor

Analyze unknown Excel files to understand purpose, audit formulas, detect errors, and generate documentation.

## Fidelity Firewall (never violate)

**Auditing is reporting what the extraction found — not what a plausible spreadsheet of this kind would contain.** An audit is only worth the trust placed in it. A confident, well-written finding built on a fact the extractor never surfaced is a *fabrication*, not an audit — no matter how reasonable it sounds. The failure mode this firewall exists to stop: on a sparse, ambiguous, or near-empty workbook, inventing a confident purpose and flagging formula errors that the extraction did not detect.

**The hard rule — every claim must trace to extractor output.** The JSON from `extract_formulas.py` and `extract_structure.py` is the *only* ground truth. Before you write any of the following, point to the exact field that supports it:

- **Every flagged error** (`#REF!`, `#DIV/0!`, `#VALUE!`, circular reference, broken external link, etc.) MUST appear in `errors_found`, `circular_references`, or `issues` in the extractor JSON. Never report an error the extraction did not surface. If you believe an error *could* exist but the extractor didn't catch it, say "not detected by extraction; would require manual verification" — do not assert it.
- **Every cited cell** (`Sheet1!B12`, etc.) MUST come from a real `cell` field in the JSON. Never construct a plausible-looking cell address. If you can't quote it from the output, you can't cite it.
- **Every risk claim** (hidden content, hardcoded override, formula inconsistency, volatile-function abuse, VBA) MUST trace to the corresponding finding (`hidden_content`, `hardcoded_overrides`, `formula_inconsistencies`, `volatile_functions`, `has_vba`). The `risk_assessment.workbook_score` and `risk_factors` are computed from real findings — report them, don't inflate them.

**Purpose detection must be grounded — and honest about confidence.** Purpose is inferred from *real evidence*: sheet names, headers, named ranges, and formula patterns **actually present** in the JSON (`purpose_analysis.reasoning` lists the signals that fired). Read the `confidence` field and let it govern your language:

- `confidence >= 0.7` with concrete reasoning signals → state the purpose, citing the signals.
- `confidence < 0.5`, few signals, or `purpose == "general_spreadsheet"` → say **"purpose unclear from available signal"** and give a LOW-confidence guess **clearly labeled as such** (e.g., "Low confidence (0.3): possibly a simple data list — only signal is N sheets with no formulas"). Never upgrade a weak guess into a confident claim.
- On a near-empty / ambiguous workbook (few sheets, few or no formulas), the correct answer is *insufficient signal*, not an invented purpose. Naming a specific archetype (DCF model, CRM, three-statement model) requires the archetype's indicators to actually appear in the extraction — not vibes.

> **Confidence-number trap:** `purpose_analysis.confidence` is a relative score (winner / total signal weight). When only one weak signal fires — e.g. `reasoning: ["Low formula count - likely data storage"]` — `confidence` can read `1.0` while the actual evidence is a single thin clue. **Do not treat a high `confidence` as conclusive when `reasoning` lists only one or two sparse signals.** Count the substantive signals in `reasoning`, not just the number. One or two thin signals on a small workbook = "purpose unclear from available signal," regardless of the score.

**Gate on extraction success — don't audit what you couldn't read.** Before any analysis, verify the extractor JSON parsed and contains the expected keys (structure: `sheets`, `named_ranges`, `tables`, `external_links`, `summary`; formulas: `formulas`, `complexity_metrics`, `purpose_analysis`). If either extractor returned an `error` field, empty/malformed JSON, or `support_level: "unsupported"` (password-protected, unreadable, or unsupported format), **report that limitation and stop** — do not proceed to a confident audit on absent data. A partial extraction yields a partial, explicitly-scoped report, never a full-confidence one.

**Final pass — fidelity re-check.** Before returning the report, re-read every error, cell citation, and purpose claim against the extractor JSON and delete or downgrade anything you cannot trace to a real field. This check outranks completeness and polish: a shorter honest report beats a fuller invented one.

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

### 2b. Validate Extraction Output (Firewall gate — mandatory)
Before any analysis, confirm the extractor JSON parsed and carries the expected keys:
- Structure: `sheets`, `named_ranges`, `tables`, `external_links`, `summary`
- Formulas: `formulas`, `complexity_metrics`, `purpose_analysis`

**Stop conditions** (do NOT proceed to a confident audit — report the limitation instead):
- Either extractor returned an `error` field, or empty/malformed JSON.
- `support_level: "unsupported"` (e.g., password-protected, unsupported format, missing library).
- Expected keys absent or unparseable.

If extraction is partial, the report is partial and explicitly scoped — never full-confidence. See the Fidelity Firewall above.

### 3. Semantic Analysis
With structure and formula data, perform semantic analysis:

**Purpose Detection** (governed by the Fidelity Firewall): Infer file purpose ONLY from evidence present in the extraction:
- Sheet names and structure patterns
- Named range naming conventions
- Formula patterns (financial, statistical, lookup-heavy)
- Data shapes and header labels

Use the extractor's `purpose_analysis` — read its `confidence` and `reasoning` and let them govern your language:
- `confidence >= 0.7` with real reasoning signals → state the purpose, citing those signals.
- `confidence < 0.5`, sparse signals, or `purpose == "general_spreadsheet"` → say **"purpose unclear from available signal"** and give a LOW-confidence guess explicitly labeled with the score and the one or two signals (if any) that fired. Do not upgrade it to a confident claim.

**Pattern Recognition**: Match against known archetypes (see references/patterns.md) ONLY when the archetype's indicators actually appear in the extraction. Do not name an archetype on vibes:
- Financial models (DCF, budget, P&L)
- Operational trackers (inventory, scheduling, CRM)
- Reporting templates (dashboards, KPI rollups)
- Data transformation pipelines

On a near-empty / ambiguous workbook (few sheets, few or no formulas), the honest output is *insufficient signal* — not an invented archetype.

### 4. Error Detection
Report ONLY issues the extraction surfaced (Fidelity Firewall): each flagged error must trace to `errors_found`, `circular_references`, or `issues` in the JSON, and each cited cell to a real `cell` field. If you suspect an issue the extractor did not detect, label it "not detected by extraction; requires manual verification" — never assert it as found. Identify issues in order of severity:

| Category | Issues | Severity |
|----------|--------|----------|
| **Hard Errors** | #REF!, #DIV/0!, #VALUE!, #N/A, #NAME?, #NULL!, #NUM!; Circular references (unless intentional); Broken external links | Critical - file is broken |
| **Soft Errors** | Hardcoded values that should be inputs; Inconsistent formula patterns; Volatile function overuse (NOW, TODAY, RAND, INDIRECT, OFFSET); Missing IFERROR on lookups; Implicit intersection risks | Warning - file works but fragile |
| **Smells** | Magic numbers; Excessive nesting (>3 levels); Very long formulas (>200 chars); Mixed units without labels; Color-coded logic without legend; Hidden sheets with active dependencies | Info - maintainability concerns |

### 5. Generate Report
Produce structured output using the template in `references/report_template.md`.

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
> "Extraction surfaced no formula errors (`errors_found` empty, `circular_references` empty). [summary of what it does, grounded in real signals]"

When issues found:
> "Extraction surfaced [N] issues. The most critical: [top issue, with cell address quoted from JSON]. Full audit below."

When the workbook is sparse / ambiguous (Fidelity Firewall):
> "Purpose unclear from available signal — this workbook has [N] sheet(s) and [N] formula(s), too little to classify confidently. Low-confidence guess ([score]): [guess], based only on [signal that fired, if any]. No formula errors were detected by extraction."

When extraction failed or is unsupported (Firewall gate):
> "I could not complete a reliable audit: extraction returned [error / unsupported format / password-protected]. I won't guess at purpose or errors on data I couldn't read. [state what is and isn't known]"

When file is severely broken:
> "This file has significant structural issues that prevent complete analysis. [list blocking issues traced to extractor output]"
