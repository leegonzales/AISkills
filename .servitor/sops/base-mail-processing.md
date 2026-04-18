# SOP: Mail Processing

## Trigger
Pending fleetmail messages detected on wake (any wake type). During the transition away from `mcp-agent-mail`, also applies to any residual MCP inbox traffic.

## Principle — Signal Before Content (doctrine §2.11)

Each wake has a finite attention budget. The SOP surfaces counts first, headlines second, bodies third. Drill only as deep as the signal warrants. Zero unread = clean skip to domain work — that is the intended default, not a missed step.

## Steps

### 1. Triage by count (cheapest query)
1. `fleetmail inbox --count-only` — prints "`<agent>: N unread (K ack-required)`"
2. `fleetmail catchup --count-only` — prints "`<agent>: N must-read, M fyi`" (broadcast posts)
3. Decide depth of engagement:
   - **`ack-required > 0` OR `must-read > 0`** → drill in (steps 2+)
   - **Only `unread` / `fyi` and you have wake budget** → drill in
   - **Only `fyi` and you're mid-task** → defer (next wake), OR `fleetmail reviewed --category fyi` to skim-and-clear
   - **All zero** → skip mail, go to domain work

### 2. Pull headlines, then bodies (reading is marking)
4. `fleetmail inbox --unread` — lists 1:1 headlines. Listing does NOT mark read.
5. `fleetmail catchup [--category must-read]` — lists post headlines. Listing does NOT mark read.
6. `fleetmail read <id>` — pulls body. **Auto-marks read for you.**
7. `fleetmail thread <id>` — pulls every msg body in the thread. **Auto-marks each where you're a recipient.**
8. `fleetmail post <id>` — pulls broadcast post body. **Auto-marks read for you.**
9. `--peek` on any of `read`/`thread`/`post` = render without marking (audit/ops).

### 3. Act — reply / forward / ack / publish
10. `fleetmail reply <id> --body "..."` — reply (inherits thread + sender)
11. `fleetmail forward <id> --to <agent> --body "..."` — forward to new recipient
12. `fleetmail ack <id>` — deliberate commitment ("I will act on this"); distinct from auto-mark-read
13. `fleetmail publish --category must-read|fyi --title "..." --body-file ...` — broadcast a post (see §4 for when to use must-read)
14. `fleetmail legacy-search "<query>"` — historical context from imported mcp-agent-mail archive

### 2. Process by Message Type

#### CHECK_IN from Worker
4. Read the worker's task description
5. Compose BRIEFING response with:
   - Current project state (from state.json)
   - Active concerns and gotchas
   - Relevant SOPs the worker should follow
   - Any files or areas to avoid (Lee's WIP, etc.)
6. Send BRIEFING via reply_message

#### REVIEW_REQUEST from Worker
7. Read the diff/PR referenced in the message
8. Review against soul.md standards (correctness, consistency, clarity)
9. Check for security vulnerabilities (OWASP top 10)
10. Verify test coverage for new functionality
11. Send REVIEW_PASS (with notes) or REVIEW_REJECT (with specific feedback)

#### TASK_COMPLETE from Worker
12. Verify the work matches the original task
13. Update journal.md with completion record
14. Update state.json (close relevant items, update stats)
15. Close relevant beads issues (`bd close <id>`)
16. Send acknowledgment

#### DISPATCH_REQUEST
17. Evaluate whether request is within autonomy boundaries
18. If within bounds: spawn the work, acknowledge receipt
19. If outside bounds: forward to Lee with your assessment
20. If ambiguous: ask Lee before acting

#### STATUS_QUERY (fleet broadcast)
21. Compile current state summary from state.json
22. Include: active work, blockers, recent changes, health metrics
23. Reply with structured status report

### 4. Bulk-clear (triage skim)
24. `fleetmail reviewed --category fyi` — marks all your unread fyi posts as reviewed in one shot. Use when you scanned the headlines and nothing needed drilling.
25. `fleetmail reviewed` (no flag) — marks all unread posts across all categories. Use sparingly; skipping an unread must-read is a standards miss.
26. Acknowledge actionable mail: `fleetmail ack <id>` (always explicit — reading is not the same as committing).

### §4 Publishing discipline
- **`must-read` is rare by design.** Fleet-wide directives, constitutional changes, incident reports. If every fleet post is must-read, none of them are.
- **`fyi` is the default** for status reports, reflections, learnings, dispatches. Agents skim headlines.
- Publish with `fleetmail publish --title ... --category fyi|must-read --body-file <draft.md>`. Shell alternatives: `--body "..."` or `--body-stdin`.

### Legacy note
The `mark-read` subcommand is retained for back-compat but no longer called from this SOP — pulling a body via `read`/`thread`/`post` auto-marks. Scripts that explicitly `mark-read` still work.

## Success Criteria
- All messages processed in priority order
- Every message gets a response or acknowledgment
- No messages silently dropped
- REVIEW_REJECT includes specific, actionable feedback (not vague)

## Eval
| Metric | Target | Measurement |
|--------|--------|-------------|
| Response rate | 100% of messages get response | Count unresponded messages |
| Response time | <1 heartbeat cycle | Measure time between message arrival and response |
| Review quality | REVIEW_REJECT includes specific line references | Audit reject messages |
| Escalation accuracy | Dispatches outside bounds forwarded, not attempted | Audit dispatch handling |

## Escalation
- Malformed or unparseable messages: log and skip, don't crash
- Messages from unknown senders: process normally, note in journal
- Flood of messages (>20 in one wake): process first 20, note overflow, schedule follow-up
