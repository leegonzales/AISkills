#!/usr/bin/env python3
"""Post fleet line-anchored review comments to a GitHub PR.

The orchestrator (e.g. Adama) calls this AFTER collecting structured,
line-anchored comments from fleet persona subagents. Subagents have no
`gh` access and no GitHub identity, so attribution lives in the comment
BODY (prefixed with the persona name), not the GitHub author.

Why a script (not inline gh): line-level comment payloads must pin to a
commit_id + path + line + side, the `line` field must serialize as an
integer (the `gh api -F/-f` repeated-array form is fragile about this),
and we want per-comment success/failure reporting + diff validation.
Piping a JSON object to `gh api --input -` sidesteps the typing problem
entirely. This is the proven posting path.

Usage:
    post_fleet_comments.py --repo OWNER/REPO --pr N --comments comments.json
    post_fleet_comments.py --repo OWNER/REPO --pr N --comments - < comments.json
    # add --dry-run to validate + print payloads without posting.

comments.json shape — a JSON array of objects:
    [
      {"agent": "Pike",   "path": "src/foo.py", "line": 42, "comment": "..."},
      {"agent": "Thufir", "path": "src/foo.py", "line": 17, "side": "RIGHT",
       "start_line": 15, "comment": "multi-line anchor ..."}
    ]

Fields:
    agent      (required) persona name; prefixed as **[Agent]** in the body.
    path       (required) file path as it appears in the PR diff.
    line       (required) line number in the file (RIGHT side by default).
    comment    (required) the review text.
    side       (optional) "RIGHT" (added/context, default) or "LEFT" (deleted).
    start_line (optional) for a multi-line comment range; with start_side.
    start_side (optional) side for start_line (defaults to side).

The commit_id is resolved automatically to the PR head SHA (override with
--commit). Each comment is posted independently so one failure never blocks
the rest, and every result is reported.
"""
import argparse
import json
import subprocess
import sys


def run_gh(args, input_str=None):
    return subprocess.run(
        ["gh", *args],
        input=input_str,
        capture_output=True,
        text=True,
    )


def pr_head_sha(repo, pr):
    p = run_gh(["pr", "view", str(pr), "--repo", repo,
                "--json", "headRefOid", "--jq", ".headRefOid"])
    if p.returncode != 0:
        sys.exit(f"FATAL: could not resolve PR head SHA: {p.stderr.strip()}")
    return p.stdout.strip()


def addressable_lines(repo, pr):
    """Map {path: set(RIGHT-side line numbers addressable in the diff)}.

    A line is addressable on the RIGHT side if it is an added (+) line or a
    context line in a hunk. We parse `gh pr diff` hunk headers and walk lines.
    LEFT-side validation is best-effort; LEFT comments skip strict validation.
    """
    p = run_gh(["pr", "diff", str(pr), "--repo", repo])
    if p.returncode != 0:
        # Non-fatal: skip validation rather than block posting.
        sys.stderr.write(f"WARN: could not fetch diff for validation: "
                         f"{p.stderr.strip()}\n")
        return None
    result = {}
    cur_path = None
    new_ln = 0
    for raw in p.stdout.splitlines():
        if raw.startswith("+++ b/"):
            cur_path = raw[6:]
            result.setdefault(cur_path, set())
        elif raw.startswith("@@"):
            # @@ -a,b +c,d @@
            try:
                plus = raw.split("+", 1)[1].split(" ", 1)[0]
                new_ln = int(plus.split(",")[0])
            except (IndexError, ValueError):
                new_ln = 0
        elif cur_path is not None and (raw.startswith(" ") or raw.startswith("+")):
            if not raw.startswith("+++"):
                result[cur_path].add(new_ln)
                new_ln += 1
        elif cur_path is not None and raw.startswith("-"):
            pass  # deleted line: advances OLD only, not new_ln
    return result


def build_payload(c, commit_id):
    agent = c["agent"]
    body = f"**[{agent}]** {c['comment']}"
    payload = {
        "body": body,
        "commit_id": commit_id,
        "path": c["path"],
        "line": int(c["line"]),
        "side": c.get("side", "RIGHT"),
    }
    if "start_line" in c and c["start_line"] is not None:
        payload["start_line"] = int(c["start_line"])
        payload["start_side"] = c.get("start_side", payload["side"])
    return payload


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", required=True, help="OWNER/REPO")
    ap.add_argument("--pr", required=True, type=int, help="PR number")
    ap.add_argument("--comments", required=True,
                    help="path to JSON array file, or '-' for stdin")
    ap.add_argument("--commit", help="commit_id to pin to (default: PR head SHA)")
    ap.add_argument("--dry-run", action="store_true",
                    help="validate + print payloads, post nothing")
    ap.add_argument("--no-validate", action="store_true",
                    help="skip diff line-validation")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.comments == "-" else open(args.comments).read()
    try:
        comments = json.loads(raw)
    except json.JSONDecodeError as e:
        sys.exit(f"FATAL: comments is not valid JSON: {e}")
    if not isinstance(comments, list):
        sys.exit("FATAL: comments JSON must be an array of objects")

    commit_id = args.commit or pr_head_sha(args.repo, args.pr)
    valid_map = None if args.no_validate else addressable_lines(args.repo, args.pr)

    endpoint = f"/repos/{args.repo}/pulls/{args.pr}/comments"
    n_ok = n_fail = n_skip = 0

    for i, c in enumerate(comments):
        missing = [k for k in ("agent", "path", "line", "comment") if k not in c]
        if missing:
            print(f"  [{i}] SKIP   missing fields: {missing}")
            n_skip += 1
            continue

        line, path, agent = int(c["line"]), c["path"], c["agent"]
        side = c.get("side", "RIGHT")

        # Validate the line is addressable on the RIGHT side of the diff.
        if valid_map is not None and side == "RIGHT":
            if path not in valid_map:
                print(f"  L{line:<4} {agent:<10} SKIP   path not in diff: {path}")
                n_skip += 1
                continue
            if line not in valid_map[path]:
                near = sorted(valid_map[path])
                hint = f" (addressable: {near[:1]}..{near[-1:]})" if near else ""
                print(f"  L{line:<4} {agent:<10} SKIP   line not in diff{hint}")
                n_skip += 1
                continue

        payload = build_payload(c, commit_id)

        if args.dry_run:
            print(f"  L{line:<4} {agent:<10} DRY    {path}")
            print("         " + json.dumps(payload))
            continue

        p = run_gh(["api", "--method", "POST", endpoint, "--input", "-"],
                   input_str=json.dumps(payload))
        if p.returncode == 0:
            url = ""
            try:
                url = json.loads(p.stdout).get("html_url", "")
            except json.JSONDecodeError:
                pass
            print(f"  L{line:<4} {agent:<10} OK     {url}")
            n_ok += 1
        else:
            print(f"  L{line:<4} {agent:<10} FAIL   {p.stderr.strip()[:140]}")
            n_fail += 1

    print()
    if args.dry_run:
        print(f"DRY RUN: {len(comments)} comments, {n_skip} would-skip, "
              f"rest ready to post against {commit_id[:8]}")
    else:
        print(f"posted {n_ok} OK, {n_fail} FAIL, {n_skip} SKIP "
              f"(of {len(comments)}) against {commit_id[:8]}")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
