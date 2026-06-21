---
name: loop-builder
description: Design and build robust agent loops — iterative workflows that drive toward a goal and know when to stop. Use when creating any repeated/iterative agent process (refine until good, search until found, review until approved, improve until converged), choosing a loop pattern, or fixing a loop that runs away, degrades, or never finishes. Specializes in loops WITHOUT deterministic stop conditions (judgment-based "good enough"). Triggers include "build a loop", "iterate until", "refine/improve until", "keep going until", "agent loop", "when should it stop", "loop won't terminate", or designing a self-improving/review/discovery loop.
---

# Loop Builder

Build agent loops that are **productive** (they make progress), **safe** (they always terminate), and **honest** (they stop for a real reason, not because they got tired or graded themselves).

## When to use

Reach for this whenever you're designing a process that *repeats*: refine-until-good, search-until-found, review-until-approved, improve-until-converged, generate-and-select, monitor-and-act, discover-until-dry. Also use it to *diagnose* a loop that misbehaves (runs forever, gets worse over time, oscillates, or declares itself done falsely).

## The core model

> **A loop is a `body` + a `stop`.** The body is the work that repeats. The stop is the condition that ends it. Getting the body right is usually easy; **getting the stop right is the whole craft.**

Two kinds of stop:

- **Deterministic** — a predicate you can mechanically check: `tests pass`, `count == 0`, `i < n`. **If you can write it, write it.** Cheap, trustworthy, done.
- **Non-deterministic** — "done" depends on *judgment* about open-ended quality/completeness/correctness ("good enough?", "found them all?", "do reviewers agree?"). You can't write a fixed predicate, so you **replace it with an evaluator** — and now you must make that evaluator trustworthy. This is the hard, valuable case. → **[references/non-deterministic-stops.md](references/non-deterministic-stops.md)**

## Build workflow

1. **State the goal as a stop, not a body.** Write the sentence "this loop is done when ___." If you can't finish it, you don't understand the loop yet.
2. **Classify the stop.** Is "done" a predicate (deterministic) or a judgment (non-deterministic)? If deterministic — write the predicate, add a budget cap, done. If non-deterministic — continue. *Discovery/coverage cue:* if the work to do is **enumerable** ("can I list the things to check?" — files, endpoints, rows), it's **worklist-exhaustion (deterministic)**, not saturation; only genuinely unlistable spaces need a judgment stop.
3. **Pick a stop family** (see taxonomy below) — judge-gate, convergence, mutual-approval, diminishing-returns, streak, saturation, holdout-generalization, human-checkpoint, epistemic-stopping-point. Often compose 2-3.
4. **Pick or adapt a loop shape** from **[references/loop-library.md](references/loop-library.md)** (57 cataloged loops by category, each tagged deterministic vs non-deterministic with its stop family). Don't invent what's cataloged.
5. **Add the mandatory guardrails** (below).
6. **Red-team it** against **[references/loop-failure-modes.md](references/loop-failure-modes.md)** before shipping.

## Non-deterministic stop families (pick/compose)

| Family | Ends when… |
|--------|-----------|
| **judge-gate** | an *external* evaluator scores ≥ a pre-committed bar |
| **convergence** | successive iterations stop changing materially |
| **mutual-approval** | 2+ *independent* reviewers approve the same unchanged version |
| **diminishing-returns** | marginal gain per round drops below threshold (with a minimum-rounds floor) |
| **streak** | N consecutive successes (counter resets on any failure) |
| **coverage / worklist-exhaustion** | an *enumerable* work set is fully processed — *deterministic*; prefer this whenever the discovery space is finite/listable |
| **saturation (loop-until-dry)** | K consecutive rounds find nothing new — only for *unbounded/unlistable* discovery |
| **holdout-generalization** | the gain holds on fresh, unseen cases (anti-overfit) |
| **human-checkpoint** | a person decides continue/stop at a gate or on a signal |
| **epistemic-stopping-point** | one more round wouldn't change the downstream decision |

Full detail, implementation, and per-family failure modes: **[references/non-deterministic-stops.md](references/non-deterministic-stops.md)**.

## Mandatory guardrails (every non-deterministic loop)

1. **Soft stop + hard budget — always.** The judgment stop decides *quality reached*; a hard budget ceiling (iterations / tokens / wall-clock / $) guarantees *termination*. Never ship one without the other. On cap-hit, **report what's unfinished** — never silently truncate.
2. **Evaluator external to the generator.** A loop that grades its own output will pass itself. Separate the hand that makes from the eye that judges (use a different model/agent, a panel, or a human).
3. **Keep-best, not keep-last.** Track and return the best artifact across rounds; non-deterministic loops can degrade — don't assume the latest is the best.
4. **Diverse > redundant judges.** Correlated reviewers give false confidence; two copies of one judge ≈ one judge (effective-n).
5. **Pre-commit the bar in writing.** A bar you can move mid-loop isn't a bar.

The canonical robust shape:
```
best ← null
for round in 1..BUDGET:                  # hard backstop — always present
    candidate ← body(best)
    score ← EXTERNAL_evaluate(candidate) # external judge, pre-committed bar
    if better(candidate, best): best ← candidate   # keep-best
    if score ≥ BAR: break                # quality reached
    if plateau(last K) or cycle(): break/escalate   # progress stalled
return best                              # ship best, not last
```

## Composing with other skills
The evaluator in a judge-gate or mutual-approval loop should reuse existing review infrastructure rather than reinvent it: **multiagent-review** (parallel reviewer panel), **gemini-peer-review** / **codex-peer-review** (independent external models for true convergence), **prose-polish** (quality scoring for written artifacts), **claimify** (assumption/contradiction checks). For execution-heavy loops, the **ralph-wiggum** plugin is a ready loop engine; **Beads** (`bd`) holds cross-session task state.

## What good looks like
A finished loop design names: the body, the stop family(ies), the external evaluator and its pre-committed bar, the budget ceiling, the keep-best rule, and how it handles cap-hit and non-progress. If any of those is missing, it's not done.
