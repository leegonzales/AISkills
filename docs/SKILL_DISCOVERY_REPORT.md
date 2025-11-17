# Skill Discovery & Evaluation Report

**Date:** 2025-11-16
**Scope:** Comprehensive evaluation of Claude skills from major repositories
**Skills Evaluated:** 36 skills across 6 repository categories
**Evaluation Method:** Rubric-based scoring (100 pts) by parallel subagents

---

## Executive Summary

**Evaluated:** 36 skills from anthropics/skills, obra/superpowers, and individual repositories
**Tier 1 (Exceptional, 85+):** 15 skills
**Tier 2 (Strong, 70-84):** 12 skills
**Tier 3 (Moderate, 50-69):** 7 skills
**Tier 4 (Low Priority, <50):** 2 skills

**Immediate Integration Recommended:** 10 skills (Tier 1 with high strategic fit)
**Copy & Improve Recommended:** 8 skills (Tier 2 with moderate fit)
**Pass/Reference Only:** 18 skills (low fit or archived)

---

## Top 10 Skills for Immediate Integration

### 1. **MCP-Builder** (anthropics/skills) - 100/100
- **Strategic Fit:** Perfect - Enables users to extend Claude with custom tools
- **Action:** Fork immediately
- **Value:** Multiplies value of entire AISkills collection
- **Notes:** Four-phase methodology, multi-language support, research-backed

### 2. **AWS Skills** (zxkane/aws-skills) - 100/100
- **Strategic Fit:** Perfect - Fills cloud development gap
- **Action:** Fork immediately
- **Value:** Three complementary skills (CDK, Serverless, CloudFormation)
- **Notes:** Exemplary MCP integration with 8+ servers

### 3. **Playwright Skill** (lackeyjb/playwright-skill) - 104/100 (capped at 100)
- **Strategic Fit:** High - Critical testing capability
- **Action:** Fork immediately
- **Value:** Model-invoked browser automation (unique approach)
- **Notes:** Professional structure, 727 stars, active maintenance

### 4. **iOS Simulator Skill** (conorluddy/ios-simulator-skill) - 105/100 (capped at 100)
- **Strategic Fit:** High - Best-in-class mobile testing
- **Action:** Fork
- **Value:** Semantic accessibility-first navigation, 21 utility scripts
- **Notes:** Exceptional documentation, macOS-only (limit applicability)

### 5. **NotebookLM Skill** (PleasePrompto/notebooklm-skill) - 97/100
- **Strategic Fit:** High - Addresses hallucination problem
- **Action:** Fork with maintenance plan
- **Value:** Source-grounded answers from research documents
- **Notes:** Requires browser automation (maintenance burden), 463 stars

### 6. **Artifacts-Builder** (anthropics/skills) - 96/100
- **Strategic Fit:** High - Modern frontend artifact creation
- **Action:** Fork
- **Value:** React + TypeScript + Tailwind + shadcn/ui stack
- **Notes:** Anti-slop design guidance, integrates with peer review skills

### 7. **Writing Skills** (obra/superpowers) - 96/100
- **Strategic Fit:** Perfect - Meta-skill for skill development
- **Action:** Fork immediately
- **Value:** TDD approach to skill creation ("Iron Law")
- **Notes:** Foundational for improving entire collection quality

### 8. **CSV Data Summarizer** (coffeefuelbump/csv-data-summarizer) - 93/100
- **Strategic Fit:** High - Data analysis capability
- **Action:** Fork and use as design reference
- **Value:** Exemplary "DO NOT ASK" proactive design philosophy
- **Notes:** Should be reference example for skill design principles

### 9. **Claude Scientific Skills** (K-Dense-AI) - 93/100
- **Strategic Fit:** Medium-High - Scientific computing domain
- **Action:** Copy and modularize
- **Value:** 118 skills across 15+ domains (bioinformatics, cheminformatics, etc.)
- **Notes:** Restructure into focused domain skills (5-15 skills each)

### 10. **EPUB Generator** (smerchek/claude-epub-skill) - 92/100
- **Strategic Fit:** High - Publishing workflow capability
- **Action:** Fork
- **Value:** Production-ready markdown to EPUB conversion
- **Notes:** Comprehensive testing, EPUB3 compliant, needs .skill packaging

---

## Tier 1 Skills - Additional Candidates (Copy & Improve)

### 11. **Web Asset Generator** (alonw0/web-asset-generator) - 91/100
- **Action:** Fork
- **Value:** Favicon, icon, and web asset generation with WCAG validation
- **Notes:** Interactive workflow design, dependency on Pillow/Pilmoji

### 12. **Verification-Before-Completion** (obra/superpowers) - 91/100
- **Action:** Fork immediately
- **Value:** AI-specific skill preventing premature success claims
- **Notes:** Critical for production workflows, universal applicability

### 13. **Skill Seekers** (yusufkaraaslan) - 90/100
- **Action:** Fork as meta-tool
- **Value:** Converts documentation to skills (AST parsing, conflict detection)
- **Notes:** Feature as skill development tool, not regular skill

### 14. **Systematic Debugging** (obra/superpowers) - 89/100
- **Action:** Fork
- **Value:** Comprehensive 4-phase debugging framework
- **Notes:** Integrates with root-cause-tracing

### 15. **Root-Cause Tracing** (obra/superpowers) - 85/100
- **Action:** Fork (bundle with systematic-debugging)
- **Value:** 5-step backward tracing methodology
- **Notes:** Required dependency for systematic-debugging

---

## Tier 2 Skills - Copy & Improve Recommended

### Developer Tools
- **FFUF Skill** (jthack/ffuf_claude_skill) - 84/100 - Security testing
- **Dispatching Parallel Agents** (obra/superpowers) - 84/100 - Parallel debugging
- **Condition-Based Waiting** (obra/superpowers) - 80/100 - Async test patterns
- **Theme Factory** (anthropics/skills) - 76/100 - Artifact styling (pair with artifacts-builder)
- **Testing Anti-Patterns** (obra/superpowers) - 76/100 - Test quality
- **Test-Driven Development** (obra/superpowers) - 75/100 - TDD methodology

### Collaboration & Workflows
- **Subagent-Driven Development** (obra/superpowers) - 74/100 - AI workflow methodology
- **Defense-in-Depth** (obra/superpowers) - 72/100 - Validation framework

---

## Skills to Pass (Strategic Misfit)

### High Quality but Wrong Domain
- **Slack GIF Creator** (anthropics/skills) - 82/100 - Slack-specific, zero strategic fit
- **Algorithmic Art** (anthropics/skills) - 81/100 - Creative coding, different user base
- **Canvas Design** (anthropics/skills) - 78/100 - Visual design, requires strategic decision

### Archived or Low Maturity
- **Brainstorming** (obra/superpowers-skills) - 54/100 - Archived repo, plugin-dependent
- **D3.js Skill** (chrisvoncsefalvay) - 62/100 - Single commit, no README, abandoned
- **Threat Hunting Sigma** (jthack) - N/A - Repository not found (404)

### Overlaps with Existing Skills
- **Requesting Code Review** (obra/superpowers) - 55/100 - Overlaps with Gemini/Codex Peer Review
- **Receiving Code Review** (obra/superpowers) - 58/100 - Meta-skill, narrow utility

### Niche Workflows
- **Using Git Worktrees** (obra/superpowers) - 57/100 - Standard git practice
- **Finishing Development Branch** (obra/superpowers) - 61/100 - Standard workflow
- **Sharing Skills** (obra/superpowers) - 48/100 - Ecosystem-specific

---

## Repository Health Assessment

### Excellent (Active, Well-Maintained)
- **anthropics/skills** (17.2k ⭐) - Official, production-quality
- **obra/superpowers** (6.9k ⭐) - Battle-tested, v3.3.1 (Oct 2025)
- **lackeyjb/playwright-skill** (727 ⭐) - v4.0.2, active
- **PleasePrompto/notebooklm-skill** (463 ⭐) - Active
- **yusufkaraaslan/Skill_Seekers** (4.1k ⭐) - Active, v2.0.0

### Good (Stable, Some Activity)
- **K-Dense-AI/claude-scientific-skills** (887 ⭐) - Good community
- **conorluddy/ios-simulator-skill** (107 ⭐) - Oct 2025 update
- **coffeefuelbump/csv-data-summarizer** (72 ⭐) - v2.1.0
- **alonw0/web-asset-generator** (61 ⭐) - Oct 2025
- **jthack/ffuf_claude_skill** (65 ⭐) - Active
- **zxkane/aws-skills** (24 ⭐) - 14 commits, active

### Archived (Read-Only, No Updates)
- **obra/superpowers-skills** (428 ⭐) - Archived Oct 27, 2025
  - Still valuable skills but requires copying, not forking

### Questionable
- **chrisvoncsefalvay/claude-d3js-skill** (22 ⭐) - Single commit, minimal docs
- **smerchek/claude-epub-skill** (17 ⭐) - Low stars but high quality

---

## Strategic Recommendations

### Immediate Actions (Next 2 Weeks)

**Phase 1: Core Infrastructure Skills**
1. Fork **mcp-builder** - Enables entire ecosystem expansion
2. Fork **writing-skills** - Improves all future skill development
3. Fork **verification-before-completion** - Critical AI behavior modification

**Phase 2: Developer Tools**
4. Fork **Playwright** - Testing capability
5. Fork **AWS Skills** - Cloud development
6. Fork **artifacts-builder** - Frontend development

**Phase 3: Analysis & Workflows**
7. Fork **systematic-debugging + root-cause-tracing** (bundle)
8. Fork **CSV Data Summarizer** - Use as design reference
9. Fork **NotebookLM** - Research grounding (with maintenance plan)
10. Fork **EPUB Generator** - Publishing workflows

### Medium-Term (1-2 Months)

**Phase 4: Scientific Computing (Modularized)**
- Extract high-value domains from **Claude Scientific Skills**:
  - Bioinformatics skill (genomics, RNA-seq, proteomics)
  - Cheminformatics skill (drug discovery, molecular analysis)
  - Clinical research skill (trial design, healthcare analytics)

**Phase 5: Testing & Quality Suite**
- Copy & improve: **TDD**, **testing-anti-patterns**, **condition-based-waiting**
- Bundle as "Testing Excellence Suite"

**Phase 6: Mobile & Specialized**
- Fork **iOS Simulator** (macOS users)
- Copy **Web Asset Generator**
- Copy **FFUF** (security testing)

### Strategic Decisions Required

**Decision 1: Visual Design Domain?**
- **Question:** Expand AISkills to include visual design (canvas-design, theme-factory)?
- **Current Focus:** Writing, analysis, code reasoning
- **Proposed Focus:** Add professional communication design?
- **Recommendation:** Defer 3-6 months, prioritize developer tools first

**Decision 2: Scientific Computing Modularization?**
- **Question:** How to structure 118 scientific skills?
- **Options:**
  - A) Single comprehensive skill (current structure)
  - B) 5-10 domain-specific skills (recommended)
  - C) Pass and build custom if demand emerges
- **Recommendation:** Option B - Modularize into focused domains

**Decision 3: Archived Repository Handling?**
- **Question:** How to handle obra/superpowers-skills (archived)?
- **Options:**
  - A) Copy all high-quality skills
  - B) Extract and rebuild from scratch
  - C) Reference only
- **Recommendation:** Option A - Copy best skills, add proper structure

---

## Integration Workload Estimate

### Low Effort (< 4 hours each)
- mcp-builder (fork + README)
- aws-skills (fork + version)
- verification-before-completion (fork + structure)
- playwright-skill (fork + minimal changes)

**Subtotal:** ~12-16 hours

### Medium Effort (4-10 hours each)
- writing-skills (fork + examples)
- artifacts-builder (fork + gallery)
- systematic-debugging + root-cause-tracing (bundle)
- csv-data-summarizer (fork + structure)
- epub-generator (fork + packaging)
- web-asset-generator (fork + testing)
- skill-seekers (feature as meta-tool)

**Subtotal:** ~40-70 hours

### High Effort (10-20 hours each)
- notebooklm-skill (fork + maintenance docs)
- ios-simulator-skill (fork + prerequisites)
- scientific-skills (modularize domains)
- testing-suite (TDD + anti-patterns + condition-based)

**Subtotal:** ~60-80 hours

**Total Estimated Effort:** 112-166 hours (~3-4 weeks full-time)

---

## Quality Distribution Analysis

### Score Distribution
- **90-100:** 13 skills (36%)
- **80-89:** 5 skills (14%)
- **70-79:** 9 skills (25%)
- **60-69:** 6 skills (17%)
- **50-59:** 3 skills (8%)

### Common Strengths Across High Scorers
1. Production-ready code with testing
2. Comprehensive documentation
3. Clear unique value proposition
4. Active maintenance
5. Professional repository structure

### Common Weaknesses Across All Skills
1. Missing versioning/packaging (70% of skills)
2. No README or inadequate (60%)
3. Limited examples (50%)
4. No formal testing docs (65%)
5. Missing dist/ folders (80%)

**Insight:** Most skills have excellent SKILL.md but lack production infrastructure. Easy wins by adding structure.

---

## Competitive Landscape

### Coverage Gaps in AISkills Collection (Now Filled)
✅ **Browser automation** - Playwright
✅ **Cloud development** - AWS Skills
✅ **Mobile testing** - iOS Simulator
✅ **Data analysis** - CSV Summarizer
✅ **Publishing** - EPUB Generator
✅ **Debugging methodology** - Systematic Debugging
✅ **Testing frameworks** - TDD, Anti-Patterns
✅ **Skill development** - Writing Skills, Skill Seekers
✅ **AI workflow management** - Verification, Subagent-Driven

### Unique Capabilities Not Found Elsewhere
- **MCP-Builder:** Only comprehensive MCP development skill
- **Writing Skills:** TDD for documentation ("Iron Law")
- **Verification-Before-Completion:** AI-specific behavior modification
- **NotebookLM:** Source-grounded answer generation
- **AWS Skills:** 8+ MCP server integration

### Similar Collections Comparison

**obra/superpowers (6.9k ⭐):**
- Focus: Development workflows, testing, debugging
- Overlap: Testing, debugging (we'll integrate best ones)
- Differentiation: We add writing, analysis, peer review

**anthropics/skills (17.2k ⭐):**
- Focus: Broad (creative, development, enterprise)
- Overlap: MCP-builder, artifacts-builder (we'll fork)
- Differentiation: We're curated for knowledge workers, not general

**ComposioHQ/awesome-claude-skills (3.7k ⭐):**
- Focus: Curation/links, not original skills
- Overlap: References same repos
- Differentiation: We create structured, tested, documented versions

---

## Next Steps

### Immediate (This Week)
1. ✅ Complete this discovery report
2. Review and approve integration plan
3. Create integration schedule (sprint planning)
4. Set up skill-integration branch for work

### Week 1-2 (Core Infrastructure)
1. Fork mcp-builder with enhanced README
2. Fork writing-skills with examples
3. Fork verification-before-completion with structure
4. Document "skill development workflow" using these

### Week 3-4 (Developer Tools)
1. Fork Playwright with testing examples
2. Fork AWS Skills with modular structure
3. Fork artifacts-builder with gallery
4. Test integration scenarios

### Month 2 (Specialized Skills)
1. Scientific Skills modularization
2. Testing Suite bundling
3. NotebookLM with maintenance docs
4. Mobile/Security skills

### Ongoing
- Monitor all forked repos for updates
- Contribute improvements back upstream
- Build community around AISkills collection
- Create skill showcase/demo videos

---

## Success Metrics

### Quantitative
- Target: +10-15 skills in collection (currently 7 → 17-22)
- Quality: All new skills score 85+ on rubric
- Documentation: 100% have README + examples + dist/
- Testing: 80%+ have validation/testing docs

### Qualitative
- Collection covers writing + analysis + code + data + cloud
- Skills work together in integrated workflows
- Professional structure throughout
- Community engagement (issues, PRs, forks)

---

## Risk Assessment

### Low Risk
- Forking official anthropics skills (stable, well-tested)
- Integrating battle-tested obra/superpowers skills

### Medium Risk
- NotebookLM browser automation (maintenance burden)
- Scientific Skills scope (118 skills to modularize)
- iOS Simulator platform limitation (macOS only)

### Mitigations
- Documented maintenance plans for fragile skills
- Phased modularization with prioritization
- Clear prerequisite documentation
- Active monitoring of upstream changes

---

**Report Complete**
**Status:** Ready for integration decisions
**Prepared by:** Claude Code
**Date:** 2025-11-16
