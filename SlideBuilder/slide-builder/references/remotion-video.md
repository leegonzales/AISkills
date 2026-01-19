# Remotion Video Output Reference

## 1. Overview

Remotion is a React-based video framework that renders programmatically generated videos. The slide-builder can output a `timeline.json` that feeds into a Remotion composition, enabling fully automated YouTube-ready video generation from Talk Track v5 format.

**Key Benefits:**
- Programmatic video generation (no manual editing)
- React components for visual elements
- Precise audio/caption synchronization
- Consistent, reproducible output

## 2. Architecture

```
talk-track.md (v5)
       ↓
  Parse slides + audio
       ↓
  Generate timeline.json
       ↓
  Remotion composition
       ↓
  H.264 MP4 output
```

**Data Flow:**
1. Talk Track v5 markdown parsed for slide metadata, audio paths, and timing
2. Timeline calculator computes durations from audio file lengths
3. JSON timeline fed to Remotion composition
4. React components render each frame
5. FFmpeg encodes final MP4

## 3. Timeline JSON Structure

```json
{
  "fps": 30,
  "width": 1920,
  "height": 1080,
  "totalDuration": 342.7,
  "segments": [
    {
      "slug": "title",
      "image": "images/slide-title.png",
      "audio": "audio/title.wav",
      "duration": 45.5,
      "startFrame": 0,
      "endFrame": 1365,
      "section": "opening",
      "captions": [
        {
          "text": "I'm going to tell you",
          "start": 0.0,
          "end": 0.8
        },
        {
          "text": "about something important today.",
          "start": 0.8,
          "end": 1.6
        }
      ]
    },
    {
      "slug": "problem-statement",
      "image": "images/slide-problem-statement.png",
      "audio": "audio/problem-statement.wav",
      "duration": 62.3,
      "startFrame": 1365,
      "endFrame": 3234,
      "section": "opening",
      "captions": []
    }
  ]
}
```

**Field Definitions:**
| Field | Type | Description |
|-------|------|-------------|
| `fps` | number | Frames per second (30 standard) |
| `width` | number | Video width in pixels |
| `height` | number | Video height in pixels |
| `totalDuration` | number | Total video length in seconds |
| `segments[].slug` | string | Unique slide identifier |
| `segments[].image` | string | Path to slide image |
| `segments[].audio` | string | Path to audio file |
| `segments[].duration` | number | Segment duration in seconds |
| `segments[].startFrame` | number | First frame of segment |
| `segments[].endFrame` | number | Last frame of segment |
| `segments[].section` | string | Presentation section name |
| `segments[].captions` | array | Word/phrase timing data |

## 4. Caption Sync

### Audio Provider Capabilities

| Provider | Timestamp Precision | Notes |
|----------|-------------------|-------|
| ElevenLabs v3 | Word-level | Best for caption sync |
| Kokoro | Sentence-level | Requires alignment post-processing |
| OpenAI TTS | None | Manual alignment needed |

### Caption Data Structure

```json
{
  "captions": [
    {
      "text": "Welcome to",
      "start": 0.0,
      "end": 0.45,
      "confidence": 0.98
    },
    {
      "text": "this presentation",
      "start": 0.45,
      "end": 1.2,
      "confidence": 0.95
    }
  ]
}
```

### Caption Rendering Styles

- **Karaoke**: Words highlight as spoken
- **Subtitle**: Full phrases appear/disappear
- **Teleprompter**: Scrolling text synced to audio

## 5. Remotion Composition

### Project Structure

```
src/
  video/
    Presentation.tsx      # Root composition
    components/
      Slide.tsx           # Slide image display
      AudioTrack.tsx      # Audio playback
      CaptionOverlay.tsx  # Animated captions
      Transitions.tsx     # Slide transitions
    hooks/
      useTimeline.ts      # Timeline data loader
      useCaptions.ts      # Caption state management
```

### Root Composition

```tsx
// Presentation.tsx
import { Composition } from 'remotion';
import { PresentationVideo } from './PresentationVideo';
import timeline from '../../timeline.json';

export const RemotionRoot: React.FC = () => {
  const totalFrames = Math.ceil(timeline.totalDuration * timeline.fps);

  return (
    <Composition
      id="Presentation"
      component={PresentationVideo}
      durationInFrames={totalFrames}
      fps={timeline.fps}
      width={timeline.width}
      height={timeline.height}
      defaultProps={{ timeline }}
    />
  );
};
```

### Slide Component

```tsx
// Slide.tsx
import { Img, useCurrentFrame } from 'remotion';

interface SlideProps {
  imagePath: string;
  startFrame: number;
  endFrame: number;
}

export const Slide: React.FC<SlideProps> = ({ imagePath, startFrame, endFrame }) => {
  const frame = useCurrentFrame();

  if (frame < startFrame || frame >= endFrame) {
    return null;
  }

  return (
    <Img
      src={imagePath}
      style={{
        width: '100%',
        height: '100%',
        objectFit: 'contain',
      }}
    />
  );
};
```

### Audio Track Component

```tsx
// AudioTrack.tsx
import { Audio, useCurrentFrame } from 'remotion';

interface AudioTrackProps {
  audioPath: string;
  startFrame: number;
}

export const AudioTrack: React.FC<AudioTrackProps> = ({ audioPath, startFrame }) => {
  return (
    <Audio
      src={audioPath}
      startFrom={0}
      volume={1}
    />
  );
};
```

### Caption Overlay Component

```tsx
// CaptionOverlay.tsx
import { useCurrentFrame, interpolate } from 'remotion';

interface Caption {
  text: string;
  start: number;
  end: number;
}

interface CaptionOverlayProps {
  captions: Caption[];
  fps: number;
  segmentStartFrame: number;
}

export const CaptionOverlay: React.FC<CaptionOverlayProps> = ({
  captions,
  fps,
  segmentStartFrame,
}) => {
  const frame = useCurrentFrame();
  const relativeFrame = frame - segmentStartFrame;
  const currentTime = relativeFrame / fps;

  const activeCaption = captions.find(
    (c) => currentTime >= c.start && currentTime < c.end
  );

  if (!activeCaption) return null;

  const opacity = interpolate(
    currentTime,
    [activeCaption.start, activeCaption.start + 0.1, activeCaption.end - 0.1, activeCaption.end],
    [0, 1, 1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 80,
        left: 0,
        right: 0,
        textAlign: 'center',
        opacity,
      }}
    >
      <span
        style={{
          backgroundColor: 'rgba(0, 0, 0, 0.7)',
          color: 'white',
          padding: '12px 24px',
          fontSize: 32,
          fontFamily: 'Inter, sans-serif',
          borderRadius: 8,
        }}
      >
        {activeCaption.text}
      </span>
    </div>
  );
};
```

## 6. Rendering

### Basic Render Command

```bash
npx remotion render src/video/Presentation.tsx Presentation output.mp4
```

### Production Render Options

```bash
npx remotion render \
  src/video/Presentation.tsx \
  Presentation \
  presentation.mp4 \
  --codec h264 \
  --crf 18 \
  --fps 30 \
  --pixel-format yuv420p \
  --audio-codec aac \
  --audio-bitrate 128k
```

### Render Options Reference

| Option | Value | Description |
|--------|-------|-------------|
| `--codec` | `h264` | YouTube-compatible codec |
| `--crf` | `18` | Quality (0-51, lower = better) |
| `--fps` | `30` | Frame rate |
| `--pixel-format` | `yuv420p` | Color space for compatibility |
| `--audio-codec` | `aac` | Audio codec |
| `--audio-bitrate` | `128k` | Audio quality |
| `--concurrency` | `4` | Parallel render threads |
| `--frames` | `0-300` | Render specific frame range |

### Render Performance

| Resolution | Duration | Approx. Render Time |
|------------|----------|---------------------|
| 1080p | 5 min | ~8-15 min |
| 1080p | 15 min | ~25-45 min |
| 4K | 5 min | ~30-60 min |

## 7. Output Specifications

### YouTube Recommended Settings

| Property | Value |
|----------|-------|
| Resolution | 1920x1080 (16:9) |
| Codec | H.264 |
| Container | MP4 |
| Frame Rate | 30fps |
| Audio Codec | AAC |
| Audio Bitrate | 128kbps |
| Audio Sample Rate | 48kHz |
| Color Space | BT.709 |
| Pixel Format | yuv420p |

### Alternative Resolutions

| Format | Resolution | Use Case |
|--------|------------|----------|
| 720p | 1280x720 | Draft/preview |
| 1080p | 1920x1080 | Standard YouTube |
| 1440p | 2560x1440 | High quality |
| 4K | 3840x2160 | Premium content |

## 8. Integration Notes

### AITalkShowCli Patterns

The slide-builder video pipeline is based on patterns from AITalkShowCli:

- **Timeline Calculator**: Reads audio file durations to compute segment timing
- **Segment-Based Audio**: Each slide has independent audio file for precise sync
- **Caption Extraction**: Word timestamps extracted during TTS generation
- **Asset Pipeline**: Images and audio organized in predictable directory structure

### Directory Structure

```
output/
  timeline.json
  images/
    slide-title.png
    slide-problem-statement.png
    ...
  audio/
    title.wav
    problem-statement.wav
    ...
  captions/
    title.json
    problem-statement.json
    ...
```

### Automation Script Example

```bash
#!/bin/bash
# generate-video.sh

# 1. Parse talk track and generate timeline
node scripts/parse-talk-track.js talk-track.md > output/timeline.json

# 2. Render video with Remotion
npx remotion render \
  src/video/Presentation.tsx \
  Presentation \
  output/final.mp4 \
  --codec h264 \
  --crf 18

# 3. Verify output
ffprobe -v error -show_format output/final.mp4

echo "Video generated: output/final.mp4"
```

### Error Handling

Common issues and solutions:

| Issue | Cause | Solution |
|-------|-------|----------|
| Audio desync | Incorrect duration calculation | Verify audio file lengths match timeline |
| Missing frames | Segment gaps in timeline | Ensure `endFrame` of segment N = `startFrame` of segment N+1 |
| Black frames | Image path incorrect | Check relative paths in timeline.json |
| No audio | Audio codec incompatible | Use WAV or AAC source files |

## 9. Future Enhancements

Potential improvements for the video pipeline:

- **Transitions**: Fade, slide, or zoom between slides
- **B-Roll Integration**: Insert video clips during narration
- **Speaker Video**: Picture-in-picture presenter overlay
- **Chapter Markers**: YouTube chapter metadata generation
- **Thumbnail Generation**: Auto-extract key frame for thumbnail
