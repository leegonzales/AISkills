# Skill Template

Use this template when generating extracted skills. Follow the Anthropic Agent Skills specification.

## Required Structure

```
skill-name/
├── SKILL.md (required)
└── references/ (optional)
    └── [supporting docs]
```

## SKILL.md Format

```markdown
---
name: [lowercase-with-hyphens]
description: [What the skill does and when to use it. Include trigger phrases. Max 200 chars.]
---

# [Skill Name]

[One paragraph explaining the transformation this skill performs]

## Workflow

1. [Step 1 - what Claude does]
2. [Step 2 - what Claude does]
3. [Step 3 - what Claude does]

## Input Required

- [Required input 1]
- [Required input 2]
- Optional: [Optional input]

## Output Format

[Describe structure, length, tone]

## Example

### Input
[Sample input the user might provide]

### Output
[Complete example of what Claude produces]

## Quality Criteria

**Good:**
- [Criterion 1]
- [Criterion 2]

**Avoid:**
- [Anti-pattern 1]
- [Anti-pattern 2]
```

## Writing Guidelines

### Frontmatter

**name**: Lowercase with hyphens. Keep it short and descriptive.
- Good: `weekly-update-writer`
- Bad: `my_Weekly_Update_Writing_Skill`

**description**: This is the PRIMARY triggering mechanism. Include:
- What the skill does
- When to use it (trigger phrases)
- Keep under 200 characters

Example:
```
description: Transform meeting notes into stakeholder updates. Use when asked to "write my weekly update" or "summarize this week's progress."
```

### Body

- Use imperative/infinitive form ("Extract action items" not "Extracts action items")
- Be concise—Claude is already smart
- Include one complete example (input + output)
- Only add context Claude doesn't already know

### Progressive Disclosure

Keep SKILL.md under 500 lines. For longer skills:
- Move detailed references to `references/` folder
- Keep core workflow in SKILL.md
- Reference supporting files: "See references/advanced.md for edge cases"

## Conciseness Checklist

Before finalizing, ask:
- [ ] Does Claude really need this explanation?
- [ ] Does this paragraph justify its token cost?
- [ ] Can I show this with an example instead of explaining it?
- [ ] Am I duplicating knowledge Claude already has?

## Skill Quality Signals

**Strong skills:**
- Clear, specific trigger in description
- One focused workflow (not many things)
- Complete example with real input/output
- Explicit quality criteria

**Weak skills:**
- Vague description ("helps with writing")
- Too many workflows combined
- No examples
- No quality criteria
