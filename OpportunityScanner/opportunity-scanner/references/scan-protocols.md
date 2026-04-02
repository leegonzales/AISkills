# Scan Protocols

Detailed MCP query patterns for each data source. Use these to extract maximum signal with minimum API calls.

---

## Google Calendar

### Initial Pull
```
List events for the last 30 days (today - 30d to today)
Include: summary, start, end, attendees, recurrence, description
```

### Derived Metrics
- **Meeting hours/week**: Sum event durations grouped by week
- **Meeting count/week**: Count events grouped by week
- **Recurring %**: Events with recurrence rule / total events
- **Average attendees**: Mean attendee count across all events
- **1:1 count**: Events with exactly 2 attendees (including organizer)
- **Large meetings**: Events with 6+ attendees

### Classification Query
For each event, classify by parsing title + description + attendee count:

| Type | Signal | Attendees |
|------|--------|-----------|
| 1:1 | Title contains name, 2 attendees | 2 |
| Standup/Status | "standup", "status", "sync", "check-in" | 3-8 |
| Decision meeting | "review", "decision", "approve", "plan" | 3-10 |
| Brainstorm | "brainstorm", "ideation", "workshop" | 3-15 |
| All-hands | "all-hands", "town hall", "company" | 10+ |
| External | Attendees from outside org domain | Any |
| Focus block | "focus", "no meetings", "heads down", blocked | 1 |

### Trend Analysis
Compare week-over-week:
- Is meeting load increasing or decreasing?
- Are new recurring meetings being added?
- Is focus time shrinking?

---

## Gmail

### Initial Pull
```
Search: newer_than:30d
Limit: 200 messages (100 sent, 100 received)
Fields: from, to, subject, date, snippet, labels
```

### Key Searches
```
# Emails they sent (patterns in their outgoing communication)
from:me newer_than:30d

# Emails requiring action (not newsletters, not automated)
is:inbox newer_than:14d -category:promotions -category:social -category:updates

# Emails they were slow to respond to (> 48h)
# Compare received date to reply date in threads

# Repetitive subjects (similar subject lines)
# Group by subject similarity after pulling
```

### Pattern Extraction
- **Subject clustering**: Group similar subjects to find templates
- **Sender frequency**: Who emails them most? Who do they email most?
- **Response time distribution**: Fast (< 1h), Same day (1-8h), Next day (8-24h), Slow (> 24h)
- **Thread depth**: Average replies per thread. Deep threads (5+) suggest decision complexity.
- **CC patterns**: Are they CC'd on things they don't engage with? (noise)

### Derived Metrics
- Emails sent per day (average)
- Emails received per day (average)
- % requiring response vs FYI
- Top 5 correspondents (volume)
- Most common subject patterns
- Average response time

---

## Slack

### Initial Pull
```
# Channels they're in
List channels user is a member of

# Recent activity in those channels (last 30 days)
For top 20 most active channels: read last 50 messages

# Direct mentions
Search for @user mentions in last 30 days

# DMs (last 14 days, summarize patterns not content)
Read recent DM conversations (last 14 days)
```

### Key Searches
```
# Questions directed at them
Search: "from:others @[user]" with "?" in message

# Status updates they post
Search: "from:[user]" in team/project channels, look for update patterns

# Recurring announcements
Search: "from:[user]" with repeated structure/format

# Help requests
Search: messages containing "how do I", "where is", "can someone", "does anyone know"
in channels they're active in
```

### Pattern Extraction
- **Channel activity map**: Which channels do they read vs write in?
- **Question patterns**: What do people ask them? Cluster by topic.
- **Information flow**: Who DMs them? What about? Are they forwarding info between groups?
- **Response time**: How fast do they respond to @mentions?
- **Posting patterns**: Time of day, day of week. When are they most active?
- **Thread participation**: Do they start threads or react to them?

### Derived Metrics
- Active channels count
- Messages sent/received per day
- DM vs channel ratio
- @mention frequency
- Average @mention response time
- Top conversation partners
- Question frequency (asked of them)

---

## Jira

### Initial Pull
```
# Assigned to them
Search: assignee = currentUser() AND updated >= -30d

# Created by them
Search: reporter = currentUser() AND created >= -30d

# Watched/commented by them
Search: watcher = currentUser() AND updated >= -30d
```

### Pattern Extraction
- **Ticket types**: Bug, task, story, epic — distribution
- **Status flow**: Average time in each status (to do → in progress → review → done)
- **Comment patterns**: Are they writing similar comments across tickets?
- **Creation patterns**: Do they create similar tickets repeatedly? (templates needed)
- **Blocker frequency**: How often are tickets blocked? What blocks them?
- **Sprint patterns**: Velocity, spillover rate

### Derived Metrics
- Tickets touched per week
- Average ticket cycle time
- Most common ticket types
- Blocker frequency
- Sprint completion rate
- Comment frequency and length

---

## Confluence

### Initial Pull
```
# Pages they authored or edited
Search: contributor = currentUser() AND lastModified >= now("-30d")

# Spaces they're active in
List spaces with recent activity
```

### Pattern Extraction
- **Page types**: Meeting notes, specs, runbooks, how-tos, templates?
- **Creation frequency**: How often do they create new pages?
- **Update patterns**: Which pages get updated repeatedly?
- **Stale pages**: Important pages not updated in 90+ days
- **Gap detection**: Topics active in Slack/email with no Confluence presence

### Derived Metrics
- Pages created/edited per month
- Most active spaces
- Documentation freshness score
- Topic coverage gaps

---

## Google Docs/Sheets

### Initial Pull
```
# Recently modified documents
Search: modifiedTime > 30 days ago, owned by user

# Shared documents
Search: sharedWithMe, recently accessed
```

### Pattern Extraction
- **Document types**: Classify by title and content patterns
- **Template detection**: Similar documents created repeatedly
- **Collaboration density**: Documents with many editors/commenters
- **Manual data**: Sheets with manual data entry that could be automated

---

## Cross-Source Correlation

After individual scans, correlate across sources:

1. **Meeting → Email → Slack**: Does a recurring meeting generate follow-up emails and Slack messages? (Meeting aftermath pattern)
2. **Slack question → No Confluence page**: Topic asked about in Slack that has no documentation (Knowledge gap)
3. **Jira ticket → Long Slack thread**: Tickets that generate extended Slack discussion (Process gap)
4. **Calendar heavy + Slow email response**: Meeting overload causing communication delays (Capacity signal)
5. **Same content in 3+ channels**: Status/info shared manually across email, Slack, and meetings (Broadcast pattern)
