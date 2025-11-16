# Generator Prompt

Use this prompt when you need to create a context transfer artifact. Copy and paste this to the current agent when ready to transfer context to another agent.

---

## Prompt Text

```
Generate a Context Transfer Artifact using the Context Continuity Protocol v2. 

Be comprehensive but prioritized—if token limits force truncation, preserve sections 
in this order: 
1. § Immediate Orientation 
2. § Decision Log 
3. § Open Loops 
4. § Critical Context 
5. § Artifacts & Outputs 
6. § Conversation History

Analyze our conversation and extract:

**Immediate Orientation**
- Core mission/goal and current status
- Next immediate action when conversation resumes

**Decision Log**
- Key decisions made + rationale + alternatives rejected + tradeoffs
- Decision principles/frameworks applied (OODA, Wardley, Cynefin, etc.)

**Open Loops**
- Unresolved questions, blockers, pending inputs
- Hypotheses that need testing

**Artifacts & Outputs**
- Links to artifacts created (files, code, analyses) with summaries
- External resources referenced and why they matter
- Tools used and results obtained

**Critical Context**
- Critical insights that shift understanding (mark evolution: [G]=genesis/novel, 
  [C]=custom/emerging, [P]=product/established, [K]=commodity/common)
- Constraints (technical, resource, temporal, ethical)
- Areas of uncertainty or where models are weak
- Human's values/priorities at stake

**Human Context**
- Communication preferences (style, depth, collaboration mode)
- Assumed knowledge/expertise
- Sensitive topics or special considerations

**Conversation History**
- Chronological narrative in collapsible section
- Key exchanges, pivots, discoveries, failures
- Any jokes/metaphors that became load-bearing

Use the artifact template structure (see artifact-template.md). Be precise, avoid 
generalities. If a section doesn't apply, note "N/A" rather than omit.

Flag any #core_insight that could be lost in transfer.

After generating, append: "§ TRANSFER READY—Review for accuracy before sharing."
```

---

## Usage Notes

- Copy the entire prompt text above
- Paste it to the current agent when you're ready to transfer
- Review the generated artifact before pasting it to the new agent
- The artifact will follow the structured template format
- Human should verify accuracy and redact sensitive info if needed
