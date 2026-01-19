# HTML Presentation Engine Reference

Complete technical reference for the self-contained HTML presentation format generated from talk tracks.

## Overview

The HTML presentation engine produces a **single, self-contained HTML file** that runs entirely in the browser with no external dependencies. It provides:

- Full-screen slide display
- Timer with warning/overtime states
- Per-slide audio playback
- Auto-advance mode (advances after audio ends)
- Speaker notes overlay
- Keyboard navigation
- Progress tracking by section

## Generation Pipeline

```
talk-track.md (v5 format)
        ↓
  generate-presentation.py
        ↓
  presentation.html
```

### Input: Talk Track v5 Format

The generator parses a talk track markdown file with:

1. **YAML Frontmatter** - Metadata including title and target duration
2. **Slides Table** - Structured slide definitions

```markdown
---
title: "Presentation Title"
target_minutes: 45
sections:
  opening: "#4a90d9"
  main: "#557373"
  closing: "#8b4513"
---

## Slides

| # | Slug | Title | Image | Section |
|---|------|-------|-------|---------|
| 1 | title | Opening Title | slide-title.png | opening |
| 2 | problem | The Problem | slide-problem.png | opening |
```

### Output: Single HTML File

The generator produces `presentation.html` containing:
- Embedded CSS styles
- JavaScript slides data array
- All presentation logic
- No external dependencies

## HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>/* Embedded styles */</style>
</head>
<body>
    <div class="presentation">
        <!-- Main slide display -->
        <div class="slide-container">
            <img class="slide" id="currentSlide" src="" alt="Slide">
        </div>

        <!-- Speaker notes overlay (hidden by default) -->
        <div class="speaker-notes" id="speakerNotes">
            <p id="notesText"></p>
        </div>

        <!-- Control bar -->
        <div class="control-bar">
            <!-- Timer group -->
            <div class="control-group">
                <div class="timer" id="timer">00:00</div>
                <span class="target-time">/ 45:00</span>
            </div>

            <!-- Playback controls -->
            <div class="control-group">
                <button class="btn btn-start" id="startBtn">Start</button>
                <button class="btn btn-reset" id="resetBtn">Reset</button>
            </div>

            <!-- Navigation -->
            <div class="control-group">
                <button class="btn btn-nav" id="prevBtn">&larr;</button>
                <button class="btn btn-play" id="playBtn">Play</button>
                <button class="btn btn-nav" id="nextBtn">&rarr;</button>
            </div>

            <!-- Progress display -->
            <div class="progress">
                <span class="section-label" id="sectionLabel">Opening</span>
                <div class="progress-bar">
                    <div class="progress-fill" id="progressFill"></div>
                </div>
                <span id="slideCounter">1/30</span>
            </div>

            <!-- Audio indicator (animated waveform) -->
            <div class="audio-indicator" id="audioIndicator">
                <div class="audio-wave">
                    <span></span><span></span><span></span><span></span><span></span>
                </div>
            </div>

            <!-- Mode toggle -->
            <div class="control-group">
                <button class="mode-btn active" id="modeAuto">Auto</button>
                <button class="mode-btn" id="modeManual">Manual</button>
            </div>
        </div>
    </div>

    <audio id="audioPlayer"></audio>
    <script>/* Embedded JavaScript */</script>
</body>
</html>
```

## JavaScript Slides Array

The generator creates a slides array from the talk track table:

```javascript
const slides = [
    // OPENING
    { src: 'images/slide-title.png',
      section: 'opening',
      audio: 'audio/title.wav',
      slug: 'title' },
    { src: 'images/slide-problem.png',
      section: 'opening',
      audio: 'audio/problem.wav',
      slug: 'problem' },

    // MAIN
    { src: 'images/slide-solution.png',
      section: 'main',
      audio: 'audio/solution.wav',
      slug: 'solution' },
    // ...
];
```

### Slide Object Properties

| Property | Description | Example |
|----------|-------------|---------|
| `src` | Path to slide image | `'images/slide-title.png'` |
| `section` | Section name for grouping | `'opening'` |
| `audio` | Path to audio file | `'audio/title.wav'` |
| `slug` | Unique identifier | `'title'` |

### File Path Conventions

```
presentation/
├── presentation.html
├── talk-track.md
├── images/
│   ├── slide-title.png
│   ├── slide-problem.png
│   └── ...
└── audio/
    ├── title.wav
    ├── problem.wav
    └── ...
```

- **Images**: `images/{image-filename}` (from Slides table column 4)
- **Audio**: `audio/{slug}.wav` (from Slides table column 2)

## Control Bar Features

### Timer

| State | Condition | Color | CSS Class |
|-------|-----------|-------|-----------|
| Idle | Not running | Teal (#557373) | (none) |
| Running | < 90% of target | Green (#4CAF50) | `.running` |
| Warning | 90-100% of target | Yellow (#FFC107) | `.warning` |
| Overtime | > 100% of target | Red (#f44336) | `.overtime` |

Timer behavior:
- Counts up from 00:00
- Shows target time: `/ 45:00`
- Updates every second when presentation is running
- Color transitions happen automatically

### Start/Stop Button

| State | Button Text | Action |
|-------|-------------|--------|
| Stopped | "Start" | Starts timer, plays current slide audio |
| Running | "Stop Presentation" | Stops timer, pauses audio |

### Navigation Buttons

- **Previous (←)**: Move to previous slide, pause audio
- **Play**: Toggle audio playback for current slide
- **Next (→)**: Move to next slide, optionally auto-play audio

Button states:
- Previous disabled on first slide
- Next disabled on last slide
- Play button shows "Pause" while audio playing

### Progress Display

```
[Section Label] [Progress Bar] [Slide Counter]
    OPENING     [████████░░░░░]    5 / 30
```

- **Section label**: Current section name (uppercase)
- **Progress bar**: Visual fill based on slide position
- **Slide counter**: Current / Total

### Audio Indicator

Animated waveform (5 bars) appears when audio is playing:
- Green color (#4CAF50)
- Bars animate at staggered intervals
- Hidden when audio not playing

### Mode Toggle

| Mode | Behavior | Use Case |
|------|----------|----------|
| **Auto** (default) | Advances to next slide 500ms after audio ends | Full presentation flow |
| **Manual** | Stays on current slide after audio | Practice, reviewing |

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `→` or `PageDown` | Next slide |
| `←` or `PageUp` | Previous slide |
| `Space` | Play/pause audio |
| `N` | Toggle speaker notes |
| `Enter` | Start/stop presentation |
| `Home` | Go to first slide |
| `End` | Go to last slide |
| `R` | Reset timer (without stopping) |

## Styling Reference

### Color Palette

```css
:root {
    --teal: #557373;    /* Primary accent, section labels */
    --green: #2d5a2d;   /* Start button, play button */
    --red: #6b4c4c;     /* Reset button */
}

body {
    background: #0d0d0d;  /* Dark background */
    color: white;
}

.control-bar {
    background: rgba(30,30,30,0.95);
}
```

### Typography

- **Timer**: SF Mono, Menlo, monospace (24px)
- **Body**: System font stack (-apple-system, BlinkMacSystemFont, etc.)
- **Section labels**: Uppercase, letter-spacing 0.5px

### Slide Display

```css
.slide {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    border-radius: 6px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.5);
}
```

### Speaker Notes Overlay

```css
.speaker-notes {
    position: fixed;
    bottom: 60px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(0,0,0,0.95);
    max-width: 700px;
    max-height: 180px;
    border: 1px solid rgba(255,255,255,0.15);
}
```

## Audio Integration

### Audio File Requirements

- **Format**: WAV (recommended), MP3, or other browser-supported format
- **Naming**: `audio/{slug}.wav` - must match slide slug exactly
- **Location**: `audio/` directory relative to HTML file

### Playback Behavior

1. **Manual play**: Click Play button or press Space
2. **Auto play on start**: Plays current slide when presentation starts
3. **Auto advance**: In Auto mode, waits 500ms after audio ends, then advances

### Error Handling

Audio playback failures are logged to console but don't block navigation:
```javascript
audioPlayer.play().catch(e => console.log('Audio play failed:', e));
```

## State Management

### Global State Variables

```javascript
let currentIndex = 0;           // Current slide position
let showNotes = false;          // Speaker notes visibility
let presentationRunning = false; // Timer/presentation active
let autoAdvance = true;         // Auto mode enabled
let timerInterval = null;       // Timer interval reference
let elapsedSeconds = 0;         // Elapsed time in seconds
const targetSeconds = 45 * 60;  // Target duration (from frontmatter)
```

### Key Functions

| Function | Description |
|----------|-------------|
| `updateSlide()` | Updates image, section label, counter, progress bar |
| `nextSlide()` | Advances slide, optionally triggers audio |
| `prevSlide()` | Goes back, pauses audio |
| `playCurrentAudio()` | Loads and plays current slide's audio |
| `togglePresentation()` | Starts or stops presentation mode |
| `updateTimer()` | Updates timer display and state classes |
| `setMode(mode)` | Switches between 'auto' and 'manual' modes |
| `toggleNotes()` | Shows/hides speaker notes overlay |

## Customization Points

### Modifying Target Duration

In the frontmatter:
```yaml
target_minutes: 60  # Change to your target
```

### Adjusting Timer Thresholds

Default: Warning at 90%, Overtime at 100%

```javascript
// In updateTimer()
if (elapsedSeconds > targetSeconds) {
    timerEl.classList.add('overtime');
} else if (elapsedSeconds > targetSeconds * 0.9) {  // Adjust 0.9
    timerEl.classList.add('warning');
}
```

### Changing Auto-Advance Delay

Default: 500ms delay after audio ends

```javascript
// In audioPlayer 'ended' event
setTimeout(() => {
    nextSlide();
}, 500);  // Adjust delay in milliseconds
```

### Section Colors

Define in frontmatter (if supported by generator version):
```yaml
sections:
  opening: "#4a90d9"
  main: "#557373"
  closing: "#8b4513"
```

## Browser Compatibility

Tested and working in:
- Chrome/Edge (Chromium)
- Firefox
- Safari

Requirements:
- Modern JavaScript (ES6+)
- HTML5 Audio API
- CSS Flexbox
- CSS Custom Properties

## Troubleshooting

### Audio Not Playing

1. Check file exists: `audio/{slug}.wav`
2. Check browser console for errors
3. Ensure file format is browser-supported
4. On first interaction, some browsers require user gesture to play audio

### Slides Not Loading

1. Verify `images/` directory structure
2. Check image filenames match Slides table exactly
3. Open browser console for 404 errors

### Timer Not Starting

1. Click "Start" button or press Enter
2. Check that `presentationRunning` state is being set
3. Verify no JavaScript errors in console

## Example Generator Invocation

```bash
# Generate for specific presentation
./generate-presentation.py presentations/my-talk/

# Dry run to see what would be generated
./generate-presentation.py presentations/my-talk/ --dry-run

# Use default presentation
./generate-presentation.py
```

Output:
```
Presentation: my-talk
Parsing presentations/my-talk/talk-track.md...
Title: My Amazing Talk
Target time: 45 minutes
Found 30 slides:

  [OPENING]
       1 | [title] Opening Title
       2 | [problem] The Problem

  [MAIN]
       3 | [solution] The Solution
       ...

Generating HTML...
Saved: presentations/my-talk/presentation.html

To view: open presentations/my-talk/presentation.html
```
