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
