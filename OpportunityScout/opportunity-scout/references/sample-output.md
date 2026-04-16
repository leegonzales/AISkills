# Sample Output — Complete Scout Session

An example of what a full Opportunity Scout session output looks like at the Close. Use this as a reference for the level of specificity and concreteness expected. The user leaves with *this*, not a list of possibilities.

---

## Example: Executive at a design-build construction firm

**Opening answers:**
1. "I run a ~$1B construction design-build business. Spend my week in project reviews, client escalations, and partner / team development."
2. "Post-project reviews. We do them across 40+ jobs a year and the lessons are basically never integrated back into the next project. It's a graveyard of PDFs."
3. "I use Claude for drafting emails and occasional strategic thinking. Glean for internal search."
4. "B — change how my team works."

**Mode:** Workflow Scout.

**Terrain (Stage 1):** Work sits in Procore, Glean, Outlook, and SharePoint. Post-project reviews are completed by project managers, submitted as PDFs, filed, and functionally never read again. Lessons travel via tribal knowledge. 75% of revenue is repeat clients, so compounding lessons across projects is particularly high-leverage.

**Opportunity map (Stage 2), ranked:**

| Move | Pattern | Feas. | Impact | Total |
|------|---------|-------|--------|-------|
| Synthesize patterns across 40 post-project reviews into a quarterly lessons-integrated memo | Invisible-to-Visible | 4 | 5 | 9 |
| Build a pre-mortem prompt run at project kickoff that queries past reviews for warning signs | Impossible-to-Possible | 3 | 5 | 8 |
| Draft post-project reviews from project artifacts (timelines, RFIs, close-out) | Days-to-Hours | 4 | 4 | 8 |
| Monthly project-health briefing from cross-project ops data | Days-to-Hours | 3 | 4 | 7 |
| Executive daily morning briefing | Hours-to-Minutes | 5 | 2 | 7 |

**Ember (Stage 3):** User picks the first — *synthesize patterns across post-project reviews into a quarterly lessons memo*.

**Pattern named:** "That's Making the Invisible Visible. The insight already exists in those 40 PDFs — the bottleneck is that no single person is reading all of them. The design question isn't 'can AI read,' it's 'what shape of output will your PMs and execs actually read — and act on?'"

**Constraints surfaced:**
- PDFs are in SharePoint, not yet structured. Need to extract.
- User wants the output consumable in a 30-min quarterly review.
- Traceability matters — execs will want to know which projects the claims come from.

---

## Close (the four-line summary the user walks away with)

```
Pattern:    Making the Invisible Visible
Move:       Build a quarterly lessons-integrated memo that synthesizes
            post-project reviews into 3–5 cross-project patterns with
            project-level source citations, consumable in a 30-min
            quarterly exec review.
First step: In the next 24 hours — pick 10 recent post-project review
            PDFs, drop them in a Claude project, and run a v0
            synthesis prompt (draft attached). Read the output with
            your COO. Decide if the shape is right before scaling.
Evaluation: In 4 weeks — can you name 3 cross-project patterns that
            changed a project decision, and can you trace each one
            back to the source reviews?
```

---

## 4-Week Launch Plan

### Week 1 — Setup and first attempt
- **Action:** Pick 10 recent post-project reviews. Extract text from PDFs. Run v0 synthesis prompt in a Claude project.
- **Decision point:** Does the output shape pass the "would my COO actually read this" test?
- **Evaluate:** Are the patterns specific enough to be useful, or are they generic truisms?

### Week 2 — Iteration based on what broke
- **Action:** Identify the top failure mode from Week 1 (likely: citations are weak, or patterns are too abstract). Revise prompt. Re-run on the same 10.
- **Decision point:** Is the revised output good enough to defend in front of the exec team?
- **Evaluate:** Compare v0 and v1 side-by-side. What did the revision fix?

### Week 3 — Integration into real workflow
- **Action:** Run on the full quarter's post-project reviews (~10 projects this quarter). Bring the output to the actual quarterly exec meeting.
- **Decision point:** Did anyone change a decision because of what was surfaced?
- **Evaluate:** Watch for the moment an exec says "we should change how we do X" — that's the signal the pattern paid off.

### Week 4 — Evaluation
- **Action:** Review the four weeks. Does this live? Does it need to become a recurring quarterly artifact? Who owns running it?
- **Decision point:** Keep / refactor / park.
- **Evaluate:** The 4-week evaluation question — "Can you name 3 patterns that changed a decision, traced to sources?" If yes, institutionalize. If no, diagnose: was it the prompt, the inputs, the output format, or was the pattern wrong for this work?

---

## Why this is the shape

- **One move, not five.** The user has a plan, not a buffet.
- **First step is concrete and ~1 hour of work.** It happens in the next 24–72 hours, or it doesn't happen at all.
- **Evaluation is decision-coupled.** "Did this change what we did?" beats "was the output good?"
- **Pattern named explicitly.** The user can now carry the concept to other opportunities. Next time they face unstructured information, they'll recognize the shape.

This is what good looks like. Aim here.
