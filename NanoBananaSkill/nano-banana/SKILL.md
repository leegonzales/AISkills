---
name: nano-banana
description: Generate and edit high-quality AI images using Google's Gemini 3 Pro Image model (Nano Banana Pro) via MCP. Use when user wants to create images, edit photos, generate graphics, or needs visual content with text rendering.
---

# Nano Banana Pro - AI Image Generation

Generate stunning 4K images, edit photos, and create graphics with perfect text rendering using Google's latest Gemini 3 Pro Image model via MCP.

## When to Use

Invoke when user:
- Asks to "generate an image" or "create a picture"
- Wants to "edit this photo" or "modify this image"
- Needs graphics with text (logos, infographics, diagrams)
- Requests "consistent characters" across multiple images
- Says "visualize this" or "make me a [visual thing]"

## Prerequisites

### 1. Gemini API Key

Get a free API key from [Google AI Studio](https://aistudio.google.com/):
1. Sign in with Google account
2. Click "Get API Key" → "Create API Key"
3. Copy and save securely

### 2. MCP Server Setup

**Recommended: NanoBanana-MCP** (uses Gemini 3 Pro for highest quality)

```bash
# Quick install via Claude Code CLI
claude mcp add nano-banana --env GEMINI_API_KEY=your-key-here -- npx -y nanobanana-mcp
```

Or add to `~/.claude/settings.json` manually:

```json
{
  "mcpServers": {
    "nano-banana": {
      "command": "npx",
      "args": ["-y", "nanobanana-mcp"],
      "env": {
        "GEMINI_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

**Alternative: Nano-Banana-MCP by ConechoAI** (Gemini 2.5 Flash - faster, lower cost)

```json
{
  "mcpServers": {
    "nano-banana": {
      "command": "npx",
      "args": ["nano-banana-mcp"],
      "env": {
        "GEMINI_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Available Tools

Once MCP is configured, these tools become available:

### Core Tools

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| `gemini_generate_image` | Create new images from text prompts | `prompt`, `model`, `aspectRatio`, `imageSize` |
| `gemini_edit_image` | Modify existing images with instructions | `imagePath`, `instructions`, `model` |
| `continue_editing` | Refine the last generated image | `instructions` |
| `get_image_history` | List all generated images in session | - |
| `search_history` | Search all images (persistent) by prompt, date, model | `query`, `id`, `model`, `startDate`, `endDate`, `type`, `limit` |
| `get_image_by_id` | Get full details for a specific image | `imageId` |

### Model Options

| Model ID | Description |
|----------|-------------|
| `gemini-3-pro-image-preview` | **Default.** Highest quality, 4K support, best text rendering |
| `gemini-2.0-flash-exp` | Faster generation, good quality, lower cost |
| `gemini-2.0-flash-preview-image-generation` | Alternative 2.0 model |

### Image Size (Gemini 3 only)

| Size | Use Case |
|------|----------|
| `4K` | Final assets, print, marketing materials |
| `2K` | Balanced quality and speed |
| `1K` | Fast iteration, prototyping |

### Advanced Features

| Feature | Capability |
|---------|------------|
| **4K Output** | Up to 5632×3072 pixels |
| **Text Rendering** | Accurate text in images (signs, labels, UI) |
| **Multi-Image Composition** | Combine up to 14 reference images |
| **Character Consistency** | Maintain same character across 5+ images |
| **Google Search Grounding** | Real-world accurate imagery |
| **Persistent History** | All prompts and metadata saved to manifest.json |
| **Edit Lineage Tracking** | Track parent-child relationships across edits |

## Persistent History & Search

All generated images are tracked in `~/Documents/nanobanana_generated/manifest.json` with full metadata including:
- Original prompt used
- Model and settings (aspectRatio, imageSize)
- Timestamp
- Edit lineage (which image was this edited from)

### Searching Past Images

Find images from previous sessions using `search_history`:

```
# Search by prompt text
search_history(query="sunset")

# Search by date range
search_history(startDate="2024-12-01", endDate="2024-12-31")

# Search by model
search_history(model="gemini-3")

# Combined filters
search_history(query="portrait", model="gemini-3-pro", limit=10)
```

### Getting Image Details

Retrieve full metadata for any image by ID:

```
get_image_by_id(imageId="generated-2024-12-13T20-12-45")
```

Returns:
- Full prompt used
- All generation settings
- Edit lineage (ancestors and children)
- File existence check

### Regenerating Images

To recreate or iterate on an old image:
1. Use `search_history` or `get_image_by_id` to find the original prompt
2. Copy the prompt and adjust as needed
3. Generate a new image with the same or modified prompt

## Critical Limitations

### Logos and Text Cannot Be Generated Reliably

Generative models **cannot** reliably render specific logos, watermarks, or legible text. Attempting to do so will produce distorted, incorrect, or garbled results.

**Correct Workflow for Branded Content:**
1. **Designate Space:** In your prompt, specify a location for the logo (e.g., "...with clean empty space in the bottom-right corner")
2. **Generate Image:** Generate the image without any logo or text
3. **Overlay Manually:** Use an image editor (PowerPoint, Keynote, Canva, Figma) to place the official logo file onto the generated image

This is the only way to ensure brand consistency. The watermark workflow documented below attempts to have Gemini recreate the logo from description—results will vary and may require manual correction.

---

## Prompting Best Practices

### Structure Your Prompts

```
[Subject] + [Style] + [Details] + [Technical Specs]
```

**Example:**
> "A cozy coffee shop interior, watercolor illustration style, warm lighting, wooden furniture, steaming cup on table, 4K resolution, soft morning light through windows"

### For Best Results

1. **Be Specific** - Include colors, materials, lighting, mood
2. **Specify Style** - "photorealistic", "oil painting", "3D render", "anime"
3. **Add Context** - Time of day, weather, setting
4. **Request Resolution** - "4K", "high resolution", "detailed"

### Use Negative Prompts

Tell the model what to **exclude** for better results. Add to your prompt:

> "...Avoid: [unwanted elements]"

**Common negative prompts:**
- **For cleaner images:** "Avoid: text, words, logos, watermarks, signatures"
- **For better quality:** "Avoid: blurry, low resolution, pixelated, grainy"
- **For realistic people:** "Avoid: deformed hands, extra fingers, distorted faces"
- **For professional look:** "Avoid: cartoonish, amateur, clipart style"

**Example with negative prompt:**
> "A professional headshot of a business executive in a modern office, natural lighting, shallow depth of field. Avoid: text, logos, deformed features, overly stylized"

### Specify Aspect Ratio

Match aspect ratio to your use case:

| Ratio | Use Case |
|-------|----------|
| `16:9` | Slides, presentations, widescreen |
| `1:1` | Social media, profile images |
| `9:16` | Stories, mobile-first, vertical video |
| `4:3` | Traditional presentations |
| `3:2` | Photography, print |
| `2:3` | Vertical infographics, posters |

## Precision Mode (JSON Prompting)

For high-stakes work requiring exact reproducibility, use structured JSON schemas.

### When to Activate

Trigger phrases:
- "I need exact control over..."
- "Create a product shot for [brand]..."
- "Generate a UI mockup..."
- "Make an infographic showing..."
- "I want to iterate on just the lighting..."
- "A/B test different versions..."

### Three Schema Types

| Type | Use Case | Key Controls |
|------|----------|--------------|
| `marketing_image` | Product shots, hero images | subject, props, lighting, camera, brand locks |
| `ui_builder` | App screens, dashboards | tokens, screens, containers, components |
| `diagram_spec` | Flowcharts, infographics | nodes, edges, data constraints |

### The Translator Workflow

1. **Describe** - User explains what they want in plain English
2. **Clarify** - Claude asks targeted questions for missing fields
3. **Generate** - Claude outputs structured JSON schema
4. **Review** - User checks key fields match intent
5. **Render** - JSON converts to precise prompt for Nano Banana Pro
6. **Iterate** - Modify specific fields, re-render (scoped changes)

### Example: Product Shot

**User:** "I need a hero shot for Aurora Lime seltzer"

**Claude asks:** "For the Aurora Lime hero shot:
1. Can size? (12oz standard?)
2. Props? (lime slices, ice, condensation?)
3. Background style? (solid color, gradient, bokeh?)
4. Lighting mood? (bright/refreshing or moody/premium?)"

**Result:** Structured JSON with exact specifications that can be iterated field-by-field.

### Scoped Edits (The Key Unlock)

JSON enables changing ONE thing without regenerating everything:

| Change | What Stays Fixed |
|--------|------------------|
| Swap lighting direction | Subject, props, background |
| Try different camera angle | Lighting, props, environment |
| Change background color | Subject geometry, lighting setup |
| Add/remove props | Everything else |

### Reference Docs

- `references/json-prompting.md` - Full JSON prompting guide
- `references/translator-prompt.md` - Translator system prompt
- `references/schemas/` - Template schemas for each type
- `references/examples-json.md` - Filled-out examples

### Text in Images

Nano Banana Pro excels at text rendering:
> "A vintage movie poster for 'COSMIC ADVENTURE' with bold retro typography, starfield background, astronaut silhouette, 1970s sci-fi aesthetic"

### Character Consistency

For consistent characters across images:
1. Generate initial character with detailed description
2. Use `history:0` reference in subsequent prompts
3. Describe scene changes while referencing original

```
First: "A young woman with red curly hair, freckles, green eyes, wearing a blue jacket"
Then: "The same woman from history:0, now sitting at a café, reading a book"
```

## Workflow Examples

### Basic Image Generation

```
User: "Create an image of a futuristic city at sunset"

Claude uses: gemini_generate_image
Prompt: "Futuristic cityscape at golden hour sunset, towering glass skyscrapers with holographic advertisements, flying vehicles, warm orange and purple sky, photorealistic, 4K resolution, cinematic lighting"
```

### Photo Editing

```
User: "Edit this photo to make it look like winter"

Claude uses: gemini_edit_image
Input: [user's image path]
Instructions: "Transform to winter scene: add snow on ground and surfaces, frost on windows, visible breath, overcast sky, cool blue color grading"
```

### Iterative Refinement

```
User: "Make the lighting warmer"

Claude uses: continue_editing
Instructions: "Adjust lighting to warmer tones, add golden hour glow, enhance orange/yellow highlights, softer shadows"
```

## Output Management

Images save to: `~/Documents/nanobanana_generated/`

Naming format: `generated-[timestamp]-[id].png`

## Security Notes

- API keys stored locally in environment variables
- Never committed to version control
- Images processed locally, not stored on external servers
- Use `.env` files for key management in projects

## Model Comparison

| Model | Speed | Quality | Cost | Best For |
|-------|-------|---------|------|----------|
| `gemini-3-pro-image-preview` | Slower | Highest (4K) | Higher | Final assets, print, marketing |
| `gemini-2.0-flash-exp` | Fast | Good | Lower | Prototyping, iteration, drafts |

## Prompting Philosophy: Conceptual Over Prescriptive

**Core insight:** Image models perform better with conceptual guidance than pixel-level prescriptions.

### What to Specify
- **Subject:** What/who is in the image
- **Concept:** The idea or feeling to convey
- **Style:** Aesthetic direction (photographic, illustration, etc.)
- **Mood:** The emotional tone
- **Constraints:** Color palette, format, what to avoid

### What to Let the Model Decide
- Exact composition and framing
- Element placement and proportions
- Decorative details
- How to achieve visual hierarchy

### Example

❌ **Over-prescribed (fights the model):**
> "Create an image with a woman in the exact center, standing at a 15-degree angle, with a window to her left taking up 30% of the frame, warm light at 45 degrees from upper right..."

✅ **Conceptual (lets the model compose):**
> "Professional woman in a modern office at golden hour. Contemplative mood, success and ambition. Natural warmth, depth through foreground/background blur."

### Why This Works
The model has internalized millions of well-composed images. Over-specifying fights its compositional instincts. Provide the *what* and *why*; let it figure out the *how*.

---

## Advanced Techniques

### Shot Types (Photographic Control)

Use photography terms for precise framing:

| Shot Type | Effect |
|-----------|--------|
| `macro shot` | Extreme close-up, fine details |
| `wide angle shot` | Expansive view, dramatic perspective |
| `aerial view` / `drone shot` | Top-down perspective |
| `low-angle shot` | Looking up, imposing feel |
| `portrait framing` | Head/shoulders, subject focus |
| `dutch angle` | Tilted, dynamic tension |

### Reference Artistic Styles

Guide the model with style references:

> "...in the style of Ansel Adams" (dramatic B&W landscapes)
> "...as a ukiyo-e woodblock print" (Japanese art)
> "...bauhaus design aesthetic" (geometric, modernist)
> "...vaporwave aesthetic" (80s retrowave)
> "...Studio Ghibli animation style" (anime, painterly)

### Lighting Control

Specify lighting for mood and dimension:

| Lighting | Effect |
|----------|--------|
| `golden hour` | Warm, soft, magical |
| `harsh midday sun` | High contrast, strong shadows |
| `overcast / diffused` | Soft, even, no harsh shadows |
| `rim lighting` | Edge glow, dramatic separation |
| `studio lighting` | Professional, controlled |
| `neon lighting` | Cyberpunk, vibrant colors |

### Iteration Strategy

1. **Start simple** - Subject + style only
2. **Generate 2-3 versions** - Assess what works
3. **Add one element at a time** - Lighting, then props, then environment
4. **Use continue_editing** - Refine incrementally
5. **Save good seeds** - If model provides seed, reuse for variations

---

## Common Pitfalls

### The Uncanny Valley

**Problem:** Photorealistic people with strange faces or deformed hands

**Solutions:**
- Use illustration styles instead: `vector art`, `3D render`, `anime style`
- Add to negative prompt: "Avoid: deformed hands, extra fingers, distorted faces"
- Crop or frame to avoid hands when possible

### Starting Too Complex

**Problem:** Long, detailed prompts produce confused results

**Solution:** Build iteratively:
```
❌ Bad: "A professional woman with red hair in a blue suit standing in a modern office
with glass walls and city views at sunset with warm lighting and bokeh..."

✅ Better:
1. First: "Professional woman, business portrait, studio lighting"
2. Then add: "...in modern office environment"
3. Then add: "...warm sunset lighting through windows"
```

### Expecting Readable Text

**Problem:** Generated text is gibberish or distorted

**Solution:** Never rely on generated text. Either:
- Design the image without text
- Leave space and add text in an editor afterward
- Use the image as a background and overlay text

### Color Drift in Branded Content

**Problem:** Brand colors come out slightly different

**Solutions:**
- Include hex codes in prompt: "using teal (#557373) as the primary color"
- Accept minor drift and correct in post-processing
- For exact colors, use solid color backgrounds and composite

### Inconsistent Characters

**Problem:** Same character looks different across images

**Solutions:**
- Use `history:0` reference in subsequent prompts
- Be extremely detailed in first character description
- Include distinctive features: hair color, eye color, clothing, accessories
- Consider illustration styles which are more consistent

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "API key invalid" | Verify key at [AI Studio](https://aistudio.google.com/) |
| "Rate limited" | Wait 60s, or upgrade API tier |
| "MCP not connected" | Restart Claude Code, check config syntax |
| "Image not saving" | Check write permissions on output directory |

## Integration

Works well with:
- **Artifacts Builder** - Generate images for HTML artifacts
- **Process Mapper** - Create diagram visuals
- **Research to Essay** - Add illustrations to content

## References

- `references/prompting-guide.md` - Detailed prompting techniques
- `references/examples.md` - Sample prompts by category
- `references/json-prompting.md` - Precision mode with JSON schemas
- `references/translator-prompt.md` - JSON prompt translator system

### Explainer Graphics (Photorealistic)

- `references/whiteboard-photo-prompt.md` - Professor whiteboard photos for educational content
- `references/chalkboard-prompt.md` - Academic chalkboard with vintage gravitas
- `references/napkin-sketch-prompt.md` - Back-of-napkin startup/pitch sketches

### Explainer Graphics (Illustrated)

- `references/sketchnote-prompt.md` - Visual note summaries for books, talks, concepts
- `references/mind-map-prompt.md` - Radial brainstorming and topic organization

### Branded Templates

- `references/branded-infographic-catalyst.md` - Catalyst AI Services infographics (Sage & Sand)
- `references/branded-slides-catalyst.md` - Catalyst AI Services presentation slides
- `references/lego-presentation-prompt.md` - Lego minifigure presentation slides (photorealistic toy photography)

### Social Media Templates

- `references/imessage-conversation-prompt.md` - iPhone text message screenshots (two-step method for accurate text)

## Catalyst AI Branding (Post-Processing)

Add Catalyst AI branding to ANY generated image.

### When to Use

**Only apply branding when explicitly requested.** Trigger phrases:
- "Add Catalyst branding"
- "Brand this image"
- "Add the logo"
- "Make this a Catalyst image"

**Do NOT** automatically add branding to every generated image. Wait for user to request it.

### Logo Assets

Located in `assets/`:
- `catalyst-watermark-logo.png` - **Primary watermark** - circular badge with "CATALYST AI / SERVICES" and waving robot
- `catalyst-logo-transparent.png` - Full wordmark logo with tagline (for headers)
- `catalyst-logo-compact.png` - Wordmark only, no tagline (alternate)

### Workflow Options

#### Option A: ImageMagick Composite (Recommended - Exact Logo)

Use command-line tools to overlay the actual logo file. This produces pixel-perfect results.

**Step 1: Generate the base image**
```
gemini_generate_image(prompt="Your image description...")
```

**Step 2: Composite logo with ImageMagick**
```bash
# Add branded logo to lower-right corner
magick /path/to/generated-image.png \
  \( /path/to/assets/catalyst-watermark-logo.png -resize 5% -alpha set -channel A -evaluate multiply 0.85 +channel \) \
  -gravity SouthEast -geometry +25+25 -composite \
  /path/to/output-branded.png
```

**Parameters explained:**
- `-resize 5%`: Logo at 5% of image width (subtle but visible)
- `-evaluate multiply 0.85`: 85% opacity for subtlety
- `-gravity SouthEast`: Logo in bottom-right corner
- `-geometry +25+25`: Margin from edge

#### Option B: Gemini Recreation (Fallback - Approximate)

If ImageMagick is unavailable, Gemini can attempt to recreate the logo. **Results will vary** - the logo may be distorted or incorrect.

```
gemini_edit_image(
  imagePath="[path to generated image]",
  instructions="Add Catalyst AI Services branding in the BOTTOM RIGHT corner: a tiny circular badge (about 4-5% of image width) with '© CATALYST AI' curved at top (including copyright symbol), 'SERVICES' curved at bottom, and a cute robot waving in the center (black line art). The badge should be subtle, semi-transparent (85% opacity), positioned in the lower right with a small margin. Do not obscure important content."
)
```

> **Warning:** Option B is unreliable. AI models cannot consistently render specific logos or text. Use Option A for professional results.

### Branding Layout

| Element | Position | Size/Style |
|---------|----------|------------|
| **Logo badge** | Bottom-right corner | 5% of image width, 85% opacity |

The logo includes the © symbol, so no separate copyright text is needed.

### Example

```
# 1. Generate an infographic
gemini_generate_image(
  prompt="A clean infographic showing 5 steps of AI implementation...",
  aspectRatio="4:3",
  imageSize="4K"
)

# 2. Add Catalyst branding
gemini_edit_image(
  imagePath="/Users/.../generated-xyz.png",
  instructions="Add a small Catalyst AI Services watermark in the lower right corner: 1) Tiny circular badge (3-4% width) with 'CATALYST AI' at top, 'SERVICES' at bottom, robot waving in center. 2) '© Catalyst AI Services' in small text below. Subtle, 80% opacity, bottom right with margin."
)
```

### Brand Color Palettes

**When generating branded Catalyst content, ask which palette to use:**

#### Option 1: Calm Luxury (Default)

**Use for:** Corporate messaging, financial topics, technology showcases, premium/sophisticated concepts
**Vibe:** Professional, elegant, authoritative, clean

| Role | Color | Hex |
|------|-------|-----|
| **Primary** | Teal | `#557373` |
| **Light Background** | Soft Blue Gray | `#DFE5F3` |
| **Dark Accent** | Deep Olive | `#272401` |
| **Page Background** | Warm Cream | `#F2EFEA` |
| **Text/Dark** | Near Black | `#0D0D0D` |

#### Option 2: Sage & Sand

**Use for:** Wellness, sustainability, human-centric stories, growth, organic concepts
**Vibe:** Grounded, calming, natural, approachable

| Role | Color | Hex |
|------|-------|-----|
| **Primary** | Sage Green | `#6B8E6B` |
| **Secondary** | Warm Sand | `#D4C4A8` |
| **Accent** | Terracotta | `#C4785A` |
| **Neutral Dark** | Charcoal | `#3D3D3D` |
| **Neutral Light** | Warm White | `#FAF8F5` |

**Note on Color Accuracy:** The model may generate shades that are close but not exact. For 100% brand-perfect colors, minor correction in a photo editor may be required.

For dark backgrounds: Use white/light version of watermark for visibility
