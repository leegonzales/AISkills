# WritingSamples/ Integration

How to use the reference corpus for voice calibration and few-shot matching.

---

## Purpose

WritingSamples/ contains Lee's actual writing—the ground truth for voice calibration. Use it to:
- Check if draft phrasing matches Lee's style
- Pull few-shot examples for similar topics
- Ground voice guidelines in real writing
- Demonstrate alternatives when flagging issues

---

## Corpus Structure

```
WritingSamples/
├── essays/           # Published essays, blog posts
├── conversations/    # Transcripts that became writing
├── notes/            # Shorter observations, fragments
└── drafts/           # Works in progress (if relevant)
```

Each sample should include context (topic, date, voice mode if known).

---

## When to Reference

### Before Drafting

1. Identify topic/domain of planned section
2. Search WritingSamples/ for similar topics
3. Load 1-2 relevant samples as context
4. Note patterns to match

### During Calibration

1. When voice drift flagged
2. Pull sample showing how Lee writes about similar topic
3. Quote specific passages as evidence
4. Demonstrate difference between draft and sample

### When Suggesting Alternatives

1. After flagging an issue
2. Find sample with similar sentence structure/purpose
3. Show "here's how you wrote this" as model
4. Suggest revision following that pattern

---

## How to Select Samples

### Topic Matching

Search for keywords related to current section:

```
# Example: drafting about AI collaboration
Look for: "AI", "Claude", "collaboration", "writing", "prosthesis"
```

### Voice Mode Matching

If Lee's working in a specific voice mode (@strategist, @builder, etc.), prefer samples from same mode.

### Length Matching

For paragraph comparison:
- Pull paragraphs, not full essays
- Match approximate length to draft passage
- Extract 2-3 exemplar paragraphs

---

## What to Extract

### Sentence Rhythm

- Does Lee use short punchy sentences or longer flowing ones here?
- What's the mix? (e.g., short-short-long pattern)
- How does he vary rhythm?

### Opening Moves

- Does Lee start with a question? Bold assertion? Story?
- What's the first-sentence pattern in this type of content?

### Transition Style

- Explicit ("Now let's...") or implicit (topic shift)?
- How does Lee move between ideas?

### Example Use

- Concrete specifics or abstract concepts?
- Personal anecdotes or external references?
- How specific are the examples?

### Voice of Authority

- Confident assertion or exploratory wondering?
- First-person ownership or hedged claims?
- How much does Lee own his positions?

---

## Comparison Protocol

When comparing draft to sample:

```
1. Read sample paragraph(s)
2. Note 3-5 specific patterns (rhythm, openings, examples)
3. Read draft paragraph
4. Check each pattern against sample
5. Flag mismatches with evidence

Report format:

"Comparing to WritingSamples/essays/wardley-strategy.md:

Sample pattern: Lee starts with a direct question, then answers it.
Draft pattern: Starts with context-setting ("In order to understand...")

Sample: "Why does doctrine matter? Because..."
Draft: "In order to understand the importance of doctrine..."

Recommendation: Lead with the question, then answer it."
```

---

## Few-Shot Priming

When drafting new content, load relevant samples as context:

```
"Loading WritingSamples/essays/prose-polish-launch.md as voice reference.

Patterns to match:
- Direct, first-person voice
- Concrete examples from building experience
- Thinking-out-loud parentheticals
- Contrarian setup with evidence

Drafting with these patterns..."
```

This helps maintain voice consistency from first sentence.

---

## Building the Corpus

### Good Samples to Include

- Published essays Lee is proud of
- Conversations that captured his thinking well
- Notes that show his natural voice
- Pieces where "this sounds like me"

### Samples to Avoid

- Heavily edited corporate writing
- Collaborative pieces where voice is blended
- Very old writing (voice evolves)
- AI-assisted drafts (circular reference)

### Recommended Size

- Start with 10-20 diverse samples
- Cover different topics, lengths, and modes
- Add new samples as good writing emerges
- Target 50+ samples over time

---

## Maintenance

### Adding New Samples

When Lee produces writing he likes:
1. Add to appropriate category
2. Note date and context
3. Tag with topics/keywords
4. Consider voice mode

### Pruning Old Samples

If voice has evolved significantly:
1. Archive old samples (don't delete)
2. Mark as "historical voice"
3. Weight toward recent samples in comparison

---

**See also:**
- `voice/blocklist.md` for patterns to avoid
- `integrations/prose-polish.md` for AI detection
