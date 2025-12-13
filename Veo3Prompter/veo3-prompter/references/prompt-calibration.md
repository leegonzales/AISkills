# Prompt Calibration Guide

How to find the optimal detail level for Veo 3.1 prompts.

---

## The Fundamental Tradeoff

Video generation models have a **cognitive budget**. Every instruction you add:
- **Consumes attention** the model could spend on execution quality
- **Constrains possibilities** (good when intentional, bad when excessive)
- **Creates potential conflicts** with other instructions

The goal: **Maximum creative control with minimum instruction overhead.**

---

## The Three Failure Modes

### 1. Under-specified (Too Sparse)

**What happens:** Model fills gaps with generic defaults or random choices.

**Example:**
```
"A woman walking"
```

**Problems:**
- What age? What's she wearing? Walking where?
- What mood? Happy? Sad? Rushed?
- What time of day? What weather?
- You'll get something, but it won't be YOUR vision

**When sparse is OK:** Early exploration, you genuinely want variety

---

### 2. Over-specified (Too Dense)

**What happens:** Model can't process all instructions, drops some, produces stiff or confused output.

**Example:**
```
"Extreme close-up shot at a 15-degree dutch angle using an 85mm
f/1.4 lens with creamy bokeh, of a 34-year-old East Asian woman
with shoulder-length black hair with subtle purple highlights,
wearing vintage 1970s-style round tortoiseshell glasses and a
hand-knitted cream cardigan with wooden buttons over a faded
band t-shirt, her expression transitioning from contemplative
melancholy to dawning realization as she reads a handwritten
letter on yellowed paper while sitting in a worn leather
armchair positioned next to a rain-streaked window in a
cluttered but cozy Brooklyn brownstone apartment filled with
houseplants and stacked books, late afternoon golden hour light
filtering through sheer curtains creating warm highlights on her
face while cool blue reflected light from outside fills the
shadows, the camera slowly pushing in 6 inches over 4 seconds
while simultaneously executing a subtle 3-degree clockwise
rotation, ambient sound of rain on glass and distant traffic
mixed with the quiet rustle of paper and her soft breathing,
melancholic indie folk guitar plays softly from an out-of-frame
record player, the overall aesthetic channeling Wong Kar-wai's
In the Mood for Love crossed with A24's understated naturalism,
slightly desaturated color grade with lifted blacks and gentle
film grain texture..."
```

**Problems:**
- Model can't track all details
- Motion becomes stiff (too many constraints)
- Some instructions get silently dropped
- Conflicting details may cancel out

---

### 3. Well-calibrated (Optimal)

**What happens:** Model has clear direction but room to execute naturally.

**Example:**
```
"Close-up of a woman in her 30s reading a letter by a rainy window.
Her expression shifts from sadness to hope. Cozy apartment, golden
hour light mixing with cool blue from outside. Slow gentle push-in.

Ambient: rain on glass, soft rustling paper.
Melancholic but warm, indie film aesthetic."
```

**Why this works:**
- Clear subject and action
- Emotional arc specified (sadness → hope)
- Lighting direction without over-constraining
- Camera move without exact measurements
- Audio layered simply
- Style evoked, not dictated

---

## The Priority Tiers (Expanded)

### Tier 1: Essential (Always Include)

| Element | Why Essential | Example |
|---------|---------------|---------|
| **Shot size** | Determines framing, intimacy | "Medium close-up" |
| **Subject** | Model needs to know what to generate | "A chef in his 40s" |
| **Primary action** | Video needs motion/purpose | "kneading bread dough" |
| **Dominant mood** | Sets tone for all other choices | "warm, meditative" |

**Tier 1 alone:**
> "Medium close-up of a chef in his 40s kneading bread dough. Warm, meditative."

This generates something coherent but generic.

---

### Tier 2: Important (Include Most)

| Element | Impact | When to Include |
|---------|--------|-----------------|
| **Camera movement** | Adds cinematic quality | When motion matters to story |
| **Lighting quality** | Sets mood powerfully | Always worth specifying |
| **Setting/environment** | Grounds the scene | When location matters |
| **One audio layer** | Sells realism | Dialogue OR key SFX OR ambient |

**Tier 1 + Tier 2:**
> "Medium close-up of a chef in his 40s kneading bread dough in a rustic bakery kitchen. Slow push-in. Warm morning light through dusty windows. SFX: dough slapping on wood, soft flour puff. Meditative, artisanal."

Now it has character and place.

---

### Tier 3: Enhancement (Pick 1-2 Max)

| Element | When Worth Adding |
|---------|-------------------|
| Secondary audio | Scene needs sonic richness |
| Lens type | Specific visual effect needed |
| Color palette | Strong stylistic intent |
| Film grain/texture | Period or aesthetic requirement |
| Background action | World-building matters |
| Specific costume details | Character-driven story |

**Tier 1 + Tier 2 + selective Tier 3:**
> "Medium close-up of a chef in his 40s, flour-dusted apron, kneading bread dough in a rustic bakery kitchen. Slow push-in. Warm morning light through dusty windows, shallow depth of field. SFX: dough slapping on wood, soft flour puff. Ambient: distant radio playing French cafe music. Meditative, artisanal, slightly grainy film texture."

This is near the upper limit of useful detail.

---

## Calibration by Shot Type

### Simple Action Shots
**Budget:** Tier 1 + 2-3 Tier 2 elements
```
"Wide shot of a surfer catching a wave at sunset. Tracking shot
following from the beach. Golden orange light, silhouette against
bright sky. SFX: crashing waves, seagulls. Cinematic, inspiring."
```

### Dialogue Scenes
**Budget:** Tier 1 + all Tier 2 + dialogue as primary audio
```
"Medium two-shot in a diner booth. A father and teenage daughter
sit across from each other. She looks down, he reaches across the
table. He says gently: 'I'm sorry I wasn't there.'

Warm tungsten diner light, late evening. Ambient: quiet diner sounds,
distant jukebox. Emotional, intimate."
```

### Complex Multi-beat Shots
**Budget:** Timestamp structure + Tier 1-2 per segment
```
[00:00-00:03] Wide shot of empty stage. Single spotlight clicks on.
SFX: electrical hum, switch click.

[00:03-00:06] A dancer steps into the light, begins slow movement.
First notes of piano.

[00:06-00:08] Close-up of her face, eyes closed, lost in motion.
Music swells. Intimate, transcendent.
```

---

## Diagnostic Questions

Before generating, ask:

1. **Can I remove any element without losing my core vision?**
   - If yes → remove it

2. **Am I specifying both camera angle AND camera movement?**
   - Usually pick one, not both

3. **Do I have more than two audio layers?**
   - Simplify: primary + ambient is usually enough

4. **Am I describing exact measurements or positions?**
   - Replace "6 inches over 4 seconds" with "slow push-in"

5. **Is any element purely decorative?**
   - If it doesn't serve the story/mood, cut it

---

## Iteration Protocol

### First Generation (Diagnostic)

Use Tier 1 + minimal Tier 2:
```
"Medium shot of a scientist examining a glowing sample in a dark lab.
She looks intrigued. Blue light from sample illuminates her face.
Mysterious, sci-fi."
```

Evaluate: What's missing? What's wrong?

### Second Generation (Targeted Addition)

Add ONLY what was missing:
```
"Medium shot of a scientist in her 30s, lab coat, examining a glowing
blue sample in a dark laboratory. She leans closer, expression shifting
to wonder. Blue light from sample illuminates her face, rest of lab in
shadow. Slow subtle push-in.

SFX: soft electrical hum, her quiet gasp.
Mysterious, sci-fi, cinematic."
```

### Third Generation (Refinement)

Fine-tune based on results:
- If motion was stiff → reduce constraints
- If mood was off → strengthen style keywords
- If audio was wrong → be more specific about sound

---

## Common Mistakes and Fixes

### Mistake: Specifying exact timing
**Bad:** "At exactly 2.3 seconds, she turns her head 45 degrees to the left"
**Good:** "She turns to look at something off-screen"

### Mistake: Contradictory instructions
**Bad:** "Bright sunny day, moody noir lighting, soft overcast feel"
**Good:** "Overcast day, diffused natural light, contemplative mood"

### Mistake: Character biography in prompt
**Bad:** "Sarah, 34, who grew up in Minnesota and moved to NYC after college..."
**Good:** "A woman in her 30s, urban professional look"

### Mistake: Micro-managing physics
**Bad:** "Rain falls at 15 mph with droplets approximately 2mm diameter"
**Good:** "Heavy rain"

### Mistake: Over-specifying color
**Bad:** "Hex #E8D4B8 warm beige with RGB 232, 212, 184"
**Good:** "Warm cream tones" or "golden hour palette"

---

## The Goldilocks Test

Read your prompt aloud. It should take:
- **Under 10 seconds:** Probably too sparse
- **10-25 seconds:** Likely optimal
- **Over 30 seconds:** Probably too dense

For timestamp prompts, apply this per segment.

---

## Quick Reference Card

```
OPTIMAL PROMPT STRUCTURE:
─────────────────────────
[Shot size] of [subject with 1-2 key details]
[doing primary action] in [setting].
[Camera movement OR angle, not both].
[Lighting quality], [one style word].

[Audio: dialogue OR "SFX:" OR "Ambient:"]
[Optional: one Tier 3 enhancement]
─────────────────────────

WORD COUNT TARGETS:
• Simple shot: 30-50 words
• Standard scene: 50-80 words
• Complex/dialogue: 80-120 words
• Timestamp segment: 25-40 words each
```

---

## Remember

The model is creative. Your job is to **direct**, not **dictate**.

Give it:
- Clear framing
- Emotional direction
- Essential constraints
- Room to perform

Think like a film director giving notes to a cinematographer—not like an engineer writing machine specifications.
