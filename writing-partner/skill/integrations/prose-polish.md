# Prose-Polish Integration

How to use the prose-polish skill for AI detection during voice calibration.

---

## When to Invoke

### Always

- After drafting any substantial section (300+ words)
- Before declaring a section "done"
- When user asks "does this sound like me?"
- When calibration mode flags potential issues

### Never

- During interview (no draft yet)
- On user's own words (don't second-guess their input)
- On minor edits (overkill)

---

## How to Invoke

```
Invoke prose-polish skill with the draft text.
```

Or reference in conversation:
```
"Let me run this through prose-polish for AI detection..."
```

---

## Interpreting Results

### Score Thresholds

| Score | Interpretation | Action |
|-------|---------------|--------|
| < 15 | Likely human | Minimal review, proceed |
| 15-25 | Borderline | Check flagged phrases against blocklist |
| 25-35 | Suspicious | Review with WritingSamples/ comparison |
| > 35 | Likely AI | Significant revision needed |

**Lee's threshold:** >25 warrants attention.

### What to Look For

Prose-polish provides:
- Overall AI-likelihood score
- Per-paragraph analysis
- Specific flagged phrases
- Craft assessment (rhythm, voice, commitment)

Cross-reference flagged phrases with `voice/blocklist.md`:
- If phrase is on blocklist → confirmed issue
- If phrase is not on blocklist but flagged → investigate pattern

---

## Two-Pass Workflow

### Pass 1: Draft (Writing Partner)

- Focus on getting ideas out
- Track threads
- Maintain voice heuristically (blocklist awareness)
- Don't interrupt for prose-polish

### Pass 2: Polish

1. Complete section or full draft
2. Run prose-polish
3. Review flags
4. Return to drafting mode for targeted revision
5. Re-run prose-polish to verify

```
Draft → Prose-Polish → Flags → Revise → Verify
```

---

## Handling Conflicts

### Prose-polish says "good" but voice feels off

Trust voice calibration. Prose-polish detects generic AI patterns; voice calibration is Lee-specific.

**Action:** Compare to WritingSamples/ manually. Look for:
- Rhythm mismatch
- Missing "I" ownership
- Generic instead of specific examples

### Prose-polish flags something Lee actually wrote

This can happen. Lee's style might occasionally match AI patterns.

**Action:**
1. Check if it's a quote or direct input from Lee
2. If so, mark as "trust my voice on this"
3. If not, investigate why it feels off

### Multiple low scores but draft feels hollow

Prose-polish measures detectable patterns. "Soullessness" is harder to quantify.

**Action:**
1. Read draft aloud
2. Compare to WritingSamples/ rhythm
3. Check for missing concrete examples
4. Look for "animating spirit"

---

## Reporting Format

When sharing prose-polish results:

```
Prose-polish analysis:

Overall score: 28 (above threshold)

Flagged passages:
- Paragraph 2: "It's important to note that..." (blocklist match)
- Paragraph 4: Low perplexity detected (too predictable)

Recommendation: Revise paragraphs 2 and 4 before finalizing.
```

---

## Integration with Voice Calibration

Prose-polish is Layer 2 in the detection pipeline:

1. **Layer 1:** Blocklist pattern matching (fast)
2. **Layer 2:** Prose-polish AI detection (comprehensive)
3. **Layer 3:** WritingSamples/ comparison (Lee-specific)

Run layers in order. If Layer 1 catches it, Layer 2 confirms. If Layer 2 flags something Layer 1 missed, investigate.

---

**See also:**
- `voice/blocklist.md` for pattern detection
- `integrations/writing-samples.md` for corpus comparison
