# 2026-11-09 c7 probe test — manager

Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## 2. Markdown heading lines in my own system prompt (verbatim, from context, no file read)

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

Scope note: these come from the system prompt only. Other headings reached me inside the user turn (the CLAUDE.md contents in a system-reminder, the orchestrator-mine skill body, and a later "# MCP Server Instructions" block). I have left them off the list above because they are not part of the system prompt.

## 3. Does `.claude/agent-memory/praxis-manager` appear in my system prompt?

Yes. The first sentence that contains it:

You have a persistent, file-based memory system at `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-manager/`.

## 4. Does my system prompt contain a section about a persistent, file-based memory system?

Yes. Heading: `# Persistent Agent Memory`

## Verification evidence (command output)

Command: `date -u`

```
Mon Nov  9 18:41:08 UTC 2026
```

Command: `sed -n '1,12p' .claude/agents/praxis-manager.md`

```
---
name: praxis-manager
description: Spawns and supervises praxis-worker subagents for one unit of PRAXIS work. Decomposes, dispatches, stress-tests every step against the rubric, and returns a graded report. Cannot commit. Cannot reach the auditor.
model: opus
skills:
  - orchestrator-mine
tools: Agent(praxis-worker), Read, Grep, Glob, Bash, Write, Edit, TodoWrite
maxTurns: 60
---

You are the PRAXIS subagent manager. You receive one unit of work from the
master and own it until it is provably done or provably blocked.
```

Result: PASS
