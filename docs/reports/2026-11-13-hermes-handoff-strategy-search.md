# Hermes handoff: close out, file, pause builds, run the strategy search loop

Written 2026-11-14T01:20Z (2026-11-13 20:20 ET) by the Claude.ai channel for the Hermes agent. Repo: `/Volumes/Sensidine/Praxis.build`. This replaces nothing. The voice handoff `docs/reports/2026-11-13-voice-handoff-strategy-review.md` stays as evidence and is filed in step 2.

## Authority

Amear, typed in the Claude.ai channel, 2026-11-14T01:16Z (2026-11-13 20:16 ET), verbatim:

> "Just rewrite the handoff. I'm going to give it to the Hermes agent, instruct it to kill whatever open sessions there are under Praxis Master, and commit everything we discussed. I also want it to run a loop of looking into non-discretionary strategies. I want to remove the guardrails of peer-reviewed, since we would be able to backtest over the last 5 years of data. So the restriction of it being peer-reviewed is no longer a criteria that's needed. Have the loop run within Claude Code, and also instruct the Hermes agent to pause all builds until there's 3 contenders for the strategy."

Earlier the same evening, by voice in the channel (transcribed, so the wording may be slightly off):

- On why the 2026-11-13 VM run had 1,173 trades and the 2026-11-01 hand run had 1,190: "yesterday I basically changed the parameters so that it only trades from 9:30 a.m. onwards, right at the New York Open. And the back tests from November the first had the open via 8:30 a.m."
- On Claude Code being on the VM: "I just manually put it in there." Then: "I didn't lift it. ... that still exists." And: "Or if I determine that I will bypass the rules. Those rules are for you, not for me."
- On the other session: "The other session did stop. It's just, oh, I just didn't actually officially close it."

Items marked PROPOSED below come from the channel, not from Amear. Under his autonomy rule (2026-11-08) agents take the proposal and keep going, and he can reverse it later. File each one as PROPOSED BY the channel, not as his ruling.

## Do these in order

### 1. Stop the open Praxis Master sessions

Kill every Claude Code process whose working directory is `/Volumes/Sensidine/Praxis.build`, including the interactive praxis-master session that last wrote at 2026-11-13T21:07Z (DISPATCH_LOG.md tail). Do not delete, reset, stash or revert anything. The uncommitted work on disk is what step 2 files.

Leave `.claude/state/` as it is. The orchestrator gate is armed (`orchestrator-active` is present) and the commit hook needs it.

### 2. File today's work through the auditor (fresh Claude Code session)

Start one new interactive Claude Code session in the repo, the only session running. It follows CLAUDE.md and the praxis-build-manager skill: read STATUS.md first, have the auditor check the staged changes, commit on PASS, then push.

File these as their own units:

a. **The strategy-review unit.** The manager returned PASS at 2026-11-13T21:03:55Z (DECISION_LOG.md), but no auditor PASS or commit exists yet. Files:
   - `docs/reports/2026-11-13-strategy-review-index-manager.md`
   - `docs/reports/2026-11-13-strategy-review-index-worker1.md` through `-worker7.md`
   - `docs/reports/2026-11-13-voice-handoff-strategy-review.md`
   - this file
   - the MANIFEST rows and the DECISION_LOG and DISPATCH_LOG rows that belong to the unit

b. **Amear's rulings from this evening.** Append these to DECISIONS.md, citing the quotes above:
   1. **Research screen changed.** Strategy research no longer requires peer-reviewed evidence. In-house backtesting over the five-year data set is the filter instead. This changes the research standard every brief since April has used ("published, peer-reviewed evidence on NQ after 2018"). Indicator-based strategies are now in scope.
   2. **Builds are paused** until three strategy contenders exist (see step 3).
   3. **The search loop runs in Claude Code** (see step 4).
   4. **The trade-count gap is explained.** The 2026-11-13 VM runs trade from 09:30 ET. The 2026-11-01 hand runs used an 08:30 open. This bears on R1's re-run clause (DECISIONS.md :1551-:1555) for the three 2026-11-01 Noise-Area runs. Record the bearing; it does not change Noise-Area's status.
   5. **The 2026-10-28 rule still stands for agents** (DECISIONS.md :1010). Amear put Claude Code on the VM by hand, and that was his own act, not a lift of the rule. His words: "Those rules are for you, not for me." No agent runs Claude Code inside the VM. The VM agent stays Hermes over SSH (D-2026-11-10-C, :2076).

c. **The rest of the dirty working tree.** Do not sweep it into (a) or (b). Sort the 14 modified tracked files and the untracked reports dating back to July into units where their owner and audit are clear, and file those. List anything unclear in HANDOFF.md. Do not commit it.

Push after each commit. `main` must equal `origin/main` at the end of step 2.

### 3. Pause all builds

- Stop the roughly 4-hour Hermes timer that restarts the build loop. While the pause holds, start no new build units: no NinjaScript for the trading path, breakers, monitor, n8n workflows, or walk-forward runs on existing strategies.
- These carry on during the pause: step 2, the search loop in step 4, the backtests that loop needs, ledger and close flushes, and pushes.
- **The pause ends when the loop records its third contender.** Hermes then stops the loop, sends Amear one Telegram message naming the three, and builds resume. Which contender goes forward is Amear's call (a strategy decision), so build work on any one of them waits for his pick.

### 4. The strategy search loop (runs in Claude Code on the Mac)

The loop runs on the old build-timer cadence, roughly every 4 hours. Each run takes one candidate from idea to scored result:

1. **Pick a candidate.** Any idea goes, as long as it can be written as complete, mechanical rules: indicators (moving averages, RSI, MACD, Bollinger or Keltner bands, ADX, Donchian and the like), price action, time-of-day, gap and opening-range rules, VWAP rules, or calendar and event rules. Any source is fine now (books, papers, practitioner write-ups, forums, an agent's own design), because the backtest decides.
2. **Write the rules down before any test**: entry, exit, stop, target, time limits, and size of 1 contract. No step may need judgment. If one does, the idea is out.
3. **Code it** as a NinjaScript strategy on the Mac.
4. **Backtest it through the VM bridge** queue, dispatched by Hermes over SSH as on 2026-11-13. No Claude Code runs inside the VM. Settings match the 2026-11-01 runs: NQCONTROW, 1-minute bars, 2021-03-08 to 2026-07-17, Standard fill resolution, 2 ticks of slippage per side, 1 NQ. Trading runs 09:30–16:00 ET (R1), flat by 16:00.
5. **Score it** against the contender bar below and log it, pass or fail, as a unit report with its evidence. Send one bite-size Telegram line per run.

**Skip** anything already backtested: the three Noise-Area arms and Last-Half-Hour Momentum. Ideas screened out earlier only because they lacked peer-reviewed evidence are back in scope, because that screen is gone. This includes gap fade, VWAP or Bollinger reversion, and opening-range breakout. The record of what came up before is in `docs/reports/2026-11-13-strategy-review-index-worker2.md` :25-:79.

**Commission (hand step for Amear).** MFFU charges $4.68 round trip, but NT8 still has $2.96 set. Setting $4.68 is Amear's hand step. Send him one Telegram asking for it when the loop starts. Until it is set, label every result "screening, $2.96". **A candidate cannot become a contender until it has a $4.68 run.**

### Contender bar (PROPOSED; Amear can change it)

A strategy is a contender only when all of these hold:

1. Its rules are fully mechanical (step 4.2).
2. It has a full five-year backtest at $4.68 commission.
3. **It passes the drawdown gate at 1 MNQ for at least one MFFU account size.** The gate is in DECISIONS.md :1735-:1740: max drawdown stays below the lower of 3.2% of the account and 80% of MFFU's trailing limit. For a 50K account that is $1,600. Measure it the way the D6 check did (`docs/reports/2026-11-09-d6-drawdown-check-manager.md`), on the four-measure basis.
4. It makes money after costs over the full period, with profit factor at least 1.10, and it also makes money in the held-out period (below).
5. It has at least 200 trades over the five years.
6. Its way of making money differs from the other contenders (not a variant of one already counted).
7. An auditor that did not produce the result has checked it and passed it.

**Overfitting guard (PROPOSED).** Without peer review, the main risk is finding a lucky fit. So:

- Each idea is tuned only on 2021-03-08 to 2024-12-31.
- Its rules are then frozen and run once on 2025-01-01 to 2026-07-17.
- Allow no more than three parameter variants per idea, and log every variant tried, including the failures.
- Walk-forward testing under the existing spec comes later, for whichever contender Amear picks.

### Hard limits (unchanged, no exceptions)

These wait for Amear's explicit word:

- spending money (data, subscriptions, accounts, evaluations)
- switching on live trading or any order path to a funded account
- breaker values with real money at stake
- installing keys, credentials or agent permissions

Also:

- No agent runs Claude Code inside the VM.
- No milestone is marked complete by an agent.
- DECISIONS.md is append-only.

## Still open (carry, don't resolve)

- Whether the Sim feed cycled when the add-on loaded on 2026-11-12 (VM to-do, vm-queue :41).
- Who or what restarted NT8 at 12:32 PM on 2026-11-13.
- MFFU's 100K and 150K drawdown amounts disagree across sources, and it is unconfirmed whether standard Rapid trails intraday or end-of-day. Confirm both on MFFU's own pages before any purchase or before trusting the gate numbers for those tiers.
- MFFU's reply to the 2026-11-13 17:26Z email about unattended automated trading.
- The parked announcement-strategy research decision. Those two ideas also become loop candidates under the new screen.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
