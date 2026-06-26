---
name: silicon-doppelganger
description: Build psychometrically accurate personal proxy agents for the PAIRL Conductor system. Extracts personality, decision heuristics, and values into portable schemas that enable AI agents to negotiate, filter, and act on a principal's behalf.
---

# Silicon Doppelganger

Build high-fidelity personal proxy agents ("Digital Twins") using structured personality extraction and psychometric encoding. These proxies serve as "spokes" in the PAIRL Conductor hub-and-spoke architecture, negotiating and filtering on behalf of their principals.

## When to Use

Invoke when user:
- Wants to create a personal proxy agent for automated task negotiation
- Needs to build a Digital Twin for PAIRL Conductor integration
- Is extracting personality/decision patterns for AI representation
- Wants to validate a proxy agent against real behavior
- Asks to create a "digital twin," "proxy agent," or "personal AI representative"

## Core Concept

A Silicon Doppelganger is NOT just a simulation for entertainment — it's a **functional proxy** that can:
- Accept or reject tasks based on encoded values
- Negotiate with other agents on scheduling and resource allocation
- Protect the principal's time, energy, and boundaries
- Make low-stakes decisions autonomously within defined guardrails

The persona schema acts as a "save file" that maintains fidelity across sessions and systems.

## Fidelity Firewall (READ FIRST — non-negotiable)

A proxy that confabulates is worse than no proxy: it misrepresents a real person to other agents and to the Conductor, with their name on it. The single most damaging failure mode of this skill is **inventing persona content the principal never gave you** — the persona equivalent of a fabricated citation. Treat thin interview data as a gap to flag, never a blank to fill.

**Rule 1 — Every field traces to source data.** Every quote, CliftonStrength, VIA strength, value, core driver, fear, decision rule, blind spot, origin story, and biographical detail in the schema MUST trace to actual interview transcript or source material the principal provided. You may paraphrase and organize what they said; you may NOT:
- Invent a quote the person never said (no fabricated "actual phrases").
- Assign a CliftonStrength or VIA strength they did not report. If they did not take the assessment, the field is empty — do not guess "Strategic" from vibes and present it as a measured result.
- Construct an origin story, formative failure, or shadow-self behavior they never described.
- Infer a primary motivation/fear and state it as fact when the interview never surfaced it.

**Rule 2 — On thin input, mark the gap; do not fill it.** When a field has no supporting data, write exactly `[insufficient data — needs interview]` (optionally naming the missing question, e.g. `[insufficient data — needs Q3.1 origin story]`). A sparse, honest schema with five filled fields and ten gap markers is a CORRECT output. A rich, plausible, fabricated schema is a FAILED output. Never pad a schema to look complete.

**Rule 3 — Distinguish observed from inferred.** If you draw a reasonable inference from what the principal said (e.g., risk tolerance from a story), tag it as inference, not direct report: `[inferred from Q2.3 answer — confirm with principal]`. Inferences are allowed; inferences disguised as quotes or assessment results are not.

**Rule 4 — No validation theater.** Do NOT state a validation accuracy percentage (e.g., "80%+ match," "92% accuracy") unless you have actually run a predict-vs-ground-truth question battery and counted the results. If no battery was run, the validation status is literally **"not yet validated."** A target ("aim for 80%+") is a goal, never a claim — never report an aspirational target as an achieved score.

**Self-audit before output.** Before emitting any schema, scan every populated field and ask: *"Can I point to the exact interview answer this came from?"* If not, replace it with a gap marker. If asked to deploy a proxy that still contains gap markers in `must_reject`/`must_protect` or unvalidated status, surface that to the principal rather than proceeding silently.

## Core Workflow

### Phase 1: Extraction (Data Collection)

Interview the principal individually (45-60 min):

1. **Hardware** — Collect psychometrics
   - CliftonStrengths (Top 5-10) — record only if the principal reports them; do NOT infer
   - VIA Character Strengths (Top 5-10) — record only if reported; do NOT infer
   - Communication samples (emails, Slack) for linguistic fingerprint
   - If the principal has no formal assessments, leave those fields as `[insufficient data — no assessment provided]` and rely on behavioral signals instead. Never substitute a guessed strength for a reported one.

2. **Operating System** — Map decision heuristics
   - "Good work" definition (profit vs. meaning)
   - Friction triggers (instant respect-loss behaviors)
   - Risk tolerance (guaranteed vs. volatile)
   - Information preferences (data vs. prototype vs. trusted expert)

3. **Narrative Identity** — Capture the soul
   - Origin story (formative failure/crisis → lesson enforced)
   - Shadow self (behavior under extreme stress)
   - Unpopular opinions (beliefs held against consensus)

See `references/extraction-protocol.md` for full interview script.

### Phase 2: Encoding (Persona Schema)

Compile interview data into structured XML persona profile:

```xml
<persona_profile>
    <name>Principal Name</name>
    <psychometrics>
        <clifton>Top 5 CliftonStrengths</clifton>
        <via>Top 5 VIA Character Strengths</via>
    </psychometrics>
    <linguistic_fingerprint>Syntax, tone, vocabulary patterns</linguistic_fingerprint>
    <core_drivers>
        <primary_motivation>Impact | Security | Novelty | Money</primary_motivation>
        <primary_fear>Irrelevance | Boredom | Conflict | Poverty</primary_fear>
    </core_drivers>
    <decision_logic>
        <risk_tolerance>Low | Medium | High + context</risk_tolerance>
        <data_preference>Ranked: Data | Prototype | Trusted Expert</data_preference>
        <ethical_filter>Hard constraints (Kantian test, etc.)</ethical_filter>
        <decision_sequencing>Pattern: OBSERVE → TRY → ESCALATE → EXIT</decision_sequencing>
        <blind_spots>Known biases and limitations</blind_spots>
    </decision_logic>
    <conflict_style>Debater | Diplomat | Passive | Controller + stress behavior</conflict_style>
    <narrative_anchors>
        <origin_story>Formative event and lesson</origin_story>
        <shadow_self>Behavior under extreme stress</shadow_self>
    </narrative_anchors>
    <agent_rules>
        <must_reject>Hard no categories</must_reject>
        <must_protect>Non-negotiable boundaries</must_protect>
        <should_prefer>Weighted preferences</should_prefer>
    </agent_rules>
</persona_profile>
```

See `references/persona-schema.md` for full schema specification.

### Phase 3: Validation (Behavioral Testing)

Test the proxy against real principal behavior:

1. **Question Battery** — Present scenarios with multiple-choice responses
2. **Simulant Prediction** — Proxy predicts principal's choice with reasoning
3. **Ground Truth** — Principal answers independently
4. **Refinement** — Mismatches reveal schema gaps → update schema

**Target (a goal, not a claim): aim for 80%+ accuracy on lenient match** (correct answer OR acceptable alternative). This is the bar you are working toward — it is NOT a number you may report until you have actually run the battery and counted matches. Until a battery has been run and scored, the validation status is **"not yet validated."** See Fidelity Firewall Rule 4.

See `references/simulation-guide.md` for validation methodology.

### Phase 4: Agent Integration (PAIRL Deployment)

Deploy the Digital Twin as a spoke in the PAIRL Conductor system:

1. **Agent Rules Block** — Define must_reject, must_protect, should_prefer
2. **Conductor Registration** — Register proxy with central Conductor
3. **Integration Points** — Connect to calendar, email, task systems
4. **Negotiation Protocol** — Define how proxy communicates with Conductor

```xml
<agent_rules>
    <must_reject>
        - Work that fails Kantian universalizability test
        - Commitments to untrustworthy parties
        - Tasks that compromise craft for speed
    </must_reject>
    <must_protect>
        - Deep work blocks for strategic thinking
        - Time for learning and skill-building
        - Energy reserves (watch for exhaustion patterns)
    </must_protect>
    <should_prefer>
        - Projects with learning value and future leverage
        - Work with high-trust collaborators
        - Novel challenges over routine optimization
    </should_prefer>
    <negotiation_notes>
        - Weight trusted expert recommendations heavily
        - Values conscious renegotiation over silent commitment-breaking
    </negotiation_notes>
</agent_rules>
```

See `references/agent-integration.md` for deployment guide.

## Use Cases

### Primary: Personal Proxy Agent
Build a spoke for PAIRL Conductor that represents you in automated workflows:
- Task acceptance/rejection based on values and bandwidth
- Calendar negotiation with other agents
- Filtering incoming requests before they reach you

### Secondary: Team Simulation
Load multiple proxies to forecast team dynamics:
- Predict partnership friction before it happens
- Test strategic decisions against personality profiles
- Surface unspoken tensions and misalignments

### Tertiary: Self-Knowledge Tool
The extraction process itself is valuable:
- Articulate your own decision patterns
- Surface blind spots and shadow behaviors
- Create documentation of "how I work" for collaborators

### Quaternary: Voice Calibration for Writing
The persona schema enhances **WritingPartner** skill:
- Linguistic fingerprint guides prose generation
- Core drivers inform topic framing and argument structure
- Decision logic shapes how claims are stated
- Psychometrics provide authenticity markers

See WritingPartner skill for collaborative essay writing with voice calibration.

## Key Principle

**Token-efficient persona encoding prevents AI drift.** The XML schema is a portable "save file" that maintains character consistency across:
- Different chat sessions
- Different AI models
- Different deployment contexts (simulation vs. agent proxy)

The schema is the source of truth. All behaviors derive from it.

## Output Artifacts

| Artifact | Purpose |
|----------|---------|
| `{name}-persona-schema.xml` | Core Digital Twin (Conductor-ready) |
| `{name}-origin-story.md` | Full narrative identity |
| `{name}-extraction-checkpoint.md` | Heuristics and status |
| `evals/questions/*.md` | Validation question sets |
| `evals/simulant-responses/*.md` | Proxy predictions with reasoning |

## Quality Checklist

Before deploying a proxy:

- [ ] **Traceability (Fidelity Firewall)** — Every populated field traces to a specific interview answer; no field is fabricated or inferred-as-fact
- [ ] **Gaps Marked, Not Filled** — Fields without source data carry `[insufficient data — needs interview]`, not invented content
- [ ] **Specificity** — No generic traits; all based on interview data
- [ ] **Quotes Are Real** — Any quoted phrase is verbatim from the principal; if none were captured, the quote fields are gap-marked (do NOT manufacture a quote to satisfy this item)
- [ ] **Inferences Tagged** — Inferred fields are labeled `[inferred — confirm with principal]`, not presented as direct report
- [ ] **Contradictions Noted** — Observed conflicts documented
- [ ] **Stress Behavior** — Shadow self described from what the principal reported (or gap-marked)
- [ ] **Linguistic Detail** — Enough to generate realistic dialogue, derived from actual communication samples
- [ ] **Decision Rules** — Clear enough to predict choices
- [ ] **Agent Rules** — Must_reject, must_protect, should_prefer defined (gap-marked if interview did not cover them)
- [ ] **Validation Status Honest** — Either a real battery was run and the score reported with its count, OR status reads "not yet validated." No aspirational percentages.

## Related Skills

| Skill | Integration |
|-------|-------------|
| **WritingPartner** | Uses persona schema for voice calibration in collaborative writing |
| **prose-polish** | Can validate that generated text matches linguistic fingerprint |

## Example: SiliconDoppelgangerActual

For a complete implementation, see the **SiliconDoppelgangerActual** project—the authoritative instantiation of this methodology:
- 58KB persona schema (XML)
- 95 validation questions with 40 schema refinements
- Integration ready for PAIRL Conductor

> **"Actual"** — The validated, deployed Digital Twin. Your own instantiation would be your "Actual."

SiliconDoppelgangerActual demonstrates the full extraction → encoding → validation → deployment workflow.
