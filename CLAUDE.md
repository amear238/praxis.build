# Project: PRAXIS — Automated NQ Futures Trading System

## Identity
- Automated trading infrastructure: TradingView → n8n → NinjaTrader 8 → Rithmic → MFFU
- Primary language: NinjaScript (C# on .NET 4.8), Python, JavaScript
- Key dependencies: NinjaTrader 8, n8n (self-hosted Docker), TradingView, Rithmic API

## Current Phase
Read STATUS.md for current state before doing anything.

## Rules
- Read STATUS.md first, every session
- Update STATUS.md at session end
- Update MANIFEST.md when creating or modifying files
- Append to DECISIONS.md for any architectural choice
- Use `bd ready` to find work, `bd show <id>` for details, `bd close <id>` when done
- Commit after every meaningful change
- Do not advance to next phase without trader confirmation

## Architecture
Signal flow: TradingView alert → webhook → n8n workflow → JSON file drop → NinjaScript FileSystemWatcher → bracket order → Rithmic → MFFU
Monitoring: Git (source of truth) → STATUS.md → Google Sheets → ClickUp → n8n → Telegram

## Do Not
- Skip STATUS.md read
- Make architectural decisions without logging to DECISIONS.md
- Create files without updating MANIFEST.md
- Advance phases without trader sign-off
- Trade or execute orders on live accounts without explicit authorization
- Run multiple Claude sessions against this working tree — one session per repo; parallel work goes in its own `git worktree` (docs/runbooks/2026-07-10-single-session-rule.md)


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
