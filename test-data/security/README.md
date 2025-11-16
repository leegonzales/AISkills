# Security Test Cases - Authentication Vulnerabilities

## Overview

This directory contains intentionally vulnerable authentication code examples designed to test peer review skills' capability to detect security vulnerabilities. These files are for **TESTING PURPOSES ONLY** and should never be used in production.

## Files

### 1. `jwt-auth.js` (5.0 KB)
**Focus**: JWT (JSON Web Token) authentication vulnerabilities

**Planted Vulnerabilities** (16 total):
- Weak JWT signing secret (`secret123`)
- Using HS256 instead of RS256 (symmetric vs asymmetric)
- No token expiration validation
- No refresh token mechanism
- Tokens not invalidated on logout
- No token blacklist implementation
- Role stored in JWT payload (client-controlled)
- Detailed error messages with stack traces
- Secrets logged to console
- Reset tokens in URL parameters

**Lines of Code**: ~220
**Dependencies**: `jsonwebtoken`, `express`

---

### 2. `session-management.js` (7.9 KB)
**Focus**: Session-based authentication vulnerabilities

**Planted Vulnerabilities** (18 total):
- Session fixation (accepts client-provided session IDs)
- Predictable session IDs (sequential counter)
- Session tokens in URL parameters
- No CSRF protection on state-changing operations
- Session data stored without encryption
- No session expiration/timeout
- Concurrent sessions not limited
- Session not regenerated after privilege escalation
- Logout doesn't invalidate session
- Insecure cookie configuration (missing flags)

**Lines of Code**: ~320
**Dependencies**: `express`, `crypto`

---

### 3. `api-auth.js` (8.2 KB)
**Focus**: API key authentication vulnerabilities

**Planted Vulnerabilities** (21 total):
- API keys stored in plain text
- Hardcoded master API key in source
- API keys exposed in client-side JavaScript
- No rate limiting (brute force/DoS risk)
- API keys in URL query parameters
- API keys logged in plain text
- Insufficient key rotation mechanism
- No scope validation on endpoints
- No key usage tracking
- Predictable API key format
- No revocation tracking/audit trail
- CORS misconfiguration allowing all origins
- API keys in environment variables exposed via endpoint

**Lines of Code**: ~360
**Dependencies**: `express`, `crypto`

---

### 4. `threat-model.md` (19 KB)
**Purpose**: Comprehensive threat analysis document

**Contents**:
- **Attack Vectors**: Detailed explanation of how each vulnerability can be exploited
- **Impact Assessment**: Risk severity levels (Critical, High, Medium, Low)
- **Detection Indicators**: Code patterns that indicate vulnerabilities
- **Remediation Guidance**: Best practices for fixing each vulnerability
- **OWASP Top 10 Mapping**: Links vulnerabilities to OWASP categories
- **Compliance Impact**: PCI DSS, GDPR, SOC 2, HIPAA considerations
- **Testing Methodology**: Manual review checklist, automated tools, pentest scenarios
- **Risk Scoring Matrix**: Exploitability vs Impact analysis

**Sections**: 9 major sections, 60+ individual vulnerability analyses

---

### 5. `security-requirements.md` (19 KB)
**Purpose**: Define security requirements for authentication systems

**Contents**:
- **Authentication Requirements**: Password-based, MFA, JWT, Sessions, API Keys
- **Authorization Requirements**: RBAC, ABAC, resource-level controls
- **CSRF Protection**: Token implementation, cookie configuration
- **OWASP Top 10 Compliance**: Mapping to OWASP 2021 categories
- **Logging & Monitoring**: Security event logging, anomaly detection
- **Testing Requirements**: Manual review, automated tools, penetration testing
- **Compliance Requirements**: PCI DSS, GDPR, HIPAA, SOC 2, NIST, CIS
- **Implementation Checklist**: Pre-dev, development, testing, deployment phases
- **Quick Reference**: Critical security checklist for rapid review

**Sections**: 9 major sections, 40+ specific requirements

---

## Usage

### For Testing Peer Review Skills:

1. **Run static analysis tools** (SAST):
   ```bash
   # Example with Semgrep
   semgrep --config=auto jwt-auth.js session-management.js api-auth.js
   ```

2. **Manual code review**:
   - Use `threat-model.md` as answer key
   - Check reviewer identified critical vulnerabilities
   - Verify remediation recommendations match best practices

3. **Compare against requirements**:
   - Cross-reference findings with `security-requirements.md`
   - Ensure all OWASP Top 10 relevant items covered
   - Validate compliance requirements addressed

### For Educational Purposes:

1. **Study vulnerable patterns**: Review code to understand what NOT to do
2. **Reference threat model**: Learn attack vectors and exploitation techniques
3. **Apply requirements**: Use as checklist for secure authentication implementation

---

## Running the Code (Optional)

While these files are syntactically valid Node.js code, running them is **NOT RECOMMENDED** as they are intentionally insecure. If you need to test detection tools:

```bash
# Install dependencies (in isolated test environment only)
npm install express jsonwebtoken

# Run servers (NEVER expose to internet)
node jwt-auth.js      # Port 3000
node session-management.js  # Port 3001
node api-auth.js      # Port 3002
```

**WARNING**: These servers have no security controls. Only run in isolated, local environments for testing purposes.

---

## Vulnerability Summary

### By Severity:

| Severity | JWT | Session | API Key | Total |
|----------|-----|---------|---------|-------|
| Critical | 4   | 4       | 4       | 12    |
| High     | 6   | 8       | 10      | 24    |
| Medium   | 4   | 4       | 5       | 13    |
| Low      | 2   | 2       | 2       | 6     |
| **Total**| **16** | **18** | **21** | **55** |

### By OWASP Top 10 Category:

- **A01 - Broken Access Control**: 8 vulnerabilities
- **A02 - Cryptographic Failures**: 12 vulnerabilities
- **A04 - Insecure Design**: 15 vulnerabilities
- **A05 - Security Misconfiguration**: 10 vulnerabilities
- **A07 - Authentication Failures**: 25 vulnerabilities
- **A08 - Software & Data Integrity**: 5 vulnerabilities
- **A09 - Logging & Monitoring**: 6 vulnerabilities

---

## Expected Detection Rates

### Automated Tools (SAST):
- **High confidence**: 40-50% of vulnerabilities
  - Hardcoded secrets, weak crypto, SQL injection patterns
- **Medium confidence**: 20-30% of vulnerabilities
  - Missing validation, insecure configurations

### Manual Code Review:
- **Experienced reviewer**: 80-90% detection rate
- **Junior reviewer**: 50-60% detection rate
- **With checklist**: +15-20% improvement

### Comprehensive Security Review (Manual + Automated + Pentest):
- **Expected detection**: 95-100% of planted vulnerabilities

---

## Testing Checklist

Use this checklist to evaluate peer review effectiveness:

### Critical Findings (Must Detect):
- [ ] Weak JWT signing secret
- [ ] Session fixation vulnerability
- [ ] API keys in client-side code
- [ ] Predictable session IDs
- [ ] No token/session expiration
- [ ] Hardcoded master API key

### High Findings (Should Detect):
- [ ] Missing CSRF protection
- [ ] Session ID in URLs
- [ ] No rate limiting
- [ ] Insecure cookie configuration
- [ ] API keys in URL parameters
- [ ] No scope validation

### Medium Findings (Good to Detect):
- [ ] No usage tracking
- [ ] Detailed error messages
- [ ] No key rotation
- [ ] Plaintext credential logging
- [ ] No concurrent session limits

### Low Findings (Advanced Detection):
- [ ] Missing security headers
- [ ] Verbose logging
- [ ] No geographic restrictions
- [ ] Missing audit trail

---

## References

- **OWASP Top 10**: https://owasp.org/Top10/
- **OWASP ASVS**: Application Security Verification Standard
- **NIST SP 800-63B**: Digital Identity Guidelines
- **CWE Top 25**: Most Dangerous Software Weaknesses
- **JWT Best Practices**: RFC 8725

---

## Contributing

If you identify additional vulnerabilities or have suggestions for improving these test cases, please document them in the threat model.

---

## License

These files are provided for educational and testing purposes only. Use at your own risk.

**Created**: 2024-11-12
**Purpose**: Testing peer review security detection capabilities
**Status**: Active test data
