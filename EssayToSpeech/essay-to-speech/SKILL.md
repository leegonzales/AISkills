---
name: essay-to-speech
description: Transform written essays into spoken word presentations while preserving source material. Also renders training module facilitator artifacts as standalone HTML document viewers. Use when adapting essays for verbal delivery, creating talk tracks, preparing content for presentation slides, or rendering module documents.
---

# Essay to Speech

Two modes:

## Mode 1: Essay to Talk Track (default)

Transform written essays into spoken word presentations. Outputs both the original text and talk track in connected chunks, ready for downstream slide generation.

## Mode 2: Module Document Renderer

Render a training module's facilitator artifacts (guides, prompts, skills) as a standalone HTML document viewer with sidebar navigation, dark mode, full-text search, and Catalyst Calm Luxury branding.

**Invoke Mode 2 when:**
- User points to a module directory with facilitator guides/prompts
- User asks to "render documents" or "generate guide HTML"
- Input is a directory path (not an essay file)

**Usage:**
```bash
python3 ~/.claude/skills/essay-to-speech/scripts/render-docs.py <module_dir> \
  --output <path.html> --title "Module Title"
```

**Template:** `templates/catalyst-docs.html` (Catalyst Calm Luxury palette)
**Script:** `scripts/render-docs.py` (scans for .md files, categorizes, injects into template)

---

## Fidelity Firewall (never violate)

**Adapting an essay for the ear is editing someone's real argument. Making it speakable is not the same as making it stronger than the source.** You may shorten sentences, drop notation, swap passive for active, and add rhythm — but translating notation or jargon into plain English may **NOT** change the **strength**, **direction**, or **certainty** of any claim.

**The hard rules:**

1. **Preserve the hedge.** "Suggests," "may," "appears," "is associated with," "tends to," "in this sample" are load-bearing epistemics, not academic throat-clearing. Do **not** upgrade them to "proves," "shows," "guarantees," "overwhelming," or "always." A weak claim spoken aloud is still a weak claim. When the essay hedges, the talk track hedges.

2. **Stay faithful to what the number licenses.** When converting a statistic to prose, say only what the statistic actually supports:
   - A **correlation** is not **causation** ("linked to" / "moves with," not "causes" / "drives").
   - A **small/weak** effect (e.g. `r ≈ 0.1–0.3`) is "a weak link" / "a slight tendency," not "strongly linked."
   - A **large effect size** is not "proof." Significance (`p`) is about ruling out chance, not about magnitude — don't conflate them.
   - A **confidence interval** that crosses zero (or is wide) means the result is **uncertain** — say so; don't declare the relationship "real."
   - **Preserve direction.** A negative coefficient is an *inverse* relationship; never flip the sign in translation.

3. **Never invent magnitude, significance, or interpretation the source doesn't state.** If the essay reports `r = -0.3` and calls it weak, the talk track does not promote it to "almost a perfect inverse." If the source draws no causal or practical conclusion, you don't add one.

4. **The original is never modified — literally.** Where the skill promises verbatim source (the `### Original` block), emit the essay text exactly, character for character. No silent fixing, summarizing, or strengthening.

5. **When unsure how strong a claim is, under-claim.** Round *down* on confidence, not up. An honest "seems to be a modest link" beats a false "overwhelming evidence."

The translation tables below (notation→prose, hedging→confidence) are **register conversions, not strength conversions.** Their plain-English targets are illustrative of *tone*, not licenses to inflate. Calibrate every rendering to the actual claim in front of you — if the source is hedged, pick a hedged target. This firewall outranks every stylistic or "speakability" gain.

---

## Mode 1 Details

## When to Use

Invoke when user:
- Wants to turn an essay into a presentation talk track
- Needs to adapt written content for verbal delivery
- Is preparing a speech from written material
- Uses `/essay-to-speech` command

## Transformation Intensity

Default to **full** transformation unless the essay is already conversational.

| Mode | When to Use | Approach |
|------|-------------|----------|
| **Full** (default) | Academic, formal, or dense prose | Aggressive rewrite for natural speech |
| **Light** | Already conversational, personal voice | Preserve author's voice, minimal changes |

**Auto-detect**: If the essay uses "I", contractions, and short sentences, use light mode. If it uses passive voice, complex clauses, and formal language, use full mode.

## Core Process

### 1. Segment the Essay

Break the essay into atomic chunks based on:
- **Existing structure first**: Honor headings, sections, paragraph breaks
- **Argument units**: Each chunk = one coherent point or idea
- **Slide-sized thinking**: Could this chunk support one slide?

Typical segmentation:
- Introduction → Opening hook chunk
- Each major section → 1-3 chunks depending on density
- Conclusion → Landing chunk

### 2. Transform Each Chunk

Convert written prose to spoken language:

| Written Pattern | Spoken Pattern |
|----------------|----------------|
| "This essay examines..." | "Today I want to share..." |
| "As previously mentioned..." | "Remember when I said..." |
| "It is important to note that..." | "Here's what matters..." |
| "In conclusion, this paper has demonstrated..." | "So what does this mean for you?" |
| Complex nested clauses | Shorter, punchier sentences |
| Passive voice | Active voice |
| Academic *throat-clearing* ("it is worth noting") | Direct phrasing — but keep *epistemic* hedges ("suggests," "may") intact |
| Dense paragraphs | Breathing room, varied rhythm |

#### Statistical Notation → Plain English

**Critical**: Convert all statistical notation to spoken-friendly language. Nobody says "rho equals negative 0.91" on stage.

**Bound by the Fidelity Firewall:** drop the *notation*, keep the *strength*. The plain-English rendering must match what the number actually licenses — and it must match how the **source** characterizes it. The examples below assume a strong, source-endorsed result; for a weak or hedged result, pick a weak, hedged rendering (see the calibration row).

| Written (Academic) | Spoken (only if the magnitude/source supports it) |
|-------------------|------------------|
| "ρ = -0.91" | "a strong inverse link—as one goes up, the other tends to go down" *(strong, but a link, not a cause)* |
| "β = 0.27, p < 0.001" | "an effect unlikely to be chance" *(significance ≠ size — `p` rules out luck, it doesn't make the effect big)* |
| "95% CI: 0.40-1.29" (excludes 0) | "the data point fairly consistently in one direction" |
| "95% CI: -0.05-1.29" (crosses 0) | "the result is uncertain—it could go either way" *(do NOT say 'real' or 'confident')* |
| "ΔELPD = 50.9 (SE = 10.2)" | "one model fit the data clearly better" *(only 'strong evidence' if the source says so)* |
| "coefficient: 0.65" | "a sizable association" *(association, not 'relationship that proves X')* |
| "r² = 0.73" | "this accounts for much of the variation we see" |
| "r ≈ 0.1-0.3" | "a weak link—a slight tendency, nothing more" |
| "n = 667" | "nearly 700 people" |

**Calibration rule:** the *adjective* in your rendering is set by the *number and the source's framing*, not by your desire for a punchy line. Map magnitude honestly: weak→"slight/weak," moderate→"meaningful/notable," strong→"strong." Never narrate a correlation as causation, a wide/zero-crossing interval as certainty, or significance as size. Keep the *meaning* of statistics, drop the *notation*. The audience needs to understand the insight accurately, not just dramatically.

#### Rhythm and Breath

Vary sentence length deliberately. Pattern: **Long → Short → Medium**

**Too uniform (written)**:
> The researchers found that Theory of Mind predicted collaboration. The correlation was significant. The effect was strong.

**Varied rhythm (spoken)**:
> The researchers found something surprising about what predicts AI collaboration success. Theory of Mind. Not technical skill—a social skill.

**Breath points**: Insert natural pauses by breaking at:
- After a key insight (let it land)
- Before a contrast ("But here's the thing...")
- After rhetorical questions (let audience think)

### 3. Assess Images (if present)

For essays containing images, apply a **critical eye**—not everything works on a slide at 20 feet.

**Detection**: Identify all images referenced in the essay (inline, figures, diagrams)

**Assessment questions** (be skeptical):
- Can the audience read this from the back row?
- Does this make sense without the surrounding text?
- Is this a data dump or a clear visual?
- Would a simpler version communicate better?

**Common issues to flag**:
| Image Type | Common Problem | Likely Rating |
|------------|----------------|---------------|
| Scatter plots | Too many points, tiny labels | ADAPT or RECREATE |
| Tables | Text-heavy, not visual | RECREATE as chart |
| Screenshots | Low resolution, cluttered | ADAPT (crop) or SKIP |
| Flowcharts | Too many boxes, small text | ADAPT (simplify) |
| Bar/pie charts | Usually fine if not too busy | USE or ADAPT |
| Conceptual diagrams | Often good | USE |
| Decorative images | No information value | SKIP |

**Ratings**:
- `USE` - Genuinely presentation-ready (rare for academic figures)
- `ADAPT` - Good concept, needs work (most common)
- `RECREATE` - Valuable data, wrong format (tables, dense plots)
- `SKIP` - Doesn't add value to spoken presentation

**Be honest**: Rating everything "USE" isn't helpful. Most academic figures need adaptation.

### 4. Preserve the Connection

**Critical**: Output BOTH versions for each chunk. The original is never modified — emit it **verbatim**, character for character (per the Fidelity Firewall). The talk track may rephrase; the `### Original` block may not.

## Output Format

### Filename Convention

Generate a logical filename from the essay title:
- `{slugified-title}-presentation.md`
- Drop common stop words (the, a, an, in, of, and, or) for concise filenames
- Example: "The Future of Remote Work" → `future-remote-work-presentation.md`

### Document Structure

```markdown
# [Essay Title]: Presentation Version

**Source**: [Original essay title/description]
**Chunks**: [N sections]
**Generated**: [Date]
**Mode**: [Full/Light transformation]

---

## Section 1: [Descriptive Title]

### Original
[Verbatim essay text for this section - unchanged]

### Talk Track
[HOOK] Let me start with a question: what if everything you thought you knew was wrong?

[KEY_POINT] The real issue isn't what people say—it's what they actually do.

[EVIDENCE] A recent study found a 50% gap between reported intentions and actual behavior.

[TRANSITION] Now that we understand the problem, let's look at what we can do about it.

### Images
- `figure1.png`: USE - Clear diagram, good resolution
- `chart2.png`: ADAPT - Needs larger labels for projection

### Slide Ideas
- [Suggested visual, chart type, or slide concept]
- [Alternative approach or supporting visual]

---

## Section 2: [Descriptive Title]

### Original
[Verbatim essay text for this section]

### Talk Track
[Tagged spoken content...]

### Slide Ideas
- [Visual suggestions for this chunk]

---

[Continue for all sections...]
```

### Talk Track Semantic Tags

Use tags to mark **key structural moments**—not every sentence.

| Tag | Purpose | Example |
|-----|---------|---------|
| `[HOOK]` | Opening attention-grabber | `[HOOK] Let me ask you something...` |
| `[KEY_POINT]` | Core argument or insight | `[KEY_POINT] This changes everything about...` |
| `[EVIDENCE]` | Data, examples, proof | `[EVIDENCE] Nearly 700 people were tested...` |
| `[STORY]` | Narrative or anecdote | `[STORY] I met a manager who...` |
| `[TRANSITION]` | Bridge between ideas | `[TRANSITION] So that's the problem. Now let's talk solutions.` |
| `[CALLBACK]` | Reference to earlier point | `[CALLBACK] Remember that study I mentioned?` |
| `[LANDING]` | Section or final conclusion | `[LANDING] And that's why this matters.` |
| `[CTA]` | Call to action | `[CTA] Starting tomorrow, I want you to...` |

**Tagging guidelines**:
- 2-4 tags per section is typical
- Don't tag every paragraph—it becomes noise
- Untagged sentences flow naturally between tagged moments
- Tags help the slide-builder know where visual anchors belong

### Images Section (when applicable)

If the original essay contains images, each chunk includes a `### Images` section:

```markdown
### Images
- `fig1-market-share.png`: USE - Clean pie chart, large labels, works as-is
- `fig2-scatter.png`: ADAPT - Good data but axis labels too small, needs enlargement
- `fig3-table.png`: RECREATE - Important data but tables don't work on slides, convert to horizontal bar chart
- `header-decorative.jpg`: SKIP - Decorative only, no value for presentation
```

**No images?** Omit the `### Images` section entirely for text-only chunks.

### Slide Ideas Section

Each chunk includes a `### Slide Ideas` section with 1-3 suggestions:
- Chart/graph types with specific data to visualize
- Key quote or stat callouts
- Comparison frameworks (before/after, A vs B)
- Visual metaphors or imagery concepts
- "No slide needed" if the chunk is purely transitional

When original images exist, slide ideas should reference them:
- "Use `fig1-market-share.png` as primary visual"
- "Recreate `fig3-table.png` as horizontal bar chart showing top 5 only"

These are suggestions, not requirements—the slide-builder skill makes final decisions.

## Delivery Markup (Optional)

When user requests annotated output, add delivery cues:
- `[PAUSE]` - Breath/emphasis pause (after key insights, before contrasts)
- `*word*` - Vocal emphasis
- `[SLOW]` / `[FASTER]` - Pacing shifts
- `[LOOK UP]` - Eye contact moment

## What This Skill Does NOT Do

- Design slides or visuals (that's the next skill)
- Edit or modify images (assesses only, slide-builder handles modifications)
- Fundamentally rewrite arguments or add new content
- Coach on public speaking technique
- Change the essay's core message or stance

## Best Practices

1. **Preserve meaning**: The talk track conveys the same arguments, just spoken
2. **Respect structure**: Don't arbitrarily merge or split the author's sections
3. **Natural chunking**: Each section should feel like a complete thought
4. **Opening matters**: Transform bland thesis statements into hooks
5. **Landing matters**: End with impact, not "in conclusion"
6. **Kill the jargon, not the caveat**: Statistical notation, acronyms, and academic language don't belong in speech — but the *hedge inside* a claim ("suggests," "associated with," "in this sample") does. Drop the notation; keep the claim's true strength and direction (see Fidelity Firewall)
7. **Vary the rhythm**: Mix sentence lengths—monotony kills engagement
8. **Be a critical friend on images**: Most academic figures need work; say so

## Example Transformation

**Original (written)**:
> The study found ToM strongly predicted collaborative ability with AI (coefficient: 0.65, 95% CI: 0.01-1.29). Translation: higher Theory of Mind scores meant better AI collaboration, and we can be 95% confident this relationship is real—the confidence interval stays positive.

**Talk Track (full transformation)**:
> [EVIDENCE] The study found a sizable link between Theory of Mind and AI collaboration success. Higher Theory of Mind scores went with better results when working with AI.
>
> [KEY_POINT] The confidence interval stayed on the positive side—so the direction of the effect held up, even if its exact size is fuzzy.

**What changed**:
- "coefficient: 0.65" → "a sizable link" (notation dropped, strength preserved, **"link" not "cause"**)
- "95% CI: 0.01-1.29" → "the direction of the effect held up, even if its exact size is fuzzy" — note the interval **runs nearly to zero (0.01)**, so the magnitude is genuinely uncertain. We report the direction honestly and flag the fuzz; we do **not** claim "overwhelming" or "proven."
- "predicted" → "went with" — the source reports association, not a demonstrated cause
- Complex sentence broken into two
- Same meaning *and the same certainty*, speakable language

**Firewall check**: an earlier, tempting rendering — *"the statistics are clear, this isn't a maybe, we can be confident this relationship is real"* — would **over-claim**. A CI hugging zero is the definition of "maybe." The faithful version keeps the hedge.

### Images
- `correlation-scatter.png`: ADAPT - Data points clear but axis labels "ToM Score" and "κ (Collaborative Ability)" need plain English labels

### Slide Ideas
- Single insight slide: "Theory of Mind → Better AI Collaboration"
- Visual: simplified scatter with trend line, labeled "Social Skill" → "AI Success"

## References

- `references/transformation-patterns.md` - Detailed written→spoken patterns
- `references/examples.md` - Full before/after essay transformations
