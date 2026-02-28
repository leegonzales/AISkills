---
name: render-video
description: Use when rendering a final script into a video. Takes a script with [GRAPHIC:] markers, generates images, synthesizes audio, builds a timeline, and renders MP4 via Remotion. Supports --quality draft|standard|high. Triggers include "/render-video", "render this script", or "make a video from this script".
---

# Render Video Skill

Render a script with `[GRAPHIC:]` markers into MP4. Deterministic pipeline code only -- no creative agents, no LLM content generation.

## When to Use

- Rendering a script from `/write-script` into video
- Re-rendering with different images or audio quality
- Rendering any script containing `[GRAPHIC: description | DURATION: Xs]` markers

## Usage

```
/render-video
/render-video --script path/to/05-final-script.txt
/render-video --quality draft --output output/my-video/
```

### Step 1: Detect Input

Find script: `--script` arg, then `05-final-script.txt`, then `script.txt`, then ask.
Accept `--quality draft|standard|high` (default: standard) and `--output <dir>`.

### Step 2: Validate Prerequisites

- Script has `[GRAPHIC:]` markers (parse with `parseGraphicCues()`)
- **draft**: Kokoro daemon running (`/tmp/claude-speak.sock` exists), ffmpeg installed
- **standard/high**: `ELEVENLABS_API_KEY` set (`echo $ELEVENLABS_API_KEY | head -c4`)
- **Images**: Nano Banana MCP available (ToolSearch `nanobanana`) OR `GEMINI_API_KEY` set
- **Render**: `npx remotion --version` succeeds

If no image API available, SVG placeholders are used. Report but continue.

### Step 3: Parse and List Graphic Cues

Extract markers, present to user with descriptions and inferred types (atmospheric/data_graphic/character).

### Step 4: Generate Images

Fallback chain per cue:
1. **Nano Banana MCP**: `mcp__nanobanana-mcp__gemini_generate_image` (16:9 landscape)
2. **Gemini API**: `generateImage()` from pipeline (includes QC loop)
3. **SVG placeholder**: auto-generated

Also generate opening scene via `generateOpeningImage()`. Save to `images/graphic_NNN.{png|jpg|svg}`.

**PAUSE.** Present images for review: "Want to regenerate any?"

### Step 5: Synthesize Audio

| Quality | Provider | Word Timings |
|---------|----------|-------------|
| draft | Kokoro (local, free) | Estimated |
| standard/high | ElevenLabs (paid) | Precise |

Call `synthesizeMonologue()`. Output: `narration.mp3` + word timings.

### Step 6: Build Timeline and Render

1. `buildTimeline()` -- syncs graphic cues to audio via word timings
2. `renderVideo()` -- Remotion bundles and renders MP4
3. `exportSubtitles()` -- generates `.srt` + `.vtt` if timings exist

### Step 7: Present Results

Show output path, file size, duration, image count (real vs placeholder), audio provider. Ask: "Want to re-render any images or make changes?"

## Integration

- **Upstream:** `/write-script` produces `05-final-script.txt`
- **Standalone:** any script with `[GRAPHIC:]` markers
- **Reference:** see `references/pipeline.md` for codebase entry points
