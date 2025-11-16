# SKILL-8: Create Skill Template and Integration Runbook

**Subagent Specification for Autonomous Execution**

**Mission:** Create a standardized skill template directory and integration runbook that accelerates all future skill integrations in the AISkills collection. Use the Dad Joke Validator as the reference implementation.

**Context:** We've successfully built Dad Joke Validator v1.1.0 with professional structure. This task extracts that pattern into a reusable template that will 10x our velocity for the 10+ skill integrations planned.

**Priority:** P1 (BLOCKS SKILL-10, SKILL-13, SKILL-19, and all future integrations)

**Estimated Effort:** 6-8 hours

**Subagent Readiness:** 95% (follows proven pattern from SUBAGENT_SPEC_TEMPLATE.md)

---

## Part 1: Project Setup

**Working Directory:** `/Users/leegonzales/Projects/leegonzales/AISkills/`

**Validation Commands:**
```bash
# Verify we're in the right place
pwd  # Should show: /Users/leegonzales/Projects/leegonzales/AISkills
ls -la DadJokeValidator/  # Verify Dad Joke Validator exists (our reference)

# Create working directory for SKILL-8
mkdir -p SkillTemplate
cd SkillTemplate
```

**Success Criteria:**
- ✅ Working directory created
- ✅ Dad Joke Validator available as reference
- ✅ Ready to build template

---

## Part 2: Analyze Reference Implementation

**Task:** Study Dad Joke Validator structure to extract patterns

**Commands:**
```bash
# Examine Dad Joke Validator structure
tree ../DadJokeValidator/dad-joke-validator -L 2

# Read key files to understand pattern
cat ../DadJokeValidator/dad-joke-validator/SKILL.md | head -50
cat ../DadJokeValidator/dad-joke-validator/README.md | head -100
ls -la ../DadJokeValidator/dad-joke-validator/
```

**What to Extract:**
1. **Required files** (SKILL.md, README.md, LICENSE, CHANGELOG.md)
2. **Optional directories** (references/, scripts/, assets/, dist/)
3. **Frontmatter format** (YAML in SKILL.md)
4. **Documentation patterns** (progressive disclosure)
5. **File naming conventions** (kebab-case)
6. **Version format** (vX.Y.Z)

**Success Criteria:**
- ✅ Documented Dad Joke Validator structure
- ✅ Identified required vs optional components
- ✅ Pattern extraction complete

---

## Part 3: Create Template Directory Structure

**Task:** Build complete skill-template/ directory with all standard files

**Structure to Create:**
```
skill-template/
├── SKILL.md.template           # Core skill definition template
├── README.md.template           # Comprehensive documentation template
├── CHANGELOG.md.template        # Version history template
├── LICENSE.template             # MIT license template
├── .gitignore                   # Standard ignores
├── references/                  # Progressive disclosure templates
│   ├── examples.md.template
│   ├── advanced-usage.md.template
│   └── troubleshooting.md.template
├── scripts/                     # Utility scripts templates
│   ├── validator.py.template    # Optional validation script
│   └── README.md                # Explains scripts/ purpose
├── assets/                      # Supporting data templates
│   └── README.md                # Explains assets/ purpose
└── dist/                        # Packaged releases (empty initially)
    └── README.md                # Explains dist/ purpose
```

**File: SKILL.md.template**
```markdown
---
name: {{SKILL_NAME}}
description: {{SKILL_DESCRIPTION}}
version: 1.0.0
---

# {{SKILL_TITLE}}

{{BRIEF_OVERVIEW}}

## When to Use

Invoke when user:
- {{TRIGGER_PHRASE_1}}
- {{TRIGGER_PHRASE_2}}
- {{TRIGGER_PHRASE_3}}

## Core Capabilities

### 1. {{CAPABILITY_1_NAME}}

{{CAPABILITY_1_DESCRIPTION}}

**Example:**
```
{{CAPABILITY_1_EXAMPLE}}
```

### 2. {{CAPABILITY_2_NAME}}

{{CAPABILITY_2_DESCRIPTION}}

## How to Use

**Basic Usage:**
```
{{BASIC_USAGE_EXAMPLE}}
```

**Advanced Usage:**
```
{{ADVANCED_USAGE_EXAMPLE}}
```

## Output Format

{{OUTPUT_FORMAT_DESCRIPTION}}

## Limitations

- {{LIMITATION_1}}
- {{LIMITATION_2}}

## Best Practices

1. **{{BEST_PRACTICE_1_NAME}}**: {{BEST_PRACTICE_1_DESCRIPTION}}
2. **{{BEST_PRACTICE_2_NAME}}**: {{BEST_PRACTICE_2_DESCRIPTION}}

## References

For detailed examples and advanced usage, see:
- `references/examples.md` - Worked examples
- `references/advanced-usage.md` - Advanced patterns
- `references/troubleshooting.md` - Common issues

---

**Note:** Keep this file under 500 words for context efficiency. Detailed content goes in references/.
```

**File: README.md.template**
```markdown
# {{SKILL_TITLE}}

{{COMPREHENSIVE_DESCRIPTION}}

## Features

- {{FEATURE_1}}
- {{FEATURE_2}}
- {{FEATURE_3}}

## Installation

### For Claude Code

```bash
# Install globally
cp -r {{skill-name}} ~/.claude/skills/

# Or install for specific project
cp -r {{skill-name}} your-project/.claude/skills/
```

### For Claude Web Chat

Download the packaged skill file:
- [{{skill-name}}-v1.0.0.skill](dist/{{skill-name}}-v1.0.0.skill)

Then upload to Claude:
1. Go to [claude.ai](https://claude.ai)
2. Navigate to Settings > Capabilities
3. Click "Upload skill"
4. Select the .skill file

## Usage

### Basic Example

{{BASIC_USAGE_EXAMPLE_WITH_CONTEXT}}

### Advanced Example

{{ADVANCED_USAGE_EXAMPLE_WITH_CONTEXT}}

## Documentation

- **[SKILL.md](SKILL.md)** - Core skill definition (read by Claude)
- **[examples.md](references/examples.md)** - Detailed usage examples
- **[advanced-usage.md](references/advanced-usage.md)** - Advanced patterns
- **[troubleshooting.md](references/troubleshooting.md)** - Common issues and solutions

## Development

### Testing

{{TESTING_INSTRUCTIONS}}

### Building

To package this skill:
```bash
../../scripts/package-skill.sh {{skill-name}}
```

## Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Questions?

- **Usage Issues:** Check [troubleshooting.md](references/troubleshooting.md)
- **Feature Requests:** Open an issue
- **General Help:** See [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)

---

Built with Claude Code | Part of [AISkills Collection](https://github.com/leegonzales/AISkills)
```

**File: CHANGELOG.md.template**
```markdown
# Changelog

All notable changes to {{SKILL_NAME}} will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - {{RELEASE_DATE}}

### Added
- Initial release of {{SKILL_NAME}}
- {{FEATURE_1}}
- {{FEATURE_2}}
- {{FEATURE_3}}

### Features
- {{DETAILED_FEATURE_1}}
- {{DETAILED_FEATURE_2}}

### Documentation
- Complete README with installation and usage
- Reference documentation in references/
- {{ADDITIONAL_DOCS}}

## [Unreleased]

### Planned for v1.1
- {{FUTURE_FEATURE_1}}
- {{FUTURE_FEATURE_2}}

### Under Consideration
- {{CONSIDERATION_1}}
- {{CONSIDERATION_2}}

---

[1.0.0]: https://github.com/leegonzales/AISkills/releases/tag/{{skill-name}}-v1.0.0
```

**File: LICENSE.template**
```
MIT License

Copyright (c) {{YEAR}} {{AUTHOR_NAME}}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**File: .gitignore**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.pytest_cache/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Skill-specific
*.skill.tmp
```

**File: references/examples.md.template**
```markdown
# {{SKILL_NAME}} Examples

Detailed examples demonstrating {{SKILL_NAME}} capabilities.

## Example 1: {{EXAMPLE_1_TITLE}}

**Scenario:** {{EXAMPLE_1_SCENARIO}}

**Input:**
```
{{EXAMPLE_1_INPUT}}
```

**Output:**
```
{{EXAMPLE_1_OUTPUT}}
```

**Explanation:** {{EXAMPLE_1_EXPLANATION}}

---

## Example 2: {{EXAMPLE_2_TITLE}}

**Scenario:** {{EXAMPLE_2_SCENARIO}}

**Input:**
```
{{EXAMPLE_2_INPUT}}
```

**Output:**
```
{{EXAMPLE_2_OUTPUT}}
```

**Explanation:** {{EXAMPLE_2_EXPLANATION}}

---

## Example 3: {{EXAMPLE_3_TITLE}}

**Scenario:** {{EXAMPLE_3_SCENARIO}}

**Input:**
```
{{EXAMPLE_3_INPUT}}
```

**Output:**
```
{{EXAMPLE_3_OUTPUT}}
```

**Explanation:** {{EXAMPLE_3_EXPLANATION}}

---

## Advanced Example: {{ADVANCED_EXAMPLE_TITLE}}

**Scenario:** {{ADVANCED_EXAMPLE_SCENARIO}}

**Input:**
```
{{ADVANCED_EXAMPLE_INPUT}}
```

**Output:**
```
{{ADVANCED_EXAMPLE_OUTPUT}}
```

**Explanation:** {{ADVANCED_EXAMPLE_EXPLANATION}}

---

For more examples, see the main [README.md](../README.md).
```

**File: references/advanced-usage.md.template**
```markdown
# {{SKILL_NAME}} Advanced Usage

Advanced patterns and techniques for {{SKILL_NAME}}.

## Pattern 1: {{PATTERN_1_NAME}}

**Use When:** {{PATTERN_1_USE_CASE}}

**Implementation:**
```
{{PATTERN_1_IMPLEMENTATION}}
```

**Benefits:**
- {{PATTERN_1_BENEFIT_1}}
- {{PATTERN_1_BENEFIT_2}}

---

## Pattern 2: {{PATTERN_2_NAME}}

**Use When:** {{PATTERN_2_USE_CASE}}

**Implementation:**
```
{{PATTERN_2_IMPLEMENTATION}}
```

**Benefits:**
- {{PATTERN_2_BENEFIT_1}}
- {{PATTERN_2_BENEFIT_2}}

---

## Integration with Other Skills

### With {{OTHER_SKILL_1}}

{{INTEGRATION_DESCRIPTION_1}}

### With {{OTHER_SKILL_2}}

{{INTEGRATION_DESCRIPTION_2}}

---

## Performance Optimization

### Tip 1: {{OPTIMIZATION_TIP_1}}

{{OPTIMIZATION_DESCRIPTION_1}}

### Tip 2: {{OPTIMIZATION_TIP_2}}

{{OPTIMIZATION_DESCRIPTION_2}}

---

For basic usage, see [examples.md](examples.md).
```

**File: references/troubleshooting.md.template**
```markdown
# {{SKILL_NAME}} Troubleshooting

Common issues and solutions for {{SKILL_NAME}}.

## Issue: {{ISSUE_1_TITLE}}

**Symptoms:** {{ISSUE_1_SYMPTOMS}}

**Cause:** {{ISSUE_1_CAUSE}}

**Solution:**
```
{{ISSUE_1_SOLUTION}}
```

---

## Issue: {{ISSUE_2_TITLE}}

**Symptoms:** {{ISSUE_2_SYMPTOMS}}

**Cause:** {{ISSUE_2_CAUSE}}

**Solution:**
```
{{ISSUE_2_SOLUTION}}
```

---

## Issue: {{ISSUE_3_TITLE}}

**Symptoms:** {{ISSUE_3_SYMPTOMS}}

**Cause:** {{ISSUE_3_CAUSE}}

**Solution:**
```
{{ISSUE_3_SOLUTION}}
```

---

## Getting Help

If you encounter an issue not listed here:

1. Check the [examples.md](examples.md) for correct usage
2. Review the [advanced-usage.md](advanced-usage.md) for patterns
3. Open an issue on GitHub with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (Claude Code version, OS, etc.)

---

For general usage, see the main [README.md](../README.md).
```

**File: scripts/README.md**
```markdown
# Scripts Directory

This directory contains utility scripts for {{SKILL_NAME}}.

## Common Scripts

### validator.py
Validates skill functionality and outputs (optional).

**Usage:**
```bash
python3 validator.py [options]
```

### test_*.py
Test suites for skill validation (if applicable).

**Usage:**
```bash
pytest test_*.py -v
```

## Creating New Scripts

When adding scripts:
1. Make them executable: `chmod +x script-name.py`
2. Add shebang: `#!/usr/bin/env python3`
3. Include usage documentation in docstring
4. Follow PEP 8 style guidelines

---

Scripts are optional but recommended for skills with:
- Complex validation logic
- Data processing utilities
- Testing requirements
```

**File: assets/README.md**
```markdown
# Assets Directory

This directory contains supporting data files for {{SKILL_NAME}}.

## Common Asset Types

### JSON Configuration Files
- Pattern databases
- Configuration templates
- Reference data

### Data Files
- CSV datasets
- Sample inputs
- Test fixtures

### Templates
- Output templates
- Report formats

## File Naming

Use kebab-case for consistency:
- `pun-patterns.json` ✅
- `Pun_Patterns.json` ❌

## Documentation

Document each asset's purpose and format in this README or inline comments.

---

Assets are optional but recommended for skills with:
- Configuration data
- Pattern databases
- Reference materials
```

**File: dist/README.md**
```markdown
# Distribution Directory

This directory contains packaged `.skill` files for Claude web chat.

## Contents

Packaged releases in ZIP format:
- `{{skill-name}}-v1.0.0.skill` - Version 1.0.0 release
- `{{skill-name}}-v1.0.0.skill.sha256` - SHA256 checksum

## Creating Packages

To create a new package:
```bash
# From AISkills root
./scripts/package-skill.sh {{skill-name}}
```

This will:
1. Validate skill structure
2. Create versioned ZIP file
3. Generate SHA256 checksum
4. Place files in this directory

## Installation

Users can download and upload these files to Claude web chat:
1. Download the `.skill` file
2. Go to claude.ai > Settings > Capabilities
3. Click "Upload skill"
4. Select the downloaded file

---

For Claude Code, users install from the source directory, not dist/.
```

**Commands to Create Structure:**
```bash
cd SkillTemplate

# Create all directories
mkdir -p skill-template/{references,scripts,assets,dist}

# Create all template files
cat > skill-template/SKILL.md.template << 'EOF'
[PASTE COMPLETE CONTENT FROM ABOVE]
EOF

# Repeat for all other files...
# (I'll provide complete commands in execution)
```

**Success Criteria:**
- ✅ Complete skill-template/ directory created
- ✅ All 15+ files present with proper content
- ✅ Templates use {{PLACEHOLDER}} format consistently
- ✅ Structure matches Dad Joke Validator pattern

---

## Part 4: Create Integration Runbook

**Task:** Write step-by-step integration guide

**File: INTEGRATION_RUNBOOK.md**

```markdown
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
```

**Commands to Create Runbook:**
```bash
cat > INTEGRATION_RUNBOOK.md << 'EOF'
[PASTE COMPLETE CONTENT FROM ABOVE]
EOF
```

**Success Criteria:**
- ✅ Complete integration runbook created
- ✅ All 8 phases documented
- ✅ Checklists for each step
- ✅ Time estimates provided
- ✅ Quick reference commands included

---

## Part 5: Create Customization Guide

**Task:** Document how to adapt template for different skill types

**File: CUSTOMIZATION_GUIDE.md**

```markdown
# Skill Template Customization Guide

How to adapt the skill-template for different skill types and requirements.

---

## Quick Start

### Step 1: Copy Template
```bash
cp -r skill-template/ ../{{SkillName}}/{{skill-name}}/
cd ../{{SkillName}}/{{skill-name}}/
```

### Step 2: Identify Your Skill Type

**Type A: Analysis/Validation** (e.g., Claimify, Dad Joke Validator)
- Keep: scripts/ (validation logic)
- Keep: assets/ (pattern data)
- Keep: all references/

**Type B: Generation/Creation** (e.g., Research-to-Essay, Concept Forge)
- Keep: references/ (methodology docs)
- Optional: scripts/ (helper utilities)
- Optional: assets/ (templates)

**Type C: Workflow/Process** (e.g., Process Mapper, Context Continuity)
- Keep: references/ (workflow examples)
- Remove: scripts/ (usually not needed)
- Remove: assets/ (usually not needed)

**Type D: Integration** (e.g., Codex/Gemini Peer Review)
- Keep: scripts/ (integration code)
- Keep: references/ (API usage examples)
- Optional: assets/ (configuration)

### Step 3: Replace Placeholders

**Required Replacements:**
```bash
# In all files
{{SKILL_NAME}} → your-skill-name
{{SKILL_TITLE}} → Your Skill Title
{{SKILL_DESCRIPTION}} → Brief one-sentence description

# In LICENSE
{{YEAR}} → 2025
{{AUTHOR_NAME}} → Lee Gonzales

# In CHANGELOG.md
{{RELEASE_DATE}} → 2025-11-16
```

**Context-Specific Replacements:**
- {{FEATURE_*}} → Your skill features
- {{CAPABILITY_*}} → Your skill capabilities
- {{EXAMPLE_*}} → Your actual examples
- {{TRIGGER_PHRASE_*}} → How users invoke your skill

---

## Placeholder Reference

### Core Identity
- `{{SKILL_NAME}}` - kebab-case name (e.g., "dad-joke-validator")
- `{{SKILL_TITLE}}` - Title Case name (e.g., "Dad Joke Validator")
- `{{SKILL_DESCRIPTION}}` - One-sentence description
- `{{BRIEF_OVERVIEW}}` - 1-2 paragraph overview

### Functionality
- `{{TRIGGER_PHRASE_1}}` through `{{TRIGGER_PHRASE_3}}` - How to invoke
- `{{CAPABILITY_1_NAME}}` through `{{CAPABILITY_N_NAME}}` - Main capabilities
- `{{CAPABILITY_1_DESCRIPTION}}` - What each capability does
- `{{CAPABILITY_1_EXAMPLE}}` - Example of each capability

### Features & Benefits
- `{{FEATURE_1}}` through `{{FEATURE_N}}` - Feature list
- `{{DETAILED_FEATURE_1}}` - Expanded feature description
- `{{BEST_PRACTICE_1_NAME}}` - Best practice titles
- `{{BEST_PRACTICE_1_DESCRIPTION}}` - Best practice details

### Examples
- `{{BASIC_USAGE_EXAMPLE}}` - Simple usage example
- `{{ADVANCED_USAGE_EXAMPLE}}` - Complex usage example
- `{{EXAMPLE_1_TITLE}}` through `{{EXAMPLE_N_TITLE}}` - Example names
- `{{EXAMPLE_1_SCENARIO}}` - Example context
- `{{EXAMPLE_1_INPUT}}` - Example input
- `{{EXAMPLE_1_OUTPUT}}` - Example output
- `{{EXAMPLE_1_EXPLANATION}}` - Why this example matters

### Documentation
- `{{OUTPUT_FORMAT_DESCRIPTION}}` - How skill formats output
- `{{LIMITATION_1}}` through `{{LIMITATION_N}}` - Known limitations
- `{{FUTURE_FEATURE_1}}` - Planned enhancements
- `{{CONSIDERATION_1}}` - Under consideration features

### Integration
- `{{OTHER_SKILL_1}}` - Skills this integrates with
- `{{INTEGRATION_DESCRIPTION_1}}` - How integration works
- `{{PATTERN_1_NAME}}` - Usage pattern name
- `{{PATTERN_1_USE_CASE}}` - When to use pattern
- `{{PATTERN_1_IMPLEMENTATION}}` - How to implement

### Troubleshooting
- `{{ISSUE_1_TITLE}}` - Common problem title
- `{{ISSUE_1_SYMPTOMS}}` - How to recognize problem
- `{{ISSUE_1_CAUSE}}` - Why problem occurs
- `{{ISSUE_1_SOLUTION}}` - How to fix

### Metadata
- `{{YEAR}}` - Copyright year
- `{{AUTHOR_NAME}}` - Author name
- `{{RELEASE_DATE}}` - Release date (YYYY-MM-DD)

---

## File-by-File Customization

### SKILL.md.template → SKILL.md

**Priority:** CRITICAL (read by Claude every invocation)

**Word Budget:** <500 words

**Customization Checklist:**
- [ ] Replace frontmatter (name, description, version)
- [ ] Write "When to Use" trigger phrases
- [ ] Document 2-5 core capabilities
- [ ] Provide basic + advanced usage examples
- [ ] Describe output format
- [ ] List 2-3 key limitations
- [ ] Reference additional docs

**Example:**
```markdown
---
name: claim-analyzer
description: Extract and map logical claims from text with relationship analysis
version: 1.0.0
---

# Claim Analyzer

Analyze text to extract claims, identify logical relationships, and reveal argument structure.

## When to Use

Invoke when user:
- "Analyze this argument"
- "Map the claims in this text"
- "Identify assumptions in this reasoning"

## Core Capabilities

### 1. Claim Extraction

Identifies factual, normative, and definitional claims.

**Example:**
"Universal healthcare reduces costs" → Factual claim (testable)

### 2. Relationship Mapping

Maps supports, opposes, assumes, refines, contradicts relationships.

## How to Use

**Basic:**
"Analyze this debate transcript for claims"

**Advanced:**
"Map claims with deep analysis, output as JSON"
```

**Remove:**
- Sections not needed for your skill (e.g., remove "Generation" if analysis-only)

**Add:**
- Skill-specific sections (e.g., "Data Format" for data processing skills)

### README.md.template → README.md

**Priority:** HIGH (first user touchpoint)

**Word Budget:** 1000-2000 words

**Customization Checklist:**
- [ ] Write comprehensive feature list (5-10 features)
- [ ] Provide installation instructions (Code + web chat)
- [ ] Include 2-3 usage examples with full context
- [ ] Link to all reference docs
- [ ] Add testing instructions (if applicable)
- [ ] Document build process
- [ ] Include contributing guidelines

**Remove:**
- Development section if no scripts/tests
- Testing section if no automated tests

**Add:**
- Prerequisites section if dependencies required
- Configuration section if customizable
- API reference if exposing functions

### CHANGELOG.md.template → CHANGELOG.md

**Priority:** MEDIUM (documents version history)

**Customization Checklist:**
- [ ] Document initial release features
- [ ] Add release date
- [ ] List design decisions
- [ ] Plan next version features

**Remove:**
- Unreleased section if no plans yet

**Add:**
- Breaking changes section for major versions
- Migration guide if needed

### LICENSE.template → LICENSE

**Priority:** CRITICAL (legal requirement)

**Customization:**
```bash
# Automated replacement
sed -i '' "s/{{YEAR}}/2025/g" LICENSE
sed -i '' "s/{{AUTHOR_NAME}}/Lee Gonzales/g" LICENSE
```

**Alternative Licenses:**
- MIT (recommended - permissive)
- Apache 2.0 (if patent protection needed)
- GPL (if copyleft required)

### references/examples.md.template → references/examples.md

**Priority:** HIGH (users need examples)

**Customization Checklist:**
- [ ] Provide 5-10 realistic examples
- [ ] Include edge cases
- [ ] Show error handling
- [ ] Demonstrate advanced usage

**Example Quality:**
- ✅ Complete input/output shown
- ✅ Real-world scenario
- ✅ Explanation of why example is useful
- ❌ Trivial "hello world" only
- ❌ No context provided

### references/advanced-usage.md.template → references/advanced-usage.md

**Priority:** MEDIUM (for power users)

**Customization Checklist:**
- [ ] Document 3-5 advanced patterns
- [ ] Show integration with other skills
- [ ] Provide performance tips
- [ ] Explain complex configurations

**Remove:**
- If skill is simple with no advanced patterns

### references/troubleshooting.md.template → references/troubleshooting.md

**Priority:** MEDIUM (reduces support burden)

**Customization Checklist:**
- [ ] List 3-5 common issues
- [ ] Provide symptoms for each
- [ ] Explain root cause
- [ ] Give clear solution steps

**Remove:**
- If skill is unlikely to have issues

### scripts/ Directory

**Keep If:**
- Validation logic needed
- Data processing required
- Testing automation helpful

**Remove If:**
- Skill is purely instructional (no code)
- No complex logic to validate

**Customization:**
- Rename validator.py to match purpose
- Add multiple scripts if needed
- Include test files (test_*.py)

### assets/ Directory

**Keep If:**
- Configuration data needed (JSON)
- Pattern databases required
- Templates or fixtures helpful

**Remove If:**
- No external data needed

**Customization:**
- Use JSON for structured data
- Use kebab-case filenames
- Document each file in assets/README.md

---

## Skill Type Templates

### Template: Analysis/Validation Skill

**Example:** Dad Joke Validator, Claimify

**Keep:**
- ✅ scripts/ (validation logic)
- ✅ assets/ (pattern data)
- ✅ All references/

**Structure:**
```
skill-name/
├── SKILL.md              # Analysis methodology
├── README.md
├── CHANGELOG.md
├── LICENSE
├── references/
│   ├── examples.md       # Analyzed examples
│   ├── scoring-guide.md  # (custom) Scoring criteria
│   └── troubleshooting.md
├── scripts/
│   ├── validator.py      # Validation script
│   └── test_validator.py # Tests
├── assets/
│   └── patterns.json     # Pattern database
└── dist/
    └── *.skill
```

**SKILL.md Focus:**
- Analysis dimensions
- Scoring methodology
- Output format

**README.md Focus:**
- What gets analyzed
- Scoring explanation
- Example results

### Template: Generation/Creation Skill

**Example:** Research-to-Essay, Concept Forge

**Keep:**
- ✅ references/ (methodology)
- ⚠️ scripts/ (optional helpers)
- ⚠️ assets/ (optional templates)

**Structure:**
```
skill-name/
├── SKILL.md              # Generation process
├── README.md
├── CHANGELOG.md
├── LICENSE
├── references/
│   ├── examples.md       # Generated examples
│   ├── advanced-usage.md # Complex patterns
│   └── troubleshooting.md
├── scripts/ (optional)
│   └── helper.py         # Utility functions
└── dist/
    └── *.skill
```

**SKILL.md Focus:**
- Generation process
- Methodology steps
- Quality criteria

**README.md Focus:**
- What gets generated
- Process explanation
- Example outputs

### Template: Workflow/Process Skill

**Example:** Process Mapper, Context Continuity

**Keep:**
- ✅ references/ (workflow docs)
- ❌ scripts/ (usually not needed)
- ❌ assets/ (usually not needed)

**Structure:**
```
skill-name/
├── SKILL.md              # Workflow steps
├── README.md
├── CHANGELOG.md
├── LICENSE
├── references/
│   ├── examples.md       # Workflow examples
│   └── advanced-usage.md # Complex workflows
└── dist/
    └── *.skill
```

**SKILL.md Focus:**
- Workflow phases
- Deliverables
- Best practices

**README.md Focus:**
- When to use workflow
- Step-by-step guide
- Example workflows

### Template: Integration Skill

**Example:** Codex Peer Review, Gemini Peer Review

**Keep:**
- ✅ scripts/ (integration code)
- ✅ references/ (API examples)
- ⚠️ assets/ (optional config)

**Structure:**
```
skill-name/
├── SKILL.md              # Integration instructions
├── README.md
├── CHANGELOG.md
├── LICENSE
├── references/
│   ├── examples.md       # API usage examples
│   └── troubleshooting.md # Common API issues
├── scripts/
│   └── integration.py    # API wrapper
└── dist/
    └── *.skill
```

**SKILL.md Focus:**
- How to invoke integration
- Available options
- Response format

**README.md Focus:**
- Prerequisites (API keys, etc.)
- Setup instructions
- Usage examples

---

## Common Customizations

### Adding Custom Sections to SKILL.md

**Pattern:**
```markdown
## {{CUSTOM_SECTION_NAME}}

{{SECTION_CONTENT}}
```

**Examples:**
- Data Format (for data processing skills)
- API Reference (for integration skills)
- Configuration (for configurable skills)

### Adding New Reference Docs

**When to Add:**
- Skill has specialized topic (e.g., "Dad Joke Theory")
- Integration guide needed (e.g., "MCP Server Examples")
- Methodology needs detail (e.g., "Scoring Methodology")

**Pattern:**
```bash
cat > references/custom-doc.md << 'EOF'
# {{Custom Doc Title}}

{{Content}}
EOF
```

**Link from README.md:**
```markdown
- **[custom-doc.md](references/custom-doc.md)** - {{Description}}
```

### Adding Scripts

**Pattern:**
```python
#!/usr/bin/env python3
"""
{{Script Purpose}}

Usage:
    python3 script-name.py [options]
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description="{{Description}}")
    # Add arguments
    args = parser.parse_args()

    # Implementation
    pass

if __name__ == "__main__":
    main()
```

**Make executable:**
```bash
chmod +x scripts/script-name.py
```

### Adding Assets

**Pattern:**
```json
{
  "category_1": [
    "item_1",
    "item_2"
  ],
  "category_2": {
    "key": "value"
  }
}
```

**Document in assets/README.md:**
```markdown
### {{asset-name}}.json

**Purpose:** {{What this file contains}}

**Format:**
```json
{
  "key": "value"
}
```

**Usage:** {{How skill uses this data}}
```

---

## Validation Checklist

Before finishing customization:

### Structure Validation
- [ ] All placeholder {{MARKERS}} replaced
- [ ] Removed unused directories (scripts/ if not needed)
- [ ] All files have appropriate content (no empty templates)

### Content Validation
- [ ] SKILL.md under 500 words
- [ ] README.md between 1000-2000 words
- [ ] All examples are realistic and tested
- [ ] Links to references/ work
- [ ] No dead links

### Technical Validation
- [ ] Scripts executable (`chmod +x`)
- [ ] Python files have shebang (`#!/usr/bin/env python3`)
- [ ] JSON files valid (use `python3 -m json.tool < file.json`)
- [ ] No syntax errors in code

### Documentation Validation
- [ ] Spelling checked
- [ ] Grammar checked
- [ ] Consistent terminology
- [ ] Code examples formatted

### Metadata Validation
- [ ] LICENSE has correct year and author
- [ ] CHANGELOG has release date
- [ ] Version consistent across files
- [ ] Frontmatter complete in SKILL.md

---

## Automated Replacement

**Quick placeholder replacement:**

```bash
#!/bin/bash
# replace-placeholders.sh

SKILL_NAME="your-skill-name"
SKILL_TITLE="Your Skill Title"
SKILL_DESC="Your one-sentence description"
AUTHOR="Lee Gonzales"
YEAR="2025"
DATE="2025-11-16"

# Replace in all files
find . -type f -name "*.md" -o -name "*.template" | while read file; do
  sed -i '' "s/{{SKILL_NAME}}/$SKILL_NAME/g" "$file"
  sed -i '' "s/{{SKILL_TITLE}}/$SKILL_TITLE/g" "$file"
  sed -i '' "s/{{SKILL_DESCRIPTION}}/$SKILL_DESC/g" "$file"
  sed -i '' "s/{{AUTHOR_NAME}}/$AUTHOR/g" "$file"
  sed -i '' "s/{{YEAR}}/$YEAR/g" "$file"
  sed -i '' "s/{{RELEASE_DATE}}/$DATE/g" "$file"
done

# Rename template files
for file in *.template; do
  mv "$file" "${file%.template}"
done
```

**Usage:**
```bash
chmod +x replace-placeholders.sh
./replace-placeholders.sh
```

---

## Skill-Specific Examples

### Example 1: Minimal Skill (No Scripts/Assets)

**Use Case:** Simple instructional skill like "Git Workflow Best Practices"

**Customize:**
1. Remove scripts/ directory
2. Remove assets/ directory
3. Keep only essential references/ (examples.md)
4. Focus on SKILL.md clarity

**Structure:**
```
git-workflow/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── LICENSE
├── references/
│   └── examples.md
└── dist/
```

### Example 2: Analysis Skill with Scripts

**Use Case:** Dad Joke Validator

**Customize:**
1. Keep scripts/ (validator.py, test_validator.py)
2. Keep assets/ (pattern JSONs)
3. Keep all references/ (examples, scoring, theory)
4. Add custom reference (dad-joke-theory.md)

**Structure:**
```
dad-joke-validator/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── LICENSE
├── references/
│   ├── examples.md
│   ├── scoring-guide.md
│   └── dad-joke-theory.md (custom)
├── scripts/
│   ├── validator.py
│   ├── generator.py
│   └── test_validator.py
├── assets/
│   ├── pun-patterns.json
│   └── wholesome-themes.json
└── dist/
```

### Example 3: Integration Skill

**Use Case:** API integration like Gemini Peer Review

**Customize:**
1. Keep scripts/ (API wrapper)
2. Remove assets/ (config in env vars)
3. Add troubleshooting.md (API issues)
4. Document prerequisites clearly

**Structure:**
```
api-integration/
├── SKILL.md
├── README.md (with prerequisites)
├── CHANGELOG.md
├── LICENSE
├── references/
│   ├── examples.md
│   └── troubleshooting.md (API errors)
├── scripts/
│   └── api-wrapper.py
└── dist/
```

---

## Tips & Best Practices

### Tip 1: Start Simple
**Don't over-customize initially**
- Use default structure first
- Add components as needed
- Remove unused parts later

### Tip 2: Test Early
**Validate as you customize**
```bash
# Check word count
wc -w SKILL.md

# Find remaining placeholders
grep -r "{{" .

# Test scripts
python3 scripts/*.py --help
```

### Tip 3: Use Existing Skills as Reference
**Copy patterns from similar skills**
- Analysis skill? → Study Claimify, Dad Joke Validator
- Generation skill? → Study Research-to-Essay, Concept Forge
- Integration skill? → Study Codex/Gemini Peer Review

### Tip 4: Progressive Disclosure
**Keep SKILL.md lean**
- Core instructions only (<500 words)
- Move details to references/
- Link from SKILL.md

### Tip 5: Real Examples
**Use actual use cases**
- ✅ Realistic scenarios users encounter
- ✅ Edge cases that break patterns
- ❌ Trivial "hello world" examples
- ❌ Made-up scenarios nobody uses

---

## Quick Reference

**Most Common Customizations:**
1. Replace core placeholders (name, title, description)
2. Write 3-5 trigger phrases
3. Document 2-5 capabilities with examples
4. Create 5-10 realistic examples
5. Remove unused directories
6. Update LICENSE year/author
7. Validate no placeholders remain

**Validation Command:**
```bash
# Check everything
wc -w SKILL.md && \
grep -r "{{" . && \
ls -la scripts/*.py && \
python3 -m json.tool < assets/*.json && \
echo "✅ Validation complete"
```

---

**Document Version:** 1.0
**Last Updated:** 2025-11-16
**Maintained By:** AISkills Collection

Use this guide to adapt skill-template to any skill type or requirement.
```

**Commands to Create Guide:**
```bash
cat > CUSTOMIZATION_GUIDE.md << 'EOF'
[PASTE COMPLETE CONTENT FROM ABOVE]
EOF
```

**Success Criteria:**
- ✅ Complete customization guide created
- ✅ All placeholder types documented
- ✅ File-by-file customization instructions provided
- ✅ Skill type templates included
- ✅ Validation checklist complete

---

## Part 6: Create Example Skill

**Task:** Demonstrate template usage with a simple working skill

**Create: example-skill/

**This example will be a simple "Text Statistics" skill that:
- Analyzes text for word count, reading time, complexity
- Demonstrates the template pattern
- Shows how to fill placeholders
- Can be used as a reference

I'll create complete specs for this in the next message to avoid hitting length limits.

Would you like me to:
1. **Continue with Part 6-10 of SKILL-8 spec** (complete the spec)
2. **Move to creating SKILL-9 spec** (packaging automation)
3. **Or launch with SKILL-8 as-is and create SKILL-9 in parallel**?

The SKILL-8 spec is already ~95% autonomous-ready with Parts 1-5 complete. Parts 6-10 will add the example skill, testing, and delivery instructions.

What's your preference? 🚀