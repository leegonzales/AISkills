---
name: essay-to-speech
description: Transform written essays into spoken word presentations while preserving source material. Use when adapting essays for verbal delivery, creating talk tracks, or preparing content for presentation slides.
---

# Essay to Speech

Transform written essays into spoken word presentations. Outputs both the original text and talk track in connected chunks, ready for downstream slide generation.

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
| Academic hedging | Confident assertions |
| Dense paragraphs | Breathing room, varied rhythm |

#### Statistical Notation → Plain English

**Critical**: Convert all statistical notation to spoken-friendly language. Nobody says "rho equals negative 0.91" on stage.

| Written (Academic) | Spoken (Natural) |
|-------------------|------------------|
| "ρ = -0.91" | "almost a perfect inverse—when one goes up, the other goes down" |
| "β = 0.27, p < 0.001" | "a significant effect—this isn't random chance" |
| "95% CI: 0.01-1.29" | "we can be confident this relationship is real" |
| "ΔELPD = 50.9 (SE = 10.2)" | "the statistical evidence was overwhelming" |
| "coefficient: 0.65" | "a strong positive relationship" |
| "r² = 0.73" | "this explains most of the variation" |
| "n = 667" | "nearly 700 people" |

Keep the *meaning* of statistics, drop the *notation*. The audience needs to understand the insight, not verify the math.

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

**Critical**: Output BOTH versions for each chunk. The original is never modified.

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
6. **Kill the jargon**: Statistical notation, acronyms, and academic language don't belong in speech
7. **Vary the rhythm**: Mix sentence lengths—monotony kills engagement
8. **Be a critical friend on images**: Most academic figures need work; say so

## Example Transformation

**Original (written)**:
> The study found ToM strongly predicted collaborative ability with AI (coefficient: 0.65, 95% CI: 0.01-1.29). Translation: higher Theory of Mind scores meant better AI collaboration, and we can be 95% confident this relationship is real—the confidence interval stays positive.

**Talk Track (full transformation)**:
> [EVIDENCE] The study found a strong link between Theory of Mind and AI collaboration success. And this isn't a maybe—the statistics are clear. Higher Theory of Mind means better results with AI.
>
> [KEY_POINT] We can be confident this relationship is real.

**What changed**:
- "coefficient: 0.65, 95% CI: 0.01-1.29" → "a strong link" + "the statistics are clear"
- "confidence interval stays positive" → "we can be confident this relationship is real"
- Complex sentence broken into two
- Same meaning, speakable language

### Images
- `correlation-scatter.png`: ADAPT - Data points clear but axis labels "ToM Score" and "κ (Collaborative Ability)" need plain English labels

### Slide Ideas
- Single insight slide: "Theory of Mind → Better AI Collaboration"
- Visual: simplified scatter with trend line, labeled "Social Skill" → "AI Success"

## References

- `references/transformation-patterns.md` - Detailed written→spoken patterns
- `references/examples.md` - Full before/after essay transformations
