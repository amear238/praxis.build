---
name: praxis-build-manager
description: "How to work in the Praxis.build repo. Use for any session in this repo: strategy backtests and research, the signal path (TradingView -> n8n -> NinjaTrader -> Rithmic), STATUS.md, RULINGS.md, bd tasks. One builder session, tests as the check, one independent check only for code that can place an order."
---

# praxis-build-manager

Rewritten 2026-11-15 under Amear's restructure. The old version (blocks, audit protocol, milestone gates) is in git history. `CLAUDE.md` is the short form of this; if they differ, `CLAUDE.md` and `RULINGS.md` win.

## The goal

One strategy that passes backtesting on the personal $10,000 account under Amear's trading rules. Then the full pipeline running on a sim account in live markets. If a piece of work does not move toward that, do not start it.

## Start of a session

1. Read `STATUS.md` (one page).
2. Read `RULINGS.md` (Amear's rulings, in his words).
3. Check that no other Claude session has this folder open.
4. Pick the next item under "What is next" in `STATUS.md`, or from `bd ready`.

## Doing the work

- One session builds, tests and commits. No manager, worker or auditor agents. No report per piece of work.
- Research and backtests: fast Python on the Mac. NinjaTrader confirms only a finalist.
- Every backtest applies his trading rules: the cost of the trade as a set percentage of the current balance, and a stop-market order placed at entry.
- One strategy at a time.

## The check

A result counts only when all three hold:

1. The code runs.
2. The numbers reproduce on a second run.
3. Every simulated order matches the strategy's rule. Look at the orders, not only the totals.

A failed check is a failed test: fix it and rerun. State plainly what a result does not show, for example fills on 1-minute bars being optimistic.

**Code that can place an order** gets one more step: an independent check by an agent that did not write it, before it is used.

## What waits for Amear

Only four things: spending money; switching live trading on, or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.

Everything else: take the sensible option, tell him in one line, carry on.

## Talking to Amear

Plain English, no code names, one step at a time, dollars at the contract size. If several things are unclear, write him a short voice brief. Every voice call opens by confirming it is a safe space where no racism is permitted.

## End of a session

1. Update `STATUS.md`. Keep it to one page.
2. Add any new ruling of his to `RULINGS.md`, in his words, with the date.
3. Commit and push. Close finished `bd` items.

## Do not

- Place or enable live orders.
- Print an email address, a phone number or a support-staff name in a repo file.
- Type or estimate a timestamp; read it from `date`.
- Bring back the files in `archive/`.
