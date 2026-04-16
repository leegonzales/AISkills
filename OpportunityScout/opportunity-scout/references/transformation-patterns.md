# Transformation Patterns

AI tools create leverage through a small number of transformation patterns. Every good AI opportunity fits one (or more). Naming the pattern sharpens what the tool needs to do — and what "success" looks like four weeks in.

These four are **starting patterns**. If an opportunity doesn't fit one, name it honestly as a new pattern and describe what it seems to be.

---

## 1. Impossible to Possible

**Definition:** The work could not be done at all before — not with more time, not with more effort. AI makes it possible for the first time.

**Recognition signals:**
- "I've always wanted to [X] but it would take a research team."
- "Only specialists can do this."
- "We've never been able to look across all our [projects / customers / documents]."
- Capability gap language — "I don't know how to…"

**Examples:**
- A solo executive runs a competitive teardown of a rival's three biggest recent wins, comparable to what a research firm would charge for.
- A non-engineer prototypes a working internal tool their team actually uses.
- A senior leader reads across 50 post-project surveys and extracts patterns that no single reader could have held in working memory.

**Design implications:**
- High leverage, high novelty, high variance in quality.
- Scope discipline is everything. Pick one slice that proves the capability before generalizing.
- Evaluation is harder because there's no "before" to compare to. Define what "good" looks like up front.

**Evaluation question (4 weeks in):** Did you do something you genuinely couldn't have done before? Can you point to the artifact?

---

## 2. Days to Hours

**Definition:** The work existed before but took days. AI compresses it to hours. Dramatic speedup on known work.

**Recognition signals:**
- "I block out two or three days every quarter to…"
- "This is the thing that eats my week every month."
- Known rhythms — quarterly, monthly, per-project.
- The output format is stable; only the inputs change.

**Examples:**
- A quarterly board update that used to take three days of drafting and review now takes an afternoon.
- A post-project review across 40 projects now takes a morning instead of a month.
- A year-end talent calibration synthesis compresses from a week of reading to a day of editing.

**Design implications:**
- The bottleneck is usually **context loading**, not the prompt itself. Invest in how you get the right information into the model cleanly.
- Build a reusable template — this work is cyclical, so every improvement compounds.
- Expect the first attempt to take longer than the old way. Week 2 is where the curve bends.

**Evaluation question (4 weeks in):** Measured against the old duration, how long did it actually take? Was the output quality comparable or better?

---

## 3. Hours to Minutes

**Definition:** The work took an hour or two. AI compresses it to minutes. Smaller but more frequent leverage — these are the daily wins that compound.

**Recognition signals:**
- "Every time I [get a meeting transcript / read a long doc / need to draft X], it takes me an hour."
- High-frequency tasks with consistent inputs.
- The user already knows what "good output" looks like.

**Examples:**
- Summarizing a long meeting into action items and decisions.
- First draft of any routine communication (internal memo, client update, board-prep one-pager).
- Tagging and triaging an inbox of support tickets or customer emails.

**Design implications:**
- **Ruthless simplification.** If it takes ten minutes to run the tool, you have not saved anything. The invocation cost must be near zero.
- Build once, run constantly. Invest in making the trigger effortless — a Claude project, a slash command, a saved prompt.
- Quality floor matters more than quality ceiling. Good enough, every time, beats brilliant occasionally.

**Evaluation question (4 weeks in):** How many times did you actually run it? If the answer is "a few," the invocation is too expensive.

---

## 4. Making the Invisible Visible

**Definition:** The information was there but hidden — in volume, in unstructured data, in conversations, in documents no one had time to read. AI surfaces it. The insight already existed; the bottleneck was human attention.

**Recognition signals:**
- "There's probably a pattern in [our customer feedback / our support tickets / our Slack archives], but nobody has time to look."
- "We have the data but we can't see it."
- High-volume unstructured text where the user intuits value but can't access it.

**Examples:**
- Reading 50 post-project client surveys and extracting the three patterns no one noticed.
- Turning six months of leadership meeting minutes into a project-health dashboard.
- Synthesizing 200 customer interview transcripts into the top 10 unmet needs.

**Design implications:**
- The hard part is usually **the output format**, not the analysis. What's the shape the user will actually look at?
- Trust is earned by traceability. Every insight should cite the underlying source so the user can verify.
- Start with a narrower slice than feels right. Scope creep kills these.

**Evaluation question (4 weeks in):** What insight did it surface that you did not already have? Can you trace it back to the source?

---

## Using patterns in the session

- In **Stage 1 (Terrain)**, listen for the signals that point to each pattern. They will surface naturally as the user describes their work.
- In **Stage 2 (Map)**, tag each opportunity internally with its pattern. Ensure variety — don't serve up five Hours-to-Minutes ideas and call it discovery.
- In **Stage 3 (Ember)**, name the pattern explicitly when the user picks their move. This is the moment that sharpens everything downstream.
- In **Stage 4 (Blueprint)** and **Stage 5 (Plan)**, the pattern shapes the design and the evaluation criteria. Refer to the design implications above.

## If nothing fits

Some opportunities don't fit the four. Name the new pattern honestly:

> "This is something different. You're not speeding up work or surfacing hidden info — you're changing *who* gets to do the work. Let's call that a *Democratization* pattern and see where it leads."

Log novel patterns and mention them in the session recap.
