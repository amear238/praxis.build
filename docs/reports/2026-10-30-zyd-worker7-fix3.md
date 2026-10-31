# Praxis_build-zyd — fix pass 3 (worker7)

## Task
Make fixes H1–H6 from the manager's brief. Allowed edits: the final entry of `DECISIONS.md` (`## 2026-10-30 — D-2026-10-30-A` to EOF), `config/backtest-cost-model.json` (`cost_model.fill_resolution_note` only), and `MANIFEST.md` lines 133+.

## Mode
BUILD (fix pass 3). Nothing is staged and nothing is committed, per the brief ("No git add/commit").

## Criterion
The manager's H1–H6 replacement strings, applied exactly. Verification commands 1–6 from the brief.

## Process log
1. Read the entry (DECISIONS.md:247–294), the end of MANIFEST, and `fill_resolution_note`.
2. Wrote one script, `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/w7f/apply.py`. It splits DECISIONS.md at line 246 and MANIFEST.md at line 132, and edits only the tail of each. It asserts that each old string appears exactly once in the region it edits. In the config it asserts the old note substring appears once in the whole file. Output: `APPLIED`, with no assertion failures.
3. Ran verification commands 1–6.

## Fixes
- **H1:** done. (c) label changed. "whether or when an entry or exit order is sent" sentence replaced. The "Contrary hypothesis on record…" sentence is inserted right after "Its disposition is Amear's." The ` — fill resolution may bear on this (3gm `:784`, INFERRED)` suffix is appended to the FlatEOD bullet (before `;`) and to the same-bar exit+reverse bullet (before `.`). Config note substring replaced.
- **H2:** NEEDS AMEAR item 6 added after item 5.
- **H3:** both void-clause replacements made.
- **H4:** Status line replaced.
- **H5:** "Added key `amended: 2026-10-30`…" bullet inserted as the second Scope bullet.
- **H6:** worker2 and worker4 row parentheticals replaced. worker6 and worker7 rows inserted immediately before the `zyd-f3-artifact.md` row.

## Verification evidence
```
== V1
a0c8fbeea8dcafd72f7385c2b1c50594a6cf7349c8bd49032531cb4491d5234a  -
a0c8fbeea8dcafd72f7385c2b1c50594a6cf7349c8bd49032531cb4491d5234a  -
     243            (git show HEAD:DECISIONS.md | wc -l)
ccb7c2898b679e4abb78e20fceb166b9cd58ee6d32db387e6efe2e3422a06abf  -
ccb7c2898b679e4abb78e20fceb166b9cd58ee6d32db387e6efe2e3422a06abf  -
0
== V2
PARSE_OK
== V3
where it may still bias the backtest => 1
whether or when an entry or exit order is sent => 1
Contrary hypothesis on record => 1
3gm `:784`, INFERRED) => 2
6. Scope of the => 1
in its REPORTED BY AMEAR block => 1
the commit is Amear => 1
Added key => 1
the master's reading => 0
committed per Amear => 0
does not decide this strategy => 0
== V4
True f9144cb50aab2885 f9144cb50aab2885
== V5
0
```
Config: the new note sentence is present once (`grep -o -F … | wc -l` → 1), and `does not decide entries/exits` → 0.

V6, the (c) bullet and its sub-bullets after editing:
```
- **(c) Why the fill-resolution choice does not decide which orders this strategy sends, and where it may still bias the backtest:** … so Standard's intrabar High-vs-Low ordering assumption would not decide whether or when an entry or exit order is sent. That NT8 realises these calls as market orders — and therefore that the Analyzer never needs the intrabar path — is INFERRED. A falsifier for this argument was proposed and is open, not run: the R3 Standard-vs-High control (DECISION_LOG 2026-08-29T00:40:00Z; a High run would also bear on the void clause). Its disposition is Amear's. Contrary hypothesis on record, not resolved: 3gm D4 hypothesis 5 (`:784`, INFERRED) holds that Order fill resolution High vs Standard could change how same-bar exit+reverse pairs and the 16:00 orders resolve. So the fill-resolution choice may still bias how NT8 fills those two cases; the R3 control (NEEDS AMEAR 5) is what would settle it. This is NOT a claim that the backtest is unbiased overall. …
  - stamp-to-next-open slippage (not touch adverse selection; `2026-08-29T00:35:00Z`);
  - the 16:00 FlatEOD fill path, whose "next bar" may be the next day's 09:31 (CANNOT-DETERMINE-STATICALLY, INFERRED; 3gm D2(c)) — fill resolution may bear on this (3gm `:784`, INFERRED);
  - same-bar exit+reverse resolution; early-close days (both CANNOT-DETERMINE-STATICALLY, INFERRED) — fill resolution may bear on this (3gm `:784`, INFERRED).
```
(The middle of the (c) bullet is unchanged and shortened here with "…". The full text is in the handback.)

NEEDS AMEAR item 6:
```
6. Scope of the `[N]` lock (3gm `:949`, reserved for Amear): row `2026-10-30T21:36:30Z` sets `[N]` as band-edge slippage and states it per round trip ($22.96); the Analyzer's Slippage setting applies to every market fill (INFERRED). Was the lock meant to cover session-close and stop-out exits as well?
```
`tail -n 18 MANIFEST.md | cut -c1-150` (last 5 lines):
```
| /docs/reports/2026-10-30-zyd-worker5-fix2.md | Report | 2 | 2026-10-30 | Praxis_build-zyd fix-pass-2 sub-report (worker5). NOT authoritative; sub-re
| /docs/reports/2026-10-30-zyd-worker6-final-adversarial.md | Report | 2 | 2026-10-30 | Praxis_build-zyd ADVERSARIAL re-attack sub-report (worker6; BR
| /docs/reports/2026-10-30-zyd-worker7-fix3.md | Report | 2 | 2026-10-30 | Praxis_build-zyd fix-pass-3 sub-report (worker7). NOT authoritative; sub-re
| /docs/reports/2026-10-30-zyd-f3-artifact.md | Report | 2 | 2026-10-30 | Manager report for Praxis_build-zyd (F3 artifact); ungraded at time of row |
| /config/backtest-cost-model.json | Config | 2 | 2026-07-15 | UPDATE ROW 2026-10-30 (append-only registry; supersedes the earlier row's numbers): v1.
```

## Deviations
None. Things I noticed but did not fix (out of scope):
- (a) The count of `3gm `:784`, INFERRED)` is 2, not 3. `grep -c` counts lines: the two residual-risk bullets match, and the contrary-hypothesis sentence is written as "(`:784`, INFERRED)", without "3gm " inside the parentheses.
- (b) After H3, the void-clause paragraph says "not triggered and not retired" twice: once in the existing Status sentence and once in the new 21:36:30Z sentence. It also attaches "(REPORTED: no run has set High…)" to "the VM measurement, which has not been run", which pairs a VM-measurement claim with a High-run fact.
- (c) The only Bash-run `git diff` covering the config lists 25 changed lines in total. Most of that diff predates this pass. My change to the config is the single substring swap, which the script checked for uniqueness.

## Files staged
None, because the brief says no git add.

## Result: PASS
