# Changelog

## v1.0.0 — 2026-02-16

Initial release. Generic read-aloud skill extracted from substack-specific tooling.

### Added
- Standalone HTML reader generation from any markdown file
- Kokoro TTS audio generation with per-paragraph chunking
- Drift-free Whisper word alignment (per-chunk transcription)
- Interactive reader with word highlighting, speed control, click-to-seek
- Auto-setup script that validates and installs all dependencies
- Unified Python venv at `~/.read-aloud/venv/` (mlx-audio + faster-whisper)
- Configurable output directory (`--output-dir`)
- Section stripping (`--strip-sections`) for flexible markdown handling
- Cross-platform browser open (macOS/Linux)
- YAML frontmatter stripping for any markdown file
- Voice and speed selection flags
