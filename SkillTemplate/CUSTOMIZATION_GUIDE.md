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
- [ ] Replace frontmatter (name, description)
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
find . -type f \( -name "*.md" -o -name "*.template" \) | while read file; do
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
