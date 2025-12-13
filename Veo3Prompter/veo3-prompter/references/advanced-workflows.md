# Advanced Veo 3.1 Workflows

Advanced techniques for complex video generation including image-to-video, first/last frame, and multi-shot production.

---

## Workflow 1: Reference Images to Video

Use up to 3 reference images to maintain consistency across shots.

### How It Works
1. Generate or provide reference images (character, setting, props)
2. Upload images with your text prompt
3. Veo maintains visual consistency from references

### Example: Brand Mascot Video
```
Reference Images:
- character.png (cartoon robot mascot)
- office.png (branded office setting)
- product.png (company's main product)

Prompt:
"Using the provided images for the robot mascot, office setting,
and product, create a medium shot of the robot presenting the
product at a desk. The robot gestures enthusiastically and says,
'This is going to change everything!'

Bright, cheerful lighting. Corporate video aesthetic.
SFX: Friendly robot voice, subtle mechanical whir."
```

### Best Practices
- Keep reference images under 3 for best coherence
- Use consistent lighting across reference images
- Describe how references should interact
- Reference images work best for characters and settings

---

## Workflow 2: First and Last Frame Transitions

Provide start and end images; Veo interpolates the motion between them.

### Use Cases
- Transformation sequences
- Smooth scene transitions
- Precise start/end state control
- Morphing effects

### Example: Day to Night Transition
```
First Frame: city_day.png (cityscape at noon, busy streets)
Last Frame: city_night.png (same angle at night, lights on)

Prompt:
"The camera remains static as time passes from day to night.
Shadows lengthen, sky transitions through sunset colors,
city lights gradually illuminate. Traffic flow shifts from
cars to fewer vehicles with headlights.

Time-lapse aesthetic, 8 seconds.
SFX: Time passing ambience, traffic transitioning to quiet night."
```

### Example: Character Transformation
```
First Frame: human_portrait.png (regular person)
Last Frame: werewolf.png (same person transformed)

Prompt:
"Dramatic transformation sequence. Face contorts, fur emerges,
features shift painfully. Eyes change color last. Moonlight
illuminates the process.

Horror aesthetic, dramatic shadows.
SFX: Bones cracking, growling, fabric tearing."
```

### Best Practices
- Ensure start/end frames have similar composition
- Keep camera angle consistent between frames
- Describe the transformation process explicitly
- Works best with single subject transformations

---

## Workflow 3: Image-to-Video Animation

Start from a single image and describe the motion.

### Use Cases
- Animate still photographs
- Bring artwork to life
- Add subtle movement to portraits
- Create cinemagraphs

### Example: Portrait Animation
```
Source Image: old_photo.png (vintage family portrait)

Prompt:
"Subtle animation of this vintage photograph. Eyes blink
occasionally, chest rises with breathing, slight smile forms.
Hair moves as if touched by gentle breeze.

Maintain sepia tones and aged film quality.
SFX: Soft ambient room tone, distant clock ticking."
```

### Example: Landscape Animation
```
Source Image: landscape_painting.png (impressionist sunset)

Prompt:
"Bring this painting to life. Clouds drift slowly,
water ripples gently, sun descends toward horizon.
Birds fly across the sky. Maintain painterly aesthetic
throughout—this should feel like living art.

SFX: Gentle wind, water lapping, distant birdsong."
```

### Best Practices
- Start simple—breathing, blinking, subtle movement
- Describe physics realistically for natural motion
- Keep movement consistent with source image style
- Veo excels at water, hair, and cloth physics

---

## Workflow 4: Multi-Prompt Storyboard

Generate multiple clips with consistent elements for editing together.

### Production Process

1. **Create Style Guide**
   - Define visual aesthetic
   - Lock character descriptions
   - Establish lighting rules
   - Set audio tone

2. **Generate Shots Separately**
   - Use identical character/setting descriptions
   - Reference same style guide per shot
   - Maintain consistent technical specs

3. **Edit Together**
   - Export all clips
   - Assemble in video editor
   - Add transitions, music, titles

### Example: Short Commercial (4 shots)

**Style Guide:**
```
Characters: Young professional woman, 30s, confident smile,
wearing blue blazer.
Setting: Modern minimalist office, white walls, natural light.
Mood: Aspirational, clean, professional.
Color: Cool blues, warm accents.
Audio: Upbeat corporate music undertone.
```

**Shot 1 - Establishing (4s):**
```
Wide shot of the modern office. Woman walks in confidently,
sets laptop bag on desk. Natural morning light streams through
floor-to-ceiling windows.

SFX: Door opening, bag setting down.
Ambient: Quiet office atmosphere, distant city.
```

**Shot 2 - Working (4s):**
```
Medium shot of woman at desk, typing rapidly. Screen reflects
in her glasses. She pauses, smiles at something she's written.

SFX: Keyboard clicking, notification ping.
```

**Shot 3 - Success (4s):**
```
Close-up of her face as she receives good news. Eyes widen,
genuine smile spreads. She pumps fist subtly.

She says: "Yes!"
SFX: Phone notification, satisfied sigh.
```

**Shot 4 - Product (4s):**
```
Medium shot as she holds up product (insert reference image).
Turns it toward camera. Logo visible.

She says: "This made all the difference."
End on product close-up.
```

---

## Workflow 5: Iterative Refinement

Use Gemini to enhance prompts before sending to Veo.

### Process

1. **Draft Basic Prompt**
   ```
   A man walking in the rain
   ```

2. **Enhance with Gemini**
   ```
   Prompt to Gemini:
   "Enhance this Veo 3.1 video prompt with cinematic details,
   camera direction, and audio elements: 'A man walking in the rain'"
   ```

3. **Use Enhanced Prompt**
   ```
   Medium tracking shot following a solitary man in a long coat
   walking down a glistening city street at night. Heavy rain falls,
   creating puddle reflections of neon signs. Shallow depth of field
   isolates him from the blurred urban background.

   His footsteps splash rhythmically.
   SFX: Rain pattering on umbrella, distant thunder, wet footsteps.
   Ambient: Muffled city traffic, occasional car passing.

   Noir aesthetic, melancholy mood, cool blue color grading with
   warm neon accents.
   ```

---

## Workflow 6: Object Add/Remove

Modify generated videos by adding or removing elements.

**Note:** This feature uses Veo 2 and does not include audio.

### Adding Objects
```
Original video: Office scene with empty desk
Modification prompt: "Add a steaming cup of coffee on the desk"
```

### Removing Objects
```
Original video: Street scene with visible signage
Modification prompt: "Remove the billboard from the background"
```

### Best Practices
- Works best for static objects
- May require re-adding audio
- Multiple modifications may degrade quality
- Use for minor adjustments only

---

## Workflow 7: Aspect Ratio Strategy

Choose aspect ratio based on intended use.

### 16:9 Landscape
- YouTube videos
- Film/cinema content
- TV commercials
- Desktop viewing

### 9:16 Portrait
- TikTok / Instagram Reels / YouTube Shorts
- Mobile-first content
- Vertical stories
- Mobile ads

### Prompt Adjustment by Ratio

**Landscape (16:9):**
```
Wide shot emphasizing horizontal space, environmental context,
multiple subjects side by side possible.
```

**Portrait (9:16):**
```
Full body vertical framing, single subject focus, vertical
motion (jumping, falling), tall buildings, standing portraits.
```

---

## Technical Considerations

### Duration Selection

| Duration | Best For |
|----------|----------|
| 4 seconds | Quick cuts, reactions, product shots |
| 6 seconds | Standard scenes, dialogue exchanges |
| 8 seconds | Complex action, multi-beat scenes |

### Resolution Selection

| Resolution | Best For |
|------------|----------|
| 720p | Drafts, iteration, social media |
| 1080p | Final production, high quality |

### Dialogue Length

- 4s: ~10 words maximum
- 6s: ~15 words maximum
- 8s: ~20 words maximum

**Tip:** Keep dialogue short and natural. Speaking too fast sounds artificial.

---

## Prompt Enhancement Checklist

Before generating, verify your prompt includes:

- [ ] Shot size and composition
- [ ] Camera angle and movement
- [ ] Subject description and action
- [ ] Setting and context
- [ ] Lighting and color mood
- [ ] Audio: dialogue, SFX, ambient
- [ ] Style/aesthetic reference
- [ ] Technical specs (duration, aspect ratio)
