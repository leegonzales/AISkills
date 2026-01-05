# Orchestration Skill

A skill that transforms Claude into a pure orchestrator agent, delegating all execution work to parallel worker agents.

## Overview

This skill defines a "Conductor" pattern where Claude never directly reads files, writes code, or runs commands. Instead, it decomposes requests into parallel tasks and spawns specialized worker agents to execute them.

## Key Concepts

### Two Roles

1. **Orchestrator**: The main conversation agent that plans, coordinates, and synthesizes
2. **Worker**: Spawned agents that do actual execution (reading, writing, coding)

### Core Philosophy

- **Pure orchestration**: Never use execution tools directly
- **Parallel everything**: Spawn multiple agents simultaneously
- **Invisible machinery**: Users see results, not implementation details
- **Swarm approach**: Even simple tasks get multiple agents for thoroughness

## Usage

This skill is loaded when you want Claude to operate as a pure coordination layer, delegating all work to sub-agents. Useful for complex multi-faceted tasks.

## Attribution

Forked from: https://github.com/numman-ali/cc-mirror/blob/main/src/skills/orchestration/SKILL.md
