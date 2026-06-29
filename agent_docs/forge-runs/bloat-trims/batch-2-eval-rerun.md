# Bloat-Trim Batch 2 — Behavioral Eval (corrected, frozen-worktree re-run, 2026-06-28)

This supersedes an earlier manual before/after eval that was **methodologically compromised** and should not be trusted — recorded here honestly because the failure is instructive.

## The compromised first attempt (retracted)
A first before/after run pointed the "trimmed-arm" agents at the **mutable working-tree path**. While it ran, a *concurrent agent in the same working directory* switched the branch (`chore/trim-batch-2 → main → feat/fleet-pr-review-skill`), reverting the tree to the **bloated** SKILL.md files. So the "trimmed arm" may have read bloated files, and file resolution leaked across three locations. The ~88% confidence reported from it was **not trustworthy** — the inputs were uncontrolled. Classic two-agents-one-working-dir collision (CLAUDE.md §7).

## The trustworthy re-run (this record)
Re-run in **frozen, isolated git worktrees** so no concurrent checkout could move the ground:
- `.worktrees/eval-trimmed` → `chore/trim-batch-2` (trimmed: 221/63/149 lines)
- `.worktrees/eval-bloated` → detached `main` (bloated: 698/747/741 lines)

6 fresh blind agents (3 skills × bloated/trimmed). Trimmed arms were **not** told to read references — whether they did was driven only by the SKILL.md's own pointer. Each reported `FILES OPENED`; the worktree-specific paths let me confirm which version each actually read.

| Skill | Trimmed arm read the right ref? (path-verified) | Produced ref-only content? | Verdict |
|-------|--------------------------------------------------|----------------------------|---------|
| **nano-banana** | ✓ `eval-trimmed/…/branded-infographic-catalyst.md` | **Yes** — `#C4785A`, `#B8A888`, `#8FB08F`, full per-element table | **PRESERVED — conclusive** |
| **aws-serverless-eda** | ✓ `eval-trimmed/…/serverless-patterns.md` | Yes — exact webhook CDK + `Duration.seconds(29)` + `202` | **PRESERVED** |
| **codex-peer-review** | ✓ `eval-trimmed/…/synthesis-framework.md` | Yes — Pattern-3 template + Good/Poor transparency pairs | **PRESERVED** |

## Self-verification (not agent self-report)
For nano I grepped the **frozen** files myself: `#C4785A`, `#B8A888`, `#8FB08F`, and "Container backgrounds" are **count 0 in the trimmed SKILL.md** and **>0 only in the reference**. The trimmed arm produced them — so it *provably* read the reference; the content exists nowhere else it was given. This is proof-of-read independent of the agent's self-report (which corroborates).

A correction the clean run surfaced: in the compromised run the aws trimmed arm read the *wrong* refs and answered from base knowledge, which had made the aws moved content look "base-redundant." In the frozen run it read `serverless-patterns.md` correctly — so that earlier characterization was an artifact of the broken setup, not a real property.

## Honest confidence: ~90%
Grounded (self-verified), zero regressions. Residual ceiling: **one moved-content slice tested per skill** (each skill moved several things — other slices are extrapolation), single-run, same model family. "This slice provably survives" is measured; "all moved content survives" is not.

**Standard going forward:** any trim eval runs against frozen commit-extracted paths in an isolated worktree, with the load-bearing claim grep-verified by hand — never against a mutable shared working tree.
