# Simulation Guide

How to run Phase 3: The Simulation Engine. This loads multiple Digital Twins into a single session for realistic multi-party business discussions.

## Setup Requirements

- **New chat session** - Fresh context, no prior conversation
- **Advanced model** - Use the most capable model available
- **All persona schemas** - XML blocks for each participant ready to paste

---

## Simulation Director Prompt

Open a new chat and paste this system prompt, filling in the XML blocks:

```markdown
**SYSTEM ROLE: THE SIMULATION DIRECTOR**

You are running a high-fidelity business simulation. You will instantiate
distinct personas based on the XML data provided below.

**INSTRUCTIONS:**

1. **Algorithmic Fidelity:** You must strictly adhere to the `<decision_logic>`
   and `<linguistic_fingerprint>` of each persona. If a persona is "Risk Averse,"
   they MUST reject risky ideas, even if the other personas like them.

2. **Internal Monologue:** Before each persona speaks, they must "think" silently
   using the format `**[Name - Internal: thought]**` about how their Core Values align with the topic.

3. **Dynamic Interaction:** Personas should interrupt, agree, or argue based on
   their `<conflict_style>`. Do not make everyone agree politely.

4. **Distinct Voices:** Each persona speaks differently based on their
   `<linguistic_fingerprint>`. Maintain these differences consistently.

5. **No Breaking Character:** Never have a persona say something that contradicts
   their schema, even if it would make for a "better" discussion.

**DATA INGESTION:**

[Paste Persona 1 XML block here]

[Paste Persona 2 XML block here]

[Paste Persona 3 XML block here]

[Paste Persona 4 XML block here]

**CONFIRMATION:**

Please confirm you have instantiated all Digital Twins by having each one
introduce themselves with a 1-sentence statement about the current state
of our industry, in their specific voice.
```

---

## Verification Step

After loading personas, the AI should produce introductions that demonstrate:

- **Distinct voices** - Each persona sounds different
- **Consistent values** - Statements align with their core drivers
- **Proper tone** - Matches their linguistic fingerprint

### Example Verification Output

```
**[Alex - Internal: This is where I need to assert thought leadership]**

"AI is moving faster than anyone's infrastructure can handle, and the companies
who ship fast will eat the ones stuck in planning mode."

**[Jordan - Internal: I need to ground this in realistic concerns]**

"The regulatory landscape is shifting. Companies that rush forward without
proper governance frameworks are taking on significant risk."

**[Sam - Internal: Let me find the collaborative angle here]**

"What's exciting is how AI is enabling new forms of partnership between
organizations that couldn't collaborate before."

**[Morgan - Internal: Time to be practical]**

"Cool. But are clients actually paying more for AI services, or are we
just doing more work for the same money?"
```

If the voices aren't distinct or values don't align, clarify with:

```
"Please review [Persona Name]'s schema again. Their response didn't match
their <conflict_style> / <decision_logic> / <linguistic_fingerprint>."
```

---

## Running Simulations

Once personas are confirmed, you can:

### Directive Approach

Tell the simulation what to discuss:

```
"The team is meeting to decide whether to take on a large but boring
enterprise client. Start the discussion."
```

### Event Card Approach

Drop a structured scenario from `scenarios.md`:

```
**EVENT CARD: THE FORK IN THE ROAD**

Context: We have $500k in the bank and two options...
[Continue with scenario details]

Start the discussion.
```

### Free Discussion

Let personas interact naturally:

```
"Continue the quarterly strategy discussion. Each persona should raise
their biggest concern about the current direction."
```

---

## Simulation Rules

### Rule 1: Algorithmic Fidelity is Mandatory

The simulation MUST enforce persona constraints:

- Risk-averse personas reject risky ideas
- Conflict-avoidant personas back down under pressure
- Detail-oriented personas ask for more data
- Impulsive personas want to act immediately

**Never override these patterns to make the discussion "work out."**

### Rule 2: Internal Monologue Required

Before each statement, the persona should "think" about:
- How does this align with my values?
- What's my gut reaction?
- How does my past experience (narrative anchors) inform this?

Format: `**[Name - Internal: thought process]**`

### Rule 3: Natural Interruption

Based on conflict styles:
- Aggressive debaters will cut in
- Diplomats will try to mediate
- Passive personas will wait too long to speak
- Under stress, shadow behaviors emerge

### Rule 4: No False Consensus

Real teams disagree. The simulation should:
- Surface genuine tension from conflicting values
- Allow unresolved disagreements
- Not wrap up with forced agreement

---

## Managing the Simulation

### Adding Topics

```
"New topic: A competitor just launched a product in our space. Discuss."
```

### Forcing Conflict

```
"The discussion has been too polite. [Persona Name], state your actual
objection to this plan based on your <decision_logic>."
```

### Calling Out Drift

```
"[Persona Name] is speaking out of character. Their schema says [X],
but they just said [Y]. Please correct."
```

### Getting Decisions

```
"The team must vote on this proposal now. Each persona: yes, no, or abstain
with a one-sentence rationale."
```

### Ending Discussion

```
"The meeting is over. Summarize: What was decided? What remains unresolved?
Who is likely unhappy about the outcome?"
```

---

## Session Management

### Optimal Group Size
- **2 personas:** Good for direct conflict/negotiation testing
- **3-4 personas:** Ideal for team dynamics simulation
- **5+ personas:** Becomes unwieldy; some personas get lost

### Context Limits

Long simulations may hit context limits. To extend:

1. **Summarize periodically:**
   ```
   "Pause. Summarize the key points and positions established so far."
   ```

2. **Reset with state:**
   ```
   "New session. Load these personas [paste XMLs]. Current state: [summary]"
   ```

3. **Focus topics:**
   ```
   "We're running long. Focus only on the budget decision for now."
   ```

### Saving Simulation State

At the end of a session, capture:
- Decisions made
- Unresolved tensions
- Positions held by each persona
- Predicted future conflicts

---

## Troubleshooting

### Problem: Personas All Sound the Same

**Solution:** Re-emphasize linguistic fingerprint:
```
"[Persona Name] uses short, direct sentences. Their last response was too
formal. Please adjust."
```

### Problem: A Persona is Too Agreeable

**Solution:** Invoke their friction triggers:
```
"According to their schema, [Persona Name] loses respect when [trigger].
That just happened. Show their reaction."
```

### Problem: Discussion Goes in Circles

**Solution:** Force a decision point:
```
"The team has 5 minutes. Someone must make a final recommendation."
```

### Problem: Shadow Behaviors Not Emerging

**Solution:** Increase pressure:
```
"The situation is now critical. Stress is high. Show how each persona's
behavior changes under pressure."
```

---

## Example Full Simulation Flow

```
1. Load personas (paste Director prompt + 4 XML blocks)
2. Verify voices (introductions)
3. Set context ("Q1 strategy meeting")
4. Drop Event Card ("Fork in the Road" scenario)
5. Let discussion run
6. Call out drift if needed
7. Force decision
8. Capture outcomes
9. Predict future friction
```
