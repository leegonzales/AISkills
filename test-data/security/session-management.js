/**
 * Session Management Module - INSECURE EXAMPLE FOR TESTING
 *
 * This file contains intentionally planted security vulnerabilities
 * for testing peer review detection capabilities.
 *
 * DO NOT USE IN PRODUCTION
 */

const express = require('express');
const crypto = require('crypto');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// In-memory session store
const sessions = new Map();
const users = new Map([
    ['admin', { id: 1, username: 'admin', password: 'admin123', role: 'admin' }],
    ['user', { id: 2, username: 'user', password: 'user123', role: 'user' }]
]);

// VULNERABILITY 1: Predictable session ID counter
let sessionCounter = 1000;

/**
 * VULNERABILITY 2: Session fixation vulnerability
 * Accepts session ID from client before authentication
 */
app.post('/api/login', (req, res) => {
    const { username, password, sessionId } = req.body;

    const user = users.get(username);

    if (!user || user.password !== password) {
        return res.status(401).json({ error: 'Invalid credentials' });
    }

    // PROBLEM: If client provides sessionId, use it without validation
    // Attacker can set a known session ID, then trick user to authenticate
    let sid = sessionId;

    if (!sid) {
        // VULNERABILITY 3: Predictable session IDs (sequential counter)
        sid = `sess_${sessionCounter++}`;
        // Should use: crypto.randomBytes(32).toString('hex')
    }

    // VULNERABILITY 4: Session data stored without encryption
    sessions.set(sid, {
        userId: user.id,
        username: user.username,
        role: user.role,
        createdAt: Date.now(),
        // VULNERABILITY 5: No session expiration tracking
        // lastActivity: Date.now() // Missing
    });

    // VULNERABILITY 6: Session ID in response body instead of secure cookie
    res.json({
        success: true,
        sessionId: sid,
        user: {
            id: user.id,
            username: user.username,
            role: user.role
        }
    });
});

/**
 * VULNERABILITY 7: Session token in URL parameter
 * URLs are logged by servers, proxies, and browser history
 */
app.get('/api/dashboard', (req, res) => {
    // PROBLEM: Session ID in query string instead of header/cookie
    const sessionId = req.query.sessionId;

    if (!sessionId) {
        return res.status(401).json({ error: 'Session required' });
    }

    const session = sessions.get(sessionId);

    if (!session) {
        return res.status(401).json({ error: 'Invalid session' });
    }

    // VULNERABILITY 8: No session timeout check
    // Sessions never expire, even after months of inactivity

    res.json({
        message: 'Dashboard',
        user: session.username,
        sessionCreated: new Date(session.createdAt).toISOString()
    });
});

/**
 * VULNERABILITY 9: No CSRF protection
 * State-changing operations without CSRF token validation
 */
app.post('/api/transfer-funds', validateSession, (req, res) => {
    const { toAccount, amount } = req.body;

    // PROBLEM: No CSRF token validation
    // Attacker can craft malicious form/link to trigger this action
    // if user is authenticated

    // Simulate fund transfer
    console.log(`Transferring ${amount} to ${toAccount} from user ${req.session.username}`);

    res.json({
        success: true,
        message: `Transferred ${amount} to ${toAccount}`
    });
});

/**
 * VULNERABILITY 10: Form with session ID in hidden field (exposed in HTML)
 */
app.get('/api/update-profile-form', (req, res) => {
    const sessionId = req.query.sessionId;

    // PROBLEM: Session ID embedded in HTML form
    // Vulnerable to XSS attacks that can read the form data
    const htmlForm = `
        <form method="POST" action="/api/update-profile">
            <input type="hidden" name="sessionId" value="${sessionId}">
            <input type="text" name="email" placeholder="Email">
            <input type="text" name="phone" placeholder="Phone">
            <button type="submit">Update Profile</button>
        </form>
    `;

    res.send(htmlForm);
});

/**
 * VULNERABILITY 11: Session ID accepted from POST body
 */
app.post('/api/update-profile', (req, res) => {
    const { sessionId, email, phone } = req.body;

    const session = sessions.get(sessionId);

    if (!session) {
        return res.status(401).json({ error: 'Invalid session' });
    }

    // VULNERABILITY 12: No CSRF protection on state-changing operation

    res.json({
        success: true,
        message: 'Profile updated',
        user: session.username
    });
});

/**
 * VULNERABILITY 13: Concurrent session not limited
 * Same user can have unlimited active sessions
 */
app.post('/api/login-multiple', (req, res) => {
    const { username, password } = req.body;

    const user = users.get(username);

    if (!user || user.password !== password) {
        return res.status(401).json({ error: 'Invalid credentials' });
    }

    // PROBLEM: No check for existing sessions
    // User can login from multiple locations without limit
    const sid = `sess_${sessionCounter++}`;

    sessions.set(sid, {
        userId: user.id,
        username: user.username,
        role: user.role,
        createdAt: Date.now()
    });

    res.json({ sessionId: sid });
});

/**
 * VULNERABILITY 14: Session not regenerated after privilege escalation
 */
app.post('/api/elevate-privileges', validateSession, (req, res) => {
    const { adminPassword } = req.body;

    if (adminPassword === 'supersecret') {
        // PROBLEM: Session ID not regenerated after privilege change
        // Same session ID used for both regular and admin access
        req.session.role = 'admin';
        req.session.elevated = true;

        sessions.set(req.sessionId, req.session);

        res.json({
            message: 'Privileges elevated',
            // VULNERABILITY 15: Returning session ID in response
            sessionId: req.sessionId
        });
    } else {
        res.status(403).json({ error: 'Invalid admin password' });
    }
});

/**
 * VULNERABILITY 16: Logout doesn't invalidate session
 */
app.post('/api/logout', (req, res) => {
    const sessionId = req.body.sessionId || req.query.sessionId;

    // PROBLEM: Just returns success without actually destroying session
    // Session remains valid and can be reused

    res.json({ message: 'Logged out successfully' });
});

/**
 * VULNERABILITY 17: Session validation middleware doesn't check expiration
 */
function validateSession(req, res, next) {
    const sessionId = req.body.sessionId || req.query.sessionId || req.headers['x-session-id'];

    if (!sessionId) {
        return res.status(401).json({ error: 'Session required' });
    }

    const session = sessions.get(sessionId);

    if (!session) {
        return res.status(401).json({ error: 'Invalid session' });
    }

    // PROBLEM: No session timeout validation
    // PROBLEM: No session activity update
    // PROBLEM: No device fingerprint validation

    req.session = session;
    req.sessionId = sessionId;
    next();
}

/**
 * VULNERABILITY 18: Cookie settings not secure (if using cookies)
 */
app.post('/api/login-with-cookie', (req, res) => {
    const { username, password } = req.body;

    const user = users.get(username);

    if (!user || user.password !== password) {
        return res.status(401).json({ error: 'Invalid credentials' });
    }

    const sid = `sess_${sessionCounter++}`;

    sessions.set(sid, {
        userId: user.id,
        username: user.username,
        role: user.role,
        createdAt: Date.now()
    });

    // PROBLEM: Cookie without secure, httpOnly, sameSite flags
    res.cookie('sessionId', sid, {
        // Missing: secure: true (HTTPS only)
        // Missing: httpOnly: true (prevent XSS)
        // Missing: sameSite: 'strict' (prevent CSRF)
        maxAge: 365 * 24 * 60 * 60 * 1000 // 1 year - too long!
    });

    res.json({ success: true });
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
    console.log(`Session server running on port ${PORT}`);
});

module.exports = app;
