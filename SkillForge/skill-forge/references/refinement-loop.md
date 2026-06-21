# Refinement Loop

The flywheel that turns a measured eval (see [eval-protocol.md](eval-protocol.md)) into an optimal skill. This is a non-deterministic loop — it obeys every rule in `loop-builder`'s `references/non-deterministic-stops.md`.

## The loop

```
0. FREEZE        eval set + output rubric + must-pass checks + the bar    (once, in writing)
   best ← current skill version; baseline ← Tier-B run of best

1. DIAGNOSE      across the eval outputs, find the SINGLE weakest dimension
                 or the most common failure mode (lowest mean, or a must-pass near the edge)

2. REVISE        make ONE targeted change to the skill addressing that weakness
                 (one hypothesis per round — so the lift is attributable)

3. RE-EVAL       run Tier B on the candidate over the frozen tuning set + FRESH holdouts;
                 score externally (panel, blind where possible)

4. PROMOTE?      keep the candidate ONLY if:
                   • it beats `best` by ≥ margin on the holdout, AND
                   • it regresses NO must-pass check
                 else REVERT to `best` and try a different/narrower change

5. ADVERSARIAL   red-team the promoted version: a separate agent tries to make it fail or
                 rationalize around its instructions (the writing-skills test).
                 A hole found here becomes the next DIAGNOSE.

   repeat 1-5 until a STOP fires.   best is always the shipped artifact (keep-best, not keep-last).
```

## Stop conditions (any one fires — all non-gameable)

| Stop | Fires when |
|------|-----------|
| **self-improving champion** | candidate beats baseline on *fresh* holdouts without weakening a must-pass |
| **quality streak** | N consecutive holdout tasks clear the bar (counter resets on any miss) |
| **multi-LLM convergence** | two independent reviewers approve the *same unchanged* version |
| **diminishing returns** | last K rounds each produced < threshold lift (with a minimum-rounds floor) |
| **budget ceiling** | hard cap on rounds/tokens/$ — the backstop; on cap, **report the gap**, never silent |

Compose them: a typical run stops on *champion + streak*, with *diminishing-returns* as the graceful exit and *budget* as the hard backstop.

## Why each guard exists (maps to loop-builder failure modes)

- **Freeze the eval first** → can't tell improvement from drift otherwise.
- **One change per round** → attributable lift; no tangled regressions.
- **Fresh holdout at promotion** → defeats overfitting (Goodhart / memorization).
- **External, blind, diverse scoring** → defeats self-grading and sycophantic convergence.
- **Must-pass gates promotion independently** → a higher average can't smuggle in a broken non-negotiable.
- **Keep-best** → non-deterministic loops degrade; never ship the latest just because it's latest.
- **Adversarial round** → "passes the rubric" ≠ "can't be rationalized around"; the skill must hold under pressure.

## Worked example — forging the `prd` skill

> **Freeze:** 8 real product briefs (5 tuning, 3 holdout) + the PRD rubric + must-pass {"every metric has baseline+direction+deadline", "non-goals always present"}. Bar: holdout mean ≥ 4.0/5, win-rate ≥ 0.8.
> **Baseline:** skill arm 3.4 vs no-skill 2.9. Weakest dimension: *success metrics* (2.6) — vanity metrics with no baseline.
> **Round 1 — Revise:** add a clarify-gate that refuses to emit a metric without baseline+direction+deadline. **Re-eval:** metrics 2.6→4.1, others flat, no must-pass regression → **PROMOTE**.
> **Round 2 — Diagnose:** *non-goals* thin (3.1). **Revise:** require an explicit "Out of scope (and why)" block. **Re-eval:** non-goals 3.1→4.0 but *traceability* dropped 4.2→3.6 → must-pass intact but net wobble → **keep (net +), flag traceability for next round**.
> **Round 3 — Adversarial:** red-teamer feeds a brief with no baseline data; skill estimates one silently (must-pass violation). **Revise:** skill must mark it `TBD` and ask, never fabricate. **Re-eval:** holds.
> **Stop:** rounds 4-5 yield <0.1 lift on holdout AND two independent reviewers approve the same version → *diminishing-returns + convergence*. **Ship.** Lift curve: holdout 3.4 → 4.3, win-rate 0.6 → 0.9.

## Output of a forge run (what to report)
- The frozen eval set (or a pointer to it).
- The **lift curve**: baseline → final, overall and per-dimension.
- The final externally-verified score and **win-rate** on the holdout.
- The **stop reason**.
- Confirmation the adversarial round passed.
- The diff history (what each round changed) — so the improvement is auditable.

If you can't produce the lift curve, you have a *validated* skill, not a *forged* one.
