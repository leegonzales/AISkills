# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2026-01-07

### Changed
- Updated CLI syntax from deprecated `-p`/`--prompt` flag to positional prompts
- Changed heredoc patterns from `gemini -p "$(cat <<'EOF'...)"` to `cat <<'EOF' | gemini`
- Updated all command examples in SKILL.md and gemini-commands.md
- Updated quick reference tables with new syntax

### Fixed
- CLI invocation now works with latest Gemini CLI version

## [1.0.0] - 2025-11-12

### Added
- Initial release
- AI peer review via Gemini CLI
- 1M token context window support
- Architecture validation workflows
- Security review with threat modeling
- Multimodal technical review (diagrams, PDFs)
- Google Search grounding for best practices

### Testing
- 87.5% pass rate (7/8 tests)
- 5.0/5.0 average quality score
