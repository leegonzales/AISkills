# Tier Mapping -- Prose Polish Redline

Defines the 5 quality tiers, their scope, which agents operate on each, and how conflicts between tiers are resolved.

---

## Tier Priority Order

Higher-priority tiers win conflicts with lower-priority tiers. Fix the bones before fixing the skin.

| Priority | Tier        | Color              | Hex       | Focus                                    |
|----------|-------------|--------------------|-----------|------------------------------------------|
| 1 (highest) | STRUCTURAL | Blue            | `#2b6cb0` | Organization, section flow, information architecture |
| 2        | COHERENCE   | Teal               | `#319795` | Logic, transitions, causal flow          |
| 3        | AUTHORITY   | Purple             | `#6b46c1` | Expertise signals, institutional voice, stakes |
| 4        | CRAFT       | Orange             | `#dd6b20` | Rhythm, precision, density               |
| 5 (lowest) | VOICE     | Green              | `#38a169` | Personality, perspective, distinctiveness |

---

## Tier Definitions

### 1. STRUCTURAL (Blue)

**What it measures:** Does the document's organization serve the reader? Are sections in the right order? Is information architecture sound?

**Scope:** Section-level and document-level edits. Moving, merging, or splitting sections. Reordering arguments. Adding or removing entire blocks.

**Phase:** 1 (Structural)

**Primary agents:** coherence-agent (section-level edits)

**Examples:**
- Moving a "prerequisites" section before a "how-to" section
- Merging two sections that cover the same ground
- Reordering arguments from weakest-to-strongest into strongest-first
- Removing a section that repeats earlier content

**When NOT to use:** Sentence-level logic fixes (use COHERENCE). Word-level changes (use CRAFT or VOICE).

---

### 2. COHERENCE (Teal)

**What it measures:** Does logic flow within and across paragraphs? Are transitions earned? Are causal claims sound? Is every detail doing work?

**Scope:** Sentence-level and paragraph-level edits within sections. Logical repairs, transition fixes, removal of decorative specificity.

**Phase:** 1 (Structural)

**Primary agents:** coherence-agent (sentence-level edits)

**Key katas:**
- `coherence-logic-flow` -- Do ideas connect across paragraphs?
- `coherence-transitions` -- Are transitions earned, not mechanical?
- `coherence-causal` -- Do cause-effect claims hold?
- `coherence-decorative` -- Is every specific detail functional?
- `coherence-floating-claims` -- Are bold assertions grounded?

**Detection questions:**
1. If I remove transitions, do ideas still connect?
2. Could I swap paragraphs without changing meaning? (Bad if yes)
3. Is every specific detail doing work?
4. Would a hostile reader find logical gaps?

---

### 3. AUTHORITY (Purple)

**What it measures:** Is expertise demonstrated rather than claimed? Are stakes visible? Is authority earned, delegated, or false?

**Scope:** Replacing institutional voice with speaker. Grounding claims with evidence or experience. Adding vulnerability and stakes.

**Phase:** 1 (Structural)

**Primary agents:** authority-agent, claims-agent, stakes-agent

**Key katas:**
- `authority-delegated` -- "Research shows" without citation or demonstration
- `authority-institutional` -- "It is recommended" passive hiding
- `authority-generic` -- Stereotypes as insider knowledge
- `authority-stakes` -- Missing skin in the game
- `authority-false-precision` -- "This underscores" meta-commentary

**Authority types:**
- **Earned:** Insider details, vulnerability, consequences for being wrong
- **Delegated:** Citations without synthesis, institutional voice, numbers without interpretation
- **False:** Stereotypes as expertise, generic specificity, authority cosplay

---

### 4. CRAFT (Orange)

**What it measures:** Does the prose have rhythm? Is information density varied? Are hedges classified correctly? Is language precise?

**Scope:** Sentence-level rhythm, hedge removal/preservation, word-level precision, density variation.

**Phase:** 2 (Stylistic)

**Primary agents:** rhythm-agent, hedge-agent

**Key katas:**
- `rhythm-variance` -- Sentence length variation serves meaning
- `rhythm-density` -- Information density varies strategically
- `hedge-cowardly` -- Opinion-avoidance hedges removed
- `hedge-protective` -- Epistemic-honesty hedges preserved
- `craft-precision` -- Vague words replaced with specific ones
- `craft-impersonal` -- "It is worth noting" and similar removed

**Hedge classification:**
- **Cowardly (penalize):** "Some might say," "It could be argued," "somewhat," "fairly," "rather"
- **Protective (preserve):** "The evidence suggests," "Current research indicates," "appears to," "likely"

---

### 5. VOICE (Green)

**What it measures:** Is there a recognizable author? Does the writing feel embodied? Is personality calibrated to genre?

**Scope:** Adding controlled informality, perspective injection, sensory grounding, personality markers.

**Phase:** 2 (Stylistic)

**Primary agents:** personality-agent, perspective-agent

**Key katas:**
- `voice-personality` -- Controlled informality, authorial presence
- `voice-perspective` -- Position-taking, first person, disputable claims
- `voice-embodiment` -- Sensory or experiential grounding
- `voice-register` -- Appropriate formality for genre

**Calibration warning:** "LinkedIn Influencer" overcorrection is worse than neutral prose. Voice additions must be genre-appropriate.

---

## Phase-to-Tier Mapping

| Phase | Tiers                              | Principle |
|-------|------------------------------------|-----------|
| 1 -- Structural (The Editor) | STRUCTURAL, COHERENCE, AUTHORITY | Fix logic and authority before touching style |
| 2 -- Stylistic (The Writer)  | CRAFT, VOICE                     | Refine rhythm, commitment, and voice |

**Why this order:** A polished logical fallacy is still a fallacy. Phase 1 fixes must complete before Phase 2 begins.

---

## Conflict Resolution Rules

When two edits target overlapping text:

1. **Higher-tier wins.** A COHERENCE edit always beats a CRAFT edit on the same text.
2. **Within same tier, higher severity wins.** MUST_FIX beats SHOULD_FIX.
3. **Within same tier and severity, Phase 1 beats Phase 2.** Structural edits take precedence.
4. **True conflicts (same tier, severity, phase):** Flagged for human review in the merge report.

The merge engine applies edits top-down by tier priority, skipping any edit whose `original_text` has already been modified by a higher-priority edit.
