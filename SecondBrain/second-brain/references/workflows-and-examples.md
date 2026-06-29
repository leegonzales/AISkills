# Second Brain Workflows & Examples

Extended workflow detail, examples, and guidance for the second-brain skill. The
core commands, triggers, and workflow skeleton live in `SKILL.md`; this file holds
the reference-grade detail.

## Capture Classification

The system uses AI to classify captures into node types. Confidence threshold:
- High confidence (>=0.6): auto-classified
- Low confidence (<0.6): sent to `needs_review`

Node types and the classification decision tree: see `node-types.md`.

## Query Types

- **Semantic search**: find by meaning, not just keywords
- **Graph traversal**: follow relationships (supports, blocks, contains)
- **Filter by type**: "Show me all ideas from this week"
- **Filter by domain**: "What work tasks are due?"

Usage patterns:
- "What did I say about authentication?"
- "What projects support the 'shipping velocity' goal?"
- "Show me tasks related to the SecondBrain project"
- "Who did I meet with about the budget?"

## Inbox States

- **pending**: awaiting AI classification
- **needs_review**: low confidence, needs human decision
- **processing**: currently being classified

## Digest Contents & Constraints

Digest includes: due tasks (today and overdue), high priority items, today's
meetings, items needing review, recent insights.

Constraints:
- Daily digest: <150 words
- Weekly review: <250 words

## Actions

Supported actions: complete/reopen tasks, update priority (0-4), change status
(active, completed, archived), add domain tag (work, personal, both).

Usage patterns: "Mark the PR review task done", "Complete task abc123", "Archive
the old project", "Set priority to high for...".

## Workflow Integration

### During Work Sessions

When user mentions something capture-worthy during natural conversation:

1. **Recognize capture intent:**
   - Direct: "Remember this...", "Add a task..."
   - Implicit: "I should...", "Don't forget...", "Note to self..."
2. **Capture with context:**
   - Include relevant context from current conversation
   - Tag with source: "cli" (Claude Code session)
   - Add any mentioned relationships
3. **Confirm capture:**
   - Brief confirmation with ID
   - Mention if `needs_review` due to low confidence

## Context Awareness

When capturing, leverage current conversation context:
- **File being discussed**: link to related codebase notes
- **Error being debugged**: capture as reference with solution
- **Decision being made**: note with rationale
- **Meeting notes mentioned**: parse for action items

Domain detection:
- In work project directory -> domain: work
- Personal topics mentioned -> domain: personal
- Both contexts mixed -> domain: both

## Meeting Transcript Processing

**Use case:** Paste meeting transcripts to automatically extract and capture
structured content.

### Workflow

1. **User pastes transcript** ("Here's the transcript from today's standup: ...").
2. **System processes and extracts:**
   - Meeting summary -> MEETING node
   - Action items -> TASK nodes
   - Decisions made -> REFERENCE nodes
   - People mentioned -> PERSON links
   - Follow-up meetings -> MEETING nodes
   - Key insights -> IDEA nodes
3. **Confirmation and review** (sample):

   ```
   Processed standup transcript:

   Created: "Daily Standup - Jan 15" (meeting)

   Extracted 4 tasks:
   - "Review PR #1234" -> assigned to you (high)
   - "Update API docs" -> assigned to Sarah
   - "Schedule design review" -> due Friday
   - "Fix login bug" -> blocked by infrastructure

   Captured 2 decisions:
   - "Using Postgres instead of MongoDB"
   - "Sprint ends Friday, demo at 2pm"

   Linked 3 people:
   - Sarah (mentioned 5x)
   - Mike (mentioned 2x)
   - John (new person, created)

   1 insight flagged:
   - "Team velocity improves when standups are <15 min"
   ```

### Extraction Patterns

**Action items (-> TASK):**
- "TODO: ...", "Action: ...", "Need to..."
- "Sarah will...", "I'll...", "We should..."
- "@mentions with action verbs"

**Decisions (-> REFERENCE):**
- "Decided: ...", "Agreed: ..."
- "We're going with...", "The plan is..."
- "Final decision: ..."

**Follow-ups (-> MEETING):**
- "Let's meet again...", "Schedule a follow-up..."
- "Next week we'll discuss..."
- Explicit dates/times mentioned

**People (-> PERSON links):**
- Names mentioned in context
- @mentions
- "talked to...", "asked..."

**Insights (-> IDEA):**
- Observations about patterns
- Hypotheses mentioned
- "I noticed...", "Interesting that..."

### Post-Processing

After extraction:
1. Create meeting node with summary
2. Create task nodes with assignments and due dates
3. Link people (create if new)
4. Store decisions as references
5. Write to Obsidian with wikilinks

### Configuration

```yaml
# ~/.config/secondbrain/daemons.yml
transcript_processing:
  auto_assign_unassigned: true  # Assign to self
  default_task_priority: 2
  flag_low_confidence: true     # Mark uncertain extractions
  link_to_meeting: true         # Connect all items to meeting node
```

## Example Interactions

### Capture During Work

```
User: "The deadline for the API migration is March 15th"
Assistant: [Captures as task with due date]
Captured: API migration deadline - Due March 15th (ID: abc123)
```

### Query Knowledge

```
User: "What did we decide about authentication?"
Assistant: [Searches knowledge graph]
Found 3 related items:
- [reference] "Use JWT with refresh tokens" (Jan 5)
- [task] "Implement OAuth flow" (in_progress)
- [meeting] "Auth design review with Sarah" (Jan 3)
```

### Morning Digest

```
User: "What should I focus on today?"
Assistant: [Generates digest]

Today's Focus (Wed, Jan 15):
- [OVERDUE] Review PR from Sarah (due Jan 14)
- [HIGH] Prepare API migration plan
- [DUE TODAY] Call dentist to reschedule

Meetings:
- 10:00 1:1 with Mike

Needs Review: 2 items in inbox
```

## Anti-Patterns

**Don't:**
- Capture every single thing mentioned (be selective)
- Force classification when context is unclear
- Interrupt flow for minor captures
- Create duplicate entries for same concept
- Over-classify simple notes

**Do:**
- Capture when user expresses intent or importance
- Ask for clarification if capture intent is ambiguous
- Batch confirmations when capturing multiple items
- Link to existing nodes when relationships are clear
- Respect user's domain boundaries

## Integration Points

**With beads issue tracker:**
- Cross-reference tasks with beads issues
- Import epic/task relationships

**With Obsidian vault:**
- Generated markdown syncs via Obsidian Sync
- Wikilinks enable navigation
- Daily notes include digest

**With SiliconDoppelgangerActual:**
- Deep queries via agent conversation
- Complex graph traversals
- Multi-step reasoning about priorities

## Success Metrics

Skill succeeds when:
- Captures happen naturally without flow interruption
- User finds past information quickly
- Daily digests surface actionable items
- Inbox stays manageable (<10 items needing review)
- Classification accuracy >85%

User feels: confident nothing important is lost; informed about what matters
today; in control of their knowledge system.
</content>
</invoke>
