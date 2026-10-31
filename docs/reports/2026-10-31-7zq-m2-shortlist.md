# 7zq M2 — Shortlist of three NQ-applicable intraday strategies (non-Noise-Area)

- Unit: `Praxis_build-7zq`, phase M2, worker 1. Mode: BUILD (research). Date: 2026-10-31.
- Process log with every command and its output: `docs/reports/2026-10-31-7zq-m2-worker1-research.md`.
- Scratch root (downloads, untracked): `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/m2-research/` (written below as `$B`).
- Grades: **OBSERVED** = in command output pasted here or in the process log; **INFERRED** = my reasoning from observed text; **UNVERIFIED** = not checked in this session, or seen only in a secondary source; **SPEC-SILENT** = the source does not say.
- NQ bar convention (from the brief): 1-minute bars stamped at their END. The first RTH bar is stamped 09:31 and covers 09:30:00–09:31:00. The 16:00-stamped bar is the last RTH bar. The backtest uses `Calculate.OnBarClose`, so a market order sent on bar *k*'s close fills at the open of bar *k+1* (INFERRED from standard NT8 backtest fill behaviour, not checked in this session).

---

## Candidate #1 — Last-half-hour market intraday momentum, `η(r_ROD)` (Baltussen, Da, Lammers, Martens 2021)

### Source
- Baltussen, G., Da, Z., Lammers, S., Martens, M. (2021). "Hedging demand and market intraday momentum." *Journal of Financial Economics* 142, 377–403. DOI 10.1016/j.jfineco.2021.04.029 (OBSERVED, OpenAlex + Semantic Scholar output).
- **Full text fetched** from co-author Zhi Da's Notre Dame page (linked as `href="intramom.pdf">Hedging Demand and Market Intraday Momentum` on `https://www3.nd.edu/~zda/`). OBSERVED:
  ```
  balt-nd 200 application/pdf 2397917
  .../baltussen-nd/intramom.pdf: PDF document, version 1.7, 23 pages
  623ba82490acd01546f568cf582de5a9b45dfbd97731cd548cb119d7a0acec57  .../baltussen-nd/intramom.pdf
  ```
  The file is the published JFE typeset version (header line `Journal of Financial Economics 142 (2021) 377–403`, OBSERVED). The Erasmus repository copy returned `balt 403 text/html` (an HTML page, not the paper). OBSERVED.
- Page cites: journal page = PDF page + 376. I checked this against the printed footers for PDF pages 5, 9, 10 and 11, which show 381, 385, 386 and 387 (OBSERVED). For PDF pages 19 and 21 (appendix tables) I give the PDF page only. The PDF has 23 pages but the article spans 27 journal pages, so the offset may break somewhere in the appendix. Journal pages for those two are UNVERIFIED.

### Rule set (as published; all OBSERVED unless marked)
1. Market hours for equity index futures = the underlying cash market's hours. For NQ that is **09:30–16:00** ET. Table 1 row: `NASDAQ 100 futures∗   NQ   9:30 - 16:00` (p. 383, PDF p. 7). Method text: "we select the observations of the S&P E-Mini between 09:30 and 16:00" (p. 381).
2. Signal: the rest-of-day return `r_ROD,t = P_{c−30,t} / P_{c,t−1} − 1`, "the return of buying at previous day's close and selling 30 minutes before today's close" (Eq. 2, p. 381). For NQ, c = 16:00, so the signal is the price at **15:30** divided by **yesterday's 16:00 close**, minus 1.
3. Position: "If the predictor return is positive, we will earn the last half-hour return, r_LH, otherwise we will earn −r_LH" (Eq. 12, p. 385). Long if `r_ROD > 0`. Short otherwise, **which includes r_ROD = 0** (Eq. 12's "otherwise"; INFERRED from the equation's wording).
4. Holding window: the last half hour (LH), 15:30 → 16:00 close. You are flat at the close every day, and there is one trade per day, every day.
5. No stop, no target, no sizing rule. The signal is a sign only, with 1 unit per day (INFERRED: Eq. 12 is unit exposure).
6. Data hygiene: the paper removes "all days in which the exchange closed earlier (such as Memorial Day)" and days with total volume under 100 contracts (p. 381). It rolls to the next contract "when the daily tick volume of the next back-month contract exceeds the current contract" (p. 381).
7. Tunable inputs: **none**.
8. Published variants (Table 6, p. 387): `η(r_ONFH)` uses the first-half-hour return (prev close → 10:00) as the signal, which is the Gao et al. 2018 predictor. `η(r_ONFH, r_ROD)` trades only when both returns have the same sign and "does not trade when signs differ".

### Reported results (verbatim, cited)
- NQ sample: Table A1 row `NASDAQ 100 futures∗   NQ   1996-04-12   2020-05-01   6017   09:30–16:00   USA` (PDF p. 19). OBSERVED.
- NQ-specific predictive regression, Table B1 Panel A (PDF p. 21). This is the `r_LH` regression, not a P&L. OBSERVED row: `NQ  7.45∗∗∗  2.01  1.83∗∗∗  6.95∗∗∗  5.14∗∗∗  11.54∗∗∗  4.31  3.58∗∗∗  6.36∗∗∗  4.10  3.76∗∗∗`. Per the column header, the last three are β_ROD = 6.36 (1% significant), R² = 4.10%, R²_OOS = 3.76%. INFERRED column mapping from the header line `βONFH R2(%) R2OOS(%) βrONFH βM βSLH R2(%) R2OOS(%) βROD R2(%) R2OOS(%)`.
- Trading results are reported only as a 1/N **portfolio of equity-index futures**, not for NQ alone. Table 6 Panel A (p. 387), verbatim row: `η (rROD )   6.86   3.96   1.73   0.55`. Columns: annualized average return %, std dev %, Sharpe ratio, success rate. For comparison: `Always Long   0.44   4.20   0.11   0.53` and `η (rONF H , rROD )   5.47   3.42   1.60   0.61`. "Samples range from December 1974 to May 2020." OBSERVED.
- **Gross of costs.** "Note that we do not consider transaction costs. Given that trading on market intraday momentum requires frequent rebalancing, the strategy as presented might not be exploitable to many investors after accounting for transaction costs" (p. 386). Also: "exploiting the effect in the S&P 500 futures yields a positive net Sharpe ratio when we assume transaction cost equal to a tick" (p. 386). OBSERVED.
- Supporting abstract-only seed: Gao, Han, Li, Zhou (2018), "Market intraday momentum," *JFE*, DOI 10.1016/j.jfineco.2018.05.009. Abstract via the Semantic Scholar API (OBSERVED): "Based on high frequency data of the S&P 500 ETF from 1993-2013, we document an intraday momentum pattern: the first half-hour return on the market predicts the last half-hour return." **Full text was not obtained.** Scholar's only `[PDF]` link was `papers.ssrn.com/sol3/Delivery.cfm?abstractid=2440866` (SSRN, not retried) and Wayback returned 429. Its rule set is UNVERIFIED except as Baltussen restates it in variant `η(r_ONFH)`.

### Mapping to NQ 1-min RTH
- Yesterday's close `P_{c,t−1}` = Close of yesterday's **16:00-stamped** bar. It is in the RTH series, so no ETH data is needed. INFERRED.
- Decision bar = the **15:30-stamped** bar (covers 15:29–15:30). `r_ROD = Close[15:30 bar] / Close[prev 16:00 bar] − 1`. INFERRED.
- Entry: market order on the 15:30 bar's close. It fills at the open of the 15:31-stamped bar, which is about the 15:30 price. INFERRED.
- Exit: the paper earns through the 16:00 close. With OnBarClose, an exit sent on the 16:00 bar's close fills **after** RTH. So the exit must go out on the **15:59-stamped** bar's close (fill at the 16:00 bar open), or use NT's exit-on-session-close. Which one is an Amear question (Q1.2). INFERRED.
- Holiday filter: the paper drops early-close days. PROPOSED default: skip early-close sessions. This is an Amear question (Q1.3).
- Which 1-min price the paper uses for P (open or close of the minute) is SPEC-SILENT. The paper says only "one-minute intervals containing the corresponding open price, close price and trade volume" (p. 381).

### Open questions → NEEDS AMEAR (Q1.x)

### Score row
| a completeness | b data fit | c independence | d evidence | e simplicity | total |
|---|---|---|---|---|---|
| 3 | 3 | 3 | 3 | 3 | **15** |
- (a) 3: the signal, threshold (sign), entry time, exit time and hours are all stated. There are no parameters to tune.
- (b) 3: it needs only yesterday's RTH 16:00 close and today's 15:30 bar.
- (c) 3: the signal is the sign of the full prev-close→15:30 return, with one fixed entry at 15:30. There is no band around the open, no half-hour checkpoint ladder and no VWAP exit, so it is a different signal family from Noise-Area. Caveat: both are momentum (INFERRED).
- (d) 3: NQ-specific regression evidence over 1996–2020, plus the equity-futures portfolio with Sharpe 1.73. Caveat: gross of costs, and there is no NQ-alone P&L.
- (e) 3: one decision bar, market orders, zero inputs.

---

## Candidate #2 — Timely Opening Range Breakout, TORB (Tsai, Wu, Syu, Lei, Wu, Ho, Wang 2019)

### Source
- Tsai, Y.-C., Wu, M.-E., Syu, J.-H., Lei, C.-L., Wu, C.-S., Ho, J.-M., Wang, C.-J. (2019). "Assessing the Profitability of Timely Opening Range Breakout on Index Futures Markets." *IEEE Access* 7, 32061–32071 (the page range is INFERRED from the printed footers 32063–32068, and the first and last page numbers are UNVERIFIED). DOI 10.1109/ACCESS.2019.2899177 (OBSERVED in the text header).
- **Full text fetched** (open access) from `https://ieeexplore.ieee.org/ielx7/6287639/8600701/08641124.pdf`. OBSERVED:
  ```
  ieee 200 application/pdf 8930514
  .../ieee-orb/paper.pdf: PDF document, version 1.5, 6 pages
  058bd5e8b4a21eb312b2447f7ff04c9aacc764c6530580c45a120bcb8f89e46a  .../ieee-orb/paper.pdf
  ```
  `file` reports 6 pages, but pdftotext produced form-feed pages up to at least 11, and the footers run 32063–32068. So `file`'s page count is not reliable here (OBSERVED discrepancy). **All results tables (Tables 1–13) are images.** pdftotext returned only their captions, so the per-market tables were not read (OBSERVED).
- Page cites: journal page = PDF page + 32060. I checked this on PDF page 3 (footer 32063) and PDF page 7 (footer 32067). OBSERVED.

### Rule set
1. Data: one-minute intraday index futures, including E-mini NASDAQ 100, "from 2001/1/2 to 2013/12/2" (p. 32064, OBSERVED).
2. Active hours: aligned with the underlying stock market's open and close. Text: "we align the active hours of an index futures market with its underlying stock market" (abstract, p. 32061). The Fig. 4 caption reports the E-mini NASDAQ volatility peak at "8:30 (the opening time of the underlying market)". The paper's clock is US Central, so 8:30–15:00 CT = **09:30–16:00 ET**. The clock conversion is INFERRED; the 8:30/15:00 text is OBSERVED.
3. Times: "The beginning of observed period, denoted as t_b, is set to the beginning of the active hours, and the time point of the closing position, denoted as t_e is set to the end of the active hours; the end of the observed period is the probe time t_p" (p. 32064, OBSERVED).
4. Signals (Eqs. 3–4, p. 32064, OBSERVED): `P_t′,d > max(P_tb,d, …, P_tp,d) ⇒ Buy` and `P_t′,d < min(P_tb,d, …, P_tp,d) ⇒ Sell`, where `t_p < t′ < t_e`.
5. Exit: "If there is a trading signal on a day, the position closes at t_e on that day" (p. 32064, OBSERVED). There is no stop and no target (SPEC-SILENT, meaning none is described).
6. Price P: the paper defines P_t as "the close price in the one-minute interval t on day d" when building PMVR (p. 32063, line 172 of the text). That Eqs. 3–4 use the same close price is INFERRED.
7. The probe time is the single tunable. For NQ: "The best strategies for the E-mini DJIA, E-mini S&P 500, and E-mini NASDAQ are all with short probe times (4, 1, and 1 minutes, respectively)" (p. 32068, OBSERVED). **t_p = 1 minute for NASDAQ.** This "best" value was picked in-sample from a sweep, which is a data-snooping caveat (INFERRED).
8. Costs: "assume an overall transaction cost of 0.01% (per trade)" (footnote 3, p. 32067, OBSERVED).

### Reported results (verbatim, cited)
- "the proposed strategy achieves over 8% annual returns with p-values less than 3% in all of the five markets" (abstract, p. 32061, OBSERVED).
- NASDAQ: "the annual return 5.58% is much less than the annual return 17.51% of the best TORB strategy on the same market" (p. 32069, OBSERVED). Here 5.58% is the classical TRB benchmark.
- Sub-periods: "experiments in sub-periods from 2003 to 2007 and …" (text line 96; p. 32061 or 32062, exact page UNVERIFIED; OBSERVED fragment). The NASDAQ sub-period numbers are in image tables 7–8 and are **UNVERIFIED**.

### Mapping to NQ 1-min RTH
- t_b = the 09:31-stamped bar (the first RTH minute). With t_p = 1 minute, the observed set is either {Close[09:31]} or {Close[09:31], Close[09:32]}. The paper does not pin which (SPEC-SILENT, Q2.1).
- Signal scan: from the first bar after t_p, check each bar close against the max/min of the observed closes. On the first breach, send a market order on that bar's close, which fills at the next bar's open. INFERRED.
- Exit at t_e = 16:00. With OnBarClose this has the same issue as candidate #1: send the exit on the 15:59-stamped bar or use exit-on-session-close (Q2.3).
- Whether a second, opposite signal reverses the position is SPEC-SILENT. The paper speaks of "a trading signal on a day", singular (Q2.2).

### Score row
| a | b | c | d | e | total |
|---|---|---|---|---|---|
| 2 | 3 | 2 | 2 | 3 | **12** |
- (a) 2: the equations and t_p are stated. The observed-set boundaries, reversal behaviour and whether the max uses closes or highs are not pinned.
- (b) 3: RTH 1-minute bars only.
- (c) 2: this is an opening-range breakout, an open-anchored momentum breakout like Noise-Area. But the range is fixed by the first minutes, with no volatility band, no half-hour checkpoints and no VWAP exit.
- (d) 2: NQ-specific over 2001–2013 with costs (17.51%/yr). But the result is the in-sample best of a sweep, and the tables are images I could not read.
- (e) 3: one input (t_p), market orders, exit at the close.

---

## Candidate #3 — 5-minute Opening Range Breakout on QQQ (Zarattini & Aziz 2023)

### Source
- Zarattini, C., Aziz, A. R. (2023). "Can Day Trading Really Be Profitable? Evidence of Sustainable Long-term Profits from Opening Range Breakout (ORB) Day Trading Strategy vs. Benchmark in the US Stock Market." SSRN working paper 4416622, DOI 10.2139/ssrn.4416622 (OBSERVED, Semantic Scholar output).
- **Abstract only. Full text NOT fetched.** It is only on SSRN, which is blocked from this Mac and was not retried. Scholar listed no other mirror, and Wayback returned 429. OBSERVED.
- **The rule set below is UNVERIFIED-from-secondary.** It comes from an independent replication README on GitHub, not from the paper. Fetched from `https://raw.githubusercontent.com/giovannibrusco/zarattini-2023-orb-qqq/HEAD/README.md`. OBSERVED:
  ```
  readme 200 text/plain; charset=utf-8 13751
  4f0ff1e00fdc3318f600a3c9441518544f3bfb567640ef8d865ab724d195480f  .../gh-brusco-readme/README.md
  ```

### Rule set (UNVERIFIED-from-secondary; README line numbers in brackets, all OBSERVED in the README)
1. Instrument and bars: "QQQ 5-minute bars, Jan 2016 → Feb 2023, $25,000 starting capital" [L75].
2. Opening range = the first 5-minute bar, 09:30–09:35 ET [L79].
3. Direction: a bullish first bar (close > open) → long, a bearish one → short, a doji → no trade [L79–81].
4. Entry "at 09:35 open" [L82, L84].
5. Stop: for a long, the 09:30 bar's low. For a short, the 09:30 bar's high [L82, L84].
6. Exit: "stop (−1R) · target (+10R) · or flat at session close" [L86].
7. Sizing: "position size = `min(1% equity / $R, 4 × equity / entry)`" [L90].
8. **ETH flag:** the README's *filtered* variant adds an "NQ 09:25 bar also bullish/bearish?" check [L79–80]. A 09:25 bar is pre-market, so this **needs ETH and is not in the RTH series**. The README labels it "(filtered variant only)" and says the repo "replicates Zarattini & Aziz (2023) … confirmed with NQ futures" [L22]. Whether the *paper's* headline rule includes this filter is **UNVERIFIED** (Q3.1).

### Reported results
- Abstract (Semantic Scholar, OBSERVED, verbatim): "the day trading portfolio produced an annualized alpha of 33% (net of commissions)"; "The resulting portfolio would have earned an outstanding return of 1,484% during the same period of 2016 to 2023". The abstract has no page number (SSRN abstract page).
- Secondary only (README L31, OBSERVED; the paper's own figures are UNVERIFIED): "1,775 trades (paper: 1,795), Sharpe 1.06 (paper: 1.12), max DD 22% (paper: 22%)". Also: "net PnL crosses zero at ~2.2¢/share of entry slippage" [L32].
- Independent negative evidence on MNQ, a different ORB definition (arXiv 2605.04004v3, Mesfin 2026, full text, sha256 `d0bd26e4…a80`): the OR is "09:30–09:55 ET — the first six five-minute bars" [txt L197–198]. "the Opening Range Breakout long at a 15-bar hold (net +2.82 points, T = 0.88 on net returns)" [txt L24]. OBSERVED. This is not the Zarattini rule, but it is the nearest MNQ test of the ORB family.

### Mapping to NQ 1-min RTH
- The opening 5-minute bar = 1-min bars stamped 09:31–09:35. OR open = Open[09:31 bar], OR close = Close[09:35 bar], OR high/low = max High/min Low of those five bars. INFERRED.
- Decision on the close of the **09:35-stamped bar**. The market entry fills at the open of the 09:36-stamped bar, which equals the "09:35 open". INFERRED.
- Stop and target: these are price levels. With OnBarClose and market orders only, a stop can be checked only on bar closes, which differs from the paper's (presumably) intrabar stop. Alternatively NT's stop orders could be used. Amear question (Q3.2). INFERRED.
- Session-close exit: same 15:59 vs session-close issue as #1 (Q3.3).

### Score row
| a | b | c | d | e | total |
|---|---|---|---|---|---|
| 2 | 2 | 2 | 2 | 2 | **10** |
- (a) 2: the secondary source states every parameter, but none is verified against the paper.
- (b) 2: the unfiltered rule fits RTH bars. The NQ 09:25 filter needs ETH, and whether the paper uses it is unknown.
- (c) 2: an opening-range breakout, an open-anchored momentum breakout, but with no volatility band, no half-hour checkpoints and no VWAP exits.
- (d) 2: QQQ 2016–2023, from the abstract plus secondary stats. The README reports the edge breaks even at ~2.2¢/share slippage.
- (e) 2: stop + 10R target + session exit don't fit "market orders only, OnBarClose" cleanly. The 1% risk sizing is irrelevant for fixed-contract NQ but is part of the published rule.

---

## Ranking

| Rank | Candidate | a | b | c | d | e | Total | Full text? |
|---|---|---|---|---|---|---|---|---|
| 1 | Baltussen et al. 2021, last-half-hour momentum `η(r_ROD)` | 3 | 3 | 3 | 3 | 3 | 15 | Yes (published PDF, author site) |
| 2 | Tsai et al. 2019, TORB, t_p = 1 min | 2 | 3 | 2 | 2 | 3 | 12 | Yes (IEEE OA), but tables are images |
| 3 | Zarattini & Aziz 2023, 5-min ORB on QQQ | 2 | 2 | 2 | 2 | 2 | 10 | No: abstract + GitHub replication README |

**Pick = #1 (Baltussen et al. 2021 `η(r_ROD)`).** Reasons:
1. It is the only candidate whose full rule set I read in the primary source, and it has zero free parameters.
2. It has NQ-specific published evidence over 1996-04-12 → 2020-05-01 (Tables A1/B1).
3. It is the most distinct from Noise-Area: one fixed decision at 15:30 using the full prev-close→15:30 return, no band and no intraday checkpoints.
4. It is the simplest NinjaScript build: one decision bar, one market entry, one market exit, no inputs.

Caveats that go with the pick: the published P&L is **gross** of costs and for an equity-futures *portfolio*, not NQ alone. It also trades every day (about 252 round-trips a year), so the D-2026-10-30-A cost model will matter a lot.

Note for Amear: #2 and #3 are both opening-range breakouts, so they are one signal family. If you want three distinct families, a fourth candidate would have to be researched (for example, an opening-gap fade). I did not research one in this run.

---

## NEEDS AMEAR

Unanswered. None of these is decided here. Values marked PROPOSED are only defaults offered for review.

**Candidate #1 (Baltussen `η(r_ROD)`)**
- Q1.1: Which 1-min price is the 15:30 reference: Close of the 15:30-stamped bar, or Open of the 15:31-stamped bar? The paper's minute-price choice is SPEC-SILENT. PROPOSED default: Close[15:30 bar].
- Q1.2: Exit mechanics: market exit sent on the 15:59-stamped bar's close (fills at the 16:00 bar open), or NT exit-on-session-close? The paper earns through the 16:00 close.
- Q1.3: Skip early-close sessions as the paper does? PROPOSED default: skip them.
- Q1.4: If r_ROD = 0 exactly, go short (per Eq. 12 "otherwise") or stand aside?
- Q1.5: Build the base `η(r_ROD)` only, or also the `η(r_ONFH, r_ROD)` same-sign variant (Table 6: SR 1.60 vs 1.73, success 0.61 vs 0.55)?
- Q1.6: Roll rule: does the continuous NQ series' roll convention matter vs the paper's "volume of next back-month exceeds current" rule?
- Q1.7: The first day of the series has no previous 16:00 close. Skip it? (INFERRED necessity.)

**Candidate #2 (TORB)**
- Q2.1: With t_p = 1 minute, is the observed set {09:31 close} or {09:31, 09:32 closes}?
- Q2.2: After the first signal, can an opposite breach reverse the position, or is it one trade per day?
- Q2.3: Exit at 16:00: same mechanics question as Q1.2.
- Q2.4: Use closes (as INFERRED from the PMVR definition) or highs/lows for the range and the breach test?
- Q2.5: Accept t_p = 1 (the in-sample best of the paper's sweep) as fixed, or treat t_p as the one tunable?

**Candidate #3 (Zarattini & Aziz ORB)**
- Q3.1: Does the paper's headline rule include the NQ 09:25 pre-market filter? If it does, the rule needs ETH data, which is out of scope. Needs the full text (SSRN is blocked here). Can Amear supply the PDF?
- Q3.2: Stop/target execution: check on bar close with market orders (deviates from the paper), or allow NT stop/limit orders?
- Q3.3: Session-close exit: same as Q1.2.
- Q3.4: Sizing: fixed 1 contract, or emulate "1% equity / R" risk sizing?
- Q3.5: Doji definition: is it close == open exactly at tick resolution? SPEC-SILENT in the secondary source.
