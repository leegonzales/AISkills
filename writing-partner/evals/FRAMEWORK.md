# Writing Partner Evaluation Framework

How to evaluate the skill's output and find areas for improvement.

---

## Evaluation Dimensions

The skill has three core capabilities. Each needs different evaluation.

| Capability | What to Measure | How to Measure |
|------------|-----------------|----------------|
| **Interview** | Does it extract ground truth? | Material usage rate, fabrication detection |
| **Thread Tracking** | Does it manage complexity? | Thread loss rate, surfacing accuracy |
| **Voice Calibration** | Does it sound like Lee? | Prose-polish scores, subjective recognition |

---

## 1. Interview Evaluation

### Metrics

**Material Usage Rate**
```
# of interview points appearing in final draft / # of substantive answers given
Target: >80%
```

If interview extracts 10 key points and only 3 appear in the draft, the interview isn't driving the writing.

**Ground Truth Preservation**
```
# of claims backed by Lee's stated experience / # of claims in draft
Target: 100% (no fabrications)
```

**Depth Achievement**
```
Did interview reach Phase 2 (deepening) questions?
Did Lee provide concrete examples vs. abstractions?
```

### Eval Protocol

After each session, audit:

1. **List all substantive claims in the draft**
2. **Trace each back to interview**
   - Found in interview → Check
   - Inferred from interview → Flag for review
   - Not in interview → Fabrication (fail)
3. **Score material usage:** claims traced / total claims

### Red Flags

- Draft contains experiences Lee didn't describe
- Draft makes claims more specific than interview provided
- Generic examples replace concrete ones from interview
- Interview stayed at Phase 1 (surface questions only)

---

## 2. Thread Tracking Evaluation

### Metrics

**Thread Loss Rate**
```
# of threads mentioned but not tracked / # of threads that emerged
Target: 0 (no threads lost)
```

**Surfacing Accuracy**
```
# of threads surfaced at appropriate moment / # of surfacing attempts
Target: >70%
```

**Thread Resolution Rate**
```
# of threads addressed in draft / # of threads marked
Target: >60% for MAIN/COUNTER, lower acceptable for TANGENT/SPARK
```

### Eval Protocol

After each session:

1. **Review conversation for ideas that could have been threads**
2. **Check if they were marked**
   - Marked → Check
   - Not marked but should have been → Miss
3. **Check surfacing timing**
   - Surfaced when relevant → Appropriate
   - Surfaced too early/late → Misfire
   - Never surfaced → Lost

### Red Flags

- User re-states something they mentioned earlier (thread was lost)
- Multiple ideas discussed but never tracked
- Thread explosion (>10 threads, no resolution)
- Threads marked but never referenced again

---

## 3. Voice Calibration Evaluation

### Quantitative Metrics

**Prose-Polish Score**
```
Final draft AI detection score
Target: <20
Warning: 20-30
Fail: >30
```

**Blocklist Match Rate**
```
# of blocklist patterns in final draft / # of paragraphs
Target: 0
```

**Revision Rate**
```
# of passages Lee asked to revise for voice / # of passages drafted
Lower is better (getting voice right first time)
```

### Qualitative Metrics

**Recognition Test**
```
Could Lee read this in 6 months and recognize it as his own?
Binary: Yes / No
```

**Rhythm Match**
```
Compare sentence length distribution to WritingSamples/
Similar variation → Pass
Too uniform → Flag
```

**First-Person Ownership**
```
Does draft use "I" appropriately?
Avoids ownership → AI pattern
```

### Eval Protocol

After each session:

1. **Run prose-polish on final draft**
   - Score >25 → Investigate
2. **Scan for blocklist patterns**
   - Any tier 1 matches → Fail
3. **Compare to WritingSamples/**
   - Note rhythm, openings, example specificity
4. **Lee's subjective assessment**
   - "Does this sound like me?" (1-5 scale)

### Red Flags

- Prose-polish score rises during drafting (voice drifting)
- Lee frequently overrides calibration suggestions (false positives)
- Same blocklist pattern appears repeatedly (not learning)
- Draft is technically correct but "hollow"

---

## Composite Evaluation

### Session Scorecard

After each session, complete:

```markdown
## Session Eval: [Topic] - [Date]

### Interview
- Material usage rate: ___%
- Ground truth preserved: Yes / No
- Depth achieved: Phase 1 / 2 / 3
- Fabrications detected: ___

### Thread Tracking
- Threads marked: ___
- Threads lost: ___
- Surfacing accuracy: ___%
- Resolution rate: ___%

### Voice Calibration
- Prose-polish score: ___
- Blocklist matches: ___
- Revisions for voice: ___
- Lee's recognition: ___/5

### Overall
- Would use output as-is: Yes / Minor edits / Significant rework
- Key friction points: [describe]
- Suggested improvements: [describe]
```

### Aggregated Tracking

Over multiple sessions, track trends:

| Metric | Session 1 | Session 2 | Session 3 | Trend |
|--------|-----------|-----------|-----------|-------|
| Material usage | | | | |
| Thread loss rate | | | | |
| Prose-polish score | | | | |
| Lee's recognition | | | | |

**Improvement signals:**
- Scores trending down (better)
- Fewer revisions needed
- Fewer thread losses
- Higher recognition scores

**Warning signals:**
- Scores trending up (worse)
- Same friction points recurring
- New patterns appearing on blocklist
- Lee's recognition declining

---

## Specific Test Cases

### Test 1: Prose-Polish Essay Revision

The original failure case. Use this to validate the skill.

**Setup:**
- Start fresh—don't reference the failed draft
- Interview Lee about why he built prose-polish
- Track threads that emerge
- Draft with voice awareness
- Calibrate against samples

**Success criteria:**
- No fabricated experiences
- Lee's AI tell observation appears (his discovery, not invented)
- Final prose-polish score <20
- Lee recognizes voice as his own

### Test 2: New Topic (Cold Start)

Test with something Lee hasn't written about yet.

**Setup:**
- Pick unfamiliar topic
- Full interview (Phases 1-3)
- Track threads from scratch
- Draft with minimal reference samples

**Success criteria:**
- Interview extracts sufficient material
- Threads don't explode (manageable count)
- Voice calibration works without perfect sample match
- Ground truth maintained throughout

### Test 3: Complex/Divergent Topic

Test thread tracking under load.

**Setup:**
- Pick topic that invites tangents
- Encourage divergence during interview
- Track many threads
- Converge to draft

**Success criteria:**
- No threads lost
- Appropriate threads surfaced
- Draft integrates multiple threads coherently
- Escape hatch works if needed ("too many threads")

### Test 4: Voice Edge Cases

Test calibration sensitivity.

**Setup:**
- Intentionally draft in slightly different voice
- Run calibration
- Check detection accuracy

**Success criteria:**
- Calibration catches intentional drift
- No false positives on authentic voice
- Suggestions are actionable
- Final version passes

---

## Continuous Improvement Loop

### After Each Session

1. Complete session scorecard
2. Note friction points
3. Add new patterns to blocklist if discovered
4. Update WritingSamples/ if good output emerges

### Weekly Review

1. Review aggregated metrics
2. Identify recurring issues
3. Adjust skill prompts for top issues
4. Update evaluation criteria if needed

### Monthly Assessment

1. Is the skill getting better?
2. What patterns should be promoted to blocklist?
3. Should WritingSamples/ be refreshed?
4. Ready for Phase 2 (persistence) or still refining?

---

## Anti-Gaming

Evaluations should catch real issues, not just hit metrics.

**Avoid:**
- Optimizing prose-polish score by removing all personality
- High material usage by including everything (no curation)
- 100% thread resolution by marking fewer threads

**The real test:** Does Lee want to use the output?

If metrics are green but Lee rewrites everything, the metrics are wrong.

---

**Last updated:** 2025-12-19
