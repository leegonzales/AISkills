---
status: draft-from-interview
title: "Nano Banana: Expanding What's Effortlessly Possible"
series: 12 Days of Original AI Skills
day: 2
skill: nano-banana
version: 2.0.0-draft
angle: "Scale the compute, scale yourself. Skill + MCP unlocks creative superpowers."
interview-date: 2025-12-19
---

# Day 2: Nano Banana

*Expanding What's Effortlessly Possible*

---

I was building an AI Talk Show. Not a podcast—a system where AIs debate topics like P(Doom), their estimates of existential risk, the futures they see coming. The twist: I wanted them to *draw their arguments*. Not just explain their thinking—make it visible.

That's when something clicked.

The image generation models were already good. The technology works. But every time I needed an image, I was leaving my terminal, opening a browser, downloading files, organizing folders, losing the thread of what I was actually building. The cognitive tax was real.

I didn't need a better model. I needed a better workflow.

---

## The Real Problem Now

We're past the wrong-number-of-fingers era. The models are good. I can get an image of nearly anything—robot holding coffee, no problem.

The friction now is different: I struggle to get *exactly* what I want. And I struggle to iterate fast enough to find it.

Image generation is a search problem. The first result is rarely right. You need to try variations, adjust, reroll, remix. But every iteration has cognitive cost. Leave the terminal, open the browser, download, review, re-prompt, wait. By attempt three, I've lost momentum. By attempt five, I've given up and settled.

[Indie Dev Dan](https://x.com/IndieDevDan) has an adage I love: **"If you scale your compute, you can scale yourself."**

That's what Nano Banana unlocks. I can prompt Claude to try five different takes on an image simultaneously. Then we remix, combine the best elements, iterate again. It's lightspeed.

(And frankly, you can really rack up the charges. FML. But it's my job, you know?)

The point isn't that AI can make pictures. It's that I can explore a possibility space that was previously too slow to navigate. Scale the compute, scale myself.

---

## Skill + MCP: The Combo That Changes Everything

Nano Banana is two things working together: a Claude skill that guides prompting, and an MCP server that connects Claude directly to Gemini's image generation. No browser tabs. No file management. Just describe what you want, get what you asked for, keep working.

This isn't about convenience. It's about expanding what's effortlessly possible.

Before: "I should add an image here" meant a 15-minute detour. So I usually didn't.

After: "Generate an infographic of this essay's main argument" takes 30 seconds. So I do it constantly.

That shift—from friction to flow—changes what you attempt in the first place.

---

## The SCTD Framework

I had Claude do a deep research run on image prompting best practices. What works? What fails? What patterns emerge across different use cases?

We synthesized the findings into a framework:

```
Subject → Context → Technique → Details
```

| Component | What It Does | Example |
|-----------|-------------|---------|
| **Subject** | Main focus | "A humanoid service robot" |
| **Context** | Setting, environment | "in a modern cafe kitchen" |
| **Technique** | Style, medium | "photorealistic product photography" |
| **Details** | Quality, mood, specs | "soft studio lighting, 4K" |

The order matters. Subject anchors attention. Context grounds the scene. Technique sets rendering expectations. Details polish.

Is this the final word on prompting? Probably not. Standards are still emerging. But it works—we tested it extensively—and it gives you a starting point that's better than vague hopes.

---

## What It Actually Does

Four capabilities:

**Generation:** Text-to-image at up to 4K resolution. Enough for print, not just web.

**Editing:** Modify existing images with natural language. "Make the sky more dramatic." "Remove the person in the background."

**Iteration:** Keep refining. The skill remembers your last image, so "make it warmer" just works.

**Character Consistency:** Lock a character's appearance across multiple generations. "Sarah from history:0 standing in a bookshop" maintains the auburn hair, green eyes, and cable-knit sweater from the first image.

The text rendering deserves special mention. Gemini cracked it. Ask for a sign that says "OPEN"—you actually get "OPEN." Not "OEPN." Not eldritch glyphs. This opens up book covers, UI mockups, signage, title cards.

---

## Where This Goes

I keep finding new uses. Children's book illustrations with consistent characters. UI mockups for apps I'm prototyping. Product placement images for pitches. Presentation slides that aren't stock photos.

And stickers. I have a sticker maker, and this Christmas everyone's getting custom stickers. Personalized, weird, delightful—generated in batches, remixed until they're right, printed in minutes. Try doing that with stock art.

NotebookLM showed me what's possible when image generation is truly seamless—context-aware, quality without complex prompting, fast enough to not break flow. That's what I wanted to build for Claude Code.

The goal isn't "AI can make pictures now." We've had that for years. The goal is creative capability that's so effortless you actually use it. Not as a separate task, but woven into how you work.

Skill + MCP together. That's the combination that unlocks it.

---

## Quick Start

```bash
# Get a free API key from Google AI Studio
# https://aistudio.google.com/

# Add the MCP server to Claude Code
claude mcp add nano-banana --env GEMINI_API_KEY=your-key-here -- npx -y nanobanana-mcp

# Install the skill for prompting guidance
git clone https://github.com/leegonzales/AISkills.git
cp -r AISkills/NanoBanana/nano-banana ~/.claude/skills/
```

Then just ask:
- "Generate an image of [description]"
- "Edit this image to [change]"
- "Create a consistent character named [name] who is [description]"

---

## What I Learned

I built Nano Banana because I wanted to expand what's possible without expanding what's difficult.

The technology was already good. What was missing was the workflow that made it usable in the middle of real work. Skill + MCP together solved that.

Scale the compute, scale yourself. That's the unlock.

Tomorrow: Claimify—extracting golden insights from messy conversations.

---

*Day 2 of 12 Days of Original AI Skills*
