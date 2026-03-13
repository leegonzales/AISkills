---
name: build-timeline
description: Generate interactive HTML timelines of Claude Code development activity from conversation logs and git history. Use when user wants to visualize, document, or showcase how a project was built with Claude Code.
---

# Build Timeline — Claude Code Activity Visualizer

Generate beautiful, interactive standalone HTML timelines that chronicle how a project was built with Claude Code. Parses conversation logs (`.jsonl`) and git history to produce a visual walkthrough of agent spawns, tool calls, commands, file changes, parallel work, milestones, and errors.

## When to Use

Invoke when user:
- Asks to "visualize the build process" or "show how this was built"
- Wants to "document development history" or "create a build walkthrough"
- Says "generate a timeline" or "show agent activity"
- Needs to showcase Claude Code development workflow
- Wants to review what happened during a build session

## Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `[path]` | Target repo path | Current working directory |
| `--since <date>` | Start date filter (ISO or relative like "3 days ago") | All history |
| `--until <date>` | End date filter | Now |
| `--output <path>` | Output file path | `./build-timeline.html` |
| `--phases` | Auto-detect phases from git commit patterns and agent naming | Off |
| `--detailed` | Include all tool calls, not just major events | Off |
| `--theme <name>` | Visual theme: `default`, `dark`, `afs` | `default` |

## Workflow

Execute these steps in order. The SKILL.md is your complete reference — do not look for external scripts.

### Step 1: Identify the Target

Determine the target repository and parameters:

```
REPO_PATH = argument [path] or current working directory
REPO_NAME = basename of REPO_PATH
OUTPUT_PATH = --output argument or ./build-timeline.html
SINCE = --since argument or empty (all time)
UNTIL = --until argument or empty (now)
DETAILED = --detailed flag present
THEME = --theme argument or "default"
```

Verify the repo exists and is a git repository:
```bash
git -C "$REPO_PATH" rev-parse --git-dir
```

### Step 2: Locate Conversation Logs

Claude Code stores conversation logs in `~/.claude/projects/`. The directory name is the repo path with `/` replaced by `-` and leading `-` stripped:

```bash
# Convert repo path to Claude's encoded format
# /Users/lgonzales/Projects/foo → -Users-lgonzales-Projects-foo
ENCODED_PATH=$(echo "$REPO_PATH" | tr '/' '-')
LOG_DIR="$HOME/.claude/projects/$ENCODED_PATH"
```

Find all `.jsonl` conversation log files:
```bash
ls -lt "$LOG_DIR"/*.jsonl 2>/dev/null
```

If `--since` or `--until` are specified, filter files by modification time. Each `.jsonl` file represents one conversation session.

### Step 3: Parse Conversation Logs

Each line in a `.jsonl` file is a JSON object. Parse these event types:

#### Message Structure
```json
{
  "type": "human" | "assistant",
  "message": {
    "role": "human" | "assistant",
    "content": [...],  // array of content blocks
    "model": "...",
  },
  "timestamp": "2026-03-13T10:00:00.000Z",
  "sessionId": "...",
  "parentMessageId": "..."
}
```

#### Content Block Types

Content blocks in the `content` array have a `type` field:

**Tool Use blocks** (`type: "tool_use"`):
```json
{
  "type": "tool_use",
  "id": "toolu_...",
  "name": "Bash" | "Read" | "Write" | "Edit" | "Glob" | "Grep" | "Agent" | "TaskCreate" | "TaskUpdate" | "TaskList" | "SendMessage" | etc.,
  "input": { ... }  // tool-specific parameters
}
```

**Tool Result blocks** (`type: "tool_result"`):
```json
{
  "type": "tool_result",
  "tool_use_id": "toolu_...",
  "content": "..." | [{"type": "text", "text": "..."}],
  "is_error": false
}
```

**Text blocks** (`type: "text"`):
```json
{
  "type": "text",
  "text": "..."
}
```

#### Event Extraction Rules

For each tool_use content block, extract based on the `name` field:

| Tool Name | What to Extract | Key Input Fields |
|-----------|----------------|-----------------|
| `Agent` | Agent spawn — name, prompt, background flag | `name`, `prompt`, `run_in_background` |
| `Bash` | Shell command execution | `command`, `description` |
| `Read` | File read | `file_path` |
| `Write` | File create/overwrite | `file_path` |
| `Edit` | File edit | `file_path`, `old_string`, `new_string` |
| `Glob` | File search | `pattern` |
| `Grep` | Content search | `pattern`, `path` |
| `TaskCreate` | Task created | `description` |
| `TaskUpdate` | Task status change | `task_id`, `status` |
| `TaskList` | Task listing | — |
| `SendMessage` | Team communication | `teammate_id`, `type` |

For tool_result blocks, match by `tool_use_id` to correlate results with calls. Check `is_error` for failures.

#### Parsing Strategy

Use `jq` or Python to parse. Recommended approach with `jq`:

```bash
# Extract all tool_use events with timestamps from a .jsonl file
cat "$LOG_FILE" | jq -c '
  select(.type == "assistant") |
  .timestamp as $ts |
  .message.content[]? |
  select(.type == "tool_use") |
  {timestamp: $ts, tool: .name, id: .id, input: .input}
'
```

```bash
# Extract tool results (errors)
cat "$LOG_FILE" | jq -c '
  select(.type == "human") |
  .timestamp as $ts |
  .message.content[]? |
  select(.type == "tool_result") |
  select(.is_error == true) |
  {timestamp: $ts, tool_use_id: .tool_use_id, error: true, content: (.content | if type == "array" then .[0].text? else . end)}
'
```

```bash
# Extract user messages
cat "$LOG_FILE" | jq -c '
  select(.type == "human") |
  .timestamp as $ts |
  .message.content[]? |
  select(.type == "text") |
  {timestamp: $ts, type: "user_message", text: .text}
'
```

For large files, use streaming/line-by-line processing to avoid memory issues.

### Step 4: Parse Git History

Extract git log with file changes:

```bash
git -C "$REPO_PATH" log \
  --format='{"hash":"%h","full_hash":"%H","author":"%an","date":"%aI","message":"%s"}' \
  --name-status \
  ${SINCE:+--since="$SINCE"} \
  ${UNTIL:+--until="$UNTIL"}
```

Parse the output to get commits with their changed files. Each commit produces:
- Hash, author, date, message
- List of changed files with status (A=added, M=modified, D=deleted)

Also get overall stats:
```bash
git -C "$REPO_PATH" log --shortstat ${SINCE:+--since="$SINCE"} ${UNTIL:+--until="$UNTIL"}
```

### Step 5: Correlate Events

Match conversation events to git commits by timestamp proximity (within 5 minutes). This connects "what Claude was doing" to "what was committed."

Build a unified timeline by merging:
1. Conversation events (tool calls, agent spawns, messages)
2. Git commits
3. Errors and retries

Sort all events chronologically.

### Step 6: Detect Phases

If `--phases` flag is set, auto-detect phases by:

1. **Git commit prefixes**: Group by conventional commit prefixes (`feat:`, `fix:`, `chore:`, `docs:`, etc.)
2. **Agent names**: Group by agent `name` field from Agent tool calls
3. **Time gaps**: Split phases at gaps > 30 minutes
4. **User messages**: Use user prompts as phase boundaries

Assign each phase a color from the palette:
```
Phase colors: #4299E1 (blue), #48BB78 (green), #ED8936 (orange), #9F7AEA (purple), #F56565 (red), #38B2AC (teal)
```

If `--phases` is not set, group events into a single "Development" phase.

### Step 7: Build Timeline Data

Structure the parsed data for HTML generation. Create a JSON data structure:

```json
{
  "repoName": "my-project",
  "generatedAt": "2026-03-13T12:00:00Z",
  "timespan": "2h 34m",
  "stats": {
    "totalPhases": 4,
    "totalAgents": 12,
    "totalCommands": 87,
    "totalFiles": 34,
    "totalCommits": 8
  },
  "phases": [
    {
      "name": "Phase Name",
      "color": "#4299E1",
      "startTime": "...",
      "endTime": "...",
      "events": [...]
    }
  ]
}
```

Each event in the events array:
```json
{
  "type": "agent_spawn" | "command" | "file_op" | "commit" | "error" | "user_message" | "task" | "team_message",
  "timestamp": "...",
  "data": { ... }
}
```

### Step 8: Generate HTML

Read the HTML template from:
```
/Users/lgonzales/Projects/leegonzales/AISkills/BuildTimeline/build-timeline/references/html-template.html
```

Replace these placeholders in the template with generated content:

| Placeholder | Content |
|-------------|---------|
| `{{REPO_NAME}}` | Repository name |
| `{{GENERATED_AT}}` | Generation timestamp (human-readable) |
| `{{STATS_BAR}}` | HTML for the stats bar |
| `{{TIMELINE_EVENTS}}` | All timeline event cards as HTML |
| `{{PHASE_FILTERS}}` | Phase filter toggle buttons |
| `{{TOTAL_PHASES}}` | Number of phases |
| `{{TOTAL_AGENTS}}` | Number of agent spawns |
| `{{TOTAL_COMMANDS}}` | Number of shell commands |
| `{{TOTAL_FILES}}` | Number of files changed |
| `{{TOTAL_COMMITS}}` | Number of git commits |
| `{{TIMESPAN}}` | Human-readable duration |
| `{{THEME_VARS}}` | CSS custom properties for the selected theme |

#### Generating Event Cards HTML

For each event, generate an HTML card. Here are the card templates:

**Agent Spawn Card:**
```html
<div class="timeline-event event-left phase-{phaseIndex}" data-phase="{phaseName}">
  <div class="event-dot" style="background: {phaseColor}"></div>
  <div class="event-card agent-card" style="border-left-color: {phaseColor}">
    <div class="event-time">{timestamp}</div>
    <div class="event-type"><span class="badge badge-agent">Agent</span></div>
    <h3>{agentName}</h3>
    <p class="event-summary">{promptExcerpt}</p>
    <div class="event-detail expandable">
      <button class="expand-btn">Show full prompt</button>
      <div class="expand-content">{fullPrompt}</div>
    </div>
    {backgroundBadge}
    {childAgentsList}
  </div>
</div>
```

**Command Card:**
```html
<div class="timeline-event event-right phase-{phaseIndex}" data-phase="{phaseName}">
  <div class="event-dot" style="background: {phaseColor}"></div>
  <div class="event-card command-card">
    <div class="event-time">{timestamp}</div>
    <div class="event-type"><span class="badge badge-command">Command</span></div>
    <code class="command-text">{command}</code>
    <div class="event-detail expandable">
      <button class="expand-btn">Show output</button>
      <div class="expand-content"><pre>{output}</pre></div>
    </div>
    {exitCodeBadge}
  </div>
</div>
```

**File Change Card:**
```html
<div class="timeline-event event-left phase-{phaseIndex}" data-phase="{phaseName}">
  <div class="event-dot" style="background: {phaseColor}"></div>
  <div class="event-card file-card">
    <div class="event-time">{timestamp}</div>
    <div class="event-type"><span class="badge badge-file">{Write|Edit|Read}</span></div>
    <code class="file-path">{filePath}</code>
  </div>
</div>
```

**Git Commit Card:**
```html
<div class="timeline-event event-right phase-{phaseIndex}" data-phase="{phaseName}">
  <div class="event-dot dot-commit" style="background: {phaseColor}"></div>
  <div class="event-card commit-card">
    <div class="event-time">{timestamp}</div>
    <div class="event-type"><span class="badge badge-commit">Commit</span></div>
    <code class="commit-hash">{hash}</code>
    <h3>{commitMessage}</h3>
    <div class="files-changed">{fileCount} files changed</div>
    <div class="event-detail expandable">
      <button class="expand-btn">Show files</button>
      <div class="expand-content">{fileList}</div>
    </div>
  </div>
</div>
```

**Error Card:**
```html
<div class="timeline-event event-left phase-{phaseIndex}" data-phase="{phaseName}">
  <div class="event-dot dot-error"></div>
  <div class="event-card error-card">
    <div class="event-time">{timestamp}</div>
    <div class="event-type"><span class="badge badge-error">Error</span></div>
    <p>{errorSummary}</p>
    <div class="event-detail expandable">
      <button class="expand-btn">Show details</button>
      <div class="expand-content"><pre>{errorDetail}</pre></div>
    </div>
  </div>
</div>
```

**Phase Header:**
```html
<div class="phase-header" style="border-color: {phaseColor}">
  <h2><span class="phase-dot" style="background: {phaseColor}"></span>{phaseName}</h2>
  <span class="phase-time">{startTime} — {endTime}</span>
  <span class="phase-stats">{eventCount} events</span>
</div>
```

Alternate `event-left` and `event-right` classes for the zigzag layout.

When `--detailed` is NOT set, filter to only major events:
- Agent spawns
- Git commits
- Write/Edit operations (skip Read/Glob/Grep)
- Errors
- User messages
- Commands that modify state (skip read-only commands like `ls`, `cat`, `git status`, `git log`)

#### Theme CSS Variables

**Default theme:**
```css
:root {
  --bg-primary: #F8F7F4;
  --bg-card: #FFFFFF;
  --text-primary: #2D3748;
  --text-secondary: #718096;
  --border-color: #E2E8F0;
  --timeline-line: #CBD5E0;
  --shadow: 0 1px 3px rgba(0,0,0,0.1);
}
```

**Dark theme:**
```css
:root {
  --bg-primary: #1A202C;
  --bg-card: #2D3748;
  --text-primary: #E2E8F0;
  --text-secondary: #A0AEC0;
  --border-color: #4A5568;
  --timeline-line: #4A5568;
  --shadow: 0 1px 3px rgba(0,0,0,0.3);
}
```

**AFS theme:**
```css
:root {
  --bg-primary: #F8F7F4;
  --bg-card: #FFFFFF;
  --text-primary: #1B2A4A;
  --text-secondary: #5A6B8A;
  --border-color: #D4DAE6;
  --timeline-line: #1B2A4A;
  --shadow: 0 2px 8px rgba(27,42,74,0.08);
}
```

### Step 9: Write Output

Write the final HTML to the output path. Report summary stats to the user:

```
Build Timeline generated:
- Output: {outputPath}
- Repo: {repoName}
- Timespan: {timespan}
- {totalPhases} phases, {totalAgents} agents, {totalCommands} commands
- {totalFiles} files changed across {totalCommits} commits
```

## Tips for Best Results

1. **Large repos**: Use `--since` to scope to a recent time window. Parsing all history for a large project can be slow.
2. **Phase detection**: The `--phases` flag works best when the build used conventional commit prefixes or named agents.
3. **Detailed mode**: Use `--detailed` for debugging or comprehensive documentation. Default mode focuses on milestone events.
4. **Multiple sessions**: If the project spans multiple conversation sessions, all `.jsonl` files are parsed and merged chronologically.
5. **Missing logs**: If conversation logs aren't found (e.g., different machine), the timeline falls back to git-only mode.

## Example Usage

```
# Timeline of current repo, all history
/build-timeline

# Last 24 hours, detailed
/build-timeline --since "1 day ago" --detailed

# Specific repo with dark theme
/build-timeline /Users/lgonzales/Projects/my-app --theme dark

# Scoped time range with custom output
/build-timeline --since "2026-03-12" --until "2026-03-13" --output build-report.html

# With phase detection
/build-timeline --phases --output phased-timeline.html
```
