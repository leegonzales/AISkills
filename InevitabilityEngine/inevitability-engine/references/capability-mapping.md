# Phase 1: Capability Frontier Mapping

**Goal**: Map the current and projected AI capability landscape to identify what unlocks at each time horizon.

---

## Step 1.1: Decompose the AI Stack by Evolution Stage

**Use Wardley mapping to classify capabilities by evolution:**

```
GENESIS → CUSTOM → PRODUCT → COMMODITY

Update these positions each time you run the engine. Capabilities move
rightward over time. The positions below are a starting template — validate
against current benchmarks and announcements.

COMMODITY (Standard, undifferentiated):
- Basic text generation, summarization, translation
- Code completion and generation
- Simple Q&A and classification
- Context windows <200K
- Streaming outputs

PRODUCT (Productized but still differentiating):
- Multimodal reasoning (vision + text + audio)
- Function calling / tool use / MCP integration
- Agentic coding (Claude Code, Cursor, Devin, etc.)
- Computer use / browser automation
- Advanced RAG systems
- Context windows 200K-1M
- Domain-specific fine-tuning

CUSTOM (Requires expertise, bespoke solutions):
- Multi-hour autonomous task execution
- Multi-agent orchestration (Claude Agent SDK, etc.)
- Extended thinking / chain-of-thought planning
- Compound AI system design (model routing, specialized pipelines)
- Voice/real-time conversational agents
- Production eval frameworks
- Cross-platform workflow orchestration

GENESIS (Novel, uncertain, requires research):
- Real-time continuous learning loops
- Multi-day autonomous planning
- Causal reasoning
- Self-improving agent systems
- General-purpose embodied AI
```

**Research Protocol 1.1:**

Execute these searches to understand current state. Replace `[current_year]` with the actual year.

```
1. "[frontier model] capabilities benchmarks [current_year]"
2. "Anthropic Claude capabilities announcement [current_year]"
3. "OpenAI model capabilities [current_year]"
4. "Google Gemini capabilities [current_year]"
5. "LLM tool use MCP reliability enterprise deployment"
6. "agent orchestration frameworks production [current_year]"
7. "multimodal AI capabilities vision audio reasoning"
8. "agentic coding tools comparison [current_year]"
9. "computer use browser automation AI [current_year]"
10. "AI voice agents production deployment"
```

**Also check:**
- Anthropic blog and documentation (anthropic.com)
- OpenAI blog and API docs
- Hugging Face model cards and leaderboards
- AI benchmark aggregators (LMSYS Chatbot Arena, etc.)
- Archive.org for historical capability snapshots

**Analysis questions:**
- What capabilities moved from custom → product in the last 12 months?
- What's moving from product → commodity in the next 6 months?
- What's emerging from genesis → custom?
- What compound capabilities emerged (e.g., tool use + extended thinking)?

**Output**: Evolution map showing current position and trajectory for each capability

---

## Step 1.2: Identify Constraint Removals

**What was impossible 12 months ago that's now trivial?**

**Framework**: constraint_removed → business_unlock mapping

**Examples (historical — update with current constraint removals):**

| Constraint (Prior Gen) | Removed (Current Gen) | Business Unlock |
|------------------------|-----------------------|-----------------|
| 8K context limit | 200K-2M available | Full document comprehension, entire codebases |
| Unreliable function calling | MCP + tool use at production-grade | Standardized agent workflows across tools |
| $30/1M tokens | $0.50-3/1M for frontier models | High-volume automation economically viable |
| Text-only | Multimodal (vision + audio) | Screenshot analysis, design review, voice agents |
| Brittle multi-step | Multi-hour autonomous agent execution | End-to-end workflow automation |
| No computer use | Browser automation, GUI interaction | Web scraping, form filling, legacy system integration |
| Manual coding only | Agentic coding (Claude Code, etc.) | Code generation, testing, deployment as a service |

**Research Protocol 1.2:**

Execute these searches to understand constraint removals:

```
1. "[current frontier model] vs [previous gen] capabilities comparison"
2. "LLM context window evolution [current_year-1] [current_year]"
3. "AI tool use MCP reliability improvements"
4. "inference cost reduction trends [current_year]"
5. "agentic coding capabilities improvements"
6. "computer use AI production readiness"
7. "AI voice agent improvements [current_year]"
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

**Capability timeline template (fill in with current research):**

> **Instructions**: Research current values for "Today" row, then project forward using observed improvement rates, announced roadmaps, and scaling law projections. Be conservative — use lower-bound estimates.

|Horizon|Context Window|Cost/1M tokens (input)|Tool Reliability|Agentic Autonomy|Multimodal|
|-------|--------------|---------------------|----------------|----------------|----------|
|**Today**|[research]|[research]|[research]|[research]|[research]|
|**3 months**|[project]|[project]|[project]|[project]|[project]|
|**6 months**|[project]|[project]|[project]|[project]|[project]|
|**12 months**|[project]|[project]|[project]|[project]|[project]|
|**18 months**|[project]|[project]|[project]|[project]|[project]|
|**24 months**|[project]|[project]|[project]|[project]|[project]|

**Research Protocol 1.3:**

Execute these searches for forecasting:

```
1. "scaling laws LLM compute inference efficiency [current_year]"
2. "anthropic claude roadmap capabilities [current_year]"
3. "openai model capabilities predictions [current_year]"
4. "inference cost trends projection [current_year] [current_year+1]"
5. "AI agent planning horizon autonomous improvements"
6. "LLM reliability improvement rate production"
7. "MCP tool integration ecosystem growth"
8. "compound AI systems architecture trends"
```

**Additional sources for forecasting:**
- Epoch AI (epochai.org) — compute trends, scaling analysis
- AI Index Report (Stanford HAI) — annual capability survey
- Frontier model provider blogs and changelogs
- Hugging Face Open LLM Leaderboard — benchmark trajectories
- Archive.org snapshots of benchmark sites for historical comparison

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
1. "[segment] AI automation opportunities [current_year]"
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
