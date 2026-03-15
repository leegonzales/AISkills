# Flywheel Scan Scoring Rubric

**Version:** 1.0
**Purpose:** 4 dimensions x 5 points = max 20. Used by the doppelganger to score proposed work items.

---

## Dimensions

### Goals Alignment (1-5)

How directly does this work item serve Lee's 2026 objectives?

| Score | Definition |
|:-----:|-----------|
| 1 | No connection to any stated objective |
| 2 | Tangential — serves a goal indirectly or with many assumptions |
| 3 | Supports a goal but isn't on the critical path |
| 4 | Directly advances a primary objective (Revenue, Impact, Capability) |
| 5 | Multiplier — advances 2+ objectives simultaneously |

**Reference:** Goals graph objectives: Revenue ($120K), Impact (visibility), Capability (compounding assets), Optionality, Resilience.

### Energy/Impact Ratio (1-5)

How much output per unit of Lee's scarce time and energy?

| Score | Definition |
|:-----:|-----------|
| 1 | High effort, low payoff — energy sink |
| 2 | Moderate effort for modest returns |
| 3 | Fair trade — effort proportional to value |
| 4 | High leverage — small effort, significant impact |
| 5 | Asymmetric — minimal effort unlocks disproportionate value (automation, delegation, compound effect) |

**Constraint awareness:** W-2 + Differential + content + speaking = full capacity. Score against the binding constraint.

### Unblocking Value (1-5)

Does completing this unblock other high-value work?

| Score | Definition |
|:-----:|-----------|
| 1 | Standalone — nothing depends on this |
| 2 | Unblocks 1 low-priority item |
| 3 | Unblocks 1-2 moderate-priority items |
| 4 | Critical dependency — 3+ items waiting on this |
| 5 | Keystone — removing this blocker cascades across multiple repos or goals |

**Check:** beads dependency graph, thread blockers, cross-repo imports.

### Tension Awareness (1-5)

Does this work item navigate or resolve a known tension?

| Score | Definition |
|:-----:|-----------|
| 1 | Ignores or worsens an active tension |
| 2 | Neutral — doesn't engage with tensions |
| 3 | Acknowledges a tension without resolving it |
| 4 | Navigates a tension skillfully (e.g., BetterUp differentiation) |
| 5 | Resolves a tension — creates clarity where there was ambiguity |

**Known tensions:** Revenue focus vs. optionality, W-2 stability vs. independence, volume vs. polish, commitment depth vs. breadth.

---

## Tier Assignment

After scoring, assign to tier based on total score:

| Tier | Score Range | Label | Time Horizon |
|------|:-----------:|-------|-------------|
| 1 | 17-20 | Launch-Critical | This week |
| 2 | 14-16 | Q1 Close | This month |
| 3 | 11-13 | Q2 Setup | Next quarter |
| 4 | 8-10 | Maintain | Low priority |
| 5 | 0-7 | Archive/Defer | Deprioritize |

---

## Scoring Protocol

1. Read all scout findings for the repo
2. Cross-reference with goals graph (`goals_query.py status`)
3. Check beads for existing issues and dependencies
4. Score each dimension independently (don't let one dimension contaminate another)
5. Write rationale before assigning numbers (reasoning first, scoring second)
6. Rank all scored items by total, break ties by unblocking_value
