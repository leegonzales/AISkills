# Phase 3: Business Model Generation

**Goal**: Transform high-potential opportunities into concrete business models with defined synthetic worker roles.

---

## Step 3.1: Define Synthetic Worker Primitives

**15 atomic job functions that become commoditized:**

### 1. Continuous Monitor
**Job description**: Watches systems, processes, or information sources; alerts on anomalies, changes, or threshold crossings.

**SLA template**:
- Monitoring frequency: Real-time to hourly
- Alert latency: <5 minutes from trigger
- False positive rate: <5%
- False negative rate: <1%

**Example applications**:
- Regulatory change tracking (legal)
- Competitor monitoring (marketing)
- System health checks (IT operations)
- Price changes (e-commerce)
- Security threat detection (infosec)

**Current feasibility**: HIGH (3-month horizon)

---

### 2. Research Synthesizer
**Job description**: Gathers sources from multiple channels, reads and comprehends, synthesizes findings, provides citations.

**SLA template**:
- Research depth: 20-100+ sources
- Turnaround time: 30min - 4 hours
- Citation accuracy: >98%
- Synthesis quality: Graduate student level
- Bias detection: Flags contradictions

**Example applications**:
- Legal case law research
- Academic literature review
- Market research reports
- Competitive intelligence
- Investment due diligence

**Current feasibility**: HIGH (production-ready with current context windows and tool use)

---

### 3. Document Processor
**Job description**: Extracts data from documents, validates against rules, transforms into structured format.

**SLA template**:
- Processing speed: 100-1000 pages/hour
- Extraction accuracy: >99%
- Validation rule enforcement: 100%
- Format flexibility: PDF, images, scanned docs
- Error flagging: Ambiguous cases sent to human

**Example applications**:
- Invoice processing (finance)
- Contract data extraction (legal)
- Medical record parsing (healthcare)
- Resume screening (HR)
- Insurance claims intake

**Current feasibility**: HIGH (today with current multimodal)

---

### 4. Communication Coordinator
**Job description**: Drafts messages, routes to correct recipients, tracks follow-ups, maintains communication context.

**SLA template**:
- Response time: <5 minutes
- Tone consistency: Matches brand voice
- Context retention: Full conversation history
- Routing accuracy: >95%
- Escalation triggers: Defined rule set

**Example applications**:
- Customer support triage
- Meeting scheduling
- Status update emails
- Internal notifications
- Client relationship management

**Current feasibility**: HIGH (today with prompt engineering)

---

### 5. Compliance Auditor
**Job description**: Checks documents/processes against rule sets, flags violations, suggests corrections, maintains audit trail.

**SLA template**:
- Coverage: 100% of transactions
- Detection accuracy: >99.5%
- False positive rate: <2%
- Audit trail: Complete, immutable
- Regulatory updates: Real-time incorporation

**Example applications**:
- Financial reporting compliance (SOX, GAAP)
- Healthcare privacy (HIPAA)
- Data protection (GDPR)
- Code quality standards
- Contract term verification

**Current feasibility**: HIGH (production-ready with current capabilities)

---

### 6. Creative Collaborator
**Job description**: Generates variants based on specifications, iterates on feedback, maintains brand/style consistency.

**SLA template**:
- Variant generation: 5-20 options
- Iteration speed: <5 minutes per round
- Brand consistency: >90% alignment score
- Feedback incorporation: 95% accuracy
- Style transfer: Maintains voice/tone

**Example applications**:
- Marketing copy variations
- Design mockup generation
- Code refactoring suggestions
- Product name brainstorming
- Email subject line testing

**Current feasibility**: HIGH (today with proper prompting)

---

### 7. Knowledge Curator
**Job description**: Organizes information, applies taxonomies, creates retrievable structures, maintains knowledge graph.

**SLA template**:
- Indexing speed: 1000+ documents/hour
- Retrieval accuracy: >95%
- Taxonomy consistency: 100%
- Deduplication: >98%
- Update frequency: Real-time to daily

**Example applications**:
- Internal wiki management
- Customer support knowledge base
- Research library organization
- Document management systems
- Institutional memory capture

**Current feasibility**: HIGH (today with vector databases)

---

### 8. Workflow Orchestrator
**Job description**: Manages multi-step processes, coordinates between systems/people, tracks progress, handles exceptions.

**SLA template**:
- Process adherence: >99%
- Handoff accuracy: 100%
- Exception detection: >95%
- Progress visibility: Real-time dashboard
- Completion rate: >98%

**Example applications**:
- Approval workflows
- Onboarding processes
- Order fulfillment
- Content production pipelines
- Project task management

**Current feasibility**: MEDIUM-HIGH (MCP + agent frameworks make orchestration production-viable)

---

### 9. Analysis Generator
**Job description**: Runs analytical processes on data, identifies patterns, generates insights, creates visualizations.

**SLA template**:
- Analysis depth: Descriptive to predictive
- Turnaround: Minutes to hours
- Insight quality: Analyst-level
- Visualization: Publication-ready
- Explanation: Clear methodology

**Example applications**:
- Financial reporting
- Sales pipeline analysis
- A/B test evaluation
- User behavior analytics
- Operational dashboards

**Current feasibility**: HIGH (today with code execution)

---

### 10. Relationship Maintainer
**Job description**: Tracks relationship context, personalizes outreach, remembers preferences, maintains engagement cadence.

**SLA template**:
- Context retention: Complete history
- Personalization accuracy: >90%
- Timing optimization: Data-driven cadence
- Tone matching: Relationship-appropriate
- Relationship health: Scored and tracked

**Example applications**:
- Sales follow-up
- Investor relations
- Customer success
- Partnership management
- Networking maintenance

**Current feasibility**: HIGH (production-ready with persistent memory systems)

---

### 11. Code Developer
**Job description**: Writes, tests, reviews, refactors, and deploys code. Handles bug fixes, feature implementation, test generation, and CI/CD pipeline management.

**SLA template**:
- Code quality: Passes linting + type checking
- Test coverage: >80% for generated code
- Review turnaround: <10 minutes
- Bug fix accuracy: >85% first-attempt resolution
- Security: No OWASP top-10 vulnerabilities introduced

**Example applications**:
- Automated bug fixing and triage
- Test generation and maintenance
- Code review and refactoring services
- Migration automation (framework, language, API version)
- Internal tooling development

**Current feasibility**: HIGH (production-ready — Claude Code, Cursor, Devin shipping today)

---

### 12. Browser Operator
**Job description**: Navigates web UIs, fills forms, scrapes structured data, interacts with legacy systems that lack APIs, and automates browser-based workflows.

**SLA template**:
- Navigation accuracy: >95%
- Form fill accuracy: >98%
- Data extraction quality: >97%
- Error recovery: Automatic retry with fallback
- Session management: Handles auth, cookies, CAPTCHAs (with human escalation)

**Example applications**:
- Legacy system data entry (EHR, government portals, ERPs)
- Competitive price monitoring via web scraping
- Automated form submissions (insurance, compliance, permits)
- Web-based testing and QA
- Data migration from systems without APIs

**Current feasibility**: HIGH (computer use shipping in production)

---

### 13. Voice Agent
**Job description**: Handles phone calls, participates in meetings, conducts real-time conversations, provides negotiation support, and manages voice-based workflows.

**SLA template**:
- Response latency: <500ms
- Comprehension accuracy: >95%
- Tone consistency: Matches brand/persona
- Escalation triggers: Defined rule set for human handoff
- Language support: Configurable per deployment

**Example applications**:
- Inbound/outbound sales calls (SDR replacement)
- Appointment scheduling and confirmation
- Customer support phone lines
- Meeting participation and note-taking
- Debt collection and follow-up calls

**Current feasibility**: MEDIUM-HIGH (voice APIs maturing rapidly, production deployments emerging)

---

### 14. Data Pipeline Operator
**Job description**: Manages ETL processes, transforms data between formats, monitors data quality, maintains schema consistency, and orchestrates data workflows.

**SLA template**:
- Pipeline uptime: >99.5%
- Data quality score: >98% accuracy
- Schema drift detection: Real-time alerts
- Transformation accuracy: >99%
- Recovery time: <15 minutes for pipeline failures

**Example applications**:
- Automated ETL pipeline management
- Data quality monitoring and remediation
- Schema migration and versioning
- Cross-system data synchronization
- Reporting data preparation

**Current feasibility**: HIGH (code generation + tool use enables this today)

---

### 15. Security Sentinel
**Job description**: Scans for vulnerabilities, analyzes security threats, responds to incidents, maintains audit trails, and ensures compliance with security policies.

**SLA template**:
- Scan coverage: 100% of codebase/infrastructure
- False positive rate: <10%
- Incident response time: <5 minutes for detection
- Compliance reporting: Automated, continuous
- Threat intelligence: Updated in real-time

**Example applications**:
- Continuous code security scanning (SAST/DAST)
- Incident response triage and initial analysis
- Compliance audit preparation (SOC2, ISO 27001)
- Penetration testing assistance
- Security policy enforcement

**Current feasibility**: MEDIUM-HIGH (code analysis strong, real-time threat response emerging)

---

## Step 3.2: Combinatorial Business Model Generation

**Process**: Cross synthetic worker primitives with segment pain points from Phase 2.

**Template:**

```
[Synthetic Worker Primitive] × [Segment] = [Business Opportunity]

Example:
Research Synthesizer × Legal = AI Legal Research Associate
```

**Systematic generation:**

For each **P1 opportunity** from Phase 2:
1. Identify which primitive(s) apply
2. Define specific role for that segment
3. Specify SLA for the segment
4. Design eval framework
5. Identify human-in-loop points
6. Calculate unit economics
7. Map competitive landscape

---

## Step 3.3: Business Model Canvas Template

**For each opportunity, complete this canvas:**

### 1. Business Concept

**Name**: [Descriptive name]
**Tagline**: [One-sentence value prop]
**Segment**: [Primary target market]
**Synthetic worker role**: [Which primitive(s)]

### 2. Problem & Solution

**Problem**:
- Current state (how it's done today)
- Pain points (what's broken)
- Economic impact (cost of current approach)

**Solution**:
- Synthetic worker description
- What it automates
- What remains human-in-loop
- Integration points

### 3. SLA Definition

**Performance metrics**:
- Accuracy: [%]
- Speed: [time]
- Throughput: [volume]
- Availability: [uptime %]
- Error handling: [escalation rules]

**Quality benchmarks**:
- vs. Junior human: [performance comparison]
- vs. Mid-level human: [performance comparison]
- vs. Senior human: [performance comparison]

### 4. Eval Framework

**How performance is measured**:
- Automated metrics (accuracy, speed, etc.)
- Human evaluation protocol (sampling rate, criteria)
- Customer feedback loop
- Continuous improvement process

**Example eval for legal research**:
- Citation accuracy (automated check against databases)
- Relevance score (attorney rates 1-10 on random 10% sample)
- Time saved (tracked per research project)
- Quarterly blind test (AI vs. junior associate comparison)

### 5. Unit Economics

**Customer acquisition**:
- CAC: $[X]
- Payback period: [months]
- LTV: $[X]

**Delivery costs**:
- Inference: $[X]/customer/month
- Infrastructure: $[X]/customer/month
- Human oversight: $[X]/customer/month
- Total COGS: $[X]/customer/month

**Pricing**:
- Model: [per seat / usage-based / outcome-based]
- Price point: $[X]/month or $[X]/transaction
- Gross margin: [%]

**Example for legal research assistant**:
- Pricing: $500/month per attorney
- Inference cost: $20/month (100 research projects @ $0.20)
- Infrastructure: $5/month
- Human QA: $10/month (spot-checking)
- COGS: $35/month
- **Gross margin: 93%**

### 6. Go-to-Market

**Customer acquisition**:
- Primary channel: [SEO / sales / partnerships / community]
- Wedge: [initial narrow use case]
- Expansion: [land-and-expand strategy]

**Positioning**:
- vs. Incumbents: [differentiation]
- vs. Substitutes: [why not hire human]
- vs. DIY: [why not build in-house]

**Initial target**:
- Segment: [specific niche to start]
- Size: [how many potential customers]
- Why them first: [strategic reasoning]

### 7. System Architecture (Compound AI Design)

**Modern AI products are compound systems — not single models. Define the architecture:**

**Model layer**:
- **Frontier model**: [Which tasks require frontier reasoning? (e.g., complex synthesis, strategic analysis)]
- **Specialized models**: [Which tasks use smaller/fine-tuned models? (e.g., classification, extraction, routing)]
- **Model routing**: [How does the system decide which model handles which task?]

**Agent layer**:
- **Agent roles**: [What specialized agents exist? (e.g., research agent, validation agent, output agent)]
- **Orchestration**: [How do agents coordinate? (sequential, parallel, hierarchical)]
- **Tool integrations**: [What external tools/APIs do agents use? (MCP servers, databases, APIs)]

**Quality layer**:
- **AI-reviewing-AI**: [Where does one model check another's work?]
- **Human-in-loop points**: [Where do humans intervene? (approval gates, quality sampling, edge cases)]
- **Eval pipeline**: [Automated quality metrics, regression testing, drift detection]

**Cost optimization**:
- **Estimated cost per task**: [Break down inference costs by model tier]
- **Cost at scale**: [How costs change at 10x, 100x volume]
- **Optimization levers**: [Caching, batching, model distillation, prompt optimization]

---

### 8. Moat & Defensibility

**Competitive advantages**:
- Data flywheel: [how usage improves product]
- Network effects: [if applicable]
- Switching costs: [integration depth, data lock-in]
- Brand/trust: [if applicable]
- Specialized models: [domain fine-tuning]

**Barriers to entry**:
- Technical: [what's hard to replicate]
- Data: [proprietary datasets]
- Relationships: [partnerships, integrations]
- Regulatory: [compliance, certifications]

### 9. Risk Factors

**Technical risks**:
- Capability assumptions (what if AI doesn't improve as projected?)
- Hallucination/accuracy (what if error rate too high?)
- Integration complexity (what if too hard to deploy?)

**Market risks**:
- Adoption friction (will customers trust AI for this?)
- Incumbent response (what if they add AI features?)
- Pricing pressure (race to the bottom?)

**Regulatory risks**:
- Professional liability (who's responsible for AI errors?)
- Data privacy (GDPR, industry-specific rules)
- Licensing requirements (e.g., legal practice restrictions)

**Mitigation strategies**: [For each risk]

---

## Step 3.4: Time-Horizon Business Categories

**Map business opportunities to capability unlock timelines:**

### 3-Month Horizon (Today's Tech)

> **Note**: Refresh capability assumptions each run. The categories below remain stable; the specific capabilities that unlock them shift over time.

**Unlocked capabilities** (update with Phase 1 research):
- Current context windows, cost, tool reliability
- Computer use / browser automation
- Agentic coding
- Multimodal (vision + audio)

**Business categories**:
1. **Document workspace agents**
   - Real-time contract negotiation assistant
   - Meeting summarization service
   - Design feedback aggregator

2. **Routine communication automation**
   - Customer support triage
   - Email response drafting
   - Status update generation

3. **Data aggregation services**
   - Multi-system reporting
   - Competitive intelligence gathering
   - Market research automation

4. **Agentic coding services**
   - Automated bug triage and fixing
   - Test generation and maintenance
   - Code migration and modernization

5. **Browser-based automation**
   - Legacy system data entry
   - Form submission automation
   - Web scraping and monitoring

**Example**: **SupportSynth** - Customer support triage agent
- Reads incoming tickets, categorizes, routes to right team
- Drafts response for human approval
- Learns from corrections
- SLA: <2 min response time, 95% routing accuracy
- Pricing: $200/month per support agent replaced
- TAM: 2M support agents in US

---

### 6-Month Horizon

**Unlocked capabilities** (update with Phase 1 research):
- Larger context windows, lower costs
- Multi-hour autonomous task execution
- Voice agent production readiness
- Improved multi-tool orchestration

**Business categories**:
1. **Research automation platforms**
   - Academic literature synthesis service
   - Legal case law research
   - Market analysis automation

2. **Complex document processing**
   - Multi-party contract analysis
   - Due diligence automation
   - Regulatory filing preparation

3. **Strategic content creation**
   - Long-form content generation
   - Presentation deck creation
   - Strategic memo writing

4. **Voice agent services**
   - Inbound/outbound sales calls
   - Appointment scheduling
   - Customer support phone lines

**Example**: **LegalMind** - AI legal research associate
- Researches case law across jurisdictions
- Synthesizes findings with citations
- Identifies relevant precedents
- SLA: 4-hour turnaround, 98% citation accuracy
- Pricing: $500/month per attorney
- TAM: 520K solo/small firm attorneys

---

### 12-Month Horizon

**Unlocked capabilities**:
- 1M context
- 98% reliability
- $0.50/1M tokens
- 8-16 hour planning
- Cross-platform orchestration

**Business categories**:
1. **Synthetic operations teams**
   - AI-powered customer success org
   - Automated project management office
   - Synthetic sales development reps

2. **Strategic analysis services**
   - Investment thesis generation
   - Market entry strategy
   - Competitive positioning

3. **Complex workflow automation**
   - End-to-end procurement
   - Full-cycle recruiting
   - Multi-step compliance processes

**Example**: **CustomerOS** - Synthetic customer success team
- Monitors customer health scores
- Proactive outreach on issues
- Quarterly business reviews (automated)
- Expansion opportunity identification
- SLA: 100% account coverage, <24hr response
- Pricing: $2,000/month per CSM replaced
- TAM: 100K CSMs in B2B SaaS

---

### 18-Month Horizon

**Unlocked capabilities**:
- 2M context
- 98.5% reliability
- $0.25/1M tokens
- 16-24 hour planning

**Business categories**:
1. **Executive co-pilots**
   - Board deck generation from raw data
   - Strategic planning facilitation
   - Organizational design

2. **Advanced analytics**
   - Predictive modeling automation
   - Causal inference analysis
   - Complex simulation

3. **Cross-functional coordination**
   - Program management
   - M&A integration
   - Product launch orchestration

**Example**: **StrategyAI** - Executive strategy co-pilot
- Analyzes market trends, competitive moves
- Generates strategic options
- Models scenarios
- Produces board-ready materials
- SLA: Weekly strategic updates, quarterly deep dives
- Pricing: $5,000/month per executive
- TAM: 500K executives at mid-market+ companies

---

### 24-Month Horizon

**Unlocked capabilities**:
- 5M+ context
- 99% reliability
- $0.10/1M tokens
- 24-48+ hour planning
- Near-human strategic reasoning

**Business categories**:
1. **Synthetic departments**
   - Entire compliance function as software
   - Automated finance & accounting
   - AI-powered HR operations

2. **Autonomous business units**
   - Self-managing product lines
   - Algorithmic market makers
   - Synthetic research labs

**Example**: **ComplianceOS** - Entire compliance department as software
- Continuous policy monitoring
- Automated control testing
- Regulatory change management
- Audit preparation
- SLA: 100% coverage, real-time monitoring
- Pricing: $20,000/month (vs. $500K/year for team)
- TAM: 50K mid-market companies with compliance needs

---

## Step 3.5: Business Model Patterns

**Identify common patterns across opportunities:**

### Pattern 1: Task Automation (Replace Specific Activity)
- **Value prop**: Do X task 10x faster/cheaper
- **Pricing**: Usage-based or per-task
- **Example**: Document processing, data entry
- **Margin**: 70-90% (low COGS)
- **Moat**: Data flywheel, workflow integration

### Pattern 2: Role Augmentation (AI Co-pilot)
- **Value prop**: Make expert 2-5x more productive
- **Pricing**: Per-seat subscription
- **Example**: Legal research, code review
- **Margin**: 80-95% (low COGS)
- **Moat**: Specialized models, user workflows

### Pattern 3: Role Replacement (Synthetic Worker)
- **Value prop**: Replace junior-to-mid level role
- **Pricing**: % of salary saved
- **Example**: Customer support, sales development
- **Margin**: 85-95% (scales with inference)
- **Moat**: SLA guarantees, integration depth

### Pattern 4: Department-in-a-Box
- **Value prop**: Entire function as software
- **Pricing**: Fixed monthly fee (vs. headcount)
- **Example**: Compliance, HR operations
- **Margin**: 90-95% (pure software)
- **Moat**: Regulatory expertise, compound integration

### Pattern 5: Compound AI Platform
- **Value prop**: Orchestrated system of specialized agents working together
- **Pricing**: Platform fee + usage-based for agent compute
- **Example**: End-to-end recruiting (sourcing agent + screening agent + scheduling agent + reporting agent)
- **Margin**: 75-90% (higher infrastructure costs, but higher value capture)
- **Moat**: Orchestration logic, inter-agent protocols, data flywheel across agents
- **Key differentiator**: Multiple specialized models (small/fine-tuned for routine, frontier for complex) with intelligent routing — not just one model doing everything

---

## Phase 3 Deliverable

**Document structure:**

### 1. Synthetic Worker Definitions
- All 10 primitives with SLAs
- Example applications per primitive
- Feasibility timeline

### 2. Business Model Canvases
- Top 25 opportunities with complete canvas
- Problem, solution, SLA, eval, economics, GTM, moat, risks

### 3. Time-Horizon Roadmap
- Business categories per horizon (3mo, 6mo, 12mo, 18mo, 24mo)
- 5-10 example businesses per horizon
- Capability dependencies

### 4. Pattern Analysis
- Common business model patterns
- Pricing model options
- Moat strategies

### 5. Prioritized Portfolio
- Top 10 businesses to pursue
- Ranking by opportunity size, feasibility, time to market

---

## Quality Checks

**Good business model has:**
- [ ] Clear synthetic worker role with SLA
- [ ] Defined eval framework (how to measure success)
- [ ] Unit economics that work (>70% gross margin)
- [ ] Realistic capability assumptions (not vaporware)
- [ ] Identified human-in-loop points (not full automation BS)
- [ ] Go-to-market wedge (specific first customer)
- [ ] Defensibility (some kind of moat)
- [ ] Risk mitigation (know what could go wrong)

**Red flags:**
- Vague role definition ("AI helps with...")
- No measurement framework (can't prove value)
- Unrealistic margins (ignoring oversight costs)
- Assumes capabilities that don't exist yet
- Claims 100% automation (naive)
- Generic "everyone needs this" targeting
- No moat (easily copied)
- Ignoring obvious risks

---

**Next phase**: Take business models → validate with market research → score inevitability

Return to main SKILL.md to proceed to Phase 4: Market Validation
