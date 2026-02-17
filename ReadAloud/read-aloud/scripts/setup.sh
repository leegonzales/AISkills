#!/usr/bin/env bash
set -euo pipefail

# Read Aloud — Setup & Dependency Validator
#
# Usage:
#   setup.sh          Full install (create venv, install packages)
#   setup.sh --check  Validate only, no changes

VENV_DIR="$HOME/.read-aloud/venv"
PYTHON_CMD="${VENV_DIR}/bin/python"
CHECK_ONLY=false

if [[ "${1:-}" == "--check" ]]; then
    CHECK_ONLY=true
fi

echo "═══════════════════════════════════════════"
echo "  Read Aloud — Setup"
if $CHECK_ONLY; then
    echo "  Mode: Check only (no changes)"
else
    echo "  Mode: Full install"
fi
echo "═══════════════════════════════════════════"
echo

ERRORS=0

# ── Check 1: Platform ──
echo "Checking platform..."
if [[ "$(uname -s)" != "Darwin" ]]; then
    echo "  ✗ macOS required (found: $(uname -s))"
    echo "    Kokoro TTS uses MLX which requires Apple Silicon."
    ERRORS=$((ERRORS + 1))
else
    ARCH="$(uname -m)"
    if [[ "$ARCH" != "arm64" ]]; then
        echo "  ✗ Apple Silicon required (found: $ARCH)"
        echo "    MLX only runs on M1/M2/M3/M4 chips."
        ERRORS=$((ERRORS + 1))
    else
        echo "  ✓ macOS on Apple Silicon ($ARCH)"
    fi
fi

# ── Check 2: Python ──
# MLX requires Python 3.13+ on recent macOS. Find the best available Python.
echo "Checking Python..."
BEST_PYTHON=""
for candidate in python3.13 python3.14 python3; do
    if command -v "$candidate" &>/dev/null; then
        PY_VERSION="$($candidate -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
        PY_MAJOR="$(echo "$PY_VERSION" | cut -d. -f1)"
        PY_MINOR="$(echo "$PY_VERSION" | cut -d. -f2)"
        if [[ "$PY_MAJOR" -ge 3 && "$PY_MINOR" -ge 13 ]]; then
            BEST_PYTHON="$(command -v "$candidate")"
            echo "  ✓ Python $PY_VERSION ($BEST_PYTHON)"
            break
        fi
    fi
done

if [[ -z "$BEST_PYTHON" ]]; then
    # Fallback: check if any python3 exists
    if command -v python3 &>/dev/null; then
        PY_VERSION="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
        echo "  ✗ Python 3.13+ required for MLX (found: $PY_VERSION)"
    else
        echo "  ✗ Python 3.13+ not found"
    fi
    echo "    Install via: brew install python@3.13"
    ERRORS=$((ERRORS + 1))
fi

# ── Check 3: ffmpeg ──
echo "Checking ffmpeg..."
if ! command -v ffmpeg &>/dev/null; then
    echo "  ⚠ ffmpeg not found (optional but recommended)"
    echo "    Without ffmpeg, audio is embedded as WAV (5-10x larger files)."
    if ! $CHECK_ONLY; then
        REPLY=""
        if [[ -t 0 ]]; then
            read -p "    Install ffmpeg via Homebrew? [Y/n] " -n 1 -r
            echo
        fi
        if [[ ! $REPLY =~ ^[Nn]$ ]]; then
            echo "    Installing ffmpeg..."
            brew install ffmpeg
            echo "  ✓ ffmpeg installed"
        else
            echo "  ⚠ Skipping ffmpeg (reader will use WAV embedding)"
        fi
    fi
else
    echo "  ✓ ffmpeg $(ffmpeg -version 2>&1 | head -1 | grep -oE '[0-9]+\.[0-9]+(\.[0-9]+)?'  | head -1)"
fi

# ── Check 4: Venv ──
echo "Checking Python environment..."
if [[ -d "$VENV_DIR" ]] && [[ -f "$PYTHON_CMD" ]]; then
    # Verify key packages are installed
    MISSING_PKGS=()
    if ! "$PYTHON_CMD" -c "import mlx_audio" &>/dev/null; then
        MISSING_PKGS+=("mlx-audio")
    fi
    if ! "$PYTHON_CMD" -c "import faster_whisper" &>/dev/null; then
        MISSING_PKGS+=("faster-whisper")
    fi
    if ! "$PYTHON_CMD" -c "import soundfile" &>/dev/null; then
        MISSING_PKGS+=("soundfile")
    fi
    if ! "$PYTHON_CMD" -c "import misaki" &>/dev/null; then
        MISSING_PKGS+=("misaki")
    fi

    if [[ ${#MISSING_PKGS[@]} -eq 0 ]]; then
        echo "  ✓ Venv exists with all packages at $VENV_DIR"
    else
        echo "  ⚠ Venv exists but missing: ${MISSING_PKGS[*]}"
        if ! $CHECK_ONLY; then
            echo "    Installing missing packages..."
            "$VENV_DIR/bin/pip" install --quiet "${MISSING_PKGS[@]}"
            echo "  ✓ Packages installed"
        else
            ERRORS=$((ERRORS + 1))
        fi
    fi
else
    if $CHECK_ONLY; then
        echo "  ✗ Venv not found at $VENV_DIR"
        echo "    Run setup.sh (without --check) to create it."
        ERRORS=$((ERRORS + 1))
    else
        if [[ -z "$BEST_PYTHON" ]]; then
            echo "  ✗ Cannot create venv: Python 3.13+ required"
            ERRORS=$((ERRORS + 1))
        else
            echo "  Creating venv at $VENV_DIR (using $BEST_PYTHON)..."
            mkdir -p "$(dirname "$VENV_DIR")"
            "$BEST_PYTHON" -m venv "$VENV_DIR"
            echo "  Installing packages (this takes 1-2 minutes)..."
            "$VENV_DIR/bin/pip" install --quiet --upgrade pip
            "$VENV_DIR/bin/pip" install --quiet mlx-audio faster-whisper soundfile misaki num2words spacy phonemizer
            echo "  ✓ Venv created with all packages"
        fi
    fi
fi

# ── Check 5: Model cache ──
echo "Checking model cache..."
KOKORO_CACHE="$HOME/.cache/huggingface/hub/models--mlx-community--Kokoro-82M-bf16"
if [[ -d "$KOKORO_CACHE" ]]; then
    echo "  ✓ Kokoro model cached"
else
    echo "  ⚠ Kokoro model not cached (will download ~200MB on first run)"
fi

WHISPER_CACHE="$HOME/.cache/huggingface/hub/models--Systran--faster-whisper-base"
if [[ -d "$WHISPER_CACHE" ]]; then
    echo "  ✓ Whisper model cached"
else
    echo "  ⚠ Whisper model not cached (will download ~150MB on first run)"
fi

# ── Summary ──
echo
echo "═══════════════════════════════════════════"
if [[ $ERRORS -eq 0 ]]; then
    echo "  ✓ All checks passed. Ready to use."
else
    echo "  ✗ $ERRORS issue(s) found."
    if $CHECK_ONLY; then
        echo "  Run setup.sh (without --check) to fix."
    fi
fi
echo "═══════════════════════════════════════════"

exit $ERRORS
