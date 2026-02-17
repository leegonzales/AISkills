---
name: read-aloud
description: Generate a standalone HTML reader with Kokoro TTS audio and word-synced highlighting from any markdown file. Use when user wants to listen to an essay, proofread by ear, or create an audio reader.
---

# Read Aloud

Generate a standalone HTML reader with high-quality TTS audio and real-time word highlighting from any markdown file.

## When to Use

Invoke when user:
- Asks to "read this aloud" or "generate audio" for a markdown file
- Wants to proofread by ear (catch awkward phrasing, rhythm issues)
- Needs a shareable audio reader (single HTML file, no server needed)
- Uses `/read-aloud` command

## Prerequisites

- macOS with Apple Silicon (M1+)
- Python 3.13+ (required for MLX)
- ffmpeg (for MP3 compression)

## Core Command

```bash
SKILL_DIR="path/to/read-aloud"
$SKILL_DIR/scripts/read-aloud.sh <markdown-file> [options]
```

First run auto-installs dependencies to `~/.read-aloud/venv/`.

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `--voice` | `af_heart` | Kokoro voice variant |
| `--speed` | `1.0` | Speech rate (0.5-2.0) |
| `--output-dir` | `~/.read-aloud/output/<slug>/` | Custom output directory |
| `--strip-sections` | *(none)* | Comma-separated heading names to skip |
| `--no-open` | *(off)* | Don't open browser after generation |

## Pipeline

Three-stage process (~2-5 min for a typical essay):

1. **Generate Audio** — Kokoro TTS produces per-paragraph WAV chunks
2. **Align Words** — Whisper transcribes each chunk for drift-free word timestamps
3. **Build Reader** — Assembles standalone HTML with embedded MP3 + word sync

## Output

Single `reader.html` file with:
- Base64-embedded MP3 audio (fully standalone, no server needed)
- Per-word highlighting synced to audio playback
- Sticky playback controls (play/pause, stop, speed, progress bar)
- Keyboard shortcuts (Space, Escape, Arrow keys)
- Click any word to seek

## Available Voices

| Voice | Description |
|-------|-------------|
| `af_heart` | American female, warm (default) |
| `af_bella` | American female, clear |
| `am_adam` | American male, deep |
| `am_michael` | American male, neutral |
| `bf_emma` | British female, elegant |
| `bm_george` | British male, distinguished |

## Examples

```bash
# Basic usage — generates reader at ~/.read-aloud/output/my-essay/
$SKILL_DIR/scripts/read-aloud.sh ~/Documents/my-essay.md

# Custom voice and speed
$SKILL_DIR/scripts/read-aloud.sh post.md --voice bm_george --speed 1.1

# Output to specific directory
$SKILL_DIR/scripts/read-aloud.sh draft.md --output-dir ./preview/

# Strip specific sections before generating
$SKILL_DIR/scripts/read-aloud.sh post.md --strip-sections "Brief,Links & Resources"
```

## References

- Load `references/voice-guide.md` for detailed voice descriptions and speed tuning
- Load `references/examples.md` for worked examples with expected output
- Load `references/troubleshooting.md` when errors occur
