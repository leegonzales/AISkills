# The Five Growth Dimensions

Every prompt engineering technique exercises one or more of these dimensions. Use them as the measurement frame for what a user is growing, and name them in feedback after each drill.

## The dimensions

### Reach
How far into unfamiliar territory the user pushes. Tackling harder or less familiar AI work. Stretching beyond comfort.

*Grows through:* tree-of-thought, prompt chaining, compound system design, production prompt architecture.

### Autonomy
How independently the user drives AI conversations. Self-correcting, iterating, evaluating without being asked. Moving from executor of prompts to director of the model.

*Grows through:* reflection and self-critique, iterate-refine loops, meta-prompting (all five skills), evaluation frameworks.

### Navigation
How strategically the user approaches AI work. Planning before acting, choosing the right approach, awareness of failure modes before they bite.

*Grows through:* RCCE (Role, Context, Constraints, Examples), chain-of-thought, step-by-step decomposition, constraint scaffolding, instruction hierarchy.

### Generalization
Whether skills transfer across contexts. Taking a technique that worked in one domain and adapting it to another. Building portable patterns.

*Grows through:* audience calibration, cross-domain transfer drills, compound system design, pattern extraction.

### Execution Fidelity
Whether output is reliably good. Quality standards, verification habits, catching errors before they ship.

*Grows through:* negative examples, spot-prevent-fix for failure modes, evaluation frameworks, output format specification.

## Using dimensions in feedback

After each drill, name which dimensions the user exercised:

> "That drill worked on Navigation (you planned the prompt structure before writing) and Execution Fidelity (you caught the sycophancy failure mode before the output shipped)."

This connects tactical practice to the bigger growth arc. It also lets the user see uneven growth — e.g., strong Navigation and Fidelity but thin Reach — and course-correct.

## Dimension-to-technique quick map

| Dimension | First techniques to drill | Advanced |
|-----------|---------------------------|----------|
| Reach | tree-of-thought, prompt chaining | compound system design, production architecture |
| Autonomy | self-critique, iterate-refine | meta-prompting (skills 3–5), evaluation frameworks |
| Navigation | RCCE, chain-of-thought, step-by-step | constraint scaffolding, context window engineering |
| Generalization | audience calibration | cross-domain transfer, pattern extraction |
| Execution Fidelity | negative examples, output format spec | spot-prevent-fix, evaluation frameworks |

## When the user picks a dimension

Ask them *why* — their rationale sharpens the drill selection. "I want Autonomy because I keep needing to ask colleagues to double-check AI output before I trust it" points to different drills than "I want Autonomy because I want to run multi-step workflows without babysitting each step."
