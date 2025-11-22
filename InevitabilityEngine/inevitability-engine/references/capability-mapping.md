# Phase 1: Capability Frontier Mapping

**Goal**: Map the current and projected AI capability landscape to identify what unlocks at each time horizon.

---

## Step 1.1: Decompose the AI Stack by Evolution Stage

**Use Wardley mapping to classify capabilities by evolution:**

```
GENESIS → CUSTOM → PRODUCT → COMMODITY

GENESIS (Novel, uncertain, requires research):
- Real-time learning loops
- Multi-agent coordination frameworks
- Causal reasoning
- True long-horizon planning (multi-day tasks)

CUSTOM (Requires expertise, bespoke solutions):
- Long-horizon planning (multi-hour tasks)
- Inter-agent coordination
- Domain-specific fine-tuning
- Sophisticated eval frameworks
- Computer use / tool orchestration

PRODUCT (Productized but still differentiating):
- Multimodal reasoning (vision + text)
- Advanced RAG systems
- Function calling / tool use
- Context windows 100K-500K
- Streaming outputs

COMMODITY (Standard, undifferentiated):
- Basic text generation
- Simple Q&A
- Summarization
- Translation
- Code completion
- Context windows <100K
```

**Research Protocol 1.1:**

Execute these searches to understand current state:

```
1. "GPT-4 Turbo capabilities benchmarks 2024"
2. "Claude 3.5 Sonnet computer use production"
3. "OpenAI GPT-5 predictions roadmap"
4. "Anthropic Claude Opus 4 announcement"
5. "LLM tool use reliability enterprise deployment"
6. "agent orchestration frameworks production 2024"
7. "multimodal AI capabilities vision reasoning"
```

**Analysis questions:**
- What capabilities moved from custom → product in the last 12 months?
- What's moving from product → commodity in the next 6 months?
- What's emerging from genesis → custom?

**Output**: Evolution map showing current position and trajectory for each capability

---

## Step 1.2: Identify Constraint Removals

**What was impossible 12 months ago that's now trivial?**

**Framework**: constraint_removed → business_unlock mapping

**Examples:**

| Constraint (2023) | Removed (2024) | Business Unlock |
|-------------------|----------------|-----------------|
| 8K context limit | 128K-200K available | Full document comprehension, entire codebases |
| Unreliable function calling | 95%+ accuracy | Production agent workflows |
| $30/1M tokens | $3-5/1M tokens | High-volume automation economically viable |
| Text-only | Multimodal (vision) | Screenshot analysis, design review, document OCR |
| Brittle multi-step | Robust tool chains | End-to-end workflow automation |

**Research Protocol 1.2:**

Execute these searches to understand constraint removals:

```
1. "what can GPT-4 do that GPT-3.5 couldn't"
2. "Claude 3.5 vs Claude 3 capabilities comparison"
3. "LLM context window evolution 2023 2024"
4. "AI tool use reliability improvements"
5. "inference cost reduction trends 2024"
6. "function calling accuracy benchmarks"
```

**For each constraint removal, ask:**
1. What workflows were bottlenecked by this?
2. What human roles existed ONLY because this was hard?
3. What markets are now addressable?
4. What's the economic leverage? (10x? 100x? 1000x?)

**Key patterns to look for:**
- **Threshold crossings**: When capability goes from <70% → >90% accuracy
- **Cost cliff dives**: When price drops enable high-volume use cases
- **Modality additions**: When new input/output types unlock domains
- **Reliability milestones**: When error rates drop below human tolerance

**Output**: Constraint removal log with business implications

---

## Step 1.3: Project Forward (Capability Forecasting)

**Use scaling laws + roadmaps + observed improvement rates**

**Forecasting methodology:**

1. **Chinchilla scaling laws**: Model performance scales predictably with compute + data
2. **Announced roadmaps**: OpenAI, Anthropic, Google publish capability targets
3. **Observed rates**: Track improvement velocity over 6-12 months
4. **Extrapolate conservatively**: Use lower bound of projections

**Capability timeline template:**

|Horizon|Context Window|Cost/1M tokens|Tool Reliability|Multimodal|Planning Horizon|
|-------|--------------|--------------|----------------|----------|----------------|
|**Today**|128K-200K|$3-5|95%|Vision good|30min-2hr|
|**3 months**|200K-300K|$2-3|96%|Vision + audio|2-4hr|
|**6 months**|500K|$1-2|97%|Native multimodal|4-8hr|
|**12 months**|1M|$0.50-1|98%|Real-time video|8-16hr|
|**18 months**|2M|$0.25-0.50|98.5%|Full multimedia|16-24hr|
|**24 months**|5M+|$0.10-0.25|99%|Seamless modalities|24-48hr+|

**Research Protocol 1.3:**

Execute these searches for forecasting:

```
1. "scaling laws LLM compute tokens chinchilla"
2. "anthropic claude context window roadmap 2025"
3. "openai gpt capabilities 2025 predictions"
4. "inference cost trends projection 2025"
5. "AI agent planning horizon improvements"
6. "LLM reliability improvement rate"
```

**Capability unlock mapping:**

For each horizon, identify:

1. **What becomes automatable?**
   - New task types that cross viability threshold
   - Workflows that require new context window
   - Use cases enabled by cost reduction

2. **What role gets commoditized?**
   - Job functions that become fully automatable
   - Workflows that become "good enough" for production

3. **What new business category emerges?**
   - Products impossible before this horizon
   - Markets addressable for first time
   - Business models enabled by new economics

**Example:**

**6-month horizon unlock:**
- **Capability**: 500K context + $1/1M tokens + 97% tool reliability
- **Automatable**: Multi-hour research projects with source synthesis
- **Role commoditized**: Junior research analyst
- **New category**: Research-as-a-service for knowledge workers

**Output**: Time-horizon capability unlock matrix

---

## Step 1.4: Build Capability × Segment Matrix

**Cross capability unlocks with target segments:**

| Segment | Current Bottleneck | Capability Needed | Horizon | Business Opportunity |
|---------|-------------------|-------------------|---------|---------------------|
| Legal | Manual case law research | 500K context + legal corpus | 6mo | AI legal research associate |
| Finance | Data gathering for analysis | Reliable tool use + APIs | 3mo | Automated data aggregation |
| Healthcare | Patient note synthesis | HIPAA-compliant + summarization | 12mo | Clinical documentation assistant |
| Engineering | Spec-to-code translation | Long context + code execution | 6mo | Specification validator |
| Marketing | Content research & drafting | Multimodal + brand voice | 3mo | Brand-aware content generator |

**Research protocol:**

For each segment:
```
1. "[segment] AI automation opportunities 2024"
2. "[segment] workflow bottlenecks"
3. "[segment] software spending priorities"
4. "AI capabilities for [segment] use cases"
```

**Output**: Capability-segment opportunity matrix

---

## Phase 1 Deliverable

**Document structure:**

### 1. Evolution Map
- Current capability positions on Wardley axis
- Movement trajectories (genesis→custom→product→commodity)
- Timeline for transitions

### 2. Constraint Removal Log
- What was impossible → now trivial
- Business unlocks for each removal
- Economic leverage calculations

### 3. Capability Forecast
- 3mo, 6mo, 12mo, 18mo, 24mo projections
- Context, cost, reliability, modality, planning horizon
- Confidence levels (high/medium/low)

### 4. Unlock Timeline
- What becomes automatable at each horizon
- Roles that get commoditized
- New business categories enabled

### 5. Capability × Segment Matrix
- Segment bottlenecks mapped to capabilities
- Time horizon for each unlock
- Preliminary business concepts

---

## Quality Checks

**Good capability mapping has:**
- [ ] Specific capability metrics (not vague "better AI")
- [ ] Cited sources for projections (roadmaps, papers, benchmarks)
- [ ] Conservative estimates (under-promise)
- [ ] Clear threshold crossings (when % goes from not viable → viable)
- [ ] Business implications for each technical unlock
- [ ] Time horizons with confidence levels
- [ ] Both optimistic and pessimistic scenarios

**Red flags:**
- Vague predictions ("AI will get better")
- No sources or benchmarks
- Overly optimistic timelines
- Missing economic analysis
- No consideration of constraints
- Assumes linear improvement (usually comes in jumps)

---

## Tips for Effective Capability Mapping

1. **Follow the frontier labs**: OpenAI, Anthropic, Google are transparent about roadmaps
2. **Watch the benchmark shifts**: When scores jump 10-20% in months, pay attention
3. **Track cost aggressively**: Often the unlock is economic, not technical
4. **Look for threshold crossings**: 70% → 90% accuracy changes everything
5. **Consider system effects**: Capabilities combine (context + tools + multimodal)
6. **Be conservative**: Better to be surprised by early arrival than late
7. **Update frequently**: This field moves fast, re-map quarterly

---

**Next phase**: Take capability unlocks → discover segment problems → match opportunities

Return to main SKILL.md to proceed to Phase 2: Opportunity Discovery
