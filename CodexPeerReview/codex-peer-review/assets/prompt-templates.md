# Prompt Templates for Codex Peer Review

Ready-to-use prompt templates for common peer review scenarios. Copy, customize with your context, and use with Codex CLI.

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

**Usage:**
```bash
codex exec --sandbox workspace-read "$(cat <<'EOF'
[paste filled template]
EOF
)"
```

---

### Template 2: Database Architecture Review

```markdown
[ARCHITECTURE REVIEW: Database Design]

System Context: [What application/feature this supports]
Data Characteristics: [Size, growth rate, access patterns]
Scale Requirements: [Read/write ratio, latency requirements, throughput]

Database Approach:

**Technology:** [PostgreSQL / MySQL / MongoDB / etc.]

**Schema Design:**
[High-level schema description or ERD]

Key Tables:
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

---

## Design Decision Templates

### Template 1: Technology/Framework Selection

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

---

### Template 2: Implementation Approach Decision

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

---

## Security Review Templates

### Template 1: Authentication System Review

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

---

### Template 2: API Security Review

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

---

## Performance Analysis Templates

### Template 1: Endpoint Performance Review

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

---

### Template 2: Database Query Performance

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

---

## Testing Strategy Templates

### Template 1: Test Coverage Review

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

---

## Usage Examples

### Example 1: Using Architecture Review Template

```bash
# 1. Copy template from above
# 2. Fill in with your specific context
# 3. Execute with Codex CLI

codex exec --sandbox workspace-read "$(cat <<'EOF'
[ARCHITECTURE REVIEW: E-Commerce Microservices]

System Purpose: E-commerce platform for B2C retail
Scale: 100K daily active users, 1M products, 10K orders/day
Stage: Refactoring from monolith

Current Architecture:

**Services:**
1. Product Service - Manages catalog (Node.js, PostgreSQL)
2. Order Service - Handles purchases (Node.js, PostgreSQL)
3. Payment Service - Processes payments (Node.js, external payment gateway)
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
- AWS ECS with Docker containers
- Application Load Balancer
- RDS for databases, ElastiCache for Redis

Key Architectural Decisions:
1. Separate databases per service - Rationale: Strong service boundaries, independent scaling
2. Event-driven for inventory updates - Rationale: Avoid tight coupling between orders and inventory
3. REST over gRPC - Rationale: Team familiarity, easier debugging

Specific Concerns:
- Data consistency between Order and Inventory services (eventual consistency)
- Distributed transaction handling for order placement
- Service communication overhead (latency)

Review Focus:
- Service boundaries and cohesion
- Data consistency approach (sagas vs other patterns)
- Scalability bottlenecks
- Failure modes (what happens if Inventory service is down during order?)
- Alternative architectural approaches

Expected Output: Risk assessment with severity levels, improvement recommendations, alternative approaches to consider
EOF
)"
```

---

### Example 2: Using Security Review Template

```bash
codex exec --sandbox none "$(cat <<'EOF'
[SECURITY REVIEW: JWT Authentication]

System Purpose: SaaS project management platform
User Sensitivity: Business data, multiple user roles
Compliance Requirements: SOC2 compliance required

Authentication Flow:
1. User submits email/password
2. Server validates credentials against bcrypt hash
3. Server generates JWT access token (15min expiry) + refresh token (7 day expiry)
4. Client stores tokens in localStorage
5. Client includes access token in Authorization header
6. On expiry, client uses refresh token to get new access token

Code for Review:
```typescript
// Token generation
async function generateTokens(userId: string) {
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

  await db.refreshTokens.insert({
    userId,
    token: refreshToken,
    expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
  });

  return { accessToken, refreshToken };
}

// Token validation
async function validateToken(token: string) {
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    return decoded.userId;
  } catch (error) {
    throw new Error('Invalid token');
  }
}

// Refresh endpoint
async function refreshAccessToken(refreshToken: string) {
  const decoded = jwt.verify(refreshToken, process.env.REFRESH_SECRET);

  const storedToken = await db.refreshTokens.findOne({
    userId: decoded.userId,
    token: refreshToken
  });

  if (!storedToken) {
    throw new Error('Invalid refresh token');
  }

  const accessToken = jwt.sign(
    { userId: decoded.userId, type: 'access' },
    process.env.JWT_SECRET,
    { expiresIn: '15m' }
  );

  return accessToken;
}
```

Threat Model:
- XSS attacks (token theft from localStorage)
- Man-in-the-middle (token interception)
- Refresh token theft and reuse
- Concurrent refresh attacks (multi-tab)
- Brute force attacks
- Session fixation

Specific Security Concerns:
- Tokens in localStorage (XSS vulnerability)
- No refresh token rotation
- No token revocation mechanism
- Missing rate limiting on auth endpoints
- Timing attacks on token comparison

Review Focus:
- Token storage security
- Refresh token handling
- Token validation robustness
- Attack vector analysis
- Best practice compliance
- Missing security controls

Expected Output: Prioritized vulnerabilities with severity, attack vectors, and remediation recommendations
EOF
)"
```

---

## Tips for Using Templates

### Customization

1. **Be Specific:** Replace bracketed placeholders with actual details
2. **Add Context:** Include relevant constraints and requirements
3. **Focus Questions:** Tailor "Review Focus" to your specific concerns
4. **Set Expectations:** Clearly state what format/detail you need in output

### Common Mistakes

**Too Vague:**
```
System: Web app
Question: Is it good?
```

**Better:**
```
System: E-commerce checkout flow processing 10K orders/day
Question: Review for payment security, data consistency during order processing, and scalability to 50K orders/day
```

### Iteration

If first response isn't satisfactory:
1. Add more specific context
2. Narrow or broaden the question
3. Clarify what output format you need
4. Provide example of what you're looking for

---

These templates provide starting points for effective peer review. Customize them for your specific needs and context.
