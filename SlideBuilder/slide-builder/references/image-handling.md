# Image Handling Reference

This document defines how SlideBuilder processes image ratings from Essay-to-Speech and integrates with Nano Banana for image generation.

## Overview

Essay-to-Speech assesses images with a critical eye, rating them for presentation readiness. SlideBuilder consumes these ratings and takes appropriate action: copying, noting modifications, generating new images, or omitting entirely.

---

## 1. Image Ratings from Essay-to-Speech

Essay-to-Speech outputs image assessments in each section's `### Images` block:

```markdown
### Images
- `fig1-market-share.png`: USE - Clean pie chart, large labels, works as-is
- `fig2-scatter.png`: ADAPT - Good data but axis labels too small
- `fig3-table.png`: RECREATE - Important data, convert to horizontal bar chart
- `header-decorative.jpg`: SKIP - Decorative only, no presentation value
```

SlideBuilder parses this format to determine handling for each image.

---

## 2. Rating Definitions

| Rating | Meaning | SlideBuilder Action |
|--------|---------|---------------------|
| **USE** | Presentation-ready as-is | Copy directly to output `images/` |
| **ADAPT** | Good concept, needs modification | Note modification in output, flag for manual work |
| **RECREATE** | Valuable data, wrong format | Generate Nano Banana prompt for new image |
| **SKIP** | No presentation value | Omit entirely from output |

### Rating Distribution (Typical)

Academic and essay figures rarely arrive presentation-ready. Expect:
- **USE**: ~10-20% (diagrams, clean charts)
- **ADAPT**: ~40-50% (most common—needs label/crop/contrast work)
- **RECREATE**: ~20-30% (tables, dense plots, multi-panel figures)
- **SKIP**: ~10-20% (decorative, redundant, low-value)

---

## 3. USE Handling

Images rated USE are presentation-ready. Copy directly without modification.

### Workflow

```bash
# Direct copy to output
cp source/images/fig1-market-share.png output/images/fig1-market-share.png
```

### Slide Reference

Reference in slide markdown:

```markdown
## [slug] Market Distribution

![Market share breakdown by segment](images/fig1-market-share.png)

- Key insight from the data
- Supporting point
```

### What Qualifies as USE

- Clear, readable labels at projection distance
- High resolution (>1080p preferred)
- Simple composition (not cluttered)
- Self-explanatory without surrounding text
- Good contrast between elements

---

## 4. ADAPT Handling

Images rated ADAPT have good concepts but need modification before use.

### Workflow

SlideBuilder notes the required modifications but **does not perform edits**. The image is flagged for manual intervention.

### Output Format

```markdown
## [slug] Correlation Analysis

![Relationship between variables](images/fig2-scatter.png)

**Image Note**: `fig2-scatter.png` requires adaptation before final presentation:
- Enlarge axis labels for projection visibility
- Consider cropping to focus on main data cluster
- Add plain English axis titles (replace "ToM Score" with "Theory of Mind")
```

### Common ADAPT Modifications

| Issue | Solution |
|-------|----------|
| Small labels/text | Enlarge in image editor |
| Cluttered composition | Crop to focus area |
| Poor contrast | Adjust colors/brightness |
| Technical axis labels | Replace with plain English |
| Low resolution | Upscale or find higher-res source |
| Busy background | Simplify or remove |

### Manual Intervention Options

1. **Image Editor**: Photoshop, GIMP, Preview (macOS)
2. **Presentation Software**: PowerPoint/Keynote can crop, resize, overlay
3. **Nano Banana Edit**: `gemini_edit_image` for AI-assisted modifications

#### Using Nano Banana for ADAPT

For modifications AI can handle:

```
gemini_edit_image(
  imagePath="/path/to/fig2-scatter.png",
  instructions="Enlarge the axis labels to be clearly readable. Change 'ToM Score' to 'Theory of Mind' and 'κ' to 'AI Collaboration Score'. Maintain all data points as-is.",
  model="gemini-3-pro-image-preview"
)
```

**Limitations**: AI editing works for:
- Label resizing and repositioning
- Color/contrast adjustments
- Background simplification
- Cropping and reframing

AI editing struggles with:
- Adding precise numerical labels
- Maintaining exact data accuracy
- Complex multi-step modifications

When in doubt, use traditional image editing tools.

---

## 5. RECREATE Handling

Images rated RECREATE contain valuable data but need complete regeneration. This is where Nano Banana integration shines.

### Workflow

1. **Extract the insight**: What data/concept does the original communicate?
2. **Choose target format**: What visualization type works better?
3. **Generate Nano Banana prompt**: Craft detailed prompt for new image
4. **Generate and validate**: Create image, verify it communicates the insight

### Output Format

```markdown
## [slug] Performance Comparison

**Image Needed**: Bar chart showing adoption rates by industry

**Original**: `fig3-table.png` (data table with 8 rows)

**Nano Banana Prompt**:
> A clean horizontal bar chart showing 5 industries and their AI adoption percentages.
> Modern minimalist style, dark background (#0d0d0d), teal bars (#557373).
> Clear white labels on left (industry names), percentage values on right.
> No 3D effects, no gridlines. Professional data visualization.
>
> Data to visualize:
> - Technology: 78%
> - Finance: 65%
> - Healthcare: 52%
> - Manufacturing: 41%
> - Retail: 38%
>
> Aspect ratio: 16:9
>
> Avoid: decorative elements, gradients, shadows, text in bars

**Generation Command**:
```
gemini_generate_image(
  prompt="[prompt above]",
  aspectRatio="16:9",
  imageSize="4K"
)
```
```

### Common RECREATE Scenarios

| Source Format | Target Format | Prompt Focus |
|---------------|---------------|--------------|
| Data table | Horizontal bar chart | "horizontal bar chart showing..." |
| Dense scatter plot | Simplified trend line | "trend line visualization with..." |
| Complex flowchart | 3-4 step diagram | "simple process diagram with..." |
| Multi-panel figure | Single focused visual | "single visualization highlighting..." |
| Pie chart (many slices) | Bar chart or top-5 pie | "bar chart showing top 5..." |
| Screenshot (UI) | Clean mockup | "minimalist UI mockup showing..." |
| Academic diagram | Conceptual illustration | "clean conceptual diagram of..." |

### Prompt Crafting Guidelines

#### Structure

```
[Subject/Data] + [Style] + [Visual Details] + [Technical Specs] + [Avoid]
```

#### Key Elements

1. **Be specific about data**: Include actual values if known
2. **Specify style**: "modern minimalist", "corporate professional", "clean infographic"
3. **Define colors**: Use hex codes for brand consistency (`#557373` not "teal")
4. **Set aspect ratio**: 16:9 for slides, 1:1 for thumbnails
5. **List what to avoid**: "text, logos, decorative elements, 3D effects"

#### Example Prompts by Type

**Bar Chart**:
> A horizontal bar chart showing 5 project outcomes. Clean modern style, white background.
> Teal bars (#557373) with dark labels. Clear percentage labels on right side.
> No gridlines, no 3D effects. Aspect ratio 16:9.
> Avoid: decorative elements, gradients, shadows

**Process Diagram**:
> A 4-step linear process diagram showing AI implementation phases.
> Minimalist style, dark background (#0d0d0d), teal (#557373) connecting arrows.
> Each step as a rounded rectangle with white text label.
> Left to right flow. Clean, professional. Aspect ratio 16:9.
> Avoid: clip art, icons, complex decorations

**Comparison Visual**:
> Side-by-side comparison of two approaches: Traditional vs AI-Assisted.
> Split layout, left side in gray (#888), right side in teal (#557373).
> Clean icons representing each approach. Minimal text.
> Professional, modern style. Aspect ratio 16:9.
> Avoid: photographs, detailed illustrations

### Nano Banana MCP Integration

Use the `gemini_generate_image` tool:

```javascript
gemini_generate_image({
  prompt: "Your detailed prompt here...",
  aspectRatio: "16:9",
  imageSize: "4K",
  model: "gemini-3-pro-image-preview"
})
```

#### Parameters

| Parameter | Options | Use Case |
|-----------|---------|----------|
| `aspectRatio` | `16:9`, `1:1`, `9:16`, `4:3`, `3:4` | Match slide format |
| `imageSize` | `4K`, `2K`, `1K` | `4K` for final, `1K` for iteration |
| `model` | `gemini-3-pro-image-preview` (default) | Highest quality |

#### Iteration Strategy

1. **Start with 1K** for fast feedback
2. **Refine prompt** based on results
3. **Use `continue_editing`** for adjustments
4. **Final generation at 4K** when satisfied

```javascript
// Initial test
gemini_generate_image({ prompt: "...", imageSize: "1K" })

// Refine
continue_editing({ instructions: "Make the labels larger and bolder" })

// Final
gemini_generate_image({ prompt: "[refined prompt]", imageSize: "4K" })
```

---

## 6. SKIP Handling

Images rated SKIP provide no presentation value. Omit entirely.

### Workflow

Simply do not include in output. No reference, no placeholder, no note.

### What Gets SKIP

- Decorative headers/banners
- Stock photos with no informational content
- Redundant images (same data shown elsewhere)
- Low-quality images that can't be rescued
- Images that only make sense with extensive context

### When SKIP Might Be Wrong

If you notice a SKIP rating for an image that seems important:
- The image may contain data that wasn't recognized
- The context may have been misunderstood
- Consider upgrading to RECREATE with new visualization

---

## 7. Output Structure

### Directory Layout

```
output/
├── slides.md              # Main slide deck
├── speaker-notes.md       # Talk track by slide
└── images/
    ├── fig1-market-share.png     # USE - copied from source
    ├── fig2-scatter.png          # ADAPT - copied with notes
    ├── industry-adoption.png     # RECREATE - generated via Nano Banana
    └── ...
```

### Image Manifest

Include an image manifest in output for tracking:

```markdown
## Image Manifest

| Slide | Image | Rating | Action | Source |
|-------|-------|--------|--------|--------|
| 3 | fig1-market-share.png | USE | Copied | source/images/ |
| 5 | fig2-scatter.png | ADAPT | Copied with notes | source/images/ |
| 7 | industry-adoption.png | RECREATE | Generated | Nano Banana |
| - | header-decorative.jpg | SKIP | Omitted | - |
```

---

## 8. Slide Ideas Integration

Essay-to-Speech provides `### Slide Ideas` alongside image assessments. SlideBuilder uses both together.

### Example Input

```markdown
### Images
- `fig3-table.png`: RECREATE - Table needs conversion to bar chart

### Slide Ideas
- Key stat callout: "Theory of Mind → Better AI Collaboration"
- Recreate `fig3-table.png` as horizontal bar chart showing top 5
- Consider before/after comparison visual
```

### SlideBuilder Integration

1. **For RECREATE images**: Slide Ideas often specify the target format
   - "Recreate as horizontal bar chart" → Informs Nano Banana prompt

2. **For new visuals**: Slide Ideas may suggest images not in the original
   - "Key stat callout" → Generate typographic slide or callout image

3. **For slide structure**: Slide Ideas guide layout decisions
   - "Before/after comparison" → Two-column slide layout

### Generating Slide Idea Visuals

When Slide Ideas request visuals that don't map to existing images:

```markdown
**Suggested Visual**: Key stat callout

**Nano Banana Prompt**:
> A bold typographic slide showing the text "Theory of Mind → Better AI Collaboration"
> Large, confident sans-serif font. Arrow rendered as a stylized graphic element.
> Dark background (#0d0d0d), teal text (#557373), white arrow.
> Centered composition, plenty of breathing room.
>
> Aspect ratio: 16:9
>
> Avoid: decorative elements, photos, complex backgrounds
```

---

## 9. Quality Checklist

Before finalizing images:

### USE/ADAPT Images
- [ ] Readable from back of room (test at 50% zoom)
- [ ] High enough resolution (no pixelation at full screen)
- [ ] Clear labels in plain English
- [ ] Good contrast between elements
- [ ] ADAPT notes are actionable

### RECREATE Images
- [ ] Nano Banana prompt is specific and detailed
- [ ] Data/insight is accurately represented
- [ ] Style matches other slide visuals
- [ ] Generated at appropriate resolution
- [ ] Text rendering is accurate (if applicable)

### Overall
- [ ] Image manifest is complete
- [ ] No orphaned images (every image has a slide reference)
- [ ] Consistent visual style across deck
- [ ] SKIP decisions are justified

---

## 10. Troubleshooting

### Nano Banana Issues

| Problem | Solution |
|---------|----------|
| Text rendering garbled | Keep text minimal; add in Keynote/PowerPoint |
| Wrong aspect ratio | Specify `aspectRatio` explicitly |
| Style inconsistent | Include color hex codes in every prompt |
| Data visualization inaccurate | Provide explicit data values in prompt |
| Generation failing | Simplify prompt, reduce complexity |

### Image Quality Issues

| Problem | Solution |
|---------|----------|
| Pixelated at full screen | Generate at `4K`, or use higher-res source |
| Labels too small | Specify "large, bold labels" in prompt |
| Busy/cluttered result | Add "minimalist", "clean", "simple" to prompt |
| Colors don't match brand | Use hex codes, not color names |

### Workflow Issues

| Problem | Solution |
|---------|----------|
| Too many RECREATE items | Batch similar prompts, iterate on template |
| ADAPT notes unclear | Be specific: "enlarge to 24pt" not "make bigger" |
| Missing images in output | Check manifest against slide references |

---

## References

- `/NanoBananaSkill/nano-banana/SKILL.md` - Full Nano Banana skill documentation
- `/NanoBananaSkill/nano-banana/references/prompting-guide.md` - Detailed prompting techniques
- `/EssayToSpeech/essay-to-speech/SKILL.md` - Image assessment definitions
