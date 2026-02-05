#!/bin/bash
# MoltBot Enclave Runner
# This script orchestrates the secure Moltbook check:
# 1. Fetch and sanitize feed (Python - no LLM)
# 2. Process outbox if any posts queued
# 3. Signal to cron job that fetch is complete

set -e

MOLTBOOK_DIR="$HOME/.moltbook"
ENCLAVE_DIR="$MOLTBOOK_DIR/enclave"

cd "$ENCLAVE_DIR"

echo "[$(date -Iseconds)] Starting enclave run..."

# Fetch and sanitize feed
python3 moltbot.py fetch

# Post anything in outbox
python3 moltbot.py post

echo "[$(date -Iseconds)] Enclave run complete."
