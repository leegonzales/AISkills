# Meta-Analysis: Building Claimify
## Teaching the System to Teach Itself

---

## What We Built

**Claimify** = claim extraction + structural analysis + argument mapping

A skill that transforms discourse → structured claim-networks, exposing:
- Explicit/implicit claims
- Logical relationships (supports/opposes/assumes)
- Evidence chains
- Argument structure
- Tension points, gaps, contradictions

**Core insight:** Most thinking happens in prose. Prose obscures structure. Structure reveals weaknesses.

---

## Design Doctrine: What Makes a Good Skill?

### 1. Conciseness as Constraint

**The context window is a commons tragedy.**

Every token competes. Skills share context with:
- System prompt
- Conversation history  
- Other skills' metadata
- The actual user request

**Implication:** Only add what Claude doesn't already know.

**Applied in Claimify:**
- SKILL.md: 180 lines (well under 500 limit)
- Examples: 230 lines → separate reference file
- No redundancy between SKILL.md and examples
- Validator: executable script (not loaded unless needed)

**Anti-pattern avoided:** Explaining what "claims" are. Claude knows. Focus on *workflow* and *output structure*.

---

### 2. Appropriate Degrees of Freedom

**Match specificity to task fragility.**

- **High freedom** (guidelines): Multiple valid approaches, context-dependent decisions
- **Medium freedom** (pseudocode/templates): Preferred patterns, configurable
- **Low freedom** (exact scripts): Fragile operations, consistency critical

**Applied in Claimify:**
- **High freedom**: Claim extraction (heuristics, not rules)
- **Medium freedom**: Output formats (templates with adaptation language)
- **Low freedom**: JSON validation (exact schema)

**Design question:** Is this task a narrow bridge over cliffs, or an open field?

Claimify = open field. Many valid ways to analyze discourse. Provide map + compass, not a railroad.

---

### 3. Progressive Disclosure

**Three-level loading system:**

1. **Metadata** (name + description) → Always loaded (~100 words)
2. **SKILL.md body** → When skill triggers (<5k words)
3. **Bundled resources** → As needed (unlimited, scripts can execute without context)

**Pattern:** Keep SKILL.md to essentials. Split content at ~500 lines.

**Applied in Claimify:**
```
claimify/
├── SKILL.md (180 lines - core workflow)
├── references/
│   └── examples.md (230 lines - 6 worked examples)
└── scripts/
    └── claim_validator.py (executable - not loaded)
```

**Trigger architecture:**
- Description = primary triggering mechanism
- Must include: what it does + when to use + example phrases
- Body only loads AFTER trigger → "When to Use" in body = useless

---

### 4. Structure Follows Purpose

**Four structural patterns:**

| Pattern | Use Case | Example |
|---------|----------|---------|
| **Workflow-based** | Sequential processes | DOCX skill (decision tree → read/create/edit) |
| **Task-based** | Tool collections | PDF skill (quick start → merge/split/extract) |
| **Reference/Guidelines** | Standards/specs | Brand guidelines (colors → typography → usage) |
| **Capabilities-based** | Integrated systems | Product management (core capabilities list) |

**Claimify choice:** **Workflow-based**
- Clear process: Ingest → Extract → Classify → Map → Analyze → Output
- Sequential but not rigid (can skip steps)
- Decision points (depth level, output format)

---

## Anti-Patterns Avoided

### ❌ Verbosity Theatre
"Claude is a large language model trained by Anthropic to be helpful, harmless, and honest. In this skill, Claude will learn to..."

→ **No.** Get to the workflow.

### ❌ Explaining the Obvious
"Claims are statements that can be true or false..."

→ **No.** Claude knows. Explain the *non-obvious*: atomic vs. compound claims, relationship types, depth levels.

### ❌ Auxiliary Documentation
README.md, INSTALLATION.md, CHANGELOG.md

→ **No.** Skills are for AI agents, not humans. Only include what Claude needs to execute.

### ❌ Putting "When to Use" in Body
Description: "Analyzes arguments"  
Body: "## When to Use This Skill..."

→ **No.** Body loads AFTER trigger. Put triggers in description.

---

## What Makes This Skill Work

### 1. Atomic Claims as Primitives

**Insight:** Discourse = graph of atomic claims, not flat text.

**Operationalized:**
- Define atomicity with examples (good/bad)
- Claim types taxonomy (6 categories)
- Relationship types (6 types)

**Why this works:** Gives Claude a *representation format* that maps well to LLM capabilities (classification, relationship extraction).

---

### 2. Output Format Flexibility

**Four formats, different affordances:**

- **Table** → Quick scanning, claim tracking
- **Graph** → Visual structure, relationships
- **Narrative** → Understanding flow, identifying tensions
- **JSON** → Programmatic processing

**Design principle:** Let user choose representation based on use case, not skill designer's preference.

---

### 3. Depth Levels

**Surface / Standard / Deep**

Not arbitrary—reflects:
- **Cognitive load** (how hard to extract)
- **Time cost** (how long to analyze)
- **Use case** (exploring vs. presenting vs. deep research)

**Makes visible:** The user controls the tradeoff between speed and comprehensiveness.

---

### 4. Examples as Pedagogy

**Six worked examples:**
1. Simple argument (shows basics)
2. Debate transcript (shows opposition mapping)
3. Strategic document (shows implicit assumptions)
4. Meeting notes → decisions (shows applied use)
5. Research synthesis (shows multi-source)
6. Red-teaming (shows self-improvement)

**Pattern:** Example = Input + Output + Meta-analysis

Not just "here's what to do"—show *why* the output is structured that way.

---

## Skill-Building as Doctrine

### The Meta-Skill Pattern

**Building Claimify required:**
1. Reading skill-creator SKILL.md (doctrine)
2. Reading workflow patterns (sequential/conditional)
3. Reading output patterns (template/examples)
4. Following the 6-step process:
   - Understand (concrete examples)
   - Plan (scripts/references/assets)
   - Initialize (run init script)
   - Edit (implement resources + SKILL.md)
   - Package (validate + distribute)
   - Iterate (test on real usage)

**Observation:** The skill-creator skill *itself* follows its own doctrine.
- Concise (18k SKILL.md, moved examples to references/)
- Progressive disclosure (3-level loading)
- Appropriate freedom (high - lots of valid skill designs)
- Structure follows purpose (workflow-based for skill creation)

**Recursive elegance:** Teaching the system to teach itself requires applying the same principles to the teaching process.

---

## Strategic Implications for Your Work

### 1. AI Transformation = Skill Creation

**Pattern match:**
- **Claimify skill** → **AI Flight School curriculum**
- Teaching Claude to extract claims → Teaching humans to shape context
- Progressive disclosure → Scaffolded learning
- Worked examples → Practice-based pedagogy

**Both are:** Packaging procedural knowledge for reuse.

---

### 2. Doctrine > Templates

**What transfers:**
- Conciseness principles
- Freedom calibration
- Progressive disclosure
- Structure-purpose alignment

**Not templates.** Principles you apply to new domains.

**Your AI Tractability Grid:** Similar pattern—doctrine for mapping problems, not a fixed template.

---

### 3. Skills as Organizational Capabilities

**Companies don't "adopt AI"—they build organizational skills.**

- Claimify = capability to analyze arguments systematically
- Your Flight School = capability to shape AI context effectively
- Both require: workflow + examples + scaffolding + iteration

**Observation:** Most "AI adoption" efforts skip the skill-building step. They provide tools without procedural knowledge.

**Your edge:** You're building the procedural knowledge layer.

---

### 4. Meta-Skills as Force Multipliers

**Skill-creator is a meta-skill—it creates skills.**

**Pattern for your work:**
- Train people to use AI → good
- Train people to teach others to use AI → better
- Train people to create organizational capabilities → force multiplier

**AI Flight School v2:** Not just "here's how to use Claude"—"here's how to build your team's AI capabilities."

---

## Limitations & Extensions

### Current Limitations

1. **No quantitative analysis:** Doesn't assess argument strength, just structure
2. **No domain-specific claim types:** Generic taxonomy
3. **No interactive refinement:** One-shot extraction
4. **No visual diagram generation:** Only Mermaid text

### Possible Extensions

**Claimify v2 could add:**
- Argument strength scoring (validity + soundness)
- Domain-specific templates (legal reasoning, scientific claims, etc.)
- Interactive claim refinement workflow
- Integration with knowledge graphs
- Toulmin model support (warrants, backing, rebuttals)
- Automated bias detection

**Skill composition pattern:** Build specialized variants:
- `claimify-legal` (legal reasoning structures)
- `claimify-scientific` (hypothesis/evidence chains)
- `claimify-strategic` (claims → decisions → actions)

---

## Reflection: What Did We Learn?

### About Skills

**Skills are cognitive scaffolds.** They give Claude:
- A representation format (atomic claims + relationships)
- A workflow (6-step process)
- Output templates (4 formats)
- Examples to pattern-match against (6 use cases)

**Not:** Memorized knowledge. Claude already knows about arguments.  
**Is:** Procedural structure for *systematic* analysis.

---

### About Skill Creation

**The hardest part:** Deciding what NOT to include.

Every explanation you remove:
- Saves context
- Reduces noise
- Forces precision

**Second hardest:** Calibrating freedom.

Too prescriptive → brittle, can't adapt.  
Too loose → inconsistent, unhelpful.

**Solution:** Examples. Show valid variations, Claude learns the pattern.

---

### About Teaching

**Skills teach by structure, not by instruction.**

Claimify doesn't say "be thorough" or "think carefully"—it provides:
- Atomic claim definition
- Relationship taxonomy  
- Depth levels
- Output formats

**Structure = constraint = clarity.**

---

### About Your Work

**You're building meta-capabilities.**

Not "here's how to use Claude for X"—you're teaching:
- How to shape context systematically
- How to evaluate outputs critically
- How to build organizational fluency

**This is skill-building at scale.**

The Claimify pattern applies:
- Concise core (no fluff)
- Progressive disclosure (scaffolded depth)
- Appropriate freedom (guidelines, not scripts)
- Examples over explanation (practice-based)

**Your frameworks (OODA, Wardley, AI Tractability Grid):** Same pattern. Doctrine > templates. Structure > instruction.

---

## Closing: The Recursive Nature of Teaching

Building Claimify = using skill-creator skill = following doctrine = applying same principles to the teaching process.

**Observation:** Good pedagogy is fractal. The principles that make skills work (conciseness, freedom calibration, progressive disclosure, examples) also make teaching work.

**Your Flight School:** Same fractal pattern. Teaching humans to use AI well requires the same structure-giving that skills give Claude.

**The meta-insight:** Teaching systems to perform well and teaching humans to perform well follow similar principles—not because they're similar beings, but because learning itself has structure.

**Claimify now exists.** You can use it to analyze arguments, map debates, red-team reasoning.

**More importantly:** The *process* of building it demonstrates the principles you're already using in your transformation work—just applied to a different domain.

**#core_insight:** Skills are crystallized doctrine. Building them well requires the same clarity of thought you bring to strategic frameworks. Both are map-making: revealing structure that was always there but hidden in the weeds.
