# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- **Fidelity Firewall** (top-level, mandatory): every flagged formula error, cited cell, and risk claim must trace to actual extractor JSON output — never assert errors the extraction didn't surface or construct plausible cell addresses.
- Extraction-success gate: malformed/empty/unsupported extractor output halts the audit instead of proceeding to a confident report.
- LICENSE file (MIT) for packaging/validation compliance.

### Changed
- Purpose detection now grounded in `purpose_analysis.confidence` + `reasoning`; sparse/ambiguous workbooks must report "purpose unclear from available signal" with an explicitly LOW-confidence guess rather than a fabricated archetype. Added "confidence-number trap" caveat (a single weak signal can read confidence 1.0).
- Error Response Templates rewritten to be evidence-grounded (sparse-workbook and extraction-failure cases added).

## [1.0.0] - 2025-12-05

### Added
- Initial release (In Testing)
- Structure extraction (sheets, named ranges, tables, VBA, external links)
- Formula analysis with complexity metrics
- Error detection (7 Excel error types)
- Volatile function identification
- Purpose inference from formula patterns
- Pattern recognition for common archetypes
- Python extraction scripts
