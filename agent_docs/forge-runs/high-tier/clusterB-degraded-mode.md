# HIGH-tier Forge — Cluster B: Degraded Mode (3 tool-absent confabulation skills)

Added a degraded-mode / anti-confabulation gate to 3 skills that invent content when their tool/MCP/CLI is absent. The shared rule: **a fact that depends on a tool you didn't run is not yours to assert — report unavailable, never confabulate.** All 3 self-tested PASS + validate.

| Skill | Bead | Gate |
|-------|------|------|
| **gemini-peer-review** | SKILL-44s | Only report what the `gemini` CLI actually returned this session; CLI absent/errors → "second opinion unavailable", proceed Claude-only, never invent "Gemini agrees…". (38KB bloat-trim deferred.) |
| **aws-cdk-development** | SKILL-buq | Service limits/quotas/regional-availability/runtime-versions must be verified vs the AWS-Docs MCP; absent → flag-for-verification / conditional / version-agnostic code, never assert a confident "X is supported" from memory. |
| **aws-cost-operations** | SKILL-1rg | Every account-specific figure (spend/cost/usage/savings) must come from a real MCP query; absent → refuse + name the data source + generic-labeled guidance only, never invent "$X spent". Added crisp Pricing/CostExplorer/Billing routing. |

**Caveats:** self-tests self-graded by the authoring agents (Cluster A's independent external verify confirmed the pattern generalizes); instruction-strength, not runtime interlock; directional (SKILL-t77). Incidental: both AWS agents flagged CLAUDE.md's validate path `./SkillPackager/scripts/validate-skill.sh` is stale (lives at `SkillTemplate/scripts/`) — logged to SKILL-j0z.
