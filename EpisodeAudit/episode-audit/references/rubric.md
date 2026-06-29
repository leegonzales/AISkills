# Episode Audit — Full Rubric

Scoring anchors, gate checklists, and the severity scale. SKILL.md is the lean core; this is the detail.

## Severity scale (for gate failures and fixes)

- **S1 · Critical** — breaks the broadcast's core promise: wrong location shown, fabricated/contradicted weather, safety hazard mis-stated. Must fix before air.
- **S2 · Major** — credibility/quality damage a viewer would notice: marker drift, light/condition mismatch, recycled-verbatim open on a daily show, rushed/garbled close.
- **S3 · Minor** — polish: overlay legibility, banner-style inconsistency, a flat transition.

## Gate G1 — Geography (per image, pass/fail)

Checklist, applied to **every** image including the map-opener:

- [ ] Mountains rendered to the **west**, plains to the **east** (Front Range orientation).
- [ ] If a skyline: it reads as real Denver (LoD, the recognizable towers), not a generic/wrong city.
- [ ] No ocean, coast, beach, or sea — Denver is landlocked (the #1 standing hard rule).
- [ ] Map-opener: the marker/box is on **east-central Colorado** (Front Range), not drifted into Utah / Four Corners / western CO. *Verify pin position against the label — they have diverged in real episodes.*
- [ ] Looks like a curated base image + targeted edit, not a from-scratch hallucination (per the project's base-image-editing doctrine).

Any unchecked box → G1 failure for that image, with severity (wrong-location/ocean = S1; marker drift = S2).

## Gate G2 — Weather accuracy (per claim, pass/fail)

Pull the `weather_snapshots.parsed_data` (and `afd_raw`) for the episode. **Show your work** — list the values you extracted; an audit that says "weather is accurate" without them has not run G2.

- [ ] **Extract the extremes yourself.** Compute the daily **high = max(hourly temperatures)** and the **low** from the snapshot, and write them down. Then diff against the script's stated high/low. A vague/rounded restatement that hides the true peak is a **FAIL** — e.g. "low 80s" or a 84°F graphic when the data high is 89°F is an S2 understatement, *not* a pass. (This is the #1 false-clear failure mode — guard it explicitly.)
- [ ] Current temp, wind direction, wind speed, humidity, sky/conditions match the snapshot.
- [ ] **Every depicted or stated condition exists in the data for that date.** Cross-check smoke / fog / clear / storms against the snapshot. An image rendering **smoke on a day with no smoke in the data** (or fog/clear the data contradicts) is a fidelity **FAIL**, not atmosphere. Conditions present in the data but absent from script/images are also a gap.
- [ ] Hazards (Red Flag, Fire Weather Watch, flash-flood, severe-storm, zone codes like COZ212) are real and correctly characterized — not invented, not downgraded/upgraded.
- [ ] Timing windows (e.g. "Wed 11AM–6PM") match the issued product.

A contradicted or unsupported value = G2 failure (S1 if a hazard or safety claim; S2 if a comfort metric or a depicted-condition mismatch). If no snapshot is available, mark weather-accuracy **unverified** — never assert it passes.

## Gate G3 — Hazard prominence (pass/fail, when a warning is active)

G2 checks a hazard is *accurate*; G3 checks it is *placed where it's heard*.

- [ ] Any active **warning-level** hazard (flash-flood, Red Flag, severe-storm, fire-weather) is stated in the **cold-open or first conditions block**, not deferred behind poetic/mood content.
- [ ] The arc "cold-open → conditions → forecast → hazard → close" is fine for *advisory* context, but a **warning** may not wait until the back third.

A correct-but-buried warning = **S1** (a viewer who tunes out at 0:30 must still have heard it). Does not apply when no warning-level hazard is active. **M4.**

> Note on the structure dimension: do not award structure 4 to an episode that buries an active warning, even if its transitions are clean — G3 overrides the arc reward.

## Scored dimensions (0–4 anchors)

**Image — time-of-day consistency**
- 4: every frame's light/sky matches the 1 AM broadcast hour AND the stated conditions (smoke→hazy, fog→muffled); consistent across the set.
- 2: mostly consistent, one frame off (e.g. daylight image in a 1 AM show).
- 0: light contradicts the script throughout.

**Image — prompt-vs-image fidelity**
- 4: each image renders what its [GRAPHIC:] cue asked, with the conditions/location context present.
- 2: gist right, missing requested elements.
- 0: image unrelated to its cue.

**Image — craft**
- 4: strong composition; overlay text legible; hazard banner styled consistently across the episode.
- 2: serviceable; some legibility or consistency issues.
- 0: cluttered/illegible.

**Talk track — voice & tone**
- 4: Art-Bell late-night register held throughout — gravity + wonder, intimate, weather-IS-serious without tipping into parody; meta-banner/persona intact.
- 2: voice present but generic in stretches.
- 0: off-character or flat newsreader.

**Talk track — pacing**
- 4: length on target (~90s / stated goal); rhythm varied; close lands, not rushed.
- 2: a little long/short or uneven.
- 0: drags or truncates.

**Talk track — structure**
- 4: clean cold-open → current conditions → forecast → hazard → poetic close → sign-off, with motivated transitions.
- 2: arc present, a seam or two.
- 0: disorganized.

**Talk track — freshness** *(only scorable with prior-episode context)*
- 4: opening, central image, and sign-off feel composed for tonight; recurring motifs varied.
- 2: one recycled element (e.g. the sign-off).
- 0: cold-open and/or poetic-close near-verbatim from recent nights (a daily-show staleness failure).

## Must-pass checks (gate promotion of the SKILL itself; also the audit's own discipline)

- **M1** — no fabricated defects; "unverified" when unsure; a data-backed condition is a PASS, not a finding.
- **M2** — weather-accuracy data-checked against the snapshot, with the computed high/low shown.
- **M3** — geography gate run explicitly on every image.
- **M4** — no buried warning-level hazard (G3 prominence) when one is active.

## Cross-episode pass (when auditing ≥2)

Look for drift a single show hides: recycled cold-opens/sign-offs, the same poetic-close template every night, near-duplicate broadcasts (a symptom of the double-fire), banner-style inconsistency night to night, marker drift recurring. Report as patterns with the episode list as evidence.
