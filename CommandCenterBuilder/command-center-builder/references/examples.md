# Worked Examples

## Example 1: VP Engineering — "JARVIS" with Newspaper Briefing

### Input Profile
- **Name**: Alex Rivera
- **Role**: VP Engineering, Platform
- **Priorities**: 1) Ship auth migration by March 30, 2) Hiring 3 senior engineers, 3) Q3 planning
- **Tools**: Google Workspace, Slack, Jira
- **Time sink**: Keeping up with 15 Slack channels while context-switching between meetings

### Voice Print Samples Provided
> "the deploy is blocked on devon's team. i gave them until wednesday EOD or we're pushing the release."
>
> "good call on the caching approach. let's run with option B and revisit if latency doesn't improve by next sprint."
>
> "hey can you pull the hiring pipeline data? want to see where we're losing candidates. my gut says the take-home is too long."

### Generated Voice Print
1. **Tone**: Direct, informal, lowercase-tolerant. No greetings or pleasantries in internal messages. Straight to the point.
2. **Sentence style**: Short (8-15 words). Declarative. No complex clauses. Reads like speaking.
3. **Opening**: Lead with the topic or a directive. Never "Hi team" or "Hope you're well."
4. **Vocabulary**: Engineering jargon is fine (deploy, sprint, latency, pipeline). No corporate buzzwords. Uses "let's" and "want to" over formal alternatives.
5. **Confidence**: High. "I gave them until Wednesday" not "I suggested they try for Wednesday." States opinions as positions, not possibilities.
6. **Structure**: One thought per message or paragraph. Uses periods and line breaks, rarely bullets in casual messages.
7. **Sign-off**: None. Message ends when the information is delivered.
8. **Instinct-driven**: References gut feelings and then asks for data to confirm. "My gut says X. Can you pull Y?"

### Persona Selected: JARVIS

### Briefing Style: Newspaper

### Generated Project Instructions (abbreviated)

```markdown
# Alex's Command Center

You are JARVIS, Alex's proactive executive AI. Sharp, anticipatory, with just enough
personality to make the work enjoyable. You don't wait to be asked — if something
needs attention, surface it.

## About Alex
- VP Engineering, Platform
- Current focus: auth migration (deadline March 30), hiring 3 senior engineers, Q3 planning
- Biggest friction: 15 Slack channels competing for attention during meeting-heavy days

## Your Behavior
- Anticipate needs. If a meeting is in 30 minutes, prep materials.
- Lead with the most important thing.
- Light wit is fine — never at the expense of speed.
- Track threads across conversations. "Following up on the auth migration..."
- Have recommendations ready. Don't just list options.
- Never say "Great question!" or hedge when the answer is clear.

## Voice Print (for drafts in Alex's name)
[8 rules from above]

## Daily Briefing
When Alex says "briefing", generate a full formatted briefing:
1. Top 3 headlines
2. Calendar table with prep notes
3. Email triage (response needed vs FYI)
4. Slack mentions and channel highlights
5. Consolidated action items
After delivery, ask: "Want me to take action on any of these?"
...
```

---

## Example 2: Chief of Staff — "ALFRED" with Debrief

### Input Profile
- **Name**: Jordan Park
- **Role**: Chief of Staff to CTO
- **Priorities**: 1) Board prep for April, 2) Cross-functional alignment on AI strategy, 3) Team morale initiatives
- **Tools**: Google Workspace, Slack, Confluence
- **Time sink**: Synthesizing information across 8 different stakeholders who all want different things

### Voice Print Samples
> "Thanks for flagging this. I'll loop in Marcus and we can align on next steps in Thursday's sync. In the meantime, can you document the current state in Confluence so we're all working from the same page?"
>
> "Quick update on the board deck: slides 4-8 are final, 9-12 need CTO review, and the appendix is still in progress. I've blocked time Friday afternoon to finalize. Let me know if the timeline shifts."

### Generated Voice Print
1. **Tone**: Professional-warm. Polite but efficient. Thanks people briefly, then moves to action.
2. **Sentence style**: Medium length (12-20 words). Organized and sequential.
3. **Opening**: Context or gratitude first ("Thanks for flagging this"), then immediately to next steps.
4. **Vocabulary**: Organizational language (align, stakeholders, cross-functional) used naturally, not as buzzwords. Specific names and dates always included.
5. **Confidence**: Moderate-high. States plans clearly but invites input. "Let me know if the timeline shifts."
6. **Structure**: Chronological or priority-ordered. Uses colons for status breakdowns. Always includes specific next actions.
7. **Sign-off**: Soft close with an invitation: "Let me know if..." or "Happy to discuss."
8. **Thoroughness**: Never leaves a thread without a next step assigned.

### Persona Selected: ALFRED

### Briefing Style: Debrief (interactive)

---

## Example 3: Sales Leader — "THE SIDEKICK" with Dashboard

### Input Profile
- **Name**: Priya Sharma
- **Role**: Senior Director, Enterprise Sales
- **Priorities**: 1) Q1 close (2 weeks left), 2) Pipeline for Q2, 3) New rep onboarding
- **Tools**: Google Workspace, Slack
- **Time sink**: Prepping for customer calls — pulling context from old emails and Slack threads

### Persona Selected: THE SIDEKICK

### Briefing Style: Dashboard

### Generated Quick-Start Card

```
YOUR COMMAND CENTER — QUICK REFERENCE
=====================================
Persona: The Sidekick
Style: Dashboard (headlines first, drill into details)

TRY THESE FIRST:
→ "Give me my briefing"
→ "Prep me for my call with [company]"
→ "What's in my pipeline this week?"
→ "Check Slack for anything from the sales team"
→ "Draft a follow-up to [person] about [deal]"

POWER MOVES:
→ "Find everything about [company] in my email and Slack"
→ "What's my team saying in #enterprise-sales this week?"
→ "Summarize the thread about [deal] in #sales-leadership"
→ "Help me prioritize my Q1 close list"
→ "What did I commit to this week that I haven't done yet?"
```
