# Node Types Reference

Detailed guide for classifying captures into the appropriate node type.

## Classification Decision Tree

```
Is it actionable?
├── Yes → Has a completion state?
│   ├── Yes → Is it time-bound?
│   │   ├── Yes → MEETING
│   │   └── No → TASK
│   └── No → Is it a desired outcome?
│       ├── Yes → GOAL
│       └── No → Is it a collection of work?
│           ├── Yes → PROJECT
│           └── No → TASK (default actionable)
└── No → Is it about a person?
    ├── Yes → PERSON
    └── No → Is it a guiding principle?
        ├── Yes → VALUE
        └── No → Is it an insight/observation?
            ├── Yes → IDEA
            └── No → REFERENCE (default non-actionable)
```

## Type Details

### VALUE
**Definition:** Core principles that guide decisions and priorities.

**Characteristics:**
- Rarely changes over time
- Influences other decisions
- Abstract but deeply held
- Often discovered, not created

**Examples:**
- "Family comes first"
- "Always be learning"
- "Shipping beats perfection"
- "Transparency in communication"

**NOT a value:** Things you want to do (goals), things you believe (ideas), or things you know (references).

---

### GOAL
**Definition:** Desired outcomes you're actively working toward.

**Characteristics:**
- Has measurable success criteria
- Time-bounded (explicit or implicit)
- Supports one or more values
- Achieved through projects/tasks

**Examples:**
- "Run a marathon by December 2026"
- "Get promoted to Senior Engineer"
- "Launch the new product by Q2"
- "Build closer relationship with Dad"

**NOT a goal:** Ongoing activities (tasks), vague aspirations without criteria (ideas), or things you already know (references).

---

### PROJECT
**Definition:** Collection of related work with a defined outcome.

**Characteristics:**
- Contains multiple tasks
- Has clear completion criteria
- Supports one or more goals
- Has a defined scope

**Examples:**
- "Kitchen renovation"
- "API migration to v2"
- "Plan Sarah's birthday party"
- "Q1 performance reviews"

**NOT a project:** Single tasks, ongoing responsibilities (recurring tasks), or abstract goals.

---

### TASK
**Definition:** Specific actionable items that can be completed.

**Characteristics:**
- Single clear action
- Can be marked done
- Often part of a project
- May have a due date

**Examples:**
- "Call dentist to schedule appointment"
- "Review PR #1234"
- "Buy groceries for dinner"
- "Send quarterly report to Mike"

**NOT a task:** Vague intentions (ideas), multi-step projects, or reference information.

---

### PERSON
**Definition:** Context about relationships and people in your life.

**Characteristics:**
- Represents an individual
- Contains relationship context
- Links to tasks/meetings
- Tracks interaction history

**Examples:**
- "Sarah Chen - VP Engineering at Acme"
- "Dr. Martinez - Primary care physician"
- "Mom - calls every Sunday"
- "Mike - direct report, started Jan 2026"

**Fields:**
- Name
- Context/role
- How you know them
- Key details to remember

---

### MEETING
**Definition:** Time-bound events with specific participants.

**Characteristics:**
- Has a specific date/time
- Involves other people
- May generate action items
- Captures discussion notes

**Examples:**
- "1:1 with Sarah - Jan 15 at 10am"
- "Q1 Planning Meeting - Jan 20"
- "Dinner with parents - Sunday 6pm"
- "Interview: Backend Engineer candidate"

**Automatic extraction:**
- Action items → tasks
- Decisions → references
- People mentioned → person links

---

### IDEA
**Definition:** Non-actionable insights worth remembering.

**Characteristics:**
- Observation or hypothesis
- Not immediately actionable
- May inspire future work
- Worth revisiting later

**Examples:**
- "What if we used AI for customer onboarding?"
- "Noticed correlation between standup length and sprint velocity"
- "The best managers seem to ask more questions than give answers"
- "Reading before bed might be helping my sleep"

**NOT an idea:** Things you plan to do (tasks), things you know for sure (references), or principles you live by (values).

---

### REFERENCE
**Definition:** Information to retrieve later.

**Characteristics:**
- Factual information
- Lookup-oriented
- Not actionable
- Stable over time

**Examples:**
- "API rate limit is 1000 requests/minute"
- "Company WiFi password: hunter2"
- "Sarah's preferred pronouns: she/her"
- "Sprint planning happens every other Monday at 9am"

**NOT a reference:** Opinions or hypotheses (ideas), things to do (tasks), or guiding principles (values).

---

## Priority Levels

| Level | Name | Description | Example |
|-------|------|-------------|---------|
| 0 | Critical | Needs immediate attention | System down |
| 1 | High | Important, do soon | Due tomorrow |
| 2 | Medium | Normal priority (default) | Regular work |
| 3 | Low | Nice to have | Someday tasks |
| 4 | Backlog | Maybe someday | Ideas to revisit |

---

## Domain Classification

| Domain | Description | Signals |
|--------|-------------|---------|
| work | Professional context | Company names, coworkers, work projects |
| personal | Personal life | Family, hobbies, personal goals |
| both | Overlaps contexts | Career growth, health affecting work |

**Heuristics:**
- Mentions employer/coworkers → work
- Mentions family/friends → personal
- Professional development → both
- Health/wellness → personal (usually)
- Side projects → check intent
