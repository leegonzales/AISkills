# HTML Rendering Reference

Detailed rendering material for Step 8 (Generate HTML) of the build-timeline workflow:
placeholder map, event-card HTML templates, and theme CSS variable blocks.

The HTML template file is at `references/html-template.html`. Replace its `{{...}}`
placeholders with generated content.

## Template Placeholders

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

## Event Card HTML Templates

Alternate `event-left` and `event-right` classes for the zigzag layout.

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

## Default-Mode Event Filtering

When `--detailed` is NOT set, filter to only major events:
- Agent spawns
- Git commits
- Write/Edit operations (skip Read/Glob/Grep)
- Errors
- User messages
- Commands that modify state (skip read-only commands like `ls`, `cat`, `git status`, `git log`)

## Theme CSS Variables

Emit the matching block as `{{THEME_VARS}}` based on the `--theme` argument.

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
