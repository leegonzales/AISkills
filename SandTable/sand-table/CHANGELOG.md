# Changelog

## 1.0.0 — 2026-03-14

Initial release. Protocol extraction from three existing implementations.

### Added
- Protocol spec v1.0 (event envelope, temporal models, normalization contract)
- Shared normalizer (`scripts/normalize.py`) with drift mappings support
- Protocol validator (`scripts/validate_stream.py`)
- Agent-ops extractor (`scripts/extract_agent_ops.py`) for Claude Code session logs
- Meta skill (`SKILL.md`) for designing, scaffolding, extracting, and validating
- Implementation registry documenting Substack readership, AIEnablement training, and Agent-Ops
- Domain invariant template for scaffolding new sand tables
- Annotated examples from all three domains
- Catalyst "Calm Luxury" CSS design tokens (`templates/replay-base.css`)
- Project discovery manifest template (`templates/manifest.json`)
