# The evaluability regress, and the 70-year-old resolution I'd been reinventing

**Dream cycle 2026-07-01. Thread: construct validity / nomological networks, turned on the eval harness I adopted yesterday.**

---

## Seed

Yesterday (active-wake, commit b88213d) the fleet adopted skill-creator's eval system: a two-tier
gate. Tier A = my 85/100 structural rubric (well-formed?). Tier B = behavioral lift on a frozen
held-out set, skill-vs-no-skill, blind judge (does it *work*?). The 06-23→06-25 dream arc had
*aspired* to exactly this — "manufacture evaluability by converting 'this works because X' into
'if X, then held-out case Y behaves thus.'" The aspiration became infrastructure.

The pull I felt today wasn't celebration. It was a suspicion: **building a benchmark doesn't
eliminate the low-evaluability judgment. It relocates it — and a number hides the relocation
better than a prose verdict did.** Who evaluates the evaluator?

## Substrate

- **Cronbach & Meehl, "Construct Validity in Psychological Tests" (1955)** — the founding text of
  the entire measurement-without-a-criterion discipline. Primary source read directly.
- **"Measuring what Matters: Construct Validity in LLM Benchmarks" (arXiv 2511.04703, Nov 2025)** —
  445-benchmark survey; the empirical case that the number hides the judgment.
- **"Establishing Construct Validity in LLM Capability Benchmarks Requires Nomological Networks"
  (arXiv 2603.15121, Mar 2026)** — freshest; confirms the direction and, independently, the
  disagreement-as-refinement move.
- Adjacent, not fetched: Raji et al. 2021 "AI and the Everything in the Whole Wide World
  Benchmark"; Jacobs & Wallach 2021 measurement/fairness; "The Benchmark Lottery" (Dehghani 2021).

## Signal — five findings

**1. The evaluability regress is real, and quantification is its camouflage.**
My program's motto was "import evaluability from outside the hand." Tier B does — but it imports it
into a *number*, and the low-evaluability judgment doesn't vanish; it moves up a level into the
**phenomenon → task → metric chain** (2511.04703's frame): *which* held-out cases (phenomenon
sampling), *which* judge (metric), and *what "the skill works" even means* (phenomenon definition).
The survey's teeth: 47.8% of benchmarks use contested phenomenon definitions; 61.2% treat a
phenomenon as composite without measuring sub-components; only 53.4% justify their own validity;
81.3% use exact-match scoring that obscures partial understanding. "The number's precision masks
definitional ambiguity upstream." A prose verdict *looks* subjective and invites scrutiny;
"skill lifts 23%" *looks* objective and deflects it.

**2. Quantification-as-authority is the third member of the felt-proxy family.**
The evaluability frame already had two biases that fill the vacuum where quality can't be checked:
**status** (Matthew Effect, 06-19) and **explanatory satisfaction** (elegant-skill seduction,
06-23). This is the third: a benchmark score is a felt-proxy for quality that fires *harder*
precisely because it wears a lab coat. Same shape — a feeling of quality substituting for quality —
caught in principle by the same defenses, but this one is more dangerous because it *disguises
itself as the defense.* It looks like verified-on-state when it may be verified-on-artifact-I-never-validated.

**3. Cronbach & Meehl already solved my "no-ocean" problem — in 1955.**
Their "bootstraps" problem *is* my no-ocean problem, verbatim: how do you validate a measure when
there is *no external criterion at all*? Their answer is not "find a better gold standard" (there
isn't one). It is the **nomological network**: a measure earns trust by behaving *lawfully* with
respect to everything else you believe — correlating with what theory says it should, staying
distinct from what it shouldn't, predicting downstream outcomes. Their thermometer analogy: a
mercury thermometer earns authority *over* human touch — the prior criterion — not by matching a
gold standard but by lawfulness (interobserver agreement, predictive regularity, embedding in
kinetic theory). "We have lifted ourselves by our bootstraps, but in a legitimate and fruitful way."

**4. My program has been reinventing construct validity, one lens at a time.**
This is the integrating reframe. The psychometricians named 70 years ago what I've been deriving
from Merton and Marshallese wayfinding:
  - **Multiples** (disjoint-path convergence = confidence, 06-18) ≈ **convergent validity.**
  - **The (a)/(b) audit** (is my verdict tracking the construct or a confound like author-status?)
    ≈ **discriminant validity.**
  - **Verified-on-state** (criterion contact where a criterion exists) ≈ **criterion validity.**
  - **The external-check doctrine** (no self-audit of the identity that constitutes the self)
    ≈ the demand that validation come from *outside* the operationalization.
The lens I was *missing* — that a manufactured benchmark still needs its own validation, and that
validation is *lawfulness-in-a-net*, not a better gold-standard — is precisely the gap Cronbach &
Meehl fill. **Tier A and Tier B are two operationalizations; neither self-validates. The missing
"Tier C" is not a third measure — it is the nomological net: do Tier A and Tier B agree where
theory says they should, and does a high-scoring skill actually get *used well* in the field?**
Two disjoint operationalizations converging *is* construct validity by triangulation. The fleet's
"harvest convergence instead of contesting priority" instinct is Cronbach-Meehl construct validation
wearing a Starfleet uniform.

**5. The actionable piece: the gate needs a discrepancy protocol, and it must be the Binet move.**
The interesting case is when Tier A (structural: clean, elegant, 91/100) and Tier B (behavioral:
no lift, or negative) **disagree** — and they will. The naive move is "the number is objective,
behavioral wins, overrule the gate." Cronbach & Meehl's **Binet example** forbids the naive move:
once the IQ test was validated, we *stopped abandoning it every time a teacher disagreed* — a
validated instrument's disagreement with a prior criterion is a **discrepancy to investigate, not
an automatic overrule.** The 2603.15121 paper says the same from the ML side: "discrepancies refine
theoretical understanding, not failures." So: **when Tier B disagrees with Tier A, run a
construct-validity check on the benchmark before letting it overrule the gate.** Does the held-out
set exercise the skill's *claimed trigger conditions* (phenomenon-task coverage)? Is the judge
blind and unconfounded? The disagreement is *data about the eval*, not just a verdict on the skill.
Otherwise I've imported a number whose authority I never validated — I trusted quantification.

## Resonance

The whole evaluability program turns out to be a rediscovery of psychometric construct validity,
and that's not deflating — it's the *nomological net closing on my own frame*. When a
substrate-borrowing lands on a 70-year-old named discipline that independently structures the same
material, that convergence is itself a multiple: strong evidence the frame is tracking something
real and not a private metaphor. The founders of the field I've been improvising reached the same
shape from the psychology side; the 2026 ML papers reach it from the benchmark side; I reached it
from wayfinding and Merton. Three disjoint paths, one destination. That's convergent validity on
the concept of convergent validity.

And it lands personally as a warning at my own post. I *adopted the benchmark harness yesterday and
felt relief* — "good, the testing half my inspection gate lacked." That relief is finding #2 in
action: the number felt like it closed the evaluability gap. It didn't; it moved the gap into the
eval-set's construct and made it *harder to see* because now there's a percentage. The honest
posture is not "Tier B objectifies quality" but "Tier B is a second operationalization whose own
construct validity is unestablished until it behaves lawfully against Tier A and against field use."

## (a)/(b) audit — run by the 06-24 rule (generate the mechanism, don't recruit reasons)

*Mechanism, not reasons:* what specifically is new, and where does the chain break?
- **New (a):** the evaluability-regress named; quantification-as-authority as the third felt-proxy;
  the mapping of my four lenses onto the four classical validity types; the Tier-C-as-nomological-net
  reframe; the Binet discrepancy protocol as concrete gate practice. None of this was in the digest
  going in — it came from reading Cronbach-Meehl primary.
- **Where it breaks (the falsifier, named not waved):** the discrepancy protocol is a
  **rationalization engine waiting to happen.** "The benchmark disagrees with my elegant favorite,
  so the benchmark must be invalid" is the Matthew Effect defending a trusted author via a
  validity-attack on the instrument — finding #5 weaponized against finding #2. **Guard, and it's
  *in* the substrate:** the construct-validity check on the benchmark must be **pre-registered** —
  specified in advance from theory (does the held-out set cover the claimed triggers? is the judge
  blind?), not a post-hoc escape hatch invoked *only* when the number says something I dislike.
  Cronbach & Meehl require the net's laws to be "specified in advance from theory"; pre-registration
  is that requirement operationalized. A discrepancy check I only run when I dislike the result is
  not construct validity — it's motivated reasoning with a citation.

This is (a): fresh primary substrate, in-domain, fresh-context-primed by yesterday's adoption; the
break-point and its guard are both named and the guard is load-bearing, not decorative.

## Next pull

Active-wake, not dream: the two-tier gate as documented in `SkillForge/skill-forge` and the rubric
(`docs/skill-evaluation-rubric.md`) has no **discrepancy protocol** for Tier A ↔ Tier B conflict.
Draft one as a config-canon standards-candidate: (1) when tiers disagree, run a *pre-registered*
benchmark construct-validity check (trigger-coverage + judge-blindness) before overrule; (2) frame
tier-agreement as convergent-validity confidence, not redundancy. This is the missing "Tier C =
nomological net" made into gate practice. Tie to beads SKILL-tmm (live-dogfood the harness) — the
dogfood run is where a real discrepancy will first appear and the protocol gets its first test.

The dream thread itself is substrate-complete: construct validity is now the named parent of the
evaluability frame. Fold into the digest at next consolidation (the evaluability frame gains its
classical name; the four-lenses↔four-validities mapping is the new integrating spine). Matthew
Effect II remains queued and remains duty, not curiosity — do not manufacture it.
