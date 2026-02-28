# AIPresentationMaker Pipeline Reference

Codebase location: `~/Projects/leegonzales/AIPresentationMaker`

This reference documents the real entry points for each render stage. The skill calls these TypeScript modules either programmatically (via the producer) or as individual stages.

---

## Full Pipeline Orchestrator

**File:** `src/pipeline/producer.ts`

```typescript
runProduction(options: ProductionOptions): Promise<ProductionResult>
```

Runs all stages end-to-end. Accepts:

```typescript
interface ProductionOptions {
  topic: string;
  context?: string;
  mode?: 'monologue' | 'debate' | 'interview';
  skipResearch?: boolean;
  skipImages?: boolean;
  skipWritersRoom?: boolean;
  researchData?: string;
  targetDurationSecs?: number;
  videoType?: VideoType;       // kids_5_10 | kids_10_15 | corporate | documentary | entertainment | technical
  qualityTier?: QualityTier;   // draft | standard | high
}
```

For the `/render-video` skill, we typically call individual stages rather than the full producer, since the script already exists.

---

## Stage 1: Parse Graphic Cues

**File:** `src/content/graphic-cue-parser.ts`

### Key Functions

```typescript
parseGraphicCues(script: string): GraphicCue[]
```

Parses `[GRAPHIC: description | DURATION: Xs]` markers. Returns array of:

```typescript
interface GraphicCue {
  index: number;
  description: string;
  duration: number;          // seconds (default 5)
  type: 'atmospheric' | 'data_graphic' | 'character' | 'custom';
  position: number;          // char position in original script
  cleanPosition: number;     // char position in cleaned script (for audio sync)
  contextText: string;       // surrounding text for timing
  imagePath?: string;        // set after image generation
}
```

Type inference is automatic based on keywords in the description (e.g., "chart" -> data_graphic, "host" -> character).

### Other Utilities

| Function | Purpose |
|----------|---------|
| `removeGraphicCues(script)` | Strip markers for audio synthesis |
| `extractAudioScript(script)` | Clean script for TTS (removes markers + emphasis) |
| `countWords(script)` | Word count excluding markers |
| `estimateDuration(script)` | Estimate seconds at 150 WPM |
| `parseSegments(script, names)` | Parse multi-speaker segments |

---

## Stage 2: Image Generation

**File:** `src/images/generator.ts`

### Single Image

```typescript
generateImage(
  request: ImageGenerationRequest,
  productionId?: string,
  videoType?: VideoType
): Promise<ImageGenerationResult>
```

Request shape:

```typescript
interface ImageGenerationRequest {
  prompt: string;
  type: GraphicCue['type'];    // atmospheric | data_graphic | character | custom
  outputPath: string;           // e.g., images/graphic_001.png
}
```

Result shape:

```typescript
interface ImageGenerationResult {
  imagePath: string;
  prompt: string;
  cached: boolean;
  type: GraphicCue['type'];
  mimeType?: string;           // image/png, image/jpg, image/svg+xml (placeholder)
  qcPassed?: boolean;
  qcAttempts?: number;
}
```

### Batch (All Cues)

```typescript
generateImagesForCues(
  cues: GraphicCue[],
  outputDir: string,
  productionId?: string,
  onProgress?: (completed: number, total: number) => void,
  videoType?: VideoType
): Promise<ImageGenerationResult[]>
```

Includes QC loop: generates image, reviews via Gemini Flash, regenerates if text is garbled (max 2 attempts).

### Special Images

```typescript
generateOpeningImage(topic, outputDir, productionId?, videoType?): Promise<ImageGenerationResult>
generateClosingImage(topic, script, outputDir, productionId?, videoType?): Promise<ImageGenerationResult>
```

Closing infographic only generated for `corporate` and `technical` video types (controlled by `shouldShowClosingInfographic()`).

### Fallback Chain

1. **Gemini 3 Pro Image** (`gemini-3-pro-image-preview`): Primary. Requires `GEMINI_API_KEY`.
2. **SVG placeholder**: Auto-generated when API unavailable or generation fails. Color-coded by type.

### Style Presets

**File:** `src/images/stylePresets.ts`

Each `VideoType` has a `StylePreset` with:
- `styleKeywords`: appended to image prompts
- `colorGuidance`: palette instructions
- `avoidTerms`: negative prompt terms
- `technicalSpecs`: quality/rendering specs

Default (no videoType): uses `entertainment` preset.

---

## Stage 3: Audio Synthesis

**File:** `src/audio/synthesizer.ts`

### Monologue (Single Speaker)

```typescript
synthesizeMonologue(
  text: string,
  voiceId: string,
  outputDir: string,
  productionId?: string,
  filePrefix?: string,
  audioProvider?: IAudioProvider
): Promise<{ audioPath: string; durationSecs: number; wordTimings: WordTiming[] }>
```

### Multi-Speaker

```typescript
synthesizeSegments(
  segments: ContentSegment[],
  voiceMap: Record<string, string>,
  outputDir: string,
  productionId?: string,
  audioProvider?: IAudioProvider
): Promise<SynthesizedAudioResult>
```

### Audio Provider Selection

**File:** `src/audio/audio-provider-factory.ts`

```typescript
AudioProviderFactory.getProvider(config: QualityConfig): IAudioProvider
```

| Quality Tier | Provider | Details |
|-------------|----------|---------|
| `draft` | Kokoro | Local TTS via `claude-speak-daemon`. Socket at `/tmp/claude-speak.sock`. Requires ffmpeg for WAV->MP3. Word timings are estimated (proportional to char length). Free. |
| `standard` | ElevenLabs | Cloud TTS. Requires `ELEVENLABS_API_KEY`. Provides precise word-level timings. ~$0.01/char. |
| `high` | ElevenLabs | Same as standard but uses premium models. |

**Kokoro voice mapping** (`src/audio/kokoro-provider.ts`): ElevenLabs voice IDs are mapped to Kokoro voice names (e.g., `21m00Tcm4TlvDq8ikWAM` -> `bm_george`). Default: `bm_george`.

### WordTiming Format

```typescript
interface WordTiming {
  word: string;
  start: number;  // seconds
  end: number;    // seconds
}
```

---

## Stage 4: Timeline Builder

**File:** `src/video/timeline-builder.ts`

```typescript
buildTimeline(options: TimelineBuildOptions): Promise<VideoTimeline>
```

Options:

```typescript
interface TimelineBuildOptions {
  graphicCues: GraphicCue[];
  audioPath: string;
  audioDuration: number;
  wordTimings?: WordTiming[];
  imagesDir: string;
  title: string;
  topic: string;
  fps?: number;                // default 30
  width?: number;              // default 1920
  height?: number;             // default 1080
  segmentAudios?: SegmentAudio[];
  scriptLength?: number;       // character count for timing accuracy
  introAudioPath?: string;
  introAudioDuration?: number;
  videoType?: VideoType;       // determines closing infographic
}
```

### Timing Synchronization

Two modes:

1. **Word-timing mode** (precise): When `wordTimings` and `scriptLength` are provided, builds a character-to-time interpolation map. Each graphic cue's `cleanPosition` is mapped to a time offset.

2. **Position-ratio mode** (fallback): Without word timings, uses `cleanPosition / totalScriptLength * audioDuration` to estimate start times.

Each graphic segment extends from its start time until the next graphic's start (or end of audio for the last cue).

### Output

```typescript
interface VideoTimeline {
  fps: number;
  durationInFrames: number;
  width: number;
  height: number;
  segments: TimelineSegment[];
  audioPath: string;
  audioDuration: number;
  title: string;
  topic: string;
  captions?: CaptionTrack;
  branding?: BrandingConfig;
  opening?: OpeningConfig;     // if opening_scene image exists
  closing?: ClosingConfig;     // if closing infographic exists (corporate/technical only)
}
```

Serialization: `serializeTimeline()` and `deserializeTimeline()` for JSON I/O.

---

## Stage 5: Video Renderer

**File:** `src/video/renderer.ts`

```typescript
renderVideo(
  timeline: VideoTimeline,
  options: VideoRenderOptions,
  onProgress?: (progress: number) => void
): Promise<VideoRenderResult>
```

Options:

```typescript
interface VideoRenderOptions {
  outputPath: string;
  width?: number;      // default from timeline or 1920
  height?: number;     // default from timeline or 1080
  fps?: number;        // default from timeline or 30
  codec?: 'h264' | 'h265' | 'vp8' | 'vp9';  // default h264
}
```

### What It Does

1. Copies audio to `public/audio/audio.mp3` and images to `public/images/`
2. Updates timeline paths to web-relative (`/audio/audio.mp3`, `/images/graphic_000.png`)
3. Writes `timeline.json` to output dir
4. Bundles Remotion composition from `src/video/remotion-entry.tsx` (auto-created if missing)
5. Renders via `@remotion/renderer` with h264 codec
6. Bundle is cached between renders (same session)

### Subtitles

```typescript
exportSubtitles(timeline, outputPath): Promise<{ srtPath: string; vttPath: string }>
```

Generates `.srt` and `.vtt` from word timings (6 words per subtitle line).

---

## Nano Banana MCP Integration

When available as an MCP server, Nano Banana provides direct image generation:

```
Tool: mcp__nanobanana-mcp__gemini_generate_image
```

Use ToolSearch to check availability. If available, prefer it over the built-in Gemini API calls for interactive use, since it provides a richer editing workflow:

- `gemini_generate_image`: Initial generation
- `continue_editing`: Refine an existing image
- `get_image_by_id`: Retrieve a specific image
- `search_history`: Find previously generated images

For batch generation in the pipeline, the built-in `generateImagesForCues()` is more efficient since it includes QC loops and cost tracking.

---

## Quality Tiers

**File:** `src/quality/types.ts`

```typescript
const QUALITY_PRESETS = {
  draft: {
    tier: 'draft',
    audio: { provider: 'kokoro' },
    llm: {},
  },
  standard: {
    tier: 'standard',
    audio: { provider: 'elevenlabs' },
    llm: {},
  },
  high: {
    tier: 'high',
    audio: { provider: 'elevenlabs' },
    llm: {
      claudeModel: 'claude-opus-4-20250514',
      geminiModel: 'gemini-2.5-pro',
    },
  },
};
```

Draft is free (local Kokoro TTS). Standard/high use ElevenLabs (paid). High also upgrades LLM models but that is irrelevant for render-video (no LLM calls).

---

## CLI Entry Point

**File:** `src/cli/commands/generate.ts`

The `generate` CLI command wraps `runProduction()`:

```bash
npx tsx src/cli/index.ts generate "topic" --quality draft --video-type documentary
```

For skill use, call individual pipeline stages rather than the full CLI.
