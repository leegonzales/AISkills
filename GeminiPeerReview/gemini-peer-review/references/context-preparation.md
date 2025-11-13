# Context Preparation for Gemini Peer Review

Effective peer review depends on providing Gemini with clear, focused context. This guide covers what to include, how to frame questions, and how to leverage Gemini's unique capabilities for the best results.

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

### 3. Leverage Gemini's Strengths

**Massive Context Window (1M tokens):**
- Can process entire monorepos without chunking
- Include broader codebase context when needed
- Don't fear providing comprehensive file sets

**Multimodal Capabilities:**
- Include architecture diagrams as images
- Reference design mockups (PNG, JPG)
- Attach specification PDFs
- Screenshots of UI issues

**Google Search Grounding:**
- Ask about current best practices
- Request comparisons with latest frameworks
- Get real-time technology recommendations

---

## Domain-Specific Context Templates

### Template 1: Architecture Review

```
[ARCHITECTURE REVIEW REQUEST]

System Purpose: [What the system does]
Scale: [Expected users, data volume, transaction rate]
Current Stage: [Greenfield / Existing system / Refactoring]

Key Components:
- [Component 1: purpose, technology]
- [Component 2: purpose, technology]
- [Component 3: purpose, technology]

Architecture Diagram: [Attach image or describe]
@./architecture-diagram.png

Code Structure:
@./src/services/
@./src/api/

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
- Alternative approaches using current best practices

Expected Output: Risk assessment and improvement recommendations
```

**Gemini Advantage:** With 1M token context, include entire service directories without worrying about token limits. Attach architecture diagrams as images for visual analysis.

---

### Template 2: Design Decision

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

Additional Context:
- Search for current industry best practices in this area
- Consider frameworks/tools released in 2025

Question: Which option is recommended given these criteria? What trade-offs are most significant?

Expected Output: Comparative analysis and recommendation with rationale, including industry current practices
```

**Gemini Advantage:** Can search current best practices and latest framework releases to inform recommendations. Ask it to ground decisions in real-time information.

---

### Template 3: Security Review

```
[SECURITY REVIEW REQUEST]

Code Purpose: [What this code does]
Sensitivity: [Data handled, access level, compliance requirements]
Threat Model: [Known threats or attack vectors]

Code for Review:
@./src/auth/jwt-handler.ts
@./src/middleware/auth-middleware.ts

Security Concerns:
- [Concern 1: authentication, authorization, etc.]
- [Concern 2: injection, XSS, etc.]
- [Concern 3: data exposure, etc.]

Compliance Requirements:
- [GDPR, HIPAA, SOC2, PCI DSS, etc. if applicable]

Current Security Measures:
- [Existing protections]
- [Security tools in use]

Review Focus:
- Vulnerability identification
- Attack vector analysis
- Security hardening opportunities
- Best practice compliance (check against latest OWASP guidelines)
- Timing attack risks
- Data exposure paths

Expected Output: Prioritized security issues with severity levels and remediation recommendations
```

**Gemini Advantage:** Request latest OWASP guidelines and current security best practices. Gemini can search for recently discovered vulnerabilities in dependencies.

---

### Template 4: Performance Analysis

```
[PERFORMANCE ANALYSIS REQUEST]

System Context: [What this code does in the larger system]
Current Performance: [Observed metrics: latency, throughput, etc.]
Performance Requirements: [Target metrics]
Scale: [Expected load, data volume]

Code for Analysis:
@./src/api/query-handler.ts
@./src/database/repositories/

Profiling Data: [If available]
@./profiling-report.txt

Current Metrics:
- Latency: [current vs target]
- Throughput: [current vs target]
- Resource usage: [CPU, memory, database connections]

Known Issues:
- [Issue 1: slow queries, N+1, etc.]
- [Issue 2]

Constraints:
- Technology: [database, framework constraints]
- Infrastructure: [cloud provider, instance types]
- Budget: [cost considerations]

Analysis Focus:
- Bottleneck identification
- Optimization opportunities
- Algorithmic improvements
- Caching strategies
- Database query optimization
- Trade-offs in optimization approaches

Additional Request:
- Search for current performance optimization techniques for [technology stack]
- Compare with industry benchmarks

Expected Output: Prioritized optimization recommendations with complexity/impact assessment
```

**Gemini Advantage:** Can analyze large profiling outputs and search for current optimization techniques specific to your stack.

---

### Template 5: Testing Strategy

```
[TESTING STRATEGY REVIEW]

Code/Feature Under Test: [What's being tested]
Current Test Coverage: [Percentage, what's covered]
Test Types: [Unit, integration, e2e currently used]

Code Structure:
@./src/features/payment-processing/
@./tests/payment-processing/

Current Tests:
@./tests/unit/payment-handler.test.ts
@./tests/integration/checkout-flow.test.ts

Testing Concerns:
- [Concern 1: coverage gaps, brittle tests, etc.]
- [Concern 2: missing edge cases]
- [Concern 3: test maintainability]
- [Concern 4: slow test execution]

Testing Infrastructure:
- Framework: [Jest, Pytest, etc.]
- CI/CD: [GitHub Actions, etc.]
- Test data: [fixtures, factories, etc.]

Review Focus:
- Coverage gap identification
- Edge case discovery
- Test strategy improvements
- Test maintainability
- Alternative testing approaches
- Modern testing patterns for [framework]

Additional Request:
- Search for current testing best practices in [language/framework]
- Recommend modern testing tools if applicable

Expected Output: Testing improvement plan with prioritized recommendations
```

**Gemini Advantage:** With large context window, can analyze entire test suites and production code together. Can search for latest testing frameworks and patterns.

---

### Template 6: Code Review & Learning

```
[CODE REVIEW FOR LEARNING]

Code Context: [Where this code comes from, what it does]
Learning Goal: [What you want to understand]

Code for Review:
@./src/advanced-feature/
@./lib/custom-implementation.ts

Specific Questions:
1. [Question 1: What pattern is being used here?]
2. [Question 2: Why this approach vs alternatives?]
3. [Question 3: Are there concerns or improvements?]
4. [Question 4: What are modern alternatives?]

Background:
- My familiarity: [Your level with the domain/technology]
- What's unclear: [Specific confusing parts]
- What I've tried: [Previous attempts to understand]

Visual Aids (if applicable):
@./flow-diagram.png
@./class-structure.png

Additional Request:
- Explain in terms accessible to someone with [experience level]
- Search for tutorial resources on this pattern
- Compare with how this is typically done in [current year]

Expected Output: Clear explanation of patterns, design decisions, potential concerns, and modern alternatives
```

**Gemini Advantage:** Multimodal capability means you can include diagrams you've sketched. Can search for current tutorials and documentation.

---

### Template 7: Refactoring Review

```
[REFACTORING REVIEW REQUEST]

Refactoring Goal: [What you're trying to improve]
Current Issues: [Technical debt, complexity, performance, etc.]

Before Code:
@./src/legacy/old-implementation.js

Proposed Refactoring:
@./src/refactored/new-implementation.ts

Refactoring Approach:
- [Change 1: pattern used, rationale]
- [Change 2: pattern used, rationale]
- [Change 3: pattern used, rationale]

Constraints:
- Backward compatibility: [requirements]
- Migration strategy: [how to transition]
- Risk tolerance: [how much change is acceptable]

Review Focus:
- Does refactoring achieve goals?
- Are there unintended consequences?
- Better refactoring approaches?
- Risk assessment
- Migration path validation
- Modern patterns applicable

Additional Request:
- Check against current best practices for [language/framework]
- Suggest modern alternatives if this approach is outdated

Expected Output: Assessment of refactoring approach, identified risks, alternative suggestions
```

**Gemini Advantage:** Can compare old and new implementations with full context, search for current refactoring patterns, and suggest modern alternatives.

---

## Framing Effective Questions

### Question Quality Spectrum

**Excellent questions (specific, actionable):**
- "Review this microservices architecture @./architecture.png. Are service boundaries well-defined considering domain-driven design principles? Check against current DDD best practices."
- "Compare these three caching strategies @./cache-redis.ts @./cache-memory.ts @./cache-cdn.ts for our image serving use case. Consider memory overhead, cache invalidation, and cold-start performance. Search for latest caching patterns."
- "Security review this JWT flow @./auth/jwt.ts. Focus on token expiration, refresh handling, session management. Check against latest OWASP JWT guidelines."

**Good questions (clear focus, could be more specific):**
- "Is this architecture scalable?"
  - Better: "Will this architecture @./services/ scale to 10K concurrent users with sub-100ms latency? What bottlenecks exist?"

- "Review this code for performance"
  - Better: "Identify performance bottlenecks in @./query-handler.ts that currently takes 500ms. Focus on N+1 queries and database indexing."

**Poor questions (vague, unanswerable):**
- "Is this code good?" → What aspect? What criteria?
- "What do you think?" → About what specifically?
- "Review everything" → Too broad, no focus
- "Any issues?" → What kind of issues matter?

### Question Framing Patterns

**For architecture review:**
```
Review this architecture focusing on [specific concerns].

Context: [scale, requirements, constraints]
Architecture: @./architecture-diagram.png
Code: @./src/services/

Key decisions: [decision 1], [decision 2], [decision 3]

Specific questions:
- Are [concern 1: service boundaries, data consistency, etc.] well-handled?
- What risks exist for [concern 2: scalability, reliability, etc.]?
- What are current industry best practices for [architectural choice]?
- Are there better alternatives using modern approaches?
```

**For design decisions:**
```
Compare these approaches for [specific use case].

Context: [requirements, constraints]
Option A: @./approach-a/
Option B: @./approach-b/

Evaluation criteria: [criterion 1], [criterion 2], [criterion 3]

Which approach is preferable considering:
- These criteria
- Current best practices
- Latest framework capabilities

What are the most significant trade-offs?
```

**For security review:**
```
Security review [component] focusing on [specific threats].

Code: @./security-critical/
Threats: [threat 1], [threat 2], [threat 3]
Compliance: [requirements]

Questions:
- Are there vulnerabilities in [specific area]?
- How could an attacker exploit [attack vector]?
- What hardening opportunities exist?
- Does this comply with latest [OWASP/other] guidelines?
```

**For performance:**
```
Analyze performance of [component].

Current metrics: [performance data]
Target: [performance requirements]
Scale: [expected load]

Code: @./performance-critical/
Profiling: @./profile-output.txt

Questions:
- What are the bottlenecks?
- What optimization approaches are most impactful?
- What are current best practices for optimizing [specific operation]?
- Trade-offs in optimization strategies?
```

**For learning:**
```
Explain [code/pattern] in terms accessible to [experience level].

Code: @./complex-implementation/
Diagrams: @./flow-chart.png

Background: [what you know, what's confusing]

Questions:
- What pattern is being used and why?
- How does this compare to standard approaches?
- What are modern alternatives?
- Where can I learn more? (search for resources)
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
- Related test files (when reviewing tests)

**Exclude:**
- Boilerplate or scaffolding
- Unrelated features
- Build configuration (unless relevant)
- Most vendor code
- Generated files

### Code Context Size Guidelines

**For focused review (recommended):**
- Core code: 50-500 lines
- Supporting interfaces/types
- Critical dependencies
- Total: 500-2000 lines

**For broader review (Gemini advantage):**
- Multiple related modules
- Entire feature directories
- Full service implementations
- Total: 2000-10,000 lines
- **Gemini can handle up to 1M tokens** - don't fear large contexts

**For comprehensive codebase review (unique to Gemini):**
- Entire microservice codebases
- Multiple related services
- Full architecture review
- Total: 10,000-100,000+ lines
- **Only Gemini's 1M context makes this practical**

### Providing File Structure

**When reviewing architecture:**
```
Project Structure:
@./README.md

src/
├── api/
│   ├── handlers/
│   │   @./src/api/handlers/
│   ├── middleware/
│   │   @./src/api/middleware/
│   └── routes.ts
│       @./src/api/routes.ts
├── services/
│   @./src/services/
├── data/
│   @./src/data/
└── shared/
    @./src/shared/

Architecture: @./docs/architecture.png

Key files for review:
- Order processing: @./src/api/handlers/order-handler.ts
- Business logic: @./src/services/order-service.ts
- Data access: @./src/data/repositories/order-repo.ts
```

### Including Visual Assets

**Architecture diagrams:**
```
System Architecture: @./docs/architecture-diagram.png
Database Schema: @./docs/database-erd.png
Sequence Flow: @./docs/auth-sequence.png
```

**UI/Design review:**
```
Current UI: @./screenshots/current-ui.png
Proposed Design: @./designs/new-mockup.png
User Flow: @./designs/user-journey.pdf
```

**Performance data:**
```
Profiling Output: @./profiling/flame-graph.png
Metrics Dashboard: @./monitoring/performance-screenshot.png
```

---

## Setting Output Expectations

### Output Format Options

**Analysis format:**
- Structured assessment of concerns
- Risk identification
- Trade-off analysis
- Confidence levels
- Current industry practices

**Recommendation format:**
- Clear recommendation with rationale
- Alternative approaches
- Implementation considerations
- Risk mitigation strategies
- Modern alternatives

**Comparative format:**
- Side-by-side comparison
- Scoring against criteria
- Trade-off matrix
- Decision framework
- Industry benchmark comparison

**Risk assessment format:**
- Identified risks with severity
- Likelihood assessment
- Mitigation strategies
- Prioritization

**Educational format:**
- Clear explanations
- Pattern identification
- Best practice examples
- Learning resources (via search)
- Progressive complexity

### Expectation Examples

**Good expectations:**
- "Provide risk assessment with severity levels and mitigation strategies"
- "Compare options using these criteria and recommend one with rationale grounded in current best practices"
- "Identify 3-5 key architectural concerns and suggest modern improvements"
- "List vulnerabilities by severity with specific remediation steps per latest OWASP guidelines"
- "Explain this pattern and search for tutorial resources"

**Enhanced with Gemini capabilities:**
- "Compare against current industry benchmarks (search for latest data)"
- "Recommend modern alternatives using frameworks released in 2024-2025"
- "Check security approach against latest OWASP/NIST guidelines"
- "Suggest optimization techniques used in recent performance studies"

**Poor expectations:**
- "Tell me what's wrong" → Too vague
- "Make it perfect" → Unrealistic
- "Give me the answer" → No structure requested

---

## Context Size Management

### Gemini's Advantage: 1M Token Context Window

**Practical capacity:**
- ~750,000 words of text
- Entire medium-sized codebases
- Full monorepo analysis
- Comprehensive documentation sets
- Multiple large files simultaneously

**What this means:**
- Less need to chunk large codebases
- Can include entire feature directories
- Analyze cross-service dependencies
- Review complete system architecture
- Include extensive documentation

### When to Still Be Strategic

Even with 1M tokens, focused context yields better results:

**1. Overly broad questions**
- Problem: "Review my entire company's codebase for issues"
- Solution: Focus on specific concerns even if you include large context
- Better: "Review authentication implementation across all services @./services/ focusing on security vulnerabilities"

**2. Irrelevant context**
- Problem: Including unrelated code "just in case"
- Solution: Be selective about what supports your question
- Include comprehensive relevant context, exclude irrelevant code

**3. No clear focus**
- Problem: Large context without specific questions
- Solution: Large context is fine, but questions must be specific
- Better: "Analyze entire payment service @./services/payment/ for PCI DSS compliance gaps"

### Optimization Strategies

**Use .geminiignore:**
```
# Exclude from context
node_modules/
dist/
build/
*.min.js
*.map
coverage/
.git/
```

**Focus with specific questions despite large context:**
```
Good:
"Review all services @./services/ for authentication vulnerabilities"

Not as good:
"Review all services @./services/ and tell me about them"
```

**Leverage compression for long sessions:**
```
# In Gemini CLI
gemini> /compress

# Saves tokens while preserving key context
```

### When Context is Still Too Large

**Problem:** Even 1M tokens isn't enough (very rare)

**Solutions:**

1. **Break by system boundaries**
   - Review each microservice separately
   - Then review inter-service concerns

2. **Break by concern type**
   - Security review first
   - Then performance review
   - Then architecture review

3. **Iterative review**
   - High-level architecture review
   - Drill into specific components
   - Follow-up on identified concerns

4. **Use abstraction**
   - Provide API contracts instead of implementations
   - Show architecture diagrams
   - Describe components at high level

### When Context is Too Small

**Problem:** Gemini doesn't have enough information

**Indicators:**
- Response asks for clarification
- Analysis is too generic
- Misunderstands the question
- Can't address specific concerns

**Solutions:**
1. Add more relevant code files
2. Include interface definitions
3. Provide architectural context
4. Add constraints and requirements
5. Include related documentation
6. Attach visual diagrams
7. Reference specification documents

---

## Context Preparation Checklist

Before invoking Gemini peer review, verify:

**Question:**
- [ ] Question is specific and answerable
- [ ] Clear what type of response is needed
- [ ] Focused on one decision/concern area
- [ ] Not too broad or vague
- [ ] Specifies whether to search for current best practices

**Code/Architecture:**
- [ ] Relevant code/description included via @references
- [ ] Appropriate context size (use Gemini's large window advantage)
- [ ] Key interfaces and dependencies included
- [ ] Visual assets included if helpful (diagrams, screenshots, PDFs)

**Background:**
- [ ] Project type and purpose stated
- [ ] Key constraints identified
- [ ] Scale/performance requirements noted
- [ ] Technology stack mentioned
- [ ] Compliance requirements listed

**Criteria:**
- [ ] Evaluation criteria specified
- [ ] Priorities indicated
- [ ] Trade-offs to consider identified
- [ ] Industry benchmark comparison requested if relevant

**Output:**
- [ ] Expected format specified
- [ ] Level of detail indicated
- [ ] Type of analysis requested (risk, comparison, recommendation, etc.)
- [ ] Whether to include current best practices/modern alternatives

**Gemini-Specific:**
- [ ] Considered including architecture diagrams
- [ ] Requested search for current best practices if relevant
- [ ] Leveraged large context window appropriately
- [ ] Included visual assets where helpful

---

## Common Context Preparation Mistakes

### Mistake 1: Information Overload Without Focus

**Problem:** Including massive context without specific questions

**Impact:** Even with 1M tokens, unfocused analysis is still generic

**Fix:**
- Large context is fine
- But questions must be specific
- Focus the analysis direction

**Example:**
```
Poor:
"Review everything in @./entire-codebase/"

Better:
"Review all authentication code in @./entire-codebase/ for security vulnerabilities and compliance with latest OWASP guidelines"
```

---

### Mistake 2: Missing Constraints

**Problem:** Not specifying technical, business, or time constraints

**Impact:** Recommendations may be impractical or miss important trade-offs

**Fix:** Always include key constraints and limitations

**Example:**
```
Poor:
"What's the best database?"

Better:
"What's the best database for:
- 10M daily transactions
- Strong consistency required
- Team expertise: PostgreSQL
- Budget: $5K/month
- Must deploy on AWS
- Check current performance benchmarks"
```

---

### Mistake 3: Vague Questions

**Problem:** "Is this good?" or "Any issues?" without specificity

**Impact:** Generic, unhelpful responses

**Fix:** Frame specific, answerable questions with clear focus

---

### Mistake 4: No Evaluation Criteria

**Problem:** Asking "which is better" without defining "better"

**Impact:** Can't prioritize trade-offs appropriately

**Fix:** Specify criteria and relative importance

---

### Mistake 5: Unclear Output Expectations

**Problem:** Not specifying format or type of response needed

**Impact:** Response may not be structured usefully

**Fix:** State expected output format clearly

---

### Mistake 6: Not Leveraging Multimodal Capabilities

**Problem:** Describing diagrams in text instead of attaching images

**Impact:** Missing opportunity for better analysis

**Fix:** Attach architecture diagrams, UI screenshots, PDFs directly

**Example:**
```
Poor:
"The architecture has an API gateway that routes to three services..."

Better:
"Review this architecture @./architecture-diagram.png focusing on service boundaries"
```

---

### Mistake 7: Not Requesting Current Information

**Problem:** Not asking Gemini to search for latest best practices

**Impact:** Recommendations may be outdated

**Fix:** Explicitly request current information when relevant

**Example:**
```
Enhanced:
"Review this React component and compare against current React 19 best practices (search for latest patterns)"
```

---

### Mistake 8: Excluding Visual Context

**Problem:** Not including screenshots when reviewing UI issues

**Impact:** Can't provide visual analysis feedback

**Fix:** Include screenshots, mockups, design files

---

## Context Refinement Process

If initial peer review isn't satisfactory:

1. **Assess the response:**
   - Too vague? → Add more specific questions and criteria
   - Misunderstood? → Clarify context and constraints
   - Too generic? → Add constraints, criteria, and ask for current best practices
   - Off-target? → Refocus the question with specific concerns
   - Outdated suggestions? → Request search for latest approaches

2. **Refine context:**
   - Add missing information
   - Clarify ambiguities
   - Include visual assets
   - Request search for current practices
   - Specify evaluation criteria more clearly
   - Add constraint details

3. **Leverage Gemini's capabilities:**
   - Add architecture diagrams
   - Request industry benchmark comparisons
   - Ask for search-grounded recommendations
   - Include more comprehensive code context

4. **Iterate:**
   - Follow up with specific sub-questions
   - Drill into identified concerns
   - Request alternatives or clarifications
   - Build on previous context (it's retained in session)

---

## Examples of Well-Prepared Contexts

### Example 1: Architecture Review with Multimodal Context

```
[ARCHITECTURE REVIEW: Multi-Tenant SaaS Platform]

System Purpose: B2B project management SaaS
Scale: 100-500 tenant organizations, 50-5K users per tenant
Stage: Greenfield design

Visual Architecture:
@./docs/architecture-diagram.png
@./docs/database-schema.png

Complete Service Code:
@./src/services/
@./src/api/
@./src/data/

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
- Implementation: @./prototypes/rls-approach/

Option B: Separate database per tenant
- PostgreSQL database created per tenant
- Complete data isolation at DB level
- Connection pooling per tenant
- Database provisioning automation required
- Implementation: @./prototypes/db-per-tenant/

Context:
- Strong data isolation requirements (handling sensitive project data)
- Variable tenant sizes (some very small, some very large)
- Team is experienced with PostgreSQL, less with RLS
- Cloud deployment on AWS RDS
- Budget: $10K/month for database infrastructure

Concerns:
- Data isolation security
- Operational complexity
- Query performance at scale
- Cost at 100-500 tenants
- Migration and backup complexity

Question:
Which multi-tenancy approach is recommended for this context?

Please analyze:
- Trade-offs for security, scalability, operational complexity, and cost
- Security assessment against current best practices
- Are there hybrid approaches worth considering?
- Search for recent case studies of similar scale systems
- Compare with current industry patterns for SaaS multi-tenancy

Expected Output:
- Risk assessment for each approach with severity levels
- Recommendation with detailed rationale
- Implementation considerations
- Comparison with current industry practices
- Alternative or hybrid approaches
```

**Why this is good:**
- Includes architecture diagram for visual understanding
- Provides complete code context (leverages 1M window)
- Includes prototype implementations for both options
- Specifies constraints clearly
- Requests search for current practices
- Clear evaluation criteria
- Specific output format

---

### Example 2: Security Review with Compliance Requirements

```
[SECURITY REVIEW: JWT Authentication Implementation]

System: REST API for financial data aggregation
Sensitivity: OAuth tokens, financial account credentials, PII
Compliance: SOC2, PCI DSS requirements

Authentication Flow Diagram:
@./docs/auth-sequence-diagram.png

Complete Implementation:
@./src/auth/
@./src/middleware/auth/
@./config/jwt-config.ts

Specification Documents:
@./docs/security-requirements.pdf
@./docs/pci-dss-checklist.pdf

Authentication Flow:
1. User logs in with email/password
2. Server validates credentials
3. Server issues JWT access token (15min expiry) + refresh token (7 day expiry)
4. Client includes access token in Authorization header
5. On expiry, client uses refresh token to get new access token

Current Implementation:
@./src/auth/token-generator.ts
@./src/auth/token-validator.ts
@./src/auth/refresh-handler.ts

Database Schema:
@./src/data/models/refresh-tokens.ts

Specific Security Concerns:
- Token storage (refresh tokens in database, access tokens client-side)
- Refresh token rotation and revocation
- Secret key management (currently environment variables)
- Timing attacks on token validation
- Token expiry and cleanup
- Session fixation or hijacking risks
- XSS token theft prevention

Current Security Measures:
- Tokens signed with HS256
- Refresh tokens stored in database
- HTTPS only
- CORS configured
- Rate limiting on auth endpoints

Question:
Identify security vulnerabilities in this authentication implementation.

Focus on:
- Token handling and storage
- Refresh token security and rotation
- Session management
- Timing attacks or information leakage
- XSS/CSRF protections
- Secret management

Additional Requirements:
- Check compliance with latest OWASP JWT guidelines (search)
- Check compliance with PCI DSS 4.0 requirements (search)
- Identify gaps vs current financial industry best practices (search)
- Recommend modern alternatives if current approach is outdated

Expected Output:
- Prioritized vulnerabilities with CVSS severity levels
- Specific attack vectors with PoC examples
- Remediation recommendations with code examples
- Compliance gap analysis
- Modern security patterns for financial APIs
```

**Why this is good:**
- Includes sequence diagram for flow understanding
- Provides complete auth implementation
- References compliance documents as PDFs
- Specific threat model and concerns
- Requests latest security guidelines via search
- Clear compliance requirements
- Structured output with severity levels

---

### Example 3: Performance Analysis with Profiling Data

```
[PERFORMANCE ANALYSIS: Query Handler Optimization]

System Context: E-commerce product search and filtering API
Current Performance:
- Average latency: 850ms (p50)
- P95 latency: 2.3s
- P99 latency: 4.1s

Performance Requirements:
- Target p50: <200ms
- Target p95: <500ms
- Target p99: <1s

Scale:
- 1M products in catalog
- 50K concurrent users peak
- 500 req/sec average, 2K req/sec peak

Complete Implementation:
@./src/api/handlers/search-handler.ts
@./src/services/search-service.ts
@./src/data/repositories/product-repository.ts
@./src/data/models/

Database Schema:
@./database/schema.sql

Profiling Data:
@./profiling/flame-graph.png
@./profiling/query-analysis.txt
@./profiling/trace-output.json

Example Slow Queries:
@./profiling/slow-queries.sql

Infrastructure:
- PostgreSQL 15 on AWS RDS (db.r6g.2xlarge)
- Node.js 20 application servers
- Redis for caching
- Elasticsearch for full-text search

Current Optimizations:
- Database indexes on common filter fields
- Redis caching for popular searches (TTL: 5min)
- Connection pooling (pool size: 20)
- Elasticsearch for text search

Known Issues:
- N+1 queries when loading product variants
- Complex JOIN on product attributes table
- No query result caching for custom filters
- Heavy serialization overhead

Constraints:
- Cannot change database (PostgreSQL)
- Budget for infrastructure: current + 30%
- Must maintain data consistency
- Elasticsearch budget: limited to current usage

Analysis Focus:
- Identify specific bottlenecks from profiling data
- Optimization opportunities (query, caching, indexing)
- Algorithmic improvements
- Architecture changes needed
- Trade-offs in optimization approaches

Additional Requests:
- Search for current e-commerce search optimization techniques
- Compare query performance against industry benchmarks
- Recommend modern caching strategies
- Identify if our infrastructure sizing is appropriate

Expected Output:
- Prioritized optimization recommendations
- Complexity vs impact assessment for each
- Query rewrite examples
- Architecture improvement suggestions
- Industry benchmark comparison
- Expected performance gains per recommendation
```

**Why this is good:**
- Includes profiling visualizations and data
- Provides complete code and database schema
- Clear performance targets and current metrics
- Specific constraints and budget
- Requests industry benchmarks via search
- Comprehensive context for deep analysis

---

### Example 4: Code Learning with Visual Context

```
[CODE REVIEW FOR LEARNING: Advanced React Pattern]

Code Context: Internal state management library found in production codebase
Learning Goal: Understand the pattern, why it was chosen, and if it's still appropriate

Code Implementation:
@./src/lib/state-management/
@./src/lib/state-management/core.ts
@./src/lib/state-management/hooks.ts
@./src/lib/state-management/types.ts

Usage Examples:
@./src/features/dashboard/state.ts
@./src/features/checkout/state.ts

Documentation (if any):
@./docs/state-management.md

Visual Aids:
@./diagrams/state-flow.png (hand-drawn diagram I created)
@./screenshots/devtools-state.png

Specific Questions:
1. What state management pattern is being used here?
2. Why would this custom solution be chosen over Redux/Zustand/Jotai?
3. Are there potential issues or anti-patterns?
4. How does this compare to modern React state management in 2025?
5. Should we migrate to a standard solution or is this still appropriate?

Background:
- My experience: Comfortable with React, familiar with Redux, new to advanced patterns
- What's unclear: The proxy-based state tracking mechanism
- What I've tried: Read through code, tested in DevTools
- Code was written in 2022

Team Context:
- 5 developers, varying React experience
- Onboarding new developers is important
- Maintenance burden is a concern

Additional Requests:
- Explain the proxy pattern being used
- Search for current React state management best practices
- Search for tutorial resources on this pattern
- Compare with popular 2025 state management solutions
- Recommend whether to keep or migrate

Expected Output:
- Clear explanation of the pattern (accessible to intermediate React dev)
- Rationale for why this approach was likely chosen
- Pros and cons analysis
- Comparison with modern alternatives
- Recommendation on keep vs migrate
- Learning resources for deeper understanding
```

**Why this is good:**
- Includes complete implementation for context
- Provides usage examples to show pattern in practice
- Includes visual diagrams (even hand-drawn)
- Clear learning goals and questions
- Specifies experience level for explanation
- Requests current best practices via search
- Asks for learning resources
- Team context for practical recommendations

---

These examples demonstrate how to prepare comprehensive, well-structured contexts that leverage Gemini's unique capabilities: massive context windows, multimodal analysis, search grounding, and current best practice awareness.
