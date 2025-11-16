# Skill Integration Runbook

Step-by-step guide for integrating a new skill into the AISkills collection.

**Estimated Time:** 4-12 hours depending on complexity
**Prerequisites:** Skill content prepared, GitHub access

---

## Phase 1: Preparation (30 min)

### Step 1.1: Determine Skill Type

**New Skill (Building from Scratch):**
- [ ] Concept defined and validated
- [ ] Examples prepared
- [ ] Peer review planned (Gemini + Codex required)

**Fork/Integration (External Skill):**
- [ ] Source repository identified
- [ ] License compatible (MIT/Apache preferred)
- [ ] Quality validated (see skill-evaluation-rubric.md)
- [ ] Peer review NOT required for forks

### Step 1.2: Set Up Working Directory

```bash
cd /Users/leegonzales/Projects/leegonzales/AISkills

# Create skill directory
mkdir -p {{SkillName}}
cd {{SkillName}}

# Copy template
cp -r ../SkillTemplate/skill-template ./{{skill-name}}
cd {{skill-name}}
```

### Step 1.3: Plan Customization

- [ ] Identify required files (SKILL.md, README.md always required)
- [ ] Identify optional components (scripts/, assets/, references/)
- [ ] List placeholders to replace
- [ ] Estimate effort (simple: 4-6h, moderate: 6-10h, complex: 10-14h)

---

## Phase 2: Content Development (2-8 hours)

### Step 2.1: Create SKILL.md (Core Skill Definition)

**Guidelines:**
- Keep under 500 words for context efficiency
- Use clear, imperative language
- Include 3-5 trigger phrases ("Invoke when user...")
- Provide 2-3 usage examples
- Reference detailed docs in references/

**Checklist:**
- [ ] Frontmatter complete (name, description, version)
- [ ] When to Use section (trigger phrases)
- [ ] Core Capabilities section (2-5 capabilities)
- [ ] How to Use section (basic + advanced examples)
- [ ] Output Format description
- [ ] Limitations listed
- [ ] References to additional docs
- [ ] Word count under 500

**Command to Check:**
```bash
wc -w SKILL.md  # Should be < 500 words
```

### Step 2.2: Write README.md (User Documentation)

**Guidelines:**
- Comprehensive overview (1000-2000 words)
- Installation for both Claude Code and web chat
- Multiple usage examples
- Link to all reference docs
- Development instructions

**Checklist:**
- [ ] Title and description
- [ ] Features list
- [ ] Installation instructions (Code + web chat)
- [ ] Basic usage example
- [ ] Advanced usage example
- [ ] Documentation links
- [ ] Development section (if applicable)
- [ ] Version history reference
- [ ] License information
- [ ] Contributing guidelines

### Step 2.3: Populate references/ (Progressive Disclosure)

**Create 3 reference docs minimum:**

1. **examples.md** - 5-10 detailed examples
   - [ ] Example 1 with full input/output/explanation
   - [ ] Example 2 with full input/output/explanation
   - [ ] Example 3 with full input/output/explanation
   - [ ] Advanced example
   - [ ] Edge case example (if applicable)

2. **advanced-usage.md** - Advanced patterns
   - [ ] Pattern 1 with use case
   - [ ] Pattern 2 with use case
   - [ ] Integration with other skills
   - [ ] Performance tips

3. **troubleshooting.md** - Common issues
   - [ ] Issue 1 with symptoms/cause/solution
   - [ ] Issue 2 with symptoms/cause/solution
   - [ ] Issue 3 with symptoms/cause/solution
   - [ ] Getting help instructions

### Step 2.4: Add Scripts (If Applicable)

**When to Add Scripts:**
- Validation logic needed
- Data processing utilities
- Testing required

**Guidelines:**
- [ ] Make executable: `chmod +x script-name.py`
- [ ] Add shebang: `#!/usr/bin/env python3`
- [ ] Include docstrings
- [ ] Follow PEP 8 (Python) or language standards
- [ ] Add tests if complex

**Example Structure:**
```python
#!/usr/bin/env python3
"""
Skill Validator - Validates {{SKILL_NAME}} outputs

Usage:
    python3 validator.py [options]
"""

def validate_output(output):
    """Validate skill output format."""
    # Implementation
    pass

if __name__ == "__main__":
    # CLI entry point
    pass
```

### Step 2.5: Add Assets (If Applicable)

**When to Add Assets:**
- Configuration data needed
- Pattern databases required
- Reference materials helpful

**Guidelines:**
- [ ] Use JSON for structured data
- [ ] Use kebab-case filenames
- [ ] Document in assets/README.md
- [ ] Keep files focused and modular

### Step 2.6: Create CHANGELOG.md

**Guidelines:**
- [ ] Follow Keep a Changelog format
- [ ] Document initial release (v1.0.0)
- [ ] Add release date
- [ ] List all features
- [ ] Add design decisions section
- [ ] Plan next version features

---

## Phase 3: Testing & Validation (1-3 hours)

### Step 3.1: Manual Testing

**For New Skills:**
- [ ] Test with Claude Code (if applicable)
- [ ] Test with Claude web chat (if applicable)
- [ ] Verify all examples work
- [ ] Check edge cases
- [ ] Validate error handling

**For Forks:**
- [ ] Test original functionality preserved
- [ ] Test with AISkills structure
- [ ] Verify documentation accuracy

### Step 3.2: Automated Testing (If Scripts Exist)

```bash
# Run tests
pytest scripts/test_*.py -v

# Check coverage
pytest --cov=scripts scripts/

# Lint
ruff check scripts/
black --check scripts/
```

**Checklist:**
- [ ] All tests passing
- [ ] Coverage > 80% (if applicable)
- [ ] No linting errors

### Step 3.3: Documentation Review

```bash
# Check word counts
wc -w SKILL.md        # Should be < 500
wc -w README.md       # Should be 1000-2000

# Validate links
# (manual check - ensure all references/ links work)

# Check for placeholders missed
grep -r "{{" .
```

**Checklist:**
- [ ] No {{PLACEHOLDERS}} remaining
- [ ] All links work
- [ ] Word counts appropriate
- [ ] Spelling checked

### Step 3.4: Peer Review (NEW SKILLS ONLY)

**Required for NEW skills (building from scratch):**

```bash
# Gemini review
cd ../{{skill-name}}
gemini "Review this new skill implementation for quality, design, and improvements. Focus on: SKILL.md clarity, documentation completeness, example quality, and potential issues." --files .

# Codex review
codex "Review this new skill for code quality, design patterns, and improvements. Focus on: file structure, documentation standards, example effectiveness, and maintainability." --files .
```

**Checklist:**
- [ ] Gemini review completed
- [ ] Codex review completed
- [ ] Recommendations documented
- [ ] Critical issues addressed
- [ ] Improvements implemented

**SKIP for forked/integrated skills** (already validated externally)

---

## Phase 4: Packaging (30 min)

### Step 4.1: Create LICENSE

```bash
# Use MIT license template
cp ../SkillTemplate/skill-template/LICENSE.template ./LICENSE

# Update placeholders
sed -i '' "s/{{YEAR}}/$(date +%Y)/g" LICENSE
sed -i '' "s/{{AUTHOR_NAME}}/Lee Gonzales/g" LICENSE
```

**Checklist:**
- [ ] LICENSE file created
- [ ] Year and author updated
- [ ] MIT License (or compatible)

### Step 4.2: Package Skill

```bash
# From AISkills root directory
cd /Users/leegonzales/Projects/leegonzales/AISkills

# Run packaging script (from SKILL-9)
./scripts/package-skill.sh {{SkillName}}/{{skill-name}}
```

**Script will:**
1. Validate SKILL.md exists and well-formed
2. Check required files
3. Create versioned ZIP: `{{skill-name}}-vX.Y.Z.skill`
4. Generate SHA256 checksum
5. Place in dist/ directory

**Checklist:**
- [ ] .skill file created in dist/
- [ ] SHA256 checksum generated
- [ ] Package size reasonable (<50KB typical)
- [ ] ZIP contains all required files

### Step 4.3: Verify Package

```bash
# Check package contents
unzip -l dist/{{skill-name}}-v1.0.0.skill

# Verify checksum
shasum -a 256 -c dist/{{skill-name}}-v1.0.0.skill.sha256
```

**Checklist:**
- [ ] All expected files in package
- [ ] Checksum matches
- [ ] No __pycache__ or temp files
- [ ] Size appropriate

---

## Phase 5: Documentation & Integration (1-2 hours)

### Step 5.1: Update Main README

**Add skill to README.md:**

```markdown
### {{SKILL_NUMBER}}. {{Skill Title}} (v1.0.0)

{{Brief Description}}

**Features:**
- {{Feature 1}}
- {{Feature 2}}
- {{Feature 3}}

**Use for:**
- {{Use case 1}}
- {{Use case 2}}
- {{Use case 3}}

**[View {{Skill Title}} →]({{SkillName}}/)**

---
```

**Update installation section:**
```markdown
# Add to Claude Code installation
cp -r /path/to/AISkills/{{SkillName}}/{{skill-name}} ./
```

**Update download links:**
```markdown
- **{{Skill Title}} v1.0.0**: [Download](https://github.com/leegonzales/AISkills/raw/main/{{SkillName}}/dist/{{skill-name}}-v1.0.0.skill)
```

**Update version history table:**
```markdown
| {{Skill Title}} | v1.0.0 | {{DATE}} | Initial release - {{Brief description}} |
```

**Update skill count:**
```markdown
**Current Skills**: {{NEW_COUNT}} | **Total Downloads**: {{NEW_SIZE}}KB
```

**Checklist:**
- [ ] Skill added to README.md
- [ ] Installation instructions updated
- [ ] Download link added
- [ ] Version history updated
- [ ] Skill count updated

### Step 5.2: Test README Links

```bash
# Test local links work
ls -la {{SkillName}}/
ls -la {{SkillName}}/{{skill-name}}/SKILL.md
ls -la {{SkillName}}/dist/{{skill-name}}-v1.0.0.skill
```

**Checklist:**
- [ ] All local paths valid
- [ ] Skill directory exists
- [ ] Package file exists
- [ ] README renders correctly

---

## Phase 6: Version Control (30 min)

### Step 6.1: Git Add & Commit

```bash
# Stage all changes
git add {{SkillName}}/ README.md

# Commit with conventional message
git commit -m "$(cat <<'EOF'
feat: Add {{Skill Title}} skill v1.0.0

Add {{skill type}} skill with:
- {{Key feature 1}}
- {{Key feature 2}}
- {{Key feature 3}}

{{Additional context about the skill}}

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

**Checklist:**
- [ ] All new files staged
- [ ] README.md staged
- [ ] Commit message follows convention
- [ ] Co-authored attribution added

### Step 6.2: Push to Branch

```bash
# Determine branch strategy
# Option A: Feature branch (recommended for review)
git checkout -b feature/{{skill-name}}
git push -u origin feature/{{skill-name}}

# Option B: Direct to main (if confident)
git push origin main
```

**Checklist:**
- [ ] Branch created (if using feature branch)
- [ ] Pushed to remote
- [ ] Verify on GitHub

---

## Phase 7: Pull Request (Optional, 30 min)

**If using feature branch:**

### Step 7.1: Create PR

```bash
gh pr create --title "feat: Add {{Skill Title}} skill v1.0.0" --body "$(cat <<'EOF'
## Summary
Add {{Skill Title}} skill to the AISkills collection.

## Features
- {{Feature 1}}
- {{Feature 2}}
- {{Feature 3}}

## Testing
- [ ] Tested with Claude Code
- [ ] Tested with web chat
- [ ] All examples validated
- [ ] Documentation reviewed
- [ ] Peer review completed (if new skill)

## Documentation
- Complete README with usage examples
- Reference documentation in references/
- CHANGELOG with version history

## Files Changed
- **{{N}} new files** in {{SkillName}}/
- **README.md updated**

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

**Checklist:**
- [ ] PR created
- [ ] Title follows convention
- [ ] Description complete
- [ ] Testing checklist filled

### Step 7.2: Review & Merge

**Self-review checklist:**
- [ ] All files present in PR
- [ ] No unintended changes
- [ ] README updates correct
- [ ] Links valid

**Merge:**
```bash
# After approval
gh pr merge {{PR_NUMBER}} --squash --delete-branch
```

**Checklist:**
- [ ] PR reviewed
- [ ] Tests passing (if CI configured)
- [ ] Merged to main
- [ ] Branch deleted

---

## Phase 8: Post-Integration (15 min)

### Step 8.1: Update Tracking

**If using Beads:**
```bash
bd close SKILL-{{N}} "Skill integrated and merged to main"
```

**If using GitHub Issues:**
- Close related issues
- Update project board

**Checklist:**
- [ ] Issue tracker updated
- [ ] Status marked complete

### Step 8.2: Verify Live

```bash
# Pull latest main
git checkout main
git pull origin main

# Verify skill present
ls -la {{SkillName}}/{{skill-name}}/

# Test download link (after merge)
curl -I https://github.com/leegonzales/AISkills/raw/main/{{SkillName}}/dist/{{skill-name}}-v1.0.0.skill
```

**Checklist:**
- [ ] Skill in main branch
- [ ] Download link works (200 OK)
- [ ] README renders correctly on GitHub

### Step 8.3: Test Installation

**Claude Code:**
```bash
# Test global install
cp -r {{SkillName}}/{{skill-name}} ~/.claude/skills/
# Verify skill discovered by Claude
```

**Claude Web Chat:**
1. Download the .skill file
2. Upload to claude.ai
3. Verify skill loads
4. Test basic functionality

**Checklist:**
- [ ] Claude Code installation works
- [ ] Web chat upload works
- [ ] Skill functional in both environments

---

## Success Criteria

**Skill Integration Complete When:**

✅ **Structure**
- All required files present (SKILL.md, README.md, CHANGELOG.md, LICENSE)
- Optional components added as needed (references/, scripts/, assets/)
- Template placeholders replaced

✅ **Documentation**
- SKILL.md under 500 words
- README.md comprehensive (1000-2000 words)
- References complete (examples, advanced, troubleshooting)
- No dead links

✅ **Quality**
- Manual testing completed
- Automated tests passing (if applicable)
- Peer review completed (NEW skills only)
- No critical issues

✅ **Packaging**
- .skill file generated
- SHA256 checksum created
- Package validated

✅ **Integration**
- Main README updated
- Committed to version control
- Pushed to GitHub
- PR merged (if using)

✅ **Verification**
- Download link works
- Skill functional in Claude Code
- Skill functional in web chat

---

## Common Pitfalls

### Pitfall 1: Verbose SKILL.md
**Problem:** SKILL.md exceeds 500 words, wastes context
**Solution:** Move detailed content to references/examples.md

### Pitfall 2: Missing Placeholders
**Problem:** {{PLACEHOLDERS}} remain in final files
**Solution:** Use `grep -r "{{" .` to find all placeholders

### Pitfall 3: Broken Links
**Problem:** README links to files that don't exist
**Solution:** Manually verify all links before committing

### Pitfall 4: Skipping Peer Review
**Problem:** New skills without peer review may have quality issues
**Solution:** ALWAYS run Gemini + Codex for NEW skills (forks exempted)

### Pitfall 5: Package Bloat
**Problem:** .skill file includes __pycache__, .DS_Store, etc.
**Solution:** Use .gitignore patterns in package script

---

## Time Estimates

| Skill Complexity | Preparation | Development | Testing | Packaging | Integration | Total |
|-----------------|-------------|-------------|---------|-----------|-------------|-------|
| **Simple** | 30 min | 2-3 hours | 1 hour | 30 min | 1 hour | 4-6 hours |
| **Moderate** | 30 min | 4-6 hours | 2 hours | 30 min | 1 hour | 6-10 hours |
| **Complex** | 1 hour | 6-10 hours | 3 hours | 1 hour | 1 hour | 10-15 hours |

**Simple:** Basic validation/analysis (e.g., simple format converter)
**Moderate:** Multi-capability skills (e.g., Dad Joke Validator)
**Complex:** Skills with heavy logic, multiple integrations, or novel capabilities

---

## Quick Reference Commands

```bash
# Setup
cd /Users/leegonzales/Projects/leegonzales/AISkills
mkdir -p {{SkillName}}
cp -r SkillTemplate/skill-template {{SkillName}}/{{skill-name}}

# Validate
wc -w {{skill-name}}/SKILL.md  # < 500 words
grep -r "{{" {{skill-name}}/    # No placeholders

# Test
pytest {{skill-name}}/scripts/test_*.py -v

# Package
./scripts/package-skill.sh {{SkillName}}/{{skill-name}}

# Commit
git add {{SkillName}}/ README.md
git commit -m "feat: Add {{Skill Title}} v1.0.0"
git push

# Verify
curl -I https://github.com/leegonzales/AISkills/raw/main/{{SkillName}}/dist/{{skill-name}}-v1.0.0.skill
```

---

**Document Version:** 1.0
**Last Updated:** 2025-11-16
**Maintained By:** AISkills Collection

Use this runbook for every skill integration to ensure consistency and quality.
