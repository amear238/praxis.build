# Return handoff: Claude.ai Praxis channel to praxis-master, 2026-11-13: Kimi Deep Research follow-up + audit

Written by the Claude.ai Praxis channel, 2026-11-13 about 14:35 ET. Follows docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md (its Appendix B is the brief Kimi answered). File it as written unless a de-identification check fails. REPORTED BY the channel: Amear ran the Kimi brief and supplied the output below at 14:26 ET.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.


Original, filed unedited: `claude/PRAXIS_Kimi_DeepResearch_Strategy_Verification_2026-11-13_ORIGINAL.md` (also Appendix A of the repo handoff `docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md`).
Auditor: Claude.ai channel, 2026-11-13. VERIFIED = checked against a source today; INFERRED = reasoning, not checked; UNVERIFIED = the report's claim, not confirmed.

## Verdict

Better than the Gemini run: it withdrew the source it could not find (Dean & Francis), labelled estimates as estimates, dropped London-close, and points at the right first test. But its headline cost arithmetic for the top pick is wrong by roughly 100x, its MFFU table is unverified, and its "smooth equity" claim for NQ is unsupported. Use it for ranking, not for numbers.

## What holds

1. **Top pick: Baltussen, Da, Lammers & Martens (2021), "Hedging demand and market intraday momentum", Journal of Financial Economics 142, 377-403, DOI 10.1016/j.jfineco.2021.04.029.** VERIFIED as a real, peer-reviewed paper: over 60 futures (equities, bonds, commodities, currencies), 1974-2020; the return from the previous close to 30 minutes before the close predicts the last 30 minutes. A summary of the paper (Alpha Architect) reports annualized Sharpe ratios of 0.87 to 1.73 **at the asset-class level** (diversified baskets, not one contract). The same summary reports the effect is strong on negative-gamma days and **not significant on positive-gamma days** (Table 7): a possible regime filter worth recording, not yet tested.
2. This is the strategy already written in the repo: `ninjascript/PraxisLastHalfHourMomentum.cs` (commit `0ced412`), no tunables, one trade a day. Kimi's rank 1 matches the Gemini audit's rank 1.
3. Gao-threshold vs Baltussen: Kimi prefers Baltussen (no threshold, daily trades). Agreed.
4. Gap fade (C2), VWAP (C1), London close (C4) and new C6 rated low; C4 and C6 dropped. Agreed.
5. Survival method: block-bootstrap or Monte Carlo of daily P&L against the trailing limit. Standard and usable on our trade lists.
6. Drawdown measurement must follow the account's own trailing type: intraday high-water mark (open equity) if the funded account trails intraday, end-of-day if it trails EOD. Correct and important.

## Defects

1. **Cost check for the top pick is wrong.** Kimi says about 2,300 NQ points and "$230,000 gross per year" at 1 MNQ, and "~1000 rounds" a year. INFERRED correct order of magnitude: if NQ delivered the paper's ~7% a year on notional, at an illustrative NQ price of 20,000 that is ~1,400 points, which is ~$2,800 a year at $2 per MNQ point, about $11 per trade over ~250 trades. After $6.68 costs per round trip, about $4 per trade, roughly $1,100 a year at 1 MNQ. Costs would take more than half of the gross edge. Even that assumes NQ matches a diversified basket, which nobody has shown.
2. **Win rate is inconsistent:** 55%, 61% and "55-60%" in different places. The 6.86% / Sharpe 1.73 / 0.55 "table excerpt" is UNVERIFIED (not checked against the paper's tables). 1.73 is the top of the asset-class range, not a single-contract figure.
3. **"Smooth equity" and "very high chance of passing the drawdown gate" are unsupported.** No drawdown figure for NQ exists. Must be measured.
4. **Post-2020 evidence is weak.** The paper ends in 2020. The "still alive 2022-26" claim rests on a SpotGamma market commentary (practitioner, not peer-reviewed). "Bradshaw 2026" and "Open-Alpha" on gap fades are practitioner sources. Rated low.
5. **MFFU table is UNVERIFIED and conflicts with other sources.** No URLs survived in the text. It says every plan's drawdown is 4% of the account (so 100K = $4,000, 150K = $6,000), while the Gemini run and third-party pages give $3,000 and $4,500 for 100K and 150K. Max-contract numbers also differ from other sources. It does agree with third-party pages that standard Rapid sim-funded trails **intraday** and Rapid EOD trails end-of-day.
6. **Gate dollars depend on (5).** Kimi gives $800 / $1,600 / $3,200 / $4,800. If 100K and 150K trail $3,000 / $4,500, the gate is $2,400 / $3,600 (80% of the lower of 4% and the trailing limit). Use the MFFU page on the day of purchase.
7. **Rank 2 (Gao threshold) is the same mechanism as rank 1**, so it adds little diversification. Rank 3 (gap fade) is near break-even by Kimi's own account.
8. Unit errors in C1's cost check ("30 pts ($300)" at MNQ should be $60).

## Recommended next steps (channel's recommendation; master decides under D1, changeable by Amear)

1. Backtest `PraxisLastHalfHourMomentum` on 1 MNQ, 2021-03-08 to 2026-07-17, with the standard cost and slippage settings. Report: trade count, win rate, net per trade, and continuous carried max drawdown, both closed-trade and intraday open-equity.
2. If it is net positive, run the bootstrap survival check against each MFFU account's gate, and test the negative-gamma regime split as research only.
3. Only then code a contrasting strategy (gap fade or VWAP) and test the combination.
4. Verify MFFU's drawdown table from its own help pages before any purchase.


## Appendix A: Kimi Deep Research output, unedited (as Amear supplied it)

Verified and Candidate Strategies for Intraday NQ Futures
Below we review each of the four original strategies (C1–C4) and propose two new ones, verifying their rules and evidence. We then tabulate and compare all candidates. Wherever possible we cite peer-reviewed or institutional sources (with links) for published performance; otherwise we note when figures come from unpublished estimates.

Cost check: Throughout we assume 1 MNQ cost $6.68 per round trip ($4.68 commission + 2 ticks slippage). We deduct 6.68 from each trade's gross P&L to get net outcomes.

Fill optimism: Strategies using market orders at bar close have low fill risk. Those relying on stop orders (intrabar execution) or limit orders have medium optimism. (No strategy here is high-frequency.)

Out‐of‐sample (OOS) trades: All strategies are evaluated over Mar 2021–Jul 2026 (≈4.3 years). We list expected OOS trade counts (≥250 needed).

Post-2018 evidence: We note any published or recent research confirming or disputing each edge, especially beyond 2018. If the original cite is unavailable, we list the evidence as “unverified estimate” or “no published NQ figure.”

Tunable parameters: We count main numeric rules that a developer must set (e.g. thresholds, stops). We prefer only a few per strategy.

Fit rating (High/Medium/Low): Based on evidence strength, expected win rate, drawdown potential, and how well the mechanism is defensible under modern conditions. (A rating of High means a very promising, robust strategy; Low means weak evidence or unsuitable profile.)

Each candidate below is presented with: Name, Rules (exact), Mechanism, Published vs. estimated performance, Cost check, Fill optimism, Trade count (OOS), Post-2018 evidence/decay, Tunable parameters, and a Fit paragraph.

Abbreviation	Description	Source/Ref
VWAP	Volume-Weighted Average Price	see [13][13†L223-L231], [10]
RTH	Regular Trading Hours (09:30–16:00)	
TP/ST	Take-profit/Stop-loss levels	
MNQ	Micro Nasdaq-100 futures	

C1. Volatility-Weighted VWAP Mean Reversion
Rules: During RTH (flat by 15:55), compute the 09:30–15:55 VWAP anchored at 09:30 each day. Maintain $\sigma=$ rolling 60-min std of 1-min log returns (trailing). Let threshold = $k\sigma$ (baseline $k=2.5$). From 09:45 to 15:30: if a 1-min bar closes above VWAP+$k\sigma$, short at the close; if a bar closes below VWAP–$k\sigma$, long at the close. Exit on reversion: flat at the close of the first bar that touches VWAP (i.e. price crosses back to VWAP). Use a stop: stop-loss $=+4\sigma$ if long (i.e. stop price = entry price – $4\sigma$) or $-4\sigma$ if short. No new trades after 15:30; flat by 15:55.

Mechanism: Mean-reversion of large VWAP deviations. The idea is that price swings beyond a volatility band should revert to the daily VWAP. This is a pure mean-reversion concept (no momentum element).

Published performance: No published NQ figure. We could not find “Dean & Francis (2026)” or any academic source with these exact rules. The user’s prior report claims ~60–65% wins and 180–220 trades/yr, but admits baseline expectancy was negative and only tuned parameters made it profitable. In absence of a source, we treat those numbers as estimates only (unverified).

Cost check: With threshold ~$k\sigma$ (e.g. if $\sigma\approx10$ points, threshold=25 points), average wins likely under 30 points. Win rate (~60%) by report yields low net expectancy. After $6.68 cost, if average gross win is e.g. 30 pts ($300) and loss 15 pts, PF ~2.0 gross, net PF falls below 1.0. The prior report noted net $E$ negative before tuning. In short, cost likely overwhelms raw edge.

Fill optimism: Medium. Trades execute at bar close (market order => realistic). Stops ($4\sigma$) can be large and are triggered intrabar – filled optimistically. Exit on VWAP contact is effectively a market-at-bar-close exit upon crossing (optimistic as it assumes we get that last price). Overall medium optimism.

Trade count (4.3y): At ~200/year from report → ≈860 total OOS trades (>>250). If threshold tune differs, trades could vary widely. But likely on most days some crossing occurs.

Post-2018 evidence: None found. We are not aware of any academic test of this exact VWAP+volatility band strategy on NQ or other indices. VWAP-based reversion is plausible but not established in lit. Without published results, we must “measure in backtest.” No published decay info.

Tunable parameters: $;k$ (VWAP band multiplier, e.g. 2.5); stop-multiplier (4); VWAP anchor (09:30); $\sigma$ lookback (60-min). At least 1–2.

Fit: Low. The profile is low win rate. It relies on sharp reversal moves (rare), likely with lopsided risk. The prior analysis suggests baseline expectancy <0 (before extreme tuning). No strong literature support. Mechanism (mean reversion to VWAP) may be crowded or arbitraged. Given no evidence of robust profitability and the need for heavy tuning (per original report), we rate fit low. It may be worth backtesting for completeness, but not high priority.

C2. Opening Gap Fade
Rules: Define gap $G=(P_{\text{open}} - P_{\text{prev 4pm}})/P_{\text{prev 4pm}}$. If +0.35% < $G$ < +1.50%, short at the close of the 09:34 bar (i.e. using 5-min bar 09:30–09:34); if –1.50% < $G$ < –0.35%, long at 09:34 close. Target = prior day’s 16:00 close price (placed as a limit order). Stop = beyond the 09:30–09:34 high (for shorts) or low (for longs) + 2 points (market order if hit). Do not trade if a Tier-1 event is at 09:30 or 10:00. Flat by ~15:55 if not already stopped/target.

Mechanism: Fade small-to-moderate opening gaps. Many traders believe small overnight/overnight gaps tend to retrace (lack of sustained news power). This is a mean-reversion (gap fill) effect.

Published performance: No published NQ figure. The cited “Fung et al. (JBF) 2000” is about general index-reversal and does not give NQ stats. However, Fung et al. find that large overnight moves do reverse (after costs minimal). More recent analysis of NQ (Bradshaw 2026) reports that 0.6–1.0% up-gaps had mild profits (PF≈1.12) while >1.0% lost heavily. An open-gap fade with thresholds 0.35–1.5% is thus partly in a low-edge regime. An open-source “mind-the-gap” study also found 65% fill but only tiny net edge. We conclude: if any edge, it’s slight.

Estimated (unpublished): The user’s report claimed 55–58% wins and ~60–80 trades/yr. Those likely come from a small backtest. We label them estimates (unverified).

Cost check: Suppose average gap fade wins ~5–10 points (e.g. closing prior VWAP differences) and loss similarly ~8–10. After $6.68, expectancy would be negligible. Indeed, Bradshaw’s backtest shows almost break-even per trade.

Fill optimism: Medium. Entry at 09:34 bar-close (market) – normal. Stop order (beyond high/low+2) can fill intrabar (optimistic). Target is a limit; if it’s not reached, presumably position holds until late afternoon exit (we assume exit 15:59). If reached intraday, a limit fill is usually optimistic. So medium optimism.

Trade count (4.3y): With ~70/yr (mid of report’s 60–80), ~300 total OOS trades. That meets 250. The strategy only triggers on gap days, so trades ≤1/days with moderate gap. So trades on perhaps 1/3 of days.

Post-2018 evidence: Mixed. Bradshaw (2026) shows this edge was negligible 2010–2019, better 2020–26. In SPY (the more studied S&P ETF), open-gap fade edge tends to erode over time (only certain gap sizes remained profitable). No sign that algorithmic flow changed the effect; rather, overall edge is slim and highly sensitivity to gap size. No obvious post-2018 degradation, but also no robust profit.

Tunable parameters: Lower and upper gap thresholds (0.35%, 1.50%), stop offset (2 points). We count 3. Target is fixed (prior close).

Fit: Low–Medium. The mechanism (fade of modest overnight gap) has historical basis, but the edge is razor-thin. Win rate ~50–55% is not “high,” and PF barely above 1.0. It does not meet the desired high win-rate profile. Nonetheless it trades often enough to reach count. Because of uncertain evidence and low net expectancy after cost, fit is low. It may be tested but is not a priority, especially given constraints.

C3. First- vs. Last-Half-Hour Momentum (Gao et al. 2018) and Baltussen et al. 2021
This entry covers two closely related intraday momentum strategies. We compare:

(a) Gao et al. (2018) style: (SPY evidence) If 09:30–10:00 return > +0.30%, long at 15:30; if < –0.30%, short at 15:30. Exit at 15:59 (end of RTH). “Catastrophic” stop 0.5% (i.e. 0.5% adverse move ends trade). That yields on average ~1 trade per day (some days flat if no threshold condition met). Gao et al. report ~52–54% wins (SPY, 1993–2013).

(b) Baltussen et al. (2021) style: (Cross-asset evidence) Let ROD = return from prior day’s 16:00 to today’s 15:30. If ROD > 0, long at 15:30; if ROD < 0, short at 15:30. Exit at 15:59. No threshold (always trade daily), no stop (or can use a large one). This is essentially a 1-trade-per-day momentum strategy. In published tests on equity index futures (1974–2020), this yields ~6–7% annual return (Sharpe ~1.70) and ~61% win rate.

We evaluate both in light of constraints.

Rules (Gao style): As above; threshold ±0.30% for the 09:30–10:00 return.

Rules (Baltussen style): If (today 15:30 price – prior close price) >0 → long at 15:30 close; if <0 → short. Exit at 15:59. (Optionally use a 0.5% stop to cut monsters, but Baltussen didn’t specify one, since each day only one bar open, the price can only move 0.5% by a big gap or news.)

Mechanism: Momentum. Both assume an intraday continuation: “big move early day leads to big move late day.” Possible cause: dealer gamma hedging or systematic trading flows that push prices in same direction through day.

Published performance (Gao): Gao et al. (J. Fin. Econ. 2018) find a significant effect in S&P500 futures: first-half-hour return strongly predicts last-half-hour return, with statistical and economic significance. They don’t tabulate a simple win rate or PF. The user’s report claims ~52–54% wins, ~110 trades/yr (≈once/day on threshold days). There is no published NQ figure. Likely SPY results only.

Published performance (Baltussen): For equity index futures (including NASDAQ) 1974–2020, Baltussen et al. (JFE 2021) report for the “R(t_{ROD})” strategy (our rule): avg 6.86% annualized return, Sharpe 1.73, win rate 55%. (Table excerpt: η(r_ROD) strategy: avg ret 6.86%, SR 1.73, success 0.55.) This is gross returns (no cost) on diversified equity futures. For a single instrument like NQ, actual PF after costs will be lower, but the edge is large.

Cost check: The Baltussen result implies large return per year (~2300 points on NQ); with 1 MNQ this is $\sim$ $230,000 gross per year. After commission $6.68 per day (~1000 rounds * $6.68 ≈ $6,680), net still huge. Even if NQ edge is smaller than basket, this is orders-of-magnitude above cost. For Gao-style threshold, fewer trades (~100/yr), but big swings similarly. Both easily cover $6.68/trade.

Fill optimism: Low. Both trade at specific bar closes (15:30 entry, 15:59 exit) – actual markets have enough liquidity at these times (close of bar), so realistic. The 0.5% stop (if used) might trigger intrabar, so stops are optimistic; otherwise, exits at close. Overall fill risk is low.

Trade count (4.3y):

Gao style: roughly one trade per day when threshold met. If volatility is moderate, threshold hit maybe ≈2/3 days. Report said ~110/yr → ~473 trades OOS. Good.
Baltussen style: exactly one trade every trading day (mon–Fri) except holidays. ~250/yr → ~1075 trades OOS. Well above minimum.
Post-2018 evidence: Strong. The Baltussen (2021) study covers up to 2020 and finds robust results. Moreover, a 2026 market commentary (SpotGamma) confirms first-vs-last-half-hour momentum remains alive into 2022–26. By contrast, one recent study found overnight momentum edges faded in sample, but that is a different regime. No evidence of decay for the 15:30 momentum effect is reported. This strategy is well-supported through 2020.

Comparison (Gao vs Baltussen): The Baltussen version (no threshold, daily trade) is stronger for us: it has published results on equity futures, trades every day (more than threshold-Gao), and requires only a single decision (sign of ROD) without tuning. The Gao version requires picking a threshold (weaker evidence for it and possibly worse performance out-of-sample). However, we note Gao’s conceptual idea (morning→evening momentum) is validated in Baltussen’s broader framework.

Tunable parameters:

Gao style: threshold (0.30% above), stop (0.5%). So 2.
Baltussen: no parameter (if we use as given). Possibly stop =0.5% optional (1 param).
Overall 1–2.
Fit: High. This momentum approach has by far the most evidence (JFE 2021 plus others) and robust performance. It yields daily trades with ~55–60% wins and smooth equity. The high win rate/low variance profile fits our needs well. Mechanism (dealer hedging, systematic flows) is plausible and pervasive. We rate it high-fit for backtesting.

C4. London-Close Reversal (10:30–11:15 to 11:15–12:00)
Rules: If the 10:30–11:15 return > +0.40%, short at 11:15; if < –0.40%, long; exit at 12:00. Stop fixed at ±40 points.

Mechanism: Alleged reversal following the London 11:00 fix or midday auction flows, by analogy to FX fixing strategies. No known equity evidence.

Published performance: No published figure or source for equity indices. We found only a Bank of Canada FX study (Krohn et al. 2021) documenting currency reversals around London fix times. No U.S. equity index study. This was only cited in the user’s report, without source.

Estimates: The report itself said edge is “razor-thin.” Without evidence, we must treat this as untested.

Cost check: Ignoring, as likely not profitable.

Fill optimism: Medium (market at bar close, stop intrabar).

Trade count: Potentially small (depending on how often a 0.4% move occurs in 45m). Likely <250 in 4.3y.

Post-2018 evidence: None for equities. Only FX analogues exist. No sign of a time-of-day anomaly for NQ.

Tunable parameters: threshold 0.40%, stop 40 points (2 parameters).

Fit: Drop (Low). With no supporting evidence in U.S. futures and a contrived timing, this appears spurious. We would not backtest this candidate, unless new data emerges.

New C5. End-of-Day Directional Momentum (Baltussen et al. 2021)
This is essentially the Baltussen strategy already described as part of C3. We restate it as a separate candidate emphasizing its ruleset:

Rules: Each day, compute $R_{\text{ROD}} = P_{15:30} - P_{\text{prev 16:00}}$ (return from prior close to 15:30). If $R_{\text{ROD}}>0$, go long at 15:30 (close of that 1-min bar); if $R_{\text{ROD}}<0$, go short. Exit at 15:59. (Stop = 0.5% optional.) Flat overnight.

Mechanism: Daily momentum (buy winners, sell losers) from previous session. Attributed to flows like leveraged ETF rebalancing or dealer gamma hedging (which generate a creeping continuation of yesterday’s trend).

Published performance: For equity index futures, Baltussen et al. report 6.86%/yr gross with SR~1.73 (see C3), with win rate ~55%. No published NQ-only figure, but their multi-index test includes Nasdaq.

Estimated: The original report cited “one trade every day, net Sharpe 0.43 after costs” (untested), but the published result is far stronger (net of only minimal friction).

Cost check: Gross edge 7%/yr ($7000 per $100k, ~$690 per $10k), easily > cost. For 1 MNQ, even a few tens of points per day is far above $6.68.

Fill optimism: Low (daily market-close orders).

Trade count: ~253/year (every trading day) → ~1080 OOS trades.

Post-2018 evidence: Strong. Baltussen (2021) covers up to 2020. SpotGamma (2026) reconfirms it persists into 2022-26.

Tunable parameters: Essentially none (one could optionally include stop 0.5%).

Fit: High. This matches our goals exactly: high win rate (~55%+), very smooth returns (Sharpe ≈1.7 pre-cost), daily trading, and tight exit. Mechanism is robust (documented across regimes). We rank this top priority.

(Note: C3’s “Gao style” and C5 are almost the same mechanism, so one would likely just code the non-threshold daily momentum version.)

New C6. Opening-Bars Momentum (Inspired by Grant et al. 2005)
Rules: If the first 30-minute return (09:30–10:00) exceeds +0.50%, long at 10:00; if <-0.50%, short; exit at 12:00. Stop = 0.5% (70–80 points). [Parameters are illustrative – one could tune 0.3–0.5% threshold.]

Mechanism: If the very morning moves strongly, continue that move into late morning. (This is like the reverse of many open-reversal strategies.) Potentially driven by follow-through momentum on days that open strong.

Published performance: No direct published figure for this rule. Grant et al. (JBF 2005) found highly significant intraday reversals after large opening moves, which suggests opposite trades. Thus, if anything, large opens tended to revert, not continue. We include this as a momentum contrast to test: if small open moves revert (as in C6), large moves might continue. However, Grant found profit after costs was marginal. There is no known academic support for a continuation.

Estimated: Unknown; it is not in literature.

Cost check: Likely poor. If Grant found open gaps were over-reversed, then momentum on big open moves is probably unprofitable. Any short-term continuation would be small.

Fill optimism: Medium: entry at 10:00 bar-close (market), exit at 12:00 (market). Stop intrabar.

Trade count: If threshold ±0.50%, maybe 100–150 trades/year (depending on volatility). Possibly ~400–600 OOS trades. But if profitless, not helpful.

Post-2018 evidence: None. The only study suggests open-gap reversal, not continuation. So we expect no edge or negative expectancy.

Tunable parameters: threshold (e.g. 0.5%), stop (0.5%).

Fit: Low. We have no evidence this works; existing evidence suggests the contrary. This is listed only for completeness. It conflicts with established open-reversal findings. Its expected win rate and expectancy are likely low or negative. We would not prioritize this over others.

Summary Table of Candidates
Candidate (Label)	Entry/Exit Rules	Mechanism	Publ. Stats (Instrument, Sample)	Est. Stats (MNQ, 2021–26)	Cost Check	Fill Optimism	OOS Trades (4.3y)	Tunable Param.	Fit
C1. VWAP σ-band mean reversion	See above (VWAP±2.5σ)	Mean reversion to intraday VWAP	None for NQ. (Report: ~60–65% win, 180–220/yr)	Neg expectancy (estimate)	~-$6.7/tp, win avg ~X (small).	Medium	≈860	2 (k,stop)	Low
C2. Opening Gap Fade	Gap 0.35–1.5% fade at 09:34 (target prior close)	Gap-fade mean-reversion	No NQ pub. fig.; Fung+00: small profit after costs; Open-Alpha: edge ≈0	~51% win, 60–80/yr (estimate)	Extremely small net (PF~1.0), ~-$6.7 per trade.	Medium	~300	3 (thr_lo,thr_hi,stop)	Low
C3. First→Last 30m Momentum	9:30–10:00 > +0.30% → long @15:30; <–0.30% → short; exit 15:59; 0.5% stop	Intraday momentum (morning→close)	Gao+18 (SPY): significant first-to-last momentum (no NQ data).	~53% win (est), ~110/yr	Must cover 1 stop/tp, but expect positive.	Low	~470	2 (thr, stop)	Med
C3’/C5. ROD (Rest-of-day) Momentum	If (prev close→15:30) >0 → long at 15:30; <0 → short; exit 15:59	Intraday momentum (overnight→close)	Baltussen+21 (Equity futures 1974–2020): return 6.86%/yr, Sharpe 1.73, win~61%	n/a (apply to NQ)	Large (>100 pts/yr), >> cost	Low	~1075	(stop?)	High
C4. London-Close Reversal	10:30–11:15 >+0.40% → short at 11:15; <–0.40% → long; exit 12:00	FX-fixing contrarian?	No equity source. (Bank of Canada FX fixings)	Razor-thin (est.)	Likely negative after cost.	Medium	<250	2 (thr, stop)	Drop
C6. Opening 30m Momentum	9:30–10:00 > +0.50% → long at 10:00; <-0.50% → short; exit 12:00	Morning momentum	None. (Grant+05 suggests reversal, not momentum)	Unknown (likely poor)	Likely negative (contrary to Grant’s result)	Medium	~500	2 (thr,stop)	Low

Published stats give instrument/sample and indicate net vs gross: e.g. [46] is gross on futures (pre-cost).
“Est. stats” are from internal report or other non-published sources; labeled est. if so.
Fill optimism rating: Low (market fills), Medium (stop/limit).
MyFundedFutures (MFFU) Drawdown Rules
From MFFU’s Help Center (current as of 2026-11-13):

Rapid Plan (all sizes):

Evaluation: Profit target = 6% of initial. Max drawdown = 4% (EOD) of initial. Consistency rule = 50%. No daily loss limit. Max contracts scale (3 mini @25k, 5@50k, 8@100k, 10@150k).
Sim-Funded: Drawdown = 4% (intraday trailing) of initial. Trailing stops the first time account is up by $100 (lock at +$100). No consistency requirement. No daily loss. Max contracts same as eval.
Sources: e.g. Rapid 25k pages, 50k, 100k, 150k similarly show 6%/4% with cons=50%.
Rapid EOD Plan (25k & 50k):

Evaluation: Profit = 6%. Max drawdown = 4% of initial (EOD). Consistency = 30%. No daily loss. 25k: 2 mini max; 50k: 3 mini.
Sim-Funded: Max drawdown = 4% of initial, EOD trailing (moves only on session close). Trailing lock at +$100 (then fixed). No consistency rule, no daily loss. Max contracts same as eval.
Pro Plan (50k,100k,150k):

Evaluation: Profit = 6%. Max drawdown = 4% of initial (EOD). Daily loss = none; Consistency = 50%. 50k: 3 mini; 100k: 6 mini; 150k: 9 mini. News trading allowed.
Sim-Funded: Drawdown = 4% of initial (EOD trailing). No consistency, no daily loss, no news. Contracts: 50k→3 mini; 100k→6 mini; 150k→9 mini.
Builder Plan (50k):

Evaluation: Profit = $3,000 (6%), Max drawdown = $2,000 (4%) (default MLL; there is also a 50k-add-on with 3% MLL). Daily loss soft pause $1,000. No consistency rule. 4 mini max. Trailing = EOD.
Sim-Funded: Drawdown = same $2,000 EOD trailing (starts at –2k then trails up). Daily loss soft pause $1,000. 4 mini. (Only 1 live account per user on Builder.). News is allowed on Builder eval/sim.
(All cash values for trailing locks/MLLs in tables above are 4% of initial, with a $100 lock buffer after trailing.)

A combined summary table is in the Appendix below. All info is from MFFU’s own help pages (see cited lines).

MFFU Rule Table (key fields per plan & size)
Plan	Account	Stage	Trailing Type	Drawdown (Max Loss)	Lock	Consistency	Daily Loss	Max Contracts
Rapid (intraday)	25k Eval	EOD	4% of 25k = $1000 (locks at +$100)	–	50%	None	3 minis	
25k Sim	Intraday	4% ($1000) intraday (lock $100)	$100	–	None	3 minis	
50k Eval	EOD	4% ($2000)	–	50%	None	5 minis	
50k Sim	Intraday	4% ($2000)	$100	–	None	5 minis	
100k Eval	EOD	4% ($4000)	–	50%	None	8 minis	
100k Sim	Intraday	4% ($4000)	$100	–	None	8 minis	
150k Eval	EOD	4% ($6000)	–	50%	None	10 minis	
150k Sim	Intraday	4% ($6000)	$100	–	None	10 minis	
Rapid EOD (EOD trail)	25k Eval	EOD	4% ($1000)	–	30%	None	2 minis	
25k Sim	EOD	4% ($1000) EOD trail (lock $100)	$100	–	None	2 minis	
50k Eval	EOD	4% ($2000)	–	30%	None	3 minis	
50k Sim	EOD	4% ($2000) EOD trail (lock $100)	$100	–	None	3 minis	
Pro	50k Eval	EOD	4% ($2000)	–	50%	None	3 minis	
50k Sim	EOD	4% ($2000)	–	–	None	3 minis	
100k Eval	EOD	4% ($4000)	–	50%	None	6 minis	
100k Sim	EOD	4% ($4000)	–	–	None	6 minis	
150k Eval	EOD	4% ($6000)	–	50%	None	9 minis	
150k Sim	EOD	4% ($6000)	–	–	None	9 minis	
Builder	50k Eval (default MLL)	EOD	4% ($2000)	–	0% (no cons)	$1000 soft	4 minis	
50k Sim	EOD	4% ($2000)	–	–	$1000 soft	4 minis	

Notes: “Daily Loss” shows a “soft pause” dollar value from Builder page; Rapid/Pro have none. We omitted one-day Pro variant and 50k-add-on variants for brevity. All sim-funded locks are $100 (as given). Each plan’s wording was confirmed from the MFFU Help Center pages above, current as of retrieval date.

MFFU Gate Thresholds
MyFundedFutures imposes for each account: a continuous trailing drawdown = 4% of account. We must stay below 80% of whichever is lower: (a) 4% of initial or (b) the current trailing drawdown (which is normally equal to 4%).

Thus 80% of 4% is 3.2% of account. In dollar terms at 1 MNQ:

25k → 0.8*($1000) = $800
50k → $1600
100k → $3200
150k → $4800
So a backtest’s max drawdown must never exceed 3.2% ($) of the initial account. (We state these as “dollar threshold” in the gate section.)

Trailing-Drawdown Survival Analysis
Academic and institutional literature on drawdown risk often highlights that Max Drawdown (MDD) is path-dependent and not fully captured by volatility or Sharpe metrics. For example, Choi (2021) notes maximum drawdown is a model-free risk measure with intuitive appeal. In practice, to estimate survival probability under a high-water-mark (trailing) drawdown limit, one should simulate the strategy’s equity paths.

Recommended method: A common approach is Monte Carlo simulation or block-bootstrap of the strategy’s daily P&L. Given a backtest’s daily returns, one can randomly resample (with replacement) the observed returns (block length = 1 or more days) to generate many synthetic equity paths. For each simulated path, check whether the trailing drawdown ever breaches the 80% threshold. The fraction of paths that never exceed the drawdown gives the survival probability. This approach was illustrated by QuantDare in bootstrapping portfolio returns. Alternatively, parametric Monte Carlo (e.g. Gaussian or fat-tailed shocks calibrated to observed returns) can be used. In any case, we will need to measure drawdowns on the actual trade/P&L list.

Combining strategies to reduce drawdown: No specific peer-reviewed study precisely shows “mean-reversion + momentum lowers drawdown.” However, the spirit is akin to diversification. For example, Choi (2021) finds that portfolios constructed with drawdown-based signals (a form of trend-following) yield more consistent risk-adjusted returns. By analogy, a mean-reversion strategy often wins on days momentum loses (and vice versa), so a combined portfolio can smooth returns. In absence of direct study, we note that mixing low-correlation strategies is a standard risk-control practice (Markowitz framework). We will monitor our own combined backtests to see if drawdowns shrink when pairing strategies (this must be verified on our data).

Survival probability source: While not a journal citation, the method of simulating equity curves via bootstrapping is a well-known empirical technique. Academic treatments of drawdowns exist (e.g. Chekhlov et al. 2005 on “conditional drawdown”), but none give a closed-form survival formula for a high-water mark. Hence we will rely on Monte Carlo or block-resample of our actual returns.

Rejected Strategies
Below are other intraday ideas explicitly excluded (per instructions or lack of evidence):

Pre-FOMC drift or trading the release itself (excluded by rules).
Post-earnings drift on index (no clear daily edge).
Short-volatility carry (VIX calendar) (excluded).
Single-instrument trend following (daily or multi-day) (excluded per guidelines).
Unfiltered opening-range breakout (excluded; tends to “grab losers”).
FOMC even-week cycle (no evidence, removed).
Overnight drift across 16:00–18:00 (excluded by guidelines).
Holding through Tier-1 news (disallowed).
C4 London-close reversal (no equity evidence – dropped).
C1 VWAP strategy (if pure mean-reversion on VWAP persists).
C6 large open continuation (lack of support).
Others mentioned by user guidelines.
Each of the above was either forbidden or had weak/contradictory evidence, so we do not consider them further.

Recommended Backtests (Top-3 Priorities)
Based on the above, we rank the following three to backtest first:

End-of-Day Momentum (Baltussen et al.). This has the strongest support: multi-year evidence on futures, trades daily, high win-rate profile. We expect very high chance of passing the drawdown gate given reported Sharpe.
First-to-Last 30m Momentum (Gao et al.). A variation on (1) with a threshold, but still momentum. Even though Baltussen dominates, it is worth testing Gao’s threshold version to see if tuning (e.g. threshold 0.30% vs none) improves returns in-sample or OOS. It trades slightly fewer days but similar net directional edge, if any.
Opening Gap Fade. This is the best-supported mean-reversion candidate. It trades often enough to meet sample size. Even though its edge is small, it is a contrasting mechanism to momentum; combining it with momentum might smooth equity. Also, many traders expect some gap fill, so it’s worth verifying.
(If a fourth were allowed: the VWAP mean-reversion (C1) could be a distant candidate, but evidence suggests low expectancy.)

Caveats and Unknowns
Many reported figures (especially for C1, C2, C6) come from unpublished backtests or dealer notes. We have no peer-reviewed verification of their NQ performance. All such stats are “must be measured in our backtest.”
Fill execution: Even 1-min bars can hide microstructure issues. We rated fill optimism qualitatively, but actual slippage/backtest fill behavior must be checked. E.g. the stop/limit assumptions in NT8 backtesting (optimistic fill) could overstate performance, especially for wide stops.
Tier-1 stops: Strategies avoid trading around releases, per rules. Careful coding needed to skip entries (e.g. skip 09:30/10:00 entries).
Parameter sensitivity: We list default thresholds (e.g. 2.5σ, 0.35%, 0.30%). If backtest shows break-even at those, we should consider tuning within constraints. However, we must keep tunables to ≤2, and avoid overfitting.
Correlated signals: C3 and C5 are both momentum, C2 and C6 mean-reversion. If combining strategies, beware correlation of returns and of drawdowns.
Drawdown measurement: We must compute the continuous equity high-water mark (intraday for Rapid, EOD for EOD plans) per MFFU definition when evaluating the gate. This will be done on our backtest P&L.
MFFU rules: We assume no changes beyond those cited. If MFFU updates rules (e.g. Pro plan changed Oct 2026), we’ll adjust.
Sources: We cited only peer-reviewed or institutional sources above: Fung et al. 2000, Baltussen et al. 2021, Gao et al. 2018, Grant et al. 2005, Bank of Canada staff, plus open-research notes where needed. Retail forums and unsourced claims have been avoided or flagged low-confidence.

