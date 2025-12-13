---
name: veo3-prompter
description: Craft professional video prompts for Google Veo 3.1 using cinematic techniques, audio direction, and timestamp choreography. Use when generating AI videos, creating video prompts, or working with Veo 3.
---

# Veo 3.1 Video Prompter

Transform ideas into professional Veo 3.1 prompts using cinematic structure, audio direction, and multi-shot choreography.

## When to Use

Invoke when user:
- Says "create a video prompt" or "generate a Veo prompt"
- Wants to "make a video of..." or "animate this..."
- Asks for help with "video generation" or "AI video"
- Needs "Veo 3" or "Veo 3.1" prompt assistance
- Wants to create "multi-shot" or "cinematic" video sequences

## Core Prompt Formula

**[Cinematography] + [Subject] + [Action] + [Context] + [Style & Audio]**

Every prompt should address these five elements for maximum control.

## Cinematography Elements

### Shot Composition
- Wide shot, medium shot, close-up, extreme close-up
- Single shot, two shot, over-the-shoulder shot
- High angle, low angle, eye level, worm's eye, bird's eye

### Camera Movement
- Dolly (in/out), tracking shot, crane shot
- Pan (left/right), tilt (up/down), zoom
- Steadicam, handheld, aerial, POV

### Lens & Focus
- Shallow depth of field, deep focus
- Wide-angle lens, telephoto, macro lens
- Soft focus, rack focus, bokeh

## Audio Direction

Veo 3.1 generates synchronized sound. Direct it explicitly:

**Dialogue** (use quotes):
> "A man says, 'The storm is coming.'"

**Sound Effects** (label with SFX):
> "SFX: Thunder rumbles in the distance, rain patters on glass"

**Ambient Noise**:
> "Ambient noise: busy café chatter, clinking cups, soft jazz"

**Music**:
> "A swelling orchestral score begins to play"

## Timestamp Prompting

For multi-shot sequences within one generation (max 8 seconds):

```
[00:00-00:02] Medium shot of a detective at his desk, lighting a cigarette.
SFX: Match strike, paper rustling.

[00:02-00:04] Close-up of his eyes narrowing as he reads a letter.
Ambient: Rain against the window.

[00:04-00:06] Reverse shot of a shadowy figure in the doorway.
A woman's voice: "You shouldn't have looked."

[00:06-00:08] Wide shot as the detective stands, reaching for his gun.
SFX: Chair scraping, thunder crack.
```

## Style Keywords

**Visual Aesthetic:**
- Photorealistic, cinematic, documentary, animation
- Retro (sepia, grainy film, 1980s vaporwave)
- Noir, epic fantasy, sci-fi, romantic, horror

**Mood & Lighting:**
- Warm golden hour, cool blue tones, moody shadows
- Harsh fluorescent, soft morning light, dramatic chiaroscuro
- Neon-lit, candlelit, overcast diffused

**Film Grain Tip:**
> Add "slightly grainy, film-like" to avoid overly clean AI look

## Output Formats

**Quick Prompt:** Single sentence for simple shots
**Structured Prompt:** Multi-line with all five elements
**Timestamp Sequence:** Choreographed multi-shot within 8s
**Storyboard Mode:** Multiple prompts for full narrative

## Example Prompts

**Action Shot:**
> "Tracking shot following a parkour athlete sprinting across rooftops at sunset, warm orange light, urban cityscape background, cinematic, shallow depth of field. SFX: footsteps on concrete, wind rushing past."

**Dialogue Scene:**
> "Medium two-shot in a dimly lit bar, a woman in red leans toward a man in a suit. She says quietly, 'I know what you did.' Ambient: jazz music, glasses clinking. Moody noir aesthetic, warm tungsten lighting."

**Nature Documentary:**
> "Slow-motion close-up of a hummingbird drinking from a flower, macro lens with shallow focus, lush green garden background, soft morning light. SFX: gentle buzzing, birdsong."

## Technical Specs

- **Duration:** 4, 6, or 8 seconds
- **Resolution:** 720p or 1080p
- **Aspect Ratio:** 16:9 (landscape) or 9:16 (portrait)
- **Frame Rate:** 24 FPS

## References

- `references/cinematography-glossary.md` - Full camera terms
- `references/prompt-examples.md` - 20+ categorized examples
- `references/advanced-workflows.md` - Image-to-video, first/last frame
