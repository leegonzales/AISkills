---
name: research-to-essay
description: Research-driven essay and post creation with thematic synthesis, citation management, and voice calibration. Use when creating Substack/LinkedIn posts, long-form essays synthesizing multiple sources, or publication-grade writing requiring web search, narrative arc, and proper attribution. Triggers include "research and write about [topic]" or "dig into this idea and write."
license: Complete terms in LICENSE.txt
---

# Research-to-Essay Skill

Systematic workflow for producing publication-grade essays from research. Handles multi-source synthesis, narrative construction, voice calibration, and citation management.

## Citation Fidelity Firewall (HARD GATE — never violate)

**Citing is reporting what a real source actually said. Writing persuasively is not the same as inventing the evidence.** Every citation, statistic, study name, author-year, institution, direct quote, finding, and URL in the essay MUST come from a `web_search` or `web_fetch` you **actually executed in this session** and whose result you **saw with your own eyes**. A fluent sentence resting on a fabricated source is a *fabrication*, not an essay — no matter how plausible it reads or how perfectly it fits the argument. This is the same failure class as fabricating an author's anecdote during prose polishing: persuasive surface, invented substance.

**The hard rule: no retrieved source → no citation.** If you did not run a search/fetch that returned a given source, you may not cite it, name it, link to it, or attribute a claim to it. Before writing any citation, you must be able to point to the specific tool call in *this session* whose output contains that exact source. If you cannot, the citation does not exist.

**You must STOP — not improvise — when research is thin.** If research was never run, or ran but returned too little to support the essay, you have exactly these honest moves, in order:

1. **Run the searches now** — execute the `web_search`/`web_fetch` calls and cite only what comes back.
2. **Tell the user you cannot cite responsibly** — say plainly that the available verified sources are insufficient, and ask whether to research further or proceed with explicitly uncited, clearly-hedged claims.
3. **Reduce the claim to match the evidence** — soften or cut any assertion you cannot ground in a retrieved source, rather than manufacturing support for it.

You may **NEVER** manufacture a citation, author name, author-year, institution, study title, statistic, finding, or link to satisfy a structural target. The "5-8 sources" / "8-12 sources" / "6-10 sources" minimums (see Step 2) are a **floor on VERIFIED sources actually retrieved this session — not a quota to pad toward.** If you have four real sources, you have four; invent a fifth and the whole essay is compromised. Falling short of the floor is a signal to research more or narrow the claim, never to fabricate.

**Every URL must be one you actually retrieved.** Do not construct, guess, autocomplete, or "reconstruct from memory" plausible-looking URLs (e.g. a `stanford.edu/hai/...` path that *looks* right). A URL you did not see returned by a tool is a fabricated URL even if the domain is real. When in doubt about whether you actually retrieved a source, treat it as not retrieved and remove the citation.

**This gate outranks every stylistic, structural, and completeness goal in this skill.** The "Evidence & citation check" in Step 5 and the "always cite empirical claims" rule in Step 4 presuppose this firewall: a citation only counts if it passed this gate first.

**Final pass — provenance re-check:** before delivering, walk every citation, statistic, quote, and URL in the essay and confirm each traces to a tool result you saw this session. Roll back any you cannot trace. This check outranks every other quality signal.

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

**Source quality requirements:** *(these minimums are a floor on VERIFIED sources you actually retrieved this session via `web_search`/`web_fetch` — see the Citation Fidelity Firewall above. Never pad toward a number by inventing sources; falling short means research more or narrow the claim.)*
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

**Evidence & citation check:** *(presupposes the Citation Fidelity Firewall — a citation only counts if every author, statistic, quote, and URL traces to a `web_search`/`web_fetch` result you saw this session)*
- [ ] **Provenance verified**: every citation, statistic, study name, quote, and URL traces to a tool call you actually executed this session — none manufactured, none reconstructed from memory
- [ ] Every major claim has warrant (evidence or citation)
- [ ] Primary sources used for factual claims
- [ ] Counter-arguments acknowledged with credible sources
- [ ] No citation decay (secondary sources when primary available)
- [ ] Links functional and actually retrieved (not plausible-looking URLs you constructed), citations complete

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
- **Don't** EVER manufacture a citation, author, statistic, or URL to hit a source count—an invented Tier-1-looking source is the worst failure this skill can produce (see Citation Fidelity Firewall)
- **Don't** pad length artificially—every paragraph must earn its keep
- **Don't** summarize in conclusion—reframe or extrapolate instead
