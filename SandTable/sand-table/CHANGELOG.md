# Changelog

## [1.3.0] - 2026-05-10

Round 2 of the subagent-panel-driven hardening: same 4 personas re-audited the v1.2.0 changes and surfaced 4 fresh substantive findings, all patched here.

### Added
- `narrative_check.py` `_collect_text()` — recursively walks each event's nested dict/list values and pulls every prose string for scanning, with a `_NON_PROSE_KEYS` denylist (IDs, timestamps, scores, structural fields). Closes the **nested-payload smuggling gap**: previously, single-author tells written under `payload.speech`, `content.body`, `message.text`, etc., bypassed all 5 signals because the flat-field `TEXT_FIELDS` loop never reached them. Now scanned with bounded recursion (depth 4)
- Pattern 7 `bid_arbitration` roster field — declared allocation rule (`fifo` / `equity_weighted` / `persona_weighted` / `facilitator_select` / custom). Without this, the orchestrator silently encodes its own rule and stipulated dominance returns through the back door
- Pattern 7 "Format-Specific Variants" sub-section — explicit support for IRE/IRF (teacher-fronted Socratic) via an `evaluation` third-turn event, and Harkness peer-discussion via `equity_weighted` + omit evaluation

### Changed
- `narrative_check.py` `scan()` and `_scan_signal_5_pairs()` now use `_collect_text()` instead of flat `TEXT_FIELDS` iteration — the legacy `TEXT_FIELDS` constant is retained for backward reference but no longer the scan boundary
- SKILL.md `What is a Sand Table?` opener rewritten in plainer prose: removed jargon ("stream of typed events", "narrative integrity", "no premature merging") from the intro paragraph; added a tiny shown-output snippet (the 4-line restaurant log) so non-technical readers can see what a run produces; removed the "structured ensemble protocol" alternative naming (it backfired in user testing — added more confusion than it removed)

### Fixed
- `narrative_check.py` module docstring: "~6 words" corrected to "~40 characters (≈8 words)" — matches the actual `_GAP = r"[^.!?\n]{0,40}"` regex bound

## [1.2.0] - 2026-05-10

Subagent-panel-driven hardening: 4 personas (novice, skeptic, educator, adversarial) audited the skill in parallel and each surfaced one substantive issue, all patched in this release.

### Added
- `## What is a Sand Table?` opener in `SKILL.md` — plain-language explanation of the concept (what units, what events, what the output looks like) with a tiny restaurant-pickers example, plus an explicit metaphor escape-hatch ("structured ensemble protocol") for teams allergic to the sand-table image
- Pattern 7 in `references/patterns.md` — Interaction-Order Modeling extension pattern for discussion-style domains (turn-bid grammar, `floor_time_budget` field, `participation_equity` derived metric); explains why it's not in the base protocol and how to layer it into a domain invariant

### Fixed
- `narrative_check.py` `_first_token` no longer crashes with `AttributeError` when an agent roster entry is missing `name` or has a non-string name (returns empty string, lets downstream loops continue)
- `SKILL.md` `Narrative Integrity` description now honestly scopes what `narrative_check.py` catches (5 specific regex signals; does not parse dialogue, strip quotes, or detect self-name dissociation; CLEAN means "no patterns matched", not "narrative is sound")
- `references/patterns.md` §3.2 no longer claims drift mappings are "reliably produced across domains" — clarified as observed-during-development, not measured, and invites extension

## [1.1.0] - 2026-03-24

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

## [1.0.0] — 2026-03-14

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
