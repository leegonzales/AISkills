# Creative Fiction AI Detection Patterns

Extension of ProsePolish for narrative fiction, including patterns specific to AI-generated creative writing that may not appear in technical or business contexts.

**Source:** Adapted from a paranormal romance author's AI detection workflow, incorporating research from GPTZero, VERMILLION framework, and genre-specific analysis.

---

## Philosophy for Creative Fiction

Creative fiction has different quality signals than technical or business writing:
- **Voice > Authority:** A distinctive narrative voice matters more than demonstrated expertise
- **Embodiment > Clarity:** The reader should feel the story through the character's body
- **Surprise > Structure:** Predictability is a greater sin than imperfect organization
- **Risk > Safety:** Characters (and prose) should take emotional risks

---

## Fiction-Specific Structural Tells

### Echo Repetition for False Profundity

**Pattern:** Repeating a word or phrase from dialogue as a standalone paragraph to manufacture emotional depth.

**AI-Typical Examples:**
```
"Together, then," I said.

Together.
```

```
"This changes everything."

Everything.
```

```
"I love you," he whispered.

Love.
```

**Why it fails:** This is mechanical profundity. AI uses this pattern constantly because it thinks single-word echoes create emotional resonance. Instead, it reads as manufactured drama—the prose equivalent of dramatic ellipsis (...).

**Threshold:** Zero tolerance in creative fiction. If you find this pattern, it's almost certainly AI-generated.

**When repetition WORKS:**
- Character genuinely echoing/questioning: "Together? After everything?"
- Internal thought that expands: "Together. The word felt both terrifying and right."
- Intentional rhythmic device where the echo adds meaning, not just emphasis

**Fix:** Delete the echo entirely, or expand it into a full thought.

---

### "Was Enough" False Completion

**Pattern:** Using "[X] was enough" to signal emotional resolution without earning it.

**AI-Typical Examples:**
```
His touch was enough.

The silence was enough.

Being here was enough.

This—right now—was enough.

For now, it was enough.
```

**Why it fails:** AI uses this to manufacture emotional depth. It tells the reader "this is meaningful" instead of showing why it matters. No emotional texture, no specificity, no earned feeling.

**Threshold:** Zero, or use VERY sparingly (once per book) and only when deeply earned.

**When it might work (rare):**
- After extensive emotional buildup where character has struggled with "enough"
- When subverted: "His touch should have been enough. It wasn't."
- When expanded: "His hand on mine was enough to steady me, to remind me I wasn't alone."

**Fix:** Delete entirely, or show what the character experiences instead of declaring it "enough."

---

### Staccato Drama Clusters

**Pattern:** Five or more consecutive short sentences (under 8 words) attempting to manufacture intensity.

**AI-Typical Example:**
```
You tried. You learned. You improved. That matters. You survived. You grew. You became.
```

**Why it fails:** AI picked this cadence from social media and self-help prose. In small doses, staccato rhythm creates emphasis. Overused, it feels like a script trying to manufacture emotion.

**Threshold:** Maximum 3-4 consecutive short sentences without a longer sentence breaking the pattern.

**Fix:** Keep your best short punch. Expand at least one of the others into a fuller thought.

**Note:** Characters being dramatic in dialogue might speak in staccato bursts—that's voice. In narration, watch the density.

---

### Participial Phrase Overload

**Pattern:** "Main clause, [verb]-ing phrase" construction appearing repeatedly.

**AI-Typical Examples:**
```
She crossed the room, her heart pounding in her chest.
He smiled, his eyes crinkling at the corners.
I stepped back, my breath catching in my throat.
```

**Why it fails:** This construction appears 2-5x more in AI text than human writing. One per scene is fine. Multiple in the same paragraph creates robotic rhythm.

**Detection:** Search for ", [verb]ing" patterns. Check density.

**Fix:** Vary the structure:
- Move participial phrase to beginning
- Convert to separate sentence
- Use different construction entirely

---

### Formulaic Chapter Endings

**Pattern:** AI tends to end chapters on an "upbeat forward-looking rosy glow"—hopeful, resolved, inspirational.

**Signs of formulaic endings:**
- Characters restating hope/determination
- Emotional resolution that should carry into next chapter
- Inspirational internal monologue
- Everything tied up neatly

**Why it fails:** AI's positivity bias. Even in bleak stories, AI defaults to resolved endings. This kills tension and makes every ending feel the same.

**What fiction needs:** Unresolved tension, lingering questions, emotional hooks pulling readers forward.

**Detection:** Do your chapter endings vary in emotional register? Some should be hopeful, some anxious, some angry, some unresolved.

---

## Fiction-Specific Phrase Patterns

### Emotional Placeholders

Phrases that fill space where specific emotion should be:

- "I'd take it" / "I'll take it" (as acceptance)
- "At least we were together"
- "Something like [emotion]" ("something like hope")
- "If nothing else"
- "For what it's worth"
- "Despite everything"
- "Against all odds"
- "More than I cared to admit"
- "Part of me [felt/knew/wondered]" (overuse is the problem)

---

### Empathy Pivots

**Pattern:** Performative emotional awareness—narrating the decision to feel empathy rather than showing it.

**AI-Typical Examples:**
```
I reminded myself that he had feelings too.
It was important to remember that everyone was dealing with their own struggles.
I tried to see it from his perspective.
```

**Why it fails:** Tells us the character is empathetic rather than showing empathy through action or reaction.

**Fix:** Show empathy through behavior, not announcement.

**Example - Before:**
"I reminded myself that Ryu had his own pain, his own reasons for being difficult."

**Example - After:**
"Ryu's jaw was tight, that muscle jumping the way it did when he was holding something back. Whatever was driving his mood, it wasn't about me."

---

### Metaphor Mixing

**Pattern:** Stacking incompatible metaphor domains in the same passage.

**AI-Typical Examples:**
```
I navigated the storm of emotions while diving deep into my feelings.
The fire of his gaze pierced through the walls I'd built.
My heart was a battlefield where hope waged war against the shadows.
```

**Rule:** Commit to ONE metaphor domain per passage, or use literal language.

**Fixed:**
"His gaze burned through every defense I had." (fire domain only)

OR literal:
"He looked at me, and I couldn't hold it—couldn't keep pretending I didn't feel anything."

---

### Setting Description Clichés

Generic descriptions that any AI could produce:

- "nestled" (especially "nestled in the heart of")
- "bustling" (every city is "bustling")
- "picturesque"
- "quaint"
- "charming"

---

### Abstract Metaphor Clichés

- "tapestry" (especially "rich tapestry")
- "symphony" (of flavors, emotions)
- "beacon" (of hope)
- "labyrinth" / "labyrinthine"
- "crucible"
- "mosaic"
- "landscape" (when not literal geography)

---

## Voice Drift Detection

### What Voice Drift Looks Like

Character voice shifts unexpectedly—protagonist suddenly sounds formal, supporting character becomes verbose, antagonist loses their edge.

**Causes:**
- Switching between writing sessions without re-reading
- AI generation defaulting to neutral register
- Fatigue leading to flatter prose

### Detection Method

Read a scene and ask:
- Does this sound like [character]?
- Would they use these specific words?
- Is sentence complexity consistent with their established voice?

### Character-Specific Markers

Track distinctive speech patterns for each character. When those patterns disappear, voice has drifted.

**Example markers:**
- Sharp/sarcastic characters losing their edge
- Sparse speakers becoming verbose
- Formal characters becoming casual
- Casual characters becoming formal
- Arrogant characters becoming polite

---

## Punctuation Patterns for Fiction

### Em Dash Usage

**AI Pattern:** Uses em dashes (—) formulaically for false emphasis.

**Recommended Threshold for Fiction:**
- **Narration:** Maximum 1 per 500 words (some authors recommend zero tolerance)
- **Dialogue interruptions:** Unlimited (this is correct usage)

**When dashes work:**
- Interruption in dialogue or thought
- Dramatic pause before reveal
- Breaking a long sentence for rhythm

**When dashes fail:**
- Multiple dashes in same paragraph
- Every other sentence using dash for "impact"
- Where comma or period would work fine

---

## Show vs. Tell Regression

**Pattern:** AI tells emotions directly instead of showing through body and action.

**AI-Typical:**
```
I felt nervous and excited.
She was angry.
He seemed sad.
```

**Better:**
```
My hands wouldn't stop shaking.
Her words could have cut glass.
He looked away, and something in his shoulders collapsed.
```

**Detection:** Search for "felt [emotion]," "was [emotion]," "seemed [emotion]" in narration.

---

## Connective Usage Diagnostic

**Research finding:** AI uses "however" 3x more than humans. Humans prefer "because" (15x more), "so" (10x more), and "if" (5x more).

**What this means for fiction:** Overuse of "however" creates formal, essay-like tone. "Because," "so," and "if" feel more natural in character voice.

**Quick check:** Search for "however" in narrative (not dialogue). More than 1-2 per chapter suggests AI assistance.

**Replace with:**
- "But" (simpler, more conversational)
- Restructure to show causation
- Delete if contrast is clear from context

---

## Quality Tests for Fiction

Every polished scene should pass all five:

### 1. Read-Aloud Test
Does it sound like human breath and thinking? No stumbling points, natural rhythm.

### 2. Surprise Test
Is there at least ONE sentence you didn't see coming? An unexpected word choice, fresh turn of phrase, reaction that subverts expectation.

### 3. Specificity Test
Does the prose include concrete sensory details? Specific colors, textures, sounds. Details that could only exist in THIS moment.

### 4. Risk Test
Does the POV character make at least one bold claim or take an emotional risk? States an opinion without hedging, commits to an emotion fully, shows vulnerability.

### 5. Embodiment Test
Does this feel like it came from someone with a body? Physical grounding, bodily sensations, reactions that feel lived rather than observed.

---

## Genre-Specific Thresholds for Fiction

| Pattern | Fiction Threshold | Notes |
|---------|-------------------|-------|
| Sentence variance | StdDev >8 words | Higher variance expected |
| Hedge tolerance | Low | POV characters should be decisive about own feelings |
| Passive voice | Low | Active voice for immediacy |
| Em dashes (narration) | Max 1/500 words | Some authors: zero |
| "However" | Max 1-2/chapter | Use "but" or restructure |
| Parallel constructions | Max 1/scene | Break up formulaic rhythm |
| "In that moment" | Max 1/chapter | Overused temporal marker |
| "Part of me" | Max 2/chapter | Overused hedge |

---

## Integration Notes

### Adapting Business/Technical Patterns

These ProsePolish patterns DON'T apply to fiction:
- Authority cosplay (no "research shows" in fiction)
- Delegated authority (no citations needed)
- Business jargon detection (unless character-appropriate)
- Academic formality

These patterns DO apply:
- Structural rhythm (fully applicable)
- Hedge stacking (with fiction adjustments)
- Parallel construction limits
- Repetition pattern detection
- Decorative specificity

### Creative Fiction Effectiveness Weights

Suggested dimension weights for creative fiction:
- Craft: 15%
- Coherence: 20%
- Authority: 10%
- Purpose: 15%
- **Voice: 40%**

Voice dominates because distinctive character voice is the primary quality signal in fiction.

---

## Research Sources

- [GPTZero Detection Methodology](https://gptzero.me) - Perplexity and burstiness metrics
- [University College Cork Study](https://www.ucc.ie/en/news/2025/new-study-reveals-that-ai-cannot-fully-write-like-a-human.html) - Literary stylometry
- [The Ten Telltale Signs of AI-Generated Text](https://www.theaugmentededucator.com/p/the-ten-telltale-signs-of-ai-generated)
- [13 Signs You Used ChatGPT To Write That](https://seanjkernan.substack.com/p/13-signs-you-used-chatgpt-to-write)
- [The 6 Warning Signs Of An AI-generated Book](https://stevefenton.co.uk/blog/2025/01/generated-books/)
- [VERMILLION Framework](https://researchleap.com/the-disappearing-author-linguistic-and-cognitive-markers-of-ai-generated-communication/) - Linguistic markers
- [AI Writing Detection Guide](https://lithub.com/heres-a-handy-guide-to-help-you-spot-ai-writing/)

---

*Contributed by creative fiction practitioner. Patterns derived from paranormal romance editing workflow with AI-assisted drafting.*
