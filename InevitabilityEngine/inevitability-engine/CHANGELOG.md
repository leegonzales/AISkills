# Changelog

All notable changes to the Inevitability Engine skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-22

### Added
- Initial release of the Inevitability Engine skill
- Six-phase research protocol:
  - Phase 1: Capability Frontier Mapping
  - Phase 2: Opportunity Discovery (Segment-Problem Analysis)
  - Phase 3: Business Model Generation
  - Phase 4: Market Validation & Refinement
  - Phase 5: Inevitability Scoring
  - Phase 6: Synthesis & Output
- Comprehensive reference documentation:
  - `capability-mapping.md` - Detailed Phase 1 protocol
  - `opportunity-discovery.md` - Detailed Phase 2 protocol
  - `business-model-generation.md` - Detailed Phase 3 protocol
  - `validation-refinement.md` - Detailed Phase 4 protocol
  - `inevitability-framework.md` - Scoring system and formulas
  - `research-protocols.md` - Complete query library for all phases
  - `output-templates.md` - Structured deliverable formats
- Inevitability scoring framework with formula: `((E + T + M) / 3) - (F / 2)`
- 10 synthetic worker primitives (archetypes)
- Time-horizon capability unlock matrix (3mo, 6mo, 12mo, 18mo, 24mo)
- Complete research query patterns for capability tracking, pain point mining, competitive analysis
- Output templates for executive summaries, opportunity matrices, deep dives, research appendices
- Interactive workflow allowing users to run full process or jump to specific phases
- Integration guidelines with other skills (process-mapper, research-to-essay, strategy-to-artifact)

### Framework Components
- Wardley evolution mapping for AI capabilities
- Segment-problem matrix for systematic opportunity enumeration
- First principles decomposition for automation feasibility
- Economic leverage calculations
- TAM/SAM/SOM market sizing framework
- Competitive differentiation analysis
- Build-vs-buy decision matrix
- Risk assessment templates
- Sensitivity analysis methodology

### Documentation
- Comprehensive README with quick start guide
- Example use cases (legal services, contract review, B2B SaaS)
- Success criteria definitions
- Quality check checklists for each phase
- Anti-patterns and common mistakes
- Tips for effective research and analysis

### Meta-Instructions
- Prioritize AI-native infrastructure over bolt-on solutions
- Focus on 10-100x cost reductions
- Target workflow replacement over enhancement
- Prefer high-margin software businesses (>70% gross margin)
- Exclude crypto/web3, consumer social, hardware-dependent models

## [2.0.0] - 2026-03-28

### Fixed
- **Formula inconsistency**: Unified inevitability formula across all files (SKILL.md, README.md, inevitability-framework.md, output-templates.md). Now consistently uses geometric mean: `(E × T × M)^(1/3) - (F / 3)` on a 0-10 scale
- **Removed debugging artifacts**: Cleaned up formula calibration notes that shipped in v1.0's inevitability-framework.md
- **Recalculated all examples**: Updated comparative scoring table, sensitivity analysis, and time-horizon scores to use new formula
- **Score thresholds**: Updated from mixed scales (>25, >30, >7) to consistent 0-10 scale (>7.5 = inevitable NOW)

### Changed
- **Capability projections**: Replaced static projection tables with methodology-based approach. Tables now provide the framework for research rather than hardcoded numbers that go stale
- **Wardley evolution map**: Updated to reflect current AI capability landscape (agentic coding, computer use, MCP, extended thinking now positioned accurately)
- **Synthetic worker primitives**: Expanded from 10 to 15 primitives, adding Code Developer, Browser Operator, Voice Agent, Data Pipeline Operator, and Security Sentinel
- **Feasibility ratings**: Updated existing primitives (Research Synthesizer, Compliance Auditor, Workflow Orchestrator, Relationship Maintainer) to reflect current production readiness
- **Time estimates**: Revised from 40-50 hours to 13-23 hours for AI-assisted execution
- **Research protocols**: Parameterized all date references (`[current_year]` instead of hardcoded years), updated model name references
- **Organizational references**: Replaced hardcoded BetterUp/Catalyst references with parameterized `[your_organization]` placeholders
- **Integration points**: Updated to reference modern research tools (Brave Search, archive search, web fetch, AI model knowledge)
- **Self-evaluation**: Revised EVALUATION.md with honest scoring reflecting v1.0 issues and v2.0 improvements

### Added
- **Five forcing functions**: Added "agentic autonomy" and "compound AI systems" to the original three forcing functions
- **Compound AI system architecture**: New section in business model canvas for designing multi-model, multi-agent product architectures
- **Business model Pattern 5**: "Compound AI Platform" pattern for orchestrated multi-agent systems
- **Research source guide**: Comprehensive list of high-quality information sources (Epoch AI, Stanford HAI, Hugging Face, LMSYS, archive.org, etc.)
- **New research protocol sections**: Agentic coding, computer use, voice AI, multi-agent systems query libraries
- **Refresh protocol**: Instructions for updating capability positions and projections each time the engine runs
- **Configuration section**: Users can define organizational context before running for personalized strategic recommendations

## [Unreleased]

### Planned Features
- Case study library of analyzed opportunities with real research data
- Calculation validation scripts for inevitability scoring
- Template library for specific industries (legal, finance, healthcare)
- Automated inevitability score calculator tool
- Time-series tracking for capability evolution

### Potential Enhancements
- Integration with Claude Agent SDK for automated multi-phase research workflows
- Integration with MCP servers for automated data gathering
- Real-time capability tracking dashboard
- Export to various formats (PDF, Notion, Confluence, Google Docs)

---

## Version Numbering

- **Major version** (X.0.0): Significant changes to framework or methodology
- **Minor version** (0.X.0): New phases, reference docs, or major features
- **Patch version** (0.0.X): Bug fixes, clarifications, template improvements

---

## Feedback & Contributions

This skill is part of the AISkills collection. Feedback and contributions are welcome through the main repository.
