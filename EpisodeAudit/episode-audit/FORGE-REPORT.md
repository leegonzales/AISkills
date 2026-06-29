# Forge Report — episode-audit

A `skill-forge` campaign run 2026-06-25. Frozen eval = Elliot Skyfall episodes 76/78/79/80/81
(tuning: 76, 78, 80 · holdout: 79, 81). Value shape: **(a) artifact-quality lift + (c) gating/correctness**
(geography & weather-accuracy are hard gates; the panel was warned a correct gate-call may be terse).

## Tier A — structural gate
`validate-skill.sh` PASS at every version (v0.1 → v0.3). Description 663 chars, lean SKILL.md, progressive
disclosure to `references/`.

## Tier B — behavioral lift (two arms: skill vs no-skill baseline; external blind panel; within-pass deltas)

### Round 1 — baseline (v0.1), tuning set, 2 diverse judges
Mean lift (skill − baseline): Judge-fact-checker **+2.0**, Judge-showrunner **+6.0** (both positive; large
inter-judge spread → directional, n=3). Win/■: skill won ep76 decisively, contested on ep78/80.
**Diagnosis (robust, objective — not judge-dependent):** the skill committed a **must-pass M2 false-clear on
ep78** — declared "every claim matches the snapshot" when the data high (89°F) was understated to 84°F. The
gate discipline reliably caught the map-marker drift + freshness (baseline twice skipped the geo gate, M3),
but G2 was executed shallowly and the rubric funneled attention away from un-enumerated defects.

### Round 2 — ONE change: harden G2 (v0.2)
G2 now requires extracting the numeric daily high (= max hourly) and low and diffing vs the script ("low 80s"
when data says 89 is a FAIL), and verifying every depicted condition (smoke/fog) exists in the data. Must show
the numbers checked.

**Promotion eval on FRESH holdout (ep79, ep81), 2 diverse judges, within-pass:**
- ep79: skill **20** vs baseline **10–12** (baseline commits M2 + M3). Both judges agree, decisive.
- ep81: skill **20** vs baseline **10** (baseline fabricates a smoke defect, M1; judge-A mislabeled files — a
  logged noise event the diverse panel + answer key caught).
- **Objective must-pass check (operator-held ground truth):** skill v0.2 is clean on M1/M2/M3 on BOTH holdouts
  and **fixes the R1 M2 violation** (catches 89→84 on ep79, 87→80 on ep81, correctly clears data-backed smoke
  on ep81). Baseline fails M3 on both, M2 on ep79.
- **Decision: PROMOTE v0.2.** Margin far exceeds inter-judge noise; no must-pass regression.

### Round 3 — adversarial round → ONE change: add G3/M4 (v0.3)
Red-team found a real, safety-relevant hole the eval episodes under-stressed: **hazard prominence (buried-lede)
was not gated** — the structure-arc reward literally permitted burying an active flash-flood warning behind
poetry. Independently corroborated by the baseline audit of ep80 ("buries the day's biggest story").
**Change:** G3 hazard-prominence gate + must-pass M4 (an active warning must be in the cold-open/first
conditions block; correct-but-buried = S1). Plus M1/M2 wording tightenings and a documented known-limitations
section (seasonal-scene, timezone, audio, dupe-frames — hand-check, not yet gated).
**Confirmation (single-episode, ep80):** v0.3 fires G3 correctly (catches the buried Red Flag as S1) while
passing data-backed smoke (M1), showing computed high/low (M2), gating all 6 images (M3). *Not* re-run through
the full holdout panel — reported as directional, not a fresh-holdout promotion.

## Lift curve (holdout, skill vs baseline, /20)
```
v0.1 baseline eval (tuning):  skill ≈ baseline +2 to +6, but M2 FALSE-CLEAR present
v0.2 (harden G2):  holdout skill 20 / 20  vs baseline 10 / 10   — must-pass CLEAN, PROMOTED
v0.3 (add G3/M4):  ep80 confirm — G3 buried-lede caught (S1), M1–M4 self-check clean
```
Win-rate skill vs baseline on holdout: **2/2**. Must-pass regressions: **0**. M2 false-clear: **fixed**.

## Stop reason
**Diminishing returns + adversarial-fix-confirmed + budget ceiling.** v0.2 promoted clean on fresh holdout;
v0.3 closed the adversarial finding. Remaining adversarial items are documented as hand-check limitations
(honest gap, not silent). A second campaign should gate the documented limitations (seasonal-scene mismatch,
timezone label, intra-episode dupe frames, rendered-audio) — these need eval episodes that stress them.

## Honest caveats (eval-protocol §6)
- n is small (3 tuning + 2 holdout) → lift magnitudes are **directional**, carried by win-rate + the objective
  must-pass check, not a fragile mean.
- One judge mislabeled audits on ep81 R2 — a real reminder that a single judge is gameable by noise; the
  diverse panel + objective answer key is what caught it.
- v0.3's G3 was confirmed on one episode, not a full fresh-holdout panel.
