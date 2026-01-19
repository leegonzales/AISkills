# Changelog

All notable changes to the Essay to Speech skill.

## [1.1.0] - 2026-01-19

### Added
- **Transformation intensity modes**: Full (default) vs Light for already-conversational essays
- **Statistical notation → Plain English**: Conversion table for academic notation (ρ, β, CI, p-values)
- **Rhythm and breath guidance**: Sentence length variation patterns, breath point placement
- **Critical image assessment**: Skeptical evaluation framework with common issues table by image type
- **Tagging guidelines**: 2-4 tags per section, guidance on when NOT to tag

### Changed
- Image assessment now defaults to skepticism ("most academic figures need adaptation")
- Example transformation updated to show statistical notation conversion
- Best practices expanded from 5 to 8 items
- Document structure now includes Mode field

### Fixed
- Addressed issue where talk tracks stayed too close to academic source language
- Image assessments now more critical (not everything is "USE")

## [1.0.0] - 2025-01-19

### Added
- Initial release
- Core transformation engine (written → spoken)
- Atomic chunking with argument-based segmentation
- Connected output format preserving original + talk track
- Optional delivery markup (pause, emphasis, pacing)
- Comprehensive transformation patterns reference
- Full before/after examples

### Designed For
- Pipeline integration with downstream slide-builder skill
- Preservation of source material for multi-step processing
