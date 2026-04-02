# Pattern Catalog

Complete catalog of work patterns the scanner detects, with trigger conditions, ROI potential, and recommended builds.

---

## High-Value Patterns (10+ hours/week potential)

### 1. The Information Broker

**Signal**: High DM volume + frequent email forwarding + active in 10+ channels
**What's happening**: Person is manually routing information between people and teams. They read something in one place and relay it to another.
**Scan evidence**:
- DMs received asking "did you see..." or "what's the latest on..."
- Emails that are forwards with added context
- Active in channels spanning multiple teams/functions

**Personal recommendation**: **Daily Digest Project** — Claude project that scans their key channels and email, generates a synthesized briefing, and drafts relay messages for each audience.
**ROI**: 5-10 hours/week (reading, synthesizing, forwarding)
**Effort**: Medium

**Team recommendation**: **Cross-Team Digest Skill** — Automated digest that pulls relevant updates from each team's channels and distributes summaries. Eliminates the human router.
**ROI**: 5-10 hours/week for the broker + reduced information lag for the team
**Effort**: Medium

---

### 2. The Repetitive Reporter

**Signal**: Recurring meetings with follow-up emails + Slack status posts + similar docs created weekly
**What's happening**: Same information gets reformatted and delivered to different audiences — team standup, manager update, stakeholder email, Slack channel post.
**Scan evidence**:
- Weekly/biweekly meetings followed by email summaries within 24h
- Slack messages with similar structure posted on a regular cadence
- Google Docs with similar titles created repeatedly ("Week N Update", "Sprint Review")

**Personal recommendation**: **Auto-Report Skill** — Skill that pulls data from Jira/Slack/Calendar and generates all status updates in each required format. One scan, multiple outputs.
**ROI**: 3-8 hours/week (writing, formatting, distributing)
**Effort**: Medium

**Team recommendation**: **Automated Status Board Artifact** — A standing artifact (doc or dashboard) that auto-updates with team status pulled from Jira + Slack. Replace the meeting with the doc.
**ROI**: 3-8 hours/week for the reporter + 1-2 hours/week for each meeting attendee
**Effort**: High

---

### 3. The Question Magnet

**Signal**: Frequent DMs with questions + similar questions from different people + slow response to some
**What's happening**: Person holds institutional knowledge that isn't documented. People come to them because it's faster than searching (or the docs don't exist).
**Scan evidence**:
- DM threads starting with "quick question", "do you know", "how do I"
- Same question asked by 3+ different people in 30 days
- Channel messages where they're the primary responder

**Personal recommendation**: **FAQ Generator Artifact** — Claude scans the last 90 days of questions asked of them, clusters by topic, and generates a comprehensive FAQ document. Post it in relevant channels and Confluence.
**ROI**: 3-5 hours/week (answering questions)
**Effort**: Low

**Team recommendation**: **Team Knowledge Project** — Claude project the whole team can use. Pre-loaded with the FAQ, team processes, and relevant Confluence links. Team members ask the project instead of the person.
**ROI**: 3-5 hours/week for the magnet + faster answers for the team
**Effort**: Medium

---

## Medium-Value Patterns (3-8 hours/week potential)

### 4. The Meeting Machine

**Signal**: 20+ hours/week in meetings + minimal focus time + prep/follow-up emails around meetings
**What's happening**: Calendar dominates the workday. Real work happens in the margins.
**Scan evidence**:
- Calendar showing 20+ hours/week of meetings
- Email threads before meetings ("agenda for tomorrow's...") and after ("notes from today's...")
- Slack messages scheduling, rescheduling, or following up on meetings

**Personal recommendation**: **Meeting Prep Project** — Project that knows all recurring meetings, pulls context (last meeting notes, relevant Jira tickets, recent Slack threads), and generates prep docs 30 min before each meeting.
**ROI**: 3-5 hours/week (manual prep + context-gathering)
**Effort**: Medium

**Team recommendation**: **Async Status Skill** — Replace status meetings with async reports. Skill scans Jira + Slack and generates a structured update. Meeting time recovered for the whole team.
**ROI**: 2-4 hours/week per person for cancelled meetings
**Effort**: Medium

---

### 5. The Template Seeker

**Signal**: Similar emails sent to different people + similar docs created + repetitive Slack message formats
**What's happening**: They're doing the same thing with slight variations and don't have templates — or have templates they manually fill in.
**Scan evidence**:
- 3+ emails with similar structure sent to different recipients
- Documents with similar titles/structure created in the same month
- Slack messages with consistent format (e.g., weekly updates, request responses)

**Personal recommendation**: **Smart Template Skill** — Skill that identifies the document/email type, pulls relevant context, and generates a personalized draft. Not a static template — a context-aware generator.
**ROI**: 2-4 hours/week (writing, copying, customizing)
**Effort**: Low

**Team recommendation**: **Department Playbook Artifact** — Generated collection of templates, scripts, and standard responses for the team's most common communications.
**ROI**: 1-3 hours/week per team member
**Effort**: Low

---

### 6. The Context Switcher

**Signal**: Fragmented calendar + slow response times + active in many channels but shallow engagement
**What's happening**: Attention is scattered across too many streams. They're present everywhere but deep nowhere.
**Scan evidence**:
- Calendar shows 30+ minute gaps between meetings (not enough for deep work)
- Email response times vary wildly (some < 1h, some > 48h)
- Slack shows reads across many channels but brief responses
- Multiple Jira tickets in progress simultaneously

**Personal recommendation**: **Daily Priority Project** — Morning briefing that scans all inboxes, triages by urgency, and recommends a focus sequence. Batches low-priority items for end-of-day.
**ROI**: 2-4 hours/week (context-switching cost + missed items)
**Effort**: Medium

---

### 7. The Decision Bottleneck

**Signal**: Long Slack threads waiting on their input + Jira tickets blocked on them + email chains awaiting response
**What's happening**: Team velocity depends on this person's availability. Things stall when they're in meetings or focused elsewhere.
**Scan evidence**:
- Slack threads where someone asks a question and hours/days pass before their response
- Jira tickets in "blocked" or "waiting" status assigned to them
- Email chains with "following up on..." or "bumping this"

**Personal recommendation**: **Decision Queue Skill** — Scans for pending decisions across Slack, email, Jira. Presents them ranked by urgency with enough context to decide in 30 seconds each.
**ROI**: 2-3 hours/week (and unblocks others)
**Effort**: Low

**Team recommendation**: **Delegation Framework Artifact** — Decision matrix showing which decisions can be made without this person, with escalation criteria. Reduce the bottleneck.
**ROI**: Variable but high — unblocks team velocity
**Effort**: Low

---

## Lower-Value but Quick Win Patterns (1-2 hours/week, < 1 hour to build)

### 8. The Calendar Negotiator
**Signal**: Frequent meeting reschedules, "let me find a time" emails
**Build**: Calendar management project that handles scheduling

### 9. The Newsletter Reader
**Signal**: Many subscription emails, low open rate
**Build**: Newsletter digest artifact that summarizes subscriptions weekly

### 10. The Manual Note-Taker
**Signal**: Meeting notes documents created after every meeting
**Build**: Meeting summary skill that generates notes from calendar + context

### 11. The Status Checker
**Signal**: Frequent Jira searches, "what's the status of..." Slack messages
**Build**: Project status dashboard artifact

### 12. The Onboarding Repeater
**Signal**: Similar DM conversations with new team members
**Build**: Onboarding guide artifact + team project with FAQ

### 13. The Thread Summarizer
**Signal**: Long Slack threads they participate in, followed by summary messages
**Build**: Thread summary skill triggered on demand

### 14. The Weekly Planner
**Signal**: Calendar review + task list management at start of week
**Build**: Weekly planning skill that scans calendar + Jira and generates a priority plan

---

## Pattern Detection Priority

When multiple patterns are detected, prioritize by:

1. **Compound patterns**: Person is BOTH a Question Magnet AND Decision Bottleneck → they're the single point of failure. Team recommendations take priority.
2. **Time-dominant patterns**: Whatever consumes the most hours/week gets addressed first.
3. **Team-multiplied patterns**: If 5 people each waste 1 hour/week on the same thing, that's a 5x ROI vs a personal 5 hour/week pattern. Flag both, but note the multiplier.
4. **Quick wins**: If a quick win is available in the same space as a big recommendation, list it as "start here."
