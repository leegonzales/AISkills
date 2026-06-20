# Verified-on-State: Analogy Pressure Test — Research Notes

**Date:** 2026-05-06
**Thread:** Test three candidate analogies from yesterday's reinvestment dream against realistic contested-call pressure scenarios. Goal: identify which analogy (if any) survives reinvestment-style decomposition under stress.

---

## The three candidates

From 2026-05-05 dream-journal:

1. **"Read the swell before consulting the chart."** — verify ground-truth state before claiming based on memory.
2. **"The chart goes ashore before the voyage."** — once internalized, the checklist isn't carried into the performance.
3. **"The fleet is the critical audience."** — verification is external, not self-claimed. (Lord Stage 3 + Masters audience-pressure literature.)

---

## What "survives a contested call" means operationally

A contested-call scenario in Pike's domain is one where:
- An apprentice has made a verification claim
- A senior agent (or Lee) pushes back
- Working memory is now under pressure (defend the claim, re-check the work, manage the social dynamic)
- The analogy either *holds* (cues the right action without needing decomposition) or *decomposes* (the apprentice consults its rules and reinvests)

Masters' criterion: an analogy holds if it doesn't decompose into propositions the apprentice can consult under pressure. If you can ask "what does the analogy literally mean step-by-step" and get a checklist back, it has decomposed and lost its protective function.

---

## Three contested-call scenarios

### Scenario A: The stale fact

Apprentice reviewer claims a skill's external API reference is current. Walsh pushes back: *"Are you sure? I think that endpoint deprecated in February."* The apprentice's mental record says they checked it during review. Three minutes ago. Working memory now competing between (i) defend the claim, (ii) re-verify against current state, (iii) explain methodology to Walsh.

**Test each analogy:**

- **"Read the swell before consulting the chart."** Holds. The image cues exactly the right action: stop defending the chart-record (memory), go feel the actual swell (current state). The metaphor doesn't need decomposition — the apprentice doesn't translate it into "Step 1: open the docs URL. Step 2: ..." — they just go check. Reinvestment-resistant because the image *is* the action.

- **"The chart goes ashore before the voyage."** Wobbles. The analogy is about training-time scaffolding being left behind, not about how to handle a contested verification claim mid-performance. Wrong domain. The apprentice would have to ask "what does this mean here?" and that's already reinvestment.

- **"The fleet is the critical audience."** Holds, but indirectly. Cues the apprentice to recognize that Walsh's challenge IS the verification mechanism — not an obstacle to defend against. Reframes the social pressure into the verification loop itself. Strong, but more abstract than #1.

**Verdict:** #1 wins this scenario. #3 is a close second with different work.

### Scenario B: The fast claim

Apprentice asked at speed: *"Is this skill compliant with the new TEMPLATE_UPDATE v6?"* They have a half-formed sense from glancing at the skill yesterday. The temptation is to claim from memory because the questioner is waiting and looks impatient.

**Test each analogy:**

- **"Read the swell before consulting the chart."** Holds. The image distinguishes "the chart says X" (memory-based) from "the swell says Y" (current state). Apprentice recognizes "I'm about to consult the chart, not the swell" — pause, go verify. The metaphor protects against speed-pressure without requiring rule-recall.

- **"The chart goes ashore before the voyage."** Doesn't engage. This scenario isn't about leaving training scaffolding behind; it's about the temptation to claim from memory under time pressure. Wrong analogy, no purchase.

- **"The fleet is the critical audience."** Engages but weakly. Reminds the apprentice that the claim will be tested by others, but doesn't directly counter the speed pressure. The apprentice could still rationalize: "I'll claim now and accept correction later if wrong." That's bad behavior the analogy doesn't prevent.

**Verdict:** #1 wins again. The fast-claim scenario is exactly what verified-on-state discipline is supposed to prevent, and #1 is the analogy that fires in that exact moment.

### Scenario C: The cross-station claim

Apprentice on Pike-station claims something about how Walsh-station handles training-build dispatch. Walsh contests: *"That's not actually how we do it — where did you get that?"* The apprentice's source was a journal entry from three weeks ago, which may or may not still be current.

**Test each analogy:**

- **"Read the swell before consulting the chart."** Holds, but with translation. The "chart" here is the cross-station memory; the "swell" is the current state of Walsh-station. Apprentice should go verify directly against Walsh-station now, not defend the memory. Works but requires more interpretive work than scenarios A/B.

- **"The chart goes ashore before the voyage."** Wrong domain again.

- **"The fleet is the critical audience."** Holds powerfully here. The audience IS Walsh — the cross-station expert who knows the ground truth. Apprentice's job is to defer to the critical audience, not defend the inherited claim. Cleaner than #1 in this specific case because the audience-as-verifier reframe matches the cross-station structure.

**Verdict:** #3 edges #1 here. Cross-station claims are exactly where audience-as-verifier shines.

---

## What I learned from the test

**#1 ("Read the swell before consulting the chart") wins two of three scenarios cleanly and survives the third.** It's the strongest candidate. Specific enough to be operational, abstract enough to generalize, and it fires in the exact moment of temptation (memory-claim vs. ground-truth-claim).

**#3 ("The fleet is the critical audience") wins one scenario decisively (cross-station claims) and supports the others.** Worth keeping as a *complementary* analogy, not a replacement. Different work: #1 governs the verification action, #3 governs the verification structure.

**#2 ("The chart goes ashore before the voyage") fails the pressure test.** Beautiful as a meta-statement about training-time scaffolding, but it doesn't fire in any of the three contested-call scenarios. Wrong analogy for this work. Reassign it to its actual domain (skill-design / SKILL.md philosophy), not verified-on-state.

---

## A fourth analogy emerged

Running the scenarios surfaced something I didn't see yesterday: the strongest verified-on-state moments are the ones where the apprentice notices the difference between *what they remember* and *what is currently true*. The action is always the same: stop, go look, return with current state.

A candidate fourth analogy compressed from that observation:

**"Doubt the chart, trust the swell."**

Or alternately: **"Memory is a chart. Verify against the swell."**

This is more concentrated than #1 — it names the failure mode (over-trusting memory) and the corrective (re-engaging with current state) in a single image. It also generalizes outside ocean-metaphor: the same image-pair (recorded knowledge vs. current state) maps to scientific replication, journalism fact-checking, debugging, code review.

Worth comparing head-to-head with #1 in a future cycle, but my first read is that #1 ("Read the swell before consulting the chart") is more *operationally directive* (do this thing, in this order), while #4 ("Doubt the chart, trust the swell") is more *epistemically directive* (this is the relative trust calibration). They might both belong in v0 — one as the action-cue, one as the stance-cue.

---

## Implications for the v0 verified-on-state shape

The v0 should lead with **#1 as the operational analogy** (action-shaped, scenario-tested, holds under pressure). Add #3 as the **structural analogy** for cross-station and audience-tested cases. Possibly add #4 as the **stance analogy** that compresses the why. Three analogies, each governing a different layer (action / structure / epistemics), is still chunked enough to internalize and is more useful than one over-stretched analogy.

The checklist still gets written, but its function is derivation. The analogies are what get carried into the chair. The checklist proves the analogies are sound; the analogies are what survive when working memory is full.

---

## What I want to remember

1. **#1 is the strongest single analogy.** "Read the swell before consulting the chart" survives all three pressure scenarios. Lead with it.
2. **#2 fails the test.** Reassign to its actual domain (skill-design philosophy), not verified-on-state.
3. **#3 has a specific niche** (cross-station / audience-tested verification). Keep it for that.
4. **#4 emerged from the test:** "Doubt the chart, trust the swell." Worth a future head-to-head with #1.
5. **The pressure test itself is reusable.** Three-scenario contested-call test is a method I can run on any future analogy candidate. Worth naming as a Pike-domain practice.
