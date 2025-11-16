# Alternative Approach Scenario: Collaborative Document Editing Conflict Resolution

## Problem Statement

**System:** Real-time collaborative document editor (similar to Google Docs, Notion, or Figma)
**Current Approach:** Last-Write-Wins (LWW) conflict resolution
**Critical Issue:** Users lose edits during concurrent editing, causing frustration and data loss

## Current Implementation: Last-Write-Wins (LWW)

### How It Works

```javascript
// Simplified current implementation
class Document {
  constructor(id, content) {
    this.id = id;
    this.content = content;
    this.lastModified = Date.now();
    this.version = 1;
  }

  update(newContent, userId, timestamp) {
    // Last write wins - whoever writes last overwrites previous changes
    if (timestamp > this.lastModified) {
      this.content = newContent;
      this.lastModified = timestamp;
      this.version++;
      return { success: true, version: this.version };
    }
    return { success: false, error: 'Stale update' };
  }
}
```

### Issues with Current Approach

**Scenario 1: Simultaneous Edits**
```
T0: Document content = "Hello world"
T1: User A edits to "Hello beautiful world" (starts typing)
T2: User B edits to "Hello world today" (starts typing)
T3: User A saves (timestamp 100)
T4: User B saves (timestamp 101)
Result: User A's changes ("beautiful") are LOST
```

**Scenario 2: Network Latency**
```
T0: Document content = "Meeting at 2pm"
T1: User A (slow connection) changes to "Meeting at 3pm"
T2: User B (fast connection) changes to "Meeting at 2pm in Room A"
T3: User B's change arrives first (timestamp 100)
T4: User A's change arrives late (timestamp 99, rejected)
Result: User A sees "Conflict" error, must manually reconcile
```

**Scenario 3: Offline Editing**
```
T0: Document content = "Project deadline: Q1 2025"
T1: User A goes offline, edits to "Project deadline: Q2 2025"
T2: User B (online) edits to "Project deadline: Q1 2025 (extended)"
T3: User A comes back online, tries to sync
Result: Either A or B's changes are lost, no way to merge
```

### Metrics Showing Problem Severity

- **Conflict rate:** 15% of collaborative sessions experience lost edits
- **User complaints:** 200+ support tickets per month about lost changes
- **Session abandonment:** 25% of users stop collaborating after experiencing data loss
- **Recovery time:** Average 10 minutes to manually reconcile lost changes
- **Cost:** Estimated $50,000/year in support costs and lost productivity

## Requirements for New Solution

### Functional Requirements

1. **Preserve All Edits:** Never lose user changes during concurrent editing
2. **Automatic Conflict Resolution:** Merge changes without user intervention when possible
3. **Offline Support:** Allow users to edit offline and sync when reconnected
4. **Real-time Updates:** Changes appear on other users' screens within 500ms
5. **Character-Level Granularity:** Merge at character level, not document level
6. **Undo/Redo Support:** Must work correctly with concurrent edits
7. **Rich Content Support:** Handle text, images, links, formatting

### Non-Functional Requirements

1. **Performance:** <50ms latency for operations, <100KB memory per document
2. **Scalability:** Support 100 concurrent editors on same document
3. **Consistency:** Eventually consistent (within 5 seconds)
4. **Reliability:** 99.9% uptime, no data loss
5. **Compatibility:** Must integrate with existing WebSocket infrastructure

### Data Characteristics

- **Document size:** Average 50KB, max 10MB
- **Edit frequency:** 10-50 edits per minute per active user
- **Session duration:** Average 15 minutes, max 4 hours
- **Concurrent editors:** Average 3, max 100
- **Network conditions:** 50% of users on mobile with varying latency (50-500ms)

## Research Context: Conflict Resolution Approaches

### Approach 1: Operational Transformation (OT)

**What It Is:**
Transform each user's operation to account for concurrent operations from other users.

**How It Works:**
```javascript
// Simplified OT example
class Operation {
  constructor(type, position, content) {
    this.type = type; // 'insert' or 'delete'
    this.position = position;
    this.content = content;
  }
}

function transform(op1, op2) {
  // If op2 happens before op1's position, adjust op1's position
  if (op1.type === 'insert' && op2.type === 'insert') {
    if (op2.position <= op1.position) {
      return new Operation('insert', op1.position + op2.content.length, op1.content);
    }
  }
  // More transformation rules...
  return op1;
}
```

**Example:**
```
Document: "Hello"
User A: Insert "world" at position 5 → "Helloworld"
User B: Insert " " at position 5 → "Hello "

OT transforms B's operation:
- B's insert was at position 5
- A's insert added 5 characters at position 5
- Transform B's position to 10
Result: "Hello world"
```

**Pros:**
- Proven technology (Google Docs uses OT)
- Predictable results for text editing
- Strong consistency guarantees
- Works with any data structure

**Cons:**
- Complex implementation (transformation functions are tricky)
- Requires central server to order operations
- Difficult to implement undo/redo correctly
- Hard to debug when things go wrong

**References:**
- Original paper: "Operational Transformation in Real-Time Group Editors" (1995)
- Google Wave OT implementation (open source)

---

### Approach 2: Conflict-free Replicated Data Types (CRDTs)

**What It Is:**
Data structures that automatically merge concurrent changes without conflicts.

**How It Works:**
```javascript
// Simplified CRDT example (YJS-style)
class CharNode {
  constructor(char, id, leftId, rightId) {
    this.char = char;
    this.id = id; // Unique identifier (userId + counter)
    this.leftId = leftId; // Previous character
    this.rightId = rightId; // Next character
    this.deleted = false;
  }
}

class CRDTDocument {
  constructor() {
    this.characters = new Map(); // id -> CharNode
  }

  insert(char, leftId, userId, counter) {
    const newId = `${userId}:${counter}`;
    const newChar = new CharNode(char, newId, leftId, null);
    this.characters.set(newId, newChar);
    // Link to left neighbor
    if (leftId) {
      const left = this.characters.get(leftId);
      newChar.rightId = left.rightId;
      left.rightId = newId;
    }
  }

  delete(id) {
    const char = this.characters.get(id);
    char.deleted = true; // Tombstone, not actually removed
  }

  toString() {
    // Traverse linked list, skip deleted
    let result = '';
    let current = this.characters.get('ROOT');
    while (current) {
      if (!current.deleted) result += current.char;
      current = this.characters.get(current.rightId);
    }
    return result;
  }
}
```

**Example:**
```
Document: "Hello"
User A: Insert "world" at end → "Helloworld"
User B: Insert " " at end → "Hello "

CRDT automatically merges:
- A inserts 'w', 'o', 'r', 'l', 'd' with IDs A:1, A:2, A:3, A:4, A:5
- B inserts ' ' with ID B:1
- Both characters point to same left neighbor ('o' in "Hello")
- IDs determine order: "Hello world" or "Hello world" depending on ID sort
```

**Pros:**
- No central server needed (peer-to-peer)
- Simple mental model (merge is automatic)
- Great offline support
- Mathematically proven convergence
- Easy to implement undo/redo

**Cons:**
- Growing document size (tombstones)
- Memory overhead (metadata per character)
- Potential ordering issues (depends on CRDT type)
- Less control over merge behavior

**References:**
- YJS library (popular CRDT implementation)
- Automerge (JSON CRDT)
- Paper: "A Comprehensive Study of CRDTs" (2011)

---

### Approach 3: Hybrid OT + CRDT

**What It Is:**
Combine OT's predictable ordering with CRDT's offline support.

**How It Works:**
```javascript
class HybridDocument {
  constructor() {
    this.crdt = new CRDTDocument(); // For offline merging
    this.operationLog = []; // For OT ordering
    this.serverClock = 0; // Central clock for ordering
  }

  async applyOperation(operation, isLocal) {
    if (isLocal) {
      // Local operation: apply to CRDT, send to server
      this.crdt.applyOperation(operation);
      const serverOp = await this.sendToServer(operation);
      this.operationLog.push(serverOp);
    } else {
      // Remote operation: transform against pending ops, apply
      const transformed = this.transformAgainstPending(operation);
      this.crdt.applyOperation(transformed);
      this.operationLog.push(operation);
    }
  }

  transformAgainstPending(op) {
    // Use OT to transform against operations not yet acknowledged
    let transformed = op;
    for (const pending of this.getPendingOperations()) {
      transformed = transform(transformed, pending);
    }
    return transformed;
  }
}
```

**Pros:**
- Best of both worlds
- Offline support + predictable ordering
- Easier debugging than pure CRDT

**Cons:**
- Most complex to implement
- Still requires central server for ordering
- Performance overhead of both approaches

---

### Approach 4: Event Sourcing with Merge Strategies

**What It Is:**
Store all changes as events, apply custom merge strategies during sync.

**How It Works:**
```javascript
class EventSourcedDocument {
  constructor() {
    this.events = []; // All edit events
    this.snapshot = ''; // Current state
    this.version = 0;
  }

  recordEvent(event) {
    this.events.push({
      id: uuidv4(),
      userId: event.userId,
      type: event.type, // 'insert', 'delete', 'format'
      position: event.position,
      content: event.content,
      timestamp: Date.now(),
      dependencies: event.dependencies // Events this depends on
    });
  }

  merge(remoteEvents) {
    // Custom merge strategy based on event types
    const merged = this.threewayMerge(
      this.events,
      remoteEvents,
      this.findCommonAncestor(remoteEvents)
    );
    this.events = merged;
    this.snapshot = this.replayEvents(merged);
  }

  threewayMerge(local, remote, ancestor) {
    // Strategy 1: Text region doesn't overlap → accept both
    // Strategy 2: Same region, different content → pick timestamp winner
    // Strategy 3: Same region, compatible content → merge intelligently
    // ...custom logic per event type...
  }
}
```

**Pros:**
- Full audit trail (useful for compliance)
- Flexible merge strategies (can evolve over time)
- Time-travel debugging
- Custom conflict resolution per content type

**Cons:**
- Event log grows unbounded (need compaction)
- Replaying events is slow for large documents
- Merge strategy complexity (case-by-case decisions)
- Requires snapshot strategy for performance

---

## Constraints

1. **Existing Infrastructure:** WebSocket-based real-time system, Node.js backend
2. **Team Expertise:** 3 engineers, strong in distributed systems, no CRDT experience
3. **Timeline:** Must be production-ready in 3 months
4. **Migration:** 500,000 existing documents must be migrated without data loss
5. **Backwards Compatibility:** Must support clients on old version during rollout (2-week overlap)
6. **Performance Budget:** Cannot increase server costs by more than 30%
7. **Mobile Support:** Must work on iOS/Android with limited bandwidth

## Current System Architecture

```
Client (React)
   ↓ WebSocket
Server (Node.js + Redis)
   ↓
Database (PostgreSQL)

Current flow:
1. User types character
2. Client sends delta over WebSocket
3. Server applies LWW logic
4. Server broadcasts to other clients
5. Periodic DB save (every 5 seconds)
```

## Questions for Evaluation

1. **Which approach best fits our requirements and constraints?**
   - Consider: team expertise, timeline, infrastructure

2. **How would you handle the migration of 500,000 existing documents?**
   - Versioning strategy?
   - Gradual rollout?

3. **What happens if two users are editing offline for hours, then reconnect?**
   - Merge strategy?
   - User notification?

4. **How would you test the new conflict resolution system?**
   - Property-based testing?
   - Fuzzing?
   - Chaos engineering?

5. **What fallback strategy if the new system fails in production?**
   - Can we roll back to LWW?
   - Feature flag?

6. **How do we handle undo/redo with concurrent edits?**
   - Local undo only?
   - Global history?

7. **What about rich content (images, tables, embeds)?**
   - Per-element CRDT?
   - Separate conflict resolution?

## Success Metrics

- **Conflict rate:** < 1% (down from 15%)
- **User complaints:** < 10 tickets/month (down from 200)
- **Data loss:** 0% (currently occasional losses)
- **Merge latency:** < 100ms (for 100 concurrent editors)
- **Memory overhead:** < 2x current usage
- **Session abandonment:** < 5% (down from 25%)
- **User satisfaction:** > 90% in post-rollout survey

## Additional Context

### Typical Editing Patterns

1. **Co-located team editing meeting notes:**
   - 5 users, same physical location
   - Low latency, high edit frequency
   - Editing different sections mostly

2. **Remote team on design spec:**
   - 10 users, different time zones
   - High latency (200-500ms)
   - Occasional overlapping edits

3. **Writer with editor reviewing:**
   - 2 users, asynchronous
   - One person writing, one suggesting changes
   - High conflict potential

4. **Mobile user on train:**
   - 1 user, intermittent connectivity
   - Goes offline/online frequently
   - Needs robust offline support

### Content Types in Documents

- **Plain text:** 70% of content
- **Rich formatting:** 20% (bold, italic, headers)
- **Embedded content:** 10% (images, links, code blocks)
- **Collaborative elements:** Comments, suggestions, @mentions

### Technical Debt Considerations

- Current LWW code is tightly coupled to WebSocket layer
- No proper abstraction for conflict resolution (would need refactoring)
- Limited test coverage (< 40% for collaboration features)
- No distributed testing framework (would need to build)
