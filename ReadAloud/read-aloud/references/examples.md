# Read Aloud — Worked Examples

## Example 1: Basic Essay

**Input:** A markdown file with frontmatter and body text.

```bash
./scripts/read-aloud.sh ~/Documents/essays/on-complexity.md
```

**What happens:**
1. Frontmatter (YAML between `---` delimiters) is stripped automatically
2. Body text is split into paragraphs
3. Each paragraph gets its own audio chunk (~2-15 seconds each)
4. Whisper aligns words within each chunk
5. HTML reader is built and opened in browser

**Output:**
```
~/.read-aloud/output/on-complexity/
  reader.html       # 45 MB standalone HTML (12 min audio)
  audio.wav         # 120 MB raw audio
  body.md           # Extracted body (no frontmatter)
  text.txt          # Plain text for TTS
  manifest.json     # 47 chunks, timing metadata
  timestamps.json   # 3,200 word-level timestamps
  chunks/           # 47 individual WAV files
```

**Terminal output:**
```
═══════════════════════════════════════════
  Read Aloud
  Input: on-complexity.md
  Voice: af_heart  Speed: 1.0
  Output: ~/.read-aloud/output/on-complexity/
═══════════════════════════════════════════

▶ Step 1/3: Generating audio with Kokoro TTS (per-paragraph chunks)...
Extracted 3200 words, 47 paragraphs
Loading Kokoro model...
Generating audio (voice=af_heart, speed=1.0)...
  Paragraph 1/47: 68 words, 18.2s (total: 0m 18s)
  ...
  Paragraph 47/47: 42 words, 11.1s (total: 12m 34s)

▶ Step 2/3: Aligning words with Whisper (per-chunk, drift-free)...
Loading Whisper model (base)...
  Chunk 1/47: 65 whisper / 68 source words (offset: 0.0s)
  ...

▶ Step 3/3: Building standalone HTML reader...
Paragraphs: 47
HTML words: 3200
Timestamps: 3200
Audio compressed: WAV → MP3 (8.2 MB)
Reader → reader.html (9.1 MB, standalone)

═══════════════════════════════════════════
  Done! Opening reader...
═══════════════════════════════════════════
```

---

## Example 2: Custom Voice and Speed

**Input:** A technical blog post, read by a British male voice at slightly faster pace.

```bash
./scripts/read-aloud.sh ~/blog/api-design-patterns.md \
    --voice bm_george \
    --speed 1.15
```

**Why these settings:**
- `bm_george` has a measured, authoritative tone suited for technical content
- `1.15` speed keeps the reader engaged without feeling rushed

---

## Example 3: Stripping Sections

**Input:** A newsletter post with Brief and Links sections you don't want narrated.

```bash
./scripts/read-aloud.sh ~/newsletter/issue-42.md \
    --strip-sections "Brief,Links & Resources,Acknowledgments"
```

**What gets stripped:**
- Any `## Brief` section (including content until next heading)
- Any `## Links & Resources` section
- Any `## Acknowledgments` section
- YAML frontmatter (always stripped)

---

## Example 4: Custom Output Directory

**Input:** Generating a reader for a project-specific preview directory.

```bash
./scripts/read-aloud.sh posts/drafts/2026-02-10-wardley-maps.md \
    --output-dir ./preview/read-aloud/wardley-maps/
```

**Notes:**
- The date prefix `2026-02-10-` is stripped from the slug automatically
- Output goes to the specified directory instead of `~/.read-aloud/output/`

---

## Example 5: Plain Text Input

**Input:** A plain `.txt` file (no markdown formatting).

```bash
./scripts/read-aloud.sh ~/Documents/speech-draft.txt
```

**Behavior:**
- No frontmatter to strip, no markdown to convert
- Text is split on blank lines into paragraphs
- HTML output wraps each paragraph in `<p>` tags
- Everything else works identically

---

## Timing Guidelines

| Essay Length | Words | Audio Duration | Generation Time |
|-------------|-------|----------------|-----------------|
| Short post | ~800 | ~5 min | ~1 min |
| Standard essay | ~2,500 | ~15 min | ~3 min |
| Long-form | ~5,000 | ~30 min | ~6 min |
| Book chapter | ~10,000 | ~60 min | ~12 min |

*Times measured on M1 Pro. First run adds ~2 min for model downloads.*
