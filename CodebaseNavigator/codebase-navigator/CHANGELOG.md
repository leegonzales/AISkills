# Changelog

All notable changes to this project will be documented in this file.

## [1.0.1] - 2025-12-07

### Added
- Query refinement section with step-by-step guidance
- osgrep vs grep decision guide table
- Combining tools section (osgrep + Glob, osgrep + grep, osgrep + Read)
- Real-world examples from pressure testing

### Changed
- Enhanced anti-patterns with specific failure cases
- Added iterative refinement to DO list

### Validated
- Retroactive TDD validation with 5 pressure scenarios
- Identified gaps: query refinement, tool selection, combining tools
- All gaps addressed in this update

## [1.0.0] - 2025-12-07

### Added
- Complete skill rewrite with comprehensive osgrep documentation
- Full command reference (search, index, list, serve, doctor)
- Output mode documentation (default, content, compact, json, scores)
- Search tuning options (max-count, per-file, sync)
- Query formulation patterns reference
- Troubleshooting guide
- Language-specific query examples
- Integration guidance with other tools

### Changed
- Restructured to follow AISkills standard (skill-slug directory, references/)
- Expanded from 32 lines to comprehensive skill with references

### Removed
- Old minimal SKILL.md at root level (replaced with proper structure)
