# How to Use the Skill Template

## Quick Start (5 minutes)

1. **Copy the template**
   ```bash
   cp -r skill-template my-new-skill
   cd my-new-skill
   ```

2. **Fill core placeholders in SKILL.md**
   - `{{SKILL_NAME}}` → your-skill-name (lowercase, hyphens)
   - `{{SKILL_DESCRIPTION}}` → Brief description (max 1024 chars)
   - `{{SKILL_TITLE}}` → Your Skill Title (display name)

3. **Customize capabilities**
   - Edit "When to Use" section with 3-5 trigger phrases
   - Document 2-5 core capabilities with examples
   - Remove sections you don't need

4. **Validate**
   ```bash
   ../scripts/validate-skill.sh .
   ```

5. **Test loading**
   ```bash
   python3 ../scripts/test-skill-loading.py .
   ```

6. **Package** (when ready)
   ```bash
   cd ..
   ./SKILL-9-packaging-automation.sh my-new-skill
   ```

## Complete Workflow

### Step 1: Plan Your Skill

**Questions to answer:**
- What does this skill do? (1 sentence)
- When should Claude use it? (3-5 scenarios)
- What are the core capabilities? (2-5 main features)
- Does it need scripts/assets? (optional)

### Step 2: Copy and Rename

```bash
# Copy template
cp -r skill-template ../MyAwesomeSkill/my-awesome-skill
cd ../MyAwesomeSkill/my-awesome-skill
```

### Step 3: Fill SKILL.md

**Required replacements:**
```yaml
---
name: my-awesome-skill  # lowercase, hyphens, numbers only
description: Does X when user needs Y. Use for Z scenarios.  # Max 1024 chars
---
```

**Then customize body:**
- Title (`# Your Skill Name`)
- When to Use triggers
- Core Capabilities (2-5 sections)
- Output Format (if applicable)
- Examples (link to references/)

### Step 4: Fill README.md

- Title and one-line description
- Features list
- When to Use scenarios
- Example usage (input/output)
- Installation instructions
- Version and license

### Step 5: Add References (Optional)

In `references/`:
- `examples.md` - 5-10 realistic examples
- `advanced-usage.md` - Complex scenarios
- `troubleshooting.md` - Common issues

### Step 6: Add Scripts/Assets (Optional)

**If you need Python scripts:**
```bash
# In scripts/
cp validator.py.template my_analyzer.py
# Edit to implement your logic
```

**If you need data files:**
```bash
# In assets/
cat > patterns.json << 'EOF'
{
  "category1": ["item1", "item2"],
  "category2": ["item3", "item4"]
}
EOF
```

### Step 7: Update Metadata

**CHANGELOG.md:**
```markdown
# Changelog

## [1.0.0] - YYYY-MM-DD

### Added
- Initial release
- [List key features]
```

**LICENSE:**
- Update year
- Update copyright holder name

### Step 8: Validate

```bash
# Run validation
../skill-template/scripts/validate-skill.sh .

# Should see:
# ✅ VALIDATION PASSED - Skill is ready
```

### Step 9: Test Locally

```bash
# Test YAML parsing
python3 ../skill-template/scripts/test-skill-loading.py .

# Test any Python scripts
cd scripts
python3 -m pytest test_*.py  # if you have tests
```

### Step 10: Package

```bash
# Use SKILL-9 packaging automation (once built)
cd ..
zip -r dist/my-awesome-skill-v1.0.0.skill my-awesome-skill -x "*.pyc" -x "__pycache__/*"
shasum -a 256 dist/my-awesome-skill-v1.0.0.skill > dist/my-awesome-skill-v1.0.0.skill.sha256
```

## Common Customizations

See `CUSTOMIZATION_GUIDE.md` for detailed customization patterns.

## Troubleshooting

**"Unfilled placeholders detected"**
- Search for `{{` in all .md files
- Replace all template placeholders

**"YAML frontmatter missing"**
- Ensure SKILL.md starts with `---` on line 1
- Ensure closing `---` is on its own line
- No spaces before `---`

**"Name format invalid"**
- Use only lowercase letters, numbers, hyphens
- Examples: `text-analyzer`, `code-review-bot`, `data-formatter`

**"Description exceeds 1024 chars"**
- Keep description concise
- Move detailed info to markdown body

## Best Practices

1. **Keep SKILL.md under 500 words** - Move details to references/
2. **Use concrete examples** - Show realistic use cases
3. **Test on real inputs** - Validate with actual scenarios
4. **Progressive disclosure** - Core in SKILL.md, details in references/
5. **Validate before packaging** - Always run validation scripts

## Reference Implementations

- **Dad Joke Validator** - Full implementation with scripts + assets
- **example-skill** - Minimal but complete text statistics skill

Both follow this template pattern exactly.

---

**Need Help?**
- Review `CUSTOMIZATION_GUIDE.md` for detailed patterns
- Check `example-skill/` for working implementation
- Run `validate-skill.sh` for instant feedback
