<div align="center">

# NotebookLM Claude Code Skill

**Let [Claude Code](https://github.com/anthropics/claude-code) chat directly with NotebookLM for source-grounded answers based exclusively on your uploaded documents**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-purple.svg)](https://www.anthropic.com/news/skills)
[![Based on](https://img.shields.io/badge/Based%20on-NotebookLM%20MCP-green.svg)](https://github.com/PleasePrompto/notebooklm-mcp)
[![GitHub](https://img.shields.io/github/stars/PleasePrompto/notebooklm-skill?style=social)](https://github.com/PleasePrompto/notebooklm-skill)

> Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed answers from Gemini. Browser automation, library management, persistent auth. Drastically reduced hallucinations - answers only from your uploaded documents.

[Installation](#installation) • [Quick Start](#quick-start) • [Why NotebookLM](#why-notebooklm-not-local-rag) • [How It Works](#how-it-works) • [MCP Alternative](https://github.com/PleasePrompto/notebooklm-mcp)

</div>

---

## ⚠️ Important: Local Claude Code Only

**This skill works ONLY with local [Claude Code](https://github.com/anthropics/claude-code) installations, NOT in the web UI.**

The web UI runs skills in a sandbox without network access, which this skill requires for browser automation. You must use [Claude Code](https://github.com/anthropics/claude-code) locally on your machine.

---

## The Problem

When you tell [Claude Code](https://github.com/anthropics/claude-code) to "search through my local documentation", here's what happens:
- **Massive token consumption**: Searching through documentation means reading multiple files repeatedly
- **Inaccurate retrieval**: Searches for keywords, misses context and connections between docs
- **Hallucinations**: When it can't find something, it invents plausible-sounding APIs
- **Manual copy-paste**: Switching between NotebookLM browser and your editor constantly

## The Solution

This Claude Code Skill lets [Claude Code](https://github.com/anthropics/claude-code) chat directly with [**NotebookLM**](https://notebooklm.google/) — Google's **source-grounded knowledge base** powered by Gemini 2.5 that provides intelligent, synthesized answers exclusively from your uploaded documents.

```
Your Task → Claude asks NotebookLM → Gemini synthesizes answer → Claude writes correct code
```

**No more copy-paste dance**: Claude asks questions directly and gets answers straight back in the CLI. It builds deep understanding through automatic follow-ups, getting specific implementation details, edge cases, and best practices.

---

## Why NotebookLM, Not Local RAG?

| Approach | Token Cost | Setup Time | Hallucinations | Answer Quality |
|----------|------------|------------|----------------|----------------|
| **Feed docs to Claude** | 🔴 Very high (multiple file reads) | Instant | Yes - fills gaps | Variable retrieval |
| **Web search** | 🟡 Medium | Instant | High - unreliable sources | Hit or miss |
| **Local RAG** | 🟡 Medium-High | Hours (embeddings, chunking) | Medium - retrieval gaps | Depends on setup |
| **NotebookLM Skill** | 🟢 Minimal | 5 minutes | **Minimal** - source-grounded only | Expert synthesis |

### What Makes NotebookLM Superior?

1. **Pre-processed by Gemini**: Upload docs once, get instant expert knowledge
2. **Natural language Q&A**: Not just retrieval — actual understanding and synthesis
3. **Multi-source correlation**: Connects information across 50+ documents
4. **Citation-backed**: Every answer includes source references
5. **No infrastructure**: No vector DBs, embeddings, or chunking strategies needed

---

## Installation

### The simplest installation ever:

```bash
# 1. Create skills directory (if it doesn't exist)
mkdir -p ~/.claude/skills

# 2. Clone this repository
cd ~/.claude/skills
git clone https://github.com/PleasePrompto/notebooklm-skill notebooklm

# 3. That's it! Open Claude Code and say:
"What are my skills?"
```

When you first use the skill, it automatically:
- Creates an isolated Python environment (`.venv`)
- Installs all dependencies including **Google Chrome**
- Sets up browser automation with Chrome (not Chromium) for maximum reliability
- Everything stays contained in the skill folder

**Note:** The setup uses real Chrome instead of Chromium for cross-platform reliability, consistent browser fingerprinting, and better anti-detection with Google services

---

## Quick Start

### 1. Check your skills

Say in Claude Code:
```
"What skills do I have?"
```

Claude will list your available skills including NotebookLM.

### 2. Authenticate with Google (one-time)

```
"Set up NotebookLM authentication"
```
*A Chrome window opens → log in with your Google account*

### 3. Create your knowledge base

Go to [notebooklm.google.com](https://notebooklm.google.com) → Create notebook → Upload your docs:
- 📄 PDFs, Google Docs, markdown files
- 🔗 Websites, GitHub repos
- 🎥 YouTube videos
- 📚 Multiple sources per notebook

Share: **⚙️ Share → Anyone with link → Copy**

### 4. Add to your library

**Option A: Let Claude figure it out (Smart Add)**
```
"Query this notebook about its content and add it to my library: [your-link]"
```
Claude will automatically query the notebook to discover its content, then add it with appropriate metadata.

**Option B: Manual add**
```
"Add this NotebookLM to my library: [your-link]"
```
Claude will ask for a name and topics, then save it for future use.

### 5. Start researching

```
"What does my React docs say about hooks?"
```

Claude automatically selects the right notebook and gets the answer directly from NotebookLM.

---

## How It Works

This is a **Claude Code Skill** - a local folder containing instructions and scripts that Claude Code can use when needed. Unlike the [MCP server version](https://github.com/PleasePrompto/notebooklm-mcp), this runs directly in Claude Code without needing a separate server.

### Key Differences from MCP Server

| Feature | This Skill | MCP Server |
|---------|------------|------------|
| **Protocol** | Claude Skills | Model Context Protocol |
| **Installation** | Clone to `~/.claude/skills` | `claude mcp add ...` |
| **Sessions** | Fresh browser each question | Persistent chat sessions |
| **Compatibility** | Claude Code only (local) | Claude Code, Codex, Cursor, etc. |
| **Language** | Python | TypeScript |
| **Distribution** | Git clone | npm package |

### Architecture

```
~/.claude/skills/notebooklm/
├── SKILL.md              # Instructions for Claude
├── scripts/              # Python automation scripts
│   ├── ask_question.py   # Query NotebookLM
│   ├── notebook_manager.py # Library management
│   └── auth_manager.py   # Google authentication
├── .venv/                # Isolated Python environment (auto-created)
└── data/                 # Local notebook library
```

When you mention NotebookLM or send a notebook URL, Claude:
1. Loads the skill instructions
2. Runs the appropriate Python script
3. Opens a browser, asks your question
4. Returns the answer directly to you
5. Uses that knowledge to help with your task

---

## Core Features

### **Source-Grounded Responses**
NotebookLM significantly reduces hallucinations by answering exclusively from your uploaded documents. If information isn't available, it indicates uncertainty rather than inventing content.

### **Direct Integration**
No copy-paste between browser and editor. Claude asks and receives answers programmatically.

### **Smart Library Management**
Save NotebookLM links with tags and descriptions. Claude auto-selects the right notebook for your task.

### **Automatic Authentication**
One-time Google login, then authentication persists across sessions.

### **Self-Contained**
Everything runs in the skill folder with an isolated Python environment. No global installations.

### **Human-Like Automation**
Uses realistic typing speeds and interaction patterns to avoid detection.

---

## Common Commands

| What you say | What happens |
|--------------|--------------|
| *"Set up NotebookLM authentication"* | Opens Chrome for Google login |
| *"Add [link] to my NotebookLM library"* | Saves notebook with metadata |
| *"Show my NotebookLM notebooks"* | Lists all saved notebooks |
| *"Ask my API docs about [topic]"* | Queries the relevant notebook |
| *"Use the React notebook"* | Sets active notebook |
| *"Clear NotebookLM data"* | Fresh start (keeps library) |

---

## Real-World Examples

### Example 1: Workshop Manual Query

**User asks**: "Check my Suzuki GSR 600 workshop manual for brake fluid type, engine oil specs, and rear axle torque."

**Claude automatically**:
- Authenticates with NotebookLM
- Asks comprehensive questions about each specification
- Follows up when prompted "Is that ALL you need to know?"
- Provides accurate specifications: DOT 4 brake fluid, SAE 10W-40 oil, 100 N·m rear axle torque

![NotebookLM Chat Example](images/example_notebookchat.png)

### Example 2: Building Without Hallucinations

**You**: "I need to build an n8n workflow for Gmail spam filtering. Use my n8n notebook."

**Claude's internal process:**
```
→ Loads NotebookLM skill
→ Activates n8n notebook
→ Asks comprehensive questions with follow-ups
→ Synthesizes complete answer from multiple queries
```

**Result**: Working workflow on first try, no debugging hallucinated APIs.

---

## Technical Details

### Core Technology
- **Patchright**: Browser automation library (Playwright-based)
- **Python**: Implementation language for this skill
- **Stealth techniques**: Human-like typing and interaction patterns

Note: The MCP server uses the same Patchright library but via TypeScript/npm ecosystem.

### Dependencies
- **patchright==1.55.2**: Browser automation
- **python-dotenv==1.0.0**: Environment configuration
- Automatically installed in `.venv` on first use

### Data Storage

All data is stored locally within the skill directory:

```
~/.claude/skills/notebooklm/data/
├── library.json       - Your notebook library with metadata
├── auth_info.json     - Authentication status info
└── browser_state/     - Browser cookies and session data
```

**Important Security Note:**
- The `data/` directory contains sensitive authentication data and personal notebooks
- It's automatically excluded from git via `.gitignore`
- NEVER manually commit or share the contents of the `data/` directory

### Session Model

Unlike the MCP server, this skill uses a **stateless model**:
- Each question opens a fresh browser
- Asks the question, gets the answer
- Adds a follow-up prompt to encourage Claude to ask more questions
- Closes the browser immediately

This means:
- No persistent chat context
- Each question is independent
- But your notebook library persists
- **Follow-up mechanism**: Each answer includes "Is that ALL you need to know?" to prompt Claude to ask comprehensive follow-ups

For multi-step research, Claude automatically asks follow-up questions when needed.

---

## Known Issues and Limitations

### Browser Automation Fragility (CRITICAL)

**UI Changes Will Break the Skill:**
- NotebookLM UI updates will break selectors
- Requires manual selector updates (see Maintenance section)
- Expected and normal for browser automation
- Community typically reports and fixes quickly

**Workaround:** Monitor weekly, check original repository for updates, be prepared to update selectors yourself (step-by-step guide in Maintenance section).

### Skill-Specific Limitations

**1. Local Claude Code Only**
- Does NOT work in Claude web UI (sandbox restrictions)
- Requires local Claude Code installation
- Needs network access for browser automation

**2. Stateless Sessions**
- Each question opens fresh browser session
- No persistent chat context between queries
- Can't reference "previous answer" across questions
- **Mitigation:** Follow-up mechanism prompts comprehensive questioning

**3. Browser Overhead**
- Each query takes 3-5 seconds (browser launch + interaction)
- Slower than direct API calls
- **Trade-off:** Hallucination reduction worth the wait

**4. Python Playwright Limitation**
- Cannot pass `storage_state` to `launch_persistent_context` in Python
- Known bug: Session cookies don't persist in browser profile
- **Workaround:** Hybrid approach (browser profile + manual cookie injection)
- See `AUTHENTICATION.md` for technical details

### NotebookLM Service Limitations

**1. Rate Limits**
- Free tier: ~50 queries per day
- Resets around midnight Pacific Time
- **Workaround:** Switch Google accounts or upgrade to Workspace

**2. Manual Upload Required**
- Must upload documents to NotebookLM via web interface
- Skill cannot automate document upload
- Create notebooks manually first

**3. Share Requirement**
- Notebooks must be shared ("Anyone with link")
- Required for skill to access via URL
- Links remain private to those who have them

**4. Source Limitations**
- Maximum 50 sources per notebook
- File size limits (~25MB per source typically)
- Supported formats: PDF, Google Docs, markdown, websites, YouTube

### Technical Limitations

**1. Browser Detection Risk**
- Google may detect automation despite stealth techniques
- Humanization reduces but doesn't eliminate risk
- **Recommendation:** Use dedicated Google account for automation

**2. Network Dependency**
- Requires network access to notebooklm.google.com
- Cannot work offline
- Proxy configuration supported via environment variables

**3. Regional Availability**
- NotebookLM not available in all regions
- Check availability at notebooklm.google.com
- May require VPN in unsupported regions

### Comparison with Alternatives

| Factor | NotebookLM Skill | Local RAG | Direct Doc Feed | MCP Server |
|--------|------------------|-----------|-----------------|------------|
| **Maintenance** | Required (UI changes) | Low | None | Required (UI changes) |
| **Setup Time** | 5 minutes | Hours | Instant | 10 minutes |
| **Token Cost** | Minimal | Medium-High | Very High | Minimal |
| **Hallucinations** | Minimal (source-grounded) | Medium | Yes (fills gaps) | Minimal (source-grounded) |
| **Query Speed** | 3-5 seconds | <1 second | Instant | 3-5 seconds |
| **Multi-tool Support** | Claude Code only | N/A | N/A | Multiple tools |
| **Sessions** | Stateless | N/A | N/A | Persistent |

**When to use NotebookLM Skill:**
- Need source-grounded answers with citations
- Can tolerate occasional maintenance
- Token efficiency important
- Working with comprehensive documentation sets

**When to avoid:**
- Mission-critical zero-downtime requirements
- Cannot handle selector update maintenance
- Simple queries where Claude's knowledge suffices
- Need guaranteed long-term stability

---

## FAQ

**Why doesn't this work in the Claude web UI?**
The web UI runs skills in a sandbox without network access. Browser automation requires network access to reach NotebookLM.

**How is this different from the MCP server?**
This is a simpler, Python-based implementation that runs directly as a Claude Skill. The MCP server is more feature-rich with persistent sessions and works with multiple tools (Codex, Cursor, etc.).

**Can I use both this skill and the MCP server?**
Yes! They serve different purposes. Use the skill for quick Claude Code integration, use the MCP server for persistent sessions and multi-tool support.

**What if Chrome crashes?**
Run: `"Clear NotebookLM browser data"` and try again.

**Is my Google account secure?**
Chrome runs locally on your machine. Your credentials never leave your computer. Use a dedicated Google account if you're concerned.

---

## Maintenance: The Reality of Browser Automation

### Critical Understanding

**This is the most important section - browser automation is fragile by design.**

This skill works by automating interactions with NotebookLM's web interface. Google can (and will) change their UI at any time, which will break the skill until selectors are updated.

**Set realistic expectations:**
- ✅ Skill provides immense value through source-grounded answers
- ⚠️ UI changes WILL eventually break automation
- 🔧 You may need to fix selectors yourself or wait for updates
- 📅 Expect maintenance required after NotebookLM updates

**This is normal** for browser automation. The value of hallucination reduction makes the trade-off worthwhile.

### Current UI Selectors (December 2024)

The skill uses these selectors to interact with NotebookLM:

```python
# Chat input box
"textarea.query-box-input"
'textarea[aria-label="Feld für Anfragen"]'  # German fallback

# Response content
".response-content"
".message-content"
".query-response"
```

### Detecting UI Changes

**Signs that NotebookLM UI has changed:**
1. Skill worked yesterday, fails today
2. Error: `Element not found: textarea.query-box-input`
3. Timeout errors when previously working
4. Browser opens but doesn't type or interact

**Immediate actions:**
```bash
# 1. Test with visible browser to see what's happening
cd ~/.claude/skills/notebooklm
python scripts/run.py ask_question.py --question "test" --show-browser

# 2. Check original repository for updates
# Visit: https://github.com/PleasePrompto/notebooklm-skill/issues

# 3. Look for community reports of breakage
```

### Updating Selectors When UI Changes

**Step-by-step fix process:**

**1. Inspect the new UI:**
```bash
# Run with browser visible
python scripts/run.py ask_question.py --question "test" --show-browser

# In the browser window:
# - Right-click on chat input box → Inspect Element
# - Note the class names, aria-labels, and attributes
# - Take screenshots for reference
```

**2. Locate selector definitions:**
```bash
# Edit browser_session.py
cd ~/.claude/skills/notebooklm/scripts
# Look for these lines:

# Chat input selector (around line 177-182):
chat_input_selector = "textarea.query-box-input"
try:
    self.page.wait_for_selector(chat_input_selector, timeout=5000)
except Exception:
    chat_input_selector = 'textarea[aria-label="NEW_ARIA_LABEL_HERE"]'
```

**3. Update selectors:**
```python
# Replace with new selectors found in step 1
chat_input_selector = "textarea.NEW_CLASS_NAME"  # Your new selector
try:
    self.page.wait_for_selector(chat_input_selector, timeout=5000)
except Exception:
    # Add fallback selector
    chat_input_selector = 'textarea[aria-label="New Aria Label"]'
```

**4. Update response selectors if needed:**
```python
# Around line 241 in browser_session.py:
responses = self.page.query_selector_all(
    ".response-content, .message-content, .query-response, .YOUR_NEW_SELECTOR"
)
```

**5. Test the fix:**
```bash
python scripts/run.py ask_question.py --question "What topics are in this notebook?" --show-browser
```

**6. Share your fix:**
- Report to [original repository issues](https://github.com/PleasePrompto/notebooklm-skill/issues)
- Help others facing same breakage
- Consider contributing pull request

### Version Compatibility Tracking

**Current compatibility (as of integration):**
- NotebookLM UI: December 2024 version
- Selectors: Confirmed working at integration time
- Patchright: 1.55.2
- Chrome: Latest stable via Patchright

**Check your environment:**
```bash
cd ~/.claude/skills/notebooklm
source .venv/bin/activate

# Patchright version
pip show patchright

# Python version
python --version
```

### Monitoring Strategy

**Weekly check:**
```bash
# Quick test query to verify skill works
python scripts/run.py ask_question.py --question "What topics does this notebook cover?"
```

**Monthly review:**
- Check [original repository](https://github.com/PleasePrompto/notebooklm-skill) for updates
- Review any issues about UI changes
- Update if community reports problems

**Watch for Google announcements:**
- Google I/O events often include NotebookLM updates
- Subscribe to NotebookLM blog or Twitter for announcements
- UI redesigns typically announced in advance

### Community Support

**When skill breaks:**

1. **Check original repository first:**
   - Issues: https://github.com/PleasePrompto/notebooklm-skill/issues
   - Someone has likely already reported it
   - Solution may already be posted

2. **Report new breakage:**
   - Include error messages
   - Note what changed in UI
   - Include screenshots if possible
   - Mention NotebookLM URL that fails

3. **Share your fixes:**
   - Post working selectors
   - Help others troubleshoot
   - Consider pull request to original repo

### Maintenance Schedule Recommendation

| Frequency | Task | Purpose |
|-----------|------|---------|
| **Weekly** | Quick test query | Verify still working |
| **Monthly** | Check for updates | Stay current with fixes |
| **After major Google events** | Full test | Anticipate UI changes |
| **When errors occur** | Investigate immediately | Fix while UI change is fresh |

### Alternative: MCP Server Version

If maintenance burden is too high, consider the [NotebookLM MCP Server](https://github.com/PleasePrompto/notebooklm-mcp):
- TypeScript implementation
- Same Patchright browser automation (same maintenance needs!)
- Works with multiple tools (Codex, Cursor, Claude Code)
- Persistent sessions
- **Note:** Has identical UI change vulnerability

---

## Troubleshooting

For detailed troubleshooting, see `references/troubleshooting.md`. Quick reference below:

### Skill not found
```bash
# Make sure it's in the right location
ls ~/.claude/skills/notebooklm/
# Should show: SKILL.md, scripts/, etc.
```

### Authentication issues
```bash
# Check status
python scripts/run.py auth_manager.py status

# Setup authentication (browser MUST be visible)
python scripts/run.py auth_manager.py setup

# Re-authenticate if expired
python scripts/run.py auth_manager.py reauth

# Clear and start fresh
python scripts/run.py auth_manager.py clear
python scripts/run.py auth_manager.py setup
```

Natural language in Claude Code:
```
"Reset NotebookLM authentication"
"Set up NotebookLM authentication"
```

### Browser crashes
```bash
# Kill hanging browser processes
pkill -f chromium
pkill -f chrome

# Clean browser state (keeps library)
python scripts/run.py cleanup_manager.py --preserve-library --confirm

# Re-authenticate
python scripts/run.py auth_manager.py reauth
```

Natural language: `"Clear NotebookLM browser data"`

### Dependencies issues

**Most common cause:** Not using run.py wrapper!

```bash
# ✅ CORRECT - Always use run.py
python scripts/run.py ask_question.py --question "test"

# ❌ WRONG - Never call scripts directly
python scripts/ask_question.py --question "test"  # Will fail!
```

Manual environment rebuild:
```bash
cd ~/.claude/skills/notebooklm
rm -rf .venv
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m patchright install chromium
```

### Rate limiting (50 queries/day free tier)

```bash
# Option 1: Wait for reset (midnight Pacific Time)

# Option 2: Switch Google accounts
python scripts/run.py auth_manager.py clear
python scripts/run.py auth_manager.py setup  # Login with different account

# Option 3: Check usage
python scripts/run.py notebook_manager.py stats
```

### Selector failures (UI changed)

See **Maintenance** section above for complete selector update process.

Quick fix attempt:
```bash
# Test with visible browser to see what's wrong
python scripts/run.py ask_question.py --question "test" --show-browser

# Check for updates
git pull  # If installed via git

# Check original repository issues
# https://github.com/PleasePrompto/notebooklm-skill/issues
```

### Complete nuclear reset

```bash
# Backup library first!
mkdir -p ~/notebooklm-backup
cp ~/.claude/skills/notebooklm/data/library.json ~/notebooklm-backup/ 2>/dev/null

# Kill browsers
pkill -f chromium
pkill -f chrome

# Remove everything
cd ~/.claude/skills/notebooklm
rm -rf .venv data/

# Reinstall (run.py handles automatically)
python scripts/run.py auth_manager.py setup

# Restore library
if [ -f ~/notebooklm-backup/library.json ]; then
    mkdir -p data
    cp ~/notebooklm-backup/library.json data/
fi
```

### Detailed troubleshooting

See `references/troubleshooting.md` for:
- Network issues and proxy configuration
- Virtual environment problems
- Notebook access errors
- Error message reference table
- Debugging techniques
- Common questions and answers

---

## Disclaimer

This tool automates browser interactions with NotebookLM to make your workflow more efficient. However, a few friendly reminders:

**About browser automation:**
While I've built in humanization features (realistic typing speeds, natural delays, mouse movements) to make the automation behave more naturally, I can't guarantee Google won't detect or flag automated usage. I recommend using a dedicated Google account for automation rather than your primary account—think of it like web scraping: probably fine, but better safe than sorry!

**About CLI tools and AI agents:**
CLI tools like Claude Code, Codex, and similar AI-powered assistants are incredibly powerful, but they can make mistakes. Please use them with care and awareness:
- Always review changes before committing or deploying
- Test in safe environments first
- Keep backups of important work
- Remember: AI agents are assistants, not infallible oracles

I built this tool for myself because I was tired of the copy-paste dance between NotebookLM and my editor. I'm sharing it in the hope it helps others too, but I can't take responsibility for any issues, data loss, or account problems that might occur. Use at your own discretion and judgment.

That said, if you run into problems or have questions, feel free to open an issue on GitHub. I'm happy to help troubleshoot!

---

## Credits

This skill is inspired by my [**NotebookLM MCP Server**](https://github.com/PleasePrompto/notebooklm-mcp) and provides an alternative implementation as a Claude Code Skill:
- Both use Patchright for browser automation (TypeScript for MCP, Python for Skill)
- Skill version runs directly in Claude Code without MCP protocol
- Stateless design optimized for skill architecture

If you need:
- **Persistent sessions** → Use the [MCP Server](https://github.com/PleasePrompto/notebooklm-mcp)
- **Multiple tool support** (Codex, Cursor) → Use the [MCP Server](https://github.com/PleasePrompto/notebooklm-mcp)
- **Quick Claude Code integration** → Use this skill

---

## The Bottom Line

**Without this skill**: NotebookLM in browser → Copy answer → Paste in Claude → Copy next question → Back to browser...

**With this skill**: Claude researches directly → Gets answers instantly → Writes correct code

Stop the copy-paste dance. Start getting accurate, grounded answers directly in Claude Code.

```bash
# Get started in 30 seconds
cd ~/.claude/skills
git clone https://github.com/PleasePrompto/notebooklm-skill notebooklm
# Open Claude Code: "What are my skills?"
```

---

<div align="center">

Built as a Claude Code Skill adaptation of my [NotebookLM MCP Server](https://github.com/PleasePrompto/notebooklm-mcp)

For source-grounded, document-based research directly in Claude Code

</div>
