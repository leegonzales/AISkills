# Loop Failure Modes

The ways agent loops — especially non-deterministic ones — go wrong, how to detect each, and how to defend. Use this as the red-team checklist when designing or reviewing a loop.

| # | Failure mode | What it looks like | Detect | Defend |
|---|--------------|--------------------|--------|--------|
| 1 | **Runaway** | Loop never terminates; burns tokens/cost/time | No hard cap; soft stop that never fires | **Budget ceiling on every loop** (iterations/tokens/wall-clock/$). The one rule with no exceptions. |
| 2 | **Degradation / drift** | Later iterations are *worse* than earlier ones; final output below an earlier peak | Score later rounds vs earlier | **Keep-best, not keep-last** — track and return the best artifact seen, never blindly the latest. |
| 3 | **Oscillation / non-convergence** | A→B→A→B flip-flop; "fixes" undo each other | Cycle detection (hash/embedding of recent states) | Detect cycles, not just progress; on cycle → perturb, change strategy, or escalate to a human. |
| 4 | **Premature convergence** | Stops early at a local optimum; "stable" but mediocre | Output stable but quality bar unmet | Require *improvement* not mere sameness; add perturbation/temperature; minimum-rounds floor. |
| 5 | **Self-declared done (reward hacking)** | The loop grades its own work and passes itself | Evaluator == generator | **External evaluator.** The judge must be a different hand than the maker. |
| 6 | **Sycophantic / correlated convergence** | Multiple judges "agree" because they share blind spots, not because it's right | All judges same model/prompt/lens | **Diverse evaluators** (different models, different lenses). Effective-n, not raw count: two copies of one judge ≈ one judge. |
| 7 | **Goodhart / metric gaming** | Score climbs while real quality doesn't; loop optimizes the proxy | Score up but spot-checks/holdouts flat | Hold out fresh cases; rotate/expand criteria; keep a qualitative human spot-check; tie the metric to the downstream decision. |
| 8 | **Overfitting to the eval set** | Great on the tuning set, fails on anything new | Gap between tuning-set and holdout performance | Sacred holdout checked at promotion; never let the loop see it; rotate. |
| 9 | **False saturation (premature "dry")** | "No new findings" but a whole modality was never searched | All searchers used the same angle | Diverse search angles each round; a completeness-critic pass: "what did we never try?" |
| 10 | **Silent truncation** | Budget cap hit, output presented as if complete | Cap-hit not surfaced | On cap, **report what's unfinished**; never let a backstop masquerade as a quality stop. |
| 11 | **Context rot (long loops)** | Quality decays as context fills with stale iteration history | Long-running loop, degrading coherence | Fresh context per round where possible (re-read source-of-truth, à la Ralph); summarize/compact; carry forward only what's load-bearing. |
| 12 | **Cost blowup** | Correct but economically ruinous (huge fan-out × many rounds) | Token/$ per useful unit of progress | Budget in $/tokens, not just iterations; cheaper models for cheap stages; cap fan-out width. |
| 13 | **Thrash without progress** | Busy every round, goal no closer | Progress metric flat despite activity | Diminishing-returns stop; escalate on flat-progress; re-examine whether the body actually advances the goal. |
| 14 | **Moving goalposts** | "Done" keeps being redefined so the loop never ends (or ends whenever) | Bar changes mid-loop | Pre-commit the bar in writing before the loop runs; changing it opens a new, logged experiment. |

## The two rules that prevent most of these

1. **Soft stop + hard budget on every loop.** (#1, #10, #12)
2. **External, diverse evaluator scoring against a pre-committed bar, keep-best across rounds.** (#2, #5, #6, #7, #14)

## Red-team prompt for reviewing any loop design
> Could this loop run forever? (→ #1) Could it end *worse* than it started? (→ #2) Could it flip-flop? (→ #3, #13) Who judges "done," and could they pass themselves or share the maker's blind spots? (→ #5, #6) Is the bar fixed in writing? (→ #14) Does success on the eval set mean success in the world? (→ #7, #8) When the budget caps it, does the user learn what's unfinished? (→ #10)
