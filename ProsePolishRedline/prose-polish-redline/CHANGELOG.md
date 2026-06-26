# Changelog

## 1.1.0 (2026-06-25)

### Added
- **Fidelity Firewall** (SKILL.md + edit-schema.md + authority/claims/stakes agents): no edit may introduce a citation, statistic, number, date, name, quote, or fact absent from the source document; honest moves are sharpen-from-source / `comment`-flag / soften. Closes the `insert` bypass (no `original_text` -> the verbatim guard can't catch invented content; `insert` may add connective phrasing only). Surfaced by the skill-forge audit (SKILL-l30): the skill auto-applies edits to .docx and its own schema/agent examples taught citation injection.
- MIT LICENSE (was missing).

### Changed
- Reworked the edit-schema `insert` example (was injecting "(Schuch et al., 2019)") and the `replace` example (was inventing "40%") into faithful, fact-preserving examples.

### Verified
- Hardened authority+claims agents on a citation-thin draft: 14 edits, zero fabricated citations/numbers — flags for the author instead of inventing.

## 1.0.0 (2026-03-11)

Initial release.

- 9 kata agents: genre-scorer, coherence, authority, claims, stakes, rhythm, hedge, personality, perspective
- 5 editing tiers: STRUCTURAL, COHERENCE, AUTHORITY, CRAFT, VOICE
- Two-phase pipeline with merge engine (dedup, conflict resolution, Phase 2 rebasing)
- Tracked-changes .docx output via python-docx
- Animated HTML replay with tier-by-tier visualization
- Per-agent match rate diagnostics
- Three depth levels: conservative (3 agents), moderate (7), aggressive (9)
- Dry-run mode for prompt tuning
- Genre-calibrated thresholds for academic, technical, business, creative, personal, journalistic
- Comment-first mode for hallucination-prone agents (authority, claims, stakes, hedge)
- No-chaining rule for rhythm-agent
