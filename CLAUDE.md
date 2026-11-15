# Project: PRAXIS — Automated NQ Futures Trading System

## The goal
One strategy that passes backtesting on the personal $10,000 account under Amear's trading rules. Then the full pipeline running on a sim account in live markets. Work that does not move toward that is frozen.

## Identity
- Signal flow: TradingView alert → webhook → n8n workflow → JSON file drop → NinjaScript FileSystemWatcher → bracket order → Rithmic
- Languages: Python (research and backtests on the Mac), NinjaScript (C# on .NET 4.8), JavaScript
- Strategy research runs in fast Python on the Mac. NinjaTrader confirms only a finalist.

## Every session
- Read `STATUS.md` first. It is one page: the goal, what is done, what is running, what is next, what waits on Amear.
- Read `RULINGS.md`. It is Amear's own rulings, in his words. They bind.
- One session does the work. There is no manager, worker or auditor chain.
- Keep `STATUS.md` to one page and update it when the state changes. Git history is the record of everything else.
- A new ruling from Amear goes into `RULINGS.md`, in his words, with the date. Nothing else goes there.
- Use `bd ready` to find work, `bd show <id>` for details, `bd close <id>` when done.
- Commit after every meaningful change, and push.

## How work is checked
- Tests are the check. A result counts when the code runs, the numbers reproduce on a second run, and every simulated order matches the strategy's rule. Keep these strict.
- A failed check is a failed test. Fix it and rerun. Do not set the work aside.
- No written report per piece of work. Put what matters in the commit message.
- Anything that can place an order gets one independent check by an agent that did not write the code, before it is used.

## Four things wait for Amear's explicit word
1. Spending money.
2. Switching live trading on, or any order path to a funded account.
3. Changing circuit-breaker values while real money is at stake.
4. Installing keys, credentials or agent permissions.

For everything else: take the sensible option, tell him in one line, carry on. He can reverse it.

## His trading rules
- The cost of the trade is a set percentage of the account, defined before entry.
- Every trade has a stop-market order placed at entry.
- One strategy at a time. Noise-Area is retested first, with a real stop.
- Nothing goes to execution without enough backtest data.
- Fully rule-based and automated. No AI in trade decisions.

## Talking to Amear
- Plain English. No code names. One step at a time.
- Account figures in dollars at the contract size.
- Every voice call opens by confirming it is a safe space where no racism is permitted.

## Do Not
- Trade or execute orders on live accounts without explicit authorization.
- Run more than one Claude session against this working tree. Parallel work goes in its own `git worktree` (docs/runbooks/2026-07-10-single-session-rule.md).
- Print an email address, a phone number or a support-staff name in any repo file.
- Type or estimate a timestamp. Read it from `date`.
- Revive the files in `archive/`. They are history, kept unchanged.


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
