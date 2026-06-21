# Changelog

All notable changes to the Loop Builder skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-06-21

### Added
- **Coverage / worklist-exhaustion** stop family, distinct from saturation: when a discovery space is *enumerable* (listable files/endpoints/rows), the correct stop is deterministic exhaustion, not a fuzzy "K dry rounds." Added the classification cue ("can I list the things to check?") to the build workflow, the family table (SKILL.md), and the saturation section (references/non-deterministic-stops.md). Surfaced by a skill-forge behavioral eval where the skill misframed an enumerable bug-hunt as saturation.

## [1.0.0] - 2026-06-20

### Added
- Initial release of the loop-builder skill.
- Core model (`body` + `stop`; deterministic vs non-deterministic) and a 6-step build workflow in SKILL.md.
- `references/non-deterministic-stops.md` — the stop-condition taxonomy (10 families), the canonical robust loop shape, and 9 design rules.
- `references/loop-failure-modes.md` — 14 failure modes with detection and defense; a red-team review prompt.
- `references/loop-library.md` — a catalog of 57 loops across 10 categories, each tagged deterministic vs non-deterministic with its stop family.
- Mandatory guardrails: soft-stop + hard-budget, external evaluator, keep-best-not-last, diverse judges, pre-committed bar.
