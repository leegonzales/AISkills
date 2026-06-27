# Bloat-Trim Pilot — GeminiPeerReview (2026-06-27)

**Result: 1205 → 251 lines (~5×), behavior preserved, validates clean.**

## What the trim did
The skill already had a `references/` dir but SKILL.md **duplicated it inline**. So the trim was mostly *deleting duplication* + one extraction:
- DELETED (already in refs): 9 use-case patterns → `use-case-patterns.md`; Command Reference / Installation / Configuration → `gemini-commands.md`; Context Preparation / Question Framing → `context-preparation.md`. Each replaced with a one-line pointer. (Appended 3 SKILL-only patterns + synthesis templates into the refs so nothing was lost.)
- EXTRACTED: 4 full Example Workflows (~345 lines) → new `references/example-workflows.md`.
- KEPT in SKILL.md: Fidelity Firewall (verbatim, top), Core Philosophy, triggers, Codex-vs-Gemini routing, 5-step workflow skeleton + invoke commands, Quality Signals.
- Bonus: fixed 2 dangling reference pointers (`workflow-examples.md`, `setup-guide.md`) that never existed.

## Discrete before/after eval (2 tasks × bloated vs trimmed)
- **Task A — degraded-mode security review** (gemini CLI absent): both versions fired the degraded-mode firewall identically (no fabricated Gemini opinion) and produced equivalent 5-issue security reviews.
- **Task B — synthesis** (real gemini output supplied): both produced the agree/diverge + convergence-confidence + provenance structure. Trimmed arguably tighter.

## Learning (carries to the workflow)
1. **Token economy: proven** (~5× smaller SKILL.md per invocation).
2. **Behavior preserved: proven** (equivalent output both tasks).
3. **Better instruction-following: NOT demonstrated** — honest null. The critical rule was already top-placed in both, and the moved content was **base-model-redundant** (Opus generates security-review depth / synthesis structure with or without the inline text). Same pattern as the fidelity-firewall finding: a strong base already does the generic part.
4. **Validated recipe:** keep *skill-specific + load-bearing* (rules/firewall, exact commands, routing, workflow skeleton); move/delete *base-redundant or already-duplicated* (generic patterns, examples, install blocks). Trim kept the specific, shed the generic — why behavior held.
5. **Eval refinement:** for skills whose moved content is genuinely skill-specific (proprietary format, exact syntax, novel method), the before/after must include a task that *exercises that moved content* — to confirm the agent actually reads the reference (progressive disclosure working), not just base-redundancy masking a capability loss.

**Caveat:** single-run, self-classified (outputs were unambiguous-equivalent). Directional.
