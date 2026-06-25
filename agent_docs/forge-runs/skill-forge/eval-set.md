# Frozen Eval Set — skill-forge

**Frozen 2026-06-21, before any refinement round. Do not edit mid-run.**

## Behavioral question
Does an agent given the skill-forge skill produce a **better plan for evaluating/improving a skill** than an agent without it — measurably, on tasks it wasn't tuned against?

## Output rubric (score each 0-4)
| Dim | Dimension | Strong = |
|-----|-----------|----------|
| E1 | **Behavioral focus** | Measures whether the skill improves real OUTPUTS, not just structure/format. |
| E2 | **External, non-self-grading** | Scoring is independent of the agent/skill that produced the output. |
| E3 | **Anti-overfit / held-out** | Uses fresh, held-out cases; doesn't tune and judge on the same set. |
| E4 | **Lift defined** | Compares against a no-skill baseline; states magnitude AND reliability/win-rate. |
| E5 | **Loop discipline** | One change/round, keep-best, pre-committed bar, an explicit stop condition. |
| E6 | **Variance/noise handling** | Enough tasks/judges that the signal is trustworthy; distinguishes noise from lift. |
| E7 | **Right-sized & actionable** | A plan you could actually run this week; not ceremony. |

**Overall** = mean. **Win** = skill-arm strictly > baseline.

## Must-pass (regression = REVERT)
- **MP1:** Never declares a skill "good/ready" on structure alone, with no behavioral/output evidence.
- **MP2:** Never relies solely on the skill grading its own output (self-grading).

## Tasks
### Tuning
- **T1:** "How would you evaluate whether a new `commit-message-writer` skill is actually good — not just well-formatted?"
- **T2:** "I tweaked my PRD skill's prompt and it feels better. How do I know it actually improved the skill?"

### Holdout (scored only at promotion)
- **H1:** "Set up an evaluation to decide whether our `incident-postmortem` skill is ready to ship to the team."

## Arms
Baseline = capable agent, task only. Skill = same agent + skill-forge SKILL.md + references. Panel scores blind to arm + authorship.

## Stop conditions (budget-bounded dogfood)
- Budget: 2 refinement rounds max.
- Early stop: holdout win with no must-pass regression, OR diminishing returns (< +0.3).

## Prior (from the loop-builder forge run)
That run surfaced **eval-score noise**: the same baseline text scored 3.36–4.00 across panel runs. Strong hypothesis that skill-forge's **E6 (variance handling)** is its weakest dimension — it under-specifies eval-set size, panelist count, and within-round vs cross-round comparison. Likely Round-1 target.
