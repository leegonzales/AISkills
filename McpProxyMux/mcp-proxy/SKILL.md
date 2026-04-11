---
name: mcp-proxy
description: Manage the MCP proxy multiplexer that wraps stdio MCP servers as shared HTTP endpoints. Use when checking MCP proxy health, troubleshooting MCP tool failures, starting/stopping the proxy, or managing proxied server configs. Triggers include "mcp proxy", "check mcp servers", "proxy status", MCP tool errors, or fleet resource management.
---

# MCP Proxy Mux

Multiplexing proxy that runs **one** stdio MCP server process per service and exposes each as an HTTP endpoint. All Claude Code agents share the single backend instead of each spawning their own copy.

## When to Use

Invoke when:
- MCP tool calls fail or timeout (check if proxy is running)
- User asks about MCP proxy status, health, or server processes
- Fleet is launching and MCP servers need to be confirmed running
- User asks to add/remove a server from the proxy
- Troubleshooting resource usage or high process count
- User says "check mcp servers", "proxy status", or "mcp proxy"

## Architecture

```
17 Claude Code agents ──POST /mcp──► HTTP Server (:port) ──► 1 stdio process
```

Each proxied server gets its own port (9100-9105). Claude Code connects via `{"type": "http", "url": "http://127.0.0.1:<port>/mcp"}` instead of spawning a stdio child.

## Core Commands

```bash
# Check health of all proxied servers
mcp-proxy-mux --status

# Start all servers
mcp-proxy-mux

# Start a single server
mcp-proxy-mux --server brave-search

# Debug logging
mcp-proxy-mux -v

# Custom config
mcp-proxy-mux -c /path/to/config.toml
```

## Proxied Servers

| Server | Port | Type | Status |
|--------|------|------|--------|
| google-workspace-personal | 9100 | node (GWS personal) | LIVE |
| google-workspace | 9101 | node (GWS org) | LIVE |
| nanobanana-mcp | 9102 | node (image gen) | LIVE |
| brave-search | 9103 | npx (web search) | disabled (no API key) |
| netlify | 9104 | npx (deploy) | LIVE |
| veo-mcp | 9105 | node (video gen) | LIVE |

## NOT Proxied (and why)

- **chrome-devtools, playwright** — browser session state; concurrent agents would conflict
- **mattermost-channel** — per-agent identity (unique bot tokens)
- **mcp-agent-mail, imessage** — already HTTP (shared)
- **maps-grounding-lite, stripe** — already cloud HTTP endpoints

## Health Check

Each server exposes `/health`:

```bash
curl http://127.0.0.1:9102/health
# {"status": "ok", "server": "nanobanana-mcp", "pid": 12345, "sessions": 3}
```

Or check all at once:
```bash
mcp-proxy-mux --status
```

## Troubleshooting

**MCP tool call fails with connection error:**
```bash
# Is the proxy running?
mcp-proxy-mux --status

# If not, start it
mcp-proxy-mux &
```

**A single server is down but others work:**
```bash
# Check that specific server
curl http://127.0.0.1:9103/health

# Restart just that server
mcp-proxy-mux --server brave-search
```

**High memory / CPU from MCP processes:**
```bash
# Check if agents are still spawning their own stdio servers
# (they shouldn't be if settings.json is updated)
ps aux | grep -E "workspace-server|nanobanana|brave-search" | grep -v grep | wc -l
# Should show 6 (one per proxied server), not 17+
```

## Config Location

```
~/Projects/leegonzales/dev-environment/mcp-proxy/config.toml
```

To add a new server, add a `[servers.<name>]` block with `command`, `args`, `port`, and optional `env`.

## Launchd Daemon

The proxy runs as a launchd daemon (`com.mcp-proxy-mux.daemon`) so it starts at boot before the fleet:

```bash
# Check daemon status
launchctl list | grep mcp-proxy

# Restart daemon
launchctl kickstart -k gui/$(id -u)/com.mcp-proxy-mux.daemon
```

## Settings.json Mapping

When the proxy is running, Claude Code settings.json entries look like:

```json
"nanobanana-mcp": {
  "type": "http",
  "url": "http://127.0.0.1:9102/mcp"
}
```

Instead of the old stdio format:
```json
"nanobanana-mcp": {
  "command": "node",
  "args": ["/path/to/nanobanana-mcp/dist/index.js"]
}
```
