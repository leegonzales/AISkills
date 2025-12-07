# Packaging Skills

How to package skills for distribution using the SkillPackager tooling.

## Quick Commands

```bash
# Validate before packaging
./SkillPackager/scripts/validate-skill.sh SkillName/skill-slug

# Package single skill (auto-detects version from CHANGELOG.md)
./SkillPackager/scripts/package-skill.sh SkillName/skill-slug

# Package with explicit version
./SkillPackager/scripts/package-skill.sh SkillName/skill-slug 1.2.0

# Package all skills
./SkillPackager/scripts/batch-package.sh

# Test packaged skill
./SkillPackager/scripts/test-skill-installation.sh dist/skill-slug-v1.0.0.skill
```

## Output Files

For each packaged skill, creates in `dist/`:

| File | Purpose |
|------|---------|
| `skill-slug-vX.Y.Z.skill` | ZIP package |
| `skill-slug-vX.Y.Z.skill.sha256` | Checksum for verification |
| `skill-slug-vX.Y.Z.metadata.json` | Package metadata |

## Version Detection

Version is auto-detected from `CHANGELOG.md`:

```markdown
# Changelog

## [1.2.0] - 2025-12-07

### Added
- New feature
```

Extracts `1.2.0` from first `## [X.Y.Z]` line. Defaults to `1.0.0` if no CHANGELOG.

## Validation Checks

**Pre-packaging:**
- YAML frontmatter syntax
- Required fields (name, description)
- Name format (lowercase, hyphens)
- No unfilled placeholders
- Valid UTF-8 encoding
- Valid JSON in assets/
- Valid Python syntax in scripts/

**Post-packaging:**
- Package extracts successfully
- SKILL.md present and valid
- No development artifacts

## Auto-Excluded Files

These are automatically excluded from packages:
- `*.pyc`, `__pycache__/`
- `.DS_Store`, `.git/`
- `.pytest_cache/`
- `dist/`, `.venv/`, `venv/`
- `node_modules/`
- `.idea/`, `.vscode/`

## Workflow

```bash
# 1. Create/update skill
vim SkillName/skill-slug/SKILL.md

# 2. Update CHANGELOG with new version
vim SkillName/skill-slug/CHANGELOG.md

# 3. Validate
./SkillPackager/scripts/validate-skill.sh SkillName/skill-slug

# 4. Package
./SkillPackager/scripts/package-skill.sh SkillName/skill-slug

# 5. Test
./SkillPackager/scripts/test-skill-installation.sh dist/skill-slug-v*.skill

# 6. Commit dist/ artifacts
git add dist/
git commit -m "chore: Package skill-slug v1.2.0"
```

## Common Errors

**"Validation failed"**
- Check YAML frontmatter syntax
- Ensure `name` and `description` fields exist
- Remove any `{{placeholder}}` text

**"Invalid field 'version' in frontmatter"**
- Remove `version:` from SKILL.md frontmatter
- Use CHANGELOG.md for versioning instead

**"Skill directory not found"**
- Check path includes both SkillName and skill-slug directories

## Requirements

- Bash 4.0+
- zip command
- shasum (or sha256sum)
- Python 3 (for validation)
