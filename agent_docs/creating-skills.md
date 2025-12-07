# Creating Skills

How to create new Claude skills for the AISkills collection.

## Quick Start

```bash
# 1. Copy template
cp -r SkillTemplate/example-skill NewSkillName/skill-slug

# 2. Edit SKILL.md
# 3. Add references/ content
# 4. Validate
./SkillPackager/scripts/validate-skill.sh NewSkillName/skill-slug
```

## Directory Structure

```
NewSkillName/           # PascalCase
  skill-slug/           # kebab-case (matches SKILL.md name field)
    SKILL.md            # Required - core skill definition
    README.md           # Human-facing documentation
    LICENSE             # MIT recommended
    CHANGELOG.md        # Version history
    references/         # Progressive disclosure content
      examples.md
      patterns.md
    scripts/            # Helper scripts (optional)
```

## SKILL.md Structure

```markdown
---
name: skill-slug
description: One sentence describing when to use this skill. Use when [trigger conditions].
---

# Skill Name

Brief description of capability.

## When to Use

Invoke when user:
- [Trigger phrase 1]
- [Trigger phrase 2]

## Core Workflow

[Main process or methodology]

## Output Format

[Expected output structure]

## References

For detailed protocols, see:
- `references/examples.md`
```

## Frontmatter Rules

**Required fields:**
- `name` - kebab-case identifier (e.g., `prose-polish`)
- `description` - One sentence with trigger conditions

**Never include:**
- `version` - Use CHANGELOG.md instead
- `author` - Use LICENSE file

## Progressive Disclosure

Keep SKILL.md focused (~100-300 lines). Move detailed content to `references/`:

| File | Content |
|------|---------|
| `examples.md` | Usage examples with inputs/outputs |
| `patterns.md` | Pattern libraries, templates |
| `protocols.md` | Detailed step-by-step procedures |
| `research.md` | Background research, sources |

## Naming Conventions

- **Directory:** `PascalCase` (e.g., `ProsePolish`)
- **Skill slug:** `kebab-case` (e.g., `prose-polish`)
- **Files:** lowercase with hyphens

## Validation Checklist

Before submitting:
- [ ] SKILL.md has valid YAML frontmatter
- [ ] `name` field matches directory slug
- [ ] `description` includes trigger conditions
- [ ] No placeholders ({{...}}) remain
- [ ] All files are UTF-8 encoded
- [ ] CHANGELOG.md has version entry
- [ ] README.md documents installation

## Common Mistakes

1. **Version in frontmatter** - Use CHANGELOG.md, not `version:` field
2. **Too much in SKILL.md** - Use references/ for detail
3. **Missing triggers** - Description must say "Use when..."
4. **Wrong naming** - Must be kebab-case, match directory

## Integration

After creating, update:
1. `GEMINI.md` - Add to skill registry table
2. Test with `skill: "skill-slug"` in Claude Code
