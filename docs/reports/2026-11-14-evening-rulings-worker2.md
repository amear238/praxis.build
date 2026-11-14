# Evening rulings, worker 2: walk-forward spec vs the proposed contender bar

## Task
Research only. Compare the PROPOSED contender bar and overfitting guard (hermes handoff :59-:88) with the walk-forward spec and values at HEAD 9ff8a48, and with the DECISIONS.md R2/R3 and A7/A8 gates.

## Mode
BUILD (read-only research; this report is the only file written).

## Criterion
Answer Q1-Q4 with file:line quotes. Commands and outputs are pasted (S1). Each claim is graded OBSERVED or INFERRED. Conflicts are reported as findings and left unresolved.

## Process log
All reads used `git show HEAD:<path>` at HEAD 9ff8a48, except the handoff, which was read only at :59-:88 from the working tree (it is not in the "do not read the working tree" list). Line counts: WF spec 224, values 349 (OBSERVED). I used /usr/bin/grep, not the zsh grep. 12 tool calls.

Commands run, with outputs cut at 260 characters (the full transcripts are in this session's tool log). The extracts cited below are quoted exactly as they appeared in those outputs:
- `git rev-parse --short HEAD` -> `9ff8a48`. `git show HEAD:<spec> | wc -l` -> 224 and 349.
- `git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | /usr/bin/grep -n -i -E 'arm|noise|strategy|scope'` (and the same on the values file)
- `... | /usr/bin/grep -n -i -E 'in-sample|out-of-sample|IS |OOS|window|fold|anchor|2021|2025|2026|held|reserv|span|252|63'`
- `... | /usr/bin/grep -n -i -E 'gate|profit factor|PF|trades|WFE|efficiency|drawdown'`
- `... | /usr/bin/grep -n -i -E 'peer|publish'`, `'variant|grid|optimi|parameter'`, `'held.?out|reserv|holdout|untouched|lockbox'`, `'2\.96|4\.68|5\.76|commission'`
- `git show HEAD:DECISIONS.md | sed -n '1556,1560p;1735,1760p'`, plus an awk pass for the `## ` heading above each.

## Verification evidence (quotes, file:line at HEAD)

### Q1. Scope, span, windows, held-out period, limits on optimisation

**Scope.** OBSERVED:
- WF spec `:3`: "# Walk-forward test specification — NQ Noise-Area, arms (a) and (b)"
- WF spec `:17`: "9. Baseline `ninjascript/PraxisNoiseAreaBreakout.cs`."
- WF spec `:29` (D-2026-11-05-A item 1): "(a) paper's fixed rules, nothing optimised; (b) four parameters tuned per window — lookback, noise multiplier, stop-ATR multiplier, exit policy."
- Values `:29`: "The paper is Zarattini/Aziz/Barbon, SSRN 4824172"
- Values `:38`: "## 2. Arm (a) — fixed rules, the judged arm"
- Values `:42`: "**Judged arm = (a)** — RULED (ruling 4 of 2026-11-06: "judged arm = (a) fixed rules")"

Neither file mentions any other strategy (OBSERVED: the scope grep hits only Noise-Area arms (a) and (b)).

**Data span.** OBSERVED:
- WF spec `:87`: "inside the run-4 range 2021-03-08 → 2026-07-17 ... Monday–Friday dates only: **1,352**."
- Values `:83`: "inside the baseline range 2021-03-08 → 2026-07-17. Weekend-dated bars are excluded."

**Window lengths and fold design.** OBSERVED:
- WF spec `:30` (item 2): "2. Windows per spec: 252-day in-sample / 63-day out-of-sample / 63-day step."
- WF spec `:89`: "rolling, so window k's in-sample is sessions 63(k−1)+1 … 63(k−1)+252 and its out-of-sample is the next 63". The spec grades this INFERRED.
- Values `:82`: "**Partial last window dropped** — RULED".
- Values `:85`: "N = 1,352 (s1 = 2021-03-08, s1352 = 2026-07-17). K = 17; out-of-sample sessions = 1,071; **29 sessions dropped** (s1324–s1352, 2026-06-08 → 2026-07-17). Window 1: IS 2021-03-08 → 2022-03-16, OOS 2022-03-17 → 2022-06-15. Window 17: IS 2025-02-26 → 2026-03-09, OOS 2026-03-10 → 2026-06-05."
- Values `:87`: "the configuration picked on window k's in-sample is applied unchanged to window k's out-of-sample; the 17 out-of-sample segments are joined into arm (b)'s result. Alternative: an anchored (growing) in-sample window." The design is rolling, not anchored.
- Values `:43`: "arm (a) is run once over the full span and reported on the same 17 out-of-sample windows as arm (b) (§5), plus the full-span total."

**Held-out or reserved period.** None in either file (OBSERVED). The grep `held.?out|reserv|holdout|untouched|lockbox` returns no hits in the WF spec. In the values file its only hits are "preserved" (`:3`, `:11`, `:337`) and "untouched" in "F2 is untouched" (`:42`). None of them is a data period. The design uses every session from s1 to s1323 in some window. The last 29 sessions are dropped only because they fill no complete window, not because they are held out.

**Limits on optimisation, variants and grid size.** OBSERVED:
- Values `:17` (ruling 4 of 2026-11-06): "strictest reasonable defaults: small grid around the paper's published values (no wide search); ATR 14; ... in-sample objective = risk-adjusted return with a minimum trade count, never net profit; partial last window dropped; judged arm = (a) fixed rules; arm (b) counts only if it also passes PBO < 0.05."
- Values `:60`: "**Total grid: 3 × 3 × 3 × 3 = 81 configurations, all stop-on**". The file grades this INFERRED arithmetic from ruled counts.
- Values `:94`: minimum trade count "100 trades per 252-session in-sample window" (SETTLED).
- Values `:108`: "arm (b) counts only if **PBO < 0.05**".

So arm (a) has 0 tuned parameters, and arm (b) has a fixed 81-point grid that is re-selected in each of the 17 windows. Neither file has a "max N variants per idea" rule (OBSERVED).

### Q2. Block 2 pass gates compared with the PROPOSED bar

**Gates.** OBSERVED:
- WF spec `:153-:159`, REPORTED BY Phase 3 spec `:80-85`: "OOS profit factor ≥ 1.30" / "OOS Sharpe ≥ 1.0" / "Max drawdown ≤ 4% of equity" / "≥ 250 aggregate OOS trades" / "≥ 60% of walk-forward windows profitable" / "Walk-forward efficiency ≥ 0.50".
- Values `:121-:127` lists the same six. Values `:121` (Q8): "both arms are judged against all six Phase 3 gates; arm (b) must also pass PBO < 0.05."
- DECISIONS.md `:1556-:1558` (D-2026-11-08-A, heading `:1534`): "R2  GO requires arm (a) to pass. Arm (b) can only add confidence or block a GO; it can never carry a GO on its own" / "R3  Gate 6 (WFE) applies to arm (b) only".
- DECISIONS.md `:1735-:1740` (D-2026-11-08-B, heading `:1710`), A4: "Max-DD gate = backtest max drawdown must stay below 80% of the ruled limit, i.e. below the lower of 3.2% of the MFFU account size and 80% of MFFU's trailing drawdown limit. ... Evaluated against every tier row; tier pick stays Q9."
- DECISIONS.md `:1746-:1750`: "A7  R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not applicable). Arm (b) on gates 1-6 plus PBO < 0.05." / "A8  O1 is discharged by R2 + R3 + A7. Gate 6 formula (Pardo WFE): annualised OOS net profit / annualised IS net profit of the selected parameter set, pooled across all windows; pass >= 0.50."

**Item-by-item comparison** (bar = handoff `:73-:88`). The weaker/stronger judgments are INFERRED. The quotes are OBSERVED.

| Gate (WF / ledger) | Bar item | Judgment |
|---|---|---|
| OOS PF ≥ 1.30 (spec `:154`) | PF ≥ 1.10 over the full period (`:78`) | **Weaker** (1.10 < 1.30), and **a different measure**: full five years, including the tuning span, not aggregate out-of-sample. The bar sets no PF threshold on the held-out period, only "makes money". |
| OOS Sharpe ≥ 1.0 (`:155`) | none | **Missing** from the bar, so weaker. The Sharpe definition is still OPEN (values `:93`). |
| Max DD (spec `:156` "≤ 4% of equity"; amended by A4 `:1735-:1740` to below the lower of 3.2% and 80% of trailing) | "passes the drawdown gate at 1 MNQ for at least one MFFU account size", citing `:1735-:1740`, "four-measure basis" (`:77`) | **Same threshold as A4.** It is **weaker on coverage**: A4 says "Evaluated against every tier row; tier pick stays Q9", while the bar needs only one size to pass. It is **narrower on size**: the bar uses 1 MNQ only, while WF spec `:32` item 4 reports "1 MNQ and 1 NQ". Spec `:156` and values `:124` still carry the pre-A4 "4% of equity" wording (see finding F2). |
| ≥ 250 aggregate OOS trades (`:157`) | ≥ 200 trades over five years (`:79`) | **Weaker** (200 < 250), and **a different measure**: full period, not out-of-sample only. |
| ≥ 60% of WF windows profitable (`:158`) | profitable after costs over the full period and over the held-out period (`:78`) | **A different measure**: two segments instead of 17 windows. Its strength cannot be compared directly. |
| WFE ≥ 0.50, arm (b) only (R3 `:1558`, A8 formula `:1748-:1750`) | none; walk-forward "comes later" (`:88`) | **Deferred**, not at the contender stage. |
| PBO < 0.05 for tuned arm (b) (values `:108`, A7 `:1747`) | at most 3 variants, all logged (`:87`) | **A different control.** The variant cap is a weaker-to-different substitute for PBO: there is no statistical test of overfitting. |
| R2: GO needs the fixed-rules arm (`:1556`) | tuning is allowed on 2021-03-08..2024-12-31 (`:85`) | **Different.** A tuned contender corresponds to arm (b) semantics, which under R2 "can never carry a GO on its own". R2 is written for Noise-Area arms only. INFERRED. |
| Commission: WF runs at $4.68 NQ RT (values `:115`, "RULED (ruling 2 of 2026-11-06: "NQ $4.68")") | $4.68 (`:69`, `:76`) | **Same for NQ.** See finding F3 for MNQ. |

### Q3. Conflict check: reuse of the held-out period, and deviation from the spec

**F1 — contamination (INFERRED, from the OBSERVED boundaries at values `:85`).** Suppose the existing spec's 252/63/63 rolling design is later applied unchanged to a contender over 2021-03-08 → 2026-07-17. Then:

- **(a) The held-out period is reused as out-of-sample.** The joined OOS runs from 2022-03-17 to 2026-06-05. That covers the bar's held-out period 2025-01-01..2026-06-05, which falls in the out-of-sample segments of roughly the last five windows (about windows 12/13 to 17). The window index is approximate, because only the boundaries of windows 1 and 17 are pasted. The last 2026-06-08..2026-07-17 is the 29 dropped sessions.
- **(b) The held-out period is also reused as in-sample.** Window 17's in-sample is 2025-02-26 → 2026-03-09 (OBSERVED, values `:85`), so 2025-2026 data is in-sample for the last windows too.
- **(c) The tuning span is reused as out-of-sample, which is worse.** The bar tunes on 2021-03-08..2024-12-31. That span contains every WF out-of-sample segment from 2022-03-17 to about the end of 2024, roughly windows 1 to 12. So most of the later walk-forward's OOS is data the idea's rules and parameter choices were already fitted to. In addition, Amear picks the contender after seeing the held-out result, which adds selection bias to the later OOS.

None of this is resolved here.

**F1b — is the bar's split a deviation from the WF design?** The WF spec governs only the Noise-Area arms (a) and (b) (spec `:3`). It has no held-out period, and it uses a rolling 252/63/63 design over the whole span (OBSERVED). For those arms, a single tune/hold-out split is **a different design**, not a variant of the spec. For new strategies the spec is **silent**: they are outside its scope. "Walk-forward testing under the existing spec" (`:88`) would mean applying a Noise-Area-specific spec to a non-Noise-Area strategy. The grid is anchored to "the paper's published values" (values `:17`, `:47-:52`), and gate applicability is written per arm (A7). A contender has no paper anchor and no "fixed rules" arm unless one is defined, so new values would be needed (INFERRED). The bar does not modify the WF for the three Noise-Area arms. The handoff `:67` says those are skipped.

**F2 — the spec's DD text is stale against the ledger (OBSERVED).** WF spec `:31` and `:107` give the gate base as "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit". Values `:124` says "Max drawdown ≤ 4% of equity". DECISIONS A4 (`:1735-:1738`) "amends D-2026-11-05-A item 3" to 3.2% and 80%. The bar follows A4. The HEAD specs do not reflect A4. This is reported, not resolved.

**F3 — commission versus contract size (INFERRED conflict, OBSERVED inputs).** The bar requires a "full five-year backtest at $4.68 commission" (`:76`) and the drawdown gate "at 1 MNQ" (`:77`). $4.68 is the NQ round trip. DECISIONS `:1063` (ruling 2): "NQ $4.68, MNQ $1.90". WF spec `:217` (NEEDS AMEAR 22) asks whether the 1 MNQ drawdown comes "from its own run with MNQ point value and MNQ cost, or scaled from the 1 NQ run". The bar points to the D6 check's "four-measure basis" for the method. I did not read that D6 report (UNVERIFIED how it scales MNQ cost). So the bar does not say which commission applies to the 1 MNQ drawdown measurement.

**F4 — the trade-count floor is near the minimum (INFERRED).** The bar needs ≥ 200 trades over the full five years, with no out-of-sample floor. The WF in-sample selection minimum alone is "100 trades per 252-session in-sample window" (values `:94`), and the gate is ≥ 250 OOS trades. So a contender with only about 200 total trades could pass the bar and then fail both WF floors. This is not a contradiction, but it is a likely bar-pass / WF-fail path.

### Q4. Peer review or published evidence in the WF files

OBSERVED:
- WF spec: the grep `peer|publish` gives 0 hits.
- Values: 2 hits, both about the paper's *published values* used as grid anchors, not about peer review as a requirement. `:17` (ruling 4): "small grid around the paper's published values (no wide search)". `:27`: "## 1. Where "the paper's published values" were found".

Neither file makes peer review a gate. The word "peer" does not appear in either. The handoff `:67` and `:83` say the peer-review screen is gone. That does not conflict with the WF files, but it removes the reason ruling 4 gives for the grid's anchor ("published values") for any non-paper strategy (INFERRED).

## Files staged
None. This report is untracked, and the git index was not touched.

## Result
PASS (research brief answered; findings F1-F4 reported, not resolved).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
