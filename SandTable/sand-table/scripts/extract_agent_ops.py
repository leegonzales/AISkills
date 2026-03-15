#!/usr/bin/env python3
"""Extract agent-ops events from Claude Code session logs.

Transforms JSONL conversation logs into Sand Table Protocol-compliant
event streams. This is LOG REPLAY, not simulation — we transform real traces.

Input: JSONL session logs from ~/.claude/projects/{encoded-path}/
Output: Protocol-compliant JSON with agent-ops events

Usage:
    python extract_agent_ops.py --project ~/Projects/myrepo -o agent-ops.json
    python extract_agent_ops.py --session <session-file.jsonl> -o agent-ops.json
    python extract_agent_ops.py --project ~/Projects/myrepo --since 2026-03-14 -o out.json
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


# Maps Claude Code tool names to agent-ops event types
TOOL_EVENT_MAP = {
    "Task": "agent_spawn",
    "Bash": "command",
    "Write": "file_change",
    "Edit": "file_change",
    "TaskCreate": "task_event",
    "TaskUpdate": "task_event",
    "SendMessage": "message",
}


def _encode_project_path(project_path: str) -> str:
    """Convert a project path to Claude's encoded directory format.

    /Users/lee/Projects/foo → -Users-lee-Projects-foo
    """
    return project_path.replace("/", "-")


def _find_session_files(
    project_path: Path, since: str | None = None
) -> list[Path]:
    """Find JSONL session files for a project."""
    encoded = _encode_project_path(str(project_path.resolve()))
    log_dir = Path.home() / ".claude" / "projects" / encoded

    if not log_dir.exists():
        print(f"Error: No session logs found at {log_dir}", file=sys.stderr)
        sys.exit(1)

    files = sorted(log_dir.glob("*.jsonl"), key=lambda p: p.stat().st_mtime)

    if since:
        try:
            since_dt = datetime.fromisoformat(since).replace(tzinfo=timezone.utc)
        except ValueError:
            since_dt = datetime.strptime(since, "%Y-%m-%d").replace(
                tzinfo=timezone.utc
            )
        files = [
            f for f in files
            if datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc) >= since_dt
        ]

    return files


def _parse_tool_use(block: dict, timestamp: str) -> dict | None:
    """Convert a tool_use content block into an agent-ops event."""
    tool = block.get("name", "")
    inp = block.get("input", {})
    tool_id = block.get("id", "")

    if tool == "Task":
        return {
            "type": "agent_spawn",
            "timestamp": timestamp,
            "agent": inp.get("name", inp.get("description", "unnamed")),
            "prompt_excerpt": (inp.get("prompt", "") or "")[:200],
            "background": bool(inp.get("run_in_background", False)),
            "_tool_use_id": tool_id,
        }

    if tool == "Bash":
        return {
            "type": "command",
            "timestamp": timestamp,
            "command": (inp.get("command", "") or "")[:500],
            "description": inp.get("description", ""),
            "_tool_use_id": tool_id,
        }

    if tool in ("Write", "Edit"):
        return {
            "type": "file_change",
            "timestamp": timestamp,
            "operation": tool.lower(),
            "file_path": inp.get("file_path", ""),
            "_tool_use_id": tool_id,
        }

    if tool == "TaskCreate":
        return {
            "type": "task_event",
            "timestamp": timestamp,
            "action": "create",
            "subject": inp.get("subject", inp.get("description", "")),
            "status": "pending",
            "_tool_use_id": tool_id,
        }

    if tool == "TaskUpdate":
        return {
            "type": "task_event",
            "timestamp": timestamp,
            "action": "update",
            "subject": "",
            "status": inp.get("status", ""),
            "owner": inp.get("owner", ""),
            "_tool_use_id": tool_id,
        }

    if tool == "SendMessage":
        return {
            "type": "message",
            "timestamp": timestamp,
            "sender": "orchestrator",
            "recipient": inp.get("recipient", inp.get("target_agent_id", "")),
            "content_excerpt": (inp.get("content", "") or "")[:200],
            "_tool_use_id": tool_id,
        }

    return None


def _parse_tool_result(block: dict, timestamp: str) -> dict | None:
    """Check tool results for errors."""
    if block.get("is_error"):
        content = block.get("content", "")
        if isinstance(content, list):
            content = content[0].get("text", "") if content else ""
        return {
            "type": "error",
            "timestamp": timestamp,
            "tool_use_id": block.get("tool_use_id", ""),
            "error_excerpt": str(content)[:500],
        }
    return None


def _parse_session_file(path: Path) -> list[dict]:
    """Parse a single JSONL session file into agent-ops events."""
    events = []
    tool_use_ids: dict[str, dict] = {}  # id → event for correlation

    with open(path) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue

            timestamp = record.get("timestamp", "")
            msg = record.get("message", {})
            content_blocks = msg.get("content", [])

            if not isinstance(content_blocks, list):
                continue

            for block in content_blocks:
                if not isinstance(block, dict):
                    continue

                btype = block.get("type", "")

                if btype == "tool_use":
                    event = _parse_tool_use(block, timestamp)
                    if event:
                        tool_id = event.pop("_tool_use_id", "")
                        if tool_id:
                            tool_use_ids[tool_id] = event
                        events.append(event)

                elif btype == "tool_result":
                    error_event = _parse_tool_result(block, timestamp)
                    if error_event:
                        # Try to enrich with tool name from correlated call
                        corr_id = error_event.get("tool_use_id", "")
                        if corr_id in tool_use_ids:
                            corr = tool_use_ids[corr_id]
                            error_event["tool"] = corr.get("type", "unknown")
                        events.append(error_event)

    return events


def _discover_agents(events: list[dict]) -> list[dict]:
    """Build agents array from spawned agent names and message participants."""
    agent_names = set()
    agent_names.add("orchestrator")

    for ev in events:
        if ev["type"] == "agent_spawn":
            agent_names.add(ev.get("agent", ""))
        if ev["type"] == "message":
            agent_names.add(ev.get("sender", ""))
            agent_names.add(ev.get("recipient", ""))
        if ev["type"] == "task_event":
            owner = ev.get("owner", "")
            if owner:
                agent_names.add(owner)

    agent_names.discard("")
    return [
        {"id": name, "name": name, "role": "subagent" if name != "orchestrator" else "lead"}
        for name in sorted(agent_names)
    ]


def _get_git_commits(
    project_path: Path, since: str | None = None
) -> list[dict]:
    """Extract git commits from the project for enrichment."""
    cmd = ["git", "-C", str(project_path), "log", "--format=%H|%h|%aI|%s", "--no-merges"]
    if since:
        cmd.extend([f"--since={since}"])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            return []
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []

    commits = []
    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        parts = line.split("|", 3)
        if len(parts) < 4:
            continue

        # Get file count for this commit
        stat_cmd = [
            "git", "-C", str(project_path), "diff-tree",
            "--no-commit-id", "--name-only", "-r", parts[0],
        ]
        try:
            stat_result = subprocess.run(
                stat_cmd, capture_output=True, text=True, timeout=10
            )
            files_changed = len([
                l for l in stat_result.stdout.strip().split("\n") if l
            ])
        except (subprocess.TimeoutExpired, FileNotFoundError):
            files_changed = 0

        commits.append({
            "type": "commit",
            "timestamp": parts[2],
            "hash": parts[1],
            "message": parts[3],
            "files_changed": files_changed,
        })

    return commits


def extract(
    project_path: Path | None = None,
    session_file: Path | None = None,
    since: str | None = None,
) -> dict:
    """Extract agent-ops events from Claude Code sessions.

    Returns a protocol-compliant dict.
    """
    if session_file:
        session_files = [session_file]
        effective_project = project_path
    elif project_path:
        session_files = _find_session_files(project_path, since)
        effective_project = project_path
    else:
        print("Error: provide --project or --session", file=sys.stderr)
        sys.exit(1)

    # Parse all sessions
    all_events = []
    for sf in session_files:
        print(f"  Parsing: {sf.name}", file=sys.stderr)
        all_events.extend(_parse_session_file(sf))

    # Enrich with git commits
    if effective_project:
        commits = _get_git_commits(effective_project, since)
        all_events.extend(commits)
        print(f"  Git commits: {len(commits)}", file=sys.stderr)

    # Sort chronologically
    def sort_key(ev):
        ts = ev.get("timestamp", "")
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            return datetime.min.replace(tzinfo=timezone.utc)

    all_events.sort(key=sort_key)

    # Clean up internal fields
    for ev in all_events:
        ev.pop("tool_use_id", None)

    # Build output
    agents = _discover_agents(all_events)
    project_name = (
        effective_project.name if effective_project
        else session_file.stem if session_file
        else "unknown"
    )

    return {
        "meta": {
            "domain": "agent-ops",
            "id": project_name,
            "title": f"Agent-Ops — {project_name}",
            "created": datetime.now(timezone.utc).isoformat(),
            "source": "extraction",
            "run": 1,
        },
        "agents": agents,
        "events": all_events,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract agent-ops events from Claude Code session logs."
    )
    parser.add_argument(
        "--project", type=Path, default=None,
        help="Path to the project repository"
    )
    parser.add_argument(
        "--session", type=Path, default=None,
        help="Path to a specific .jsonl session file"
    )
    parser.add_argument(
        "--since", type=str, default=None,
        help="Filter sessions modified after this date (ISO or YYYY-MM-DD)"
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=None,
        help="Output JSON path (default: stdout)"
    )
    args = parser.parse_args()

    if not args.project and not args.session:
        parser.error("Provide --project or --session")

    print("Agent-Ops Extractor", file=sys.stderr)
    print("=" * 40, file=sys.stderr)

    data = extract(
        project_path=args.project,
        session_file=args.session,
        since=args.since,
    )

    print(
        f"\n  Extracted: {len(data['events'])} events, "
        f"{len(data['agents'])} agents",
        file=sys.stderr,
    )

    output = json.dumps(data, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
        print(f"  Wrote: {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
