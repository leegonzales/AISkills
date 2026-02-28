# Review Panel -- Multi-Model Script Review

Commands, synthesis framework, and Showrunner decision process for Phase C of the write-script pipeline.

---

## Overview

Three reviewers run in parallel against `03-draft-script.txt`, each bringing a different lens:

| Reviewer             | Tool        | Focus                        | Output                      |
|----------------------|-------------|------------------------------|-----------------------------|
| Scientist            | Gemini CLI  | Factual accuracy vs. claims  | `04a-accuracy-report.json`  |
| Structural Reviewer  | Codex CLI   | Pacing, transitions, craft   | `04b-structural-review.txt` |
| Craft Reviewer       | Claude Code | Narrative flow, outline fit  | Inline (no file)            |

---

## 1. Scientist -- Gemini CLI

### Command

```bash
cat 03-draft-script.txt | gemini "You are a science consultant reviewing a narration script. The claims registry from the research brief is provided below.

CLAIMS REGISTRY:
$(cat 01-research-brief.json | jq '.claims_registry')

For each factual claim in the script, determine its status:
- matches: aligns with a registered claim
- extends: goes beyond what a registered claim supports
- contradicts: conflicts with a registered claim
- unsourced: no matching claim in the registry

Output valid JSON with this structure:
{
  \"verified\": [{\"script_line\": \"...\", \"claim_id\": \"...\", \"status\": \"matches\"}],
  \"flagged\": [{\"script_line\": \"...\", \"issue\": \"...\", \"severity\": \"warning|error\"}],
  \"missingNuance\": [{\"script_line\": \"...\", \"nuance\": \"what the script oversimplifies\"}],
  \"overallAccuracy\": \"high|medium|low\",
  \"claimsCrossReference\": [{\"claim_id\": \"...\", \"used_in_script\": true, \"faithful\": true}]
}
"
```

### Fallback

If `gemini` CLI is not available:
```bash
echo "Gemini CLI not installed. Run: npm install -g @google/gemini-cli"
```

Proceed with Claude-only fact-check as fallback. Note the limitation to the Showrunner.

### What to Look For

- **extends**: The script makes a claim stronger than the source supports. Common with statistics ("doubled" vs. "increased significantly").
- **unsourced**: A claim appears in the script but has no backing in the research brief. Could be hallucinated or common knowledge -- flag for Showrunner judgment.
- **contradicts**: Rare but critical. The script says the opposite of what the research found.
- **missingNuance**: The script simplifies correctly but loses important caveats.

Save output as `04a-accuracy-report.json`.

---

## 2. Structural Reviewer -- Codex CLI

### Command

```bash
cat 03-draft-script.txt | codex exec "You are a structural editor reviewing a narration script. Analyze the following dimensions and be specific about locations (quote the relevant text):

1. TRANSITIONS: Are transitions between scenes smooth? Flag any jarring jumps or missing bridges.
2. PACING: Is there monotony? Flag sequences where 3+ paragraphs have the same rhythm or energy level.
3. SENTENCE STRUCTURE: Flag repetitive patterns (e.g., three sentences starting with 'This...', consecutive same-length sentences).
4. UNGROUNDED STATISTICS: Flag any numbers or statistics that appear without attribution or context.
5. EMOTION TAG DISTRIBUTION: Are [emotion] tags clustered or evenly distributed? Flag imbalances.
6. GRAPHIC CUE QUALITY: Are [GRAPHIC:] prompts specific enough for image generation? Flag vague ones.

For each issue, provide:
- The exact text location (quote 5-10 words)
- What the problem is
- A specific suggestion to fix it

Be direct. Do not pad with praise."
```

### Fallback

If `codex` CLI is not available:
```bash
echo "Codex CLI not installed. Run: npm i -g @openai/codex"
```

Proceed with Claude-only structural review as fallback. Note the limitation to the Showrunner.

Save output as `04b-structural-review.txt`.

---

## 3. Craft Reviewer -- Claude Code (Inline)

This review is performed by Claude Code directly (no external CLI). Read `03-draft-script.txt` and `02b-detailed-outline.json`, then assess:

### Review Checklist

1. **Outline Adherence**: Does every scene from the Director's outline appear in the script? Are transitions the types specified?
2. **Narrative Flow**: Does the script feel like a continuous story or a list of facts?
3. **Rhythm**: Read sentences aloud mentally. Do they vary in length and structure?
4. **Hook Strength**: Does the opening grab attention within the first two sentences?
5. **Landing Strength**: Does the closing leave a memorable image or call to action?
6. **Burke Chain**: Is the guilt-redemption arc present and emotionally resonant?
7. **Spoken Voice**: Does this sound like narration or does it read like an essay?
8. **Graphic Placement**: Do graphic cues appear at natural visual moments, not awkwardly mid-sentence?

### Output Format

Present findings inline when synthesizing the review panel results. No separate file.

---

## Synthesis Framework

After all three reviewers complete, synthesize their findings into a single presentation for the Showrunner.

### Structure

```
## Review Panel Results

### Accuracy (Scientist / Gemini)
- Overall accuracy: {high|medium|low}
- Verified claims: {count}
- Flagged issues: {list with severity}
- Key concern: {most important finding}

### Structure (Codex)
- Transition issues: {count and summary}
- Pacing issues: {count and summary}
- Repetition issues: {count and summary}
- Key concern: {most important finding}

### Craft (Claude)
- Outline adherence: {assessment}
- Narrative flow: {assessment}
- Key concern: {most important finding}

### Convergence
Where 2+ reviewers flagged the same area -- high confidence these need attention:
- {list}

### Divergence
Where reviewers disagreed or only one flagged an issue:
- {list with context for Showrunner judgment}

## Showrunner Decision Needed
Which feedback do you want to apply?
- [ ] Fix accuracy issues (Scientist flags)
- [ ] Rework transitions at {locations} (Structural review)
- [ ] Adjust pacing in {scenes} (Structural review)
- [ ] Strengthen {section} for narrative flow (Craft review)
- [ ] Other: ___
```

---

## Showrunner Decision Framework

The user is the Showrunner. Present findings clearly and let them decide. Key principles:

1. **Convergence signals confidence.** If Gemini and Codex both flag the same paragraph, it almost certainly needs work. Say so.

2. **Divergence signals a creative choice.** If only Codex flags a "slow" section but the Craft Reviewer says the pacing serves the emotional arc, present both views and let the Showrunner decide.

3. **Accuracy trumps craft.** If the Scientist flags a factual error, it must be fixed regardless of how well the sentence reads. Non-negotiable.

4. **Never auto-apply.** Even if all three reviewers agree on a fix, present it and wait. The Showrunner may have context the reviewers lack.

5. **Offer re-runs.** After revisions, offer to re-run specific reviewers. "Want me to have the Scientist re-check the accuracy of the revised section?"

---

## Revision Process (Phase D)

After the Showrunner selects which feedback to apply:

1. Read `03-draft-script.txt` and the accepted feedback items.
2. Apply changes, maintaining the Director's scene structure.
3. If accuracy issues were flagged, cross-reference fixes against the claims registry.
4. Save as `05-final-script.txt`.
5. Offer to re-run any reviewer on the revised script.
6. Present the final script to the Showrunner for sign-off.

### Partial Re-Review

If the Showrunner wants only one reviewer re-run:

```bash
# Re-run Scientist only
cat 05-final-script.txt | gemini "..." > 04a-accuracy-report-v2.json

# Re-run Structural only
cat 05-final-script.txt | codex exec "..." > 04b-structural-review-v2.txt
```

The Craft Reviewer (Claude) can re-review inline without a separate command.

---

## Artifact Summary

| File                        | Phase | Producer             |
|-----------------------------|-------|----------------------|
| `01-research-brief.json`    | Input | /research-brief      |
| `02-narrative-blueprint.json` | A   | Storyteller          |
| `02b-detailed-outline.json` | A     | Director             |
| `03-draft-script.txt`       | B     | Writer               |
| `04a-accuracy-report.json`  | C     | Scientist (Gemini)   |
| `04b-structural-review.txt` | C     | Structural (Codex)   |
| `05-final-script.txt`       | D     | Revision             |
