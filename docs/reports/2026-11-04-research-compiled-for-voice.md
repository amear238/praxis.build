# Research compiled for the voice session — tick data, comparable builds, proof of concept (2026-11-04)

**From:** Code (Mac), praxis-master. **For:** Amear, to discuss in the Claude app voice project.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Status of the three reports.** All three passed independent audit, but only after each one failed once and was corrected. Every correction was appended, and none of the original text was overwritten.
- A, tick data: `docs/reports/2026-11-04-tick-data-sources.md`. Passed on re-audit; the original failed on three citation gaps.
- B, comparable builds: `docs/reports/2026-11-04-comparable-builds.md`. Passed on re-audit. The original had three blocking problems: one wrong claim, a dozen claims with no pasted lines, and use of your GitHub login.
- C, proof of concept: `docs/reports/2026-11-04-proof-of-concept-standard.md`. Passed on re-audit; the original had some figures with no output behind them. The auditor re-ran C's statistics with its own script and got the same numbers.

Nothing was bought, signed up for, imported or run. No code changed. The figures below are Claude's arithmetic on your 11-01 trade list, which the auditors checked independently. They are not new backtests.

---

## 1. The short version

1. **Your baseline edge is real enough to beat zero but not strong enough to call proven.** On 1,190 trades the per-trade t-statistic is 2.63. The 95% range for profit factor is about 1.08 to 1.54. It can't yet be told apart from a Sharpe of 1.0.
2. **The edge is concentrated, and the recent period is weak.** Take out the best 20 of 1,190 trades and PF drops from 1.29 to 1.02. PF by exit year is 1.11 for 2025 and 0.97 for 2026. The last two half-years are both negative. The paper's own authors show 2025 (Jan–Aug) at +1.0%, against 24–37% a year in 2020–2024.
3. **For the strategy as coded today, tick data is a refinement, not a prerequisite.** Every order is a market order decided on a bar close at HH:00 or HH:30. Ticks could change fill prices and the slippage cap. They can't change which trades happen. This is inferred from the code and NT's own fill document; no High run exists to test it. Reports A and C reached it independently.
4. **That flips the moment a resting stop exists.** Two places could add one: circuit breakers built as resting price stops, or the Phase 3 spec's walk-forward, which optimises a stop-ATR multiplier on High/1-tick. Whether the breakers are resting stops is not defined yet.
5. **The cheapest full-window tick data with a published price is Kibot.**
   - Kibot sells $580 one-time for a continuous NQ file, which would need new code to split per contract. The per-contract package is $1,100. You keep the data either way. Licence: "internal use only".
   - Portara's $695, which you declined, sits between those two.
   - Massive (formerly Polygon) is $199 a month. You must delete the data within 30 days of stopping, and the licence is "personal, non-business, non-commercial".
6. **Every NinjaTrader-native tick route needs a new connection.** That covers Rithmic, Kinetick, IQFeed and NT's own feed. D-071 currently allows only the Simulated Data Feed. Flagged, not acted on.
7. **No public project is ready to drop in.** 24 GitHub repos were read at file level, and none is adoptable as-is. 16 have patterns or reference code worth adapting, if you approve the licences. Nobody publishes a Standard-vs-High fill comparison, and nobody checks whether a forward test reproduces its backtest.
8. **Two problems no data purchase fixes:**
   - The 1-minute file has 33 weekdays with no regular-session data that aren't NYSE holidays. If the 2025-01-09 national day of mourning closure counts, it's 32; that closure is unverified.
   - Early-close days exit at 12:15, about an hour before the file's last bar.

---

## 2. Brief C — what "proof of concept" could mean

**Where the numbers come from:** your baseline (BandOrVWAP, NQCONTROW, 2021-03 → 2026-07), its 11-01 trade CSV, and the 1-minute file. All of it is Claude's arithmetic. The auditor reproduced it independently.

- **Distinguishable from zero:** yes on most tests.
  - t = 2.63.
  - The chance the true Sharpe is above zero is about 99.9%.
  - The PF interval stays above 1.0 both ways it was tested: 1.08–1.54 treating trades as independent, and 1.12–1.46 resampling whole months.
- **Distinguishable from "good" (Sharpe 1.0):** no.
  - The chance the true Sharpe beats 1.0 is about 67%.
  - Proving that to normal confidence would take about 74 years of data at this edge.
- **Deflated Sharpe** (which corrects for how many variants were tried): it depends entirely on how many tries count. That is your call.
  - Counting 4 runs (R0–R3), it's 0.62.
  - Counting 2, it's 0.998.
  - Counting 100, it's essentially zero.
  - The literature's bar is 0.95.
- **Your Phase 3 gates against the literature:**
  - **≥ 250 OOS trades is looser than the statistics.** 250 trades at this edge give t = 1.2. You'd need about 660 trades for t = 2.
  - **OOS PF ≥ 1.30 is stricter than the baseline's own in-sample PF of 1.29.** Even if the edge is exactly real, a 250-trade sample passes it only about 47% of the time.
  - **Max DD ≤ 4% of equity has no equity base anywhere in the repo.** For scale, the baseline's max drawdown ($45,282, one contract) is about 30 times MFFU's $1,500 trailing drawdown. That is a fact, not a judgement.
  - **Sharpe ≥ 1.0 doesn't say daily or per-trade.**
  - **WFE ≥ 0.50 matches the one vendor rule of thumb found (TradeStation).** It means nothing without an optimisation step, and the baseline has none.
  - **Five of the six gates need walk-forward to evaluate**, and walk-forward waits on r8j.
- **A test you can run without buying anything** (T-a to T-d in report C §3) tells refinement from prerequisite:
  - **T-a.** Count resting-order fills in the judged version. Today there are zero.
  - **T-b.** Check that market fills match next-bar open ± slippage. Today 96.9% do, and the rest hit the bar's cap.
  - **T-c.** Measure break-even extra slippage. Today it's 16.6 ticks per side against the 2 modelled.
  - **T-d.** If there are brackets, count how often one 1-minute bar touches both levels. Under 1% means refinement. For example, a 20/20-point bracket comes out at 1.6%.
- **PROPOSED checklist** (report C, its own section, 12 items). Nothing in it is decided.
  - **Tier A, before buying data (P1–P9):**
    - the data is clean;
    - the trial count is fixed by you;
    - deflated Sharpe ≥ 0.95;
    - minimum backtest length is met (it is);
    - t ≥ 3 (now 2.63);
    - the month-block PF floor is above 1 (it is);
    - a cost stress at a slippage level you set;
    - the refinement test is run on the judged version;
    - a concentration check (barely passes at 1.02).
  - **Tier B, before forward trading (P10–P12):** walk-forward passes your gates; if optimised, overfitting probability < 0.05; then a forward test of at least 6 weeks or 25 trades spanning an FOMC day, an NFP day and a rollover.
  - P1 and P9 have no literature source; they are project-specific proposals.
- **Cost of being wrong, facts only.** On today's code, $695 of ticks would refine fill prices on a strategy whose break-even is 16.6 extra ticks per side. Each extra tick per side is worth $11,900 in total. A minute-data walk-forward needs no purchase. It does need r8j, your gate-set ruling, and your word on whether minute-data walk-forward is acceptable, since the spec names High/1-tick.

## 3. Brief A — tick data sources

| Source | Covers 2021-03 → 2026-07? | Price (published, read today) | Keep data? | Into NT8 |
|---|---|---|---|---|
| Kibot continuous | Yes, NQ from 2009 (end date inferred) | $580 one-time ($800 with bid/ask) | Yes; "internal use only" | New code to split per contract, then TickPrep |
| Portara/CQG | Yes, 2014 → | $695 (declined 11-03) | Not published | TickPrep plan exists |
| Kibot per-contract | Yes, contracts from April 2010 | $1,100 ($1,700 with bid/ask) | Yes | TickPrep-ready only if Kibot delivers NT format for the package (unconfirmed) |
| Massive Advanced | Probably (futures from 2017; NQ named; start for NQ inferred) | $199/month; 20% off annual | No, delete within 30 days of stopping; personal non-commercial | New code (API → NT text) |
| IQFeed | No, 180 days of ticks only (reaches ~May 2026 today; none of the window after ~Jan 2027) | ~$262 first month | n/a | Native, but needs a new connection |
| Kinetick / NT feed / Rithmic | Depth unknown | various | n/a | Native, but needs a new connection |
| Databento, TickData, CME DataMine, Barchart | Likely, unpriced | Not readable without login or quote | — | New code |
| FirstRate | No tick for NQ (1-minute bars only) | — | — | — |

- **Partial (last 12 months only):** no vendor publishes a 12-month NQ tick price.
- **Mixed High and Standard in one run:** NT8's help guide doesn't say. As documented it's one fill resolution per run, so this would mean two runs combined by hand.
- **1-second bars as a middle ground:** NT8 builds second bars from ticks, so they don't save buying ticks. No quantitative comparison was found.
- **Free forward collection:** NT's "record live data" needs a real feed, which means a new connection (D-071). The Simulated Data Feed is generated data.

## 4. Brief B — comparable builds

- **Noise-Area in NinjaScript:**
  - One public implementation exists (skizzunni/money, MNQ, 5-minute, no licence). It was being pushed to on the day it was read.
  - Its author reports native Strategy Analyzer runs matching his simulator on 86–92 of 97–98 trades. That is his report; we ran nothing.
  - Read-only reference unless he grants a licence.
- **Walk-forward from outside NT8:** eman007/cli-nt-bridge (MIT) drives NT8's own walk-forward mode. The author reports it on 8.1.8.2; on our 8.1.7.2 it's unverified. Installing it on the trading box is your call.
- **Rollover / back-adjust:** nothing replaces TickPrep. giovannibrusco's MIT Python `stitch()`, with its published ES roll table, could serve as an independent cross-check.
- **Patterns for the unbuilt breakers** (all MIT, all adaptable, none drop-in):
  - PropGuard: session reset, halt latch, reduce-only flatten. Off by default.
  - projectx-desk: persistent halt file; unreadable means halted.
  - deadman-guardian (NT8 add-on): day P&L = realized + unrealized − commissions. The owner reports sim use only.
  - cli-nt-bridge: stale-request rejection, plus an atomic file write (`.tmp` then move). Relevant to the n8n → file-drop path.
- **How others decide "worth forward-testing":** five repos write it down. One example is a fail-closed paper→real gate: ≥ 100 forward trades, PF ≥ 1.3. Another kills a strategy if in-sample ranking doesn't survive out-of-sample. None checks that a forward test reproduces its backtest within a tolerance.
- **Incompatible:** projects that bypass the NinjaScript strategy, such as ATI/OIF relays and direct Rithmic order routing, because in-strategy breakers wouldn't apply. Also an HTTP listener inside NT8 with no auth, and ratio-adjusted rollover libraries.

---

## 5. Decisions that are yours

Grouped; none is answered in the reports.

**Proof of concept (R-1104-3)**
1. Accept, edit or reject the PROPOSED checklist. Is Tier A alone the condition for buying data?
2. What counts as a "trial" for the deflated Sharpe: R0–R3, all variants ever, or the paper's own choices?
3. The Sharpe definition (daily or per-trade), and the equity base for the 4% drawdown gate, given MFFU's $1,500 trailing drawdown.
4. Fix the 33 missing sessions and the 12:15 early-close template before judging results, or accept them?
5. Does the $2.96 round turn include exchange, clearing and NFA fees? The export shows $0 for them.

**Design questions that decide whether ticks are needed**
6. Will the circuit breakers be resting price stops? If yes, ticks become a prerequisite.
7. Is a walk-forward on minute data acceptable, given the spec names High/1-tick with an optimised stop?

**Data and connections**
8. D-071: may any connection other than the Simulated Data Feed be opened to collect or backfill ticks?
9. Do Kibot's "internal use only" or Massive's "personal, non-commercial" licences fit trading an MFFU account?
10. May agents request vendor quotes that need an account or email? That would turn unknown prices into known ones.
11. Is CME's own wiki acceptable as a source, given that cmegroup.com blocks scraping?

**Repos**
12. Licences, as read-only reference, re-implementation, or asking the author. Third-party add-ons on the trading NT8 install. A second Rithmic connection for read-only cross-checks.
13. **Your GitHub login.** Research unit B's workers used your existing `gh` login (`amear238`) without your authorisation, under GET-only instructions. No write activity was found, but that can't be proven from the logs. What do you want done about the past use, and may it be used in future? The corrections used no login.

**Carried from earlier today**
14. The commit-gate change you approved is built and is being audited. Three questions from that unit are pending:
    - accept that anything running as your user can forge the harness files;
    - let auditors cite criteria by id;
    - keep the word-filter heuristic for "PASS".
15. r8j at P0, which you haven't confirmed. It blocks walk-forward and five of the six gates.

---

## 6. What we can't tell yet

- Whether NT8 High resolution actually changes these fills, since no High run exists.
- NQ-only Kibot price, Databento's real cost for this window, and TickData's and DataMine's prices, because each needs a quote or a login.
- Whether "Second" bars can be chosen as the High fill series. That's a two-minute look at the VM dropdown, with no run.
- Tick depth from Rithmic, Kinetick and NT's own feed.
