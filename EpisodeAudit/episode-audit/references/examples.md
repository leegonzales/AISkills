# Episode Audit — Worked Example

A real audit pass over Elliot Skyfall episodes 76–81 (June 2026), showing the gate-first method and what grounded findings look like.

## Single-episode audit — Episode #81 (2026-06-24)

**Verdict:** Pass with one S2 gate failure (map-marker drift).

**Gate G1 — Geography (per image):**
- `map-opener.png` — US night-lights map, Denver labeled "69°F AREAS OF SMOKE," hazard banner across top. **FAIL (S2):** the starburst/box sits over eastern Utah / Four Corners, ~1–2 states west of Denver's true Front Range position. Label says Denver; pin doesn't. Smoke plumes present (good, matches theme).
- `graphic-01.png` — real Denver skyline, Front Range to the **west** (correct), smoky orange sky matching "areas of smoke," South Platte in foreground. **PASS.** Clean base-edit.
- (remaining graphics: check each the same way.)

**Gate G2 — Weather accuracy:** 69°F / ESE 5mph / 63% humidity / areas of smoke; Red Flag Wed 11AM–6PM, Fire Weather Watch, flash-flood Wed–Thu. Cross-check each against `weather_snapshots` — **PASS** if matched; flag any value that isn't in the snapshot.

**Scored (0–4):** voice 4 (the "stars aren't available for comment" register is strong) · structure 4 · pacing 3 (141s vs ~90s target — long) · freshness **1** (cold-open near-verbatim with ep78/ep80; the "smoke started as fire… weather doesn't recognize borders" close is the same template as every recent night).

**Top fixes (prioritized):**
1. **S2 — Fix the map-opener marker.** The opener prompt/pipeline places Denver too far west. Pin to Denver's real coordinates (≈39.74°N, 104.99°W) or correct the geo-reference in the map prompt. Recurs across nights → pipeline-level fix, not a one-off.
2. **S2 — Refresh the cold-open + poetic close.** Vary the "Wherever you are right now…" open and the "this weather traveled a thousand miles" close; they're near-identical across ep76/78/79/80/81. Rotate motifs or seed from the night's distinct weather.
3. **S3 — Pacing.** 141s vs ~90s target; tighten the hazard section.

## Cross-episode patterns (ep76–81)

- **Verbatim cold-open (S2):** "Good evening, Denver… voice of the skies… Wherever you are right now —" is near-identical in ep78/80/81 (variants in 76/79). Daily-show staleness.
- **Single poetic-close template (S2):** 5/5 episodes end with weather "traveling to arrive here" (ocean/Gulf/fire) + "weather doesn't recognize borders/state lines." Strong device, overused.
- **Recurring map-marker drift (S2):** westward marker confirmed in ep80 and ep81 — a pipeline defect, not chance.
- **Near-duplicate broadcasts (S1 process):** ep78 and ep79 (same night, 5 min apart, from the launchd double-fire) share near-identical weather and content — two shows where one was intended.
- **Image overwrite:** date-scoped filenames (`graphic-NN.png`) mean same-night reruns overwrite the earlier episode's images — ep78's images were replaced by ep79's.

## What a BAD audit looks like (avoid)

- "The images look great and the script is atmospheric and engaging." — no frame cited, no gate run, no fix. Ungrounded.
- "The map seems a bit off." — vague; doesn't say marker-is-in-Utah or name the fix.
- Inventing a defect ("the skyline looks like Chicago") without looking — violates M1.
- Praising weather accuracy without opening the snapshot — violates M2.
