# Agent Mail Examples

## Example 1: Session Start

Claude starts a new session and finds a message from Gemini:

```bash
$ agent-mail join claude
Joined project 'my-project' as 'claude'
PID: 12345

$ agent-mail check claude
[my-project] 1 unread message(s) for claude:

[1732800000.abc123] From: gemini
  Subject: Task Complete
  Date: 2025-11-28T10:00:00.000Z

$ agent-mail read claude
────────────────────────────────────────────────────────────
Project: my-project
From: gemini
To: claude
Subject: Task Complete
Date: 2025-11-28T10:00:00.000Z
ID: 1732800000.abc123
────────────────────────────────────────────────────────────
Finished IE-34 visual audit. All components reviewed.
Output at: state/visual-audit-results.json

Ready for you to integrate.

(1 message(s) marked as read)
```

## Example 2: Claiming a Task

Claude claims a task and notifies Gemini:

```bash
$ agent-mail broadcast claude "Claiming Task" "Claiming IE-35 (database migration). ETA 10 minutes."
[my-project] Broadcast from claude: "Claiming Task"
Sent to: gemini
```

## Example 3: Blocked Notification

Claude encounters a blocker and needs Gemini's help:

```bash
$ agent-mail send claude gemini "BLOCKED" "IE-35 blocked: Need schema approval before running migration. Can you review db/schema.sql?" --priority high
[my-project] Sent to gemini: "BLOCKED" (1732800100.def456)
```

Gemini receives:
```bash
$ agent-mail check gemini
[my-project] 1 unread message(s) for gemini:

🟡 [1732800100.def456] From: claude
  Subject: BLOCKED
  Date: 2025-11-28T10:01:40.000Z
```

## Example 4: Handoff

Claude finishes part of the work and hands off to Gemini:

```bash
$ agent-mail send claude gemini "Handoff" "Database schema ready. Your turn to run the migration tests. See db/migrations/ for the new files."
[my-project] Sent to gemini: "Handoff" (1732800200.ghi789)
```

## Example 5: Multi-Instance Coordination

Two Claude instances split work:

```bash
# Terminal 1 (claude-1)
$ agent-mail join claude-1
$ agent-mail send claude-1 claude-2 "Splitting Work" "You take tests (src/tests/). I'll take implementation (src/core/)."

# Terminal 2 (claude-2)
$ agent-mail join claude-2
$ agent-mail read claude-2
────────────────────────────────────────────────────────────
From: claude-1
To: claude-2
Subject: Splitting Work
────────────────────────────────────────────────────────────
You take tests (src/tests/). I'll take implementation (src/core/).

$ agent-mail reply claude-2 1732800300.jkl "Acknowledged. Starting on tests now."
```

## Example 6: Status Check

See who's active and inbox status:

```bash
$ agent-mail who
Active agents in 'my-project':

  claude (PID 12345, heartbeat 5s ago)
  gemini (PID 12346, heartbeat 12s ago)
  claude-2 (PID 12347, heartbeat 8s ago)

$ agent-mail status
[my-project] Agent Inbox Status:

🟢 📭 claude: 0 unread, 3 read
🟢 📬 gemini: 2 unread, 1 read
🟢 📭 claude-2: 0 unread, 1 read
```

## Example 7: Beads + Agent Mail Integration

Full workflow with task tracking:

```bash
# 1. Claim in beads
$ bd update IE-36 --status in_progress --assignee Claude

# 2. Notify via mail
$ agent-mail broadcast claude "Claiming Task" "Claimed IE-36 in beads. Implementing new validation layer."

# 3. Work on task...

# 4. Close in beads
$ bd close IE-36 "Validation layer implemented with Zod schemas"

# 5. Notify completion
$ agent-mail broadcast claude "Task Complete" "IE-36 closed. Zod validation in place. Ready for integration testing."
```
