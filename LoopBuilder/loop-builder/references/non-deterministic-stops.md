# Non-Deterministic Stop Conditions

The hard part of loop design. Read this when the loop's "done" can't be written as a fixed predicate.

## The core model

A loop is **`body` + `stop`**.

- A **deterministic stop** is a predicate over state you can mechanically check: `i < n`, `tests pass`, `queue empty`, `error == null`. If you can write it, write it — it's cheap and trustworthy.
- A **non-deterministic stop** is needed when "done" depends on a *judgment* about open-ended quality, completeness, or correctness — "is this design good enough?", "have we found all the bugs?", "is the prose there yet?". You cannot write a fixed predicate, so you **replace the predicate with an evaluator.**

> The entire craft of a non-deterministic loop is making that evaluator trustworthy — and **always** pairing it with a deterministic budget ceiling so a judgment that never fires still terminates.

Two non-negotiable rules before anything else:

1. **Every non-deterministic loop pairs a soft (judgment) stop with a hard (budget) stop.** Belt and suspenders. The soft stop decides *quality is reached*; the hard stop guarantees *termination*. Ship neither alone.
2. **The evaluator is external to the generator.** A loop that grades its own output will declare itself done. Separation of powers is the difference between a real gate and theater.

---

## The taxonomy of non-deterministic stops

Pick one (or compose several). Each: what it is · when to use · how to implement · how it fails.

### 1. Judge-gate (rubric "good enough")
- **What:** an evaluator scores the artifact against an explicit, *pre-committed* rubric; stop when score ≥ bar.
- **When:** quality is the target and you can articulate what good looks like.
- **Implement:** external LLM-as-judge or a human, scoring against a written rubric. The bar is fixed *before* the loop runs (no moving goalposts).
- **Fails via:** self-grading (model passes itself), sycophancy, Goodhart (optimizes the rubric, not the goal). **Mitigate:** external + diverse judges; held-out cases; rotate/expand criteria when you see gaming.

### 2. Convergence / fixed-point
- **What:** stop when iteration N's output is materially the same as N−1.
- **When:** refinement-to-stability (editing, optimization that asymptotes).
- **Implement:** semantic/embedding diff or structural diff between rounds; stop when delta < ε for ≥2 consecutive rounds.
- **Fails via:** premature convergence (stuck in a local optimum), oscillation (A→B→A). **Mitigate:** require *improvement*, not mere sameness; add perturbation; detect cycles (see failure-modes).

### 3. Mutual approval (multi-party convergence)
- **What:** two or more **independent** reviewers approve the *same unchanged* version.
- **When:** high-stakes artifacts where one judge isn't enough.
- **Implement:** round-trip — reviewer A flags → fix → reviewer B reviews the fixed version → succeed only when neither requests changes on one version.
- **Fails via:** correlated reviewers (low effective n) agreeing because they share blind spots, not because it's right. **Mitigate:** diverse models/lenses (the n_eff principle — two copies of the same judge ≈ one judge).

### 4. Diminishing returns
- **What:** stop when marginal gain per round falls below a worthwhile threshold over the last K rounds.
- **When:** improvement is measurable and asymptotic; you want the knee of the curve, not perfection.
- **Implement:** track score delta per round; stop when smoothed delta < threshold for K rounds. Enforce a **minimum-rounds floor** so you don't stop in the first flat spot.
- **Fails via:** noisy metric masking real gains; stopping in a temporary plateau. **Mitigate:** smoothing; minimum floor; pair with a quality bar so you don't stop *below* acceptable just because gains slowed.

### 5. Streak / stability
- **What:** stop after N consecutive successes with no failure.
- **When:** reliability/robustness is the target (flaky-test fixing, "prove it works").
- **Implement:** counter that **resets to zero on any failure**; stop at N. Use realistic, varied cases.
- **Fails via:** N too small (luck passes as proof). **Mitigate:** size N to the confidence you need; diversify the cases so a streak means generalization, not repetition.

### 6. Saturation (loop-until-dry)
- **FIRST, classify the discovery space — this is the most-missed call, and the trap is subtle.** Separate the **search territory** (the surface you sweep) from the **findings** (what you're looking for). The findings are often unbounded ("all the bugs", "every edge case"). Classify on the **territory**, and on a *second* axis — **is the territory static or regenerating during the sweep?** Three cases, three different stops:
  - **Static enumerable territory** (files in a repo at HEAD, rows in a fixed table, endpoints in a spec) → **coverage / worklist-exhaustion**, a *deterministic* stop: build the prioritized worklist, process every item until empty, done. Budget is a backstop.
  - **Regenerating / streaming enumerable territory** (error logs, a live queue, lint on a changing tree, a self-feeding codegen worklist) → **loop-until-dry *with a re-scan*** — and here the **budget ceiling is the PRIMARY termination guarantee, not a backstop**, because "process until empty" can run forever when items refill as fast as you clear them. A regeneration detector (is the inflow rate ≥ the clear rate?) is mandatory; if it is, you're draining an ocean — switch to a time-boxed/rate-based stop, not exhaustion.
  - **Non-enumerable space** (open-ended ideation, "what else could possibly break?" with no listable surface) → **true saturation**: K consecutive dry rounds.
  The classic error: seeing unbounded *findings* → reaching for saturation → throwing away the clean deterministic coverage you could have had over a static territory. The *dangerous* error: seeing a listable territory → "process until empty" → **runaway** on a regenerating queue. Ask both: *can I list the territory?* and *does it refill while I work?*
  (Note: some `loop-library.md` entries are tagged "Det | saturation" — read those as the *static-coverage* or *regenerating-drain* cases above; the library label predates this three-way split.)
- **What (saturation proper):** stop after K consecutive rounds surface **nothing new** (no new findings/ideas) over a space you *cannot* enumerate.
- **When:** open-ended discovery of unknown size where no worklist exists.
- **Implement:** dedup each round's output against a `seen` set; count consecutive empty rounds; stop at K.
- **Fails via:** stopping at the easy tail; correlated searchers all missing a whole modality (so "dry" is false); **and being used at all when the space was actually enumerable.** **Mitigate:** classify enumerable-vs-unbounded first; diverse search angles each round; a final completeness-critic pass ("what modality did we never try?").

### 7. Holdout generalization
- **What:** promote/stop only when the gain holds on **fresh cases unseen during iteration**.
- **When:** any loop optimizing against an eval set (skill-tuning, prompt-tuning) — the anti-overfitting stop.
- **Implement:** keep a sacred holdout set; at each promotion, check the candidate on fresh holdouts; keep only if it beats baseline there too.
- **Fails via:** holdout leakage (the loop has secretly seen them). **Mitigate:** keep holdouts out of the loop's context entirely; rotate.

### 8. Budget ceiling (the backstop — ALWAYS present)
- **What:** a hard cap on iterations / tokens / wall-clock / dollar cost.
- **When:** **always.** This is not a quality stop; it's the safety net under every soft stop.
- **Implement:** a counter and an abort. When hit, stop and **report what was unfinished** (never silently truncate as if complete).
- **Fails via:** being the *only* stop (you get a fixed-length grind, not a quality outcome), or silent truncation. **Mitigate:** pair with a real quality stop; log the cap-hit loudly.

### 9. Human / escalation checkpoint
- **What:** hand the continue/stop decision to a person at a gate.
- **When:** stakes are high, confidence is low, the loop is thrashing, or the judgment genuinely can't be automated safely.
- **Implement:** pause-and-ask at defined points; or auto-escalate when another condition (oscillation, low judge-confidence, budget 80%) trips.
- **Fails via:** asking too often (defeats the point) or never (defeats the safety). **Mitigate:** escalate on signal, not on schedule.

### 10. Epistemic stopping point (the judgment gate)
- **What:** the meta-condition — *"is another iteration worth its cost, given the goal?"* Explicitly weigh expected marginal value against marginal cost.
- **When:** the honest answer to "when is it good enough" — usually composed from several of the above.
- **Implement:** at each round, an evaluator answers "would one more round plausibly change the decision this artifact feeds?" If no, stop. This is the disciplined version of taste.
- **Fails via:** rationalizing "done" because you're tired (premature) or because it's never perfect (endless). **Mitigate:** tie it to the *downstream decision* the artifact serves, not to abstract perfection.

---

## Composition: the standard robust shape

Most good non-deterministic loops compose **a quality stop + a progress stop + a budget backstop**, and keep the best result seen:

```
best ← null
for round in 1..BUDGET:                      # (8) budget ceiling — hard backstop
    candidate ← body(best)
    score ← EXTERNAL_evaluate(candidate)     # (1) judge-gate — external, not self
    if score > score(best): best ← candidate # keep-BEST, never blindly take latest
    if score ≥ BAR: break                    # (1) quality reached
    if delta(score) < ε for last K: break    # (4) diminishing returns
    if cycle_detected(): escalate()          # (9) thrashing → human
return best                                  # ship the best, not the last
```

Note **`keep-best`**: track and return the best artifact across iterations; never assume the latest round is the best — non-deterministic loops can degrade.

---

## Side effects break keep-best — handle them explicitly

The canonical shape assumes a **pure body**: each round produces a *candidate* you can score and discard. Many real loops **act on the world** each round — delete files, send email, open PRs, change prod config. For those, "keep-best, ship the best not the last" is a **dangerous illusion**: you cannot un-send round 3's email or un-delete its branch by selecting an earlier "best." When the body has irreversible side effects:

- **Separate proposing from committing.** Loop to a *decision* (pure), then act once at the end — don't act every round.
- If you must act each round: **dry-run / checkpoint / commit-per-round** so each action is individually reversible, and treat the loop as advancing real state (not producing a discardable candidate). keep-best does not apply; "best" is wherever you stopped.
- **Gate irreversible actions behind a confirmation or a human checkpoint**, especially when the stop is a judgment.

## Design rules (the checklist)

1. **Soft stop + hard budget, always.** No exceptions.
2. **Evaluator external to generator.** Separate the hand that makes from the eye that judges.
3. **Pre-commit the bar, in writing.** A bar you can move mid-loop is not a bar.
4. **Keep-best, not keep-last.** Defend against degradation.
5. **Detect non-progress, not just progress.** Oscillation and plateaus are stop signals too.
6. **Diverse > redundant evaluators.** Correlated judges give false confidence (n_eff).
7. **Generalize, don't memorize.** Check fresh holdouts before declaring victory.
8. **On budget-cap, report the gap.** Silent truncation reads as "done" when it isn't.
9. **Tie "good enough" to the downstream decision**, not to abstract perfection.

See [loop-failure-modes.md](loop-failure-modes.md) for the dangers each rule defends against, and [loop-library.md](loop-library.md) for worked examples classified by stop family.
