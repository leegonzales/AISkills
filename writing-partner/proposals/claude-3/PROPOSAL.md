# Claude 3 Implementation Proposal: Voice Calibration & Authenticity Detection

**Author:** Claude Sonnet 4.5
**Date:** 2025-12-18
**Status:** Design exploration
**Approach:** Embedding-first hybrid with active learning

---

## Executive Summary

This proposal takes a strong stance: **voice calibration is fundamentally a similarity search problem dressed up as style matching**. The system should operate like a forensic linguist with perfect memory of every sentence Lee has ever written, continuously asking "have I seen this person write like this before?"

The proposed architecture combines:
1. Dense embeddings for semantic similarity (what is being said)
2. Sparse feature extraction for stylistic patterns (how it's being said)
3. Active learning from corrections (evolution over time)
4. Few-shot dynamic retrieval from corpus (showing, not telling)

**Core Philosophy:** Trust the corpus over guidelines. Guidelines are useful signposts; actual writing samples are ground truth.

---

## 1. Voice Corpus Integration

### 1.1 Corpus Structure

```
WritingSamples/
├── published/           # Public writing (blog posts, essays)
├── private/            # Personal writing (journals, notes)
├── conversations/      # AI chat transcripts that became writing
├── drafts/            # Works in progress
└── corrections/       # Passages Lee edited for voice
```

Each sample stored as:
```markdown
---
id: unique-hash
date: 2025-12-18
type: essay|conversation|draft|correction
topic: [tags]
voice_mode: @strategist|@builder|etc
perplexity_score: 42.3
length_tokens: 850
---

[Content]
```

### 1.2 Indexing Strategy

**Dual-index architecture:**

#### Dense Index (Semantic)
- Model: `sentence-transformers/all-mpnet-base-v2` (768-dim embeddings)
- Granularity: Paragraph-level chunks (100-300 tokens)
- Vector store: ChromaDB or FAISS for local operation
- Metadata filters: type, topic, date range, voice_mode

**Why paragraph-level?** Sentences are too granular (lose context), full documents too coarse (dilute signal). Paragraphs preserve local coherence while enabling precise retrieval.

#### Sparse Index (Stylistic)
Extract and index:
- N-gram patterns (2-4 grams) weighted by TF-IDF
- Sentence length distribution (mean, variance, percentiles)
- Punctuation density and patterns
- Dialogue ratio
- Question frequency
- Transition word usage ("however", "but", "frankly")
- First-person voice ratio
- Contrarian markers ("actually", "really", "in fact")

Store as inverted index with occurrence counts and positions.

### 1.3 Corpus Bootstrapping

**Phase 1: Seed corpus (Week 1)**
- Collect 20-30 diverse writing samples
- Include: published essays, email threads turned insights, chat transcripts
- Manually tag voice_mode if known
- Run baseline perplexity analysis

**Phase 2: Incremental growth**
- Every accepted draft passage → corpus
- Every Lee correction → high-value corpus entry (flagged)
- Interview transcripts → conversation corpus
- Target: 100+ diverse samples within 3 months

**Phase 3: Automated enrichment**
- Prose-polish scores on all samples (establish baseline)
- Topic extraction via LDA or BERTopic
- Cross-reference detection (same idea expressed differently)

### 1.4 Corpus Query Interface

```python
class VoiceCorpus:
    def find_similar_semantic(self, text: str, k=5, filters=None) -> List[Sample]
        """Dense retrieval: what has Lee said about similar topics?"""

    def find_similar_stylistic(self, text: str, k=5) -> List[Sample]
        """Sparse retrieval: how does Lee write about anything?"""

    def find_hybrid(self, text: str, semantic_weight=0.6, k=5) -> List[Sample]
        """Weighted combination of both signals"""

    def find_corrections(self, pattern: str) -> List[Correction]
        """What has Lee explicitly corrected before?"""

    def find_by_voice_mode(self, mode: str, k=10) -> List[Sample]
        """Examples of specific reasoner in action"""
```

**Key insight:** Different query modes for different calibration needs. Sometimes you want semantic similarity ("has Lee written about this topic?"), sometimes stylistic ("does this sentence structure feel like Lee?").

---

## 2. Detection Approach

### 2.1 Multi-Layer Detection Pipeline

**Layer 1: Pattern Blocklist (Fast rejection)**
Hard-coded patterns from Lee's explicit tells:
- "You might think X... but actually Y" and derivatives
- "It's important to note that..."
- "In today's world..." / "In the modern era..."
- "At the end of the day..."
- Listicle headings with emoji + bold (🎯 **Key Insight:**)

**Exit condition:** If matched, flag immediately with 95% confidence. No need for deeper analysis.

**Why this layer?** Fast, interpretable, catches the obvious offenders. Lee has explicitly named these patterns. Trust him.

---

**Layer 2: Prose-Polish Integration (AI detection)**
Run draft through existing prose-polish skill:
- Overall AI-likelihood score (0-100)
- Per-paragraph scores
- Flagged phrases with confidence

**Threshold calibration:**
- Score < 15: Likely human, minimal review
- Score 15-35: Borderline, deeper analysis needed
- Score > 35: Likely AI, flag for revision

**Why integrate prose-polish?** It's already built, already tuned. Don't reinvent. Leverage the multi-layer craft assessment (rhythm, voice, commitment) that prose-polish provides.

---

**Layer 3: Corpus Deviation Score (Voice drift)**

For each paragraph in draft:
1. Retrieve top-k semantically similar paragraphs from corpus
2. Retrieve top-k stylistically similar paragraphs from corpus
3. Compute deviation scores:

```python
def voice_drift_score(draft_para: str) -> VoiceDrift:
    # Semantic similarity (0-1, cosine distance)
    semantic_matches = corpus.find_similar_semantic(draft_para, k=10)
    semantic_sim = mean([match.similarity for match in semantic_matches])

    # Stylistic similarity (custom metric)
    style_matches = corpus.find_similar_stylistic(draft_para, k=10)
    style_features_draft = extract_style_features(draft_para)
    style_features_corpus = [extract_style_features(m.text) for m in style_matches]

    style_sim = compute_style_similarity(
        style_features_draft,
        style_features_corpus
    )

    # Hybrid score (weighted)
    hybrid_score = (0.4 * semantic_sim) + (0.6 * style_sim)

    # Confidence: how consistent are top matches?
    confidence = 1.0 - std_dev([m.similarity for m in semantic_matches])

    return VoiceDrift(
        semantic_similarity=semantic_sim,
        style_similarity=style_sim,
        hybrid_score=hybrid_score,
        confidence=confidence,
        closest_matches=semantic_matches[:3]
    )
```

**Thresholds:**
- hybrid_score > 0.75: Strong match, keep
- hybrid_score 0.6-0.75: Borderline, suggest alternatives
- hybrid_score < 0.6: Weak match, likely needs revision

**Why 60/40 weight toward style?** Lee's complaint is not about topics (semantic) but about "doesn't sound like me" (style). Topics can be new; voice should be consistent.

---

**Layer 4: Perplexity Analysis (Soullessness detection)**

Compute sentence-level perplexity using GPT-2 or similar language model:
- Low perplexity = predictable, "grammatically perfect but soulless"
- High perplexity = surprising, potentially more authentic
- Lee's writing should have moderate-to-high perplexity in specific places

**Baseline from corpus:**
- Extract perplexity distribution from Lee's samples
- Flag sentences with z-score < -1.5 (too predictable)

**Nuance:** Not all low-perplexity is bad. Transitions and setup sentences are naturally predictable. Flag low-perplexity in *key insight sentences* or *narrative moments*.

```python
def flag_soulless_sentences(paragraph: str, corpus_baseline) -> List[Flag]:
    sentences = split_sentences(paragraph)
    flags = []

    for i, sent in enumerate(sentences):
        perplexity = compute_perplexity(sent)
        z_score = (perplexity - corpus_baseline.mean) / corpus_baseline.std

        # Only flag if it's a content sentence (not transition)
        if z_score < -1.5 and not is_transition_sentence(sent):
            flags.append(Flag(
                sentence=sent,
                position=i,
                perplexity=perplexity,
                reason="Too predictable for Lee's voice",
                severity="medium"
            ))

    return flags
```

---

### 2.2 Aggregated Detection Output

For each draft paragraph, produce:

```json
{
  "paragraph_id": 3,
  "text": "[paragraph text]",
  "flags": {
    "blocklist_match": {
      "matched": true,
      "pattern": "You might think X but actually Y",
      "confidence": 0.95
    },
    "prose_polish": {
      "ai_score": 42,
      "flagged_phrases": ["It's important to note", "in today's world"],
      "craft_issues": ["low commitment", "generic rhythm"]
    },
    "voice_drift": {
      "hybrid_score": 0.58,
      "semantic_similarity": 0.71,
      "style_similarity": 0.49,
      "closest_matches": [
        {"text": "[sample 1]", "similarity": 0.73},
        {"text": "[sample 2]", "similarity": 0.71}
      ]
    },
    "perplexity": {
      "mean": 28.3,
      "z_score": -1.8,
      "flagged_sentences": [
        {"text": "This is a transformative approach.", "perplexity": 12.4}
      ]
    }
  },
  "overall_authenticity": 0.42,  // Weighted combination
  "recommendation": "revise"      // keep | suggest | revise
}
```

**Weighting for overall_authenticity:**
- Blocklist match: Automatic 0.0 (override everything)
- Prose-polish: 30%
- Voice drift: 50%
- Perplexity: 20%

---

## 3. Prose-Polish Integration

### 3.1 Bidirectional Integration

**Detection flow:**
```
Draft → Voice Calibration → Prose-Polish → Combined Report
```

**Why this order?** Voice calibration is Lee-specific. Prose-polish is general AI detection. Voice calibration can pre-filter obvious issues, then prose-polish provides craft-level analysis.

### 3.2 Leveraging Prose-Polish Capabilities

Prose-polish already provides:
1. **AI likelihood scoring** - Multi-layer assessment
2. **Craft analysis** - Rhythm, voice, commitment
3. **Remediation suggestions** - How to improve flagged passages

**Integration points:**

#### Use prose-polish for:
- **Baseline AI detection** (Layer 2 in pipeline)
- **Craft quality check** (after voice is calibrated)
- **Generic improvement suggestions** (when voice is right but craft is weak)

#### Voice calibration adds:
- **Lee-specific pattern detection** (blocklist)
- **Corpus comparison** (has Lee written like this before?)
- **Few-shot alternatives** (show how Lee would say this)

### 3.3 Conflict Resolution

**Scenario:** Prose-polish says "good", voice calibration says "doesn't sound like Lee"

**Resolution:** Voice calibration wins. The goal is Lee's voice, not generic good writing.

**Scenario:** Prose-polish says "AI-generated", voice calibration says "matches corpus"

**Resolution:** Investigate. Either:
- Lee's corpus contains AI-generated passages (needs corpus cleaning)
- Prose-polish is overcalibrated (threshold adjustment needed)
- This is a novel voice evolution (accept with caution)

Default: Flag for manual review.

### 3.4 Shared Metadata

Both systems should tag passages with:
```yaml
author_confidence: 0.0-1.0  # How confident this is Lee
ai_confidence: 0.0-1.0      # How confident this is AI
craft_quality: 0.0-1.0      # How good is the writing
needs_review: boolean
```

**Decision matrix:**

| author_conf | ai_conf | craft | Action |
|-------------|---------|-------|--------|
| high | low | high | **Keep** - ideal state |
| high | low | low | **Improve craft** - use prose-polish |
| low | high | any | **Revise voice** - use corpus alternatives |
| med | med | high | **Manual review** - borderline |

---

## 4. Remediation Strategies

### 4.1 Three-Tier Remediation

**Tier 1: Show, don't tell (Preferred)**

When a passage fails voice calibration:
1. Retrieve 3-5 corpus examples where Lee wrote about similar topics
2. Present side-by-side:

```
❌ Draft version:
"In today's world, AI-assisted writing is becoming increasingly important.
It's important to note that maintaining authentic voice remains a challenge."

📚 How Lee wrote about similar topics:

Example 1 (from essay "Intellectual Prosthesis"):
"I made prose-polish to make my writing better, and to improve Claude's
writing. Not because AI is bad—but because collaborative emergence needs
both human spark and AI elevation."

Example 2 (from conversation transcript):
"Frankly, I love digressions and side quests. That's how my mind works.
Things bubble in my subconscious, then snap into reality as insights."

💡 Notice the difference:
- Lee uses first-person, owns his perspective
- Specific verbs (made, love, bubble, snap)
- No hedging or "it's important to note"
- Direct, heartfelt tone
```

**Psychological principle:** Seeing concrete examples is more actionable than abstract guidelines. Lee can pattern-match intuitively.

---

**Tier 2: Generative alternatives (When showing isn't enough)**

Use the corpus as few-shot context for LLM rewriting:

```python
def generate_voice_aligned_alternative(draft_text: str, corpus: VoiceCorpus) -> str:
    # Get similar passages from corpus
    examples = corpus.find_hybrid(draft_text, k=5)

    # Build few-shot prompt
    prompt = f"""
    Here are examples of how Lee Gonzales writes:

    {format_examples(examples)}

    Now rewrite this passage in Lee's voice:
    {draft_text}

    Preserve the core meaning but match Lee's style:
    - First-person ownership
    - Specific, concrete verbs
    - No hedging or corporate speak
    - Heartfelt, direct tone
    """

    return llm_generate(prompt)
```

**Critical:** The few-shot examples are doing the heavy lifting. The instructions are backup.

---

**Tier 3: Structured guidance (Last resort)**

When Tier 1 and 2 fail, provide actionable rewrites:

```
🔧 Voice calibration issues:

Problem: Generic opening
Location: Paragraph 1, sentence 1
Pattern: "In today's world..." (blocklist match)

Suggested fix:
- Remove temporal hedging
- Start with specific observation or question
- Use first-person if relevant

Example revision:
"I built prose-polish because I was tired of essays that sounded like
everyone and no one."
```

### 4.2 Correction Tracking

Every time Lee edits a flagged passage:
1. Store original + revised in `corrections/` corpus
2. Extract edit patterns (what changed, why)
3. Build correction classifier over time

**Pattern learning:**
```python
class CorrectionPattern:
    original_phrase: str
    revised_phrase: str
    context: str
    pattern_type: str  # word_choice | structure | tone | specificity
    frequency: int     # How many times Lee made this type of edit
```

After 20+ corrections, patterns emerge:
- Lee always removes "it's important to note"
- Lee changes "increasingly" to specific verbs
- Lee replaces abstract nouns with concrete examples
- Lee adds first-person ownership to claims

**Use corrections to:**
- Auto-flag similar patterns in future drafts
- Suggest Lee-specific alternatives
- Update blocklist dynamically

### 4.3 Interactive Remediation Flow

**Proposed UX:**

```
📝 Calibrating voice for paragraph 3...

⚠️  Voice drift detected (score: 0.58 - below threshold)

Issues found:
- [Blocklist] "It's important to note" (high confidence)
- [Style] Sentence complexity doesn't match corpus (z-score: -2.1)
- [Perplexity] Too predictable (perplexity: 14.2 vs corpus avg: 32.4)

📚 Here's how you wrote about similar topics:
[Shows 3 examples from corpus]

🤖 Suggested revision:
[Tier 2 generated alternative]

What would you like to do?
1. Accept suggested revision
2. Show more examples
3. Edit manually (I'll learn from your changes)
4. Keep as-is (mark as intentional deviation)
```

**Key principle:** Agency. Lee always has final say. System learns from his choices.

---

## 5. Few-Shot Selection

### 5.1 Dynamic Retrieval Strategy

**Problem:** Not all corpus examples are equally useful for a given draft passage.

**Solution:** Multi-criteria ranking for few-shot selection.

#### Selection Criteria

For draft passage P, rank corpus examples by:

```python
def rank_few_shot_examples(draft_passage: str, corpus: VoiceCorpus) -> List[Example]:
    candidates = corpus.find_similar_semantic(draft_passage, k=50)

    for candidate in candidates:
        score = compute_few_shot_score(candidate, draft_passage)

    return sorted(candidates, key=lambda c: c.score, reverse=True)[:5]

def compute_few_shot_score(example: Sample, draft: str) -> float:
    scores = {
        'semantic_sim': cosine_similarity(embed(example), embed(draft)),
        'length_match': 1.0 - abs(len(example) - len(draft)) / max(len(example), len(draft)),
        'voice_mode_match': 1.0 if example.voice_mode == current_voice_mode else 0.5,
        'recency': decay_function(example.date),  # Prefer recent writing
        'correction_count': example.times_lee_edited * 2.0,  # High-value examples
        'topic_overlap': jaccard_similarity(extract_topics(example), extract_topics(draft))
    }

    weights = {
        'semantic_sim': 0.3,
        'length_match': 0.1,
        'voice_mode_match': 0.15,
        'recency': 0.1,
        'correction_count': 0.25,  # Heavily weight examples Lee explicitly corrected
        'topic_overlap': 0.1
    }

    return sum(scores[k] * weights[k] for k in scores)
```

**Why weight corrections heavily?** Those are examples where Lee explicitly demonstrated "not this, but this." They're gold.

### 5.2 Diversity in Selection

**Problem:** Top-5 by similarity might all be from same essay (redundant).

**Solution:** Diversity-aware selection.

```python
def select_diverse_examples(ranked_examples: List[Example], k=5) -> List[Example]:
    selected = [ranked_examples[0]]  # Always take top match

    for candidate in ranked_examples[1:]:
        if len(selected) >= k:
            break

        # Check diversity against already selected
        min_similarity = min([
            cosine_similarity(candidate, s) for s in selected
        ])

        # Only add if sufficiently different from existing selections
        if min_similarity < 0.85:
            selected.append(candidate)

    return selected
```

**Goal:** Show range of how Lee writes, not just one essay's style.

### 5.3 Context-Aware Selection

**Match selection to draft stage:**

| Draft Stage | Selection Priority |
|-------------|-------------------|
| Opening paragraph | Examples of strong openings (first para of essays) |
| Argument building | Examples with evidence/reasoning |
| Narrative moments | Examples with story or anecdote |
| Conclusions | Examples of synthesis/call-to-action |

**Implementation:**
```python
def context_aware_selection(draft_passage: str, position: str) -> List[Example]:
    base_candidates = corpus.find_hybrid(draft_passage, k=100)

    if position == 'opening':
        # Filter for first paragraphs
        candidates = [c for c in base_candidates if c.position == 'first_para']
    elif position == 'narrative':
        # Filter for high dialogue/story markers
        candidates = [c for c in base_candidates if c.has_narrative_markers]
    else:
        candidates = base_candidates

    return select_diverse_examples(candidates, k=5)
```

### 5.4 Few-Shot Prompt Construction

**Template for generative remediation:**

```python
def build_few_shot_prompt(draft: str, examples: List[Example]) -> str:
    prompt_parts = [
        "You are helping rewrite a passage to match Lee Gonzales's writing voice.",
        "",
        "Here are examples of how Lee writes:",
        ""
    ]

    for i, ex in enumerate(examples, 1):
        prompt_parts.extend([
            f"Example {i}:",
            f"Topic: {ex.topic}",
            f"Voice mode: {ex.voice_mode}",
            f'"""',
            ex.text,
            f'"""',
            ""
        ])

    prompt_parts.extend([
        "Now rewrite this passage to match Lee's voice:",
        f'"""',
        draft,
        f'"""',
        "",
        "Key voice characteristics to preserve:",
        "- First-person ownership",
        "- External processing style (thinking out loud)",
        "- Specific verbs and concrete details",
        "- Heartfelt directness",
        "- No corporate hedging or AI tells",
        "",
        "Rewritten passage:"
    ])

    return "\n".join(prompt_parts)
```

**Why include metadata?** Helps the model understand the context of each example (topic, voice mode), not just mimic surface patterns.

---

## 6. Voice Profile Evolution

### 6.1 Active Learning Architecture

**Core insight:** Every interaction where Lee accepts, rejects, or edits is a training signal.

#### Feedback Loop

```
Draft → Detection → Remediation → Lee's Action → Profile Update
```

**Lee's actions:**
1. **Accept suggested revision** → Positive signal for retrieval/remediation
2. **Reject suggestion, edit manually** → Negative signal + capture new pattern
3. **Mark passage as good** → Add to corpus (high confidence)
4. **Mark intentional deviation** → Don't penalize, track as exception

### 6.2 Profile Components

**Static profile (infrequent updates):**
- Blocklist patterns (explicit tells to avoid)
- Voice guidelines (from interview, VOICE.md)
- Preferred reasoner modes
- Topic expertise areas

**Dynamic profile (updates with every interaction):**

```python
class DynamicVoiceProfile:
    # Pattern frequencies
    ngram_preferences: Dict[str, float]  # "frankly" → 0.85 (Lee uses it)
    sentence_length_dist: Distribution   # Updated from accepted passages

    # Correction patterns
    common_edits: List[CorrectionPattern]
    auto_flags: List[str]  # Patterns Lee always corrects

    # Corpus weights
    example_weights: Dict[str, float]  # example_id → effectiveness score

    # Drift tracking
    recent_acceptances: Deque[Sample]  # Last 50 accepted passages
    recent_rejections: Deque[Sample]   # Last 50 rejected passages

    # Temporal evolution
    voice_snapshot_history: List[VoiceSnapshot]  # Monthly snapshots
```

### 6.3 Learning from Corrections

**When Lee edits a flagged passage:**

```python
def learn_from_correction(original: str, revised: str, context: str):
    # Extract edit operations
    edits = diff(original, revised)

    for edit in edits:
        if edit.type == 'deletion':
            # Lee removed this phrase → add to blocklist candidates
            pattern = extract_pattern(edit.content)
            update_blocklist_candidate(pattern, confidence=0.7)

        elif edit.type == 'replacement':
            # Lee changed X to Y → learn preference
            correction_pattern = CorrectionPattern(
                original_phrase=edit.old,
                revised_phrase=edit.new,
                context=context,
                pattern_type=classify_edit_type(edit)
            )
            add_correction_pattern(correction_pattern)

        elif edit.type == 'addition':
            # Lee added detail → learn expansion strategy
            track_addition_context(edit.content, context)

    # Store complete correction
    corpus.add_correction(original, revised, context, high_value=True)

    # Update retrieval weights
    if was_similar_to_examples(original, retrieved_examples):
        # Those examples didn't help → downweight
        for ex in retrieved_examples:
            profile.example_weights[ex.id] *= 0.9
```

### 6.4 Blocklist Evolution

**Dynamic blocklist management:**

```python
class DynamicBlocklist:
    confirmed_patterns: List[Pattern]    # Lee explicitly named these
    candidate_patterns: Dict[Pattern, CandidateStats]

    def add_candidate(self, pattern: str, source: str):
        """Add pattern Lee corrected but hasn't explicitly confirmed"""
        if pattern not in self.candidate_patterns:
            self.candidate_patterns[pattern] = CandidateStats(
                occurrences=1,
                corrections=1,
                false_positives=0
            )
        else:
            self.candidate_patterns[pattern].corrections += 1

    def promote_candidate(self, pattern: str):
        """Promote to confirmed after sufficient evidence"""
        stats = self.candidate_patterns[pattern]
        confidence = stats.corrections / (stats.corrections + stats.false_positives)

        if stats.corrections >= 3 and confidence > 0.85:
            self.confirmed_patterns.append(Pattern(
                text=pattern,
                source='learned',
                confidence=confidence
            ))
            return True
        return False

    def handle_false_positive(self, pattern: str):
        """Lee marked this match as acceptable"""
        if pattern in self.candidate_patterns:
            self.candidate_patterns[pattern].false_positives += 1
```

**Human-in-the-loop confirmation:**

Every 25 corrections, surface candidates for review:
```
📊 Voice profile learning summary:

I've noticed you consistently remove these patterns:
1. "It's worth noting that..." (corrected 4/4 times)
2. "This highlights the importance of..." (corrected 3/3 times)
3. "One key takeaway is..." (corrected 5/6 times)

Should I auto-flag these in future drafts?
- Yes, add to blocklist
- Not yet, keep tracking
- No, these were context-specific
```

### 6.5 Corpus Quality Management

**Problem:** As corpus grows, quality dilutes if not managed.

**Solution:** Weighted corpus with quality indicators.

```python
class CorpusSample:
    text: str
    metadata: Dict
    quality_indicators: QualityMetrics

class QualityMetrics:
    source_type: str  # published | draft | correction | conversation
    lee_approved: bool
    prose_polish_score: float
    usage_count: int  # How often retrieved in few-shot
    success_rate: float  # How often Lee accepts passages influenced by this

    @property
    def corpus_weight(self) -> float:
        """Compute overall quality weight for retrieval"""
        weights = {
            'published': 1.0,
            'correction': 1.5,  # Lee explicitly refined these
            'draft': 0.7,
            'conversation': 0.8
        }

        base_weight = weights.get(self.source_type, 0.5)

        # Boost for approval and success
        if self.lee_approved:
            base_weight *= 1.3

        # Boost for proven utility
        if self.usage_count > 10:
            base_weight *= (1.0 + 0.1 * self.success_rate)

        # Penalize low prose-polish scores
        if self.prose_polish_score > 35:
            base_weight *= 0.5

        return base_weight
```

**Corpus pruning strategy:**

Every 3 months or 500+ samples:
1. Compute quality weights for all samples
2. Remove bottom 10% (lowest weight, rarely used)
3. Flag low-success examples for review
4. Deduplicate near-identical passages

### 6.6 Voice Drift Monitoring

**Concept:** Lee's voice will evolve over time. System should adapt, but warn of sudden changes.

```python
class VoiceDriftMonitor:
    def __init__(self):
        self.snapshots = []  # Monthly voice snapshots
        self.baseline = None

    def create_snapshot(self, date: datetime) -> VoiceSnapshot:
        """Capture current voice profile state"""
        recent_samples = corpus.get_recent_samples(days=30)

        return VoiceSnapshot(
            date=date,
            style_features=aggregate_style_features(recent_samples),
            ngram_distribution=compute_ngram_dist(recent_samples),
            perplexity_mean=mean([s.perplexity for s in recent_samples]),
            topic_distribution=extract_topics(recent_samples)
        )

    def detect_drift(self, current: VoiceSnapshot, baseline: VoiceSnapshot) -> DriftReport:
        """Compare current voice to baseline"""
        style_distance = cosine_distance(
            current.style_features,
            baseline.style_features
        )

        ngram_shift = kl_divergence(
            current.ngram_distribution,
            baseline.ngram_distribution
        )

        perplexity_change = abs(current.perplexity_mean - baseline.perplexity_mean)

        # Flag significant drift
        if style_distance > 0.3 or ngram_shift > 0.4:
            return DriftReport(
                severity='high',
                style_distance=style_distance,
                ngram_shift=ngram_shift,
                recommendation='review_recent_samples'
            )

        return DriftReport(severity='normal')
```

**When to alert Lee:**

```
⚠️  Voice drift detected

Your writing style has shifted noticeably in the past month:
- Sentence complexity increased (mean: 18 → 24 words)
- First-person usage decreased (32% → 18%)
- New frequent phrases: "fundamentally", "structural"

This could mean:
1. Natural evolution (new topics, new thinking)
2. AI influence creeping in
3. Different voice mode emerging

Review recent samples? [Yes/No]
```

**Key insight:** Don't prevent evolution. Just make it visible and intentional.

---

## 7. Implementation Roadmap

### Phase 1: Foundation (Weeks 1-2)

**Goals:**
- Corpus infrastructure in place
- Basic retrieval working
- Pattern blocklist operational

**Tasks:**
1. Set up ChromaDB or FAISS vector store
2. Implement dual-index (dense + sparse)
3. Collect and index initial 20-30 writing samples
4. Code pattern blocklist (hard-coded from interview)
5. Build basic CLI for corpus queries

**Deliverable:** Can query "find similar to [text]" and get meaningful results.

---

### Phase 2: Detection Pipeline (Weeks 3-4)

**Goals:**
- Multi-layer detection working
- Integration with prose-polish
- Output structured reports

**Tasks:**
1. Implement Layer 1 (blocklist matching)
2. Integrate prose-polish as Layer 2
3. Implement Layer 3 (corpus deviation scoring)
4. Implement Layer 4 (perplexity analysis)
5. Build aggregated report generator

**Deliverable:** Can analyze a draft and produce actionable voice calibration report.

---

### Phase 3: Remediation (Weeks 5-6)

**Goals:**
- Show corpus examples (Tier 1)
- Generate alternatives (Tier 2)
- Interactive correction flow

**Tasks:**
1. Build few-shot selection logic
2. Implement context-aware retrieval
3. Build generative remediation with few-shot prompts
4. Design and implement interactive UX
5. Set up correction tracking

**Deliverable:** Can suggest voice-aligned alternatives with corpus backing.

---

### Phase 4: Learning System (Weeks 7-8)

**Goals:**
- Learn from corrections
- Dynamic blocklist
- Corpus quality management

**Tasks:**
1. Implement correction pattern extraction
2. Build dynamic blocklist with promotion logic
3. Implement corpus weighting system
4. Build voice drift monitoring
5. Create monthly snapshot and review flow

**Deliverable:** System improves over time from Lee's edits.

---

### Phase 5: Integration & Polish (Weeks 9-10)

**Goals:**
- Integrate into writing-partner skill
- End-to-end testing
- Documentation

**Tasks:**
1. Integrate voice calibration into skill modes
2. Test on prose-polish essay revision
3. Test on new essay creation
4. Write documentation for corpus management
5. Create onboarding flow for corpus bootstrapping

**Deliverable:** Production-ready skill with voice calibration.

---

## 8. Technical Architecture

### 8.1 System Components

```
┌─────────────────────────────────────────────────────────┐
│                  Writing Partner Skill                   │
│  (Orchestration: Interview, Thread, Draft, Calibrate)    │
└─────────────────────┬───────────────────────────────────┘
                      │
                      │ Invokes during Draft/Calibrate
                      ▼
┌─────────────────────────────────────────────────────────┐
│              Voice Calibration Engine                    │
│                                                          │
│  ┌────────────┐  ┌────────────┐  ┌─────────────┐       │
│  │  Blocklist │  │   Prose-   │  │   Corpus    │       │
│  │  Matcher   │  │   Polish   │  │   Scorer    │       │
│  │  (Layer 1) │  │  (Layer 2) │  │  (Layer 3)  │       │
│  └────────────┘  └────────────┘  └─────────────┘       │
│                                                          │
│  ┌────────────────────────────────────────────┐         │
│  │    Perplexity Analyzer (Layer 4)            │         │
│  └────────────────────────────────────────────┘         │
│                                                          │
│  ┌────────────────────────────────────────────┐         │
│  │      Aggregator & Report Generator          │         │
│  └────────────────────────────────────────────┘         │
└─────────────────────┬───────────────────────────────────┘
                      │
                      │ Queries
                      ▼
┌─────────────────────────────────────────────────────────┐
│                  Voice Corpus                            │
│                                                          │
│  ┌──────────────────┐      ┌───────────────────┐       │
│  │  Dense Index     │      │   Sparse Index    │       │
│  │  (ChromaDB)      │      │   (Inverted)      │       │
│  │  768-dim vectors │      │   N-grams, Style  │       │
│  └──────────────────┘      └───────────────────┘       │
│                                                          │
│  ┌────────────────────────────────────────────┐         │
│  │          Samples Storage                    │         │
│  │  (published/ private/ conversations/        │         │
│  │   drafts/ corrections/)                     │         │
│  └────────────────────────────────────────────┘         │
└─────────────────────┬───────────────────────────────────┘
                      │
                      │ Learns from
                      ▼
┌─────────────────────────────────────────────────────────┐
│              Active Learning Module                      │
│                                                          │
│  ┌────────────────┐  ┌─────────────────────────┐       │
│  │  Correction    │  │  Dynamic Blocklist       │       │
│  │  Tracker       │  │  Manager                 │       │
│  └────────────────┘  └─────────────────────────┘       │
│                                                          │
│  ┌────────────────┐  ┌─────────────────────────┐       │
│  │  Corpus        │  │  Voice Drift             │       │
│  │  Weight Mgr    │  │  Monitor                 │       │
│  └────────────────┘  └─────────────────────────┘       │
└─────────────────────────────────────────────────────────┘
```

### 8.2 Data Flow

**Calibration request:**
```
1. Draft paragraph → Voice Calibration Engine
2. Engine runs all 4 layers in parallel
3. Each layer produces flags/scores
4. Aggregator combines into single report
5. Report includes few-shot examples from corpus
6. Remediation module generates alternatives
7. Present to Lee for action
```

**Learning from action:**
```
1. Lee's action (accept/reject/edit) → Active Learning Module
2. Module extracts patterns from edit
3. Updates dynamic blocklist candidates
4. Adjusts corpus weights
5. Stores correction in high-value corpus
6. Triggers drift monitoring check (if monthly threshold)
```

### 8.3 Storage Schema

**Corpus sample:**
```yaml
id: sha256-hash
metadata:
  date: 2025-12-18
  type: published
  source_file: essays/intellectual-prosthesis.md
  topic: [ai, writing, collaboration]
  voice_mode: @strategist
  length_tokens: 842
quality:
  lee_approved: true
  prose_polish_score: 18.5
  usage_count: 12
  success_rate: 0.83
  corpus_weight: 1.45
embeddings:
  dense_vector: [0.234, -0.521, ...]  # 768-dim
  sparse_features:
    ngrams: {"I wonder": 2, "frankly": 1, ...}
    sentence_lengths: [18, 22, 15, 31, ...]
    punctuation_density: 0.042
    first_person_ratio: 0.31
content:
  text: |
    [Full paragraph text]
  position: first_para
  has_narrative_markers: false
```

**Correction pattern:**
```yaml
id: correction-0042
date: 2025-12-18
original: "It's important to note that voice calibration is crucial."
revised: "Voice calibration matters because readers know when something doesn't sound like you."
context: |
  Paragraph about voice calibration in writing-partner proposal.
  Lee removed corporate hedging and added personal perspective.
pattern_type: tone_shift
edits:
  - type: deletion
    content: "It's important to note that"
    position: 0
  - type: replacement
    old: "is crucial"
    new: "matters because readers know when something doesn't sound like you"
    position: 50
classification:
  primary: remove_hedging
  secondary: add_specificity
frequency: 1
promoted_to_blocklist: false
```

**Dynamic blocklist entry:**
```yaml
pattern: "It's important to note"
type: phrase
confidence: 0.92
source: learned
evidence:
  corrections: 5
  false_positives: 0
  first_seen: 2025-12-10
  promoted: 2025-12-18
regex: null  # Optional: for pattern matching
case_sensitive: false
```

### 8.4 Configuration

**Voice calibration config:**
```yaml
detection:
  layers:
    blocklist:
      enabled: true
      confidence_threshold: 0.90

    prose_polish:
      enabled: true
      threshold_low: 15
      threshold_high: 35

    corpus_deviation:
      enabled: true
      semantic_weight: 0.4
      style_weight: 0.6
      threshold_keep: 0.75
      threshold_suggest: 0.60
      k_neighbors: 10

    perplexity:
      enabled: true
      z_score_threshold: -1.5
      exclude_transitions: true

  aggregation:
    weights:
      blocklist: 1.0  # Override weight
      prose_polish: 0.3
      corpus_deviation: 0.5
      perplexity: 0.2

remediation:
  tier1_examples: 5
  tier2_enabled: true
  diversity_threshold: 0.85

few_shot:
  selection_criteria:
    semantic_sim: 0.3
    length_match: 0.1
    voice_mode_match: 0.15
    recency: 0.1
    correction_count: 0.25
    topic_overlap: 0.1

learning:
  blocklist_promotion:
    min_corrections: 3
    min_confidence: 0.85

  corpus_pruning:
    interval_days: 90
    bottom_percentile: 10

  drift_monitoring:
    snapshot_interval_days: 30
    alert_threshold: 0.3
```

---

## 9. Risk Mitigation

### 9.1 Cold Start Problem

**Risk:** Empty or tiny corpus won't provide good few-shot examples.

**Mitigation:**
1. **Minimum viable corpus:** 20 diverse samples before going live
2. **Fallback to prose-polish only:** If corpus too small, rely on Layer 2
3. **Seed with interview transcript:** Lee's answers are authentic voice data
4. **Manual curation:** First 50 samples hand-picked for quality
5. **Progressive enablement:** Start with blocklist + prose-polish, add corpus scoring as it grows

### 9.2 Overfitting to Corpus

**Risk:** System penalizes novel but authentic voice evolutions.

**Mitigation:**
1. **Confidence scores:** Low-confidence flags are suggestions, not mandates
2. **Intentional deviation option:** Lee can mark passages as "new voice, keep it"
3. **Drift monitoring:** Track evolution over time, don't lock to old baseline
4. **Diversity in retrieval:** Don't just match closest sample, show range
5. **Monthly reviews:** Conscious decision to update baseline or revert

### 9.3 False Positives

**Risk:** Flagging passages that are actually fine.

**Mitigation:**
1. **Tiered recommendations:** keep | suggest | revise (not binary)
2. **Confidence thresholds:** Only hard-block on 90%+ confidence matches
3. **Human-in-loop:** Lee always has final say
4. **False positive tracking:** Learn from when Lee overrides system
5. **Context awareness:** Don't flag quote attributions or deliberate style mimicry

### 9.4 Corpus Contamination

**Risk:** AI-generated passages leak into corpus, diluting signal.

**Mitigation:**
1. **Source tagging:** All samples marked with origin (published, draft, AI-collab)
2. **Prose-polish gating:** Run all corpus additions through detection
3. **Lee approval required:** High-weight samples must be explicitly approved
4. **Periodic audits:** Review high-usage samples quarterly
5. **Correction prioritization:** Heavily weight samples Lee explicitly refined

### 9.5 Computational Cost

**Risk:** Real-time embedding/detection too slow for interactive use.

**Mitigation:**
1. **Paragraph-level batching:** Process full draft at once, not word-by-word
2. **Caching:** Cache embeddings for draft paragraphs during revision
3. **Incremental indexing:** Update corpus index asynchronously
4. **Layer short-circuiting:** If Layer 1 flags, skip expensive Layer 3/4
5. **Local deployment:** ChromaDB runs locally, no API latency

**Performance targets:**
- Blocklist scan: < 50ms
- Prose-polish: < 2s (existing skill)
- Corpus scoring: < 1s for 10 paragraphs
- Total per-paragraph: < 500ms average

---

## 10. Success Metrics

### 10.1 System Performance

**Detection accuracy:**
- **True positive rate:** % of AI-like passages correctly flagged
  - Target: > 85% (based on Lee's post-hoc labeling)
- **False positive rate:** % of authentic passages incorrectly flagged
  - Target: < 15%
- **Precision on blocklist:** When blocklist fires, how often is Lee's correction needed?
  - Target: > 90%

**Remediation effectiveness:**
- **Acceptance rate:** % of Tier 2 suggestions Lee accepts
  - Target: > 60% after 50+ corrections learned
- **Edit distance reduction:** How much does Lee edit suggested revisions?
  - Target: < 30% of original edit distance

### 10.2 User Experience

**Engagement:**
- **Correction rate:** How often does Lee engage with flagged passages?
  - Healthy: 70-90% (not ignored, not overwhelming)
- **Override rate:** How often does Lee mark "keep as-is" on flags?
  - Healthy: 10-20% (system has legitimate objections, but Lee has agency)

**Satisfaction:**
- **Subjective voice match:** "Does this sound like you?" (1-5 scale)
  - Target: Mean > 4.0 after calibration
- **Usefulness rating:** "Did voice calibration improve the draft?" (1-5)
  - Target: Mean > 3.5

### 10.3 Learning Progress

**Corpus growth:**
- **Size:** Target 100+ samples within 3 months
- **Diversity:** At least 5 distinct topic clusters
- **Quality:** Mean prose-polish score < 25

**Pattern learning:**
- **Blocklist evolution:** 5-10 new learned patterns per month
- **Correction patterns:** 20+ captured correction patterns after 2 months
- **Example effectiveness:** Top-10 examples have success_rate > 0.70

**Voice drift:**
- **Snapshot consistency:** Month-to-month style distance < 0.2 (stable voice)
- **Intentional evolution:** Lee approves 1-2 drift alerts per quarter (not stagnant)

---

## 11. Open Questions & Future Research

### 11.1 Voice Mode Adaptation

**Question:** Should the system adjust expectations based on active voice mode (@strategist vs @builder vs @dissident_poet)?

**Current approach:** Track voice_mode in corpus, use as weak signal in few-shot selection.

**Future research:**
- Build separate voice profiles per mode?
- Learn mode-specific patterns (e.g., @dissident_poet allows more provocative language)?
- Auto-detect which mode a draft is in based on content?

**Hypothesis:** Voice modes are stylistic variations on the same underlying voice. System should recognize Lee across all modes, but allow for mode-specific flourishes.

### 11.2 Multi-Author Corpus

**Question:** What if Lee wants to write "in the style of" someone else intentionally (e.g., mimicking Taleb for rhetorical effect)?

**Current approach:** Mark as intentional deviation, don't penalize.

**Future research:**
- Build secondary corpus of target authors?
- "Voice transfer" mode that calibrates to different target?
- Hybrid profiles (80% Lee, 20% Taleb)?

**Use case:** Writing parody, homage, or explicitly adopting another thinker's frame.

### 11.3 Collaborative Emergence Tracking

**Question:** How to distinguish "Lee's voice enhanced by AI" from "AI voice with Lee's content"?

**Current approach:** Corpus comparison + prose-polish detection.

**Future research:**
- Track edit history: how much did Lee modify AI suggestions?
- Measure "intellectual ownership" beyond just stylistic match?
- Build separate metric for "collaborative authenticity"?

**Insight:** The interview revealed Lee wants *collaborative emergence*, not just voice mimicry. System should maybe measure "did the AI elevate Lee's spark" rather than "does this sound like solo Lee."

### 11.4 Cross-Modal Voice

**Question:** Does Lee's voice in conversation (transcripts) differ from his voice in polished essays?

**Current approach:** Separate corpus categories (conversations vs published).

**Future research:**
- Train mode classifier: casual vs formal?
- Adjust calibration based on target medium (blog post vs academic paper)?
- Track register-shifting across modes?

**Hypothesis:** Voice is consistent across modes, but register shifts. System should recognize core voice while allowing appropriate formality.

### 11.5 Temporal Context

**Question:** Should older writing samples be weighted less (voice has evolved)?

**Current approach:** Recency decay factor (weak signal).

**Future research:**
- Explicitly model voice trajectory over time?
- Detect major shift points (before/after events, learning)?
- Allow Lee to mark "this is old voice, don't match to this anymore"?

**Trade-off:** Capture evolution vs maintain consistency. Needs Lee's input on philosophy.

---

## 12. Conclusion & Recommendations

### Core Recommendations

**1. Start with hybrid approach (not pure embeddings, not pure rules)**

Neither embeddings alone nor pattern-matching alone will suffice. Lee's voice has both semantic (what he talks about) and stylistic (how he says it) dimensions. The system must measure both.

**2. Trust the corpus over guidelines**

WritingSamples/ is ground truth. VOICE.md and interview notes are useful priors, but concrete examples trump abstract principles. When in doubt, show Lee how he actually wrote, don't tell him how he should write.

**3. Build in learning from day one**

Don't wait to add active learning. Every correction is valuable training data. Capture it immediately. The first 50 corrections are the most informative—they teach the system what actually matters to Lee.

**4. Maintain human agency**

Never auto-rewrite. Always suggest. Lee must have final say on every change. This is both ethical (his voice, his choice) and practical (his overrides teach the system).

**5. Integrate with prose-polish, don't replace**

Prose-polish solves a different problem (generic AI detection). Voice calibration solves Lee-specific authenticity. Both are needed. Use prose-polish as Layer 2, add voice-specific layers around it.

### Critical Success Factors

**For MVP (Phase 1-3):**
- Collect 20+ diverse writing samples (quality over quantity)
- Code Lee's explicit blocklist from interview
- Integrate prose-polish seamlessly
- Build few-shot retrieval that returns genuinely useful examples

**For production (Phase 4-5):**
- Capture corrections religiously
- Implement dynamic blocklist promotion
- Build voice drift monitoring
- Create intuitive UX for remediation

### Final Thoughts

This system is fundamentally about **operationalizing taste**. Lee has clear intuitions about what sounds like him ("heartfelt writing where my mind shines through") and what doesn't ("grammatically perfect but soulless"). The challenge is making those intuitions computational without losing nuance.

The proposed architecture bets on:
- **Similarity search** as the primary mechanism (not rules)
- **Few-shot learning** as the primary remediation (show, don't tell)
- **Active learning** as the primary evolution strategy (Lee teaches by doing)

This is opinionated. It assumes:
1. Voice is learnable from examples
2. Lee's corrections are more valuable than abstract guidelines
3. Authenticity is measurable through corpus comparison
4. The system should be a mirror, not a mold

If those assumptions hold, this architecture should work. If they don't, we'll learn quickly from Lee's corrections and adapt.

The goal is not perfection. The goal is a system that helps Lee recognize when something doesn't sound like him, shows him how he actually writes about similar topics, and learns from his choices to get better over time.

That's achievable. Let's build it.

---

**Appendices**

- A: Blocklist patterns (from interview)
- B: Sample corpus query outputs
- C: Example detection reports
- D: Few-shot prompt templates
- E: Correction learning pseudocode

*(Note: Appendices to be filled in during implementation)*
