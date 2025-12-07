# Changelog

All notable changes to Claude Project Docs will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-07

### Added

- Initial release of Claude Project Docs skill
- Core SKILL.md with CLAUDE.md generation methodology
- The 60-Line Rule for optimal CLAUDE.md sizing
- WHAT/WHY/HOW structure template
- Progressive disclosure via agent_docs/ pattern
- Comprehensive anti-patterns guide
- Reference templates:
  - `claude-md-template.md` - Minimal starter template
  - `agent-docs-catalog.md` - Complete agent_docs file specifications
  - `anti-patterns.md` - What NOT to include guide
- Project-type examples:
  - `examples/minimal-web-app.md` - Next.js + PostgreSQL example
  - `examples/minimal-python.md` - Python library example
  - `examples/minimal-monorepo.md` - TypeScript monorepo example
- Audit capability for existing CLAUDE.md files
- Agent docs generation workflow

### Research Foundation

Based on recommendations from:
- HumanLayer: Writing a good CLAUDE.md
- Claude Code Best Practices (Anthropic)
- Community patterns from claude-md-examples
