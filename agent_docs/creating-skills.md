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

## Frontmatter Rules (Agent Skills spec)

**Required fields:**
- `name` - kebab-case identifier, ≤64 chars, lowercase/numbers/hyphens only, no reserved words (`anthropic`, `claude`). Gerund form preferred (`processing-pdfs`). Must match the directory slug.
- `description` - ≤1024 chars, **third person**, states *what it does AND when to use it* (it's injected into the system prompt and drives skill selection). Good: "Extracts text and tables from PDF files. Use when working with PDFs or forms." Avoid first/second person ("I can help...", "You can use...").

**Optional standard fields (spec-portable):**
- `license` - e.g., `MIT`, `Apache-2.0`
- `metadata` - arbitrary key-value; **this is where `version`, `owner`, `reviewed_at` belong** (not top-level)
- `compatibility` - environment requirements (e.g., Python 3.14+)
- `allowed-tools` - space-delimited pre-approved tools (experimental; a security surface — scope it tight)

**Never at top level:**
- `version:` - put it under `metadata:` (or use CHANGELOG.md). A top-level `version:` fails `validate-skill.sh`.
- `author:` - use the LICENSE file.

## Evaluation-First Development

Build the eval **before** writing extensive docs — otherwise you document imagined problems, not real ones.

1. **Identify the gap:** run Claude on representative tasks *without* the skill; note specific failures.
2. **Write 3+ evals:** `{query, files, expected_behavior[]}` capturing those gaps.
3. **Baseline:** measure no-skill performance.
4. **Write minimal instructions** to close the gap and pass the evals.
5. **Iterate:** re-run, compare skill-vs-no-skill, refine. For behavioral hardening use `SkillForge/skill-forge` (Tier B).

Test across the models you'll use it with (Haiku needs more spelled out than Opus).

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

1. **Top-level `version:`** - Put it under `metadata:` (or CHANGELOG.md), never top-level
2. **Too much in SKILL.md** - Use references/ for detail (body <500 lines)
3. **Missing triggers** - Description must say "Use when..." in third person
4. **Wrong naming** - Must be kebab-case, match directory, no reserved words
5. **Deeply nested references** - Keep references one level deep from SKILL.md; Claude partial-reads nested files. Add a table of contents to any reference file >100 lines.
6. **Too many options** - Give one default with an escape hatch, not "use A or B or C or D"
7. **Time-sensitive info** - No "before August 2025..." in the body; use a collapsed "old patterns" section
8. **Unclear code role** - State whether Claude should *execute* a script or *read it as reference*
9. **Unqualified MCP tools** - Always `ServerName:tool_name`, never bare tool names
10. **Windows paths** - Forward slashes only (`scripts/x.py`)

## Degrees of Freedom

Match instruction specificity to task fragility:
- **High freedom (prose):** open field, many valid paths — code review, synthesis.
- **Low freedom (exact scripts, "do not modify"):** narrow bridge, one safe way — migrations, destructive/batch ops. For those, use plan → validate → execute with a verifiable intermediate file.

## Integration

After creating, update:
1. `SKILLS.md` - Add to skill registry table
2. Test with `skill: "skill-slug"` in Claude Code
