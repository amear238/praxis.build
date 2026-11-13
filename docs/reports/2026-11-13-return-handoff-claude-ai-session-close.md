# Return handoff: Claude.ai Praxis channel to praxis-master, 2026-11-13 session close: research outcome, correction, and today's updates

Written by the Claude.ai Praxis channel, 2026-11-13 about 14:45 ET. File it as written unless a de-identification check fails. Everything attributed to Amear is REPORTED BY this channel. Read this AFTER the two earlier files from today; where they disagree, this file governs.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## 1. Amear's instruction (REPORTED BY the channel, chat 2026-11-13 14:35 ET)

Amear, verbatim: "Give me a handoff that includes the research. I want the research to get uh, committed so that way I'm not fucking going down the same rabbit hole again. And then any updates from this chat from today."

Requested of the master: file and COMMIT these three untracked files, in this order, with MANIFEST rows:
1. `docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md` (Gemini Deep Research output + channel audit + Kimi brief)
2. `docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md` (Kimi Deep Research output + channel audit)
3. this file

## 2. CORRECTION to files 1 and 2 (governs)

Files 1 and 2 recommend backtesting `PraxisLastHalfHourMomentum` first. **Withdrawn.** The channel missed that it was already tested and retired:
- 2026-11-01 hand-test run, 1 NQ (NQCONTROW SEP25), $2.96 round-trip commission, 2 ticks/side slippage: 1,304 trades, net -$76,009.84, PF 0.84, max DD -$99,806.96, win rate 47.62%, average trade -$58.29 (`docs/reports/2026-11-01-three-strategy-results.md`, comparison table; re-checked MATCH in `docs/reports/2026-11-01-csv-analyses.md`).
- Retired by Amear's ruling R-VN3-1, filed as D-2026-11-02-A (bead `Praxis_build-afe`, closed). Retire, not delete.
- INFERRED by the channel: at 1 NQ, costs are about $23 a trade ($2.96 commission + 4 ticks x $5 slippage), so an average trade of -$58.29 means it lost roughly $35 a trade BEFORE costs. Costs are not the reason it failed.
- The channel saw no flaw flagged against that test in the records it read. **Do not re-run it unless a record shows a flaw in the 2026-11-01 test.**

## 3. Research outcome, 2026-11-13 (for the record, so it is not repeated)

Two deep-research runs (Gemini, then Kimi) were asked for a steady, high-win-rate intraday NQ strategy that survives an MFFU trailing drawdown at 1 MNQ. **Neither found a viable new candidate.** Status of everything they proposed:

| Candidate | Status | Why |
|---|---|---|
| Last-half-hour momentum (Baltussen, Da, Lammers & Martens 2021, JFE 142:377-403) | TESTED, RETIRED (D-2026-11-02-A) | Lost money on NQ 2021-2026, before and after costs (section 2). The paper's results are for diversified baskets, 1974-2020. |
| First-to-last half-hour momentum with a +/-0.30% threshold (Gao, Han, Li & Zhou 2018, JFE) | NOT TESTED; deprioritised | Same mechanism as the retired strategy above; the threshold filter is the only difference. Test only with a stated reason to expect a different result. |
| Opening gap fade (0.35%-1.50% gap, target prior close) | NOT TESTED; low | Both runs: near break-even at best; Kimi cites practitioner sources only. Limit-order target and intrabar stop fill optimistically on 1-minute bars. |
| VWAP sigma-band mean reversion | NOT TESTED; low | No source found ("Dean & Francis 2026" could not be identified and was withdrawn). Negative after costs at the proposer's own baseline. |
| London-close reversal (10:30-11:15 fade) | DROPPED | Mechanism borrowed from an FX fixing paper; no equity-index evidence. |
| Opening 30-minute momentum (Kimi's new C6) | DROPPED | Kimi's own cited evidence (Grant et al. 2005) points the other way. |

Also ruled out in earlier work and restated by both runs: pre-FOMC drift; trading the release itself; post-earnings drift; short volatility; single-instrument CTA trend; unfiltered opening range breakout; FOMC even-week cycle; overnight drift held across 16:00-18:00; anything holding through a Tier 1 release. Noise-Area breakout and its variants fail the D6 drawdown check (`f10603a`).

Useful leftovers (not decisions):
- Survival check method: block-bootstrap or Monte Carlo of daily P&L against each account's trailing limit. Usable on any future trade list.
- Drawdown must be measured the way the target account trails: intraday open-equity high-water mark if it trails intraday, end-of-day if it trails EOD. Third-party pages and both research runs say standard Rapid sim-funded trails INTRADAY and Rapid EOD trails end-of-day. UNVERIFIED against MFFU's own help pages.
- MFFU drawdown amounts for 100K/150K disagree across sources ($3,000/$4,500 vs $4,000/$6,000). UNVERIFIED. Verify from MFFU's help pages before any purchase.

Channel's view (not an Amear ruling): the next research brief, if any, should exclude everything in the table above and ask a different question rather than re-searching the same space.

## 4. Today's other updates (REPORTED BY the channel)

- **MFFU email:** follow-up sent 2026-11-13 17:26Z in the pre-purchase thread, addressed to the human rep who answered on 11-12. It asks for (1) a written yes/no that unattended automated trading is permitted on Evaluation and Sim Funded (Rapid, Pro, Builder), and (2) whether "Builder Plans" in the news policy includes Builder Sim Funded. No reply yet at filing.
- **VM clock:** Amear checked about 12:27 ET and reported the VM taskbar time matched real time. The earlier "55m43s fast" reading is unconfirmed. Nothing was changed.
- **NT8 Sim connection:** Amear looked at the Control Center and reported no disconnect or reconnect.
- **VM bridge queue:** Amear reported (about 14:30 ET) that the VM code agent has finished. The channel has NOT seen RESULTS.md, QUEUE.log or LOG.md and states nothing about the results. T1 reference: hand run 1,173 trades, net $176,392.92, PF 1.26, max DD $38,905.64, commission $3,472.08. If T2 (ExitMode=OppBand) equals T1 exactly, the bridge may not have applied the enum.
- **Still waiting on Amear (unchanged):** a ruling on parked `ckh` (the channel recommended resuming it; Amear has not ruled); his two questions (does MFFU's reply close R6 OPEN-1; should F4's bar change). D2 items unchanged.
- **Amear asked when PRAXIS can go live.** The channel's answer (an estimate, not a decision): not this year; the critical path is finding a strategy that passes the drawdown gate, and this research did not find one.

