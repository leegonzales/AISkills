# Claude Code Skill Template

**Professional skill template for rapid Claude Code skill development**

Built from Dad Joke Validator reference implementation. Includes complete template structure, integration runbook, validation tools, and working example.

## Quick Links

- 🚀 **[How to Use](HOW_TO_USE_TEMPLATE.md)** - Start here (5 min quick start)
- 📋 **[Integration Runbook](INTEGRATION_RUNBOOK.md)** - 8-phase integration workflow
- 🎨 **[Customization Guide](CUSTOMIZATION_GUIDE.md)** - Detailed patterns for all skill types
- ✅ **[Validation Scripts](scripts/)** - Automated validation and testing

## What's Included

### 1. skill-template/
Complete template directory with:
- SKILL.md.template (YAML frontmatter + markdown)
- README.md.template (comprehensive documentation)
- CHANGELOG.md.template (version history)
- LICENSE.template (MIT license)
- references/ (progressive disclosure templates)
- scripts/ (optional Python utilities)
- assets/ (optional data files)

### 2. example-skill/
Working "Text Statistics" skill demonstrating:
- Proper placeholder filling
- Dad Joke Validator pattern
- Realistic examples
- Production-ready structure

### 3. Integration Runbook
8-phase workflow:
1. Preparation
2. Content Development
3. Testing & Validation
4. Packaging
5. Documentation & Integration
6. Version Control
7. Pull Request
8. Post-Integration

### 4. Validation Tools
- `validate-skill.sh` - Bash validation script
- `test-skill-loading.py` - Python YAML/loading test

## Quick Start

```bash
# 1. Copy template
cp -r skill-template ../MySkill/my-skill
cd ../MySkill/my-skill

# 2. Fill SKILL.md frontmatter
# Edit name, description

# 3. Customize content
# Edit capabilities, examples

# 4. Validate
../SkillTemplate/scripts/validate-skill.sh .

# 5. Package (once SKILL-9 is ready)
```

## Usage Patterns

### Analysis Skill
Use for: Evaluation, scoring, quality checks
Example: Dad Joke Validator, Code Reviewer

### Generation Skill
Use for: Content creation, template-based output
Example: Meme Generator, ASCII Art

### Workflow Skill
Use for: Multi-step processes, integrations
Example: Research to Essay, Deploy Assistant

### Integration Skill
Use for: External tool coordination
Example: Gemini Peer Review, API Integrator

See [CUSTOMIZATION_GUIDE.md](CUSTOMIZATION_GUIDE.md) for detailed patterns.

## File Specifications

**SKILL.md Requirements:**
- YAML frontmatter with `name` and `description`
- Name: lowercase, hyphens, numbers only (max 64 chars)
- Description: max 1024 chars, include "what" and "when"
- Markdown body: < 500 words (use references/ for details)

**Validation:**
- No unfilled placeholders (`{{...}}`)
- Valid UTF-8 encoding
- Valid JSON in assets/
- Syntax-valid Python in scripts/

## Integration with AISkills

This template enables rapid integration of:
- **SKILL-10**: Research to Essay (workflow)
- **SKILL-13**: Code Explainer (analysis)
- **SKILL-19**: Meeting BS Detector (analysis)
- Future skill discoveries (10+ planned)

Target: 10x velocity on skill integrations using this standardized pattern.

## Reference Implementation

**Dad Joke Validator** served as the reference:
- v1.1.0 with generation capability
- Complete test suite (11 tests, 100% pass)
- Gemini peer-reviewed and improved
- Production-ready with professional structure

## Version

Template v1.0.0 - 2025-11-16

## License

MIT License - Free to use and adapt

---

**Next Steps:**
1. Read [HOW_TO_USE_TEMPLATE.md](HOW_TO_USE_TEMPLATE.md)
2. Study [example-skill/](example-skill/)
3. Build your first skill
4. Validate with scripts/
5. Package and integrate

For integration workflow, see [INTEGRATION_RUNBOOK.md](INTEGRATION_RUNBOOK.md).
