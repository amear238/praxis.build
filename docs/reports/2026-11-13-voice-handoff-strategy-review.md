# Voice handoff: strategy review with Amear, 2026-11-13

Written by praxis-master for the voice-chat agent. You can read every file in this repo (/Volumes/Sensidine/Praxis.build). Every figure below is quoted from a named file and line. The evidence behind each one, as pasted command output, is in `docs/reports/2026-11-13-strategy-review-index-manager.md` (the "index"; its Verification evidence section starts at :191). If a figure here and a source file disagree, the source file wins. Say so to Amear.

## What Amear wants from this conversation

His words this session: "the strategy research what it came back with as well as what the code agent did on the VM with him today and yesterday being that today is November 13 I from what I've gotten so far it would appear that the strategies are not promising so far so I also want to know whether we considered indicatoror what is going on".

So there are four things to cover: (1) what the strategy research found; (2) what the VM code agent did on 2026-11-12 and 2026-11-13; (3) whether indicator-based strategies were ever considered; (4) where things stand overall.

## How to run it

- Plain English. Give account figures in dollars, and always name the contract size (1 NQ or 1 MNQ). One MNQ is one tenth of one NQ.
- Label every figure by where it came from: Amear's hand run, a Mac-side recomputation, or "reported by the channel" (second-hand).
- You do not decide anything. If Amear rules on something, write down his words and the time, so the master can file it in the next Code session. Four things always wait for his explicit word: spending money; switching on live trading or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.
- Do not edit repo files. If you want to leave notes, write one new file under docs/reports/ named `2026-11-13-voice-notes-strategy-review.md`, and Amear's words in it must be verbatim.

## Read these, in this order

1. `docs/reports/2026-11-13-strategy-review-index-manager.md`: start with its 15-line summary at :3-:18, then Q1 to Q5 at :43-:160.
2. `docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md`: the channel's close-out from today. Its research outcome table is at :28-:35 and its correction withdrawing the Last-Half-Hour recommendation at :18-:22. Where it disagrees with the two research files, it governs (:3).
3. `docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md` (the Gemini run plus the channel's audit of it) and `docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md` (the Kimi run plus the channel's audit). Use them for detail only. Their backtest order at strategy-research :30 is superseded.
4. `docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md`: the VM bridge runs T1 to T3.
5. `docs/reports/2026-11-01-three-strategy-results.md` :402-:405: the four hand-run results table.
6. `docs/reports/2026-11-09-d6-drawdown-check-manager.md`: the drawdown check every strategy failed. Its summary is at :7.
7. If the indicator question goes deeper: `docs/reports/2026-11-13-strategy-review-index-worker3.md` (term counts at :11-:49). For the research history: `docs/reports/2026-11-13-strategy-review-index-worker2.md` (runs table at :10-:23, what happened to each proposal at :25-:64, ideas that keep coming back at :66-:79).

## 1. What has been tested (index Q1, :43-:75)

Four strategies have recorded backtests. Amear ran all four by hand in NinjaTrader on 2026-11-01: NQ continuous contract, 1-minute bars, 2021-03-08 to 2026-07-17, 2 ticks slippage per side, $2.96 round-trip commission, 1 NQ. Mac-side workers recomputed all four from the exported CSVs and got the same results (index :47).

| Strategy | Trades | Net at 1 NQ | Profit factor | Max drawdown at 1 NQ | Win rate | Status |
|---|---|---|---|---|---|---|
| Noise-Area breakout, baseline (exit at band or VWAP) | 1190 | $197,327.60 | 1.29 | -$45,282.04 | 40.67% | kept "for the record" (D7) |
| Noise-Area, OppBand exit | 810 | $210,182.40 | 1.26 | -$50,748.88 | 58.02% | no decision entry; status after D7 not stated |
| Noise-Area, flat at 15:59 | 1190 | $193,017.60 | 1.28 | -$40,637.04 | 40.50% | no decision entry; status after D7 not stated |
| Last-Half-Hour Momentum | 1304 | -$76,009.84 | 0.84 | -$99,806.96 | 47.62% | retired, D-2026-11-02-A |

Why none of them is a go:
- The drawdown gate (rule A4, DECISIONS.md :1735-:1740) says the backtest max drawdown must stay below the lower of 3.2% of the account size and 80% of MFFU's trailing drawdown limit. For a 50K account that works out to $1,600 at 1 MNQ (D6 report :31).
- The D6 check (commit `f10603a`) measured the three Noise-Area arms at 1 MNQ, derived from the NQ trade lists rather than an MNQ run. Its worst within-window stretch was "$2,774 to $2,914", under the ceiling "only on the 150K accounts". On the committed four-measure basis it was "$4,463 to $5,280. That fails every account size." At 1 NQ, "every account fails." (D6 report :7)
- So Noise-Area makes money at 1 NQ, but it swings too hard for MFFU's drawdown rules at any size the record has checked. D7 (DECISIONS.md :1940-:1944) fired: Noise-Area "continues through the VM tests for the record, but a GO on MFFU is not expected from it."
- Last-Half-Hour Momentum lost about $58 a trade at 1 NQ. The channel's own arithmetic says costs are about $23 a trade, so it lost money before costs too (session-close :21, labelled INFERRED by the channel).
- No walk-forward test (rolling out-of-sample testing) has been run; it is specified only (index :74).

## 2. What the research found (index Q2, :76-:109)

Eight research efforts are on record: two in April 2026, one in May, plus 31 October, 4 November, 8 November, and today's Gemini and Kimi runs. Only two ideas were ever backtested: Noise-Area and Last-Half-Hour Momentum. Opening-range breakout (TORB and ORB) and the two announcement strategies, Pre-Announcement Drift and Announcement-Day Premium, are written specs or designs with no code.

Today's two runs (Gemini, then Kimi) were asked for a steady, high-win-rate intraday NQ strategy that survives an MFFU trailing drawdown at 1 MNQ. The session-close sums them up (:26): "Neither found a viable new candidate." The full table is at session-close :28-:35. In short: last-half-hour momentum was already tested and retired; the threshold variant was deprioritised as the same mechanism; gap fade and VWAP band reversion were rated "NOT TESTED; low"; London-close reversal and opening-30-minute momentum were dropped.

The same ideas keep coming back across runs (index :103-:109). Last-half-hour momentum has appeared 5 times (a count the index labels INFERRED); gap fade and VWAP/Bollinger reversion were excluded in early runs, then proposed again today. The channel's view (session-close :44, not a ruling): any next research brief should exclude everything already covered and ask a different question.

## 3. Were indicators considered? (index Q3, :111-:125)

Plain answer from the record: no, not systematically. Across every tracked file and the April source documents, there are zero hits for moving average, RSI, MACD, Keltner, ADX, stochastic, Supertrend, cumulative delta, Ichimoku and Donchian (index :125, evidence E3.2). No indicator-driven strategy has been coded or backtested.

Where indicators do show up:
- Inside Noise-Area: session VWAP is its coded default exit, and it was backtested that way. An ATR(14) stop for another walk-forward arm is written but has never been compiled or run (index :116-:117).
- As screened-out ideas: standalone VWAP/Bollinger reversion on NQ ("EXCLUDED — no peer-reviewed NQ evidence post-2018"), standalone 5-minute opening-range breakout ("ELIMINATED — no robust standalone edge on NQ without filters"), order-flow imbalance ("EXCLUDED — 2-price-change horizon, requires co-location"), and today's VWAP band reversion (Kimi: "Post-2018 evidence: None found."). (index :120-:123)

Why it happened: every research run screened ideas by published, peer-reviewed evidence on NQ after 2018. Classic indicator strategies rarely have that kind of evidence, so they were filtered out before anyone tested them (index :125). That is a choice about how the research was framed. The record contains no decision that indicators are ruled out. Whether to look at them is Amear's call.

## 4. What the VM code agent did, 2026-11-12 and 2026-11-13 (index Q4, :127-:147)

Be clear about the evidence level. The repo's only record of this is two channel files, and both are second-hand: the VM session wrote a report, Amear pasted it to the Claude.ai channel, and the channel wrote it up (vm-queue :5). The VM agent's own files (results T1 to T3, bridge.log, its commits) live in a local repo on the VM at `C:\praxis\vm-bridge`, which has no remote. None of them are on this Mac.

As reported for 2026-11-13 (vm-queue :11-:31):
- The agent ran three headless Strategy Analyzer backtests through the bridge, on Noise-Area, at 1 NQ.
- T1 (BandOrVWAP exit): 1,173 trades, $176,392.92 net, profit factor 1.2615, max drawdown -$38,905.64, reported as an exact match to an earlier hand run of Amear's. That hand run has no primary record in this repo.
- T2 (OppBand exit): 1,112 trades, $188,618.48 net, profit factor 1.2861, max drawdown -$37,906.24.
- T3 (BandOrVWAP again): identical to T1.
- What this shows, per the channel: the bridge can run a backtest without anyone clicking, it applies parameters including the exit mode, and the Analyzer tab can be put back the way it was. Commission could not be checked, because the result files carry no commission total. The channel labels this its reading ("INFERRED, not a ruling", :33).
- Deviations: Amear had to open the Analyzer tab by hand. NT8 restarted at 12:32 PM, and who or what restarted it is not stated. The queue script was not used because the `claude` command is not installed on the VM. The send-backtest script was extended to pass parameters.
- Channel's arithmetic, not a run: at 1 MNQ, T2's drawdown would be about $3,790, above the 50K gate of $1,600.

For 2026-11-12, the repo has one line only: vm-queue :41 quotes the agent's to-do, "check in the Control Center whether the Sim feed cycled when the AddOn loaded yesterday." Nothing in the repo records the AddOn load itself, who did it, or how it went. Ask Amear what happened that day. Do not fill the gap.

Three things in the record don't line up. Mention them; don't resolve them:
- T1 has 1,173 trades, but the 2026-11-01 baseline hand run has 1190 (index :61). T1's tab is named "PRAXIS baseline NQCONTROW 0930". Nobody has looked into the difference.
- Amear ruled on 2026-10-28 "No more Cowork or in-VM Claude Code executor work.", "lifted COMPLETELY once two tests pass" (DECISIONS.md :1010). The last VM-agent decision on record is D-2026-11-10-C, "VM agent = Hermes over SSH" (DECISIONS.md :2076). The repo does not record how the 2026-11-13 VM Claude Code session fits those two (index :145).
- The VM results used the $2.96 commission. MFFU's is $4.68 round trip, and the re-run at that rate has not happened (vm-queue :40).

## 5. Where things stand (index Q5, :149-:160)

- No strategy in the record passes the drawdown gate. Finding one is the critical path. The channel's estimate for go-live (session-close :53, "an estimate, not a decision"): not this year.
- The next research thread on record is the announcement strategies, Pre-Announcement Drift and Announcement-Day Premium (ruled for research under D-2026-11-08-A R6, DECISIONS.md :1572-:1579). That bead, `Praxis_build-ckh`, is parked and needs Amear's decision to resume. No code exists for it.
- Waiting on Amear (HANDOFF.md working copy :20-:22): the decision on `ckh`, plus two open questions: "(1) does MFFU's 2026-11-11T22:41:33Z point 4 close R6 OPEN-1; (2) should F4's bar change."
- Waiting on MFFU: a follow-up email went out today at 17:26Z asking for a written yes or no on unattended automated trading, and whether "Builder Plans" in the news policy includes Builder Sim Funded. No reply at filing (session-close :48).
- Hand steps: setting the $4.68 commission before the re-run; checking whether the Sim feed cycled on the 11-12 AddOn load (vm-queue :40-:41).
- Not verified: MFFU's drawdown amounts for 100K and 150K accounts disagree across sources, and whether standard Rapid trails intraday or end-of-day is unconfirmed against MFFU's own pages (session-close :41-:42). Check these before any purchase.

## If Amear wants to look at indicators

Write down what he wants and why, and nothing more. A new research brief or backtest is a unit for the master to dispatch in a Code session. That brief would need to: exclude everything in session-close :28-:37; say whether the post-2018 peer-reviewed screen still applies; and measure drawdown the way the target MFFU account trails (intraday or end-of-day, session-close :41).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
