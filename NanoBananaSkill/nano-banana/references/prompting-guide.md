# Nano Banana Pro Prompting Guide

Advanced techniques for generating optimal images with Gemini 3 Pro Image.

## Prompt Architecture

### The SCTD Framework

Structure prompts with four components:

```
Subject → Context → Technique → Details
```

| Component | Description | Example |
|-----------|-------------|---------|
| **Subject** | Main focus of image | "A golden retriever puppy" |
| **Context** | Setting, environment | "in a sunlit meadow" |
| **Technique** | Style, medium, approach | "oil painting style" |
| **Details** | Specifics, quality, mood | "soft bokeh, warm tones, 4K" |

**Combined:**
> "A golden retriever puppy in a sunlit meadow, oil painting style, soft bokeh background, warm golden tones, 4K resolution"

## Style Keywords

### Photographic Styles

| Keyword | Effect |
|---------|--------|
| `photorealistic` | Indistinguishable from photo |
| `DSLR quality` | Sharp, professional camera look |
| `35mm film` | Slight grain, vintage colors |
| `Polaroid` | Instant camera aesthetic |
| `macro photography` | Extreme close-up detail |
| `aerial drone shot` | Bird's eye perspective |
| `long exposure` | Motion blur, light trails |
| `tilt-shift` | Miniature/toy-like effect |

### Artistic Styles

| Keyword | Effect |
|---------|--------|
| `oil painting` | Rich textures, brush strokes |
| `watercolor` | Soft edges, transparent washes |
| `digital art` | Clean, modern illustration |
| `concept art` | Entertainment industry style |
| `anime/manga` | Japanese animation style |
| `pixel art` | Retro 8/16-bit aesthetic |
| `vector illustration` | Clean, scalable graphics |
| `charcoal sketch` | Black and white, textured |

### 3D & Technical

| Keyword | Effect |
|---------|--------|
| `3D render` | Computer-generated look |
| `Unreal Engine` | Game-quality graphics |
| `octane render` | Photorealistic 3D |
| `isometric` | 45-degree angle, no perspective |
| `blueprint` | Technical drawing style |
| `wireframe` | 3D mesh visualization |

## Lighting Keywords

### Natural Light

- `golden hour` - Warm, orange sunset/sunrise light
- `blue hour` - Cool twilight tones
- `overcast` - Soft, diffused, no harsh shadows
- `dappled sunlight` - Light through leaves
- `backlit` - Subject silhouetted against light
- `harsh midday sun` - Strong shadows, high contrast

### Artificial Light

- `studio lighting` - Professional, controlled
- `neon lights` - Cyberpunk, urban glow
- `candlelight` - Warm, flickering, intimate
- `spotlight` - Dramatic single source
- `rim lighting` - Glowing edges on subject
- `volumetric lighting` - Visible light rays/fog

### Mood Lighting

- `moody` - Dark, atmospheric
- `high key` - Bright, minimal shadows
- `low key` - Dark, dramatic shadows
- `chiaroscuro` - Strong light/dark contrast

## Composition Keywords

- `rule of thirds` - Subject off-center
- `centered composition` - Symmetrical, balanced
- `leading lines` - Lines draw eye to subject
- `negative space` - Minimalist, breathing room
- `close-up` - Tight framing on subject
- `wide shot` - Environmental context
- `Dutch angle` - Tilted, dynamic tension
- `bird's eye view` - Looking down
- `worm's eye view` - Looking up

## Text Rendering Tips

Nano Banana Pro excels at text. For best results:

### Do:

```
✓ "A neon sign reading 'OPEN 24 HOURS' in pink and blue"
✓ "Book cover with title 'THE LAST GARDEN' in elegant serif font"
✓ "Protest sign with handwritten text 'SAVE THE BEES'"
```

### Specify Font Style:

| Style | Use Case |
|-------|----------|
| `bold sans-serif` | Modern, impactful |
| `elegant serif` | Classic, sophisticated |
| `handwritten` | Personal, casual |
| `retro typography` | Vintage posters |
| `graffiti style` | Urban, street art |
| `gothic/blackletter` | Medieval, heavy metal |

### Avoid:

```
✗ Very long text passages (keep under 10 words)
✗ Multiple different text elements competing
✗ Tiny text that would be illegible
```

## Character Consistency

### Initial Character Definition

Be extremely specific on first generation:

```
"Portrait of a 30-year-old woman named Sarah:
- Auburn wavy hair, shoulder length
- Green eyes with gold flecks
- Light freckles across nose and cheeks
- Warm smile, slight dimples
- Wearing a cream cable-knit sweater
Photorealistic, soft natural lighting"
```

### Subsequent Scenes

Reference the original with `history:0`:

```
"Sarah from history:0, now in a different scene:
- Standing in a bookshop
- Browsing old leather-bound books
- Same outfit (cream sweater)
- Afternoon light through window
- Same photorealistic style"
```

### Consistency Tips

1. **Lock core features** - Always mention distinctive traits
2. **Vary only context** - Change setting, not character
3. **Maintain style** - Keep artistic approach consistent
4. **Use session history** - Reference previous generations

## Quality Enhancement Keywords

### Resolution & Detail

- `4K resolution` - High detail output
- `highly detailed` - Intricate elements
- `sharp focus` - Crisp subject
- `intricate details` - Fine textures/patterns

### Professional Quality

- `award-winning` - Competition-level quality
- `professional` - Polished, commercial
- `masterpiece` - Exceptional craftsmanship
- `trending on ArtStation` - Contemporary digital art style

### Negative Prompting

Tell the model what to avoid:

```
"Beautiful landscape, no people, no text, no watermarks,
no blurry elements, no oversaturation"
```

## Domain-Specific Prompts

### Product Photography

```
"[Product] on white seamless background,
studio lighting with soft shadows,
commercial product photography,
high-end catalog style, 4K"
```

### Architecture

```
"[Building type] in [location],
[architectural style],
[time of day] lighting,
architectural photography,
sharp lines, professional"
```

### Food Photography

```
"[Dish name], overhead shot,
rustic wooden table setting,
natural window light,
food styling with garnish,
appetizing, editorial quality"
```

### Portraits

```
"Portrait of [subject description],
[expression/mood],
[lighting type],
[background],
shallow depth of field,
[style: photorealistic/artistic]"
```

## Troubleshooting Prompts

| Problem | Solution |
|---------|----------|
| Too generic | Add 3+ specific details |
| Wrong style | Explicitly state style twice |
| Bad composition | Specify camera angle and framing |
| Poor lighting | Name exact lighting setup |
| Inconsistent character | Reference history, repeat key features |
| Text errors | Reduce text length, use quotes |
