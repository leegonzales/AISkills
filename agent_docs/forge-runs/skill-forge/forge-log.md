# Forge Log — skill-forge

skill-forge dogfooding itself. Newest entries at the bottom.

| Round | Change | Tuning lift | Holdout | Must-pass | Decision |
|-------|--------|-------------|---------|-----------|----------|
| 0 | (baseline) | skill 3.68 vs base 2.82 = **+0.86** | not yet scored | clean (1 MP2-partial on *baseline*) | diagnose |
| 1 | +E6 variance/noise protocol (v1.1) | — | **H1 skill 3.95 vs base 3.22 = +0.73** | clean | **PROMOTE v1.1** |

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

---

## Round 1 — Change: variance/noise handling (E6), v1.1.0

**Edit:** added eval-protocol.md §6 "Trust the signal before you trust the lift" + a 6th mandatory discipline in SKILL.md — compare arms within the same panel pass; report judge spread; lift smaller than inter-judge spread = inconclusive; prefer more tasks over more judges; label small-n results directional.

**Re-eval on holdout H1** (incident-postmortem readiness; A=skill v1.1, B=baseline; panel blind). Note the baseline H1 *independently* included inter-rater agreement + a pilot, so this was a fair, strong comparator:

| Panel | Skill v1.1 | Baseline |
|-------|-----------|----------|
| Measurement | 3.9 | 3.3 |
| Skeptic | 4.0 | 3.14 |
| **Mean** | **3.95** | **3.22 → +0.73** |

Both panels explicitly: the skill now **handles E6 better** (lift-vs-noise: within-round re-scoring + noise band + directional-at-small-n) than the baseline's narrower human-inter-rater-agreement. E6 rose from 1-3 (round 0) to 3-4. No must-pass breaks.

**Decision: PROMOTE v1.1.** Holdout lift +0.73, the diagnosed weak dimension improved, clean must-pass. Both panels named one further micro-improvement — fold in an explicit **inter-rater-agreement statistic** (the one thing the baseline did that the skill doesn't yet name) — a sub-0.3 marginal → **diminishing returns**. Stop refinement after the adversarial pass (1 of 2 budgeted rounds used).

---

## Adversarial pass (red-team v1.1) — the most valuable finding of the whole exercise

The red-team found **two CRITICAL issues that my own runs had been silently demonstrating**:

- **[CRITICAL] Value-shape assumption.** Tier B hard-codes ONE value shape — *better artifact, same task, mean-lift, artifact-quality panel*. That structurally mis-measures whole classes of skill: **safety/refusal** (correct behavior is a shorter/no artifact → a quality panel *penalizes* it), **variance-reduction** (improves worst-case, not mean → invisible on a small set), **routing/triage** (no artifact), **interaction/process** (a trajectory, not one output). Worse: skill-forge's *own loop would degrade a safety skill toward its failure mode* by "improving" away the gate that scores as "incomplete."
- **[CRITICAL] Baseline contamination.** The metric is `skill − baseline`, but a capable base model *already* does much of what a good skill prescribes → lift compresses toward zero for genuinely good skills, and near-zero lift is ambiguous (useless skill vs already-competent base). **This is exactly what both forge runs showed** — strong baselines, modest absolute lift. The red-team named the cause my runs only hinted at.
- **[MAJOR, fix] Internal contradictions:** (4.1) SKILL.md says "re-eval on fresh holdouts every round" but eval-protocol says "holdout is sacred, only at promotion" — opposite handling. (4.2) the `self-improving champion` STOP is identical to the per-round PROMOTE gate → the stop is illusory (fires on first promotion). (2.1) promotion compares to `best` (a prior round) while §6 forbids cross-round comparison → must re-score `best` in the same pass.
- **[MINOR, fix] (4.3)** the worked example keeps a traceability regression on net-positive average — the exact anti-pattern the skill warns against.
- **[MAJOR, backlog]** no cost/length axis (+ blind panels are length-biased toward the skill arm); "external/holdout/bar" asserted not verified (correlated judges, leaky holdout, trivially-low bar); selecting-on-noise when diagnosing the weakest of 6+ dimensions at n=5; no tool/state-dependent-skill guidance; no "skill is net-negative, don't ship at all" exit.

**Could NOT break:** the §6 noise discipline itself (attacks were on omissions), and external-scoring-never-self-grade (holes are in *correlated* externals, not smuggled self-grading).

→ Round 2 = adversarial hardening: fix the two CRITICALs (value-shape classification + baseline-competence check) and the contradictions (4.1/4.2/2.1/4.3). Remaining MAJORs logged as backlog. **These are coherence/correctness fixes verified by re-reading + a re-check, NOT measured by the eval** — honest, because several findings say the eval itself is mis-shaped, so re-running it can't validate the meta-fixes.

---

## Round 2 — Adversarial hardening (v1.2.0)

**Edits:** (1) value-shape classification as workflow step 1 — (a) artifact-lift / (b) variance-reduction / (c) gating-refusal / (d) routing / (e) interaction, each with its own eval shape; names "the loop deletes the gate" as the cardinal error. (2) baseline-contamination guidance in step 3 — build tasks where the base model fails; near-zero lift ≠ useless. (3) reconciled the holdout contradiction (diagnose from tuning + adversarial only; holdouts only at promote). (4) made champion-stop distinct (≥2 sustained batches) from the promote-gate. (5) within-pass re-scoring of `best`; margin must exceed noise band. (6) fixed the worked example to revert a per-dimension regression instead of keeping it on net-positive. 4 MAJOR findings logged as backlog.

**Re-check (focused, all four):** **FIXED** — value-shape steers a refusal-skill to a trigger-conditional eval; baseline-contamination gives the "0 lift ≠ useless" rule + build-harder-tasks; holdout handling now agrees across both files; champion-stop distinct. Verified by re-reading, not by the eval (these meta-fixes aren't eval-measurable — and several findings are *about* the eval being mis-shaped, so re-running it couldn't validate them).

---

# RUN SUMMARY — skill-forge forge (v1.0 → v1.2)

**Outcome: PROMOTED. Measured behavioral lift, the diagnosed weakness fixed, and the most valuable result of the whole exercise — skill-forge's adversarial pass exposed two CRITICAL design holes that its own runs had been silently demonstrating.**

**Lift (within-round, same panel both arms):**

| | Skill | Baseline | Lift |
|--|-------|----------|------|
| Round 0 tuning (T1+T2) | 3.68 | 2.82 | **+0.86** |
| Round 1 holdout (H1) | 3.95 | 3.22 | **+0.73** |

Bigger lift than loop-builder: skill-forge's methodology (two-arm baseline, keep-best, pre-committed bar, must-pass gating) is genuinely non-obvious, so the base model leaves more on the table.

**What the forge bought:**
1. **Confirmed E6 (variance/noise)** as the weak dimension via unanimous independent panels → added the §6 noise protocol (within-round comparison, judge spread, noise-band, small-n directional caveat). Holdout re-eval confirmed E6 improved.
2. **Adversarial pass found 2 CRITICALs the runs only hinted at:** the value-shape assumption (mis-measures safety/gate/variance/routing/process skills) and baseline contamination (strong baselines compress lift — *exactly what both runs showed*). Both fixed.
3. **Fixed 3 internal contradictions** (holdout sacred-vs-every-round; champion-stop ≡ promote-gate; within-round-vs-keep-best) + a self-undercutting worked example.

**Honest limitations:**
- Same low-n_eff / small-eval / cross-run-noise caveats as the loop-builder run (and skill-forge now *documents* these as its own §6 — the tool absorbed its own lesson).
- Round 2 fixes are **coherence/correctness, verified by re-read, not eval-measured** — disclosed, because the findings are about the eval model itself.
- **4 MAJOR findings deferred** (cost/length axis + length bias; verify-don't-assert external/holdout/bar; selecting-on-noise at small n; tool/state skills + net-negative exit) — logged in CHANGELOG, not fixed.

**Verdict:** skill-forge v1.2 is materially better than v1.0 — +0.86/+0.73 measured lift, the noise dimension hardened, and two CRITICAL design holes closed. **Hardened, not yet "optimal"** — the deferred backlog (especially the cost axis and verify-the-defenses items) is the path to that. The single most useful product of the run is the value-shape classification: without it, skill-forge confidently mis-measures most skills that aren't "write a nicer document."
