# Craft Guide — Dimensions, Diagnostics, and Genre Calibration

This is the deep reference for *what good prose is* and *how to recognize the specific problem in front of you*. SKILL.md gives the workflow; this gives the judgment.

---

## The Six Dimensions in Depth

For each dimension: what it is, the diagnostic questions to ask, the common failure, and the fix — with before/after.

### 1. Clarity
**What it is:** A first-time reader extracts the intended meaning on one pass, without backtracking.

**Diagnostics:**
- Does every pronoun and "this/that/it" have one obvious referent?
- Is the real actor the grammatical subject, or is it buried in a nominalization ("the implementation of the decision was made")?
- Are abstractions anchored to something concrete?
- Is the logical connector ("therefore," "but," "because") accurate?

**Common failure:** Nominalization + passive voice hiding the agent.

> **Before:** "A determination regarding the cancellation of the project was reached by the committee."
> **After:** "The committee decided to cancel the project."

Meaning preserved; six words gone; the actor is visible.

### 2. Structure
**What it is:** The order of ideas serves the argument. The reader is never asked to hold an unexplained term, and the payoff lands where it has the most force.

**Diagnostics:**
- Does the opening earn the reader's attention or warm up first ("In today's fast-paced world…")?
- Could you reorder paragraphs and lose nothing? (If so, the structure isn't doing work.)
- Is the strongest sentence buried in the middle? (Move it to open or close.)
- Does the conclusion restate, or resolve?

**Common failure:** Burying the lede; throat-clearing openings; weak endings that trail off.

> **Before (opening):** "There are many factors to consider when thinking about remote work. In this piece I will discuss several of them."
> **After:** "Remote work didn't kill the office. It killed the commute — and that's a bigger deal than anyone admits."

The promise is now specific and the reader has a reason to continue. Note: this rewrite is legitimate only if "the commute matters more than the office" is actually what the author argues. If not, find *their* sharpest claim and lead with it. Never manufacture a thesis.

### 3. Economy
**What it is:** Every word earns its place. Tightening is the single highest-yield edit for most drafts.

**Diagnostics — cut or compress:**
- Filler openers: "It is important to note that," "In order to," "The fact that," "needless to say."
- Redundant pairs: "each and every," "first and foremost," "basic fundamentals."
- Hedge stacks: "I think that maybe it could possibly be."
- Adverbs propping weak verbs: "ran quickly" → "sprinted"; "very unique" → "unique."
- Sentences that restate the prior sentence.

> **Before:** "It is important to note that in order to achieve success, one must basically put in the necessary effort that is required."
> **After:** "Success takes effort."

**Caution:** Economy is not the goal *per se* — clarity and impact are. Do not strip a deliberately leisurely or lyrical passage to its bones. In fiction and personal essay, rhythm can outrank brevity.

### 4. Authority
**What it is:** Claims feel earned — specific, confident, grounded — so the reader trusts the writer.

**Diagnostics:**
- Vague quantifiers ("many," "various," "a lot") where the author likely knows the specific.
- Reflexive hedging that signals lack of conviction ("sort of," "kind of," "I would argue that perhaps").
- Abstract claims with no concrete instance.

**The hard line:** Authority comes from *sharpening* what the author knows, never from *adding* what they don't.
- Allowed: "Studies have shown X" → "X" (if the author owns the claim and the source isn't load-bearing), or removing a needless hedge.
- **Forbidden:** inventing the study, the statistic, the date, or the example. If a claim is weak because it lacks evidence, the fix is to flag it — "this assertion needs support" — not to fabricate the support.

> **Before:** "Some people might say that this approach could potentially be somewhat beneficial in certain cases."
> **After:** "This approach works." (only if the author clearly believes it; otherwise surface the hedge as a real uncertainty to resolve.)

### 5. Voice
**What it is:** A distinct, consistent human presence — the thing that makes prose sound like *someone*.

**Diagnostics:**
- Is there a consistent register, or does it lurch between casual and formal?
- Are there signature moves (dry asides, rhetorical questions, em-dash interruptions, short punchy fragments) worth protecting?
- Has prior editing already flattened it toward LLM-default smoothness?

**The discipline:** You are a ghost editor, not a co-author. Read enough of the draft to internalize the author's cadence before changing a word. Preserve their diction and idiom; fix only what undermines them. When two valid edits exist, choose the one closer to how *they* already write.

> **Author writes wry, clipped prose.**
> **Bad edit:** "It would be prudent to consider the ramifications of this decision in a holistic manner."
> **Good edit:** "Think it through. All of it."

The second keeps the voice; the first murders it.

### 6. Genre Fit
**What it is:** Register, structure, and diction match the form and the reader's expectations. See the calibration table below.

---

## Genre Calibration Table

| Genre | Voice latitude | Economy | Authority style | Structure default | Edit intensity |
|---|---|---|---|---|---|
| Personal essay / opinion | High — protect idiom | Medium | Earned via specificity & conviction | Hook → argument → resonant close | Light |
| Technical / docs | Low | High | Precision, correctness, no flourish | Task/answer first; scannable; parallel | Medium–heavy |
| Business email / memo | Low–medium | High | Direct, BLUF (bottom line up front) | Ask first, context after | Medium |
| Report / whitepaper | Medium | Medium | Evidence + measured claims | Exec summary → body → recommendation | Medium |
| Marketing / persuasive | High | High | Concrete benefit, rhythm, social proof (real) | One promise, escalate, single CTA | Medium |
| Fiction / narrative | Very high — cadence is craft | Low | N/A (voice & scene) | Author's; do not impose | Very light |
| Academic | Low | Medium | Citation, hedged precision | Field convention | Light–medium |

**Reading the table:** "Voice latitude" = how much of the author's idiosyncrasy to protect. High latitude means resist standardizing. "Edit intensity" = default aggressiveness; always start lighter than you think.

---

## The Homogenization Trap (read before every edit)

The strongest pull on an automated editor is toward a smooth, hedged, faintly corporate register — the average of all prose. Resist it actively:

- A blunt sentence is not "unprofessional." A fragment is not "an error." Repetition is often rhetoric.
- If your edit makes a distinctive piece sound like every other piece, you have failed even if each sentence is "cleaner."
- The test: would the author recognize this as their own writing, just better? If not, back off.

## Meaning-Preservation Tripwires

Stop and flag rather than edit when:
- A sentence has two plausible readings — ask which is meant.
- A claim is unsupported — note it; do not invent support.
- Cutting a clause would also cut a nuance, caveat, or scope limit the author intended.
- A term is jargon to you but may be precise term-of-art to the audience — verify before "simplifying."
