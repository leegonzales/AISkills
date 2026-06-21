# Changelog

All notable changes to the Loop Builder skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2026-06-21

### Added
- **Static-vs-regenerating territory axis** (extends the v1.2 coverage cue): static enumerable territory -> coverage/worklist-exhaustion; *regenerating* enumerable territory (logs, queues) -> loop-until-dry where the **budget is the primary stop** (process-until-empty runs forever if it refills); non-enumerable -> true saturation. Fixes a runaway-on-regenerating-queue hole found in adversarial review.
- **Side-effects guardrail (#6):** keep-best is an illusion when the body acts irreversibly each round (deletes/sends/deploys); loop to a decision then act once, or checkpoint/dry-run, or gate behind a human. Added to SKILL.md guardrails + a dedicated section in references/non-deterministic-stops.md.

### Known backlog (from the skill-forge adversarial pass, deferred to a future cycle)
- "External evaluator" is launderable (same model+diff prompt; generator-authored rubric) — wire external + decorrelated + independently-authored-bar into one test.
- Budget ceiling has no sizing guidance (report cap-hit rate; cap should bind rarely).
- Missing topologies: nested loops (budget multiplication), concurrent/fan-out loops (stop on first/all/quorum), cold-start.
- convergence vs diminishing-returns definitions blur.

## [1.2.0] - 2026-06-21

### Changed
- Sharpened the coverage/worklist classification cue: **classify on the search *territory*, not the findings.** Findings may be unbounded ("all the bugs") but the territory (files/endpoints/rows) is usually enumerable → coverage-spine is the primary stop, with saturation only a within-budget secondary for the unlistable remainder. (Round-2 skill-forge finding: the v1.1 cue was right but aimed at findings, leading designs to default to saturation for sweepable surfaces.)

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
