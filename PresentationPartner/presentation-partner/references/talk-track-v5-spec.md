# Talk Track v5 Format Specification

The authoritative format for PresentationKit presentation content. This document describes the complete structure of a Talk Track v5 markdown file.

---

## Document Structure

A Talk Track v5 file consists of three main parts:

1. **YAML Frontmatter** - Metadata and configuration
2. **Slides Table** - Slide definitions and routing
3. **Slide Sections** - Individual slide content with audio blocks

```markdown
---
[YAML Frontmatter]
---

## Slides

[Slides Table]

## [slug] Title

[Slide Content]

---

## [slug] Title

[Slide Content]

...
```

---

## 1. YAML Frontmatter

Required and optional metadata for the presentation.

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `version` | `5` or `6` | Format version (use 5) |
| `title` | string | Presentation title |
| `author` | string | Presenter name |
| `target_minutes` | integer | Target duration in minutes |
| `sections` | array | Section definitions (see below) |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `subtitle` | string | Presentation subtitle |
| `event` | string | Event or venue name |
| `date` | string | Presentation date (YYYY-MM-DD) |
| `audio_voice` | string | Kokoro TTS voice ID (default: "af_heart") |
| `branding` | object | Visual theme configuration |

### Section Definition

Each section must have:

```yaml
sections:
  - id: opening       # lowercase-kebab-case identifier
    name: "Opening"   # Human-readable display name
    color: "#557373"  # Hex color for visual theming
```

### Branding Configuration

```yaml
branding:
  primary: "#2563eb"    # Primary brand color
  background: "#1e1e2e" # Background color
  text: "#f8fafc"       # Text color
```

### Complete Example

```yaml
---
version: 5
title: "AI-Native Software Development"
subtitle: "Building the Future of Code"
author: "Jane Developer"
event: "TechConf 2026"
date: "2026-03-15"
target_minutes: 15
audio_voice: "af_heart"

branding:
  primary: "#2563eb"
  background: "#1e1e2e"
  text: "#f8fafc"

sections:
  - id: opening
    name: "Opening"
    color: "#557373"
  - id: problem
    name: "The Problem"
    color: "#6B4C4C"
  - id: solution
    name: "Our Solution"
    color: "#4C6B5D"
  - id: closing
    name: "Closing"
    color: "#5D4C6B"
  - id: appendix
    name: "Appendix"
    color: "#666666"
---
```

---

## 2. Slides Table

A markdown table defining all slides. Must appear after frontmatter in a `## Slides` section.

### Required Columns

| Column | Description |
|--------|-------------|
| `#` | Slide position: "1", "2", etc. Use "A1", "A2" for appendix |
| `Slug` | Unique identifier in lowercase-kebab-case |
| `Title` | Human-readable slide title |
| `Image` | Filename of slide image (in images/ folder) |
| `Section` | Section ID (must match a defined section) |

### Example

```markdown
## Slides

| # | Slug | Title | Image | Section |
|---|------|-------|-------|---------|
| 1 | title-slide | Welcome to AI-Native Dev | slide-01-title.png | opening |
| 2 | hook-problem | The Current State | slide-02-hook.png | problem |
| 3 | evidence-stats | By the Numbers | slide-03-stats.png | problem |
| 4 | solution-intro | A New Approach | slide-04-solution.png | solution |
| 5 | demo-walkthrough | See It In Action | slide-05-demo.png | solution |
| 6 | call-to-action | Get Started Today | slide-06-cta.png | closing |
| A1 | appendix-resources | Additional Resources | slide-a1-resources.png | appendix |
```

### Slug Rules

- Must be unique within the document
- Must be lowercase-kebab-case: `title-slide`, `hook-problem`
- Used to link table rows to content sections

---

## 3. Slide Sections

Individual slide content. Each slide gets its own section.

### Section Header

```markdown
## [slug] Title
```

The slug in brackets must match a slug from the slides table.

### Section Components

Each slide section can contain:

1. **Image** - Slide visual
2. **Audio Block** - Narration text
3. **Speaker Notes** - Presenter-only context

### Image

```markdown
![Alt Text](images/slide-01-title.png)
```

Path is relative to the markdown file.

### Audio Block

The spoken narration for the slide:

```markdown
<!-- AUDIO -->
[HOOK] What if writing code felt less like fighting with syntax and more like having a conversation with a brilliant collaborator?

Welcome everyone. I'm Jane Developer.

[PAUSE:500]

This isn't about AI replacing developers. It's about AI amplifying what developers can do.
<!-- /AUDIO -->
```

- Must be wrapped in `<!-- AUDIO -->` and `<!-- /AUDIO -->` comments
- Can include semantic tags (see semantic-tags-guide.md)
- Plain text is the spoken narration

### Speaker Notes

Optional presenter context (not spoken):

```markdown
**Speaker Notes:**
- Make eye contact with the audience
- Pause for effect after the hook
- This slide usually gets questions
```

### Slide Separator

Use `---` between slides:

```markdown
---

## [next-slug] Next Title
```

### Complete Slide Example

```markdown
## [title-slide] Welcome to AI-Native Dev

![Title](images/slide-01-title.png)

<!-- AUDIO -->
[HOOK] What if writing code felt less like fighting with syntax and more like having a conversation with a brilliant collaborator?

Welcome everyone. I'm Jane Developer, and today we're going to explore how AI is fundamentally changing the way we build software.

[PAUSE:500]

This isn't about AI replacing developers. It's about AI amplifying what developers can do.
<!-- /AUDIO -->

**Speaker Notes:**
- Make eye contact with the audience
- Gauge the room's technical level
- Pause for effect after the hook

---
```

---

## Semantic Tags

Tags provide structure within audio blocks. See `semantic-tags-guide.md` for full reference.

### Available Tags

| Tag | Purpose |
|-----|---------|
| `[HOOK]` | Attention-grabbing opening |
| `[KEY_POINT]` | Core insight for the slide |
| `[EVIDENCE]` | Data or proof supporting a claim |
| `[STORY]` | Narrative or case study |
| `[TRANSITION]` | Connecting flow between sections |
| `[CALLBACK]` | Reference to earlier point |
| `[LANDING]` | Closing message or feeling |
| `[CTA]` | Call to action |
| `[PAUSE:ms]` | Timing pause in milliseconds |

### Tag Syntax

- Content tags: `[TAG] Content following the tag`
- Pause tag: `[PAUSE:500]` (value in milliseconds)

---

## Validation Rules

The parser enforces these rules:

### Frontmatter
- Must start with `---` on first line
- Must have all required fields
- `version` must be 5 or 6
- Each section must have id, name, color
- Color must be valid hex (#RGB or #RRGGBB)

### Slides Table
- Must have all 5 columns
- All slugs must be unique
- Section values must match defined section IDs
- Position must be valid (integer or A-prefix)

### Slide Sections
- Every slug in table must have a corresponding `## [slug]` section
- Each section should have an `<!-- AUDIO -->` block
- Slugs in headers must match table exactly

---

## Voice IDs

Available Kokoro TTS voices:

| Voice ID | Description |
|----------|-------------|
| `af_heart` | Default warm female voice |
| `af_bella` | Clear female voice |
| `am_adam` | Male voice |
| `am_michael` | Male voice |

---

## File Organization

Recommended structure for a talk track project:

```
my-presentation/
├── talk-track.md      # Main Talk Track v5 file
├── images/            # Slide images
│   ├── slide-01-title.png
│   ├── slide-02-hook.png
│   └── ...
└── public/            # Generated outputs
    ├── audio/         # Generated audio files
    └── html/          # Generated HTML
```

---

## Parser API

PresentationKit provides these parser functions:

```typescript
import { parseTalkTrack, validateTalkTrack } from '@leegonzales/presentation-kit';

// Parse markdown content
const talkTrack = parseTalkTrack(markdownContent);

// Validate without parsing
const errors = validateTalkTrack(markdownContent);
```

---

**See also:**
- `semantic-tags-guide.md` - When to use each tag
- `presentation-blocklist.md` - Patterns to avoid in audio
- CLAUDE.md (project root) - PresentationKit CLI commands
