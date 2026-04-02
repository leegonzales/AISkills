# MCP Setup Guide

## What Are MCPs?

MCPs (Model Context Protocol) connect Claude to your work tools. Once connected, Claude can read your calendar, search Slack, pull Jira tickets, and more — directly in conversation.

**For first-timers, explain it this way**: "MCPs are like giving Claude login access to your work tools. Instead of you copy-pasting information into the chat, Claude can go look things up directly."

---

## Available MCPs

Availability depends on your Claude environment (personal, team, or enterprise). Check what's available in your Claude project settings under **Integrations** or **Connected Apps**.

### Google Workspace (Calendar, Gmail, Docs, Sheets)

**What it gives you**:
- Read and create calendar events
- Search and read emails
- Find meeting times and free slots
- Access Google Docs and Sheets
- Create drafts

**Setup**:
1. In your Claude project, go to **Integrations** (or **Connected Apps**)
2. Find **Google Workspace** (or **Google Calendar**, **Gmail** — may appear separately)
3. Click **Connect** and sign in with your work Google account
4. Grant the requested permissions
5. **Test it**: Ask Claude "What's on my calendar today?"

**Common commands once connected**:
- "What's on my calendar today?"
- "Find a free 30-minute slot this week"
- "Search my email for messages from [person]"
- "Summarize the unread emails in my inbox"
- "Create a calendar event for [topic] on [date]"

---

### Slack

**What it gives you**:
- Read channels and DMs
- Search messages (public and private)
- Send messages and drafts
- Read threads
- Look up user profiles

**Setup**:
1. In your Claude project, go to **Integrations**
2. Find **Slack** and click **Connect**
3. Authorize with your Slack workspace
4. **Test it**: Ask Claude "Search Slack for recent messages mentioning [your project]"

**Common commands once connected**:
- "Check Slack for anything mentioning me in the last 24 hours"
- "Read the latest messages in #[channel-name]"
- "Draft a Slack message to [person] about [topic]"
- "Search Slack for discussions about [topic]"
- "Summarize the thread in #[channel] about [topic]"

---

### Atlassian (Jira + Confluence)

**What it gives you**:
- Search and read Jira issues
- Create and update tickets
- Transition issue status
- Search and read Confluence pages
- Add comments

**Setup**:
1. In your Claude project, go to **Integrations**
2. Find **Atlassian** and click **Connect**
3. Sign in with your Atlassian account
4. Select your organization's site when prompted
5. **Test it**: Ask Claude "Show me my open Jira tickets"

**Common commands once connected**:
- "What are my open Jira tickets?"
- "Show me the status of [project-key]"
- "Search Jira for issues assigned to me"
- "Find the Confluence page about [topic]"
- "Create a Jira ticket for [description]"
- "Update [TICKET-123] status to In Progress"

---

### Microsoft 365 (Outlook, Teams, OneDrive)

**What it gives you**:
- Read calendar events and find free time
- Search and read Outlook emails
- Access Teams messages and channels
- Browse OneDrive files

**Setup**:
1. In your Claude project, go to **Integrations**
2. Find **Microsoft 365** (or **Outlook**, **Teams** — may appear separately)
3. Sign in with your work Microsoft account
4. Grant the requested permissions
5. **Test it**: Ask Claude "What meetings do I have today?"

**Common commands once connected**:
- "What's on my Outlook calendar today?"
- "Search my email for messages from [person]"
- "Check Teams for recent messages in [channel]"
- "Find the file about [topic] in OneDrive"

---

### Notion

**What it gives you**:
- Search and read pages and databases
- Create and update pages
- Query databases with filters

**Setup**:
1. In your Claude project, go to **Integrations**
2. Find **Notion** and click **Connect**
3. Select which Notion pages/databases to share with Claude
4. **Test it**: Ask Claude "Search Notion for [topic]"

**Common commands once connected**:
- "Find the Notion page about [project]"
- "What's in my task database?"
- "Create a Notion page with notes from today's meeting"

---

### Linear

**What it gives you**:
- Search and read issues
- Create and update tickets
- Track project progress

**Setup**:
1. In your Claude project, go to **Integrations**
2. Find **Linear** and click **Connect**
3. Authorize with your Linear workspace
4. **Test it**: Ask Claude "Show me my assigned Linear issues"

---

### GitHub

**What it gives you**:
- Search repositories and code
- Read and create issues
- Review pull requests
- Check CI/CD status

**Setup**:
1. In your Claude project, go to **Integrations**
2. Find **GitHub** and click **Connect**
3. Authorize with your GitHub account
4. Select which repositories to grant access to
5. **Test it**: Ask Claude "Show me open PRs in [repo]"

---

### Other MCPs

New integrations are added regularly. Check your Claude project's **Integrations** page for the latest. If you use a tool that isn't listed, you can still:
- Paste content from that tool into conversations
- Ask Claude to help you format outputs for that tool
- Use webhooks or Zapier to bridge the gap

---

## Recommended Setup by Role

### Engineering Leaders
**Must-have**: Calendar + Email, Slack/Teams, Jira/Linear
**Nice-to-have**: GitHub, Confluence/Notion
- Calendar for meeting prep and scheduling
- Slack/Teams for team monitoring and communication
- Jira/Linear for sprint tracking and ticket management
- Confluence/Notion for docs and specs

### Business Leaders / Executives
**Must-have**: Calendar + Email, Slack/Teams
**Nice-to-have**: Jira/Linear (if you track projects), Notion
- Calendar and email are your primary tools
- Slack/Teams for staying connected without drowning in channels

### Program / Project Managers
**Must-have**: Calendar + Email, Slack/Teams, Jira/Linear/Notion
- Full integration — you live in all these tools

### People Leaders (HR, L&D)
**Must-have**: Calendar + Email, Slack/Teams
- Calendar-heavy for 1:1s and team meetings
- Slack/Teams for team engagement

### Startup / Small Team
**Must-have**: Calendar + Email, Slack
**Nice-to-have**: Linear/Notion, GitHub
- Fewer tools, but deeper integration with each

### Freelancer / Solo
**Must-have**: Calendar + Email
**Nice-to-have**: Notion, GitHub
- Calendar and email cover most needs — add project tools as needed

---

## Troubleshooting

**"Claude can't access my calendar/email"**
- Check that you connected with your work account (not personal)
- Try disconnecting and reconnecting the integration
- Some calendar items from external orgs may not be accessible

**"Slack search isn't finding messages"**
- Slack search respects your permissions — Claude can only see channels you're a member of
- Private channels require explicit access
- Very recent messages (< 1 minute) may not be indexed yet

**"Jira/Confluence isn't connecting"**
- Make sure you selected the correct Atlassian site for your organization
- Check that your Atlassian account has the necessary permissions
- Some project boards may have restricted access

**"I connected everything but Claude seems slow"**
- First queries after connecting are slower as Claude establishes the connection
- Subsequent queries in the same conversation are faster
- If consistently slow, try starting a new conversation

---

## Privacy & Security Notes

Generate these notes in the project instructions to set expectations:

- MCPs use OAuth — Claude never sees or stores your password
- Claude accesses tools on your behalf with your permissions
- Claude cannot access anything you don't have access to
- Conversations with tool data follow the same privacy policies as regular Claude conversations
- You can disconnect any integration at any time
