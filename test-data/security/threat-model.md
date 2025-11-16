# Security Threat Model - Authentication Test Cases

## Overview

This document outlines the threat model for the intentionally vulnerable authentication code examples. These examples are designed to test peer review skills' capability to detect common security vulnerabilities in authentication and authorization systems.

---

## 1. JWT Authentication Threats (`jwt-auth.js`)

### 1.1 Weak Signing Secret

**Vulnerability**: JWT signed with short, predictable secret (`secret123`)

**Attack Vector**:
- Attacker brute-forces the signing secret
- Uses common wordlists and rainbow tables
- Once found, can forge arbitrary tokens

**Impact**: Critical
- Complete authentication bypass
- Privilege escalation to any role
- Ability to impersonate any user

**Detection Indicators**:
- Secret length < 32 characters
- Common words in secret
- Secret not using cryptographically random generation

**Remediation**:
- Use minimum 256-bit (32-byte) cryptographically random secret
- Store secret in secure vault (e.g., AWS Secrets Manager, HashiCorp Vault)
- Rotate secrets periodically
- Use RS256 (asymmetric) instead of HS256 (symmetric)

---

### 1.2 Algorithm Downgrade Attack

**Vulnerability**: Using HS256 (symmetric) instead of RS256 (asymmetric)

**Attack Vector**:
- Attacker obtains signing secret (leaked, brute-forced, or insider threat)
- Can immediately forge tokens
- With RS256, only private key can sign (better separation of concerns)

**Impact**: High
- Single point of failure (secret compromise = total breach)
- All services with access to secret can forge tokens
- Difficult to rotate without downtime

**Detection Indicators**:
- `algorithm: 'HS256'` in jwt.sign()
- Symmetric algorithm used for distributed systems
- Secret shared across multiple services

**Remediation**:
- Use RS256 or ES256 (asymmetric algorithms)
- Keep private key secure, distribute only public key
- Separate signing authority from verification
- Use key management service (KMS)

---

### 1.3 Missing Token Expiration

**Vulnerability**: Tokens issued without expiration time

**Attack Vector**:
- Stolen token remains valid indefinitely
- Lost/forgotten tokens never expire
- Compromised tokens can't be time-limited

**Impact**: High
- Stolen tokens grant permanent access
- No automatic session timeout
- Increased window for token theft/replay attacks

**Detection Indicators**:
- Missing `expiresIn` option in jwt.sign()
- No expiration validation in jwt.verify()
- No token refresh mechanism

**Remediation**:
- Set short expiration (5-15 minutes for access tokens)
- Implement refresh token flow
- Validate expiration on every request
- Monitor for expired token reuse attempts

---

### 1.4 No Token Revocation

**Vulnerability**: Logout doesn't invalidate JWT

**Attack Vector**:
- User logs out, but token still valid
- Attacker with stolen token can continue access
- No way to force logout from all devices

**Impact**: Medium-High
- Compromised tokens can't be revoked
- Logout provides false sense of security
- No kill-switch for breached accounts

**Detection Indicators**:
- Logout only removes local session reference
- No token blacklist/denylist
- No token versioning/rotation on logout

**Remediation**:
- Implement token blacklist (Redis cache)
- Use short-lived tokens + refresh tokens
- Include token version/nonce in payload
- Invalidate all tokens on password change
- Implement "logout all devices" functionality

---

### 1.5 Detailed Error Messages

**Vulnerability**: JWT verification errors leak implementation details

**Attack Vector**:
- Error messages reveal token structure
- Stack traces expose library versions
- Timing attacks on error responses

**Impact**: Low-Medium
- Information disclosure aids attackers
- Reveals technology stack
- Facilitates targeted exploits

**Detection Indicators**:
- Returning `err.message` and `err.stack` to client
- Different error messages for different failure modes
- Detailed validation error messages

**Remediation**:
- Return generic error messages to client
- Log detailed errors server-side only
- Use same error for invalid/expired/malformed tokens
- Implement consistent response times

---

## 2. Session Management Threats (`session-management.js`)

### 2.1 Session Fixation

**Vulnerability**: Accepts session ID from client before authentication

**Attack Vector**:
1. Attacker creates session ID
2. Tricks victim to authenticate with that session ID
3. Attacker now has authenticated session
4. Bypasses authentication entirely

**Impact**: Critical
- Complete authentication bypass
- Attacker-controlled session IDs
- User unknowingly authenticates attacker's session

**Detection Indicators**:
- Session ID accepted in login request body
- No session regeneration after authentication
- Client-provided session ID trusted without validation

**Remediation**:
- Always generate new session ID after successful authentication
- Ignore client-provided session IDs
- Invalidate any pre-auth session on login
- Generate session ID server-side only

---

### 2.2 Predictable Session IDs

**Vulnerability**: Session IDs use sequential counter

**Attack Vector**:
- Attacker observes session ID pattern (`sess_1000`, `sess_1001`, etc.)
- Enumerates valid session IDs
- Hijacks active sessions

**Impact**: Critical
- Trivial session hijacking
- Mass account compromise
- Automated brute-force attacks

**Detection Indicators**:
- Sequential/incremental session IDs
- Timestamp-based session IDs
- Short session IDs (< 128 bits entropy)
- Predictable patterns in ID generation

**Remediation**:
- Use `crypto.randomBytes(32)` for session IDs
- Minimum 128-bit entropy
- Base64/hex encoding for transport
- No predictable components

---

### 2.3 Session ID in URL

**Vulnerability**: Session ID passed as query parameter

**Attack Vector**:
- Session ID logged in server logs, proxy logs
- Session ID in browser history
- Session ID in referrer headers when following links
- Session ID visible in URL bar (shoulder surfing)

**Impact**: High
- Session IDs leaked through multiple channels
- Persistent in logs even after session expires
- Exposed in analytics/monitoring tools

**Detection Indicators**:
- `req.query.sessionId`
- Session ID in GET request URLs
- Session ID in form action URLs

**Remediation**:
- Use HTTP-only secure cookies for session IDs
- Or use Authorization header
- Never include session ID in URL
- Use POST for session-related endpoints

---

### 2.4 Missing CSRF Protection

**Vulnerability**: State-changing operations without CSRF token

**Attack Vector**:
1. User authenticated to vulnerable site
2. User visits attacker's site
3. Attacker's site makes request to vulnerable site
4. Browser includes session cookie
5. Unauthorized action performed

**Impact**: High
- Unauthorized fund transfers
- Account settings changes
- Privilege escalation
- Data modification

**Detection Indicators**:
- No CSRF token validation on POST/PUT/DELETE
- State-changing operations in GET requests
- Missing `sameSite` cookie attribute
- No origin/referer validation

**Remediation**:
- Implement CSRF token (synchronizer token pattern)
- Set cookie `sameSite: 'strict'` or `'lax'`
- Validate Origin/Referer headers
- Use custom headers (require preflight)
- Double-submit cookie pattern

---

### 2.5 No Session Timeout

**Vulnerability**: Sessions never expire

**Attack Vector**:
- Old sessions remain valid indefinitely
- Stolen session used months later
- Shared computer sessions not cleaned up

**Impact**: Medium-High
- Unlimited attack window
- Increased risk from session theft
- Abandoned sessions accessible

**Detection Indicators**:
- No session expiration check
- No `maxAge` or `expiresAt` tracking
- No inactivity timeout
- No absolute timeout

**Remediation**:
- Implement idle timeout (15-30 minutes)
- Implement absolute timeout (24 hours max)
- Track `lastActivity` timestamp
- Prompt for re-authentication after timeout

---

### 2.6 Insecure Cookie Configuration

**Vulnerability**: Cookies without `secure`, `httpOnly`, `sameSite` flags

**Attack Vector**:
- **No `httpOnly`**: XSS can steal session cookie
- **No `secure`**: Cookie sent over HTTP (MITM attack)
- **No `sameSite`**: CSRF attacks possible

**Impact**: High
- Session hijacking via XSS
- Session theft via network sniffing
- CSRF attacks

**Detection Indicators**:
```javascript
res.cookie('sessionId', sid, {
    // Missing flags
});
```

**Remediation**:
```javascript
res.cookie('sessionId', sid, {
    httpOnly: true,    // Prevent XSS
    secure: true,      // HTTPS only
    sameSite: 'strict', // Prevent CSRF
    maxAge: 3600000    // 1 hour
});
```

---

## 3. API Key Authentication Threats (`api-auth.js`)

### 3.1 API Keys in Client-Side Code

**Vulnerability**: API key embedded in JavaScript file

**Attack Vector**:
- User views page source
- API key visible in `.js` file
- Attacker extracts and uses key
- No way to track who leaked it

**Impact**: Critical
- Complete API access compromise
- Keys shared publicly on GitHub
- Unable to identify legitimate vs malicious use
- API abuse, data exfiltration

**Detection Indicators**:
- API key in response body sent to client
- Key in `<script>` tag or `.js` file
- Key in HTML comments
- Key in mobile app code

**Remediation**:
- Never send API keys to client
- Use backend proxy for API calls
- Implement OAuth/JWT for client auth
- Use temporary tokens with limited scope

---

### 3.2 No Rate Limiting

**Vulnerability**: Unlimited API requests allowed

**Attack Vector**:
- Brute-force key enumeration
- Denial of service attacks
- Resource exhaustion
- Cost amplification (cloud billing)

**Impact**: High
- Service degradation/outage
- Unexpected costs
- Key discovery through brute force
- API abuse

**Detection Indicators**:
- No rate limiting middleware
- No request throttling
- No quota enforcement
- No usage tracking

**Remediation**:
- Implement rate limiting per key (e.g., 100 req/min)
- Use token bucket or sliding window algorithm
- Return 429 (Too Many Requests) when exceeded
- Track usage per key for analytics/billing
- Consider geographic/IP-based rate limits

---

### 3.3 API Keys in URL Parameters

**Vulnerability**: API key passed as query parameter

**Attack Vector**:
- Keys logged in server/proxy/CDN logs
- Keys in browser history
- Keys in referrer headers
- Keys visible to browser extensions
- Keys in bookmarks

**Impact**: High
- Persistent key exposure in logs
- Keys leaked to third parties via referrer
- Keys accessible to malicious extensions

**Detection Indicators**:
```javascript
// Bad
GET /api/data?api_key=ak_1234567890
```

**Remediation**:
```javascript
// Good
GET /api/data
Headers: {
    'X-API-Key': 'ak_1234567890'
}
```
- Use custom header or Authorization header
- Never include credentials in URL
- Sanitize logs to redact headers

---

### 3.4 Plaintext API Key Logging

**Vulnerability**: API keys logged to console/files

**Attack Vector**:
- Logs stored in centralized logging system
- Logs accessible to support/ops teams
- Logs backed up and retained
- Logs exported for analysis

**Impact**: Medium-High
- Keys accessible to internal actors
- Keys in log aggregation systems
- Keys in backups
- Increased blast radius

**Detection Indicators**:
```javascript
console.log(`Request from API key: ${apiKey}`);
```

**Remediation**:
- Redact API keys in logs
- Log only last 4 characters or hash
- Use structured logging with field-level redaction
- Implement log scrubbing

---

### 3.5 No Key Rotation

**Vulnerability**: API keys never expire or rotate

**Attack Vector**:
- Compromised key remains valid forever
- No forced rotation on breach
- Keys leaked years ago still work
- Can't sunset old integration

**Impact**: Medium-High
- Unlimited validity of compromised keys
- No mechanism to force upgrades
- Difficult to deprecate old API versions

**Detection Indicators**:
- No `expiresAt` field on keys
- No rotation mechanism
- No deprecation warnings
- No key versioning

**Remediation**:
- Set expiration on API keys (90-365 days)
- Implement key rotation API endpoint
- Warn before expiration
- Support overlapping keys during rotation
- Track key age and usage

---

### 3.6 Insufficient Scope Validation

**Vulnerability**: API keys not restricted by scope/permissions

**Attack Vector**:
- Read-only key used for write operations
- Key with limited scope exceeds permissions
- Single key has god-mode access

**Impact**: High
- Principle of least privilege violated
- Compromised key has excessive permissions
- No defense in depth

**Detection Indicators**:
- No scope checking in endpoints
- All keys have same permissions
- No role-based access control

**Remediation**:
- Implement scope-based authorization
- Check `key.scopes` includes required permission
- Use granular scopes (read:users, write:posts, etc.)
- Deny by default, allow explicitly

---

### 3.7 No Usage Tracking

**Vulnerability**: API key usage not monitored

**Attack Vector**:
- Compromised key used without detection
- Anomalous usage patterns not flagged
- No audit trail for investigation

**Impact**: Medium
- Delayed breach detection
- Difficult to identify compromised keys
- No forensics data

**Detection Indicators**:
- No tracking of last used timestamp
- No request count per key
- No IP address logging
- No geographic tracking

**Remediation**:
- Track key usage metrics (requests, bytes, errors)
- Monitor for anomalies (new IPs, countries, usage spikes)
- Alert on suspicious patterns
- Implement key usage dashboard

---

### 3.8 Hardcoded Master Keys

**Vulnerability**: Master API key hardcoded in source

**Attack Vector**:
- Key committed to git repository
- Key visible in source code
- Key in public GitHub repos
- Key in container images

**Impact**: Critical
- God-mode access exposed
- Keys in git history (hard to remove)
- Keys distributed in builds

**Detection Indicators**:
```javascript
const MASTER_API_KEY = 'ak_master_9876543210';
```

**Remediation**:
- Use environment variables for secrets
- Use secret management service (Vault, AWS Secrets Manager)
- Scan repos for secrets (git-secrets, truffleHog)
- Rotate immediately if exposed

---

### 3.9 CORS Misconfiguration

**Vulnerability**: Allow all origins with credentials

**Attack Vector**:
- Malicious website makes API request
- Browser includes API key from victim's storage
- Attacker receives sensitive data

**Impact**: High
- Cross-origin data theft
- API key theft from localStorage/sessionStorage

**Detection Indicators**:
```javascript
res.header('Access-Control-Allow-Origin', '*');
res.header('Access-Control-Allow-Credentials', 'true'); // Dangerous combo!
```

**Remediation**:
- Whitelist specific origins
- Don't use `*` with credentials
- Validate Origin header
- Consider not allowing credentials at all for API keys

---

## 4. Cross-Cutting Concerns

### 4.1 Information Disclosure

**Severity**: Low-Medium across all modules

**Manifestations**:
- Detailed error messages
- Stack traces in responses
- Library version exposure
- Technology stack disclosure

**Remediation**:
- Generic error messages to client
- Detailed errors only in server logs
- Disable stack traces in production
- Remove version headers

---

### 4.2 Insufficient Logging & Monitoring

**Severity**: Medium across all modules

**Manifestations**:
- No audit trail
- Missing security events
- No anomaly detection

**Remediation**:
- Log authentication events
- Log authorization failures
- Monitor for brute force
- Alert on suspicious patterns

---

### 4.3 Missing HTTPS Enforcement

**Severity**: High across all modules

**Manifestations**:
- Credentials sent over HTTP
- No redirect to HTTPS
- No HSTS header

**Remediation**:
- Enforce HTTPS at load balancer
- Redirect HTTP to HTTPS
- Set HSTS header
- Use secure cookies

---

## 5. Expected Peer Review Findings

A comprehensive security review should identify:

### Critical Findings (Must Fix):
1. Weak JWT signing secret
2. Session fixation vulnerability
3. API keys in client-side code
4. Predictable session IDs
5. No token/session expiration
6. Hardcoded secrets

### High Findings (Should Fix):
7. Missing CSRF protection
8. Session ID in URLs
9. No rate limiting
10. Insecure cookie configuration
11. API keys in URL parameters
12. Missing scope validation

### Medium Findings (Consider Fixing):
13. No usage tracking/monitoring
14. Detailed error messages
15. No key rotation mechanism
16. Plaintext storage of secrets
17. No concurrent session limits

### Low Findings (Nice to Have):
18. Missing security headers
19. Verbose logging
20. No geographic restrictions
21. Missing audit trail

---

## 6. Testing Methodology

### 6.1 Automated Detection

Expected tool findings:
- **SAST**: Hardcoded secrets, weak crypto
- **DAST**: Missing security headers, CSRF
- **Secret scanners**: API keys in code
- **Dependency scanners**: Vulnerable libraries

### 6.2 Manual Review Checklist

- [ ] Review authentication logic
- [ ] Check session management
- [ ] Verify token handling
- [ ] Inspect error handling
- [ ] Test authorization checks
- [ ] Examine logging practices
- [ ] Check crypto implementations
- [ ] Review secret storage

### 6.3 Penetration Testing Scenarios

1. **Token Theft & Reuse**: Extract token, use after logout
2. **Session Hijacking**: Predict session ID, hijack session
3. **CSRF Attack**: Craft malicious form, trick authenticated user
4. **Key Enumeration**: Brute-force API keys
5. **Privilege Escalation**: Modify JWT role claim
6. **Replay Attack**: Reuse captured authentication request

---

## 7. Risk Scoring Matrix

| Vulnerability | Exploitability | Impact | Overall Risk |
|---------------|----------------|---------|--------------|
| Weak JWT secret | High | Critical | Critical |
| Session fixation | Medium | Critical | Critical |
| API key in client | High | High | Critical |
| Predictable session ID | High | Critical | Critical |
| No CSRF protection | Medium | High | High |
| No rate limiting | High | Medium | High |
| Session in URL | Low | High | Medium |
| No expiration | Medium | Medium | Medium |
| Information disclosure | High | Low | Medium |

---

## 8. Compliance Impact

### OWASP Top 10 2021 Mapping:

- **A01 - Broken Access Control**: Session fixation, missing authorization
- **A02 - Cryptographic Failures**: Weak secrets, plaintext storage
- **A03 - Injection**: Not demonstrated (out of scope)
- **A04 - Insecure Design**: No security controls designed in
- **A05 - Security Misconfiguration**: CORS, cookies, error handling
- **A06 - Vulnerable Components**: Not demonstrated
- **A07 - Authentication Failures**: All JWT/session vulnerabilities
- **A08 - Software & Data Integrity**: No token validation
- **A09 - Logging & Monitoring**: Missing audit logs
- **A10 - SSRF**: Not demonstrated

### Regulatory Compliance:

- **PCI DSS**: Multiple violations (encryption, access control, logging)
- **GDPR**: Insufficient protection of personal data access
- **SOC 2**: Inadequate security controls, monitoring
- **HIPAA**: Insufficient access controls for PHI

---

## Conclusion

These test cases provide a comprehensive set of realistic vulnerabilities that should be detectable through:
1. Automated security scanning tools
2. Manual peer code review
3. Security-focused testing

The threat model establishes clear expectations for what a mature security review process should identify and prioritize for remediation.
