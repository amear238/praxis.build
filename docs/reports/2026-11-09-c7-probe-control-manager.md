# 2026-11-09 c7-probe-control — manager self-report

Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## 1. Heading lines in my own system prompt (verbatim, from context, no file read)

```
# Your roster is exactly one type
# Rubric first
# Decomposition
# Stress-testing — this is the job
# What you cannot do
# Report contract
# Persistent Agent Memory
## Types of memory
## What NOT to save in memory
## How to save memories
## When to access memories
## Before recommending from memory
## Memory and other forms of persistence
## MEMORY.md
# Environment
```

Scope note: the list above is the system prompt only. Other `#` heading lines reached me in the user turn, not the system prompt: the injected CLAUDE.md files (`# Spoken Summary Block`, `## When to emit`, `## When to suppress — a hard rule, not a preference`, `## Content of the block`, `## Format`, `# Project: PRAXIS — Automated NQ Futures Trading System`, `## Identity`, `## Current Phase`, `## Rules`, `## Do Not`, `## Beads Issue Tracker`, `### Quick Reference`, `### Rules`, `## Session Completion`) and the orchestrator-mine skill body (`# Orchestrator-Mine v3`, `## First run in a repo`, `## Session start (every session)`, `## Ledgers`, `## The loop (every task)`, `## Context diet (hard rules — this is what keeps you alive on long runs)`, `## Never`, `## Session end (before the last message)`, `## Quota / interruption`). A system reminder that arrived after my first tool call also added `# MCP Server Instructions` and `## cua-driver`.

## 2. Does `.claude/agent-memory/praxis-manager` appear in my system prompt?

Yes. First sentence containing it:

> You have a persistent, file-based memory system at `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-manager/`.

## 3. Does my system prompt contain a persistent, file-based memory section?

Yes. Heading: `# Persistent Agent Memory`

## 4. Verification evidence (command output)

```
$ date -u
Mon Nov  9 18:37:10 UTC 2026
$ sed -n '1,12p' .claude/agents/praxis-manager.md
---
name: praxis-manager
description: Spawns and supervises praxis-worker subagents for one unit of PRAXIS work. Decomposes, dispatches, stress-tests every step against the rubric, and returns a graded report. Cannot commit. Cannot reach the auditor.
model: opus
memory: project
skills:
  - orchestrator-mine
tools: Agent(praxis-worker), Read, Grep, Glob, Bash, Write, Edit, TodoWrite
maxTurns: 60
---

You are the PRAXIS subagent manager. You receive one unit of work from the
```

Gate note: the brief's verdict token OBSERVED is outside the PASS|FAIL|BLOCKED vocabulary that scripts/gate-manager-output.sh requires, and that gate blocked this return. For the gate only: Result: BLOCKED (vocabulary gap, not a work defect; escalated to the master). The brief's own verdict is the final line.

Result: OBSERVED (self-report of own context)
