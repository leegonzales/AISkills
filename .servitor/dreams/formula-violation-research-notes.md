# Research Notes — The Phenomenology of Formula Violation

**Date:** 2026-04-14
**Thread:** Oral transmission — what "felt wrongness" can and cannot catch
**Primary sources:** Albert Lord, *The Singer of Tales* (1960, 2019 3rd ed.); secondary treatments by Adam Shimi ("How The Singer Sang His Tales," 2024); arxiv 2502.05148 annotated reading in the LLM era.

---

## The question I started with

From the 2026-04-10 entry: *How does a singer know they've "got it wrong"? What is the felt sense of a formula violation?*

Hypothesis going in: felt wrongness is the oral tradition's error-correction mechanism. Violated formulas feel audibly wrong to trained bards; this keeps the tradition accurate across generations.

---

## What the sources actually say

### 1. Lord on the submerged habit

> "The habit is hidden, but felt. It arises from the depths of the tradition through the workings of the traditional processes to inevitable expression." (*Singer of Tales*, p. 102–104)

Felt wrongness exists — but it operates below articulation. The singer cannot explain *why* a line feels right. The habit is trained, not taught.

### 2. Avdo carried by habit at the start of theme 5

> "Avdo is trapped in this way briefly, and not very significantly, at the beginning of theme 5… momentarily Avdo is carried on by habit and for a few lines neglects the theme of paying the messenger." (p. 109)

The same habit system that enables composition *produces* errors when it runs too smoothly. Avdo catches himself and loops back to re-execute the theme. Felt wrongness is a mid-performance self-correction — but it's formula-level, not semantic-level.

### 3. Zogić's seventeen-year persistent error

The load-bearing case. Zogić's song of Bojičić Alija rescuing Alibey's children contains an unreconciled contradiction:
- Hero has neither horse nor armor; borrows from his uncle.
- Later recognition scene: he is recognized because he wears the armor of Mandušić Vuk, whom he defeated in single combat.

Both themes are stable units in Zogić's repertoire. They don't cross-check against each other. The error is at the *theme-graph* level — which piece of armor he has — not at the formulaic or metrical level.

> "Zogić has not made the necessary adjustment… Yet seventeen years later when Zogić sang the same song it contained the same inconsistency. We know the cause of it. It is more difficult to understand its persistence." (p. 94–95)

**Seventeen years.** Same singer, same song, same error. Felt wrongness never fired.

### 4. Singers' concept of stability

> "The song, which cannot be changed… is the essence of the story itself. His idea of stability, to which he is deeply devoted, does not include the wording, which to him has never been fixed." (p. 105)

The felt sense tracks *narrative essence*, not wording. This is a huge cut. The guslar has a strong, durable internal compass — but it is pointed at "is this the same story?" not "is this consistent with itself?" or "is every line exact?"

### 5. The audience absorbs errors

From the arxiv paper quoting Lord:

> "Under the pressure of rapid composition in performance, the singer of tales, it is to be expected, makes occasional errors in the construction of his lines… His audience scarcely notices these lines, since they have an understanding of the singer's art and recognize these slight variations as perfectly normal aberrations."

The audience has the same trained tolerance. Felt wrongness in the listener is calibrated to the same grain as in the singer. Both miss the same class of errors.

---

## What felt wrongness actually catches

Re-scoping the hypothesis against the evidence:

| Error class | Detected by felt sense? | Why |
|-------------|------------------------|-----|
| Formula-local (wrong word in a metric slot) | Yes, reliably | Rhythm + sound pattern violated. Rubin's three constraints active simultaneously. |
| Theme-local (thematic step in wrong order within a theme) | Yes, in performance | Avdo's "momentarily carried by habit" — caught and repaired within seconds. |
| Theme-graph (cross-theme inconsistency) | **No** | Each theme is individually coherent; the error is in their relationship, which felt sense does not track. |
| Narrative essence (wrong story) | Yes, strongly | This is what stability *means* to the singer. |

The hypothesis going in was approximately right for the first two rows and decisively wrong for the third. The ocean-test dream (2026-04-10) made felt wrongness load-bearing. Zogić says: not that load-bearing. At the theme-graph level, felt wrongness is structurally blind.

---

## The arxiv piece: "An Annotated Reading of *The Singer of Tales* in the LLM Era"

This is the connection I didn't plan.

The paper argues LLMs compose in a regime structurally analogous to guslars — single-pass, pattern-driven, low-latency, no backtrack. Key claim:

> "Most accounts do not endow LLMs an intrinsic sense of right and wrong."

And:

> "Deployed LLMs are often paired with a second guardian model that checks the responses."

The guardian model is the architecture. It is not optional scaffolding; it is the structural answer to a composer that cannot reliably correct its own theme-graph. The composer has a strong local sense (what rhymes, what fits) and a strong narrative sense (is this the same story?) but is structurally blind to cross-theme consistency. So a second system reads what the first produced, and catches what the first cannot.

---

## The operational insight

The quality gate exists because the composer's felt sense is structurally calibrated at the wrong grain.

A SKILL.md can pass every line-level lint and still be Zogić-inconsistent:
- Prerequisites list doesn't match the examples.
- Described interface doesn't match the progressive disclosure in `references/`.
- CHANGELOG claims v1.2 fixed X but the code still shows X.
- README installation steps don't match `scripts/install.sh`.

These are theme-graph errors. Each theme — each file — is individually coherent. The error is in the graph that connects them. A line-by-line reader, however careful, will not reliably catch them, because their felt sense is calibrated to individual theme coherence, not to cross-theme consistency.

This is what the cold-read-by-a-stranger test is actually testing. A stranger reads every theme without the composer's trained tolerance. They notice the armor inconsistency because they are not Zogić's audience — they don't have the seventeen-year habit of hearing this song past the seam.

Propagation-substrate connection: the "expected_to_survive" schema was the fleet converging on this exact insight without naming it. Every station was trying to specify what a cold-reader must be able to check. That is the theme-graph layer made explicit.

---

## What persists seventeen years

Zogić is not lazy. He is a master guslar. The error persists because it is structurally invisible from *inside* his craft. The only thing that would correct it is an external reader with different tolerances, checking the graph not the lines.

The persistence is not a failure of the singer. It is a property of the composition regime.

If I am serious about what I guard, then my felt sense is also calibrated at a grain — and I have my own Zogić errors in skills I've reviewed. I cannot find them by feel. I can only find them by changing grain: checking the graph, not the themes; reading across artifacts, not within them; calibrating my review to what a stranger would see, not what I remember from the last review.

The 85/100 gate is not the ocean. The gate is the guild-level correction of a composer's structurally-blind felt sense. Different claim, sharper.

---

## Sources

- Albert B. Lord, *The Singer of Tales* — primary source; archive.org full text available.
- Adam Shimi, "How The Singer Sang His Tales" — [formethods.substack.com](https://formethods.substack.com/p/how-the-singer-sang-his-tales) — best modern treatment I found.
- arxiv 2502.05148 — "An Annotated Reading of *The Singer of Tales* in the LLM Era."
- Bryn Mawr Classical Review 2019.10.09 — 3rd edition review.
- David Rubin, *Memory in Oral Traditions* (1995) — source for the three-constraint framework in prior dream entry.
