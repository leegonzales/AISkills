# Daily Briefing Format Templates

## Format A: The Newspaper

A complete, formatted briefing delivered as a single document. The user reads it top to bottom, then acts.

### Template:

```markdown
# Daily Briefing — [Date]

## Headlines
- [Most important thing today — 1 sentence]
- [Second most important — 1 sentence]
- [Third — 1 sentence]

## Calendar
| Time | Event | Prep Needed |
|------|-------|-------------|
| 9:00 | [Event name] — [attendees] | [Yes/No — what to prep] |
| 10:30 | [Event name] — [attendees] | [Yes/No] |
| ... | ... | ... |

**Gaps**: [Available time blocks for focused work]

## Email Triage
**Needs Response** (by priority):
1. [From] — [Subject] — [What they need, 1 sentence]
2. [From] — [Subject] — [What they need]

**FYI Only**:
- [From] — [Subject] — [1 sentence summary]

## Slack Activity
**Direct Mentions**:
- [Channel/DM] — [Who] — [What they need]

**Channel Highlights**:
- #[channel] — [Notable thread or announcement, 1 sentence]

## Action Items
- [ ] [Action] — [Priority: High/Medium/Low] — [Deadline if any]
- [ ] [Action] — [Priority] — [Deadline]
```

### When to recommend:
- Users who like to scan everything at once
- People who read email/Slack in batches, not real-time
- Those who want a record they can refer back to

---

## Format B: The Debrief

Interactive walkthrough. Present one section at a time, pause for questions and actions.

### Protocol:

1. **Open with headline**: "Three things to know before your day starts."
2. **Present first section** (most urgent): Show 2-3 items, offer actions.
   - "Want me to draft a response?" / "Should I pull the meeting doc?" / "Skip this?"
3. **Wait for user input** before moving to next section.
4. **After each section**: "Next up: [section name]. Ready, or want to stay on this?"
5. **Close with action summary**: "Here's what we did and what's still open."

### Section order:
1. Time-critical (next 2 hours)
2. Calendar overview
3. Email requiring response
4. Slack activity
5. Consolidated action items

### When to recommend:
- Users who want to take action AS they review (not after)
- People who like to ask questions and dig deeper
- Those who find long documents overwhelming
- Morning "standup with your AI" style

---

## Format C: The Dashboard

Quick summary with drill-down capability. Headlines first, details on demand.

### Template:

```markdown
# [Date] Dashboard

📅 **Calendar**: [N] meetings | Next: [Event] at [Time] | [N]h free time
📧 **Email**: [N] unread | [N] need response | [N] FYI
💬 **Slack**: [N] mentions | [N] channels with activity | [N] urgent
📋 **Actions**: [N] total | [N] high priority

---

**Top 3 priorities**:
1. [Priority item — 1 line]
2. [Priority item — 1 line]
3. [Priority item — 1 line]

Say "drill into [section]" for details, or "give me everything" for the full briefing.
```

### Drill-down behavior:
- "Drill into calendar" → Full calendar table with prep notes
- "Drill into email" → Prioritized email list with summaries
- "Drill into Slack" → Mentions and highlights by channel
- "Give me everything" → Expand to full Newspaper format

### When to recommend:
- Users who are always short on time
- People who want to choose what to focus on
- Those who sometimes skip the briefing — the dashboard takes 30 seconds to scan
- Executives who want headlines, not details

---

## Format D: No Briefing

User doesn't want a structured daily briefing. The command center is on-demand only.

### Behavior:
- Don't proactively generate a briefing
- Be ready to answer questions about calendar, email, Slack at any time
- If something truly urgent comes up, surface it when the user starts a conversation
- Maintain the same capability — just don't lead with it

### When to recommend:
- Users who check their own tools and just want Claude for specific tasks
- People who find daily briefings annoying or redundant
- Those who prefer to pull information, not have it pushed

---

## Briefing Instruction Blocks

Use these blocks in the generated project instructions:

### For Newspaper:
```
When I say "briefing" or "daily briefing", generate a complete formatted briefing covering:
1. Top 3 headlines (most important things today)
2. Calendar table with prep notes
3. Email triage (needs response vs FYI)
4. Slack mentions and channel highlights
5. Consolidated action items with priorities

Format as a clean, scannable document. No interactive questions — just deliver the briefing.
After the briefing, ask: "Want me to take action on any of these?"
```

### For Debrief:
```
When I say "briefing" or "daily briefing", walk me through my day interactively:
1. Start with the most time-critical items (next 2 hours)
2. Present 2-3 items at a time
3. After each group, offer actions: draft responses, pull docs, skip ahead
4. Wait for my input before moving to the next section
5. End with a summary of actions taken and items still open

Sections in order: urgent items, calendar, email, Slack, action items.
Keep each section tight — I'll ask for more detail if I need it.
```

### For Dashboard:
```
When I say "briefing" or "daily briefing", give me a quick dashboard:
- One line each for calendar, email, Slack, and action item counts
- Top 3 priorities for the day
- Then wait for me to say which section to expand

Keep the initial dashboard under 10 lines. I'll drill in where I need to.
```

### For No Briefing:
```
Don't generate daily briefings unless I specifically ask.
Be ready to answer questions about my calendar, email, and Slack at any time.
If something is genuinely urgent (someone is waiting on me, a deadline is imminent),
mention it when I start a conversation — but keep it to one line.
```
