# Forge Log — loop-builder

Running log of the skill-forge dogfood run on loop-builder. Newest entries appended at the bottom.

| Round | Change made | Tuning lift (overall) | Holdout | Must-pass | Decision |
|-------|-------------|----------------------|---------|-----------|----------|
| 0 | (baseline, no change) | skill 3.91 vs base 3.74 = **+0.17** | not yet scored | clean both arms | diagnose |

---

## Round 0 — Baseline (frozen eval, no skill change)

Two arms (baseline = no skill; skill = loop-builder in context) each produced loop designs for T1-T3. External panel of 2 (reliability lens + skeptic lens), blind to arm and to skill authorship, scored substance not vocabulary. Design A = skill, Design B = baseline (panel did not know this).

**Scores (mean of both panels, 0-4):**

| Task | Skill arm | Baseline arm | Lift | Note |
|------|-----------|--------------|------|------|
| T1 refinement (judge-gate) | 3.93 | 3.43 | **+0.50** | Skill wins decisively on **D4 keep-best** — baseline could ship a degraded last iteration. |
| T2 SQL (deterministic, disguised) | 3.93 | 3.79 | +0.14 | Near-tie. BOTH arms correctly resisted over-engineering the deterministic stop (D1/D7 strong both). |
| T3 bug-hunt (coverage) | 3.86 | 4.00 | **−0.14** | **Skill LOSES.** Both panels: skill framed an enumerable problem as "saturation/loop-until-dry" (convergence frame); baseline's "coverage/worklist-with-exhaustion" frame is sounder. Skeptic docked skill's D1 here. |
| **Overall** | **3.91** | **3.74** | **+0.17** | Win rate: 1 clear win, 1 marginal, 1 loss. No MP1/MP2 violations either arm. |

**Interpretation.** Lift is real but modest — expected, because the base model is already strong at loop design, so the skill can only add at the margins. Lift concentrates where the skill says something non-obvious (keep-best on refinement). Where the base model already had a good instinct (deterministic SQL), the skill adds little. And on T3 the skill actively *misframed* the problem.

**DIAGNOSIS (weakest dimension → Round 1 target):** **D1 classification on enumerable/coverage discovery.** loop-builder's `saturation (loop-until-dry)` family is the only discovery stop offered, so it gets applied to *finite, enumerable* spaces (a prioritized worklist) where plain **exhaustion** is the correct, sounder stop. The skill conflates two distinct things: unbounded discovery (→ saturation) vs enumerable coverage (→ worklist-exhaustion, a near-deterministic stop). Fix: add the coverage/worklist distinction and teach the classification.
