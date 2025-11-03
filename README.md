# AI Skills Collection

A curated collection of professional skills for Claude Code and Claude web chat, designed for enhanced development, analysis, writing, and reasoning workflows.

## What Are Claude Skills?

Skills are modular, model-invoked capabilities that extend Claude's functionality. Unlike slash commands that require explicit invocation, skills are **automatically discovered and used by Claude based on context**, enabling complex workflows with seamless discovery.

This collection includes skills for:
- **Writing & Communication**: Professional writing, research synthesis, essay creation
- **Analysis & Reasoning**: Argument mapping, concept development, process documentation
- **Development Workflows**: Available in Claude Code for enhanced IDE integration

Many skills work in both Claude Code and Claude web chat, providing flexible capabilities wherever you interact with Claude.

## Skills in This Collection

### 1. Prose Polish (v1.1.0)

Polish writing to professional excellence through systematic craft analysis. Multi-layer assessment of rhythm, voice, and commitment with targeted remediation using proven frameworks.

**Features:**
- Detection & analysis across 4 layers (Lexical, Structural, Rhetorical, Voice)
- Three-pass remediation (Rhythm → Commitment → Voice)
- Prevention mode with anti-cliché prompts
- Register-specific guidelines (Technical, Business, Academic, Creative)

**Use for:**
- Refine drafts to professional excellence
- Analyze writing quality with systematic craft assessment
- Generate polished content with quality-first prompts
- Teach writing craft and quality standards
- 100% detection accuracy validated on real-world samples

**[View Prose Polish →](ProsePolish/)**

---

### 2. Research-to-Essay (v1.0.0)

Systematic workflow for research-driven writing. Transform research into publication-grade essays with thematic synthesis, citation management, and voice calibration.

**Features:**
- 6-phase methodology (Intake → Research → Synthesis → Drafting → Refinement → Delivery)
- Source credibility hierarchy (4-tier system)
- Python synthesis script for multi-source essays
- 5 essay structures, 4 voice profiles
- Platform-specific formatting (Substack, LinkedIn, Academic)

**Use for:**
- Substack/LinkedIn posts requiring research
- Long-form essays synthesizing multiple sources
- Academic writing with proper citations
- Executive briefs with actionable insights
- Publication-grade content with proper attribution

**[View Research-to-Essay →](ResearchToEssay/)**

---

### 3. Concept Forge (v1.0.0)

Transform nebulous ideas into sharp, testable frameworks through multi-perspective interrogation. Dialectical concept development from vague intuition to actionable doctrine.

**Features:**
- 7-stage concept development (Intuition → Communication)
- 13 interrogation archetypes from philosophical traditions
- 5 orchestration patterns (Solo, Duo, Ensemble, Delegated, Transmutation)
- Steelman opposition and pressure-testing techniques
- Embodies "reflection, resistance, refinement" philosophy

**Use for:**
- Clarify vague intuitions ("There's something about X...")
- Structure half-formed frameworks
- Pressure-test ideas with dialectical interrogation
- Distinguish new concepts from existing ones
- Collaborative concept development

**[View Concept Forge →](ConceptForge/)**

---

### 4. Process Mapper (v1.0.0)

Map workflows, extract SOPs, and identify automation opportunities. Systematic process discovery, tacit knowledge documentation, and AI tractability assessment.

**Features:**
- 5-round discovery interview methodology
- 3-state diagnostic (Fiction, Nonexistent, Accurate)
- Shadow process detection
- Automation tractability assessment framework
- Labeled black box approach for tacit knowledge
- Implements "SOP-first doctrine": *You can't automate what you can't see*

**Use for:**
- Document workflows and create SOPs
- Identify automation opportunities
- Capture tribal knowledge before people leave
- Process optimization and bottleneck identification
- AI/automation feasibility assessment

**[View Process Mapper →](ProcessMapper/)**

---

### 5. Claimify (v1.0.0)

Transform messy discourse into structured argument maps. Extract claims, map logical relationships, identify assumptions, and reveal the structure of reasoning.

**Features:**
- 3 analysis depth levels (Surface, Standard, Deep)
- 4 output formats (Table, Graph, Narrative, JSON)
- 6 claim types (Factual, Normative, Definitional, Causal, Predictive, Assumption)
- 5 relationship types (Supports, Opposes, Assumes, Refines, Contradicts)
- Python validator for JSON output

**Use for:**
- Debate analysis
- Strategic document review
- Meeting notes → decision maps
- Research synthesis
- Red-teaming arguments
- Identifying logical gaps and contradictions

**[View Claimify →](Claimifty/)**

---

## Installation

### For Claude Code

Skills are automatically discovered from your skills directories. Install system-wide or per-project.

#### Personal Skills (Available Globally)

```bash
# Navigate to your global skills directory
cd ~/.claude/skills/

# Clone or download, then copy skills
cp -r /path/to/AISkills/ProsePolish/prose-polish ./
cp -r /path/to/AISkills/ResearchToEssay/research-to-essay ./
cp -r /path/to/AISkills/ConceptForge/concept-forge ./
cp -r /path/to/AISkills/ProcessMapper/process-mapper ./
cp -r /path/to/AISkills/Claimifty/claimify ./
```

#### Project Skills (Project-Specific)

```bash
# Install skills for a specific project
cd your-project/
mkdir -p .claude/skills

# Copy desired skills
cp -r /path/to/AISkills/ProsePolish/prose-polish .claude/skills/
cp -r /path/to/AISkills/ResearchToEssay/research-to-essay .claude/skills/
# ... add others as needed
```

**Documentation:** [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)

---

### For Claude Web Chat

Each skill includes a versioned `.skill` file in its `dist/` folder. Simply download and upload to any Claude conversation.

#### Download Links

- **Prose Polish v1.1.0**: [prose-polish-v1.1.0.skill](ProsePolish/dist/prose-polish-v1.1.0.skill)
- **Research-to-Essay v1.0.0**: [research-to-essay-v1.0.0.skill](ResearchToEssay/dist/research-to-essay-v1.0.0.skill)
- **Concept Forge v1.0.0**: [concept-forge-v1.0.0.skill](ConceptForge/dist/concept-forge-v1.0.0.skill)
- **Process Mapper v1.0.0**: [process-mapper-v1.0.0.skill](ProcessMapper/dist/process-mapper-v1.0.0.skill)
- **Claimify v1.0.0**: [claimify-v1.0.0.skill](Claimifty/dist/claimify-v1.0.0.skill)

#### Upload Instructions

1. Go to [claude.ai](https://claude.ai)
2. Start a new conversation or open an existing one
3. Click the attachment button (📎)
4. Upload the `.skill` file
5. The skill will be available for that conversation

**Note:** Skills uploaded to Claude web chat are conversation-specific and persist for that conversation only.

---

## Using Skills

Once installed, skills are **automatically invoked by Claude** based on your natural language requests. No special commands required.

### Example Triggers

**Prose Polish:**
```
"Analyze this text for writing quality"
"Polish this draft to professional standards"
```

**Research-to-Essay:**
```
"Research and write a Substack post about distributed systems"
"Create a LinkedIn post about AI safety governance"
```

**Concept Forge:**
```
"Help me develop this vague idea into a framework"
"Pressure-test this concept from multiple angles"
```

**Process Mapper:**
```
"Help me document our customer onboarding process"
"Analyze this workflow for automation opportunities"
```

**Claimify:**
```
"Analyze this argument and map the claims"
"What assumptions does this reasoning make?"
```

---

## Repository Structure

```
AISkills/
├── README.md                           # This file
├── ProsePolish/                        # Writing quality analysis
│   ├── dist/
│   │   └── prose-polish-v1.1.0.skill
│   ├── prose-polish/                   # Source skill
│   ├── CHANGELOG.md
│   └── README.md
├── ResearchToEssay/                    # Research-driven writing
│   ├── dist/
│   │   └── research-to-essay-v1.0.0.skill
│   ├── research-to-essay/              # Source skill
│   └── README.md
├── ConceptForge/                       # Dialectical concept development
│   ├── dist/
│   │   └── concept-forge-v1.0.0.skill
│   ├── concept-forge/                  # Source skill
│   └── README.md
├── ProcessMapper/                      # SOP documentation & automation
│   ├── dist/
│   │   └── process-mapper-v1.0.0.skill
│   ├── process-mapper/                 # Source skill
│   └── README.md
└── Claimifty/                          # Argument structure analysis
    ├── dist/
    │   └── claimify-v1.0.0.skill
    ├── claimify/                       # Source skill
    └── README.md
```

Each skill follows a standardized structure:

```
SkillName/
├── dist/
│   └── skill-name-vX.Y.Z.skill        # Versioned release for web chat
├── skill-name/                         # Source skill directory
│   ├── SKILL.md                        # Required: Skill definition
│   ├── references/                     # Optional: Reference docs
│   └── assets/ or scripts/             # Optional: Supporting files
└── README.md                           # Skill documentation
```

---

## Skill Design Philosophy

All skills in this collection follow these principles:

1. **Concise Core**: Lean skill definitions optimized for context efficiency
2. **Progressive Disclosure**: Essential content in SKILL.md, examples in references
3. **Appropriate Freedom**: Guidelines over rigid rules for Claude's flexibility
4. **Research-Backed**: Incorporating proven frameworks and validated patterns
5. **Examples Over Explanation**: Worked examples showing real usage
6. **Versioned Releases**: Semantic versioning for all packaged skills

---

## Version History

| Skill | Version | Release Date | Notes |
|-------|---------|--------------|-------|
| Prose Polish | v1.1.0 | 2025-11-01 | Enhanced detection patterns, 100% accuracy validation |
| Research-to-Essay | v1.0.0 | 2025-11-02 | Initial release |
| Concept Forge | v1.0.0 | 2025-11-02 | Initial release |
| Process Mapper | v1.0.0 | 2025-11-02 | Initial release |
| Claimify | v1.0.0 | 2025-10-31 | Initial release |

---

## Creating Your Own Skills

Want to build a custom skill? Each skill directory demonstrates best practices:

### Minimal Skill Structure

```
my-skill/
├── SKILL.md              # Required: Name, description, instructions
├── references/           # Optional: Examples and additional docs
│   └── examples.md
└── scripts/              # Optional: Utilities and validators
    └── helper.py
```

### SKILL.md Format

```yaml
---
name: my-skill
description: Clear description of what the skill does and when to use it
---

# Skill Name

Instructions for Claude...
```

**Resources:**
- [Claude Code Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills)
- [Skill Creation Best Practices](https://docs.claude.com/en/docs/claude-code/skills#best-practices)
- Study existing skills in this repo for patterns

---

## Contributing

Contributions welcome! To add a new skill:

1. Fork this repository
2. Create a new skill directory following the structure above
3. Include comprehensive SKILL.md with clear trigger phrases
4. Add worked examples in references/
5. Create versioned release in dist/
6. Update this README with the new skill
7. Submit a pull request

For issues or feature requests, please open an issue.

---

## Roadmap

Potential skills for future development:

- **Strategic Mapping**: Wardley mapping and doctrine analysis
- **Decision Analysis**: Multi-criteria decision frameworks
- **Code Architecture**: System design pattern recognition
- **Project Planning**: OODA loop and agile methodologies
- **Data Analysis**: Statistical analysis and visualization workflows

---

## Resources

### Documentation
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- [Claude Web Chat](https://claude.ai)

### Community
- [Claude Code GitHub Issues](https://github.com/anthropics/claude-code/issues)
- [Skill Development Best Practices](https://docs.claude.com/en/docs/claude-code/skills#best-practices)

---

## License

MIT License - feel free to use, modify, and distribute.

Each skill may have its own license - check individual skill directories for details.

---

## Questions?

- **Skill Usage**: Check individual skill README files
- **Installation Issues**: See [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- **Bugs/Features**: Open an issue in this repository
- **General Claude Help**: Visit [claude.ai](https://claude.ai)

---

**Current Skills**: 5 | **Total Downloads**: 78KB | **Last Updated**: 2025-11-03

Built with Claude Code | [Learn More](https://docs.claude.com/en/docs/claude-code)
