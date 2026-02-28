---
name: write-script
description: Use when transforming a research brief into a polished narration script for video production. Runs a 4-phase pipeline (Architecture, Drafting, Multi-Model Review, Revision) with human-in-the-loop approval at each stage. Reads 01-research-brief.json, outputs 05-final-script.txt. The user acts as Showrunner -- all creative decisions require explicit approval.
---

# Write Script

Transform a research brief into a production-ready narration script through a structured, human-approved pipeline. The user is the **Showrunner** -- this skill never auto-approves or auto-applies changes.

## When to Use

Invoke when user:
- Has a `01-research-brief.json` and wants a narration script
- Says "write the script" or uses `/write-script`
- Needs to go from research to narrated video content

## Inputs

- `01-research-brief.json` in working directory (or user-provided path)
- **Video type**: kids_5_10, kids_10_15, corporate, documentary, entertainment, technical
- **Target duration**: seconds (used to calibrate word count at ~150 wpm)

## Pipeline

### Phase A -- Architecture

1. **Storyteller** (Task tool): Read research brief. Design a narrative blueprint -- hook, act structure with purpose/beats/revelations, throughline, and closing image. Save as `02-narrative-blueprint.json`.

   **PAUSE** -- Present blueprint to user. "Here's the narrative architecture. Approve, or what would you change?"

2. **Director** (Task tool): Read research brief + approved blueprint. Create a detailed outline with scenes, transitions, emotional registers, pacing, claim references, and Burke Chain placements. Save as `02b-detailed-outline.json`.

   **PAUSE** -- Present outline to user. Show scene flow, transitions, pacing map.

### Phase B -- Drafting

3. **Writer** (Task tool): Read research brief + blueprint + outline. Write the complete narration script with `[emotion]` tags and `[GRAPHIC: description | DURATION: Xs]` markers. Save as `03-draft-script.txt`.

   **PAUSE** -- Present draft to user.

### Phase C -- Multi-Model Review Panel (parallel)

Run three reviewers simultaneously:

- **Scientist** (Gemini CLI): Fact-check against the claims registry. Output `04a-accuracy-report.json`.
- **Structural Reviewer** (Codex CLI): Review transitions, pacing, repetition, ungrounded stats. Output `04b-structural-review.txt`.
- **Craft Review** (Claude Code inline): Assess narrative flow, rhythm, and outline adherence.

**PAUSE** -- Present synthesized review. "Here's what the review panel found. Your call as Showrunner -- which feedback do you want to apply?"

### Phase D -- Revision

4. Apply user's accepted changes. Re-run specific reviewers if needed. Save as `05-final-script.txt`.

## Output Format

Plain text script with:
- `[emotion]` tags: excited, thoughtful, whispers, softly, curious, emphatically, sighs, laughs
- `[GRAPHIC: description | DURATION: Xs]` markers on their own lines
- Scene structure following Director's outline

## Integration

| Direction  | Skill            | Artifact                 |
|------------|------------------|--------------------------|
| Upstream   | /research-brief  | `01-research-brief.json` |
| Downstream | /render-video    | `05-final-script.txt`    |

## References

- `references/agent-prompts.md` -- Full prompts for Storyteller, Director, Writer
- `references/review-panel.md` -- Gemini/Codex commands, synthesis framework, Showrunner decisions
