# Skill Extractor

Transform conversation patterns into reusable Claude skills.

## What It Does

When you find yourself repeatedly asking Claude to do the same type of task, this skill helps you:

1. **Identify** the repeatable pattern in your conversations
2. **Extract** the workflow into a structured SKILL.md file
3. **Test** the skill to ensure it works consistently
4. **Refine** based on results

## Usage

**In Claude:**
```
I keep asking Claude to turn meeting notes into weekly updates. Can you extract that into a skill?
```

**Or share conversation excerpts:**
```
Here's a conversation where Claude did a task I'd like to repeat:
[paste conversation]

Can you turn this into a reusable skill?
```

## Trigger Phrases

- "Turn this into a skill"
- "Extract a skill from this"
- "I keep doing this same task"
- "Make this repeatable"

## Output

You'll receive:
- Complete **SKILL.md** file
- **Test prompt** to verify it works
- **Usage examples**
- **Refinement notes** for iteration

## Examples

See `references/example-extractions.md` for real before/after examples:
- Meeting notes → Weekly update writer
- Customer feedback → Theme analyzer
- Meeting transcript → Action item extractor

## Best Candidates for Extraction

✅ **Good:**
- Tasks done 3+ times with similar structure
- Clear input → output transformation
- Required specific prompting to work well

❌ **Skip:**
- One-off creative tasks
- Simple Q&A with no workflow
- Tasks requiring external data Claude can't access

## File Structure

```
SkillExtractor/
└── skill-extractor/
    ├── SKILL.md                    # Core skill definition
    ├── README.md                   # This file
    └── references/
        ├── skill-template.md       # Template for generated skills
        └── example-extractions.md  # Before/after examples
```

## Related Skills

- **Prose Polish** — Improve extracted skill documentation
- **Claude Project Docs** — Create full project documentation
