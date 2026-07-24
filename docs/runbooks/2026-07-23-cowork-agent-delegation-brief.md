# Cowork Agent — Delegation Brief & Capability Reference

**Source:** provided verbatim by Amear, 2026-07-23 (session 24). Save into
agent-automation / delegation-planning context.
**Also in bd memory:** key `cowork-agent-delegation` (search `bd memories cowork`).

This describes **the other agent in the PRAXIS workflow** — the one running in
**Cowork mode** on Amear's Windows desktop (the machine that hosts the NinjaTrader 8
VM). Read it before delegating any VM-side task so work routes to the right place and
nobody assumes capabilities that aren't there.

---

## Why this matters for PRAXIS (delegation implications — read first)

1. **The "coworker" / VM operator IS this Cowork agent, not a human.** Every "VM hands"
   task in the signal path (compile `PraxisNoiseAreaBreakout.cs`, import CSV, run
   Strategy Analyzer, reconcile, hash-verify) is delegated to Claude-in-Cowork on the
   Windows machine. Briefs must be written *for an agent* and self-contained.

2. **AUDIT-INTEGRITY FIX — verification must be self-computed, never pasted.** Per the
   Cowork agent's own report, the session-23 CRLF hash was *pasted to it twice* (once as
   "proof," once as "independently re-verified by an auditor") and **it did not compute
   the hash itself** — it proceeded on the pasted numbers at the trader's choice. So our
   "independent" PASS was grading a pasted assertion, not a fresh computation. **Going
   forward: the agent with hands on the machine RECOMPUTES the hash/checksum directly
   before any compile/deploy step** — especially for a strategy that will eventually
   route real orders. Do not let a "trust me, already verified" claim be the input to an
   automated deploy. (See [[vm-cs-crlf-hash-gate]] for the CRLF gotcha itself.)

3. **Real Windows paths only.** The Cowork agent's `mcp__workspace__bash` is an
   **isolated Linux sandbox** that does NOT touch the Windows filesystem. Delegated tasks
   must use real Windows paths (`C:\Users\...`, `C:\Mac\Home\praxis-signals\...`,
   `%USERPROFILE%\Documents\NinjaTrader 8\...`) — a sandbox path (`/mnt/...`, `/home/...`)
   will not reach NT8.

4. **Sim/backtest only — the hard limit is absolute.** The agent will inspect/edit/
   compile strategy code, run Strategy-Analyzer backtests, hash-verify, and reconcile
   data — all non-live. It will **not** place a live order, enable auto-trade on a live
   or sim-*funded* account, or move money. Any "go live" step is Amear's alone. Every
   PRAXIS block ≤4 is inside its envelope; Block 5 graduation execution is not.

5. **No session memory — restate context every time.** A fresh Cowork session knows
   nothing of prior ones. Each delegated brief must restate: real Windows paths, what's
   already verified, and which checklist step we're on. (This is why the 4uu brief is
   fully self-contained.)

6. **No web-fetch workarounds.** If `web_fetch`/`WebSearch` says a domain is blocked,
   that's a hard stop — do not ask it to reroute via curl/requests. Don't design tasks
   that depend on such a workaround.

---

## Verbatim brief (as provided)

### Who I am
I'm Claude, running in **Cowork mode**, a feature of the Claude desktop app (research
preview). Built on Claude Code / Claude Agent SDK infrastructure, but **not** Claude Code
— different product, session model, and tool surface. Each Cowork session is independent;
no memory between sessions except through files/artifacts explicitly saved somewhere
persistent (a connected folder, ClickUp, Drive, etc.). Anything meant to survive has to
be written down. In this session a "Praxis" persona (trading-discipline coach voice) is
loaded as a prompt overlay — not a platform capability.

### What I can actually do
- **File and code work.** Read/Write/Edit on a working directory + any connected folder.
  Separately, `mcp__workspace__bash` runs shell in an **isolated Linux sandbox** (NOT the
  Windows machine; paths don't overlap).
- **Windows desktop control** (two toolsets on the real machine):
  - `mcp__computer-use__*` — screenshot-driven mouse/keyboard, gated per-app via
    `request_access`, tiered: **browsers = read tier** (click/type blocked → hand off to
    Chrome MCP); **terminals/IDEs = click tier** (can click, cannot type); **everything
    else = full tier** (unrestricted — NT8's native GUI is full tier).
  - `mcp__Windows-MCP__*` and `mcp__Desktop_Commander__*` — direct Windows automation:
    PowerShell, filesystem read/write, process management, registry, clipboard, app launch.
  - Both exist in-session, but which is live/authorized varies — check, don't assume.
- **Browser.** `mcp__claude-in-chrome__*` for DOM-aware nav / reading / forms; used
  instead of computer-use for web apps and required for actually opening links.
- **Connectors (live once authorized):** Gmail, Google Calendar, Google Drive, ClickUp,
  Spotify, Zapier (→ 9,000+ apps). **Pending user auth (not usable yet):** Asana,
  Atlassian, Linear, Monday, MS365, Notion, Slack.
- **Skills.** Document generation (docx/pdf/pptx/xlsx), scheduled/recurring tasks, deep
  research, and account skills (`adhd-coach`, `addiction-agent`, `productivity` suite,
  skill-creator, setup-cowork, plugin tooling). Can invoke; cannot create/edit a skill's
  saved definition from inside a session.
- **Scheduled tasks & artifacts.** `mcp__scheduled-tasks__*` for recurring/delayed
  automations; `mcp__cowork__create_artifact` for persistent live-data HTML pages.

### Hard limits — do not delegate around these
- **No trade execution, no money movement.** Inspect/edit/compile strategy code, run
  Strategy Analyzer backtests, verify hashes, reconcile history — all non-live. Will NOT
  place a live order, enable auto-trade on a live/sim-funded account, or initiate a
  trade/transfer. "Go live" is always the user's.
- **No independent verification without doing it itself.** Prefer recomputing the
  hash/checksum directly over accepting a pasted "already verified" assertion — especially
  before a compile/deploy that touches an order-routing strategy. (See implication #2.)
- **No web-fetch workarounds.** Blocked/unfetchable domain = hard stop, not a puzzle to
  route around via curl/requests/etc.
- **Session boundaries.** No reach-back into a prior Cowork session; a fresh session has
  no memory unless re-given the context. Restate file paths, what's verified, and which
  checklist step we're on.

### Practical guidance for delegating to me
- Use **real Windows paths** (`C:\Users\...`), not sandbox paths — different filesystems;
  I'll flag a mismatch.
- Say explicitly whether a task stays in **backtest/sim** (safe) or touches **live** (I'll
  decline the execution step and ask the human).
- NinjaTrader specifically: **compiling, backtesting, code review = fair game**;
  connecting to a live/funded account or flipping on auto-trade = not on anyone's behalf.
