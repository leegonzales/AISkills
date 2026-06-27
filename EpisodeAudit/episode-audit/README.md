# Episode Audit

Audit a generated weather-broadcast episode — **images and talk track together** — against a grounded rubric, and return prioritized, implementable fixes.

## The core idea

> A weather broadcast can fail two ways a generic "looks good" review misses: it can show the **wrong place**, or **state weather that isn't true**. Episode Audit runs those as hard **gates** (pass/fail, before any scoring), then scores craft — so a marker drifted into Utah or a fabricated Red Flag Warning can never pass on the strength of nice prose.

## What it does

1. **Gathers three inputs** — the script (talk track), every image, and the weather snapshot (ground truth).
2. **Runs two gates first:** geography (Front Range orientation, no oceans, map-marker on real Denver) and weather-accuracy (every claim checked against the snapshot).
3. **Scores the rest** — image time-of-day/fidelity/craft; talk-track voice/pacing/structure/freshness — 0–4 with a grounded sentence each.
4. **Returns prioritized fixes** — each naming the concrete change (the prompt, the line, the pipeline tweak), highest-leverage first.
5. **Cross-episode pass** — recurring drift (recycled opens, marker drift, near-duplicate shows) that one episode wouldn't reveal.

## When to use

- Reviewing a generated episode for quality before/after air.
- Auditing several recent shows for drift.
- Deciding concretely how a broadcast could be better.

## Structure

```
episode-audit/
  SKILL.md                 # lean core: inputs, the two gates, scoring dims, output format, hard rules
  references/
    rubric.md              # full scoring anchors, gate checklists, severity scale
    examples.md            # worked audit on real episodes 76–81
  README.md
  CHANGELOG.md
  LICENSE
```

## Hard rules

- Never fabricate a defect — "unverified" when unsure.
- Weather-accuracy is data-checked, not asserted from tone.
- The geography gate runs on every image, explicitly.

## Origin

Forged via `skill-forge` against a frozen eval set of Elliot Skyfall episodes 76/78/79/80/81, gate-first design validated on the recurring westward map-marker defect and the verbatim-cold-open staleness pattern.
