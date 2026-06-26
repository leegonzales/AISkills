# Changelog

All notable changes to this project will be documented in this file.

## [1.2.0] - 2026-06-25

### Added
- **Fidelity Firewall / Degraded Mode** section (top of SKILL.md): anti-confabulation gate. The skill may report only what the `gemini` CLI actually returned in-session — never invent, paraphrase-from-imagination, or embellish a Gemini opinion. If the CLI is absent/errors/times out/returns nothing usable, it must say "second opinion unavailable" and proceed Claude-only rather than fabricate a false consensus.
- Firewall-aligned error-handling rules in the Invoke step.
- Firewall reminder + conditional guard on the "Both Claude and Gemini agree…" synthesis example.

### Note (future work)
- SKILL.md is ~40KB and verbose (instruction dilution risk). A future pass should trim the 9 use-case patterns and the Gemini-vs-Claude appendix into `references/` to tighten the core. Firewall added now; trim deferred.

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
