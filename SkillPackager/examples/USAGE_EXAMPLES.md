# Skill Packaging Usage Examples

## Example 1: Package Dad Joke Validator

```bash
cd AISkills
./SkillPackager/scripts/package-skill.sh DadJokeValidator/dad-joke-validator
```

**Result:**
- `dad-joke-validator-v1.1.0.skill` (53K)
- `dad-joke-validator-v1.1.0.skill.sha256`
- `dad-joke-validator-v1.1.0.metadata.json`

## Example 2: Package All Skills in Collection

```bash
./SkillPackager/scripts/batch-package.sh \
    DadJokeValidator/dad-joke-validator \
    ProsePolish/prose-polish \
    GeminiPeerReview/gemini-peer-review \
    CodexPeerReview/codex-peer-review \
    ConceptForge/concept-forge \
    ProcessMapper/process-mapper \
    ResearchToEssay/research-to-essay \
    Claimify/claimify \
    ContextContinuity/context-continuity
```

## Example 3: Package and Test New Skill

```bash
# Create from template
cp -r SkillTemplate/skill-template MySkill/my-skill
cd MySkill/my-skill

# Customize skill
# ... edit SKILL.md, README.md, etc.

# Validate
../../SkillTemplate/scripts/validate-skill.sh .

# Package
../../SkillPackager/scripts/package-skill.sh .

# Test
../../SkillPackager/scripts/test-skill-installation.sh ../dist/my-skill-v1.0.0.skill
```

## Example 4: Pre-Release Workflow

```bash
# 1. Update version in CHANGELOG.md
echo "## [1.2.0] - $(date +%Y-%m-%d)" >> my-skill/CHANGELOG.md
echo "### Added" >> my-skill/CHANGELOG.md
echo "- New feature" >> my-skill/CHANGELOG.md

# 2. Package
./scripts/package-skill.sh my-skill

# 3. Test installation
./scripts/test-skill-installation.sh dist/my-skill-v1.2.0.skill

# 4. Commit and tag
git add -A
git commit -m "Release v1.2.0"
git tag v1.2.0
git push && git push --tags
```

## Example 5: CI/CD Integration

```yaml
# .github/workflows/package-skills.yml
name: Package Skills

on:
  push:
    tags:
      - 'v*'

jobs:
  package:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Package all skills
        run: |
          ./SkillPackager/scripts/batch-package.sh

      - name: Test packages
        run: |
          for skill in dist/*.skill; do
            ./SkillPackager/scripts/test-skill-installation.sh "$skill"
          done

      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: skill-packages
          path: dist/*.skill*
```

## Example 6: Troubleshooting Failed Package

```bash
# Run with verbose output
set -x
./scripts/package-skill.sh my-skill 2>&1 | tee package.log

# Check validation errors
./SkillTemplate/scripts/validate-skill.sh my-skill

# Check for unfilled placeholders
grep -r "{{" my-skill --include="*.md"

# Test YAML parsing
python3 ./SkillTemplate/scripts/test-skill-loading.py my-skill
```
