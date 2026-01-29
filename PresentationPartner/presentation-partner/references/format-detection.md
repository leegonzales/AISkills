# Format Detection Guide

How to recognize input formats and route them appropriately in the presentation-partner skill.

---

## Purpose

Users arrive with content in various formats. Correct detection determines the conversation path:
- Some formats need full Discovery interview
- Some can jump to structure extraction
- Some need format conversion + audio authoring

---

## Format Recognition Patterns

### Talk Track v5 (Native Format)

**Indicators:**
- YAML frontmatter with `version: 5` or `version: 6`
- `## Slides` section with markdown table
- `## [slug] Title` section headers
- `<!-- AUDIO -->` blocks

**Example:**
```markdown
---
version: 5
title: "My Presentation"
...
---

## Slides

| # | Slug | Title | Image | Section |
...

## [intro-slide] Introduction

![Slide](images/slide-01.png)

<!-- AUDIO -->
Welcome to the presentation...
<!-- /AUDIO -->
```

**Action:** Jump to Calibration mode. Content exists; validate and refine.

---

### Partial Talk Track (Draft in Progress)

**Indicators:**
- YAML frontmatter present
- Slides table may be incomplete
- Some `<!-- AUDIO -->` blocks missing
- Or audio blocks are placeholders

**Example:**
```markdown
---
version: 5
title: "My Presentation"
...
---

## Slides

| # | Slug | Title | Image | Section |
| 1 | intro | Intro | TBD | opening |
| 2 | main | Main Point | TBD | content |

## [intro] Intro

<!-- AUDIO -->
TODO: Write narration
<!-- /AUDIO -->
```

**Action:** Identify gaps. Interview for missing content. Draft to complete.

---

### Structured Outline (Headings + Bullets)

**Indicators:**
- `# Heading` hierarchy
- Bullet points under headings
- No YAML frontmatter
- No `<!-- AUDIO -->` blocks

**Example:**
```markdown
# Presentation Title

## Opening
- Hook: The 70% problem
- Introduce myself

## Problem
- Developers waste time on non-code
- Stats from Stack Overflow

## Solution
- AI-native approach
- Demo walkthrough

## Close
- Call to action
- Resources
```

**Action:**
1. Extract structure as section candidates
2. Map bullets to slide concepts
3. Interview for narration content
4. Build Talk Track from material

---

### Raw Notes (Unstructured)

**Indicators:**
- Loose bullet points or sentences
- No clear hierarchy
- Stream of consciousness
- Mixed topics without grouping

**Example:**
```
- AI tools are changing development
- 70% time on non-code stuff
- need to mention stack overflow data
- demo the workflow
- maybe talk about my team's experience
- call to action: try one thing
- probably 15 minutes?
```

**Action:** Full Discovery interview. Extract insights, then structure.

---

### PowerPoint/Keynote Text Export

**Indicators:**
- Slide number markers (`Slide 1:`, `[1]`, etc.)
- Minimal formatting
- Title followed by bullets per slide
- Speaker notes may be inline

**Example:**
```
Slide 1: Welcome
- AI-Native Development
- Jane Developer, TechConf 2026

Slide 2: The Problem
- 70% time on non-code
- Debugging, docs, context switching
- Speaker notes: Pause here

Slide 3: By the Numbers
...
```

**Action:**
1. Parse slide structure
2. Interview for audio (bullet points aren't narration)
3. Generate Talk Track with structure preserved

---

### Other Markdown Formats (Marp, Slidev, reveal.js)

**Indicators:**
- `---` horizontal rules as slide separators
- Special directives (`<!-- class: lead -->`, `::page::`)
- Format-specific frontmatter
- No `<!-- AUDIO -->` blocks

**Marp Example:**
```markdown
---
marp: true
theme: default
---

# Title Slide

---

# The Problem

- Bullet one
- Bullet two

---
```

**Slidev Example:**
```markdown
---
theme: seriph
---

# Welcome

---
layout: center
---

# Main Point
```

**Action:**
1. Extract slide boundaries
2. Map content to Talk Track structure
3. Interview for narration (these formats have no audio)
4. Convert to Talk Track v5

---

### Existing Presentation Files (Non-Markdown)

**Indicators:**
- User mentions: "I have a deck", "existing slides", "PowerPoint"
- Can't paste directly (binary format)

**Action:**
1. Ask for text export or copy-pasted content
2. Request slide images if available
3. Treat extracted content as appropriate format above

---

## Detection Algorithm

When content is pasted:

```
1. Check for YAML frontmatter
   → If `version: 5` or `version: 6` → Talk Track (native or partial)

2. Check for `<!-- AUDIO -->` blocks
   → If present → Talk Track (even if other parts missing)

3. Check for slide separator patterns
   → `---` alone on line → Other markdown format
   → `Slide N:` patterns → PowerPoint export

4. Check for heading hierarchy
   → `#` `##` `###` with bullets → Structured outline

5. Otherwise → Raw notes
```

---

## Response Templates

### Recognized Talk Track

> "I see a Talk Track v5 document with [N] slides. Let me run calibration to check format validity and narrative flow."

### Recognized Partial Talk Track

> "This is a Talk Track in progress. I see [N] slides defined, but [X] are missing audio blocks. Want me to help complete those?"

### Recognized Outline

> "I see a structured outline with [N] sections. Before I convert this to a Talk Track, let me ask a few questions about narration. What should the audience do differently after this talk?"

### Recognized PowerPoint Export

> "This looks like slide content from PowerPoint/Keynote. I can see the structure, but I'll need to develop the narration. Let's start: what's the key insight you want them to remember?"

### Recognized Raw Notes

> "These are great notes to work from. Let's structure this into a talk. First: who's the audience and what action should they take after your presentation?"

### Recognized Other Markdown

> "I see a [Marp/Slidev/reveal.js] presentation. I can convert the structure to Talk Track v5 and help you write the narration. The current format has slides but no audio—that's what we'll add."

---

## Edge Cases

### Mixed Formats

Content might combine patterns (e.g., outline with some attempted audio blocks).

**Action:** Acknowledge the hybrid state. Address strongest signal first.

### Empty or Minimal Input

User says "I want to present about X" with no content.

**Action:** Full Discovery mode. No format to detect.

### Image-Heavy Requests

User has slides but they're images, not text.

**Action:**
1. Ask for slide images
2. Interview for narration per slide
3. Build Talk Track with image references

---

## Format Conversion Notes

When converting from other formats:

### Structure Preservation
- Slide count and order typically preserved
- Headings → Slide titles
- Major sections → Talk Track sections

### Content Requirements
- Bullets are not narration (too choppy)
- Interview for spoken-word content
- Apply semantic tags during drafting

### Validation After Conversion
- Run Talk Track parser
- Check all slugs are valid
- Verify section IDs match

---

**See also:**
- `talk-track-v5-spec.md` - Target format specification
- SKILL.md - Import mode details
