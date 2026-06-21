# MCP Proxy Skill

A guide for managing the MCP proxy multiplexer (`mcp-proxy-mux`) — a multiplexing proxy that runs **one** stdio MCP server process per service and exposes each as a shared HTTP endpoint. Instead of every Claude Code agent spawning its own copy of each MCP server, all agents share a single backend process per service.

## Overview

In a fleet of Claude Code agents, naively configured stdio MCP servers multiply fast: 17 agents each spawning their own copy of a server means 17 redundant processes per service. The MCP proxy multiplexer fixes this by running a single backend process per service and fronting it with an HTTP endpoint that all agents connect to.

```
17 Claude Code agents ──POST /mcp──► HTTP Server (:port) ──► 1 stdio process
```

Each proxied server is assigned its own port in the 9100-9105 range. Claude Code connects via an HTTP config entry (`{"type": "http", "url": "http://127.0.0.1:<port>/mcp"}`) rather than spawning a stdio child process.

## Features

- **Shared backends**: One stdio process per service, shared across all agents
- **Per-server HTTP endpoints**: Each proxied server on its own port (9100-9105)
- **Health checks**: `/health` endpoint per server, plus a fleet-wide `--status` view
- **Selective multiplexing**: Only servers that are safe to share are proxied; session-stateful and per-identity servers are intentionally left as-is
- **Config-driven**: Servers defined in a single `config.toml`
- **Boot-time daemon**: Runs as a launchd daemon so it is up before the fleet launches

## When to Use This Skill

Use the mcp-proxy skill when:

- MCP tool calls fail or time out and you need to check whether the proxy is running
- A user asks about MCP proxy status, health, or server processes
- The fleet is launching and MCP servers need to be confirmed running
- A user asks to add or remove a server from the proxy
- You are troubleshooting resource usage or a high MCP process count
- A user says "check mcp servers", "proxy status", or "mcp proxy"

## Prerequisites

- The `mcp-proxy-mux` CLI installed and on `PATH`
- A proxy config file (default location below)
- For inspecting daemon state: `launchctl` (macOS) access for the current user
- `curl` for direct per-server health checks

## Proxied Servers

| Server | Port | Type | Status |
|--------|------|------|--------|
| google-workspace-personal | 9100 | node (GWS personal) | LIVE |
| google-workspace | 9101 | node (GWS org) | LIVE |
| nanobanana-mcp | 9102 | node (image gen) | LIVE |
| brave-search | 9103 | npx (web search) | disabled (no API key) |
| netlify | 9104 | npx (deploy) | LIVE |
| veo-mcp | 9105 | node (video gen) | LIVE |

### Not Proxied (and why)

Some servers should **not** be multiplexed:

- **chrome-devtools, playwright** — hold browser session state; concurrent agents would conflict
- **mattermost-channel** — per-agent identity (each agent uses a unique bot token)
- **mcp-agent-mail, imessage** — already HTTP, so already shared
- **maps-grounding-lite, stripe** — already cloud HTTP endpoints

## Usage

### Core Commands

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

### Health Checks

Each server exposes a `/health` endpoint:

```bash
curl http://127.0.0.1:9102/health
# {"status": "ok", "server": "nanobanana-mcp", "pid": 12345, "sessions": 3}
```

Or check everything at once:

```bash
mcp-proxy-mux --status
```

## Troubleshooting

**MCP tool call fails with a connection error**

```bash
# Is the proxy running?
mcp-proxy-mux --status

# If not, start it
mcp-proxy-mux &
```

**A single server is down but others work**

```bash
# Check that specific server
curl http://127.0.0.1:9103/health

# Restart just that server
mcp-proxy-mux --server brave-search
```

**High memory / CPU from MCP processes**

```bash
# Check whether agents are still spawning their own stdio servers
# (they should not be, if settings.json is updated)
ps aux | grep -E "workspace-server|nanobanana|brave-search" | grep -v grep | wc -l
# Should show 6 (one per proxied server), not 17+
```

## Configuration

The proxy reads its server definitions from:

```
~/Projects/leegonzales/dev-environment/mcp-proxy/config.toml
```

To add a new server, add a `[servers.<name>]` block with `command`, `args`, `port`, and an optional `env`.

### settings.json Mapping

When the proxy is running, Claude Code `settings.json` entries use the HTTP form:

```json
"nanobanana-mcp": {
  "type": "http",
  "url": "http://127.0.0.1:9102/mcp"
}
```

…instead of the old stdio form:

```json
"nanobanana-mcp": {
  "command": "node",
  "args": ["/path/to/nanobanana-mcp/dist/index.js"]
}
```

## Launchd Daemon

The proxy runs as a launchd daemon (`com.mcp-proxy-mux.daemon`) so it starts at boot, before the fleet:

```bash
# Check daemon status
launchctl list | grep mcp-proxy

# Restart daemon
launchctl kickstart -k gui/$(id -u)/com.mcp-proxy-mux.daemon
```

## Relationship to the mcp-proxy-mux CLI

This skill is the operational guide for the `mcp-proxy-mux` CLI. The CLI does the work — starting backends, fronting them with HTTP endpoints, and reporting health. The skill tells Claude *when* to reach for the CLI (failing tool calls, status requests, fleet launch, config changes) and *how* to read its output and act on it, including which servers are safe to multiplex and which must stay per-agent.

## Documentation

- **SKILL.md**: Architecture, commands, proxied-server table, health checks, troubleshooting, config, and launchd management
- **README.md**: This human-facing overview

## Version

Current: v1.0.0

See [CHANGELOG.md](./CHANGELOG.md) for version history.

## License

MIT License — see [LICENSE](./LICENSE) for complete terms.

---

**Version**: 1.0.0
**Last Updated**: 2026-06-20
**Maintained By**: AISkills Collection
