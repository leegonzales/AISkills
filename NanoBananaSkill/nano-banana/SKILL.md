---
name: nano-banana
description: Generate and edit high-quality AI images using Google's Gemini 3 Pro Image model (Nano Banana Pro) via MCP. Use when user wants to create images, edit photos, generate graphics, or needs visual content with text rendering.
---

# Nano Banana Pro - AI Image Generation

Generate 4K images, edit photos, and create graphics with text rendering using Google's Gemini 3 Pro Image model via MCP.

## When to Use

Invoke when user:
- Asks to "generate an image" or "create a picture"
- Wants to "edit this photo" or "modify this image"
- Needs graphics with text (logos, infographics, diagrams)
- Requests "consistent characters" across multiple images
- Says "visualize this" or "make me a [visual thing]"

## Prerequisites

### 1. Gemini API Key

Get a free key from [Google AI Studio](https://aistudio.google.com/) → "Get API Key" → "Create API Key".

### 2. MCP Server Setup

**Recommended: NanoBanana-MCP** (Gemini 3 Pro, highest quality):

```bash
claude mcp add nano-banana --env GEMINI_API_KEY=your-key-here -- npx -y nanobanana-mcp
```

Or add to `~/.claude/settings.json` manually:

```json
{
  "mcpServers": {
    "nano-banana": {
      "command": "npx",
      "args": ["-y", "nanobanana-mcp"],
      "env": { "GEMINI_API_KEY": "your-api-key-here" }
    }
  }
}
```

**Alternative: nano-banana-mcp by ConechoAI** (Gemini 2.5 Flash — faster, lower cost): same config with `"args": ["nano-banana-mcp"]`.

## Available Tools

Once MCP is configured, these tools become available:

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| `gemini_generate_image` | Create new images from text prompts | `prompt`, `model`, `aspectRatio`, `imageSize` |
| `gemini_edit_image` | Modify existing images with instructions | `imagePath`, `instructions`, `model` |
| `continue_editing` | Refine the last generated image | `instructions` |
| `get_image_history` | List all generated images in session | - |
| `search_history` | Search all images (persistent) | `query`, `id`, `model`, `startDate`, `endDate`, `type`, `limit` |
| `get_image_by_id` | Get full details for a specific image | `imageId` |

### Model Options

| Model ID | Description |
|----------|-------------|
| `gemini-3-pro-image-preview` | **Default (Nano Banana Pro).** Highest quality, 4K, best text. Verify the live model ID via the nanobanana MCP — don't hardcode dated/preview suffixes. |
| `<flash-tier model>` | Faster generation, good quality, lower cost |
| `<alternative flash model>` | Alternative 2.0 model |

### Image Size (Gemini 3 only)

`4K` (final assets, print, marketing) · `2K` (balanced) · `1K` (fast iteration).

### Aspect Ratios

`16:9` slides/widescreen · `1:1` social · `9:16` stories/vertical · `4:3` presentations · `3:2` photo/print · `2:3` vertical posters.

### Advanced Capabilities

4K output up to 5632×3072 · accurate text rendering · multi-image composition (up to 14 refs) · character consistency (5+ images) · Google Search grounding · persistent history (`manifest.json`) · edit lineage tracking.

## Persistent History & Search

All generated images are tracked in `~/Documents/nanobanana_generated/manifest.json` with the prompt, model/settings, timestamp, and edit lineage.

```
search_history(query="sunset")
search_history(startDate="2026-06-01", endDate="2026-06-30")
search_history(model="gemini-3")
search_history(query="portrait", model="gemini-3-pro", limit=10)
get_image_by_id(imageId="generated-2026-06-13T20-12-45")
```

To regenerate/iterate on an old image: find the original prompt via `search_history`/`get_image_by_id`, copy and adjust it, then generate fresh.

## Critical Limitation: Logos and Text Cannot Be Generated Reliably

Generative models **cannot** reliably render specific logos, watermarks, or legible text — attempting it produces distorted/garbled results.

**Correct workflow for branded content:**
1. **Designate space** — in your prompt, specify a location for the logo (e.g., "...clean empty space in the bottom-right corner")
2. **Generate** the image without any logo or text
3. **Overlay manually** — composite the official logo file with an editor (ImageMagick, PowerPoint, Keynote, Canva, Figma)

This is the only way to ensure brand consistency. The Gemini-recreation watermark fallback below is unreliable.

## Prompting

Structure prompts as `[Subject] + [Style] + [Details] + [Technical Specs]`. Be specific (colors, materials, lighting, mood), name the style, add context, and use negative prompts (`...Avoid: text, logos, deformed hands`).

**Conceptual over prescriptive:** Specify the *what* and *why* (subject, concept, style, mood, constraints); let the model decide composition, placement, and visual hierarchy. Over-specifying pixel-level geometry fights the model's compositional instincts.

For the full toolkit — SCTD framework, style/lighting/composition/shot-type keyword tables, text-rendering tips, character-consistency recipes (`history:0`), quality keywords, and prompt troubleshooting — see `references/prompting-guide.md`. Copy-paste prompts by category are in `references/examples.md`.

## Precision Mode (JSON Prompting)

For high-stakes work requiring exact reproducibility (product shots, UI mockups, infographics, A/B iteration), use structured JSON schemas.

**Trigger phrases:** "I need exact control over...", "Create a product shot for [brand]...", "Generate a UI mockup...", "Make an infographic showing...", "I want to iterate on just the lighting...", "A/B test different versions..."

**Three schema types:**

| Type | Use Case | Key Controls |
|------|----------|--------------|
| `marketing_image` | Product shots, hero images | subject, props, lighting, camera, brand locks |
| `ui_builder` | App screens, dashboards | tokens, screens, containers, components |
| `diagram_spec` | Flowcharts, infographics | nodes, edges, data constraints |

**Translator workflow:** Describe (plain English) → Clarify (Claude asks for missing fields) → Generate (structured JSON) → Review → Render (JSON → precise prompt) → Iterate (modify specific fields, re-render).

**Scoped edits** are the key unlock — change one field (lighting, camera angle, background color, props) while everything else stays fixed, no full regeneration.

See `references/json-prompting.md` (full guide), `references/translator-prompt.md` (translator system prompt), `references/schemas/` (templates per type), and `references/examples-json.md` (filled examples).

## Workflow Examples

**Basic generation** — `gemini_generate_image(prompt="Futuristic cityscape at golden hour, glass skyscrapers, holographic ads, flying vehicles, photorealistic, 4K, cinematic lighting")`

**Photo editing** — `gemini_edit_image(imagePath=[user image], instructions="Transform to winter: snow on surfaces, frost on windows, visible breath, overcast sky, cool blue grading")`

**Iterative refinement** — `continue_editing(instructions="Adjust lighting to warmer tones, add golden-hour glow, softer shadows")`

## Output Management

Images save to `~/Documents/nanobanana_generated/` as `generated-[timestamp]-[id].png`.

## Security Notes

API keys live in local environment variables (never committed); use `.env` for project key management. Images are processed locally.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "API key invalid" | Verify key at [AI Studio](https://aistudio.google.com/) |
| "Rate limited" | Wait 60s, or upgrade API tier |
| "MCP not connected" | Restart Claude Code, check config syntax |
| "Image not saving" | Check write permissions on output directory |

Prompt-level issues (wrong style, bad composition, gibberish text, uncanny faces, color drift, inconsistent characters) are covered in `references/prompting-guide.md`.

## Integration

Works well with Artifacts Builder (images for HTML), Process Mapper (diagram visuals), and Research to Essay (illustrations).

---

## Branding (Post-Processing)

Branding is applied as a **post-processing composite step** — only when explicitly requested, never automatically.

### Catalyst AI Branding

Trigger phrases: "Add Catalyst branding", "Brand this image", "Add the logo", "Make this a Catalyst image".

**Logo assets** (in `assets/`): `catalyst-watermark-logo.png` (primary circular badge), `catalyst-logo-transparent.png` (wordmark + tagline), `catalyst-logo-compact.png` (wordmark only). For dark backgrounds use the white watermark variant.

**Option A — ImageMagick composite (recommended, pixel-perfect):**
```bash
# 1. Generate the base image, then composite the real logo:
magick /path/to/generated-image.png \
  \( /path/to/assets/catalyst-watermark-logo.png -resize 5% -alpha set -channel A -evaluate multiply 0.85 +channel \) \
  -gravity SouthEast -geometry +10+10 -composite \
  /path/to/output-branded.png
```
`-resize 5%` = logo at 5% of width · `-evaluate multiply 0.85` = 85% opacity · `-gravity SouthEast -geometry +10+10` = bottom-right with margin. The logo already includes the © symbol.

**Option B — Gemini recreation (fallback, approximate):** if ImageMagick is unavailable, `gemini_edit_image` can attempt to add a tiny circular badge (~4-5% width, '© CATALYST AI' top / 'SERVICES' bottom, waving robot center, ~85% opacity, lower-right). **Unreliable** — AI cannot consistently render specific logos; use Option A for professional results.

**Brand color palettes:** ask which to use — **Calm Luxury** (default; corporate/financial/tech; primary teal `#557373`) or **Sage & Sand** (wellness/sustainability/organic; primary sage green `#6B8E6B`). Full hex tables, usage guidance, and per-element color roles are in `references/branded-slides-catalyst.md` and `references/branded-infographic-catalyst.md`. The model may produce close-but-not-exact shades; correct in a photo editor for brand-perfect color.

### BetterUp AI Flight School (AFS) Branding

Trigger phrases: "AI Flight School slide", "AFS branded", "BetterUp slide", "Flight School branding". Full AFS design system: `references/branded-slides-afs.md`.

**Logo assets** (in `assets/`, 348x33px transparent ✦ AI Flight School BetterUp lockup): `afs-watermark-logo.png` (dark — for light/cream backgrounds) and `afs-watermark-logo-white.png` (white — for dark/atmospheric backgrounds).

```bash
# Pick the logo file matching the slide mode (white for dark backgrounds):
magick "input.png" \
  \( /path/to/assets/afs-watermark-logo.png \
     -resize 300x -alpha set -channel A -evaluate multiply 0.85 +channel \) \
  -gravity SouthEast -geometry +25+20 -composite \
  "output-branded.png"
```
`-resize 300x` = 300px wide (~15% of a 2000px slide) · `0.85` opacity · bottom-right with margin.

**AFS workflow:** generate the slide from the `references/branded-slides-afs.md` template → choose dark/light logo by slide mode → composite with ImageMagick → save to the project `images/` folder.

## Reference Files

- `references/prompting-guide.md` — full prompting techniques (SCTD, style/lighting/composition/shot-type tables, text rendering, character consistency, quality keywords, troubleshooting)
- `references/examples.md` — copy-paste sample prompts by category
- `references/json-prompting.md` — precision-mode JSON schema guide
- `references/translator-prompt.md` — JSON prompt translator system prompt
- `references/schemas/` — template JSON schemas (`marketing-image`, `ui-builder`, `diagram-spec`)
- `references/examples-json.md` — filled-out JSON examples
- **Explainer graphics (photorealistic):** `references/whiteboard-photo-prompt.md`, `references/chalkboard-prompt.md`, `references/napkin-sketch-prompt.md`
- **Explainer graphics (illustrated):** `references/sketchnote-prompt.md`, `references/mind-map-prompt.md`
- **Branded templates:** `references/branded-infographic-catalyst.md`, `references/branded-slides-catalyst.md`, `references/branded-slides-afs.md`, `references/lego-presentation-prompt.md`
- **Social media:** `references/imessage-conversation-prompt.md` (iPhone text-message screenshots, two-step method)
