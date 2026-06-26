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
        ((ERRORS++))
    fi
done
echo ""

# Validate SKILL.md YAML frontmatter
echo "📝 Validating SKILL.md..."
if [ -f "$SKILL_DIR/SKILL.md" ]; then
    # Check for YAML frontmatter
    if head -1 "$SKILL_DIR/SKILL.md" | grep -q "^---$"; then
        echo "  ✅ YAML frontmatter present"

        # Extract frontmatter (only the first --- ... --- block)
        FRONTMATTER=$(awk 'BEGIN{n=0} /^---$/{n++; if(n==1){next} if(n==2){exit}} n==1' "$SKILL_DIR/SKILL.md")

        # Check required fields
        if echo "$FRONTMATTER" | grep -q "^name:"; then
            SKILL_NAME=$(echo "$FRONTMATTER" | grep "^name:" | sed 's/name: *//')
            echo "  ✅ name field present: $SKILL_NAME"

            # Validate name format (lowercase, hyphens only)
            if [[ $SKILL_NAME =~ ^[a-z0-9-]+$ ]]; then
                echo "  ✅ name format valid"
            else
                echo "  ❌ name format invalid (use lowercase, numbers, hyphens only)"
                ((ERRORS++))
            fi
        else
            echo "  ❌ name field missing"
            ((ERRORS++))
        fi

        if echo "$FRONTMATTER" | grep -q "^description:"; then
            DESC=$(echo "$FRONTMATTER" | grep "^description:" | cut -d: -f2-)
            DESC_LEN=${#DESC}
            echo "  ✅ description field present ($DESC_LEN chars)"

            if [ $DESC_LEN -gt 1024 ]; then
                echo "  ⚠️  description exceeds 1024 chars"
                ((ERRORS++))
            fi
        else
            echo "  ❌ description field missing"
            ((ERRORS++))
        fi

        # Check for invalid fields
        if echo "$FRONTMATTER" | grep -qE "^version:"; then
            echo "  ❌ Invalid field 'version' in frontmatter (not supported)"
            ((ERRORS++))
        fi
    else
        echo "  ❌ YAML frontmatter missing (must start with ---)"
        ((ERRORS++))
    fi
fi
echo ""

# Check for unfilled placeholders.
# NOT a blanket "{{" check — legit runtime template variables (e.g. {{REPO_NAME}},
# {{USER_CONTENT}}) are valid skill content. We flag only the skill-template's own
# authoring tokens (derived dynamically, so this tracks template changes) plus obvious
# TODO/FIXME markers. A finished skill should contain none of these.
echo "🔧 Checking for unfilled placeholders..."
TEMPLATE_DIR="$(cd "$(dirname "$0")/.." 2>/dev/null && pwd)/skill-template"
# Only UNAMBIGUOUS placeholder forms — bare "TODO:"/"FIXME:" appear legitimately in
# code-search and capture-pattern skills, so they are NOT flagged.
PH_PATTERN='\{\{TODO\}\}|\[TODO\]|\[FIXME\]|\[PLACEHOLDER\]|REPLACE_ME|YOUR_[A-Z_]+_HERE'
if [ -d "$TEMPLATE_DIR" ]; then
    TPL_TOKENS=$(grep -rhoE '\{\{[A-Za-z0-9_]+\}\}' "$TEMPLATE_DIR" 2>/dev/null | sort -u | sed 's/[{}]/\\&/g' | paste -sd'|' - || true)
    [ -n "$TPL_TOKENS" ] && PH_PATTERN="$PH_PATTERN|$TPL_TOKENS"
fi
PLACEHOLDERS=$(grep -rEn "$PH_PATTERN" "$SKILL_DIR" --include="*.md" 2>/dev/null || true)
if [ -z "$PLACEHOLDERS" ]; then
    echo "  ✅ No unfilled placeholders found"
else
    echo "  ❌ Unfilled placeholders detected:"
    echo "$PLACEHOLDERS" | sed 's/^/    /'
    ((ERRORS++))
fi
echo ""

# Validate UTF-8 encoding.
# Use python3 (standards-correct + portable) rather than the platform `iconv`, which on
# macOS wrongly rejects valid multi-byte UTF-8 (box-drawing chars, emoji). Falls back to
# iconv only if python3 is unavailable.
echo "🔤 Checking file encoding..."
for file in "$SKILL_DIR"/*.md; do
    if [ -f "$file" ]; then
        if command -v python3 >/dev/null 2>&1; then
            enc_ok=$(python3 -c "import sys; open(sys.argv[1],encoding='utf-8').read()" "$file" 2>/dev/null && echo ok)
        else
            iconv -f UTF-8 -t UTF-8 "$file" >/dev/null 2>&1 && enc_ok=ok || enc_ok=""
        fi
        if [ "$enc_ok" = "ok" ]; then
            echo "  ✅ $(basename "$file") is valid UTF-8"
        else
            echo "  ❌ $(basename "$file") has encoding issues"
            ((ERRORS++))
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
                ((JSON_COUNT++))
            else
                echo "  ❌ $(basename "$json_file") is invalid JSON"
                ((ERRORS++))
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
                ((PY_COUNT++))
            else
                echo "  ❌ $(basename "$py_file") has syntax errors"
                ((ERRORS++))
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
