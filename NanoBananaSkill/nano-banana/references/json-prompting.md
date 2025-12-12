# JSON Prompting for Nano Banana Pro

Structured specifications for precision image generation.

## When to Use JSON Prompting

**Use JSON when:**
- You need exact reproducibility across generations
- You're iterating on one element without changing others
- The image has strict brand/data constraints
- You're building a system, not generating one-offs
- Stakes are high (marketing materials, client work, production)

**Use natural language when:**
- You're exploring and want the model to surprise you
- You don't yet know what the important variables are
- A single prose prompt captures what you want
- Speed matters more than precision

## The Core Concept: Handles

JSON gives every important element a stable identifier. These "handles" enable **scoped edits**.

```
Traditional prompting:
  "Make the lighting warmer" → entire scene regenerates

JSON prompting:
  Change lighting.color_temperature: "warm" → only lighting changes
```

## Three Schema Types

| Schema | Domain | Key Fields |
|--------|--------|------------|
| `marketing_image` | Product shots, brand photos | subject, props, environment, camera, lighting, brand |
| `ui_builder` | App screens, dashboards | tokens, screens, containers, components |
| `diagram_spec` | Flowcharts, infographics | nodes, edges, groups, data_constraints |

## The Translator Workflow

You don't have to write JSON yourself.

```
1. Describe what you want in plain English
2. Claude translates to structured JSON schema
3. Review: check key fields match intent
4. Render with Nano Banana Pro
5. Iterate: modify specific fields, re-render
```

## Schema Anatomy: Marketing Image

```json
{
  "marketing_image": {
    "meta": {
      "title": "Aurora Lime Hero Shot",
      "brand_name": "Aurora Lime"
    },
    "subject": {
      "type": "product_can",
      "name": "Aurora Lime Seltzer",
      "physical_properties": {
        "volume_oz": 12,
        "finish": "matte"
      }
    },
    "props": {
      "foreground": [
        {"type": "lime_slice", "count": 3, "position": "front_left"}
      ],
      "midground": [
        {"type": "ice_cube", "count": 12, "position": "around_base"}
      ]
    },
    "environment": {
      "surface": {"material": "glossy", "reflection_strength": 0.7},
      "background": {"color": "#003b47", "effect": "bokeh_soft"}
    },
    "camera": {
      "angle": "three_quarter_front",
      "framing": "medium_close",
      "focal_length_mm": 50
    },
    "lighting": {
      "key_light_direction": "right",
      "key_light_intensity": "high",
      "fill_light_direction": "left",
      "fill_light_intensity": "low",
      "color_temperature": "neutral"
    },
    "controls": {
      "lock_subject_geometry": true,
      "lock_logo_and_label": true,
      "allow_background_variation": false
    }
  }
}
```

## Key Fields Explained

### Subject Block
What the image is of. Be specific about physical properties.

| Field | Purpose |
|-------|---------|
| `type` | Category: product_can, bottle, device, person |
| `name` | Product/brand name |
| `physical_properties` | Size, finish, material |

### Props Block
Objects around the subject, organized by depth.

| Layer | Position |
|-------|----------|
| `foreground` | Closest to camera |
| `midground` | Same plane as subject |
| `background` | Behind subject |

### Environment Block
Everything that isn't subject or props.

| Field | Controls |
|-------|----------|
| `surface.material` | What subject sits on |
| `surface.reflection_strength` | 0-1 reflectivity |
| `background.color` | Hex code or name |
| `background.effect` | bokeh_soft, gradient, solid |

### Camera Block
Your virtual camera setup.

| Field | Options |
|-------|---------|
| `angle` | front, three_quarter_front, overhead, low |
| `framing` | close_up, medium, medium_close, wide |
| `focal_length_mm` | 24 (wide) → 85 (compressed) |
| `depth_of_field` | shallow, medium, deep |

### Lighting Block
Where light comes from and how intense.

| Field | Controls |
|-------|----------|
| `key_light_direction` | Primary light: left, right, front, back, top |
| `key_light_intensity` | low, medium, high, very_high |
| `fill_light_*` | Secondary light (softens shadows) |
| `rim_light` | Boolean: edge highlight from behind |
| `color_temperature` | cool, neutral, warm |

### Controls Block
What stays locked during iteration.

| Field | Effect |
|-------|--------|
| `lock_subject_geometry` | Can't turn can into bottle |
| `lock_logo_and_label` | Brand elements stay exact |
| `allow_background_variation` | Can background change? |
| `allow_prop_relayout` | none, small_only, free |

## Iteration Patterns

### Lighting Variation
Keep everything fixed, test lighting setups:

```json
// Version A
"lighting": {"key_light_direction": "right", "key_light_intensity": "high"}

// Version B
"lighting": {"key_light_direction": "left", "key_light_intensity": "medium"}
```

### Camera Moves
Same scene, different perspective:

```json
// Version A
"camera": {"angle": "three_quarter_front", "framing": "medium"}

// Version B
"camera": {"angle": "overhead", "framing": "close_up"}
```

### Theme Swap
Same structure, different visual treatment:

```json
// Summer theme
"environment": {"background": {"color": "#FFE4B5"}, "atmosphere": {"mood": "bright, refreshing"}}

// Winter theme
"environment": {"background": {"color": "#E8F4F8"}, "atmosphere": {"mood": "cool, crisp"}}
```

## Validation Checklist

Before rendering, verify:

- [ ] Subject type and name correct
- [ ] Props positioned logically
- [ ] Colors are valid hex codes
- [ ] Lighting creates desired mood
- [ ] Camera angle matches composition intent
- [ ] Controls lock what should stay fixed

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Over-specification | Leave non-critical fields null or default |
| Under-specification | Be explicit about things that matter |
| Wrong lock settings | Set controls based on iteration intent |
| Vague positions | Use specific: "front_left" not "nearby" |

## When JSON Breaks Down

JSON isn't always the answer:

- **Creative exploration** - Prose prompts let model surprise you
- **One-off images** - Setup cost exceeds benefit
- **Abstract concepts** - Hard to specify "feeling" in fields
- **Rapid ideation** - Speed > precision

Use the right tool for the job.
