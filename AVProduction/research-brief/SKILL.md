---
name: research-brief
description: Use when researching a topic to produce a structured brief with claims registry, stories, and emotional anchors for video production or general research. Spawns a Researcher teammate that uses web search to find real facts, then optionally fact-checks claims via Gemini CLI. Triggers include "/research-brief", "research this topic", or "build a research brief for".
---

# Research Brief Skill

Research a topic and produce a structured brief with a full claims registry. Output is JSON on disk, ready for downstream consumption by `/write-script` or any process that needs grounded, structured research.

## When to Use

- Researching a topic for video production (documentary, corporate, kids, technical, entertainment)
- Building a structured evidence base for any creative or analytical project
- Generating a claims registry with confidence ratings and source tracking
- Finding stories, emotional anchors, and Burke Chains (cross-domain connections)

## How to Use

```
/research-brief "Why self-report surveys fail for AI training measurement"
/research-brief "The history of zero" --type documentary
```

**Intake** -- Gather from user: topic (required), video type (optional: documentary/corporate/kids/technical/entertainment), additional context, source material file paths, working directory (default: `output/{slug}/writers-room/`).

**Research** -- Spawn a Researcher teammate via Task tool using `references/researcher-prompt.md`. The teammate uses web search to find facts, stories, Burke Chains, and emotional anchors. Writes `01-research-brief.json`.

**Fact-Check (optional)** -- Pipe the brief through Gemini CLI for independent claim verification. See `references/researcher-prompt.md` for the command template and disagreement matrix.

**Present & Iterate** -- Summarize findings, highlight low-confidence claims and Gemini disagreements, ask user whether to dig deeper or proceed to `/write-script`.

## Output Format

Output file: `01-research-brief.json`

```json
{
  "keyFacts": [{ "claim": "...", "source": "...", "confidence": "verified|likely|unverified" }],
  "stories": [{ "title": "...", "characters": ["..."], "stakes": "...", "surprise": "..." }],
  "emotionalAnchors": ["..."],
  "burkeChains": [{ "from": "...", "to": "...", "link": "..." }],
  "missingContext": ["..."],
  "claimsRegistry": [{
    "id": "C1",
    "text": "Atomic testable assertion",
    "type": "factual|causal|statistical|historical|definitional",
    "source": "Paper, study, incident report",
    "confidence": "verified|likely|unverified",
    "supports": ["C3"],
    "assumes": ["C5"]
  }]
}
```

## Integration

- **Standalone:** User provides topic, gets structured research brief
- **Downstream:** `/write-script` reads `01-research-brief.json`
- **General purpose:** Any research task needing structured claims with provenance

## Best Practices

- Let the Researcher finish before reviewing -- don't interrupt the search process
- Use Gemini fact-check for high-stakes topics or when many claims are "unverified"
- Iterate on specific claims rather than re-running the entire research phase
- Provide source material file paths when you have existing documents to ground the research
- Review the `missingContext` array -- it tells you what the Researcher could not find
