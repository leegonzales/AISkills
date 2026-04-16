# Prompt Engineering Curriculum Map

A map of techniques organized by level. **Not a gate.** Start where the user is, move as they are ready. If they already know a technique, skip it. Do not announce levels by name — just work with them at the level they are at.

## Level 1 — Foundations

- **Zero-shot prompting.** Ask clearly and directly without examples. When it's enough, use it.
- **Role setting.** "You are a [role]" — calibrates tone, vocabulary, and assumed context.
- **Few-shot examples.** Two or three demonstrations of input → output before the real task.
- **Output format specification.** Explicitly state the format you want (markdown table, JSON, bullet list with three items).
- **Constraint setting.** Word limits, tone rules, what to avoid.

## Level 2 — Structured Thinking

- **RCCE (Role, Context, Constraints, Examples).** The workhorse structure for any serious prompt. Every piece has a job.
- **Chain-of-thought.** "Think step by step." Force the model to reason visibly before answering. Catches shallow reasoning.
- **Step-by-step decomposition.** Break a complex task into ordered sub-tasks the model executes in sequence.
- **Self-consistency.** Ask for three attempts, take the majority. Good for fact-adjacent tasks.
- **Instruction hierarchy.** Order instructions from most to least important; the model weights earlier instructions more heavily.

## Level 3 — Advanced Control

- **Tree-of-thought.** Have the model explore multiple reasoning branches before converging.
- **Constraint scaffolding.** Nested constraints that activate conditionally ("if X, then also Y").
- **Format templates.** Reusable scaffolds where the model fills in slots you define.
- **Negative examples.** "Here are three bad outputs — do not do this." Sharpens output surprisingly effectively.
- **Audience calibration.** Explicitly describe the reader ("a busy executive who will skim on mobile") — changes everything.
- **Spot-prevent-fix for common failure modes.** Design prompts that pre-empt hallucination, sycophancy, shallow reasoning, context loss, and semantic-vs-functional correctness errors.

## Level 4 — Meta Techniques

- **Reflection and self-critique.** Have the model score its own output and revise. Works.
- **Iterate-refine loops.** Multiple passes, each narrower. "First pass: structure. Second pass: tone. Third pass: final polish."
- **Meta-prompting.** Use the model to build or improve your prompts. See the five-skill progression below — this is a learning arc, not a single technique.
- **Prompt chaining.** Output of prompt A becomes input of prompt B. Splits complex work into composable stages.
- **Error recovery patterns.** What the prompt tells the model to do when it does not have enough info, or when it detects its own uncertainty.

## Level 5 — Mastery

- **Context window engineering.** Deliberate management of what's in-context, what's summarized, what's cached, what's retrieved.
- **Compound system design.** Multi-agent or multi-prompt systems where each part has a well-scoped job.
- **Evaluation frameworks.** How you measure whether a prompt is working — rubrics, comparisons, test sets.
- **Production prompt architecture.** Patterns for prompts that run unattended at scale — error handling, fallbacks, observability, version control.

---

## Meta-Prompting — The Five-Skill Progression

Meta-prompting is not one technique. It is a progression that builds toward using the model as your prompt engineer, so you iterate at a higher level of abstraction.

Each skill assumes fluency in the ones before it. Introduce one at a time. Let the user practice it for multiple drills before moving on. The full progression takes weeks or months.

### Skill 1 — Clarification First (Level 2)

**What:** Before writing the prompt, ask the model what it needs. "I want to [X]. Before I give you the full prompt, what information do you need to do this well?"

**Why:** The user stops guessing at requirements and starts eliciting them. The model becomes a collaborator in prompt design.

**Drill:** Give the user a messy, underspecified task. Have them open a conversation that starts by asking Claude what it needs. Use Claude's questions to build the actual prompt. Reflect: what did Claude surface that the user would have missed?

### Skill 2 — Reverse Engineering (Level 2–3)

**What:** Take a prompt that works. Ask the model to explain why. What does each part do? What would break if you removed a specific element? What assumptions is the prompt making?

**Why:** You cannot ask the model to write better prompts if you cannot recognize what makes one good. Teaches structural reading of prompts.

**Drill:** Paste a working prompt. Have the user predict why it works before asking the model. Then ask the model. Compare — what did the user miss?

### Skill 3 — Prompt Critique (Level 3)

**What:** Take the user's own current prompt. Have the model critique it — what is missing, ambiguous, likely to fail. Have the model rewrite it. Compare.

**Why:** The user learns to see their own blind spots through the model's lens.

**Drill:** User shares a prompt they use. They paste it to Claude and ask for a structural critique. Then ask for a rewrite. They pick which version to use — and explain why.

### Skill 4 — Prompt Generation (Level 4)

**What:** Describe an outcome. The model writes two or three candidate prompts. The user evaluates, picks, or refines. Then uses the winner on the real task.

**Why:** The user is no longer writing prompts — they are curating prompts the model generates. Higher leverage.

**Drill:** User names an outcome. They prompt: "I need to [outcome]. Write three different prompts that would accomplish this, each taking a different approach." They evaluate, pick, run, reflect.

### Skill 5 — Pattern Extraction (Level 5)

**What:** Give the model three or four prompts that worked well for similar tasks. The model extracts the pattern — what is common, what varies, what is the reusable template. The user then uses the template to build new prompts for new tasks.

**Why:** Mastery. The user is designing prompt patterns, not prompts. One level further up the abstraction ladder.

**Drill:** User shares 3–4 prompts they have used successfully. Ask Claude to extract the common pattern. Test the template on a new task. Does it hold up? What needs to change?

---

## Technique → Dimension Mapping

| Technique | Primary dimensions |
|-----------|-------------------|
| Zero-shot | Execution Fidelity |
| Role setting | Execution Fidelity, Navigation |
| Few-shot examples | Execution Fidelity, Navigation |
| Output format spec | Execution Fidelity |
| Constraint setting | Navigation, Execution Fidelity |
| RCCE | Navigation, Execution Fidelity |
| Chain-of-thought | Navigation, Execution Fidelity |
| Step-by-step decomposition | Navigation, Autonomy |
| Self-consistency | Execution Fidelity, Autonomy |
| Instruction hierarchy | Navigation |
| Tree-of-thought | Navigation, Reach |
| Constraint scaffolding | Navigation, Execution Fidelity |
| Negative examples | Execution Fidelity |
| Audience calibration | Generalization, Execution Fidelity |
| Spot-prevent-fix | Execution Fidelity, Navigation, Autonomy |
| Reflection / self-critique | Autonomy, Execution Fidelity |
| Iterate-refine loops | Autonomy, Execution Fidelity |
| Meta-prompting (skills 1–5) | Autonomy, Navigation |
| Prompt chaining | Navigation, Reach |
| Error recovery | Execution Fidelity, Autonomy |
| Context window engineering | Navigation, Execution Fidelity |
| Compound system design | Reach, Navigation, Generalization |
| Evaluation frameworks | Execution Fidelity, Autonomy |
| Production prompt architecture | Reach, Navigation, Generalization, Execution Fidelity |
