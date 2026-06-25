# Frozen Eval Set — loop-builder

**Frozen 2026-06-21, before any refinement round. Do not edit mid-run** (changing the target invalidates the measurement). Tasks split into tuning (loop may iterate against) and holdout (scored only at promotion).

## The behavioral question
Does an agent given the loop-builder skill design **better agent loops** than an agent without it — measurably, reliably, on tasks it wasn't tuned against?

## Output rubric (score each 0-4: Absent / Weak / Adequate / Strong)
A loop *design* is scored on:

| Dim | Dimension | What strong looks like |
|-----|-----------|------------------------|
| D1 | **Stop correctly classified** | Recognizes whether the stop is deterministic (writes the predicate) or non-deterministic (uses an evaluator). Does NOT over-engineer a deterministic problem. |
| D2 | **Termination guaranteed** | A hard budget/iteration ceiling is present so the loop always halts. |
| D3 | **Stop is non-gameable** | For judgment stops: evaluator is external to the generator; bar pre-committed; not self-graded. |
| D4 | **Degradation handled** | Keep-best-not-last, or otherwise defends against later rounds being worse. |
| D5 | **Non-progress handled** | Detects oscillation/plateau; escalates or exits rather than thrashing. |
| D6 | **Body is sound & actionable** | The repeated step actually advances the goal; design is concrete enough to implement. |
| D7 | **Right-sized** | No needless ceremony for a simple loop; no missing rigor for a hard one. |

**Overall** = mean of D1-D7 ×, reported per-dimension too. **Win** = skill-arm strictly > baseline-arm on overall.

## Must-pass checks (regression here = REVERT, regardless of average)
- **MP1:** Never proposes a non-deterministic loop with no hard budget ceiling (the cardinal sin — a runaway loop).
- **MP2:** Never proposes self-grading as the sole gate on a judgment stop.

## Tasks

### Tuning (loop may iterate against these)
- **T1 (refinement / judge-gate):** "Design an agent loop that refines a marketing landing page until it's good enough to ship." *(Trap: easy to write a runaway 'until good' loop with no budget and self-grading.)*
- **T2 (deterministic, disguised):** "Design a loop that keeps optimizing a SQL query until it's fast enough." *(Trap: 'fast enough' can be a real deterministic predicate — `p95 < 200ms`. A strong design recognizes this and does NOT reach for a judge. Tests D1/D7.)*
- **T3 (discovery / saturation):** "Design a loop for an agent to find as many real bugs as possible in a large codebase." *(Tests saturation/loop-until-dry + diverse-search + completeness; trap: stop at the easy tail.)*

### Holdout (scored ONLY at promotion — kept out of iteration context)
- **H1 (convergence / mutual-approval, no deterministic stop):** "Design a loop where two agents negotiate a contract back-and-forth until they reach an agreement." *(Tests convergence vs mutual-approval, oscillation handling, and a budget backstop when 'agreement' may never come.)*

## Arms
- **Baseline:** capable agent, the task only, no skill.
- **Skill:** same agent + the loop-builder SKILL.md and references in context.
Same model, same framing, same budget. Panel scores blind to arm + blind to skill authorship.

## Stop conditions for THIS forge run (budget-bounded dogfood)
- Budget ceiling: **3 refinement rounds max**.
- Early stop: diminishing returns (a round yields < +0.3 overall lift on tuning) OR holdout win achieved with no must-pass regression.
