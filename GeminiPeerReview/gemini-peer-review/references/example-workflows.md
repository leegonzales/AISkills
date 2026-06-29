# Example Workflows

End-to-end Gemini peer review scenarios showing context preparation, CLI invocation, and synthesis.

> **Firewall reminder:** Only quote/attribute Gemini after a real `gemini` run with real output this session. If the CLI is unavailable, use the degraded-mode template from SKILL.md and proceed Claude-only.

---

## Example 1: Architecture Decision

**User:** "I'm designing a multi-tenant SaaS architecture. Should I use separate databases per tenant or a shared database with row-level security?"

**Claude initial analysis:** [Provides analysis of trade-offs]

**Invoke peer review:**
```bash
cat <<'EOF' | gemini
Review multi-tenant SaaS architecture decision:

CONTEXT:
- B2B SaaS with 100-500 tenants expected
- Varying data volumes per tenant (small to large)
- Strong data isolation requirements
- Team familiar with PostgreSQL
- Cloud deployment (AWS)
- Growth projection: 2x tenants annually

OPTIONS:
A) Separate database per tenant
   - Complete isolation
   - Independent scaling
   - Operational complexity

B) Shared database with row-level security (RLS)
   - Simpler operations
   - Shared resources
   - RLS overhead

CURRENT CODEBASE:
[Include relevant ORM models, database config, auth system]

QUESTION:
Analyze trade-offs for scalability, operational complexity, data isolation,
and cost. Which approach is recommended for this context?
Consider both current state and 3-year growth trajectory.

EXPECTED OUTPUT:
- Analysis of each approach
- Trade-off matrix
- Recommendation with rationale
- Migration path considerations
EOF
```

**Synthesis:**
Compare Claude's and Gemini's trade-off analysis, extract key insights, present balanced recommendation with rationale from both perspectives.

---

## Example 2: Security Review with Code Context

**User:** "Review authentication implementation for security issues"

**Invoke peer review:**
```bash
cat <<'EOF' | gemini
Security review of authentication system:

THREAT MODEL:
- Session hijacking
- Token replay attacks
- Credential stuffing
- CSRF attacks
- XSS-based token theft

IMPLEMENTATION:
[Include auth code from src/auth/session.py, tokens.py, middleware/auth.py]

SECURITY REQUIREMENTS:
- 99.9% prevention of unauthorized access
- Compliance: SOC2, HIPAA
- Session timeout: 30 min inactivity
- MFA support required

QUESTION:
Identify vulnerabilities, attack vectors, and hardening opportunities.
Prioritize findings by severity and likelihood.

EXPECTED OUTPUT:
- Vulnerability assessment (severity ratings)
- Attack vector analysis
- Specific remediation recommendations
- Best practice gaps
EOF
```

**Synthesis:**
Combine security findings from both AIs, create prioritized remediation list.

---

## Example 3: Large Codebase Architecture Analysis

**User:** "Help me understand this unfamiliar 60k LOC codebase"

**Invoke peer review (leveraging 1M context):**
```bash
cat <<'EOF' | gemini
Analyze this complete backend codebase:

CODEBASE:
[Include entire codebase - Gemini's 1M token window can process 60k LOC!]

CONTEXT:
- E-commerce platform backend
- Microservices architecture
- New engineer onboarding perspective needed

QUESTIONS:
1. What are the major architectural patterns?
2. How does a typical request flow from API → Database?
3. What are the core abstractions/modules?
4. Where are the critical integration points?
5. What are potential scalability bottlenecks?
6. What technical debt is visible?

EXPECTED OUTPUT:
- High-level architecture summary
- Request lifecycle walkthrough
- Module dependency map
- Critical code paths
- Scalability considerations
- Onboarding guide structure
EOF
```

**Gemini advantage on display:**
This is where Gemini truly shines—processing entire codebases in one context to see patterns, dependencies, and architectural decisions that would be impossible to detect with chunked analysis.

---

## Example 4: Multimodal Design-to-Implementation Review

**User:** "Does our implementation match the original architecture design?"

**Invoke peer review with diagram:**
```bash
cat <<'EOF' | gemini
Compare architecture design vs. implementation:

[Architecture diagram: @docs/architecture-v2.png]

DESIGN SPECIFICATION:
[See attached architecture diagram showing intended service structure]

IMPLEMENTATION:
[Include implementation code from src/services/*, src/api/*, infrastructure/*]

QUESTIONS:
1. Does implementation match intended architecture?
2. What deviations exist and why might they be problematic?
3. Are there missing components from the design?
4. Are there additional components not in the design?
5. Do the actual service boundaries align with designed boundaries?

EXPECTED OUTPUT:
- Match/deviation analysis
- Gap identification
- Risk assessment of deviations
- Recommendations for alignment
EOF
```

**Gemini advantage on display:**
Multimodal analysis—comparing visual architecture with actual code—is a unique Gemini capability that Claude cannot replicate alone.
