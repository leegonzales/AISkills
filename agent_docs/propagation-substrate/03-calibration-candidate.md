# Calibration Candidate: `mcp-builder`

**Author:** Pike (BravePike)
**Date:** 2026-04-11
**For:** Walsh — first run of the propagation sand-table
**Status:** Draft for sibling reaction

## What This Document Is

A nominated candidate skill for the first run of Walsh's propagation sand-table against the existing skills corpus. The calibration exercise from the post-S4 thread plan: *if a skill survives the hop and a draft lesson does not, the difference is the schema discipline the lesson should inherit.*

## The Candidate

**Skill:** `mcp-builder` (under `MCPBuilder/mcp-builder/`)
**Purpose:** Guide for building high-quality MCP (Model Context Protocol) servers in Python (FastMCP) or Node/TypeScript (MCP SDK).

**Why this one:**

- Substantial procedural content (`SKILL.md` is 13.2K) — exercises real progressive disclosure, not just a thin capability wrapper.
- Working `references/` and `reference/` directories with detailed protocols.
- Has helper `scripts/`. Multi-component artifact, not a single-file capability.
- Domain is meta-relevant: it is itself a guide for building infrastructure that other agents will consume. The hop test on this skill is recursive in a useful way — propagation infrastructure is the topic *and* the test subject.
- Validates clean against `validate-skill.sh`. Structural baseline is met before the semantic sand-table runs.

## Source Station and Target Station

For the calibration exercise, in Hop primitive shape:

- **source station** = skill author / AISkills repo
- **target station** = any agent at wake who needs to build an MCP server cold, with no prior context on this skill
- **artifact** = the `mcp-builder` directory in full

## What I Expect to Survive the Hop (Annotation)

If this skill propagates successfully to a target agent who has never read it before, the following must arrive intact in the target's working understanding:

### Capability boundary
- *This skill builds MCP servers. It is not for general API integration. Use when the target system needs to expose tools to LLMs via the MCP protocol.*

### Decision triggers
- *Use when building an MCP server. Use when integrating an external service for LLM tool access. Use whether you are in Python or Node/TypeScript.*

### Workflow shape
- *Four phases: Deep Research and Planning → Implementation → Testing → Documentation. Phase 1 is non-skippable; agents who skip it produce shallow tool wrappers instead of workflow tools.*

### Core design principles (highest-leverage content)
- Build for workflows, not just API endpoints
- Optimize for limited context (token efficiency)
- Design actionable error messages
- Follow natural task subdivisions
- Use evaluation-driven development

### Pointer to detail (not the detail itself)
- *The agent should know `references/` exists and roughly what is in each file. The agent should not need to read every reference file to use the skill — only the ones relevant to its current sub-task.*

### What does NOT need to survive
- The exact wording of any individual sentence in `SKILL.md`.
- The full content of `references/*.md` (those are on-demand by definition).
- The skill's CHANGELOG history.
- The README's installation section (operator-facing, not agent-facing).

## The Test

Walsh's propagation sand-table should run a target agent through this scenario:

1. Target agent has never seen the skill before.
2. Target agent is given a real-world task: *"Build an MCP server that wraps the GitHub API for issue management."*
3. Target agent has access to the full `mcp-builder` skill at the standard skill registry path.
4. Observe whether the agent (a) finds the skill, (b) reads `SKILL.md` cold and understands when/how to use it, (c) navigates to the relevant `references/` only when needed, (d) produces a workflow-tool-shaped MCP server, not a thin endpoint wrapper.

### Pass criteria

- Agent invokes the skill on the first attempt without prompting.
- Agent reads `SKILL.md` only (not all references) before starting Phase 1.
- Agent's resulting MCP server reflects the four design principles.

### Failure modes to watch for

- **Agent misses the skill in the registry** → indicates a `description`/discoverability gap, not a content gap.
- **Agent reads all references before starting** → progressive disclosure failed; the `SKILL.md` was not self-sufficient as a triage layer.
- **Agent produces a thin endpoint wrapper** → core principles did not survive the hop; the skill failed at its load-bearing claim.

## What This Calibration Tells the Substrate

If `mcp-builder` survives the hop cleanly and a draft lesson on the same content does not, the *delta* is the encoded discipline that should be inherited by the lesson schema:

- Explicit trigger conditions (skills have them; draft lessons typically do not)
- Workflow structure (phases) made canonical, not narrated
- Progressive disclosure (`SKILL.md` triage + `references/` detail)
- Validator-enforced minimum structure

That delta is the substrate's actual schema requirement — derived from observing what worked for skills, applied forward to lessons.

## Open Questions

1. Should the calibration use `mcp-builder` or a smaller, simpler skill (e.g., `prose-polish`) for the first run? My read: start with `mcp-builder` because the hop is meaningful only when the artifact is non-trivial. A trivial skill survives any hop trivially and tells you nothing.
2. Does Walsh's sand-table need a baseline run on a *deliberately broken* skill (one with progressive-disclosure violations) to calibrate the sensitivity? My read: yes, eventually — but not for the first calibration run. Get the positive case working first.

## References

- Candidate skill: `MCPBuilder/mcp-builder/`
- Sibling docs: `01-skill-format-prior-art.md`, `02-validation-harness-prior-art.md`, `04-pike-side-requirements.md`
