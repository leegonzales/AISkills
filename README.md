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

**[View Claimify →](Claimify/)**

---

### 6. Codex Peer Review (v1.0.0) 🖥️ **Claude Code Only**

Leverage OpenAI's Codex CLI for AI peer review and second opinions on architecture, design decisions, and implementations. Get multi-perspective analysis for high-stakes technical decisions.

**⚠️ Requires Claude Code** - This skill needs terminal access to execute Codex CLI commands. Not available for Claude web chat.

**Features:**
- Architecture validation and critique
- Design decision cross-validation from two AI perspectives
- Security review with complementary vulnerability analysis
- Performance optimization with multi-perspective bottleneck identification
- Testing strategy validation
- Alternative approach generation through collaborative AI reasoning

**Use for:**
- Architecture review before major implementation
- Second opinions on critical design decisions
- Security review of authentication/authorization code
- Performance analysis and optimization recommendations
- Testing strategy and coverage gap identification
- Learning from complex code with multi-perspective explanations

**Testing & Quality:**
- ✅ 100% pass rate (7/7 tests)
- ✅ 4.8/5.0 average quality score
- ✅ Production ready - comprehensive testing completed
- 📊 [View detailed test results](CodexPeerReview/TESTING.md)

**Prerequisites:**
- Claude Code environment (requires terminal access)
- [Codex CLI](https://developers.openai.com/codex/cli/) installed locally

**[View Codex Peer Review →](CodexPeerReview/)**

---

### 7. Gemini Peer Review (v1.0.0) 🖥️ **Claude Code Only**

Leverage Google's Gemini API for AI peer review with massive context windows and multimodal capabilities. Get complementary perspectives from Claude + Gemini on architecture, design, and implementation decisions.

**⚠️ Requires Claude Code** - This skill needs terminal access to invoke the Gemini API programmatically. Not available for Claude web chat.

**Features:**
- Architecture validation with 1M token context window (entire codebases)
- Design decision analysis from dual AI perspectives
- Security review with threat modeling and vulnerability identification
- Performance optimization with bottleneck detection
- Testing strategy validation and coverage gap analysis
- Multimodal technical review (diagrams, PDFs, designs)
- Large codebase analysis (60k+ lines in single context)
- Google Search grounding for current best practices

**Use for:**
- Architecture review with full codebase context
- Second opinions on critical technical decisions
- Security audits with comprehensive threat analysis
- Performance analysis across large systems
- Testing strategy development
- Multimodal technical review (diagram to code)
- Learning from complex codebases with AI collaboration

**Testing & Quality:**
- ✅ 87.5% pass rate (7/8 tests, 1 test setup issue)
- ✅ 5.0/5.0 average quality score (perfect on all executed tests)
- ✅ Production ready - comprehensive testing completed
- 🏆 Validated 9k LOC codebase in single context
- 📊 [View detailed test results](GeminiPeerReview/TESTING.md)

**Prerequisites:**
- Claude Code environment (requires terminal access)
- [Google Gemini API key](https://makersuite.google.com/app/apikey) (free tier available)
- Python 3.8+ with `google-generativeai` package

**[View Gemini Peer Review →](GeminiPeerReview/)**

---

### 8. Context Continuity (v1.0.0)

High-fidelity context transfer protocol for moving conversations between AI agents. Preserves decision tempo, open loops, and critical context with graceful degradation.

**Features:**
- Dual-mode operation: Minimal (~200 words) and Full (~1000 words) artifacts
- Auto-selects mode based on conversation complexity (user can override)
- Antifragile structure with critical information first (survives truncation)
- Decision log with taxonomy (explicit/implicit/emergent) prevents rehashing
- Handshake protocol for receiving agents to confirm understanding
- Evolution tags ([G/C/P/K] or simplified [New/Developing/Stable/Standard])
- Optional [T] tag for tool/environment state (Claude Code power users)
- Python validator for artifact quality checking

**Use for:**
- Continuing work in a fresh Claude conversation
- Switching between Claude instances while preserving context
- Working around context window limits
- Transferring complex strategic discussions to new agents
- Maintaining decision history across multiple sessions
- Cross-system handoffs (Claude to other LLMs)

**[View Context Continuity →](ContextContinuity/)**

---

### 9. Dad Joke Validator (v1.1.0)

Analyze and score jokes on the dad joke quality spectrum with scientific precision. Multi-dimensional feedback on pun quality, groan factor, wholesomeness, and structure. Can also generate dad jokes using template-based systems.

**Features:**
- 4-dimensional scoring system (Pun Quality, Groan Factor, Wholesomeness, Structure)
- Overall dad joke score (0-100 scale) with quality tiers
- Improvement suggestions for low-scoring jokes
- Template-based joke generation with automatic validation
- Batch generation with quality filtering
- CLI tools for validation and generation
- Asset databases for puns, homophones, and wholesome themes
- Comprehensive test suite (11 tests, all passing)

**Use for:**
- Validate if a joke is truly "dad joke material"
- Get detailed feedback on why jokes succeed or fail
- Generate dad jokes using 8 different templates
- Learn what makes effective wordplay and puns
- Quality-filter joke collections (only keep 85+ scores)
- Iterative joke writing with scoring feedback
- Understanding dad joke psychology and structure

**Technical Features:**
- Homophone detection (two/too, tuna/tune a, bear/bare, etc.)
- Double-meaning word analysis (light, cool, sharp, bright, etc.)
- Pun pattern matching (grew on me, make up, outstanding in field)
- Wholesome content validation with red flag detection
- Over-explanation penalties for joke clarity
- Template-based generation with best-of-N selection

**Testing & Quality:**
- ✅ 100% pass rate (11/11 tests)
- ✅ Gemini peer review completed - all recommendations implemented (v1.0.1)
- ✅ Production ready - comprehensive heuristic-based scoring

**[View Dad Joke Validator →](DadJokeValidator/)**

---

### 10. Context Continuity - Claude Code Edition (v1.0.0) 🖥️ **Claude Code Only**

Claude Code-optimized context transfer for development workflows. Preserves code context, git state, and running services when moving work between Claude Code sessions.

**⚠️ Requires Claude Code** - This skill needs terminal access for git commands and environment inspection. Not available for Claude web chat.

**Features:**
- Single development-optimized mode (~400-600 words)
- § Code Context - Active files, functions modified, code state
- § Git State - Branch, commits, staged/unstaged changes, merge status
- § Environment State - Running services, ports, dependencies, env vars
- § Technical Decisions - Design choices with peer review integration
- § Open Loops - Next actions, blockers, pending tests
- § Testing & Validation - Test status, coverage, manual testing
- Git-aware: Automatically captures `git status` and `git diff` output
- Peer review integration: Captures Codex/Gemini recommendations inline

**Use for:**
- Continuing development work in fresh Claude Code session
- Resuming after context window fills (180K+ tokens)
- Handing off work to another developer (with AI context preserved)
- Documenting state before major refactoring
- Post-peer-review implementation tracking
- Bug fix investigations in progress

**Peer Review Integration Example:**
```markdown
§ TECHNICAL DECISIONS
**Peer Review Integration**:
- Codex consulted: Yes - Recommended Redis, flagged memory limits
- Gemini consulted: Yes - Suggested Redis Cluster for scaling
- Agreements: Both validated Redis for performance needs
- Disagreements: Memory limits (1GB vs 2GB) - chose 1.5GB
```

**Difference from Base Context Continuity:**
| Feature | Base Skill | Code Edition |
|---------|-----------|--------------|
| Target | General conversations | Development only |
| Tool State | Optional [T] tags | Mandatory §§ sections |
| Git Context | Not included | Required |
| Peer Review | Not mentioned | Integrated workflow |

**Prerequisites:**
- Claude Code environment (requires terminal access)
- Git repository (skill runs git commands)

**[View Context Continuity - Code Edition →](ContextContinuityCode/)**

---

## Installation

### For Claude Code

Skills are automatically discovered from your skills directories. Install system-wide or per-project.

#### Option 1: Clone Entire Repository (Recommended)

```bash
# Clone the repository
git clone https://github.com/leegonzales/AISkills.git

# Install globally (available in all projects)
cd ~/.claude/skills/
cp -r /path/to/AISkills/ProsePolish/prose-polish ./
cp -r /path/to/AISkills/ResearchToEssay/research-to-essay ./
cp -r /path/to/AISkills/ConceptForge/concept-forge ./
cp -r /path/to/AISkills/ProcessMapper/process-mapper ./
cp -r /path/to/AISkills/Claimify/claimify ./
cp -r /path/to/AISkills/CodexPeerReview/codex-peer-review ./
cp -r /path/to/AISkills/GeminiPeerReview/gemini-peer-review ./
cp -r /path/to/AISkills/ContextContinuity/context-continuity ./
cp -r /path/to/AISkills/ContextContinuityCode/context-continuity-code ./
cp -r /path/to/AISkills/DadJokeValidator/dad-joke-validator ./

# Or install for specific project only
cd your-project/.claude/skills/
cp -r /path/to/AISkills/ProsePolish/prose-polish ./
# ... add other skills as needed
```

#### Option 2: Download Individual Skills via GitHub

```bash
# Navigate to your skills directory
cd ~/.claude/skills/  # for global install
# or
cd your-project/.claude/skills/  # for project-specific install

# Download individual skills using curl
# Example: Prose Polish
curl -L https://github.com/leegonzales/AISkills/archive/refs/heads/main.tar.gz | \
  tar xz --strip=2 AISkills-main/ProsePolish/prose-polish

# Example: Codex Peer Review
curl -L https://github.com/leegonzales/AISkills/archive/refs/heads/main.tar.gz | \
  tar xz --strip=2 AISkills-main/CodexPeerReview/codex-peer-review

# Example: Gemini Peer Review (requires CLI setup - see skill docs)
curl -L https://github.com/leegonzales/AISkills/archive/refs/heads/main.tar.gz | \
  tar xz --strip=2 AISkills-main/GeminiPeerReview/gemini-peer-review
```

**Documentation:** [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)

---

### For Claude Web Chat

Each skill includes a versioned `.skill` file (ZIP format) in its `dist/` folder.

#### Download .skill Files

**Option 1: Direct GitHub Download**

Click to download from GitHub:
- **Prose Polish v1.1.0**: [Download](https://github.com/leegonzales/AISkills/raw/main/ProsePolish/dist/prose-polish-v1.1.0.skill)
- **Research-to-Essay v1.0.0**: [Download](https://github.com/leegonzales/AISkills/raw/main/ResearchToEssay/dist/research-to-essay-v1.0.0.skill)
- **Concept Forge v1.0.0**: [Download](https://github.com/leegonzales/AISkills/raw/main/ConceptForge/dist/concept-forge-v1.0.0.skill)
- **Process Mapper v1.0.0**: [Download](https://github.com/leegonzales/AISkills/raw/main/ProcessMapper/dist/process-mapper-v1.0.0.skill)
- **Claimify v1.0.0**: [Download](https://github.com/leegonzales/AISkills/raw/main/Claimify/dist/claimify-v1.0.0.skill)
- **Context Continuity v1.0.0**: [Download](https://github.com/leegonzales/AISkills/raw/main/ContextContinuity/dist/context-continuity-v1.0.0.skill)
- **Dad Joke Validator v1.1.0**: [Download](https://github.com/leegonzales/AISkills/raw/main/DadJokeValidator/dist/dad-joke-validator-v1.1.0.skill)

**Option 2: Download via curl**

```bash
# Download to current directory
curl -LO https://github.com/leegonzales/AISkills/raw/main/ProsePolish/dist/prose-polish-v1.1.0.skill
curl -LO https://github.com/leegonzales/AISkills/raw/main/ResearchToEssay/dist/research-to-essay-v1.0.0.skill
curl -LO https://github.com/leegonzales/AISkills/raw/main/ConceptForge/dist/concept-forge-v1.0.0.skill
curl -LO https://github.com/leegonzales/AISkills/raw/main/ProcessMapper/dist/process-mapper-v1.0.0.skill
curl -LO https://github.com/leegonzales/AISkills/raw/main/Claimify/dist/claimify-v1.0.0.skill
curl -LO https://github.com/leegonzales/AISkills/raw/main/ContextContinuity/dist/context-continuity-v1.0.0.skill
curl -LO https://github.com/leegonzales/AISkills/raw/main/DadJokeValidator/dist/dad-joke-validator-v1.1.0.skill
```

**Note:** Codex and Gemini Peer Review skills are Claude Code only (require terminal access) - not available for web chat.

#### Method 1: Install Globally (Recommended)

Install skills to make them available across all your conversations:

1. Go to [claude.ai](https://claude.ai)
2. Navigate to **Settings > Capabilities**
3. Ensure "Code execution and file creation" is enabled
4. Click **"Upload skill"** in the Skills section
5. Select the downloaded `.skill` file (ZIP)
6. Toggle the skill on/off as needed

**Benefits:** Skill persists across all conversations, automatically invoked when relevant.

#### Method 2: Upload Per-Conversation

Upload skills to individual conversations for temporary use:

1. Go to [claude.ai](https://claude.ai)
2. Start a new conversation or open an existing one
3. Click the attachment button (📎)
4. Upload the `.skill` file
5. The skill will be available for that conversation only

**Use when:** Testing skills or temporary one-off usage.

**Documentation:** [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

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

**Codex Peer Review:**
```
"Get a second opinion on this architecture"
"Review this code with Codex for security issues"
"What would Codex think about this design decision?"
```

**Gemini Peer Review:**
```
"Get Gemini's perspective on this architecture"
"Review this entire codebase for security vulnerabilities"
"Analyze this diagram and code together for inconsistencies"
"What would Gemini recommend for this performance issue?"
```

**Context Continuity:**
```
"Transfer this conversation to another chat"
"Create a handoff artifact for continuing this work"
"I need to continue this in a fresh conversation"
"Prepare a context transfer for another agent"
```

**Dad Joke Validator:**
```
"Is this a dad joke? 'Why did the bicycle fall over?'"
"Score this joke on dad joke quality"
"Generate 5 dad jokes about programming"
"Help me write a better dad joke about food"
"Validate my joke collection and keep only the best ones"
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
├── Claimify/                           # Argument structure analysis
│   ├── dist/
│   │   └── claimify-v1.0.0.skill
│   ├── claimify/                       # Source skill
│   └── README.md
├── CodexPeerReview/                    # AI peer review with Codex (Claude Code only)
│   ├── codex-peer-review/              # Source skill
│   └── README.md
├── GeminiPeerReview/                   # AI peer review with Gemini (Claude Code only)
│   ├── gemini-peer-review/             # Source skill
│   └── README.md
├── ContextContinuity/                  # High-fidelity context transfer
│   ├── dist/
│   │   └── context-continuity-v1.0.0.skill
│   ├── context-continuity/             # Source skill
│   ├── Context Continuity Guide.md
│   ├── Context Continuity Analysis.md
│   └── README.md
└── DadJokeValidator/                   # Dad joke analysis and generation
    ├── dist/
    │   └── dad-joke-validator-v1.1.0.skill
    ├── dad-joke-validator/             # Source skill
    ├── CHANGELOG.md
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
| Codex Peer Review | v1.0.0 | 2025-11-12 | Initial release - AI peer review with Codex CLI |
| Gemini Peer Review | v1.0.0 | 2025-01-12 | Initial release - AI peer review with Gemini API, 1M context |
| Context Continuity | v1.0.0 | 2025-11-16 | Initial release - High-fidelity context transfer protocol |
| Context Continuity - Code Edition | v1.0.0 | 2025-11-16 | Claude Code-optimized dev context transfer with peer review integration |
| Dad Joke Validator | v1.1.0 | 2025-11-16 | Template-based generation, Gemini peer review improvements |

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

## Testing & Quality Assurance

Both Codex and Gemini Peer Review skills have been validated for production readiness through comprehensive testing.

| Skill | Pass Rate | Avg Quality | Status |
|-------|-----------|-------------|--------|
| **Codex Peer Review** | 100% (7/7) | 4.8/5.0 | ✅ Production Ready |
| **Gemini Peer Review** | 87.5% (7/8) | 5.0/5.0 | ✅ Production Ready |

**For complete testing documentation, methodology, and detailed results:**
- [CodexPeerReview/TESTING.md](CodexPeerReview/TESTING.md) - Codex testing results and capabilities
- [GeminiPeerReview/TESTING.md](GeminiPeerReview/TESTING.md) - Gemini testing results and capabilities

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

**Current Skills**: 10 | **Total Downloads**: 191KB | **Last Updated**: 2025-11-16

Built with Claude Code | [Learn More](https://docs.claude.com/en/docs/claude-code)
