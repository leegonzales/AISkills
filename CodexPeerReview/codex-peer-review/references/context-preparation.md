# Context Preparation Guide

Effective peer review depends on providing Codex with clear, focused context. This guide covers what to include, how to frame questions, and how to set appropriate expectations.

---

## Principles of Effective Context

### 1. Specificity Over Completeness

**Good context is focused:**
- Target the specific decision or code area
- Include only relevant information
- Avoid information overload

**Bad context is comprehensive:**
- Dumps entire codebase
- Includes tangential information
- Overwhelms with unnecessary detail

### 2. Context Hierarchy

**Essential (always include):**
- The specific question or decision point
- Relevant code or architecture description
- Key constraints (technical, business, time)
- Expected output format

**Important (include when relevant):**
- Project type and purpose
- Technology stack
- Team expertise level
- Performance/scale requirements
- Security/compliance requirements

**Optional (include if directly relevant):**
- Historical context
- Previous decisions
- Organizational constraints
- User feedback or requirements

---

## Context Template Structure

### Basic Template

```
[CONTEXT]
Project: [type, purpose, scale]
Technology: [stack, frameworks]
Team: [size, expertise level]
Constraints: [technical, business, time]

[SITUATION]
[What exists now or what's being proposed]

[CODE/ARCHITECTURE]
[Relevant code, architecture description, or diagram]

[QUESTION]
[Specific question or review request]

[CRITERIA]
[What factors matter most: performance, maintainability, security, etc.]

[EXPECTED OUTPUT]
[Format: analysis, alternatives, recommendations, risk assessment, etc.]
```

### Architecture Review Template

```
[ARCHITECTURE REVIEW REQUEST]

System Purpose: [What the system does]
Scale: [Expected users, data volume, transaction rate]
Current Stage: [Greenfield / Existing system / Refactoring]

Key Components:
- [Component 1: purpose, technology]
- [Component 2: purpose, technology]
- [Component 3: purpose, technology]

Architecture Diagram: [Description or attached image]

Key Design Decisions:
1. [Decision 1: what and why]
2. [Decision 2: what and why]
3. [Decision 3: what and why]

Specific Concerns:
- [Concern 1: scalability, complexity, etc.]
- [Concern 2]
- [Concern 3]

Review Focus:
Please analyze:
- Service boundaries and cohesion
- Data consistency approach
- Scalability bottlenecks
- Operational complexity
- Alternative approaches

Expected Output: Risk assessment and improvement recommendations
```

### Design Decision Template

```
[DESIGN DECISION VALIDATION]

Decision Point: [What needs to be decided]

Context:
- System: [relevant system or feature]
- Requirements: [functional and non-functional]
- Constraints: [technical, business, time]
- Team expertise: [relevant skills and gaps]

Options Under Consideration:

Option A: [Name]
- Approach: [How it works]
- Pros: [Advantages]
- Cons: [Disadvantages]
- Complexity: [Implementation and operational]

Option B: [Name]
- Approach: [How it works]
- Pros: [Advantages]
- Cons: [Disadvantages]
- Complexity: [Implementation and operational]

Option C: [Name] (if applicable)
- Approach: [How it works]
- Pros: [Advantages]
- Cons: [Disadvantages]
- Complexity: [Implementation and operational]

Evaluation Criteria (in priority order):
1. [Criterion 1: e.g., maintainability]
2. [Criterion 2: e.g., performance]
3. [Criterion 3: e.g., time to implement]

Question: Which option is recommended given these criteria? What trade-offs are most significant?

Expected Output: Comparative analysis and recommendation with rationale
```

### Security Review Template

```
[SECURITY REVIEW REQUEST]

Code Purpose: [What this code does]
Sensitivity: [Data handled, access level, compliance requirements]
Threat Model: [Known threats or attack vectors]

Code for Review:
```
[relevant security-critical code]
```

Security Concerns:
- [Concern 1: authentication, authorization, etc.]
- [Concern 2: injection, XSS, etc.]
- [Concern 3: data exposure, etc.]

Compliance Requirements:
- [GDPR, HIPAA, SOC2, etc. if applicable]

Review Focus:
- Vulnerability identification
- Attack vector analysis
- Security hardening opportunities
- Best practice compliance

Expected Output: Prioritized security issues and remediation recommendations
```

### Performance Analysis Template

```
[PERFORMANCE ANALYSIS REQUEST]

System Context: [What this code does in the larger system]
Current Performance: [Observed metrics: latency, throughput, etc.]
Performance Requirements: [Target metrics]
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
- [Time/budget constraints]

Analysis Focus:
- Bottleneck identification
- Optimization opportunities
- Algorithmic improvements
- Caching strategies
- Trade-offs in optimization approaches

Expected Output: Prioritized optimization recommendations with complexity/impact assessment
```

### Testing Strategy Template

```
[TESTING STRATEGY REVIEW]

Code/Feature Under Test: [What's being tested]
Current Test Coverage: [Percentage, what's covered]
Test Types: [Unit, integration, e2e currently used]

Code Structure:
```
[relevant code structure]
```

Current Tests:
```
[sample of existing tests]
```

Testing Concerns:
- [Concern 1: coverage gaps, brittle tests, etc.]
- [Concern 2: missing edge cases]
- [Concern 3: test maintainability]

Review Focus:
- Coverage gap identification
- Edge case discovery
- Test strategy improvements
- Test maintainability
- Alternative testing approaches

Expected Output: Testing improvement plan with prioritized recommendations
```

### Learning/Code Review Template

```
[CODE REVIEW FOR LEARNING]

Code Context: [Where this code comes from, what it does]
Learning Goal: [What you want to understand]

Code for Review:
```
[code to understand]
```

Specific Questions:
1. [Question 1: What pattern is being used here?]
2. [Question 2: Why this approach vs alternatives?]
3. [Question 3: Are there concerns or improvements?]

Background:
- [Your familiarity with the domain/technology]
- [What's unclear or confusing]
- [What you've tried to understand it]

Expected Output: Clear explanation of patterns, design decisions, and potential concerns
```

---

## Framing Effective Questions

### Question Quality Spectrum

**Excellent questions (specific, actionable):**
- "Review this microservices architecture. Are service boundaries well-defined considering domain-driven design principles? Any data consistency concerns with the eventual consistency approach?"
- "Compare these three caching strategies (Redis, in-memory LRU, CDN) for our image serving use case. Consider memory overhead, cache invalidation complexity, and cold-start performance."
- "Security review this JWT authentication flow. Focus on token expiration, refresh token handling, and session management. Are there timing attack vulnerabilities?"

**Good questions (clear focus, could be more specific):**
- "Is this architecture scalable?"
  - Better: "Will this architecture scale to 10K concurrent users with sub-100ms latency? What bottlenecks exist?"
- "Review this code for performance"
  - Better: "Identify performance bottlenecks in this query handler that currently takes 500ms. Focus on N+1 queries and database indexing."

**Poor questions (vague, unanswerable):**
- "Is this code good?" → What aspect? What criteria?
- "What do you think?" → About what specifically?
- "Review everything" → Too broad, no focus
- "Any issues?" → What kind of issues matter?

### Question Framing Patterns

**For architecture review:**
```
Review [system/component] architecture focusing on [specific concerns].

Context: [scale, requirements, constraints]
Key decisions: [decision 1], [decision 2], [decision 3]

Specific questions:
- Are [concern 1: service boundaries, data consistency, etc.] well-handled?
- What risks exist for [concern 2: scalability, reliability, etc.]?
- Are there better alternatives for [specific architectural choice]?
```

**For design decisions:**
```
Compare [approach A] vs [approach B] for [specific use case].

Context: [requirements, constraints]
Evaluation criteria: [criterion 1], [criterion 2], [criterion 3]

Which approach is preferable considering these criteria?
What are the most significant trade-offs?
```

**For security review:**
```
Security review [component] focusing on [specific threats/concerns].

Code: [relevant security-critical code]
Threats: [threat 1], [threat 2], [threat 3]
Compliance: [any requirements]

Questions:
- Are there vulnerabilities in [specific area]?
- How could an attacker exploit [attack vector]?
- What hardening opportunities exist?
```

**For performance:**
```
Analyze performance of [component] with current metrics [current performance].

Target: [performance requirements]
Scale: [expected load]

Questions:
- What are the bottlenecks?
- What optimization approaches are most impactful?
- What are trade-offs in optimization strategies?
```

---

## Code Extraction Strategies

### What to Include

**Include:**
- Code directly relevant to the question
- Interfaces/contracts the code depends on
- Key data structures
- Critical dependencies
- Configuration relevant to behavior

**Exclude:**
- Boilerplate or scaffolding
- Unrelated features
- Most test code (unless reviewing tests)
- Build configuration (unless relevant)
- Large chunks of third-party code

### Code Context Size Guidelines

**For focused review (recommended):**
- 50-200 lines of core code
- Key interfaces and types
- Critical dependencies
- Total context: 200-500 lines

**For broader review (when necessary):**
- Multiple files showing system structure
- Key architectural components
- Total context: 500-1000 lines

**Avoid:**
- Entire file dumps (unless file is small)
- Multiple unrelated files
- Context over 1000 lines (too much to analyze effectively)

### Providing File Structure

**When reviewing architecture, include file structure:**
```
project/
├── src/
│   ├── api/
│   │   ├── handlers/
│   │   ├── middleware/
│   │   └── routes.ts
│   ├── services/
│   │   ├── user-service.ts
│   │   ├── order-service.ts
│   │   └── payment-service.ts
│   ├── data/
│   │   ├── repositories/
│   │   └── models/
│   └── shared/
│       ├── errors.ts
│       └── types.ts
└── tests/

Key files for review:
- src/api/handlers/order-handler.ts (order processing logic)
- src/services/order-service.ts (business logic)
- src/data/repositories/order-repo.ts (data access)
```

---

## Setting Output Expectations

### Output Format Options

**Analysis format:**
- Structured assessment of concerns
- Risk identification
- Trade-off analysis
- Confidence levels

**Recommendation format:**
- Clear recommendation with rationale
- Alternative approaches
- Implementation considerations
- Risk mitigation strategies

**Comparative format:**
- Side-by-side comparison
- Scoring against criteria
- Trade-off matrix
- Decision framework

**Risk assessment format:**
- Identified risks with severity
- Likelihood assessment
- Mitigation strategies
- Prioritization

### Expectation Examples

**Good expectations:**
- "Provide risk assessment with severity levels and mitigation strategies"
- "Compare options using these criteria and recommend one with rationale"
- "Identify 3-5 key architectural concerns and suggest improvements"
- "List vulnerabilities by severity with specific remediation steps"

**Poor expectations:**
- "Tell me what's wrong" → Too vague
- "Make it perfect" → Unrealistic
- "Give me the answer" → No structure requested

---

## Context Size Management

### When Context is Too Large

**Problem:** Question requires too much context to be practical

**Solutions:**

1. **Break into smaller questions**
   - Review architecture → Review each component separately
   - Broad security review → Focus on authentication, then authorization, then data handling

2. **Use abstraction**
   - Provide interface/API definitions instead of implementations
   - Show architectural diagram instead of all code
   - Describe components at high level

3. **Focus on decision point**
   - Identify the specific decision that matters
   - Provide only context relevant to that decision
   - Reference broader context without including it all

4. **Iterative review**
   - Start with high-level review
   - Drill into specific concerns in follow-up
   - Build context progressively

### When Context is Too Small

**Problem:** Codex doesn't have enough information to provide useful analysis

**Indicators:**
- Response asks for clarification
- Analysis is too generic
- Misunderstands the question
- Can't address specific concerns

**Solutions:**
1. Add constraint information
2. Include relevant interfaces/types
3. Provide more background on requirements
4. Clarify the specific question
5. Add examples or use cases

---

## Context Preparation Checklist

Before invoking Codex peer review, verify:

**Question:**
- [ ] Question is specific and answerable
- [ ] Clear what type of response is needed
- [ ] Focused on one decision/concern
- [ ] Not too broad or vague

**Code/Architecture:**
- [ ] Relevant code/description included
- [ ] Not too much context (under 1000 lines)
- [ ] Not too little context (enough to understand)
- [ ] Key interfaces and dependencies included

**Background:**
- [ ] Project type and purpose stated
- [ ] Key constraints identified
- [ ] Scale/performance requirements noted
- [ ] Technology stack mentioned

**Criteria:**
- [ ] Evaluation criteria specified
- [ ] Priorities indicated
- [ ] Trade-offs to consider identified

**Output:**
- [ ] Expected format specified
- [ ] Level of detail indicated
- [ ] Type of analysis requested (risk, comparison, recommendation, etc.)

---

## Common Context Preparation Mistakes

### Mistake 1: Information Overload

**Problem:** Dumping entire codebase or overly comprehensive context

**Impact:** Dilutes focus, analysis becomes generic, misses specific concerns

**Fix:** Extract only relevant code/architecture for the specific question

---

### Mistake 2: Missing Constraints

**Problem:** Not specifying technical, business, or time constraints

**Impact:** Recommendations may be impractical or miss important trade-offs

**Fix:** Always include key constraints and limitations

---

### Mistake 3: Vague Questions

**Problem:** "Is this good?" or "Any issues?" without specificity

**Impact:** Generic, unhelpful responses

**Fix:** Frame specific, answerable questions with clear focus

---

### Mistake 4: No Evaluation Criteria

**Problem:** Asking "which approach is better" without specifying what "better" means

**Impact:** Codex can't prioritize trade-offs appropriately

**Fix:** Specify criteria and their relative importance

---

### Mistake 5: Unclear Output Expectations

**Problem:** Not specifying what format or type of response is needed

**Impact:** Response may not be structured usefully

**Fix:** State expected output format (analysis, recommendation, comparison, etc.)

---

## Context Refinement Process

If initial peer review isn't satisfactory:

1. **Assess the response:**
   - Too vague? → Add more specific questions
   - Misunderstood? → Clarify context
   - Too generic? → Add constraints and criteria
   - Off-target? → Refocus the question

2. **Refine context:**
   - Add missing information
   - Clarify ambiguities
   - Narrow or broaden scope as needed
   - Reframe question more specifically

3. **Retry once:**
   - One refinement iteration is usually sufficient
   - If still unsatisfactory, may not be good use case for peer review

---

## Examples of Well-Prepared Context

### Example 1: Architecture Review

```
[ARCHITECTURE REVIEW: Multi-Tenant SaaS Platform]

System Purpose: B2B project management SaaS
Scale: 100-500 tenant organizations, 50-5K users per tenant
Stage: Greenfield design

Key Components:
- API Gateway (Kong) → routes requests, enforces rate limits
- Application Layer (Node.js) → business logic, multi-tenant aware
- Database Layer (PostgreSQL) → stores tenant data
- Cache Layer (Redis) → sessions, frequently accessed data
- Background Jobs (BullMQ) → async processing, reports

Design Decision: Database Multi-Tenancy Strategy

Option A: Shared database with row-level security (RLS)
- Single PostgreSQL instance
- tenant_id column on all tables
- Row-level security policies enforce tenant isolation
- Shared connection pool

Option B: Separate database per tenant
- PostgreSQL database created per tenant
- Complete data isolation at DB level
- Connection pooling per tenant
- Database provisioning automation required

Context:
- Strong data isolation requirements (handling sensitive project data)
- Variable tenant sizes (some very small, some very large)
- Team is experienced with PostgreSQL, less with RLS
- Cloud deployment on AWS RDS

Concerns:
- Data isolation security
- Operational complexity
- Query performance at scale
- Cost at 100-500 tenants
- Migration and backup complexity

Question:
Which multi-tenancy approach is recommended for this context?
Analyze trade-offs for security, scalability, operational complexity, and cost.
Are there hybrid approaches worth considering?

Expected Output: Risk assessment for each approach, recommendation with rationale, and implementation considerations
```

### Example 2: Security Review

```
[SECURITY REVIEW: JWT Authentication Implementation]

System: REST API for financial data aggregation
Sensitivity: OAuth tokens, financial account credentials, PII
Compliance: SOC2, PCI DSS requirements

Authentication Flow:
1. User logs in with email/password
2. Server validates credentials
3. Server issues JWT access token (15min expiry) + refresh token (7 day expiry)
4. Client includes access token in Authorization header
5. On expiry, client uses refresh token to get new access token

Implementation:
```typescript
// Token generation
function generateTokens(userId: string) {
  const accessToken = jwt.sign(
    { userId, type: 'access' },
    process.env.JWT_SECRET,
    { expiresIn: '15m' }
  );

  const refreshToken = jwt.sign(
    { userId, type: 'refresh' },
    process.env.REFRESH_SECRET,
    { expiresIn: '7d' }
  );

  // Store refresh token in database
  await db.refreshTokens.insert({
    userId,
    token: refreshToken,
    expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
  });

  return { accessToken, refreshToken };
}

// Token validation middleware
async function validateToken(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];

  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.userId = decoded.userId;
    next();
  } catch (error) {
    return res.status(401).json({ error: 'Invalid token' });
  }
}

// Refresh token endpoint
async function refreshAccessToken(req, res) {
  const { refreshToken } = req.body;

  const decoded = jwt.verify(refreshToken, process.env.REFRESH_SECRET);

  // Verify token exists in database
  const storedToken = await db.refreshTokens.findOne({
    userId: decoded.userId,
    token: refreshToken
  });

  if (!storedToken) {
    return res.status(401).json({ error: 'Invalid refresh token' });
  }

  // Generate new access token
  const accessToken = jwt.sign(
    { userId: decoded.userId, type: 'access' },
    process.env.JWT_SECRET,
    { expiresIn: '15m' }
  );

  return res.json({ accessToken });
}
```

Specific Security Concerns:
- Token storage (refresh tokens in database, access tokens in memory/localStorage)
- Refresh token rotation and revocation
- Secret key management
- Timing attacks on token validation
- Token expiry and cleanup
- Session fixation or hijacking risks

Question:
Identify security vulnerabilities in this authentication implementation.
Focus on:
- Token handling and storage
- Refresh token security
- Session management
- Timing attacks or information leakage
- Best practice compliance for financial systems

Expected Output: Prioritized vulnerabilities with severity levels, specific attack vectors, and remediation recommendations
```

These examples show well-prepared context with clear questions, relevant code, specific concerns, and output expectations.
