---
name: research-to-essay
description: Research-driven essay and post creation with thematic synthesis, citation management, and voice calibration. Use when creating Substack/LinkedIn posts, long-form essays synthesizing multiple sources, or publication-grade writing requiring web search, narrative arc, and proper attribution. Triggers include "research and write about [topic]" or "dig into this idea and write."
license: Complete terms in LICENSE.txt
---

# Research-to-Essay Skill

Systematic workflow for producing publication-grade essays from research. Handles multi-source synthesis, narrative construction, voice calibration, and citation management.

## Core Workflow

### 1. Intake & Planning

Parse user request to determine:
- **Format target**: Substack (1500-3000w), LinkedIn (150-300w), Academic (3000-8000w), or Executive Brief (500-1000w)
- **Topic & angle**: What question/claim is central?
- **Essay structure**: Which arc fits? (Persuasive, Exploratory, Diagnostic, Narrative-Conceptual, Synthesis)
  - Consult `references/essay-structures.md` for detailed arc patterns
- **Voice profile**: Which register? (Poetic Rigor, Professional Signal, Scholarly Precision, Surgical Clarity)
  - Consult `references/voice-profiles.md` for characteristics and forbidden patterns

**Output from this phase:** Research plan with target structure and voice

---

### 2. Research Execution

Conduct systematic research following source credibility hierarchy:

**Search strategy:**
- Start with **primary sources** (research papers, official data, technical documentation)
- Layer in **expert analysis** (domain specialists, academic reviews, investigative journalism)
- Add **informed commentary** (practitioner Substacks, conference talks) for applied context
- Avoid weak sources (social media speculation, content marketing, AI-generated farms)

**Source quality requirements:**
- Minimum 5-8 sources for persuasive essays
- Minimum 8-12 sources for exploratory essays
- Minimum 6-10 sources for diagnostic essays
- Always include strongest counter-argument sources
- Prioritize recent sources for rapidly-changing topics, foundational sources for stable concepts

**Citation extraction:**
- Record: title, URL, author, date, credibility tier (1-4), key claims
- Use `web_fetch` to read full articles when `web_search` snippets insufficient
- For each source, extract 3-5 core claims explicitly
- Tag sources with themes for clustering

Consult `references/research-patterns.md` for:
- Source credibility hierarchy (Tiers 1-4)
- Research strategy by essay type
- Quality checks and anti-patterns

---

### 3. Synthesis

Organize research into thematic structure using one of two methods:

**Method A: Manual thematic clustering** (for simpler essays)
- Group claims by theme, not by source
- Identify convergent claims (multiple sources agree) → high confidence
- Identify divergent claims (sources disagree) → flag as tension
- Map claim dependencies (which claims require which others)

**Method B: Script-assisted synthesis** (for complex multi-source essays)
- Create JSON file with sources in required format (see script usage below)
- Run `scripts/synthesize_sources.py <sources.json> <output.md>`
- Review generated synthesis report showing themes, convergence, tensions

**Script format:**
```json
[
  {
    "title": "Source Title",
    "url": "https://example.com",
    "source_type": "primary",
    "claims": ["Claim 1", "Claim 2"],
    "themes": ["theme1", "theme2"],
    "date": "2025-01-15",
    "credibility_tier": 1
  }
]
```

**Synthesis output:** Thematic map showing:
- Core themes with supporting sources
- Convergent evidence (agreement across sources)
- Divergent claims (tensions or debates)
- Gaps or under-supported areas

---

### 4. Drafting

Build essay iteratively using chosen structure template:

**Template selection:**
- Use `assets/essay-template.md` for Substack/long-form
- Use `assets/linkedin-template.md` for LinkedIn posts
- Adapt templates based on selected essay structure from Step 1

**Drafting principles:**
- **Lead with strongest material**: Hook in first paragraph, no throat-clearing
- **Integrate sources naturally**: Embed citations in argument flow, don't list separately
- **Section logic**: Each section should build necessarily on the previous
- **Evidence before abstraction**: Concrete examples, then pattern extraction
- **Tension acknowledgment**: Include counter-arguments and complications honestly
- **Progressive depth**: Can write full essay in one pass OR build iteratively:
  - Pass 1: Outline with section headers
  - Pass 2: Fill core argument sections
  - Pass 3: Add evidence and citations
  - Pass 4: Write intro/conclusion last

**Voice application:**
- Apply selected voice profile consistently (from Step 1)
- Check against forbidden patterns in `references/voice-profiles.md`
- Calibrate tone dimensions: warmth, certainty, abstraction, humor

**Citation style:**
- **Substack/LinkedIn**: Inline hyperlinks on key phrases, footnotes for tangential details
- **Academic**: Numbered footnotes/endnotes with full bibliography
- **Executive**: Minimal citation, only for key data points
- Always cite: empirical claims, direct quotes, novel frameworks, counter-intuitive findings
- Never cite: common knowledge, your own synthesis, widely-known facts

---

### 5. Refinement

Quality assurance checks before delivery:

**Structural review:**
- [ ] Hook is genuinely compelling (test: would you click "read more"?)
- [ ] Stakes are established early (why should reader care?)
- [ ] Each section advances the argument necessarily
- [ ] Conclusion reframes rather than summarizes
- [ ] Length appropriate to format (Substack: 1500-3000w, LinkedIn: 150-300w)

**Voice & style check:**
- [ ] Run `prose-polish` skill on draft
- [ ] Check for forbidden patterns in selected voice profile
- [ ] Verify tone consistency throughout
- [ ] Confirm readability for target audience

**Evidence & citation check:**
- [ ] Every major claim has warrant (evidence or citation)
- [ ] Primary sources used for factual claims
- [ ] Counter-arguments acknowledged with credible sources
- [ ] No citation decay (secondary sources when primary available)
- [ ] Links functional, citations complete

**Platform-specific polish:**
- **LinkedIn**: Paragraph breaks every 2-3 sentences, key phrases bolded, CTA included
- **Substack**: Section transitions smooth, footnotes formatted, metadata complete
- **Academic**: All citations complete, methodology transparent, limitations noted

---

### 6. Delivery

Present final essay as artifact with metadata:

**Include:**
- Complete essay in appropriate markdown format
- Word count and target audience notation
- Source list with tiers noted
- Key frameworks or concepts referenced
- Research date and any time-sensitivity notes

**Optional additions based on context:**
- Alternative versions for different platforms (e.g., Substack long-form + LinkedIn teaser)
- "Further Reading" section organized by theme
- Open questions or research gaps identified
- Suggested images or visual elements

---

## When to Use References

**Load these files as needed:**

- `references/voice-profiles.md` — When clarifying voice characteristics or checking against forbidden patterns
- `references/essay-structures.md` — When uncertain about narrative arc or need structure template
- `references/research-patterns.md` — When evaluating source quality, planning research strategy, or checking synthesis methodology

**Load scripts when:**
- `scripts/synthesize_sources.py` — When dealing with 8+ sources requiring systematic thematic clustering

---

## Quality Signals

**High-quality output:**
- Opens with genuine insight, not preamble
- Every paragraph necessary, no filler
- Sources integrated into argument, not appended
- Counter-arguments acknowledged, not buried
- Conclusion offers new lens, not recap
- Voice consistent and appropriate to format
- Citations complete and properly tiered
- Length justified by complexity, not padding

**Red flags:**
- Generic opening ("In today's world...")
- List structure when narrative needed
- No acknowledgment of complexity or tradeoffs
- All sources from same perspective
- Summary conclusion
- Inconsistent tone or register shifts
- Weak or missing citations for key claims
- Excessive length without proportional depth

---

## Iteration Protocol

After delivering draft, typical refinement requests:

- **"Make this more [voice]"** → Reload `references/voice-profiles.md` and adjust tone calibration
- **"Add more evidence for X"** → Return to research phase for specific claim
- **"This section feels weak"** → Restructure using `references/essay-structures.md` patterns
- **"Too long / too short"** → Audit for filler vs. density, adjust scope
- **"Challenge this argument"** → Load strongest counter-sources, revise tensions section

---

## Anti-Patterns to Avoid

- **Don't** search once and write—iterate research based on draft gaps
- **Don't** list sources separately from argument—integrate naturally
- **Don't** write intro first—write it last after you know what you said
- **Don't** ignore voice profile constraints—they prevent AI slop
- **Don't** cite weak sources when primary available—tier matters
- **Don't** pad length artificially—every paragraph must earn its keep
- **Don't** summarize in conclusion—reframe or extrapolate instead
