#!/bin/bash
# Skill Template Validation Script
# Usage: ./validate-skill.sh <skill-directory>

set -e

SKILL_DIR="${1:-.}"
ERRORS=0

echo "🔍 Validating skill in: $SKILL_DIR"
echo ""

# Check required files
echo "📁 Checking required files..."
REQUIRED_FILES=("SKILL.md" "README.md" "LICENSE" "CHANGELOG.md")
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$SKILL_DIR/$file" ]; then
        echo "  ✅ $file exists"
    else
        echo "  ❌ $file missing"
        ERRORS=$((ERRORS + 1))
    fi
done
echo ""

# Validate SKILL.md YAML frontmatter
echo "📝 Validating SKILL.md..."
if [ -f "$SKILL_DIR/SKILL.md" ]; then
    # Check for YAML frontmatter
    if head -1 "$SKILL_DIR/SKILL.md" | grep -q "^---$"; then
        echo "  ✅ YAML frontmatter present"

        # Extract frontmatter
        FRONTMATTER=$(awk '/^---$/{flag=!flag; next} flag' "$SKILL_DIR/SKILL.md" | head -n 20)

        # Check required fields
        if echo "$FRONTMATTER" | grep -q "^name:"; then
            SKILL_NAME=$(echo "$FRONTMATTER" | grep "^name:" | sed 's/name: *//')
            echo "  ✅ name field present: $SKILL_NAME"

            # Validate name format (lowercase, hyphens only)
            if [[ $SKILL_NAME =~ ^[a-z0-9-]+$ ]]; then
                echo "  ✅ name format valid"
            else
                echo "  ❌ name format invalid (use lowercase, numbers, hyphens only)"
                ERRORS=$((ERRORS + 1))
            fi
        else
            echo "  ❌ name field missing"
            ERRORS=$((ERRORS + 1))
        fi

        if echo "$FRONTMATTER" | grep -q "^description:"; then
            DESC=$(echo "$FRONTMATTER" | grep "^description:" | cut -d: -f2-)
            DESC_LEN=${#DESC}
            echo "  ✅ description field present ($DESC_LEN chars)"

            if [ $DESC_LEN -gt 1024 ]; then
                echo "  ⚠️  description exceeds 1024 chars"
                ERRORS=$((ERRORS + 1))
            fi
        else
            echo "  ❌ description field missing"
            ERRORS=$((ERRORS + 1))
        fi

        # Check for invalid fields
        if echo "$FRONTMATTER" | grep -qE "^version:"; then
            echo "  ❌ Invalid field 'version' in frontmatter (not supported)"
            ERRORS=$((ERRORS + 1))
        fi
    else
        echo "  ❌ YAML frontmatter missing (must start with ---)"
        ERRORS=$((ERRORS + 1))
    fi
fi
echo ""

# Check for unfilled placeholders
# Allowlist documented protocol/API placeholders that legitimately appear in skill docs.
# Skills can extend this via .validate-allowlist (one regex per line) at the skill root.
echo "🔧 Checking for unfilled placeholders..."
ALLOWLIST_PATTERN='\{\{(SIMULATION_DATA|SKILL_NAME|SKILL_SLUG|VERSION|DOMAIN|TODO_REPLACE_ME|EXAMPLE_PLACEHOLDER)\}\}'
if [ -f "$SKILL_DIR/.validate-allowlist" ]; then
    while IFS= read -r line; do
        [ -z "$line" ] && continue
        case "$line" in \#*) continue;; esac
        ALLOWLIST_PATTERN="${ALLOWLIST_PATTERN}|${line}"
    done < "$SKILL_DIR/.validate-allowlist"
fi
PLACEHOLDERS=$(grep -rE "\{\{" "$SKILL_DIR" --include="*.md" 2>/dev/null \
    | grep -vE "$ALLOWLIST_PATTERN" || true)
if [ -z "$PLACEHOLDERS" ]; then
    echo "  ✅ No unfilled placeholders found"
else
    echo "  ❌ Unfilled placeholders detected:"
    echo "$PLACEHOLDERS" | sed 's/^/    /'
    ERRORS=$((ERRORS + 1))
fi
echo ""

# Validate UTF-8 encoding
echo "🔤 Checking file encoding..."
for file in "$SKILL_DIR"/*.md; do
    if [ -f "$file" ]; then
        if iconv -f UTF-8 -t UTF-8 "$file" >/dev/null 2>&1; then
            echo "  ✅ $(basename "$file") is valid UTF-8"
        else
            echo "  ❌ $(basename "$file") has encoding issues"
            ERRORS=$((ERRORS + 1))
        fi
    fi
done
echo ""

# Check JSON files if assets/ exists
if [ -d "$SKILL_DIR/assets" ]; then
    echo "📊 Validating JSON assets..."
    JSON_COUNT=0
    for json_file in "$SKILL_DIR/assets"/*.json; do
        if [ -f "$json_file" ]; then
            if python3 -m json.tool "$json_file" >/dev/null 2>&1; then
                echo "  ✅ $(basename "$json_file") is valid JSON"
                JSON_COUNT=$((JSON_COUNT + 1))
            else
                echo "  ❌ $(basename "$json_file") is invalid JSON"
                ERRORS=$((ERRORS + 1))
            fi
        fi
    done
    if [ $JSON_COUNT -eq 0 ]; then
        echo "  ⚠️  No JSON files in assets/"
    fi
    echo ""
fi

# Check Python scripts if scripts/ exists
if [ -d "$SKILL_DIR/scripts" ]; then
    echo "🐍 Validating Python scripts..."
    PY_COUNT=0
    for py_file in "$SKILL_DIR/scripts"/*.py; do
        if [ -f "$py_file" ]; then
            if python3 -m py_compile "$py_file" 2>/dev/null; then
                echo "  ✅ $(basename "$py_file") syntax valid"
                PY_COUNT=$((PY_COUNT + 1))
            else
                echo "  ❌ $(basename "$py_file") has syntax errors"
                ERRORS=$((ERRORS + 1))
            fi
        fi
    done
    if [ $PY_COUNT -eq 0 ]; then
        echo "  ℹ️  No Python files in scripts/"
    fi
    echo ""
fi

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ $ERRORS -eq 0 ]; then
    echo "✅ VALIDATION PASSED - Skill is ready"
    exit 0
else
    echo "❌ VALIDATION FAILED - $ERRORS error(s) found"
    exit 1
fi
