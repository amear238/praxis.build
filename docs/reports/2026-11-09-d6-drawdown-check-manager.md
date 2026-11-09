Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

# D6 drawdown viability check — manager report (unit `2026-11-09-d6-drawdown-check`)

## For Amear (plain English, D10)

At 1 micro (MNQ), each of the three strategies had a worst 63-session stretch that fell $2,774 to $2,914 from its high. That stays under the safety ceiling only on the 150K accounts, where the ceiling is $3,600. Smaller accounts fail. If the losing run that carries over from earlier windows is counted, which is the project's committed measure, the worst figure is $4,463 to $5,280. That fails every account size. At 1 full NQ the worst stretch is $26,942 to $28,337, and every account fails. No daily-loss limit value has been written down yet, so the capped run could not be done at a real value. On the committed measure the D7 rule is triggered.

## Task

Amear ruling D-2026-11-08-D D6 (DECISIONS.md :1930-1944, committed at ec73ba8). Mac-only and read-only. No VM, no purchase, no network. The check computes the worst drawdown per walk-forward window on the three committed 2026-11-01 trade lists, at 1 MNQ and 1 NQ, with and without breaker #1. It compares each figure with the A4 ceiling for each tier row. It also tries a 09:30 ET re-run, and applies the D7 test.

## Rubric criteria addressed

S1 (pasted output: Verification evidence and Appendix), S2 (Evidence level), S6 (S6 cross-block check), S8 (Decisions taken), S13 (line 1 only).

## Result tables (from the pasted output in Appendix A; dollars, after commission and slippage)

Ceiling for each row = below min(3.2% of size, 80% of MFFU limit) (A4). Verdict = PASS only if all 17 windows are strictly below the ceiling. Two measures are shown:
- **WIN**: inside the window only. It is the worse of closed-trade and end-of-day equity, both reset to 0 at the window's start.
- **VS4**: the committed values-spec measure (`git show HEAD:docs/specs/2026-11-06-walk-forward-values.md` :139). It is the worst of four: WIN's two, plus the same two carried across windows.

For the Rapid Sim-Funded (intraday) rows, each measure also includes an MAE-based intratrade low (see Method).

**1 MNQ, no cap — worst window (verdict) for BASELINE / OPPBAND / FLAT1559**

| Tier row | Ceiling | WIN | VS4 |
|---|---|---|---|
| Studio 5K / 10K / 20K (trailing measure, stricter) | $160 / $320 / $640 | $2,913.90 / $2,786.70 / $2,774.40, FAIL all | $4,927.60 / $5,280.20 / $4,463.10, FAIL all |
| Rapid 25K, Rapid EOD 25K, Builder 25K | $800 | FAIL all | FAIL all |
| Rapid 50K, Rapid EOD 50K, Pro 50K, Builder 50K | $1,600 | FAIL all | FAIL all |
| Builder 50K add-on | $1,200 | FAIL all | FAIL all |
| Rapid 100K, Pro 100K, Builder 100K | $2,400 | FAIL all (15 or 16 of 17 windows below) | FAIL all |
| Rapid 150K [Eval EOD], Pro 150K, Builder 150K | $3,600 | **PASS all three** ($2,913.90 / $2,786.70 / $2,774.40) | FAIL all (14 or 15 of 17 below) |
| Rapid 150K [Sim-Funded intraday] | $3,600 | **PASS all three** ($3,031.30 / $3,259.10 / $2,891.80) | FAIL all ($5,267.00 / $5,525.30 / $4,802.50) |

**1 NQ, no cap:** every row FAILS on both measures, for all three strategies. WIN worst window: $28,337.08 / $27,394.44 / $26,942.08. VS4: $45,710.32 / $50,969.04 / $41,065.32.

**With the daily-loss cap at breaker #1's spec value:** NOT COMPUTABLE. No numeric spec value exists (evidence E4). A SENSITIVITY run at round caps is in Appendix A, last block. It is not a recommendation and not a breaker value.

**D7 test: does it fail at every tier at 1 MNQ?**
- On the committed measure (VS4): **YES.** All three strategies fail all 17 tier rows, including both Rapid stages.
- On the within-window measure (WIN): **NO.** The four 150K rows pass, for all three strategies. The margins are $686.10 / $813.30 / $825.60 at EOD and $568.70 / $340.90 / $708.20 intraday.

The D7 test is judged on VS4 (Decision 5). **D7 consequence:** no breaker value is designed to fit the ceiling. R6's research (higher-win-rate, steadier-equity strategies) is pulled forward to P0. The Noise-Area baseline continues through the VM tests for the record, but a GO on MFFU is not expected from it. Nothing was tuned in this unit. Acting on the work order is the master's job. This report does not change any ledger.

## Method (S2: what each figure is)

- **Inputs.** Each trade list is an NT8 grid CSV at 1 NQ per trade. Commission is $2.96 on every row, and Profit = points × 20 − 2.96 on every row (0 exceptions, Appendix A). Slippage is already in the fill prices (results report :51, quoted in E2), so it is not added again.
  - Points per trade = (exit − entry) × side.
  - NQ net = points × $20 − $4.68.
  - MNQ net = points × $2 − $1.90 (cost model v1.2.0). This equals the committed rule "MNQ net = (NQ gross ÷ 10) − $1.90" (values spec :139). That this equals an own MNQ run is INFERRED there and here.
- **Sessions and windows.** The session list and windows come from `scripts/wf/sessions.py` `build_calendar` (committed, imported read-only with `-B`): N = 1,352, K = 17, sessions 1324-1352 dropped. Every trade has entry date = exit date, and every exit date is a session (0 exceptions).
- **Equity basis.** Closed-trade equity and end-of-day equity. Intrabar equity is not in the trade list. The CSV's MAE column (NT8's worst excursion per trade, untimed, method UNVERIFIED) gives an intratrade low: equity before the trade − MAE − round-turn commission. That low is used only for the intraday (Rapid Sim-Funded) stage. It is a bound built from untimed per-trade figures, not a measured equity path. W1 computed the same low without the commission, so its figures sit $1.90 under mine (Adversarial findings).
- **Daily-loss cap rule (sensitivity only).** Trades in a session are taken in exit order. After a trade closes, if the day's realised net is at or below −cap, every later trade that session is skipped. The breaching trade counts in full. Intrabar limitation: breaker #1 as specified acts on "unrealized + realized P&L" (Phase 3 spec :97). This simulation sees only closed trades. A trade that breaches intratrade and then recovers is not stopped, and no trade is cut at the cap level.
- **Evidence level.** These are COMPUTED figures on NT8 trade lists (OBSERVED inputs) at Standard resolution with no breakers. They are not the judged High-resolution, breakers-on version (values spec :42). They are not tested on the VM. The MNQ figures are derived, not an MNQ run.

## Decisions taken (S8). Each one was decided by the acting unit (praxis-manager) under D-2026-11-08-D D1, and the master or Amear can change it. None of them is one of the four items reserved to Amear.

1. **"The three committed trade lists".** These are the three base-strategy NT8 exports on the Desktop: baseline 07-10, OppBand 07-57, Flat1559 07-59. They are **not in git** (E1: `git ls-files` shows no trade CSV). Their sha256 values are committed in the results report :29-31 and match in full. Committed code reads them from there (`test_baseruns.py:27`), and the voice-2 filing names them that way (`docs/reports/2026-11-08-amear-rulings-voice-2.md:98`). Nothing is reconstructed. LastHalfHourMomentum (08-00) is excluded as retired.
2. **Rapid rows** (Eval EOD vs Sim-Funded intraday trailing; C5 (ii), DECISIONS.md :1837-1838, open reading (i) :1886). Both stages are shown. Eval is judged on closed-trade and EOD equity. Sim-Funded is judged on the same plus the MAE intratrade low, which is the stricter of the two.
3. **Studio Static rows** (C5 (ii): "use the stricter limit type and stage, both shown"). The static measure (worst loss below the window-start balance) is shown. The verdict uses the trailing peak-to-trough measure, which is always at least as large and so is the stricter.
4. **Pass rule.** All 17 windows must be strictly below the ceiling (A4: "must stay below").
5. **Measure for the D7 test.** VS4 is used, because it is the committed SETTLED per-window measure (values spec :139). Each VS4 figure is still a per-window worst drawdown in D6's sense, and A4's wording is "backtest max drawdown". WIN is shown beside it because the brief defines drawdown "within each walk-forward window". **The answer flips between the two.** This is the one decision in this unit that changes a headline. It is flagged here for the master.
6. **Breaker #1.** No numeric value exists, so the capped run at the spec value is not done. Sensitivity was run at $100 / $200 / $300 / $500 (1 MNQ) and $1,000 / $2,000 / $3,000 / $5,000 (1 NQ): round values, the same points at both sizes, chosen before any result was seen. Nothing in this report proposes a cap.
7. **NQ commission.** The v1.2.0 rate of $4.68 is used, not the CSV's $2.96.

## Verification evidence (pasted output)

**E1 — no trade list in git; the Desktop files exist and match the committed hashes.** `git ls-files | grep -iE '\.csv$|\.xlsx$|\.tsv$'`:
```
tools/tickprep/nt-implied-offsets.csv
```
Committed results report :29-31 (grep output):
```
29:| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv` | baseline grid | `421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd` |
30:| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv` | OppBand grid | `4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8` |
31:| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv` | Flat1559 grid | `5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0` |
```
`shasum -a 256` on the Desktop files:
```
421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv
4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv
5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv
```
`docs/reports/2026-11-08-amear-rulings-voice-2.md:98` and `scripts/wf/oracle/tests/test_baseruns.py:27`:
```
   - the three committed trade lists, found from `scripts/wf/oracle/tests/test_baseruns.py`, which reads them from the Desktop.
DESK = "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 %s.csv"
```
Results report :402-404 (the committed full-span DDs). My script reproduces all three exactly on the CSV basis (Appendix A, "full-span closed-trade max DD" lines):
```
| BASELINE (`PraxisNoiseAreaBreakout`, BandOrVWAP) | 1190 | $197327.60 | 1.29 | -$45282.04 | -$45282.04 | ...
| OPPBAND | 810 | $210182.40 | 1.26 | -$50748.88 | -$50748.88 | ...
| FLAT1559 | 1190 | $193017.60 | 1.28 | -$40637.04 | -$40637.04 | ...
```

**E2 — cost model and slippage.** The first line of Appendix A prints the version 1.2.0, NQ RT 4.68, MNQ RT 1.9, tick 0.25 and NQ $20/pt, all read from `config/backtest-cost-model.json`. Results report :51 (excerpt): "in this data, slippage is 2 ticks adverse from the bar open, clipped to the bar's range."

**E3 — A4, C5 and the tier rows (committed).** `git show HEAD:DECISIONS.md`, numbered:
```
  1735	A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80%
  1736	    of the ruled limit, i.e. below the lower of 3.2% of the MFFU
  1737	    account size and 80% of MFFU's trailing drawdown limit. This
  1738	    amends D-2026-11-05-A item 3 with a safety buffer for model error.
  1739	    Evaluated against every tier row; tier pick stays Q9. Closes the
  1740	    notes-4 DD equity-base item.
  1836	C5  D-2026-11-08-B (i) win/loss judged by price, consistent with
  1837	    B = exit at entry price; (ii) Studio Static rows use the stricter
  1838	    limit type and stage, both shown; (iii) A8 annualisation = mean net
```
The tier rows are `git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md` :115-130 (sizes and limits as coded in `TIERS` in Appendix B; Flex :131 is UNVERIFIED and has no figures, so it is not computed). Excerpt:
```
   115	| Studio #003 · 5K | $5,000 | 0.04 × 5,000 = $200 | $250 (Static, not trailing) | min(200, 250) = **$200** | ...
   118	| Rapid · 25K | $25,000 | $1,000 | $1,000 (Eval EOD; Sim-Funded intraday trailing) | min(1,000, 1,000) = **$1,000** (equal) | ...
   124	| Builder · 50K | $50,000 | $2,000 | $2,000; $1,500 with add-on (EOD trailing) | **$2,000**; with add-on min(2,000, 1,500) = **$1,500** | ...
   128	| Rapid · 150K | $150,000 | $6,000 | $4,500 (Eval EOD; Sim-Funded intraday trailing) | min(6,000, 4,500) = **$4,500** | ...
   131	| Flex | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED — ...
```

**E4 — breaker #1 has no numeric spec value.** `git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md` :97:
```
    97	1. Daily loss limit — unrealized + realized P&L drops below threshold → cancel all, flatten, disable for session
```
`git grep -n -iE 'daily.loss|loss.limit|breaker #?1\b|breaker 1\b' HEAD -- docs/specs specs config ninjascript n8n`:
```
HEAD:docs/specs/2026-11-05-phase3-build-specification.md:97:1. Daily loss limit — unrealized + realized P&L drops below threshold → cancel all, flatten, disable for session
HEAD:docs/specs/2026-11-05-phase3-build-specification.md:109:The deterministic fallback script. A standalone Python script that runs independently of n8n. It polls the broker API directly, checks hardcoded thresholds (daily loss, max trades, session time), and
```
R8 (DECISIONS.md :1587-1589) keeps breaker #1 and gives it no value: "KEEP: #1 daily loss limit; ... New values come back to Amear as PROPOSED."

**E5 — 09:30 ET re-run: not possible with committed code.** Every module under `scripts/wf/oracle/` says it trades nothing (`grep -n 'trades nothing' scripts/wf/oracle/*.py`):
```
scripts/wf/oracle/atr.py:84:    ap = argparse.ArgumentParser(description="arm (b) ATR(14) oracle for one session (test oracle; trades nothing)")
scripts/wf/oracle/band.py:170:    ap = argparse.ArgumentParser(description="arm (b) band oracle at one bar (test oracle; trades nothing)")
scripts/wf/oracle/grade.py:4:Test oracle only: it trades nothing and is not the walk-forward. It reads one or more trade lists produced
scripts/wf/oracle/grade.py:907:    ap = argparse.ArgumentParser(description="arm (b) T8-T11 grader (test oracle; trades nothing)")
scripts/wf/oracle/market.py:4:Test oracle only (values-spec T6(ii), docs/specs/2026-11-06-walk-forward-values.md:191): it trades nothing
scripts/wf/oracle/policy.py:4:Test oracle only: it trades nothing and is not the walk-forward. grade.py's load_policy() loads this file by
scripts/wf/oracle/t6ii.py:9:Test oracle only; trades nothing.
scripts/wf/oracle/t6ii.py:58:    ap = argparse.ArgumentParser(description="T6(ii) oracle table (test oracle; trades nothing)")
```
The top-level modules (`sessions.py`, `tradelist.py`, `select.py`, `pbo.py`, `report.py`) read NT8 or bridge trade lists. None of them defines a simulator (`grep -c -iE 'def (simulate|generate|backtest|run_strategy)'` gives 0 in all 11 files):
```
scripts/wf/pbo.py:0
scripts/wf/report.py:0
scripts/wf/select.py:0
scripts/wf/sessions.py:0
scripts/wf/tradelist.py:0
scripts/wf/oracle/atr.py:0
scripts/wf/oracle/band.py:0
scripts/wf/oracle/grade.py:0
scripts/wf/oracle/market.py:0
scripts/wf/oracle/policy.py:0
scripts/wf/oracle/t6ii.py:0
```
W1 found committed building blocks: `grade.py:731` `_scan_entry`, `policy.py:92` `walk_cstar` and `market.py:338-351` fills. Nothing chains them into a trade list. Building that chain would mean writing a new strategy simulator, which is a build unit and not part of this read-only check. The relevant context is `scripts/wf/oracle/market.py:17-19`:
```
      "08:31" -- OBSERVED fit on the three committed 2026-11-01 NT8 base runs (baseline BandOrVWAP, OppBand,
                 Flat1559: fill rules and T12 (iii)/(iv)/(v) fit every trade only with the 08:31-09:30 bars
                 in the session); UNVERIFIED for arm (b) on the VM.
```
So the three lists used here are the 08:31-start lists (finding B1), not R1's 09:30 ET session. No 09:30 run exists.

**E6 — the uncommitted U7 edits do not change any figure.** Hunks in `git diff -U0 HEAD` for the two specs: WF spec @@ -5, -28, -107, -113 (header only), -156. Values spec @@ -1, -3, -5, -12, -72, -93, -121, -128, -132,4, -206, -310,2, -325,4, -330, -349. `git diff -U0 HEAD -- <values spec> | grep -c 'Worst drawdown per window'` → `0`, so the :139 measure is unchanged. No tier row (:115-130) is changed. The new header text marks Static and Rapid rows "NEEDS AMEAR (ii)". The committed C5 (ii) answers that for Studio, and Decisions 2-3 cover the rest.

**E7 — negative tests of the gate (`/tmp/d6/negtest.py`, Appendix B):**
```
ceiling Pro 150K = 3600.0
17 windows all at ceiling - 0.01 -> PASS
one window EXACTLY at ceiling (A4 says 'below') -> FAIL
one window above ceiling -> FAIL
Builder 50K add-on ceiling (expect 1200 = 80% of 1500, not 1600) = 1200.0
Studio 5K ceiling (expect 160 = 3.2% of 5000, not 200) = 160.0
DD of [+100,-300,+50,-100] (expect 350) = 350.0
carried DD, empty window, start 200 below peak (expect 200) = 200.0
```
Both verdicts occur in the live tables (PASS on the 150K rows under WIN; FAIL elsewhere). The gate has been seen to trip.

**E8 — producer vs W1, Flat1559 at 1 MNQ (`/tmp/d6/cmp.py`):**
```
fields compared per row: OOS first, OOS last, trades, net, DD closed-trade, DD end-of-day
rows MATCH 17, MISMATCH 0
```

## Workers dispatched

| id | mode | outcome |
|---|---|---|
| W1 (agentId ae2572a87347a8e77) | ADVERSARIAL, foreground, independent recompute (it did not see my numbers) | `VERDICT: DEFECT`, on the brief's within-window rule. The tables computed cleanly, and its Task 1 matches mine 17/17 (E8). |

## Adversarial findings (W1's output, labelled as the worker's)

W1's Task 1 table (the worker's, verbatim):
```
k | OOS first  | OOS last   | trades | net MNQ  | DD(a)   | DD(b)   | max
 1 | 2022-03-17 | 2022-06-15 |     54 |  3325.40 |  850.10 |  834.00 |  850.10
 2 | 2022-06-16 | 2022-09-13 |     57 |  2681.70 |  700.10 |  683.20 |  700.10
 3 | 2022-09-14 | 2022-12-09 |     55 |  -913.00 | 1744.40 | 1744.40 | 1744.40
 4 | 2022-12-12 | 2023-03-10 |     65 |    89.00 |  568.60 |  538.00 |  568.60
 5 | 2023-03-13 | 2023-06-08 |     54 |  2140.90 |  292.70 |  285.50 |  292.70
 6 | 2023-06-09 | 2023-09-05 |     55 |   435.50 |  500.30 |  438.30 |  500.30
 7 | 2023-09-06 | 2023-12-01 |     52 |   551.70 |  460.50 |  460.50 |  460.50
 8 | 2023-12-04 | 2024-03-01 |     63 |  -177.20 |  722.10 |  628.80 |  722.10
 9 | 2024-03-04 | 2024-05-30 |     60 |   739.00 | 1045.30 |  937.90 | 1045.30
10 | 2024-05-31 | 2024-08-27 |     55 |  1837.00 |  823.40 |  823.40 |  823.40
11 | 2024-08-28 | 2024-11-22 |     53 |   612.80 |  934.70 |  934.70 |  934.70
12 | 2024-11-25 | 2025-02-25 |     55 |  1814.50 |  883.00 |  829.90 |  883.00
13 | 2025-02-26 | 2025-05-27 |     56 |  1913.10 | 1125.40 | 1024.40 | 1125.40
14 | 2025-05-28 | 2025-08-22 |     54 |  -568.10 | 1344.20 | 1120.60 | 1344.20
15 | 2025-08-25 | 2025-11-20 |     59 |   375.40 | 1517.50 | 1488.40 | 1517.50
16 | 2025-11-21 | 2026-03-09 |     59 | -2435.60 | 2774.40 | 2774.40 | 2774.40
17 | 2026-03-10 | 2026-06-05 |     59 |   627.90 | 2272.20 | 2272.20 | 2272.20
MAX over windows of max(DD(a),DD(b)) = 2774.40 (window 16)
sum OOS trades=965 net=13050.00
```
W1's Task 2 (the worker's, verbatim):
```
  Pro 150K             0.032*150000=4800.00  0.8*4500=3600.00  ceiling=3600.00
  Pro 100K             0.032*100000=3200.00  0.8*3000=2400.00  ceiling=2400.00
  Builder 50K add-on   0.032*50000=1600.00  0.8*1500=1200.00  ceiling=1200.00
Pro 150K             ceiling 3600.00 | within-window (brief's rule): PASS  fails=[] | four-measure (values spec 6): FAIL  fails=[16, 17]
Pro 100K             ceiling 2400.00 | within-window (brief's rule): FAIL  fails=[16] | four-measure (values spec 6): FAIL  fails=[15, 16, 17]
Builder 50K add-on   ceiling 1200.00 | within-window (brief's rule): FAIL  fails=[3, 14, 15, 16, 17] | four-measure (values spec 6): FAIL  fails=[3, 4, 14, 15, 16, 17]
```
W1's verdict line (the worker's): `VERDICT: DEFECT — the tables compute cleanly, but the brief's within-window pass rule omits the carried-across-windows measures that committed values spec §6 (line 139) says to judge; under the committed four-measure rule, Pro 150K fails in windows 16 and 17 (carried drawdown 3759.00 and 4463.10 against the 3600 ceiling)`

How each finding is handled:
1. **Within-window vs four-measure.** Accepted. The report already showed both. The D7 test is judged on VS4 (Decision 5). W1's Flat1559 VS4 figures (window 16: 3759.00 closed / 3673.90 EOD; window 17: 4463.10 / 4378.00) equal mine in Appendix A, Flat1559 1 MNQ, ct_carry and eod_carry columns.
2. **Window 16 contains the 17-day data hole** (2025-12-14 → 2026-01-01, WF spec :102). W1 said: 14 weekdays with no RTH bar; peak 2025-12-04, trough 2026-03-06. This is noted, not corrected: the data is used as is, per R-VN3-3. WIN's worst window is window 16 for all three strategies. Under WIN, the 100K rows of baseline and Flat1559 fail only in window 16 (16/17 below). That is an observation about the data. It is not a reason to drop the window.
3. **MAE.** W1 agrees it is a bound and not an equity path. Its window 16 and 17 lows (2889.90, 2609.70) sit $1.90 under mine (2891.80, 2611.60) because I also subtract the round-turn commission at the low.
4. **CSV commission $2.96 vs $4.68.** Already handled: points from prices, v1.2.0 commission (Decision 7).
5. **2023-04-05 ends at 14:03** (truncated data day, window 5). Noted. The data is used as is.
6. **Clean checks.** W1 reports: 0 cross-session trades, 0 non-session exit dates, 0 overlaps, prices on the 0.25 grid, 965 of 1190 Flat1559 trades in OOS.

## S6 cross-block check

- **Block 2 (walk-forward).** The committed sessions/windows code and the committed values-spec :139 measure are used (VS4). The extra WIN view is labelled. Arm (b) is not touched. These are arm (a) base lists only.
- **Block 3 (breakers).** No breaker value is set or proposed. The sensitivity caps are labelled as not values (D7; R8 says new values come back to Amear as PROPOSED). Breaker #6's $1,500 (Phase 3 spec :102) is used only as the Builder 50K add-on row's MFFU limit, which is the values-spec :136 reporting rule. F2 is not touched.
- **F4 / MFFU terms.** The tier sizes and limits are the WF spec's 2026-11-05 capture. MFFU's current pages were not re-read (no network). They are UNVERIFIED as of today.
- **R1 (09:30 ET session).** The lists used fit the 08:31 start (E5). The figures here belong to that NT8 run, not to R1's session. A 09:30 list does not exist and cannot be made with committed code.
- **Uncommitted U7 text.** No figure changes (E6).

## Process log

1. Read the rubric and the brief's inputs. Found that no trade CSV is committed (E1). Took Decision 1 on the documented hash-pinned reading.
2. Read the committed cost model, WF spec :113-131, values spec §5 and :139, A4, C5 and Phase 3 :97.
3. Wrote `/tmp/d6/d6.py`. It reuses `sessions.build_calendar` and `report._dd_series` / `four_measure_drawdowns` read-only, with `-B`. `git status --short scripts/wf` was empty after the runs.
4. First run judged only VS4. I added WIN because the brief's definition is within-window, re-ran, and saved the output to `/tmp/d6/out.txt` (Appendix A).
5. Dispatched W1 in the foreground. It returned with a verdict. Compared tables (E8). Ran the negative tests (E7).
6. Appended one MANIFEST.md row after line 311. Staged nothing.

## Files staged

None by this unit (the brief says stage nothing). Working-tree changes by this unit: this report (new, untracked) and one MANIFEST.md row appended after line 311 (unstaged). The pre-existing staged set was unchanged across the unit. `git diff --cached --stat | tail -1`, before and after:
```
 12 files changed, 5726 insertions(+), 2 deletions(-)
 12 files changed, 5726 insertions(+), 2 deletions(-)
```
Scratch files, outside the repo: `/tmp/d6/d6.py`, `/tmp/d6/negtest.py`, `/tmp/d6/cmp.py`, `/tmp/d6/w1_table.txt`, `/tmp/d6/out.txt`. W1's scratch is in `/tmp/d6adv/`.

## Appendix A — full output of `python3 -I -B /tmp/d6/d6.py` (saved as /tmp/d6/out.txt)

```
cost model version 1.2.0 | NQ RT 4.68 | MNQ RT 1.9 | tick 0.25 | NQ $/pt 20.0 | slippage ticks/side 2 (already in NT8 fills; not added again)
data sha256 307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454
N sessions 1352 first 2021-03-08 last 2026-07-17 K 17 dropped [1324, 1352] ['2026-06-08', '2026-07-17']

=== BASELINE BandOrVWAP | sha256 421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd | MATCH | rows 1190 (expect 1190) | Profit != pts*20-2.96 rows: 0
entry date != exit date: 0 | exit date not a session: 0 | MAE < closed loss (impossible if MAE is worst excursion): 0
full-span closed-trade max DD on CSV Profit (cost $2.96): -$45,282.04 ; net $197,327.60

=== OPPBAND | sha256 4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8 | MATCH | rows 810 (expect 810) | Profit != pts*20-2.96 rows: 0
entry date != exit date: 0 | exit date not a session: 0 | MAE < closed loss (impossible if MAE is worst excursion): 0
full-span closed-trade max DD on CSV Profit (cost $2.96): -$50,748.88 ; net $210,182.40

=== FLAT1559 | sha256 5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0 | MATCH | rows 1190 (expect 1190) | Profit != pts*20-2.96 rows: 0
entry date != exit date: 0 | exit date not a session: 0 | MAE < closed loss (impossible if MAE is worst excursion): 0
full-span closed-trade max DD on CSV Profit (cost $2.96): -$40,637.04 ; net $193,017.60

--- BASELINE BandOrVWAP @ 1 MNQ, no cap: per OOS window (dollars) ---
k | OOS dates | trades | net | ct_start | eod_start | ct_carry | eod_carry | WORST4 | mae_start | mae_carry | static_ct | static_mae
1 | 2022-03-17..2022-06-15 | 54 | $3,374.40 | $874.10 | $858.00 | $874.10 | $858.00 | $874.10 | $940.00 | $940.00 | $95.80 | $161.70
2 | 2022-06-16..2022-09-13 | 57 | $2,615.70 | $758.60 | $741.70 | $758.60 | $741.70 | $758.60 | $843.60 | $843.60 | $120.00 | $178.00
3 | 2022-09-14..2022-12-09 | 55 | $-816.00 | $1,756.40 | $1,756.40 | $1,848.90 | $1,848.90 | $1,848.90 | $1,862.80 | $1,955.30 | $1,756.40 | $1,862.80
4 | 2022-12-12..2023-03-10 | 65 | $128.50 | $613.60 | $593.00 | $1,364.60 | $1,275.00 | $1,364.60 | $673.80 | $1,428.50 | $456.10 | $520.00
5 | 2023-03-13..2023-06-08 | 54 | $2,169.90 | $292.70 | $276.00 | $1,015.20 | $1,015.20 | $1,015.20 | $324.60 | $1,056.60 | $235.20 | $276.60
6 | 2023-06-09..2023-09-05 | 55 | $693.50 | $508.40 | $435.30 | $508.40 | $435.30 | $508.40 | $611.40 | $611.40 | $430.50 | $462.00
7 | 2023-09-06..2023-12-01 | 52 | $555.20 | $518.90 | $518.90 | $518.90 | $518.90 | $518.90 | $557.70 | $557.70 | $371.80 | $481.90
8 | 2023-12-04..2024-03-01 | 63 | $-243.20 | $674.10 | $588.30 | $759.30 | $695.60 | $759.30 | $690.40 | $775.60 | $652.00 | $668.30
9 | 2024-03-04..2024-05-30 | 60 | $723.50 | $1,082.30 | $974.90 | $1,131.50 | $1,024.10 | $1,131.50 | $1,160.80 | $1,210.00 | $781.00 | $859.50
10 | 2024-05-31..2024-08-27 | 55 | $1,915.50 | $823.40 | $823.40 | $823.40 | $823.40 | $823.40 | $875.90 | $875.90 | $418.30 | $529.70
11 | 2024-08-28..2024-11-22 | 53 | $558.30 | $982.20 | $982.20 | $982.20 | $982.20 | $982.20 | $1,060.20 | $1,060.20 | $118.70 | $234.30
12 | 2024-11-25..2025-02-25 | 55 | $1,944.50 | $917.00 | $863.90 | $917.00 | $863.90 | $917.00 | $1,005.40 | $1,005.40 | $0.00 | $4.90
13 | 2025-02-26..2025-05-27 | 56 | $1,938.60 | $1,170.50 | $1,043.50 | $1,170.50 | $1,043.50 | $1,170.50 | $1,279.50 | $1,279.50 | $811.40 | $897.00
14 | 2025-05-28..2025-08-22 | 54 | $-667.10 | $1,423.20 | $1,172.10 | $2,368.80 | $2,032.60 | $2,368.80 | $1,448.10 | $2,393.70 | $1,423.20 | $1,448.10
15 | 2025-08-25..2025-11-20 | 59 | $14.90 | $1,616.50 | $1,604.40 | $3,137.20 | $3,040.00 | $3,137.20 | $1,662.40 | $3,183.10 | $1,524.50 | $1,570.40
16 | 2025-11-21..2026-03-09 | 59 | $-2,627.10 | $2,913.90 | $2,913.90 | $4,299.00 | $4,213.90 | $4,299.00 | $3,031.30 | $4,416.40 | $2,701.20 | $2,818.60
17 | 2026-03-10..2026-06-05 | 59 | $809.90 | $2,239.20 | $2,239.20 | $4,927.60 | $4,842.50 | $4,927.60 | $2,578.60 | $5,267.00 | $702.70 | $1,042.10
MAX over windows: WORST4 $4,927.60 | MAE-incl $5,267.00 | static_ct $2,701.20 | static_mae $2,818.60

--- BASELINE BandOrVWAP @ 1 NQ, no cap: per OOS window (dollars) ---
k | OOS dates | trades | net | ct_start | eod_start | ct_carry | eod_carry | WORST4 | mae_start | mae_carry | static_ct | static_mae
1 | 2022-03-17..2022-06-15 | 54 | $34,517.28 | $8,612.12 | $8,436.80 | $8,612.12 | $8,436.80 | $8,612.12 | $9,256.80 | $9,256.80 | $714.56 | $1,359.24
2 | 2022-06-16..2022-09-13 | 57 | $26,973.24 | $7,457.12 | $7,302.44 | $7,457.12 | $7,302.44 | $7,457.12 | $8,307.12 | $8,307.12 | $1,128.40 | $1,708.40
3 | 2022-09-14..2022-12-09 | 55 | $-7,372.40 | $17,191.68 | $17,191.68 | $17,901.88 | $17,901.88 | $17,901.88 | $18,241.36 | $18,951.56 | $17,191.68 | $18,241.36
4 | 2022-12-12..2023-03-10 | 65 | $2,215.80 | $5,863.92 | $5,643.60 | $12,443.12 | $11,532.80 | $12,443.12 | $6,438.92 | $13,067.80 | $4,360.52 | $4,985.20
5 | 2023-03-13..2023-06-08 | 54 | $22,472.28 | $2,812.44 | $2,616.80 | $8,175.84 | $8,175.84 | $8,175.84 | $3,117.12 | $8,575.52 | $2,309.04 | $2,708.72
6 | 2023-06-09..2023-09-05 | 55 | $7,722.60 | $4,998.08 | $4,252.76 | $4,998.08 | $4,252.76 | $4,998.08 | $6,028.08 | $6,028.08 | $4,018.60 | $4,333.60
7 | 2023-09-06..2023-12-01 | 52 | $6,296.64 | $4,888.28 | $4,888.28 | $4,888.28 | $4,888.28 | $4,888.28 | $5,177.64 | $5,177.64 | $3,617.76 | $4,733.08
8 | 2023-12-04..2024-03-01 | 63 | $-1,529.84 | $5,967.72 | $5,066.76 | $6,776.76 | $6,111.12 | $6,776.76 | $6,112.40 | $6,921.44 | $5,732.40 | $5,877.08
9 | 2024-03-04..2024-05-30 | 60 | $8,094.20 | $10,364.76 | $9,305.08 | $10,364.76 | $9,305.08 | $10,364.76 | $11,149.76 | $11,149.76 | $7,308.80 | $8,093.80
10 | 2024-05-31..2024-08-27 | 55 | $19,942.60 | $8,148.08 | $8,148.08 | $8,148.08 | $8,148.08 | $8,148.08 | $8,673.08 | $8,673.08 | $4,154.36 | $5,254.04
11 | 2024-08-28..2024-11-22 | 53 | $6,341.96 | $9,635.84 | $9,635.84 | $9,635.84 | $9,635.84 | $9,635.84 | $10,415.84 | $10,415.84 | $929.24 | $2,314.36
12 | 2024-11-25..2025-02-25 | 55 | $20,232.60 | $8,740.40 | $8,195.08 | $8,740.40 | $8,195.08 | $8,740.40 | $9,687.32 | $9,687.32 | $0.00 | $34.68
13 | 2025-02-26..2025-05-27 | 56 | $20,187.92 | $11,633.40 | $10,220.20 | $11,633.40 | $10,220.20 | $11,633.40 | $12,723.40 | $12,723.40 | $7,813.28 | $8,622.96
14 | 2025-05-28..2025-08-22 | 54 | $-5,897.72 | $13,687.84 | $11,162.52 | $22,871.76 | $19,481.12 | $22,871.76 | $13,922.52 | $23,106.44 | $13,687.84 | $13,922.52
15 | 2025-08-25..2025-11-20 | 59 | $993.88 | $15,878.60 | $15,743.28 | $29,968.64 | $28,968.00 | $29,968.64 | $16,323.28 | $30,413.32 | $14,887.00 | $15,331.68
16 | 2025-11-21..2026-03-09 | 59 | $-25,426.12 | $28,337.08 | $28,337.08 | $40,269.20 | $39,403.88 | $40,269.20 | $29,496.76 | $41,428.88 | $26,181.44 | $27,341.12
17 | 2026-03-10..2026-06-05 | 59 | $8,943.88 | $21,919.44 | $21,919.44 | $45,710.32 | $44,845.00 | $45,710.32 | $25,299.12 | $49,090.00 | $6,196.44 | $9,576.12
MAX over windows: WORST4 $45,710.32 | MAE-incl $49,090.00 | static_ct $26,181.44 | static_mae $27,341.12

--- OPPBAND @ 1 MNQ, no cap: per OOS window (dollars) ---
k | OOS dates | trades | net | ct_start | eod_start | ct_carry | eod_carry | WORST4 | mae_start | mae_carry | static_ct | static_mae
1 | 2022-03-17..2022-06-15 | 40 | $3,837.00 | $949.00 | $949.00 | $949.00 | $949.00 | $949.00 | $1,069.50 | $1,069.50 | $129.80 | $250.30
2 | 2022-06-16..2022-09-13 | 39 | $2,781.90 | $1,006.80 | $951.20 | $1,006.80 | $951.20 | $1,006.80 | $1,149.10 | $1,149.10 | $208.20 | $244.70
3 | 2022-09-14..2022-12-09 | 35 | $731.00 | $1,352.90 | $1,328.30 | $1,352.90 | $1,328.30 | $1,352.90 | $1,476.80 | $1,476.80 | $1,285.20 | $1,409.10
4 | 2022-12-12..2023-03-10 | 42 | $2.70 | $972.70 | $946.30 | $1,076.30 | $1,076.30 | $1,076.30 | $1,212.80 | $1,342.80 | $946.30 | $1,212.80
5 | 2023-03-13..2023-06-08 | 41 | $1,347.10 | $1,114.50 | $1,114.50 | $1,452.90 | $1,452.90 | $1,452.90 | $1,170.40 | $1,508.80 | $743.90 | $799.80
6 | 2023-06-09..2023-09-05 | 39 | $115.90 | $1,090.60 | $1,090.60 | $1,090.60 | $1,090.60 | $1,090.60 | $1,236.10 | $1,236.10 | $877.00 | $1,022.50
7 | 2023-09-06..2023-12-01 | 42 | $21.20 | $1,048.30 | $1,048.30 | $1,146.60 | $1,146.60 | $1,146.60 | $1,090.70 | $1,189.00 | $949.80 | $992.20
8 | 2023-12-04..2024-03-01 | 39 | $120.40 | $814.40 | $814.40 | $814.40 | $814.40 | $814.40 | $1,039.10 | $1,039.10 | $381.30 | $606.00
9 | 2024-03-04..2024-05-30 | 37 | $1,051.20 | $1,319.70 | $1,175.80 | $1,344.70 | $1,200.80 | $1,344.70 | $1,361.70 | $1,386.70 | $1,032.00 | $1,074.00
10 | 2024-05-31..2024-08-27 | 38 | $2,715.30 | $1,364.30 | $1,364.30 | $1,364.30 | $1,364.30 | $1,364.30 | $1,404.70 | $1,404.70 | $663.30 | $774.70
11 | 2024-08-28..2024-11-22 | 37 | $119.70 | $1,149.30 | $1,149.30 | $1,149.30 | $1,149.30 | $1,149.30 | $1,266.80 | $1,266.80 | $684.30 | $801.80
12 | 2024-11-25..2025-02-25 | 32 | $2,555.70 | $1,028.10 | $1,028.10 | $1,028.10 | $1,028.10 | $1,028.10 | $1,116.60 | $1,116.60 | $0.00 | $4.90
13 | 2025-02-26..2025-05-27 | 37 | $2,145.20 | $2,415.80 | $2,349.70 | $2,415.80 | $2,349.70 | $2,415.80 | $2,833.10 | $2,833.10 | $80.90 | $498.20
14 | 2025-05-28..2025-08-22 | 34 | $-240.60 | $1,381.70 | $1,381.70 | $3,175.90 | $3,175.90 | $3,175.90 | $1,645.50 | $3,439.70 | $1,381.70 | $1,645.50
15 | 2025-08-25..2025-11-20 | 42 | $-59.80 | $2,205.10 | $2,205.10 | $4,130.20 | $4,130.20 | $4,130.20 | $2,317.60 | $4,242.70 | $2,095.40 | $2,207.90
16 | 2025-11-21..2026-03-09 | 37 | $-2,605.80 | $2,786.70 | $2,786.70 | $4,817.60 | $4,817.60 | $4,817.60 | $3,259.10 | $5,290.00 | $2,723.00 | $3,195.40
17 | 2026-03-10..2026-06-05 | 41 | $1,027.10 | $2,106.90 | $2,106.90 | $5,280.20 | $5,280.20 | $5,280.20 | $2,446.30 | $5,525.30 | $579.80 | $824.90
MAX over windows: WORST4 $5,280.20 | MAE-incl $5,525.30 | static_ct $2,723.00 | static_mae $3,195.40

--- OPPBAND @ 1 NQ, no cap: per OOS window (dollars) ---
k | OOS dates | trades | net | ct_start | eod_start | ct_carry | eod_carry | WORST4 | mae_start | mae_carry | static_ct | static_mae
1 | 2022-03-17..2022-06-15 | 40 | $38,942.80 | $9,418.72 | $9,418.72 | $9,418.72 | $9,418.72 | $9,418.72 | $10,623.72 | $10,623.72 | $1,126.16 | $2,403.40
2 | 2022-06-16..2022-09-13 | 39 | $28,377.48 | $10,039.36 | $9,469.04 | $10,039.36 | $9,469.04 | $10,039.36 | $11,433.72 | $11,433.72 | $2,039.04 | $2,404.04
3 | 2022-09-14..2022-12-09 | 35 | $7,811.20 | $13,371.48 | $13,111.16 | $13,371.48 | $13,111.16 | $13,371.48 | $14,596.16 | $14,596.16 | $12,665.84 | $13,890.52
4 | 2022-12-12..2023-03-10 | 42 | $628.44 | $9,540.84 | $9,434.36 | $10,662.76 | $10,662.76 | $10,662.76 | $12,099.36 | $13,327.76 | $9,434.36 | $12,099.36
5 | 2023-03-13..2023-06-08 | 41 | $14,058.12 | $11,001.80 | $11,001.80 | $14,013.48 | $14,013.48 | $14,013.48 | $11,546.48 | $14,558.16 | $7,138.28 | $7,682.96
6 | 2023-06-09..2023-09-05 | 39 | $1,717.48 | $10,562.32 | $10,562.32 | $10,562.32 | $10,562.32 | $10,562.32 | $12,017.32 | $12,017.32 | $8,340.40 | $9,795.40
7 | 2023-09-06..2023-12-01 | 42 | $813.44 | $10,167.96 | $10,167.96 | $10,979.12 | $10,979.12 | $10,979.12 | $10,577.64 | $11,388.80 | $9,039.76 | $9,449.44
8 | 2023-12-04..2024-03-01 | 39 | $1,762.48 | $8,058.08 | $8,058.08 | $8,058.08 | $8,058.08 | $8,058.08 | $10,262.12 | $10,262.12 | $3,497.96 | $5,702.00
9 | 2024-03-04..2024-05-30 | 37 | $11,041.84 | $13,082.44 | $11,586.16 | $13,082.44 | $11,586.16 | $13,082.44 | $13,430.84 | $13,430.84 | $10,105.20 | $10,453.60
10 | 2024-05-31..2024-08-27 | 38 | $27,697.16 | $13,614.36 | $13,614.36 | $13,614.36 | $13,614.36 | $13,614.36 | $14,004.04 | $14,004.04 | $6,604.36 | $7,704.04
11 | 2024-08-28..2024-11-22 | 37 | $1,726.84 | $11,403.08 | $11,403.08 | $11,403.08 | $11,403.08 | $11,403.08 | $12,578.08 | $12,578.08 | $6,671.16 | $7,846.16
12 | 2024-11-25..2025-02-25 | 32 | $26,015.24 | $10,223.72 | $10,223.72 | $10,223.72 | $10,223.72 | $10,223.72 | $11,108.72 | $11,108.72 | $0.00 | $34.68
13 | 2025-02-26..2025-05-27 | 37 | $21,981.84 | $24,129.36 | $23,454.04 | $24,129.36 | $23,454.04 | $24,129.36 | $28,273.72 | $28,273.72 | $508.28 | $4,652.64
14 | 2025-05-28..2025-08-22 | 34 | $-1,919.12 | $13,487.64 | $13,487.64 | $31,243.48 | $31,243.48 | $31,243.48 | $16,097.00 | $33,852.84 | $13,487.64 | $16,097.00
15 | 2025-08-25..2025-11-20 | 42 | $3.44 | $21,850.52 | $21,850.52 | $40,399.84 | $40,399.84 | $40,399.84 | $22,975.52 | $41,524.84 | $20,724.88 | $21,849.88
16 | 2025-11-21..2026-03-09 | 37 | $-25,528.16 | $27,394.44 | $27,394.44 | $46,400.32 | $46,400.32 | $46,400.32 | $32,104.12 | $51,110.00 | $26,728.80 | $31,438.48
17 | 2026-03-10..2026-06-05 | 41 | $10,858.12 | $20,768.28 | $20,768.28 | $50,969.04 | $50,969.04 | $50,969.04 | $24,147.96 | $53,164.04 | $5,769.36 | $7,964.36
MAX over windows: WORST4 $50,969.04 | MAE-incl $53,164.04 | static_ct $26,728.80 | static_mae $31,438.48

--- FLAT1559 @ 1 MNQ, no cap: per OOS window (dollars) ---
k | OOS dates | trades | net | ct_start | eod_start | ct_carry | eod_carry | WORST4 | mae_start | mae_carry | static_ct | static_mae
1 | 2022-03-17..2022-06-15 | 54 | $3,325.40 | $850.10 | $834.00 | $850.10 | $834.00 | $850.10 | $916.00 | $916.00 | $90.30 | $156.20
2 | 2022-06-16..2022-09-13 | 57 | $2,681.70 | $700.10 | $683.20 | $700.10 | $683.20 | $700.10 | $785.10 | $785.10 | $91.50 | $149.50
3 | 2022-09-14..2022-12-09 | 55 | $-913.00 | $1,744.40 | $1,744.40 | $1,783.40 | $1,783.40 | $1,783.40 | $1,850.80 | $1,889.80 | $1,744.40 | $1,850.80
4 | 2022-12-12..2023-03-10 | 65 | $89.00 | $568.60 | $538.00 | $1,423.60 | $1,325.50 | $1,423.60 | $626.80 | $1,487.50 | $471.60 | $535.50
5 | 2023-03-13..2023-06-08 | 54 | $2,140.90 | $292.70 | $285.50 | $1,098.20 | $1,098.20 | $1,098.20 | $324.60 | $1,139.60 | $235.20 | $276.60
6 | 2023-06-09..2023-09-05 | 55 | $435.50 | $500.30 | $438.30 | $500.30 | $438.30 | $500.30 | $611.40 | $611.40 | $468.50 | $500.00
7 | 2023-09-06..2023-12-01 | 52 | $551.70 | $460.50 | $460.50 | $460.50 | $460.50 | $460.50 | $495.30 | $495.30 | $367.80 | $477.90
8 | 2023-12-04..2024-03-01 | 63 | $-177.20 | $722.10 | $628.80 | $822.30 | $751.10 | $822.30 | $738.00 | $838.20 | $700.00 | $715.90
9 | 2024-03-04..2024-05-30 | 60 | $739.00 | $1,045.30 | $937.90 | $1,045.30 | $937.90 | $1,045.30 | $1,123.80 | $1,123.80 | $725.00 | $803.50
10 | 2024-05-31..2024-08-27 | 55 | $1,837.00 | $823.40 | $823.40 | $823.40 | $823.40 | $823.40 | $875.90 | $875.90 | $359.30 | $470.70
11 | 2024-08-28..2024-11-22 | 53 | $612.80 | $934.70 | $934.70 | $934.70 | $934.70 | $934.70 | $1,007.70 | $1,007.70 | $63.30 | $234.30
12 | 2024-11-25..2025-02-25 | 55 | $1,814.50 | $883.00 | $829.90 | $883.00 | $829.90 | $883.00 | $986.60 | $986.60 | $0.00 | $4.90
13 | 2025-02-26..2025-05-27 | 56 | $1,913.10 | $1,125.40 | $1,024.40 | $1,125.40 | $1,024.40 | $1,125.40 | $1,240.00 | $1,240.00 | $790.00 | $899.00
14 | 2025-05-28..2025-08-22 | 54 | $-568.10 | $1,344.20 | $1,120.60 | $2,371.80 | $2,063.10 | $2,371.80 | $1,369.10 | $2,396.70 | $1,344.20 | $1,369.10
15 | 2025-08-25..2025-11-20 | 59 | $375.40 | $1,517.50 | $1,488.40 | $2,967.20 | $2,853.00 | $2,967.20 | $1,563.40 | $3,013.10 | $1,371.50 | $1,417.40
16 | 2025-11-21..2026-03-09 | 59 | $-2,435.60 | $2,774.40 | $2,774.40 | $3,759.00 | $3,673.90 | $3,759.00 | $2,891.80 | $3,876.40 | $2,538.70 | $2,656.10
17 | 2026-03-10..2026-06-05 | 59 | $627.90 | $2,272.20 | $2,272.20 | $4,463.10 | $4,378.00 | $4,463.10 | $2,611.60 | $4,802.50 | $807.20 | $1,146.60
MAX over windows: WORST4 $4,463.10 | MAE-incl $4,802.50 | static_ct $2,538.70 | static_mae $2,656.10

--- FLAT1559 @ 1 NQ, no cap: per OOS window (dollars) ---
k | OOS dates | trades | net | ct_start | eod_start | ct_carry | eod_carry | WORST4 | mae_start | mae_carry | static_ct | static_mae
1 | 2022-03-17..2022-06-15 | 54 | $34,027.28 | $8,372.12 | $8,196.80 | $8,372.12 | $8,196.80 | $8,372.12 | $9,016.80 | $9,016.80 | $659.56 | $1,304.24
2 | 2022-06-16..2022-09-13 | 57 | $27,633.24 | $6,872.12 | $6,717.44 | $6,872.12 | $6,717.44 | $6,872.12 | $7,722.44 | $7,722.44 | $843.40 | $1,423.40
3 | 2022-09-14..2022-12-09 | 55 | $-8,342.40 | $17,071.68 | $17,071.68 | $17,246.88 | $17,246.88 | $17,246.88 | $18,121.36 | $18,296.56 | $17,071.68 | $18,121.36
4 | 2022-12-12..2023-03-10 | 65 | $1,820.80 | $5,413.92 | $5,093.60 | $13,033.12 | $12,037.80 | $13,033.12 | $5,988.92 | $13,657.80 | $4,515.52 | $5,140.20
5 | 2023-03-13..2023-06-08 | 54 | $22,182.28 | $2,812.44 | $2,711.80 | $9,005.84 | $9,005.84 | $9,005.84 | $3,117.12 | $9,405.52 | $2,309.04 | $2,708.72
6 | 2023-06-09..2023-09-05 | 55 | $5,142.60 | $4,858.40 | $4,282.76 | $4,858.40 | $4,282.76 | $4,858.40 | $6,028.08 | $6,028.08 | $4,398.60 | $4,713.60
7 | 2023-09-06..2023-12-01 | 52 | $6,261.64 | $4,533.40 | $4,533.40 | $4,533.40 | $4,533.40 | $4,533.40 | $4,822.76 | $4,822.76 | $3,577.76 | $4,693.08
8 | 2023-12-04..2024-03-01 | 63 | $-869.84 | $6,447.72 | $5,471.76 | $7,406.76 | $6,666.12 | $7,406.76 | $6,592.40 | $7,551.44 | $6,212.40 | $6,357.08
9 | 2024-03-04..2024-05-30 | 60 | $8,249.20 | $9,994.76 | $8,935.08 | $9,994.76 | $8,935.08 | $9,994.76 | $10,779.76 | $10,779.76 | $6,748.80 | $7,533.80
10 | 2024-05-31..2024-08-27 | 55 | $19,157.60 | $8,148.08 | $8,148.08 | $8,148.08 | $8,148.08 | $8,148.08 | $8,673.08 | $8,673.08 | $3,564.36 | $4,664.04
11 | 2024-08-28..2024-11-22 | 53 | $6,886.96 | $9,160.84 | $9,160.84 | $9,160.84 | $9,160.84 | $9,160.84 | $9,890.84 | $9,890.84 | $604.36 | $2,314.36
12 | 2024-11-25..2025-02-25 | 55 | $18,932.60 | $8,452.96 | $7,907.64 | $8,452.96 | $7,907.64 | $8,452.96 | $9,522.32 | $9,522.32 | $0.00 | $34.68
13 | 2025-02-26..2025-05-27 | 56 | $19,932.92 | $11,168.08 | $10,158.08 | $11,168.08 | $10,158.08 | $11,168.08 | $12,288.08 | $12,288.08 | $7,398.80 | $8,488.80
14 | 2025-05-28..2025-08-22 | 54 | $-4,907.72 | $12,897.84 | $10,647.52 | $22,901.76 | $19,786.12 | $22,901.76 | $13,132.52 | $23,136.44 | $12,897.84 | $13,132.52
15 | 2025-08-25..2025-11-20 | 59 | $4,598.88 | $14,888.60 | $14,583.28 | $28,268.64 | $27,098.00 | $28,268.64 | $15,389.56 | $28,769.60 | $13,357.00 | $13,857.96
16 | 2025-11-21..2026-03-09 | 59 | $-23,511.12 | $26,942.08 | $26,942.08 | $34,869.20 | $34,003.88 | $34,869.20 | $28,101.76 | $36,028.88 | $24,556.44 | $25,716.12
17 | 2026-03-10..2026-06-05 | 59 | $7,123.88 | $22,249.44 | $22,249.44 | $41,065.32 | $40,200.00 | $41,065.32 | $25,629.12 | $44,445.00 | $7,241.44 | $10,621.12
MAX over windows: WORST4 $41,065.32 | MAE-incl $44,445.00 | static_ct $24,556.44 | static_mae $25,716.12

=== TIER TABLE @ 1 MNQ | NO CAP | measure WIN ===
tier | ceiling | BASELINE BandOrVWAP: worst window, verdict (windows below ceiling) | OPPBAND: worst window, verdict (windows below ceiling) | FLAT1559: worst window, verdict (windows below ceiling)
Studio #003 5K [trailing measure = stricter] | $160.00 | $2,913.90 FAIL (0/17) | $2,786.70 FAIL (0/17) | $2,774.40 FAIL (0/17)
Studio #003 5K [static measure, shown] | $160.00 | $2,701.20 FAIL (4/17) | $2,723.00 FAIL (3/17) | $2,538.70 FAIL (4/17)
Studio #001 10K [trailing measure = stricter] | $320.00 | $2,913.90 FAIL (1/17) | $2,786.70 FAIL (0/17) | $2,774.40 FAIL (1/17)
Studio #001 10K [static measure, shown] | $320.00 | $2,701.20 FAIL (5/17) | $2,723.00 FAIL (4/17) | $2,538.70 FAIL (5/17)
Studio #002 20K [trailing measure = stricter] | $640.00 | $2,913.90 FAIL (4/17) | $2,786.70 FAIL (0/17) | $2,774.40 FAIL (4/17)
Studio #002 20K [static measure, shown] | $640.00 | $2,701.20 FAIL (9/17) | $2,723.00 FAIL (6/17) | $2,538.70 FAIL (9/17)
Rapid 25K [Eval EOD] | $800.00 | $2,913.90 FAIL (6/17) | $2,786.70 FAIL (0/17) | $2,774.40 FAIL (6/17)
Rapid 25K [SimF intraday] | $800.00 | $3,031.30 FAIL (5/17) | $3,259.10 FAIL (0/17) | $2,891.80 FAIL (6/17)
Rapid EOD 25K | $800.00 | $2,913.90 FAIL (6/17) | $2,786.70 FAIL (0/17) | $2,774.40 FAIL (6/17)
Builder 25K | $800.00 | $2,913.90 FAIL (6/17) | $2,786.70 FAIL (0/17) | $2,774.40 FAIL (6/17)
Rapid 50K [Eval EOD] | $1,600.00 | $2,913.90 FAIL (13/17) | $2,786.70 FAIL (13/17) | $2,774.40 FAIL (14/17)
Rapid 50K [SimF intraday] | $1,600.00 | $3,031.30 FAIL (13/17) | $3,259.10 FAIL (12/17) | $2,891.80 FAIL (14/17)
Rapid EOD 50K | $1,600.00 | $2,913.90 FAIL (13/17) | $2,786.70 FAIL (13/17) | $2,774.40 FAIL (14/17)
Pro 50K | $1,600.00 | $2,913.90 FAIL (13/17) | $2,786.70 FAIL (13/17) | $2,774.40 FAIL (14/17)
Builder 50K | $1,600.00 | $2,913.90 FAIL (13/17) | $2,786.70 FAIL (13/17) | $2,774.40 FAIL (14/17)
Builder 50K add-on | $1,200.00 | $2,913.90 FAIL (12/17) | $2,786.70 FAIL (9/17) | $2,774.40 FAIL (12/17)
Rapid 100K [Eval EOD] | $2,400.00 | $2,913.90 FAIL (16/17) | $2,786.70 FAIL (15/17) | $2,774.40 FAIL (16/17)
Rapid 100K [SimF intraday] | $2,400.00 | $3,031.30 FAIL (15/17) | $3,259.10 FAIL (14/17) | $2,891.80 FAIL (15/17)
Pro 100K | $2,400.00 | $2,913.90 FAIL (16/17) | $2,786.70 FAIL (15/17) | $2,774.40 FAIL (16/17)
Builder 100K | $2,400.00 | $2,913.90 FAIL (16/17) | $2,786.70 FAIL (15/17) | $2,774.40 FAIL (16/17)
Rapid 150K [Eval EOD] | $3,600.00 | $2,913.90 PASS (17/17) | $2,786.70 PASS (17/17) | $2,774.40 PASS (17/17)
Rapid 150K [SimF intraday] | $3,600.00 | $3,031.30 PASS (17/17) | $3,259.10 PASS (17/17) | $2,891.80 PASS (17/17)
Pro 150K | $3,600.00 | $2,913.90 PASS (17/17) | $2,786.70 PASS (17/17) | $2,774.40 PASS (17/17)
Builder 150K | $3,600.00 | $2,913.90 PASS (17/17) | $2,786.70 PASS (17/17) | $2,774.40 PASS (17/17)

=== TIER TABLE @ 1 NQ | NO CAP | measure WIN ===
tier | ceiling | BASELINE BandOrVWAP: worst window, verdict (windows below ceiling) | OPPBAND: worst window, verdict (windows below ceiling) | FLAT1559: worst window, verdict (windows below ceiling)
Studio #003 5K [trailing measure = stricter] | $160.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Studio #003 5K [static measure, shown] | $160.00 | $26,181.44 FAIL (1/17) | $26,728.80 FAIL (1/17) | $24,556.44 FAIL (1/17)
Studio #001 10K [trailing measure = stricter] | $320.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Studio #001 10K [static measure, shown] | $320.00 | $26,181.44 FAIL (1/17) | $26,728.80 FAIL (1/17) | $24,556.44 FAIL (1/17)
Studio #002 20K [trailing measure = stricter] | $640.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Studio #002 20K [static measure, shown] | $640.00 | $26,181.44 FAIL (1/17) | $26,728.80 FAIL (2/17) | $24,556.44 FAIL (2/17)
Rapid 25K [Eval EOD] | $800.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Rapid 25K [SimF intraday] | $800.00 | $29,496.76 FAIL (0/17) | $32,104.12 FAIL (0/17) | $28,101.76 FAIL (0/17)
Rapid EOD 25K | $800.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Builder 25K | $800.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Rapid 50K [Eval EOD] | $1,600.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Rapid 50K [SimF intraday] | $1,600.00 | $29,496.76 FAIL (0/17) | $32,104.12 FAIL (0/17) | $28,101.76 FAIL (0/17)
Rapid EOD 50K | $1,600.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Pro 50K | $1,600.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Builder 50K | $1,600.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Builder 50K add-on | $1,200.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Rapid 100K [Eval EOD] | $2,400.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Rapid 100K [SimF intraday] | $2,400.00 | $29,496.76 FAIL (0/17) | $32,104.12 FAIL (0/17) | $28,101.76 FAIL (0/17)
Pro 100K | $2,400.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Builder 100K | $2,400.00 | $28,337.08 FAIL (0/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (0/17)
Rapid 150K [Eval EOD] | $3,600.00 | $28,337.08 FAIL (1/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (1/17)
Rapid 150K [SimF intraday] | $3,600.00 | $29,496.76 FAIL (1/17) | $32,104.12 FAIL (0/17) | $28,101.76 FAIL (1/17)
Pro 150K | $3,600.00 | $28,337.08 FAIL (1/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (1/17)
Builder 150K | $3,600.00 | $28,337.08 FAIL (1/17) | $27,394.44 FAIL (0/17) | $26,942.08 FAIL (1/17)

=== TIER TABLE @ 1 MNQ | NO CAP | measure VS4 ===
tier | ceiling | BASELINE BandOrVWAP: worst window, verdict (windows below ceiling) | OPPBAND: worst window, verdict (windows below ceiling) | FLAT1559: worst window, verdict (windows below ceiling)
Studio #003 5K [trailing measure = stricter] | $160.00 | $4,927.60 FAIL (0/17) | $5,280.20 FAIL (0/17) | $4,463.10 FAIL (0/17)
Studio #003 5K [static measure, shown] | $160.00 | $2,701.20 FAIL (4/17) | $2,723.00 FAIL (3/17) | $2,538.70 FAIL (4/17)
Studio #001 10K [trailing measure = stricter] | $320.00 | $4,927.60 FAIL (0/17) | $5,280.20 FAIL (0/17) | $4,463.10 FAIL (0/17)
Studio #001 10K [static measure, shown] | $320.00 | $2,701.20 FAIL (5/17) | $2,723.00 FAIL (4/17) | $2,538.70 FAIL (5/17)
Studio #002 20K [trailing measure = stricter] | $640.00 | $4,927.60 FAIL (2/17) | $5,280.20 FAIL (0/17) | $4,463.10 FAIL (2/17)
Studio #002 20K [static measure, shown] | $640.00 | $2,701.20 FAIL (9/17) | $2,723.00 FAIL (6/17) | $2,538.70 FAIL (9/17)
Rapid 25K [Eval EOD] | $800.00 | $4,927.60 FAIL (4/17) | $5,280.20 FAIL (0/17) | $4,463.10 FAIL (3/17)
Rapid 25K [SimF intraday] | $800.00 | $5,267.00 FAIL (3/17) | $5,525.30 FAIL (0/17) | $4,802.50 FAIL (3/17)
Rapid EOD 25K | $800.00 | $4,927.60 FAIL (4/17) | $5,280.20 FAIL (0/17) | $4,463.10 FAIL (3/17)
Builder 25K | $800.00 | $4,927.60 FAIL (4/17) | $5,280.20 FAIL (0/17) | $4,463.10 FAIL (3/17)
Rapid 50K [Eval EOD] | $1,600.00 | $4,927.60 FAIL (12/17) | $5,280.20 FAIL (12/17) | $4,463.10 FAIL (12/17)
Rapid 50K [SimF intraday] | $1,600.00 | $5,267.00 FAIL (12/17) | $5,525.30 FAIL (12/17) | $4,802.50 FAIL (12/17)
Rapid EOD 50K | $1,600.00 | $4,927.60 FAIL (12/17) | $5,280.20 FAIL (12/17) | $4,463.10 FAIL (12/17)
Pro 50K | $1,600.00 | $4,927.60 FAIL (12/17) | $5,280.20 FAIL (12/17) | $4,463.10 FAIL (12/17)
Builder 50K | $1,600.00 | $4,927.60 FAIL (12/17) | $5,280.20 FAIL (12/17) | $4,463.10 FAIL (12/17)
Builder 50K add-on | $1,200.00 | $4,927.60 FAIL (11/17) | $5,280.20 FAIL (8/17) | $4,463.10 FAIL (11/17)
Rapid 100K [Eval EOD] | $2,400.00 | $4,927.60 FAIL (14/17) | $5,280.20 FAIL (12/17) | $4,463.10 FAIL (14/17)
Rapid 100K [SimF intraday] | $2,400.00 | $5,267.00 FAIL (14/17) | $5,525.30 FAIL (12/17) | $4,802.50 FAIL (14/17)
Pro 100K | $2,400.00 | $4,927.60 FAIL (14/17) | $5,280.20 FAIL (12/17) | $4,463.10 FAIL (14/17)
Builder 100K | $2,400.00 | $4,927.60 FAIL (14/17) | $5,280.20 FAIL (12/17) | $4,463.10 FAIL (14/17)
Rapid 150K [Eval EOD] | $3,600.00 | $4,927.60 FAIL (15/17) | $5,280.20 FAIL (14/17) | $4,463.10 FAIL (15/17)
Rapid 150K [SimF intraday] | $3,600.00 | $5,267.00 FAIL (15/17) | $5,525.30 FAIL (14/17) | $4,802.50 FAIL (15/17)
Pro 150K | $3,600.00 | $4,927.60 FAIL (15/17) | $5,280.20 FAIL (14/17) | $4,463.10 FAIL (15/17)
Builder 150K | $3,600.00 | $4,927.60 FAIL (15/17) | $5,280.20 FAIL (14/17) | $4,463.10 FAIL (15/17)

=== TIER TABLE @ 1 NQ | NO CAP | measure VS4 ===
tier | ceiling | BASELINE BandOrVWAP: worst window, verdict (windows below ceiling) | OPPBAND: worst window, verdict (windows below ceiling) | FLAT1559: worst window, verdict (windows below ceiling)
Studio #003 5K [trailing measure = stricter] | $160.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Studio #003 5K [static measure, shown] | $160.00 | $26,181.44 FAIL (1/17) | $26,728.80 FAIL (1/17) | $24,556.44 FAIL (1/17)
Studio #001 10K [trailing measure = stricter] | $320.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Studio #001 10K [static measure, shown] | $320.00 | $26,181.44 FAIL (1/17) | $26,728.80 FAIL (1/17) | $24,556.44 FAIL (1/17)
Studio #002 20K [trailing measure = stricter] | $640.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Studio #002 20K [static measure, shown] | $640.00 | $26,181.44 FAIL (1/17) | $26,728.80 FAIL (2/17) | $24,556.44 FAIL (2/17)
Rapid 25K [Eval EOD] | $800.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Rapid 25K [SimF intraday] | $800.00 | $49,090.00 FAIL (0/17) | $53,164.04 FAIL (0/17) | $44,445.00 FAIL (0/17)
Rapid EOD 25K | $800.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Builder 25K | $800.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Rapid 50K [Eval EOD] | $1,600.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Rapid 50K [SimF intraday] | $1,600.00 | $49,090.00 FAIL (0/17) | $53,164.04 FAIL (0/17) | $44,445.00 FAIL (0/17)
Rapid EOD 50K | $1,600.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Pro 50K | $1,600.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Builder 50K | $1,600.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Builder 50K add-on | $1,200.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Rapid 100K [Eval EOD] | $2,400.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Rapid 100K [SimF intraday] | $2,400.00 | $49,090.00 FAIL (0/17) | $53,164.04 FAIL (0/17) | $44,445.00 FAIL (0/17)
Pro 100K | $2,400.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Builder 100K | $2,400.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Rapid 150K [Eval EOD] | $3,600.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Rapid 150K [SimF intraday] | $3,600.00 | $49,090.00 FAIL (0/17) | $53,164.04 FAIL (0/17) | $44,445.00 FAIL (0/17)
Pro 150K | $3,600.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)
Builder 150K | $3,600.00 | $45,710.32 FAIL (0/17) | $50,969.04 FAIL (0/17) | $41,065.32 FAIL (0/17)

=== D7 test: 1 MNQ, no cap, all 17 tier rows (Rapid: both stages) ===
WIN | BASELINE BandOrVWAP: rows passing = ['Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] -> does NOT fail every tier
WIN | OPPBAND: rows passing = ['Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] -> does NOT fail every tier
WIN | FLAT1559: rows passing = ['Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] -> does NOT fail every tier
VS4 | BASELINE BandOrVWAP: rows passing = NONE -> FAILS EVERY TIER
VS4 | OPPBAND: rows passing = NONE -> FAILS EVERY TIER
VS4 | FLAT1559: rows passing = NONE -> FAILS EVERY TIER
1 NQ, no cap, rows passing: {('WIN', 'BASELINE BandOrVWAP'): 'NONE', ('WIN', 'OPPBAND'): 'NONE', ('WIN', 'FLAT1559'): 'NONE', ('VS4', 'BASELINE BandOrVWAP'): 'NONE', ('VS4', 'OPPBAND'): 'NONE', ('VS4', 'FLAT1559'): 'NONE'}

=== SENSITIVITY ONLY: round daily-loss caps. Not breaker values, not recommendations (D7). ===
cap $100 @1 MNQ | BASELINE BandOrVWAP | trades skipped 166 | max WIN $2,290.70 rows passing ['Rapid 100K [Eval EOD]', 'Pro 100K', 'Builder 100K', 'Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] | max VS4 $4,626.90 rows passing NONE
cap $100 @1 MNQ | OPPBAND | trades skipped 18 | max WIN $2,786.70 rows passing ['Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] | max VS4 $4,961.40 rows passing NONE
cap $100 @1 MNQ | FLAT1559 | trades skipped 166 | max WIN $2,156.20 rows passing ['Rapid 100K [Eval EOD]', 'Rapid 100K [SimF intraday]', 'Pro 100K', 'Builder 100K', 'Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] | max VS4 $4,054.40 rows passing NONE
cap $200 @1 MNQ | BASELINE BandOrVWAP | trades skipped 54 | max WIN $2,237.00 rows passing ['Rapid 100K [Eval EOD]', 'Rapid 100K [SimF intraday]', 'Pro 100K', 'Builder 100K', 'Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] | max VS4 $4,957.30 rows passing NONE
cap $200 @1 MNQ | OPPBAND | trades skipped 18 | max WIN $2,786.70 rows passing ['Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] | max VS4 $4,961.40 rows passing NONE
cap $200 @1 MNQ | FLAT1559 | trades skipped 54 | max WIN $2,089.80 rows passing ['Rapid 100K [Eval EOD]', 'Rapid 100K [SimF intraday]', 'Pro 100K', 'Builder 100K', 'Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] | max VS4 $4,372.30 rows passing NONE
cap $300 @1 MNQ | BASELINE BandOrVWAP | trades skipped 24 | max WIN $2,725.10 rows passing ['Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] | max VS4 $5,849.40 rows passing NONE
cap $300 @1 MNQ | OPPBAND | trades skipped 18 | max WIN $2,786.70 rows passing ['Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] | max VS4 $4,961.40 rows passing NONE
cap $300 @1 MNQ | FLAT1559 | trades skipped 24 | max WIN $2,585.60 rows passing ['Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] | max VS4 $5,310.70 rows passing NONE
cap $500 @1 MNQ | BASELINE BandOrVWAP | trades skipped 4 | max WIN $2,913.90 rows passing ['Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] | max VS4 $6,202.60 rows passing NONE
cap $500 @1 MNQ | OPPBAND | trades skipped 12 | max WIN $2,786.70 rows passing ['Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] | max VS4 $4,961.40 rows passing NONE
cap $500 @1 MNQ | FLAT1559 | trades skipped 4 | max WIN $2,774.40 rows passing ['Rapid 150K [Eval EOD]', 'Rapid 150K [SimF intraday]', 'Pro 150K', 'Builder 150K'] | max VS4 $5,756.90 rows passing NONE
cap $1000 @1 NQ | BASELINE BandOrVWAP | trades skipped 164 | max WIN $22,291.24 rows passing NONE | max VS4 $42,668.76 rows passing NONE
cap $1000 @1 NQ | OPPBAND | trades skipped 18 | max WIN $27,394.44 rows passing NONE | max VS4 $47,809.68 rows passing NONE
cap $1000 @1 NQ | FLAT1559 | trades skipped 164 | max WIN $20,946.24 rows passing NONE | max VS4 $36,898.76 rows passing NONE
cap $2000 @1 NQ | BASELINE BandOrVWAP | trades skipped 53 | max WIN $21,686.36 rows passing NONE | max VS4 $47,425.44 rows passing NONE
cap $2000 @1 NQ | OPPBAND | trades skipped 18 | max WIN $27,394.44 rows passing NONE | max VS4 $47,809.68 rows passing NONE
cap $2000 @1 NQ | FLAT1559 | trades skipped 53 | max WIN $21,134.76 rows passing NONE | max VS4 $41,575.44 rows passing NONE
cap $3000 @1 NQ | BASELINE BandOrVWAP | trades skipped 24 | max WIN $26,477.72 rows passing NONE | max VS4 $54,613.28 rows passing NONE
cap $3000 @1 NQ | OPPBAND | trades skipped 18 | max WIN $27,394.44 rows passing NONE | max VS4 $47,809.68 rows passing NONE
cap $3000 @1 NQ | FLAT1559 | trades skipped 24 | max WIN $25,082.72 rows passing NONE | max VS4 $49,197.64 rows passing NONE
cap $5000 @1 NQ | BASELINE BandOrVWAP | trades skipped 4 | max WIN $28,337.08 rows passing NONE | max VS4 $57,959.12 rows passing NONE
cap $5000 @1 NQ | OPPBAND | trades skipped 12 | max WIN $27,394.44 rows passing NONE | max VS4 $47,809.68 rows passing NONE
cap $5000 @1 NQ | FLAT1559 | trades skipped 4 | max WIN $26,942.08 rows passing NONE | max VS4 $53,473.48 rows passing NONE
```

## Appendix B — scripts, verbatim

`/tmp/d6/d6.py`:

```python
#!/usr/bin/env python3
# D6 drawdown viability check (unit 2026-11-09-d6-drawdown-check). Read-only. Run:
#   python3 -I -B /tmp/d6/d6.py
# Reuses scripts/wf/sessions.py (calendar, windows) and scripts/wf/report.py
# (four_measure_drawdowns) read-only via import; -B stops __pycache__ writes.
import csv, hashlib, json, sys
from decimal import Decimal
from fractions import Fraction
from datetime import datetime

REPO = "/Volumes/Sensidine/Praxis.build"
sys.path.insert(0, REPO + "/scripts/wf")
import sessions as S          # noqa: E402
import report as R            # noqa: E402

DATA = "/Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt"
DESK = "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 %s.csv"
RUNS = [("BASELINE BandOrVWAP", DESK % "07-10 AM", "421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd", 1190),
        ("OPPBAND", DESK % "07-57 AM", "4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8", 810),
        ("FLAT1559", DESK % "07-59 AM", "5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0", 1190)]

cm = json.load(open(REPO + "/config/backtest-cost-model.json"))
C = cm["cost_model"]
assert cm["version"] == "1.2.0"
COMM = {"NQ": Fraction(str(C["commission_round_turn_usd"])), "MNQ": Fraction(str(C["commission_round_turn_usd_mnq"]))}
PV = {"NQ": Fraction(20), "MNQ": Fraction(2)}   # NQ from cost model; MNQ = NQ/10 (values-spec :139)
assert Fraction(str(cm["instrument"]["point_value_usd"])) == 20
CSV_COMM = Fraction("2.96")
print("cost model version", cm["version"], "| NQ RT", float(COMM["NQ"]), "| MNQ RT", float(COMM["MNQ"]),
      "| tick", cm["instrument"]["tick_size"], "| NQ $/pt", cm["instrument"]["point_value_usd"],
      "| slippage ticks/side", C["slippage_ticks_per_side"], "(already in NT8 fills; not added again)")

# ---------- tier rows: WF spec HEAD :115-130; A4 = below min(3.2% size, 80% limit) ----------
TIERS = [("Studio #003 5K", 5000, 250, "Static"), ("Studio #001 10K", 10000, 500, "Static"),
         ("Studio #002 20K", 20000, 1000, "Static"),
         ("Rapid 25K", 25000, 1000, "Eval EOD / SimF intraday"), ("Rapid EOD 25K", 25000, 1000, "EOD"),
         ("Builder 25K", 25000, 1000, "EOD"),
         ("Rapid 50K", 50000, 2000, "Eval EOD / SimF intraday"), ("Rapid EOD 50K", 50000, 2000, "EOD"),
         ("Pro 50K", 50000, 2000, "EOD"), ("Builder 50K", 50000, 2000, "EOD"),
         ("Builder 50K add-on", 50000, 1500, "EOD"),
         ("Rapid 100K", 100000, 3000, "Eval EOD / SimF intraday"), ("Pro 100K", 100000, 3000, "EOD"),
         ("Builder 100K", 100000, 3000, "EOD"),
         ("Rapid 150K", 150000, 4500, "Eval EOD / SimF intraday"), ("Pro 150K", 150000, 4500, "EOD"),
         ("Builder 150K", 150000, 4500, "EOD")]


def ceiling(size, limit):
    return min(Fraction(32, 1000) * size, Fraction(8, 10) * limit)


def money(x):
    return "${:,.2f}".format(float(x))


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def t(s):
    return datetime.strptime(s.strip(), "%Y-%m-%d %I:%M:%S %p")


def load(path):
    rows = list(csv.reader(open(path, encoding="utf-8-sig", newline="")))
    hdr = rows[0]
    ix = {h: i for i, h in enumerate(hdr)}
    out, bad = [], 0
    for r in rows[1:]:
        if not any(c.strip() for c in r):
            continue
        side = r[ix["Market pos."]].strip()
        sgn = 1 if side == "Long" else -1
        assert side in ("Long", "Short") and int(r[ix["Qty"]]) == 1
        pts = (Fraction(r[ix["Exit price"]]) - Fraction(r[ix["Entry price"]])) * sgn
        prof = Fraction(r[ix["Profit"]].replace("$", "").replace(",", ""))
        comm = Fraction(r[ix["Commission"]].replace("$", ""))
        mae = Fraction(r[ix["MAE"]].replace("$", "").replace(",", ""))
        if prof != pts * 20 - comm or comm != CSV_COMM:
            bad += 1
        en, ex = t(r[ix["Entry time"]]), t(r[ix["Exit time"]])
        out.append({"en": en, "ex": ex, "pts": pts, "csv_profit": prof, "mae_nq": mae})
    return out, bad


def dd(points, eq0=Fraction(0), pk0=Fraction(0)):
    return R._dd_series(points, eq0, pk0)


# ---------- calendar ----------
print("data sha256", sha(DATA))
cal = S.build_calendar(DATA)
dates = [s["date"] for s in cal["sessions"]]
d2n = {d: i + 1 for i, d in enumerate(dates)}
print("N sessions", cal["N"], "first", dates[0], "last", dates[-1], "K", cal["K"], "dropped", cal["dropped"], cal["dropped_dates"])
W = cal["windows"]

results = {}
for name, path, want, n in RUNS:
    got = sha(path)
    trades, bad = load(path)
    print("\n=== %s | sha256 %s | %s | rows %d (expect %d) | Profit != pts*20-2.96 rows: %d" %
          (name, got, "MATCH" if got == want else "MISMATCH", len(trades), n, bad))
    assert got == want and len(trades) == n
    trades.sort(key=lambda x: (x["ex"], x["en"]))
    # sanity: same-day trades, every exit date a session
    cross = sum(1 for x in trades if x["en"].date() != x["ex"].date())
    nosess = sum(1 for x in trades if x["ex"].date().isoformat() not in d2n)
    maebad = sum(1 for x in trades if x["mae_nq"] < max(Fraction(0), -x["pts"] * 20))
    print("entry date != exit date: %d | exit date not a session: %d | MAE < closed loss (impossible if MAE is worst excursion): %d" % (cross, nosess, maebad))
    # full-span check vs committed results report :402-404 (CSV basis, closed-trade, from 0)
    fs = dd([x["csv_profit"] for x in trades])[0]
    print("full-span closed-trade max DD on CSV Profit (cost $2.96): -%s ; net %s" % (money(fs), money(sum(x["csv_profit"] for x in trades))))
    results[name] = {"trades": trades}

CAPS = {"MNQ": [None, 100, 200, 300, 500], "NQ": [None, 1000, 2000, 3000, 5000]}


def apply_cap(trades, inst, cap):
    """Rule: within a session (trades in exit order), once the day's realised net reaches -cap
    or worse, no further trade that day; the breaching trade counts in full."""
    if cap is None:
        return trades, 0
    kept, day, cum, stopped, skipped = [], None, Fraction(0), False, 0
    for x in trades:
        d = x["ex"].date()
        if d != day:
            day, cum, stopped = d, Fraction(0), False
        if stopped:
            skipped += 1
            continue
        kept.append(x)
        cum += x["pts"] * PV[inst] - COMM[inst]
        if cum <= -cap:
            stopped = True
    return kept, skipped


def window_measures(trades, inst):
    net = lambda x: x["pts"] * PV[inst] - COMM[inst]
    pw_tr, pw_daily, pw_mae = [], [], []
    for w in W:
        c, d = w["oos"]
        tr = [x for x in trades if c <= d2n[x["ex"].date().isoformat()] <= d]
        daily = []
        for s in range(c, d + 1):
            daily.append(sum((net(x) for x in tr if d2n[x["ex"].date().isoformat()] == s), Fraction(0)))
        pw_tr.append([net(x) for x in tr])
        pw_daily.append(daily)
        # intratrade points: low = equity before trade - MAE (scaled) - round-turn commission, then close
        pts = []
        for x in tr:
            pts.append(("low", -(x["mae_nq"] * PV[inst] / 20) - COMM[inst]))
            pts.append(("close", net(x)))
        pw_mae.append(pts)
    four = R.four_measure_drawdowns(pw_tr, pw_daily)
    eq = pk = Fraction(0)
    for k, w in enumerate(W):
        # MAE-inclusive, from window start and carried
        def run(e0, p0):
            e, p, m, base = e0, p0, p0 - e0, e0
            for kind, v in pw_mae[k]:
                if kind == "low":
                    lo = e + v
                    m = max(m, p - lo)
                else:
                    e = e + v
                    p = max(p, e)
                    m = max(m, p - e)
            return m, e, p
        ms = run(Fraction(0), Fraction(0))[0]
        mc, eq, pk = run(eq, pk)
        four[k]["mae_start"], four[k]["mae_carry"] = ms, mc
        # static: worst closed-trade / intratrade level below the window-start balance
        e, lo_c, lo_m = Fraction(0), Fraction(0), Fraction(0)
        for kind, v in pw_mae[k]:
            if kind == "low":
                lo_m = min(lo_m, e + v)
            else:
                e += v
                lo_c = min(lo_c, e)
                lo_m = min(lo_m, e)
        four[k]["static_ct"], four[k]["static_mae"] = -lo_c, -lo_m
        four[k]["n"] = len(pw_tr[k])
        four[k]["net"] = sum(pw_tr[k], Fraction(0))
        four[k]["mae_worst"] = max(ms, mc)
    return four


ALL = {}
for name in results:
    for inst in ("MNQ", "NQ"):
        for cap in CAPS[inst]:
            tr, skipped = apply_cap(results[name]["trades"], inst, cap)
            ALL[(name, inst, cap)] = (window_measures(tr, inst), skipped)

# ---------- per-window table, no cap ----------
for name in results:
    for inst in ("MNQ", "NQ"):
        m, _ = ALL[(name, inst, None)]
        print("\n--- %s @ 1 %s, no cap: per OOS window (dollars) ---" % (name, inst))
        print("k | OOS dates | trades | net | ct_start | eod_start | ct_carry | eod_carry | WORST4 | mae_start | mae_carry | static_ct | static_mae")
        for k, w in enumerate(W):
            r = m[k]
            print("%d | %s..%s | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s" % (
                w["k"], w["oos_dates"][0], w["oos_dates"][1], r["n"], money(r["net"]), money(r["ct_start"]),
                money(r["eod_start"]), money(r["ct_carry"]), money(r["eod_carry"]), money(r["worst"]),
                money(r["mae_start"]), money(r["mae_carry"]), money(r["static_ct"]), money(r["static_mae"])))
        print("MAX over windows: WORST4 %s | MAE-incl %s | static_ct %s | static_mae %s" % (
            money(max(r["worst"] for r in m)), money(max(r["mae_worst"] for r in m)),
            money(max(r["static_ct"] for r in m)), money(max(r["static_mae"] for r in m))))




# ======================= tier judgement (appended to d6.py head) =======================
# Two drawdown measures, both reported (manager's decision under D-2026-11-08-D D1, logged in report):
#  WIN  = within the window only (D6: "per-walk-forward-window worst drawdown"): max(ct_start, eod_start);
#         intraday stage adds mae_start.
#  VS4  = values-spec :139 worst of four (adds the two carried measures); intraday stage adds mae_worst.
def judged(r, kind, meas):
    if meas == "WIN":
        v = max(r["ct_start"], r["eod_start"])
        return max(v, r["mae_start"]) if kind == "SimF" else v
    v = r["worst"]
    return max(v, r["mae_worst"]) if kind == "SimF" else v


def rows_for(typ):
    if "SimF" in typ:
        return [(" [Eval EOD]", "EOD"), (" [SimF intraday]", "SimF")]
    if typ == "Static":
        return [(" [trailing measure = stricter]", "EOD")]
    return [("", "EOD")]


def tier_lines(inst, cap, meas):
    print("\n=== TIER TABLE @ 1 %s | %s | measure %s ===" % (
        inst, "NO CAP" if cap is None else "SENSITIVITY cap $%d/day (NOT a recommendation)" % cap, meas))
    print("tier | ceiling | " + " | ".join("%s: worst window, verdict (windows below ceiling)" % n for n in results))
    for tn, size, lim, typ in TIERS:
        ce = ceiling(size, lim)
        for lab, kind in rows_for(typ):
            cells = []
            for n in results:
                vals = [judged(r, kind, meas) for r in ALL[(n, inst, cap)][0]]
                ok = sum(1 for v in vals if v < ce)
                cells.append("%s %s (%d/17)" % (money(max(vals)), "PASS" if ok == 17 else "FAIL", ok))
            print("%s%s | %s | %s" % (tn, lab, money(ce), " | ".join(cells)))
        if typ == "Static" and cap is None:
            cells = []
            for n in results:
                vals = [r["static_ct"] for r in ALL[(n, inst, cap)][0]]
                ok = sum(1 for v in vals if v < ce)
                cells.append("%s %s (%d/17)" % (money(max(vals)), "PASS" if ok == 17 else "FAIL", ok))
            print("%s [static measure, shown] | %s | %s" % (tn, money(ce), " | ".join(cells)))


def passing(n, inst, cap, meas):
    out = []
    for tn, size, lim, typ in TIERS:
        ce = ceiling(size, lim)
        for lab, kind in rows_for(typ):
            if all(judged(r, kind, meas) < ce for r in ALL[(n, inst, cap)][0]):
                out.append(tn + lab)
    return out


for meas in ("WIN", "VS4"):
    for inst in ("MNQ", "NQ"):
        tier_lines(inst, None, meas)

print("\n=== D7 test: 1 MNQ, no cap, all 17 tier rows (Rapid: both stages) ===")
for meas in ("WIN", "VS4"):
    for n in results:
        p = passing(n, "MNQ", None, meas)
        print("%s | %s: rows passing = %s -> %s" % (meas, n, p if p else "NONE",
              "FAILS EVERY TIER" if not p else "does NOT fail every tier"))
print("1 NQ, no cap, rows passing:", {(meas, n): passing(n, "NQ", None, meas) or "NONE"
                                      for meas in ("WIN", "VS4") for n in results})

print("\n=== SENSITIVITY ONLY: round daily-loss caps. Not breaker values, not recommendations (D7). ===")
for inst in ("MNQ", "NQ"):
    for cap in CAPS[inst][1:]:
        for n in results:
            m, skipped = ALL[(n, inst, cap)]
            print("cap $%d @1 %s | %s | trades skipped %d | max WIN %s rows passing %s | max VS4 %s rows passing %s" % (
                cap, inst, n, skipped,
                money(max(judged(r, "EOD", "WIN") for r in m)), passing(n, inst, cap, "WIN") or "NONE",
                money(max(judged(r, "EOD", "VS4") for r in m)), passing(n, inst, cap, "VS4") or "NONE"))
```

`/tmp/d6/negtest.py`:

```python
#!/usr/bin/env python3
# Negative tests for the D6 gate logic. Functions copied verbatim from /tmp/d6/d6.py.
import sys
from fractions import Fraction
sys.path.insert(0, "/Volumes/Sensidine/Praxis.build/scripts/wf")
import report as R  # noqa: E402


def ceiling(size, limit):
    return min(Fraction(32, 1000) * size, Fraction(8, 10) * limit)


def verdict(vals, ce):
    ok = sum(1 for v in vals if v < ce)
    return "PASS" if ok == 17 else "FAIL"


ce = ceiling(150000, 4500)
print("ceiling Pro 150K =", float(ce))
print("17 windows all at ceiling - 0.01 ->", verdict([ce - Fraction(1, 100)] * 17, ce))
print("one window EXACTLY at ceiling (A4 says 'below') ->", verdict([ce] + [Fraction(0)] * 16, ce))
print("one window above ceiling ->", verdict([ce + 1] + [Fraction(0)] * 16, ce))
print("Builder 50K add-on ceiling (expect 1200 = 80% of 1500, not 1600) =", float(ceiling(50000, 1500)))
print("Studio 5K ceiling (expect 160 = 3.2% of 5000, not 200) =", float(ceiling(5000, 250)))
# drawdown function: +100, -300, +50, -100 -> peak 100, trough -250 -> DD 350
print("DD of [+100,-300,+50,-100] (expect 350) =", float(R._dd_series([Fraction(x) for x in (100, -300, 50, -100)])[0]))
# carried: a window starting 200 below its carried peak with no trades still shows 200
print("carried DD, empty window, start 200 below peak (expect 200) =", float(R._dd_series([], Fraction(-200), Fraction(0))[0]))
```

`/tmp/d6/cmp.py`:

```python
#!/usr/bin/env python3
# Compare W1's independent Flat1559 @1 MNQ table with the producer's output (/tmp/d6/out.txt).
L = open("/tmp/d6/out.txt").read().splitlines()
i = L.index("--- FLAT1559 @ 1 MNQ, no cap: per OOS window (dollars) ---")
mine = {}
for l in L[i + 2:i + 19]:
    c = [x.strip() for x in l.split("|")]
    num = lambda s: round(float(s.replace("$", "").replace(",", "")), 2)
    a, b = c[1].split("..")
    mine[int(c[0])] = (a, b, int(c[2]), num(c[3]), num(c[4]), num(c[5]))
match = mism = 0
for l in open("/tmp/d6/w1_table.txt"):
    c = [x.strip() for x in l.split("|")]
    k = int(c[0])
    w = (c[1], c[2], int(c[3]), round(float(c[4]), 2), round(float(c[5]), 2), round(float(c[6]), 2))
    if w == mine[k]:
        match += 1
    else:
        mism += 1
        print("MISMATCH k=%d worker=%r producer=%r" % (k, w, mine[k]))
print("fields compared per row: OOS first, OOS last, trades, net, DD closed-trade, DD end-of-day")
print("rows MATCH %d, MISMATCH %d" % (match, mism))
```

Result: PASS
