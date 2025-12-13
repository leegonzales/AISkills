# Veo 3.1 Video Prompter

Craft professional-grade video prompts for Google's Veo 3.1 model using cinematic techniques, synchronized audio direction, and timestamp choreography.

## Features

- **Cinematic Structure** - Five-element formula for consistent, high-quality prompts
- **Audio Direction** - Dialogue, SFX, ambient noise, and music cues
- **Timestamp Prompting** - Multi-shot choreography in single generations
- **Camera Vocabulary** - Complete glossary of cinematography terms
- **Style Keywords** - Aesthetic, mood, and lighting descriptors
- **20+ Examples** - Categorized prompts across genres

## When to Use

Perfect for:
- Creating AI video content with Veo 3.1
- Drafting prompts in Google AI Studio or Vertex AI
- Storyboarding multi-shot sequences
- Learning cinematic video direction vocabulary
- Transforming ideas into structured video prompts

## Installation

### For Claude Code

```bash
# Install globally
cp -r veo3-prompter ~/.claude/skills/

# Or install for specific project
cp -r veo3-prompter your-project/.claude/skills/
```

### For Claude Projects (Web)

1. Go to [claude.ai](https://claude.ai)
2. Open or create a Project
3. Navigate to Project Knowledge
4. Upload `SKILL.md` file

## Quick Start

**Basic Usage:**
```
"Help me create a Veo 3.1 prompt for a sunset beach scene"
```

**With Specifications:**
```
"Create a cinematic Veo prompt: two people walking on a beach at sunset,
talking about the future, warm romantic mood, include dialogue"
```

**Multi-Shot Sequence:**
```
"Generate a timestamp prompt for an 8-second coffee shop scene
with three distinct shots"
```

## The Five-Element Formula

Every effective Veo 3.1 prompt should include:

| Element | Description | Example |
|---------|-------------|---------|
| **Cinematography** | Camera angle, movement, lens | "Slow dolly-in, medium close-up" |
| **Subject** | Main focus of the shot | "A tired office worker" |
| **Action** | What's happening | "rubbing her temples" |
| **Context** | Setting and environment | "in a cluttered cubicle at night" |
| **Style & Audio** | Aesthetic, mood, sound | "Harsh fluorescent light, ambient: keyboard typing" |

## Example Output

**User Request:** "Create a prompt for a detective discovering a clue"

**Generated Prompt:**
```
Close-up of a weathered detective's hands carefully lifting a
photograph from a dusty drawer. Slow dolly-in as his expression
shifts from confusion to recognition.

The scene is lit by a single desk lamp casting dramatic shadows,
noir aesthetic, 1940s period setting.

SFX: Drawer creaking open, paper rustling, distant thunder.
A clock ticks steadily in the background.
```

## Veo 3.1 Specifications

| Parameter | Options |
|-----------|---------|
| Duration | 4, 6, or 8 seconds |
| Resolution | 720p, 1080p |
| Aspect Ratio | 16:9 (landscape), 9:16 (portrait) |
| Frame Rate | 24 FPS |
| Audio | Synchronized dialogue, SFX, ambient |

## Access Veo 3.1

- **Flow** - Visual editor at [flow.google.com](https://flow.google.com)
- **Google AI Studio** - Developer access via Gemini API
- **Vertex AI** - Enterprise deployment on Google Cloud

## Documentation

- **[SKILL.md](SKILL.md)** - Core skill definition (read by Claude)
- **[cinematography-glossary.md](references/cinematography-glossary.md)** - Full camera terms reference
- **[prompt-examples.md](references/prompt-examples.md)** - 20+ categorized examples
- **[advanced-workflows.md](references/advanced-workflows.md)** - Image-to-video, transitions

## Version

Current: v1.0.0

## Sources

Built from official documentation:
- [Google DeepMind Veo 3.1](https://deepmind.google/models/veo/)
- [Ultimate Prompting Guide for Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- [Veo Prompt Guide - DeepMind](https://deepmind.google/models/veo/prompt-guide/)
- [Veo on Vertex AI Prompt Guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)

## License

MIT License - See LICENSE file

---

Built with Claude Code | Part of [AISkills Collection](https://github.com/leegonzales/AISkills)
