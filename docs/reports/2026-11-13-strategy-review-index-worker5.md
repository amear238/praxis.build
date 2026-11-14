# Strategy review index: worker5 (Q1 part B)

## Task
Unit 2026-11-13-strategy-review-index, worker5. Mode: BUILD (read-only research). Working dir /Volumes/Sensidine/Praxis.build, main, HEAD 9ff8a48.
Scope: (1) A20 results, (2) D6 drawdown check (f10603a) plus DECISIONS.md D-2026-11-08-D D6/D7 and gate provenance, (3) walk-forward status, (4) pointers to other recorded backtest results outside the 2026-11-01 runs.

## A20
**A20 is not a strategy backtest. It records no trading figures.**
- Title, `docs/reports/2026-10-20-a20-results.md:1`: "# a20 results: Fusion time zones and Kinetick (voice run)".
- Who and when, `:3`: "**Recorded:** 2026-10-20T15:50:05Z by praxis-master. Bead `Praxis_build-a20`."
- Run, `:4`: "**Run:** Amear, by hand, guided by a Claude voice chat using `2026-10-20-a20-voice-handoff.md`. Reads made around 11:37–11:50 EDT on 2026-10-20."
- Status of values, `:5`: "Each value is REPORTED: Amear read it, and the voice chat wrote it down. The master saw none of it directly."
- Mapping status, `:6`: "**Mapping to the tables:** done by the master against the pre-registered tables in the walkthrough. **NOT AUDITED.**"
- Content: Windows/NinjaTrader time-zone labels and connection-row states, e.g. `:25` "Windows Time zone (exact text): (UTC-05:00) Eastern Time (US & Canada)", `:47` "**K8 FIRED** | **Simulation has no dot**".
- Limit it states itself, `:53`: "It does not show that bar timestamps are right, how NinjaTrader handles the 2026-11-01 change (P13), or that P6 (NQCONT imported as US Eastern) is more than reported."
- Open items, `:58-63` (five questions for Amear, incl. K5/K8 under D-071, the "Trend" box screenshot).
- Strategy / instrument / trades / net / PF / max DD / win rate / avg trade: **NOT IN RECORD** in this file. The grep for `profit factor|net profit|max.*drawdown|win rate|trades` returned nothing (exit=1, Evidence E2).

## D6 and the gate
### Commit and file
`f10603a 2026-11-09 docs: D6 drawdown viability check (Amear D-2026-11-08-D D6) on the three 2026-11-01 trade lists at 1 MNQ and 1 NQ per walk-forward window vs the A4 ceiling per tier; D7 test met on the committed values-spec measure; MANIFEST row 306`. Files: `MANIFEST.md`, `docs/reports/2026-11-09-d6-drawdown-check-manager.md` (Evidence E3). All `:n` below refer to that report unless named otherwise.

### What it is and its evidence level
- Scope, `:11`: "The check computes the worst drawdown per walk-forward window on the three committed 2026-11-01 trade lists, at 1 MNQ and 1 NQ, with and without breaker #1. It compares each figure with the A4 ceiling for each tier row."
- Inputs, `:60`: "These are the three base-strategy NT8 exports on the Desktop: baseline 07-10, OppBand 07-57, Flat1559 07-59. They are **not in git** ... LastHalfHourMomentum (08-00) is excluded as retired."
- Evidence level, `:56`: "These are COMPUTED figures on NT8 trade lists (OBSERVED inputs) at Standard resolution with no breakers. They are not the judged High-resolution, breakers-on version (values spec :42). They are not tested on the VM. The MNQ figures are derived, not an MNQ run."
- MNQ derivation, `:52`: "MNQ net = points × $2 − $1.90 (cost model v1.2.0). ... That this equals an own MNQ run is INFERRED there and here."
- Slippage, `:49`: "Slippage is already in the fill prices (results report :51, quoted in E2), so it is not added again."
- Status: computed from one Standard-resolution backtest per strategy, split into 17 OOS-calendar windows. It is NOT a walk-forward test (no IS selection; see next section).

### Drawdown measures and gate
- Gate rule, `:19`: "Ceiling for each row = below min(3.2% of size, 80% of MFFU limit) (A4). [V] = PASS only if all 17 windows are strictly below the ceiling."
- WIN, `:20`: "inside the window only. It is the worse of closed-trade and end-of-day equity, both reset to 0 at the window's start."
- VS4, `:21`: "the committed values-spec measure (`git show HEAD:docs/specs/2026-11-06-walk-forward-values.md` :139). It is the worst of four: WIN's two, plus the same two carried across windows."
- Which measure decides D7, `:64`: "VS4 is used, because it is the committed SETTLED per-window measure (values spec :139). ... **The answer flips between the two.**"
- Gate source in DECISIONS.md (quoted inside the D6 report, `:102`): "A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80%" (DECISIONS.md :1735 at that HEAD; current line checked below).
- Negative tests of the gate, `:170-174`: "17 windows all at ceiling - 0.01 -> PASS" / "one window EXACTLY at ceiling (A4 says 'below') -> FAIL" / "Builder 50K add-on ceiling (expect 1200 = 80% of 1500, not 1600) = 1200.0" / "Studio 5K ceiling (expect 160 = 3.2% of 5000, not 200) = 160.0".

### Figures per strategy and per tier (1 MNQ, no cap; order BASELINE / OPPBAND / FLAT1559)
| Tier row (`:n`) | Ceiling | WIN | VS4 |
|---|---|---|---|
| Studio 5K / 10K / 20K (`:29`) | $160 / $320 / $640 | $2,913.90 / $2,786.70 / $2,774.40, FAIL all | $4,927.60 / $5,280.20 / $4,463.10, FAIL all |
| Rapid 25K, Rapid EOD 25K, Builder 25K (`:30`) | $800 | FAIL all | FAIL all |
| Rapid 50K, Rapid EOD 50K, Pro 50K, Builder 50K (`:31`) | $1,600 | FAIL all | FAIL all |
| Builder 50K add-on (`:32`) | $1,200 | FAIL all | FAIL all |
| Rapid 100K, Pro 100K, Builder 100K (`:33`) | $2,400 | FAIL all (15 or 16 of 17 windows below) | FAIL all |
| Rapid 150K [Eval EOD], Pro 150K, Builder 150K (`:34`) | $3,600 | **PASS all three** ($2,913.90 / $2,786.70 / $2,774.40) | FAIL all (14 or 15 of 17 below) |
| Rapid 150K [Sim-Funded intraday] (`:35`) | $3,600 | **PASS all three** ($3,031.30 / $3,259.10 / $2,891.80) | FAIL all ($5,267.00 / $5,525.30 / $4,802.50) |

(Table rows quoted from `:29-35`; the `:n` column is mine.)
- 1 NQ, `:37`: "every row FAILS on both measures, for all three strategies. WIN worst window: $28,337.08 / $27,394.44 / $26,942.08. VS4: $45,710.32 / $50,969.04 / $41,065.32."
- The 50K gate: $1,600 at 1 MNQ for Rapid 50K, Rapid EOD 50K, Pro 50K, Builder 50K (`:31`), FAIL all on both measures. INFERRED arithmetic: $1,600 = 3.2% × $50,000 = 80% × $2,000 (Builder 50K limit $2,000 per WF spec row quoted at D6 `:116`).
- Breaker #1 cap, `:39`: "NOT COMPUTABLE. No numeric spec value exists (evidence E4)." Sensitivity caps `:65` are "not a recommendation and not a breaker value".
- Full-span figures quoted in D6 E1 (`:93-95`, from results report :402-404, the 2026-11-01 runs covered by another worker): BASELINE "| 1190 | $197327.60 | 1.29 | -$45282.04 |", OPPBAND "| 810 | $210182.40 | 1.26 | -$50748.88 |", FLAT1559 "| 1190 | $193017.60 | 1.28 | -$40637.04 |". Column headers not read here (UNVERIFIED which column is which; the grep hit at `:271` says "full-span closed-trade max DD on CSV Profit (cost $2.96): -$45,282.04 ; net $197,327.60").

### Conclusion (D6 report)
- Plain English, `:7`: "At 1 micro (MNQ), each of the three strategies had a worst 63-session stretch that fell $2,774 to $2,914 from its high. That stays under the safety ceiling only on the 150K accounts, where the ceiling is $3,600. Smaller accounts fail. If the losing run that carries over from earlier windows is counted, which is the project's committed measure, the worst figure is $4,463 to $5,280. That fails every account size. At 1 full NQ the worst stretch is $26,942 to $28,337, and every account fails. ... On the committed measure the D7 rule is triggered."
- D7 test, `:42-43`: "On the committed measure (VS4): **YES.** All three strategies fail all 17 tier rows, including both Rapid stages." / "On the within-window measure (WIN): **NO.** The four 150K rows pass, for all three strategies."
- D7 consequence, `:45`: "no breaker value is designed to fit the ceiling. R6's research (higher-win-rate, steadier-equity strategies) is pulled forward to P0. The Noise-Area baseline continues through the VM tests for the record, but a GO on MFFU is not expected from it. Nothing was tuned in this unit."

### DECISIONS.md: how a strategy is judged against the gate, and D6/D7
- A4 gate, `DECISIONS.md:1735-1740` (current HEAD 9ff8a48 line numbers): "A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80% / of the ruled limit, i.e. below the lower of 3.2% of the MFFU / account size and 80% of MFFU's trailing drawdown limit. This / amends D-2026-11-05-A item 3 with a safety buffer for model error. / Evaluated against every tier row; tier pick stays Q9."
- Measure judged, `docs/specs/2026-11-06-walk-forward-values.md:139`: "**Worst drawdown per window** (WF spec NEEDS AMEAR 21) — SETTLED, strictest reasonable: measured on closed-trade equity and on end-of-day equity, each both from the window's start and carried across windows; the worst of these four is judged."
- Same line on MNQ: "**1 MNQ figures** ... SETTLED: derived from the 1 NQ trade list. Per trade, MNQ net = (NQ gross ÷ 10) − $1.90 ... That this equals an own MNQ run is INFERRED."
- D6 ruling, `DECISIONS.md:1930-1939`: "D6  FIRST: drawdown viability check, Mac-only, read-only, no VM, no / purchase. On the three committed 2026-11-01 trade lists, compute / per-walk-forward-window worst drawdown at 1 MNQ (MFFU MNQ / commission per cost model v1.2.0), with and without a simulated / daily-loss cap (breaker #1 at its spec value). Compare to the A4 / ceiling per tier row (80% of the lower of 4% of account and the / trailing limit). ... Report: pass/fail per tier at 1 MNQ and / 1 NQ."
- D7 ruling, `DECISIONS.md:1940-1944`: "D7  If D6 fails at every tier at 1 MNQ: do not design breaker values / to fit the drawdown ceiling (that is curve-fitting). Report it, and / pull R6's research (higher-win-rate, steadier-equity strategies) / forward to P0. The Noise-Area baseline continues through the VM / tests for the record, but a GO on MFFU is not expected from it."
- D7 recorded as fired, `DECISIONS.md:2283` (R6 entry): "pulled forward to P0 by Amear's D-2026-11-08-D D7 (DECISIONS.md:1940–1944) after D6 failed (HANDOFF.md:289 at `c29d08b`: \"D6 result → D7 FIRED\")".
- Gate value provenance: there is no literal "$1,600" in DECISIONS.md or the values spec. The `1,600|$1600|50K` grep hits there are only the Builder 50K add-on / $1,500 rows (`DECISIONS.md:1388-1389`; values spec `:136`, `:297-298`, `:331`, `:338`). Values spec `:136` (excerpt): "**The Phase 3 spec's $1,500** ... not used as a gate figure. The per-tier table governs; $1,500 appears only as the Builder 50K add-on row." The $1,600 50K ceiling appears as a computed figure in the D6 report (`:31`); it comes from A4's formula applied to the WF spec tier rows (`docs/specs/2026-11-05-walk-forward-spec.md:115-130`, per D6 `:112`). INFERRED: 0.032 × 50,000 = 1,600 and 0.8 × 2,000 = 1,600.

## Walk-forward status
**Specified, and Mac-side maths/oracles WRITTEN + TESTED on synthetic fixtures. No walk-forward has been RUN; no OOS walk-forward result is recorded.** Do not read the D6 per-window drawdowns (above) as walk-forward OOS results: D6 slices one full-span Standard-resolution backtest per strategy into the 17 OOS calendar windows, with no in-sample selection.

- Spec status, `docs/specs/2026-11-05-walk-forward-spec.md:5`: "**Status: DERIVED — not yet ruled on as a whole by Amear.**"
- Values spec status, `docs/specs/2026-11-06-walk-forward-values.md:3`: "**Status: version 2.2 (2026-11-08).**" The v2.2 amendment is uncommitted and parked (bead below).
- Values spec on what any first result would be, `:42`: "this Standard-resolution, breaker-less walk-forward gives a provisional result, labelled so in every report. It is not by itself the go/no-go judgement. R-1104-3 frames the judged version as High fill resolution with circuit breakers on".
- STATUS.md 2026-11-07 evening section (heading `STATUS.md:170`), `:193`: "WF Mac-side maths: WRITTEN + TESTED on synthetic fixtures and the real calendar (212 tests); UNVERIFIED against NT8"; `:194`: "Oracles: WRITTEN + TESTED on synthetic fixtures (59 tests); values COMPUTED on the real file at both session starts; UNVERIFIED against NT8 arm (b)"; `:195`: "- T1–T13: none has run. All wait for the VM."
- `docs/reports/2026-11-07-wf-mac-side-maths-manager.md:5`: "UNVERIFIED against real NT8 output: nothing here has run on a real bridge result or NT8 export." `:55`: "Every P&L input in every test is synthetic."
- `docs/reports/2026-11-07-wf-oracles-manager.md:5`: "No arm (b) run has happened on the VM. Nothing here has graded a real arm (b) trade list."
- STATUS.md:195 sits in a dated 2026-11-07 section; it is the only `none has run|T1.T13` hit (Evidence E8). No later report named `*wf*`/`*walk*` other than `2026-11-09-wf-spec-amendment-resume-manager.md` (a spec-amendment resume, not a run) was found (Evidence E9). The 2026-11-13 VM bridge queue "T1-T3" (next section) are full-span bridge backtests, not WF spec T1–T13 runs; INFERRED from their content (single runs per ExitMode, no windows).
- Bead `Praxis_build-diq`, `bd show`: "PARKED: wf-spec-amendment (values spec v2.2 + WF spec A4) - audit FAIL 2, absolute park rule fired   [● P1 · OPEN]"; comment 2026-11-09 06:36: "C1 resume unit 2026-11-09-wf-spec-amendment-resume. The single C1 audit FAILED ... Parked again; ... Working tree holds the work. A human resumes."
- Level: walk-forward = SPECIFIED (spec DERIVED, values v2.2 parked) + tooling WRITTEN/TESTED on synthetic data. Not walk-forward tested.

## Other results pointers
Pointers only; figures quoted are short excerpts so the reader can identify the run. Grades are as each file states them. The 2026-11-01 three-strategy-results, csv-analyses and run3 files are another worker's scope and are only cross-referenced.

**Primary records of Praxis NT8 backtests outside the 2026-11-01 runs:**
1. `docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md` (committed in 9ff8a48). VM bridge queue T1-T3 (bridge-driven Strategy Analyzer runs). Source `:5`: "the VM Claude Code session's own report, pasted to this channel by Amear at 14:37 ET (REPORTED BY Amear; the channel has not read the VM repo)". Setup `:11`: "PraxisNoiseAreaBreakout, NQCONTROW SEP25, 1-minute, 2021-03-08 to 2026-07-17, CME US Index Futures RTH 0930 ET, commission PRAXIS $2.96 round trip, slippage 2, Standard fill resolution, 1 NQ." Table `:13-17`, e.g. `:15` "| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615 | -$38,905.64 | Exact match |", `:16` "| T2 | OppBand | 1,112 | $188,618.48 | 1.2861 | -$37,906.24 | ...". Grade: REPORTED (second-hand); result files live only on the VM (`results\T1.json` etc., `:5`). Full-span, not walk-forward.
   - The "T1 reference (Amear's hand run)" of 1,173 trades (the 09:30 ET session-start run): no primary record found in `docs/reports`, STATUS.md or HANDOFF.md. The `1,173|176,392` grep (Evidence E11) hits only the 2026-11-13 handoffs and the research-filing workers that copy them. Its original record: NOT IN RECORD in the paths searched.
2. `docs/reports/2026-10-28-voice-session-notes.md`: first Fusion runs, `:36-40` table. Run 3 `:40`: "| 3 (full history, same settings) | 2021-03-08 → 2026-07-17 | **1,075** | **$1,281.61** | — | **1.04** | **$4,051.57** |"; `:53` a later full run: "**1,211 trades** ... **net $3,136.84** ... **PF 1.08** · **max DD −$4,108.84**". These predate the point-value fix: `docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:30`: "With a $1 point value, points and dollars are the same number." Superseded as figures; historical only (INFERRED from o78 and the later 1,190-trade runs).
3. `docs/reports/2026-10-31-voice-session-notes-2.md:23`: "1,190 trades (556 L / 634 S) · net $200,850.00 · ... COMMISSION $0.00 · PF 1.30 · max DD −$44,545.00 · ... avg trade $168.78"; `:63` "→ STOP condition met." (trade count differs from run 4). A pre-commission run; not re-checked here.
4. `docs/reports/2026-10-31-voice-session-notes.md:22` (run 4 net spoken "$3,136") and `docs/reports/2026-10-31-voice-handoff-backtest-session.md` (runs 3/4 slippage and extreme-trade checks, `:43`, `:48`): secondary notes on the same early runs.
5. `docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:7`: run 4 long/short split "shorts lost (−$1,404.56 on 627 trades)"; analysis of the early $1/pt runs, every cause "INFERRED" (`:28`).

**Secondary copies of the 2026-11-01 figures (not primary; other worker's scope):** `docs/reports/2026-11-01-voice-handoff-results-and-next-build.md:33-37` (four-column table incl. LastHalfHourMomentum "−$76,009.84", PF "0.84"); `docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md:19` (the LastHalfHourMomentum hand-test line: "1,304 trades, net -$76,009.84, PF 0.84, max DD -$99,806.96, win rate 47.62%, average trade -$58.29"); D6 report `:93-95`.

**Not Praxis backtest results (literature, plans, specs, breaker design):** `2026-11-04-research-compiled-for-voice(-v2).md`, `2026-11-04-comparable-builds.md`, `2026-11-04-proof-of-concept-standard.md`, `2026-11-13-return-handoff-claude-ai-strategy-research.md` and `-kimi-research.md` (candidate strategies; `:19` of the strategy-research handoff says its drawdown checks are "a floor, not the continuous carried maximum drawdown the gate requires"), the 2026-11-12/13 fgd, o4 and open-a2 units (breaker parity design; the grep hits are rule text, e.g. o4-parity `:64`), 7zq hand-test checklists, 3gm checklists. Judged from the triage grep only (Evidence E10); not opened in full: UNVERIFIED that none holds a figure.
- R6 research results (D7 pull-forward): the design is on branch `r6/announcement-research` in a separate worktree (`DECISIONS.md:2283`); not on `main` and not searched here.

## Evidence
Redaction note: by brief rule one word is not written in this report; in quotes and pasted output it is shown as `[V]` (2 occurrence(s)). No other character of the pasted output is changed.

Captured by one bash runner (`printf` of the literal command, then its output and exit code), run 2026-11-13 at HEAD 9ff8a48. Other quotes in this report come from tool calls made earlier in this session with the same commands or narrower `sed -n` ranges.

**E1**
```
$ sed -n '1,6p' docs/reports/2026-10-20-a20-results.md | cut -c1-200
# a20 results: Fusion time zones and Kinetick (voice run)

**Recorded:** 2026-10-20T15:50:05Z by praxis-master. Bead `Praxis_build-a20`.
**Run:** Amear, by hand, guided by a Claude voice chat using `2026-10-20-a20-voice-handoff.md`. Reads made around 11:37–11:50 EDT on 2026-10-20. That is after the walkthrough commit `efcf690` (10:41:5
**Source of every value below:** the send-back block Amear pasted from the voice session, quoted unchanged. Each value is REPORTED: Amear read it, and the voice chat wrote it down. The master saw none
**Mapping to the tables:** done by the master against the pre-registered tables in the walkthrough. **NOT AUDITED.**
exit=0
```

**E2**
```
$ grep -n -i -E 'profit factor|net profit|max.*drawdown|win rate|trades' docs/reports/2026-10-20-a20-results.md
exit=1
```

**E3**
```
$ git show --format='%h %ad %s' --date=short --name-only f10603a | grep -v -E '2026-10-28-f4-|/evidence/'
f10603a 2026-11-09 docs: D6 drawdown viability check (Amear D-2026-11-08-D D6) on the three 2026-11-01 trade lists at 1 MNQ and 1 NQ per walk-forward window vs the A4 ceiling per tier; D7 test met on the committed values-spec measure; MANIFEST row 306

MANIFEST.md
docs/reports/2026-11-09-d6-drawdown-check-manager.md
exit=0
```

**E4**
```
$ sed -n '7p;19,21p;29,37p;42,45p' docs/reports/2026-11-09-d6-drawdown-check-manager.md | cut -c1-330
At 1 micro (MNQ), each of the three strategies had a worst 63-session stretch that fell $2,774 to $2,914 from its high. That stays under the safety ceiling only on the 150K accounts, where the ceiling is $3,600. Smaller accounts fail. If the losing run that carries over from earlier windows is counted, which is the project's com
Ceiling for each row = below min(3.2% of size, 80% of MFFU limit) (A4). [V] = PASS only if all 17 windows are strictly below the ceiling. Two measures are shown:
- **WIN**: inside the window only. It is the worse of closed-trade and end-of-day equity, both reset to 0 at the window's start.
- **VS4**: the committed values-spec measure (`git show HEAD:docs/specs/2026-11-06-walk-forward-values.md` :139). It is the worst of four: WIN's two, plus the same two carried across windows.
| Studio 5K / 10K / 20K (trailing measure, stricter) | $160 / $320 / $640 | $2,913.90 / $2,786.70 / $2,774.40, FAIL all | $4,927.60 / $5,280.20 / $4,463.10, FAIL all |
| Rapid 25K, Rapid EOD 25K, Builder 25K | $800 | FAIL all | FAIL all |
| Rapid 50K, Rapid EOD 50K, Pro 50K, Builder 50K | $1,600 | FAIL all | FAIL all |
| Builder 50K add-on | $1,200 | FAIL all | FAIL all |
| Rapid 100K, Pro 100K, Builder 100K | $2,400 | FAIL all (15 or 16 of 17 windows below) | FAIL all |
| Rapid 150K [Eval EOD], Pro 150K, Builder 150K | $3,600 | **PASS all three** ($2,913.90 / $2,786.70 / $2,774.40) | FAIL all (14 or 15 of 17 below) |
| Rapid 150K [Sim-Funded intraday] | $3,600 | **PASS all three** ($3,031.30 / $3,259.10 / $2,891.80) | FAIL all ($5,267.00 / $5,525.30 / $4,802.50) |

**1 NQ, no cap:** every row FAILS on both measures, for all three strategies. WIN worst window: $28,337.08 / $27,394.44 / $26,942.08. VS4: $45,710.32 / $50,969.04 / $41,065.32.
- On the committed measure (VS4): **YES.** All three strategies fail all 17 tier rows, including both Rapid stages.
- On the within-window measure (WIN): **NO.** The four 150K rows pass, for all three strategies. The margins are $686.10 / $813.30 / $825.60 at EOD and $568.70 / $340.90 / $708.20 intraday.

The D7 test is judged on VS4 (Decision 5). **D7 consequence:** no breaker value is designed to fit the ceiling. R6's research (higher-win-rate, steadier-equity strategies) is pulled forward to P0. The Noise-Area baseline continues through the VM tests for the record, but a GO on MFFU is not expected from it. Nothing was tuned in
exit=0
```

**E5**
```
$ grep -n -E '\bD6\b|\bD7\b' DECISIONS.md | head -20 | cut -c1-140
1877:**S4 timing.** This entry is written before any unit it authorises is dispatched (`git show HEAD:DECISIONS.md | grep -c 'D-2026-11-08-[
1930:D6  FIRST: drawdown viability check, Mac-only, read-only, no VM, no
1940:D7  If D6 fails at every tier at 1 MNQ: do not design breaker values
1961:D12 Sequence after D6: U7 resume (C1), rubric unit (C2, C6, C8, and
1980:- **D6** (:40–49). *(paraphrase)* "FIRST": a drawdown viability check, "Mac-only, read-only, no VM, no purchase". It runs on "the three
1981:- **D7** (:50–54). *(paraphrase)* If D6 fails at every tier at 1 MNQ, breaker values are not designed to fit the drawdown ceiling ("tha
1986:- **D12** (:71–75). "Sequence after D6: U7 resume (C1), rubric unit (C2, C6, C8, and D1-D5 as a new "Autonomy" section), values spec (C
1990:- *Manager's reading, not a ruling — §4 numbering.* D8's "(3)"–"(8)" match the items 3–8 of the strategy brief §4 (`docs/reports/2026-1
1994:- Master's reading (filing note 4, :85–92), changeable by Amear: the order in force is (a) U8, (b) U9 files D, (c) "One audit of both e
1995:- Master's reading (filing note 5, :93–98), changeable by Amear: D6's inputs are named in the D6 brief "read when the unit runs, not as
1997:**What this entry does NOT do.** It makes no rubric edit; the S8 scope change waits for the D12 rubric unit. It makes no spec, values-s
1999:**S4 timing.** This entry is written before any unit that acts on D is dispatched. OBSERVED by unit `2026-11-09-c-d-filing` (its report
2003:**S6 cross-block (interactions only; nothing decided here).** Manager's readings, not rulings. D1–D5 ↔ S8 (rubric :122) and the D12 rub
2005:**S13.** The standing sentence is carried once, in the header. No backtest or P&L figure is stated in this entry. D6 asks for drawdown 
2283:**Authority chain.** Amear's ruling D-2026-11-08-A R6 (DECISIONS.md:1572–1579: research and backtest on the existing 1-minute data only
2308:- Direction long only; no stop, no target, no optimisation in the first pass. Size 1 MNQ (1 NQ shown alongside, as D6).
2327:**6. Rubric F3 (FROZEN).** F3 (`specs/SPEC_RUBRIC.md`:19–31) concerns "The fill resolution the Strategy Analyzer will actually run at" 
2407:- R6 (read-only): DECISIONS.md:2350 (parked D-2026-11-12-B) "without breakers as design :116 (O4) states"; `bf6fcc7:docs/specs/2026-11-
exit=0
```

**E6**
```
$ sed -n '1735,1740p;1930,1944p' DECISIONS.md
A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80%
    of the ruled limit, i.e. below the lower of 3.2% of the MFFU
    account size and 80% of MFFU's trailing drawdown limit. This
    amends D-2026-11-05-A item 3 with a safety buffer for model error.
    Evaluated against every tier row; tier pick stays Q9. Closes the
    notes-4 DD equity-base item.
D6  FIRST: drawdown viability check, Mac-only, read-only, no VM, no
    purchase. On the three committed 2026-11-01 trade lists, compute
    per-walk-forward-window worst drawdown at 1 MNQ (MFFU MNQ
    commission per cost model v1.2.0), with and without a simulated
    daily-loss cap (breaker #1 at its spec value). Compare to the A4
    ceiling per tier row (80% of the lower of 4% of account and the
    trailing limit). If scripts/wf can regenerate the trade list from
    the 09:30 ET session start (R1), run that too and label it
    UNVERIFIED against NT8. Report: pass/fail per tier at 1 MNQ and
    1 NQ.
D7  If D6 fails at every tier at 1 MNQ: do not design breaker values
    to fit the drawdown ceiling (that is curve-fitting). Report it, and
    pull R6's research (higher-win-rate, steadier-equity strategies)
    forward to P0. The Noise-Area baseline continues through the VM
    tests for the record, but a GO on MFFU is not expected from it.
exit=0
```

**E7**
```
$ grep -n -E '1,600|\$1600|50K' DECISIONS.md docs/specs/2026-11-06-walk-forward-values.md | head -20 | cut -c1-160
DECISIONS.md:1388:| Per-tier reporting rule | Static rows and the Builder 50K add-on row included; a contradiction shows both figures, the lower used | SETTLED;
DECISIONS.md:1389:| $1,500 figure | Not a gate figure; only the Builder 50K add-on row; no breaker limit set | SETTLED for walk-forward use only; the breaker #6
DECISIONS.md:1886:- (i) **C5 (ii) and rows whose Eval and Sim-Funded types differ.** B (ii) (DECISIONS.md:1802): "Which limit type and stage A4 means for the St
docs/specs/2026-11-06-walk-forward-values.md:136:- **Per-tier reporting** — RULED (D-2026-11-05-A item 4, :815: "Every window also reports worst drawdown at 1 M
docs/specs/2026-11-06-walk-forward-values.md:297:| 38 | Per-tier reporting rule (WF NA 12, 13) | Every WF spec §6 row, Studio Static rows and the Builder 50K ad
docs/specs/2026-11-06-walk-forward-values.md:298:| 39 | $1,500 (WF NA 20) | For walk-forward use only: not a gate figure; the per-tier table governs; it appears
docs/specs/2026-11-06-walk-forward-values.md:331:| 13 | MFFU page contradictions; Builder 50K add-on | Reporting rule SETTLED: both figures shown, the lower use
docs/specs/2026-11-06-walk-forward-values.md:338:| 20 | The Phase 3 spec's $1,500 trailing-drawdown figure | SETTLED for walk-forward use only: not a gate figur
exit=0
```

**E8**
```
$ grep -n -E 'none has run|T1.T13' STATUS.md | head; sed -n '170p' STATUS.md | cut -c1-90; sed -n '5p' docs/specs/2026-11-05-walk-forward-spec.md | cut -c1-90; sed -n '3p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-60
195:- T1–T13: none has run. All wait for the VM.
## 2026-11-07 evening — the build half of Amear's loop order landed: 7 gated commits today
**Status: DERIVED — not yet ruled on as a whole by Amear.** **Changelog.** 2026-11-08, uni
**Status: version 2.2 (2026-11-08).** (v2.2 changes: unit `2
exit=0
```

**E9**
```
$ ls docs/reports | grep -i -E 'wf|walk' | grep -v -E '2026-10-28-f4-'
2026-08-29-session52-nt8-voice-walkthrough-v2.md
2026-08-29-session52-nt8-voice-walkthrough.md
2026-10-20-a20-fusion-tz-kinetick-walkthrough.md
2026-10-20-fusion-analyzer-physical-click-walkthrough-v2.md
2026-10-20-fusion-analyzer-physical-click-walkthrough-v3.md
2026-10-20-fusion-analyzer-physical-click-walkthrough.md
2026-10-31-a9d-walkthrough-future-row.md
2026-10-31-voice-handoff-future-row-walkthrough.md
2026-11-05-fusion-shared-folders-walkthrough-manager.md
2026-11-05-fusion-shared-folders-walkthrough.md
2026-11-05-r8j-phase3-import-and-wf-spec-manager.md
2026-11-06-wf-values-manager.md
2026-11-07-wf-mac-side-maths-manager.md
2026-11-07-wf-oracles-manager.md
2026-11-07-wf-values-fresh-manager.md
2026-11-08-wf-spec-amendment-correction-1-manager.md
2026-11-08-wf-spec-amendment-correction-2-manager.md
2026-11-08-wf-spec-amendment-correction-3-manager.md
2026-11-08-wf-spec-amendment-manager.md
2026-11-09-wf-spec-amendment-resume-manager.md
exit=0
```

**E9b**
```
$ bd show Praxis_build-diq 2>&1 | head -3
○ Praxis_build-diq · PARKED: wf-spec-amendment (values spec v2.2 + WF spec A4) - audit FAIL 2, absolute park rule fired   [● P1 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-11-08 · Updated: 2026-11-08
exit=0
```

**E10**
```
$ grep -l -E 'Profit factor|profit factor' docs/reports/*.md --exclude='2026-10-28-f4-*' | grep -v -E 'strategy-review-index|/evidence/|2026-10-28-f4-' | head -40
docs/reports/2026-10-28-voice-session-notes.md
docs/reports/2026-10-30-3gm-fidelity-check.md
docs/reports/2026-10-30-3gm-worker1-checklist.md
docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md
docs/reports/2026-10-30-run3-backtest-screenshot-record.md
docs/reports/2026-10-31-7zq-handtest-checklist.md
docs/reports/2026-10-31-7zq-m2-handtest-checklist.md
docs/reports/2026-10-31-a9d-walkthrough-future-row.md
docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md
docs/reports/2026-11-01-voice-handoff-commission-fix.md
docs/reports/2026-11-01-voice-handoff-results-and-next-build.md
docs/reports/2026-11-04-comparable-builds.md
docs/reports/2026-11-04-proof-of-concept-standard.md
docs/reports/2026-11-04-research-compiled-for-voice-v2.md
docs/reports/2026-11-04-research-compiled-for-voice.md
docs/reports/2026-11-05-r8j-phase3-import-and-wf-spec-manager.md
docs/reports/2026-11-07-wf-mac-side-maths-manager.md
docs/reports/2026-11-07-wf-values-fresh-manager.md
docs/reports/2026-11-08-rulings-filing-manager.md
docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md
docs/reports/2026-11-13-research-filing-resume-manager.md
docs/reports/2026-11-13-research-filing-resume-worker1.md
docs/reports/2026-11-13-research-filing-resume-worker2.md
docs/reports/2026-11-13-research-filing-worker1.md
docs/reports/2026-11-13-research-filing-worker2.md
docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md
docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
exit=0
```

**E11**
```
$ grep -rn -E '1,173|176,392' docs/reports/*.md STATUS.md HANDOFF.md --exclude='2026-10-28-f4-*' | grep -v -E 'strategy-review-index|/evidence/' | cut -c1-120
docs/reports/2026-11-13-research-filing-resume-worker2.md:254:2) on NQ. Our backtest, 2021-03-08 to 2026-07-17, 1-minute
docs/reports/2026-11-13-research-filing-worker2.md:405:15:| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615 | -$38,9
docs/reports/2026-11-13-research-filing-worker2.md:407:17:| T3 | BandOrVWAP | 1,173 | $176,392.92 | 1.26 | -$38,905
docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md:51:- **VM bridge queue:** Amear reported (about 14:30 
docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md:41:The current strategy is the Zarattini-Aziz-Barb
docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:15:| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615
docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:17:| T3 | BandOrVWAP | 1,173 | $176,392.92 | 1.26 |
docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:40:1. **MFFU commission re-run:** Amear sets both P
exit=0
```


**E12 (de-identification check, last step)**
```
$ grep -c -i -w "$(ls /Volumes/Sensidine/Praxis.build/docs/reports | grep '^2026-10-28-f4-' | head -1 | sed 's/^2026-10-28-f4-//; s/-.*//')" /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-strategy-review-index-worker5.md
0
```

## Gaps
- A20: no backtest figures exist in it; any expectation that "A20" holds strategy results is not met by the record (E2, exit=1).
- The 1,173-trade "T1 reference (Amear's hand run)" at 09:30 ET: no primary record found in docs/reports, STATUS.md or HANDOFF.md (E11). NOT IN RECORD in the paths searched.
- VM bridge T1-T3 result files (`results\T*.json`) are only on the VM; the record is REPORTED second-hand.
- D6 inputs (the three trade CSVs) are not in git (D6 `:60`); D6 figures cannot be re-derived from the repo alone.
- D6 breaker #1 capped run: NOT COMPUTABLE, no spec value (D6 `:39`).
- No walk-forward OOS result exists (STATUS.md:195, dated 2026-11-07; no later WF run report found, E9). The WF values v2.2 amendment is parked uncommitted (bead `Praxis_build-diq`, OPEN P1).
- MFFU tier limits behind the ceilings are the WF spec's 2026-11-05 capture; D6 `:240` marks them "UNVERIFIED as of today".
- The column headers of D6 E1 `:93-95` were not read; which column is PF vs max DD there is UNVERIFIED (values agree with the 2026-11-01 secondary copy, `2026-11-01-voice-handoff-results-and-next-build.md:34-37`).
- The "not Praxis results" classification of the remaining profit-factor hits rests on the triage grep only (E10); files not opened in full.
- R6 research results, if any, are on branch `r6/announcement-research` and were not searched.
- Nothing in this report is a new figure. The INFERRED arithmetic is the $1,600 = 3.2% × 50,000 = 80% × 2,000 check.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
