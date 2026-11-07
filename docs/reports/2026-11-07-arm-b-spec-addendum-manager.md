# 2026-11-07 — unit 2026-11-07-arm-b-spec-addendum — manager report

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Task

Record the master's two decisions of DECISION_LOG `[2026-11-07T16:45:00Z] WHO: praxis-master` (made under delegation R-1104-2, DECISIONS.md:748, not Amear's word, changeable by him). Deliverables: (1) `docs/specs/2026-11-06-walk-forward-values.md` → version 2.1 in place: §4 Precedence, T8's matching sentence, §5 Warm-up, T11, and a new §9 subsection "Oracle inputs from the code unit (2026-11-07)"; (2) DECISIONS.md append "D-2026-11-07-B addendum 1"; (3) two MANIFEST rows; (4) this report. Stage nothing, real index untouched, nothing under `.claude/` edited, `ninjascript/PraxisNoiseAreaBreakoutArmB.cs` and `docs/reports/2026-11-07-arm-b-code-manager.md` untouched.

## Rubric criteria addressed (verbatim from specs/SPEC_RUBRIC.md)

- S1 | Every claim in a report has pasted command output, not a description of output. — Met: every claim below points at pasted output in "Verification evidence" (V1–V7).
- S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. — Met: the spec edits are SPECIFIED text only. Grades in the edits: decision (1) SETTLED (master); s16 = 2021-03-29 and N = 1352 OBSERVED by the code unit's data-file trace, with the weekend-bar caveat added after the adversary's NOTE 9; s12 / s20 INFERRED; the enum conversion and the full early-close list UNVERIFIED. The code's behaviour under (1) is cited at WRITTEN level (code report :14, V6). Nothing was compiled or run.
- S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after. — Met for the code landing: the entry (DECISIONS.md:1479–1516) is written before the arm (b) code is recorded in git; the branch does not exist (V5: `0`). Stated in the entry, not hidden: the `.cs` was written before this entry and already keeps the base behaviour decision (1) chooses. Chain: the 16:45:00Z row → R-1104-2 (DECISIONS.md:748).
- S8 | No question that belongs to Amear is answered on his behalf. — Met: nothing is labelled his word (V6: no `WHO: amear` / `RULED` in the new entry; V3 counts "not Amear's word; changeable by him" 4× in the spec). Questions that may be his are listed under "Still Amear's", not answered.
- S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: [the sentence — carried once, at line 3 of this report; not repeated here so that "once" holds] — Met: this report carries it once, at line 3 (V7). The DECISIONS entry states no backtest or P&L figure, and says so (adversary finding 13).

## Workers dispatched

| id | mode | outcome |
|---|---|---|
| ab1aab911c2ba8f1b | ADVERSARIAL (read-only fidelity pass on spec v2.1, the entry and the MANIFEST rows) | VERDICT: PASS. 0 BLOCKING, 4 MINOR, 4 NOTE. MINOR 7, MINOR 8, NOTE 9 and NOTE 12 fixed in place; MINOR 5 and MINOR 6 disclosed, not edited (out of scope) |

The manager made the edits as pure doc edits by script (`scratchpad/u/edit_spec.py`, `splice.py`, `fix1.py`), under the brief's "or do it yourself" option. No BUILD worker.

## Process log

1. Baseline 2026-11-07T16:38:28Z (V5 "before"): HEAD afea575; `.cs` and code-report shas; index hashes; `git branch --list 'arm-b*' | wc -l` = 0; MANIFEST `2 0`. The 16:45:00Z row is stamped later than this clock reading; the row itself says "WHEN: ~16:45Z 11-07 (estimate)". It was already at DECISION_LOG.md:695 when read.
2. Read the row (DECISION_LOG.md:695) in full, the code report :605–:655, E6 (:523–:539), E10 (:587–:604), R19 (d1 :89), the rubric (:107–:119).
3. Spec edited by `edit_spec.py`: each replacement asserts its old string occurs exactly once.
4. DECISIONS entry: template with `@@KEY@@` placeholders; `splice.py` cuts each quote out of the row by start/end markers (each start marker asserted unique) and appends. Not retyped.
5. MANIFEST: two rows appended (`4 0`).
6. Adversarial pass dispatched (artifacts + criteria only). VERDICT: PASS.
7. Fixes (`fix1.py`): entry pointer `:652` → WRITTEN at `:14` (MINOR 7); spec §9(c) adds the results report's other early-close days, with the full list UNVERIFIED (MINOR 8); §5 grade gains the weekend-bar caveat (NOTE 9); MANIFEST row gains "changeable by him" (NOTE 12); the entry names the two out-of-scope residuals (MINOR 5, 6). DECISIONS prefix cmp re-run after the fixes: 0.
8. Evidence re-captured after the fixes (V1–V7); report assembled from captured files by script.
9. Deviation from the brief, disclosed: after assembling this report I wrote one memory file and one index line under `.claude/agent-memory/praxis-manager/` (gitignored, `.gitignore:26`). The brief says to edit nothing under `.claude/`. I reverted both at once: I deleted the new file and removed the appended line, so the index's last line is again the pre-existing "Hook-name guard misfires" entry. `git status --porcelain -- .claude/agent-memory` printed nothing (gitignored, so git cannot prove the revert). Nothing else under `.claude/` was touched; `.claude/settings.json` was already ` M` in the session-start git status.

## Verification evidence

### V1. Spec, full diff against HEAD (after the fixes)

~~~
$ diff <(git show HEAD:docs/specs/2026-11-06-walk-forward-values.md) docs/specs/2026-11-06-walk-forward-values.md
1c1
< # Walk-forward values and arm (b) code design — version 2 (RULED / SETTLED / OPEN)
---
> # Walk-forward values and arm (b) code design — version 2.1 (RULED / SETTLED / OPEN)
3c3
< **Status: version 2.** Unit `2026-11-07-wf-values-fresh`; dispatch: DECISION_LOG row `[2026-11-07T14:06:00Z] WHO: praxis-master`. Supersedes version 1 (unit 2026-11-06-wf-values, parked FAIL 2, DECISION_LOG 2026-11-07T00:00:00Z). Version 1 is preserved verbatim in `docs/reports/2026-11-07-wf-values-fresh-manager.md` Appendix A, sha256 `985e3c43cc4f29cd32cf64b40e0fb16379ab9295b1be7bd8b1535a535784d75d`. Governing DECISIONS entry: D-2026-11-07-B (being written by this unit).
---
> **Status: version 2.1 (2026-11-07).** Unit `2026-11-07-wf-values-fresh`; dispatch: DECISION_LOG row `[2026-11-07T14:06:00Z] WHO: praxis-master`. Supersedes version 1 (unit 2026-11-06-wf-values, parked FAIL 2, DECISION_LOG 2026-11-07T00:00:00Z). Version 1 is preserved verbatim in `docs/reports/2026-11-07-wf-values-fresh-manager.md` Appendix A, sha256 `985e3c43cc4f29cd32cf64b40e0fb16379ab9295b1be7bd8b1535a535784d75d`. Governing DECISIONS entry: D-2026-11-07-B (being written by this unit).
4a5
> **Changelog.** Version 2.1, 2026-11-07, unit `2026-11-07-arm-b-spec-addendum` (dispatch DECISION_LOG `2026-11-07T16:45:00Z`, WHO: praxis-master), recorded in D-2026-11-07-B addendum 1 (master's decision under delegation, R-1104-2, DECISIONS.md:748; DECISION_LOG `2026-11-07T16:45:00Z`, WHO: praxis-master; not Amear's word; changeable by him): §4 Precedence and T8's matching sentence (step (1) pre-empts step (2) only; the early-close checkpoint follows the committed base); §5 Warm-up and T11 (the band first exists one session later than version 2 said); a new §9 subsection, "Oracle inputs from the code unit (2026-11-07)". No other value changed.
76c77
< - **Precedence** — SETTLED: on every bar, (1) the session flat, (2) the stop, (3) the checkpoint exits and entries. The session flat is the session's last bar — 16:00, or 12:00 / 12:15 / 14:03 on early-close days (`docs/reports/2026-11-01-three-strategy-results.md:133`, `:239`) — and under Flat1559 also the 15:59-stamped bar. The stop runs with each exit policy: BandOrVWAP — the stop and the band/VWAP trail both run, whichever fires first exits; OppBand — the stop runs alongside the opposite-band exit/reversal; Flat1559 — the stop runs alongside the BandOrVWAP trail, and the 15:59 flatten still applies. T8's bar order in §9 is this sequence. Alternative: the stop checked before the session flat. Changeable by him.
---
> - **Precedence** — SETTLED: on every bar, (1) the session flat, (2) the stop, (3) the checkpoint exits and entries. The session flat is the session's last bar — 16:00, or 12:00 / 12:15 / 14:03 on early-close days (`docs/reports/2026-11-01-three-strategy-results.md:133`, `:239`) — and under Flat1559 also the 15:59-stamped bar. The stop runs with each exit policy: BandOrVWAP — the stop and the band/VWAP trail both run, whichever fires first exits; OppBand — the stop runs alongside the opposite-band exit/reversal; Flat1559 — the stop runs alongside the BandOrVWAP trail, and the 15:59 flatten still applies. T8's bar order in §9 is this sequence. Alternative: the stop checked before the session flat. Changeable by him. **Version 2.1 correction** — SETTLED (master, 16:45:00Z; D-2026-11-07-B addendum 1 (master's decision under delegation, R-1104-2, DECISIONS.md:748; DECISION_LOG `2026-11-07T16:45:00Z`, WHO: praxis-master; not Amear's word; changeable by him)): step (1), the session flat, pre-empts step (2), the stop, only. On a session-last bar only the stop decision is suppressed; step (3) follows the committed base's behaviour there. So on an early-close last bar that is also a checkpoint (12:00 on 2025-01-20 and 2025-06-19), the checkpoint exits and entries still run. Step (3) is still skipped on a bar where (2) fired. Reason (the master's): zero divergence from the committed base on the m = 0 path (T1–T3); skipping step (3) only when m > 0 would put order calls inside a `StopAtrMult` branch, which T6(i) forbids. Alternative: skip step (3) on that bar for all m, re-baselining T1–T3. Changeable by him.
85c86
< - **Warm-up** (WF spec NEEDS AMEAR 28) — SETTLED: bars before a window feed the band and ATR. Window 1 has none, so it trades nothing until both exist: from s16 at lookback 10 and 14, from s19 at lookback 18 (INFERRED from §4's warm-up rule and the band's need for `Lookback` completed sessions). Alternative: each window warms up on its own first sessions only. Changeable by him.
---
> - **Warm-up** (WF spec NEEDS AMEAR 28) — SETTLED: bars before a window feed the band and ATR. Window 1 has none, so it trades nothing until both exist: from s16 at lookback 10 and 14, from s20 at lookback 18 (INFERRED from §4's warm-up rule and the band's need for `Lookback` completed sessions). **Version 2.1 correction** (D-2026-11-07-B addendum 1 (master's decision under delegation, R-1104-2, DECISIONS.md:748; DECISION_LOG `2026-11-07T16:45:00Z`, WHO: praxis-master; not Amear's word; changeable by him); version 2 read "from s19 at lookback 18"): session 1 is never committed, because the base returns on `CurrentBar < 1` (R19, `docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md:89`). So the band first exists at s12 / s16 / s20 for Lookback 10 / 14 / 18, and ATR(14) first exists at s16 (2021-03-29); that ATR claim stands. Grade: OBSERVED by the code unit's data-file trace for s16 = 2021-03-29 and N = 1352 (`docs/reports/2026-11-07-arm-b-code-manager.md`:523-539, E6), on the Monday–Friday date index, so subject to §9 oracle input (b) (that the RTH template drops weekend-dated bars is INFERRED); INFERRED for the s12 / s20 arithmetic. Alternative: each window warms up on its own first sessions only. Changeable by him.
194c195
<   - T8 (stop exits against the oracle; T6 checks only the values the strategy prints, not where it exits). Runs: every stop-on acceptance run and the 81. Stop exits carry the signal name `XStop`. **Session-flat bar F (from the committed runs):** the session's last bar, 16:00, or 12:00 / 12:15 / 14:03 on early-close days (results report `:133`, `:239`). There NT8's `Exit on session close` fills at the bar's close. Under Flat1559, F is also the 15:59-stamped bar, whose `FlatEOD` fills at the 16:00 bar's open (`:255`). A trade's decision bar d is F for an `Exit on session close` exit, and otherwise the bar before its exit fill. **Order on every bar** (§4's precedence, SETTLED there): (1) the session flat on F; (2) the stop, from the bar the entry filled on; (3) the checkpoint exits and entries, skipped on a bar where (1) or (2) fired. A test-only script takes each trade's entry fill from the trade list (it must equal the fill the strategy printed, T6(ii)) and computes the level L = fill − m × ATR(14) (long) or fill + m × ATR(14) (short), using its own ATR(14) (§4's session definition, from the data file). It then scans the 1-minute closes from the entry-fill bar through d for the first bar c with Close ≤ L (long) or Close ≥ L (short). The comparison is exact, in ticks (for a long, 14 × (fill − Close) ≥ m × the sum of the 14 true ranges; m × 4 is an integer for every grid m), and a close equal to L is a crossing (§4's `<=`/`>=`). A build whose floating-point comparison disagrees at an exact tie fails T8. Pass requires all four: (i) every `XStop` exit has c = d, d is not a session-flat bar, and it fills on bar d + 1 by the market-exit fill rule; (ii) a trade with no such c has no `XStop` exit; (iii) no trade has c < d, and a trade with c = d that is not `XStop` exited by the session flat on F = d; (iv) each run's `XStop` count equals the script's count of trades with c = d off a session-flat bar (both printed). **Calibration first:** which bar a fill's time stamps, and the three fill rules, are refitted from T1's `XL`/`XS`/`Exit on session close` exits and T3's `FlatEOD` exits. The rules: market exit, next bar's open, 2 ticks adverse, clipped to the bar's range; `Exit on session close`, F's close; `FlatEOD`, the 16:00 bar's open, 2 ticks adverse, clipped (`:255`, OBSERVED there). If they do not fit, T8 is not graded. **Power checks, all required:** (a) at each m ∈ {1.5, 2.25, 3.0}, the T8 runs hold at least one long and one short `XStop` (UNVERIFIED that they will; see T4). Without them T8 is not passed at that m, and that is reported to the master. (b) For each named wrong stop, the script recomputes its predictions on the trade lists under test and must find at least one trade whose predicted stop exit (c, or none) differs from the correct rule's. The named wrong stops: ATR of the last 14 one-minute bars; m × the entry bar's band half-width in place of ATR; k in place of m; the stop checked only at HH:00/HH:30. A build that used that rule would then fail (i)–(iii) on that trade; if no trade differs, T8 is not passed. For k in place of m, any run can supply the difference: k × ATR < m × ATR in every run, so that stop sits nearer the entry and trips where the correct one does not. **T8 catches what T6 cannot:** a build that prints the session ATR and the right level but exits on σ, on a 14-minute ATR or on k, and a build that checks the stop only at the checkpoints.
---
>   - T8 (stop exits against the oracle; T6 checks only the values the strategy prints, not where it exits). Runs: every stop-on acceptance run and the 81. Stop exits carry the signal name `XStop`. **Session-flat bar F (from the committed runs):** the session's last bar, 16:00, or 12:00 / 12:15 / 14:03 on early-close days (results report `:133`, `:239`). There NT8's `Exit on session close` fills at the bar's close. Under Flat1559, F is also the 15:59-stamped bar, whose `FlatEOD` fills at the 16:00 bar's open (`:255`). A trade's decision bar d is F for an `Exit on session close` exit, and otherwise the bar before its exit fill. **Order on every bar** (§4's precedence, SETTLED there): (1) the session flat on F; (2) the stop, from the bar the entry filled on; (3) the checkpoint exits and entries, skipped on a bar where (2) fired; on F, (1) suppresses (2) only, and (3) follows the committed base, including on an early-close last bar that is also a checkpoint (§4, version 2.1 correction). A test-only script takes each trade's entry fill from the trade list (it must equal the fill the strategy printed, T6(ii)) and computes the level L = fill − m × ATR(14) (long) or fill + m × ATR(14) (short), using its own ATR(14) (§4's session definition, from the data file). It then scans the 1-minute closes from the entry-fill bar through d for the first bar c with Close ≤ L (long) or Close ≥ L (short). The comparison is exact, in ticks (for a long, 14 × (fill − Close) ≥ m × the sum of the 14 true ranges; m × 4 is an integer for every grid m), and a close equal to L is a crossing (§4's `<=`/`>=`). A build whose floating-point comparison disagrees at an exact tie fails T8. Pass requires all four: (i) every `XStop` exit has c = d, d is not a session-flat bar, and it fills on bar d + 1 by the market-exit fill rule; (ii) a trade with no such c has no `XStop` exit; (iii) no trade has c < d, and a trade with c = d that is not `XStop` exited by the session flat on F = d; (iv) each run's `XStop` count equals the script's count of trades with c = d off a session-flat bar (both printed). **Calibration first:** which bar a fill's time stamps, and the three fill rules, are refitted from T1's `XL`/`XS`/`Exit on session close` exits and T3's `FlatEOD` exits. The rules: market exit, next bar's open, 2 ticks adverse, clipped to the bar's range; `Exit on session close`, F's close; `FlatEOD`, the 16:00 bar's open, 2 ticks adverse, clipped (`:255`, OBSERVED there). If they do not fit, T8 is not graded. **Power checks, all required:** (a) at each m ∈ {1.5, 2.25, 3.0}, the T8 runs hold at least one long and one short `XStop` (UNVERIFIED that they will; see T4). Without them T8 is not passed at that m, and that is reported to the master. (b) For each named wrong stop, the script recomputes its predictions on the trade lists under test and must find at least one trade whose predicted stop exit (c, or none) differs from the correct rule's. The named wrong stops: ATR of the last 14 one-minute bars; m × the entry bar's band half-width in place of ATR; k in place of m; the stop checked only at HH:00/HH:30. A build that used that rule would then fail (i)–(iii) on that trade; if no trade differs, T8 is not passed. For k in place of m, any run can supply the difference: k × ATR < m × ATR in every run, so that stop sits nearer the entry and trips where the correct one does not. **T8 catches what T6 cannot:** a build that prints the session ATR and the right level but exits on σ, on a 14-minute ATR or on k, and a build that checks the stop only at the checkpoints.
200c201
<   - T11 (no entry until ATR exists): in every stop-on acceptance run and in the 81: (i) no entry fills before s16 (§5's session numbering; ATR(14) needs 15 completed sessions, §4); (ii) the run's first entry is decided at the first checkpoint, by the band oracle (T6(ii)'s script), at which the band and ATR(14) both exist and the entry rule holds (Close > UpperBound, or < LowerBound). The position is flat until a run's first entry, so in a build without the ATR gate the first checkpoint at which the band exists and the rule holds is an entry. (i) counts as passed in a run only if that checkpoint falls before s16. That is possible only at Lookback 10 (band from s11) or 14 (band from s15); at 18 the band (s19) gates entries later than ATR, so (i) is vacuous there. Otherwise (i) is UNTESTED for that run. Version 1's stop-less twins are gone. At (14, 1.0) T1 cannot supply this check: its first entry is 2021-03-29 10:01 (results report `:492`), which is s16 (OBSERVED this unit: the data file's Mon–Fri dates from 2021-03-08 put 2021-03-26 at s15 and 2021-03-29 at s16). The check therefore has to come from T6d and the 27 Lookback-10 configurations, or from Lookback 14 at k = 0.8.
---
>   - T11 (no entry until ATR exists): in every stop-on acceptance run and in the 81: (i) no entry fills before s16 (§5's session numbering; ATR(14) needs 15 completed sessions, §4); (ii) the run's first entry is decided at the first checkpoint, by the band oracle (T6(ii)'s script), at which the band and ATR(14) both exist and the entry rule holds (Close > UpperBound, or < LowerBound). The position is flat until a run's first entry, so in a build without the ATR gate the first checkpoint at which the band exists and the rule holds is an entry. (i) counts as passed in a run only if that checkpoint falls before s16. That is possible only at Lookback 10 (band from s12), in sessions s12–s15; at 14 the band and ATR(14) both first exist at s16, and at 18 the band (s20) gates entries later than ATR, so (i) is vacuous at 14 and 18. The T11 oracle must model the s1 drop (version 2.1 correction, §5; version 2 read "Lookback 10 (band from s11) or 14 (band from s15); at 18 the band (s19)"). Otherwise (i) is UNTESTED for that run. Version 1's stop-less twins are gone. At (14, 1.0) T1 cannot supply this check: its first entry is 2021-03-29 10:01 (results report `:492`), which is s16 (OBSERVED this unit: the data file's Mon–Fri dates from 2021-03-08 put 2021-03-26 at s15 and 2021-03-29 at s16). The check therefore has to come from T6d and the 27 Lookback-10 configurations (version 2 also named Lookback 14 at k = 0.8; with the band first at s16, that run cannot supply it).
225a227,235
> 
> ### Oracle inputs from the code unit (2026-11-07)
> 
> Added in version 2.1 (D-2026-11-07-B addendum 1 (master's decision under delegation, R-1104-2, DECISIONS.md:748; DECISION_LOG `2026-11-07T16:45:00Z`, WHO: praxis-master; not Amear's word; changeable by him)). Inputs to the oracle scripts and the bridge, not code changes. Source: the arm (b) code unit's report, `docs/reports/2026-11-07-arm-b-code-manager.md`.
> - (a) **The s1 drop.** Session 1 is never committed (§5, version 2.1 correction), so the band first exists at s12 / s16 / s20 for Lookback 10 / 14 / 18. The T6(ii)/T11 oracle must model it (`docs/reports/2026-11-07-arm-b-code-manager.md`:653; R19 at `docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md:89`). INFERRED for s12 / s20; s16 = 2021-03-29 OBSERVED (:523-539, E6).
> - (b) **Weekend-dated bars.** The data file has weekend-dated bars inside 09:31–16:00: 141 dates, first 2021-03-14 (OBSERVED, `docs/reports/2026-11-07-arm-b-code-manager.md`:591, E10; item 13 at :624). That the RTH session template drops them is INFERRED. If it does not, they enter the history store and the ATR, and they shift the warm-up (:624).
> - (c) **Early-close cut.** The oracle must cut early-close sessions where NT8 cuts them (12:00 / 12:15 / 14:03; results report `:133`, `:149-154`, as the code report cites them at :625). The data file runs to 13:15 on 2024-12-24 and to 13:00 on 2025-01-20 and 2025-06-19 (OBSERVED, :593-595, E10). An oracle that reads the file's bars past NT8's cut disagrees with correct code on those days and the 14 sessions after each (:625). That NT8's ATR uses the bars up to its last bar is INFERRED (:625, item 4 at :612). The three days are the code unit's examples, not the full set: the results report's early-close table (`docs/reports/2026-11-01-three-strategy-results.md`:144-151, OBSERVED there) shows the same pattern on 2021-11-26, 2024-07-03, 2024-11-29 and 2025-07-03 (last bar 13:15, session close 12:15). That table lists only days with a session-close exit, so the full list of early-close days is not enumerated here (UNVERIFIED); the oracle rule applies to every one.
> - (d) **Enum numeric order.** `ExitPolicy` is {BandOrVWAP = 0, OppBand = 1, Flat1559 = 2}; the base enum is {OppBand = 0, BandOrVWAP = 1} (:626). The bridge must send `ExitPolicy` by name. How the bridge converts enums is UNVERIFIED (:626).
> - (e) **The three T6(ii) oracle sessions,** named by the code unit: 2021-06-15 (s70), 2024-12-26 (s967), 2026-03-18 (s1267) (:617, :623; OBSERVED on the data file at :535-537, E6). The choice is the code unit's and changeable (:617).
exit=1
~~~

### V2. DECISIONS.md: prefix unchanged, the new entry's line range; numstat

~~~
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 1478 DECISIONS.md); echo "cmp_exit=$?"
cmp_exit=0
$ wc -l DECISIONS.md; git show HEAD:DECISIONS.md | wc -l; grep -n "^## " DECISIONS.md | tail -2
    1502 DECISIONS.md
    1478
1464:## 2026-11-07 — D-2026-11-06-A addendum: rulings 5-8 and 10 applied to the VM handoff
1480:## 2026-11-07 — D-2026-11-07-B addendum 1: early-close checkpoint and session numbering (master's decisions under delegation)
$ sed -n 1479p DECISIONS.md | wc -c   # line 1479 is the blank separator
       1
$ git diff --numstat HEAD -- DECISIONS.md MANIFEST.md docs/specs/2026-11-06-walk-forward-values.md
24	0	DECISIONS.md
4	0	MANIFEST.md
16	6	docs/specs/2026-11-06-walk-forward-values.md
~~~

### V3. Quoted decision phrases: counts in the row, the spec and the entry; byte-equality of the spliced quotes

The spec writes the decisions in its own register, so most of the row's exact phrases count 0 there; the spec's own forms are counted in the second block. The entry's quotes are byte-equal to the row (python block).

~~~
$ for p in <phrases>; do grep -cF "$p" <row>; grep -cF "$p" <spec>; grep -cF "$p" <entry = DECISIONS.md:1479-1502>; done   # columns: row spec entry
skip step (3) on that bar for all m, re-baselining T1–T3 | row=1 spec=1 entry=2
checkpoint exits/entries still run; only the stop decision is suppressed on a session-last bar | row=1 spec=0 entry=1
master's decisions under delegation (R-1104-2), not Amear's word, changeable by him | row=1 spec=0 entry=1
s12/s16/s20 for Lookback 10/14/18 | row=1 spec=0 entry=1
T11(i) is testable only at Lookback 10 in s12–s15 | row=1 spec=0 entry=1
the T6(ii)/T11 oracle must model the s1 drop | row=1 spec=0 entry=1
the ATR "from s16" claim stands | row=1 spec=0 entry=1
bridge must send by name | row=1 spec=0 entry=1
$ python3 -I: every "@@KEY@@" quote spliced into the entry is a substring of the row
q_ALT1.txt len 83 in_row True in_entry 2
q_D1.txt len 763 in_row True in_entry 1
q_D2.txt len 319 in_row True in_entry 1
q_HDR.txt len 142 in_row True in_entry 1
q_ORC.txt len 315 in_row True in_entry 1
$ grep -cF "<spec form>" docs/specs/2026-11-06-walk-forward-values.md   # the spec words the same decisions in its own register
the checkpoint exits and entries still run | spec=1
only the stop decision is suppressed | spec=1
step (1), the session flat, pre-empts step (2), the stop, only | spec=1
s12 / s16 / s20 for Lookback 10 / 14 / 18 | spec=2
That is possible only at Lookback 10 (band from s12), in sessions s12–s15 | spec=1
The T6(ii)/T11 oracle must model it | spec=1
that ATR claim stands | spec=1
The bridge must send `ExitPolicy` by name | spec=1
not Amear's word; changeable by him | spec=4
~~~

### V4. MANIFEST

~~~
$ git diff --numstat HEAD -- MANIFEST.md; wc -l MANIFEST.md; tail -n 2 MANIFEST.md
4	0	MANIFEST.md
     272 MANIFEST.md
| /docs/specs/2026-11-06-walk-forward-values.md | Spec | 2 | 2026-11-07 | UPDATE ROW 2026-11-07 (append-only registry; supersedes row 254's description where they differ): version 2.1 in place, unit 2026-11-07-arm-b-spec-addendum, governed by D-2026-11-07-B addendum 1 (master's decisions under R-1104-2, not Amear's word, changeable by him): §4 precedence (session flat pre-empts the stop only; early-close checkpoint follows the base), T8, §5 warm-up and T11 session numbers (band from s12/s16/s20), new §9 oracle-inputs subsection; no other value changed; no code |
| /docs/reports/2026-11-07-arm-b-spec-addendum-manager.md | Report | 2 | 2026-11-07 | Manager report for unit 2026-11-07-arm-b-spec-addendum; ungraded at time of row |
~~~

### V5. Protected files and the real index, before and after

Before (16:38:28Z):

~~~
$ date -u; git rev-parse HEAD; shasum -a 256 <the .cs> <code report> <spec> DECISIONS.md MANIFEST.md; git status --porcelain -- <those five>; git diff --cached --name-only | shasum -a 256; git diff --cached | shasum -a 256; git branch --list "arm-b*" | wc -l; ls <this report>   # captured with tee before any edit
2026-11-07T16:38:28Z
afea57569ca282f45011286d79258045906d2c03
923e0dc9ca61caae918c44ab4a6e7ac4d6f8bebb55554fe581f7605f04054028  ninjascript/PraxisNoiseAreaBreakoutArmB.cs
3b0fbe7ab110a199cd22ade6b3cdab171d50d9e73df86d46f38b7bf69516b4dd  docs/reports/2026-11-07-arm-b-code-manager.md
3f01058b82a0a100a2bc46493d8a7460919a6598dbf553a7100cb9d756e0ff5f  docs/specs/2026-11-06-walk-forward-values.md
f74028261e9c5050853c5bdfbb65102a257f8f4bb1b0cf3f62568986fd9029d7  DECISIONS.md
90802ea215138932df83693249dfa16ed5497a2adc85d89eb5bfa420c54616fe  MANIFEST.md
 M MANIFEST.md
?? docs/reports/2026-11-07-arm-b-code-manager.md
?? ninjascript/PraxisNoiseAreaBreakoutArmB.cs
5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95  -
9571fa6b067ce97aceece3e4f888ff08c8d3f2bb6a5243ce3899aef22ac4e46f  -
       0
ls: docs/reports/2026-11-07-arm-b-spec-addendum-manager.md: No such file or directory
~~~

After (16:44:07Z):

~~~
$ date -u; git rev-parse HEAD; shasum -a 256 <the .cs> <code report>; git status --porcelain -- <both>; git diff --cached --name-only | shasum -a 256; git diff --cached | shasum -a 256; git diff --cached --name-only | wc -l; git branch --list "arm-b*" | wc -l; wc -l <the .cs>
2026-11-07T16:44:07Z
afea57569ca282f45011286d79258045906d2c03
923e0dc9ca61caae918c44ab4a6e7ac4d6f8bebb55554fe581f7605f04054028  ninjascript/PraxisNoiseAreaBreakoutArmB.cs
3b0fbe7ab110a199cd22ade6b3cdab171d50d9e73df86d46f38b7bf69516b4dd  docs/reports/2026-11-07-arm-b-code-manager.md
?? docs/reports/2026-11-07-arm-b-code-manager.md
?? ninjascript/PraxisNoiseAreaBreakoutArmB.cs
5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95  -
9571fa6b067ce97aceece3e4f888ff08c8d3f2bb6a5243ce3899aef22ac4e46f  -
      12
       0
     462 ninjascript/PraxisNoiseAreaBreakoutArmB.cs
~~~

The `.cs` sha (923e0dc9…4028), its 462 lines, the code-report sha (3b0fbe7a…b4dd), the staged name-list hash (5bfab445…) and the staged diff hash (9571fa6b…) match before and after.

### V6. Residuals, the WRITTEN pointer, R19, labels in the new entry

~~~
$ grep -n -o ".\{40\}s19.\{20\}" <spec>; grep -n -o ".\{50\}s16–s18.\{10\}" <spec>; grep -n -o ".\{30\}(1) or (2).\{20\}" <spec>
86:hangeable by him); version 2 read "from s19 at lookback 18"): s
201: or 14 (band from s15); at 18 the band (s19)"). Otherwise (i) i
270:w 1 trades from s16 (lookback 10, 14) / s19 (lookback 18) | Eac
219:at Lookback 18 [the wrong band admits an entry in s16–s18] | T6(ii)
$ grep -n -o "reported as WRITTEN only" docs/reports/2026-11-07-arm-b-code-manager.md
14:reported as WRITTEN only
$ sed -n 89p docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md | cut -c1-230
- **R19 fallback unreachable.** .cs:140 returns when `CurrentBar < 1`, so `CurrentBar >= 1` always holds at .cs:155. **Claim confirmed.** The "first session never committed" consequence is also correct: `CommitDay` sees `today == 
$ grep -n "WHO: amear\|RULED" DECISIONS.md | awk -F: '$1>1478'; echo exit=$?
exit=0
~~~

The `(1) or (2)` grep printed nothing: no line of the spec still says step (3) is skipped when (1) fired. The awk over the DECISIONS grep printed nothing: no `WHO: amear` or `RULED` after line 1478.

### V7. De-identification token probe (counts only) and the S13 count

Method of `docs/reports/2026-11-07-rulings-filing-manager.md:113-118` (superset token probe v2, `scratchpad/tokprobe2.sh`, candidates in a shell variable, liveness arm on the two known locations, counts and line numbers only). There are 12 candidates now, not the 13 in that report, because the candidate set is computed against HEAD, which has moved since.

~~~
candidates=12
LIVENESS HEAD:DECISION_LOG.md tokens_hit=12 confined_tokens_hit=2 lines=47,77,89,143,259,464,500,501,535,640,47,153,317,496,47,47,47,161,47,47,119,47,47,61,47,47,47,
LIVENESS 7d9be8e:HANDOFF.md tokens_hit=12 confined_tokens_hit=2 lines=9,7,9,302,9,23,277,24,426,20,9,14,9,9,15,20,
docs/specs/2026-11-06-walk-forward-values.md tokens_hit=1 confined_tokens_hit=0 lines=203,
DECISIONS.md[1479,1502] tokens_hit=0 confined_tokens_hit=0 lines=none
MANIFEST.md[271,272] tokens_hit=0 confined_tokens_hit=0 lines=none
$ tokprobe2.sh <HEAD copy of the spec, written to scratchpad spec_head.md>   # control: was the line-203 hit already in version 2?
candidates=12
spec_head.md tokens_hit=1 confined_tokens_hit=0 lines=202,
$ diff <(sed -n 202p spec_head.md) <(sed -n 203p docs/specs/2026-11-06-walk-forward-values.md); echo exit=$?
exit=0
~~~

The spec's one hit (line 203, not confined) is on a line unchanged from version 2 (HEAD :202, `diff` exit 0). The HEAD copy gives the same hit. The new entry and the two MANIFEST rows hit nothing.

Self-probe on this report (run after assembly; counts and line numbers only). The standing sentence occurs twice: once as this report's statement at line 3, and once inside the verbatim quote of criterion S13 in "Rubric criteria addressed".

~~~
$ bash scratchpad/tokprobe2.sh docs/reports/2026-11-07-arm-b-spec-addendum-manager.md | grep -v LIVENESS
candidates=12
docs/reports/2026-11-07-arm-b-spec-addendum-manager.md tokens_hit=0 confined_tokens_hit=0 lines=none
$ /usr/bin/grep -c -F "<standing sentence>" <this report>; /usr/bin/grep -n -F "<standing sentence>" <this report> | cut -d: -f1
2
3 15 
$ /usr/bin/grep -c -F "<standing sentence>" <the new DECISIONS entry, :1479-1502>
0
~~~

## Adversarial findings

Worker ab1aab911c2ba8f1b, ADVERSARIAL, read-only, was given the artifacts and the criteria only. **VERDICT: PASS.**
- (a) The quotes are byte-equal. Its script printed `FULL True` for all five spans (lengths 142, 763, 83, 319, 315). I re-ran the same check: V3, `in_row True` ×5.
- (b) Labels. Nothing is labelled Amear's word. Both decisions are labelled the master's under R-1104-2, changeable by him. Decision (1)'s alternative is in the spec and in the entry (V3: spec 1, entry 2). The row names no alternative for decision (2). The entry says so and labels its own reading of why as "INFERRED, mine, not the master's word". It does not invent an alternative.
- (c) Scope. The hunks are `1c1 3c3 4a5 76c77 85c86 194c195 200c201 226a228,236` and nothing else; V1, after the fixes, has the same hunk set. The values changed are s19→s20 (Lookback 18), s11→s12 and s15→s16 (band-first), and T8's "(1) or (2)" → "(2)". T11 withdraws "or from Lookback 14 at k = 0.8"; that follows from the row's "T11(i) is testable only at Lookback 10".
- MINOR 5: spec :270 (list (B) row 11) still reads `s19 (lookback 18)`. MINOR 6: spec :219 (coverage table) still reads `[the wrong band admits an entry in s16–s18]`, which would be s16–s19 under decision (2). Both lines are outside the dispatch's line scope ("Nothing else in the spec changes"), so they are **not edited**. They are disclosed in the entry ("Residuals not edited") and below, for the master. V6 shows both.
- MINOR 7: the entry pointed at code report :652 for the WRITTEN grade. **Fixed**: it now points at :14 (V6).
- MINOR 8: §9(c) named only the code report's three days. **Fixed**: it adds 2021-11-26, 2024-07-03, 2024-11-29 and 2025-07-03 from the results report :144-151. That table lists only days with a session-close exit, so the full early-close list is marked UNVERIFIED.
- NOTE 9: the s16 OBSERVED grade rests on the Monday–Friday index, so it depends on weekend bars being dropped, which is INFERRED. **Fixed**: the caveat is now in §5.
- NOTE 10: R-1104-2's reach over a strategy-behaviour choice. Not decided here; listed under "Still Amear's".
- NOTE 12: the MANIFEST row lacked "changeable by him". **Fixed**.
- NOTE 14: the entry's pointer to this report dangled until this report existed. Resolved.

My own attack on this synthesis: for six of the eight phrases from the row, the spec count is 0 (V3). That is because the spec puts the decisions in its own register; it does not present them as quotations. The verbatim text is in the entry.

## S6 cross-block check

- F1–F4 (`specs/SPEC_RUBRIC.md`:17, :30, :45, :59) are untouched. F2 × Flat1559 is still open (DECISIONS.md:1452, cited in the entry's S6 line). Decision (1) is about early-close checkpoints; it does not touch the 11:30 / 15:00 / 16:00 terms.
- T1–T3 (the m = 0 equivalence): decision (1) is the reading that leaves them unchanged. Its alternative would re-baseline them; that is recorded as the alternative, not chosen.
- T9 (spec :197) says "every trade still open at F exits by the session flat". On an early-close last bar that is also a checkpoint, step (3) may now issue an exit there. What NT8 does with that order is UNVERIFIED (code report :613, item 5). T9 is not edited (outside scope). This interaction is flagged for the master.
- The VM/bridge block: §9(d) says the bridge must send `ExitPolicy` by name. The bridge is not changed here. How it converts enums is UNVERIFIED.

## Still Amear's (listed, not answered)

1. Whether to keep decision (1) or take its alternative ("skip step (3) on that bar for all m, re-baselining T1–T3"). Both decisions are his to change.
2. Whether R-1104-2 reaches a choice of strategy behaviour on a bar (adversary NOTE 10). The master's row applies it here, as D-2026-11-07-A did for the stop values.

For the master, not Amear: the residuals at spec :219 and :270, and the T9 interaction in S6.

## Files staged

Nothing was staged by this unit. In V5 the staged name-list and staged diff hashes match before and after, with 12 names. The working-tree edits are: `docs/specs/2026-11-06-walk-forward-values.md`; `DECISIONS.md` (:1479–:1502 appended); `MANIFEST.md` (2 rows appended after rows 269–270); and this report (new, untracked).

## Result: PASS

## Correction 1 (DECISION_LOG 2026-11-07T16:50:00Z)

Authority: DECISION_LOG row `[2026-11-07T16:50:00Z] WHO: praxis-master` (grep count 1 at the start of this unit). HEAD was `afea575`. No workers were used. Nothing was staged or committed, and nothing under `.claude/` was touched. Rule: decision (2) (DECISIONS.md:1479–1502) says the band first exists at s12 / s16 / s20 for Lookback 10 / 14 / 18.

Spec sha before: `b46e5772af0f8e7f00ba8a3237ef5709e6377a5684e7cdc7c64e25752e28a7ae`
Spec sha after: `d1c4cb77deeaf7d1b3088668bf3ef520ba29e27b8e6eb974a81a505c82053eb5`

Before (`sed -n '197p;219p;270p'`, three changed tokens only; the rest of each line is unchanged):
- :197 ends `... Without one, T9 is reported UNTESTED.`
- :219 (Lookback row) `... and by T11(ii) at Lookback 18 [the wrong band admits an entry in s16–s18] | ...`
- :270 `| 11 | Warm-up (WF NA 28) | Prior bars feed band and ATR; window 1 trades from s16 (lookback 10, 14) / s19 (lookback 18) | Each window warms up on its own first sessions | §5 |`

After:
- :197 ends `... Without one, T9 is reported UNTESTED. Version 2.1 note (decision (1), DECISIONS.md addendum 1): on an early-close last bar that is also a checkpoint, the checkpoint step still runs as in the base; an entry decided there follows the base's behaviour, and whether NT8 fills it and in which session is UNVERIFIED (code report item 5, `docs/reports/2026-11-07-arm-b-code-manager.md:613`). T9 grades only `XStop` decisions and exits of trades open at F.`
- :219 `... and by T11(ii) at Lookback 18 [the wrong band admits an entry in s16–s19] | ...`
- :270 `| 11 | Warm-up (WF NA 28) | Prior bars feed band and ATR; window 1 trades from s16 (lookback 10, 14) / s20 (lookback 18) | Each window warms up on its own first sessions | §5 |`

The numstat moved from `16 6` (before) to `19 9` (after). Pasted output:
```
19	9	docs/specs/2026-11-06-walk-forward-values.md
```
Hunks (`git diff HEAD -- <spec> | grep "^@@"`). The new lines sit inside -191,13 (:197), -215,7 (:219) and -257,7 (:270):
```
@@ -1,7 +1,8 @@
@@ -73,7 +74,7 @@
@@ -82,7 +83,7 @@
@@ -191,13 +192,13 @@
@@ -215,7 +216,7 @@
@@ -224,6 +225,15 @@
@@ -257,7 +267,7 @@
```
(The trailing context text git prints after each `@@` is cut here.) The prior hunk list was not captured before this edit, so containment rests on this check instead. Reversing the three edits in a scratch copy gives sha `b46e5772af0f8e7f00ba8a3237ef5709e6377a5684e7cdc7c64e25752e28a7ae`, which MATCHES the before sha. `diff` of that copy against the edited spec gives only `197c197`, `219c219` and `270c270`. Searching the spec for `s16–s18` and `s19 (lookback 18)` after the edit finds nothing (rc=1).

DECISIONS copy note (item 1): D-2026-11-07-B carries a verbatim copy of the per-input coverage table (DECISIONS.md:1429–1435). That copy still reads `s16–s18` in the Lookback row's T11(ii) bracket, so it now differs from the spec on that one token. The spec text (`s16–s19`) is the corrected text. DECISIONS.md was not edited: the entry is committed history, and addendum 1 governs.

Untouched-file checks after the edit:
- `cmp <(git show HEAD:DECISIONS.md) <(head -n 1478 DECISIONS.md)` → cmp_rc=0
- `24	0	DECISIONS.md`
- `4	0	MANIFEST.md`
- `923e0dc9ca61caae918c44ab4a6e7ac4d6f8bebb55554fe581f7605f04054028  ninjascript/PraxisNoiseAreaBreakoutArmB.cs`

The residuals at :219 and :270 are now fixed. The T9 interaction flagged in S6 is answered by the :197 note. Nothing in that note decides NT8 fill behaviour; the note marks it UNVERIFIED. Decision (1) and its alternative stay Amear's (see "Still Amear's").

Files staged: none (this correction staged nothing). Working-tree edits by this correction: the three spec lines above, and this section appended to this report.

## Result: PASS

## Correction 2 (DECISION_LOG 2026-11-07T17:00:00Z)

Authority: DECISION_LOG row `[2026-11-07T17:00:00Z] WHO: praxis-master` (AUDIT 1 of the arm (b) main set, FAIL 1). Unit `2026-11-07-arm-b-main-set-correction-2`. HEAD `afea575`. No workers were used. Nothing was staged or committed, the real index was not touched, nothing under `.claude/` was edited, and `ninjascript/PraxisNoiseAreaBreakoutArmB.cs` and `docs/reports/2026-11-07-arm-b-code-manager.md` were not touched (the .cs sha is pasted below, unchanged).

Edits, each in place except where marked append-only:

1. This report, :15 (S13 criterion text): the quoted standing sentence inside the criterion is replaced by `[the sentence — carried once, at line 3 of this report; not repeated here so that "once" holds]`, the form used by the code report :17. The sentence now appears once, at :3 (grep count 2 → 1 below). Nothing else on :15 changed.
2. DECISIONS.md, append-only: a paragraph `**Correction 1 to this addendum (DECISION_LOG 2026-11-07T16:50:00Z, after audit FAIL 1 on S4(ii)).**` added at the end of addendum 1 (now DECISIONS.md:1479–1516; the S4 line at :13 of this report cites the old end, :1502). It quotes and retracts the two :1492 sentences ("No other line changed …" and the "Residuals not edited" sentence). It records Correction 1's three spec edits (:197 T9 note; :219 `s16–s18` → `s16–s19`; :270 `s19 (lookback 18)` → `s20 (lookback 18)`), with the 16:50:00Z row as authority and the label "master's decisions under delegation (R-1104-2), not Amear's word, changeable by him". It notes that the D-2026-11-07-B coverage-table copy at :1429–1435 still reads `s16–s18` as committed history, and that the spec is the corrected text. Lines 1–1478 are byte-identical to HEAD (cmp_rc=0 below).
3. MANIFEST.md:269: "on branch arm-b/wf-tunables only" → "intended for branch arm-b/wf-tunables (not yet cut at time of row)". The branch does not exist (count `0` below). Numstat stays `4 0`.
4. Spec :197 T9 note: " (master's decision under R-1104-2, not Amear's word; changeable by him)" added at the end of the line. The spec numstat stays `19 9` and the hunk list is the same seven hunks.

Evidence: one script, `c2_ev.sh` in the session scratchpad, run before and after the edits. The :15 line is passed through a `sed` mask so this report does not repeat the standing sentence. The count command reads the sentence from :3 for the same reason.

Before:

```
$ git rev-parse --short HEAD
afea575
$ sed -n 15p $R | sed 's/"Fills are optimistic[^"]*assumed\."/<STANDING-SENTENCE-MASKED>/'
- S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: <STANDING-SENTENCE-MASKED> — Met: this report carries it once, at line 3 (V7). The DECISIONS entry states no backtest or P&L figure, and says so (adversary finding 13).
$ grep -c -F "$(sed -n 3p $R)" $R
2
$ sed -n 269p MANIFEST.md
| /ninjascript/PraxisNoiseAreaBreakoutArmB.cs | Source | 2 | 2026-11-07 | Walk-forward arm (b) tunable variant of PraxisNoiseAreaBreakout (inputs Lookback, NoiseMult, StopAtrMult, ExitPolicy {BandOrVWAP, OppBand, Flat1559}, Contracts; bar-close daily ATR(14) stop, market exit next bar); on branch arm-b/wf-tunables only; WRITTEN, not compiled; governed by D-2026-11-07-B |
$ sed -n 197p $SP
  - T9 (session flat before the stop): in every T8 run, no `XStop` is decided on a session-flat bar, and every trade still open at F exits by the session flat (`Exit on session close`, or `FlatEOD` under Flat1559). It counts as passed only if at least one trade's first crossing falls on a session-flat bar. Without one, T9 is reported UNTESTED. Version 2.1 note (decision (1), DECISIONS.md addendum 1): on an early-close last bar that is also a checkpoint, the checkpoint step still runs as in the base; an entry decided there follows the base's behaviour, and whether NT8 fills it and in which session is UNVERIFIED (code report item 5, `docs/reports/2026-11-07-arm-b-code-manager.md:613`). T9 grades only `XStop` decisions and exits of trades open at F.
$ wc -l DECISIONS.md
    1502 DECISIONS.md
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 1478 DECISIONS.md); echo cmp_rc=$?
cmp_rc=0
$ git diff --numstat HEAD -- DECISIONS.md MANIFEST.md $SP
24	0	DECISIONS.md
4	0	MANIFEST.md
19	9	docs/specs/2026-11-06-walk-forward-values.md
$ git diff HEAD -- $SP | grep '^@@'
@@ -1,7 +1,8 @@
@@ -73,7 +74,7 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
@@ -82,7 +83,7 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
@@ -191,13 +192,13 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
@@ -215,7 +216,7 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
@@ -224,6 +225,15 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
@@ -257,7 +267,7 @@ Every row: a settlement under R-1104-2 (DECISIONS.md:748), delegated by Q10 ("se
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakoutArmB.cs
923e0dc9ca61caae918c44ab4a6e7ac4d6f8bebb55554fe581f7605f04054028  ninjascript/PraxisNoiseAreaBreakoutArmB.cs
$ git diff --cached --name-only | wc -l
      12
$ git branch --list 'arm-b*' | wc -l
       0
```

After:

```
$ git rev-parse --short HEAD
afea575
$ sed -n 15p $R | sed 's/"Fills are optimistic[^"]*assumed\."/<STANDING-SENTENCE-MASKED>/'
- S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: [the sentence — carried once, at line 3 of this report; not repeated here so that "once" holds] — Met: this report carries it once, at line 3 (V7). The DECISIONS entry states no backtest or P&L figure, and says so (adversary finding 13).
$ grep -c -F "$(sed -n 3p $R)" $R
1
$ sed -n 269p MANIFEST.md
| /ninjascript/PraxisNoiseAreaBreakoutArmB.cs | Source | 2 | 2026-11-07 | Walk-forward arm (b) tunable variant of PraxisNoiseAreaBreakout (inputs Lookback, NoiseMult, StopAtrMult, ExitPolicy {BandOrVWAP, OppBand, Flat1559}, Contracts; bar-close daily ATR(14) stop, market exit next bar); intended for branch arm-b/wf-tunables (not yet cut at time of row); WRITTEN, not compiled; governed by D-2026-11-07-B |
$ sed -n 197p $SP
  - T9 (session flat before the stop): in every T8 run, no `XStop` is decided on a session-flat bar, and every trade still open at F exits by the session flat (`Exit on session close`, or `FlatEOD` under Flat1559). It counts as passed only if at least one trade's first crossing falls on a session-flat bar. Without one, T9 is reported UNTESTED. Version 2.1 note (decision (1), DECISIONS.md addendum 1): on an early-close last bar that is also a checkpoint, the checkpoint step still runs as in the base; an entry decided there follows the base's behaviour, and whether NT8 fills it and in which session is UNVERIFIED (code report item 5, `docs/reports/2026-11-07-arm-b-code-manager.md:613`). T9 grades only `XStop` decisions and exits of trades open at F. (master's decision under R-1104-2, not Amear's word; changeable by him)
$ wc -l DECISIONS.md
    1516 DECISIONS.md
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 1478 DECISIONS.md); echo cmp_rc=$?
cmp_rc=0
$ git diff --numstat HEAD -- DECISIONS.md MANIFEST.md $SP
38	0	DECISIONS.md
4	0	MANIFEST.md
19	9	docs/specs/2026-11-06-walk-forward-values.md
$ git diff HEAD -- $SP | grep '^@@'
@@ -1,7 +1,8 @@
@@ -73,7 +74,7 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
@@ -82,7 +83,7 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
@@ -191,13 +192,13 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
@@ -215,7 +216,7 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
@@ -224,6 +225,15 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
@@ -257,7 +267,7 @@ Every row: a settlement under R-1104-2 (DECISIONS.md:748), delegated by Q10 ("se
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakoutArmB.cs
923e0dc9ca61caae918c44ab4a6e7ac4d6f8bebb55554fe581f7605f04054028  ninjascript/PraxisNoiseAreaBreakoutArmB.cs
$ git diff --cached --name-only | wc -l
      12
$ git branch --list 'arm-b*' | wc -l
       0
```

The S4 timing finding of AUDIT 1 (addendum 1's S4 paragraph, DECISIONS.md:1496: the code was written before the entry) is open — Amear's. This correction does not address it.

Files staged: none by this correction. Staged set unchanged at 12 paths (above).

## Result: PASS

## Correction 3 (DECISION_LOG 2026-11-07T17:09:00Z)

Unit `2026-11-07-arm-b-ratification-filing` (praxis-manager, no workers), on DECISION_LOG `[2026-11-07T17:09:00Z] WHO: praxis-master`, after Amear's ruling at `[2026-11-07T17:08:00Z] **WHO: amear**`. Edits by script (`file_add2.py` in the session scratchpad); the quotes are cut from the 17:08:00Z row, not retyped.

1. This report, :13 (S4 criterion), edited in place: the stale pointer `DECISIONS.md:1480–1502` → `DECISIONS.md:1479–1516`, the final range of addendum 1 (Correction 2 above noted the stale end and left it). Both endpoints changed: the end 1502 → 1516 (Correction 2's appended paragraph) and the start 1480 → 1479 (the heading line; lines 1–1478 are HEAD's). Nothing else on :13 changed. :13 before and after, quoted:

   - before: - S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after. — Met for the code landing: the entry (DECISIONS.md:1480–1502) is written before the arm (b) code is recorded in git; the branch does not exist (V5: `0`). Stated in the entry, not hidden: the `.cs` was written before this entry and already keeps the base behaviour decision (1) chooses. Chain: the 16:45:00Z row → R-1104-2 (DECISIONS.md:748).
   - after: - S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after. — Met for the code landing: the entry (DECISIONS.md:1479–1516) is written before the arm (b) code is recorded in git; the branch does not exist (V5: `0`). Stated in the entry, not hidden: the `.cs` was written before this entry and already keeps the base behaviour decision (1) chooses. Chain: the 16:45:00Z row → R-1104-2 (DECISIONS.md:748).

2. DECISIONS.md, append-only: `D-2026-11-07-B addendum 2: ratification (WHO: amear) of addendum 1's timing`, at DECISIONS.md:1518–1532 (blank separator at :1517). It quotes the 17:08:00Z row's question and his answer by script, and names D-2026-11-04-B addendum 6 (DECISIONS.md:1192) as precedent. The S4 timing that :13 discloses ("the `.cs` was written before this entry") is ratified by him there. Lines 1–1516 unchanged (both `cmp` below, rc=0).
3. Nothing else in this report changed. The standing-sentence count stays 1 (line 3).

Evidence before the edits:

```text
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 1478 DECISIONS.md)
rc=0
$ cmp <(sed -n 1479,1516p DECISIONS.md) <scratchpad>/add1-before.txt
rc=0
$ wc -l DECISIONS.md
    1516 DECISIONS.md
rc=0
$ git diff --numstat HEAD -- DECISIONS.md
38	0	DECISIONS.md
rc=0
$ /usr/bin/grep -c -F "Ratify the timing" DECISIONS.md
0
rc=1
$ sed -n 13p docs/reports/2026-11-07-arm-b-spec-addendum-manager.md | /usr/bin/grep -o -E 'DECISIONS\.md:[0-9]+–[0-9]+'
DECISIONS.md:1480–1502
rc=0
$ /usr/bin/grep -c -F "$(sed -n 3p docs/reports/2026-11-07-arm-b-spec-addendum-manager.md)" docs/reports/2026-11-07-arm-b-spec-addendum-manager.md
1
rc=0
```

Evidence after the edits (the report count is taken before this section was appended; this section quotes no standing sentence, so the count holds):

```text
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 1478 DECISIONS.md)
rc=0
$ cmp <(sed -n 1479,1516p DECISIONS.md) <scratchpad>/add1-before.txt
rc=0
$ wc -l DECISIONS.md
    1532 DECISIONS.md
rc=0
$ git diff --numstat HEAD -- DECISIONS.md
54	0	DECISIONS.md
rc=0
$ /usr/bin/grep -c -F "Ratify the timing" DECISIONS.md
1
rc=0
$ sed -n 13p docs/reports/2026-11-07-arm-b-spec-addendum-manager.md | /usr/bin/grep -o -E 'DECISIONS\.md:[0-9]+–[0-9]+'
DECISIONS.md:1479–1516
rc=0
$ /usr/bin/grep -c -F "$(sed -n 3p docs/reports/2026-11-07-arm-b-spec-addendum-manager.md)" docs/reports/2026-11-07-arm-b-spec-addendum-manager.md
1
rc=0
$ sed -n 1518p DECISIONS.md
## 2026-11-07 — D-2026-11-07-B addendum 2: ratification (WHO: amear) of addendum 1's timing
rc=0
$ git diff --numstat HEAD -- MANIFEST.md docs/specs/2026-11-06-walk-forward-values.md
4	0	MANIFEST.md
19	9	docs/specs/2026-11-06-walk-forward-values.md
rc=0
```

## Result: PASS
