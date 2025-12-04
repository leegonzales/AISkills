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

| Tool | Purpose |
|------|---------|
| `gemini_generate_image` | Create new images from text prompts |
| `gemini_edit_image` | Modify existing images with instructions |
| `continue_editing` | Refine the last generated image |
| `get_image_history` | List all generated images in session |

### Advanced Features

| Feature | Capability |
|---------|------------|
| **4K Output** | Up to 5632×3072 pixels |
| **Text Rendering** | Accurate text in images (signs, labels, UI) |
| **Multi-Image Composition** | Combine up to 14 reference images |
| **Character Consistency** | Maintain same character across 5+ images |
| **Google Search Grounding** | Real-world accurate imagery |

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
| Gemini 3 Pro Image | Slower | Highest (4K) | Higher | Final assets, print, marketing |
| Gemini 2.5 Flash Image | Fast | Good (2K) | Lower | Prototyping, iteration, drafts |

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
