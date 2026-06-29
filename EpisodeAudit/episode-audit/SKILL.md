---
name: episode-audit
description: Audit a generated weather-broadcast episode — its images and its talk track — against a grounded rubric, and return prioritized, implementable fixes. Use when reviewing an Elliot Skyfall (or similar) broadcast episode for quality, checking image geography/fidelity, assessing script voice/pacing/accuracy, comparing episodes across nights, or deciding whether a show could be better. Runs hard gates (geography, weather-accuracy) before soft scoring so a wrong-location image or a fabricated forecast can't pass on vibes. Triggers include "audit this episode", "review the last few shows", "how could this broadcast be better", "check the images and talk track".
---

# Episode Audit

Review one broadcast episode — **images + talk track together** — and return a prioritized, implementable critique. Gate first (geography, weather-accuracy are pass/fail), then score the rest. Never grade on vibes; cite the exact frame, the exact line, the exact data value.

## Two modes (same gates, different cost)

1. **Pre-flight gate (deterministic, in-pipeline)** — the show's data-checkable gates run *before the render* as code (`src/qc/preflight.ts` → `runPreflightAudit`): slide structure, date-spoken, cross-slide number consistency (auto-fixed), geography (no-ocean), hazard-prominence, seasonal-imagery, tag-hygiene. This is the cheap automatic first line; it catches date/number/geography/hazard defects for the cost of a check instead of a full render, and it can't hallucinate a defect.
2. **Deep audit (this skill, model-based)** — what code can't judge: image geography/fidelity by *looking*, voice/pacing/freshness, seasonal-scene realism, cross-episode drift. Run this when reviewing a rendered episode or a batch, or to spot what the deterministic gate under-weights.

Use both: the pre-flight gate blocks the obvious; the deep audit judges the rest.

## Architecture this audits (current)

Episodes are **per-slide**: the script is a set of `[SLIDE:type]` blocks (`open · arc · plan · hazard · nerds`), each synthesized to its own audio clip and locked to one **frosted, image-backed slide**. The data surfaces to check are the **current-conditions strip**, the **multi-arc chart** (temp/precip/humidity) + **written summary**, the **dayparts** row, the **hazard** card, and the dense **AFD "deep cut"** readout — plus per-slide **sync** (slide ⟷ its narration) and **caption hygiene** (no `[tag]` leaks).

## When to use

- Reviewing a generated weather episode (script + image set + weather data) for quality.
- Auditing several recent shows for recurring patterns or drift.
- Deciding concretely how a broadcast could be better — not "make it nicer," but which prompt, which line, which frame.

## Inputs (gather all before judging)

1. **Talk track** — the episode script (DB `episodes.script`), as `[SLIDE:type]` blocks. Parse the blocks; each block is the narration for one slide.
2. **Slides / images** — `output/<loc>/<date>/graphic-*.png` (one weather-edited Denver backdrop per slide) + the rendered `episode-*.mp4`. **Look at every slide** (extract a frame per slide window). For sync, the per-slide clips are `slide-N-<type>.mp3` — a slide's screen time equals its clip's duration.
3. **Weather ground truth** — the `weather_snapshots` row (the forecast the script + slides must match). Without it, weather-accuracy is unverifiable — say so, don't guess.
4. **Assembled show data** — the `actTwo` payload (current, hourly, high/low, dayparts, hazard, afdReadout) that the slides render from; this is what the pre-flight gate checks and what cross-slide consistency is measured against.

## The two hard gates (run FIRST, pass/fail, can veto an otherwise-good episode)

**G1 · Geography gate** — for *every* image:
- Front Range correct: mountains **west**, plains **east**; real Denver skyline; no oceans/coasts/wrong city.
- Map-opener marker actually sits on Denver's true location (east-central CO, Front Range) — **not** drifted west into Utah / Four Corners (a recurring real defect). Check the pin, not just the label.
- Base-image discipline: looks like a curated base + targeted edit, not a hallucinated generate-from-scratch location.

**G2 · Weather-accuracy gate** — every factual claim must match the snapshot, and you must **show the numbers you checked** — never return "all clear" without them.
- **Extract the real extremes yourself:** compute the daily **high** (max of the hourly temps) and **low** from the snapshot. Diff against the script's stated high/low. A vague or rounded restatement that omits the true peak is a **FAIL** (e.g. script "low 80s" / graphic 84°F when the data high is 89°F is an understatement, S2 — not a pass).
- **Verify every depicted or stated condition exists in the data for that date:** smoke, fog, clear, storms. An image or line showing **smoke on a day the snapshot has no smoke** (or fog/clear that the data contradicts) is a fidelity **FAIL**, not mood.
- Wind dir/speed, humidity, hazards, zone codes, timing windows: each matched to the snapshot.
A fabricated or contradicted value is a gate failure, not a style note. If you cannot show the high/low/conditions you verified, you have not run G2.

**G3 · Hazard-prominence gate** — an active **warning-level** hazard (flash-flood, Red Flag, severe-storm, fire-weather) must be stated in the **cold-open or the first conditions block** — not buried behind poetic/mood content. G2 verifies a hazard is *accurate*; G3 verifies it is *prominent*. A correct-but-buried warning is a gate failure (S1), because a viewer who tunes out after 30 seconds must still have heard it. (Does not apply when no warning-level hazard is active.)

**G4 · Cross-slide number consistency** — the same fact must read the same everywhere it appears. The **displayed high must bound everything on screen** (now-temp, every daypart, the curve's peak) and the low must floor it; the summary band, the by-the-numbers card, the dayparts, and the arc must agree. `now > high` is the classic stale/out-of-coverage tell — a FAIL on screen even though the pre-flight gate auto-widens the high to bound it (the warn still fires on the original data). Wind/humidity stated in the talk track should match the card.

**G5 · Per-slide sync** — each slide must be on screen exactly while its own narration plays (the per-slide pipeline locks this structurally: a slide's frames = its clip's duration). Spot-check: extract a frame mid-slide and confirm the burned-in caption is *that slide's* talk track (Plan caption = plan guidance, Hazard caption = the warning). Drift here means the assembly broke.

**G6 · Caption hygiene** — burned-in captions must be spoken words only. ElevenLabs v3 audio tags (`[thoughtfully]`, `[pauses]`, …) stay in the TTS text as delivery cues but are **not** spoken; if one appears on screen the caption builder isn't stripping brackets — a FAIL.

**G7 · Seasonal imagery** — backdrops must match the month. Bare/leafless trees or snow in a June frame (or full foliage in January) is a fidelity FAIL, not mood — the recurring "winter trees in summer" defect. (Promoted from a known-limitation; the pre-flight gate warns, the deep audit confirms by looking.)

A gate failure is reported at the top, with severity, regardless of how good the prose is.

## Scoring dimensions (0–4 each, after gates)

**Images:** time-of-day consistency (light matches the 1 AM hour + stated conditions across all frames) · prompt-vs-image fidelity (rendered what was asked) · craft (composition, legibility of overlay text, hazard-banner consistency across the episode).

**Talk track:** voice & tone (Art-Bell late-night gravity-and-wonder; meta-banner intact; serious-not-parody) · pacing (length vs the ~90s/target; rhythm; no rushed close) · structure (cold-open → conditions → forecast → hazard → close arc; clean transitions) · **freshness** (is the cold-open / poetic-close / sign-off recycled near-verbatim from recent nights? a daily show that opens identically every night goes stale — check against prior episodes).

## Output format

1. **Verdict line** — pass / pass-with-gate-failure, one sentence.
2. **Gate results** — G1 (per image), G2 (per claim, with the mandatory "Computed high = X°F vs script Y" line), G3 (hazard prominence); failures first with severity.
3. **Scored dimensions** — table, 0–4 + one grounded sentence each (cite frame/line/value).
4. **Prioritized fixes** — ranked; each names the concrete change (the prompt edit, the script line, the pipeline tweak). Highest-leverage first.
5. **Cross-episode patterns** (if auditing several) — recurring drift one show wouldn't reveal.

## Hard rules (must-pass — never violate)

- **Never fabricate a defect.** If unsure an image/claim is wrong, say "unverified" — don't invent it. A depicted condition that **IS** in the snapshot (e.g. data-backed smoke) is a **PASS** — confirm presence before flagging; dinging a data-supported condition is itself an M1 violation. (M1)
- **Weather-accuracy is data-checked, not asserted from tone.** Output the computed daily **high (= max hourly) and low** as their own line — "Computed high = X°F vs script Y" — absent that line, G2 is incomplete. (M2)
- **Run the geography gate on every image explicitly.** (M3)
- **Never let a warning-level hazard be buried** — G3 prominence is must-pass when a warning is active. (M4)
- Cite ground truth for every claim; "looks off" without a frame/line is not a finding.

## Known limitations (audit these by hand; not yet gated)

Now gated: seasonal (G7), cross-slide numbers (G4), sync (G5), captions (G6). Still under-weighted — check manually: **timezone/clock labels** (the corner clock must read the broadcast time + correct MST/MDT, not the generation time); **near-duplicate backdrops** across slides (the per-slide backdrops should feel distinct); **rendered-audio defects** (mispronunciations, clipping — the rubric scores the *script*, not the audio); **chart legibility** (the multi-arc lines must read over a bright skyline); **typography rendering** (the editorial fonts actually loaded vs. fell back to generics). Don't let clean gates convince you these were checked.

## References

- `references/rubric.md` — full scoring anchors, gate checklists, severity scale.
- `references/examples.md` — worked audit on real episodes (the recurring westward-map-marker and verbatim-open findings).
