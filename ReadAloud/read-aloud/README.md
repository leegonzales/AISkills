# Read Aloud

Generate standalone HTML audio readers with word-synced highlighting from any markdown file. Uses Kokoro TTS (via MLX) for high-quality speech and Whisper for drift-free word alignment.

## Features

- **Standalone output** — Single HTML file with embedded MP3; share via email, Slack, anywhere
- **Word-synced highlighting** — Real-time word tracking as audio plays
- **Drift-free alignment** — Per-paragraph Whisper transcription prevents timing cascade errors
- **Interactive reader** — Play/pause, speed control (0.5x-2.0x), click-to-seek, keyboard shortcuts
- **Auto-setup** — First run validates and installs all dependencies automatically

## Prerequisites

| Requirement | Notes |
|-------------|-------|
| macOS + Apple Silicon | Kokoro TTS uses MLX (Apple's ML framework) |
| Python 3.13+ | Required for MLX (`brew install python@3.13`) |
| ffmpeg | For WAV→MP3 compression (`brew install ffmpeg`) |

## Installation

```bash
# Clone or copy the skill
git clone https://github.com/leegonzales/AISkills.git && cd AISkills/ReadAloud/read-aloud

# Option 1: Auto-setup on first run
./scripts/read-aloud.sh my-file.md

# Option 2: Explicit setup
./scripts/setup.sh

# Option 3: Check requirements without installing
./scripts/setup.sh --check
```

Setup creates a dedicated Python environment at `~/.read-aloud/venv/` with:
- `mlx-audio` — Kokoro TTS on Apple Silicon
- `faster-whisper` — Word-level timestamp alignment
- `soundfile` — Audio I/O
- `misaki`, `num2words`, `spacy`, `phonemizer` — Kokoro's text processing deps

## Usage

```bash
# Basic — output to ~/.read-aloud/output/<slug>/
./scripts/read-aloud.sh essay.md

# Custom voice and speed
./scripts/read-aloud.sh essay.md --voice bm_george --speed 1.1

# Custom output directory
./scripts/read-aloud.sh essay.md --output-dir ./my-output/

# Skip specific markdown sections by heading
./scripts/read-aloud.sh essay.md --strip-sections "Brief,Links & Resources"

# Generate without opening browser
./scripts/read-aloud.sh essay.md --no-open
```

## Output

```
~/.read-aloud/output/essay-slug/
  reader.html       # Standalone HTML reader (shareable)
  audio.wav         # Full audio (WAV)
  body.md           # Extracted markdown body
  text.txt          # Plain text version
  manifest.json     # Per-chunk metadata
  timestamps.json   # Per-word alignment data
  chunks/           # Per-paragraph WAV files
```

## How It Works

1. **Generate Audio** — Kokoro TTS generates a separate WAV for each paragraph
2. **Align Words** — Whisper transcribes each chunk independently (drift-free)
3. **Build Reader** — Converts markdown to HTML, wraps words with timestamp spans, compresses audio to MP3, embeds everything as base64 in a single HTML file

The per-paragraph chunking is key: by aligning words within each paragraph independently, timing errors in one paragraph never cascade to the next.

## Available Voices

| Voice | Style | Best For |
|-------|-------|----------|
| `af_heart` | American female, warm | Essays, narratives (default) |
| `af_bella` | American female, clear | Technical content |
| `am_adam` | American male, deep | Authoritative pieces |
| `am_michael` | American male, neutral | General purpose |
| `bf_emma` | British female, elegant | Literary content |
| `bm_george` | British male, distinguished | Formal writing |

## Troubleshooting

See `references/troubleshooting.md` for common issues. Quick fixes:

- **OMP error**: Handled automatically (`KMP_DUPLICATE_LIB_OK=TRUE`)
- **No ffmpeg**: `brew install ffmpeg` (falls back to WAV embedding without it)
- **Model download slow**: First run downloads ~350MB of models; subsequent runs are instant

## License

MIT
