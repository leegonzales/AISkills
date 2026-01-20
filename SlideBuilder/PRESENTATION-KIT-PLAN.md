# PresentationKit: Unified Presentation Infrastructure

## Vision

A single, composable infrastructure for transforming content into multi-format presentations (HTML, Video, PDF) with a clean separation between content transformation (Claude Skills) and rendering (TypeScript/Python generators).

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         INPUT: Talk Track v5                            │
│                    (From slide-builder or manual)                       │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      PRESENTATIONKIT CORE                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐                │
│  │   PARSERS    │   │  GENERATORS  │   │  RENDERERS   │                │
│  ├──────────────┤   ├──────────────┤   ├──────────────┤                │
│  │ talk-track   │   │ audio        │   │ html         │                │
│  │ timeline     │   │ images       │   │ remotion     │                │
│  │ manifest     │   │ captions     │   │ notes        │                │
│  └──────────────┘   └──────────────┘   └──────────────┘                │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                         ORCHESTRATOR                              │  │
│  │  • State machine with persistence                                 │  │
│  │  • Cost tracking                                                  │  │
│  │  • Progress callbacks                                             │  │
│  │  • Resumable workflows                                            │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                            CLI                                    │  │
│  │  pk build talk-track.md --output html,video,notes                 │  │
│  │  pk audio talk-track.md --voice af_heart                          │  │
│  │  pk video talk-track.md --quality 1080p                           │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                            OUTPUTS                                      │
├────────────────────┬────────────────────┬───────────────────────────────┤
│   presentation.html│   presentation.mp4 │   speaker-notes.html          │
│   (Interactive)    │   (YouTube-ready)  │   (Printable PDF)             │
└────────────────────┴────────────────────┴───────────────────────────────┘
```

## Project Structure

```
~/Projects/leegonzales/PresentationKit/
├── package.json                 # Node.js project (TypeScript + Remotion)
├── tsconfig.json
├── CLAUDE.md                    # Project instructions
├── README.md
│
├── src/
│   ├── cli/
│   │   ├── index.ts             # Main CLI entry (Commander.js)
│   │   ├── commands/
│   │   │   ├── build.ts         # Full pipeline command
│   │   │   ├── audio.ts         # Audio-only command
│   │   │   ├── video.ts         # Video-only command
│   │   │   ├── html.ts          # HTML-only command
│   │   │   └── notes.ts         # Speaker notes command
│   │   └── progress.ts          # Progress display helpers
│   │
│   ├── parsers/
│   │   ├── talk-track.ts        # Parse Talk Track v5 format
│   │   ├── types.ts             # Shared type definitions
│   │   └── validators.ts        # Input validation
│   │
│   ├── generators/
│   │   ├── audio/
│   │   │   ├── index.ts         # Audio generation orchestrator
│   │   │   ├── kokoro.ts        # Kokoro TTS adapter
│   │   │   ├── elevenlabs.ts    # ElevenLabs adapter
│   │   │   └── types.ts
│   │   ├── images/
│   │   │   ├── index.ts         # Image generation orchestrator
│   │   │   ├── nano-banana.ts   # Gemini image generation
│   │   │   └── types.ts
│   │   └── timeline/
│   │       ├── index.ts         # Timeline builder
│   │       ├── caption-sync.ts  # Caption alignment
│   │       └── types.ts
│   │
│   ├── renderers/
│   │   ├── html/
│   │   │   ├── index.ts         # HTML generator
│   │   │   └── template.ts      # HTML template
│   │   ├── remotion/
│   │   │   ├── Root.tsx         # Remotion composition registry
│   │   │   ├── Presentation.tsx # Main composition
│   │   │   ├── components/
│   │   │   │   ├── Slide.tsx
│   │   │   │   ├── CaptionOverlay.tsx
│   │   │   │   ├── Transition.tsx
│   │   │   │   └── Waveform.tsx
│   │   │   ├── renderer.ts      # Remotion render wrapper
│   │   │   └── types.ts
│   │   └── notes/
│   │       ├── index.ts         # Speaker notes generator
│   │       └── template.ts      # HTML template
│   │
│   ├── orchestrator/
│   │   ├── index.ts             # Main orchestrator
│   │   ├── state-machine.ts     # State management
│   │   ├── cost-tracker.ts      # Cost tracking
│   │   └── types.ts
│   │
│   └── utils/
│       ├── config.ts            # Configuration management
│       ├── retry.ts             # Retry logic
│       ├── file-utils.ts        # File operations
│       └── logger.ts            # Logging
│
├── templates/
│   ├── html-presentation.html   # HTML viewer template
│   └── speaker-notes.html       # Speaker notes template
│
├── public/                      # Remotion static assets (runtime)
│   ├── audio/
│   └── images/
│
└── tests/
    ├── fixtures/
    │   └── sample-talk-track.md
    └── integration/
```

## Core Data Types

### Talk Track v5 (Input)

```typescript
interface TalkTrackV5 {
  // Frontmatter
  version: 5;
  title: string;
  subtitle?: string;
  author: string;
  event?: string;
  date?: string;
  targetMinutes: number;
  audioVoice: string;
  branding?: string;
  sections: Section[];

  // Slides table
  slides: SlideDefinition[];

  // Slide content
  slideContent: Map<string, SlideContent>;
}

interface Section {
  id: string;
  name: string;
  color: string;
}

interface SlideDefinition {
  position: string;      // "1", "2", "A1", "A2"
  slug: string;
  title: string;
  image: string;
  section: string;
}

interface SlideContent {
  slug: string;
  title: string;
  imagePath: string;
  audioText: string;     // Content between <!-- AUDIO --> tags
  speakerNotes?: string;
  semanticTags: SemanticTag[];
}

interface SemanticTag {
  type: 'HOOK' | 'KEY_POINT' | 'EVIDENCE' | 'STORY' | 'TRANSITION' | 'CALLBACK' | 'LANDING' | 'CTA' | 'PAUSE';
  content?: string;
  duration?: number;     // For PAUSE tags
}
```

### Timeline (Internal)

```typescript
interface Timeline {
  fps: number;
  width: number;
  height: number;
  totalDuration: number;

  slides: TimelineSlide[];

  // Computed sequences
  sequences: {
    openingDuration?: number;
    closingDuration?: number;
    creditsDuration?: number;
  };
}

interface TimelineSlide {
  slug: string;
  title: string;
  section: string;
  sectionColor: string;

  // Timing
  startTime: number;
  endTime: number;
  duration: number;

  // Assets
  imagePath: string;
  audioPath: string;

  // Captions (from TTS timestamps)
  captions: Caption[];
}

interface Caption {
  text: string;
  startTime: number;
  endTime: number;
  // Word-level for karaoke effect
  words?: WordTiming[];
}

interface WordTiming {
  word: string;
  start: number;
  end: number;
}
```

### Build Manifest (Output)

```typescript
interface BuildManifest {
  id: string;
  createdAt: string;
  completedAt?: string;

  source: {
    talkTrack: string;
    hash: string;
  };

  outputs: {
    html?: string;
    video?: string;
    notes?: string;
    timeline?: string;
  };

  assets: {
    audio: AudioAsset[];
    images: ImageAsset[];
  };

  costs: CostEntry[];

  state: BuildState;
  error?: string;
}
```

## Code Reuse Map

| Component | Source Project | Files to Adapt |
|-----------|---------------|----------------|
| **Talk Track Parser** | AIEnablementTraining | `generate-presentation.py` lines 25-67 |
| **HTML Template** | AIEnablementTraining | `generate-presentation.py` lines 94-606 |
| **Audio Generation (Kokoro)** | AIEnablementTraining | `generate-audio.py` full file |
| **Audio Generation (ElevenLabs)** | AIPresentationMaker | `src/audio/elevenlabs-service.ts` |
| **Remotion Root** | AITalkShowCli | `src/video/remotion/Root.tsx` |
| **Caption Overlay** | AITalkShowCli | `src/video/remotion/UnifiedCaptionOverlay.tsx` |
| **Layout Mode Hook** | AITalkShowCli | `src/video/remotion/useLayoutMode.ts` |
| **Full-Screen Image** | AITalkShowCli | `src/video/remotion/FullScreenImageOverlay.tsx` |
| **Video Renderer** | AITalkShowCli | `src/video/VideoRenderer.ts` |
| **State Machine** | AIPresentationMaker | `src/content/orchestrator.ts` |
| **Cost Tracker** | AIPresentationMaker | `src/storage/costs.ts` |
| **Retry Logic** | AIPresentationMaker | `src/utils/retry.ts` |
| **Speaker Notes** | AIEnablementTraining | `generate-speaker-notes.py` |

## Implementation Phases

### Phase 1: Foundation (Days 1-2)
- Project setup (package.json, tsconfig, directory structure)
- Talk Track v5 parser
- Type definitions
- Configuration management

### Phase 2: Generators (Days 3-4)
- Audio generator (Kokoro adapter)
- Audio generator (ElevenLabs adapter)
- Timeline builder
- Caption sync logic

### Phase 3: Renderers (Days 5-7)
- HTML renderer (port from AIEnablementTraining)
- Remotion composition (adapt from AITalkShowCli)
- Video renderer
- Speaker notes renderer

### Phase 4: Orchestrator (Day 8)
- State machine
- Cost tracking
- Progress callbacks

### Phase 5: CLI (Day 9)
- Commander.js setup
- Build command
- Individual commands (audio, video, html, notes)

### Phase 6: Testing & Polish (Day 10)
- Integration tests
- Documentation
- Example workflow

## CLI Commands

```bash
# Full build (all outputs)
pk build presentations/my-talk/talk-track.md --output html,video,notes

# Audio only
pk audio presentations/my-talk/talk-track.md --voice af_heart --provider kokoro
pk audio presentations/my-talk/talk-track.md --voice rachel --provider elevenlabs

# Video only (requires audio to exist)
pk video presentations/my-talk/talk-track.md --quality 1080p --fps 30

# HTML only
pk html presentations/my-talk/talk-track.md

# Speaker notes only
pk notes presentations/my-talk/talk-track.md

# Resume failed build
pk resume presentations/my-talk/

# Check status
pk status presentations/my-talk/

# Cost report
pk costs presentations/my-talk/
```

## Configuration

```yaml
# pk.config.yaml (project-level)
defaults:
  voice: af_heart
  provider: kokoro
  fps: 30
  resolution: 1080p

providers:
  kokoro:
    command: ~/Projects/claude-speak/.venv/bin/claude-speak-client
  elevenlabs:
    apiKey: ${ELEVENLABS_API_KEY}
    model: eleven_v3

video:
  codec: h264
  crf: 18
  transitions:
    type: fade
    duration: 0.3

costs:
  track: true
  warn_threshold: 5.00
```

## Deprecation Strategy (Post-Build)

After PresentationKit is complete, these projects can be simplified:

### AIEnablementTraining
**Before:** Full generator pipeline (audio, html, notes)
**After:** Thin wrapper that calls `pk build`
```python
# generate-all.py (new)
import subprocess
subprocess.run(['pk', 'build', 'talk-track.md', '--output', 'html,notes'])
```
**Deprecate:** `generate-presentation.py`, `generate-audio.py`, `generate-speaker-notes.py`
**Keep:** Talk track content, images, presentation-specific customizations

### AITalkShowCli
**Before:** Full Remotion video pipeline for talk shows
**After:** Uses PresentationKit's Remotion renderer as library
```typescript
import { renderVideo } from '@leegonzales/presentation-kit';
// Talk show specific logic...
const timeline = buildTalkShowTimeline(conversation);
await renderVideo(timeline, options);
```
**Deprecate:** Duplicated Remotion components, timeline builder
**Keep:** Talk show business logic, conversation-to-timeline transformation

### AIPresentationMaker
**Before:** Full pipeline with state machine, cost tracking
**After:** Uses PresentationKit for rendering, keeps orchestration for its specific workflow
```typescript
import { generateAudio, renderVideo } from '@leegonzales/presentation-kit';
// Monologue-specific script generation...
// Uses PK for rendering
```
**Deprecate:** Duplicate audio/video code
**Keep:** Script generation, graphic cue parsing, monologue-specific logic

## Success Criteria

1. **Single command** builds complete presentation from Talk Track v5
2. **Video output** matches quality of AITalkShowCli
3. **HTML output** matches quality of AIEnablementTraining
4. **Cost tracking** works for all providers
5. **Resumable builds** work correctly
6. **All three legacy projects** can use PresentationKit as a library
