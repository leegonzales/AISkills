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
