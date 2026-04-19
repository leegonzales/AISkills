# Changelog — fleetops

## [1.0.0] — 2026-04-19

### Added

- Initial skill release.
- `SKILL.md` agent-facing primer covering what FleetOps is, why it matters, the full verb map, composition patterns, and the new wake ritual (TEMPLATE_UPDATE v4).
- `README.md` with purpose, scope, dependencies, success criteria, and known limitations.
- `references/tool-reference.md` — man-page-style flag reference for every verb.
- `references/wake-ritual.md` — step-by-step wake open and close-out with real commands.
- `references/permission-model.md` — `session-stamp`, `FLEETOPS_SESSION_ID`, write-rejection failure modes.
- `references/troubleshooting.md` — common failures: rejected writes, doctor failures, wake_number collisions, harvester stalls.
- `references/bulk-import-kata.md` — operator-supervised one-time migration of `.servitor/journal.md` into `fleet.db`, triggered by Lee hailing each agent in Mattermost.

### Context

FleetOps v1 is live on `servitor` main. Journal-write verbs (`add/update/show/tail/grep/render`) are being added in parallel with this skill. TEMPLATE_UPDATE v4 will roll the new wake ritual into the base servitor protocol once Pike signs off on this skill.
