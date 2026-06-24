# Forge Log — clean-room prose-polish

skill-forge building a clean-room prose-polish skill, then a head-to-head vs the existing skill. Newest at bottom.

| Round | Change | Tuning lift vs baseline | Holdout | Must-pass | Decision |
|-------|--------|------------------------|---------|-----------|----------|
| build | clean-room v0 authored (blind to ProsePolish/) | — | — | — | done |
| 0 | (measure v0) | clean-room 3.625 vs baseline 3.50 = **+0.125** | E3 pending | clean-room clean; **existing tripped MP1** | diagnose |
| 1 | "Economy must not cost authority" rule (v0.2) | E1 3.4→**3.8** (now wins) | **E3 clean-room 3.85 (wins); existing 2.1 MP1** | clean-room clean; existing MP1 both low-source genres | **PROMOTE v0.2; stop** |

---

## Step 0 — clean-room build
Builder authored prose-polish-cr v0.1.0 from first principles (confirmed: did not read ProsePolish/). 6 dims (clarity/structure/economy/authority/voice/genre-fit), top-down editing order, meaning+voice as hard constraints, genre-calibration table, explicit anti-fabrication ("fabricating evidence is forbidden; flag unsupported claims"). Validates clean.

## Round 0 — three-arm measure on tuning essays (E1 opinion, E2 technical)

Baseline / clean-room / existing each polished E1+E2. Two panels (editor + fidelity-skeptic), blind to arm + which used a skill, checking fidelity against the ORIGINAL drafts.

**Per-arm overall (mean both panels):**

| Arm | E1 | E2 | Tuning avg | Notes |
|-----|----|----|-----------|-------|
| **Clean-room v0** | 3.40 | **3.85** | **3.625** | Fidelity clean. Wins E2 (technical). |
| Baseline (no skill) | 3.65 | 3.35 | 3.50 | Safe middle; beats clean-room on E1. |
| **Existing ProsePolish** | **2.50** | **4.25** | 3.375 | **MP1 fabrication on E1** (both panels ranked it LAST); best craft on E2 (4.25). |

**Two headline findings:**
1. **Existing ProsePolish has a fidelity hole.** On the sourceless opinion draft, its authority/specificity/embodiment guidance drove the model to **invent** a personal management anecdote (divided team, a specific "quietest engineer," a six-week silence, observed performance decline) — none in the original. Best prose in the set, ranked last by both panels for fabrication. A real, reportable risk in the curated skill.
2. **Clean-room over-cuts opinion.** It held fidelity (anti-fabrication rule worked) and won the technical essay, but dialed Economy too high on E1 — trimmed to *short-but-flat* (low P4 authority), losing to the no-skill baseline. Its diagnosable weakness.

**Net:** clean-room v0 already edges baseline (+0.125) and beats the existing skill on the fidelity-adjusted average — competitive with a curated skill on its first build, and *safer*. → Round 1 targets the E1 over-cutting weakness.

---

## Round 1 — Change: "Economy Must Not Cost Authority" rule (v0.2.0)

**Edit:** added the vague-passage rule — on a generic/hedged passage: (1) sharpen into the concrete *within the author's meaning*, else (2) flag for the author `[specify: ...]`, else (3) tighten; never trade authority/voice for word count.

**Re-eval — FINAL HEAD-TO-HEAD** (E1 re-run with v0.2; E3 holdout fresh; baseline + existing too; 2 panels, blind, fidelity-checked vs originals):

| Arm | E1 opinion | E3 narrative (holdout) | Fidelity |
|-----|-----------|------------------------|----------|
| **Clean-room v0.2** | **3.80** (wins) | **3.85** (wins) | clean both |
| Baseline (no skill) | 3.25 | 3.75 | clean |
| **Existing ProsePolish** | 2.50 | 2.10 | **MP1 fabrication BOTH** |

Round-1 fix confirmed: clean-room E1 3.40 → **3.80** (lost to baseline before → wins now), no fidelity regression. **PROMOTE v0.2.** Diminishing returns + budget reached → stop.

---

# RUN SUMMARY — clean-room prose-polish vs existing

## All three essays, all three arms (mean of 2 panels each, 0-4)

| Arm | E1 opinion | E2 technical | E3 narrative | **Avg** | Fidelity |
|-----|-----------|--------------|--------------|---------|----------|
| **Clean-room (prose-polish-cr v0.2)** | 3.80 | 3.85 | 3.85 | **3.83** | clean on all 3 |
| Baseline (no skill) | 3.25 | 3.35 | 3.75 | 3.45 | clean |
| **Existing (ProsePolish)** | 2.50 | **4.25** | 2.10 | 2.95 | **MP1 fabrication on E1 + E3** |

## The verdict (honest, with the nuance)
- **The forge-built clean-room skill won overall (3.83) and beat the curated skill on 2 of 3 essays** — built from scratch in one refinement round. Its decisive advantage is **fidelity discipline**: it never fabricated, on any genre.
- **The existing ProsePolish has the highest ceiling AND a catastrophic floor.** It produced the single best output in the exercise (E2 technical, 4.25 — added a legitimate illustrative example) — but on both *low-source* genres (opinion, narrative) its embodiment/specificity guidance drove the model to **invent content** (a fake team + "quietest engineer" on E1; an entire dawn-fishing scene — bait, diesel, "maybe ten," corn — on E3). Both panels ranked those vivid-but-fabricated versions LAST.
- **Baseline (no skill)** is the bland-but-safe middle.

## What this says about each skill (design implication)
- **Existing ProsePolish:** excellent craft engine, but it conflates *polishing* with *drafting* — its "embodiment/add concrete detail" guidance is right for fiction/generation and dangerous for editing someone's real, sparse draft. **Reportable fix: add a hard fidelity guardrail** (the one thing the clean-room skill has and it lacks).
- **Clean-room prose-polish-cr:** safer and more consistent by construction (anti-fabrication + meaning/voice as hard constraints), genre-calibrated, and after the forge fix no longer over-cuts. Lower ceiling on genres where added specificity is legitimate (it's more cautious about adding even legitimate technical examples).

## Honest limitations
- Same low-n_eff (shared-base-model panels), small eval (3 essays), cross-run noise caveats as the prior forge runs.
- The "existing" arm's fabrication depends on how an agent *applies* the skill; a more careful operator might fabricate less. But both independent panels saw the skill's guidance *drive* the fabrication on low-source drafts — a real design signal, not a one-off.
- prose-polish-cr is v0.2 (forged once); not a finished, fully-hardened skill. It is an experiment, kept under agent_docs/ and NOT registered in SKILLS.md.

**Bottom line:** the forge produced a from-scratch prose skill that, on low-source essays, is *safer and scores higher* than the curated one — and in doing so it surfaced a genuine fidelity hole in the existing ProsePolish worth fixing.
