# Flywheel Scan Event Schema

**Version:** 1.0
**Purpose:** Defines all event types emitted by scouts and doppelganger during a flywheel scan.

---

## Top-Level Structure

```json
{
  "session": {
    "id": "flywheel-scan",
    "title": "Cross-Project Roadmap Discovery",
    "date": "YYYY-MM-DD",
    "duration_min": null
  },
  "agents": [
    { "id": "scout-biz", "name": "Scout: Business", "role": "Domain Scanner", "color": "#3182CE" }
  ],
  "events": [ ... ]
}
```

---

## Event Types

### 1. `scan_start`

Scout begins scanning a repo.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | yes | `"scan_start"` |
| `agent` | string | yes | Agent ID (e.g., `"scout-biz"`) |
| `repo` | string | yes | Short repo path (e.g., `"catalyst/coaching"`) |
| `time_offset` | int | yes | Ordinal position in scan sequence |

### 2. `scan_finding`

Discovery during repo scan.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | yes | `"scan_finding"` |
| `agent` | string | yes | Agent ID |
| `repo` | string | yes | Short repo path |
| `finding_type` | string | yes | `"code_state"` \| `"risk"` \| `"deadline"` \| `"plan_doc"` \| `"beads_issue"` \| `"gap"` \| `"blocker"` |
| `text` | string | yes | Description of finding |
| `severity` | string | yes | `"info"` \| `"warn"` \| `"high"` |

### 3. `repo_triage`

Classification decision for a repo.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | yes | `"repo_triage"` |
| `agent` | string | yes | Agent ID |
| `repo` | string | yes | Short repo path |
| `classification` | string | yes | `"active-invest"` \| `"maintain"` \| `"archive"` |
| `rationale` | string | yes | Why this classification |
| `goals_alignment` | string[] | yes | Which goals this repo serves (e.g., `["Revenue", "Capability"]`) |
| `proposed_beads` | object[] | no | Array of `{ title, priority, energy?, description? }` |

### 4. `repo_missing`

Repo path doesn't exist or isn't accessible.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | yes | `"repo_missing"` |
| `agent` | string | yes | Agent ID |
| `repo` | string | yes | Short repo path |
| `detail` | string | yes | Error description |

### 5. `observation`

Commentary from any agent.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | yes | `"observation"` |
| `agent` | string | yes | Agent ID |
| `text` | string | yes | Observation text |

### 6. `priority_score`

Doppelganger scores a proposed work item.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | yes | `"priority_score"` |
| `agent` | string | yes | `"lee-doppelganger"` |
| `repo` | string | yes | Short repo path |
| `bead_title` | string | yes | Work item title |
| `scores` | object | yes | `{ goals_alignment, energy_impact_ratio, unblocking_value, tension_awareness }` — each 1-5 |
| `total` | int | yes | Sum of 4 scores (max 20) |
| `rank` | int | yes | Position in ranked queue |
| `rationale` | string | yes | Why this score |

### 7. `thread_proposal`

Doppelganger proposes options for an open strategic thread.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | yes | `"thread_proposal"` |
| `agent` | string | yes | `"lee-doppelganger"` |
| `thread_id` | string | yes | Stable thread identifier |
| `thread_title` | string | yes | Human-readable thread name |
| `options` | object[] | yes | Array of `{ label, description, trade_offs, recommendation: bool }` |
| `lee_voice` | string | no | Doppelganger's voice quote |

### 8. `master_queue`

Final ranked work queue (single event, emitted last).

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | yes | `"master_queue"` |
| `agent` | string | yes | `"lee-doppelganger"` |
| `queue` | object[] | yes | Array of `{ rank, repo, title, score, energy }` |

---

## Supplementary Event Types

These may appear but are not required:

| Type | When | Key Fields |
|------|------|------------|
| `scan_complete` | Scout finishes a repo | `repo`, `classification`, `detail` |
| `scan_end` | Scout finishes all repos | `detail` |
| `roadmap_proposal` | Scout proposes milestones for top repos | `repo`, `milestones[]`, `text` |

---

## Agent ID Conventions

Agent IDs must match exactly: `scout-biz`, `scout-training`, `scout-tooling`, `scout-personal`, `lee-doppelganger`.

## Repo Path Conventions

Use short paths relative to `~/Projects/`: e.g., `catalyst/coaching`, `leegonzales/cass`, `Difflab/bizops`. Drop the `~/Projects/` prefix for readability.
