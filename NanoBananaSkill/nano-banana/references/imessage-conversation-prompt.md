# iMessage Conversation Screenshots

Generate realistic iPhone text message conversation images for social media posts.

## The Two-Step Method

**Key insight:** Generating text-heavy images in one shot often produces typos or garbled text. The solution is to generate a blank template first, then edit to add the exact text you want.

### Step 1: Generate Blank Phone Template

```
Photorealistic iPhone 15 Pro screenshot showing a blank iMessage conversation screen.
Contact name "[NAME]" at top with back arrow, profile circle with "[INITIAL]" initial.
Standard iOS Messages interface with white/light gray background.

The message area is completely empty - no messages yet, just the blank conversation
ready for messages to appear.

Show the full phone screen from status bar at top (time, signal, battery) to the
iMessage input bar at bottom (camera icon, text field saying "iMessage", microphone icon).

Clean, realistic iOS interface. Vertical 9:16 format, high resolution.
```

**Asset available:** `assets/iphone-imessage-blank-template.png` (contact name "Alex")

### Step 2: Edit to Add Messages

Use `gemini_edit_image` with detailed message instructions:

```
Add iMessage conversation bubbles filling the white message area.
Keep the phone frame, header, and input bar exactly the same.

Add these messages in order from top to bottom:

GRAY BUBBLE (left): "[Their message 1]"
BLUE BUBBLE (right): "[Your response 1]"
GRAY BUBBLE (left): "[Their message 2]"
BLUE BUBBLE (right): "[Your response 2]"
[... continue ...]

Standard iOS message bubble styling. Gray bubbles left-aligned, blue bubbles right-aligned.
Fill the screen with messages.
```

## Best Practices

### Text Accuracy
- Be explicit about exact wording in the edit prompt
- List messages in order with GRAY/BLUE labels
- Include emoji if desired: `"the second one 😬"`

### Visual Consistency
- Use the same blank template for multi-screen carousels
- Both screens will have identical phone frames
- Enables splitting long conversations across multiple images

### Natural Conversation Flow
- Use casual texting language (lowercase, short messages)
- Include realistic back-and-forth rhythm
- Add timestamps between message groups if needed
- End with "Delivered" or "Read [time]" for realism

### Screen Density
- Aim for 8-12 message bubbles per screen
- Don't overcrowd - leave breathing room
- Split into multiple screens for longer conversations

## Use Cases

- **LinkedIn carousel posts** — conversation that tells a story
- **Product marketing** — customer testimonial conversations
- **Educational content** — Q&A format explanations
- **Event promotion** — friend inviting friend to event (natural CTA)

## Example: Event Promotion Conversation

**Screen 1 (Problem):**
- Friend venting about work frustration
- You asking diagnostic questions
- Identifying the real issue

**Screen 2 (Solution + CTA):**
- You explaining what to do
- Friend asking follow-ups
- You: "just come to my talk next week"
- Event details in a message
- Friend: "I'll be there"

This format works because it:
1. Opens with relatable pain point
2. Builds credibility through helpful dialogue
3. Lands CTA naturally (not salesy)
4. Shows social proof (friend is convinced)
