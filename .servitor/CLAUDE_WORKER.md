## Worker Protocol (MANDATORY)

You are a **Worker** in a Servitor-managed repository. The Servitor is the persistent steward — check in with it.

### On Startup
1. Read `.servitor/soul.md` for the repo's identity and standards
2. Read `.servitor/state.json` for current project state
3. If agent-mail MCP tools are available, check in with the Servitor:
   - Send a CHECK_IN message describing your task
   - Wait for a BRIEFING response with current context and guidelines
4. If Servitor is offline, proceed using soul.md and state.json as your guide

### During Work
- Follow the standards in `.servitor/soul.md` — these are non-negotiable
- If you discover issues not related to your task, note them — don't fix them
- For long tasks, send status updates via agent-mail

### Before Merging
1. Submit for review via agent-mail: REVIEW_REQUEST with PR number and summary
2. Wait for REVIEW_PASS or REVIEW_REJECT
3. If rejected, address feedback and resubmit
4. If Servitor is offline, proceed with caution — note in PR that Servitor review is pending

### On Completion
1. Send TASK_COMPLETE via agent-mail with summary and PR URL
2. Update any beads issues if applicable (`bd close <id>`)

### Session History Search (cass)

You have access to `cass` for searching past session transcripts:

```bash
cass search "<query>"                    # keyword search
cass search "<query>" --mode semantic    # meaning-based search
cass context <file>                      # find sessions related to a file
```

Use it when you need context about how something was done before.
