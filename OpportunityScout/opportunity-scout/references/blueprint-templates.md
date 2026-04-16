# Blueprint Templates — First-Version Design by Pattern

In Stage 4, you're helping the user design the first working version of their chosen move. The transformation pattern shapes the blueprint. Use these starting points — not as fill-in-the-blank forms, but as a sketch of what the first version should look like for each pattern.

---

## Impossible-to-Possible Blueprint

**Design principle:** Scope discipline. Pick one slice that proves the capability. Expect high variance in early attempts.

**First-version structure:**

1. **Name the capability you're claiming.** Write one sentence: "I will be able to [do X], which I previously couldn't do without [specialist / team / outside firm]."
2. **Pick the one slice.** What's the smallest version of this capability that would still count as "I did it"?
3. **Inputs.** What goes in? Where does it come from? How much of it?
4. **Output shape.** What will the artifact look like? (A memo? A deck? A ranked list? A decision matrix?)
5. **Quality bar.** What would a specialist have produced? What's "good enough" for the first attempt?
6. **The prompt.** A first draft, using role + context + constraints + examples.

**Common failure modes to pre-empt:**
- **Over-scope:** trying to do everything at once. Fix: the "one slice" is usually smaller than first instinct.
- **No baseline:** no way to tell if it worked. Fix: describe what a specialist would have done.
- **Hallucinated specificity:** model invents plausible-sounding detail. Fix: require source citation for every factual claim.

**Sample prompt sketch (competitive teardown example):**

```
ROLE: You are a senior competitive strategy analyst who has done
teardowns of major construction and design-build firms for 15 years.

CONTEXT: I'm the president of a $1B design-build GC. I need a
competitive teardown of [RIVAL FIRM]'s three biggest wins in the last
18 months — what they won, why they won, and what it tells us about
where they're heading.

INPUT: I'll paste links to the project announcements. Use web search
to pull public details. Do not speculate beyond what's in the sources.

OUTPUT:
- One-page teardown per project (what, why, signals)
- Cross-project synthesis: three patterns I should know about
- One strategic implication for our own positioning

CONSTRAINTS:
- Cite every factual claim with a source link.
- Flag anything you're inferring vs. observing.
- If a project is too opaque to analyze, say so — do not fabricate.
```

---

## Days-to-Hours Blueprint

**Design principle:** The bottleneck is usually context loading. Invest in how the right information gets into the model cleanly.

**First-version structure:**

1. **Name the work.** "I do [X] once a [quarter / month]. It takes about [N] days."
2. **Decompose the work.** What are the 3–5 macro steps? Which are AI-tractable, which aren't?
3. **Context inputs.** What does the model need? Historical versions of the same artifact? Raw source data? Reference documents? Pre-assemble this.
4. **Template the output.** The output shape is usually stable — previous versions of the same artifact are your best training signal. Use them as few-shot examples.
5. **Chain the steps.** Often a prompt chain beats a mega-prompt. Step 1 extracts, Step 2 structures, Step 3 drafts, Step 4 polishes.

**Common failure modes to pre-empt:**
- **Stuffing context badly:** dumping 80 pages of raw input into one prompt. Fix: pre-process into structured context.
- **No historical grounding:** model produces a generic version. Fix: show 2–3 past examples in the prompt.
- **Losing the house style:** the quarterly update starts reading like a different author. Fix: explicit tone and structure constraints, preferably extracted from past versions.

**Sample prompt sketch (quarterly board update):**

```
ROLE: You are a chief of staff drafting a quarterly board update in
the voice and structure of the three examples provided.

CONTEXT: Attached are three prior quarterly updates [paste]. Attached
is this quarter's raw inputs: ops metrics, financials, top wins/losses,
people updates, strategic initiatives.

TASK:
1. First, extract the structure and house style from the three priors
   (section order, length, tone, level of specificity).
2. Then draft this quarter's update using that structure.
3. Flag any sections where the data is thin or unclear; leave a
   [PLACEHOLDER: need input on X] note rather than inventing.

OUTPUT: Same structure as the priors. Match sentence length and voice.
```

---

## Hours-to-Minutes Blueprint

**Design principle:** Ruthless simplification of invocation cost. If it takes 10 minutes to run the tool, nothing was saved.

**First-version structure:**

1. **Name the trigger.** "When [X happens], I need to [Y]." (e.g., "When a meeting transcript arrives, I need action items in 60 seconds.")
2. **Lock the invocation.** Make it one-click or one-paste. A Claude project with the prompt pre-loaded. A slash command. A saved template. Not a page of instructions.
3. **Lock the output shape.** Same format every time. Predictable.
4. **Accept a quality floor, not ceiling.** "Good enough, every time" > "brilliant sometimes."
5. **Measure invocation count.** If the user ran it fewer than 5 times in the first two weeks, the invocation is too expensive.

**Common failure modes to pre-empt:**
- **Elaborate prompts for simple outputs:** over-engineering kills this pattern. Fix: strip to minimum viable.
- **High-ceremony setup:** user has to remember where the prompt lives. Fix: put it in a Claude project, pin it, save the workflow.
- **Output drift:** format changes subtly run-to-run. Fix: rigid output-format specification, negative examples if needed.

**Sample prompt sketch (meeting transcript → action items):**

```
ROLE: You are an executive chief of staff who turns meeting
transcripts into action items.

INPUT: A meeting transcript I'll paste.

OUTPUT (use this exact format every time):

## Decisions
- [decision, who owns it, by when if stated]

## Action items
- [ ] [action] — owner: [name] — by: [date or "unspecified"]

## Open questions
- [question raised but not resolved]

## Risks / flags
- [anything I should know about — escalations, tensions, missing info]

RULES:
- Do not paraphrase decisions — use the speaker's language.
- If ownership is unclear, say "owner: unclear" — do not guess.
- If no decisions were made, say so. Do not invent.
```

---

## Invisible-to-Visible Blueprint

**Design principle:** The hard part is the output format, not the analysis. The user needs a shape they'll actually look at.

**First-version structure:**

1. **Name the information and why it's hidden.** "There's value in [X data], but nobody can read it all."
2. **Name the consumption moment.** Where, when, and how will the user look at the output? (On a phone in the morning? In a 30-min weekly review? As input to a quarterly decision?) This shapes the format.
3. **Scope to a narrow slice.** Don't analyze all 200 docs in the first pass. Analyze 20. Show the output. See if the shape is right. Then scale.
4. **Require source citation.** Trust depends on traceability. Every insight links back to the underlying document.
5. **Design the output format first.** Draft the empty version of the output before running any analysis. If the empty version isn't useful, the filled version won't be either.

**Common failure modes to pre-empt:**
- **Output is a wall of text:** no one reads it. Fix: tight structure, visual hierarchy, max 1 page unless drilling down.
- **Insights feel generic:** "customers want better service." Fix: require specific examples with citations.
- **No decision coupling:** analysis exists but doesn't feed a decision. Fix: end every analysis with "if this pattern is real, the implication is X."

**Sample prompt sketch (post-project survey synthesis):**

```
ROLE: You are a senior operations analyst synthesizing client post-
project feedback for an executive who has 15 minutes to read.

INPUT: 20 post-project surveys [paste or attach]. Each has scores and
open-text responses.

TASK:
1. Surface the top 3 patterns across the 20 surveys. A pattern means:
   it appears in at least 5 surveys, in similar language or with
   similar substance.
2. For each pattern: (a) name it in one line, (b) quote 2–3 source
   responses verbatim with survey ID, (c) describe the implication
   for how we run projects.
3. Flag any outlier surveys that don't fit the patterns — these may
   be the most important.

OUTPUT (max 1 page):

## Pattern 1: [name]
- Evidence: [quote 1 — Survey #X], [quote 2 — Survey #Y]
- Implication: [one sentence]

## Pattern 2: ... (same structure)
## Pattern 3: ... (same structure)

## Outliers worth a second look
- [Survey #Z: one-line summary of why it doesn't fit]

RULES:
- Every claim must trace to at least 2 surveys, quoted.
- Do not smooth over disagreements — if two patterns contradict,
  say so explicitly.
- If fewer than 3 real patterns exist, say so. Do not manufacture.
```

---

## Cross-pattern design tips

- **Always start smaller than feels right.** The first version exists to prove the shape works, not to do the whole job.
- **Design the output format before the prompt.** If you can draw the final artifact on a napkin, the prompt will follow. If you can't, the prompt won't save you.
- **Build in evaluation from day one.** Week 4 is when you decide keep / refactor / park. That decision needs data — define what "working" means before Week 1.
- **Prefer chains over mega-prompts for anything over moderate complexity.** Debuggability > elegance.
