# Changelog

All notable changes to the Episode Audit skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2026-06-28

### Added
- **Two-mode model:** a deterministic **pre-flight gate** (`src/qc/preflight.ts`, in-pipeline, pre-render, auto-fixes number consistency) as the cheap automatic first line, plus the **deep audit** (this skill, model-based) for what code can't judge.
- **Four gates promoted/added:** G4 cross-slide number consistency (displayed high bounds now + dayparts; `now > high` warn on stale data), G5 per-slide sync (slide frames = its clip duration; caption must match its slide), G6 caption hygiene (no `[tag]` leaks), G7 seasonal imagery (winter trees in June = FAIL — promoted from known-limitation).

### Changed
- **Architecture re-point:** audits the per-slide `[SLIDE:type]` blocks (open · arc · plan · hazard · nerds) and the frosted, image-backed slide deck — current strip, multi-arc chart + summary, dayparts, hazard card, dense AFD "deep cut". Inputs now include the assembled `actTwo` payload.
- Known-limitations trimmed to what is still ungated (clock labels, near-duplicate backdrops, audio defects, chart legibility, font-render fallback).

## [0.3.0] - 2026-06-25

### Added
- **G3 hazard-prominence gate + must-pass M4** (forge Round 3, from the adversarial round). An active warning-level hazard (flash-flood, Red Flag, severe, fire-weather) must appear in the cold-open or first conditions block; a correct-but-buried warning is now an S1 gate failure (the structure-arc reward no longer excuses burying a warning behind poetry). Closes the highest-value adversarial finding — independently corroborated by the baseline audit of ep80 ("buries the day's biggest story").
- **M1 tightening:** a depicted condition that IS in the snapshot (e.g. data-backed smoke) is an explicit PASS; flagging it is itself an M1 violation.
- **M2 tightening:** the computed daily high (= max hourly) and low must be shown as their own output line.
- **Known-limitations section:** seasonal-scene mismatch, timezone/clock labels (MST/MDT), intra-episode duplicate frames, rendered-audio defects, and banner legibility are documented as hand-check items not yet gated (next campaign), so a clean G1/G2/G3 doesn't read as "everything checked."

## [0.2.0] - 2026-06-25

### Changed
- **Hardened G2 weather-accuracy gate** (forge Round 2). The gate now requires extracting the numeric daily high (= max of hourly temps) and low and diffing them against the script's stated values — a vague/rounded restatement that hides the true peak (e.g. "low 80s" vs a data high of 89°F) is now an explicit FAIL. Added: every depicted/stated condition (smoke, fog, clear) must be verified to exist in the data for that date — smoke imagery on a no-smoke day is a fidelity FAIL. The audit must show the numbers it checked; "all clear" without them does not count as running G2. Fixes a must-pass M2 false-clear observed in the baseline eval (ep78).

## [0.1.0] - 2026-06-25

### Added
- Initial draft forged via `skill-forge` against a frozen eval set (Elliot Skyfall ep 76/78/79/80/81).
- Gate-first design: G1 geography (Front Range orientation, no oceans, map-marker placement) and G2 weather-accuracy (claims vs `weather_snapshots`), both pass/fail, run before scoring.
- Scoring dimensions (0–4): image time-of-day / fidelity / craft; talk-track voice / pacing / structure / freshness.
- Must-pass discipline: M1 no fabricated defects, M2 weather data-checked, M3 geography gate on every image.
- `references/rubric.md` (anchors + severity), `references/examples.md` (worked audit on real episodes).
