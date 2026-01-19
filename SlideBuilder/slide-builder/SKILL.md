---
name: slide-builder
description: Transform essay-to-speech output into complete presentations with multiple output formats. Use when converting talk tracks to slides, generating presentation decks, or creating video-ready content from spoken word material.
---

# Slide Builder

Transform essay-to-speech output into complete, presentation-ready slide decks with multiple output format support (HTML, Remotion video, PowerPoint).

## When to Use

Invoke when user:
- Has essay-to-speech output and wants slides
- Says "create slides from this talk track"
- Needs to "build a presentation" from spoken content
- Wants to convert a talk track to video format
- Uses `/slide-builder` command
- Asks for "presentation slides" from transformed essay content

## Prerequisites

**Input required:** Output from the `essay-to-speech` skill containing:
- `### Original` sections (verbatim essay text)
- `### Talk Track` sections with semantic tags
- `### Images` sections with ratings (USE/ADAPT/RECREATE/SKIP)
- `### Slide Ideas` suggestions

## Core Process

### 1. Parse Essay-to-Speech Output

Extract structured data from each section:

```
Section → {
  title: string,
  original: string,
  talkTrack: TaggedContent[],
  images: ImageAssessment[],
  slideIdeas: string[]
}
```

**Semantic tags to identify:**
- `[HOOK]` - Opening attention-grabber → Title/hook slide
- `[KEY_POINT]` - Core argument → Statement slide
- `[EVIDENCE]` - Data/proof → Data visualization slide
- `[STORY]` - Narrative → Story/quote slide
- `[TRANSITION]` - Bridge → Section divider or no slide
- `[CALLBACK]` - Reference → Recap element
- `[LANDING]` - Conclusion → Summary slide
- `[CTA]` - Call to action → Action slide

### 2. Plan Slide Deck

Map semantic tags to slides:

| Tag | Slide Type | Typical Visual |
|-----|------------|----------------|
| `[HOOK]` | Title/Opening | Bold statement, striking image |
| `[KEY_POINT]` | Statement | Single phrase, minimal graphic |
| `[EVIDENCE]` | Data | Chart, statistic callout, comparison |
| `[STORY]` | Story | Photo, quote attribution, timeline |
| `[TRANSITION]` | Divider (optional) | Section title, progress indicator |
| `[CALLBACK]` | Recap | Reference to earlier slide |
| `[LANDING]` | Summary | Key takeaways, visual recap |
| `[CTA]` | Action | Contact info, next steps, QR code |

**Slide count heuristic:**
- 1-2 slides per `[KEY_POINT]`
- 1 slide per `[EVIDENCE]` block
- Section dividers are optional (skip for tight decks)
- Target: 1 slide per 45-60 seconds of speaking

### 3. Handle Images

Process image assessments from essay-to-speech:

| Rating | Action |
|--------|--------|
| `USE` | Include directly in slide |
| `ADAPT` | Note modifications needed (enlarge labels, crop, simplify) |
| `RECREATE` | Generate Nano Banana prompt for new visual |
| `SKIP` | Do not include |

**For RECREATE images:**
Generate a Nano Banana prompt following these guidelines:
- 16:9 aspect ratio for slides
- Clear, simple compositions
- Large readable text/labels
- Brand colors if specified

Example RECREATE prompt:
```
"Clean horizontal bar chart comparing 5 items, minimal style,
white background, teal (#557373) bars, large bold labels,
no gridlines, presentation-ready, 16:9 aspect ratio"
```

### 4. Generate Output

## Output Format: Talk Track v5

The primary output format for presentations.

### Structure

```yaml
---
version: 5
title: "Presentation Title"
subtitle: "Optional Subtitle"
author: "Presenter Name"
date: "2025-01-15"
target_minutes: 15
audio_voice: "af_heart"
brand:
  primary: "#557373"
  background: "#F2EFEA"
  text: "#0D0D0D"
sections:
  - id: opening
    name: "Opening"
    color: "#557373"
  - id: problem
    name: "The Problem"
    color: "#6B8E6B"
  - id: solution
    name: "The Solution"
    color: "#C4785A"
  - id: closing
    name: "Closing"
    color: "#557373"
---

## Slides

| # | Slug | Title | Image | Section |
|---|------|-------|-------|---------|
| 1 | hook | The Question | hook.png | opening |
| 2 | problem-1 | What's Broken | problem-chart.png | problem |
| 3 | evidence | The Data | evidence.png | problem |
| 4 | solution | A New Approach | solution.png | solution |
| 5 | action | Your Next Step | cta.png | closing |

---

## [hook] The Question

![The Question](images/hook.png)

<!-- AUDIO -->
[HOOK] Let me ask you something that might change how you think about this entire problem...

What if everything you believed was based on outdated assumptions?
<!-- /AUDIO -->

**Speaker Notes:**
- Pause after the question
- Make eye contact with audience
- Let the tension build

---

## [problem-1] What's Broken

![What's Broken](images/problem-chart.png)

<!-- AUDIO -->
[KEY_POINT] The current approach fails in three critical ways.

[EVIDENCE] First, efficiency drops by 40% when teams scale past 10 people. Second, communication overhead grows exponentially. Third, institutional knowledge gets siloed.
<!-- /AUDIO -->

**Speaker Notes:**
- Point to chart as you mention each stat
- Emphasize "exponentially"

---
```

### Format Rules

1. **YAML Frontmatter** - Metadata, timing, voice, sections
2. **Slide Index Table** - Quick reference for all slides
3. **Individual Slides** - Each with:
   - H2 header: `## [slug] Title`
   - Image reference (if applicable)
   - `<!-- AUDIO -->` block with talk track
   - `**Speaker Notes:**` for presenter context

### Audio Block Format

Content between `<!-- AUDIO -->` and `<!-- /AUDIO -->` is:
- Read aloud by TTS engines
- Preserves semantic tags for timing hints
- Excludes speaker notes and visual descriptions

### Timing Calculation

Estimate duration based on word count:
- Speaking rate: 130-150 words/minute
- Add 2-3 seconds per slide transition
- Add pause time for `[PAUSE]` markers

## Voice Options

### Development: Kokoro TTS (via claude-speak)

- **Local, free, fast iteration**
- Invoke: `/claude-speak` skill with audio block text
- Voice: `af_heart` (default) or specify in frontmatter
- Output: Local audio file per slide or full presentation

### Production: ElevenLabs v3

- **Word-level timestamps** for precise video sync
- **Higher quality** for final distribution
- Requires ElevenLabs API key
- Output: Audio + JSON timing data

See `references/voice-options.md` for full configuration.

## Alternative Output Formats

### HTML Slide Engine

Static HTML presentation with:
- Keyboard navigation (arrows, space)
- Speaker notes toggle (N key)
- Timer display
- Print to PDF support

See `references/html-engine.md` for template.

### Remotion Video

Export to React-based video for:
- YouTube/social publishing
- Embedded animations
- Precise audio sync with timestamps

See `references/remotion-video.md` for project setup.

## Workflow

### Standard Flow

```
essay-to-speech output
        ↓
   [slide-builder]
        ↓
   Talk Track v5 (.md)
        ↓
   ┌─────┼─────┐
   ↓     ↓     ↓
  HTML  Video  Audio
```

### Quick Start

1. **Input:** Provide essay-to-speech output
2. **Review plan:** Claude proposes slide structure
3. **Confirm or adjust:** Modify slide count, sections, visuals
4. **Generate:** Claude outputs Talk Track v5 markdown
5. **Images:** Generate RECREATE images via Nano Banana
6. **Audio:** Generate voice via claude-speak or ElevenLabs
7. **Render:** Export to HTML, video, or both

## Best Practices

### Slide Design Principles

1. **One idea per slide** - Split dense content
2. **6 words or less** on screen - The rest is spoken
3. **High contrast** - Readable from back row
4. **Consistent visual language** - Same fonts, colors, style
5. **Images > bullet points** - Visual storytelling wins

### Talk Track Integration

1. **Audio is king** - Slides support speech, not replace it
2. **Match pacing** - Visual changes align with spoken transitions
3. **Build reveals** - Don't show everything at once
4. **Breathing room** - Not every sentence needs a slide change

### Image Guidance

For RECREATE images, always specify:
- Aspect ratio (16:9 for slides)
- Style (clean, minimal, professional)
- Key data to visualize
- What to AVOID (clutter, small text, decorative elements)

## What This Skill Does NOT Do

- Edit or create original essay content (that's essay-to-speech)
- Design custom graphics (use Nano Banana for that)
- Record actual audio (use claude-speak or ElevenLabs)
- Render final video (use Remotion or video editor)
- Create PowerPoint/Keynote files directly (exports markdown)

## Integration

**Upstream:**
- `essay-to-speech` - Provides structured input

**Downstream:**
- `nano-banana` - Generates RECREATE images
- `claude-speak` - Generates audio narration
- `veo3-prompter` - Creates video segments (if needed)

## References

- `references/talk-track-v5.md` - Complete format specification
- `references/html-engine.md` - Static HTML slide player
- `references/remotion-video.md` - React video export setup
- `references/voice-options.md` - TTS configuration and comparison
- `references/image-handling.md` - Full image processing workflow
- `references/examples.md` - Complete input→output examples
