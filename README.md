# AISkills

A curated collection of **28 professional skills** for Claude Code and Claude web chat. Skills extend Claude's capabilities for development, analysis, writing, and specialized workflows.

## What Are Claude Skills?

Skills are modular capabilities that Claude automatically discovers and uses based on context. Unlike slash commands requiring explicit invocation, skills seamlessly enhance Claude's responses when relevant.

## Skills Collection

### Development & Cloud (10 skills)

| Skill | Description | Platform |
|-------|-------------|----------|
| [MCP Builder](MCPBuilder/) | Build custom Model Context Protocol servers with 4-phase methodology | All |
| [AWS CDK](AWSSkills/aws-cdk-development/) | Infrastructure as Code with AWS CDK best practices | All |
| [AWS Serverless](AWSSkills/aws-serverless-eda/) | Serverless apps & event-driven architecture (7 design principles) | All |
| [AWS Cost & Ops](AWSSkills/aws-cost-operations/) | Cost optimization, monitoring, and observability | All |
| [Playwright](PlaywrightSkill/) | Model-invoked browser automation with smart helpers | 🖥️ Code |
| [Codex Peer Review](CodexPeerReview/) | AI peer review via OpenAI Codex CLI | 🖥️ Code |
| [Gemini Peer Review](GeminiPeerReview/) | AI peer review with 1M token context window | 🖥️ Code |
| [PR Review Loop](PRReviewLoop/) | Manage PR feedback cycles with Gemini/Claude fallback | 🖥️ Code |
| [Codebase Navigator](CodebaseNavigator/) | Semantic code search with osgrep integration | 🖥️ Code |
| [Artifacts Builder](ArtifactsBuilder/) | React artifacts with 43 shadcn/ui components | All |

### Writing & Content (5 skills)

| Skill | Description | Platform |
|-------|-------------|----------|
| [Prose Polish](ProsePolish/) | Writing analysis across 4 layers (lexical, structural, rhetorical, voice) | All |
| [Research-to-Essay](ResearchToEssay/) | 6-phase workflow for research-driven publication-grade writing | All |
| [Writing Partner](WritingPartner/) | Collaborative essay writing with interview, thread tracking, voice calibration | All |
| [Writing Skills](WritingSkills/) | META-SKILL: TDD methodology for documentation ("Iron Law") | All |
| [Claimify](Claimify/) | Transform discourse into structured argument maps | All |

### Analysis & Reasoning (5 skills)

| Skill | Description | Platform |
|-------|-------------|----------|
| [Concept Forge](ConceptForge/) | Dialectical concept development with 13 interrogation archetypes | All |
| [Process Mapper](ProcessMapper/) | Map workflows, extract SOPs, identify automation opportunities | All |
| [Excel Auditor](ExcelAuditor/) | Audit Excel files, analyze formulas, assess risk 🧪 | All |
| [Inevitability Engine](InevitabilityEngine/) | AI business opportunity discovery with inevitability scoring | All |
| [CSV Data Summarizer](CSVDataSummarizer/) | Proactive CSV analysis (exemplary "DO NOT ASK" design pattern) | All |

### AI & Automation (4 skills)

| Skill | Description | Platform |
|-------|-------------|----------|
| [NotebookLM](NotebookLMSkill/) | Source-grounded Q&A with browser automation | 🖥️ Code |
| [Agent Mail](AgentMail/) | Email automation and management for AI agents | All |
| [Nano Banana](NanoBananaSkill/) | AI image generation via Google Gemini 3 Pro | All |
| [Veo3 Prompter](Veo3Prompter/) | Craft cinematic prompts for Veo 3.1 video generation | All |

### Context & Workflow (3 skills)

| Skill | Description | Platform |
|-------|-------------|----------|
| [Context Continuity](ContextContinuity/) | High-fidelity context transfer between conversations | All |
| [Context Continuity Code](ContextContinuityCode/) | Dev-optimized context transfer for Claude Code | 🖥️ Code |
| [Claude Project Docs](ClaudeProjectDocs/) | Generate CLAUDE.md files with progressive disclosure | All |

### Fun (1 skill)

| Skill | Description | Platform |
|-------|-------------|----------|
| [Dad Joke Validator](DadJokeValidator/) | Rate and generate dad jokes with scientific precision | All |

**Legend:** 🖥️ Code = Claude Code only (requires terminal) | 🧪 = In testing

---

## Installation

### Claude Code

```bash
# Clone repository
git clone https://github.com/leegonzales/AISkills.git

# Install globally (all projects)
cp -r /path/to/AISkills/ProsePolish/prose-polish ~/.claude/skills/

# Or install per-project
cp -r /path/to/AISkills/ProsePolish/prose-polish your-project/.claude/skills/
```

### Claude Web Chat

1. Download `.skill` file from skill's `dist/` folder
2. Go to [claude.ai](https://claude.ai) → Settings → Capabilities
3. Click "Upload skill" and select the file

**Available packages:** [ProsePolish](ProsePolish/dist/), [MCPBuilder](MCPBuilder/dist/), [Playwright](PlaywrightSkill/dist/), [WritingSkills](WritingSkills/dist/), [ArtifactsBuilder](ArtifactsBuilder/dist/), and more in each skill's `dist/` folder.

---

## Repository Structure

```
AISkills/
├── README.md                    # This file
├── CLAUDE.md                    # Claude Code project context
├── SKILLS.md                    # Complete skill registry
├── agent_docs/                  # Progressive disclosure docs
│   ├── creating-skills.md       # How to create skills
│   ├── packaging.md             # Distribution workflow
│   └── quality.md               # Quality standards (85+ rubric)
├── docs/                        # Specifications & planning
│   ├── SKILL-8-SPEC.md          # Full skill format spec
│   └── skill-evaluation-rubric.md
├── SkillTemplate/               # Template + validation scripts
│   ├── skill-template/          # Blank template to copy
│   ├── example-skill/           # Complete working example
│   └── scripts/validate-skill.sh
├── SkillPackager/               # Packaging automation
│   └── scripts/
│       ├── package-skill.sh     # Single skill packager
│       └── batch-package.sh     # Package all skills
└── [SkillName]/                 # Each skill follows this pattern:
    ├── skill-slug/
    │   ├── SKILL.md             # Core definition (required)
    │   ├── README.md            # Human documentation
    │   ├── CHANGELOG.md         # Version history
    │   ├── references/          # Progressive disclosure content
    │   └── scripts/             # Helper scripts (if any)
    └── dist/                    # Packaged releases (.skill files)
```

---

## Creating Skills

```bash
# 1. Copy template
cp -r SkillTemplate/skill-template NewSkill/new-skill

# 2. Edit SKILL.md with your definition

# 3. Validate
./SkillTemplate/scripts/validate-skill.sh NewSkill/new-skill

# 4. Package for distribution
./SkillPackager/scripts/package-skill.sh NewSkill/new-skill
```

**The Iron Law (from Writing Skills META-SKILL):** NO SKILL WITHOUT A FAILING TEST FIRST

See [agent_docs/creating-skills.md](agent_docs/creating-skills.md) for full guide.

---

## Quality Standards

All skills follow these principles:

- **Concise Core** - Lean SKILL.md files optimized for context efficiency
- **Progressive Disclosure** - Essential in SKILL.md, details in references/
- **Appropriate Freedom** - Guidelines over rigid rules
- **Examples Over Explanation** - Worked examples showing real usage
- **Versioned Releases** - Semantic versioning for all packages

Minimum quality score: **85/100** on evaluation rubric. See [agent_docs/quality.md](agent_docs/quality.md).

---

## Infrastructure Tools

| Tool | Purpose |
|------|---------|
| **SkillTemplate** | Template with validation, reduces integration to ~1 hour |
| **SkillPackager** | Zero-manual-steps packaging with SHA256 checksums |
| **validate-skill.sh** | YAML, UTF-8, placeholder, JSON, Python syntax checks |
| **package-skill.sh** | Auto-version detection, validation, metadata generation |

---

## Testing Status

| Skill | Pass Rate | Quality | Status |
|-------|-----------|---------|--------|
| Codex Peer Review | 100% (7/7) | 4.8/5.0 | ✅ Production |
| Gemini Peer Review | 87.5% (7/8) | 5.0/5.0 | ✅ Production |
| Dad Joke Validator | 100% (11/11) | — | ✅ Production |

---

## Contributing

1. Fork repository
2. Use SkillTemplate as starting point
3. Follow Writing Skills methodology (test first)
4. Include comprehensive SKILL.md with clear triggers
5. Add examples in references/
6. Create versioned release in dist/
7. Submit pull request

---

## Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

---

## License

MIT License. Individual skills may have their own licenses - check skill directories.

---

**27 skills** | **MIT License** | **Last Updated:** 2025-12-17

Built with Claude Code | [Learn More](https://docs.claude.com/en/docs/claude-code)
