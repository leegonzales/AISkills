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
