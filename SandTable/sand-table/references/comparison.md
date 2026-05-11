# Sand Table vs. the LLM-Simulation Landscape

Honest landscape read. Sand Table is **not** a runtime competitor to AutoGen / CrewAI / TinyTroupe / Concordia. It occupies a different slot — *meta-discipline for AI-coder-assisted bespoke simulator generation* — that no other open package currently fills. This doc explains the slot and where each adjacent system actually wins.

## Where Sand Table sits

```
                   [LLM multi-agent runtime]   ← AutoGen, CrewAI, TinyTroupe, Concordia
                              ∩
              [agent-based modeling discipline] ← NetLogo, MASON, mesa
                              ∩
                 [output validation / eval]     ← Guardrails, LangSmith, Promptfoo
                              ∩
                          ← Sand Table (meta + audit, runtime-agnostic)
```

## Adjacent systems and where each wins

### LLM multi-agent runtimes — they win for general-purpose orchestration

| System | Use it when… |
|---|---|
| **AutoGen** (Microsoft) | You need a battle-tested multi-agent conversation framework with explicit roles, group chat, and the largest community |
| **CrewAI** | You want task-oriented "crews" with role assignment and a polished DX |
| **LangGraph** | Your orchestration is graph-shaped and you want first-class state machines |
| **CAMEL** | You want the academic root of LLM role-play; lightweight |
| **MetaGPT** | You're building a software-dev simulation specifically |

**Sand Table does not compete with these.** It assumes Claude Code is the runtime. If you've already standardized on one of the above, Sand Table can be used as an audit layer over its output (validate the event stream those runtimes produce).

### Persona simulators — TinyTroupe / Concordia win for off-the-shelf personas

| System | Use it when… |
|---|---|
| **Microsoft TinyTroupe** | General-purpose persona simulation (focus groups, ad testing, product feedback). Persona libraries, simulation API, MIT-licensed, well-resourced |
| **DeepMind Concordia** | Generative social simulation with `GameMaster`/`Players`, scenarios, evaluation hooks |
| **Generative Agents** (Park et al.) | You want to read the seminal paper or fork the codebase as a frozen reference |

**Reach for Sand Table when your domain doesn't fit their abstractions.** TinyTroupe is excellent for "test this ad copy with simulated buyers." It's a poor fit for a substack readership where archetypes are paid-vs-lurker-vs-ICP and you care which essay caused churn — that domain wants its own roster schema, its own event types, its own scoring rubric. Sand Table is the kit for building that bespoke simulator.

### Agent-based modeling — mesa / NetLogo win the rule-based discipline lineage

| System | Use it when… |
|---|---|
| **NetLogo / MASON / Repast / AnyLogic** | You're doing rule-based ABM (no LLM in the loop); 30 years of academic depth |
| **mesa** (Python) | Modern Python ABM with familiar idioms; no LLM awareness |

**Sand Table inherits the meta-shape** (declarative invariant → scaffold → run → validate) but adds LLM-specific failure modes (drift, narrative collapse, ghostwriter tells) that rule-based ABM tooling doesn't address.

### Output validation / eval — overlap is narrow

| System | What it validates |
|---|---|
| **Guardrails AI / NeMo Guardrails** | Schema validation, output safety, hallucination checks |
| **LangSmith / Langfuse** | Observability + per-turn evaluation across LLM apps |
| **Promptfoo / DeepEval / Ragas** | Eval harnesses for RAG, retrieval correctness, faithfulness |

**These check different things.** Sand Table's `narrative_check.py` looks for "did one ghostwriter secretly author all the personas?" — single-author tells across an event stream. That signal class is genuinely uncovered by current eval frameworks. Use Sand Table's narrative scan *alongside* LangSmith/Promptfoo — they're complementary, not redundant.

### Constrained-generation libraries — they win for Layer 1

| System | What it does |
|---|---|
| **Outlines, Guidance, Instructor, Pydantic AI** | Constrain decoding so the LLM physically cannot emit `module_id` when the schema demands `module` |

**Adopt these for upstream defense.** Sand Table's three-layer drift defense (prompt hardening → validator → normalization) is necessary when implementations *don't* use constrained generation. Once you adopt Outlines or Instructor, Sand Table's Layer 3 normalization is largely redundant — but Layers 1 (prompt hardening) and the drift catalog (as documentation of what to constrain against) remain useful.

## What's genuinely novel in Sand Table

After honest comparison, four artifacts occupy real empty space:

1. **`narrative_check.py`** — deterministic regex-based scan for single-author tells (other-agent predictions, internal-state knowledge, scoring awareness, synchronized phrasing, self-name dissociation). I don't know of another open package that does this.

2. **Multi-session cohort+exit-context discipline** — exit-context schema, cohort matching, lineage tracking. Most LLM frameworks are single-session; ABM frameworks aren't LLM-aware. Sand Table sits in the gap.

3. **LLM-specific failure-mode catalog** — drift patterns (field-name substitutions), narrative signals, scoring-awareness leaks, premature merging. Hard-won knowledge from three real implementations, packaged as patterns.

4. **Domain-invariant template applied to LLM agents** — ABM brought the "declare the world before you run it" discipline; Sand Table adapts it for LLM-specific concerns (roster schema with aliases, drift mappings, narrative integrity config, multi-session continuity).

## Strategic positioning

**Sand Table is the methodology + audit toolkit for AI-coder-assisted bespoke simulator generation.** Three things make this slot defensible:

- AI coding assistants (Claude Code, Cursor, Aider, Codex) are mainstream and growing
- General-purpose runtimes don't cover the long tail of niche simulator needs
- The "vibe-code a multi-agent sim" default workflow produces unprincipled output

Sand Table fills the gap: opinionated discipline that turns "Claude, build me a multi-agent sim" into a rigorously specified instrument rather than slop. Use it *with* Claude Code, *over* (or *alongside*) any of the runtimes above.
