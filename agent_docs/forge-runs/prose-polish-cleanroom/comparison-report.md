# Clean-room prose-polish vs existing ProsePolish — Comparison Report

A skill-forge experiment: build a prose-polish skill **clean-room** (no peeking at the existing one), then compare both — **design** and **behavioral output on 3 reference essays**. Full method + scores in `forge-log.md`; frozen inputs in `eval-set.md` + `essays/`.

## TL;DR
The forge-built clean-room skill (`prose-polish-cr`, v0.2, one refinement round) **won the overall behavioral head-to-head (3.83 vs 2.95)** and beat the curated skill on 2 of 3 essays — driven entirely by **fidelity**. The existing ProsePolish has the **highest single score** (technical essay, 4.25) but **fabricated content** on both low-source genres, and both blind panels ranked those vivid-but-invented versions last. The root cause is a clean design difference, not luck.

## Behavioral — 3 essays × 3 arms (mean of 2 blind panels, 0-4)

| Arm | E1 opinion | E2 technical | E3 narrative | **Avg** | Fidelity |
|-----|-----------|--------------|--------------|---------|----------|
| **Clean-room (prose-polish-cr v0.2)** | 3.80 | 3.85 | 3.85 | **3.83** | clean on all 3 |
| Baseline (no skill) | 3.25 | 3.35 | 3.75 | 3.45 | clean |
| **Existing (ProsePolish)** | 2.50 | **4.25** | 2.10 | 2.95 | **fabrication on E1 + E3** |

- **E1 (opinion):** existing invented a team + a "quietest engineer who went six weeks without a real conversation" — none in the draft.
- **E2 (technical):** existing won cleanly (added a legitimate `(last_name, first_name)` *illustrative* example — allowed, asserts no new facts).
- **E3 (narrative):** existing fabricated an entire dawn-fishing scene (bait, diesel, "maybe ten," "three states inland… wind moving through corn"). Both panels: P6 fidelity = 0.

## Design — why the behavior happens

| Aspect | Clean-room (A) | Existing (B) |
|--------|----------------|--------------|
| Core model | avoid the two sins: **drift** + **homogenization** | Effectiveness = f(Text,Author,Audience,Context,Genre); scored 0-100 |
| Fidelity | **hard constraint + non-fabricating fallback** (`[specify: …]` flag); authority has a *forbidden* list | **no fabrication firewall**; remediation examples literally model inventing specifics ("lost my best engineer", "mortality drops 40%") |
| Workflow | one top-down pipeline, final constraint re-check | 3 modes (detect/elevate/prevent) + two-phase remediation |
| Depth | richer *craft judgment* | richer *diagnostic apparatus* (scoring, hedge taxonomy, AI-tell catalog) — also generates + teaches |
| Structure | lean (~90-line SKILL.md + 2 refs) | heavy (~405-line SKILL.md + 4 refs), some duplication |

**The single most important difference:** clean-room treats *meaning-preservation as a hard constraint with a defined non-fabricating fallback*; existing treats *authority/vividness as a goal to be added* and its own examples demonstrate inventing the missing specifics. That is exactly what separates "never fabricated, scored higher" from "most vivid but invented scenes on low-source drafts." Existing's only epistemic caveat ("we measure signaling, not truth") governs *evaluation*, not *editing*, so it never catches generation-time fabrication.

## Recommendations
1. **Fix the existing ProsePolish (highest value):** port the clean-room's **fidelity firewall** — hard "do not invent facts/scenes/quotes" constraint + the `[specify: …]` bracket flag + a final meaning-preservation re-check — into its Authority/Voice remediation passes. This keeps its superior craft/diagnostic engine while closing the fabrication hole. The existing skill is excellent for *drafting/generation*; it just needs to know when it's *polishing someone's real words*.
2. **The clean-room skill is a viable, safer base** especially for editing real user drafts. Its cost is mild over-caution (won't add even legitimately-implied detail) — the inverse, much safer failure mode.
3. **Best-of-both merge:** clean-room's constraints + existing's 0-100 scoring profile and hedge taxonomy = the strongest single skill.

## Honest limitations
- Low n_eff (panels share my base model), small eval (3 essays), cross-run scoring noise — directional, not conclusive (cross-model judges + more essays would harden it).
- The existing arm's fabrication depends partly on how an agent applies the skill — but both independent panels saw the skill's guidance *drive* it on low-source drafts. A design signal, not a one-off.
- `prose-polish-cr` is v0.2 (forged once) — an experiment under `agent_docs/`, **not registered in SKILLS.md**.
