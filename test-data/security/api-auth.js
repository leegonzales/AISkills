/**
 * API Key Authentication Module - INSECURE EXAMPLE FOR TESTING
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

// VULNERABILITY 1: API keys stored in plain text
const apiKeys = new Map([
    ['ak_1234567890abcdef', {
        userId: 1,
        name: 'admin-key',
        scopes: ['read', 'write', 'delete'],
        createdAt: '2024-01-01'
    }],
    ['ak_test123', {
        userId: 2,
        name: 'test-key',
        scopes: ['read'],
        createdAt: '2024-01-15'
    }]
]);

// VULNERABILITY 2: Hardcoded API key in source code
const MASTER_API_KEY = 'ak_master_9876543210';

/**
 * VULNERABILITY 3: API key exposed in client-side JavaScript
 */
app.get('/api/client-config.js', (req, res) => {
    // PROBLEM: API key embedded in JavaScript file served to client
    const clientScript = `
        const API_CONFIG = {
            baseUrl: 'https://api.example.com',
            apiKey: 'ak_1234567890abcdef', // EXPOSED!
            timeout: 5000
        };

        // Client makes requests with API key in header
        fetch(API_CONFIG.baseUrl + '/data', {
            headers: {
                'X-API-Key': API_CONFIG.apiKey
            }
        });
    `;

    res.type('application/javascript');
    res.send(clientScript);
});

/**
 * VULNERABILITY 4: No rate limiting on API endpoints
 * Allows brute force attacks and DoS
 */
app.get('/api/data', authenticateApiKey, (req, res) => {
    // PROBLEM: No rate limiting
    // Attacker can make unlimited requests

    res.json({
        data: 'Sensitive information',
        user: req.apiKey.name
    });
});

/**
 * VULNERABILITY 5: API key in URL query parameter
 * Keys logged in server logs, proxy logs, browser history
 */
app.get('/api/public-data', (req, res) => {
    // PROBLEM: API key in query string
    const apiKey = req.query.api_key;

    if (!apiKey) {
        return res.status(401).json({ error: 'API key required' });
    }

    if (!apiKeys.has(apiKey) && apiKey !== MASTER_API_KEY) {
        return res.status(401).json({ error: 'Invalid API key' });
    }

    // Log request with API key
    console.log(`Request from API key: ${apiKey}`); // VULNERABILITY 6: Logging API keys

    res.json({ data: 'Public information' });
});

/**
 * VULNERABILITY 7: Insufficient key rotation
 * No expiration or rotation mechanism
 */
app.post('/api/create-key', (req, res) => {
    const { userId, name, scopes } = req.body;

    // PROBLEM: Keys created without expiration
    // PROBLEM: No key rotation policy
    const newKey = `ak_${crypto.randomBytes(8).toString('hex')}`;

    apiKeys.set(newKey, {
        userId,
        name,
        scopes: scopes || ['read'],
        createdAt: new Date().toISOString()
        // Missing: expiresAt, rotateAfter, lastRotated
    });

    // VULNERABILITY 8: API key returned in response (should only show once)
    res.json({
        success: true,
        apiKey: newKey,
        message: 'API key created'
    });
});

/**
 * VULNERABILITY 9: No scope validation
 * Keys can access endpoints beyond their intended scope
 */
app.delete('/api/delete-user/:userId', authenticateApiKey, (req, res) => {
    const { userId } = req.params;

    // PROBLEM: No check if API key has 'delete' scope
    // Any valid API key can delete users

    console.log(`Deleting user ${userId}`);

    res.json({
        success: true,
        message: `User ${userId} deleted`
    });
});

/**
 * VULNERABILITY 10: API key sent over unencrypted connection
 */
app.get('/api/insecure-endpoint', (req, res) => {
    // PROBLEM: No enforcement of HTTPS
    // API keys transmitted in plain text over HTTP

    const apiKey = req.headers['x-api-key'];

    if (!apiKey) {
        return res.status(401).json({ error: 'API key required' });
    }

    res.json({
        message: 'This endpoint should require HTTPS',
        protocol: req.protocol
    });
});

/**
 * VULNERABILITY 11: Predictable API key format
 * Easy for attackers to guess valid keys
 */
function generateWeakApiKey(userId) {
    // PROBLEM: Predictable pattern
    return `ak_user${userId}_${Date.now()}`;
    // Attacker can enumerate: ak_user1_*, ak_user2_*, etc.
}

/**
 * VULNERABILITY 12: No API key revocation mechanism
 */
app.post('/api/revoke-key', (req, res) => {
    const { apiKey } = req.body;

    // PROBLEM: Just deletes from Map, but doesn't track revocation
    // No revocation list, no audit trail
    apiKeys.delete(apiKey);

    res.json({ message: 'Key revoked' });
});

/**
 * VULNERABILITY 13: Error messages leak information
 */
app.get('/api/check-key', (req, res) => {
    const apiKey = req.headers['x-api-key'];

    if (!apiKey) {
        return res.status(401).json({
            error: 'API key missing',
            hint: 'Include X-API-Key header' // Information leakage
        });
    }

    const keyData = apiKeys.get(apiKey);

    if (!keyData) {
        // PROBLEM: Detailed error reveals key format and existence
        return res.status(401).json({
            error: 'Invalid API key',
            format: 'Expected format: ak_[16 hex chars]',
            received: apiKey,
            suggestion: 'Check your API key in the dashboard'
        });
    }

    // VULNERABILITY 14: Returning sensitive key metadata
    res.json({
        valid: true,
        keyInfo: keyData // Contains userId, internal name, all scopes
    });
});

/**
 * VULNERABILITY 15: No key usage tracking
 * Can't detect compromised keys
 */
function authenticateApiKey(req, res, next) {
    const apiKey = req.headers['x-api-key'];

    if (!apiKey) {
        return res.status(401).json({ error: 'API key required' });
    }

    const keyData = apiKeys.get(apiKey);

    if (!keyData && apiKey !== MASTER_API_KEY) {
        return res.status(401).json({ error: 'Invalid API key' });
    }

    // PROBLEM: No tracking of:
    // - IP addresses
    // - Request count
    // - Last used timestamp
    // - Geographic location
    // - Anomalous usage patterns

    req.apiKey = keyData || { name: 'master', scopes: ['*'] };
    next();
}

/**
 * VULNERABILITY 16: API keys with unlimited scope
 */
app.post('/api/create-master-key', (req, res) => {
    const { adminPassword } = req.body;

    if (adminPassword === 'admin123') { // Weak check
        // PROBLEM: Creating API key with god-mode access
        const masterKey = `ak_master_${crypto.randomBytes(8).toString('hex')}`;

        apiKeys.set(masterKey, {
            userId: 0,
            name: 'master-key',
            scopes: ['*'], // All permissions
            admin: true,
            createdAt: new Date().toISOString()
        });

        res.json({
            masterKey, // VULNERABILITY 17: Returning master key in response
            warning: 'This key has unlimited access. Keep it secure!'
        });
    } else {
        res.status(403).json({ error: 'Invalid admin password' });
    }
});

/**
 * VULNERABILITY 18: API keys stored in environment variables
 * Exposed through /proc, process managers, logs
 */
const ENV_API_KEY = process.env.API_KEY || 'ak_default_insecure';

app.get('/api/env-config', (req, res) => {
    // PROBLEM: Exposing environment configuration
    res.json({
        apiKey: ENV_API_KEY, // Leaked!
        nodeEnv: process.env.NODE_ENV,
        port: process.env.PORT
    });
});

/**
 * VULNERABILITY 19: CORS misconfiguration allows key theft
 */
app.use((req, res, next) => {
    // PROBLEM: Allows all origins to make requests
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', '*');
    res.header('Access-Control-Allow-Methods', '*');

    // Malicious site can make requests with user's API key
    next();
});

/**
 * VULNERABILITY 20: API keys in git repository
 * Check .env.example, config files, etc.
 */
const DEFAULT_KEYS = {
    development: 'ak_dev_1234567890',
    staging: 'ak_staging_abcdefgh',
    production: 'ak_prod_zyxwvuts' // Committed to git!
};

const PORT = process.env.PORT || 3002;
app.listen(PORT, () => {
    console.log(`API Auth server running on port ${PORT}`);
    console.log(`Master API Key: ${MASTER_API_KEY}`); // VULNERABILITY 21: Logging secrets
});

module.exports = app;
