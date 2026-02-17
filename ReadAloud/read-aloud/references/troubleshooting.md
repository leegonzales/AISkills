# Read Aloud — Troubleshooting

## OpenMP Duplicate Library Error

**Symptom:**
```
OMP: Error #15: Initializing libomp.dylib, but found libiomp5.dylib already initialized.
```

**Cause:** Both `mlx-audio` and `faster-whisper` bundle OpenMP libraries that conflict.

**Solution:** The orchestrator script sets `KMP_DUPLICATE_LIB_OK=TRUE` automatically. If you're running Python scripts directly, set it yourself:

```bash
KMP_DUPLICATE_LIB_OK=TRUE ~/.read-aloud/venv/bin/python scripts/align_words.py output/
```

---

## ffmpeg Not Found

**Symptom:**
```
Audio embedded as WAV (120.3 MB)
```
(Reader works but is much larger than expected)

**Solution:**
```bash
brew install ffmpeg
```

Without ffmpeg, the reader embeds raw WAV audio instead of compressed MP3. This makes the HTML file 5-10x larger but otherwise works fine.

---

## Model Download Issues

**Symptom:** First run hangs or fails during "Loading Kokoro model..." or "Loading Whisper model..."

**Cause:** Models are downloaded from Hugging Face on first use (~350 MB total).

**Solutions:**
- Check internet connection
- If behind a proxy, set `HTTPS_PROXY` environment variable
- Models cache to `~/.cache/huggingface/` — check disk space
- If download was interrupted, clear the cache and retry:
  ```bash
  rm -rf ~/.cache/huggingface/hub/models--mlx-community--Kokoro-82M-bf16
  ```

---

## Venv Creation Fails

**Symptom:** `setup.sh` fails during pip install.

**Common causes:**
1. **Wrong Python version** — Need 3.13+ for MLX. Check with `python3.13 --version`.
2. **No Apple Silicon** — MLX only works on M1/M2/M3/M4 Macs.
3. **Disk space** — Venv + models need ~2 GB total.

**Manual recovery:**
```bash
rm -rf ~/.read-aloud/venv
python3.13 -m venv ~/.read-aloud/venv
~/.read-aloud/venv/bin/pip install mlx-audio faster-whisper soundfile misaki num2words spacy phonemizer
```

---

## Paragraph Count Mismatch Warning

**Symptom:**
```
WARNING: 47 MD paragraphs vs 45 audio chunks
```

**Cause:** The markdown-to-HTML paragraph splitter and the text-to-plain paragraph splitter disagree on block boundaries. This can happen with:
- Horizontal rules (`---`) that get treated differently
- Nested blockquotes
- Code blocks

**Impact:** Minor. The builder truncates to the shorter list — the last 1-2 paragraphs may lack audio. The rest works perfectly.

**Workaround:** Simplify markdown formatting in the affected area. Horizontal rules and complex nesting are the usual culprits.

---

## Audio Quality Issues

**Symptom:** Words sound garbled or mispronounced.

**Tips:**
- Kokoro handles standard English well but may struggle with:
  - Acronyms (write "API" as-is; it usually works)
  - URLs (strip them before generating)
  - Code snippets (strip or describe in plain English)
  - Non-English words
- The `--strip-sections` flag can remove sections with heavy technical jargon
- Speed above 1.3x degrades quality for some voices

---

## Reader HTML Won't Open

**Symptom:** Browser shows blank page or error.

**Common causes:**
1. **File too large** — Very long essays (10,000+ words) produce 100+ MB HTML files. Some browsers struggle. Try a different browser.
2. **Incomplete generation** — Check that `reader.html` exists and is non-zero size.
3. **Audio encoding issue** — If base64 encoding was interrupted, the audio tag may be malformed. Re-run the pipeline.

---

## Setup Check Mode

Run `setup.sh --check` to validate your environment without making changes:

```bash
./scripts/setup.sh --check
```

This reports:
- Platform and architecture
- Python version
- ffmpeg availability
- Venv status
- Cached model status
