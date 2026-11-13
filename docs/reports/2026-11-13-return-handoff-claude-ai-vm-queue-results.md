# Follow-up to the 2026-11-13 session-close handoff: VM bridge queue results (T1-T3)

Written by the Claude.ai Praxis channel, 2026-11-13 about 14:45 ET. Read with `docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md`; this file replaces its "VM bridge queue" bullet, which said the channel had not seen the results.

Source: the VM Claude Code session's own report, pasted to this channel by Amear at 14:37 ET (REPORTED BY Amear; the channel has not read the VM repo). The VM agent is the session working in `C:\praxis\vm-bridge` on the Windows VM. It is not praxis-master. Its results and commits live in that local git repo (no remote), with result files at `results\T1.json`, `results\T2.json`, `results\T3.json`. They are not in Praxis.build.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## 1. Results (as reported by the VM agent)

Setup: Strategy Analyzer tab "PRAXIS baseline NQCONTROW 0930", PraxisNoiseAreaBreakout, NQCONTROW SEP25, 1-minute, 2021-03-08 to 2026-07-17, CME US Index Futures RTH 0930 ET, commission PRAXIS $2.96 round trip, slippage 2, Standard fill resolution, 1 NQ.

| Run | ExitMode | Trades | Net | Profit factor | Max drawdown | vs T1 reference (Amear's hand run) |
|---|---|---|---|---|---|---|
| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615 | -$38,905.64 | Exact match |
| T2 | OppBand | 1,112 | $188,618.48 | 1.2861 | -$37,906.24 | -61 trades, +$12,225.56 net, DD $999.40 smaller |
| T3 | BandOrVWAP | 1,173 | $176,392.92 | 1.26 | -$38,905.64 | Identical to T1 trade by trade (request id excepted); same file size, 219,831 bytes |

- T1 run time about 19 seconds. `bridge.log` showed `param set: ExitMode="BandOrVWAP"`, `param set: Contracts=1`, `backtest: executing RunCommand`.
- **ExitMode (an enum) is applied by the bridge:** `bridge.log` shows `param set: ExitMode="OppBand"` for T2, and T2's result differs from T1. The open question in the VM handoff ("T2 may equal T1 if the enum is not applied") is closed.
- **The tab state is restorable:** T3 reproduced T1 exactly after T2, so a parameter change is cleanly overwritten. The tab was left at BandOrVWAP, 1 contract.
- **No connection changes during any run:** no connect or disconnect lines in `bridge.log` while T1, T2 or T3 ran.
- **Commission not compared:** the bridge's result files carry no commission total, so the hand run's $3,472.08 could not be checked.

## 2. What went differently from the plan (REPORTED BY the VM agent)

1. **First T1 attempt stopped, nothing ran:** NT8 had no Strategy Analyzer window open. Amear opened the tab by hand; the VM agent treated his explicit go as a new T1 run, not a retry, logged his words, and re-ran the pre-send checks.
2. **NT8 restarted at 12:32:48 PM** (new process, PID 11820), between the two T1 attempts. Its startup reloaded the AddOn and connected the Sim feed (six new `bridge.log` lines), before any request was sent. The VM agent judged this normal startup, not a bridge action and not a breach of the "no connection lines during a run" rule, and logged it. **Who or what restarted NT8 is not stated in the report** (open).
3. **`run-queue.ps1` was not used:** it needs the `claude` command, which is not installed on the VM. The VM agent ran the three tasks itself, one at a time, as the script's own fallback allows.
4. **`tools\send-backtest.ps1` was changed:** extended so it can pass strategy parameters. It worked for all three runs.
5. Timestamps are consistent with the VM clock now being correct: bridge.log 17:36:47 UTC for the T1 send, against Amear's report of a correct taskbar clock at about 12:27 ET (INFERRED by the channel).

## 3. What this means (the channel's reading, INFERRED, not a ruling)

- **The bridge works for headless backtests:** it reproduces a hand run exactly, applies parameters including enums, and leaves the tab restorable. That is the infrastructure result of the day. Walk-forward still needs the optimizer command, which is not allowed yet.
- **These are Noise-Area numbers, kept for the record only** (D7 after the D6 drawdown check). T2's better net does not change that: at 1 MNQ its max drawdown would be about $3,790 (one tenth of $37,906.24), above the 50K gate of $1,600. Not a candidate.

## 4. What's left (from the VM agent, with channel notes)

1. **MFFU commission re-run:** Amear sets both PRAXIS commission rows to 2.34 by hand ($4.68 round trip); the VM agent then re-sends T1's parameters. Expected: 1,173 trades, net about $174,375.36 (channel check: 1,173 x $1.72 extra per round trip = $2,017.56 less than $176,392.92, which matches).
2. **Sim feed check:** the VM agent still lists "check in the Control Center whether the Sim feed cycled when the AddOn loaded yesterday." Amear reported today (voice, about 12:30 ET) that he looked and saw no disconnect or reconnect. Whether today's Control Center view covers yesterday's load is not confirmed.
3. **Later, not today:** Analyzer tabs for `PraxisNoiseAreaBreakout_Flat1559` and `PraxisLastHalfHourMomentum`, set by hand or via the bridge's `satemplate` command (needs Amear's OK). Channel note: `PraxisLastHalfHourMomentum` is retired (D-2026-11-02-A; session-close handoff section 2), so its tab is not needed unless Amear says otherwise.
4. **Open:** what restarted NT8 at 12:32 PM.

