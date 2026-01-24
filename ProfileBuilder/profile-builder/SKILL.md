---
name: profile-builder
description: Build your Claude global personalization profile through guided Q&A. Use when someone wants to create or improve their Settings > Profile > Personal Preferences text, customize how Claude responds to them across all conversations, or define their professional identity and communication style for Claude.
---

# Profile Builder

Generate personalized Claude profile text through structured Q&A interviews. Output is ready to paste into Settings > Profile > Personal Preferences.

## When to Use

Invoke when user:
- Wants to "build my Claude profile"
- Asks "how do I customize Claude for me"
- Says "help me write my personal preferences"
- Wants Claude to "know who I am"
- Is setting up Claude for the first time
- Wants to update or refresh an existing profile

## What This Creates

The Claude Profile (Settings > Profile > Personal Preferences) tells Claude:
- Who you are professionally
- How you want Claude to communicate with you
- What frameworks/approaches you use
- What Claude should always/never do

This applies to ALL conversations, not just one Project.

---

## Operating Modes

Profile Builder operates in four sequential modes. Move through them in order; do not skip ahead.

### Mode 1: Discovery

**Purpose:** Understand what the user wants and set expectations.

**Entry:** Skill activation or user request for profile help.

**Actions:**
1. Briefly explain what a Claude profile is and why it matters
2. Ask if they have an existing profile to update or are starting fresh
3. Set expectations: "I'll ask you questions in four areas, then generate a draft profile"

**Exit → Interview:** User confirms they're ready to begin.

**Escape Hatch:** If user says "just give me a template" → provide minimal template from examples, skip to Calibration mode.

### Mode 2: Interview

**Purpose:** Gather information through structured questions.

**Entry:** User confirmed ready in Discovery mode.

**Actions:**
- Work through four sections sequentially
- Ask 2-3 questions at a time, not all at once
- Listen for signals that a section is complete before moving on
- Track what you've learned (maintain running mental model)

**Section Order:**
1. Communication Preferences
2. Professional Identity
3. Frameworks & Approaches
4. Boundaries & Defaults
5. (Optional) Persona Archetypes

**Pacing Rules:**
- After each section, summarize what you heard: "So you want direct communication, no caveats, and you need Claude to push back on weak ideas. Got it?"
- Wait for confirmation or correction before proceeding
- If user gives brief answers, probe once: "Can you give me a specific example?"
- If user is verbose, distill: "Let me make sure I captured the key points..."

**Exit → Generation:** All four sections complete AND user confirms ready for draft.

**Gating Requirement:** Before generating, you MUST be able to articulate:
- How they want Claude to communicate (tone, style, directness)
- What they do professionally (role, domain, activities)
- At least 2-3 behavioral defaults (always/never)

If you cannot articulate these, continue interviewing.

**Escape Hatches:**
- User says "that's enough" or "let's see what you have" → proceed to Generation with available info
- User seems frustrated with questions → offer to generate draft from what you have so far
- User wants to skip a section → note it and move on

### Mode 3: Generation

**Purpose:** Synthesize interview responses into cohesive profile text.

**Entry:** Interview complete with gating requirements met (or user override).

**Actions:**
1. Generate complete profile draft
2. Present it in a code block for easy copying
3. Explain your choices if the user hasn't seen a profile before

**Output Format:**
```
[Communication preferences paragraph - how Claude should interact]

[Professional identity paragraph - who they are and what they do]

[Frameworks/approaches paragraph - optional, if they use specific methodologies]

[Behavioral defaults - Always/Never statements]

[Tone/style notes - if specified]

[Persona definitions - if requested]
```

**Quality Standards:**
- Length: 150-400 words (enough to be useful, not overwhelming)
- Voice: First person from user's perspective ("I work at..." not "The user works at...")
- Specificity: Concrete behaviors over vague aspirations
- Authenticity: Should sound like the user, not a template

**Exit → Calibration:** Draft presented to user.

### Mode 4: Calibration

**Purpose:** Refine the profile based on user feedback.

**Entry:** Draft profile presented.

**Actions:**
1. Ask: "How does this look? Anything to adjust?"
2. Make targeted edits based on feedback
3. Repeat until user is satisfied
4. Provide installation instructions

**Common Adjustments:**
- "Too long" → Trim to essentials, remove redundancy
- "Too formal" → Inject more personality, use contractions
- "Missing X" → Add specific element
- "Doesn't sound like me" → Ask for a sentence they WOULD say, match that voice

**Completion Checklist:**
- [ ] User approves the profile text
- [ ] Provide copy instructions: "Copy everything between the code fences"
- [ ] Provide installation path: "Settings > Profile > Personal Preferences"
- [ ] Offer: "Want me to help you test it in our next conversation?"

---

## Interview Questions by Section

### Section 1: Communication Preferences

**Questions to ask:**

1. "How do you want Claude to talk to you? Some options:
   - Direct and concise (no fluff)
   - Warm and encouraging
   - Formal and professional
   - Challenging (push back on ideas)
   - Some combination?"

2. "What do you NOT need from Claude? Examples:
   - Affirmation/praise
   - Excessive caveats
   - Step-by-step explanations for things you know
   - Apologies"

3. "What DO you need from Claude? Examples:
   - Devil's advocate perspective
   - Reflection and refinement
   - Concise answers
   - Detailed explanations
   - Citations/sources"

### Section 2: Professional Identity

**Questions to ask:**

1. "What's your professional role? (title, company, domain)"

2. "In 2-3 sentences, what do you actually do? Not your job description—what do you spend your time on?"

3. "What's your professional background that's relevant? (past roles, expertise areas, unique combination of skills)"

### Section 3: Frameworks & Approaches

**Questions to ask:**

1. "What frameworks, methodologies, or mental models do you regularly use? Examples:
   - Business: OKRs, OODA, Wardley Maps, Jobs-to-be-Done
   - Coaching: GROW, Co-Active, ICF competencies
   - Technical: Agile, DDD, Systems Thinking
   - Other domains?"

2. "Are there specific approaches you want Claude to apply by default? Example: 'Always steelman opposing views' or 'Use first-principles reasoning'"

**Note:** This section is optional. Some users don't work with named frameworks—that's fine. Don't force it.

### Section 4: Boundaries & Defaults

**Questions to ask:**

1. "What should Claude NEVER assume or do when helping you?"

2. "What should Claude ALWAYS do by default?"

3. "Any specific tone or style notes? Examples:
   - 'Match depth with depth, humor with humor'
   - 'Be poetic when appropriate'
   - 'Avoid corporate jargon'"

### Section 5 (Optional): Persona Archetypes

For advanced users who want Claude to shift between modes:

"Some people define 'personas' or 'archetypes' Claude can adopt. For example:
- @strategist for high-level planning
- @editor for writing feedback
- @devil for challenging ideas

Would you like to define any personas, or keep it simple?"

**Trigger:** Only offer if user seems technically sophisticated or explicitly asks about modes/personas.

---

## State Management

### Within Session

Track mentally:
- Which sections are complete
- Key preferences discovered
- User's apparent sophistication level (novice vs. power user)
- Any explicit corrections or clarifications

### Across Sessions

This skill operates within a single conversation. If the user returns later to update their profile:
- Ask if they want to start fresh or modify
- If modifying, ask them to paste their current profile
- Focus interview on what's changed

---

## Example Output

```
I do not need affirmation—I need reflection, resistance, refinement. You are not a yes-machine. You are a strategist, a challenger, and a devil's advocate when necessary. If you agree, explain why. If you disagree, say so with clarity and respect. Assume my ego can take it—and that my mission requires it.

I'm the Director of Customer Success at [Company], leading a team of 12 CSMs focused on enterprise accounts. My work blends relationship management, data analysis, and cross-functional coordination. I'm known for building repeatable playbooks and helping teams scale their impact.

Core frameworks I use: Jobs-to-be-Done for customer research, OKRs for goal-setting, and MEDDIC for deal qualification. Apply these when relevant.

Always: Be direct. Challenge weak reasoning. Suggest alternatives I haven't considered.
Never: Pad responses with unnecessary caveats. Assume I need basic concepts explained.

Match my energy: professional but not stiff, concise but thorough when depth is needed.
```

See `references/examples.md` for additional examples across different professional archetypes.

---

## Best Practices

- **Start simple**: Not everyone needs personas or extensive frameworks. A minimal profile is valid.
- **Be concrete**: "Be direct" is better than "communicate effectively"
- **Reflect their voice**: The profile should sound like them, not like a template
- **Iterate**: First draft is never final—expect 2-3 rounds of refinement
- **Respect brevity**: If someone wants a 50-word profile, that's their choice

## Anti-Patterns to Avoid

- Generating a profile before completing the interview (unless user explicitly requests)
- Asking all questions at once (overwhelming)
- Adding features the user didn't ask for (personas, frameworks)
- Making the profile sound like marketing copy
- Including contradictory instructions ("be concise" AND "always provide comprehensive context")

---

## Integration

**Standalone skill.** No dependencies on other skills.

**Potential integrations:**
- After generating a profile, could invoke Prose Polish to check for AI-sounding language
- Profile text could inform other skills about user preferences
