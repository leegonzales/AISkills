# Voice Generation Options

Reference for TTS options in SlideBuilder presentations.

## 1. Overview

SlideBuilder supports two TTS options optimized for different stages of the workflow:

| Stage | Tool | Cost | Quality | Use Case |
|-------|------|------|---------|----------|
| Draft/Preview | Kokoro TTS (local) | Free | Good | Rapid iteration, testing timing |
| Final Publish | ElevenLabs v3 | ~$0.30/1K chars | Excellent | Production videos with caption sync |

**Default behavior:** Use Kokoro for all iteration; switch to ElevenLabs only for final publish.

## 2. Kokoro TTS (Local)

### Setup

Uses the claude-speak skill infrastructure. The daemon runs in background via launchd for instant response.

```bash
~/Projects/claude-speak/.venv/bin/claude-speak-client "Text to speak"
```

### Available Voices

| Voice | Description | Best For |
|-------|-------------|----------|
| `af_heart` | American female, warm | **DEFAULT for presentations** |
| `bm_george` | British male, distinguished | Technical/formal content |
| `am_adam` | American male, deep | Authoritative narration |
| `bf_emma` | British female, elegant | Polished delivery |

### Command Options

```bash
# Specify voice
~/Projects/claude-speak/.venv/bin/claude-speak-client -v af_heart "Text"

# Adjust speed (default 1.0)
~/Projects/claude-speak/.venv/bin/claude-speak-client -s 1.1 "Slightly faster"
~/Projects/claude-speak/.venv/bin/claude-speak-client -s 0.9 "Slightly slower"

# Quiet mode (suppress errors)
~/Projects/claude-speak/.venv/bin/claude-speak-client -q "Silent on success"

# Custom timeout for long text (default: 300s / 5 min)
~/Projects/claude-speak/.venv/bin/claude-speak-client -t 600 "Very long text..."
```

### Pause Syntax

Kokoro supports pause markers in text for natural pacing:

```markdown
Let me explain this concept. [PAUSE] First, we start with the basics.

For longer pauses: [PAUSE:500] inserts a 500ms pause.
```

### Output

- **Format:** WAV
- **Location:** `presentations/{slug}/audio/`
- **Naming:** `{slide-slug}.wav` per slide

### Long Text Handling

For content longer than 3 sentences:

1. **Set longer timeout:** Use `timeout: 300000` (5 min) in Bash tool
2. **Run in background:** Use `run_in_background: true` to avoid blocking

```bash
# Background mode - continues while audio generates
~/Projects/claude-speak/.venv/bin/claude-speak-client "Your longer narration text..."
```

### Troubleshooting

If "Daemon not running" error appears:

```bash
~/Projects/claude-speak/.venv/bin/claude-speak-daemon start
```

## 3. ElevenLabs v3 (Publish Mode)

### Features

- **Word-level timestamps** for precise caption synchronization
- **Emotion tags** for expressive delivery
- **Higher quality** voice synthesis
- **Consistent voice** across all slides

### Emotion Tags

ElevenLabs v3 supports inline emotion markers:

```markdown
[excited] This is amazing news!
[whispers] But here's the secret...
[serious] This requires careful attention.
```

### API Usage

```python
from elevenlabs import generate, Voices

audio = generate(
    text="Your presentation text",
    voice="Rachel",
    model="eleven_v3"
)
```

### Word-Level Timestamps

ElevenLabs v3 returns alignment data for caption sync:

```json
{
  "audio": "base64...",
  "alignment": {
    "characters": ["H","e","l","l","o"],
    "character_start_times_seconds": [0.0, 0.05, 0.1, 0.15, 0.2],
    "character_end_times_seconds": [0.05, 0.1, 0.15, 0.2, 0.3]
  }
}
```

This character-level timing enables precise Remotion caption positioning.

### Cost Estimation

| Content Length | Approx. Characters | Cost |
|----------------|-------------------|------|
| 30-second slide | ~500 chars | ~$0.15 |
| 5-minute presentation | ~5,000 chars | ~$1.50 |
| 20-minute presentation | ~20,000 chars | ~$6.00 |

Subscription tiers available for volume usage.

## 4. Generation Workflow

### Draft Mode (Default)

```
talk-track.md
    → parse slides
    → generate audio with Kokoro
    → audio/{slug}.wav
```

Quick iteration cycle:
1. Edit talk-track.md
2. Regenerate audio for changed slides
3. Preview in Remotion
4. Repeat

### Publish Mode (--elevenlabs flag)

```
talk-track.md
    → parse slides
    → generate with ElevenLabs
    → audio/{slug}.wav + timestamps.json
```

Publish workflow:
1. Finalize talk-track.md
2. Generate with `--elevenlabs` flag
3. Timestamps enable precise caption sync
4. Render final video

## 5. Integration with AIEnablementTraining

The generate-audio.py script handles batch audio generation:

```bash
# Draft mode (Kokoro)
./generators/generate-audio.py presentations/my-presentation/

# Publish mode (ElevenLabs)
./generators/generate-audio.py presentations/my-presentation/ --elevenlabs

# Regenerate specific slides
./generators/generate-audio.py presentations/my-presentation/ --slides intro,conclusion
```

### Directory Structure

```
presentations/my-presentation/
    talk-track.md          # Source content
    audio/
        intro.wav          # Generated audio per slide
        main-content.wav
        conclusion.wav
        timestamps.json    # ElevenLabs only: word-level timing
```

## 6. Best Practices

### For Kokoro (Draft)

- Keep individual slide narration under 2 minutes
- Use natural pauses with `[PAUSE]` markers
- Test pacing before committing to ElevenLabs
- Speed adjustments: 1.0-1.1 works well for most content

### For ElevenLabs (Publish)

- Finalize all content before generating (cost per generation)
- Use emotion tags sparingly for emphasis
- Review timestamps.json for caption alignment issues
- Consider voice consistency across presentation series

### Voice Selection Guide

| Presentation Type | Recommended Voice |
|-------------------|-------------------|
| Training/Tutorial | `af_heart` (warm, approachable) |
| Technical Deep-dive | `bm_george` (authoritative) |
| Executive Summary | `am_adam` (confident) |
| Product Demo | `af_heart` or `bf_emma` |
