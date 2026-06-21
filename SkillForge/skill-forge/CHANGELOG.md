# Changelog

All notable changes to the Skill Forge skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-06-21

### Added
- **Variance & noise handling (E6)** — eval-protocol.md §6 "Trust the signal before you trust the lift" + a 6th mandatory discipline in SKILL.md. Concrete rules: compare arms *within the same panel pass* (absolute scores drift between runs — the observed baseline swing was 3.36-4.00); report judge **spread** not just the mean; treat lift **smaller than the inter-judge spread as inconclusive**; prefer more tasks over more judges; with a 3-5 task eval, label the result directional not conclusive. Surfaced + confirmed by skill-forge dogfooding itself (E6 was the unanimous weakest dimension) and by the loop-builder forge run's eval-noise finding.

## [1.0.0] - 2026-06-20

### Added
- Initial release of the skill-forge skill.
- Two-axis definition of "optimal" (structurally sound + behaviorally lifting) and a 6-step workflow in SKILL.md.
- `references/eval-protocol.md` — Tier A structural gate + Tier B behavioral outcome eval; how to build a non-leaky held-out task set, run two arms, and score externally; eval failure modes.
- `references/refinement-loop.md` — the freeze→diagnose→revise→re-eval→promote→adversarial flywheel, five non-gameable stop conditions, and a worked example (forging a `prd` skill).
- Mandatory disciplines: external scoring (never self-grade), held-out-fresh-at-promotion, keep-best-not-last, one-change-per-round, pre-committed eval + bar.
- Composes with loop-builder (loop design), the skill-evaluation rubric (Tier A), and multiagent-review / peer-review (external panel).
