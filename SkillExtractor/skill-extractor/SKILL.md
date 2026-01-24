---
name: skill-extractor
description: Extract reusable skills from conversation patterns. Use when asked to "turn this into a skill," "extract a skill," or "I keep doing this task repeatedly."
---

# Skill Extractor

Transform repeated conversation patterns into reusable SKILL.md files.

## Workflow

### 1. Gather Evidence

Ask: "Share a conversation excerpt where Claude did this task well, or describe a task you do repeatedly."

Accept:
- Pasted conversation excerpts
- Task descriptions with examples
- Multiple examples to find common patterns

### 2. Identify the Pattern

Analyze for these elements:

| Element | Find This |
|---------|-----------|
| **Trigger** | What phrase starts this workflow? |
| **Input** | What does user provide? |
| **Transform** | What does Claude do with it? |
| **Output** | What format/structure results? |
| **Quality** | What separates good from bad? |

### 3. Validate

Confirm: "It sounds like you want to [workflow]. Is that right?"

Refine: "What would you change? What context made it work?"

### 4. Generate SKILL.md

Output a complete skill file following the format in `references/skill-template.md`.

### 5. Test

Run the extracted skill on fresh input. Iterate until it works reliably.

## Skill Archetypes

| Type | Pattern | Example |
|------|---------|---------|
| **Transformer** | Format A → Format B | Notes → Email |
| **Analyzer** | Input → Assessment | Code → Review |
| **Generator** | Parameters → Content | Topic → Blog |
| **Synthesizer** | Many → One | Feedback → Themes |

## Viability Check

**Strong candidates:**
- Done 3+ times with similar structure
- Clear input → output transformation
- Required specific prompting to work
- Explainable to a colleague

**Weak candidates:**
- One-off creative tasks
- Simple Q&A (no workflow)
- Requires external data
- Too vague to define success

## Output Deliverables

Provide:
1. **SKILL.md** — Complete, ready to use
2. **Test prompt** — Verify it works
3. **Usage examples** — How to invoke
4. **Refinement notes** — Next iteration

## Example Extraction

**User says:** "I keep asking Claude to turn meeting notes into weekly updates."

**Extracted pattern:**
- Trigger: "write weekly update" / "summarize this week"
- Input: Bullet points from meetings
- Transform: Organize by Accomplishments/In Progress/Blockers
- Output: Professional email format
- Quality: Outcome-focused, not activity-focused

**Result:** See `references/example-extractions.md` for the full `weekly-update-writer` skill.

## References

- `references/skill-template.md` — Standard skill format
- `references/example-extractions.md` — Before/after examples
