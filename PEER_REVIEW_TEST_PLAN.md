# Peer Review Skills - Comprehensive Test Plan

**Version:** 1.0
**Date:** 2025-01-12
**Skills Under Test:**
- Codex Peer Review v1.0.0
- Gemini Peer Review v1.0.0

## Test Objectives

1. **Functional Verification** - Confirm all use cases work as documented
2. **Quality Assessment** - Evaluate synthesis quality and insight value
3. **Integration Testing** - Verify skills trigger correctly in Claude Code
4. **Comparative Analysis** - Compare Codex vs Gemini strengths across use cases
5. **Edge Case Handling** - Test boundaries and error conditions

---

## Test Environment

### Prerequisites
- ✅ Claude Code with both skills installed in `~/.claude/skills/`
- ✅ Codex CLI installed and authenticated
- ✅ Gemini CLI installed and authenticated
- ✅ Test code repositories prepared
- ✅ Sample architecture diagrams and design documents

### Test Data Requirements
- Small microservices example (~2k LOC)
- Medium-sized backend service (~10k LOC)
- Large codebase for Gemini testing (~50k LOC)
- Security-critical code samples (authentication, authorization)
- Performance-critical code (database queries, caching)
- Test suite examples with gaps
- Architecture diagrams (PNG/PDF)
- Design specification documents (PDF)

---

## Test Cases by Use Case

### UC-1: Architecture Review

**Codex Test (UC-1-C)**
- **Objective:** Validate Codex can review microservices architecture
- **Test Input:**
  - Microservices architecture with 5 services
  - Service boundaries, API contracts, data flow
  - Architecture diagram (optional for Codex)
- **Trigger Phrase:** "Get Codex's opinion on this microservices architecture"
- **Expected Behavior:**
  1. Claude recognizes need for peer review
  2. Prepares context with architecture details
  3. Invokes Codex CLI with appropriate prompt
  4. Receives Codex analysis
  5. Synthesizes Claude + Codex perspectives
  6. Presents balanced architecture assessment
- **Success Criteria:**
  - ✓ Both perspectives documented clearly
  - ✓ Points of agreement identified
  - ✓ Points of divergence explained
  - ✓ Trade-offs made explicit
  - ✓ Actionable recommendations provided
- **Quality Metrics:**
  - Synthesis quality (1-5): ___
  - Insight value (1-5): ___
  - Practical recommendations: Yes/No

**Gemini Test (UC-1-G)**
- **Objective:** Validate Gemini can review architecture with large context
- **Test Input:**
  - Microservices architecture with 8-10 services
  - Complete source code for all services (~30k LOC)
  - Architecture diagram (Gemini can process image)
- **Trigger Phrase:** "Review this architecture with Gemini, include the diagram"
- **Expected Behavior:**
  1. Claude recognizes need for peer review
  2. Prepares extensive context (leverage 1M token window)
  3. Includes architecture diagram via `--image` flag
  4. Invokes Gemini CLI
  5. Synthesizes Claude + Gemini perspectives
  6. Highlights Gemini's holistic insights
- **Success Criteria:**
  - ✓ Large context handled successfully
  - ✓ Diagram analysis integrated
  - ✓ System-wide patterns identified
  - ✓ Cross-service concerns surfaced
  - ✓ Actionable architecture improvements
- **Quality Metrics:**
  - Synthesis quality (1-5): ___
  - Large context handling (1-5): ___
  - Multimodal integration (1-5): ___

---

### UC-2: Design Decision Validation

**Codex Test (UC-2-C)**
- **Objective:** Validate Codex can compare design alternatives
- **Test Input:**
  - Decision: Event Sourcing vs CRUD vs CQRS
  - Context: E-commerce order management
  - Constraints: Team expertise, scalability needs, audit requirements
- **Trigger Phrase:** "Get a second opinion on whether to use event sourcing or CRUD for orders"
- **Expected Behavior:**
  1. Claude prepares trade-off context
  2. Invokes Codex for alternative analysis
  3. Synthesizes perspectives into trade-off matrix
  4. Provides context-dependent recommendation
- **Success Criteria:**
  - ✓ Trade-off matrix created
  - ✓ Both perspectives compared
  - ✓ Context-dependent guidance provided
  - ✓ No forced consensus
  - ✓ User can make informed decision
- **Quality Metrics:**
  - Trade-off clarity (1-5): ___
  - Recommendation quality (1-5): ___

**Gemini Test (UC-2-G)**
- **Objective:** Validate Gemini provides design decision analysis
- **Test Input:**
  - Decision: Caching strategy (Redis, Memcached, In-memory, CDN)
  - Full codebase context showing current patterns
  - Performance requirements
- **Trigger Phrase:** "What caching strategy should we use? Ask Gemini to analyze our codebase patterns"
- **Expected Behavior:**
  1. Claude prepares context with full codebase
  2. Gemini analyzes existing patterns for consistency
  3. Synthesizes recommendation based on codebase reality
- **Success Criteria:**
  - ✓ Existing patterns identified
  - ✓ Consistency analysis provided
  - ✓ Migration path suggested
- **Quality Metrics:**
  - Codebase pattern analysis (1-5): ___

---

### UC-3: Security Review

**Codex Test (UC-3-C)**
- **Objective:** Validate Codex identifies security vulnerabilities
- **Test Input:**
  - JWT authentication implementation
  - Session management code
  - Access control logic
  - Known vulnerabilities planted (e.g., weak token signing, no refresh rotation)
- **Trigger Phrase:** "Security review this authentication code with Codex"
- **Expected Behavior:**
  1. Claude prepares security context
  2. Codex performs security analysis
  3. Synthesis prioritizes vulnerabilities
  4. Remediation steps provided
- **Success Criteria:**
  - ✓ Critical vulnerabilities identified (planted ones found)
  - ✓ Both AIs find different issues (complementary)
  - ✓ Prioritization clear
  - ✓ Remediation actionable
- **Quality Metrics:**
  - Vulnerability detection (1-5): ___
  - Complementary insights: Yes/No
  - Remediation quality (1-5): ___

**Gemini Test (UC-3-G)**
- **Objective:** Validate Gemini traces security boundaries across codebase
- **Test Input:**
  - OAuth2 implementation across multiple modules
  - Full codebase showing indirect attack vectors
- **Trigger Phrase:** "Gemini, trace security boundaries across this entire auth system"
- **Expected Behavior:**
  1. Gemini analyzes full codebase for security flows
  2. Identifies indirect vulnerabilities
  3. Maps attack surface
- **Success Criteria:**
  - ✓ Indirect vulnerabilities found
  - ✓ Attack surface mapped
  - ✓ Cross-module concerns identified
- **Quality Metrics:**
  - Cross-module analysis (1-5): ___

---

### UC-4: Performance Analysis

**Codex Test (UC-4-C)**
- **Objective:** Validate Codex identifies performance bottlenecks
- **Test Input:**
  - Slow API endpoint (N+1 queries, missing indexes, inefficient caching)
  - Performance profile data
  - Target: <100ms, Current: 2s
- **Trigger Phrase:** "This endpoint is too slow, get Codex's analysis"
- **Expected Behavior:**
  1. Codex identifies bottlenecks
  2. Synthesis creates optimization priority matrix
  3. Trade-offs explained (complexity vs gain)
- **Success Criteria:**
  - ✓ Major bottlenecks identified
  - ✓ Optimization priority clear
  - ✓ Quick wins vs long-term improvements separated
- **Quality Metrics:**
  - Bottleneck identification (1-5): ___
  - Optimization priority (1-5): ___

**Gemini Test (UC-4-G)**
- **Objective:** Validate Gemini finds systemic performance issues
- **Test Input:**
  - Slow endpoint + entire data access layer
  - Database schema and query patterns
- **Trigger Phrase:** "Analyze performance of this endpoint and the entire data layer with Gemini"
- **Expected Behavior:**
  1. Gemini analyzes systemic data access patterns
  2. Identifies architectural performance issues
- **Success Criteria:**
  - ✓ Systemic issues found beyond single endpoint
  - ✓ Architectural recommendations provided
- **Quality Metrics:**
  - Systemic analysis (1-5): ___

---

### UC-5: Testing Strategy

**Codex Test (UC-5-C)**
- **Objective:** Validate Codex identifies test coverage gaps
- **Test Input:**
  - Complex state machine implementation
  - Existing test suite with gaps
  - Critical paths documented
- **Trigger Phrase:** "Review our testing strategy for this state machine with Codex"
- **Expected Behavior:**
  1. Codex analyzes test coverage
  2. Identifies missing edge cases
  3. Suggests testing improvements
- **Success Criteria:**
  - ✓ Coverage gaps identified
  - ✓ Edge cases suggested
  - ✓ Testing strategy improvements practical
- **Quality Metrics:**
  - Gap identification (1-5): ___
  - Suggestion quality (1-5): ___

**Gemini Test (UC-5-G)**
- **Objective:** Validate Gemini analyzes tests alongside implementation
- **Test Input:**
  - Implementation + full test suite
  - Test coverage report
- **Trigger Phrase:** "Gemini, analyze our test suite and implementation together to find systematic gaps"
- **Expected Behavior:**
  1. Gemini correlates tests to implementation
  2. Finds systematic testing gaps
- **Success Criteria:**
  - ✓ Test-to-implementation mapping provided
  - ✓ Systematic gaps found
- **Quality Metrics:**
  - Systematic analysis (1-5): ___

---

### UC-6: Code Review & Learning

**Codex Test (UC-6-C)**
- **Objective:** Validate Codex explains complex code patterns
- **Test Input:**
  - Recursive backtracking algorithm
  - Complex async/await pattern
  - Unfamiliar design pattern
- **Trigger Phrase:** "Help me understand this algorithm, get Codex's explanation too"
- **Expected Behavior:**
  1. Both AIs explain the pattern
  2. Synthesis combines explanations
  3. Learning objectives addressed
- **Success Criteria:**
  - ✓ Clear explanations from both
  - ✓ Different perspectives add value
  - ✓ Learning goal achieved
- **Quality Metrics:**
  - Explanation clarity (1-5): ___
  - Learning value (1-5): ___

**Gemini Test (UC-6-G)**
- **Objective:** Validate Gemini finds similar patterns via Search grounding
- **Test Input:**
  - Complex functional programming pattern
- **Trigger Phrase:** "Explain this FP pattern and find similar examples with Gemini"
- **Expected Behavior:**
  1. Gemini explains pattern
  2. References similar patterns (Search grounding)
  3. Provides learning resources
- **Success Criteria:**
  - ✓ Pattern explained
  - ✓ Similar examples found
  - ✓ Learning resources provided
- **Quality Metrics:**
  - Search grounding value (1-5): ___

---

### UC-7: Alternative Approach Generation

**Codex Test (UC-7-C)**
- **Objective:** Validate Codex generates creative alternatives
- **Test Input:**
  - Stuck problem: Real-time collaborative editing conflicts
  - Current approach limitations
  - CRDT/OT research context
- **Trigger Phrase:** "We're stuck on conflict resolution, generate alternatives with Codex"
- **Expected Behavior:**
  1. Codex generates alternative approaches
  2. Synthesis evaluates alternatives
  3. Trade-offs explained
- **Success Criteria:**
  - ✓ Novel alternatives provided
  - ✓ Feasibility assessed
  - ✓ Trade-offs clear
- **Quality Metrics:**
  - Creativity (1-5): ___
  - Feasibility (1-5): ___

**Gemini Test (UC-7-G)**
- **Objective:** Validate Gemini references current research
- **Test Input:**
  - Same stuck problem
- **Trigger Phrase:** "Generate alternatives with Gemini, include current research"
- **Expected Behavior:**
  1. Gemini generates alternatives
  2. References current research (Search grounding)
  3. Provides state-of-the-art context
- **Success Criteria:**
  - ✓ Alternatives grounded in research
  - ✓ Current best practices referenced
- **Quality Metrics:**
  - Research grounding (1-5): ___

---

### UC-8: Large Codebase Analysis (Gemini-Specific)

**Gemini Test (UC-8-G)**
- **Objective:** Validate Gemini's 1M token context for large codebases
- **Test Input:**
  - 50-60k LOC monorepo
  - Multiple modules and services
  - Request: Map architecture and data flows
- **Trigger Phrase:** "Gemini, analyze this entire codebase and map the architecture"
- **Expected Behavior:**
  1. Claude prepares extensive context (full codebase)
  2. Gemini processes in single context
  3. Provides architectural overview
  4. Maps data flows and dependencies
- **Success Criteria:**
  - ✓ Entire codebase processed successfully
  - ✓ Architectural map provided
  - ✓ Module dependencies identified
  - ✓ Data flows traced
  - ✓ Core abstractions explained
- **Quality Metrics:**
  - Large context handling (1-5): ___
  - Architectural insight (1-5): ___
  - Comprehensiveness (1-5): ___

**Note:** This is Gemini's killer feature - not comparable with Codex

---

### UC-9: Multimodal Technical Review (Gemini-Specific)

**Gemini Test (UC-9-G)**
- **Objective:** Validate Gemini's multimodal analysis (diagrams + PDFs + code)
- **Test Input:**
  - API design specification (PDF)
  - Architecture diagram (PNG)
  - Implementation code
  - Mockups/wireframes (if available)
- **Trigger Phrase:** "Gemini, check if our implementation matches the design spec and diagram"
- **Expected Behavior:**
  1. Claude includes PDF + diagram via CLI flags
  2. Gemini processes all modalities
  3. Performs gap analysis
  4. Identifies implementation deviations
- **Success Criteria:**
  - ✓ PDF content analyzed
  - ✓ Diagram analyzed
  - ✓ Code analyzed
  - ✓ Cross-modal consistency checked
  - ✓ Gaps identified with specifics
  - ✓ Recommendations actionable
- **Quality Metrics:**
  - Multimodal integration (1-5): ___
  - Gap analysis quality (1-5): ___
  - Deviation detection (1-5): ___

**Note:** This is Gemini's unique capability - not available with Codex

---

## Integration & Workflow Tests

### IT-1: Automatic Skill Trigger Detection
- **Test:** Use natural language without explicit skill mention
- **Input:** "I need a second opinion on this architecture"
- **Expected:** Claude recognizes and offers peer review
- **Success:** Skill triggers appropriately

### IT-2: Skill Selection (Codex vs Gemini)
- **Test:** User mentions specific AI
- **Input:** "Get Gemini's take on this" vs "What would Codex think?"
- **Expected:** Correct skill invoked
- **Success:** Right AI consulted

### IT-3: Synthesis Quality
- **Test:** Evaluate synthesis across all use cases
- **Criteria:**
  - Clear attribution (Claude said X, Gemini said Y)
  - No forced consensus
  - Trade-offs explicit
  - Complementary insights extracted
  - Actionable recommendations
- **Quality Scale:** 1-5 for each test case

### IT-4: Error Handling
- **Test:** CLI not available
- **Expected:** Graceful degradation, user informed
- **Success:** No crashes, clear error message

### IT-5: Context Preparation Quality
- **Test:** Review prepared contexts in tests
- **Criteria:**
  - Sufficient context provided
  - Clear questions asked
  - Expectations set
  - Appropriate detail level
- **Quality Scale:** 1-5 for each test case

---

## Edge Cases & Boundaries

### EC-1: Empty Response Handling
- **Test:** Gemini/Codex returns empty or error
- **Expected:** Claude handles gracefully, retries if appropriate
- **Success:** No crash, user informed

### EC-2: Rate Limiting
- **Test:** Hit Gemini free tier rate limit (60/min)
- **Expected:** Claude detects and waits or informs user
- **Success:** Graceful handling

### EC-3: Context Too Large
- **Test:** Context exceeds even Gemini's 1M tokens
- **Expected:** Claude chunks or reduces context
- **Success:** Reasonable fallback strategy

### EC-4: Unclear Synthesis
- **Test:** Both AIs provide vague responses
- **Expected:** Claude recognizes and reformulates
- **Success:** Quality signal detected, refinement attempted

### EC-5: Conflicting Recommendations
- **Test:** Claude and peer AI strongly disagree
- **Expected:** Both perspectives presented honestly
- **Success:** No false consensus, user can decide

---

## Comparative Analysis Tests

### CA-1: Codex vs Gemini - Architecture Review
- **Test:** Same architecture reviewed by both
- **Compare:**
  - Depth of analysis
  - Types of concerns raised
  - Complementary vs overlapping insights
  - Response time
- **Goal:** Understand relative strengths

### CA-2: Codex vs Gemini - Security Review
- **Test:** Same security-critical code reviewed by both
- **Compare:**
  - Vulnerability detection rates
  - Unique findings per AI
  - Remediation quality
- **Goal:** Identify which AI excels at security

### CA-3: Codex vs Gemini - Performance Analysis
- **Test:** Same performance issue analyzed by both
- **Compare:**
  - Bottleneck identification
  - Optimization suggestions
  - Systemic vs localized analysis
- **Goal:** Understand performance analysis strengths

---

## Success Criteria Summary

### Functional Requirements
- [ ] All 7 Codex use cases execute successfully
- [ ] All 9 Gemini use cases execute successfully
- [ ] Skills trigger correctly in Claude Code
- [ ] CLI invocations work as documented
- [ ] Error handling is graceful

### Quality Requirements
- [ ] Average synthesis quality ≥ 4/5 across all tests
- [ ] Complementary insights found in ≥70% of tests
- [ ] Trade-offs made explicit in ≥90% of tests
- [ ] Actionable recommendations in ≥80% of tests
- [ ] No forced consensus in any test

### Performance Requirements
- [ ] Codex responses within reasonable time (<30s typical)
- [ ] Gemini responses within reasonable time (<60s for large context)
- [ ] No Claude Code crashes or hangs
- [ ] Rate limiting handled gracefully

### Documentation Requirements
- [ ] All behaviors match documented skill descriptions
- [ ] Reference docs accurately describe usage
- [ ] Examples in docs are representative

---

## Test Execution Plan

### Phase 1: Core Use Cases (Priority)
1. UC-1-C, UC-1-G: Architecture Review (both)
2. UC-2-C, UC-2-G: Design Decision Validation (both)
3. UC-3-C, UC-3-G: Security Review (both)

### Phase 2: Specialized Use Cases
4. UC-4-C, UC-4-G: Performance Analysis (both)
5. UC-5-C, UC-5-G: Testing Strategy (both)
6. UC-6-C, UC-6-G: Code Review & Learning (both)
7. UC-7-C, UC-7-G: Alternative Approach Generation (both)

### Phase 3: Gemini-Specific Features
8. UC-8-G: Large Codebase Analysis (Gemini only)
9. UC-9-G: Multimodal Technical Review (Gemini only)

### Phase 4: Integration & Edge Cases
10. IT-1 through IT-5: Integration tests
11. EC-1 through EC-5: Edge case tests
12. CA-1 through CA-3: Comparative analysis

---

## Test Reporting Template

For each test case, record:

```markdown
### Test: [UC-X-Y] [Use Case Name]

**Date:** YYYY-MM-DD
**Tester:** [Name]
**Status:** ✅ Pass / ❌ Fail / ⚠️ Partial

**Execution Notes:**
- [What happened during test]
- [Any unexpected behaviors]
- [Response times]

**Success Criteria Results:**
- [ ] Criterion 1
- [ ] Criterion 2
- [...]

**Quality Metrics:**
- Synthesis quality: X/5
- Insight value: X/5
- [Other metrics]: X/5

**Issues Found:**
1. [Issue description]
2. [Issue description]

**Recommendations:**
- [Improvements needed]
- [Follow-up actions]
```

---

## Appendix: Test Data Preparation

### A1: Microservices Example
- **Location:** `test-data/microservices-ecommerce/`
- **Services:** Orders, Inventory, Payments, Notifications, Users
- **Size:** ~2k LOC per service
- **Include:** API contracts, service boundaries, deployment config

### A2: Security-Critical Code
- **Location:** `test-data/security/authentication/`
- **Contents:** JWT auth, OAuth2 flow, session management
- **Planted vulnerabilities:** For vulnerability detection tests

### A3: Performance Test Case
- **Location:** `test-data/performance/slow-endpoint/`
- **Contents:** API endpoint with N+1 queries, inefficient caching
- **Profiling data:** Response times, query logs

### A4: Large Codebase
- **Location:** `test-data/large-monorepo/`
- **Size:** 50-60k LOC
- **Structure:** Multiple modules, services, shared libraries

### A5: Multimodal Assets
- **Location:** `test-data/multimodal/`
- **Contents:**
  - Architecture diagrams (PNG, SVG)
  - API specifications (PDF)
  - Design mockups (PNG)
  - Wireframes (PDF)

---

**End of Test Plan**
