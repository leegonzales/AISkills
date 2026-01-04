---
status: drafting
title: "Nano Banana: AI Images That Actually Work"
series: 12 Days of Original AI Skills
day: 2
skill: nano-banana
version: 1.0.0
angle: "Image generation isn't hard. Getting consistent, usable results is."
---

# Day 2: Nano Banana

*AI Images That Actually Work*

---

I needed a picture of a robot holding a coffee cup.

Simple request. Five minutes with any AI image generator, right?

Three hours later, I had: a robot with seven fingers gripping a mug that seemed to phase through its hand. A photorealistic robot next to a cartoon coffee cup. A beautiful coffee cup with no robot anywhere in frame. And my personal favorite—a robot holding what appeared to be a coffee cup melted into a banana.

That last one gave the skill its name.

---

## The Problem I Was Solving

Image generation tools are everywhere now. DALL-E, Midjourney, Stable Diffusion. The technology works. So why was I burning hours on what should be a five-minute task?

Three problems kept recurring:

**Consistency.** Generate five images of the same character, get five different people. Need a series of illustrations for a blog post? Good luck making them look like they belong together.

**Text rendering.** Ask for a sign that says "OPEN"—get a sign that says "OEPN" or "OPNE" or some eldritch glyph that approximates letters. This was embarrassing. AI could generate photorealistic landscapes but couldn't spell a four-letter word.

**Context switching.** Every image meant leaving my terminal, opening a web app, downloading files, organizing folders. The cognitive tax was real. By the time I got the image, I'd lost the thread of what I was actually working on.

I built Nano Banana to solve all three.

---

## What Nano Banana Actually Does

The skill wraps [Google's Gemini 3 Pro Image model](https://ai.google.dev/) in an MCP server that lives inside Claude Code. No browser tabs. No file management. Just describe what you want, get what you asked for.

Four core capabilities:

**Generation:** Text-to-image at up to 4K resolution (5632×3072 pixels). Enough detail for print, not just web.

**Editing:** Modify existing images with natural language. "Make the sky more dramatic." "Remove the person in the background." "Change the season to winter."

**Iteration:** Keep refining. `continue_editing` remembers the last image, so "make it warmer" works without re-uploading.

**History:** Track all generated images in a session. Reference any previous generation for consistency.

---

## The SCTD Framework

This is the original prompting system I developed after generating hundreds of images. Most prompts fail because they're either too vague ("a nice picture") or too scattered (random details in random order).

SCTD structures every prompt:

```text
Subject → Context → Technique → Details
```

| Component | What It Does | Example |
|-----------|-------------|---------|
| **Subject** | Main focus | "A golden retriever puppy" |
| **Context** | Setting, environment | "in a sunlit meadow" |
| **Technique** | Style, medium | "oil painting style" |
| **Details** | Quality, mood, specs | "soft bokeh, warm tones, 4K" |

**Combined:**
> "A golden retriever puppy in a sunlit meadow, oil painting style, soft bokeh background, warm golden tones, 4K resolution"

The order matters. Subject first anchors the model's attention. Context grounds the scene. Technique sets expectations for rendering style. Details polish the output.

Most failed prompts I debugged were missing one component—usually Context or Technique. "A robot holding coffee" lacks both. "A humanoid service robot in a modern cafe kitchen, photorealistic product photography, clean white surfaces, soft studio lighting, 4K"—that works.

---

## Text That Actually Works

Gemini 3 Pro cracked the text rendering problem. I don't know exactly how—Google hasn't published the architecture details—but it consistently renders legible text when other models hallucinate.

This opened up use cases I'd given up on:

**Book covers.** Generate mockups with actual titles. "Book cover for 'THE MIDNIGHT GARDEN' in elegant serif typography, dark botanical illustration, silver foil accents, mysterious atmosphere."

**Signage.** "Vintage neon sign reading 'OPEN 24 HOURS' in pink and blue, rainy city street background, reflections on wet pavement, moody noir aesthetic."

**UI mockups.** "Mobile app screenshot showing a meditation timer at 14:32, minimal interface, dark mode, clean sans-serif font, subtle gradient background."

The key: keep text under 10 words. Quote the exact text you want. Specify font style. Three rules, consistently followed, consistently work.

---

## Character Consistency Across Images

This was the breakthrough that made the skill actually useful for content creation.

The `history` reference system lets you lock a character's appearance:

**First generation:**
> "Portrait of a 30-year-old woman named Sarah: auburn wavy hair shoulder length, green eyes with gold flecks, light freckles across nose and cheeks, warm smile with slight dimples, wearing a cream cable-knit sweater. Photorealistic, soft natural lighting."

**Subsequent scenes:**
> "Sarah from history:0 standing in a bookshop, browsing old leather-bound books, same outfit, afternoon light through window, same photorealistic style."

The model doesn't perfectly preserve every detail. But it gets close enough for a blog series, a presentation deck, a consistent visual narrative across multiple posts.

Three tips I learned:

1. **Overspecify the first generation.** Every distinctive feature you don't mention becomes a variable the model can change.
2. **Vary context, not character.** Change the setting, lighting, activity. Keep physical features and clothing constant.
3. **Reference explicitly.** "Sarah from history:0" works better than "the same woman."

---

## A Real Workflow

Here's how I actually used this while writing:

**Me:** "Generate an image for a blog post about AI tools—a human and a robot collaborating at a desk, warm lighting, modern office, watercolor illustration style, friendly and approachable mood."

**Result:** Clean watercolor-style illustration. Human and robot side by side, both clearly engaged with something on the desk. Warm orange tones. No melted-banana appendages.

**Me:** "The robot's arm looks stiff. Make the pose more natural, like they're pointing at something together."

**Result:** Same scene, adjusted pose. The robot's gesture now reads as collaborative rather than robotic.

**Me:** "Add a subtle laptop screen between them showing some kind of diagram."

**Result:** Laptop added, generic diagram visible. Maintains the watercolor style and warm tones from earlier.

Total time: maybe four minutes. And I never left the terminal. The images saved automatically to `~/Documents/nanobanana_generated/`. When I needed to add one to a post, the filepath was already in my clipboard.

---

## Where It Falls Short

The skill isn't magic. Limitations you should know:

**Complex scenes with many elements.** Ask for "a crowded marketplace with fifteen distinct vendors, each selling different products, with customers browsing, children playing, a musician in the corner"—and something will go wrong. The model handles 2-3 main subjects well. Beyond that, quality degrades.

**Precise spatial relationships.** "Put the coffee cup to the left of the laptop, with the phone between them" often doesn't parse correctly. The model understands "near" better than "left of."

**Matching specific real-world references.** "In the style of Monet's Water Lilies" gets you impressionistic water scenes. But it's inspired by, not faithful to, the actual paintings. For brand-accurate work, you'll need more specialized tools.

**Speed vs. quality tradeoff.** Gemini image generation produces the best results but takes 15-30 seconds per generation. If you're iterating rapidly, that adds up. For quick drafts, the Flash variant is faster at lower quality.

---

## Why This Matters Beyond Pictures

I thought I was building an image generation wrapper. I accidentally built a lesson about AI tool integration.

The skill works because it respects workflow. It lives where I work. It saves files where I expect them. It remembers context so I don't have to re-explain myself.

Most AI tools fail not because the AI is bad, but because the integration is bad. Brilliant model, terrible workflow. Powerful capability, wrong context.

Nano Banana taught me that the wrapper matters as much as the model. Sometimes more.

---

## Quality Checklist

Every image generation should pass:

**Coherence Test:** Do all elements look like they belong in the same image? Same style, same lighting, same level of detail?

**Text Test:** If there's text, is it legible? Does it say what you asked for?

**Consistency Test:** If this is part of a series, does it match previous generations?

**Usability Test:** Is the resolution high enough? Is the composition right for your use case (blog header vs. social thumbnail vs. print)?

**The Five-Second Test:** Would a viewer understand what this image is about within five seconds?

---

## Quick Start

```bash
# Get a free API key from Google AI Studio
# https://aistudio.google.com/ → Get API Key → Create API Key

# Add the MCP server to Claude Code
claude mcp add nano-banana --env GEMINI_API_KEY=your-key-here -- npx -y nanobanana-mcp

# Install the skill for prompting guidance
git clone https://github.com/leegonzales/AISkills.git
cd AISkills
cp -r NanoBanana/nano-banana ~/.claude/skills/
```

Then just ask:
- "Generate an image of [description]"
- "Edit this image to [change]"
- "Create a consistent character named [name] who is [description]"

The skill activates automatically when you request images.

---

## What I Learned Building This

Building Nano Banana taught me that AI capabilities and AI usability are different problems.

Gemini 3 Pro Image was already excellent before I wrapped it. What wasn't excellent was the experience of using it in my actual work. Download the image. Find the file. Remember what I was doing. Get back to writing.

The skill eliminated those steps. Not by improving the model—by improving the workflow around it.

Every AI tool you build should ask: where does this live in someone's actual work? Not where *could* it live. Where *should* it live to be effortless?

Tomorrow: Claimify—extracting golden insights from messy conversations.

---

*This is Day 2 of 12 Days of Original AI Skills—a series showcasing Claude Code skills I built from scratch to solve real problems.*
