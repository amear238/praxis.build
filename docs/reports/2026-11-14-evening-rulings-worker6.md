# Evening rulings, worker 6: F3/F4, fgd/ckh/D7, drawdown gate, commission, Block 2 fill spec

## Task
Read-only research on five questions about the strategy-search loop in the 2026-11-13 Hermes handoff (`docs/reports/2026-11-13-hermes-handoff-strategy-search.md`). HEAD 9ff8a48.

## Mode
BUILD (read-only research; the only file written is this report).

## Criterion
Brief items 1-5. Paste commands and outputs (S1). Grade OBSERVED vs INFERRED. Report conflicts as findings; do not resolve them.

## Process log

Calls 1-12: report skeleton; handoff :51-88, :105-111 and rubric :17-44; `bd show` 4uu/fgd/ckh; git grep in HEAD DECISIONS.md and specs; DECISION_LOG grep (working tree, grep only); D6 report via `git show HEAD:`; cost-model JSON at HEAD. No tracked file, bead or index touched.

## Verification evidence and findings

### Item 1: F3 and F4

```
$ sed -n 17,44p specs/SPEC_RUBRIC.md   (excerpt, verbatim lines)
## FROZEN — nothing downstream may proceed until these clear
### F3 — Backtest fill resolution vs. acquired data granularity
**Why frozen.** The Block 2 spec requires Order Fill Resolution = High with a
1-tick resolution series, 1-tick slippage, $2.96 round-trip. Deviation F
**Unblocks when.** The assumption is committed and the backtest report carries
it as a stated limitation.
**Blocks.** `4uu`. Everything downstream of `4uu`.
### F4 — MFFU automation compliance
**Blocks.** Block 4. Block 5.
$ git diff --quiet HEAD -- specs/SPEC_RUBRIC.md && echo "rubric unchanged vs HEAD"
rubric unchanged vs HEAD
$ bd show Praxis_build-4uu | head -30   (excerpt)
◐ Praxis_build-4uu · b2-signal-repro: re-implement Noise-Area Breakout entry logic in NinjaScript + reconcile vs live/sim TV alerts   [● P2 · IN_PROGRESS]
  4uu closes on auditor PASS of those checks once VM output lands.
$ git grep -n '4uu' HEAD -- DECISIONS.md specs | cut -c1-260 | head -20
HEAD:DECISIONS.md:243:**Unblocks:** Praxis_build-6bw real-data validate+run (in volume-only mode, once raw/ is fully populated) → NT8 re-import → 4uu reconcile → zi1 (WFA) → ajj (MC) → xdr (refdist).
HEAD:specs/SPEC_RUBRIC.md:31:**Blocks.** `4uu`. Everything downstream of `4uu`.
$ git grep -n -E '\bF3\b' HEAD -- DECISIONS.md | cut -c1-260 | tail -20
(no output)
$ git grep -c -w 'F3' HEAD -- DECISIONS.md
HEAD:DECISIONS.md:34
```

**FINDING 1a (OBSERVED): the brief's `\bF3\b` command is a false negative.** It printed nothing; `-w F3` finds 34 lines. Anyone reading "no output" as "F3 never addressed" would be wrong.

**FINDING 1b (OBSERVED): an F3 assumption IS committed, as a CONDITIONAL, and F3 is NOT recorded as cleared.**
```
HEAD:DECISIONS.md:247:## 2026-10-30 — D-2026-10-30-A: F3 backtest fill resolution (CONDITIONAL, void clause live) + band-edge slippage [N] = 2 ticks/side (locked by Amear); ...
:258 (b) ... `Order fill resolution` = **Standard**, set explicitly ... No secondary / 1-tick series. Slippage **2 ticks per side** ...
:300 NEEDS AMEAR 5 → RULED: "Commit conditional + R3 control tomorrow." ... Identical → (c) is OBSERVED and F3 moves to PASSED by Amear's edit of `specs/SPEC_RUBRIC.md`; different → the `2026-08-29T00:10:00Z` void clause fires
:301 NEEDS AMEAR 2 → RULED: "Yes — the 10-28 notes are the writing."
:302 NEEDS AMEAR 4 → RULED: limitation sentence APPROVED as proposed. Every backtest report carries: [the limitation sentence; output cut here so the sentence appears once, as this report's last line]
:304 **Status after these rulings:** CONDITIONAL, committable; bead zyd (c) closes on the 2026-10-31 control result, not on this entry.
:342 - **F3 — Backtest fill resolution** (`specs/SPEC_RUBRIC.md:45-57`): untouched. ... F3 stays FROZEN until a backtest report carries the limitation sentence
DECISION_LOG :647 [2026-10-31T15:03:07Z] WHO: amear ... the Future-row baseline, where the Standard-vs-High control (R-F3-1) is then run.
$ grep -c 'R-F3-1' DECISION_LOG.md
3
```
The three R-F3-1 rows are :458 (the ruling), :647 (deferral to the Future-row baseline) and :651 (a voice handoff). None records a control result (OBSERVED, for that label). Whether the control ran under some other label is UNVERIFIED. The rubric still lists F3 under FROZEN at HEAD (OBSERVED).

**FINDING 1c (OBSERVED, stale citations):** D-2026-10-30-A (:251), :342 and :1038 cite F3 at `specs/SPEC_RUBRIC.md:45-57` / `:45`. At HEAD, F3 sits at :19-31. Named here, not fixed.

**OPEN QUESTION (not resolved): are the loop's new-strategy backtests "downstream of `4uu`"?**
- Reasons to say no (OBSERVED text): 4uu is the Noise-Area Breakout re-implementation. The only downstream chain on record is DECISIONS.md:243 (`4uu reconcile → zi1 (WFA) → ajj (MC) → xdr`), which names no new strategy. F3's "Why frozen" talks about a *band-touch* strategy. The handoff loop skips the Noise-Area arms (handoff :71).
- Reasons to say yes (OBSERVED text): F3's Criterion is generic ("The fill resolution the Strategy Analyzer will actually run at ... stated in writing before the backtest runs"). The section header says "nothing downstream may proceed until these clear". The loop runs exactly the configuration F3 is about: 1-minute bars, Standard, no intrabar series (handoff :65).
- Related facts (OBSERVED): the loop's settings match D-2026-10-30-A (b). The ruled limitation sentence is for "Every backtest report" (:302). Handoff :51-88 does not tell loop reports to carry that sentence. I did not read the rest of the handoff, so whether it says so elsewhere is UNVERIFIED.
- I make no claim that F3 is cleared.

**F4 (OBSERVED + INFERRED):** F4 blocks Block 4 and Block 5. Rubric :95 says "Block 4 paper trading". What Block 5 covers was not checked (UNVERIFIED). The loop in handoff :60-71 is: write rules, code NinjaScript on the Mac, backtest through the VM bridge, score, log. It names no paper, sim-live or funded order path, and handoff :95 keeps "any order path to a funded account" as a hard limit. INFERRED: the loop as written touches neither Block 4 nor Block 5. Note that the handoff's "builds resume" (:55) after three contenders does not override F4.

### Item 2: fgd, ckh, D7

```
$ bd show Praxis_build-fgd | head -30   (excerpt)
○ Praxis_build-fgd · F2 amendment S6 follow-ups F-1..F-9: specs/code still citing 11:30 close or 15:00-18:00 disable (topology ..., Noise-Area ruleset ..., WF values :65, Flat1559.cs :31, OPEN-F2-5)   [● P2 · OPEN]
  2026-11-13 17:00Z run: OPEN-A1 landed 9bf653a (D-2026-11-13-B, option a, CONDITIONAL; strike ended at 1). OPEN-A2 landed 661e073 (D-2026-11-13-C, ...). Remaining: F-4/F-5 wait for parked diq; F-6 optional; F-8 not edited under D1; residuals OPEN-F2-1 and the 15:00-18:00 lockout overlap with the 4:10 alert step.
$ bd show Praxis_build-ckh | head -30   (excerpt)
○ Praxis_build-ckh · R6 research P0 under D7: Pre-Announcement Drift and Announcement-Day Premium on existing 1-minute data, own worktree, nothing bought   [● P0 · OPEN]
  ... before any build read the MFFU T1 news rule and whether an evening entry counts as the same trading day. Noise-Area baseline continues through VM tests for the record (D7).
  2026-11-12 PARKED (absolute park rule, audit-fail-x2): ... A human resumes; cure recipe in HANDOFF top card ... No R6 code exists.
$ git show HEAD:DECISIONS.md | sed -n 1940,1944p
D7  If D6 fails at every tier at 1 MNQ: do not design breaker values
    to fit the drawdown ceiling (that is curve-fitting). Report it, and
    pull R6's research (higher-win-rate, steadier-equity strategies)
    forward to P0. The Noise-Area baseline continues through the VM
    tests for the record, but a GO on MFFU is not expected from it.
```
- **fgd** (OBSERVED): P2, OPEN. It covers the spec/code follow-ups to the F2 breaker amendment, including Flat1559.cs and breaker #4 residual OPEN-F2-1. HEAD's two most recent decision commits (9bf653a, 661e073) are fgd units. INFERRED: the pause (:53, "no NinjaScript for the trading path, breakers, monitor ...") covers fgd's remaining breaker/topology and `.cs` items. Spec-only edits are not named in the pause list, so whether they are covered is an OPEN QUESTION.
- **ckh** (OBSERVED): P0, OPEN, and PARKED under the absolute park rule with "A human resumes". It is not in the pause list. It is research, not a named build type.
- **FINDING 2a (conflict, not resolved):** handoff :111 says the two parked announcement ideas "also become loop candidates under the new screen". Three points of friction with ckh: (i) ckh is parked and its note says "A human resumes"; the loop picking up its two ideas would resume that work without the human step. (ii) ckh's precondition, "before any build read the MFFU T1 news rule", is not in the loop's steps at :60-69. (iii) handoff :111 also lists "the parked announcement-strategy research decision" as still open, and the handoff says to carry it, not resolve it.
- **FINDING 2b (D7 vs the pause, possible conflict):** D7 says "The Noise-Area baseline continues through the VM tests for the record". The pause (:53) stops "walk-forward runs on existing strategies". Whether those Noise-Area "VM tests" count as walk-forward runs is an OPEN QUESTION.
- **D7 vs the loop (INFERRED, no literal conflict):** the loop is broadly what D7 asks for when it pulls "R6's research ... forward to P0". D7's curve-fitting bar is aimed at *breaker values*. The loop tunes *strategies* against the same drawdown ceiling. The overfitting guard (:84-88) limits that, but whether it respects D7's intent is Amear's call. D7 names "higher-win-rate, steadier-equity strategies"; the contender bar (:73-82) has no win-rate term.

### Item 3: drawdown gate
```
$ git show HEAD:DECISIONS.md | sed -n 1735,1740p
A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80%
    of the ruled limit, i.e. below the lower of 3.2% of the MFFU
    account size and 80% of MFFU's trailing drawdown limit. This
$ git cat-file -e HEAD:docs/reports/2026-11-09-d6-drawdown-check-manager.md && echo present
present
$ git show HEAD:<D6 report> | grep -n -i -E 'four|measure|50K|...' | cut -c1-260 | head -25   (excerpt)
19:Ceiling for each row = below min(3.2% of size, 80% of MFFU limit) (A4). Verdict = PASS only if all 17 windows are strictly below the ceiling. Two measures are shown:
21:- **VS4**: the committed values-spec measure (...walk-forward-values.md :139). It is the worst of four: WIN's two, plus the same two carried across windows.
31:| Rapid 50K, Rapid EOD 50K, Pro 50K, Builder 50K | $1,600 | FAIL all | FAIL all |
32:| Builder 50K add-on | $1,200 | FAIL all | FAIL all |
116:   124	| Builder · 50K | $50,000 | $2,000 | $2,000; $1,500 with add-on (EOD trailing) | **$2,000**; with add-on min(2,000, 1,500) = **$1,500** | ...
$ git show HEAD:<D6 report> | grep -n -i -E 'four[- ]measure' | cut -c1-300   (excerpt)
222:Pro 150K             ceiling 3600.00 | within-window (brief's rule): PASS  fails=[] | four-measure (values spec 6): FAIL  fails=[16, 17]
226:W1's verdict line ...: under the committed four-measure rule, Pro 150K fails in windows 16 and 17
229:1. **Within-window vs four-measure.** Accepted. ... The D7 test is judged on VS4 (Decision 5).
```
- **$1,600 (OBSERVED + arithmetic):** 3.2% × 50,000 = $1,600, and 80% × $2,000 trailing = $1,600. The two are equal, so neither is lower. The D6 report prints $1,600 for Rapid, Rapid EOD, Pro and Builder 50K (:31). **FINDING 3a:** the Builder 50K *add-on* row has a $1,500 trailing limit, so its ceiling is $1,200 (:32). That means "For a 50K account that is $1,600" does not hold for every 50K row on record. The handoff (:109) also says MFFU tier figures are unconfirmed for 100K/150K; for 50K they come from the record and were not re-checked against MFFU (UNVERIFIED).
- **"four-measure basis" (OBSERVED):** the phrase appears 5 times in the D6 report as "four-measure" (:222-229) and is the same thing as **VS4**, "the worst of four" (:21). D6 judged the D7 test on VS4 (:229, Decision 5). INFERRED: the handoff's phrase means VS4. **FINDING 3b:** VS4 is a per-window measure (17 windows of 63 sessions, :7/:19), while A4 says "backtest max drawdown". D6 Decision 5 (:64) bridges the two. The handoff applies the gate to a "full five-year backtest" (:76) without saying whether drawdown is taken per window or over the whole period. Named, not resolved.

### Item 4: commission
```
$ git grep -n -E '4\.68|2\.96|1\.90' HEAD -- DECISIONS.md | cut -c1-200 | head -20   (excerpt)
HEAD:DECISIONS.md:970:- (iii) R-VN4-6 with the fee report (...mffu-fee-check.md:7-10): MFFU's own page gives NQ $4.68 round trip (MNQ $1.90), not $5.76; $5.76 on that page is YM
HEAD:DECISIONS.md:1118:## 2026-11-06 — D-2026-11-06-C: cost model amendment — MFFU published round turn NQ $4.68 / MNQ $1.90 (ruling 2)
$ git show HEAD:config/backtest-cost-model.json | grep -n -i -E 'commission|version|mnq'   (excerpt)
19:    "commission_round_turn_usd": 4.68,
22:    "commission_round_turn_usd_mnq": 1.90,
$ git show HEAD:<D6 report> | grep -n -i -E '1\.90|4\.68|2\.96|...'   (excerpt)
49:- **Inputs.** Each trade list is an NT8 grid CSV at 1 NQ per trade. Commission is $2.96 on every row, ...
52:  - MNQ net = points × $2 − $1.90 (cost model v1.2.0). This equals the committed rule "MNQ net = (NQ gross ÷ 10) − $1.90" (values spec :139).
66:7. **NQ commission.** The v1.2.0 rate of $4.68 is used, not the CSV's $2.96.
$ git show HEAD:DECISIONS.md | sed -n 1911,1916p   (D2, verbatim)
D2  Only four things stop and wait for Amear's word: (a) spending
    money; (b) switching live trading on, or any order path to a
    funded account; (c) changing circuit-breaker values while real
    money is at stake; (d) installing keys, credentials or agent
    permissions. Everything else is D1.
```
- **$4.68 is NQ** (OBSERVED, :970, :1118, JSON :19). MNQ is $1.90.
- **FINDING 4a (mismatch):** bar item 3 measures drawdown at 1 MNQ, and the committed MNQ rule is "(NQ gross ÷ 10) − $1.90" (D6 :52). Bar item 2 (:75) and the gate at :67 require a "$4.68 run", which is an NQ commission. A $4.68 NQ run does not price the 1-MNQ drawdown test: the gate uses $1.90.
- **FINDING 4b:** D6 did not use an NT8 run at $4.68. It re-priced a $2.96 CSV from fill prices (:49, :66). So the record shows the $4.68 / $1.90 costs can be applied in post-processing. The handoff's rule that no candidate can be a contender "until it has a $4.68 run" is stricter than the method the handoff itself points to for the gate. Named, not resolved.
- **D2 (INFERRED from D2's text):** changing NT8's commission setting is not (a) spending money, not (b) an order path, not (c) breaker values, and not (d) keys, credentials or agent permissions. By D2's own text it is a D1 item. The handoff calls it "Amear's hand step" (:73) but does not call it D2. A hand step (the VM GUI is in Amear's hands) is not the same as a D2 hold. No conflict is asserted. Also OBSERVED: the record's cost model was already set to $4.68 on 2026-11-06 (D-2026-11-06-C); only the NT8 setting lags. That is the handoff's claim and was not checked on the VM (UNVERIFIED).

### Item 5: Block 2 spec text vs the loop

| Term | F3 "Why frozen" quotes the Block 2 spec | Loop (handoff :65, :73) | Record at HEAD |
|---|---|---|---|
| Order Fill Resolution | High | Standard | Standard (D-2026-10-30-A (b), CONDITIONAL) |
| Intrabar series | 1-tick resolution series | none (1-minute bars) | none (D-2026-10-30-A (b)) |
| Slippage | 1 tick | 2 ticks per side | 2 ticks/side (D-2026-10-30-A, locked by Amear) |
| Commission | $2.96 RT | $4.68 RT required for contender; "screening, $2.96" until set | $4.68 NQ / $1.90 MNQ (D-2026-11-06-C) |

All four terms differ. F3's text at HEAD still quotes the superseded spec terms. D-2026-10-30-A :284 names the spec lines that still carry them and does not edit them (OBSERVED). The rubric text has not been updated to match the later decisions. That is a finding only; the F3 grade belongs to Amear.

## Files staged
None. The only file written is this report, and it is untracked and not staged.

## Result
PASS (research complete). The findings above are reported, not resolved: 1a, 1b, 1c, the F3 open question, 2a, 2b, 3a, 3b, 4a, 4b.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
