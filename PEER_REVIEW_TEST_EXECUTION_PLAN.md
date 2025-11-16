# Peer Review Skills - Test Execution Plan with Subagents

**Version:** 1.0
**Date:** 2025-01-12
**Parent Document:** PEER_REVIEW_TEST_PLAN.md

## Overview

This document outlines the strategy for executing the comprehensive peer review test plan using subagents to preserve context and enable parallel execution.

---

## Execution Strategy

### Parallel vs Sequential Execution

**Parallel Execution (where possible):**
- Test data preparation (all can run in parallel)
- Independent use case tests (no dependencies)
- Comparative analysis tests (after use cases complete)

**Sequential Execution (where required):**
- Integration tests (require use case completion)
- Edge case tests (build on integration learnings)

### Subagent Allocation

**Total Subagents Needed:** 15-20
**Execution Phases:** 4
**Estimated Total Time:** 4-6 hours

---

## Phase 1: Test Data Preparation (Parallel)

### Using Existing Repositories

**Available Real Codebases:**
- **prompt-evolve** - `/Users/leegonzales/Projects/leegonzales/prompt-evolve/`
  - Language: Go
  - Files: 36 Go files
  - Size: ~9,033 LOC
  - Purpose: Prompt evolution system with genetic algorithms
  - Good for: Architecture review, large codebase analysis, code review

- **AISkills** - `/Users/leegonzales/Projects/leegonzales/AISkills/` (current repo)
  - Language: Markdown + skill definitions
  - Size: ~10k+ lines of documentation
  - Purpose: Claude Code skills collection
  - Good for: Documentation review, structure analysis

- **LangChainExamples** - `/Users/leegonzales/Projects/leegonzales/LangChainExamples/`
  - Language: Jupyter notebooks (Python)
  - Files: 8 notebooks
  - Purpose: LangChain examples and experiments
  - Good for: Code review, learning use cases

- **PathfinderOpenReference** - `/Users/leegonzales/Projects/leegonzales/PathfinderOpenReference/`
- **SpellBook** - `/Users/leegonzales/Projects/leegonzales/SpellBook/`
- **AIPrompts** - `/Users/leegonzales/Projects/leegonzales/AIPrompts/`

### Agent Group 1: Test Data Preparation (3 agents in parallel)

**Agent 1-1: Create Architecture Diagrams for prompt-evolve**
- **Task:** Generate architecture diagrams for prompt-evolve codebase
- **Deliverable:** `test-data/diagrams/`
- **Contents:**
  - Read prompt-evolve codebase structure
  - Create architecture diagram (Mermaid → PNG)
  - Create component diagram showing modules
  - Create data flow diagram for evolution process
  - Document key abstractions and patterns
- **Time Estimate:** 30 minutes
- **Model:** Sonnet

**Agent 1-2: Security Test Cases (Focused extraction)**
- **Task:** Extract or create focused security examples from existing code
- **Deliverable:** `test-data/security/`
- **Approach:**
  - Check prompt-evolve and other repos for auth/security code
  - If found, extract relevant sections
  - If not found, create minimal auth examples with planted vulnerabilities:
    - JWT implementation with weak signing
    - Session management with fixation vulnerability
    - API key handling with exposure risk
  - Document threat model
- **Time Estimate:** 25 minutes
- **Model:** Sonnet

**Agent 1-3: Create Supplementary Test Materials**
- **Task:** Create additional test materials not covered by existing repos
- **Deliverable:** `test-data/supplementary/`
- **Contents:**
  - Performance test case (slow API endpoint simulation)
  - Design decision scenario (caching strategy comparison)
  - Testing strategy example (state machine with test gaps)
  - Alternative approach scenario (conflict resolution problem)
- **Time Estimate:** 30 minutes
- **Model:** Sonnet

---

## Phase 2: Core Use Cases Testing (Parallel)

### Agent Group 2: Architecture Review (2 agents)

**Agent 2-1: UC-1-C (Codex Architecture Review)**
- **Dependencies:** Agent 1-1 (architecture diagrams)
- **Task:** Execute architecture review test with Codex using prompt-evolve
- **Test Repository:** `/Users/leegonzales/Projects/leegonzales/prompt-evolve/`
- **Steps:**
  1. Read prompt-evolve codebase structure (pkg/, cmd/, internal/)
  2. Read architecture diagram from test-data/diagrams/
  3. Trigger peer review: "Get Codex's opinion on this prompt-evolve architecture"
  4. Observe Claude's behavior:
     - Context preparation (how much code included)
     - Codex CLI invocation
     - Synthesis quality
  5. Evaluate against success criteria
  6. Record results using test reporting template
- **Deliverable:** Test report for UC-1-C
- **Time Estimate:** 20 minutes
- **Model:** Sonnet (needs to execute and evaluate)

**Agent 2-2: UC-1-G (Gemini Architecture Review)**
- **Dependencies:** Agent 1-1 (architecture diagrams)
- **Task:** Execute architecture review test with Gemini using prompt-evolve
- **Test Repository:** `/Users/leegonzales/Projects/leegonzales/prompt-evolve/` (full 9k LOC)
- **Steps:**
  1. Read entire prompt-evolve codebase (~9k LOC)
  2. Include architecture diagram via --image flag
  3. Trigger: "Review this prompt-evolve architecture with Gemini, include the diagram"
  4. Verify entire codebase can be processed (1M token window test)
  5. Verify diagram is included via --image flag
  6. Evaluate synthesis quality
  7. Compare with Codex results (complementary insights?)
  8. Record results
- **Deliverable:** Test report for UC-1-G
- **Time Estimate:** 25 minutes
- **Model:** Sonnet

### Agent Group 3: Design Decision Validation (2 agents)

**Agent 2-3: UC-2-C (Codex Design Decision)**
- **Dependencies:** Agent 1-1 (for context)
- **Task:** Test design decision validation (Event Sourcing vs CRUD)
- **Steps:**
  1. Prepare decision context (orders domain from microservices)
  2. Trigger: "Should we use event sourcing or CRUD for orders? Get Codex's take"
  3. Evaluate trade-off matrix quality
  4. Check for context-dependent recommendations
  5. Record results
- **Deliverable:** Test report for UC-2-C
- **Time Estimate:** 15 minutes
- **Model:** Sonnet

**Agent 2-4: UC-2-G (Gemini Design Decision)**
- **Dependencies:** Agent 1-4 (large codebase for pattern analysis)
- **Task:** Test design decision with codebase pattern analysis
- **Steps:**
  1. Use large codebase as context
  2. Trigger: "What caching strategy should we use? Gemini, analyze our codebase patterns"
  3. Verify Gemini identifies existing patterns
  4. Evaluate consistency analysis
  5. Record results
- **Deliverable:** Test report for UC-2-G
- **Time Estimate:** 20 minutes
- **Model:** Sonnet

### Agent Group 4: Security Review (2 agents)

**Agent 2-5: UC-3-C (Codex Security Review)**
- **Dependencies:** Agent 1-2 (security test cases)
- **Task:** Test security vulnerability detection with Codex
- **Steps:**
  1. Read security test cases with planted vulnerabilities
  2. Trigger: "Security review this authentication code with Codex"
  3. Verify planted vulnerabilities are detected
  4. Check for complementary insights (different vulns found)
  5. Evaluate remediation quality
  6. Record results
- **Deliverable:** Test report for UC-3-C
- **Time Estimate:** 20 minutes
- **Model:** Sonnet

**Agent 2-6: UC-3-G (Gemini Security Review)**
- **Dependencies:** Agent 1-2 (security test cases)
- **Task:** Test cross-module security analysis with Gemini
- **Steps:**
  1. Provide full auth system context
  2. Trigger: "Gemini, trace security boundaries across this entire auth system"
  3. Verify cross-module analysis
  4. Check for indirect vulnerabilities
  5. Evaluate attack surface mapping
  6. Record results
- **Deliverable:** Test report for UC-3-G
- **Time Estimate:** 20 minutes
- **Model:** Sonnet

---

## Phase 3: Specialized Use Cases (Parallel)

### Agent Group 5: Performance & Testing (4 agents)

**Agent 3-1: UC-4-C (Codex Performance)**
- **Dependencies:** Agent 1-3 (performance test cases)
- **Task:** Test performance analysis with Codex
- **Deliverable:** Test report for UC-4-C
- **Time Estimate:** 15 minutes
- **Model:** Sonnet

**Agent 3-2: UC-4-G (Gemini Performance)**
- **Dependencies:** Agent 1-3 (performance test cases)
- **Task:** Test systemic performance analysis with Gemini
- **Deliverable:** Test report for UC-4-G
- **Time Estimate:** 15 minutes
- **Model:** Sonnet

**Agent 3-3: UC-5-C (Codex Testing Strategy)**
- **Dependencies:** Agent 1-1 (use state machine from services)
- **Task:** Test coverage gap identification with Codex
- **Deliverable:** Test report for UC-5-C
- **Time Estimate:** 15 minutes
- **Model:** Sonnet

**Agent 3-4: UC-5-G (Gemini Testing Strategy)**
- **Dependencies:** Agent 1-4 (large codebase with tests)
- **Task:** Test systematic gap analysis with Gemini
- **Deliverable:** Test report for UC-5-G
- **Time Estimate:** 15 minutes
- **Model:** Sonnet

### Agent Group 6: Learning & Alternatives (4 agents)

**Agent 3-5: UC-6-C (Codex Code Review)**
- **Task:** Test code explanation with Codex
- **Deliverable:** Test report for UC-6-C
- **Time Estimate:** 15 minutes
- **Model:** Sonnet

**Agent 3-6: UC-6-G (Gemini Code Review)**
- **Task:** Test Search grounding for similar patterns
- **Deliverable:** Test report for UC-6-G
- **Time Estimate:** 15 minutes
- **Model:** Sonnet

**Agent 3-7: UC-7-C (Codex Alternatives)**
- **Task:** Test alternative approach generation with Codex
- **Deliverable:** Test report for UC-7-C
- **Time Estimate:** 15 minutes
- **Model:** Sonnet

**Agent 3-8: UC-7-G (Gemini Alternatives)**
- **Task:** Test research-grounded alternatives with Gemini
- **Deliverable:** Test report for UC-7-G
- **Time Estimate:** 15 minutes
- **Model:** Sonnet

### Agent Group 7: Gemini-Specific Features (2 agents)

**Agent 3-9: UC-8-G (Large Codebase Analysis)**
- **Dependencies:** Agent 1-4 (large monorepo)
- **Task:** Test Gemini's 1M token context capability
- **Steps:**
  1. Provide full 50-60k LOC codebase
  2. Trigger: "Gemini, analyze this entire codebase and map the architecture"
  3. Verify entire codebase processed
  4. Evaluate architectural insights
  5. Check dependency mapping
  6. Record results
- **Deliverable:** Test report for UC-8-G
- **Time Estimate:** 25 minutes
- **Model:** Sonnet

**Agent 3-10: UC-9-G (Multimodal Technical Review)**
- **Dependencies:** Agent 1-1, Agent 1-5 (code + multimodal assets)
- **Task:** Test multimodal analysis (PDF + diagram + code)
- **Steps:**
  1. Provide API spec (PDF), diagram (PNG), implementation
  2. Trigger: "Gemini, check if our implementation matches the design spec and diagram"
  3. Verify multimodal integration
  4. Evaluate gap analysis quality
  5. Record results
- **Deliverable:** Test report for UC-9-G
- **Time Estimate:** 20 minutes
- **Model:** Sonnet

---

## Phase 4: Integration, Edge Cases & Comparative Analysis (Sequential)

### Agent Group 8: Integration Tests (3 agents sequential)

**Agent 4-1: IT-1 through IT-3**
- **Dependencies:** All Phase 2 & 3 agents (learn from use case executions)
- **Task:** Test automatic triggering, skill selection, synthesis quality
- **Steps:**
  1. Test natural language triggers (no explicit AI mention)
  2. Test specific AI selection ("Get Gemini's take" vs "What would Codex think")
  3. Evaluate synthesis quality across all completed tests
  4. Record results
- **Deliverable:** Integration test report (IT-1, IT-2, IT-3)
- **Time Estimate:** 30 minutes
- **Model:** Sonnet

**Agent 4-2: IT-4 & IT-5**
- **Dependencies:** Agent 4-1
- **Task:** Test error handling and context preparation quality
- **Steps:**
  1. Simulate CLI not available (rename binary temporarily)
  2. Verify graceful error handling
  3. Review all context preparations from Phase 2 & 3
  4. Evaluate context quality across tests
  5. Record results
- **Deliverable:** Integration test report (IT-4, IT-5)
- **Time Estimate:** 20 minutes
- **Model:** Sonnet

### Agent Group 9: Edge Cases (2 agents sequential)

**Agent 4-3: EC-1 through EC-5**
- **Dependencies:** Agent 4-2
- **Task:** Test edge cases and boundary conditions
- **Steps:**
  1. Test empty response handling (malformed CLI call)
  2. Test rate limiting (rapid-fire requests)
  3. Test context too large (provide 2M token context)
  4. Test unclear synthesis (vague question)
  5. Test conflicting recommendations (controversial decision)
  6. Record results for all 5 edge cases
- **Deliverable:** Edge case test report
- **Time Estimate:** 40 minutes
- **Model:** Sonnet

### Agent Group 10: Comparative Analysis (1 agent)

**Agent 4-4: CA-1 through CA-3**
- **Dependencies:** All test results from Phases 2 & 3
- **Task:** Comparative analysis of Codex vs Gemini across use cases
- **Steps:**
  1. Analyze UC-1-C vs UC-1-G (Architecture Review)
  2. Analyze UC-3-C vs UC-3-G (Security Review)
  3. Analyze UC-4-C vs UC-4-G (Performance Analysis)
  4. Compare:
     - Depth of analysis
     - Types of concerns raised
     - Complementary vs overlapping insights
     - Response times
     - Strengths and weaknesses
  5. Create comparative analysis report
- **Deliverable:** Comparative analysis report
- **Time Estimate:** 45 minutes
- **Model:** Sonnet

---

## Phase 5: Test Report Synthesis (1 agent)

### Agent 5-1: Final Test Summary

- **Dependencies:** All agents from Phases 1-4
- **Task:** Synthesize all test results into final comprehensive report
- **Steps:**
  1. Collect all test reports
  2. Calculate success rates:
     - Functional requirements (% tests passed)
     - Quality metrics (average scores)
     - Performance metrics
  3. Identify issues found across all tests
  4. Prioritize issues by severity
  5. Create recommendations for improvements
  6. Write executive summary
  7. Generate final test report with all results
- **Deliverable:** `PEER_REVIEW_FINAL_TEST_REPORT.md`
- **Time Estimate:** 60 minutes
- **Model:** Sonnet

---

## Execution Command Template

When ready to execute, use this template for each agent:

```markdown
Agent [X-Y]: [Name]
Task: [Description]
Dependencies: [List agents that must complete first]
Deliverable: [What this agent produces]

Prompt for subagent:
"Execute test case [UC-X-Y] for the peer review skill testing.

Test Case: [Use Case Name]
Test Plan Location: /Users/leegonzales/Projects/leegonzales/AISkills/PEER_REVIEW_TEST_PLAN.md
Section: [Specific section in test plan]

[If test data preparation:]
Create test data as specified in the test plan:
- [Specific requirements from test plan]
- [Deliverable location]
- [Contents needed]

[If test execution:]
Execute the test following these steps:
1. [Step 1 from plan]
2. [Step 2 from plan]
...

Evaluate against success criteria:
- [Criterion 1]
- [Criterion 2]
...

Record results using the test reporting template from the plan.

Deliverable: [Specific file to write with results]"
```

---

## Timeline Estimation

### Phase 1: Test Data Preparation
- **Agents:** 5 parallel
- **Duration:** ~60 minutes (longest agent)
- **Start:** T+0
- **Complete:** T+60min

### Phase 2: Core Use Cases
- **Agents:** 6 parallel (2 groups of 3)
- **Duration:** ~40 minutes (longest tests)
- **Start:** T+60min
- **Complete:** T+100min

### Phase 3: Specialized Use Cases
- **Agents:** 10 parallel
- **Duration:** ~25 minutes (longest test)
- **Start:** T+100min
- **Complete:** T+125min

### Phase 4: Integration & Comparative
- **Agents:** 4 sequential
- **Duration:** ~135 minutes (cumulative)
- **Start:** T+125min
- **Complete:** T+260min

### Phase 5: Final Synthesis
- **Agent:** 1
- **Duration:** ~60 minutes
- **Start:** T+260min
- **Complete:** T+320min (5h 20min total)

---

## Resource Requirements

### Compute
- **Concurrent agents max:** 10
- **Claude API usage:** ~30 agent invocations × average complexity
- **Model preference:** Sonnet for quality and complexity

### Storage
- **Test data:** ~50-60k LOC + diagrams + PDFs (~100MB)
- **Test reports:** ~20 markdown files (~2MB)
- **Final report:** 1 comprehensive document (~100KB)

### Tools
- **Required:** Both Codex and Gemini CLI must be installed and authenticated
- **Optional:** Git for test data repositories

---

## Execution Checklist

**Before Starting:**
- [ ] Both skills installed in `~/.claude/skills/`
- [ ] Codex CLI installed and authenticated (`codex --version`)
- [ ] Gemini CLI installed and authenticated (`gemini --version`)
- [ ] Test data directory created: `test-data/`
- [ ] Test results directory created: `test-results/`
- [ ] Test plan reviewed and understood

**Phase 1 Ready:**
- [ ] All 5 test data preparation agents defined
- [ ] Prompts ready for parallel execution

**Phase 2 Ready:**
- [ ] Test data from Phase 1 complete and verified
- [ ] Core use case test agents defined

**Phase 3 Ready:**
- [ ] Phase 2 tests complete
- [ ] Specialized test agents defined

**Phase 4 Ready:**
- [ ] All use case tests complete
- [ ] Integration and edge case test agents defined

**Phase 5 Ready:**
- [ ] All test reports collected
- [ ] Final synthesis agent defined

**After Completion:**
- [ ] Final test report reviewed
- [ ] Issues documented
- [ ] Recommendations prioritized
- [ ] Follow-up actions assigned

---

## Success Criteria for Execution Plan

- [ ] All 21 agents execute successfully
- [ ] All test reports generated
- [ ] No blocking errors that prevent test completion
- [ ] Final comprehensive report produced
- [ ] Timeline adhered to within ±20%
- [ ] Resource usage within acceptable limits

---

**End of Test Execution Plan**
