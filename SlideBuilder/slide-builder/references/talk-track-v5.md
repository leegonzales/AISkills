# Talk Track v5 Format Specification

The Talk Track v5 format is the intermediate representation produced by slide-builder. It serves as the authoritative source for presentation content, bridging the gap between creative authoring and automated generation of HTML slides and audio narration.

## Format Overview

A Talk Track v5 file is a Markdown document with:

1. **YAML frontmatter** - Metadata and section definitions
2. **Slides table** - Index of all slides with routing information
3. **Slide content sections** - Individual slide definitions with images, audio scripts, and speaker notes

---

## 1. YAML Frontmatter

The document begins with YAML frontmatter enclosed in `---` delimiters.

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `version` | integer | Format version, must be `5` |
| `title` | string | Presentation title |
| `author` | string | Presenter name |
| `target_minutes` | integer | Target presentation duration |
| `sections` | array | Section definitions (see below) |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `subtitle` | string | Presentation subtitle |
| `event` | string | Event or venue name |
| `date` | string | Presentation date (YYYY-MM-DD) |
| `audio_voice` | string | Kokoro TTS voice ID (default: `af_heart`) |
| `branding` | string | Visual branding theme identifier |

### Section Definitions

Each section in the `sections` array defines a logical grouping of slides:

```yaml
sections:
  - id: opening
    name: "Opening"
    color: "#557373"
  - id: main-content
    name: "Main Content"
    color: "#6B4C4C"
  - id: appendix
    name: "Appendix"
    color: "#888888"
```

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique identifier (lowercase-kebab-case) |
| `name` | string | Human-readable display name |
| `color` | string | Hex color code for visual theming |

### Complete Frontmatter Example

```yaml
---
version: 5
title: "Becoming an AI Pilot"
subtitle: "AI Flight School & The 10,000 Pilots Mission"
author: "Lee Gonzales"
event: "Agile Denver Human-Centered AI Meetup"
date: "2026-01-21"
target_minutes: 45
audio_voice: "af_heart"
branding: "catalyst"

sections:
  - id: opening
    name: "Opening"
    color: "#557373"
  - id: urgency
    name: "Urgency"
    color: "#6B4C4C"
  - id: framework
    name: "Framework"
    color: "#557373"
  - id: closing
    name: "Closing"
    color: "#557373"
  - id: appendix
    name: "Appendix"
    color: "#888888"
---
```

---

## 2. Slides Table

Immediately after frontmatter, include a slides table under the `## Slides` heading.

```markdown
## Slides

| # | Slug | Title | Image | Section |
|---|------|-------|-------|---------|
| 1 | title | Title | slide-title.png | opening |
| 2 | maria | Maria Portrait | slide-maria-portrait.png | opening |
| 3 | metr | METR Benchmark | metr-benchmark.png | urgency |
```

### Column Definitions

| Column | Description |
|--------|-------------|
| `#` | Slide number. Main slides use integers (1, 2, 3...). Appendix slides use A-prefix (A1, A2, A3...) |
| `Slug` | Unique identifier in lowercase-kebab-case. Used for audio file naming (`{slug}.wav`) |
| `Title` | Human-readable slide title |
| `Image` | Filename of slide image in the `images/` folder |
| `Section` | Section ID from frontmatter (must match a defined section `id`) |

### Slide Numbering Convention

- **Main slides**: Sequential integers starting at 1
- **Appendix slides**: A-prefix with sequential integers (A1, A2, A3...)

The table provides a complete index enabling generators to:
- Build navigation structures
- Associate audio files with slides
- Apply section-based styling

---

## 3. Slide Content Sections

Each slide receives its own Markdown section following a consistent structure.

### Section Header Format

```markdown
## [slug] Title
```

The header combines the slug in brackets with the slide title. This enables both human readability and programmatic parsing.

### Complete Slide Structure

```markdown
## [slug] Title

![Alt text](images/filename.png)

<!-- AUDIO -->
Spoken narration content goes here.

Use semantic tags sparingly for emphasis and timing.
[PAUSE]
Continue with more narration.
<!-- /AUDIO -->

**Speaker Notes:**
Additional context, reminders, or talking points for the presenter.
These are not spoken aloud.
```

### Components

| Component | Required | Description |
|-----------|----------|-------------|
| Header | Yes | `## [slug] Title` format |
| Image | Yes | Markdown image reference to `images/` folder |
| Audio block | Yes | Content between `<!-- AUDIO -->` and `<!-- /AUDIO -->` delimiters |
| Speaker Notes | No | Additional presenter context under `**Speaker Notes:**` |

### Slide Separators

Use horizontal rules (`---`) between slides to provide clear visual separation:

```markdown
## [slide-one] First Slide
...content...

---

## [slide-two] Second Slide
...content...
```

---

## 4. Semantic Tags

Semantic tags provide structure and emphasis within audio blocks. Use sparingly for maximum effect.

### Content Tags

| Tag | Purpose | Example |
|-----|---------|---------|
| `[HOOK]` | Opening attention-grabber | `[HOOK] What if everything you know about AI is wrong?` |
| `[KEY_POINT]` | Core insight or main argument | `[KEY_POINT] Mindsets are malleable, not fixed.` |
| `[EVIDENCE]` | Data, statistics, or proof | `[EVIDENCE] Ninety-three percent of participants completed the program.` |
| `[STORY]` | Narrative or anecdote | `[STORY] Let me tell you about Maria...` |
| `[TRANSITION]` | Bridge between topics | `[TRANSITION] Now let's look at the framework.` |
| `[CALLBACK]` | Reference to earlier point | `[CALLBACK] Remember that widening gap we discussed?` |
| `[LANDING]` | Conclusion or summary | `[LANDING] That's what it means to be an AI Pilot.` |
| `[CTA]` | Call to action | `[CTA] Subscribe to my Substack to go deeper.` |

### Timing Tags

| Tag | Purpose | Example |
|-----|---------|---------|
| `[PAUSE]` | Standard breath/emphasis pause | `That's the real question. [PAUSE] Let me show you.` |
| `[PAUSE:ms]` | Specific pause duration in milliseconds | `[PAUSE:750]` for 750ms, `[PAUSE:3000]` for 3 seconds |

### Usage Guidelines

1. **Sparingly**: Not every sentence needs a tag. Tags highlight exceptional moments.
2. **Natural flow**: Tags should enhance natural speech rhythm, not interrupt it.
3. **Pauses for emphasis**: Use `[PAUSE]` after key revelations or before important statements.
4. **Longer pauses for reflection**: Use `[PAUSE:ms]` with higher values (2000-5000) when audience needs time to process or participate.

### Example with Semantic Tags

```markdown
<!-- AUDIO -->
[HOOK] I'm going to tell you upfront what I'm here to do tonight.

I'm here to enroll you in my mission of creating ten thousand AI Pilots.

[PAUSE]

[KEY_POINT] These aren't personality traits. They're muscles. They can be developed.

[EVIDENCE] BetterUp's coaching outcomes research quantified them: People who feel 'seen, heard, valued, and cared for' by their organization? Eighty-nine percent greater growth in agency.

[PAUSE:750]

[TRANSITION] So the question becomes: how do you actually build those muscles?
<!-- /AUDIO -->
```

---

## 5. Generator Compatibility

Talk Track v5 is designed as input for the presentation generation pipeline:

### generate-presentation.py

Consumes the talk track to produce:
- HTML/CSS presentation with slide transitions
- Navigation structure based on slides table
- Section-based color theming
- Embedded images

### generate-audio.py

Consumes the talk track to produce:
- Individual WAV files per slide (named `{slug}.wav`)
- Kokoro TTS synthesis using the specified `audio_voice`
- Semantic tag interpretation for pacing and emphasis
- Pause timing from `[PAUSE]` and `[PAUSE:ms]` tags

---

## 6. File Organization

A complete presentation directory structure:

```
presentation-name/
  talk-track.md          # Talk Track v5 file
  images/
    slide-title.png
    slide-content.png
    ...
  audio/                 # Generated by generate-audio.py
    title.wav
    content.wav
    ...
  presentation/          # Generated by generate-presentation.py
    index.html
    styles.css
    ...
```

---

## 7. Validation Checklist

Before processing, verify:

- [ ] Frontmatter `version` is `5`
- [ ] All required frontmatter fields present
- [ ] Each section in slides table has matching section `id` in frontmatter
- [ ] All slugs are unique and lowercase-kebab-case
- [ ] All image files exist in `images/` folder
- [ ] Each slide section header matches format `## [slug] Title`
- [ ] All audio blocks have matching open/close delimiters
- [ ] Semantic tags are properly formatted (brackets, no typos)

---

## 8. Best Practices

### Writing Audio Content

1. **Write for the ear**: Use contractions, conversational rhythm, and natural phrasing
2. **Spell out numbers**: "twenty twenty-seven" not "2027" for clearer TTS
3. **Avoid acronyms on first use**: Spell them out, then use the acronym
4. **One idea per paragraph**: Helps with pacing and comprehension
5. **Signal transitions**: Help listeners follow the structure

### Structuring Presentations

1. **Keep sections balanced**: Similar number of slides per section
2. **Use appendix strategically**: Content that supports but isn't essential to the main flow
3. **Match colors to mood**: Use section colors to signal tone shifts
4. **Order slides table correctly**: It defines presentation sequence

### Semantic Tag Strategy

1. **Hooks at section starts**: Draw attention when transitioning topics
2. **Key points for retention**: Mark what you want remembered
3. **Evidence for credibility**: Highlight data and research
4. **Pauses for impact**: Let important moments land
