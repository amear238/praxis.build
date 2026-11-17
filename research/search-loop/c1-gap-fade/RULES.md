# C1 Opening Gap Fade — rules (written before any test)

Unit `2026-11-14-search-c1-gap-fade`, bead `Praxis_build-vn4`. Strategy search loop candidate 1. Mac-side Python PRE-SCREEN only (D-2026-11-14-A). A pre-screen result is never a contender result.

## Instrument and data
- NQ continuous, 1-minute bars, `/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt` (format `yyyyMMdd HHmmss;O;H;L;C;V`, no header). 1 contract. NQ point value $20; MNQ $2. Tick 0.25.

## Session definitions
- RTH bars: stamps 09:31 to 16:00 ET inclusive. A trading day is a date with a 09:31-stamped bar.
- PC (prior close): close of the last bar stamped at or before 16:00 in the previous trading day's RTH bars. Skip the day if the previous trading day is more than 4 calendar days back.
- O: open of the 09:31-stamped bar.
- gap_pct = (O - PC) / PC x 100.

## Entry
- If GMIN <= |gap_pct| <= GMAX, enter at O: SHORT if gap_pct > 0, LONG if gap_pct < 0.
- Entry fill = O worsened by 0.5 points (2 ticks).

## Exits
- Target: PC. Hit when a bar (the entry bar included) trades through PC by at least 1 tick: short needs low <= PC - 0.25; long needs high >= PC + 0.25. Exit fill = PC worsened by 0.5 points.
- Stop: distance = |O - PC|. Short stop = O + |O - PC|; long stop = O - |O - PC|. Hit when short high >= stop, long low <= stop. Exit fill = stop worsened by 0.5 points.
- If one bar hits both stop and target: the stop is taken.
- Time exit: if neither is hit, exit at the close of the last RTH bar of the day (normally the 16:00-stamped bar), worsened by 0.5 points.
- At most one trade per day. No other filter.

## Costs
- Every result reported at $2.96 and at $4.68 per round trip (NQ).
- 1 MNQ: the D6 check's method (`docs/reports/2026-11-09-d6-drawdown-check-manager.md` :50-52), quoted:
  - "Points per trade = (exit − entry) × side."
  - "NQ net = points × $20 − $4.68."
  - "MNQ net = points × $2 − $1.90 (cost model v1.2.0). This equals the committed rule "MNQ net = (NQ gross ÷ 10) − $1.90" (values spec :139). That this equals an own MNQ run is INFERRED there and here."

## Variants (no more)
- V1: GMIN 0.10, GMAX 0.50.
- V2: GMIN 0.20, GMAX 0.80.
- V3: GMIN 0.05, GMAX 0.30.

## Periods
- In-sample: 2021-03-08 to 2024-12-31.
- Holdout: 2025-01-01 to 2026-07-17.
- Full: 2021-03-08 to 2026-07-17.

## Selection (fixed now)
- Among variants with in-sample net > 0 at $4.68 AND in-sample profit factor >= 1.10, select the highest in-sample net at $4.68. Freeze it. Run it ONCE on the holdout and once on the full period.
- If no variant qualifies, the candidate FAILS in-sample; still run the highest in-sample-net variant once on holdout and full, labelled "for the record, not selected".

## Max drawdown
- Peak-to-trough of closed-trade cumulative P&L, plus every other measure the D6 report's "four-measure basis" uses, each computed as D6 defines it. D6's definitions, quoted:
  - D6 :20-21: "**WIN**: inside the window only. It is the worse of closed-trade and end-of-day equity, both reset to 0 at the window's start." "**VS4**: the committed values-spec measure (`git show HEAD:docs/specs/2026-11-06-walk-forward-values.md` :139). It is the worst of four: WIN's two, plus the same two carried across windows."
  - D6 :23: "For the Rapid Sim-Funded (intraday) rows, each measure also includes an MAE-based intratrade low (see Method)."
  - D6 :54: "Closed-trade equity and end-of-day equity. Intrabar equity is not in the trade list. The CSV's MAE column (NT8's worst excursion per trade, untimed, method UNVERIFIED) gives an intratrade low: equity before the trade − MAE − round-turn commission. That low is used only for the intraday (Rapid Sim-Funded) stage."
  - D6 :19: "Ceiling for each row = below min(3.2% of size, 80% of MFFU limit) (A4). Verdict = PASS only if all 17 windows are strictly below the ceiling."
- This candidate's trade list has no NT8 MAE column. The MAE used for the intratrade low is computed from the 1-minute bars of the trade (see the unit report's method section); it is a bar-based bound, not NT8's figure.
