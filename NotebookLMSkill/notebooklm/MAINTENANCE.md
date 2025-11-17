# NotebookLM Skill Maintenance Guide

**Critical Resource for Long-Term Success**

This guide provides everything you need to maintain the NotebookLM skill when Google changes their UI (which they will). Browser automation is fragile - this guide makes it manageable.

---

## Table of Contents

- [The Reality](#the-reality)
- [Current UI State](#current-ui-state)
- [Detecting Changes](#detecting-changes)
- [Updating Selectors](#updating-selectors)
- [Version Tracking](#version-tracking)
- [Testing Updates](#testing-updates)
- [Community Coordination](#community-coordination)
- [Maintenance Schedule](#maintenance-schedule)
- [Preventive Strategies](#preventive-strategies)

---

## The Reality

### Browser Automation is Fragile

**This is not a bug, it's the nature of browser automation:**

- ✅ NotebookLM provides immense value (source-grounded answers, reduced hallucinations)
- ⚠️ NotebookLM is a web interface that Google controls
- 🔧 Google WILL change their UI without notice
- 📅 Changes WILL break CSS selectors
- 🛠️ You WILL need to update selectors

**This is normal.** Every tool that automates web interfaces faces this. The key is being prepared.

### Why We Accept This Trade-Off

**Benefits:**
- Drastically reduced hallucinations through source grounding
- Citation-backed answers from Gemini
- Multi-source synthesis across 50+ documents
- Token efficiency (avoid feeding massive docs to Claude)

**Cost:**
- Occasional maintenance when UI changes
- 5-30 minutes to update selectors when broken
- Need to monitor for breakage

**Verdict:** For most users, the hallucination reduction is worth the occasional maintenance.

---

## Current UI State

### As of Integration (January 2025)

**NotebookLM Version:** December 2024 UI
**Last Verified:** January 16, 2025
**Status:** Working

### Current Selectors

**Chat Input:**
```python
# Primary selector (English UI)
"textarea.query-box-input"

# Fallback selector (German UI example)
'textarea[aria-label="Feld für Anfragen"]'
```

**Response Content:**
```python
# Multiple selectors for robustness
".response-content"
".message-content"
".query-response"
```

**Location in code:**
- Chat input: `scripts/browser_session.py` lines 177-182
- Response content: `scripts/browser_session.py` line 241

### Why Multiple Selectors?

- **Internationalization**: NotebookLM UI varies by language
- **Robustness**: If one selector fails, fallback to another
- **Version changes**: Different UI versions may use different classes

---

## Detecting Changes

### Signs of UI Change

**Immediate indicators:**
1. Skill worked yesterday, fails today
2. Error messages mentioning selectors:
   ```
   Element not found: textarea.query-box-input
   Timeout waiting for selector
   ```
3. Browser opens but doesn't type/interact
4. No response retrieved after question submitted

### First Response Steps

**1. Verify it's a UI change (not other issue):**
```bash
# Test with visible browser
cd ~/.claude/skills/notebooklm
python scripts/run.py ask_question.py --question "test" --show-browser
```

Watch what happens:
- Does browser open? (If not, authentication issue)
- Does it navigate to notebook? (If not, network/auth issue)
- Does it find the input box? (If not, SELECTOR ISSUE)
- Does it type and submit? (If not, selector issue)
- Does it extract response? (If not, response selector issue)

**2. Check for existing fixes:**
```bash
# Check original repository first
# Visit: https://github.com/PleasePrompto/notebooklm-skill/issues
# Look for recent issues about selector failures
```

Someone else has likely already encountered and possibly fixed it.

**3. Check for announcements:**
- Google NotebookLM blog/Twitter
- Recent Google I/O or AI announcements
- NotebookLM changelog if available

---

## Updating Selectors

### Complete Step-by-Step Process

#### Step 1: Inspect the New UI

**Enable browser visibility and pause on error:**

```bash
cd ~/.claude/skills/notebooklm
python scripts/run.py ask_question.py --question "test" --show-browser
```

**In the browser window that opens:**

1. Right-click on the chat input textarea
2. Select "Inspect" or "Inspect Element"
3. The browser DevTools will open highlighting the element

**Gather information:**
- **Element type**: `<textarea>`, `<input>`, `<div contenteditable>`, etc.
- **Class names**: e.g., `class="query-input-box new-style"`
- **ID**: e.g., `id="notebook-chat-input"`
- **Aria labels**: e.g., `aria-label="Ask a question"`
- **Data attributes**: e.g., `data-testid="chat-input"`

**Take screenshots for reference.**

#### Step 2: Determine Best Selector Strategy

**Selector priority (from most to least stable):**

1. **Data attributes**: `[data-testid="chat-input"]` (most stable, rarely change)
2. **ARIA labels**: `[aria-label="Ask a question"]` (semantic, stable)
3. **IDs**: `#notebook-chat-input` (stable but may change)
4. **Class names**: `.query-box-input` (least stable, change frequently)

**Recommendation**: Use data attributes or aria labels when available, with class name fallback.

#### Step 3: Update browser_session.py

**Location**: `~/.claude/skills/notebooklm/scripts/browser_session.py`

**Find the chat input selector section (around line 177-182):**

```python
# OLD (broken):
chat_input_selector = "textarea.query-box-input"
try:
    self.page.wait_for_selector(chat_input_selector, timeout=5000, state="visible")
except Exception:
    chat_input_selector = 'textarea[aria-label="Feld für Anfragen"]'
    self.page.wait_for_selector(chat_input_selector, timeout=5000, state="visible")
```

**Update with new selectors:**

```python
# NEW (updated):
# Try data attribute first (most stable)
chat_input_selector = 'textarea[data-testid="chat-input"]'
try:
    self.page.wait_for_selector(chat_input_selector, timeout=5000, state="visible")
except Exception:
    # Fallback to aria label
    try:
        chat_input_selector = 'textarea[aria-label="Ask a question"]'
        self.page.wait_for_selector(chat_input_selector, timeout=5000, state="visible")
    except Exception:
        # Last resort: class name (update with new class)
        chat_input_selector = "textarea.NEW-CLASS-NAME"
        self.page.wait_for_selector(chat_input_selector, timeout=5000, state="visible")
```

**Key points:**
- Keep multiple fallbacks for robustness
- Most stable selector first, least stable last
- Include timeout and state="visible"

#### Step 4: Update Response Selectors (if needed)

**Find response selector section (around line 241):**

```python
# OLD (if broken):
responses = self.page.query_selector_all(".response-content, .message-content, .query-response")
```

**Inspect response elements the same way:**
1. Right-click on a response in NotebookLM
2. Inspect element
3. Note selectors

**Update with new selectors:**

```python
# NEW (updated):
responses = self.page.query_selector_all(
    ".response-content, .message-content, .query-response, "
    "[data-testid='response'], .new-response-class"
)
```

**Add new selectors to the comma-separated list, don't remove old ones (backward compatibility).**

#### Step 5: Update _wait_for_ready Method (if needed)

**Location**: Around line 148-156

This method waits for the page to be ready before interacting.

```python
# Check if this also needs updating based on new UI
def _wait_for_ready(self):
    """Wait for NotebookLM page to be ready"""
    try:
        # Try primary selector
        self.page.wait_for_selector("textarea.query-box-input", timeout=10000, state="visible")
    except Exception:
        # Try alternative selector
        self.page.wait_for_selector('textarea[aria-label="Feld für Anfragen"]', timeout=5000, state="visible")
```

**Update with same selectors as chat input section for consistency.**

---

## Version Tracking

### Document Your Changes

**After updating selectors, document:**

1. **Update MAINTENANCE.md** (this file) with new current state:
   ```markdown
   ### As of [Date]

   **NotebookLM Version:** [Month Year] UI
   **Last Verified:** [Date]
   **Status:** Working

   **Selectors changed:**
   - Chat input: `[old selector]` → `[new selector]`
   - Reason: [UI redesign / class rename / etc.]
   ```

2. **Update CHANGELOG.md** with new version:
   ```markdown
   ## [1.0.1] - YYYY-MM-DD

   ### Fixed
   - Updated chat input selectors for NotebookLM UI change (January 2025)
   - Changed from `.query-box-input` to `[data-testid="chat-input"]`
   - Added fallback selectors for internationalization
   ```

3. **Track in code comments:**
   ```python
   # Updated 2025-01-XX for NotebookLM UI redesign
   # Original selector: "textarea.query-box-input"
   # New selector: 'textarea[data-testid="chat-input"]'
   chat_input_selector = 'textarea[data-testid="chat-input"]'
   ```

### Check Your Environment

```bash
cd ~/.claude/skills/notebooklm
source .venv/bin/activate

# Python version
python --version

# Patchright version
pip show patchright

# Chrome/Chromium version
python -c "from patchright.sync_api import sync_playwright; p = sync_playwright().start(); b = p.chromium.launch(channel='chrome'); print(b.version); b.close(); p.stop()"
```

**Document versions when issues occur** to help troubleshoot patterns.

---

## Testing Updates

### Test Suite for Selector Changes

**After updating selectors, run comprehensive tests:**

#### Test 1: Basic Authentication Check
```bash
python scripts/run.py auth_manager.py status
```
Expected: Shows authentication status without errors.

#### Test 2: Notebook List
```bash
python scripts/run.py notebook_manager.py list
```
Expected: Shows your notebook library.

#### Test 3: Simple Question (Visible Browser)
```bash
python scripts/run.py ask_question.py \
  --question "What topics are covered in this notebook?" \
  --show-browser
```

**Watch for:**
- ✅ Browser opens
- ✅ Navigates to notebook
- ✅ Finds input box
- ✅ Types question smoothly
- ✅ Submits (Enter key press)
- ✅ Waits for response
- ✅ Extracts answer
- ✅ Closes browser
- ✅ Returns answer to terminal

#### Test 4: Follow-Up Question
```bash
# Ask two questions in sequence
python scripts/run.py ask_question.py --question "What is this notebook about?"
python scripts/run.py ask_question.py --question "What are the key topics covered?"
```

Expected: Both complete successfully.

#### Test 5: Different Notebook
```bash
python scripts/run.py ask_question.py \
  --question "test" \
  --notebook-url "https://notebooklm.google.com/notebook/[different-id]"
```

Expected: Works with different notebook URLs.

### Regression Testing

**Test that old functionality still works:**
- Authentication still persists
- Library management still functions
- Cleanup manager still works
- All scripts accessible via run.py

---

## Community Coordination

### Reporting Issues

**When you discover UI changes:**

1. **Check if already reported:**
   - Visit: https://github.com/PleasePrompto/notebooklm-skill/issues
   - Search for recent selector issues
   - Check if someone already posted a fix

2. **Report new breakage:**
   ```markdown
   Title: Selectors broken after NotebookLM UI update (Jan 2025)

   ## Problem
   Chat input selector `textarea.query-box-input` no longer works as of [date].

   ## Error Message
   ```
   [paste error message]
   ```

   ## Environment
   - NotebookLM URL: https://notebooklm.google.com/notebook/...
   - Patchright version: 1.55.2
   - Python version: 3.11
   - Date noticed: 2025-01-XX

   ## Investigation
   New selector appears to be: `[data-testid="chat-input"]`

   ## Screenshots
   [attach screenshot of inspected element]
   ```

3. **Share your fix:**
   ```markdown
   ## Solution
   Updated `browser_session.py` line 177:

   ```python
   chat_input_selector = 'textarea[data-testid="chat-input"]'
   ```

   Tested and working as of [date].
   ```

### Contributing Fixes Back

**If you fix selectors, consider pull request:**

1. Fork original repository
2. Create branch: `fix/selectors-jan-2025`
3. Update selectors with documentation
4. Test thoroughly
5. Submit PR with clear description
6. Help others facing same issue

### Staying Informed

**Monitor for updates:**

- **Watch original repo**: https://github.com/PleasePrompto/notebooklm-skill
- **Check issues regularly**: Especially after Google events
- **Subscribe to NotebookLM announcements**: Google AI blog, Twitter
- **Join community discussions**: GitHub Discussions if available

---

## Maintenance Schedule

### Recommended Monitoring Frequency

| Frequency | Task | Time Required | Purpose |
|-----------|------|---------------|---------|
| **Weekly** | Quick test query | 1 minute | Verify still working |
| **Monthly** | Check for updates | 5 minutes | Stay current with fixes |
| **After major Google events** | Full test | 10 minutes | Anticipate UI changes |
| **When errors occur** | Investigate & fix | 15-30 minutes | Repair immediately |

### Weekly Quick Test

```bash
#!/bin/bash
# Save as: test-notebooklm.sh
cd ~/.claude/skills/notebooklm
echo "Testing NotebookLM skill..."
python scripts/run.py ask_question.py --question "What topics does this notebook cover?"
if [ $? -eq 0 ]; then
    echo "✅ NotebookLM skill working"
else
    echo "❌ NotebookLM skill broken - check maintenance guide"
fi
```

Run weekly: `bash test-notebooklm.sh`

### Monthly Review Checklist

- [ ] Run quick test query
- [ ] Check original repository for issues
- [ ] Review any selector change reports
- [ ] Update skill if fixes available
- [ ] Document any changes
- [ ] Verify authentication still valid

### Post-Google-Event Check

**After Google I/O, AI summits, or major announcements:**

1. Run full test suite (see Testing Updates section)
2. Check NotebookLM for visible UI changes
3. Monitor community for reports
4. Be ready to update selectors quickly

---

## Preventive Strategies

### Making Selectors More Resilient

**Use multiple selector strategies simultaneously:**

```python
def find_chat_input(self):
    """Try multiple selector strategies"""
    selectors = [
        'textarea[data-testid="chat-input"]',      # Most stable
        'textarea[aria-label*="Ask"]',              # Partial match, flexible
        'textarea.query-box-input',                 # Class name
        'textarea.query-input',                     # Variation
        'div[role="textbox"]',                      # Semantic role
        'textarea:not([disabled])',                 # Any enabled textarea
    ]

    for selector in selectors:
        try:
            element = self.page.wait_for_selector(selector, timeout=2000, state="visible")
            if element:
                return element
        except:
            continue

    raise Exception("Could not find chat input with any known selector")
```

**Benefits:**
- Gracefully degrades through selector list
- Catches UI changes before complete failure
- Logs which selector worked for debugging

### Automatic Selector Discovery (Advanced)

**For very resilient automation, consider:**

```python
def smart_find_textarea(self):
    """Find textarea by characteristics rather than specific selector"""
    # Look for any textarea that:
    # - Is visible
    # - Is not disabled
    # - Has a parent form or submission mechanism
    # - Is large enough for chat input

    textareas = self.page.query_selector_all("textarea:not([disabled])")
    for textarea in textareas:
        box = textarea.bounding_box()
        if box and box['height'] > 30:  # Likely chat input, not tiny field
            return textarea

    raise Exception("Could not find suitable chat input")
```

**Trade-offs:**
- More resilient to selector changes
- May match wrong element if UI has multiple textareas
- Slower (checks multiple elements)

### Documentation as Defense

**The best defense is good documentation:**

1. **Clear selector locations**: Anyone can find and update
2. **Step-by-step guides**: This maintenance file
3. **Known working versions**: Version tracking
4. **Community coordination**: Fast fixes when issues occur

---

## Emergency Recovery

### Complete Selector Failure

**If you can't figure out new selectors:**

1. **Use NotebookLM manually** while you troubleshoot
2. **Check original repository** for community fixes
3. **Ask for help** in GitHub issues
4. **Consider MCP server** as temporary alternative (same issue though)
5. **Document for future**: Take screenshots, note error messages

### Temporary Workarounds

**While waiting for fix:**

```bash
# Option 1: Direct NotebookLM usage
# Use NotebookLM in browser, copy/paste answers to Claude

# Option 2: Switch to MCP server temporarily
# May have same issue, but community might fix it first

# Option 3: Feed docs directly to Claude
# Higher token cost, but no automation dependency
```

---

## Success Metrics

### How to Know You're Maintaining Well

**Good maintenance looks like:**
- ✅ Skill works consistently week-to-week
- ✅ You catch UI changes within days
- ✅ Fixes take 15-30 minutes, not hours
- ✅ You contribute fixes back to community
- ✅ Documentation stays current

**Poor maintenance looks like:**
- ❌ Skill broken for weeks before you notice
- ❌ Can't figure out how to fix when broken
- ❌ No documentation of changes
- ❌ Frustrated users with no support

### Measuring Value vs. Maintenance Cost

**Track over time:**
- **Queries per month**: How much are you using it?
- **Maintenance hours per month**: How much time fixing?
- **Value delivered**: Hallucinations prevented, time saved

**Rule of thumb:**
- If maintenance > 1 hour/month: Consider alternatives
- If value < cost: Stick with direct doc feeding or local RAG
- If value > cost: Maintenance worth it

---

## Conclusion

Browser automation maintenance is **manageable with preparation**. This guide gives you everything you need to keep the NotebookLM skill running long-term.

**Remember:**
- UI changes are normal, not emergencies
- Community typically fixes issues quickly
- 15-30 minutes of maintenance every few months
- Value of hallucination reduction makes it worthwhile

**When in doubt:**
- Check this guide first
- Check original repository issues second
- Ask for help third

**You've got this!**

---

**Last Updated**: January 16, 2025
**Next Review**: February 16, 2025
**Maintainer**: [Your name / AISkills repository]
