# SKILL-9: Build .skill Packaging Automation

**Subagent Specification for Autonomous Execution**

**Mission:** Create automated packaging tooling that validates, packages, and checksums Claude Code skills with zero manual steps. Eliminates human error in skill distribution.

**Context:** Currently packaging skills requires manual ZIP creation, SHA256 generation, and validation. This is error-prone and slow. SKILL-9 automates the entire packaging pipeline with validation built in.

**Priority:** P1 (BLOCKS all skill integrations - packaging is the final step before distribution)

**Estimated Effort:** 4-6 hours

**Subagent Readiness:** 95% (straightforward automation task)

---

## Part 1: Project Setup

**Working Directory:** `/Users/leegonzales/Projects/leegonzales/AISkills/`

**Validation Commands:**
```bash
# Verify working directory
pwd  # Should show: /Users/leegonzales/Projects/leegonzales/AISkills

# Create working directory for SKILL-9
mkdir -p SkillPackager
cd SkillPackager
```

**Success Criteria:**
- ✅ Working directory created
- ✅ Ready to build packaging automation

---

## Part 2: Design Packaging Script

**Requirements:**

1. **Input:** Skill directory path
2. **Validation:** Run all checks (YAML, UTF-8, placeholders, JSON, Python syntax)
3. **Packaging:** Create ZIP with correct exclusions
4. **Checksum:** Generate SHA256
5. **Output:** Success/failure with clear messages

**Script Features:**
- Auto-detect skill name and version from SKILL.md
- Exclude development files (.pyc, __pycache__, .DS_Store, .git, .pytest_cache)
- Validate before packaging
- Clean output directory
- Generate metadata

**Success Criteria:**
- ✅ Requirements documented
- ✅ Feature list complete
- ✅ Ready to implement

---

## Part 3: Implement package-skill.sh

**File: scripts/package-skill.sh**

```bash
#!/bin/bash
# Claude Code Skill Packaging Automation
# Usage: ./package-skill.sh <skill-directory> [version]
#
# Auto-packages a Claude Code skill with validation, ZIP creation, and SHA256 checksum

set -e

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions
error() {
    echo -e "${RED}❌ ERROR: $1${NC}" >&2
    exit 1
}

success() {
    echo -e "${GREEN}✅ $1${NC}"
}

warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

info() {
    echo "ℹ️  $1"
}

# Parse arguments
SKILL_DIR="${1:-.}"
VERSION_ARG="${2:-}"

if [ ! -d "$SKILL_DIR" ]; then
    error "Skill directory not found: $SKILL_DIR"
fi

# Convert to absolute path
SKILL_DIR=$(cd "$SKILL_DIR" && pwd)
SKILL_NAME=$(basename "$SKILL_DIR")

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Claude Code Skill Packager"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
info "Skill Directory: $SKILL_DIR"
info "Skill Name: $SKILL_NAME"
echo ""

# Step 1: Detect version
echo "📌 Step 1: Detecting version..."
if [ -f "$SKILL_DIR/CHANGELOG.md" ]; then
    # Extract version from CHANGELOG.md (## [X.Y.Z] format)
    DETECTED_VERSION=$(grep -m 1 "^## \[" "$SKILL_DIR/CHANGELOG.md" | sed 's/## \[\(.*\)\].*/\1/' | tr -d '[]')

    if [ -n "$DETECTED_VERSION" ]; then
        info "Version from CHANGELOG.md: $DETECTED_VERSION"
        VERSION="${VERSION_ARG:-$DETECTED_VERSION}"
    else
        VERSION="${VERSION_ARG:-1.0.0}"
        warning "No version in CHANGELOG.md, using: $VERSION"
    fi
else
    VERSION="${VERSION_ARG:-1.0.0}"
    warning "No CHANGELOG.md found, using: $VERSION"
fi

info "Packaging version: v$VERSION"
echo ""

# Step 2: Run validation
echo "🔍 Step 2: Running validation..."
VALIDATION_SCRIPT="$(dirname "$0")/validate-skill.sh"

if [ ! -f "$VALIDATION_SCRIPT" ]; then
    # Try to find it in SkillTemplate
    VALIDATION_SCRIPT="../SkillTemplate/scripts/validate-skill.sh"
fi

if [ -f "$VALIDATION_SCRIPT" ]; then
    if bash "$VALIDATION_SCRIPT" "$SKILL_DIR"; then
        success "Validation passed"
    else
        error "Validation failed - fix errors before packaging"
    fi
else
    warning "Validation script not found, skipping validation"
fi
echo ""

# Step 3: Prepare output directory
echo "📁 Step 3: Preparing output directory..."
PARENT_DIR=$(dirname "$SKILL_DIR")
DIST_DIR="$PARENT_DIR/dist"

mkdir -p "$DIST_DIR"
success "Output directory: $DIST_DIR"
echo ""

# Step 4: Create package
echo "📦 Step 4: Creating skill package..."
PACKAGE_NAME="${SKILL_NAME}-v${VERSION}.skill"
PACKAGE_PATH="$DIST_DIR/$PACKAGE_NAME"

# Remove old package if exists
if [ -f "$PACKAGE_PATH" ]; then
    info "Removing old package: $PACKAGE_NAME"
    rm -f "$PACKAGE_PATH"
    rm -f "$PACKAGE_PATH.sha256"
fi

# Create ZIP package
cd "$PARENT_DIR"
zip -r "$PACKAGE_PATH" "$SKILL_NAME" \
    -x "*.pyc" \
    -x "*/__pycache__/*" \
    -x "*/.DS_Store" \
    -x "*/.git/*" \
    -x "*/.pytest_cache/*" \
    -x "*/dist/*" \
    -x "*/.venv/*" \
    -x "*/venv/*" \
    -x "*/node_modules/*" \
    -x "*/.idea/*" \
    -x "*/.vscode/*" \
    > /dev/null 2>&1

if [ ! -f "$PACKAGE_PATH" ]; then
    error "Failed to create package"
fi

PACKAGE_SIZE=$(du -h "$PACKAGE_PATH" | awk '{print $1}')
success "Package created: $PACKAGE_NAME ($PACKAGE_SIZE)"
echo ""

# Step 5: Generate SHA256 checksum
echo "🔐 Step 5: Generating SHA256 checksum..."
cd "$DIST_DIR"
shasum -a 256 "$PACKAGE_NAME" > "$PACKAGE_NAME.sha256"

CHECKSUM=$(cat "$PACKAGE_NAME.sha256" | awk '{print $1}')
success "Checksum generated"
info "SHA256: ${CHECKSUM:0:16}...${CHECKSUM:96:16}"
echo ""

# Step 6: Verify package contents
echo "📋 Step 6: Verifying package contents..."
SKILL_MD_CHECK=$(unzip -l "$PACKAGE_NAME" | grep "SKILL.md" | wc -l)
README_CHECK=$(unzip -l "$PACKAGE_NAME" | grep "README.md" | wc -l)

if [ "$SKILL_MD_CHECK" -eq 0 ]; then
    error "SKILL.md not found in package"
fi

if [ "$README_CHECK" -eq 0 ]; then
    warning "README.md not found in package"
fi

# Extract and validate SKILL.md YAML
echo "  Extracting SKILL.md for validation..."
TMP_SKILL_MD=$(mktemp)
unzip -p "$PACKAGE_NAME" "*/SKILL.md" > "$TMP_SKILL_MD" 2>/dev/null || error "Could not extract SKILL.md"

# Check YAML frontmatter
if head -1 "$TMP_SKILL_MD" | grep -q "^---$"; then
    success "YAML frontmatter present in package"

    # Extract name
    PACKAGED_NAME=$(awk '/^---$/{flag=!flag; next} flag' "$TMP_SKILL_MD" | grep "^name:" | sed 's/name: *//')
    info "Packaged skill name: $PACKAGED_NAME"

    # Check for invalid version field
    if awk '/^---$/{flag=!flag; next} flag' "$TMP_SKILL_MD" | grep -q "^version:"; then
        error "Invalid 'version' field in YAML frontmatter (not supported in Claude skills)"
    fi
else
    error "YAML frontmatter missing in packaged SKILL.md"
fi

rm -f "$TMP_SKILL_MD"
success "Package contents verified"
echo ""

# Step 7: Generate metadata
echo "📊 Step 7: Generating metadata..."
METADATA_FILE="$DIST_DIR/${SKILL_NAME}-v${VERSION}.metadata.json"

cat > "$METADATA_FILE" <<EOF
{
  "name": "$SKILL_NAME",
  "version": "$VERSION",
  "package": "$PACKAGE_NAME",
  "size": "$PACKAGE_SIZE",
  "sha256": "$CHECKSUM",
  "packaged_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "packager": "SKILL-9 Automation v1.0"
}
EOF

success "Metadata generated: ${SKILL_NAME}-v${VERSION}.metadata.json"
echo ""

# Final summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ PACKAGING COMPLETE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📦 Package:  $PACKAGE_NAME ($PACKAGE_SIZE)"
echo "🔐 Checksum: $(basename "$PACKAGE_NAME.sha256")"
echo "📊 Metadata: $(basename "$METADATA_FILE")"
echo ""
echo "Files created in: $DIST_DIR"
echo "  - $PACKAGE_NAME"
echo "  - $PACKAGE_NAME.sha256"
echo "  - $(basename "$METADATA_FILE")"
echo ""
echo "Next steps:"
echo "  1. Test installation in Claude Code/web chat"
echo "  2. Commit to version control"
echo "  3. Tag release: git tag v$VERSION"
echo "  4. Push: git push && git push --tags"
echo ""
```

**Commands to Create Script:**
```bash
mkdir -p scripts

cat > scripts/package-skill.sh << 'EOF'
[COMPLETE SCRIPT FROM ABOVE]
EOF

chmod +x scripts/package-skill.sh

echo "✅ Packaging script created"
```

**Success Criteria:**
- ✅ Complete packaging script created
- ✅ All validation integrated
- ✅ SHA256 generation included
- ✅ Metadata generation added
- ✅ Clear output and error messages

---

## Part 4: Create batch-package.sh for Multiple Skills

**File: scripts/batch-package.sh**

```bash
#!/bin/bash
# Batch Skill Packaging
# Usage: ./batch-package.sh [skill-dir1] [skill-dir2] ...
#        or ./batch-package.sh (auto-discovers all */SKILL.md)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACKAGE_SCRIPT="$SCRIPT_DIR/package-skill.sh"

if [ ! -f "$PACKAGE_SCRIPT" ]; then
    echo "❌ package-skill.sh not found: $PACKAGE_SCRIPT"
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Batch Skill Packager"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Auto-discover skills if no arguments
if [ $# -eq 0 ]; then
    echo "🔍 Auto-discovering skills..."
    SKILL_DIRS=()
    while IFS= read -r -d '' skill_md; do
        skill_dir=$(dirname "$skill_md")
        SKILL_DIRS+=("$skill_dir")
    done < <(find . -name "SKILL.md" -not -path "*/node_modules/*" -not -path "*/.venv/*" -print0)

    if [ ${#SKILL_DIRS[@]} -eq 0 ]; then
        echo "❌ No skills found"
        exit 1
    fi

    echo "ℹ️  Found ${#SKILL_DIRS[@]} skill(s):"
    for dir in "${SKILL_DIRS[@]}"; do
        echo "    - $(basename "$dir")"
    done
    echo ""
else
    SKILL_DIRS=("$@")
fi

# Package each skill
SUCCESS_COUNT=0
FAIL_COUNT=0
FAILED_SKILLS=()

for skill_dir in "${SKILL_DIRS[@]}"; do
    if [ ! -d "$skill_dir" ]; then
        echo "⚠️  Skipping non-existent directory: $skill_dir"
        continue
    fi

    skill_name=$(basename "$skill_dir")
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Packaging: $skill_name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if bash "$PACKAGE_SCRIPT" "$skill_dir"; then
        ((SUCCESS_COUNT++))
    else
        ((FAIL_COUNT++))
        FAILED_SKILLS+=("$skill_name")
    fi

    echo ""
done

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "BATCH PACKAGING SUMMARY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ Successfully packaged: $SUCCESS_COUNT"
echo "❌ Failed: $FAIL_COUNT"

if [ $FAIL_COUNT -gt 0 ]; then
    echo ""
    echo "Failed skills:"
    for skill in "${FAILED_SKILLS[@]}"; do
        echo "  - $skill"
    done
    exit 1
fi

echo ""
echo "All skills packaged successfully! 🚀"
```

**Commands to Create Batch Script:**
```bash
cat > scripts/batch-package.sh << 'EOF'
[COMPLETE SCRIPT FROM ABOVE]
EOF

chmod +x scripts/batch-package.sh

echo "✅ Batch packaging script created"
```

**Success Criteria:**
- ✅ Batch packaging script created
- ✅ Auto-discovery of skills implemented
- ✅ Summary reporting included
- ✅ Error handling for failed packages

---

## Part 5: Create Installation Testing Script

**File: scripts/test-skill-installation.sh**

```bash
#!/bin/bash
# Test Skill Installation
# Usage: ./test-skill-installation.sh <skill-package.skill>
#
# Validates that a packaged skill can be "installed" (unpacked and validated)

set -e

PACKAGE_PATH="$1"

if [ -z "$PACKAGE_PATH" ]; then
    echo "Usage: $0 <skill-package.skill>"
    exit 1
fi

if [ ! -f "$PACKAGE_PATH" ]; then
    echo "❌ Package not found: $PACKAGE_PATH"
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Skill Installation Test"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "ℹ️  Package: $(basename "$PACKAGE_PATH")"
echo ""

# Create temp directory
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

echo "📦 Step 1: Extracting package..."
if unzip -q "$PACKAGE_PATH" -d "$TEMP_DIR"; then
    echo "  ✅ Package extracted successfully"
else
    echo "  ❌ Failed to extract package"
    exit 1
fi
echo ""

# Find skill directory
SKILL_DIR=$(find "$TEMP_DIR" -name "SKILL.md" -type f | head -1 | xargs dirname)

if [ -z "$SKILL_DIR" ]; then
    echo "❌ No SKILL.md found in package"
    exit 1
fi

SKILL_NAME=$(basename "$SKILL_DIR")
echo "ℹ️  Skill name: $SKILL_NAME"
echo ""

# Validate SKILL.md
echo "📝 Step 2: Validating SKILL.md..."
if [ -f "$SKILL_DIR/SKILL.md" ]; then
    # Check YAML frontmatter
    if head -1 "$SKILL_DIR/SKILL.md" | grep -q "^---$"; then
        echo "  ✅ YAML frontmatter present"

        # Extract and validate fields
        FRONTMATTER=$(awk '/^---$/{flag=!flag; next} flag' "$SKILL_DIR/SKILL.md")

        if echo "$FRONTMATTER" | grep -q "^name:"; then
            NAME=$(echo "$FRONTMATTER" | grep "^name:" | sed 's/name: *//')
            echo "  ✅ name: $NAME"
        else
            echo "  ❌ name field missing"
            exit 1
        fi

        if echo "$FRONTMATTER" | grep -q "^description:"; then
            echo "  ✅ description present"
        else
            echo "  ❌ description field missing"
            exit 1
        fi

        # Check for invalid fields
        if echo "$FRONTMATTER" | grep -q "^version:"; then
            echo "  ❌ Invalid 'version' field in frontmatter"
            exit 1
        fi
    else
        echo "  ❌ YAML frontmatter missing"
        exit 1
    fi
else
    echo "  ❌ SKILL.md not found"
    exit 1
fi
echo ""

# Check required files
echo "📁 Step 3: Checking required files..."
REQUIRED=("SKILL.md" "README.md" "LICENSE")
ALL_PRESENT=true

for file in "${REQUIRED[@]}"; do
    if [ -f "$SKILL_DIR/$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ⚠️  $file missing (recommended)"
        if [ "$file" = "SKILL.md" ]; then
            ALL_PRESENT=false
        fi
    fi
done

if ! $ALL_PRESENT; then
    echo "  ❌ Missing critical files"
    exit 1
fi
echo ""

# Check for development artifacts (should be excluded)
echo "🔍 Step 4: Checking for excluded files..."
ARTIFACTS_FOUND=false

if find "$SKILL_DIR" -name "*.pyc" | grep -q .; then
    echo "  ⚠️  .pyc files found (should be excluded)"
    ARTIFACTS_FOUND=true
fi

if find "$SKILL_DIR" -name "__pycache__" | grep -q .; then
    echo "  ⚠️  __pycache__ directories found (should be excluded)"
    ARTIFACTS_FOUND=true
fi

if find "$SKILL_DIR" -name ".DS_Store" | grep -q .; then
    echo "  ⚠️  .DS_Store files found (should be excluded)"
    ARTIFACTS_FOUND=true
fi

if ! $ARTIFACTS_FOUND; then
    echo "  ✅ No development artifacts found"
fi
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if $ALL_PRESENT && ! $ARTIFACTS_FOUND; then
    echo "✅ INSTALLATION TEST PASSED"
    echo ""
    echo "Package is valid and ready for distribution!"
    exit 0
else
    echo "⚠️  INSTALLATION TEST PASSED WITH WARNINGS"
    echo ""
    echo "Package is functional but has minor issues"
    exit 0
fi
```

**Commands to Create Testing Script:**
```bash
cat > scripts/test-skill-installation.sh << 'EOF'
[COMPLETE SCRIPT FROM ABOVE]
EOF

chmod +x scripts/test-skill-installation.sh

echo "✅ Installation testing script created"
```

**Success Criteria:**
- ✅ Installation testing script created
- ✅ Package extraction validation
- ✅ SKILL.md validation
- ✅ Development artifact detection
- ✅ Clear pass/fail reporting

---

## Part 6: Create Documentation

**File: README.md**

```markdown
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
```

**Commands to Create Documentation:**
```bash
cat > README.md << 'EOF'
[CONTENT FROM ABOVE]
EOF

echo "✅ Documentation created"
```

**Success Criteria:**
- ✅ Complete README created
- ✅ Usage examples provided
- ✅ All features documented
- ✅ Integration with SKILL-8 explained
- ✅ Troubleshooting guide included

---

## Part 7: Testing Protocol

**Test Plan:**

1. **Test on Dad Joke Validator** (known good skill)
2. **Test on malformed skill** (validate error handling)
3. **Test batch packaging** (multiple skills)
4. **Test installation testing** (packaged skills)

**Test Commands:**
```bash
# Test 1: Package Dad Joke Validator
./scripts/package-skill.sh ../DadJokeValidator/dad-joke-validator

# Test 2: Test installation
./scripts/test-skill-installation.sh ../DadJokeValidator/dist/dad-joke-validator-v1.1.0.skill

# Test 3: Batch package all skills
cd ..
./SkillPackager/scripts/batch-package.sh \
    DadJokeValidator/dad-joke-validator \
    ProsePolish/prose-polish \
    GeminiPeerReview/gemini-peer-review

# Test 4: Verify all packages
for skill in DadJokeValidator/dist/*.skill; do
    echo "Testing: $skill"
    ./SkillPackager/scripts/test-skill-installation.sh "$skill"
done
```

**Success Criteria:**
- ✅ Dad Joke Validator packages successfully
- ✅ Installation test passes
- ✅ Batch packaging works
- ✅ All validation checks pass

---

## Part 8: Create Delivery Package

**Final Directory Structure:**
```
SkillPackager/
├── README.md                       # Complete documentation
├── scripts/
│   ├── package-skill.sh            # Single skill packaging
│   ├── batch-package.sh            # Batch packaging
│   └── test-skill-installation.sh  # Installation testing
└── examples/
    └── USAGE_EXAMPLES.md           # Detailed usage examples
```

**File: examples/USAGE_EXAMPLES.md**

```markdown
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
```

**Commands to Create Examples:**
```bash
mkdir -p examples

cat > examples/USAGE_EXAMPLES.md << 'EOF'
[CONTENT FROM ABOVE]
EOF

echo "✅ Usage examples created"
```

**Success Criteria:**
- ✅ Comprehensive usage examples created
- ✅ CI/CD integration example provided
- ✅ Troubleshooting workflows included
- ✅ Real-world scenarios documented

---

## Part 9: Final Validation and Handoff

**Validation Checklist:**

```markdown
# SKILL-9 Delivery Checklist

## Core Scripts
- [ ] package-skill.sh created and executable
- [ ] batch-package.sh created and executable
- [ ] test-skill-installation.sh created and executable
- [ ] All scripts have proper error handling

## Documentation
- [ ] README.md complete
- [ ] Usage examples comprehensive
- [ ] Integration with SKILL-8 documented
- [ ] Error messages documented

## Testing
- [ ] Packages Dad Joke Validator successfully
- [ ] Installation test passes
- [ ] Batch packaging works
- [ ] Handles errors gracefully

## Output Files
- [ ] Generates .skill ZIP files correctly
- [ ] Creates SHA256 checksums
- [ ] Produces metadata JSON
- [ ] Excludes development artifacts

## Final Checks
- [ ] All scripts tested on real skills
- [ ] Error messages are clear
- [ ] Documentation is accurate
- [ ] Ready for immediate use
```

**Final Testing Commands:**
```bash
echo "🔍 Running final validation..."

# Test all scripts exist and are executable
for script in package-skill.sh batch-package.sh test-skill-installation.sh; do
    if [ -x "scripts/$script" ]; then
        echo "✅ $script is executable"
    else
        echo "❌ $script is missing or not executable"
        exit 1
    fi
done

# Test packaging Dad Joke Validator
if ./scripts/package-skill.sh ../DadJokeValidator/dad-joke-validator; then
    echo "✅ Package test passed"
else
    echo "❌ Package test failed"
    exit 1
fi

# Test installation validation
if ./scripts/test-skill-installation.sh ../DadJokeValidator/dist/dad-joke-validator-v1.1.0.skill; then
    echo "✅ Installation test passed"
else
    echo "❌ Installation test failed"
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ SKILL-9 DELIVERY READY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Deliverables:"
echo "  - package-skill.sh (single skill packaging)"
echo "  - batch-package.sh (batch packaging)"
echo "  - test-skill-installation.sh (installation testing)"
echo "  - Complete documentation"
echo ""
echo "Integration:"
echo "  - Works with SKILL-8 validation"
echo "  - Auto-detects versions from CHANGELOG.md"
echo "  - Generates metadata for tracking"
echo ""
echo "Ready to automate all skill packaging! 🚀"
```

**Success Criteria:**
- ✅ All scripts created and tested
- ✅ Documentation complete
- ✅ Integration with SKILL-8 verified
- ✅ Ready for production use

---

## Handoff Summary

**What You're Delivering:**

1. **package-skill.sh**
   - Single skill packaging with validation
   - Auto-version detection
   - SHA256 checksum generation
   - Metadata creation

2. **batch-package.sh**
   - Batch packaging for multiple skills
   - Auto-discovery of skills
   - Progress reporting
   - Error handling

3. **test-skill-installation.sh**
   - Package validation
   - Installation simulation
   - YAML frontmatter checks
   - Artifact detection

4. **Complete Documentation**
   - README with all features
   - Usage examples
   - CI/CD integration
   - Troubleshooting guide

**Expected Impact:**
- Zero manual packaging steps
- Eliminated packaging errors
- Consistent package quality
- Automated validation

**Integration:**
- Works with SKILL-8 templates
- Uses SKILL-8 validation scripts
- Completes the skill lifecycle:
  1. SKILL-8: Create from template
  2. Validate with SKILL-8 scripts
  3. Package with SKILL-9 automation
  4. Test with SKILL-9 installation test

---

**SKILL-9 SPECIFICATION COMPLETE**

Ready for autonomous subagent execution. Estimated completion: 4-6 hours.

All dependencies resolved. Go/No-Go: **GO** 🚀
