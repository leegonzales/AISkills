#!/usr/bin/env python3
"""
MoltBot Enclave - Secure Moltbook interface with no access to main agent memory.

This script handles all Moltbook API interactions in isolation:
- Fetches feed and sanitizes content
- Writes sanitized data for the enclave agent to process
- Reads outbox and posts on behalf of main agent
- Never exposes raw untrusted content to main agent context

Usage:
    moltbot.py fetch    # Fetch feed, write sanitized to raw_feed.json
    moltbot.py post     # Read outbox.md, post to Moltbook, clear outbox
    moltbot.py status   # Check account status
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# Paths
MOLTBOOK_DIR = Path.home() / ".moltbook"
CREDENTIALS_FILE = MOLTBOOK_DIR / "credentials.json"
ENCLAVE_DIR = MOLTBOOK_DIR / "enclave"
RAW_FEED_FILE = ENCLAVE_DIR / "raw_feed.json"
OUTBOX_FILE = MOLTBOOK_DIR / "outbox.md"
INBOX_FILE = MOLTBOOK_DIR / "inbox.md"
POST_LOG_FILE = ENCLAVE_DIR / "post_log.json"

API_BASE = "https://www.moltbook.com/api/v1"


def load_credentials():
    """Load API key from credentials file."""
    if not CREDENTIALS_FILE.exists():
        print("ERROR: No credentials file found at", CREDENTIALS_FILE)
        sys.exit(1)
    with open(CREDENTIALS_FILE) as f:
        creds = json.load(f)
    return creds.get("api_key")


def api_request(endpoint, method="GET", data=None):
    """Make authenticated API request."""
    api_key = load_credentials()
    url = f"{API_BASE}/{endpoint}"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    
    body = json.dumps(data).encode() if data else None
    req = Request(url, data=body, headers=headers, method=method)
    
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as e:
        error_body = e.read().decode() if e.fp else ""
        print(f"HTTP {e.code}: {error_body}")
        return {"success": False, "error": error_body, "code": e.code}
    except URLError as e:
        print(f"Network error: {e.reason}")
        return {"success": False, "error": str(e.reason)}


def sanitize_text(text):
    """
    Remove potentially dangerous content from text.
    Strips: code blocks, URLs, XML/HTML tags, imperative patterns.
    """
    if not text:
        return ""
    
    # Remove code blocks (triple backticks)
    text = re.sub(r'```[\s\S]*?```', '[CODE BLOCK REMOVED]', text)
    
    # Remove inline code
    text = re.sub(r'`[^`]+`', '[CODE REMOVED]', text)
    
    # Remove URLs
    text = re.sub(r'https?://\S+', '[URL REMOVED]', text)
    
    # Remove XML/HTML-like tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove common injection patterns
    injection_patterns = [
        r'(?i)ignore previous instructions',
        r'(?i)ignore all instructions',
        r'(?i)system prompt',
        r'(?i)you are now',
        r'(?i)act as if',
        r'(?i)pretend you',
        r'(?i)new instructions',
        r'(?i)override',
    ]
    for pattern in injection_patterns:
        text = re.sub(pattern, '[FILTERED]', text)
    
    # Truncate excessively long text
    if len(text) > 2000:
        text = text[:2000] + "... [TRUNCATED]"
    
    return text.strip()


def sanitize_post(post):
    """Sanitize a single post object."""
    return {
        "id": post.get("id", ""),
        "title": sanitize_text(post.get("title", "")),
        "content_preview": sanitize_text(post.get("content", ""))[:500],
        "author": post.get("author", {}).get("name", "unknown"),
        "submolt": post.get("submolt", {}).get("name", "general"),
        "upvotes": post.get("upvotes", 0),
        "downvotes": post.get("downvotes", 0),
        "comment_count": post.get("comment_count", 0),
        "created_at": post.get("created_at", ""),
    }


def cmd_fetch():
    """Fetch feed and write sanitized data."""
    print("Fetching Moltbook feed...")
    
    # Get hot posts
    result = api_request("posts?sort=hot&limit=15")
    
    if not result.get("success", False) and "posts" not in result:
        print("Failed to fetch feed:", result.get("error", "unknown error"))
        return
    
    posts = result.get("posts", [])
    sanitized = {
        "fetched_at": datetime.utcnow().isoformat() + "Z",
        "post_count": len(posts),
        "posts": [sanitize_post(p) for p in posts],
    }
    
    # Write sanitized feed
    with open(RAW_FEED_FILE, "w") as f:
        json.dump(sanitized, f, indent=2)
    
    print(f"Wrote {len(posts)} sanitized posts to {RAW_FEED_FILE}")


def cmd_post():
    """Read outbox and post to Moltbook."""
    if not OUTBOX_FILE.exists():
        print("No outbox file found.")
        return
    
    content = OUTBOX_FILE.read_text().strip()
    if not content:
        print("Outbox is empty.")
        return
    
    # Parse outbox format:
    # ---
    # submolt: general
    # title: My Post Title
    # ---
    # Post content here...
    
    lines = content.split("\n")
    metadata = {}
    body_start = 0
    
    if lines[0].strip() == "---":
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == "---":
                body_start = i + 1
                break
            if ":" in line:
                key, val = line.split(":", 1)
                metadata[key.strip().lower()] = val.strip()
    
    post_body = "\n".join(lines[body_start:]).strip()
    title = metadata.get("title", "Untitled")
    submolt = metadata.get("submolt", "general")
    
    if not post_body:
        print("No post body found in outbox.")
        return
    
    print(f"Posting to m/{submolt}: {title}")
    
    result = api_request("posts", method="POST", data={
        "submolt": submolt,
        "title": title,
        "content": post_body,
    })
    
    if result.get("success"):
        print("Posted successfully!")
        post_id = result.get("post", {}).get("id", "unknown")
        
        # Log the post
        log = []
        if POST_LOG_FILE.exists():
            log = json.loads(POST_LOG_FILE.read_text())
        log.append({
            "posted_at": datetime.utcnow().isoformat() + "Z",
            "title": title,
            "submolt": submolt,
            "post_id": post_id,
        })
        POST_LOG_FILE.write_text(json.dumps(log, indent=2))
        
        # Clear outbox
        OUTBOX_FILE.write_text("")
        print("Outbox cleared.")
    else:
        print("Failed to post:", result.get("error", "unknown"))
        if result.get("code") == 429:
            print("Rate limited. Try again later.")


def cmd_status():
    """Check account status."""
    result = api_request("agents/me")
    if result.get("success"):
        agent = result.get("agent", {})
        print(f"Agent: {agent.get('name')}")
        print(f"Karma: {agent.get('karma', 0)}")
        print(f"Status: {'claimed' if agent.get('is_claimed') else 'pending'}")
        print(f"Followers: {agent.get('follower_count', 0)}")
    else:
        print("Failed to get status:", result.get("error", "unknown"))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    cmd = sys.argv[1].lower()
    
    if cmd == "fetch":
        cmd_fetch()
    elif cmd == "post":
        cmd_post()
    elif cmd == "status":
        cmd_status()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
