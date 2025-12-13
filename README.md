# AI Skills Collection

[![Run in Smithery](https://smithery.ai/badge/skills/leegonzales)](https://smithery.ai/skills?ns=leegonzales&utm_source=github&utm_medium=badge)


A curated collection of professional skills for Claude Code and Claude web chat, designed for enhanced development, analysis, writing, and reasoning workflows.

## What Are Claude Skills?

Skills are modular, model-invoked capabilities that extend Claude's functionality. Unlike slash commands that require explicit invocation, skills are **automatically discovered and used by Claude based on context**, enabling complex workflows with seamless discovery.

This collection includes skills for:
- **Development & Cloud**: AWS infrastructure, MCP tools, browser automation, artifact creation
- **Writing & Meta-Skills**: Professional writing, research synthesis, TDD for documentation
- **Analysis & Reasoning**: Argument mapping, concept development, process documentation, data analysis
- **AI Collaboration**: Peer review with Gemini and Codex, source-grounded Q&A
- **Workflow Enhancement**: Context transfer, dad jokes (because why not?)

Many skills work in both Claude Code and Claude web chat, providing flexible capabilities wherever you interact with Claude.

---

## Skills in This Collection

### Development & Cloud Infrastructure

#### 11. MCP Builder (v1.0.0)

Build custom Model Context Protocol (MCP) servers to create specialized Claude tools. 4-phase methodology for designing LLM-optimized interfaces.

**Features:**
- Research & Planning phase with capability mapping
- Dual language support (Python FastMCP + TypeScript MCP SDK)
- Implementation guidance with agent-centric design principles
- Review & Refine with functionality and UX validation
- Complete evaluations framework for quality assurance
- Integration examples with existing MCP servers

**Use for:**
- Create custom Claude tools for specific APIs or services
- Design LLM-optimized interfaces for databases or SaaS platforms
- Build specialized development workflows
- Integrate external tools into Claude conversations
- Extend Claude's capabilities with domain-specific tools

**[View MCP Builder →](MCPBuilder/)**

---

#### 12. AWS Skills (v1.0.0) - Triple Pack

Three comprehensive skills for AWS development: CDK, Serverless, and Cost & Operations. Integrates with 15+ AWS MCP servers.

##### AWS CDK Development

Infrastructure as Code with AWS Cloud Development Kit and best practices.

**Features:**
- Resource naming best practices (reusable stacks without explicit names)
- Lambda function development with automatic bundling
- Multi-layer validation (cdk-nag + synthesis + pre-commit hooks)
- Pre-deployment validation scripts
- Comprehensive CDK patterns reference
- Integration with AWS Documentation MCP and AWS CDK MCP

**Use for:**
- Build cloud infrastructure with TypeScript/Python
- Create reusable CDK constructs and patterns
- Validate infrastructure before deployment
- Follow AWS Well-Architected Framework

##### AWS Serverless & Event-Driven Architecture

Build scalable serverless applications based on AWS Well-Architected Framework.

**Features:**
- 7 Well-Architected serverless design principles
- 5 event-driven architecture patterns (EventBridge, SQS, SNS, Saga, Event Sourcing)
- 5 serverless patterns (API microservices, stream processing, scheduled jobs, webhooks, async tasks)
- Complete lifecycle management with SAM
- 6 comprehensive reference files (300+ pages of patterns)
- Integration with 5 AWS MCP servers (Serverless, Lambda, Step Functions, SNS, SQS)

**Use for:**
- Design event-driven microservices architectures
- Build serverless APIs and data pipelines
- Implement saga patterns for distributed transactions
- Create scalable async processing workflows

##### AWS Cost & Operations

Cost optimization, monitoring, observability, and operational excellence.

**Features:**
- Pre-deployment cost estimation workflows
- Real-time billing and budget monitoring
- CloudWatch metrics, logs, and alarms configuration
- Application performance monitoring (APM)
- Container monitoring with Prometheus
- CloudTrail security auditing
- Well-Architected security assessment

**Use for:**
- Estimate costs before deploying infrastructure
- Monitor and optimize AWS spending
- Set up comprehensive observability
- Security auditing and compliance
- Performance monitoring and optimization

**Integration:** 15+ AWS MCP servers documented across all three skills

**[View AWS Skills →](AWSSkills/)**

---

#### 13. Playwright Browser Automation (v1.0.0) 🖥️ **Claude Code Only**

Model-invoked browser automation with Playwright. Claude writes custom code for each unique request.

**⚠️ Requires Claude Code** - Needs Node.js execution environment.

**Features:**
- Universal executor (run.js) with proper module resolution
- Smart helpers (auto-detect dev servers, safe clicks with retry, cookie banner handling)
- CI/CD integration (GitHub Actions, GitLab CI)
- Performance testing patterns (Core Web Vitals measurement)
- Screenshot and video capture
- Multi-browser support (Chromium, Firefox, WebKit)
- Headless and headed modes

**Use for:**
- End-to-end testing automation
- Web scraping and data extraction
- Form automation and submissions
- Performance testing and monitoring
- Visual regression testing
- CI/CD integration for automated testing

**[View Playwright →](PlaywrightSkill/)**

---

#### 14. Artifacts Builder (v1.0.0)

Create sophisticated React artifacts for claude.ai using modern frontend stack (React 18 + TypeScript + Tailwind + shadcn/ui).

**Features:**
- Project initialization with Vite + React 18 + TypeScript
- 43 pre-installed shadcn/ui components
- Tailwind CSS 3.4.1 with complete theming system
- Single-file bundling (Parcel + html-inline)
- Anti-"AI slop" design guidelines (no purple gradients, avoid generic aesthetics)
- Professional component library built on Radix UI primitives

**Components Categories:**
- Layout & Structure (5): card, separator, aspect-ratio, resizable, scroll-area
- Navigation (4): navigation-menu, breadcrumb, menubar, tabs
- Forms & Inputs (10): form, input, textarea, select, checkbox, radio-group, switch, slider, calendar, command
- Feedback & Status (6): alert, toast, toaster, sonner, progress, skeleton, badge
- Overlays & Dialogs (8): dialog, sheet, drawer, popover, tooltip, hover-card, context-menu, dropdown-menu
- Data Display (5): table, accordion, collapsible, carousel, avatar
- Interactive Elements (3): button, toggle, toggle-group
- Plus utilities: cn(), useToast, and more

**Example Artifacts:**
- Interactive dashboards with filtering
- Multi-step forms with validation
- Task management apps (Kanban-style)
- Data explorers with advanced filtering
- Interactive games and educational tools

**Use for:**
- Build interactive dashboards for claude.ai
- Create complex multi-component applications
- Develop form wizards and data entry interfaces
- Build games, puzzles, and educational tools
- Professional-looking UI components with Tailwind + shadcn/ui

**[View Artifacts Builder →](ArtifactsBuilder/)**

---

### Writing & Meta-Skills

#### 1. Prose Polish (v1.1.0)

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

#### 2. Research-to-Essay (v1.0.0)

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

#### 15. Writing Skills (v1.0.0) **[META-SKILL]**

Test-Driven Development applied to process documentation. The "Iron Law" methodology for creating bulletproof skills.

**Features:**
- Iron Law: "NO SKILL WITHOUT A FAILING TEST FIRST"
- RED-GREEN-REFACTOR workflow for documentation
- Persuasion principles (Authority, Commitment, Social Proof)
- Research-backed: 33% → 72% compliance improvement (Meincke et al. 2025, N=28,000)
- Claude Search Optimization (CSO) guidelines
- Token efficiency principles
- Progressive disclosure patterns
- Loophole closing framework

**Includes:**
- anthropic-best-practices.md (45KB) - Official Anthropic skill authoring guidelines
- persuasion-principles.md (6KB) - Research-backed psychology for LLM compliance
- graphviz-conventions.dot (6KB) - Visual documentation standards

**Use for:**
- Creating new skills with evidence-based approach
- Improving existing skills systematically
- Understanding what makes skills work
- Applying persuasion principles to documentation
- Building bulletproof, loophole-closed instructions

**This is a META-SKILL** - It improves how all other skills are created and refined.

**[View Writing Skills →](WritingSkills/)**

---

### Analysis & Reasoning

#### 3. Concept Forge (v1.0.0)

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

#### 4. Process Mapper (v1.0.0)

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

#### 5. Claimify (v1.0.0)

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

### Data & Analysis

#### 18. Excel Auditor (v1.0.0) 🧪 **IN TESTING**

Analyze unknown or inherited Excel files to understand what they do, document their purpose, audit formulas for errors, and assess maintainability risk.

**🧪 Status: In Testing** - Core functionality complete, validation in progress.

**Features:**
- Structure extraction (sheets, named ranges, tables, VBA detection, external links)
- Formula analysis with function categorization and complexity metrics
- Error detection (7 Excel error types: #REF!, #DIV/0!, #VALUE!, etc.)
- Volatile function identification (NOW, TODAY, RAND, INDIRECT, OFFSET)
- Purpose inference from formula patterns (financial, lookup, aggregation, scheduling)
- Pattern recognition for common archetypes (DCF, Budget, P&L, Inventory, CRM)
- Risk flags (VBA macros, hidden sheets, external links, merged cells)
- Comprehensive audit report generation

**Use for:**
- Understanding inherited/legacy spreadsheets ("what does this do?")
- Formula auditing and error detection
- Spreadsheet risk and complexity assessment
- Documentation generation for undocumented Excel files
- Identifying maintainability concerns before taking ownership

**Prerequisites:**
- Python 3.8+ with `openpyxl` package

**[View Excel Auditor →](ExcelAuditor/)**

---

#### 19. Inevitability Engine (v1.0.0)

Systematic research protocol for discovering AI-native business opportunities. Maps capability trajectories, analyzes segment-problem spaces, and calculates inevitability scores across 3-24 month horizons.

**Features:**
- 6-phase discovery workflow (Capability Mapping → Synthesis)
- Capability frontier mapping with time horizon projections
- Segment-problem matrix analysis (50-100+ pain points)
- 10 synthetic worker primitives for business model generation
- Inevitability scoring formula with threshold analysis
- 7 comprehensive reference files (4,700+ lines of methodology)

**Use for:**
- AI business opportunity discovery
- Market research for AI-native ventures
- Capability trajectory analysis
- Synthetic workforce opportunity mapping
- Investment thesis development

**[View Inevitability Engine →](InevitabilityEngine/)**

---

#### 20. Agent Mail (v1.0.0)

Email automation and management for AI agents. Structured email handling with templates and workflow integration.

**[View Agent Mail →](AgentMail/)**

---

#### 21. Codebase Navigator (v1.0.0)

Semantic code search with osgrep integration. Find code patterns, understand architecture, and navigate large codebases efficiently.

**[View Codebase Navigator →](CodebaseNavigator/)**

---

#### 22. Claude Project Docs (v1.0.0)

Generate concise CLAUDE.md files following progressive disclosure best practices. Create well-crafted project documentation (~60 lines) with agent_docs/ structure.

**Features:**
- 60-line rule for CLAUDE.md (universal, every session)
- Progressive disclosure with agent_docs/
- WHAT/WHY/HOW structure
- Anti-pattern detection and prevention
- Template library and examples

**Use for:**
- Set up Claude for new projects
- Audit existing CLAUDE.md files
- Create agent documentation structure
- Optimize context efficiency

**[View Claude Project Docs →](ClaudeProjectDocs/)**

---

#### 23. Nano Banana (v1.0.0)

AI image generation via Google's Gemini 3 Pro Image model through MCP. Generate and edit high-quality images with text rendering capabilities.

**Features:**
- Text-to-image generation
- Image editing and modification
- High-quality text rendering in images
- MCP server integration

**Use for:**
- Generate images for content
- Edit and modify existing images
- Create graphics with text overlays
- Visual content generation

**[View Nano Banana →](NanoBananaSkill/)**

---

#### 16. CSV Data Summarizer (v1.0.0) **[DESIGN REFERENCE]**

Proactive CSV analysis without user prompting. Exemplary "DO NOT ASK" design pattern for autonomous agent behavior.

**Features:**
- Immediate, comprehensive analysis (no "What would you like?" friction)
- Intelligent adaptation to data types (sales, financial, customer, survey, operational)
- Complete statistical summaries with visualizations
- Smart visualization selection (3-5 charts based on actual data structure)
- Quality checks and data validation
- Python-based with pandas, matplotlib, seaborn

**Design Pattern Value:**
- 3,193-word extracted design principles document
- Reusable template for proactive skills
- Language patterns that eliminate decision paralysis
- Connected to persuasion research (Commitment, Authority, Social Proof)
- Referenced in Writing Skills as exemplary implementation

**Use for:**
- Instant CSV file analysis and insights
- Data exploration without manual prompting
- Automated reporting and visualization
- Quality checking datasets
- Learning proactive skill design patterns

**This skill serves dual purpose:** Functional data analysis + Design reference for future skill development

**[View CSV Data Summarizer →](CSVDataSummarizer/)**

---

### AI Collaboration & Peer Review

#### 6. Codex Peer Review (v1.0.0) 🖥️ **Claude Code Only**

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

#### 7. Gemini Peer Review (v1.0.0) 🖥️ **Claude Code Only**

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

#### 17. NotebookLM (v1.0.0) 🖥️ **Claude Code Only**

Source-grounded Q&A with Google NotebookLM. Get answers exclusively from uploaded documents with mandatory citations, drastically reducing hallucination.

**⚠️ Requires Claude Code** - Needs terminal access for browser automation.

**Features:**
- Source-grounded answers with citations (minimal hallucination)
- Patchright browser automation (enhanced Playwright fork)
- Hybrid authentication (browser profile + manual cookie injection)
- Gemini 2.5 synthesis of answers from up to 50 documents
- Human-like stealth automation (320-480 WPM typing, curved mouse movements)
- Comprehensive 4-tier maintenance documentation

**Maintenance Approach:**
- Complete UI change monitoring strategy
- Step-by-step selector update guide
- Version compatibility tracking
- Community coordination workflow
- Expected and normal for browser automation

**Use for:**
- Get citation-backed answers from documentation
- Research with source grounding requirements
- Query technical documentation with precision
- Avoid hallucination on critical information
- Multi-source document synthesis

**Known Trade-offs:**
- Requires occasional maintenance (UI changes)
- 3-5 second overhead per query (browser launch)
- Manual document upload required
- Rate limited (50 queries/day free tier)

**[View NotebookLM →](NotebookLMSkill/)**

---

### Context & Workflow

#### 8. Context Continuity (v1.0.0)

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

#### 9. Context Continuity - Claude Code Edition (v1.0.0) 🖥️ **Claude Code Only**

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

**[View Context Continuity - Code Edition →](ContextContinuityCode/)**

---

### Fun & Quirky

#### 10. Dad Joke Validator (v1.1.0)

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

**Testing & Quality:**
- ✅ 100% pass rate (11/11 tests)
- ✅ Gemini peer review completed - all recommendations implemented (v1.0.1)
- ✅ Production ready - comprehensive heuristic-based scoring

**[View Dad Joke Validator →](DadJokeValidator/)**

---

## Infrastructure & Development Tools

### SkillTemplate (v1.0.0)

Complete skill template with validation, integration runbook, and customization guide. Reduces integration time from 10-20 hours to ~1 hour per skill.

**Includes:**
- Skill template with all file types (SKILL.md, README.md, CHANGELOG.md, LICENSE, references/, scripts/, assets/)
- validate-skill.sh - Automated validation (YAML, UTF-8, placeholders, JSON, Python syntax)
- 8-phase integration runbook (Preparation → Post-Integration)
- Example skill (Text Statistics) demonstrating pattern
- Customization guide for 4 skill types (Analysis, Generation, Workflow, Integration)
- Testing protocol and quality checklists

**[View SkillTemplate →](SkillTemplate/)**

---

### SkillPackager (v1.0.0)

Zero-manual-steps packaging automation for .skill files with validation and checksums.

**Includes:**
- package-skill.sh - Auto-detects version, validates, packages, generates SHA256 + metadata
- batch-package.sh - Package multiple skills in one command
- test-skill-installation.sh - Verify packages install correctly

**Features:**
- Automatic version detection from CHANGELOG.md
- Pre-package validation (calls validate-skill.sh)
- Smart exclusions (*.pyc, __pycache__, .DS_Store, .git, .pytest_cache, dist/)
- SHA256 checksum generation
- Metadata JSON creation
- Post-package verification

**[View SkillPackager →](SkillPackager/)**

---

## Installation

### For Claude Code

Skills are automatically discovered from your skills directories. Install system-wide or per-project.

#### Clone Repository (Recommended)

```bash
# Clone the repository
git clone https://github.com/leegonzales/AISkills.git

# Install globally (available in all projects)
cd ~/.claude/skills/
cp -r /path/to/AISkills/ProsePolish/prose-polish ./
cp -r /path/to/AISkills/MCPBuilder/mcp-builder ./
cp -r /path/to/AISkills/WritingSkills/writing-skills ./
cp -r /path/to/AISkills/PlaywrightSkill/playwright ./
cp -r /path/to/AISkills/ArtifactsBuilder/artifacts-builder ./
cp -r /path/to/AISkills/NotebookLMSkill/notebooklm ./
cp -r /path/to/AISkills/CSVDataSummarizer/csv-data-summarizer ./
# ... add other skills as needed

# Or install for specific project only
cd your-project/.claude/skills/
cp -r /path/to/AISkills/[SkillCollection]/[skill-name] ./
```

#### AWS Skills Installation

```bash
# AWS skills are in one collection, copy all three
cd ~/.claude/skills/
cp -r /path/to/AISkills/AWSSkills/aws-cdk-development ./
cp -r /path/to/AISkills/AWSSkills/aws-serverless-eda ./
cp -r /path/to/AISkills/AWSSkills/aws-cost-operations ./
```

**Documentation:** [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)

---

### For Claude Web Chat

Each skill includes a versioned `.skill` file (ZIP format) in its `dist/` folder.

#### Download .skill Files

**Direct GitHub Downloads:**
- [Prose Polish v1.1.0](https://github.com/leegonzales/AISkills/raw/main/ProsePolish/dist/prose-polish-v1.1.0.skill)
- [MCP Builder v1.0.0](https://github.com/leegonzales/AISkills/raw/main/MCPBuilder/dist/mcp-builder-v1.0.0.skill)
- [Playwright v1.0.0](https://github.com/leegonzales/AISkills/raw/main/PlaywrightSkill/dist/playwright-v1.0.0.skill)
- [Writing Skills v1.0.0](https://github.com/leegonzales/AISkills/raw/main/WritingSkills/dist/writing-skills-v1.0.0.skill)
- [AWS CDK v1.0.0](https://github.com/leegonzales/AISkills/raw/main/AWSSkills/dist/aws-cdk-development-v1.0.0.skill)
- [AWS Serverless v1.0.0](https://github.com/leegonzales/AISkills/raw/main/AWSSkills/dist/aws-serverless-eda-v1.0.0.skill)
- [AWS Cost & Ops v1.0.0](https://github.com/leegonzales/AISkills/raw/main/AWSSkills/dist/aws-cost-operations-v1.0.0.skill)
- [Artifacts Builder v1.0.0](https://github.com/leegonzales/AISkills/raw/main/ArtifactsBuilder/dist/artifacts-builder-v1.0.0.skill)
- [NotebookLM v1.0.0](https://github.com/leegonzales/AISkills/raw/main/NotebookLMSkill/dist/notebooklm-v1.0.0.skill)
- [CSV Data Summarizer v1.0.0](https://github.com/leegonzales/AISkills/raw/main/CSVDataSummarizer/dist/csv-data-summarizer-v1.0.0.skill)
- [Research-to-Essay v1.0.0](https://github.com/leegonzales/AISkills/raw/main/ResearchToEssay/dist/research-to-essay-v1.0.0.skill)
- [Concept Forge v1.0.0](https://github.com/leegonzales/AISkills/raw/main/ConceptForge/dist/concept-forge-v1.0.0.skill)
- [Process Mapper v1.0.0](https://github.com/leegonzales/AISkills/raw/main/ProcessMapper/dist/process-mapper-v1.0.0.skill)
- [Claimify v1.0.0](https://github.com/leegonzales/AISkills/raw/main/Claimify/dist/claimify-v1.0.0.skill)
- [Context Continuity v1.0.0](https://github.com/leegonzales/AISkills/raw/main/ContextContinuity/dist/context-continuity-v1.0.0.skill)
- [Dad Joke Validator v1.1.0](https://github.com/leegonzales/AISkills/raw/main/DadJokeValidator/dist/dad-joke-validator-v1.1.0.skill)

**Note:** Skills marked 🖥️ **Claude Code Only** require terminal access and are not available for web chat.

#### Installation Method

1. Go to [claude.ai](https://claude.ai)
2. Navigate to **Settings > Capabilities**
3. Ensure "Code execution and file creation" is enabled
4. Click **"Upload skill"** in the Skills section
5. Select the downloaded `.skill` file (ZIP)
6. Toggle the skill on/off as needed

**Documentation:** [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

---

## Repository Structure

```
AISkills/
├── README.md                           # This file
├── CLAUDE.md                           # Claude Code context (~55 lines)
├── GEMINI.md                           # Gemini context (mirrors CLAUDE.md)
├── SKILLS.md                           # Source of truth skill manifest
├── LICENSE                             # MIT License
├── agent_docs/                         # Progressive disclosure docs
│   ├── creating-skills.md
│   ├── packaging.md
│   └── quality.md
├── docs/                               # Documentation and planning
│   ├── INTEGRATION_PLAN.md
│   ├── QUALITY_AUDIT_REPORT.md
│   ├── SKILL-8-SPEC.md
│   └── SKILL-9-SPEC.md
├── SkillTemplate/                      # Infrastructure: Template + validation
│   ├── INTEGRATION_RUNBOOK.md
│   ├── scripts/validate-skill.sh
│   └── skill-template/
├── SkillPackager/                      # Infrastructure: Packaging automation
│   └── scripts/
│       ├── package-skill.sh
│       ├── batch-package.sh
│       └── test-skill-installation.sh
├── ProsePolish/                        # Writing quality analysis
├── ResearchToEssay/                    # Research-driven writing
├── ConceptForge/                       # Dialectical concept development
├── ProcessMapper/                      # SOP documentation & automation
├── Claimify/                           # Argument structure analysis
├── CodexPeerReview/                    # AI peer review with Codex
├── GeminiPeerReview/                   # AI peer review with Gemini
├── ContextContinuity/                  # High-fidelity context transfer
├── ContextContinuityCode/              # Dev-optimized context transfer
├── DadJokeValidator/                   # Dad joke analysis and generation
├── ExcelAuditor/                       # Excel file auditing and analysis 🧪
├── InevitabilityEngine/                # AI business opportunity discovery
├── AgentMail/                          # Email automation for agents
├── CodebaseNavigator/                  # Semantic code search
├── ClaudeProjectDocs/                  # CLAUDE.md generation
├── NanoBananaSkill/                    # AI image generation via MCP
├── MCPBuilder/                         # Custom MCP tool development
├── PlaywrightSkill/                    # Browser automation
├── WritingSkills/                      # TDD for documentation (META-SKILL)
├── AWSSkills/                          # AWS triple-pack
│   ├── aws-cdk-development/
│   ├── aws-serverless-eda/
│   └── aws-cost-operations/
├── ArtifactsBuilder/                   # React artifacts for claude.ai
├── NotebookLMSkill/                    # Source-grounded Q&A
└── CSVDataSummarizer/                  # Proactive data analysis
```

Each skill follows a standardized structure:
```
SkillCollection/
├── skill-name/                         # Source skill directory
│   ├── SKILL.md                        # Required: Skill definition
│   ├── README.md                       # Documentation
│   ├── CHANGELOG.md                    # Version history
│   ├── LICENSE                         # License file
│   ├── references/                     # Optional: Reference docs
│   └── scripts/ or assets/             # Optional: Supporting files
└── dist/                               # Distribution packages
    ├── skill-name-vX.Y.Z.skill         # Packaged release
    ├── skill-name-vX.Y.Z.skill.sha256  # Checksum
    └── skill-name-vX.Y.Z.metadata.json # Metadata
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
7. **Evidence-Based**: Use Writing Skills META-SKILL for TDD approach to documentation

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
| Context Continuity - Code Edition | v1.0.0 | 2025-11-16 | Claude Code-optimized dev context transfer |
| Dad Joke Validator | v1.1.0 | 2025-11-16 | Template-based generation, Gemini peer review improvements |
| MCP Builder | v1.0.0 | 2025-11-16 | Custom MCP server development methodology |
| Playwright | v1.0.0 | 2025-11-16 | Browser automation with model-invoked code generation |
| Writing Skills | v1.0.0 | 2025-11-16 | META-SKILL: TDD for documentation, Iron Law methodology |
| AWS CDK Development | v1.0.0 | 2025-11-16 | Infrastructure as Code with AWS CDK |
| AWS Serverless & EDA | v1.0.0 | 2025-11-16 | Serverless applications and event-driven architecture |
| AWS Cost & Operations | v1.0.0 | 2025-11-16 | Cost optimization, monitoring, observability |
| Artifacts Builder | v1.0.0 | 2025-11-16 | React artifacts with 43 shadcn/ui components |
| NotebookLM | v1.0.0 | 2025-11-16 | Source-grounded Q&A with browser automation |
| CSV Data Summarizer | v1.0.0 | 2025-11-16 | Proactive data analysis, design pattern reference |
| Excel Auditor | v1.0.0 | 2025-12-05 | 🧪 IN TESTING - Excel file auditing and formula analysis |

---

## Testing & Quality Assurance

Comprehensive testing validates production readiness for peer review skills:

| Skill | Pass Rate | Avg Quality | Status |
|-------|-----------|-------------|--------|
| **Codex Peer Review** | 100% (7/7) | 4.8/5.0 | ✅ Production Ready |
| **Gemini Peer Review** | 87.5% (7/8) | 5.0/5.0 | ✅ Production Ready |
| **Dad Joke Validator** | 100% (11/11) | N/A | ✅ Production Ready |

**Infrastructure Quality:**
- 100% validation pass rate on all integrated skills
- 10x velocity improvement with SkillTemplate + SkillPackager
- Zero packaging errors across all distributions

**For complete testing documentation:**
- [CodexPeerReview/TESTING.md](CodexPeerReview/TESTING.md)
- [GeminiPeerReview/TESTING.md](GeminiPeerReview/TESTING.md)
- [docs/QUALITY_AUDIT_REPORT.md](docs/QUALITY_AUDIT_REPORT.md)

---

## Creating Your Own Skills

Want to build a custom skill? Use the SkillTemplate for rapid development:

### Quick Start

```bash
# Copy the template
cp -r SkillTemplate/skill-template my-new-skill

# Customize SKILL.md, README.md, CHANGELOG.md

# Validate before packaging
./SkillTemplate/scripts/validate-skill.sh my-new-skill

# Package for distribution
./SkillPackager/scripts/package-skill.sh my-new-skill
```

### Follow the Writing Skills META-SKILL

**The Iron Law:** NO SKILL WITHOUT A FAILING TEST FIRST

1. Create pressure scenario (test without skill)
2. Watch agent fail - document exact behavior
3. Write minimal skill addressing those failures
4. Verify agent now complies
5. Close loopholes systematically

**Resources:**
- [SkillTemplate Documentation](SkillTemplate/README.md)
- [Writing Skills META-SKILL](WritingSkills/writing-skills/SKILL.md)
- [Integration Runbook](SkillTemplate/INTEGRATION_RUNBOOK.md)
- [Claude Code Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills)

---

## Contributing

Contributions welcome! To add a new skill:

1. Fork this repository
2. Use SkillTemplate as starting point
3. Follow Writing Skills META-SKILL methodology (test first!)
4. Include comprehensive SKILL.md with clear trigger phrases
5. Add worked examples in references/
6. Create versioned release in dist/
7. Update this README with the new skill
8. Submit a pull request

For issues or feature requests, please open an issue.

---

## Roadmap

Planned skills for future development:

**Priority 2 Skills (In Progress):**
- EPUB Generator (92/100) - Production-ready markdown to EPUB conversion
- Web Asset Generator (91/100) - Favicon/icon generation with WCAG validation
- Meme Generator - Contextual meme creation with template library
- ASCII Art Generator - Terminal-friendly visualizations
- Meeting Bullshit Detector - Corporate buzzword analysis

**Under Consideration:**
- Strategic Mapping (Wardley mapping and doctrine analysis)
- Decision Analysis (Multi-criteria decision frameworks)
- Code Architecture (System design pattern recognition)

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

**Current Skills**: 27 skills | **Total Size**: ~600KB | **Last Updated**: 2025-12-07

Built with Claude Code | [Learn More](https://docs.claude.com/en/docs/claude-code)
