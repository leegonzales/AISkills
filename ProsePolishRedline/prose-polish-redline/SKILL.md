---
name: prose-polish-redline
description: Run prose-polish analysis as parallel agents that produce tracked-changes .docx and animated HTML replay. Composable kata agents generate line-level edits in a shared JSON schema.
---

# Prose Polish Redline

Composable prose-editing system that runs focused agents in parallel, merges their edits with conflict resolution, and outputs tracked-changes .docx + animated HTML replay.

## Quick Start

```
/prose-polish-redline essays/range-framework-essay.md
/prose-polish-redline essays/range-framework-essay.md --depth aggressive
/prose-polish-redline essays/range-framework-essay.md --depth conservative --genre academic
/prose-polish-redline essays/range-framework-essay.md --dry-run
```

## Pipeline

```
INPUT: essay.md [--depth moderate] [--genre academic] [--dry-run]
  │
  ├── md_to_docx.py   → .docx
  ├── extract_text.py  → plain text (canonical for all agents)
  │
  ├── Wave 0: genre-scorer → genre + 6D quality profile
  │
  ├── Wave 1 (parallel): Phase 1 kata agents → edit JSONs
  │     ├── coherence-agent.md
  │     ├── authority-agent.md
  │     ├── claims-agent.md
  │     └── stakes-agent.md
  │
  ├── merge_edits.py → merged Phase 1 edits
  │
  ├── Wave 2 (parallel): Phase 2 kata agents → edit JSONs
  │     ├── rhythm-agent.md
  │     ├── hedge-agent.md
  │     ├── personality-agent.md
  │     └── perspective-agent.md
  │
  ├── merge_edits.py → final merged review JSON
  │
  ├── apply_redlines.py → tracked-changes .docx
  └── generate_replay.py → animated HTML replay

OUTPUT: {stem}_reviewed.docx + {stem}_replay.html + {stem}_review.json
```

## Process

### Step 0: Setup

1. Determine the working directory: use the input file's directory
2. Set depth from CLI arg or default to `moderate`
3. Set genre from CLI arg or auto-detect in Wave 0

### Step 1: Convert and Extract

```bash
python ~/.claude/skills/prose-polish-redline/scripts/md_to_docx.py INPUT.md OUTPUT.docx
python ~/.claude/skills/prose-polish-redline/scripts/extract_text.py OUTPUT.docx -o EXTRACTED.txt
```

Report: "Converted {INPUT.md} → {OUTPUT.docx} ({N} paragraphs extracted)"

### Step 2: Wave 0 — Genre Scoring

Run the genre-scorer agent with the extracted text.

**Input to agent:** Full contents of EXTRACTED.txt
**Agent prompt:** Load `agents/genre-scorer.md` and follow its instructions
**Output:** Genre result JSON (genre, scores, priorities)

Report: "Genre: {genre} (confidence: {confidence}). Priority dimensions: {priorities}"

Save genre result to `{stem}_genre.json`

### Step 3: Wave 1 — Phase 1 Agents (Parallel)

Based on depth, launch Phase 1 agents **in parallel**:

| Depth | Agents |
|-------|--------|
| conservative | coherence-agent, authority-agent |
| moderate | coherence-agent, authority-agent, claims-agent, stakes-agent |
| aggressive | coherence-agent, authority-agent, claims-agent, stakes-agent |

**Input to each agent:**
1. Full contents of EXTRACTED.txt
2. Genre result JSON from Wave 0
3. The agent's prompt from `agents/{agent-name}.md`
4. The edit schema from `references/edit-schema.md`

**Critical instruction for each agent:** "You MUST use the FULL contents of EXTRACTED.txt passed below as your source document. Do not summarize, truncate, or paraphrase it. Your `original_text` must be a verbatim character-for-character copy-paste from this document text. This is code-level exact string matching — if your `original_text` is off by even one character, the edit will silently fail."

**Model guidance:** For authority-agent, claims-agent, and stakes-agent, consider using `model: "opus"` for better instruction-following on the verbatim constraint. These agents are prone to fabricating `original_text`. Coherence-agent works well with sonnet.

**Output from each agent:** Edit JSON per edit-schema.md

Save each agent's output to `{stem}_{agent-name}.json`

Report: "Wave 1 complete: {N} total edits from {M} agents"

### Step 4: Phase 1 Merge

```bash
python ~/.claude/skills/prose-polish-redline/scripts/merge_edits.py \
  --document EXTRACTED.txt \
  --phase1 {stem}_coherence-agent.json {stem}_authority-agent.json ... \
  -o {stem}_phase1_merged.json
```

Report per-agent match rates from the merge JSON's `stats.per_agent` field:

```
Phase 1 merge: {final_count} edits kept ({duplicates} dupes, {conflicts} conflicts)
  coherence-agent: 14/15 matched
  claims-agent: 6/6 matched
  authority-agent: 0/6 matched ⚠️ — re-run recommended
  stakes-agent: 0/4 matched ⚠️ — re-run recommended
```

**Match-rate gate:** If any agent has 0% match rate with >0 input edits, warn the operator explicitly. Do not silently continue. Suggest: "Agent {name} produced {N} edits but none matched the document. Consider re-running with opus model, or check that the full document text was passed to the agent."

Also report unmatched edits from the merge JSON's `unmatched` array — these show which specific `original_text` values failed to locate.

**If `--dry-run` is set:** Stop here. Report match rates and edit counts, then skip Steps 5-8.

### Step 5: Wave 2 — Phase 2 Agents (Parallel)

**Skip if depth is `conservative`.**

Based on depth, launch Phase 2 agents **in parallel**:

| Depth | Agents |
|-------|--------|
| moderate | rhythm-agent, hedge-agent |
| aggressive | rhythm-agent, hedge-agent, personality-agent, perspective-agent |

**Input to each agent:**
1. Phase-1-edited text (apply Phase 1 edits to extracted text to produce this)
2. Genre result JSON from Wave 0
3. The agent's prompt from `agents/{agent-name}.md`
4. The edit schema from `references/edit-schema.md`

**Critical instruction:** "You are receiving Phase-1-edited text. Your `original_text` must match THIS text, not the original document."

**Model guidance:** For hedge-agent, consider using `model: "opus"` for better instruction-following on the verbatim constraint. The hedge-agent's connective-diagnostic kata is prone to fabricating connectives (inserting "However", "Moreover" into `original_text` that doesn't contain them). Rhythm-agent works well with sonnet.

Save each agent's output to `{stem}_{agent-name}.json`

Report: "Wave 2 complete: {N} total edits from {M} agents"

### Step 6: Final Merge

```bash
python ~/.claude/skills/prose-polish-redline/scripts/merge_edits.py \
  --document EXTRACTED.txt \
  --phase1 {stem}_coherence-agent.json {stem}_authority-agent.json ... \
  --phase2 {stem}_rhythm-agent.json {stem}_hedge-agent.json ... \
  -o {stem}_review.json
```

Report final merge with per-agent breakdown (same format as Step 4). Include Phase 2 agents in the per-agent report.

### Step 7: Apply Redlines

**If `--dry-run` is set:** Skip this step and Step 8.

```bash
python ~/.claude/skills/prose-polish-redline/scripts/apply_redlines.py \
  OUTPUT.docx {stem}_review.json OUTPUT_DIR
```

Report: "Redlined document: {path} (match rate: {rate}%)"

**Match rate warnings:**
- 90%+: Excellent — proceed
- 80-89%: Good — note unmatched edits in output
- <80%: Warning — investigate unmatched edits, likely text normalization issues

### Step 8: Generate Replay

```bash
python ~/.claude/skills/prose-polish-redline/scripts/generate_replay.py \
  OUTPUT.docx {stem}_review.json \
  -o {stem}_replay.html
```

Report: "Replay generated: {path} ({size})"

### Step 9: Summary

Present a final summary:

```
PROSE POLISH REDLINE COMPLETE

Document: {input}
Genre: {genre} ({confidence})
Depth: {depth}
Agents: {count}

Quality Profile (before):
  Craft: {score}/10
  Coherence: {score}/10
  Authority: {score}/10
  Purpose: {score}/10
  Voice: {score}/10

Edits by Tier:
  STRUCTURAL: {count}
  COHERENCE: {count}
  AUTHORITY: {count}
  CRAFT: {count}
  VOICE: {count}

Match Rate: {rate}%

Per Agent:
  coherence-agent: {matched}/{input} matched
  authority-agent: {matched}/{input} matched
  claims-agent: {matched}/{input} matched
  stakes-agent: {matched}/{input} matched

Outputs:
  Tracked changes: {docx_path}
  Replay animation: {html_path}
  Review JSON: {json_path}
```

## Depth Control

| Depth | Wave 0 | Wave 1 | Wave 2 | Total Agents |
|-------|--------|--------|--------|-------------|
| **conservative** | genre-scorer | coherence + authority | — | 3 |
| **moderate** (default) | genre-scorer | coherence + authority + claims + stakes | rhythm + hedge | 7 |
| **aggressive** | genre-scorer | coherence + authority + claims + stakes | rhythm + hedge + personality + perspective | 9 |

## Dry-Run Mode

When `--dry-run` is specified, the pipeline runs Steps 0-4 (genre scoring, Wave 1 agents, Phase 1 merge) but skips apply_redlines and generate_replay. This gives a fast feedback loop for prompt tuning:

- Runs agents and merge — reports per-agent match rates and edit counts
- Does NOT produce .docx or .html output files
- Useful for: testing agent prompts, checking match rates, verifying verbatim constraint compliance

## Tier System

| Tier | Color | Phase | Focus |
|------|-------|-------|-------|
| STRUCTURAL | Blue (#2b6cb0) | 1 | Organization, section flow |
| COHERENCE | Teal (#319795) | 1 | Logic, transitions, causal flow |
| AUTHORITY | Purple (#6b46c1) | 1 | Expertise signals, stakes |
| CRAFT | Orange (#dd6b20) | 2 | Rhythm, precision, density |
| VOICE | Green (#38a169) | 2 | Personality, perspective |

## Error Handling

- **Agent fails to produce valid JSON:** Skip that agent's edits, log warning, continue
- **Agent 0% match rate:** Warn the operator explicitly. The agent's `original_text` values didn't match the document. Suggest re-running with opus model or verifying full document text was passed. Check the `unmatched` array in merge output for specifics.
- **Match rate below 80%:** Warn but don't abort — some edits are still valuable
- **No edits from an agent:** Normal for well-written documents. Report "0 edits" and continue
- **Merge conflict losses:** Logged in discarded array with reason — reviewable in the JSON

## Dependencies

- Python 3.10+
- python-docx (`pip install python-docx`)

## Reference Files

- `references/edit-schema.md` — JSON contract for all agents
- `references/tier-mapping.md` — Tier definitions and priority order
- `references/genre-calibration.md` — Genre-specific thresholds
