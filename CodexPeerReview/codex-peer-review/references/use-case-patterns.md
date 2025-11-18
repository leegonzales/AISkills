# Use Case Patterns

Detailed patterns for common Codex peer review scenarios with examples, templates, and expected outcomes.

---

## Pattern 1: Architecture Review

### When to Use

**Triggers:**
- Designing new system or major feature
- Planning significant refactoring
- Before committing to architectural approach
- User says: "Review this architecture," "Is this design sound?"

**Value add:**
- Independent validation of architectural decisions
- Identification of scalability/reliability concerns
- Alternative approaches you might not have considered
- Risk assessment from different perspective

---

### Process

**1. Document Architecture**

Extract or create:
- System components and their responsibilities
- Data flow and dependencies
- Technology choices and why
- Scale requirements (users, data, throughput)
- Key architectural decisions

**2. Prepare Context**

Use template from `context-preparation.md`:
```markdown
[ARCHITECTURE REVIEW]

System Purpose: [What it does]
Scale: [Expected load, data volume]
Stage: [Greenfield/Existing/Refactor]

Components:
- [Component 1: role, technology]
- [Component 2: role, technology]
...

Key Decisions:
1. [Decision 1 and rationale]
2. [Decision 2 and rationale]

Concerns:
- [Concern 1: scalability, complexity, etc.]
- [Concern 2]

Question: Review for [specific aspects: scalability, maintainability, security, cost]

Expected Output: Risk assessment and improvement recommendations
```

**3. Invoke Codex**

```bash
codex exec --sandbox workspace-read "$(cat <<'EOF'
[prepared architecture context]
EOF
)"
```

**4. Synthesize**

Compare Claude's and Codex's architectural assessments:
- Where do both identify risks?
- What concerns does each uniquely raise?
- Are proposed alternatives viable?
- What trade-offs emerge?

**5. Present**

Integrated architecture assessment with:
- Risk matrix (high/medium/low concerns)
- Key trade-offs identified
- Recommendations for highest-impact improvements
- Alternative approaches worth considering

---

### Example

**Scenario:** Designing event-driven microservices architecture

**Claude's Initial Assessment:**
- Concerned about event ordering and eventual consistency
- Recommends saga pattern for distributed transactions
- Worried about operational complexity for team

**Codex's Peer Review:**
- Also identifies eventual consistency challenges
- Additionally raises concerns about event replay and idempotency
- Suggests event sourcing as alternative to sagas
- Points out monitoring and observability gaps

**Synthesis:**
```markdown
Both perspectives identify eventual consistency as the primary architectural challenge.

**Convergent Concerns:**
- Event ordering across services (both)
- Distributed transaction management (both)

**Complementary Insights:**
- Codex identifies idempotency as critical requirement not initially considered
- Claude emphasizes team operational capacity concerns
- Codex suggests event sourcing as alternative architectural pattern

**Recommendation:**
Implement saga pattern (lower complexity than event sourcing) BUT ensure:
1. All event handlers are idempotent (Codex's insight)
2. Comprehensive event replay capability (Codex's insight)
3. Team training on eventual consistency patterns (Claude's concern)
4. Strong monitoring and tracing (Codex's insight)

**Risk Mitigation:**
Start with synchronous calls for critical paths, evolve to events for non-critical paths. Reduces initial complexity while building team capability.
```

---

## Pattern 2: Design Decision Validation

### When to Use

**Triggers:**
- Choosing between multiple implementation approaches
- Significant technical decision with trade-offs
- Unclear which approach is superior
- User says: "Which approach should I use?" "Compare A vs B"

**Value add:**
- Structured comparison from two AI perspectives
- Trade-off analysis
- Identification of factors you might not have considered
- Validation or challenge of initial preference

---

### Process

**1. Document Decision Point**

Clearly articulate:
- What needs to be decided
- Why it matters
- Options being considered
- Current context and constraints

**2. Structure Options**

For each option, document:
- How it works
- Advantages
- Disadvantages
- Implementation complexity
- Operational complexity
- Risks

**3. Define Evaluation Criteria**

Explicitly prioritize factors:
1. [Most important criterion]
2. [Second most important]
3. [Third most important]

**4. Prepare Context**

```markdown
[DESIGN DECISION]

Decision: [What needs to be decided]

Context:
- System: [Relevant system/feature]
- Requirements: [Functional and non-functional]
- Constraints: [Technical, business, time]
- Team expertise: [Relevant capabilities]

Option A: [Name]
- Approach: [How it works]
- Pros: [List]
- Cons: [List]
- Complexity: [Assessment]

Option B: [Name]
- Approach: [How it works]
- Pros: [List]
- Cons: [List]
- Complexity: [Assessment]

Evaluation Criteria (priority order):
1. [Criterion 1]
2. [Criterion 2]
3. [Criterion 3]

Question: Which option is recommended? What are most significant trade-offs?

Expected Output: Comparative analysis and recommendation with rationale
```

**5. Invoke Codex**

```bash
codex exec "$(cat <<'EOF'
[prepared decision context]
EOF
)"
```

**6. Build Trade-off Matrix**

Use synthesis framework to create comparison table:
- Score each option against criteria
- Identify where perspectives agree/disagree
- Make trade-offs explicit

**7. Present Decision Framework**

Give user:
- Clear comparison
- Recommendation with rationale
- Context-dependent guidance ("If X, choose A; if Y, choose B")
- Confidence level

---

### Example

**Scenario:** Choosing caching strategy for product catalog

**Options:**
- A: Redis with TTL-based invalidation
- B: Event-driven cache invalidation
- C: Hybrid approach

**Criteria:**
1. Data freshness (most important)
2. Implementation complexity
3. Query performance
4. Operational overhead

**Claude's Analysis:**
- Recommends Option A (Redis + TTL)
- Prioritizes implementation simplicity and team expertise
- Notes: Team knows Redis well, TTL is simple to implement
- Concern: Some stale data risk with TTL

**Codex's Analysis:**
- Recommends Option B (Event-driven)
- Prioritizes data freshness (#1 criterion)
- Notes: Events ensure cache is always current
- Concern: Higher implementation and operational complexity

**Synthesis:**
```markdown
## Trade-off Analysis

| Criterion | Redis+TTL (A) | Event-driven (B) | Hybrid (C) | Weight |
|-----------|---------------|------------------|------------|--------|
| Data Freshness | Medium | Excellent | Excellent | High |
| Implementation | Simple | Complex | Medium | Medium |
| Performance | Excellent | Excellent | Excellent | Medium |
| Operations | Simple | Complex | Medium | Medium |

**Divergence:**
- Claude prioritizes implementation simplicity (criterion #2)
- Codex prioritizes data freshness (criterion #1)

**Decision Framework:**

Given data freshness is the #1 criterion, **Codex's recommendation for event-driven invalidation is technically correct**.

However, Claude raises valid concern: can the team successfully implement and operate the more complex solution?

**Recommendation:**
- If data freshness is non-negotiable (e.g., pricing, inventory): Option B (Codex)
- If some staleness acceptable (e.g., product descriptions): Option A (Claude)
- If mixed requirements: **Option C (Hybrid)**
  - Event-driven for critical data (pricing, inventory)
  - TTL for less critical data (descriptions, images)
  - Balances freshness needs with implementation reality

**Confidence:** High on hybrid approach - it addresses both perspectives' concerns.
```

---

## Pattern 3: Security Review

### When to Use

**Triggers:**
- Security-critical code (authentication, authorization, payment, PII)
- Before deploying code handling sensitive data
- Compliance requirement (SOC2, HIPAA, PCI DSS)
- User says: "Security review," "Is this secure?" "What vulnerabilities exist?"

**Value add:**
- Identification of vulnerabilities from two perspectives
- Attack vector analysis
- Security best practices validation
- Prioritized remediation recommendations

---

### Process

**1. Extract Security-Critical Code**

Focus on:
- Authentication and authorization
- Input validation and sanitization
- Data encryption and storage
- Session management
- Secret handling
- API security

**2. Document Threat Model**

Identify:
- Assets being protected
- Potential attackers and capabilities
- Attack vectors of concern
- Compliance requirements

**3. Prepare Context**

```markdown
[SECURITY REVIEW]

Code Purpose: [What this does]
Sensitivity: [Data types, access level]
Threat Model: [Known threats, attack vectors]
Compliance: [Requirements if applicable]

Code for Review:
```
[security-critical code]
```

Specific Concerns:
- [Concern 1: auth, injection, etc.]
- [Concern 2]

Review Focus:
- Vulnerability identification
- Attack vector analysis
- Security hardening opportunities
- Best practice compliance

Expected Output: Prioritized vulnerabilities with severity and remediation steps
```

**4. Invoke Codex**

```bash
codex exec --sandbox none "$(cat <<'EOF'
[prepared security context]
EOF
)"
```

**5. Aggregate Vulnerabilities**

Combine findings from both AIs:
- List all identified vulnerabilities
- Note which AI identified each
- Assign severity (Critical/High/Medium/Low)
- Identify attack vectors

**6. Present Security Assessment**

Provide:
- Executive summary (critical issues count)
- Vulnerability table (severity, description, remediation)
- Attack vector analysis
- Prioritized remediation plan
- Long-term security improvements

---

### Example

**Scenario:** JWT authentication implementation review

**Claude's Findings:**
- Missing refresh token rotation
- No token revocation mechanism
- Tokens stored in localStorage (XSS risk)
- No monitoring for suspicious token usage
- Missing rate limiting on auth endpoints

**Codex's Findings:**
- Refresh token race condition (multi-tab scenario)
- Timing-safe comparison not used (timing attacks)
- No token binding (CSRF potential)
- JWT secret in environment variable (key management concern)
- Missing token expiry cleanup in database

**Synthesis:**
```markdown
## Security Assessment: JWT Authentication

### Executive Summary
- **Critical Issues:** 2
- **High Issues:** 5
- **Medium Issues:** 3

Both Claude and Codex identified significant security gaps, particularly in refresh token handling and operational security.

### Vulnerabilities

| Severity | Issue | Identified By | Attack Vector |
|----------|-------|---------------|---------------|
| Critical | Refresh token race condition | Codex | Multi-tab token theft |
| Critical | Tokens in localStorage | Claude | XSS to token theft |
| High | No refresh token rotation | Both | Stolen tokens valid forever |
| High | No token revocation | Claude | Compromised accounts unrevocable |
| High | Timing attack vulnerability | Codex | Token brute force |
| High | Missing token binding | Codex | CSRF attacks |
| High | No rate limiting | Claude | Brute force attacks |
| Medium | JWT secret in env var | Codex | Key exposure risk |
| Medium | No token monitoring | Claude | Undetected breaches |
| Medium | No token cleanup | Codex | DB bloat + longer breach window |

### Complementary Insights

**Codex's Unique Findings:**
- Technical implementation bugs (race conditions, timing attacks)
- Low-level security details (token binding, timing-safe comparison)

**Claude's Unique Findings:**
- Operational security gaps (monitoring, revocation, rate limiting)
- Detection and response capabilities

**Combined Perspective:**
Both technical robustness (Codex) and operational maturity (Claude) are essential for production security.

### Prioritized Remediation Plan

**Phase 1: Critical Fixes (Block deployment until addressed)**
1. Store tokens in httpOnly cookies instead of localStorage (Claude)
2. Implement atomic refresh token rotation (Both)
3. Add distributed locking for refresh operations (Codex)
4. Use timing-safe comparison for tokens (Codex)

**Phase 2: High Priority (Before production traffic)**
5. Implement refresh token revocation mechanism (Claude)
6. Add token binding (CSRF tokens) (Codex)
7. Implement rate limiting on auth endpoints (Claude)
8. Move JWT secret to proper secret management (AWS Secrets Manager, etc.) (Codex)

**Phase 3: Operational Improvements (Before scale)**
9. Add token usage monitoring and alerting (Claude)
10. Implement automated token cleanup (Codex)
11. Build security audit dashboard (Claude)

### Long-term Security Improvements
- Implement anomaly detection for auth patterns
- Add security audit logging
- Set up automated security scanning
- Create incident response runbooks
- Schedule regular penetration testing

**Confidence:** High - Both perspectives independently identified overlapping critical issues, validating the severity assessment.
```

---

## Pattern 4: Performance Analysis

### When to Use

**Triggers:**
- Code not meeting performance requirements
- Optimization needed for performance-critical path
- Understanding performance bottlenecks
- User says: "Why is this slow?" "Optimize performance," "Find bottlenecks"

**Value add:**
- Bottleneck identification from two perspectives
- Optimization opportunities you might miss
- Algorithmic vs infrastructure optimizations
- Performance vs complexity trade-offs

---

### Process

**1. Define Performance Context**

Document:
- Current performance metrics (latency, throughput, resource usage)
- Target performance requirements
- Expected scale (load, data volume)
- Performance constraints

**2. Extract Performance-Critical Code**

Focus on:
- Database queries
- API calls and network I/O
- Computational algorithms
- Caching layers
- Data processing pipelines

**3. Identify Known Issues**

List:
- Observed bottlenecks
- Profiling results if available
- Suspected slow areas

**4. Prepare Context**

```markdown
[PERFORMANCE ANALYSIS]

System: [What this code does]
Current Performance: [Observed metrics]
Target Performance: [Requirements]
Scale: [Expected load, data volume]

Code for Analysis:
```
[performance-critical code]
```

Known Issues:
- [Issue 1: slow queries, N+1, etc.]
- [Issue 2]

Constraints:
- [Technology constraints]
- [Infrastructure constraints]

Analysis Focus:
- Bottleneck identification
- Optimization opportunities
- Algorithmic improvements
- Caching strategies

Expected Output: Prioritized optimizations with complexity/impact assessment
```

**5. Invoke Codex**

```bash
codex exec --sandbox workspace-read "$(cat <<'EOF'
[prepared performance context]
EOF
)"
```

**6. Build Optimization Matrix**

For each optimization:
- Estimated impact (% improvement)
- Implementation complexity
- Risk level
- Dependencies

**7. Present Performance Improvement Plan**

Provide:
- Bottleneck analysis
- Prioritized optimizations (impact vs complexity)
- Quick wins (high impact, low complexity)
- Long-term improvements
- Performance vs complexity trade-offs

---

### Example

**Scenario:** Slow API endpoint (500ms average, need 100ms)

**Claude's Analysis:**
- Identifies N+1 query problem (80% of latency)
- Missing database indexes on foreign keys
- Synchronous external API call blocking request
- Recommends: Eager loading, add indexes, async API calls

**Codex's Analysis:**
- Identifies same N+1 query problem (validates Claude)
- Additionally: Inefficient JSON serialization (10% of latency)
- Over-fetching data from database
- Missing query result caching
- Recommends: Eager loading, add indexes, caching layer, optimize serialization

**Synthesis:**
```markdown
## Performance Analysis: Order API Endpoint

### Current State
- Average: 500ms (Target: 100ms)
- p99: 2000ms (Target: 300ms)
- Bottleneck: Database access (90% of latency)

### Bottleneck Analysis

**Convergent Identification (High Confidence):**
Both Claude and Codex independently identified the N+1 query pattern as the primary bottleneck:
- Current: 1 query for order + N queries for items (N=10-50)
- Impact: 80-90% of observed latency
- Solution: Eager loading with joins

**Complementary Insights:**
- **Codex** additionally identified JSON serialization overhead (10% of latency)
- **Codex** noted over-fetching (selecting all columns when only 5 needed)
- **Codex** suggested query result caching for frequently accessed orders

### Optimization Plan

| Optimization | Impact | Complexity | Priority | Source |
|--------------|--------|------------|----------|--------|
| Fix N+1 with eager loading | 80% | Low | **P0** | Both |
| Add database indexes | 10% | Low | **P0** | Both |
| Async external API call | 5% | Medium | **P1** | Claude |
| Optimize JSON serialization | 5% | Low | **P1** | Codex |
| Select only needed columns | 2% | Low | **P1** | Codex |
| Add query result caching | 20%* | Medium | **P2** | Codex |

*Caching impact depends on access patterns (high if frequently accessed)

### Recommended Implementation Sequence

**Phase 1: Quick Wins (Target: 100ms)**
1. Implement eager loading for order items (80% improvement)
2. Add database indexes on foreign keys (10% improvement)
3. Optimize JSON serialization (5% improvement)

Expected result: 500ms → 75ms (meets target)

**Phase 2: Additional Improvements (Target: <50ms)**
4. Make external API call async (removes blocking)
5. Select only required columns (reduced data transfer)
6. Add Redis caching for frequent orders (for read-heavy workload)

Expected result: 75ms → <50ms (exceeds target with margin)

### Quick Win Analysis

P0 optimizations (eager loading + indexes) are:
- **Low complexity**: Standard ORM features
- **High impact**: 90% improvement
- **Low risk**: No architectural changes
- **Fast to implement**: 1-2 hours

**Recommendation:** Implement P0 first, measure results, then decide if P1/P2 needed.

### Trade-offs

**Caching (P2):**
- Pro: Significant improvement for read-heavy workload (Codex)
- Con: Adds infrastructure dependency and invalidation complexity
- Decision: Only implement if P0+P1 insufficient

**Async API call:**
- Pro: Removes blocking (Claude)
- Con: More complex error handling
- Decision: Implement in P2 after validating P0+P1 gains

### Confidence

**High** on P0 recommendations:
- Both AIs independently identified same bottlenecks
- Standard optimizations with proven impact
- Low risk, low complexity

**Medium** on P2 (caching):
- Depends on access patterns (not yet measured)
- Adds complexity (trade-off with operational overhead)
```

---

## Pattern 5: Testing Strategy Review

### When to Use

**Triggers:**
- Low test coverage or quality
- Missing test types (unit, integration, e2e)
- Brittle tests frequently breaking
- User says: "Improve testing," "What's missing?" "Test strategy review"

**Value add:**
- Identification of coverage gaps from two perspectives
- Test quality assessment
- Testing strategy improvements
- Edge cases you might not have considered

---

### Process

**1. Document Current Testing State**

Provide:
- Test coverage percentage
- Types of tests (unit, integration, e2e)
- Sample existing tests
- Known testing issues

**2. Identify Critical Paths**

What needs testing most:
- Business-critical functionality
- Complex logic
- Security-sensitive areas
- Frequently changing code

**3. Prepare Context**

```markdown
[TESTING STRATEGY REVIEW]

Code/Feature: [What's being tested]
Current Coverage: [Percentage, what's covered]
Test Types: [Unit, integration, e2e currently used]

Current Tests: [Sample or reference]

Testing Concerns:
- [Concern 1: coverage gaps, brittle tests, etc.]
- [Concern 2]

Review Focus:
- Coverage gap identification
- Edge case discovery
- Test strategy improvements
- Test maintainability

Expected Output: Testing improvement plan with prioritized recommendations
```

**4. Invoke Codex**

```bash
codex exec --sandbox workspace-read "$(cat <<'EOF'
[prepared testing context]
EOF
)"
```

**5. Aggregate Testing Improvements**

Combine recommendations:
- Coverage gaps identified
- Edge cases to add
- Test quality improvements
- Testing strategy suggestions

**6. Present Testing Improvement Plan**

Provide:
- Critical gaps to fill first
- Edge cases to add
- Test quality improvements
- Long-term testing strategy

---

### Example

**Scenario:** User authentication service with 60% coverage

**Claude's Findings:**
- Missing integration tests for full auth flow
- Edge cases: expired tokens, concurrent sessions, password reset
- No load testing for rate limiting
- Tests coupled to implementation (brittle)

**Codex's Findings:**
- Missing edge cases: token refresh race conditions, malformed JWT
- No property-based testing for token validation
- Missing negative test cases (invalid inputs)
- No testing for timing attack vulnerability

**Synthesis:**
```markdown
## Testing Strategy Review: User Authentication

### Current State
- Coverage: 60% (Target: 85%+)
- Tests: Unit tests only, no integration tests
- Issues: Brittle mocks, missing edge cases

### Coverage Gaps

**Critical Gaps (Both AIs):**
- No integration tests for end-to-end auth flow
- Missing edge cases for token expiration and refresh
- No testing for concurrent session handling

**Additional Gaps:**
- **Claude:** Load testing for rate limiting, password reset flow
- **Codex:** Property-based testing for token validation, timing attack testing

### Recommended Testing Improvements

**Phase 1: Critical Coverage (Block deployment)**
1. **Integration tests for auth flow** (Claude)
   - Login → Token issuance → API access → Refresh → Logout
   - Happy path and error paths

2. **Edge cases for token handling** (Both)
   - Expired access token → Refresh → Continue
   - Expired refresh token → Re-auth required
   - Concurrent token refresh (multi-tab) (Codex)
   - Malformed JWT tokens (Codex)

3. **Negative test cases** (Codex)
   - Invalid credentials
   - Missing tokens
   - Revoked tokens
   - Rate limit exceeded

**Phase 2: Quality Improvements**
4. **Refactor brittle tests** (Claude)
   - Test behavior, not implementation
   - Reduce coupling to internal structure
   - Use test fixtures for common scenarios

5. **Security-focused tests** (Codex)
   - Timing attack resistance for token validation
   - CSRF token validation
   - XSS protection in error messages

**Phase 3: Advanced Testing**
6. **Property-based testing** (Codex)
   - Generate random valid/invalid tokens
   - Test invariants (e.g., valid tokens always have userId)

7. **Load and performance testing** (Claude)
   - Rate limiting effectiveness under load
   - Token refresh performance with concurrent requests

### Test Cases to Add

**High Priority:**
```typescript
describe('Token Refresh', () => {
  it('should handle concurrent refresh requests', async () => {
    // Test multi-tab scenario (Codex's insight)
  });

  it('should reject expired refresh tokens', async () => {
    // Edge case (Both)
  });

  it('should handle malformed JWT gracefully', async () => {
    // Edge case (Codex)
  });
});

describe('Integration: Auth Flow', () => {
  it('should complete full authentication flow', async () => {
    // End-to-end test (Claude)
  });

  it('should enforce rate limiting', async () => {
    // Security test (Claude)
  });
});
```

### Testing Strategy Evolution

**Current (Unit-focused):**
- Unit tests: 100%
- Integration: 0%
- e2e: 0%

**Target (Balanced):**
- Unit tests: 70% (core logic, edge cases)
- Integration: 20% (critical flows)
- e2e: 10% (user journeys)

### Confidence

**High** on Phase 1 priorities:
- Both AIs independently identified integration testing gap
- Token edge cases validated by both perspectives
- Critical for production security

**Medium** on Phase 3 (advanced testing):
- Property-based testing valuable but not critical (Codex)
- Implement after Phase 1+2 complete
```

---

## Pattern 6: Code Review & Learning

### When to Use

**Triggers:**
- Exploring unfamiliar codebase
- Understanding complex algorithm or pattern
- Learning from existing code
- User says: "Explain this code," "How does this work?" "What pattern is this?"

**Value add:**
- Explanations from two AI perspectives
- Pattern identification
- Alternative approaches discussion
- Potential improvements identified

---

### Process

**1. Extract Code to Review**

Focus on:
- The specific code section of interest
- Surrounding context for understanding
- Related types/interfaces

**2. Formulate Learning Questions**

What do you want to understand:
- What pattern is being used?
- Why this approach vs alternatives?
- Are there potential issues?
- How could this be improved?

**3. Prepare Context**

```markdown
[CODE REVIEW FOR LEARNING]

Code Context: [Where this comes from, what it does]
Learning Goal: [What you want to understand]

Code for Review:
```
[code to understand]
```

Specific Questions:
1. [Question 1: What pattern is used here?]
2. [Question 2: Why this approach vs alternatives?]
3. [Question 3: Are there concerns or improvements?]

Background:
- [Your familiarity level]
- [What's unclear]

Expected Output: Clear explanation of patterns, design decisions, and potential concerns
```

**4. Invoke Codex**

```bash
codex exec "$(cat <<'EOF'
[prepared learning context]
EOF
)"
```

**5. Synthesize Explanations**

Combine both perspectives:
- Core explanation of what the code does
- Patterns and techniques used
- Why this approach (design rationale)
- Potential improvements or concerns
- Alternative approaches

**6. Present Learning Summary**

Provide:
- Clear explanation
- Pattern identification
- Design rationale
- Potential improvements
- Related concepts to explore

---

### Example

**Scenario:** Understanding complex recursive backtracking algorithm

**Claude's Explanation:**
- Pattern: Recursive backtracking with state accumulation
- Used for constraint satisfaction problems
- Design rationale: Explores solution space systematically
- Concern: Stack depth could cause issues with deep recursion
- Suggests: Iterative approach with explicit stack might be clearer

**Codex's Explanation:**
- Pattern: Depth-first search with pruning
- Classic algorithm design technique
- Design rationale: Pruning reduces search space
- Concern: No memoization of subproblems
- Suggests: Dynamic programming approach for overlapping subproblems

**Synthesis:**
```markdown
## Code Review: Recursive Backtracking Algorithm

### What This Code Does

This is a **recursive backtracking algorithm** (Claude) implementing **depth-first search with pruning** (Codex) to solve a constraint satisfaction problem.

### Pattern Identification

**Both AIs identify:**
- Recursive structure with base case and recursive case
- State accumulation through parameters
- Systematic exploration of solution space

**Complementary insights:**
- **Claude** emphasizes the backtracking aspect (undoing choices)
- **Codex** emphasizes the DFS + pruning optimization

### How It Works

1. **Base case:** Solution found or search space exhausted
2. **Recursive case:** Try each possible choice
3. **Pruning:** Skip branches that can't lead to valid solutions (Codex)
4. **Backtracking:** Undo choice and try next option (Claude)

This is a classic algorithm design technique for problems like:
- Sudoku solving
- N-Queens problem
- Path finding with constraints

### Design Rationale

**Why recursive approach:**
- Natural fit for tree-like search space
- Clean expression of backtracking logic
- Easy to reason about correctness

**Why pruning:**
- Dramatically reduces search space (Codex)
- Turns exponential into tractable (for many inputs)

### Potential Improvements

**Stack depth concern (Claude):**
- Deep recursion could overflow stack
- Consider iterative approach with explicit stack
- Relevant if input size is large

**Memoization opportunity (Codex):**
- If subproblems overlap, could use dynamic programming
- Cache results of subproblems to avoid recomputation
- Check if problem has optimal substructure property

**Performance optimization (Both):**
- Pruning could be more aggressive
- Consider heuristics to explore promising branches first

### Alternative Approaches

**Iterative with explicit stack (Claude):**
```python
def solve_iterative(problem):
    stack = [(initial_state, [])]
    while stack:
        state, path = stack.pop()
        if is_solution(state):
            return path
        for choice in get_choices(state):
            if is_valid(state, choice):
                new_state = apply_choice(state, choice)
                stack.append((new_state, path + [choice]))
```

**Dynamic programming (Codex):**
If subproblems overlap, consider DP:
```python
def solve_dp(problem):
    memo = {}
    def helper(state):
        if state in memo:
            return memo[state]
        # ... recursive logic with memoization
        result = ...
        memo[state] = result
        return result
```

### When to Use Each Approach

- **Recursive backtracking:** Clean, easy to understand, good for moderate depth
- **Iterative with stack:** Better for deep recursion, more control over memory
- **Dynamic programming:** When subproblems overlap significantly

### Related Concepts to Explore

- Branch and bound algorithms
- A* search with heuristics
- Constraint propagation
- Memoization and dynamic programming

### Confidence

**High** on pattern identification - both AIs independently recognized the core algorithm.

**Medium** on improvement recommendations - depends on specific problem characteristics (input size, subproblem overlap, etc.).
```

---

This completes the use case patterns. Each pattern provides a structured approach to common peer review scenarios with synthesis of Claude and Codex perspectives.
