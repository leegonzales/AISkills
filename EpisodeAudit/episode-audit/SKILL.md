---
name: episode-audit
description: Audit a generated weather-broadcast episode — its images and its talk track — against a grounded rubric, and return prioritized, implementable fixes. Use when reviewing an Elliot Skyfall (or similar) broadcast episode for quality, checking image geography/fidelity, assessing script voice/pacing/accuracy, comparing episodes across nights, or deciding whether a show could be better. Runs hard gates (geography, weather-accuracy) before soft scoring so a wrong-location image or a fabricated forecast can't pass on vibes. Triggers include "audit this episode", "review the last few shows", "how could this broadcast be better", "check the images and talk track".
---

# Episode Audit

Review one broadcast episode — **images + talk track together** — and return a prioritized, implementable critique. Gate first (geography, weather-accuracy are pass/fail), then score the rest. Never grade on vibes; cite the exact frame, the exact line, the exact data value.

## When to use

- Reviewing a generated weather episode (script + image set + weather data) for quality.
- Auditing several recent shows for recurring patterns or drift.
- Deciding concretely how a broadcast could be better — not "make it nicer," but which prompt, which line, which frame.

## Inputs (gather all three before judging)

1. **Talk track** — the episode script (DB `episodes.script` or `eval/epNN-script.txt`).
2. **Images** — `output/<loc>/<date>/graphic-*.png` + `map-opener.png`. **Look at every image.**
3. **Weather ground truth** — the `weather_snapshots` row for the episode (the forecast the script must match). Without it, weather-accuracy is unverifiable — say so, don't guess.

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

## Known limitations (audit these by hand; not yet gated — next forge campaign)

The gate-first design is strongest on geography and weather-numbers. It under-weights, so check manually: **seasonal-scene mismatch** (autumn foliage / snow in a June frame — fidelity-vs-cue passes it); **timezone/clock labels** (MST vs MDT for the episode date); **intra-episode near-duplicate frames**; **rendered-audio defects** (mispronunciations, clipping, script-audio desync — the rubric scores the *script*, not the audio); **overlay/hazard-banner legibility** beyond S3. Don't let a clean G1/G2/G3 convince you these were checked.

## References

- `references/rubric.md` — full scoring anchors, gate checklists, severity scale.
- `references/examples.md` — worked audit on real episodes (the recurring westward-map-marker and verbatim-open findings).
