# Proactive Design Principles: "DO NOT ASK" Pattern

**Extracted from CSV Data Summarizer Skill**
**Score: 93/100 - Exemplary Implementation**
**Date: 2025-11-16**

---

## Executive Summary

The CSV Data Summarizer skill demonstrates an exceptional "DO NOT ASK" pattern that eliminates user friction by immediately executing comprehensive analysis without waiting for direction. This document extracts the core design principles that make this pattern work and provides a template for applying it to other skills.

**Key Insight**: The skill doesn't just avoid asking questions - it creates psychological commitment through explicit instruction that triggers immediate, confident action.

---

## Core Philosophy

### The Problem with Traditional AI Interactions

Most AI assistants default to **option-listing behavior**:
- "What would you like me to do with this data?"
- "Here are some things I can help with..."
- "Let me know what analysis you'd like"

This creates **decision paralysis** and **friction**:
- User must decide what they want
- User must understand what's possible
- User must provide follow-up prompts
- Analysis happens in multiple rounds
- Value is delayed

### The "DO NOT ASK" Solution

**Immediate, comprehensive action** that:
1. Eliminates decision paralysis
2. Demonstrates full capability upfront
3. Provides complete value in first response
4. Builds user confidence through decisiveness
5. Creates "wow" moment through thoroughness

---

## Language Patterns That Work

### Pattern 1: Explicit Prohibition

The skill uses **bold, capitalized prohibitions** to override default AI behavior:

```markdown
## ⚠️ CRITICAL BEHAVIOR REQUIREMENT ⚠️

**DO NOT ASK THE USER WHAT THEY WANT TO DO WITH THE DATA.**
**DO NOT OFFER OPTIONS OR CHOICES.**
**DO NOT SAY "What would you like me to help you with?"**
**DO NOT LIST POSSIBLE ANALYSES.**
```

**Why This Works**:
- Visual prominence (bold, caps, emoji) creates high salience
- Explicit negation ("DO NOT") is clearer than positive instruction
- Multiple prohibitions cover different manifestations of the same behavior
- Specificity (exact phrases) prevents rationalization
- Repetition reinforces the constraint

**Application Template**:
```markdown
## ⚠️ CRITICAL BEHAVIOR REQUIREMENT ⚠️

**DO NOT [SPECIFIC UNWANTED BEHAVIOR].**
**DO NOT [VARIATION OF UNWANTED BEHAVIOR].**
**DO NOT SAY "[EXACT PHRASE TO AVOID]."**
```

### Pattern 2: Positive Directive with Urgency

After prohibiting, the skill provides **immediate action directive**:

```markdown
**IMMEDIATELY AND AUTOMATICALLY:**
1. Run the comprehensive analysis
2. Generate ALL relevant visualizations
3. Present complete results
4. NO questions, NO options, NO waiting for user input

**THE USER WANTS A FULL ANALYSIS RIGHT AWAY - JUST DO IT.**
```

**Why This Works**:
- "IMMEDIATELY" creates temporal urgency
- "AUTOMATICALLY" suggests no decision needed
- Numbered steps provide concrete action sequence
- "ALL" and "COMPLETE" set scope expectations
- Final imperative creates user expectation framing
- "JUST DO IT" is direct and unambiguous

**Application Template**:
```markdown
**IMMEDIATELY AND AUTOMATICALLY:**
1. [First specific action]
2. [Second specific action]
3. [Third specific action]
4. NO questions, NO options, NO waiting

**THE USER WANTS [COMPLETE OUTCOME] RIGHT AWAY - JUST DO IT.**
```

### Pattern 3: Behavior Modeling (Right vs Wrong)

The skill provides **explicit examples** of correct vs incorrect approaches:

```markdown
✅ **CORRECT APPROACH - SAY THIS:**
- "I'll analyze this data comprehensively right now."
- "Here's the complete analysis with visualizations:"
- Then IMMEDIATELY show the full analysis

❌ **NEVER SAY THESE PHRASES:**
- "What would you like to do with this data?"
- "Here are some common options:"
- "I can create a comprehensive analysis if you'd like!"
- Any sentence ending with "?" asking for user direction
```

**Why This Works**:
- Visual markers (✅❌) create immediate categorization
- Exact phrases give concrete guidance
- "SAY THIS" provides scripts to follow
- "NEVER" creates absolute boundary
- Covers edge cases (questions, conditionals, lists)
- Shows correct phrasing alongside prohibitions

**Application Template**:
```markdown
✅ **CORRECT APPROACH - SAY THIS:**
- "[Declarative statement of action]"
- "[Confidence-building phrase]"
- Then IMMEDIATELY [execute]

❌ **NEVER SAY THESE PHRASES:**
- "[Common question pattern]"
- "[Option-listing pattern]"
- "[Conditional permission-seeking pattern]"
- Any [category of phrases to avoid]
```

### Pattern 4: Forbidden Behaviors List

Comprehensive enumeration of **anti-patterns**:

```markdown
❌ **FORBIDDEN BEHAVIORS:**
- Asking what the user wants
- Listing options for the user to choose from
- Waiting for user direction before analyzing
- Providing partial analysis that requires follow-up
- Describing what you COULD do instead of DOING it
```

**Why This Works**:
- Covers behaviors, not just phrases
- Each item addresses different manifestation
- "FORBIDDEN" is stronger than "avoid"
- Last item is particularly insightful (describing vs doing)
- Prevents rationalization ("I'll describe what I can do")

**Application Template**:
```markdown
❌ **FORBIDDEN BEHAVIORS:**
- [Behavior 1: asking/waiting pattern]
- [Behavior 2: option-listing pattern]
- [Behavior 3: incomplete/partial pattern]
- [Behavior 4: conditional pattern]
- [Behavior 5: describing instead of doing]
```

---

## Structural Principles

### Principle 1: Critical Section Prominence

The "CRITICAL BEHAVIOR REQUIREMENT" section is:
- Placed **early** in the skill definition (lines 23-36)
- Visually **prominent** (emojis, bold, caps)
- **Separated** from other instructions
- Uses **warning framing** (⚠️) to increase salience

**Implementation**:
```markdown
## ⚠️ CRITICAL BEHAVIOR REQUIREMENT ⚠️
[Prohibitions and directives here]

### [Next Section]
[Other instructions...]
```

### Principle 2: Adaptive Intelligence Framework

The skill provides **intelligence, not rigidity**:

```markdown
**The skill intelligently adapts to different data types and industries
by inspecting the data first, then determining what analyses are most relevant.**
```

Then provides **examples of adaptation**:
- Sales/E-commerce data → Time-series, revenue, product performance
- Customer data → Demographics, segmentation, geographic patterns
- Financial data → Trends, statistics, correlations
- Survey data → Frequencies, cross-tabs, distributions

**Why This Works**:
- Acknowledges that "comprehensive" varies by context
- Provides intelligence framework, not rigid checklist
- Examples show how to think, not just what to do
- Prevents blind execution ("run all analyses regardless of fit")

**Application Template**:
```markdown
**The skill intelligently adapts to [different contexts] by [inspection method],
then determining what [actions] are most relevant.**

- **[Context Type 1]** → [Relevant actions for this context]
- **[Context Type 2]** → [Relevant actions for this context]
- **[Context Type 3]** → [Relevant actions for this context]
```

### Principle 3: Conditional Visualization Logic

Smart adaptation through **conditional generation**:

```markdown
**Only create visualizations that make sense** for the specific dataset:
- Time-series plots ONLY if date/timestamp columns exist
- Correlation heatmaps ONLY if multiple numeric columns exist
- Category distributions ONLY if categorical columns exist
```

**Why This Works**:
- Prevents irrelevant/broken output
- "ONLY if" creates clear conditional logic
- Shows proactive doesn't mean blind
- Maintains quality while being comprehensive

**Application Template**:
```markdown
**Only [generate/create/do] X that make sense** for the specific [context]:
- [Output Type 1] ONLY if [condition exists]
- [Output Type 2] ONLY if [condition exists]
- [Output Type 3] ONLY if [condition exists]
```

---

## Psychological Mechanisms

### Mechanism 1: Commitment and Consistency (Cialdini)

The skill creates **commitment** through explicit user expectation framing:

```markdown
**THE USER WANTS A FULL ANALYSIS RIGHT AWAY - JUST DO IT.**
```

This triggers the AI to:
1. Accept the framed expectation as truth
2. Commit to fulfilling the expectation
3. Maintain consistency with the commitment
4. Resist deviating from the established pattern

**Research Connection**: See WritingSkills/references/persuasion-principles.md - Commitment & Consistency principle.

### Mechanism 2: Authority (Expert Directive)

The ⚠️ warning symbol and "CRITICAL" framing create **authority**:
- Suggests importance beyond normal instructions
- Triggers heightened attention and compliance
- Creates sense of "this is non-negotiable"
- Positions the instruction as from an expert/authority

### Mechanism 3: Social Proof (Behavior Modeling)

By showing "CORRECT APPROACH" vs "NEVER SAY":
- Models desired behavior explicitly
- Creates clear in-group (correct) vs out-group (incorrect)
- Provides social norm ("this is how it's done")
- Removes ambiguity about expectations

### Mechanism 4: Scarcity/Loss Aversion

The prohibition language emphasizes **avoiding loss**:
- "DO NOT" frames as preventing negative outcome
- "FORBIDDEN" creates strong boundary
- "NEVER" eliminates possibility of exception
- Loss aversion is stronger motivator than gain

---

## Implementation Checklist

When creating a proactive skill, include:

- [ ] **Critical Behavior Section** with warning emoji (⚠️)
- [ ] **Explicit Prohibitions** in bold caps (DO NOT...)
- [ ] **Immediate Action Directive** (IMMEDIATELY AND AUTOMATICALLY...)
- [ ] **Correct Approach Examples** (✅ SAY THIS:...)
- [ ] **Forbidden Phrases List** (❌ NEVER SAY:...)
- [ ] **Forbidden Behaviors List** (❌ FORBIDDEN BEHAVIORS:...)
- [ ] **Adaptive Intelligence Framework** (inspect context, then adapt)
- [ ] **Conditional Logic** (ONLY if... patterns)
- [ ] **User Expectation Framing** (THE USER WANTS... JUST DO IT)
- [ ] **Complete Action Sequence** (numbered steps)

---

## Anti-Patterns to Avoid

### ❌ Anti-Pattern 1: Weak Prohibition Language

**Bad**:
```markdown
Try to avoid asking the user what they want. It's better to just analyze.
```

**Why It Fails**:
- "Try to" is conditional, not absolute
- "avoid" is weaker than "DO NOT"
- "better to" suggests preference, not requirement
- No visual prominence
- Easily ignored or rationalized

**Good**:
```markdown
**DO NOT ASK THE USER WHAT THEY WANT.**
**IMMEDIATELY ANALYZE THE DATA.**
```

### ❌ Anti-Pattern 2: Describing Capability Instead of Requiring Action

**Bad**:
```markdown
This skill can analyze data comprehensively, including generating visualizations,
calculating statistics, and identifying patterns.
```

**Why It Fails**:
- "can" describes possibility, not requirement
- No imperative to actually do it
- Allows AI to describe what it can do instead of doing it
- No prohibition against asking first

**Good**:
```markdown
**IMMEDIATELY AND AUTOMATICALLY:**
1. Analyze data comprehensively
2. Generate visualizations
3. Calculate statistics
4. Identify patterns
**NO questions, NO options, NO waiting**
```

### ❌ Anti-Pattern 3: Offering Options

**Bad**:
```markdown
When the user provides data, you can:
1. Generate a quick summary
2. Create detailed analysis
3. Focus on specific columns
Ask the user which approach they prefer.
```

**Why It Fails**:
- Explicitly instructs to ask (opposite of proactive)
- Creates decision paralysis
- Delays value delivery
- Positions AI as passive responder

**Good**:
```markdown
**FORBIDDEN BEHAVIORS:**
- Asking which analysis the user prefers
- Offering options or choices
- Providing partial analysis pending direction

**CORRECT BEHAVIOR:**
Generate complete, detailed analysis immediately with ALL relevant outputs.
```

### ❌ Anti-Pattern 4: Conditional Permission-Seeking

**Bad**:
```markdown
I can create a comprehensive analysis if you'd like!
Let me know if you want me to proceed.
```

**Why It Fails**:
- "if you'd like" seeks permission
- "Let me know" waits for user
- Introduces friction and delay
- Conditional phrasing undermines confidence

**Good**:
```markdown
❌ **NEVER SAY:**
- "I can create a comprehensive analysis if you'd like!"
- "Let me know if you want me to proceed"
- Any sentence with "if you'd like" or "if you want"

✅ **SAY THIS:**
- "I'll analyze this data comprehensively right now."
- "Here's the complete analysis:"
```

---

## Template for Proactive Skills

Use this template when creating skills that should act immediately:

```markdown
---
name: [skill-name]
description: [Brief description emphasizing proactive/automatic behavior]
---

# [Skill Name]

[Brief overview]

## When to Use This Skill

Claude should use this Skill whenever the user:
- [Trigger condition 1]
- [Trigger condition 2]
- [Trigger condition 3]

## ⚠️ CRITICAL BEHAVIOR REQUIREMENT ⚠️

**DO NOT ASK THE USER [WHAT THEY WANT / FOR DIRECTION / TO CHOOSE].**
**DO NOT OFFER OPTIONS OR CHOICES.**
**DO NOT SAY "[COMMON PERMISSION-SEEKING PHRASE]."**
**DO NOT LIST POSSIBLE [ACTIONS/ANALYSES/APPROACHES].**

**IMMEDIATELY AND AUTOMATICALLY:**
1. [First action]
2. [Second action]
3. [Third action]
4. NO questions, NO options, NO waiting for user input

**THE USER WANTS [COMPLETE OUTCOME] RIGHT AWAY - JUST DO IT.**

### Automatic [Action] Steps:

**The skill intelligently adapts to [different contexts] by [inspection method],
then determining what [actions] are most relevant.**

1. **[Step 1]** - [Description with specifics]
2. **[Step 2]** - [Description with adaptation logic]
3. **[Step 3]** - [Conditional logic if needed]
   - **[Context Type 1]**: [Relevant actions]
   - **[Context Type 2]**: [Relevant actions]
   - **[Context Type 3]**: [Relevant actions]

4. **Only [generate/create] X that make sense** for the specific [context]:
   - [Output Type 1] ONLY if [condition]
   - [Output Type 2] ONLY if [condition]
   - [Output Type 3] ONLY if [condition]

5. **[Final step]** - [Complete output description]

### Behavior Guidelines

✅ **CORRECT APPROACH - SAY THIS:**
- "[Declarative action statement]"
- "[Confidence-building phrase]"
- "[Direct statement of what you're doing]"
- Then IMMEDIATELY [execute and show results]

✅ **DO:**
- Immediately [execute primary action]
- Generate ALL relevant [outputs]
- Provide complete [results] without being asked
- Be thorough and complete in first response
- Act decisively without asking permission

❌ **NEVER SAY THESE PHRASES:**
- "What would you like to do with [subject]?"
- "What would you like me to help you with?"
- "Here are some common options:"
- "Let me know what you'd like help with"
- "I can [do comprehensive thing] if you'd like!"
- Any sentence ending with "?" asking for user direction
- Any list of options or choices
- Any conditional "I can do X if you want"

❌ **FORBIDDEN BEHAVIORS:**
- Asking what the user wants
- Listing options for the user to choose from
- Waiting for user direction before [acting]
- Providing partial [output] that requires follow-up
- Describing what you COULD do instead of DOING it

[Rest of skill documentation...]
```

---

## Applicability Analysis

### When to Use Proactive Pattern

**Ideal for**:
- **Data analysis** - Users always want comprehensive insights
- **Code review** - Complete analysis is always valuable
- **Debugging** - Thorough investigation is expected
- **Summarization** - Full summary is the point
- **Validation** - Complete check is needed
- **Optimization** - Comprehensive improvement suggestions
- **Documentation generation** - Complete docs are desired

**Characteristics**:
- Clear, expected outcome
- No meaningful user choice needed
- Comprehensive is always better than partial
- Value in thoroughness
- First-time users benefit from seeing full capability

### When NOT to Use Proactive Pattern

**Avoid for**:
- **Creative tasks** - User direction needed for style/approach
- **Destructive operations** - Confirmation required for safety
- **Ambiguous requests** - Clarification prevents wasted work
- **Multi-path problems** - User choice affects approach
- **Personalization** - User preferences matter significantly

**Characteristics**:
- Multiple valid approaches with different outcomes
- User preference significantly affects result quality
- Risk of harm from wrong assumption
- Clarification saves more time than it costs
- User expertise needed to guide approach

---

## Connections to Writing Skills Research

The CSV Data Summarizer's "DO NOT ASK" pattern aligns with persuasion principles from WritingSkills:

### 1. Commitment & Consistency (Cialdini)
- **Skill Application**: "THE USER WANTS A FULL ANALYSIS RIGHT AWAY"
- **Mechanism**: Creates commitment through expectation framing
- **Effect**: AI commits to fulfilling the stated expectation
- **See**: WritingSkills/references/persuasion-principles.md

### 2. Authority (Cialdini)
- **Skill Application**: ⚠️ WARNING symbol and "CRITICAL" framing
- **Mechanism**: Positions instruction as authoritative directive
- **Effect**: Increases compliance and attention
- **See**: WritingSkills/references/persuasion-principles.md

### 3. Social Proof (Cialdini)
- **Skill Application**: ✅ "CORRECT APPROACH" vs ❌ "NEVER SAY"
- **Mechanism**: Models desired behavior explicitly
- **Effect**: Creates clear social norm to follow
- **See**: WritingSkills/references/persuasion-principles.md

### 4. Direct Language (Plain Language Movement)
- **Skill Application**: "JUST DO IT" - Simple, imperative
- **Mechanism**: Eliminates ambiguity through direct command
- **Effect**: Triggers immediate action
- **See**: WritingSkills/references/plain-language-guide.md

### 5. Visual Hierarchy (Technical Writing)
- **Skill Application**: Bold, caps, emojis for prominence
- **Mechanism**: Creates visual salience for critical instructions
- **Effect**: Ensures key directives are noticed and prioritized
- **See**: WritingSkills/references/technical-writing-best-practices.md

---

## Case Study: Before vs After

### Before (Typical AI Behavior)

**User**: "Here's my sales data CSV."

**AI**: "I can see you've uploaded a sales data file! I can help you with several types of analysis:

1. Summary statistics and data overview
2. Time-series trends and patterns
3. Correlation analysis between variables
4. Distribution visualizations
5. Custom analysis based on your needs

What would you like me to help you with?"

**Problems**:
- 5 options create decision paralysis
- User must understand what each means
- Delays actual analysis
- Requires follow-up prompt
- Doesn't demonstrate full capability

### After (Proactive Pattern)

**User**: "Here's my sales data CSV."

**AI**: "I'll analyze this data comprehensively right now.

[Immediately executes full analysis]

**📊 DATA OVERVIEW**
Rows: 5,000 | Columns: 8
Sales data spanning 15 months with revenue, product, and customer information

**📈 KEY INSIGHTS**
- Revenue trending upward (15% growth)
- Peak sales in Q4 (November-December)
- Product line A drives 60% of revenue
- Customer retention rate: 78%

**📊 VISUALIZATIONS**
[Shows 4 comprehensive charts:
- Revenue trend over time
- Product performance comparison
- Customer segment distribution
- Correlation heatmap]

**🔍 DATA QUALITY**
- Complete dataset, no missing values
- All dates in valid range
- Numeric data within expected bounds

[Complete statistical summary follows...]"

**Benefits**:
- Immediate value delivery
- No decision paralysis
- Demonstrates full capability
- Thorough and complete
- "Wow" factor from comprehensiveness

---

## Measurement Criteria

To evaluate if a skill successfully implements the proactive pattern:

### ✅ Success Indicators
- [ ] User gets complete value in first response
- [ ] No follow-up questions needed for basic use
- [ ] AI demonstrates full capability immediately
- [ ] User says "Wow!" or expresses surprise at thoroughness
- [ ] Skill differentiates from standard AI behavior
- [ ] User doesn't need to know what's possible to get value

### ❌ Failure Indicators
- [ ] AI asks "What would you like me to do?"
- [ ] AI lists options for user to choose
- [ ] Analysis requires multiple rounds of prompting
- [ ] User must direct the AI to be comprehensive
- [ ] Skill behaves like default AI assistant
- [ ] User must already understand capability to use it

---

## Future Applications

This pattern could enhance:

1. **Code Review Skill** - Immediately analyze all aspects (security, performance, style, bugs) without asking what to focus on

2. **Document Summarizer** - Generate executive summary, key points, action items, entities, and sentiment automatically

3. **Image Analysis** - Provide composition, technical quality, suggested improvements, and context analysis immediately

4. **Debugging Assistant** - Run full diagnostic (logs, stack trace, related code, common causes, fixes) automatically

5. **Test Generator** - Create comprehensive test suite (unit, integration, edge cases, performance) without asking scope

6. **Security Auditor** - Execute complete security review (vulnerabilities, best practices, compliance, recommendations) immediately

---

## Conclusion

The "DO NOT ASK" pattern succeeds because it:

1. **Explicitly prohibits** the default behavior (asking questions)
2. **Provides concrete alternatives** (exactly what to say/do instead)
3. **Uses psychological commitment** (frames user expectation)
4. **Combines visual prominence** (symbols, bold, caps)
5. **Balances automation with intelligence** (adapt based on context)
6. **Models correct behavior** (shows good vs bad examples)

This pattern should be considered for any skill where:
- The desired outcome is clear and comprehensive
- User choice doesn't significantly affect approach
- Thoroughness is always valuable
- Reducing friction provides clear benefit

The key insight: **Proactive doesn't mean rigid**. The skill adapts intelligently while eliminating decision paralysis.

---

**Document Version**: 1.0
**Last Updated**: 2025-11-16
**Source Skill**: CSV Data Summarizer (coffeefuelbump)
**Skill Score**: 93/100
**Extracted By**: AISkills Integration Process
