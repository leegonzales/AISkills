# AISkills

A collection of Claude Skills - specialized system prompts that extend AI capabilities for specific domains.

## Project Structure

```
{SkillName}/
  {skill-slug}/
    SKILL.md          # Core skill definition (required)
    README.md         # Human documentation
    references/       # Progressive disclosure content
    scripts/          # Helper scripts (if any)
```

## Development

```bash
# Validate skill structure
./SkillPackager/scripts/validate-skill.sh {SkillName}/{skill-slug}

# Package for distribution
./SkillPackager/scripts/package-skill.sh {SkillName}/{skill-slug}
```

## Creating Skills

1. Copy `SkillTemplate/example-skill/` to `{NewSkillName}/{skill-slug}/`
2. Edit `SKILL.md` with your skill definition
3. Add references/ for detailed content (progressive disclosure)
4. Update `SKILLS.md` skill registry

## Critical Rules

- **SKILL.md is the source of truth** - Claude reads this when skill is invoked
- **Keep SKILL.md focused** - use references/ for detailed protocols
- **Directory naming**: PascalCase for folder, kebab-case for slug
- **Never commit secrets** - check .gitignore

## Skill Registry

See `SKILLS.md` for the complete skill manifest (41 skills).

## Reference Documentation

When working on specific tasks, read:
- `agent_docs/creating-skills.md` - How to create new skills
- `agent_docs/packaging.md` - Packaging and distribution
- `agent_docs/quality.md` - Quality standards and evaluation

For detailed specifications:
- `docs/SKILL-8-SPEC.md` - Full skill format specification
- `docs/skill-evaluation-rubric.md` - Detailed evaluation rubric
- `ClaudeProjectDocs/claude-project-docs/SKILL.md` - Documentation best practices
