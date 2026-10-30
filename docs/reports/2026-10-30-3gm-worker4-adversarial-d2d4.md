# 3gm worker 4: adversarial review of worker 2's D2/D3/D4 report

## Task
Unit `Praxis_build-3gm`. Try to break `docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md` (the D2 bar-timing walk, the D3 order inventory and slippage formula, and the D4 run-1 vs run-2 ranking).

## Mode
ADVERSARIAL, read-only. This is the only repo file written. Scratch files are in `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/w4/`. Nothing was staged, and nothing was written to agent-memory.

## Criterion
The brief's rubric lines are S1 (every claim backed by pasted command output), S2 (no claim graded above its evidence; NT8 runtime behaviour is INFERRED unless a file records an observation of it) and S8 (Amear's questions are not answered for him). D4 must not claim to resolve the gap, and it must end with exact NT8 fields to read back. I did not open `specs/SPEC_RUBRIC.md`. The criterion text above is the brief's.

## Process log
1. Re-hashed the strategy file. It matches `35393823…2752265` (312 lines).
2. Read the whole artifact (711 lines) and `cat -n` of the strategy.
3. Checked where `$121.36` comes from, the `TraceOrders` count, spec lines 57–61, DECISION_LOG lines 353 and 443, and whether any file outside `docs/` records NT8 runtime behaviour.
4. Ported lines 200–229 and 261–264 to python and fuzzed them (2,000,000 single-checkpoint cases). I also ran a 200,000-path state-machine test of the D4 #5 "OppBand gives fewer trades" claim.
5. Re-ran every read-only `$ ` command pasted in the artifact (36 of them) and diffed each against its pasted output. I then explained the two diffs.

## Verification evidence

### Hash
```
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
     312 ninjascript/PraxisNoiseAreaBreakout.cs
```

### Fuzz of the ported checkpoint logic (attack 2 and attack 4)
Script `scratchpad/w4/fuzz.py`:
```python
import random
LONG,SHORT,FLAT='L','S','F'
def band(todayOpen, prevClose, sigma, k=1.0):           # lines 261-264
    refU=max(todayOpen,prevClose); refL=min(todayOpen,prevClose)
    return refU*(1.0+k*sigma), refL*(1.0-k*sigma)
def checkpoint(price, up, lo, vwap, volpos, mp, mode):  # lines 200-229; mp = pre-fill state
    acts=[]
    if mp==LONG:
        stop = max(up,vwap) if (mode=='BandOrVWAP' and volpos) else up
        if price<=stop: acts.append('XL')
    elif mp==SHORT:
        stop = min(lo,vwap) if (mode=='BandOrVWAP' and volpos) else lo
        if price>=stop: acts.append('XS')
    if price>up and mp!=LONG: acts.append('EL')
    elif price<lo and mp!=SHORT: acts.append('ES')
    return acts
random.seed(3)
N=2_000_000; rev=0; rev_noexit=0; both=0; per={}
for i in range(N):
    grid = random.random()<0.5      # half the cases on a coarse 0.25 grid to force ties
    def px(a,b): 
        v=random.uniform(a,b); return round(v*4)/4 if grid else v
    o=px(1,30000); pc=px(1,30000)
    sigma=random.choice([0.0, random.uniform(0,0.05), random.uniform(0,2.0)])
    up,lo=band(o,pc,sigma)
    price=px(0.5,max(up,1)*1.5) if random.random()<0.8 else random.choice([up,lo])
    vwap=random.choice([px(0.5,max(up,1)*1.5), up, lo, price])
    volpos=random.random()<0.9; mp=random.choice([LONG,SHORT,FLAT]); mode=random.choice(['OppBand','BandOrVWAP'])
    a=checkpoint(price,up,lo,vwap,volpos,mp,mode)
    isrev=(mp==LONG and 'ES' in a) or (mp==SHORT and 'EL' in a)
    if isrev:
        rev+=1; ex=('XL' in a) or ('XS' in a)
        if ex: both+=1
        else: rev_noexit+=1
        per[(mp,mode,volpos)]=per.get((mp,mode,volpos),0)+1
print('cases',N,'reversals',rev,'reversal WITH explicit exit',both,'reversal WITHOUT exit',rev_noexit)
print('reversals by (state,mode,vol>0):',sorted(per.items()))
# --- Path claim D4#5: is trade count(OppBand) <= count(BandOrVWAP)? clean-fill model:
# decisions on pre-fill state; exit/entry fills before next checkpoint; flatten at day end.
def run(path, mode):
    mp=FLAT; trades=0
    for (price,up,lo,vwap) in path:
        a=checkpoint(price,up,lo,vwap,True,mp,mode)
        if 'XL' in a or 'XS' in a: mp=FLAT
        if 'EL' in a: mp=LONG; trades+=1
        if 'ES' in a: mp=SHORT; trades+=1
    return trades
viol=0; more=0; P=200000
for i in range(P):
    path=[]
    for c in range(12):
        lo=random.uniform(90,100); up=lo+random.uniform(0,10)
        path.append((random.uniform(80,120),up,lo,random.uniform(80,120)))
    o,b=run(path,'OppBand'),run(path,'BandOrVWAP')
    if o>b: viol+=1
    if b>o: more+=1
print('paths',P,'OppBand>BandOrVWAP count:',viol,' BandOrVWAP>OppBand:',more)
```
Output:
```
$ python3 -I $W/fuzz.py
cases 2000000 reversals 305112 reversal WITH explicit exit 305112 reversal WITHOUT exit 0
reversals by (state,mode,vol>0): [(('L', 'BandOrVWAP', False), 6355), (('L', 'BandOrVWAP', True), 56911), (('L', 'OppBand', False), 6248), (('L', 'OppBand', True), 57161), (('S', 'BandOrVWAP', False), 8937), (('S', 'BandOrVWAP', True), 80380), (('S', 'OppBand', False), 9032), (('S', 'OppBand', True), 80088)]
paths 200000 OppBand>BandOrVWAP count: 0  BandOrVWAP>OppBand: 66556
```
**Reading.** In both modes, and in the `vwapCumVol == 0` branch, every reverse-entry input also meets the explicit-exit condition: 0 of 305,112 cases break this. That includes σ = 0 and exact ties on the band and VWAP values. The report's algebra is right **at the code level**. A short proof backs up the path test. The two modes' states can only diverge as (OppBand in a position, BandOrVWAP flat). From that divergent state, BandOrVWAP never takes fewer new entries than OppBand, and the states re-merge. So under clean fills, OppBand gives ≤ trades. D4 #5's direction holds, and it is correctly labelled INFERRED. The fuzz does **not** test NT8 behaviour. It assumes `Position.MarketPosition` does not change inside one `OnBarUpdate` call.

### Provenance of the commission figure and other checks (attacks 2 and 5)
```
== 121.36 repo-wide (incl. untracked, excl .git)
./docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md:55: ... | $121.36 (= 41 × 2.96) | — | — |
./docs/reports/2026-10-28-voice-session-notes.md:39:| 2 (all fields read back by Amear) | 2026-04-01 → 2026-07-17 | 41 | $599.08 | $121.36 (= 41 × 2.96) | — | — |
./DECISION_LOG.md:443:- [2026-10-30T21:37:00Z] WHO: praxis-master | WHO OBSERVED: amear ...
== TraceOrders count
0
== spec 57-61
- **Base stop:** trailing stop at the **opposite** Noise-Area boundary (long stops at Lower/Upper as it trails; base model = "Stop @ Opp. Band", Table 1). Evaluated only at semi-hourly stamps.
== non-docs observations of NT8 runtime
./DECISION_LOG.md:353: ... (the line the report already quotes)
./ninjascript/PraxisSignalConsumer.cs:84:				IsExitOnSessionCloseStrategy             = false;
./ninjascript/PraxisNoiseAreaBreakout.cs:108: ...
./ninjascript/PraxisNoiseAreaBreakout.cs:109: ...
```
DECISION_LOG:443 (fragment): `**2** (same range, all fields read back) 41 trades, $599.08, commission $121.36 = 41 × 2.96`. The figure is recorded as REPORTED BY AMEAR. The record does not show whether Amear read $121.36 off the screen or the voice-side Claude computed it from 41 × 2.96. The report does not raise this question.

Outside `docs/`, no file records an observation of NT8 fill timing, EOSC or slippage behaviour. The report's "all INFERRED" grading of NT8 runtime behaviour therefore stands, and my wider search confirms it.

### S1 fidelity: all 36 re-runnable pasted commands re-run and diffed (attack 6)
Script `scratchpad/w4/s1.py`: for every `$ ` line inside a code fence, it re-runs read-only commands and runs `difflib` against the pasted lines. It skips `$W/...` and `<placeholder>` commands.
```
--- pasted
+++ rerun
@@ -1 +1 @@
-      56
+     166
--- pasted
+++ rerun
@@ -1 +1 @@
-      20
+      54
report:29 | shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs | 1 lines | IDENTICAL
report:31 | wc -l ninjascript/PraxisNoiseAreaBreakout.cs | 1 lines | IDENTICAL
report:37 | sed -n '22,44p' docs/reports/2026-10-28-voice-session-notes.md | 23 lines | IDENTICAL
report:66 | sed -n '156p' docs/reference/2026-07-24-nt8-windows-reference.md | 1 lines | IDENTICAL
report:69 | /usr/bin/grep -niE 'session template|trading hours|RTH|never captured|not captured' docs/r | 4 lines | IDENTICAL
report:81 | sed -n '353p' DECISION_LOG.md | 1 lines | IDENTICAL
report:89 | /usr/bin/grep -niE 'managed approach|next bar|ExitOnSessionClose|exit on session close|sli | 3 lines | IDENTICAL
report:97 | /usr/bin/grep -rniI 'managed approach\|next bar\|ExitOnSessionClose\|exit on session close | 1 lines | DIFF
report:162 | sed -n '43p;56p' docs/reports/2026-07-16-4uu-noise-area-strategy.md | 2 lines | IDENTICAL
report:166 | sed -n '95,104p' docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md | 9 lines | IDENTICAL
report:178 | sed -n '1,12p' docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md | 12 lines | IDENTICAL
report:205 | /usr/bin/grep -n 'Close1600' ninjascript/PraxisNoiseAreaBreakout.cs | 2 lines | IDENTICAL
report:209 | /usr/bin/grep -ciE 'early|half-day|half day|holiday|partial' docs/specs/2026-07-16-b2-nois | 1 lines | IDENTICAL
report:212 | /usr/bin/grep -ciE 'early|half-day|half day|holiday|partial' ninjascript/PraxisNoiseAreaBr | 1 lines | IDENTICAL
report:215 | /usr/bin/grep -ciE 'end-stamp|start-stamp|bar stamp|timestamp' docs/specs/2026-07-16-b2-no | 1 lines | IDENTICAL
report:220 | /usr/bin/grep -niE 'early|half-day|half day|holiday|partial' docs/specs/2026-07-16-b2-nois | 1 lines | IDENTICAL
report:226 | sed -n '36,38p;64p;99p' docs/specs/2026-07-16-b2-noise-area-ruleset.md | 5 lines | IDENTICAL
report:239 | sed -n '140,161p' ninjascript/PraxisNoiseAreaBreakout.cs | 22 lines | IDENTICAL
report:273 | sed -n '163,176p' ninjascript/PraxisNoiseAreaBreakout.cs | 14 lines | IDENTICAL
report:292 | /usr/bin/grep -n Close1600 ninjascript/PraxisNoiseAreaBreakout.cs | 2 lines | IDENTICAL
report:299 | sed -n '178,186p' ninjascript/PraxisNoiseAreaBreakout.cs | 9 lines | IDENTICAL
report:312 | sed -n '238,267p' ninjascript/PraxisNoiseAreaBreakout.cs | 30 lines | IDENTICAL
report:348 | sed -n '188,198p' ninjascript/PraxisNoiseAreaBreakout.cs | 11 lines | IDENTICAL
report:363 | sed -n '200,230p' ninjascript/PraxisNoiseAreaBreakout.cs | 31 lines | IDENTICAL
report:407 | sed -n '270,291p' ninjascript/PraxisNoiseAreaBreakout.cs | 22 lines | IDENTICAL
report:435 | sed -n '97,114p' ninjascript/PraxisNoiseAreaBreakout.cs | 17 lines | IDENTICAL
report:494 | /usr/bin/grep -ciE "early|half-day|half day|holiday|partial" ninjascript/PraxisNoiseAreaBr | 1 lines | IDENTICAL
report:516 | /usr/bin/grep -nE 'Enter(Long|Short)|Exit(Long|Short)|Set(StopLoss|ProfitTarget|TrailStop) | 8 lines | IDENTICAL
report:600 | /usr/bin/grep -rniI 'point value' docs/ | wc -l | 1 lines | DIFF
report:603 | sed -n '218,230p' docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investiga | 13 lines | IDENTICAL
report:621 | python3 -c "print('run3 slippage 1075*2*2*5 =', 1075*2*2*5); print('run3 commission 1075*2 | 10 lines | IDENTICAL
report:633 | echo '41*2.96' | bc | 1 lines | IDENTICAL
report:645 | /usr/bin/grep -nE 'Position\.AveragePrice|SystemPerformance|Account|GetProfitLoss|Executio | 6 lines | IDENTICAL
report:653 | /usr/bin/grep -cE 'Position\.AveragePrice|SystemPerformance|Account|GetProfitLoss|Executio | 1 lines | IDENTICAL
report:656 | /usr/bin/grep -cE 'Position\.MarketPosition' ninjascript/PraxisNoiseAreaBreakout.cs | 1 lines | IDENTICAL
report:659 | /usr/bin/grep -nE 'Unrealized|Realized|Commission|Slippage|Fill|AvgPrice|Bars\.IsLastBarOf | 0 lines | IDENTICAL
commands re-run: 36  diffs: 2
```
I explained the two diffs. They come from files written after the grep ran, and the report counts itself:
```
== rt count excluding 2026-10-30-* files
      56
== per-file contribution from 2026-10-30-* files
docs/reports/2026-10-30-3gm-worker1-checklist.md:10
docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md:100
== pv count excluding 2026-10-30-*
      20
== pasted rt list line count            -> 56
== pasted pv list line count            -> 20
== rerun rt list (excl 10-30) vs pasted list, by file:line keys
rt key lists IDENTICAL
```
That covers the order grep, the null search and its positive control, the arithmetic (python and bc), and the `sed -n` blocks for 188–198, 200–230, 270–291 and DL353. All are byte-identical. The docs-wide counts reproduce exactly once the later `2026-10-30-*` files are excluded. Nothing was fabricated.

## Findings

| id | claim attacked | severity | evidence (pasted above) | correct grade |
|---|---|---|---|---|
| F1 | D3 "Same-checkpoint double fire (**OBSERVED in code**: both calls fire)" and "every reversal … **submits** an explicit exit and a reverse entry on the same bar (**OBSERVED in code**)" | **MAJOR** (S2 label upgrade) | Fuzz: 0/305,112 reversals lack the exit condition, so the code-level condition algebra is right. But the report's own step 4 grades the necessary premise INFERRED: `Position.MarketPosition` stays `Long` between lines 211 and 228, i.e. no in-call fill. "Submits" is also NT8 runtime behaviour (managed internal order-handling rules may ignore a call), and no file records an observation of it. The conclusion inherits the weakest link and is still printed as OBSERVED. | "On every reversal input both branch conditions are true: OBSERVED in code, fuzz-confirmed. That both calls run in one `OnBarUpdate`: INFERRED (pre-fill-state premise). That NT8 submits both orders: INFERRED / CANNOT-DETERMINE-STATICALLY." |
| F2 | D3 "Partial evidence for run 2: $121.36 = 82 × $1.48 … so no run-2 trade carries Qty 2 … It does not exclude outcome (iii)." The text implies the commission identity narrows outcome (ii). | **MAJOR** (S2: evidence presented as discriminating when it does not) | The identity shows only Σ(contract-sides) = 82 = 2 × 41 rows. A double-close that NT8 books as **extra Qty-1 rows** gives commission = rows × $2.96 exactly as well. A net-short-2 position closed by one Qty-2 fill is likely split per entry execution into Qty-1 rows too (INFERRED, no observation). So $121.36 is consistent with (i), (ii) as extra rows, and (iii) alike. It rules out only the Qty-2-row form of (ii). Worse, if (ii) shows up as extra rows, the 41 count is itself inflated. That bears directly on D4. Separately, whether $121.36 was read off the screen or derived by the voice-side Claude from 41 × 2.96 is not established (DL:443 / voice notes:39 print it as `$121.36 = 41 × 2.96`), and the report does not ask. | "INFERRED: the commission total equals 2 × rows × $1.48. It excludes Qty-2 rows only. It does **not** exclude double-close outcome (ii) when booked as extra rows, nor (iii). Readback: count rows sharing an exit timestamp, and executions per reversal timestamp." |
| F3 | D3 slippage condition 1: "Fills per trade = 2 … That fails under double-close outcome (ii)" | MINOR | Same algebra as F2. If every row is Qty 1, contract-sides = 2 × rows still holds under (ii)-as-extra-rows, so the formula holds **per row**. The real exposure is that the 1,075 rows may include spurious double-close rows. Also, tick size 0.25 is used as given, while point value $20 is (correctly) flagged UNVERIFIED. Both come from the same NQCONT instrument definition. | The arithmetic is correct (re-run identical: 21,500 / 3,182.0 / 25,963.61). The conditions should read: "rows are all Qty 1 (as in run 2), and the row count is free of double-close artefacts; tick size and point value both UNVERIFIED." |
| F4 | D4 readback field list ("exact NT8 fields") and hypothesis list | MINOR | The list names Trading hours … Set order quantity, but **not Instrument / data series selection**. Run 1's settings "may have reset" and were not read back, and the voice note confirms NQCONT only for the read-back configuration. A different instrument (e.g. a dated NQ contract with partial data) is a missing count hypothesis. | Add "Instrument (exact name in the Analyzer's left panel)" to the run-1 readback, and add it as a hypothesis (INFERRED). |
| F5 | D2(c) scenario set S1–S4 complete? | MINOR | S1–S4 are explicitly conditioned on "last RTH bar = 16:00 ET stamp", which is INFERRED from one date. One case is omitted. If the template's session ends after 16:00 ET (e.g. 16:15 ET; the actual template hours are an open TODO, ref:156), `FlattenAll` re-fires on 16:01+ bars and FlatEOD fills **same day at 16:01's Open**. That is none of S1–S4. S1's mechanism detail ("last bar ≥ end − 30 s, fills at that bar's Close") is specific but labelled INFERRED. That is acceptable. S4's "least likely" ranking has no evidence behind it (INFERRED). | Add S5: "template ends after 16:00 ET → FlatEOD fills same day at the 16:01 Open; exit name FlatEOD, exit time 16:01 (INFERRED)." |
| F6 | D4 #5 support: "matches the paper's 1.3 vs 1.8 trades/day (spec line 38)" | MINOR | The code's `OppBand` long stop is `curUpper` (same-side band, lines 208–209). The paper's base model is the **opposite** band (spec line 59, pasted). The report itself flags this mismatch under "Other findings", yet still cites the paper's ratio as corroboration for the code's mode. The conclusion holds on independent grounds: path fuzz 0/200,000 violations, plus the divergence proof. | "OppBand ≤ BandOrVWAP trades under clean fills: INFERRED (code-level state argument). The paper ratio is not evidence for the code's OppBand." |
| F7 | S1: "no `TraceOrders` (OBSERVED in the `cat -n` above)"; checkpoint enumeration `$ python3 -c "<enumerate …>"` | MINOR | The report never pastes a full `cat -n`, only `sed` ranges. Re-run: `TraceOrders` count = 0, so the claim is **true** but its cited evidence is not on the page. The checkpoint command is a placeholder and cannot be reproduced. Its output (12 stamps, 10:00–15:30) is right by direct reading of line 196. | Both are true. The S1 evidence is missing or placeholder-only. |
| F8 | S1: docs-wide grep counts 56 and 20 | MINOR | Re-run gives 166 and 54. The difference is entirely the report counting itself plus a sibling 2026-10-30 file. Excluding `2026-10-30-*` reproduces 56 and 20 and an identical file:line key list. | OBSERVED at time of capture. Not reproducible as written without the exclusion. |
| — | D4 "net rose despite added costs ⇒ trade set differed" | no break | Valid given the null search (re-run identical: 0 P&L/fill tokens, positive control 6) and the fact that Analyzer net = trade P&L − costs. It is redundant with the count difference and correctly labelled INFERRED. | INFERRED, which is the grade given. |
| — | D4 #5 "OppBand ⇒ fewer trades" | no break | Path fuzz: OppBand > BandOrVWAP in 0 of 200,000 paths. Proof: divergence only as (O in position, B flat); from there B's new entries ≥ O's and the states re-merge. Valid under clean fills only. | INFERRED, which is the grade given. |
| — | D4 does not claim resolution; it ends with fields | no break | "NT8 readback that would settle it (not resolved here)" ends with an exact field list (see F4 for the gap). | Compliant. |
| — | D2 10:00 checkpoint, 16:00 flatten, early close, template inconsistency, DL353 split | no break | The code facts match `sed` re-runs. DL353's "next bar's open" is correctly graded INFERRED, and no file outside `docs/` records an observation. The early-close analysis is spec-silent and labelled INFERRED/UNVERIFIED. | As graded. |
| — | S8 | no break | No `[N]`, walk-forward or phase decision is made. The suggested one-field-at-a-time re-runs are framed as readbacks. | Compliant. |

## Repo changes suggested (not made)
- Worker 2's report: regrade F1's conclusion, add the F2 caveat that the commission identity does not exclude (ii)-as-extra-rows, add Instrument to the D4 readback (F4), and add S5 (F5).

## Files staged
None.

Result: FAIL

VERDICT: FAIL
