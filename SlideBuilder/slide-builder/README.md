# SlideBuilder

Transform essay-to-speech output into complete presentations with multiple output formats.

## Overview

SlideBuilder is a Claude skill that takes the output from `essay-to-speech` and produces:

1. **Talk Track v5** (always) - YAML frontmatter + Markdown intermediate format
2. **HTML Presentation** (--html) - Self-contained slides with timer, audio, notes
3. **Remotion Video** (--video) - YouTube-ready H.264 MP4

## Pipeline

```
Essay → essay-to-speech → slide-builder → Multiple Outputs
                              ↓
                    ┌─────────┼─────────┐
                    ↓         ↓         ↓
              Talk Track   HTML      Remotion
              (v5 YAML)   Slides     Video
```

## Usage

Invoke when:
- You have essay-to-speech output ready for slides
- User asks to "build slides" or "create presentation"
- User uses `/slide-builder` command

## Input Format

Markdown from essay-to-speech with:
- Original text
- Talk Track with semantic tags
- Image ratings (USE/ADAPT/RECREATE/SKIP)
- Slide Ideas

## Output Format

Talk Track v5 with:
- YAML frontmatter (metadata, sections)
- Slides table
- Slide content with <!-- AUDIO --> blocks
- Speaker notes

## Voice Generation

| Mode | Tool | Cost |
|------|------|------|
| Draft (default) | Kokoro TTS | Free |
| Publish | ElevenLabs v3 | ~$0.30/1K chars |

## Image Handling

| Rating | Action |
|--------|--------|
| USE | Copy directly |
| ADAPT | Note modifications needed |
| RECREATE | Generate Nano Banana prompt |
| SKIP | Omit |

## Integration

- **Input**: essay-to-speech skill
- **Voice**: claude-speak skill (Kokoro TTS)
- **Images**: nano-banana skill (Gemini image generation)
- **HTML**: AIEnablementTraining generators
- **Video**: AITalkShowCli Remotion architecture

## References

- `references/talk-track-v5.md` - Format specification
- `references/html-engine.md` - HTML presentation patterns
- `references/remotion-video.md` - Video generation guide
- `references/voice-options.md` - Kokoro vs ElevenLabs
- `references/image-handling.md` - USE/ADAPT/RECREATE/SKIP
- `references/examples.md` - Full transformations
