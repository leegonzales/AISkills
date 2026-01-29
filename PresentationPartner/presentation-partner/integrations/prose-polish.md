# Prose-Polish Integration

How to use the prose-polish skill for voice calibration in presentation narration.

---

## When to Invoke

### For Presentation Partner

- After drafting narration for a major section (3+ slides)
- Before finalizing the Talk Track
- When user asks "does this sound natural?"
- When calibration mode flags potential issues

### Never

- On user's own words (they said it, trust it)
- During Discovery interview (no draft yet)
- On single sentences (overkill)

---

## How to Invoke

Reference in conversation:
```
"Let me run this narration through prose-polish..."
```

Or invoke the skill:
```
skill: prose-polish
```

---

## Interpreting Results for Narration

### Adjusted Thresholds

Presentation narration has different characteristics than essay writing:
- Shorter sentences expected
- More direct address ("you")
- Deliberately simple vocabulary

| Score | Interpretation | Action |
|-------|---------------|--------|
| < 20 | Likely authentic | Minimal review |
| 20-30 | Borderline | Check against presentation-blocklist |
| 30-40 | Suspicious | Review specific phrases |
| > 40 | Likely AI-generated | Significant revision needed |

**Presentation threshold:** >25 warrants attention.

### What to Look For

Cross-reference flagged phrases with `references/presentation-blocklist.md`:
- Tier 1 matches → Immediate fix
- Tier 2 patterns → Review in context
- "Sounds written" → Simplify for spoken delivery

---

## Narration-Specific Checks

Beyond prose-polish scores, verify:

### Spoken Rhythm
- Read aloud—does it flow naturally?
- Any sentences requiring multiple breaths?
- Varied sentence length (not all same pattern)?

### Direct Address
- Appropriate use of "you" for audience
- Not excessive "I" (unless story-telling)
- Active voice preferred

### Specificity
- Real examples, not hypotheticals
- Concrete numbers, not vague quantities
- Named sources, not "studies show"

---

## Two-Pass Workflow

### Pass 1: Draft (Presentation Partner)

- Focus on content and structure
- Apply semantic tags
- Write from interview material
- Don't interrupt for prose-polish

### Pass 2: Polish

1. Complete section or full Talk Track
2. Extract audio blocks for review
3. Run prose-polish on combined narration
4. Cross-reference flags with blocklist
5. Revise flagged passages
6. Re-run to verify

```
Draft Audio → Extract → Prose-Polish → Flags → Revise → Verify
```

---

## Handling Conflicts

### Prose-polish says "good" but narration sounds stiff

Trust your ear. Prose-polish detects patterns; spoken delivery is different.

**Action:**
1. Read aloud
2. Mark awkward spots
3. Simplify for speaking

### Prose-polish flags direct quotes

The user's own words might match AI patterns.

**Action:**
1. Check if it's from Discovery interview
2. If user said it, keep it
3. Mark as "trust my voice on this"

### Low scores but flat delivery

Prose-polish measures detectable patterns, not "energy."

**Action:**
1. Check for semantic tags (especially [PAUSE])
2. Vary sentence rhythm
3. Add concrete examples

---

## Reporting Format

When sharing prose-polish results:

```
Narration Analysis (prose-polish):

Overall score: 24 (within threshold)

Flagged passages:
- Slide 3: "It's important to note..." (Tier 1 blocklist)
- Slide 5: Long compound sentence (spoken rhythm issue)

Clean passages:
- Opening hook: Score 12 (authentic)
- Closing CTA: Score 18 (acceptable)

Recommendations:
1. Replace Tier 1 phrase in slide 3
2. Split long sentence in slide 5 for spoken delivery
```

---

## Integration with Calibration Mode

Prose-polish is Layer 2 in the calibration pipeline:

1. **Layer 1:** Blocklist pattern matching (fast, presentation-specific)
2. **Layer 2:** Prose-polish AI detection (comprehensive)
3. **Layer 3:** Read-aloud test (human judgment)

Run layers in order. Blocklist catches presentation-specific tells, prose-polish catches general AI patterns, read-aloud catches spoken rhythm issues.

---

**See also:**
- `references/presentation-blocklist.md` - Pattern detection
- SKILL.md - Calibration mode details
