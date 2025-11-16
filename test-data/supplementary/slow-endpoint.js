/**
 * Performance Test Case: Slow API Endpoint with Multiple Bottlenecks
 *
 * Current Performance: ~2000ms average response time
 * Target Performance: <100ms
 *
 * Issues:
 * 1. N+1 query problem - fetching user data in a loop
 * 2. Inefficient caching - cache check happens after expensive operations
 * 3. Synchronous blocking operations - file I/O blocks event loop
 * 4. Missing database indexes on user_orders.user_id and user_orders.status
 * 5. Large payload - no pagination, returns all orders at once
 */

const express = require('express');
const fs = require('fs');
const crypto = require('crypto');

const app = express();

// Mock database connection
const mockDb = {
  query: async (sql, params) => {
    // Simulate slow query execution
    await new Promise(resolve => setTimeout(resolve, 50));

    if (sql.includes('SELECT * FROM users')) {
      return [{ id: params[0], name: `User ${params[0]}`, email: `user${params[0]}@example.com` }];
    }

    if (sql.includes('SELECT * FROM user_orders')) {
      // Simulate returning 1000 orders (no pagination)
      const orders = [];
      for (let i = 0; i < 1000; i++) {
        orders.push({
          id: i,
          user_id: params[0],
          product_id: Math.floor(Math.random() * 10000),
          status: ['pending', 'processing', 'shipped', 'delivered'][Math.floor(Math.random() * 4)],
          total: Math.random() * 1000,
          created_at: new Date(Date.now() - Math.random() * 365 * 24 * 60 * 60 * 1000)
        });
      }
      return orders;
    }

    if (sql.includes('SELECT * FROM products')) {
      return [{ id: params[0], name: `Product ${params[0]}`, price: Math.random() * 100 }];
    }

    return [];
  }
};

// Mock cache (Redis simulation)
const mockCache = new Map();

/**
 * SLOW ENDPOINT: Get user orders with enriched data
 *
 * This endpoint demonstrates multiple performance anti-patterns:
 * - N+1 queries for user and product data
 * - Cache checked too late in the process
 * - Synchronous file operations
 * - No pagination
 * - Missing database indexes
 */
app.get('/api/users/:userId/orders', async (req, res) => {
  const { userId } = req.params;
  const startTime = Date.now();

  try {
    // ISSUE #1: N+1 Query Problem
    // First, get the user (1 query)
    const userResult = await mockDb.query(
      'SELECT * FROM users WHERE id = ?',
      [userId]
    );
    const user = userResult[0];

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    // Then get all orders for this user (1 query)
    // ISSUE #4: Missing index on user_orders.user_id causes full table scan
    const orders = await mockDb.query(
      'SELECT * FROM user_orders WHERE user_id = ? ORDER BY created_at DESC',
      [userId]
    );

    // ISSUE #5: No pagination - returns all 1000 orders

    // Then for each order, fetch product details (N queries!)
    // This is the classic N+1 problem
    const enrichedOrders = [];
    for (const order of orders) {
      // ISSUE #2: Cache check happens INSIDE the loop, after DB query
      const cacheKey = `product:${order.product_id}`;
      let product = mockCache.get(cacheKey);

      if (!product) {
        // ISSUE #1 continued: Separate query for each product
        const productResult = await mockDb.query(
          'SELECT * FROM products WHERE id = ?',
          [order.product_id]
        );
        product = productResult[0];

        // Cache for 5 minutes
        mockCache.set(cacheKey, product);
        setTimeout(() => mockCache.delete(cacheKey), 5 * 60 * 1000);
      }

      // ISSUE #3: Synchronous blocking file I/O in the event loop
      // This blocks the entire server while reading audit logs
      const auditLogPath = `/tmp/orders/${order.id}.log`;
      let auditLog = null;
      if (fs.existsSync(auditLogPath)) {
        // Synchronous read blocks the event loop
        auditLog = fs.readFileSync(auditLogPath, 'utf8');
      }

      // ISSUE #3 continued: CPU-intensive operation in request handler
      // Calculating hash synchronously
      const orderHash = crypto.createHash('sha256')
        .update(JSON.stringify(order))
        .digest('hex');

      enrichedOrders.push({
        ...order,
        user: {
          id: user.id,
          name: user.name,
          email: user.email
        },
        product: product,
        audit_log: auditLog,
        hash: orderHash
      });
    }

    const responseTime = Date.now() - startTime;

    res.json({
      success: true,
      data: enrichedOrders,
      metadata: {
        user_id: userId,
        total_orders: enrichedOrders.length,
        response_time_ms: responseTime
      }
    });

  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

/**
 * OPTIMIZED VERSION (commented out for comparison)
 *
 * Improvements needed:
 * 1. Use JOIN to fetch user and orders in single query
 * 2. Batch fetch all unique products (eliminate N+1)
 * 3. Check cache BEFORE database queries
 * 4. Use async file operations (fs.promises)
 * 5. Add pagination (limit/offset)
 * 6. Add database indexes:
 *    - CREATE INDEX idx_user_orders_user_id ON user_orders(user_id)
 *    - CREATE INDEX idx_user_orders_status ON user_orders(status)
 * 7. Move CPU-intensive operations to worker threads
 * 8. Use streaming for large responses
 */

/*
app.get('/api/users/:userId/orders/optimized', async (req, res) => {
  const { userId } = req.params;
  const { page = 1, limit = 50 } = req.query;
  const offset = (page - 1) * limit;
  const startTime = Date.now();

  try {
    // Single query with JOIN to get user and orders
    const ordersWithUser = await mockDb.query(`
      SELECT
        u.id as user_id, u.name as user_name, u.email as user_email,
        o.id, o.product_id, o.status, o.total, o.created_at
      FROM user_orders o
      JOIN users u ON o.user_id = u.id
      WHERE u.id = ?
      ORDER BY o.created_at DESC
      LIMIT ? OFFSET ?
    `, [userId, limit, offset]);

    if (ordersWithUser.length === 0) {
      return res.status(404).json({ error: 'User not found or no orders' });
    }

    // Batch fetch all unique products
    const uniqueProductIds = [...new Set(ordersWithUser.map(o => o.product_id))];

    // Check cache first
    const productsMap = new Map();
    const uncachedProductIds = [];

    for (const productId of uniqueProductIds) {
      const cacheKey = `product:${productId}`;
      const cached = mockCache.get(cacheKey);
      if (cached) {
        productsMap.set(productId, cached);
      } else {
        uncachedProductIds.push(productId);
      }
    }

    // Batch query for uncached products
    if (uncachedProductIds.length > 0) {
      const products = await mockDb.query(`
        SELECT * FROM products WHERE id IN (?)
      `, [uncachedProductIds]);

      products.forEach(product => {
        productsMap.set(product.id, product);
        mockCache.set(`product:${product.id}`, product);
      });
    }

    // Use async file operations with Promise.all
    const enrichedOrders = await Promise.all(
      ordersWithUser.map(async (order) => {
        let auditLog = null;
        const auditLogPath = `/tmp/orders/${order.id}.log`;

        try {
          auditLog = await fs.promises.readFile(auditLogPath, 'utf8');
        } catch (err) {
          // File doesn't exist or can't be read
        }

        return {
          id: order.id,
          product_id: order.product_id,
          status: order.status,
          total: order.total,
          created_at: order.created_at,
          user: {
            id: order.user_id,
            name: order.user_name,
            email: order.user_email
          },
          product: productsMap.get(order.product_id),
          audit_log: auditLog
        };
      })
    );

    const responseTime = Date.now() - startTime;

    res.json({
      success: true,
      data: enrichedOrders,
      pagination: {
        page: parseInt(page),
        limit: parseInt(limit),
        total: ordersWithUser.length
      },
      metadata: {
        user_id: userId,
        response_time_ms: responseTime
      }
    });

  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});
*/

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: Date.now() });
});

const PORT = process.env.PORT || 3000;

if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
    console.log(`Test slow endpoint: http://localhost:${PORT}/api/users/1/orders`);
  });
}

module.exports = app;
