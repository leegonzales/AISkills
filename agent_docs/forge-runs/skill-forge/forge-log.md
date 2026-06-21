# Forge Log — skill-forge

skill-forge dogfooding itself. Newest entries at the bottom.

| Round | Change | Tuning lift | Holdout | Must-pass | Decision |
|-------|--------|-------------|---------|-----------|----------|
| 0 | (baseline) | skill 3.68 vs base 2.82 = **+0.86** | not yet scored | clean (1 MP2-partial on *baseline*) | diagnose |
| 1 | +E6 variance/noise protocol | — | pending | — | pending |

---

## Round 0 — Baseline

Two arms (baseline vs skill-forge) produced skill-evaluation plans for T1-T2. External panel of 2 (measurement lens + skeptic lens), blind. A=baseline, B=skill.

**Scores (mean both panels):**

| Task | Skill arm | Baseline | Lift |
|------|-----------|----------|------|
| T1 commit-writer | 3.64 | 2.79 | +0.85 |
| T2 PRD tweak | 3.72 | 2.86 | +0.86 |
| **Overall** | **3.68** | **2.82** | **+0.86** |

Skill wins both tasks, both panels, decisively. Bigger lift than loop-builder because the skill's methodology (two-arm baseline, keep-best, pre-committed bar, must-pass gating, adversarial round) is genuinely non-obvious — the base model produces a decent eval but misses the loop discipline (E5) and the explicit baseline/lift quantification (E4). Baseline T2 drew an **MP2-partial** (author's "own blind ranking" co-grades their own tweak); the skill arm avoids it — direct evidence the skill's external-scoring rule earns its place.

**DIAGNOSIS — E6 (variance/noise) is the weakest dimension, for BOTH arms (confirmed, unanimous).** Both panels scored E6 lowest (1-3). The skill arm only reaches 2-3 because a multi-judge panel is a real noise reducer — but it **never specifies** sample-size justification, number of judges, inter-rater agreement, repeat-runs for judge self-consistency, or any significance/CI test. Skeptic verdict: *"B just hides it behind better vocabulary."* And small held-out sets (5-10) mean even a real lift can't clear noise. **This is exactly the eval-score-noise finding the loop-builder run surfaced** (same baseline text scored 3.36-4.00) — now independently confirmed. → Round 1 adds concrete variance handling.
