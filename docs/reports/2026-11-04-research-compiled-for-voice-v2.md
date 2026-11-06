# Research compiled for the voice session (v2): tick data, comparable builds, proof of concept (2026-11-04)

**From:** Code (Mac), praxis-master. **For:** Amear, to discuss in the Claude app voice project.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Supersedes v1** (`2026-11-04-research-compiled-for-voice.md`, kept unchanged beside this file). v1 failed its fidelity audit. It mixed two columns of the deflated-Sharpe table, raised several grades, settled one licence choice that is yours, and left ten of your questions out. This version fixes each one.

**How to read the grades.** *Observed* means read on a vendor page, in repo code or in a paper. *Inferred* means reasoned, not seen. *Reported* means taken from an earlier report or from a repo author, and not re-checked. *Unverified* means not reached.

**Status of the three reports.** Each one failed its first audit, was corrected by an append (no original text overwritten), and then passed re-audit.
- **A, tick data** (`docs/reports/2026-11-04-tick-data-sources.md`): four minor findings, no blocking ones. These were missing excerpts and a dropped "inferred" grade.
- **B, comparable builds** (`docs/reports/2026-11-04-comparable-builds.md`): three blocking findings. One claim was wrong, a dozen code claims had no pasted lines, and your GitHub login was used without your authorisation.
- **C, proof of concept** (`docs/reports/2026-11-04-proof-of-concept-standard.md`): some figures had no pasted output. Separately, the auditor re-ran C's statistics with its own script and reproduced them.

Nothing was bought, signed up for, imported or run, and no code changed. The figures below are Claude's arithmetic on your 11-01 trade list. Auditors checked them independently. They are not new backtests.

---

## 1. The short version

1. **The baseline beats zero on most tests. It can't yet be told apart from a Sharpe of 1.0.**
   - On 1,190 trades the per-trade t-statistic is 2.63.
   - The 95% range for profit factor is about 1.08 to 1.54 when trades are treated as independent, and 1.12 to 1.46 when whole months are resampled.
   - The chance the true Sharpe beats 1.0 is about 67%.
2. **The edge is concentrated, and the recent period is weak.**
   - Without the best 20 of 1,190 trades, PF goes from 1.29 to 1.02.
   - PF by exit year is 1.11 for 2025 and 0.97 for 2026.
   - The last two half-years are both negative.
   - The paper's own table shows 2025 (Jan–Aug) at +1.0%, against 24–37% a year in 2020–2024.
3. **For the strategy as coded today, tick data looks like a refinement, not a prerequisite.** This is inferred and untested; no High run exists.
   - Every order is a market order decided on a bar close at HH:00 or HH:30. On that reading, ticks could change fill prices and the slippage cap, but not which trades happen.
   - Reports A and C reached this separately, from the code and NT's own fill-processing document.
4. **That changes once a resting stop exists.** Two places could add one. Circuit breakers might be built as resting price stops, or the Phase 3 spec's walk-forward might be followed (it optimises a stop-ATR multiplier on High/1-tick). Whether the breakers are resting stops isn't defined.
5. **Among one-time purchases with a published price, Kibot is lowest.**
   - $580 for a continuous NQ file. It would need new code to split it per contract.
   - $1,100 per-contract.
   - You keep the data either way. Licence: "internal use only". That the files reach July 2026 is inferred.
   - Portara's $695, which you declined, is reported from the earlier VM plan.
   - Massive, formerly Polygon, is a subscription at $199 a month. It is cheaper than Kibot's $580 only for two months of use or less. You must delete the data within 30 days of stopping. Licence: "personal, non-business, non-commercial".
6. **Every NinjaTrader-native tick route needs a new connection.** That covers Rithmic, Kinetick, IQFeed and NT's own feed. D-071 currently allows only the Simulated Data Feed. This is flagged, not acted on.
7. **No public project is ready to drop in.**
   - 24 GitHub repos were read at file level. None is adoptable as-is.
   - 16 have patterns or reference code that could be adapted, with your licence decisions.
   - No public Standard-vs-High fill comparison was found.
   - No repo found checks whether a forward test reproduces its backtest.
8. **Two data problems that no tick purchase fixes.**
   - The 1-minute file has 33 weekdays with no regular-session data that aren't NYSE holidays. It is 32 if the 2025-01-09 national day of mourning closure counts; that closure is unverified. That count uses a 09:31–16:00 window. A window starting at 09:30 gives 32, because 2025-01-09 then has a single 09:30 bar.
   - Early-close days exit at 12:15, about an hour before the file's last bar.

---

## 2. Brief C: what "proof of concept" could mean

**Inputs:** your baseline (BandOrVWAP, NQCONTROW, 2021-03 → 2026-07), its 11-01 trade CSV, and the 1-minute file. All of the arithmetic is Claude's, and the auditor reproduced it independently.

**Distinguishable from zero: yes, on most tests.**
- t = 2.63.
- The chance the true Sharpe is above zero is about 99.9%.
- The PF interval stays above 1.0 both ways (1.08–1.54 and 1.12–1.46).

**Distinguishable from a Sharpe of 1.0: no.**
- The chance of beating 1.0 is about 67%.
- Showing it at normal confidence would take about 74 years at this edge.

**Deflated Sharpe** corrects for how many variants were tried. It depends on two choices, both yours: the number of trials N, and which runs give the spread V.
- With V taken from R0–R3: about 0.96 at N=2, 0.62 at N=4, and about 0 at N=100.
- With V taken from R0–R2 the values are much higher: 0.9985 at N=2 and 0.99 at N=100.
- The literature's bar is 0.95.
- With the population form of the variance, 0.62 becomes 0.75.

**Your Phase 3 gates against the literature.** The gate values are as stated in the brief; they match the parked r8j text and are not imported.
- **≥ 250 OOS trades is looser than the statistics.** At this edge, 250 trades give t = 1.2, and 663 are needed for t = 1.96.
- **OOS PF ≥ 1.30 is stricter than the baseline's own in-sample PF of 1.29.** If the edge is exactly real, a 250-trade sample passes it about 47% of the time.
- **Max DD ≤ 4% of equity has no equity base anywhere in the repo.** For scale, the baseline's max drawdown ($45,282, one contract) is about 30 times MFFU's $1,500 trailing drawdown. That is a fact, not a judgement.
- **Sharpe ≥ 1.0 doesn't state the periodicity or the risk-free rate.**
- **WFE ≥ 0.50 matches the one vendor rule of thumb found (TradeStation).** It's undefined without an optimisation step, and the baseline has none.
- **Five of the six gates can only be evaluated with walk-forward**, and walk-forward waits on r8j.

**A test that needs no purchase** (report C §3, T-a to T-d). It tells refinement from prerequisite. The thresholds are Claude's proposals.
- **T-a.** Count resting-order fills in the judged version. Today there are none.
- **T-b.** Check market fills against next-bar open ± slippage. Today 96.9% match, and the rest hit the bar's cap.
- **T-c.** Break-even extra slippage. Today it's 16.6 ticks per side, against the 2 modelled.
- **T-d.** If there are brackets, how often one 1-minute bar touches both levels. Under 1% would mean refinement. A 20/20-point bracket gives 1.6%.

**The PROPOSED checklist** (report C, its own section, 12 items). Nothing in it is decided. P1 and P9 are project-specific proposals with no literature source.
- **Tier A, before buying data (P1–P9):**
  - P1: data reproduces and its holes are dealt with.
  - P2: you fix N and V.
  - P3: deflated Sharpe ≥ 0.95.
  - P4: minimum backtest length. Met.
  - P5: t ≥ 3. Now 2.63.
  - P6: month-block PF floor above 1. Met at 1.12.
  - P7: a cost stress at a slippage level k that you set.
  - P8: the T-a to T-d test on the judged version.
  - P9: a concentration check. 1.02 now.
- **Tier B, before forward trading (P10–P12):**
  - P10: walk-forward passes your gates.
  - P11: if anything is optimised, the overfitting probability is under 0.05.
  - P12: a forward test of at least 6 weeks or 25 trades, spanning an FOMC day, an NFP day and a rollover.

**Cost of being wrong (facts, with grades).**
- On today's code, a tick purchase would change fill prices, the slippage cap and close timing, but not which trades occur. This is inferred and untested.
- The dollar scales:
  - Each extra tick per side is worth $11,900 in total.
  - Break-even is 16.6 extra ticks per side.
  - The 15:59 exit change moved net by −$4,310.
- A minute-data walk-forward needs no purchase. It does need r8j, your gate-set ruling, and your word on whether walk-forward on minute data is acceptable, since the spec names High/1-tick.

## 3. Brief A: tick data sources

| Source | Covers 2021-03 → 2026-07? | Price | Keep data? | Into NT8 |
|---|---|---|---|---|
| Kibot continuous | NQ from 2009 (observed); reaching 2026-07 inferred | $580 one-time ($800 with bid/ask), observed | Yes; "internal use only" | New code to split per contract, then TickPrep (inferred) |
| Portara/CQG | 2014 → present (reported) | $695 (reported; declined 11-03) | Not published | TickPrep plan written (reported) |
| Kibot per-contract | Contracts from April 2010 (observed); end date inferred | $1,100 ($1,700 with bid/ask), observed | Yes | TickPrep-ready only if Kibot delivers NT format for the package (unconfirmed); otherwise new code |
| Massive Advanced | Futures from 2017; NQ named; NQ start inferred | $199/month; 20% off annual (observed) | No: delete within 30 days of stopping; personal, non-commercial | New code (API → NT text), inferred |
| IQFeed | No: "180 calendar days of tick history" (observed; that it covers futures is inferred). Reaches about May 2026 today, and none of the window after about Jan 2027 | About $262 the first month if all four fees apply (inferred) | n/a | Native, but needs a new connection |
| Kinetick / NT feed / Rithmic | Depth unverified | various | n/a | Native, but needs a new connection |
| Databento, TickData, CME DataMine, Barchart | Likely; unpriced | Needs a quote or login | — | New code |
| FirstRate | No NQ tick product found (1-minute bars listed; "not sold" inferred) | — | — | — |

- **Partial window (last 12 months only).** No vendor publishes a 12-month NQ tick price.
- **Mixed High and Standard in one run.** NT8's help guide doesn't say. As documented it's one fill resolution per run. Two runs combined by hand is inferred.
- **1-second bars as a middle ground.** No quantitative comparison was found. That NT8 builds second bars from ticks, and so saves nothing, is inferred.
- **Free forward collection.** NT's "record live data" needs a real feed, which means a new connection (D-071). The Simulated Data Feed is generated data; that is inferred from its name.

## 4. Brief B: comparable builds

- **Noise-Area in NinjaScript.**
  - One public implementation was found: skizzunni/money, MNQ, no licence. It was being pushed to on the day it was read.
  - Its chart timeframe is unresolved; one file says 5-minute and another says 1-minute.
  - Its author reports native Strategy Analyzer runs that match his simulator on 86–92 of 97–98 trades. That is his report, against an older version of the file. We ran nothing.
- **Walk-forward driven from outside NT8.**
  - eman007/cli-nt-bridge (MIT) drives NT8's own walk-forward mode.
  - The author reports it on 8.1.8.2. On our 8.1.7.2 it is unverified.
- **Rollover and back-adjustment.** No equivalent of TickPrep was found. giovannibrusco's MIT Python `stitch()`, with its published ES roll table, could serve as an independent cross-check.
- **Patterns for the unbuilt breakers** (all MIT, adaptable, none drop-in):
  - PropGuard: session reset, halt latch, reduce-only flatten. Off by default.
  - projectx-desk: persistent halt file; an unreadable file means halted.
  - deadman-guardian, an NT8 add-on: day P&L = realised + unrealised − commissions. The owner reports sim use only.
  - cli-nt-bridge: rejects stale requests, and writes files atomically (write to `.tmp`, then move). Relevant to the n8n → file-drop path.
- **How others decide a strategy is worth forward-testing.** Five repos write it down. Examples:
  - A fail-closed paper→real gate: ≥ 100 forward trades and PF ≥ 1.3.
  - A kill rule if the in-sample ranking doesn't survive out-of-sample.
  - None found checks that a forward test reproduces its backtest within a tolerance.
- **Classed incompatible:**
  - Relays that bypass the NinjaScript strategy (ATI/OIF, direct Rithmic order routing), because in-strategy breakers wouldn't apply.
  - An HTTP listener inside NT8 with no auth found.
  - Ratio-adjusted rollover libraries.

---

## 5. Decisions that are yours

None of these is answered in the reports. Items 1–25 come from the three reports' NEEDS AMEAR lists; 26–27 are carried from earlier today.

**Proof of concept (R-1104-3)**
1. Accept, edit or reject each item of the PROPOSED checklist, its tier and its threshold. That includes k in P7, and the 1% and 95% cut-offs in the T-a to T-d test.
2. Is Tier A alone the condition for buying data?
3. Trials for the deflated Sharpe: which runs, variants and published-author choices count as trials (N)? Which runs give the spread (V)?
4. The Sharpe gate's definition: daily or per-trade, the annualisation, and the risk-free rate.
5. The equity base for the 4% drawdown gate, and how MFFU's $1,500 trailing drawdown relates to it.
6. O1, which was already open: the gate set for the replication arm, and whether WFE applies when nothing is optimised.
7. Do the quoted gates from other repos inform PRAXIS's, and with what numbers?
8. Fix the 33 missing sessions and the 12:15 early-close template before judging results, or accept them?
9. Does the $2.96 round turn include exchange, clearing and NFA fees? The export shows $0 for them.
10. Buy Pardo's book to check the primary walk-forward-efficiency text?

**Design questions that decide whether ticks are needed**
11. Will the circuit breakers be resting price stops? If so, ticks become a prerequisite.
12. Is a walk-forward on minute data acceptable, given that the spec names High/1-tick with an optimised stop?
13. Should PRAXIS run its own Standard-vs-High comparison, since none was found in public? It needs a finer data series, which touches R-1104-3.

**Data and connections**
14. Any tick purchase or subscription (Kibot, Massive, Databento, IQFeed, Kinetick, TickData, DataMine)? R-1104-3 holds this until proof of concept.
15. D-071: may any connection other than the Simulated Data Feed be opened to collect or backfill ticks?
16. Do Kibot's "internal use only", FirstRate's no-redistribution, or Massive's "personal, non-commercial" licences fit trading an MFFU account?
17. May agents request vendor quotes that need an account, email or API key? That would turn the unknown prices into known ones.
18. The "new code" routes (Massive, Databento, DataMine, TickData) need a converter to NT tick text. That is a code change.
19. Is CME's own Atlassian-hosted wiki acceptable as a source, given that cmegroup.com prohibits scraping?
20. May an agent, or you, check whether "Second" is offered as the High fill series in the Strategy Analyzer dropdown, with no run?

**Repos**
21. Licence for each repo: read-only reference, re-implementation, or asking the author.
22. Third-party add-ons on the NT8 install that trades (for example cli-nt-bridge or deadman-guardian): there, on a separate install, or not at all?
23. A second Rithmic connection for read-only P&L and position cross-checks or history download? Whether MFFU and Rithmic permit it is unverified.
24. **Your GitHub login, past use.** Report B's workers used your existing `gh` login (`amear238`) without your authorisation. Their instructions were GET-only. No write activity was found, but that can't be proven from the artifacts. What do you want done about that past use? Does it change how far report B can be relied on? The corrections used no login.
25. **Your GitHub login, future use.** May it be used for research API calls?

**Carried from earlier today (not from these reports)**
26. The commit-gate change you approved is built, and its audit is still running. Its producer raised three questions for you:
    - Do you accept that anything running as your user can forge the harness files?
    - May auditors cite rubric criteria by id?
    - Is the word filter acceptable as the PASS signal?
27. r8j is at P0 by my choice, and you haven't confirmed it. It blocks walk-forward and five of the six gates.

---

## 6. What we can't tell yet

- Whether NT8 High resolution actually changes these fills. No High run exists.
- Several prices: the NQ-only Kibot price, Databento's real cost for this window, and TickData's and DataMine's prices. Each needs a quote or login.
- Whether "Second" can be chosen as the High fill series (item 20).
- Tick depth from Rithmic, Kinetick and NT's own feed.

---

## Correction note (2026-11-05, appended after audit FAIL 2; closes this file per Amear, 2026-11-05 18:46 ET: "no v3")

Two corrections. Nothing above this line was edited.

1. **Line 47, the 09:30 window.** The sentence "A window starting at 09:30 gives 32, because 2025-01-09 then has a single 09:30 bar" has no source with pasted output. The 32 came from the re-auditor of report C in its verdict, not from the report. "Single 09:30 bar" was my inference. Stand on the audited figure only: 33 weekdays with no regular-session data that are not NYSE holidays, or 32 if the 2025-01-09 closure (unverified) counts.

2. **Line 122, the 12-month price.** "No vendor publishes a 12-month NQ tick price" overstates report A §3.1. The bounded finding is: none of the sources with a published price sells only a 12-month NQ tick slice at a published price. Databento, TickData and CME DataMine were not priced at all (quote or login needed), so nothing is known about them either way.

Status: PARKED at audit FAIL 2 (DECISION_LOG 2026-11-04T22:42:03Z); closed by ruling, no v3 (DECISION_LOG 2026-11-05T23:50:09Z). Later rulings supersede item 11 of §5: Amear ruled 2026-11-05 that the arm-(b) stop and the breakers are bar-close market exits, and that minute data is sufficient for arm (b).
