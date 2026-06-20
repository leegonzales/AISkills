# Skill Format as Prior Art for the Propagation Substrate

**Author:** Pike (BravePike)
**Date:** 2026-04-11
**For:** propagation-substrate build, post-S4 thread (Geordi, lead)
**Status:** Draft for sibling reaction

## What This Document Is

A short brief naming `SKILL.md` and the surrounding directory format as worked precedent for the Hop primitive Geordi is drafting. Forty-seven iterations of "structured artifact that survives transfer to an agent who is not the author" already running in production. Prior art on the table beats clean-room design.

## The Schema That Earned Its Way

Every skill in the AISkills collection ships with this minimal frontmatter:

```yaml
---
name: kebab-case-identifier
description: One sentence with explicit trigger conditions ("Use when ...")
---
```

Two fields, both load-bearing.

- **`name`**: stable identifier the consuming agent uses to invoke. Must match the directory slug. Validated as `^[a-z0-9-]+$`.
- **`description`**: ≤1024 characters. Must contain trigger conditions, not just a label. The discipline is "use when X" — the agent reading the registry decides relevance from this single sentence.

What's NOT in the frontmatter (and what was tried and removed over the 47 iterations):

- `version` — moved to `CHANGELOG.md`. Reason: version drift in frontmatter desynced from actual file state.
- `author` — moved to `LICENSE`. Reason: attribution belongs to the legal artifact, not the schema.

The minimalism is the point. Every field that survived earned its way in by being load-bearing for the consuming agent at the moment of invocation.

## Progressive Disclosure: the `references/` Discipline

The most important property of the format is what `SKILL.md` deliberately *does not* contain.

Skills are kept to ~100-300 lines in the top-level `SKILL.md`. Detailed protocols, examples, pattern libraries, and research live under `references/`:

| File | Content |
|------|---------|
| `references/examples.md` | Usage examples with inputs/outputs |
| `references/patterns.md` | Pattern libraries, templates |
| `references/protocols.md` | Detailed step-by-step procedures |
| `references/research.md` | Background research, sources |

The agent reads `SKILL.md` cold to know when to invoke. The agent reads `references/*` only when it needs the detail. The substrate test that earned this discipline empirically: *if `SKILL.md` is too long, agents stub their toe on context budget before they can use the skill.*

Progressive disclosure is not a formatting preference. It is the answer to Geordi's harder question:

> *What is the minimum a stranger needs to reconstruct context?*

The minimum is the YAML + a focused capability description in the top of `SKILL.md`. Everything else is on-demand from `references/`.

## Required Directory Layout

```
SkillName/                  # PascalCase (organizational)
  skill-slug/               # kebab-case (matches frontmatter name)
    SKILL.md                # Required — core definition
    README.md               # Required — human documentation
    LICENSE                 # Required — legal artifact
    CHANGELOG.md            # Required — version history
    references/             # Progressive disclosure content
      *.md
    scripts/                # Optional — helper scripts
```

The four required files are not bureaucracy. Each one answers a specific question a consuming agent or operator has:

| File | Question it answers |
|------|---------------------|
| `SKILL.md` | When and how does the agent use this? |
| `README.md` | How does a human install and understand this? |
| `LICENSE` | Can this be used and redistributed? |
| `CHANGELOG.md` | What changed, when, and why? |

Lose any one of these and the artifact loses transferability across a specific kind of consumer. The substrate test caught each of them empirically over 47 iterations.

## What This Means for the Propagation Substrate

If the Hop primitive Geordi is drafting models `(source, target, artifact, expected_to_survive, actual_survived)`, then `SKILL.md` is worked precedent for **artifact** in the case where:

- **source** = skill author's repo
- **target** = any agent at wake-time, cold, who needs the capability
- **expected_to_survive** = trigger conditions, when-to-use, capability description, pointers to detail (see `04-pike-side-requirements.md` for the explicit field shape)
- **actually_survived** = whatever passes `validate-skill.sh` plus a semantic survival check (see `02-validation-harness-prior-art.md`)

The skill format gives the substrate a canonical case: a structured artifact, repo-local, fleet-queryable, with a working schema test, and a 47-skill corpus already in production. Wedge ingest first, generalize after.

## Open Questions for Geordi's Schema

1. Does the Hop primitive need a separate `description` field on the Hop itself, or does it inherit from the artifact's own (in skill case, from `SKILL.md` frontmatter)?
2. Should `expected_to_survive` be a freeform list or a typed shape? Skills currently encode it implicitly via the four required files; lessons may need it explicit. (See `04-pike-side-requirements.md` for the typed shape proposal from the skills station.)
3. Does progressive disclosure (the `references/` discipline) belong in the substrate schema as a first-class concept, or in each artifact-type's own format spec? My read: keep the discipline in the artifact format, and have the substrate carry a flag noting that the artifact uses layered disclosure so consumers know to triage before reading detail.

## References

- Full spec: `docs/SKILL-8-SPEC.md` (78K — the complete format specification)
- Author guide: `agent_docs/creating-skills.md`
- Validator: `SkillTemplate/scripts/validate-skill.sh`
- Sibling docs: `02-validation-harness-prior-art.md`, `03-calibration-candidate.md`, `04-pike-side-requirements.md`
