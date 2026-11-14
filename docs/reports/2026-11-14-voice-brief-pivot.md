# Voice brief: does PRAXIS need a restructure before more building? (2026-11-14)

Written by praxis-master on 2026-11-14, about 9:50 AM ET, for the voice-chat agent. It replaces the overnight-updates brief for this conversation. That brief is still on disk at `docs/reports/2026-11-14-voice-brief-overnight.md` but is not needed.

## What Amear wants to discuss

His words, typed this session: "It seems that there is no strategy that would be compatible for this infrastructure and the noise area breakout being that it's averaging a less than modest profit makes me think that a major restructuring is in order at this point before any future building occurs if I'm wrong you can let me know, but that's how I see it at this point in time".

## How to run it

- Plain English. Give dollar figures and always name the contract size. One MNQ is a tenth of one NQ.
- Label every figure: Amear's hand run, a Mac recomputation, or the master's arithmetic (INFERRED).
- You do not decide anything. Write down Amear's rulings verbatim, with the time, in one new file: `docs/reports/2026-11-14-voice-notes-pivot.md`. Edit no other repo file.
- Four things always wait for his explicit word: spending money; switching on live trading or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.

## The master's view: he is right that a rethink is due, but the diagnosis needs one correction

**Where he is right.**
1. Nothing has passed so far. Five strategies have recorded results: three Noise-Area arms, Last-Half-Hour Momentum, and this morning's gap fade. The contender count is 0 of 3.
2. At the size MFFU allows, Noise-Area's profit is small. At 1 NQ it made $197,328 over 2021-03-08 to 2026-07-17, with a profit factor of 1.29. That was Amear's hand run at $2.96 commission (`docs/reports/2026-11-13-voice-handoff-strategy-review.md` :34). At 1 MNQ, the master estimates roughly $17,800 over 5.4 years, about $3,300 a year. That estimate is INFERRED: the gross profit is divided by ten, then MNQ costs are taken off ($1.90 commission plus 4 ticks of slippage at $0.50, per trade). It is not a run.
3. Building more trading-path code before a strategy exists would be waste. Builds are already paused under D-2026-11-13-D, so the record agrees with him on this point.

**Where the master thinks he is wrong, or the evidence does not reach.**
1. **The infrastructure is not what's failing; the account rules are.** The signal path (TradingView, n8n, NinjaTrader, Rithmic) has never rejected a strategy. Every strategy failed on MFFU's drawdown limit. Noise-Area's worst losing stretch at 1 MNQ was $2,774 to $2,914 inside one window, and $4,463 to $5,280 on the project's committed measure. The project's ceiling for a 50K account is $1,600, and the 150K ceiling is $3,600 (`docs/reports/2026-11-09-d6-drawdown-check-manager.md` :7, :31, :34). So the edge exists, but its swings are about two to three times too large for the prop account. That is a mismatch between the strategy and the account, not a pipeline problem.
2. **"No strategy is compatible" has not been shown.** Only one candidate has gone through the search loop. Indicator-based strategies have never been tested (strategy-review handoff :56). The record shows that the swing-trading intraday NQ ideas tried so far are too volatile for small prop accounts. It does not show that nothing fits.
3. **There is real friction, but it's in the research setup, not the trading path.**
   - A new strategy cannot be backtested from the Mac. It has to be compiled in NinjaTrader on the VM, with an Analyzer tab set up by hand (decision log 2026-11-14T13:04:00Z).
   - The process overhead is heavy. Overnight, all four commits were paperwork. This morning's single strategy test was parked for report-format reasons, even though both auditors confirmed its numbers.

## Restructure options to put to him (his choice; none of them decided)

A. **Change the account, keep the edge.** Options are a larger MFFU tier, an end-of-day trailing plan instead of an intraday one, a different prop firm with looser drawdown, or a personal cash account. Anything that costs money waits for his word. Note that the $3,600 figure at 150K is the project's own 80% safety buffer. MFFU's own limit there would be about $4,500 (INFERRED from the A4 formula; check MFFU's pages before any purchase, since sources disagree, strategy-review handoff :91).
B. **Change what the search looks for.** Make "fits a $1,600 drawdown at 1 MNQ" the first filter, ahead of profit. That points to tighter stops, shorter holds, and a daily loss cap. No daily-loss breaker value has ever been set (D6 report :39), and a cap could cut the drawdown of the strategies already tested.
C. **Change the lab.** Screen candidates quickly in Python on the Mac, and keep NinjaTrader only for confirming finalists. A draft rule for this exists (D-2026-11-14-A) but only on the parked branch. Amear has not ruled on it.
D. **Change the process.** Keep the full audit gates for anything that can place an order. Use a lighter evidence standard for research screens, so a failed idea costs minutes, not a parked branch.
E. **Settle the MFFU question first.** F4 is still frozen: MFFU has not confirmed in writing that unattended automated trading is allowed. A follow-up email went out 2026-11-13 and has had no reply on record. If the answer is no, the whole target account changes, and options A to D should wait for it.

## One thing with a clock on it

The Hermes job `praxis-search-loop` is enabled and next runs at 12:00 PM ET today (`~/.hermes/cron/jobs.json`, read this session). If Amear wants the loop held while he decides the restructure, write that down verbatim, and say it needs a Code session or Hermes to act on before noon.

## Where to read more

- `docs/reports/2026-11-13-voice-handoff-strategy-review.md`: every tested result and the research history.
- `docs/reports/2026-11-09-d6-drawdown-check-manager.md` :7-:45: the drawdown check by account size.
- DECISIONS.md, D-2026-11-13-D and D-2026-11-13-E (from about :2459): the build pause, the contender bar and the overfitting guard.
- HANDOFF.md, top card: this morning's gap-fade result and the parked branch.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
