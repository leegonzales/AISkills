# Example Skill Extractions

Real examples of conversation patterns transformed into reusable skills.

---

## Example 1: Weekly Update Writer

### Original Conversation Pattern

**User kept saying:**
> "Here are my notes from this week: [bullet points]. Turn this into a weekly update email for my skip-level."

**Claude's successful response pattern:**
- Organized into Accomplishments / In Progress / Blockers
- Rewrote bullets as outcomes, not activities
- Added stakeholder-appropriate context
- Flagged items needing decisions

### Extracted Skill

```markdown
---
name: weekly-update-writer
description: Transform meeting notes into stakeholder update emails. Use when asked to "write my weekly update," "summarize this week," or turn notes into an update.
---

# Weekly Update Writer

Transform raw notes into polished stakeholder updates.

## Workflow

1. Organize inputs into Accomplishments, In Progress, Blockers
2. Rewrite bullets as outcome-focused statements
3. Add context for stakeholders not in the weeds
4. Flag items needing escalation

## Input Required

- Raw notes from the week (bullet points fine)
- Audience (team, skip-level, executives)

## Output Format

Email with:
- Subject line
- Brief intro (1-2 sentences)
- Accomplishments (3-5 bullets)
- In Progress (2-4 bullets)
- Blockers with clear asks (0-3 bullets)

Length: 150-250 words
Tone: Professional but personable

## Example

### Input
- finished API migration
- met with design team
- blocked on prod database access
- code review taking forever

### Output

**Subject: Weekly Update - API Migration Complete 🎉**

Hi team,

Quick update on this week's progress:

**Accomplishments**
- ✅ **Completed API migration** — all endpoints now on new infrastructure
- Aligned with design team on Q2 dashboard redesign

**In Progress**
- Finishing code reviews for auth module (EOD Friday)

**Blockers**
- ⚠️ **Need prod database access** — waiting on IT ticket #4521

## Quality Criteria

**Good:** Leads with wins, uses outcomes not activities, clear asks for blockers
**Avoid:** Burying the lede, too much detail, missing context
```

---

## Example 2: Feedback Theme Analyzer

### Original Conversation Pattern

**User kept saying:**
> "Here's a bunch of customer feedback: [pasted feedback]. What themes do you see?"

**Claude's successful response pattern:**
- Grouped feedback into themes
- Counted frequency of each theme
- Pulled representative quotes
- Recommended actions

### Extracted Skill

```markdown
---
name: feedback-theme-analyzer
description: Analyze feedback collections to identify themes, sentiment, and actionable insights. Use when asked to "find themes," "analyze this feedback," or "what patterns do you see."
---

# Feedback Theme Analyzer

Identify recurring themes and insights from feedback collections.

## Workflow

1. Read all feedback items
2. Identify recurring themes (positive and negative)
3. Quantify frequency
4. Extract representative quotes
5. Generate recommendations

## Input Required

- Collection of feedback (any format)
- Optional: Specific questions to answer
- Optional: Product/service context

## Output Format

| Section | Content |
|---------|---------|
| Summary | 3 sentences max |
| Themes | Table with frequency and sentiment |
| Quotes | Representative evidence |
| Recommendations | Prioritized actions |

## Example

### Input
[12 app store reviews]

### Output

## Summary
Users love core features but are frustrated by login issues and slow performance. Login problems mentioned most (5/12).

## Themes

| Theme | Count | Sentiment |
|-------|-------|-----------|
| Login issues | 5/12 | Negative |
| Slow performance | 4/12 | Negative |
| Great core features | 4/12 | Positive |

## Key Quotes
- "Have to reset password weekly"
- "Takes forever to load dashboard"

## Recommendations
1. **Immediate:** Fix login session persistence
2. **Short-term:** Performance audit on dashboard

## Quality Criteria

**Good:** Quantifies themes, includes evidence, separates observation from recommendation
**Avoid:** Lists without counts, no quotes, mixing analysis with opinion
```

---

## Example 3: Action Item Extractor

### Original Conversation Pattern

**User kept saying:**
> "Here are my meeting notes: [transcript]. What are the action items?"

**Claude's successful response pattern:**
- Scanned for action language
- Identified owners
- Captured deadlines
- Flagged ambiguities

### Extracted Skill

```markdown
---
name: action-item-extractor
description: Extract structured action items from meeting notes with owners and deadlines. Use when asked for "action items," "what do we need to do," or "who's doing what."
---

# Action Item Extractor

Parse meeting notes to identify and structure action items.

## Workflow

1. Scan for action language (will, needs to, should, must)
2. Identify owner (explicit or inferred)
3. Extract deadlines
4. Flag items without clear owners

## Input Required

- Meeting notes or transcript

## Output Format

| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| Specific task | Name | Date | ⚪ |

Plus notes on ambiguities.

## Example

### Input
"Sarah will send designs by Friday. John said he'd set up testing. Someone should follow up with legal."

### Output

| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| Send updated designs | Sarah | Friday | ⚪ |
| Set up testing environment | John | - | ⚪ |
| Follow up with legal | TBD | - | ⚪ |

⚠️ Legal follow-up needs owner assigned

## Quality Criteria

**Good:** Every action has owner (or flagged), specific and verifiable
**Avoid:** Vague actions, missing owners, buried in paragraphs
```

---

## Extraction Patterns

### What Made These Work

1. **Clear input pattern** - Users provided similar inputs each time
2. **Consistent transformation** - Claude did the same type of work
3. **Measurable output** - Success was visible and repeatable
4. **Specific triggers** - Easy to know when to use the skill

### Red Flags During Extraction

- "It depends" too often → skill needs more constraints
- No clear output format → harder to evaluate quality
- Too many variations → split into multiple skills
- Requires real-time data → may not work as static skill
