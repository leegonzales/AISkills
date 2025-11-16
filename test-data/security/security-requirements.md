# Security Requirements - Authentication System

## Document Information

**Purpose**: Define security requirements for authentication and authorization systems
**Scope**: JWT, session-based, and API key authentication
**Audience**: Developers, security reviewers, QA engineers
**Last Updated**: 2024-11-12

---

## 1. Authentication Requirements

### 1.1 Password-Based Authentication

#### Requirements:

**REQ-AUTH-001**: Password Hashing
- **MUST** use bcrypt, scrypt, or Argon2 for password hashing
- **MUST NOT** use MD5, SHA-1, or plain SHA-256
- **MUST** use minimum work factor: bcrypt cost ≥ 12, Argon2 recommended settings
- **MUST** use unique salt per password (automatic with bcrypt/Argon2)

**REQ-AUTH-002**: Password Policies
- **MUST** enforce minimum length: 12 characters
- **SHOULD** enforce complexity: mix of uppercase, lowercase, numbers, symbols
- **MUST** check against common password lists (e.g., Have I Been Pwned)
- **SHOULD** implement passwordless options (WebAuthn, passkeys)

**REQ-AUTH-003**: Rate Limiting
- **MUST** limit login attempts: max 5 failures per 15 minutes per username
- **MUST** limit login attempts: max 20 failures per 15 minutes per IP
- **SHOULD** implement exponential backoff on repeated failures
- **MUST** implement CAPTCHA after 3 failed attempts

**REQ-AUTH-004**: Account Lockout
- **SHOULD** temporarily lock account after 10 failed attempts
- **MUST** notify user via email of lockout
- **MUST** provide secure unlock mechanism (email verification)
- **SHOULD** implement risk-based authentication for suspicious logins

---

### 1.2 Multi-Factor Authentication (MFA)

#### Requirements:

**REQ-MFA-001**: MFA Support
- **MUST** support TOTP (Time-based One-Time Password)
- **SHOULD** support WebAuthn/FIDO2 hardware keys
- **SHOULD** support SMS OTP (as fallback only, not primary)
- **MUST NOT** use SMS as sole second factor for high-risk operations

**REQ-MFA-002**: MFA Enforcement
- **MUST** enforce MFA for administrative accounts
- **SHOULD** enforce MFA for all users handling sensitive data
- **MUST** require MFA for privilege escalation
- **SHOULD** allow users to enable MFA voluntarily

**REQ-MFA-003**: Recovery Codes
- **MUST** provide recovery codes when MFA is enabled
- **MUST** allow one-time use of recovery codes
- **MUST** require secure storage recommendation to user
- **SHOULD** provide secure backup code download (not plain text in browser)

---

### 1.3 JWT (JSON Web Tokens)

#### Requirements:

**REQ-JWT-001**: Signing Algorithm
- **MUST** use RS256 (RSA Signature with SHA-256) or ES256 (ECDSA)
- **MUST NOT** use HS256 for distributed systems (shared secret risk)
- **MUST NOT** accept 'none' algorithm
- **MUST** validate algorithm in token header matches expected algorithm

**REQ-JWT-002**: Secret/Key Management
- **MUST** use minimum 256-bit (32-byte) secret for HS256
- **MUST** use 2048-bit RSA key minimum for RS256
- **MUST** store secrets in secure vault (AWS Secrets Manager, Vault, etc.)
- **MUST** rotate keys at least annually
- **MUST** support multiple active keys for rotation without downtime

**REQ-JWT-003**: Token Expiration
- **MUST** set expiration time (`exp` claim)
- **MUST** use short-lived access tokens: 5-15 minutes
- **MUST** validate expiration on every token verification
- **MUST NOT** accept expired tokens

**REQ-JWT-004**: Token Claims
- **MUST** include issuer (`iss`)
- **MUST** include subject (`sub` - user ID)
- **MUST** include issued-at time (`iat`)
- **MUST** include expiration (`exp`)
- **SHOULD** include audience (`aud`) for multi-service architecture
- **SHOULD** include JWT ID (`jti`) for revocation tracking

**REQ-JWT-005**: Token Revocation
- **MUST** implement token blacklist/denylist for logged-out tokens
- **MUST** invalidate all tokens on password change
- **SHOULD** use Redis or similar for fast blacklist lookup
- **MUST** provide "logout all devices" functionality
- **SHOULD** include token version/nonce for bulk invalidation

**REQ-JWT-006**: Refresh Tokens
- **MUST** implement refresh token flow for long-lived sessions
- **MUST** use different secret for refresh tokens
- **MUST** set refresh token expiration: 7-30 days
- **MUST** rotate refresh token on use (one-time use)
- **MUST** store refresh token hashes server-side
- **MUST** bind refresh token to device/fingerprint

**REQ-JWT-007**: Token Transport
- **MUST** transmit tokens only over HTTPS
- **SHOULD** use HTTP-only cookies for web applications
- **MAY** use Authorization header with Bearer scheme for APIs
- **MUST NOT** include tokens in URL query parameters
- **MUST NOT** log tokens in application logs

---

### 1.4 Session-Based Authentication

#### Requirements:

**REQ-SESS-001**: Session ID Generation
- **MUST** use cryptographically secure random number generator
- **MUST** generate minimum 128-bit entropy (16 bytes)
- **MUST NOT** use predictable patterns (timestamp, counter, UUID v1)
- **SHOULD** use 256-bit entropy for high-security applications

**REQ-SESS-002**: Session Fixation Protection
- **MUST** regenerate session ID after successful login
- **MUST** regenerate session ID after privilege escalation
- **MUST** invalidate pre-authentication session
- **MUST NOT** accept client-provided session IDs

**REQ-SESS-003**: Session Storage
- **MUST** store session data server-side (not in client cookie)
- **SHOULD** use Redis, Memcached, or database for session storage
- **MUST** encrypt sensitive session data at rest
- **SHOULD** use distributed session store for multi-server deployments

**REQ-SESS-004**: Session Timeout
- **MUST** implement idle timeout: 15-30 minutes of inactivity
- **MUST** implement absolute timeout: 12-24 hours
- **MUST** track last activity time
- **SHOULD** warn user before timeout (e.g., 2 minutes remaining)
- **MUST** clear session data on timeout

**REQ-SESS-005**: Cookie Configuration
- **MUST** set `HttpOnly` flag (prevent XSS access)
- **MUST** set `Secure` flag (HTTPS only)
- **MUST** set `SameSite=Strict` or `SameSite=Lax` (prevent CSRF)
- **SHOULD** use `__Host-` prefix for cookie name (stronger security)
- **MUST** set appropriate `maxAge` or `expires`

**REQ-SESS-006**: Session Concurrency
- **SHOULD** limit concurrent sessions per user (e.g., max 5 devices)
- **MUST** track active sessions per user
- **SHOULD** allow user to view active sessions
- **SHOULD** allow user to revoke individual sessions

---

### 1.5 API Key Authentication

#### Requirements:

**REQ-API-001**: API Key Generation
- **MUST** use cryptographically secure random generation
- **MUST** generate minimum 256-bit entropy (32 bytes)
- **SHOULD** use distinguishable prefix (e.g., `ak_live_`, `ak_test_`)
- **MUST** display key only once at creation
- **SHOULD** show masked key in UI (e.g., `ak_live_••••••••1234`)

**REQ-API-002**: API Key Storage
- **MUST** hash API keys before storing (bcrypt, scrypt, Argon2)
- **MUST NOT** store API keys in plain text
- **SHOULD** store hashed key with salt
- **MUST** store key metadata (created, last used, scopes)

**REQ-API-003**: API Key Scopes
- **MUST** implement scope-based authorization
- **MUST** enforce principle of least privilege
- **SHOULD** use granular scopes (e.g., `read:users`, `write:posts`)
- **MUST** validate scopes on every API request
- **SHOULD** allow users to create restricted keys

**REQ-API-004**: API Key Rotation
- **MUST** support key rotation without downtime
- **SHOULD** set expiration on API keys (90-365 days)
- **MUST** warn before key expiration (30, 7, 1 days)
- **SHOULD** allow overlapping keys during rotation period
- **MUST** provide API endpoint for programmatic rotation

**REQ-API-005**: API Key Revocation
- **MUST** provide immediate key revocation
- **MUST** log revocation events
- **MUST** notify key owner of revocation
- **SHOULD** implement grace period with warning for accidental revocation

**REQ-API-006**: Rate Limiting
- **MUST** implement per-key rate limiting
- **SHOULD** use token bucket or sliding window algorithm
- **MUST** return HTTP 429 (Too Many Requests) when exceeded
- **SHOULD** include rate limit headers (`X-RateLimit-*`)
- **SHOULD** allow different limits per scope/tier

**REQ-API-007**: Usage Tracking
- **MUST** track last used timestamp per key
- **MUST** track request count per key
- **SHOULD** track IP addresses per key
- **SHOULD** track geographic location
- **MUST** detect and alert on anomalous usage
- **SHOULD** provide usage dashboard for key owners

**REQ-API-008**: API Key Transport
- **MUST** transmit keys only over HTTPS
- **MUST** use custom header (e.g., `X-API-Key`) or `Authorization: Bearer`
- **MUST NOT** include keys in URL query parameters
- **MUST NOT** include keys in URL paths
- **MUST** redact keys in logs

**REQ-API-009**: Client-Side Protection
- **MUST NOT** expose API keys in client-side JavaScript
- **MUST NOT** embed keys in mobile apps (use OAuth instead)
- **MUST NOT** commit keys to version control
- **SHOULD** use separate keys for development/staging/production

---

## 2. Authorization Requirements

### 2.1 Access Control

#### Requirements:

**REQ-AUTHZ-001**: Principle of Least Privilege
- **MUST** grant minimum permissions required
- **MUST** deny by default, allow explicitly
- **MUST** separate read/write/delete permissions
- **SHOULD** implement role-based access control (RBAC)

**REQ-AUTHZ-002**: Role-Based Access Control
- **MUST** define clear roles with specific permissions
- **MUST** support multiple roles per user
- **SHOULD** implement hierarchical roles
- **MUST** validate role on every protected operation

**REQ-AUTHZ-003**: Attribute-Based Access Control
- **SHOULD** implement ABAC for complex scenarios
- **SHOULD** support context-aware access control (time, location, device)
- **MAY** use policy engines for dynamic authorization

**REQ-AUTHZ-004**: Resource-Level Authorization
- **MUST** verify user owns resource before allowing access
- **MUST** check authorization at API layer, not just UI
- **MUST** prevent horizontal privilege escalation (access other users' data)
- **MUST** prevent vertical privilege escalation (access admin functions)

---

### 2.2 CSRF Protection

#### Requirements:

**REQ-CSRF-001**: CSRF Token Implementation
- **MUST** use CSRF tokens for state-changing operations
- **MUST** use synchronizer token pattern or double-submit cookie
- **MUST** validate token on POST/PUT/DELETE/PATCH requests
- **SHOULD** use per-session or per-request tokens

**REQ-CSRF-002**: Cookie Configuration
- **MUST** set `SameSite=Strict` or `Lax` on session cookies
- **SHOULD** prefer `SameSite=Strict` for high-security operations
- **MAY** use `Lax` for general web applications (allows top-level navigation)

**REQ-CSRF-003**: Header Validation
- **SHOULD** validate `Origin` header matches expected domain
- **SHOULD** validate `Referer` header (as defense in depth)
- **MUST** validate custom headers (e.g., `X-Requested-With`)

---

## 3. OWASP Top 10 Compliance

### Mapping to OWASP Top 10 2021:

**A01 - Broken Access Control**
- Covered by: REQ-AUTHZ-001 through REQ-AUTHZ-004
- Mitigations: RBAC, resource-level authorization, deny by default

**A02 - Cryptographic Failures**
- Covered by: REQ-AUTH-001, REQ-JWT-001, REQ-JWT-002, REQ-API-002
- Mitigations: Strong hashing, proper algorithms, secure key management

**A04 - Insecure Design**
- Covered by: All requirements sections
- Mitigations: Security requirements defined upfront, threat modeling

**A05 - Security Misconfiguration**
- Covered by: REQ-SESS-005, REQ-JWT-007, REQ-API-008
- Mitigations: Secure defaults, proper cookie flags, HTTPS enforcement

**A07 - Identification and Authentication Failures**
- Covered by: All authentication requirements (1.1 through 1.5)
- Mitigations: MFA, secure session management, proper credential storage

**A08 - Software and Data Integrity Failures**
- Covered by: REQ-JWT-001, REQ-JWT-004
- Mitigations: Token signature validation, algorithm enforcement

**A09 - Security Logging and Monitoring Failures**
- Covered by: Section 4 (below)
- Mitigations: Audit logging, anomaly detection, alerting

**A10 - Server-Side Request Forgery**
- Not directly covered (out of scope for authentication)

---

## 4. Logging and Monitoring Requirements

### 4.1 Security Event Logging

#### Requirements:

**REQ-LOG-001**: Authentication Events
- **MUST** log successful logins (user, timestamp, IP, device)
- **MUST** log failed login attempts (username, IP, reason)
- **MUST** log logout events
- **MUST** log password changes
- **MUST** log MFA enrollment/removal

**REQ-LOG-002**: Authorization Events
- **MUST** log privilege escalation attempts
- **MUST** log access to sensitive resources
- **SHOULD** log authorization failures
- **SHOULD** log role/permission changes

**REQ-LOG-003**: Anomaly Detection
- **SHOULD** detect multiple failed logins
- **SHOULD** detect logins from new locations/devices
- **SHOULD** detect unusual API usage patterns
- **SHOULD** detect brute-force attempts
- **MUST** alert on critical security events

**REQ-LOG-004**: Log Security
- **MUST** redact credentials in logs (passwords, API keys, tokens)
- **MUST** protect log integrity (write-once, tamper-evident)
- **MUST** retain logs per compliance requirements (typically 90-365 days)
- **SHOULD** centralize logs in SIEM system
- **MUST** restrict access to logs (authorized personnel only)

---

## 5. Testing Requirements

### 5.1 Security Testing Checklist

#### Manual Code Review:

- [ ] Review authentication logic for bypasses
- [ ] Check session management for fixation/hijacking
- [ ] Verify token validation (expiration, signature, algorithm)
- [ ] Inspect error handling (no information leakage)
- [ ] Check authorization on all protected endpoints
- [ ] Verify CSRF protection on state-changing operations
- [ ] Review secret storage (no hardcoded credentials)
- [ ] Check for SQL injection, XSS (out of scope but related)
- [ ] Verify rate limiting implementation
- [ ] Review logging (no credential logging)

#### Automated Testing:

- [ ] **SAST** (Static Analysis): Detect hardcoded secrets, weak crypto
- [ ] **DAST** (Dynamic Analysis): Test running application for vulnerabilities
- [ ] **Secret Scanning**: Scan code/git history for exposed credentials
- [ ] **Dependency Scanning**: Check for vulnerable libraries
- [ ] **IAST** (Interactive): Runtime vulnerability detection

#### Penetration Testing Scenarios:

- [ ] **Brute Force**: Attempt to guess credentials/API keys
- [ ] **Session Hijacking**: Steal/predict session IDs
- [ ] **Token Manipulation**: Modify JWT claims, algorithm
- [ ] **CSRF**: Craft cross-origin requests
- [ ] **Privilege Escalation**: Attempt horizontal/vertical escalation
- [ ] **Replay Attack**: Reuse captured tokens/requests
- [ ] **Rate Limit Bypass**: Circumvent rate limiting
- [ ] **Account Enumeration**: Determine valid usernames
- [ ] **Session Fixation**: Force victim to use attacker's session
- [ ] **Logout Validation**: Verify tokens/sessions invalidated

---

## 6. Compliance Requirements

### 6.1 Regulatory Compliance

#### PCI DSS (Payment Card Industry):
- **Requirement 8**: Strong authentication and access control
- **Requirement 10**: Logging and monitoring
- Applicable: If handling credit card data

#### GDPR (General Data Protection Regulation):
- **Article 32**: Security of processing (encryption, access control)
- **Article 33**: Breach notification
- Applicable: If processing EU citizens' data

#### HIPAA (Health Insurance Portability and Accountability Act):
- **§164.312(a)**: Access control
- **§164.312(d)**: Authentication
- Applicable: If handling protected health information (PHI)

#### SOC 2 Type II:
- **CC6.1**: Logical and physical access controls
- **CC6.6**: Encryption
- Applicable: For SaaS providers, enterprise software

### 6.2 Industry Standards

#### NIST Cybersecurity Framework:
- **Identify**: Asset/risk management
- **Protect**: Access control, data security
- **Detect**: Continuous monitoring
- **Respond**: Incident response
- **Recover**: Recovery planning

#### CIS Controls:
- **Control 6**: Access Control Management
- **Control 8**: Audit Log Management
- **Control 16**: Application Software Security

---

## 7. Implementation Checklist

### Pre-Development:
- [ ] Threat model created
- [ ] Security requirements defined
- [ ] Architecture reviewed for security
- [ ] Security controls designed

### Development:
- [ ] Authentication implemented per requirements
- [ ] Authorization implemented per requirements
- [ ] Secure session management implemented
- [ ] Rate limiting implemented
- [ ] Logging implemented
- [ ] Error handling reviewed (no information leakage)

### Testing:
- [ ] Unit tests for authentication logic
- [ ] Integration tests for authorization
- [ ] Security testing completed (SAST, DAST, pentest)
- [ ] Peer code review completed
- [ ] All high/critical findings remediated

### Deployment:
- [ ] Secrets stored in vault (not in code/env files)
- [ ] HTTPS enforced
- [ ] Security headers configured
- [ ] Monitoring/alerting configured
- [ ] Incident response plan in place

### Post-Deployment:
- [ ] Security monitoring active
- [ ] Log review process established
- [ ] Key rotation schedule defined
- [ ] Vulnerability management process active
- [ ] Regular security assessments scheduled

---

## 8. References

### Standards & Guidelines:
- **OWASP Top 10**: https://owasp.org/Top10/
- **OWASP ASVS**: Application Security Verification Standard
- **NIST SP 800-63B**: Digital Identity Guidelines (Authentication)
- **RFC 6749**: OAuth 2.0 Authorization Framework
- **RFC 7519**: JSON Web Token (JWT)
- **NIST CSF**: Cybersecurity Framework

### Tools:
- **SAST**: SonarQube, Checkmarx, Semgrep
- **DAST**: OWASP ZAP, Burp Suite
- **Secret Scanning**: git-secrets, truffleHog, GitGuardian
- **Dependency Scanning**: Snyk, Dependabot, npm audit

### Libraries (Node.js/JavaScript):
- **Password Hashing**: `bcrypt`, `argon2`
- **JWT**: `jsonwebtoken` (verify algorithm!)
- **Session**: `express-session`, `connect-redis`
- **Rate Limiting**: `express-rate-limit`, `rate-limiter-flexible`
- **CSRF**: `csurf`, `csrf-csrf`

---

## 9. Document Maintenance

**Review Frequency**: Quarterly or after major security incidents
**Approval**: Security team, engineering leads
**Distribution**: All developers, security team, QA

**Change Log**:
- 2024-11-12: Initial version created for peer review testing

---

## Appendix A: Quick Reference

### Critical Security Checklist:

✅ **Authentication**:
- [ ] Strong password hashing (bcrypt/Argon2)
- [ ] MFA supported and enforced for admins
- [ ] Rate limiting on login (max 5 attempts/15min)

✅ **JWT**:
- [ ] RS256/ES256 algorithm (not HS256 for distributed systems)
- [ ] 256-bit secret minimum
- [ ] Short expiration (5-15 min)
- [ ] Refresh token flow
- [ ] Token revocation on logout

✅ **Sessions**:
- [ ] Cryptographically random session IDs (128-bit min)
- [ ] Session regeneration on login
- [ ] HTTP-only, Secure, SameSite cookies
- [ ] Session timeout (idle + absolute)
- [ ] Server-side session storage

✅ **API Keys**:
- [ ] Cryptographically random (256-bit)
- [ ] Hashed storage (not plaintext)
- [ ] Scope-based authorization
- [ ] Rate limiting per key
- [ ] Usage tracking and anomaly detection
- [ ] Never in client-side code or URLs

✅ **CSRF**:
- [ ] CSRF tokens on state-changing operations
- [ ] SameSite cookie attribute
- [ ] Origin/Referer validation

✅ **Logging**:
- [ ] Log authentication events
- [ ] Log authorization failures
- [ ] Redact credentials in logs
- [ ] Centralized logging and monitoring

---

**End of Security Requirements Document**
