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

Additional transformations:
- Add verbal signposts ("First... Second... Finally...")
- Include audience engagement ("Think about this...")
- Create transitions that work aurally
- Build to a memorable landing, not a summary

### 3. Assess Images (if present)

For essays containing images:
- **Detect**: Identify all images referenced in the essay (inline, figures, diagrams)
- **Associate**: Link each image to the chunk it belongs to
- **Assess**: Evaluate each image for presentation fitness:
  - Resolution/quality sufficient for slides?
  - Content clear and self-explanatory?
  - Text legible at presentation scale?
  - Relevant to the spoken content?
- **Recommend**: Provide guidance for the slide-builder:
  - `USE` - Image works as-is for slides
  - `ADAPT` - Good concept but needs modification (crop, enlarge text, simplify)
  - `RECREATE` - Redraw/regenerate with better presentation formatting
  - `SKIP` - Decorative or not suited for presentation context

### 4. Preserve the Connection

**Critical**: Output BOTH versions for each chunk. The original is never modified.

## Output Format

### Filename Convention

Generate a logical filename from the essay title:
- `{slugified-title}-presentation.md`
- Example: "The Future of Remote Work" → `the-future-of-remote-work-presentation.md`

### Document Structure

```markdown
# [Essay Title]: Presentation Version

**Source**: [Original essay title/description]
**Chunks**: [N sections]
**Generated**: [Date]

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

Use these tags to mark structural elements within the talk track:

| Tag | Purpose | Example |
|-----|---------|---------|
| `[HOOK]` | Opening attention-grabber | `[HOOK] Let me ask you something...` |
| `[KEY_POINT]` | Core argument or insight | `[KEY_POINT] This changes everything about...` |
| `[EVIDENCE]` | Data, examples, proof | `[EVIDENCE] Last year, 73% of companies...` |
| `[STORY]` | Narrative or anecdote | `[STORY] I met a manager who...` |
| `[TRANSITION]` | Bridge between ideas | `[TRANSITION] So that's the problem. Now let's talk solutions.` |
| `[CALLBACK]` | Reference to earlier point | `[CALLBACK] Remember that 73% figure?` |
| `[LANDING]` | Section or final conclusion | `[LANDING] And that's why this matters.` |
| `[CTA]` | Call to action | `[CTA] Starting tomorrow, I want you to...` |

Not every paragraph needs a tag—use them for key structural moments that the slide-builder can anchor to.

### Images Section (when applicable)

If the original essay contains images, each chunk includes a `### Images` section:

```markdown
### Images
- `fig1-market-share.png`: USE - Clear pie chart, good resolution, works as-is
- `fig2-workflow.png`: ADAPT - Good diagram but text too small for projection, enlarge labels
- `header-decorative.jpg`: SKIP - Decorative banner, no informational value for presentation
- `fig3-data-table.png`: RECREATE - Data is valuable but table format doesn't work for slides, convert to bar chart
```

**Assessment criteria:**
| Rating | Meaning | Slide-builder action |
|--------|---------|---------------------|
| `USE` | Presentation-ready | Include directly |
| `ADAPT` | Good concept, needs tweaks | Modify (crop, resize text, simplify) |
| `RECREATE` | Valuable content, wrong format | Rebuild as presentation-friendly visual |
| `SKIP` | Not suited for presentation | Omit or replace with slide idea |

**No images?** Omit the `### Images` section entirely for text-only chunks.

### Slide Ideas Section

Each chunk includes a `### Slide Ideas` section with 1-3 suggestions:
- Chart/graph types with specific data to visualize
- Key quote or stat callouts
- Comparison frameworks (before/after, A vs B)
- Visual metaphors or imagery concepts
- "No slide" if the chunk is purely transitional

When original images exist, slide ideas should reference them:
- "Use `fig1-market-share.png` as primary visual"
- "Recreate `fig3-data-table.png` as horizontal bar chart"

These are suggestions, not requirements—the slide-builder skill makes final decisions.

## Delivery Markup (Optional)

When user requests annotated output, add:
- `[PAUSE]` - Breath/emphasis pause
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

## Example Transformation

**Original (written)**:
> It is widely acknowledged in the literature that remote work has fundamentally altered employee expectations regarding workplace flexibility. This shift, which accelerated during the 2020 pandemic, has created lasting changes in how organizations must approach talent retention.

**Talk Track (with semantic tags)**:
> [HOOK] Here's something every leader needs to understand.
>
> [KEY_POINT] Remote work didn't just change *where* people work. It changed what they *expect*.
>
> [EVIDENCE] The pandemic accelerated a shift that's not going back.
>
> [TRANSITION] And if you're still thinking about "return to office" as your strategy? You're solving yesterday's problem.

### Images
- `remote-work-timeline.png`: ADAPT - Good timeline concept but years are hard to read, enlarge date labels

### Slide Ideas
- Title slide: "The Expectation Shift" - use adapted `remote-work-timeline.png`
- Single stat callout: "Flexibility is now table stakes"
- Optional: Icon grid showing changed expectations (location, hours, autonomy)

## References

- `references/transformation-patterns.md` - Detailed written→spoken patterns
- `references/examples.md` - Full before/after essay transformations
