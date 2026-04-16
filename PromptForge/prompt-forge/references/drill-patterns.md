# Drill Patterns

Eight drill types. Each exercises technique differently. Rotate across sessions so the user builds versatility — do not run the same type three sessions in a row.

Every drill is grounded in the user's actual work. If a drill requires a scenario the user doesn't face, pick a different drill type.

---

## 1. Construction

**Shape:** Build a prompt from scratch for a given scenario.

**Use when:** Introducing a new technique, or the user is at Level 1–2 and needs rep on the basics.

**Example:** "You mentioned you write quarterly business reviews. Write a zero-shot prompt that would produce a first draft. Then write the same prompt using RCCE. Run both and compare what changes."

**What to feedback on:** Structure, specificity of role/context, whether examples would have helped.

---

## 2. Diagnosis

**Shape:** Identify what is broken in a given prompt.

**Use when:** Building structural awareness — Skill 2 (Reverse Engineering) in the meta-prompting progression, or as a warm-up for Refinement.

**Example:** "Here's a prompt someone used to generate vendor evaluations that came back generic and unactionable. Before you run it, tell me what you predict will go wrong. Then run it. Compare."

**What to feedback on:** Did the user's diagnosis match what actually broke? What did they miss? What did they catch that the model would not?

---

## 3. Refinement

**Shape:** Improve an existing prompt iteratively.

**Use when:** The user has a prompt they use often that produces B-grade output. The ROI is high because refinement compounds across every future use.

**Example:** "Share the prompt you've been using for post-project reviews. Let's do three passes: first pass, add context the prompt is missing. Second pass, add a negative example. Third pass, add output format specification. Compare all four versions."

**What to feedback on:** Which pass produced the biggest quality jump? What does that tell you about where your prompts usually fall short?

---

## 4. Adaptation

**Shape:** Modify a working prompt for a new context.

**Use when:** Building Generalization. The user has a prompt that works in domain A and wants to move it to domain B.

**Example:** "Your post-project review prompt works for construction projects. Adapt it for evaluating a vendor contract renewal. What stays, what changes, what new constraints appear?"

**What to feedback on:** Did they preserve the structural bones and swap the domain-specific parts, or did they rewrite from scratch? Cleaner adaptation = stronger pattern recognition.

---

## 5. Comparison

**Shape:** Evaluate two or three approaches and pick the best.

**Use when:** Building evaluation muscle. Skill 4 (Prompt Generation) in the meta-prompting progression maps to this.

**Example:** "Ask Claude to write three different prompts for summarizing a 90-minute stakeholder meeting into action items, each taking a different approach. Evaluate all three against: clarity of action items, traceability to who said what, handling of ambiguous asks. Pick one and say why."

**What to feedback on:** Did they have a rubric, or were they picking by vibe? Teach them to name evaluation criteria before running the comparison.

---

## 6. Chain

**Shape:** Design a multi-step prompt sequence where the output of one becomes input of the next.

**Use when:** Building Reach. Moving from single-prompt thinking to system thinking.

**Example:** "Design a three-prompt chain for turning a raw meeting transcript into a polished executive summary: (1) extract decisions and action items, (2) draft narrative summary, (3) tighten for executive audience. What's the handoff format between each step?"

**What to feedback on:** Clean handoffs (structured output from step N becomes structured input to step N+1) separate working chains from broken ones.

---

## 7. Stress Test

**Shape:** Break a prompt deliberately, then fix it.

**Use when:** Building Execution Fidelity. Understanding failure modes by inducing them.

**Example:** "Take your best current prompt. Give it input that's deliberately ambiguous (or too long, or contradictory). Where does it break? Modify the prompt so it handles that failure gracefully."

**What to feedback on:** Did they patch symptoms or fix the underlying design? Good error recovery is architectural, not defensive.

---

## 8. Teaching

**Shape:** Explain a technique to a hypothetical colleague.

**Use when:** Cementing understanding. You don't know a technique until you can teach it.

**Example:** "A colleague asks you why you use RCCE. In under 90 seconds, explain it, give one example, and say when it's overkill."

**What to feedback on:** Conceptual clarity. Where they hedged or fumbled is where they don't yet own the technique.

---

## Drill selection heuristics

- **Level 1–2 user:** Construction and Diagnosis. Build basic structural awareness first.
- **Level 2–3 user:** Refinement, Adaptation, Comparison. Sharpening and transfer.
- **Level 3–4 user:** Chain, Stress Test, and the meta-prompting progression. Systems and self-direction.
- **Level 4–5 user:** Pattern extraction (from techniques.md), production scenarios, evaluation framework design.

**Rotate types within a session:** If the user is doing a 60-minute deep session, mix Construction and Diagnosis, or Refinement and Comparison. Variety exercises different muscles.

**If a drill falls flat:** Don't force the loop. Ask what didn't land, pick a different drill type, try again. One awkward drill is data; three in a row is a signal to slow down and talk about what the user actually wants to work on.
