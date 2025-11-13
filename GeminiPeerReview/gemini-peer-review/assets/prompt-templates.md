# Ready-to-Use Prompt Templates for Gemini Peer Review

Ready-to-use prompt templates for common peer review scenarios. Copy, customize with your context, and use with Gemini CLI or API.

---

## Overview

This guide provides battle-tested prompt templates for conducting thorough peer reviews using Google Gemini. Each template is designed to leverage Gemini's 1M token context window and advanced reasoning capabilities.

**Template Benefits:**
- Copy-paste ready for immediate use
- Optimized for Gemini 2.5 Pro and Flash models
- Structured for comprehensive analysis
- Include both CLI and Python API usage patterns
- Target specific review scenarios

**Model Selection Guide:**
- **Gemini 2.5 Pro:** Complex reasoning, architecture reviews, security analysis
- **Gemini 2.5 Flash:** Quick reviews, code quality checks, documentation review
- **Gemini 2.5 Flash-Lite:** Simple pattern checks, style validation

---

## Template Categories

1. **Architecture Review Templates** - Evaluate system design and structure
2. **Design Decision Templates** - Compare and validate technical choices
3. **Security Review Templates** - Identify vulnerabilities and risks
4. **Performance Analysis Templates** - Optimize code and query performance
5. **Testing Strategy Templates** - Improve test coverage and quality

---

## Architecture Review Templates

### Template 1: Microservices Architecture Review

```markdown
[ARCHITECTURE REVIEW: Microservices System]

System Purpose: [Describe what the system does]
Scale: [Expected users, requests/day, data volume]
Stage: [Greenfield / Existing / Refactoring]

Current Architecture:

**Services:**
1. [Service Name] - [Responsibility, technology stack]
2. [Service Name] - [Responsibility, technology stack]
3. [Service Name] - [Responsibility, technology stack]

**Data Layer:**
- [Database 1]: [Purpose, technology]
- [Database 2]: [Purpose, technology]
- [Caching]: [Technology, usage]

**Integration:**
- [Inter-service communication approach]
- [Message queue / event bus if applicable]
- [API Gateway approach]

**Deployment:**
- [Platform: AWS/GCP/Azure/on-prem]
- [Orchestration: K8s/ECS/etc.]
- [CI/CD approach]

Key Architectural Decisions:
1. [Decision 1] - Rationale: [Why]
2. [Decision 2] - Rationale: [Why]
3. [Decision 3] - Rationale: [Why]

Specific Concerns:
- [Concern 1: e.g., service boundaries, data consistency]
- [Concern 2: e.g., scalability, deployment complexity]
- [Concern 3: e.g., observability, debugging]

Review Focus:
- Service boundaries and cohesion
- Data consistency approach
- Scalability bottlenecks
- Operational complexity
- Failure modes and resilience
- Alternative architectural approaches

Expected Output: Risk assessment with severity levels, improvement recommendations, and alternative approaches to consider
```

**Usage with Gemini CLI:**
```bash
gemini --model gemini-2.5-pro -p "$(cat <<'EOF'
[paste filled template]
EOF
)"
```

**Usage with Python API:**
```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

model = genai.GenerativeModel('gemini-2.5-pro')

prompt = """
[paste filled template]
"""

response = model.generate_content(prompt)
print(response.text)
```

---

### Template 2: Database Architecture Review

```markdown
[ARCHITECTURE REVIEW: Database Design]

System Context: [What application/feature this supports]
Data Characteristics: [Size, growth rate, access patterns]
Scale Requirements: [Read/write ratio, latency requirements, throughput]

Database Approach:

**Technology:** [PostgreSQL / MySQL / MongoDB / Firestore / etc.]

**Schema Design:**
[High-level schema description or ERD]

Key Tables/Collections:
- [Table 1]: [Purpose, estimated rows, key columns]
- [Table 2]: [Purpose, estimated rows, key columns]
- [Table 3]: [Purpose, estimated rows, key columns]

**Relationships:**
- [Relationship description: one-to-many, many-to-many, etc.]

**Indexes:**
- [Index 1]: [Purpose]
- [Index 2]: [Purpose]

**Data Access Patterns:**
1. [Pattern 1]: [Description, frequency]
2. [Pattern 2]: [Description, frequency]
3. [Pattern 3]: [Description, frequency]

Key Decisions:
1. [Decision 1: e.g., normalization level] - Rationale: [Why]
2. [Decision 2: e.g., partitioning strategy] - Rationale: [Why]
3. [Decision 3: e.g., replication approach] - Rationale: [Why]

Specific Concerns:
- [Concern 1: e.g., query performance at scale]
- [Concern 2: e.g., data consistency requirements]
- [Concern 3: e.g., backup and recovery]

Review Focus:
- Schema design and normalization
- Index strategy
- Query performance at scale
- Data consistency approach
- Scalability strategy
- Backup and disaster recovery

Expected Output: Performance and scalability assessment, optimization recommendations, alternative design approaches
```

**Usage with Gemini CLI (File Reference):**
```bash
# If schema is in files
gemini --model gemini-2.5-pro -p "Review this database architecture: @./database/schema.sql @./docs/architecture.md

Focus on:
- Schema design and normalization
- Index strategy
- Query performance at scale
- Scalability approach"
```

---

## Design Decision Templates

### Template 3: Technology/Framework Selection

```markdown
[DESIGN DECISION: Technology Selection]

Decision: [What technology/framework needs to be chosen]

Context:
- Project: [Type, size, timeline]
- Team: [Size, expertise, learning capacity]
- Requirements: [Functional and non-functional]
- Constraints: [Budget, time, existing infrastructure]

Options Under Consideration:

**Option A: [Technology/Framework Name]**
Approach: [How it would be used]
Pros:
- [Advantage 1]
- [Advantage 2]
- [Advantage 3]
Cons:
- [Disadvantage 1]
- [Disadvantage 2]
- [Disadvantage 3]
Implementation Complexity: [Low / Medium / High]
Operational Complexity: [Low / Medium / High]
Team Expertise: [High / Medium / Low]
Ecosystem Maturity: [Mature / Growing / Emerging]

**Option B: [Technology/Framework Name]**
Approach: [How it would be used]
Pros:
- [Advantage 1]
- [Advantage 2]
- [Advantage 3]
Cons:
- [Disadvantage 1]
- [Disadvantage 2]
- [Disadvantage 3]
Implementation Complexity: [Low / Medium / High]
Operational Complexity: [Low / Medium / High]
Team Expertise: [High / Medium / Low]
Ecosystem Maturity: [Mature / Growing / Emerging]

**Option C: [Technology/Framework Name]** (if applicable)
[Same structure as above]

Evaluation Criteria (in priority order):
1. [Criterion 1: e.g., time to market]
2. [Criterion 2: e.g., long-term maintainability]
3. [Criterion 3: e.g., performance]
4. [Criterion 4: e.g., cost]

Question: Which option is recommended given these criteria and context? What are the most significant trade-offs?

Expected Output: Comparative analysis against criteria, recommendation with rationale, risk assessment for each option
```

**Usage with Python API (with Search Grounding):**
```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Enable Google Search grounding for current information
model = genai.GenerativeModel(
    'gemini-2.5-pro',
    tools='google_search_retrieval'
)

prompt = """
[paste filled template with search-relevant questions]

Please use current 2025 information about these technologies.
"""

response = model.generate_content(prompt)
print(response.text)
```

---

### Template 4: Implementation Approach Decision

```markdown
[DESIGN DECISION: Implementation Approach]

Feature/Problem: [What needs to be implemented or solved]

Context:
- System: [Relevant system or module]
- Current State: [Existing implementation or greenfield]
- Requirements: [What the solution must achieve]
- Constraints: [Performance, compatibility, timeline]
- Team Expertise: [Relevant skills and gaps]

Approach A: [Name/Description]
How it works: [Technical description]
Pros:
- [Advantage 1]
- [Advantage 2]
Cons:
- [Disadvantage 1]
- [Disadvantage 2]
Complexity: [Assessment]
Risk Level: [Low / Medium / High]
Estimated Effort: [Time estimate]

Approach B: [Name/Description]
How it works: [Technical description]
Pros:
- [Advantage 1]
- [Advantage 2]
Cons:
- [Disadvantage 1]
- [Disadvantage 2]
Complexity: [Assessment]
Risk Level: [Low / Medium / High]
Estimated Effort: [Time estimate]

Evaluation Criteria:
1. [Criterion 1]
2. [Criterion 2]
3. [Criterion 3]

Question: Which approach is recommended? What are the key trade-offs and risks?

Expected Output: Recommendation with rationale, trade-off analysis, risk mitigation strategies
```

**Usage with Gemini CLI (Interactive):**
```bash
gemini --model gemini-2.5-flash -i "$(cat <<'EOF'
I need help deciding on an implementation approach.
[paste filled template]
EOF
)"

# Then continue with follow-up questions:
# gemini> What if we also need to consider backward compatibility?
# gemini> Can you provide code examples for Approach A?
```

---

## Security Review Templates

### Template 5: Authentication Security Review

```markdown
[SECURITY REVIEW: Authentication System]

System Purpose: [What application/feature this supports]
User Sensitivity: [Type of users, data access levels]
Compliance Requirements: [SOC2, HIPAA, PCI DSS, GDPR, etc. if applicable]

Authentication Flow:
[Step-by-step description of authentication flow]

Authorization Model:
[Description of how permissions/roles work]

Code for Review:
```[language]
[paste authentication/authorization code]
```

Threat Model:
- Credential stuffing / brute force attacks
- Session hijacking
- Token theft (XSS, man-in-the-middle)
- Privilege escalation
- Authentication bypass
- [Other specific threats]

Implementation Details:
- Session Management: [How sessions are handled]
- Token Strategy: [JWT, session tokens, OAuth, etc.]
- Password Storage: [Hashing algorithm, salting]
- Multi-factor: [Yes/No, implementation]
- Rate Limiting: [Yes/No, approach]

Specific Security Concerns:
- [Concern 1: e.g., token storage, expiry]
- [Concern 2: e.g., password reset flow]
- [Concern 3: e.g., concurrent session handling]

Review Focus:
- Vulnerability identification
- Attack vector analysis
- Best practice compliance
- Secure configuration validation
- Token/session security
- Input validation

Expected Output: Prioritized vulnerabilities with severity (Critical/High/Medium/Low), specific attack vectors, and detailed remediation recommendations
```

**Usage with Gemini CLI (File Reference):**
```bash
gemini --model gemini-2.5-pro -p "Conduct security review of authentication system.

@./src/auth/login.ts
@./src/auth/session.ts
@./src/middleware/auth.ts

Threat Model:
- Credential stuffing / brute force attacks
- Session hijacking
- Token theft (XSS, MITM)
- Privilege escalation

Focus on:
- Vulnerability identification
- Attack vector analysis
- Best practice compliance
- Remediation recommendations with severity levels"
```

**Usage with Python API (with File Context):**
```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

model = genai.GenerativeModel('gemini-2.5-pro')

# Read authentication code files
with open('./src/auth/login.ts', 'r') as f:
    login_code = f.read()

with open('./src/auth/session.ts', 'r') as f:
    session_code = f.read()

prompt = f"""
[SECURITY REVIEW: Authentication System]

System Purpose: SaaS project management platform
User Sensitivity: Business data, multiple user roles
Compliance Requirements: SOC2 compliance required

Authentication Code - login.ts:
```typescript
{login_code}
```

Session Management - session.ts:
```typescript
{session_code}
```

Threat Model:
- Credential stuffing / brute force attacks
- Session hijacking
- Token theft (XSS, man-in-the-middle)
- Privilege escalation

Review Focus:
- Vulnerability identification with severity levels
- Attack vector analysis
- Best practice compliance
- Specific remediation recommendations

Expected Output: Prioritized vulnerabilities (Critical/High/Medium/Low) with detailed remediation steps
"""

response = model.generate_content(prompt)
print(response.text)
```

---

### Template 6: API Security Review

```markdown
[SECURITY REVIEW: API Security]

API Purpose: [What the API does]
Data Sensitivity: [Types of data exposed, sensitivity level]
Client Types: [Web app, mobile app, third-party, etc.]
Authentication: [How API authenticates requests]

API Endpoints for Review:
1. [Endpoint 1]: [Method, path, purpose]
2. [Endpoint 2]: [Method, path, purpose]
3. [Endpoint 3]: [Method, path, purpose]

Code for Review:
```[language]
[paste API handler code]
```

Threat Model:
- Injection attacks (SQL, NoSQL, command)
- Authentication/authorization bypass
- Excessive data exposure
- Rate limiting / DoS
- Mass assignment vulnerabilities
- [Other specific threats]

Current Security Measures:
- Input Validation: [Description]
- Output Encoding: [Description]
- Authentication: [Mechanism]
- Authorization: [Mechanism]
- Rate Limiting: [Yes/No, approach]
- Logging/Monitoring: [What's logged]

Specific Concerns:
- [Concern 1: e.g., SQL injection risk]
- [Concern 2: e.g., excessive data exposure]
- [Concern 3: e.g., authorization checks]

Review Focus:
- Injection vulnerabilities
- Authentication/authorization flaws
- Data exposure risks
- Rate limiting effectiveness
- Error handling and information leakage
- OWASP API Security Top 10 compliance

Expected Output: Vulnerability assessment with severity, attack scenarios, and prioritized remediation plan
```

**Usage with Gemini CLI (Multiple Files):**
```bash
gemini --model gemini-2.5-pro -p "Security review for REST API.

@./src/api/users.js
@./src/api/orders.js
@./src/middleware/validate.js

Focus on OWASP API Security Top 10:
- Injection vulnerabilities
- Broken authentication
- Excessive data exposure
- Lack of resources & rate limiting
- Security misconfiguration

Provide severity levels and remediation priority."
```

---

## Performance Analysis Templates

### Template 7: Endpoint Performance Review

```markdown
[PERFORMANCE ANALYSIS: API Endpoint]

Endpoint: [Method and path]
Current Performance:
- Average latency: [ms]
- p95 latency: [ms]
- p99 latency: [ms]
- Throughput: [requests/sec]

Target Performance:
- Average latency: [ms target]
- p95 latency: [ms target]
- p99 latency: [ms target]
- Throughput: [requests/sec target]

Scale Context:
- Expected load: [requests/sec or requests/day]
- Data volume: [records, size]
- Growth rate: [expected growth]

Code for Analysis:
```[language]
[paste endpoint handler and related code]
```

Known Performance Issues:
- [Issue 1: e.g., N+1 queries, slow external calls]
- [Issue 2: e.g., missing indexes]
- [Issue 3: e.g., synchronous processing]

Profiling Results (if available):
- [Key finding 1 from profiling]
- [Key finding 2 from profiling]

Technology Context:
- Database: [Type, configuration]
- Cache: [Type if applicable]
- External APIs: [Dependencies]
- Infrastructure: [Server specs, cloud platform]

Analysis Focus:
- Bottleneck identification (database, computation, I/O)
- N+1 query patterns
- Missing indexes
- Inefficient algorithms
- Caching opportunities
- Async vs sync operations

Expected Output: Prioritized optimization recommendations with estimated impact (% improvement), implementation complexity, and risk assessment
```

**Usage with Gemini CLI:**
```bash
gemini --model gemini-2.5-flash -p "Performance analysis for checkout endpoint.

@./src/api/checkout.ts
@./src/services/payment.ts
@./src/db/order-repository.ts

Current Performance:
- Average: 450ms
- p95: 850ms
- p99: 1200ms

Target: < 200ms average

Analysis Focus:
- N+1 query patterns
- Database optimization
- Caching opportunities
- Async operations

Provide specific recommendations with estimated impact."
```

---

### Template 8: Database Query Performance

```markdown
[PERFORMANCE ANALYSIS: Database Query]

Query Purpose: [What this query does]
Current Performance: [Execution time, rows scanned]
Target Performance: [Required execution time]
Execution Frequency: [How often this runs]

Query Code:
```sql
[paste SQL query or ORM code]
```

Table Schemas:
```sql
[relevant table definitions and indexes]
```

Query Explain Plan:
```
[paste EXPLAIN output if available]
```

Data Context:
- Table sizes: [Row counts]
- Growth rate: [How fast tables grow]
- Data distribution: [Relevant characteristics]

Known Issues:
- [Issue 1: e.g., full table scan]
- [Issue 2: e.g., missing index]
- [Issue 3: e.g., expensive join]

Analysis Focus:
- Query plan optimization
- Index usage and recommendations
- Join strategy optimization
- Query rewriting opportunities
- Partitioning considerations
- Denormalization trade-offs

Expected Output: Query optimization recommendations with estimated performance improvement, required schema changes, and trade-off analysis
```

**Usage with Python API (with Schema Context):**
```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

model = genai.GenerativeModel('gemini-2.5-flash')

# Read schema and query files
with open('./database/schema.sql', 'r') as f:
    schema = f.read()

with open('./queries/user-orders.sql', 'r') as f:
    query = f.read()

with open('./profiling/explain-plan.txt', 'r') as f:
    explain_plan = f.read()

prompt = f"""
[PERFORMANCE ANALYSIS: Database Query]

Query Purpose: Fetch user orders with product details
Current Performance: 2.4 seconds, 1.2M rows scanned
Target Performance: < 200ms
Execution Frequency: 50,000 times/day

Query Code:
```sql
{query}
```

Table Schemas:
```sql
{schema}
```

Query Explain Plan:
```
{explain_plan}
```

Data Context:
- orders table: 5M rows, growing 50K/day
- products table: 100K rows, stable
- order_items table: 15M rows, growing 150K/day

Analysis Focus:
- Query plan optimization
- Index recommendations
- Join strategy
- Query rewriting opportunities

Expected Output: Specific optimization recommendations with estimated performance gains
"""

response = model.generate_content(prompt)
print(response.text)
```

---

## Testing Strategy Templates

### Template 9: Test Coverage Review

```markdown
[TESTING STRATEGY REVIEW: Coverage Analysis]

Module/Feature: [What's being tested]
Current Test Coverage: [Percentage by type]
- Unit tests: [%]
- Integration tests: [%]
- End-to-end tests: [%]

Code for Review:
```[language]
[paste code that needs better test coverage]
```

Current Tests (Sample):
```[language]
[paste sample of existing tests]
```

Critical Paths Requiring Coverage:
1. [Critical path 1: Description]
2. [Critical path 2: Description]
3. [Critical path 3: Description]

Known Testing Gaps:
- [Gap 1: e.g., error paths not tested]
- [Gap 2: e.g., edge cases missing]
- [Gap 3: e.g., integration tests absent]

Testing Concerns:
- [Concern 1: e.g., brittle tests]
- [Concern 2: e.g., slow test suite]
- [Concern 3: e.g., flaky tests]

Review Focus:
- Critical coverage gaps
- Missing edge cases
- Error path testing
- Integration test needs
- Test quality and maintainability
- Testing strategy improvements

Expected Output: Prioritized list of test cases to add, testing strategy recommendations, and test quality improvements
```

**Usage with Gemini CLI:**
```bash
gemini --model gemini-2.5-flash -p "Review test coverage and generate missing tests.

@./src/payment-processor.ts
@./tests/payment-processor.test.ts

Current Coverage:
- Unit: 65%
- Integration: 30%
- E2E: 20%

Critical Paths:
1. Payment authorization flow
2. Refund processing
3. Failed payment handling

Generate:
1. Missing test cases prioritized by risk
2. Test code for highest priority cases
3. Integration test strategy"
```

---

## Usage Examples

### Example 1: Architecture Review with CLI

```bash
# Filled template for e-commerce microservices

gemini --model gemini-2.5-pro -p "$(cat <<'EOF'
[ARCHITECTURE REVIEW: E-Commerce Microservices]

System Purpose: E-commerce platform for B2C retail
Scale: 100K daily active users, 1M products, 10K orders/day
Stage: Refactoring from monolith

Current Architecture:

**Services:**
1. Product Service - Manages catalog (Node.js, PostgreSQL)
2. Order Service - Handles purchases (Node.js, PostgreSQL)
3. Payment Service - Processes payments (Node.js, Stripe)
4. User Service - Authentication & profiles (Node.js, PostgreSQL)
5. Inventory Service - Stock management (Python, PostgreSQL)

**Data Layer:**
- PostgreSQL (per-service databases)
- Redis (caching, session storage)
- Elasticsearch (product search)

**Integration:**
- REST APIs for synchronous communication
- RabbitMQ for async events (order placed, inventory updated)
- API Gateway (Kong) for routing and auth

**Deployment:**
- GCP Cloud Run with Docker containers
- Cloud Load Balancer
- Cloud SQL for PostgreSQL, Memorystore for Redis

Key Architectural Decisions:
1. Separate databases per service - Rationale: Strong service boundaries, independent scaling
2. Event-driven for inventory updates - Rationale: Avoid tight coupling between orders and inventory
3. REST over gRPC - Rationale: Team familiarity, easier debugging

Specific Concerns:
- Data consistency between Order and Inventory services (eventual consistency)
- Distributed transaction handling for order placement
- Service communication overhead causing latency
- How to handle inventory service downtime during order placement

Review Focus:
- Service boundaries and cohesion
- Data consistency approach (saga pattern vs alternatives)
- Scalability bottlenecks
- Failure modes and resilience strategies
- Alternative architectural approaches

Expected Output: Risk assessment with severity levels, improvement recommendations, and alternative approaches to consider
EOF
)"
```

### Example 2: Security Review with Python API

```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

model = genai.GenerativeModel('gemini-2.5-pro')

# Read authentication code
with open('./src/auth/jwt.ts', 'r') as f:
    jwt_code = f.read()

prompt = f"""
[SECURITY REVIEW: JWT Authentication]

System Purpose: SaaS project management platform
User Sensitivity: Business data, multiple user roles (admin, manager, member)
Compliance Requirements: SOC2 compliance required

Authentication Flow:
1. User submits email/password to /api/login
2. Server validates credentials against bcrypt hash in PostgreSQL
3. Server generates JWT access token (15min expiry) + refresh token (7 day expiry)
4. Client stores tokens in localStorage
5. Client includes access token in Authorization: Bearer header
6. On access token expiry, client uses refresh token at /api/refresh
7. Refresh endpoint validates and issues new access token

Code for Review:
```typescript
{jwt_code}
```

Threat Model:
- XSS attacks (token theft from localStorage)
- Man-in-the-middle (token interception over network)
- Refresh token theft and replay attacks
- Concurrent refresh token usage (multi-tab scenarios)
- Brute force attacks on login endpoint
- Session fixation attacks

Implementation Details:
- Session Management: Stateless JWT approach
- Token Strategy: JWT with HS256 signing, refresh tokens stored in database
- Password Storage: bcrypt with cost factor 10
- Multi-factor: Not implemented (planned)
- Rate Limiting: 5 attempts per 15 minutes on /api/login

Specific Security Concerns:
- Tokens in localStorage vulnerable to XSS
- No refresh token rotation implemented
- No token revocation mechanism for compromised tokens
- Missing rate limiting on /api/refresh endpoint
- Potential timing attacks in token comparison

Review Focus:
- Token storage security (localStorage vs httpOnly cookies)
- Refresh token handling and rotation strategy
- Token validation robustness
- Attack vector analysis with real-world scenarios
- OWASP best practices compliance
- Immediate vs long-term security improvements

Expected Output:
1. Prioritized vulnerabilities with severity (Critical/High/Medium/Low)
2. Specific attack scenarios for each vulnerability
3. Detailed remediation recommendations
4. Quick wins vs strategic improvements
5. Code examples for top 3 fixes
"""

response = model.generate_content(prompt)
print(response.text)

# Save review to file
with open('./security-review-report.md', 'w') as f:
    f.write(response.text)

print("\nSecurity review complete. Report saved to security-review-report.md")
```

### Example 3: Performance Analysis with File References

```bash
# Analyze slow checkout endpoint

gemini --model gemini-2.5-flash -p "Performance optimization review for checkout API.

Code files:
@./src/api/checkout.ts
@./src/services/order-service.ts
@./src/services/inventory-service.ts
@./src/db/repositories/order-repo.ts

Current Performance Metrics:
- Average latency: 680ms
- p95 latency: 1,200ms
- p99 latency: 2,100ms
- Throughput: 45 req/sec

Target Performance:
- Average latency: < 250ms
- p95 latency: < 500ms
- Throughput: 200 req/sec

Scale Context:
- Current: 10K orders/day
- Growth: 50K orders/day in 6 months
- Database: PostgreSQL with 5M orders, 15M order_items

Known Issues:
- Multiple sequential database queries in checkout flow
- Synchronous inventory check calls external service
- No caching of product data during checkout

Technology Stack:
- Node.js Express API
- PostgreSQL database
- Redis available but not utilized
- Running on GCP Cloud Run

Analysis Focus:
1. Identify N+1 query patterns
2. Database query optimization opportunities
3. Caching strategy recommendations
4. Async operation opportunities
5. Code refactoring for performance

Expected Output:
1. Prioritized optimization recommendations
2. Estimated performance impact for each (% improvement)
3. Implementation complexity (Low/Medium/High)
4. Code examples for top 3 optimizations
5. Risk assessment for each change"
```

### Example 4: Test Coverage with Interactive Session

```bash
# Start interactive session for test generation

gemini --model gemini-2.5-flash -i "I need to improve test coverage for the payment processing module.

@./src/payment-processor.ts
@./tests/payment-processor.test.ts

Current Coverage:
- Unit: 58%
- Integration: 25%
- E2E: 15%

Critical Paths Missing Coverage:
1. Failed payment retry logic (3 attempts with exponential backoff)
2. Partial refund processing
3. Concurrent payment attempts for same order
4. Payment webhook handling from Stripe
5. Idempotency key validation

Known Testing Gaps:
- Error paths not tested (network failures, API timeouts)
- Edge cases missing (zero amount, negative amounts, currency mismatch)
- Integration tests with Stripe webhook absent
- Race condition testing not implemented

Testing Concerns:
- Existing tests are brittle (hardcoded IDs, dates)
- Test suite takes 3 minutes to run
- Flaky webhook tests (timing-dependent)

Generate:
1. Prioritized list of test cases to add
2. Complete test code for top 5 highest-priority cases
3. Integration test strategy for Stripe webhooks
4. Recommendations for reducing test brittleness"

# Then continue with follow-up questions:
# gemini> Can you also generate test fixtures for these test cases?
# gemini> How should we mock the Stripe API calls?
# gemini> Show me how to test the race condition scenario
```

---

## Tips for Template Customization

### Be Specific with Context

**Vague (Avoid):**
```
Review this code for issues.
@./src/app.js
```

**Specific (Better):**
```
Security review for Express.js authentication API.

@./src/auth/login.js
@./src/middleware/auth.js

Focus on:
- JWT token handling
- Password validation
- Rate limiting implementation
- SQL injection vulnerabilities

Compliance: Must meet OWASP Top 10 requirements
```

### Leverage Gemini's Strengths

**1. Use 1M Token Context Window:**
```bash
# Review entire codebase at once
gemini --model gemini-2.5-pro -p "Architecture review of entire project.

@./src/
@./tests/
@./docs/architecture.md

Analyze service boundaries, data flow, and identify architectural risks."
```

**2. Enable Search Grounding for Current Information:**
```python
model = genai.GenerativeModel(
    'gemini-2.5-pro',
    tools='google_search_retrieval'
)

prompt = """
Technology selection: Choose between Next.js 15, Remix, and Astro for blog platform.

Use latest 2025 information about:
- Performance benchmarks
- Community support
- Production readiness
- Latest features

[rest of template]
"""
```

**3. Use Multimodal Capabilities:**
```bash
# Review architecture diagram
gemini -p "Review this architecture diagram and compare to actual implementation.

@./docs/architecture-diagram.png
@./src/

Identify discrepancies and suggest updates."
```

### Structure Output Expectations

**Generic (Avoid):**
```
Expected Output: Analysis and recommendations
```

**Structured (Better):**
```
Expected Output:
1. Executive Summary (2-3 sentences)
2. Risk Assessment Table (Risk | Severity | Impact | Mitigation)
3. Prioritized Recommendations (High/Medium/Low priority)
4. Code Examples for top 3 fixes
5. Implementation Timeline (Quick wins vs strategic improvements)
6. Trade-offs and Considerations
```

### Iterate Based on Results

If first response isn't detailed enough:

```bash
# Initial review
gemini -p "[template with security review]"

# Follow-up for more detail
gemini -p "Provide specific code examples for the top 3 vulnerabilities identified.
Include before/after code snippets."

# Request attack scenarios
gemini -p "For the XSS vulnerability, provide a concrete attack scenario with:
1. Attacker's payload
2. Step-by-step exploitation
3. Expected impact
4. Detailed remediation code"
```

---

## Common Template Mistakes

### Mistake 1: Too Little Context

**Problem:**
```bash
gemini -p "Review @./app.js"
```

**Solution:**
```bash
gemini -p "Security review for Express.js REST API.

@./app.js

Application Context:
- User authentication and profile management
- Handles sensitive PII data
- 50K daily active users
- SOC2 compliance required

Focus on:
- OWASP Top 10 vulnerabilities
- Input validation
- Authentication/authorization
- Data exposure risks

Provide severity levels and remediation priority."
```

### Mistake 2: Vague Review Focus

**Problem:**
```
Review Focus: Make it better
```

**Solution:**
```
Review Focus:
1. N+1 query patterns in ORM usage
2. Missing database indexes for common queries
3. Inefficient algorithm complexity (> O(n log n))
4. Caching opportunities for frequently accessed data
5. Synchronous operations that could be async
```

### Mistake 3: No Performance Baseline

**Problem:**
```
Optimize this code for better performance.
```

**Solution:**
```
Current Performance:
- Average response time: 850ms
- p95: 1,400ms
- Memory usage: 450MB per request

Target Performance:
- Average response time: < 200ms
- p95: < 400ms
- Memory usage: < 100MB per request

Bottlenecks identified:
- Database query takes 600ms (EXPLAIN shows full table scan)
- JSON serialization takes 150ms (2MB response)
- No caching (same data fetched on every request)
```

### Mistake 4: Missing Technology Context

**Problem:**
```
Review this database design.
```

**Solution:**
```
Database Design Review

Technology Stack:
- Database: PostgreSQL 15
- ORM: Prisma
- Expected scale: 10M rows in orders table
- Read/write ratio: 80/20
- Latency requirement: < 100ms for queries
- Infrastructure: GCP Cloud SQL with 4 vCPU, 16GB RAM
```

### Mistake 5: No Output Format Specification

**Problem:**
```
Expected Output: Analysis
```

**Solution:**
```
Expected Output Format:

## Executive Summary
[2-3 sentence overview of findings]

## Vulnerabilities
| Severity | Vulnerability | Location | Attack Vector | Remediation |
|----------|--------------|----------|---------------|-------------|

## Detailed Analysis
[For each vulnerability:]
- Description
- Code snippet showing issue
- Attack scenario
- Remediation steps
- Code example of fix

## Recommendations by Priority
### High Priority (Implement This Sprint)
### Medium Priority (Next 2 Sprints)
### Low Priority (Backlog)

## Trade-offs and Considerations
```

---

## Template Iteration Workflow

### Step 1: Start with Base Template

```bash
# Use template as-is for first review
gemini --model gemini-2.5-pro -p "$(cat <<'EOF'
[ARCHITECTURE REVIEW: Microservices System]
[filled template]
EOF
)"
```

### Step 2: Analyze Initial Response

Review the output for:
- Depth of analysis
- Specificity of recommendations
- Relevance to your concerns
- Missing areas

### Step 3: Refine with Follow-up

```bash
# Request more detail on specific areas
gemini -p "Provide more detail on the data consistency concern.

Specifically:
1. Compare Saga pattern vs 2-phase commit for our use case
2. Show code example of Saga implementation for order/inventory
3. Analyze failure scenarios and recovery mechanisms
4. Estimate implementation effort and risks"
```

### Step 4: Request Alternative Formats

```bash
# Get structured output
gemini -p "Convert the previous analysis to a decision matrix table comparing:

| Approach | Consistency | Performance | Complexity | Risk | Recommended |
|----------|-------------|-------------|------------|------|-------------|"
```

### Step 5: Generate Actionable Artifacts

```bash
# Create implementation tickets
gemini -p "Based on the architecture review, generate:

1. GitHub issue template for each high-priority recommendation
2. Technical design document outline for data consistency solution
3. Test plan for validating the improvements
4. Migration plan with rollback strategy"
```

### Step 6: Continuous Improvement

Save your refined templates:

```bash
# Save successful template variations
mkdir -p ~/.gemini-templates
cat > ~/.gemini-templates/architecture-review-v2.md <<'EOF'
[Your refined template based on successful reviews]
EOF
```

---

## Advanced Tips

### Use Session Memory for Context

```bash
# Start interactive session with project context
gemini -i "Project context:
- Node.js microservices on GCP
- PostgreSQL + Redis
- 100K DAU, 10K orders/day
- Team: 5 developers, 6-month timeline
- Focus: Scale to 50K orders/day

I'll be asking for multiple reviews using this context."

# Then use templates without repeating context
gemini> [paste architecture review template - context already loaded]
gemini> [paste security review template - context already loaded]
```

### Combine Multiple Templates

```bash
gemini --model gemini-2.5-pro -p "Comprehensive review combining:

1. Architecture Review
@./docs/architecture.md

2. Security Review
@./src/auth/

3. Performance Analysis
@./src/api/

For each area, provide:
- Risk assessment
- Prioritized recommendations
- Quick wins vs strategic improvements
- Estimated effort and impact"
```

### Use JSON Output for Automation

```bash
# Get structured JSON output
gemini --output-format json -p "Security review with JSON output.

@./src/auth/

Output format:
{
  \"vulnerabilities\": [
    {
      \"severity\": \"High|Medium|Low\",
      \"title\": \"...\",
      \"description\": \"...\",
      \"location\": \"file:line\",
      \"remediation\": \"...\"
    }
  ],
  \"summary\": {
    \"total\": 0,
    \"critical\": 0,
    \"high\": 0,
    \"medium\": 0,
    \"low\": 0
  }
}"
```

### Integrate with CI/CD

```python
#!/usr/bin/env python3
"""
security-review.py - Automated security review in CI/CD
"""
import google.generativeai as genai
import os
import json
import sys

genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel('gemini-2.5-pro')

# Read files to review
changed_files = sys.argv[1:] if len(sys.argv) > 1 else []

files_content = {}
for file_path in changed_files:
    with open(file_path, 'r') as f:
        files_content[file_path] = f.read()

# Build prompt
files_section = "\n\n".join([
    f"File: {path}\n```\n{content}\n```"
    for path, content in files_content.items()
])

prompt = f"""
[SECURITY REVIEW: Code Changes]

Files Changed:
{files_section}

Review Focus:
- OWASP Top 10 vulnerabilities
- Input validation
- Authentication/authorization
- Sensitive data exposure
- Security misconfigurations

Output JSON format:
{{
  "has_vulnerabilities": true/false,
  "vulnerabilities": [
    {{
      "severity": "Critical|High|Medium|Low",
      "file": "path",
      "line": 0,
      "title": "...",
      "description": "...",
      "remediation": "..."
    }}
  ],
  "block_merge": true/false
}}
"""

response = model.generate_content(prompt)

# Parse JSON from response
# Handle Gemini's JSON in markdown code blocks
response_text = response.text
if "```json" in response_text:
    json_str = response_text.split("```json")[1].split("```")[0].strip()
else:
    json_str = response_text

result = json.loads(json_str)

# Print results
print(json.dumps(result, indent=2))

# Exit with error if critical/high vulnerabilities found
if result.get('block_merge', False):
    print("\n❌ Security vulnerabilities found. Blocking merge.", file=sys.stderr)
    sys.exit(1)
else:
    print("\n✅ No blocking security issues found.")
    sys.exit(0)
```

---

These templates provide battle-tested starting points for effective peer review with Gemini. Customize them for your specific needs and context, and iterate based on results to develop your own refined template library.
