/**
 * Testing Strategy Example: Order State Machine with Test Gaps
 *
 * This module implements a complex order state machine for an e-commerce system.
 * Some tests exist, but critical edge cases around concurrent transitions,
 * error handling, and rollbacks are missing.
 *
 * State Transitions:
 * pending -> processing -> shipped -> delivered
 *        \-> cancelled (from pending or processing)
 *        \-> refunded (from any state except pending)
 *        \-> failed (from processing)
 */

const EventEmitter = require('events');

/**
 * Order states with business rules
 */
const OrderState = {
  PENDING: 'pending',           // Order created, payment not confirmed
  PROCESSING: 'processing',     // Payment confirmed, being prepared
  SHIPPED: 'shipped',           // Order dispatched to customer
  DELIVERED: 'delivered',       // Order received by customer
  CANCELLED: 'cancelled',       // Order cancelled by customer or system
  FAILED: 'failed',            // Processing failed (payment, inventory, etc.)
  REFUNDED: 'refunded'         // Order refunded after delivery
};

/**
 * State transition rules
 */
const VALID_TRANSITIONS = {
  [OrderState.PENDING]: [OrderState.PROCESSING, OrderState.CANCELLED, OrderState.FAILED],
  [OrderState.PROCESSING]: [OrderState.SHIPPED, OrderState.CANCELLED, OrderState.FAILED],
  [OrderState.SHIPPED]: [OrderState.DELIVERED, OrderState.REFUNDED],
  [OrderState.DELIVERED]: [OrderState.REFUNDED],
  [OrderState.CANCELLED]: [], // Terminal state
  [OrderState.FAILED]: [],    // Terminal state
  [OrderState.REFUNDED]: []   // Terminal state
};

/**
 * Order class with state machine logic
 */
class Order extends EventEmitter {
  constructor(orderId, userId, items, totalAmount) {
    super();
    this.orderId = orderId;
    this.userId = userId;
    this.items = items;
    this.totalAmount = totalAmount;
    this.state = OrderState.PENDING;
    this.history = [{ state: OrderState.PENDING, timestamp: Date.now(), reason: 'Order created' }];
    this.metadata = {
      createdAt: Date.now(),
      updatedAt: Date.now(),
      version: 1 // For optimistic locking
    };
    this.locks = new Set(); // Track concurrent transitions
  }

  /**
   * Transition to a new state with validation
   *
   * GAPS IN TESTING:
   * - Concurrent transitions (race conditions)
   * - Rollback on partial failure
   * - Event emission failures
   * - Lock acquisition timeout
   * - Version conflicts (optimistic locking)
   */
  async transition(newState, reason, context = {}) {
    // Check if transition is valid
    if (!this.canTransitionTo(newState)) {
      throw new Error(
        `Invalid transition from ${this.state} to ${newState}. ` +
        `Valid transitions: ${VALID_TRANSITIONS[this.state].join(', ')}`
      );
    }

    // CRITICAL: Lock acquisition to prevent concurrent transitions
    // GAP: What happens if lock acquisition times out?
    // GAP: What if two transitions acquire lock simultaneously?
    const lockKey = `transition:${this.orderId}`;
    if (this.locks.has(lockKey)) {
      throw new Error(`Concurrent transition already in progress for order ${this.orderId}`);
    }

    this.locks.add(lockKey);
    const previousState = this.state;

    try {
      // Run pre-transition hooks
      // GAP: What if pre-transition hook throws error?
      await this._runPreTransitionHooks(previousState, newState, context);

      // Perform state transition
      this.state = newState;
      this.metadata.updatedAt = Date.now();
      this.metadata.version += 1;

      // Record transition in history
      this.history.push({
        state: newState,
        previousState: previousState,
        timestamp: Date.now(),
        reason: reason,
        context: context
      });

      // Run post-transition hooks
      // GAP: What if post-transition hook fails? Should we rollback?
      await this._runPostTransitionHooks(previousState, newState, context);

      // Emit state change event
      // GAP: What if event listener throws error?
      this.emit('stateChanged', {
        orderId: this.orderId,
        previousState: previousState,
        newState: newState,
        reason: reason,
        timestamp: Date.now()
      });

      return true;

    } catch (error) {
      // GAP: Rollback strategy not fully tested
      // GAP: What if rollback itself fails?
      await this._rollbackTransition(previousState, error);
      throw new Error(`Transition failed: ${error.message}`);

    } finally {
      this.locks.delete(lockKey);
    }
  }

  /**
   * Check if transition to new state is allowed
   */
  canTransitionTo(newState) {
    return VALID_TRANSITIONS[this.state].includes(newState);
  }

  /**
   * Pre-transition validation and side effects
   *
   * GAPS:
   * - Inventory check failures
   * - Payment gateway timeouts
   * - External API failures
   */
  async _runPreTransitionHooks(from, to, context) {
    // Validate inventory before processing
    if (to === OrderState.PROCESSING) {
      // GAP: What if inventory check times out?
      // GAP: What if inventory changes between check and commit?
      await this._checkInventory();
    }

    // Validate payment before shipping
    if (to === OrderState.SHIPPED) {
      // GAP: What if payment verification fails mid-transition?
      await this._verifyPayment();
    }

    // Check refund eligibility
    if (to === OrderState.REFUNDED) {
      // GAP: What if refund window has passed?
      // GAP: What if payment gateway rejects refund?
      await this._validateRefundEligibility();
    }
  }

  /**
   * Post-transition side effects
   *
   * GAPS:
   * - Notification failures
   * - Webhook delivery failures
   * - Analytics event failures
   */
  async _runPostTransitionHooks(from, to, context) {
    // Send notification to user
    // GAP: Should we fail transition if notification fails?
    try {
      await this._sendNotification(to);
    } catch (error) {
      // GAP: Error handling strategy not tested
      console.error(`Failed to send notification: ${error.message}`);
    }

    // Update inventory
    if (to === OrderState.PROCESSING) {
      // GAP: What if inventory update fails after state change?
      await this._reserveInventory();
    }

    if (to === OrderState.CANCELLED || to === OrderState.FAILED) {
      // GAP: What if inventory release fails?
      await this._releaseInventory();
    }

    // Trigger webhooks for integrations
    // GAP: Webhook delivery retry logic not tested
    try {
      await this._triggerWebhooks(from, to);
    } catch (error) {
      console.error(`Failed to trigger webhooks: ${error.message}`);
    }

    // Record analytics event
    // GAP: Analytics failures should not block transition
    try {
      await this._recordAnalyticsEvent(from, to);
    } catch (error) {
      console.error(`Failed to record analytics: ${error.message}`);
    }
  }

  /**
   * Rollback failed transition
   *
   * CRITICAL GAP: Rollback strategy needs comprehensive testing
   * - What if rollback partially succeeds?
   * - How to handle distributed rollbacks?
   * - Compensation logic for external systems?
   */
  async _rollbackTransition(previousState, error) {
    // Restore previous state
    this.state = previousState;

    // Record failed transition attempt
    this.history.push({
      state: this.state,
      timestamp: Date.now(),
      reason: 'Rollback due to error',
      error: error.message
    });

    // GAP: Should we attempt to undo side effects?
    // GAP: What if rollback compensation fails?

    this.emit('transitionFailed', {
      orderId: this.orderId,
      attemptedState: error.attemptedState,
      error: error.message
    });
  }

  // Mock external dependencies
  async _checkInventory() {
    // Simulate inventory check
    if (Math.random() < 0.05) { // 5% failure rate
      throw new Error('Insufficient inventory');
    }
  }

  async _verifyPayment() {
    // Simulate payment verification
    if (Math.random() < 0.02) { // 2% failure rate
      throw new Error('Payment verification failed');
    }
  }

  async _validateRefundEligibility() {
    const daysSinceDelivery = (Date.now() - this.metadata.createdAt) / (1000 * 60 * 60 * 24);
    if (daysSinceDelivery > 30) {
      throw new Error('Refund window expired');
    }
  }

  async _sendNotification(newState) {
    // Simulate notification service call
    await new Promise(resolve => setTimeout(resolve, 100));
  }

  async _reserveInventory() {
    // Simulate inventory reservation
    await new Promise(resolve => setTimeout(resolve, 50));
  }

  async _releaseInventory() {
    // Simulate inventory release
    await new Promise(resolve => setTimeout(resolve, 50));
  }

  async _triggerWebhooks(from, to) {
    // Simulate webhook delivery
    await new Promise(resolve => setTimeout(resolve, 200));
  }

  async _recordAnalyticsEvent(from, to) {
    // Simulate analytics tracking
    await new Promise(resolve => setTimeout(resolve, 30));
  }

  /**
   * Get order status summary
   */
  getStatus() {
    return {
      orderId: this.orderId,
      state: this.state,
      userId: this.userId,
      totalAmount: this.totalAmount,
      createdAt: this.metadata.createdAt,
      updatedAt: this.metadata.updatedAt,
      version: this.metadata.version
    };
  }

  /**
   * Get transition history
   */
  getHistory() {
    return [...this.history];
  }
}

/**
 * EXISTING TESTS (some coverage, but gaps remain)
 */

// Basic happy path tests
describe('Order State Machine - Happy Path', () => {
  test('should create order in pending state', () => {
    const order = new Order('ORD-001', 'USER-123', [{ id: 1, qty: 2 }], 100.00);
    expect(order.state).toBe(OrderState.PENDING);
  });

  test('should transition from pending to processing', async () => {
    const order = new Order('ORD-002', 'USER-123', [{ id: 1, qty: 2 }], 100.00);
    await order.transition(OrderState.PROCESSING, 'Payment confirmed');
    expect(order.state).toBe(OrderState.PROCESSING);
  });

  test('should complete full order lifecycle', async () => {
    const order = new Order('ORD-003', 'USER-123', [{ id: 1, qty: 2 }], 100.00);
    await order.transition(OrderState.PROCESSING, 'Payment confirmed');
    await order.transition(OrderState.SHIPPED, 'Order dispatched');
    await order.transition(OrderState.DELIVERED, 'Order received');
    expect(order.state).toBe(OrderState.DELIVERED);
  });
});

// Invalid transition tests
describe('Order State Machine - Invalid Transitions', () => {
  test('should reject invalid transition from pending to delivered', async () => {
    const order = new Order('ORD-004', 'USER-123', [{ id: 1, qty: 2 }], 100.00);
    await expect(
      order.transition(OrderState.DELIVERED, 'Invalid')
    ).rejects.toThrow('Invalid transition');
  });

  test('should reject transition from terminal state', async () => {
    const order = new Order('ORD-005', 'USER-123', [{ id: 1, qty: 2 }], 100.00);
    await order.transition(OrderState.CANCELLED, 'Customer cancelled');
    await expect(
      order.transition(OrderState.PROCESSING, 'Invalid')
    ).rejects.toThrow('Invalid transition');
  });
});

/**
 * CRITICAL TEST GAPS TO ADDRESS
 *
 * 1. CONCURRENT TRANSITIONS:
 *    - Two threads trying to transition same order simultaneously
 *    - Lock acquisition timeout scenarios
 *    - Lock release on crash/timeout
 *
 * 2. ERROR HANDLING & ROLLBACK:
 *    - Pre-transition hook failures (inventory, payment)
 *    - Post-transition hook failures (notifications, webhooks)
 *    - Partial rollback failures
 *    - Distributed rollback coordination
 *
 * 3. EDGE CASES:
 *    - Very rapid state transitions (< 1ms apart)
 *    - State changes during hook execution
 *    - Event listener exceptions
 *    - History overflow (1000s of transitions)
 *
 * 4. EXTERNAL DEPENDENCIES:
 *    - Payment gateway timeout/failure
 *    - Inventory service unavailable
 *    - Notification service down
 *    - Webhook endpoint unreachable
 *
 * 5. DATA CONSISTENCY:
 *    - Version conflicts (optimistic locking)
 *    - Race conditions in history recording
 *    - State persistence failures
 *
 * 6. INTEGRATION SCENARIOS:
 *    - Refund after delivery with payment gateway integration
 *    - Cancellation during shipping
 *    - Order modification during processing
 *
 * 7. PERFORMANCE:
 *    - 1000 concurrent orders transitioning
 *    - Memory leak in event listeners
 *    - History cleanup/archival
 */

/**
 * SUGGESTED TEST SCENARIOS
 *
 * Scenario 1: Concurrent Cancellation Race
 * - Customer cancels order
 * - Simultaneously, system auto-cancels (payment failed)
 * - Expected: One succeeds, one gets lock error
 * - Verify: Final state is cancelled, history shows attempt
 *
 * Scenario 2: Rollback on Inventory Failure
 * - Order transitions to processing
 * - Inventory reservation fails mid-transition
 * - Expected: Rollback to pending, inventory not reserved
 * - Verify: Compensating transaction executed
 *
 * Scenario 3: Notification Failure Handling
 * - Order ships successfully
 * - Customer notification fails
 * - Expected: Order stays shipped, error logged
 * - Verify: Retry mechanism triggers
 *
 * Scenario 4: Webhook Delivery Failure
 * - Order delivered
 * - Integration webhook endpoint down
 * - Expected: Order stays delivered, webhook queued for retry
 * - Verify: Dead letter queue populated
 *
 * Scenario 5: Refund After 30 Days
 * - Order delivered 35 days ago
 * - Customer requests refund
 * - Expected: Transition rejected
 * - Verify: Customer notified of policy
 */

module.exports = { Order, OrderState, VALID_TRANSITIONS };
