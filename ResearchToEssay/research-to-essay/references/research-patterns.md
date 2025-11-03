# Research Patterns

Heuristics for source evaluation, research strategy, and synthesis methodology.

## Source Credibility Hierarchy

### Tier 1: Primary Sources (Highest Authority)
- **Original research papers**: Peer-reviewed, methodology transparent
- **Primary data releases**: Government statistics, company earnings, raw datasets
- **First-person accounts**: Interviews, memoirs, direct observation (with context)
- **Official documentation**: Policy texts, legal documents, technical specifications
- **Company blogs from named engineers**: Original system design decisions

**Use for:** Empirical claims, technical specifications, direct quotes, establishing facts

**Red flags:** Preprint servers (not peer-reviewed), press releases as sole source

---

### Tier 2: Expert Analysis (High Authority in Domain)
- **Specialized technical blogs**: From recognized domain experts
- **Academic review papers**: Synthesizing multiple primary sources
- **Industry analyst reports**: From credentialed analysts (Gartner, Forrester—with caveats)
- **Think tank publications**: With transparent methodology and funding sources
- **Investigative journalism**: From outlets with editorial standards (NYT, WSJ, The Atlantic, The Verge for tech)

**Use for:** Contextualizing findings, domain-specific interpretation, trend analysis

**Red flags:** Anonymous experts, conflict of interest not disclosed, single-source claims

---

### Tier 3: Informed Commentary (Medium Authority)
- **Substacks from practitioners**: Domain-specific, first-person experience
- **Podcasts with credentialed guests**: When transcript or detailed notes available
- **Conference talks**: From practitioners or researchers
- **Technical documentation sites**: Stack Overflow accepted answers, official docs
- **News aggregators**: When citing multiple primary sources

**Use for:** Practical insights, lived experience, emerging patterns, community sentiment

**Red flags:** No cited sources, speculation presented as fact, engagement farming

---

### Tier 4: Weak or Unreliable (Low Authority)
- **Social media posts**: Unless from verified domain expert as primary source
- **Content marketing**: Whitepapers with clear commercial agenda
- **Wikipedia**: As starting point only, chase citations to primary sources
- **Anonymous forums**: Reddit, HN comments (directionally useful, not citable)
- **AI-generated content farms**: Especially post-2023

**Use for:** Identifying questions to research, discovering terminology, never as final source

**Red flags:** SEO-optimized listicles, no author attribution, circular citations

---

## Research Strategy by Essay Type

### For Persuasive Essays
**Goal:** Build airtight case for claim

**Search strategy:**
1. Find strongest counter-argument first (steelman opposition)
2. Locate primary data supporting your claim
3. Find expert validation from credible sources
4. Identify comparable cases or precedents

**Minimum sources:** 5-8 (mix of primary and expert analysis)

**Citation density:** High—every major claim needs warrant

---

### For Exploratory Essays
**Goal:** Map terrain comprehensively

**Search strategy:**
1. Identify 3-5 distinct perspectives on the question
2. Find primary sources representing each perspective
3. Look for empirical data that cuts across perspectives
4. Seek out dissenting or edge-case examples

**Minimum sources:** 8-12 (emphasize diversity of viewpoint)

**Citation density:** Medium—establish perspectives, let synthesis breathe

---

### For Diagnostic Essays
**Goal:** Explain underlying structure

**Search strategy:**
1. Document symptoms widely (multiple case studies)
2. Find prior attempts to explain (what was tried, why it failed)
3. Locate structural analogies from other domains
4. Identify feedback loops and reinforcing patterns in data

**Minimum sources:** 6-10 (mix of cases and structural analysis)

**Citation density:** Medium-high—establish pattern, then interpret

---

## Synthesis Methodology

### Thematic Clustering
**Process:**
1. Read all sources with claim extraction active
2. Group claims by theme, not by source
3. Identify convergent claims (multiple sources agree)
4. Identify divergent claims (sources disagree—flag as tension)
5. Map dependencies (Claim A requires Claim B)

**Output:** Thematic map with supporting sources per theme

---

### Temporal Analysis
**Use when:** Topic has evolved over time

**Process:**
1. Sort sources chronologically
2. Identify inflection points (when consensus shifted)
3. Note what evidence caused shifts
4. Track prediction accuracy of earlier sources

**Output:** Timeline of conceptual evolution

---

### Conflict Mapping
**Use when:** Multiple competing frameworks exist

**Process:**
1. Steelman each competing view
2. Identify empirical disagreements (can be tested) vs. value disagreements (can't)
3. Check if disagreements are substantive or terminological
4. Look for hidden agreements or orthogonal concerns

**Output:** Tension map showing genuine vs. apparent conflicts

---

## Research Quality Checks

### Before Starting Research
- [ ] Query is specific enough to return focused results
- [ ] Timeframe specified if topic is time-sensitive
- [ ] Key terms and synonyms identified
- [ ] Potential bias in framing acknowledged

### During Research
- [ ] Am I finding sources that challenge my priors?
- [ ] Are sources citing each other (check for independence)?
- [ ] Is there geographic/demographic/ideological diversity?
- [ ] Am I falling into confirmation bias?

### Before Synthesis
- [ ] Do I have primary sources for key factual claims?
- [ ] Have I found the strongest counter-argument?
- [ ] Are there obvious gaps in the evidence?
- [ ] Is source recency appropriate for claim type?

---

## Citation Practices

### When to Cite
- Every empirical claim not in common knowledge
- Direct quotes or close paraphrases
- Specific data points or statistics
- Novel frameworks or theories from named sources
- Counter-intuitive claims that need authority
- Technical specifications or methodologies

### When Not to Cite
- Common knowledge in the field
- Your own analysis or synthesis
- Widely known historical facts
- Simple definitions
- Logical inferences from cited premises

### Citation Style
**For Substack/LinkedIn:**
- Inline hyperlinks on key phrases (not naked URLs)
- Footnotes for tangential sources or methodology notes
- "According to [Source]" for direct attribution
- Avoid academic citation formats (APA, MLA) unless required

**Example:**
> Research from Stanford's Institute for Human-Centered AI shows that...  
> [Link embedded on "Stanford's Institute for Human-Centered AI"]

**For Academic/Formal:**
- Numbered footnotes or endnotes
- Full citation details in bibliography
- Follow specified format (APA, Chicago, etc.)

---

## Anti-Patterns to Avoid

### Citation Decay
**Problem:** Citing secondary sources that cite primary sources  
**Fix:** Always chase back to the primary source

### Ghost Attribution
**Problem:** "Studies show..." or "Experts say..." without naming which studies/experts  
**Fix:** Name the source or don't make the claim

### Recency Bias
**Problem:** Only citing recent sources when historical context needed  
**Fix:** Include foundational sources where relevant

### Authority Laundering
**Problem:** Using Tier 3/4 sources as if they're Tier 1/2  
**Fix:** Explicitly calibrate confidence to source quality

### Source Monoculture
**Problem:** All sources from same ideological/geographic/professional bubble  
**Fix:** Actively seek diverse perspectives, especially dissent
