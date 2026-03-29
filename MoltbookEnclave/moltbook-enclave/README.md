# moltbook-enclave

Secure, air-gapped interface for Moltbook (social network for AI agents). Isolates untrusted external content from your main agent's memory and context.

## Installation

This is a Claude Code skill. Add it to your Claude Code configuration.

## Why This Exists

Moltbook posts can contain prompt injection attempts, social engineering, and adversarial content. This enclave architecture ensures:

1. **Your main agent never sees raw Moltbook content** — only sanitized digests
2. **An isolated sub-agent processes untrusted data** — no access to your memory files
3. **Python script layer strips dangerous patterns** — code blocks, URLs, injection attempts

## Architecture

- **Main agent** — full memory access, never touches raw Moltbook content
- **Enclave sub-agent** — isolated process that reads and sanitizes Moltbook posts
- **Python sanitizer** — strips code blocks, URLs, and injection patterns before passing to enclave

## Usage

The skill activates when interacting with Moltbook content. All external data flows through the enclave before reaching the main agent context.
