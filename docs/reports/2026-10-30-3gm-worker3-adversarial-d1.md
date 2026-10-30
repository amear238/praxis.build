# 3gm — Worker 3, ADVERSARIAL review of D1 (`2026-10-30-3gm-worker1-checklist.md`)

**Task:** Praxis_build-3gm, break the verdicts in the D1 checklist. **Mode:** ADVERSARIAL, read-only. **Date:** 2026-10-30.
**Criterion:** every §A row (4uu report L16–32) and §C bullet (L50–56) has a row with the spec line, paper page, code lines, pasted `sed -n`, and a verdict from the fixed set. Rubric S1 (pasted output for every claim) and S2 (no grade above its evidence) apply.
**Only file written:** this report. Scratch: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/w3/refid.py`. No git add, no memory writes.

## Process log
1. Re-hashed the .cs: `35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265`, 312 lines. This matches the brief.
2. Read the full .cs (1–312), the full spec (1–111), DECISION_LOG.md:42, voice notes :22–28 and :29–44, the 4uu report L16–32 and L50–56, and the whole D1 report (839 lines).
3. Grepped DECISION_LOG.md and DECISIONS.md for sizing, vol-target, Contracts, same-side, OppBand, and opposite-band. Read the StopMarket context in DL:351 and the start of DL:443.
4. Wrote `refid.py`. It extracts every `$ cmd` from all 31 pasted blocks, re-runs each one in the repo, and diffs the output against the pasted text. It also recounts the verdicts from the summary table and from the body.

## Verification evidence (pasted)

Hash gate:
```text
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
     312 ninjascript/PraxisNoiseAreaBreakout.cs
```

S1 fidelity re-run (all blocks, not a sample) and verdict recount:
```text
blocks=31 commands=112 identical=112 mismatched=0
summary rows: 29
  BUG (comment only, no runtime effect) 1
  BUG (plot only, no trade effect) 1
  CANNOT-DETERMINE-STATICALLY 5
  DEVIATION (unauthorised) 3
  FAITHFUL 15
  SPEC-SILENT 4
body verdict lines: 29
  BUG (comment only, no runtime effect) 1
  BUG (plot only, no trade effect) 1
  CANNOT-DETERMINE-STATICALLY 5
  DEVIATION (unauthorised) 3
  FAITHFUL 15
  SPEC-SILENT 4
```

Ledger greps that D1 did not paste (relevant to F1 and F4):
```text
== DL sizing/vol-target/contracts/fixed-size
351:- [2026-08-29T00:30:00Z] WHO: praxis-master (session 52) | WHAT: **MASTER'S ERROR, RECORDED NOT ABSORBED — THE MASTER TOLD AMEAR THE STRATEGY'S EDGE LIVES AT A BAND-EDGE CROSS AND THAT INTRABAR ORDERING IS THEREFORE THE F3 DAMAGE MECHANISM. THAT IS FALSE
443:- [2026-10-30T21:37:00Z] WHO: praxis-master | WHO OBSERVED: amear (by hand on Fusion; voice-reported; no screenshots seen by any Claude) | WHAT: **INTAKE OF THE 2026-10-30 HAND-RUN RESULTS, graded REPORTED BY AMEAR throughout.** (a) `PraxisNoiseAreaBreakou
== DL same-side/OppBand/opposite-band
DECISION_LOG.md:42:| 2026-07-16T19:29Z | WHO: trader (Amear) + orchestrator (session 16) | WHAT: Block-2 strategy definition LOCKED paper-faithful after Zarattini SSRN 4824172 sourced (commit 2a3f192, spec docs/specs/2026-07-16-b2-noise-area-ruleset.md) — (1
DECISION_LOG.md:46:| 2026-07-25 (session 30) | WHO: Claude.ai master/scoping agent (directive, relayed by trader Amear) + orchestrator (session 30) | WHAT: HARD PHASE-GATE raised on the Block-2 backtest — bead 4uu (Strategy-Analyzer backtest + reconcile) MUS
```
These hits match only because they contain the string "Contracts" in a code quote (351, 443) or the word "opposite-band" (42, 46). No row authorises dropping the vol-target sizing or using the same-side band.

Spec lines that drive F1 (from `cat -n` of the spec):
```text
    49	| Stop / exit variants tested | (a) opposite band; (b) `max(VWAP, band)`; (c) = (b) + vol-target sizing | Tables 1–3, pp. 11–15 |
    52	| Vol-target sizing | `σ_target = 2%` daily, leverage capped **4×** | §3 p. 15 |
    97	| **exit policy** | discrete: {opp-band ; max/min(band,VWAP) ; +vol-target} | Enum input `ExitMode` ∈ {OppBand, BandOrVWAP}. Paper's preferred = **BandOrVWAP**. |
```
DECISION_LOG.md:42 (pasted above in D1's appendix and re-read by me) locks "(3) FIRST build = pure paper replication with FIXED params (… exit=opposite-band/VWAP)".

Voice notes, run table (relevant to F3):
```text
| 1 (settings not verified; may have reset) | 2026-04-01 → 2026-07-17 | 48 | $225.64 | $0 (not included) | — | — |
| 2 (all fields read back by Amear) | 2026-04-01 → 2026-07-17 | 41 | $599.08 | $121.36 (= 41 × 2.96) | — | — |
| 3 (full history, same settings) | 2021-03-08 → 2026-07-17 | **1,075** | **$1,281.61** | — | **1.04** | **$4,051.57** |
```

On-disk search for an MNQ/MES point-value record (relevant to F2). It returns only D1 itself:
```text
== point-value records
docs/reports/2026-10-30-3gm-worker1-checklist.md:716:**Verdict: BUG (comment only, no runtime effect). Candidate (ii) confirmed as a wrong comment and refuted as a runtime problem.** OBSERVED: the comment is wrong for NQ. The project records point value 20 (`d
```

## Findings

| id | row attacked | severity | claim | evidence | grade should be |
|---|---|---|---|---|---|
| F1 | R17, R23 (sizing) | **MAJOR** | "DEVIATION (unauthorised)" is graded above its evidence. Spec L49 says the vol-target sizing belongs to variant **(c) = (b) + vol-target sizing**, so variants (a) and (b) are, per the spec, the unsized forms. DL:42 locks the first build to "exit=opposite-band/VWAP", which is (a)/(b), and spec L97 maps `ExitMode` to {OppBand, BandOrVWAP} with no +vol-target member. An unsized build is therefore the spec's variant (b), not a departure from it. Spec L52/L55/D11 do list vol-target as a paper "default", so the spec is internally ambiguous. Ambiguity cannot support a definite "unauthorised" grade. D1 itself concedes the "mitigating reading" and then grades against it. Effect: the unauthorised count goes from 3 to 1, and the master is sent to ask for a trader ruling on something the spec already scopes as a separate variant. | spec L49, L52, L97 pasted above; DL:42; my DL grep shows no sizing row either way | **SPEC-SILENT** (the spec does not state what sizing the paper used for variants (a)/(b), so fixed 1 contract cannot be compared), or DEVIATION (authorised, DL:42) if the master accepts the (a)/(b) reading. Not "unauthorised". |
| F2 | R25 ($5.00/point comment) | MINOR | The verdict (BUG, comment only) stands. The stated explanation, "$5/point is the MNQ-style value of $0.50 × 10", has no pasted evidence (an S1 breach), and nothing on disk records an MNQ or MES point value (grep above). From base knowledge, UNVERIFIED on disk: MNQ is $2/point and $0.50/tick, while $5/point and $1.25/tick is the **MES** (Micro E-mini S&P) spec. "$0.50 × 10" matches neither contract. | grep above returns only D1:716 | Keep BUG. Strike the MNQ explanation, or mark it UNVERIFIED and correct it. |
| F3 | R4, R14 ("all three hand runs used BandOrVWAP") | MINOR | voice:33 lists the saved-template settings. voice:38 says run 1's "settings not verified; may have reset". BandOrVWAP is the code default (line 118), so run 1 probably used it, but that is INFERRED, not REPORTED. The same caveat applies to run 1's trading-hours template, on which R9's RTH-only VWAP depends. | run table pasted above | Say "runs 2–3 REPORTED BandOrVWAP; run 1 INFERRED from the code default". |
| F4 | R14, R17, R23 ("unauthorised" half) | MINOR | The S1 evidence for "no authorising row" covers only DECISIONS.md (the sizing grep in R17 and the noise/4uu grep in the appendix). The DECISION_LOG.md grep for sizing and for same-side/OppBand is asserted in process-log step 3 but never pasted. My re-run (above) confirms the conclusion, so this is an evidence gap, not a wrong result. | DL grep above | Paste the DECISION_LOG grep. |
| F5 | R8, R10, R15 (minute-of-day) | MINOR | `mod = Time[0].Hour*60+Minute` is correct only if NT8's display time zone is ET. D1 never states this dependency. It is implicitly supported: Amear's 9:31 first bar and 16:00 last bar on the CME RTH template (voice:23) imply ET display, because a CT display would show 8:31 and 15:00. | .cs:143, 57–58; voice:23 (pasted in D1 R18) | Add one sentence tying `OpenMod`/`CloseMod` to the REPORTED 9:31 and 16:00 stamps. The grades stand. |
| F6 | R15, R24 (16:00 flat) | MINOR | The analysis of whether the FlatEOD exit fills omits `TimeInForce = TimeInForce.Day` (.cs:111). A Day-TIF market exit submitted on the 16:00 bar's close might expire at the session end rather than fill at the next day's 09:31 open. That is INFERRED runtime behaviour. It adds a third possible outcome to the existing CANNOT-DETERMINE. | .cs:111 (`TimeInForce = TimeInForce.Day;`, read in this session) | Grade unchanged (CANNOT-DETERMINE-STATICALLY). Add TIF to the list of things the trade-list check must resolve. |
| F7 | R8, R29 (citation form) | MINOR | The criterion asks for the paper page as the spec cites it. R8 cites "spec L30 §1; spec L94 §6" with no page, although L30 sits under the §1 heading "(§3, pp. 6–7)" and cites Fig. 1 p. 8. R29 cites spec L36 (p. 9) and L61 (p. 13) without the pages. | D1 R8 and R29 rule lines (re-read) | Add the pages. |

## Attacks tried that did NOT break (with the case tried)
- **Off-by-one minute-of-day (attack 1).** Under end-stamping, the history close at key M is the close of the bar stamped M (.cs:143, 167). The checkpoint uses `Close[0]` of the bar stamped M (.cs:196, 200). Both use the same bar convention, so there is no offset. `rec.Open` is `Open[0]` of the first RTH bar (.cs:152), which is the 09:31-stamped bar covering 09:30–09:31. Its Open is the 09:30 opening trade (voice:23–27, REPORTED). The 16:00 close is stored under key 960 but is never a checkpoint: `mod < CloseMod` (.cs:196), and the `mod >= CloseMod` return (.cs:189–193) comes first. `BuildBand(960)` affects only the plots. **No impact.**
- **Look-ahead (attack 2).** `BuildBand` reads `history` (committed days only), `todayOpen`, `prevClose`, and the VWAP accumulators (.cs:238–267). `CommitDay` runs before `today` is replaced (.cs:149–151), and `today` is never read by `BuildBand`. `todayOpen` is the first RTH trade. `prevClose = Close[1]` is the prior session's last bar. Both are known at the open. The VWAP includes the current bar, which is closed under OnBarClose. **No break.**
- **VWAP pre-RTH contamination (attack 3).** Bar 0 returns at .cs:140. Every bar before the first `IsFirstBarOfSession` returns at .cs:163–164 (`haveDay` false) before any accumulation. The reset (.cs:158–159) runs before the first-bar accumulation (.cs:171–176). Under the RTH template, no ETH bar exists. Contamination needs a non-RTH template, which is a configuration risk, not a code break (see F3 for run 1). **No break.**
- **R14 OppBand.** Spec L38, L49, and L59 say "opposite", and DL:42 literally says "opposite-band". The code uses the same-side band (.cs:45, 209, 217, 299). D1 states the L59/L61 ambiguity openly. DEVIATION (unauthorised) **stands.**
- **R19 fallback unreachable.** .cs:140 returns when `CurrentBar < 1`, so `CurrentBar >= 1` always holds at .cs:155. **Claim confirmed.** The "first session never committed" consequence is also correct: `CommitDay` sees `today == null`.
- **R20 SPEC-SILENT.** The walk-back substitutes older days only when a day lacks the minute. The spec does not address missing minutes or half-days. **Stands.**
- **R21.** `curLower ≤ curUpper ≤ stop` holds even when σ = 0 and open = prevClose, so Exit and Enter both fire on every reversal. CANNOT-DETERMINE **stands.**
- **R27.** The DL:351 "StopMarket" hit is a grep negative-control record of the order calls, not a decision. I extracted its context. **Claim confirmed.**
- **Coverage (attack 6).** Every required topic has a row: entry (R11), σ (R5), Max/Min (R6), VWAP and the exit (R9, R13, R22), checkpoints and the bounds (R10, R28), session and the 16:00 flat (R15, R24), sizing (R17, R23), Lookback (R20), prevClose (R19), and reversal (R12, R21). The 17 §A rows map to R1–R17 and the 7 §C bullets to R18–R24, confirmed by the byte-identical re-run of D1's `sed -n` of the 4uu report lines.
- **S1 fidelity (attack 5).** All 112 commands in all 31 blocks re-run identically. The summary counts (15/0/3/2/4/5 = 29) match both the table and the body.

## Files staged
None.

Result: FAIL (F1 MAJOR stands: R17/R23 "DEVIATION (unauthorised)" is graded above the spec's own variant taxonomy; F2–F7 MINOR)

VERDICT: FAIL
