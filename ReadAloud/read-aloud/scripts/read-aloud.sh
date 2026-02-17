#!/usr/bin/env bash
set -euo pipefail

# Read Aloud — Generate Kokoro TTS audio with drift-free word highlighting
#
# Usage: ./read-aloud.sh <markdown-file> [--voice af_heart] [--speed 1.0]
#                                        [--output-dir path] [--strip-sections "A,B"]
#                                        [--no-open]
#
# Generates a standalone HTML reader with embedded MP3 audio and
# per-word highlighting. Audio is chunked per paragraph for drift-free
# Whisper alignment, then compressed to MP3 and embedded as base64.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$HOME/.read-aloud/venv"
VENV_PYTHON="${VENV_DIR}/bin/python"

# Handle OpenMP duplicate library conflict between mlx and faster-whisper
export KMP_DUPLICATE_LIB_OK=TRUE

# ── Auto-setup on first run ──
if [[ ! -f "$VENV_PYTHON" ]]; then
    echo "First run detected — running setup..."
    echo
    "$SCRIPT_DIR/setup.sh"
    echo
fi

# ── Parse args ──
INPUT_FILE="${1:?Usage: ./read-aloud.sh <markdown-file> [options]}"
shift
VOICE="af_heart"
SPEED="1.0"
OUTPUT_DIR=""
STRIP_SECTIONS=""
NO_OPEN=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --voice) VOICE="$2"; shift 2 ;;
        --speed) SPEED="$2"; shift 2 ;;
        --output-dir) OUTPUT_DIR="$2"; shift 2 ;;
        --strip-sections) STRIP_SECTIONS="$2"; shift 2 ;;
        --no-open) NO_OPEN=true; shift ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

# Resolve absolute path for input
INPUT_FILE="$(cd "$(dirname "$INPUT_FILE")" && pwd)/$(basename "$INPUT_FILE")"

if [[ ! -f "$INPUT_FILE" ]]; then
    echo "Error: File not found: $INPUT_FILE"
    exit 1
fi

# ── Derive slug and output dir ──
BASENAME="$(basename "$INPUT_FILE" .md)"
# Also handle .txt extension
BASENAME="$(echo "$BASENAME" | sed 's/\.txt$//')"
SLUG="$(echo "$BASENAME" | sed 's/^[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}-//')"

if [[ -z "$OUTPUT_DIR" ]]; then
    OUTPUT_DIR="$HOME/.read-aloud/output/$SLUG"
fi

echo "═══════════════════════════════════════════"
echo "  Read Aloud"
echo "  Input: $(basename "$INPUT_FILE")"
echo "  Voice: $VOICE  Speed: $SPEED"
echo "  Output: $OUTPUT_DIR"
echo "═══════════════════════════════════════════"
echo

# ── Build strip-sections flag ──
STRIP_FLAG=()
if [[ -n "$STRIP_SECTIONS" ]]; then
    STRIP_FLAG=(--strip-sections "$STRIP_SECTIONS")
fi

# ── Step 1: Generate per-paragraph audio chunks with Kokoro ──
echo "▶ Step 1/3: Generating audio with Kokoro TTS (per-paragraph chunks)..."
"$VENV_PYTHON" "$SCRIPT_DIR/generate_audio.py" \
    "$INPUT_FILE" \
    --voice "$VOICE" \
    --speed "$SPEED" \
    --output-dir "$OUTPUT_DIR" \
    "${STRIP_FLAG[@]+"${STRIP_FLAG[@]}"}"
echo

# ── Step 2: Align words per chunk with Whisper (drift-free) ──
echo "▶ Step 2/3: Aligning words with Whisper (per-chunk, drift-free)..."
"$VENV_PYTHON" "$SCRIPT_DIR/align_words.py" \
    "$OUTPUT_DIR"
echo

# ── Step 3: Build standalone HTML reader ──
echo "▶ Step 3/3: Building standalone HTML reader..."
"$VENV_PYTHON" "$SCRIPT_DIR/build_reader.py" \
    "$OUTPUT_DIR/body.md" \
    "$OUTPUT_DIR/audio.wav" \
    "$OUTPUT_DIR/timestamps.json" \
    --output "$OUTPUT_DIR/reader.html"
echo

echo "═══════════════════════════════════════════"
echo "  Done!"
echo "  $OUTPUT_DIR/reader.html"
echo "═══════════════════════════════════════════"

# ── Open in browser ──
if ! $NO_OPEN; then
    if command -v open &>/dev/null; then
        open "$OUTPUT_DIR/reader.html"
    elif command -v xdg-open &>/dev/null; then
        xdg-open "$OUTPUT_DIR/reader.html"
    else
        echo "  (Open the reader.html file in your browser to view)"
    fi
fi
