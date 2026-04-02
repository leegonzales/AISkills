# Voice Print Protocol

## How to Analyze Writing Samples

When the user provides writing samples, extract these dimensions:

### 1. Sentence Architecture
- **Length**: Average word count per sentence. Short (5-10), Medium (10-20), Long (20+)
- **Complexity**: Simple declarative? Compound? Nested clauses?
- **Rhythm**: Consistent length or varied? Punchy staccato or flowing prose?

### 2. Tone Signature
- **Formality**: Scale 1-5 (1=texting a friend, 5=board presentation)
- **Warmth**: Scale 1-5 (1=all business, 5=relationship-first)
- **Confidence**: Scale 1-5 (1=hedging/qualifying, 5=direct assertions)
- **Humor**: None / Dry / Playful / Frequent

### 3. Vocabulary Fingerprint
- **Jargon density**: None / Light / Heavy
- **Favorite words/phrases**: Capture recurring terms
- **Words they never use**: Note absence of common corporate terms
- **Emoji/punctuation style**: None / Minimal / Frequent. Exclamation points? Ellipses?

### 4. Structure Patterns
- **Opening style**: Jump straight in? Greeting first? Context-setting?
- **Closing style**: Action items? Sign-off? Just stop?
- **Paragraph length**: Short (1-2 sentences) / Medium (3-4) / Long (5+)
- **List usage**: Bullets? Numbers? Inline?

### 5. Anti-Patterns (What They Don't Do)
Look for absence of:
- Corporate buzzwords ("synergy", "leverage", "circle back")
- Passive voice
- Hedge words ("maybe", "perhaps", "I think")
- Filler phrases ("just wanted to", "hope this helps")
- Excessive qualifiers

---

## Voice Print Rules Format

Generate rules as a numbered list, 5-8 items. Each rule should be:
- **Specific**: Not "be casual" but "use contractions, skip formal greetings, open with the point"
- **Actionable**: Claude can follow it without interpretation
- **Contrastive**: What TO do and what NOT to do

### Template:

```markdown
## [Name]'s Voice Print

1. **Tone**: [Specific description]. [Example of what this sounds like].
2. **Sentence style**: [Length, complexity, rhythm]. [What to avoid].
3. **Opening messages**: [How they start]. Never [what they don't do].
4. **Vocabulary**: [Jargon level, favorite terms]. Avoid [specific words/phrases].
5. **Structure**: [How they organize thoughts]. [Formatting preferences].
6. **Confidence level**: [How direct]. [Hedging rules].
7. **Sign-off style**: [How they close]. [What to skip].
8. **[Custom rule]**: [Anything unique to this person's style].
```

---

## Example Analysis

**Sample input** (Slack messages from a VP Engineering):

> "heads up — deploy is blocked on the auth migration. talked to devon, they're targeting thursday but no guarantees. I told them we need it by EOD wednesday or we slip the release.
>
> separately — the perf review calibrations are done. sending the summary to your DMs. couple surprises in there, mostly good."

**Extracted voice print**:

1. **Tone**: Direct and informal. No greetings, no pleasantries — straight to the point. Lowercase "i" is fine. Warmth comes through in casual phrasing, not formal courtesy.
2. **Sentence style**: Short to medium (8-15 words). No complex clauses. Conversational rhythm — reads like talking.
3. **Opening messages**: Lead with the headline or a heads-up. Never "Hi team" or "Hope you're doing well."
4. **Vocabulary**: Light jargon (deploy, auth migration, perf review). No buzzwords. Uses em dashes for asides. "couple" not "a couple of."
5. **Structure**: Topic per paragraph, separated by "separately" or line breaks. No bullet points in casual messages. No headers in Slack.
6. **Confidence level**: High. States facts and actions taken. "I told them" not "I suggested." Uses "no guarantees" not "there might be some risk."
7. **Sign-off style**: None. Message just ends when the information is delivered.
8. **Emotional register**: Measured even when delivering bad news. "couple surprises in there, mostly good" — understated, not dramatic.

---

## Voice Print Rewrite Examples

After generating the voice print, show 3 rewrites:

### Format:

**Generic Claude**: [How Claude would normally write it]

**In your voice**: [Same content rewritten with their voice rules applied]

This proves the voice print works and gives the user something concrete to react to.

### Example:

**Generic Claude**: "I've reviewed the quarterly metrics and identified several areas of concern. The customer churn rate has increased by 15% compared to last quarter, which may warrant further investigation. I'd recommend scheduling a meeting with the customer success team to discuss potential interventions."

**In their voice**: "churn is up 15% from last quarter — not great. CS team needs to dig into this. I'd set up a call with them this week to figure out what's driving it and what we're doing about it."
