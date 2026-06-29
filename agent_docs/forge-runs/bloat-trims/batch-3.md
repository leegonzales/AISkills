# Bloat-Trim Batch 3 — FFmpeg, build-timeline, second-brain (2026-06-28)

Run entirely in **isolated git worktrees** (off `main`), insulated from the concurrent-agent shared-dir
churn that compromised the first batch-2 eval. Trim via the `bloat-trim-batch` workflow (trim→first-pass),
then the **authoritative hardened eval**: frozen worktrees + hand-verified ref-only tokens.

| Skill | Lines | Cut | Verdict | Notes |
|-------|-------|-----|---------|-------|
| **ffmpeg** | 569→327 | 43% | preserved / ship | Tool-wrapper: kept ALL daily-driver CLI inline; created reference-tables.md (7 lookup tables) + advanced-operations.md (GIF/thumbnails/HLS/quality/HW-accel/multi-pass/batch). Bloated had no references/ dir. |
| **build-timeline** | 476→326 | 31% | preserved / ship | Moved 6 event-card HTML templates + 3 theme CSS blocks → html-rendering.md. Bonus: fixed a stale absolute `html-template.html` path → relative. |
| **second-brain** | 427→**115** | 73% | preserved / ship | Kept all 8 `sb` commands + flags inline (improved with inline flag annotations + intent-routing table); moved transcript/workflow prose → workflows-and-examples.md. |

## Hardened eval (the authoritative one)
6 fresh blind agents (3 skills × bloated/trimmed) against **frozen worktree paths**. Trimmed arms were NOT
told to read references. Probe per skill targeted **ref-only, unguessable** moved content; I grep-confirmed
each token is 0 in the trimmed SKILL.md and present in the ref *before* running, so a correct answer proves
a ref read.

| Skill | Probe (moved content) | Ref-only token | Result |
|-------|----------------------|----------------|--------|
| build-timeline | exact Agent-Spawn card HTML + dark-theme CSS | `agent-card`, `#1A202C` | trimmed read html-rendering.md, byte-identical to bloated |
| second-brain | daemons.yml transcript-daemon config | `default_task_priority: 2` | trimmed read workflows-and-examples.md, byte-identical |
| ffmpeg | two-pass palette GIF filtergraph | `palettegen`/`paletteuse` | trimmed read advanced-operations.md, byte-identical |

All three: **PRESERVED, conclusive** — path-verified `FILES OPENED` + reproduced ref-only tokens + byte-identical
output vs the bloated control. Stronger than batch-2 (every probe was genuinely ref-only, none base-guessable).

## Defects caught by hand (validator missed both)
- **second-brain** trimmed SKILL.md had a stray `</content>` tag at EOF (validator passes it) — stripped (116→115 lines).
- **ffmpeg** references/ failed to copy initially (bloated had no references/ dir) — caught and fixed, else the
  pointers would have dangled and the moved tables/operations would be lost.
- **ffmpeg** `vmaf_v0.6.1` model note: the first-pass eval misstated *which* ref holds it; grep confirms it's in
  advanced-operations.md (moved, not lost).

## Confidence ~90%, grounded
Same honest ceiling as batch-2: one moved-content slice tested per skill, single-run, same model family.
Method standard upheld: frozen worktrees, hand-grep verification, eyeball every trim before applying.
