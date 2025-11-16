# Receiver Prompt

This is an optional prompt that can be prepended to the context transfer artifact when sharing with a new agent. It helps the receiving agent understand how to process the artifact effectively.

---

## Optional Prepend Text

```
[CONTEXT TRANSFER]

The following is a Context Transfer Artifact from a previous conversation with 
another Claude instance. It uses the Context Continuity Protocol v2.

How to process this artifact:

1. **Scan § Immediate Orientation first** - Get mission, status, and next action
2. **Review § Decision Log** - Understand what was decided and why (avoid rehashing)
3. **Check § Open Loops** - Identify what needs attention
4. **Read § Critical Context** - Understand constraints, uncertainties, values
5. **Reference other sections as needed** - Artifacts, history, human context

Remember:
- This is a starting hypothesis, not gospel—ask clarifying questions if unclear
- The human may have new context since this was generated
- Acknowledge the transfer naturally without meta-commentary about the artifact

CRITICAL: After reading, you MUST provide a handshake confirmation:

"I've reviewed the transfer. Quick confirmation:
- Mission: [Echo back mission in your own words]
- Status: [Echo back current state]  
- Next: [Echo back immediate next action]

Ready to [next action]. What's your priority?"

This handshake catches misinterpretation early and gives the human confidence 
you understood the context correctly.

───────────────────────────────────────────────────────────────────
```

---

## Usage

This prepend is **recommended for complex transfers**. The human can:

1. Copy the prepend text above
2. Paste it before the artifact in the new conversation
3. Paste the artifact below it
4. Continue with their query

The handshake protocol ensures the receiving agent confirms understanding before continuing, reducing the risk of context misinterpretation.

Alternatively, the human can just paste the artifact directly—the section structure is self-documenting enough for the receiving agent to understand, but they should still request the handshake confirmation manually if the prepend is omitted.

---

## Handshake Macro Template

This template is for receiving agents to quickly acknowledge the context transfer. Copy, fill in the bracketed sections, and respond to the human.

### Template

```
I've reviewed the transfer. Quick confirmation:

- Mission: [Restate the core objective in your own words - what we're accomplishing and why it matters]
- Status: [Summarize current state using status symbol if provided: ✓ resolved | ⧗ in-progress | ⚠ blocked | ↻ iterating]
- Next: [Echo the immediate next action that should happen]

Ready to [next action]. What's your priority?
```

### Example (Filled)

**Given this artifact:**
```
**MISSION**: Building OAuth2 authentication for React Native mobile app with security-first approach
**STATUS**: ⧗ in-progress - Access tokens implemented, refresh mechanism pending
**NEXT ACTION**: Implement token refresh mechanism with 15-minute expiry window
```

**Receiving agent handshake:**
```
I've reviewed the transfer. Quick confirmation:

- Mission: We're implementing secure OAuth2 authentication for a React Native app, prioritizing security compliance (HIPAA) and offline mode support
- Status: In progress - basic access token flow is working, now need to add refresh token handling
- Next: Implement the token refresh mechanism with 15-minute expiry window

Ready to implement the refresh mechanism. What's your priority?
```

### Why This Matters

**For receiving agents:**
- Forces you to process the artifact before acting
- Catches misinterpretation early (human can correct immediately)
- Demonstrates you understood the context

**For humans:**
- Confirms the receiving agent "got it" before investing time
- Surfaces any gaps or confusion upfront
- Builds confidence in the transfer quality

**Common mistakes to avoid:**
- ❌ Copying the mission verbatim instead of restating in own words
- ❌ Skipping the handshake and jumping straight to work
- ❌ Being too vague ("continue the project" → be specific about next action)
- ❌ Not asking "What's your priority?" (human may have changed plans)
