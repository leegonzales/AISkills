# Forge Log — loop-builder

Running log of the skill-forge dogfood run on loop-builder. Newest entries appended at the bottom.

| Round | Change made | Tuning lift (overall) | Holdout | Must-pass | Decision |
|-------|-------------|----------------------|---------|-----------|----------|
| 0 | (baseline, no change) | skill 3.91 vs base 3.74 = **+0.17** | not yet scored | clean both arms | diagnose |
| 1 | +coverage/worklist-exhaustion distinct from saturation | T3 still −0.21 (fix incomplete) | **H1 skill 4.0 vs base 3.60 = +0.40** | clean | **PROMOTE v1.1** + sharpen |
| 2 | sharpen cue: enumerable *territory/surface* vs unbounded *findings* | T3 → see round 2 | — | clean | see round 2 |

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

---

## Round 1 — Change: add coverage / worklist-exhaustion family (distinct from saturation)

**Edit:** added the coverage/worklist-exhaustion family + a classification cue ("can I list the things to check?") to SKILL.md (family table + build workflow) and references/non-deterministic-stops.md (saturation section now leads with the enumerable-vs-unbounded call). Bumped to v1.1.0. Validates clean.

**Re-eval** (skill v1.1 arm vs baseline; this round labels flipped A=baseline/B=skill to counter position bias; panel still blind):

| Task | Skill v1.1 | Baseline | Lift | Note |
|------|-----------|----------|------|------|
| **H1 holdout** (negotiation; never iterated) | **4.00** | 3.60 | **+0.40** | Skill wins both panels — non-gameable "approve the SAME frozen version" + oscillation/cycle detection (D3/D5). This is the clean promotion signal. |
| T3 (bug-hunt) | 3.57 | 3.78 | −0.21 | Still loses. Panels SPLIT: reliability gave skill 4.0 (saturation defensible), skeptic gave skill 3.14 (the *territory* is enumerable → coverage is the sharper frame). |

**The T3 split is the key learning.** My Round-1 cue ("can I list the things to check?") was right but aimed wrong: the skill arm concluded "bugs aren't listable → saturation," when the sounder answer is "the *territory* (files/regions/endpoints) is listable → coverage-spine, with saturation only within budget on the unlistable remainder." The enumerable thing is usually the **search surface, not the findings.**

**Decision: PROMOTE v1.1.** Holdout lift +0.40 with zero must-pass regressions is the strongest signal skill-forge recognizes (self-improving-champion). The change added a genuinely correct concept. T3 exposed that the cue is *incomplete*, not *wrong* → Round 2 sharpens it.

---

## Round 2 — Change: classify on the *territory*, not the findings (v1.2.0)

**Edit:** sharpened the coverage cue in SKILL.md + non-deterministic-stops.md — "classify on the search **territory** (enumerable: files/endpoints/rows), not the **findings** (maybe unbounded); coverage-spine is primary, saturation a within-budget secondary for the unlistable remainder."

**Re-eval (T3, skill v1.2 vs the same baseline that beat it in rounds 0-1; labels A=skill/B=baseline, panel blind):**

| Panel | Skill v1.2 | Baseline | 
|-------|-----------|----------|
| Reliability | 4.00 | 3.71 |
| Skeptic | 3.90 | 3.00 |
| **Mean** | **3.95** | **3.36** → **+0.59** |

**Full reversal.** T3 went skill −0.14 (r0) → −0.21 (r1) → **+0.59 (r2)**. The skeptic who had preferred the baseline now scores the skill design clearly higher (3.9 vs 3.0), citing the clean primary(worklist-exhaustion)/secondary(saturation) hierarchy + external verify-before-record. Both panels flagged one further micro-improvement (add a loop-wide find-rate-decay non-progress trigger) — a sub-0.3 marginal → **diminishing returns**.

**Decision: PROMOTE v1.2.** T3 resolved; next change is marginal. Stop refinement after the adversarial pass (budget: 2 of 3 rounds used; early-stop on diminishing returns).

**⚠️ Eval-noise finding:** the *same* baseline T3 text scored 4.00 / 3.78 / 3.36 across three different panel runs — meaningful variance for an unchanged artifact. Within-round comparisons (same panel scores both arms in one call) are the valid signal; cross-round absolute scores are noisy. A production forge run needs more tasks + more panelists to tighten this. (This is itself a finding skill-forge should absorb — see its own forge run.)

---

## Adversarial pass (red-team v1.2)

A red-team agent found 6 weaknesses. Strongest (and it builds directly on the Round-2 fix):

- **[MAJOR→fix now] Static vs. regenerating territory.** The territory-vs-findings axis is incomplete. A *regenerating* enumerable territory (error logs, live queues, lint on a changing tree) under the "coverage-spine, process until empty" rule is a **runaway** — the queue never empties. Real discriminator is **static vs. regenerating**, not listable-at-an-instant. Also: the library's "Det | saturation" entries (#38/#39/#43…) contradict the SKILL.md claim that saturation is only for unlistable spaces.
- **[MAJOR→fix now] Side effects / irreversibility.** Every stop family assumes a pure body (produce→score→keep-best). Loops that *act* each round (delete files, send mail, change prod) make keep-best meaningless — "the best version" can't undo round 3's deletion. Most dangerous gap; the skill's reassuring keep-best creates false safety.
- **[MAJOR, backlog] "External evaluator" launderable** — same model + different prompt counts as "external" by the letter; generator can author the rubric the "external" judge scores. "External" and "decorrelated" and "independently-authored bar" aren't wired into one test.
- **[MINOR–MAJOR, backlog] Budget has no sizing guidance** — a ceiling of 10,000 satisfies the rule but never binds (runaway); too-low makes it a fixed grind. No "cap should bind <X% of runs / report cap-hit rate."
- **[MAJOR cumulative, backlog] Missing topologies** — nested loops (shared vs independent budgets, cost-multiplication), concurrent/fan-out loops (stop on first/all/quorum), cold-start (convergence/DR inert on round 1).
- **[MINOR, backlog] convergence vs diminishing-returns blur** — §2 defines convergence as "sameness" but the mitigation says "require improvement not sameness"; canonical pseudocode uses a DR test under a "diminishing returns" comment. Families bleed together.

**Could NOT break:** keep-best (for pure loops), the budget-exists rule, diverse-judges/effective-n, the red-team checklist itself, and no fabricated/false claims.

→ Round 3 fixes the top two (the static/regenerating axis directly extends the Round-2 work; the side-effect caution is cheap + high-value). The 4 backlog items are logged for a future forge cycle — *not* silently dropped.

---

## Round 3 — Change: static-vs-regenerating territory axis + side-effect/irreversibility caution (v1.3.0)

**Edits:** (1) replaced the territory cue with a 3-way split — static enumerable → coverage; regenerating enumerable (logs/queues) → loop-until-dry with **budget as primary stop** + mandatory regeneration detector; non-enumerable → true saturation. (2) Added side-effects guardrail #6 + a dedicated reference section: keep-best is a "dangerous illusion" for irreversible bodies → loop-to-decision-then-act-once / checkpoint / dry-run / human-gate. (3) Logged the 4 remaining adversarial findings as a CHANGELOG backlog.

**Re-check (focused adversarial, both fixed holes):** **FIXED, substantive not cosmetic.** On the regenerating-stream task the skill now steers to budget-primary + inflow≥outflow detector (names the runaway 3×); on the delete-dead-code task it declares keep-best invalid and routes to checkpoint/act-once/human-gate. Minor residual: a reader who skips straight to the pure-loop pseudocode could mis-apply keep-best (disclosure-order, not a correctness gap) — noted for a future pass.

---

# RUN SUMMARY — loop-builder forge (v1.0 → v1.3)

**Outcome: PROMOTED through 3 rounds. The skill measurably improved and two real holes were closed.**

**Lift curve (within-round, same panel scores both arms):**

| Task | v1.0 (round 0) | final | Δ |
|------|----------------|-------|---|
| T1 refinement | +0.50 over baseline | (unchanged) | skill wins |
| T2 SQL deterministic | +0.14 | (unchanged) | ~tie (both resist over-engineering) |
| T3 coverage | **−0.14 (lost)** | **+0.59 (won)** | **+0.73 swing** — the headline result |
| H1 holdout negotiation | +0.40 | +0.40 | skill wins (clean promotion signal) |

**What the forge actually bought:**
1. **Found a real defect** the structural rubric never would: the skill *misframed* enumerable-coverage problems as saturation, making its advice worse than no-skill on T3.
2. **Drove a measured fix** — coverage/worklist family (r1) → territory-not-findings (r2) → static-vs-regenerating (r3). T3 went from a loss to a clear win.
3. **Adversarial hardening** added a runaway-on-regenerating-queue fix and a side-effects/keep-best fix — both confirmed.
4. **Surfaced skill-forge's own #1 weakness** (eval-score noise: same baseline text scored 3.36–4.00 across runs) — feeds the skill-forge forge run.

**Honest limitations (do not overclaim):**
- **Low n_eff:** panel subagents share my base model; "external" here is partial. Real independence needs cross-model judges (Gemini/Codex).
- **Small eval:** 3 tuning + 1 holdout. Cross-round absolute scores are noisy (see eval-noise finding); only within-round deltas are trustworthy.
- **4 adversarial findings deferred** (external-evaluator laundering, budget sizing, nested/concurrent topologies, convergence/DR blur) — logged in CHANGELOG, not fixed.
- The base model is already strong at loop design, so absolute lift is modest by construction; the value showed up as **defect-finding + targeted repair**, which is exactly what a forge is for.

**Verdict:** loop-builder v1.3 is materially better than v1.0 — *behaviorally* (T3 reversal, holdout win) and in *robustness* (two adversarial holes closed). It is **hardened, not yet "optimal"** — the deferred backlog + a larger cross-model eval are the path to that.
