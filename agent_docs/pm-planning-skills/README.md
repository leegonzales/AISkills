# PM & Planning Skills — Evaluation + Build Plan

> **Status:** Evaluation complete; build not started (Lee, 2026-06-20: "capture the eval + plan as a doc first").
> **Scope:** Fleet-wide / commercial-safe — licensing defaults to MIT/Apache only (see [03-build-plan §Licensing](03-build-plan.md#licensing-guardrails)).
> **Author:** Pike (AISkills guardian). Research via 3 parallel evaluation scouts + internal inventory, 2026-06-20.

## What this is

Lee asked: *"find and evaluate the best AI skills for planning and defining software projects in loops"* — specifically iterative agent loops for Amazon-style proposals (PR-FAQ / "5-pager"), PRDs, and TRDs. This package is the answer: a landscape evaluation, the quality bars each artifact must hit, and a sequenced plan to compose the best existing pieces (plus two genuine gap-builds).

## BLUF

**The field converged on one loop in the last ~12 months, the best pieces are MIT-licensed and already proven portable into Claude skills — so this is compose-and-adapt, not build-from-scratch.** Two artifacts have no good published skill and are worth a clean net-new build: the **Amazon Working-Backwards PR-FAQ/6-pager** and a **first-class RFC/TRD design-doc with a quality loop**.

The converged loop:
```
constitution/principles → specify(what) → CLARIFY → plan(how) → tasks → ANALYZE → implement → VERIFY
   human gate at each phase · revision = edit the upstream artifact · value concentrates in CLARIFY + ANALYZE + VERIFY
```

The recommended composition (a layered stack, not one skill):
```
PLAN LAYER      spec-driven planning skill   ← port GitHub Spec Kit loop + BMAD sharding
ARTIFACT LAYER  PR-FAQ → PRD → TRD skills     ← the proposal→PRD→TRD chain
GATE LAYER      externally-verified rubric    ← multiagent-review / peer review, NOT self-grading
ENGINE LAYER    ralph-wiggum loop             ← autonomous execution (already installed)
TASK DB         Beads (bd)                    ← dependency graph, cross-session (already in repos)
```

## Index

- **[01-landscape-evaluation.md](01-landscape-evaluation.md)** — every credible external tool & published skill, evaluated against Pike's gate, with license + ADOPT/ADAPT/BORROW/SKIP verdict + sources. Plus the loop-pattern catalog and the internal-reuse inventory.
- **[02-artifact-quality-bars.md](02-artifact-quality-bars.md)** — canonical structure, scoreable rubric, and failure modes for PR-FAQ/6-pager, PRD, and TRD; plus the cross-artifact traceability chain (the backbone that makes it a loop).
- **[03-build-plan.md](03-build-plan.md)** — the layered architecture, licensing guardrails, sequenced build phases, the two net-new gap-builds, and the internal-skill reuse map.

## The one thing not to get wrong

Self-grading quality gates are gameable — a model scoring its own work will pass itself. Every gate in this stack routes the score through a **separate reviewer pass** (multiagent-review / Gemini-Codex peer review). That external-verification discipline is the differentiator a Pike-built version brings over the published skills.
