# Changelog

## 1.1.0 — 2026-03-24

Reliability, multi-session, and pattern backport from production training implementation.

### Added
- `references/patterns.md` — 6 reusable design recipes extracted from production implementations: program invariant structure, agent design recipes (orchestrator/participant/validator), event schema enforcement with known LLM drift catalog, output structure, new domain creation guide, multi-run comparison
- `references/reliability.md` — Simulation reliability patterns: impossible narrative detection (5 signals), timeout/abort rules for non-responsive agents, module batching for pacing optimization, cross-session context resolution protocol
- `references/multi-session.md` — Multi-session continuity pattern: exit context schema (generic template + training example), context loading chain with hard gates, cohort matching validation, context accumulation model, manifest/lineage tracking
- `reliability` command in SKILL.md — narrative integrity analysis, data completeness checks, context chain validation
- Execution Tiers section in protocol-spec.md — Tier 1 (narrated), Tier 2 (scripted), Tier 3 (real agent interaction with `prompt_sent`, `ai_response`, `follow_ups` fields)
- Reliability Contract section in protocol-spec.md — links to reliability patterns
- Multi-Session Continuity section in protocol-spec.md — links to multi-session pattern
- Reliability Configuration section in domain-invariant-template.md — timeout, abort, narrative integrity settings
- Multi-Session Configuration section in domain-invariant-template.md — exit context schema, context loading rules
- Known Drift Patterns section in domain-invariant-template.md — cross-domain drift baseline with customization guidance

### Changed
- Protocol spec version bumped to 1.1
- `design` command now recommends execution tier, reliability configuration, and multi-session strategy
- `validate` command now includes impossible narrative detection and drift correction details
- Domain invariant checklist expanded with reliability, multi-session, and drift pattern items
- AIEnablement Training implementation entry updated: 18 personas, Tier 3 execution, multi-session with exit context, 8+ successful runs

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
