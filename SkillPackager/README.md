# Skill Packaging Automation (SKILL-9)

**Automated packaging tooling for Claude Code skills**

Zero-configuration packaging with validation, ZIP creation, and SHA256 checksums. Eliminates manual packaging errors.

## Quick Start

```bash
# Package a single skill
./scripts/package-skill.sh ../DadJokeValidator/dad-joke-validator

# Package all skills in current directory
./scripts/batch-package.sh

# Test a packaged skill
./scripts/test-skill-installation.sh ../dist/dad-joke-validator-v1.1.0.skill
```

## Features

### package-skill.sh
- **Auto-detect version** from CHANGELOG.md
- **Validate before packaging** (YAML, UTF-8, placeholders, JSON, Python)
- **Smart exclusions** (*.pyc, __pycache__, .DS_Store, .git, etc.)
- **SHA256 checksum** generation
- **Metadata JSON** with package info
- **Clear error messages** and validation feedback

### batch-package.sh
- **Auto-discover skills** (finds all */SKILL.md)
- **Batch packaging** with progress reporting
- **Summary statistics** (success/fail counts)
- **Error handling** for individual skill failures

### test-skill-installation.sh
- **Extract and validate** packaged skills
- **YAML frontmatter validation**
- **Required file checks**
- **Development artifact detection**
- **Pass/fail reporting**

## Usage Examples

### Package a Single Skill

```bash
# Auto-detect version from CHANGELOG.md
./scripts/package-skill.sh ../DadJokeValidator/dad-joke-validator

# Specify version explicitly
./scripts/package-skill.sh ../DadJokeValidator/dad-joke-validator 1.1.0
```

**Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Claude Code Skill Packager
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ℹ️  Skill Directory: /path/to/dad-joke-validator
ℹ️  Skill Name: dad-joke-validator

📌 Step 1: Detecting version...
ℹ️  Version from CHANGELOG.md: 1.1.0
ℹ️  Packaging version: v1.1.0

🔍 Step 2: Running validation...
✅ Validation passed

📁 Step 3: Preparing output directory...
✅ Output directory: /path/to/dist

📦 Step 4: Creating skill package...
✅ Package created: dad-joke-validator-v1.1.0.skill (53K)

🔐 Step 5: Generating SHA256 checksum...
✅ Checksum generated
ℹ️  SHA256: 10ed1bb2ca0a6e1c...14fc103f37

📋 Step 6: Verifying package contents...
✅ Package contents verified

📊 Step 7: Generating metadata...
✅ Metadata generated: dad-joke-validator-v1.1.0.metadata.json

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ PACKAGING COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 Package:  dad-joke-validator-v1.1.0.skill (53K)
🔐 Checksum: dad-joke-validator-v1.1.0.skill.sha256
📊 Metadata: dad-joke-validator-v1.1.0.metadata.json
```

### Batch Package All Skills

```bash
cd AISkills
./SkillPackager/scripts/batch-package.sh
```

Auto-discovers all skills and packages them in parallel.

### Test Package Installation

```bash
./scripts/test-skill-installation.sh ../dist/dad-joke-validator-v1.1.0.skill
```

Validates package can be extracted and installed correctly.

## Integration with SKILL-8

Works seamlessly with SKILL-8 (Skill Template):

```bash
# 1. Create skill from template
cp -r SkillTemplate/skill-template MyNewSkill/my-new-skill
cd MyNewSkill/my-new-skill

# 2. Customize and validate
../SkillTemplate/scripts/validate-skill.sh .

# 3. Package with SKILL-9
../SkillPackager/scripts/package-skill.sh .

# 4. Test installation
../SkillPackager/scripts/test-skill-installation.sh ../dist/my-new-skill-v1.0.0.skill
```

## Output Files

For each packaged skill, creates:

1. **`skill-name-vX.Y.Z.skill`** - ZIP package containing skill files
2. **`skill-name-vX.Y.Z.skill.sha256`** - SHA256 checksum for verification
3. **`skill-name-vX.Y.Z.metadata.json`** - Package metadata

**Metadata JSON structure:**
```json
{
  "name": "dad-joke-validator",
  "version": "1.1.0",
  "package": "dad-joke-validator-v1.1.0.skill",
  "size": "53K",
  "sha256": "10ed1bb2ca0a6e1ccc92b7e2efa2ca8ee7f9405a6e009bbc409fdb14fc103f37",
  "packaged_at": "2025-11-16T22:30:00Z",
  "packager": "SKILL-9 Automation v1.0"
}
```

## Validation Checks

### Pre-Packaging Validation
- ✅ YAML frontmatter syntax
- ✅ Required fields (name, description)
- ✅ Name format (lowercase, hyphens, numbers)
- ✅ No unfilled placeholders ({{...}})
- ✅ Valid UTF-8 encoding
- ✅ Valid JSON in assets/
- ✅ Valid Python syntax in scripts/

### Post-Packaging Validation
- ✅ Package extracts successfully
- ✅ SKILL.md present and valid
- ✅ No invalid frontmatter fields (e.g., version)
- ✅ No development artifacts (.pyc, __pycache__)
- ✅ Required files present

## Exclusion Rules

The following files/directories are automatically excluded:

- `*.pyc` - Python bytecode
- `__pycache__/` - Python cache
- `.DS_Store` - macOS metadata
- `.git/` - Git repository
- `.pytest_cache/` - Pytest cache
- `dist/` - Distribution directory (avoids recursion)
- `.venv/`, `venv/` - Python virtual environments
- `node_modules/` - Node.js modules
- `.idea/`, `.vscode/` - IDE configurations

## Version Detection

Version is auto-detected from `CHANGELOG.md`:

```markdown
# Changelog

## [1.1.0] - 2025-11-16

### Added
- New feature
```

Extracts `1.1.0` from the first `## [X.Y.Z]` line.

If no CHANGELOG.md exists, defaults to `1.0.0` or uses version argument.

## Error Handling

Clear error messages for common issues:

**Missing SKILL.md:**
```
❌ ERROR: Skill directory not found: /path/to/skill
```

**Validation failure:**
```
❌ ERROR: Validation failed - fix errors before packaging
```

**Invalid YAML frontmatter:**
```
❌ Invalid field 'version' in frontmatter (not supported in Claude skills)
```

## Requirements

- **Bash** (4.0+)
- **zip** command
- **shasum** (or sha256sum)
- **Python 3** (for validation)
- **SKILL-8 validation scripts** (optional but recommended)

## Version

Current: v1.0.0

## License

MIT License

---

**Part of the AISkills Collection Infrastructure**
- SKILL-8: Skill Template and Integration Runbook
- SKILL-9: Packaging Automation (this tool)
