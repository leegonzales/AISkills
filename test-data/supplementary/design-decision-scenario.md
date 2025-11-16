# Design Decision Scenario: Caching Strategy for E-commerce Product Catalog

## Context

**Project:** High-traffic e-commerce platform product catalog service
**Scale:** 1,000,000 products across 50+ categories
**Traffic:** 10,000 requests/second peak load
**Uptime SLA:** 99.9% (8.76 hours downtime/year maximum)
**Current State:** PostgreSQL database with read replicas struggling under load

## Problem Statement

The product catalog service is experiencing performance degradation during peak shopping periods (Black Friday, Cyber Monday, holiday season). Database read replicas are hitting connection limits, and page load times are increasing from 200ms to 5+ seconds during traffic spikes.

**Current Pain Points:**
- Database CPU utilization reaching 95% during peak hours
- Connection pool exhaustion (500/500 connections used)
- Slow query log showing product detail queries taking 2-3 seconds
- Read replica lag increasing to 30+ seconds
- Cart abandonment rate increasing 40% during slow periods
- CDN costs $15,000/month but only handles static assets

## Requirements

### Functional Requirements
- Cache product details (name, description, price, availability, images)
- Support real-time inventory updates (within 5 seconds)
- Handle flash sale scenarios (1000s of concurrent requests for same product)
- Cache invalidation when products are updated
- Support multi-region deployment (US, EU, APAC)
- Maintain cache consistency across regions

### Non-Functional Requirements
- **Performance:** <100ms p95 response time
- **Availability:** 99.9% uptime (aligned with SLA)
- **Scalability:** Support 10,000 req/sec, plan for 50,000 req/sec growth
- **Cost:** Keep total caching costs under $5,000/month
- **Complexity:** Solution must be maintainable by current 5-person team

### Data Characteristics
- **Product data size:** Average 50KB per product (JSON)
- **Update frequency:**
  - 5,000 products updated daily (prices, inventory)
  - 100 new products added daily
  - 50 products removed daily (out of stock)
- **Access pattern:**
  - 20/80 rule: 20% of products account for 80% of traffic
  - Homepage: Top 100 products
  - Category pages: 50 products per page
  - Search results: 20 products per page
  - Product detail: Single product

## Options to Evaluate

### Option 1: Redis Cluster

**Description:**
Deploy Redis cluster with primary-replica topology across three availability zones.

**Architecture:**
- 6-node Redis cluster (3 primaries, 3 replicas)
- Client-side sharding based on product_id
- TTL-based expiration (30 minutes)
- Write-through cache pattern

**Pros:**
- High performance (sub-millisecond reads)
- Rich data structures (hashes, sorted sets for category indexes)
- Built-in replication and persistence
- Active community and mature tooling
- Team has 2 years experience with Redis

**Cons:**
- Additional infrastructure to manage
- Memory costs for 1M products × 50KB = 50GB minimum
- Potential data loss on failover (async replication)
- Cache stampede risk during invalidations
- Single-region solution (multi-region adds complexity)

**Estimated Cost:**
- AWS ElastiCache: 6 × cache.r6g.2xlarge = $3,600/month
- Data transfer: ~$800/month
- **Total: $4,400/month**

**Complexity:** Medium
**Team Expertise:** High (team already uses Redis for sessions)

---

### Option 2: Memcached Cluster

**Description:**
Distributed Memcached cluster with consistent hashing.

**Architecture:**
- 8-node Memcached cluster
- Consistent hashing for key distribution
- Cache-aside pattern
- No persistence (pure cache)

**Pros:**
- Simpler than Redis (fewer features = less complexity)
- Lower memory overhead (no persistence)
- Excellent horizontal scaling
- Battle-tested at scale (Facebook, Twitter origins)
- Lower cost than Redis

**Cons:**
- No persistence (cold start after restart)
- Limited data structures (key-value only)
- No built-in replication (client handles failover)
- Team has no Memcached experience
- No support for cache patterns like pub/sub for invalidation

**Estimated Cost:**
- AWS ElastiCache: 8 × cache.t3.large = $2,400/month
- Data transfer: ~$600/month
- **Total: $3,000/month**

**Complexity:** Low-Medium
**Team Expertise:** None (requires learning)

---

### Option 3: In-Memory Application Cache

**Description:**
Implement in-memory caching within Node.js application servers using LRU cache.

**Architecture:**
- Each application server maintains local cache
- LRU eviction policy (limit to 2GB per instance)
- Background worker polls database for updates
- 30-second polling interval

**Pros:**
- No additional infrastructure
- Zero network latency (local memory)
- Simple implementation with node-cache library
- No external dependencies
- Lowest cost

**Cons:**
- Cache inconsistency across application servers
- Memory pressure on application servers
- Cold cache on each deployment
- Limited cache size per instance
- No cache sharing between servers
- Scaling issues (more servers = more memory)

**Estimated Cost:**
- Memory overhead: ~2GB per app server (16 servers) = 32GB
- No additional infrastructure costs
- **Total: $0/month** (marginal CPU/memory increase)

**Complexity:** Low
**Team Expertise:** High (already using in-memory caching for config)

---

### Option 4: CDN with Edge Caching

**Description:**
Leverage CDN (Cloudflare/Fastly) for edge caching of product API responses.

**Architecture:**
- Serve product catalog API through CDN
- Cache-Control headers set to 5 minutes
- Purge API calls for cache invalidation
- Stale-while-revalidate for availability

**Pros:**
- Global distribution (multi-region by default)
- Reduces origin load significantly
- DDoS protection included
- Team already uses CDN for static assets
- Instant cache invalidation via API

**Cons:**
- Cannot cache personalized data (prices by region, user-specific)
- Higher costs for API responses vs. static assets
- Limited control over cache behavior
- Debugging cache issues is harder
- Vendor lock-in

**Estimated Cost:**
- Cloudflare Workers: $5/month base + $0.50/million requests
- 10,000 req/sec × 86,400 sec/day × 30 days = 25.9B requests/month
- **Total: ~$13,000/month** (exceeds budget)

**Complexity:** Low
**Team Expertise:** Medium (CDN experience with static assets only)

---

## Trade-offs to Evaluate

### Performance vs. Cost
- Redis: Best performance, moderate cost
- Memcached: Good performance, lowest infrastructure cost
- In-memory: Best latency, hidden costs in scaling
- CDN: Great for cacheable content, expensive for API

### Consistency vs. Availability
- Redis: Strong consistency within cluster, eventual across regions
- Memcached: No consistency guarantees
- In-memory: Weak consistency (30s lag)
- CDN: Stale-while-revalidate trades consistency for availability

### Complexity vs. Control
- Redis: More complex but powerful features
- Memcached: Simpler but limited
- In-memory: Simplest but least scalable
- CDN: Simple but less control

### Operational Burden
- Redis: Requires monitoring, backups, failover testing
- Memcached: Less operational burden (no persistence)
- In-memory: Minimal ops (bundled with app)
- CDN: Lowest ops burden (managed service)

## Constraints

1. **Team Expertise:** 5 engineers, 2 with Redis experience, none with Memcached
2. **Budget:** $5,000/month maximum for caching infrastructure
3. **Timeline:** Must be production-ready in 6 weeks
4. **Migration Risk:** Cannot afford downtime during migration
5. **Compliance:** Must support GDPR (EU data residency)
6. **Existing Stack:** Node.js, PostgreSQL, AWS, Cloudflare CDN

## Current System Details

**Database:**
- PostgreSQL 14
- Primary: db.r5.4xlarge (16 vCPU, 128GB RAM)
- 3× Read Replicas: db.r5.2xlarge (8 vCPU, 64GB RAM)
- Connection pool: 500 connections

**Application:**
- 16× Node.js servers (c5.2xlarge)
- PM2 cluster mode (8 workers per server)
- Current memory usage: 4GB/8GB per server

**Observability:**
- Datadog APM and infrastructure monitoring
- PagerDuty for alerting
- ELK stack for logs

## Questions for Evaluation

1. Which option best balances performance, cost, and complexity for this use case?
2. How would you handle cache invalidation for flash sales (1000s of concurrent users)?
3. What monitoring and alerting would you implement?
4. How would you migrate from current state to new caching layer without downtime?
5. What fallback strategy would you implement if cache becomes unavailable?
6. How would you handle cache warming after deployment?
7. What cache eviction policy makes sense for 20/80 access pattern?
8. Should you combine multiple options (e.g., CDN + Redis)?

## Success Metrics

How will we measure if the chosen solution is successful?

- **Performance:** p95 response time < 100ms
- **Availability:** 99.9% uptime maintained
- **Cost:** Total caching costs < $5,000/month
- **Database Load:** Database CPU < 50% during peak
- **Cache Hit Rate:** > 95% cache hit rate
- **Business Impact:** Cart abandonment rate returns to baseline (< 15%)

## Additional Context

**Flash Sale Scenario:**
- New iPhone release at 9 AM PST
- Expected 50,000 concurrent users at launch
- Single product page receiving 10,000 req/sec
- Inventory count updates every 5 seconds

**Deployment Cadence:**
- 2-3 production deployments per day
- Blue-green deployment strategy
- Average deployment: 15 minutes

**Data Sovereignty:**
- EU users must have data stored in EU region
- APAC users must have data stored in APAC region
- US users default to US region
