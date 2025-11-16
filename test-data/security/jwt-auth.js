/**
 * JWT Authentication Module - INSECURE EXAMPLE FOR TESTING
 *
 * This file contains intentionally planted security vulnerabilities
 * for testing peer review detection capabilities.
 *
 * DO NOT USE IN PRODUCTION
 */

const jwt = require('jsonwebtoken');
const express = require('express');
const app = express();

app.use(express.json());

// VULNERABILITY 1: Weak signing secret - short and predictable
const JWT_SECRET = 'secret123';

// VULNERABILITY 2: Using HS256 instead of RS256
// HS256 is symmetric - anyone with the secret can forge tokens
const JWT_ALGORITHM = 'HS256';

// In-memory store for demo purposes
const users = new Map([
    ['admin', { id: 1, username: 'admin', password: 'password123', role: 'admin' }],
    ['user', { id: 2, username: 'user', password: 'password456', role: 'user' }]
]);

const activeSessions = new Set();

/**
 * Login endpoint
 * VULNERABILITY 3: No rate limiting on login attempts
 */
app.post('/api/login', (req, res) => {
    const { username, password } = req.body;

    const user = users.get(username);

    // Plain text password comparison (another issue, but not focus here)
    if (!user || user.password !== password) {
        return res.status(401).json({ error: 'Invalid credentials' });
    }

    // VULNERABILITY 4: No token expiration set
    // Tokens live forever if not manually revoked
    const token = jwt.sign(
        {
            userId: user.id,
            username: user.username,
            role: user.role
        },
        JWT_SECRET,
        { algorithm: JWT_ALGORITHM }
        // Missing: expiresIn option
    );

    // VULNERABILITY 5: No refresh token mechanism
    // Users must stay logged in indefinitely or re-authenticate

    // Log sensitive data
    console.log(`User ${username} logged in with token: ${token}`);

    activeSessions.add(token);

    res.json({
        token,
        user: {
            id: user.id,
            username: user.username,
            role: user.role
        }
    });
});

/**
 * Protected endpoint
 * VULNERABILITY 6: No token expiration validation
 */
app.get('/api/protected', authenticateToken, (req, res) => {
    res.json({
        message: 'Access granted',
        user: req.user
    });
});

/**
 * Logout endpoint
 * VULNERABILITY 7: Tokens not invalidated on logout
 * Token remains valid even after logout
 */
app.post('/api/logout', authenticateToken, (req, res) => {
    // This only removes from local set, but token is still valid
    activeSessions.delete(req.token);

    // PROBLEM: The JWT itself is still valid and can be reused
    // There's no server-side token blacklist or expiration enforcement

    res.json({ message: 'Logged out successfully' });
});

/**
 * Middleware to authenticate JWT token
 * VULNERABILITY 8: No token blacklist check
 * VULNERABILITY 9: Accepts tokens without expiration
 */
function authenticateToken(req, res, next) {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];

    if (!token) {
        return res.status(401).json({ error: 'Token required' });
    }

    try {
        // VULNERABILITY 10: No algorithm verification
        // Attacker could change algorithm to 'none'
        const decoded = jwt.verify(token, JWT_SECRET);

        // VULNERABILITY 11: No expiration check even if exp claim exists
        // Should verify: if (decoded.exp && decoded.exp < Date.now() / 1000)

        req.user = decoded;
        req.token = token;
        next();
    } catch (err) {
        // VULNERABILITY 12: Detailed error messages leak information
        return res.status(403).json({
            error: 'Token validation failed',
            details: err.message,
            stack: err.stack
        });
    }
}

/**
 * Admin-only endpoint
 * VULNERABILITY 13: Role stored in JWT payload (client-controlled)
 * User could modify their own token to escalate privileges
 */
app.get('/api/admin', authenticateToken, (req, res) => {
    if (req.user.role !== 'admin') {
        return res.status(403).json({ error: 'Admin access required' });
    }

    res.json({
        message: 'Admin panel',
        users: Array.from(users.values()).map(u => ({
            id: u.id,
            username: u.username,
            role: u.role
        }))
    });
});

/**
 * Token refresh endpoint - MISSING ENTIRELY
 * VULNERABILITY 14: No token refresh mechanism
 * Users must either:
 * - Use tokens that never expire (security risk)
 * - Re-authenticate frequently (poor UX)
 */

/**
 * Password reset endpoint
 * VULNERABILITY 15: Reset token in URL (logged in server/proxy logs)
 */
app.post('/api/reset-password/:resetToken', (req, res) => {
    const { resetToken } = req.params;
    const { newPassword } = req.body;

    // Reset token should be in request body, not URL
    // URL parameters are logged and cached

    res.json({ message: 'Password reset successful' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
    console.log(`JWT Secret: ${JWT_SECRET}`); // VULNERABILITY 16: Logging secrets
});

module.exports = app;
