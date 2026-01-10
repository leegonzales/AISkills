# WritingSamples Integration

How to use personal writing samples for voice calibration.

---

## Overview

WritingSamples/ provides the gold standard for voice calibration—comparing AI-assisted drafts against your actual writing. This integration is **optional but recommended** for best results.

**Without samples:** The skill relies on blocklist pattern detection and prose-polish scoring.

**With samples:** Full voice calibration comparing rhythm, openings, transitions, and example usage.

---

## Setup

### Directory Structure

Place a `WritingSamples/` directory in your working directory:

```
your-project/
├── WritingSamples/
│   ├── 01-topic-description.md
│   ├── 02-another-piece.md
│   └── ...
└── ... (your other files)
```

### Sample Selection

**Good samples:**
- Authentic writing you're proud of
- Variety of topics and formats
- 500-2000 words each
- Represents your actual voice (not edited by AI)

**Avoid:**
- Heavily edited or co-written pieces
- Very short snippets (<300 words)
- Writing from years ago (voice evolves)
- Formal/academic writing if you want casual voice (or vice versa)

### Naming Convention

Use numbered prefixes for easy reference:
```
01-diversity-inclusion-essay.md
02-technical-blog-post.md
03-personal-narrative.md
```

---

## How It Works

### During Calibration

1. **Topic matching**: Identify the domain of current draft
2. **Sample search**: Find 1-2 samples with similar topics or tone
3. **Pattern extraction**: Pull 2-3 representative paragraphs
4. **Comparison**: Check draft against sample patterns
   - Sentence rhythm (short/long variation)
   - Opening styles (how paragraphs begin)
   - Transition patterns
   - Example usage (concrete vs abstract)
   - First-person ownership

### Comparison Protocol

```
Load sample → Extract patterns → Compare to draft → Flag mismatches → Suggest alternatives
```

**Example comparison:**

Sample pattern:
> "I wonder about the gap between intention and impact. When I led the migration project, we had the best intentions..."

Draft pattern:
> "It's important to note that the gap between intention and impact matters significantly in organizational contexts."

**Mismatch detected:**
- Sample uses "I wonder about..." opening
- Draft uses "It's important to note..." (blocklist item)
- Sample has concrete example ("When I led...")
- Draft is abstract

**Suggested revision:**
> "I keep coming back to the gap between intention and impact. During the migration project, I saw this firsthand..."

---

## When to Load Samples

### Always Load
- Before drafting major sections
- During calibration checks
- When user asks "does this sound like me?"

### Never Load
- During interview (no draft yet)
- For minor edits
- When user says "trust my voice on this"

---

## Building Your Sample Collection

### Starting from Scratch

If you don't have samples yet:

1. **Collect existing writing**: Blog posts, emails, memos, journal entries
2. **Curate for authenticity**: Choose pieces that feel most "you"
3. **Aim for 5-10 samples**: Enough variety without overwhelming
4. **Update periodically**: Voice evolves; refresh annually

### Voice Capture Mode (Future)

In a future version, Writing Partner will include a "voice capture" interview mode to help you articulate your voice patterns explicitly.

---

## Troubleshooting

### "No relevant samples found"

- Add samples covering more topics
- Use more general samples that show voice regardless of topic

### "Sample doesn't match my current style"

- Voice evolves; consider refreshing old samples
- Add recent writing to the collection

### "Flagging things I actually wrote"

- Your style may occasionally match AI patterns
- Use "trust my voice on this" to override
- Consider if the pattern is something you want to keep

---

## Privacy Note

WritingSamples/ should contain your personal writing. If using a public repository:

- Add `WritingSamples/` to `.gitignore`
- Keep samples in a private location
- The skill works without samples (blocklist-only mode)

---

**See also:**
- `references/blocklist.md` for AI pattern detection
- `integrations/prose-polish.md` for AI detection scoring
