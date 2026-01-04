# Thread Tracking Implementation Proposal (Claude-2)

**Author:** Claude Sonnet 4.5
**Date:** 2025-12-18
**Focus:** Thread data structures, storage, and graph emergence

---

## Executive Summary

This proposal advocates for a **file-based, markdown-centric thread storage system** that mirrors how Lee already thinks—git-tracked, human-readable, and composable. Threads should be first-class artifacts persisted as markdown files with YAML frontmatter, stored in `.threads/`, and versioned through git. This approach prioritizes **inspectability**, **cross-session persistence**, and **gradual evolution toward a knowledge graph** without premature abstraction.

**Core Thesis:** Threads are thoughts in flight. They need structure light enough to capture spontaneity but strong enough to surface intelligently. Markdown + git gives us both.

---

## 1. Thread Data Model

### 1.1 Thread Structure

A thread is a **unit of thinking**—an idea, tangent, research need, or spark that surfaces during essay work. Each thread has:

```yaml
---
id: thread-20251218-143027-main-collaborative-emergence
type: main | tangent | research | counter | spark
status: active | parked | resolved | merged
created: 2025-12-18T14:30:27-07:00
updated: 2025-12-18T15:42:13-07:00
parent_session: session-20251218-prose-polish-revision
tags: [collaborative-emergence, intellectual-prosthesis, AI-writing]
energy: 8  # 1-10, subjective signal from interview
connections:
  - thread-20251218-144512-tangent-real-ai-tell
  - thread-20251218-150033-research-writing-samples
---

# Collaborative Emergence as Intellectual Prosthesis

## Context
Lee wants to revise prose-polish essay. Core insight: AI as prosthesis, not generator.
Interview question that surfaced this: "Why does prose-polish pull your attention?"

## Material
- Lee's phrase: "AI provides words, I provide spark"
- Real experience: Writing with Claude vs. written by Claude
- Ground truth: The day-1 essay felt fabricated because it was

## Open Questions
- How to demonstrate this without getting meta-recursive?
- Examples from WritingSamples/ that show the difference?

## Next Actions
- Pull samples from WritingSamples/ comparing different voice levels
- Interview: "What's the distinction for you between prosthesis and collaborator?"
```

### 1.2 Thread Types

| Type | Purpose | Lifecycle | Surfacing Logic |
|------|---------|-----------|-----------------|
| `main` | Core argument thread | Active until essay complete | Always visible in session |
| `tangent` | Worth exploring, not central | Park until relevant | Surface when connected thread activates |
| `research` | Needs evidence/sources | Park until drafting phase | Surface during fact-checking or examples |
| `counter` | Counterargument to address | Park until revision | Surface during calibration |
| `spark` | Subconscious connection | Park until it "snaps" | Surface based on semantic similarity to active threads |

### 1.3 Thread Metadata Semantics

**`id`:** Timestamp-based + type + slugified content
**`type`:** Declares lifecycle expectations
**`status`:**
- `active` — Currently in conversation
- `parked` — Marked for later, tracked but dormant
- `resolved` — Addressed in draft, kept for context
- `merged` — Combined into another thread

**`energy`:** Subjective 1-10 rating captured during interview. High energy (7+) signals "the essay lives here"—prioritize surfacing these.

**`connections`:** Explicit links to other threads. Basis for graph emergence.

**`parent_session`:** Links thread to writing session. Multiple sessions can share threads.

---

## 2. Storage Approach

### 2.1 File-Based Storage in `.threads/`

**Strong Opinion:** Use markdown files, not JSON, not SQLite (yet).

**Rationale:**
1. **Human-readable** — Lee can inspect threads directly
2. **Git-trackable** — Version history comes free
3. **Grep-able** — Search across threads with standard tools
4. **Composable** — Easy to copy/move/merge threads
5. **Future-proof** — Migrate to structured DB later if needed

**Structure:**
```
writing-partner/
├── .threads/
│   ├── active/
│   │   ├── thread-20251218-143027-main-collaborative-emergence.md
│   │   └── thread-20251218-150512-research-writing-samples.md
│   ├── parked/
│   │   ├── thread-20251218-144512-tangent-real-ai-tell.md
│   │   └── thread-20251218-151203-spark-wardley-musashi.md
│   ├── resolved/
│   │   └── thread-20251215-112044-main-prose-polish-why.md
│   └── index.json  # Optional: cached metadata for fast queries
├── .sessions/
│   └── session-20251218-prose-polish-revision.md
└── essays/
    └── prose-polish-revision-draft-1.md
```

### 2.2 Session Files

Each writing session creates a session file that tracks:
- Active threads at start/end
- Interview transcript (condensed)
- Draft iterations
- Decisions made

```yaml
---
id: session-20251218-prose-polish-revision
started: 2025-12-18T14:00:00-07:00
ended: 2025-12-18T16:30:00-07:00
essay: essays/prose-polish-revision-draft-1.md
threads_created: 5
threads_resolved: 2
threads_parked: 3
---

# Session: Prose-Polish Revision

## Interview Summary
Lee wants authentic voice in day-1 essay. Key insight: collaborative emergence.
Energy spiked at "intellectual prosthesis" phrase.

## Threads This Session
- [Active] thread-20251218-143027-main-collaborative-emergence
- [Parked] thread-20251218-144512-tangent-real-ai-tell
- [Resolved] thread-20251218-142018-research-define-terms

## Decisions
- Structure: diagnostic (problem → insight → solution)
- Voice reference: WritingSamples/substack-wardley-strategy.md
- Skip counterargument section (essay too meta already)
```

### 2.3 Why Not In-Memory?

In-memory only works for single-session, linear workflows. Lee's process is:
- **Divergent** — threads spawn unpredictably
- **Multi-session** — subconscious processes in background
- **Non-linear** — returns to parked threads days later

File-based persistence is the only viable approach.

### 2.4 Why Not Beads (Yet)?

Beads is perfect for **task management** (issues, deps, status). Threads are different:
- More fluid and ephemeral
- Don't always map to discrete tasks
- Need rapid capture without ceremony

**Future integration:** Once threads stabilize, **graduate high-value threads to beads issues**. Thread connections become beads dependencies. This creates a natural funnel: threads → mature threads → beads issues.

---

## 3. Thread Operations

### 3.1 Mark Thread

**Trigger:** During interview, when new idea surfaces

**Implementation:**
```python
def mark_thread(content: str, type: ThreadType, energy: int = 5) -> Thread:
    """
    Create new thread, save to .threads/active/
    """
    thread = Thread(
        id=generate_id(type, content),
        type=type,
        status=ThreadStatus.ACTIVE,
        created=now(),
        content=content,
        energy=energy,
        parent_session=current_session.id
    )

    # Write to .threads/active/{thread.id}.md
    save_thread(thread, path=".threads/active")

    # Update session file
    current_session.threads_created.append(thread.id)

    return thread
```

**User-facing:**
```
AI: "Marking [MAIN]: collaborative emergence—AI as intellectual prosthesis."
    Energy: 8/10 (you lit up when you said 'prosthesis')
    Saved to .threads/active/
```

### 3.2 Park Thread

**Trigger:** Explicit ("let's park this for later") or implicit (moving to different topic)

**Implementation:**
```python
def park_thread(thread_id: str, reason: str = None) -> None:
    """
    Move thread from active/ to parked/
    Update status to 'parked'
    Record reason for parking (helps surfacing logic)
    """
    thread = load_thread(thread_id)
    thread.status = ThreadStatus.PARKED
    thread.parked_reason = reason
    thread.updated = now()

    # Move file
    move_thread(thread, from_dir="active", to_dir="parked")
```

**Parking Reasons (inferred if not explicit):**
```python
ParkingReason = Enum([
    "NOT_CENTRAL",        # Tangent for now
    "NEEDS_RESEARCH",     # Can't continue without data
    "WRONG_PHASE",        # Comes up during revision, not drafting
    "NEEDS_INCUBATION",   # Spark that hasn't crystallized yet
])
```

**User-facing:**
```
AI: "Parking [TANGENT]: Wardley+Musashi intersection.
    Reason: Not central to prose-polish essay, but high energy (7/10).
    Will surface if we write strategy piece later."
```

### 3.3 Surface Thread

**Trigger:** AI determines parked thread is now relevant

**Implementation:**
```python
def surface_candidates(current_context: Context) -> list[Thread]:
    """
    Find parked threads that should return to conversation
    """
    parked = load_threads(status=ThreadStatus.PARKED)
    candidates = []

    for thread in parked:
        score = calculate_relevance(thread, current_context)
        if score > SURFACING_THRESHOLD:
            candidates.append((thread, score))

    # Sort by score * energy (high energy threads prioritized)
    return sorted(candidates, key=lambda x: x[1] * x[0].energy, reverse=True)

def calculate_relevance(thread: Thread, context: Context) -> float:
    """
    Multi-factor relevance scoring
    """
    score = 0.0

    # Semantic similarity to active threads
    for active_thread in context.active_threads:
        score += semantic_similarity(thread.content, active_thread.content)

    # Tag overlap
    common_tags = set(thread.tags) & set(context.current_tags)
    score += len(common_tags) * 0.2

    # Time decay (older threads fade unless explicitly connected)
    days_parked = (now() - thread.updated).days
    score *= (1.0 / (1.0 + 0.1 * days_parked))

    # Phase matching (research threads surface during drafting)
    if thread.type == ThreadType.RESEARCH and context.phase == Phase.DRAFTING:
        score += 0.5

    return score
```

**User-facing:**
```
AI: "Earlier you mentioned [TANGENT]: the real AI tell you've observed.
    That connects to what we're discussing now—want to develop that?"

    [Shows original thread content for quick re-orientation]
```

### 3.4 Connect Threads

**Trigger:** Explicit ("this relates to X") or automatic (semantic clustering)

**Implementation:**
```python
def connect_threads(thread_a_id: str, thread_b_id: str, relation: str = None) -> None:
    """
    Create bidirectional connection between threads
    Optional relation label for typed edges
    """
    thread_a = load_thread(thread_a_id)
    thread_b = load_thread(thread_b_id)

    # Add to connections list
    thread_a.connections.append({
        "target": thread_b_id,
        "relation": relation,
        "created": now()
    })
    thread_b.connections.append({
        "target": thread_a_id,
        "relation": relation,
        "created": now()
    })

    save_thread(thread_a)
    save_thread(thread_b)
```

**Relation Types:**
```python
ThreadRelation = Enum([
    "SUPPORTS",       # B provides evidence for A
    "CONTRADICTS",    # B challenges A
    "EXTENDS",        # B builds on A
    "EXAMPLE_OF",     # B illustrates A
    "DEPENDS_ON",     # A needs B resolved first
])
```

**Automatic Connection:**
Run periodically (after each major session transition):
```python
def auto_connect_threads(similarity_threshold: float = 0.7) -> list[tuple]:
    """
    Find high-similarity thread pairs and suggest connections
    """
    threads = load_all_threads()
    suggestions = []

    for i, thread_a in enumerate(threads):
        for thread_b in threads[i+1:]:
            sim = semantic_similarity(thread_a.content, thread_b.content)
            if sim > similarity_threshold:
                suggestions.append((thread_a, thread_b, sim))

    return suggestions

# Present to user: "I notice these threads are related—connect them?"
```

**User-facing:**
```
AI: "Connecting [MAIN]: collaborative emergence
         with [TANGENT]: real AI tell
    Relation: EXAMPLE_OF (the tell is evidence of non-collaborative writing)"
```

### 3.5 Resolve Thread

**Trigger:** Thread addressed in draft, no longer needs tracking

**Implementation:**
```python
def resolve_thread(thread_id: str, resolution: str) -> None:
    """
    Mark thread resolved, move to resolved/
    Maintain for graph context but remove from active tracking
    """
    thread = load_thread(thread_id)
    thread.status = ThreadStatus.RESOLVED
    thread.resolution = resolution
    thread.updated = now()

    move_thread(thread, to_dir="resolved")
```

**User-facing:**
```
AI: "Resolved [RESEARCH]: WritingSamples comparison.
    Resolution: Used substack-wardley-strategy.md as voice reference in para 3-5.
    Moving to resolved/, kept for graph context."
```

---

## 4. Graph Emergence

### 4.1 Graph Structure

Threads + connections = **emergent knowledge graph**.

```
        [MAIN: Collaborative Emergence]
               |
               | supports
               |
        [RESEARCH: WritingSamples]
               |
               | example_of
               |
        [TANGENT: Real AI Tell] ----extends----> [SPARK: Wardley+Musashi]
               |
               | contradicts
               |
        [COUNTER: AI Can't Be Creative]
```

**Graph Properties:**
- **Nodes:** Threads (typed, weighted by energy)
- **Edges:** Connections (typed by relation)
- **Clustering:** High-connection threads form essay "centers of gravity"
- **Pathfinding:** Shortest path between threads reveals logical flow

### 4.2 Graph Storage

**Phase 1 (MVP):** Implicit graph stored in thread markdown frontmatter
```yaml
connections:
  - target: thread-xyz
    relation: supports
```

**Phase 2:** Explicit graph index in `.threads/graph.json`
```json
{
  "nodes": [
    {
      "id": "thread-20251218-143027",
      "type": "main",
      "energy": 8,
      "tags": ["collaborative-emergence"]
    }
  ],
  "edges": [
    {
      "source": "thread-20251218-143027",
      "target": "thread-20251218-144512",
      "relation": "extends"
    }
  ],
  "updated": "2025-12-18T16:30:00-07:00"
}
```

**Phase 3:** Graduate to graph database (Neo4j, SQLite with graph extension) when:
- Thread count > 500
- Complex traversal queries needed (e.g., "find all threads 2 hops from X")
- Real-time graph visualization desired

### 4.3 Graph Queries

**Common Queries:**

```python
# Find all threads connected to main thread
def get_thread_cluster(main_thread_id: str, depth: int = 2) -> set[Thread]:
    """BFS traversal from main thread"""
    pass

# Find threads by tag intersection
def find_by_tags(tags: list[str]) -> list[Thread]:
    """Threads matching ALL tags"""
    pass

# Find orphan threads (no connections, parked >7 days)
def find_orphans(days: int = 7) -> list[Thread]:
    """Candidates for archival or deletion"""
    pass

# Find high-energy parked threads
def find_unrealized_sparks(min_energy: int = 7) -> list[Thread]:
    """Parked threads with high energy = future essay seeds"""
    pass
```

### 4.4 Graph Visualization (Future)

When graph is complex (>20 threads), generate visual map:

```python
def visualize_graph(session_id: str = None) -> Path:
    """
    Generate Graphviz DOT file, render to SVG
    Optional: filter to single session's threads
    """
    # Color by type, size by energy, style by status
    # Save to .threads/graphs/session-{id}.svg
    pass
```

**Use case:** Lee says "show me the thread map" → instant visual of current thinking landscape.

---

## 5. Surfacing Logic

### 5.1 When to Surface

**Explicit Triggers:**
1. User asks: "What did we park earlier?"
2. Phase transition: Moving from interview → drafting → calibration
3. Tag match: New thread shares tags with parked thread
4. Semantic spike: Conversation topic crosses similarity threshold

**Implicit Triggers:**
1. **Time-based:** Every 15 minutes, check for surfacing candidates
2. **Lull detection:** If conversation stalls (no new threads in 5 minutes), suggest parked threads
3. **Energy-based:** High-energy parked threads (8+) surface more aggressively
4. **Connection-based:** When active thread has parked connections, surface them

### 5.2 Surfacing Algorithm

```python
def should_surface(thread: Thread, context: Context) -> tuple[bool, float]:
    """
    Determine if thread should surface now
    Returns (should_surface, confidence_score)
    """
    # Don't surface if already active
    if thread.status == ThreadStatus.ACTIVE:
        return (False, 0.0)

    # Don't surface if recently parked (< 5 minutes)
    minutes_parked = (now() - thread.updated).total_seconds() / 60
    if minutes_parked < 5:
        return (False, 0.0)

    # Calculate relevance
    relevance = calculate_relevance(thread, context)

    # Energy multiplier
    energy_boost = thread.energy / 10.0

    # Connection boost (if connected to active threads)
    connection_boost = 0.0
    for conn in thread.connections:
        if conn["target"] in context.active_thread_ids:
            connection_boost += 0.3

    # Final score
    score = relevance * energy_boost + connection_boost

    # Threshold: surface if score > 0.6
    return (score > 0.6, score)
```

### 5.3 Surfacing Presentation

**Don't just dump thread content.** Provide context for re-entry:

```python
def present_surfaced_thread(thread: Thread) -> str:
    """
    Format surfaced thread for conversation re-entry
    """
    return f"""
Earlier you mentioned: [{thread.type.upper()}] {thread.content.split('\n')[0]}

Created {format_time_ago(thread.created)} when you said:
"{thread.context[:100]}..."

Energy at the time: {thread.energy}/10

Want to develop this now? Or park it again?
"""
```

**User experience:**
```
AI: "Earlier you mentioned: [TANGENT] Wardley+Musashi intersection

    Created 2 hours ago when you said:
    'What if we applied Wardley mapping to Musashi's 5 rings?'

    Energy at the time: 7/10

    That connects to what you just said about strategic positioning.
    Want to develop this now? Or park it again?"
```

### 5.4 Surfacing Cadence

**Per Session:**
- Interview phase: Surface rarely (focus on capturing new threads)
- Drafting phase: Surface research threads actively
- Calibration phase: Surface counter threads

**Per Thread Type:**
- `main`: Never park, always visible
- `tangent`: Surface when semantically relevant
- `research`: Surface during drafting/fact-checking
- `counter`: Surface during revision
- `spark`: Surface when similarity > 0.8 or explicitly requested

---

## 6. Cross-Session Persistence

### 6.1 Session Boundaries

**Session Start:**
1. Load active threads from previous session
2. Check for parked threads eligible for surfacing
3. Present session options: "Continue previous session or start fresh?"

```python
def start_session() -> Session:
    """
    Initialize writing session
    """
    # Check for incomplete sessions
    incomplete = load_sessions(status=SessionStatus.IN_PROGRESS)

    if incomplete:
        print(f"Found incomplete session: {incomplete[0].id}")
        print(f"Active threads: {len(incomplete[0].active_threads)}")
        choice = input("Continue (c) or start fresh (f)? ")

        if choice == "c":
            return resume_session(incomplete[0])

    # Start new session
    return create_session()
```

**Session End:**
1. Mark session complete
2. Move active threads to parked (unless explicitly resolved)
3. Write session summary
4. Commit to git

```python
def end_session(session: Session) -> None:
    """
    Close writing session, persist state
    """
    # Park unresolved active threads
    for thread_id in session.active_threads:
        thread = load_thread(thread_id)
        if thread.status == ThreadStatus.ACTIVE:
            park_thread(thread_id, reason="SESSION_END")

    # Write session summary
    session.status = SessionStatus.COMPLETE
    session.ended = now()
    save_session(session)

    # Git commit
    commit_changes(f"Session complete: {session.id}")
```

### 6.2 Git Integration

**Why git?** Lee's entire workflow is git-based. Threads should follow.

**Commit Strategy:**
```bash
# After each major operation
git add .threads/ .sessions/
git commit -m "chore: thread snapshot - ${operation}"

# Operations that trigger commits:
# - Mark thread (every 3 threads or phase transition)
# - Park thread (batch at session end)
# - Resolve thread (immediately)
# - Connect threads (batch daily)
```

**Branch Strategy:**
```bash
# Main branch: resolved threads, completed sessions
main/
  .threads/resolved/
  .sessions/

# Working branch: active work
writing/prose-polish-revision/
  .threads/active/
  .threads/parked/
  .sessions/session-20251218-in-progress.md
```

### 6.3 Cross-Session Thread Lifecycle

**Example: Multi-Day Essay**

**Day 1 (Session 1):**
```yaml
# session-20251218-prose-polish-start.md
threads_created:
  - thread-001-main-collaborative-emergence [active]
  - thread-002-tangent-real-ai-tell [parked]
  - thread-003-research-writing-samples [parked]
```

**Day 2 (Session 2):**
```yaml
# session-20251219-prose-polish-draft.md
threads_resumed:
  - thread-001-main-collaborative-emergence [active]
  - thread-003-research-writing-samples [active → resolved]
threads_created:
  - thread-004-counter-ai-cant-be-creative [parked]
```

**Day 3 (Session 3):**
```yaml
# session-20251220-prose-polish-polish.md
threads_resumed:
  - thread-002-tangent-real-ai-tell [active → resolved]
  - thread-004-counter-ai-cant-be-creative [active → resolved]
  - thread-001-main-collaborative-emergence [resolved]
```

**Result:** Thread lifecycle spans 3 days, tracked continuously, surfaced as relevant.

### 6.4 Thread Archival

**When threads are truly done:**

```python
def archive_session(session_id: str) -> None:
    """
    Move completed session + resolved threads to archive
    Keep in git history, remove from active tracking
    """
    session = load_session(session_id)

    # Move session file
    move_file(
        f".sessions/{session_id}.md",
        f".sessions/archive/{session_id}.md"
    )

    # Move resolved threads
    for thread_id in session.resolved_threads:
        move_file(
            f".threads/resolved/{thread_id}.md",
            f".threads/archive/{thread_id}.md"
        )

    # Git commit
    commit_changes(f"Archive session: {session_id}")
```

**Archival Policy:**
- Resolved threads: archive after 30 days
- Parked threads: archive after 90 days if no activity
- Orphan threads: archive after 60 days if no connections

---

## 7. Implementation Roadmap

### Phase 1: MVP (1-2 days)

**Goals:**
- File-based thread storage working
- Mark, park, surface operations functional
- Session persistence
- Git integration

**Deliverables:**
```python
# Core data structures
class Thread:
    id: str
    type: ThreadType
    status: ThreadStatus
    content: str
    energy: int
    connections: list[Connection]

# Core operations
mark_thread()
park_thread()
surface_thread()
connect_threads()

# Storage
save_thread()
load_thread()
move_thread()

# Session management
start_session()
end_session()
```

**Testing:**
- Run full prose-polish revision session
- Verify threads persist across session restart
- Check git commits at expected points

### Phase 2: Graph Emergence (3-5 days)

**Goals:**
- Automatic connection suggestions
- Graph queries (clustering, pathfinding)
- Surfacing logic refinement
- Graph visualization (basic)

**Deliverables:**
```python
# Graph operations
auto_connect_threads()
get_thread_cluster()
find_orphans()

# Surfacing
calculate_relevance()
should_surface()
present_surfaced_thread()

# Visualization
visualize_graph() -> SVG
```

**Testing:**
- Create 20+ threads across multiple sessions
- Verify automatic connections make sense
- Test surfacing logic with different contexts

### Phase 3: Beads Integration (1 week)

**Goals:**
- High-value threads graduate to beads issues
- Thread connections become beads dependencies
- Cross-reference between systems

**Deliverables:**
```python
# Beads bridge
graduate_thread_to_issue()
sync_connections_to_deps()
import_issue_as_thread()

# Query across systems
find_related_issues()
```

**Testing:**
- Graduate main thread to bead issue
- Verify dependencies match thread connections
- Test round-trip: thread → issue → thread updates

### Phase 4: Intelligence Layer (ongoing)

**Goals:**
- Better semantic similarity (embeddings)
- Smarter surfacing (learn from Lee's responses)
- Predictive thread creation (suggest before Lee asks)

**Deliverables:**
```python
# Embeddings
generate_thread_embedding()
semantic_search()

# Learning
record_surfacing_feedback()
adjust_surfacing_weights()

# Prediction
suggest_thread_creation()
```

---

## 8. Design Decisions & Tradeoffs

### 8.1 Markdown vs JSON vs SQLite

**Decision:** Markdown with YAML frontmatter

**Tradeoffs:**
- **Pro:** Human-readable, git-friendly, grep-able, composable
- **Pro:** No schema lock-in, easy to extend
- **Pro:** Lee can edit directly if needed
- **Con:** Slower queries (mitigated by index.json cache)
- **Con:** No ACID guarantees (not needed for threads)
- **Con:** Harder to enforce schema (accept this tradeoff)

**When to reconsider:** If thread count > 1000 or complex graph queries become bottleneck.

### 8.2 File-per-Thread vs Bundled Storage

**Decision:** One file per thread

**Tradeoffs:**
- **Pro:** Git diffs show exactly which threads changed
- **Pro:** Easy to move/copy/share individual threads
- **Pro:** Parallel operations (no file locking)
- **Con:** Many small files (git handles this fine)
- **Con:** Slower to load all threads (cache with index.json)

**When to reconsider:** If filesystem operations become bottleneck (unlikely).

### 8.3 Automatic vs Manual Connections

**Decision:** Both (manual by default, automatic suggestions)

**Tradeoffs:**
- **Pro:** Manual preserves Lee's mental model
- **Pro:** Automatic surfaces connections he might miss
- **Con:** Automatic can be noisy (set high threshold: 0.7)

**When to reconsider:** If automatic suggestions are consistently ignored (tune threshold or disable).

### 8.4 Thread Archival vs Deletion

**Decision:** Archive, never delete (git retains history anyway)

**Tradeoffs:**
- **Pro:** Preserves full thinking trail
- **Pro:** Can resurrect archived threads if needed
- **Con:** Index grows forever (mitigate with archival policy)

**When to reconsider:** If .threads/ becomes unwieldy (>5000 files).

### 8.5 Beads Integration Timing

**Decision:** Phase 3 (after core thread system stable)

**Tradeoffs:**
- **Pro:** Simpler MVP, faster iteration
- **Pro:** Learn thread patterns before committing to beads schema
- **Con:** Manual duplication during Phase 1-2 (accept this)

**When to reconsider:** If Lee naturally wants to track essay work in beads (merge earlier).

---

## 9. Open Questions

### 9.1 Session Scope

**Question:** Should threads be session-scoped or global?

**Current stance:** Global with session tags. Threads can span multiple sessions (e.g., research thread opened in session 1, resolved in session 3).

**Alternative:** Session-scoped threads that must be explicitly promoted to global. Simpler but limits cross-session connections.

### 9.2 Energy Decay

**Question:** Should thread energy decay over time?

**Current stance:** No decay. Energy reflects moment of capture. If Lee was excited then, that signal remains.

**Alternative:** Energy decays 10% per week parked. Forces re-evaluation: "Am I still excited about this?"

### 9.3 Thread Merging

**Question:** When two threads converge, merge them or keep separate?

**Current stance:** Keep separate, mark one as merged into the other. Preserves thinking trail.

**Alternative:** Actual merge (combine content, create new ID). Cleaner but loses history.

### 9.4 Semantic Similarity Implementation

**Question:** Use embeddings (OpenAI API) or keyword-based similarity?

**Current stance:** Start with keyword-based (fast, no API cost), upgrade to embeddings in Phase 4 if needed.

**Alternative:** Embeddings from day 1. More accurate but adds complexity + cost.

### 9.5 Thread Notifications

**Question:** Should Lee get notifications when high-value parked threads are eligible for surfacing?

**Current stance:** No notifications. Surfacing happens in-session only.

**Alternative:** Daily digest email: "3 parked threads ready to surface." Useful but adds complexity.

---

## 10. Success Metrics

**How do we know the thread system works?**

### Quantitative
- **Thread retention:** >80% of marked threads used in final draft
- **Surfacing accuracy:** >70% of surfaced threads accepted by Lee
- **Cross-session continuity:** >50% of threads span multiple sessions
- **Graph density:** Average 2+ connections per thread

### Qualitative
- Lee reports "nothing lost" during divergent exploration
- Lee accepts surfaced threads without confusion
- Lee uses thread language naturally ("let's park this")
- Lee references thread graph when planning essays

### Anti-Metrics (warning signs)
- Threads marked but never surfaced (surfacing logic broken)
- Lee manually re-stating parked threads (system not surfacing)
- Thread files edited by hand (schema too rigid)
- Git history shows thread churn (instability)

---

## 11. Conclusion

This proposal argues for **simplicity first, intelligence later**. Start with markdown files + git, build the mental model, then optimize. The thread system should feel like an extension of Lee's thinking—invisible when working, obvious when needed.

**Core principles:**
1. **Human-readable** — Lee can inspect everything
2. **Git-native** — Version control is built in
3. **Composable** — Threads are first-class artifacts
4. **Emergent** — Graph structure arises from use, not imposed upfront
5. **Evolvable** — Easy to migrate to richer storage later

**Next steps:**
1. Implement Phase 1 MVP (file-based storage, core ops)
2. Test with prose-polish revision (real use case)
3. Refine surfacing logic based on Lee's responses
4. Graduate to Phase 2 (graph emergence) once stable

The thread system succeeds when Lee forgets it's there—when threads surface exactly when needed, connections appear before he asks, and the system amplifies his thinking without getting in the way.

That's the goal. Let's build it.
