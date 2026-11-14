Filed by praxis-manager (unit 2026-11-14-pivot-rulings-filing): worker 2 returned this report inline, because worker writes under docs/reports are refused by a hook. The body below is as returned. The manager left out the trailing return notes (file paths and the agent-memory note) and a spoken-summary block. Worker 2 graded the entry BEFORE the manager's cures; the cures are in the manager report.

## Report: 2026-11-14-pivot-rulings-filing, worker 2

**Mode:** ADVERSARIAL, read-only. HEAD 244cfc3, temp index `/tmp/praxis-pv/idx`. I checked the time with `date -u` at 15:20:57Z and 15:22:17Z.

**Attack 1: byte-identity.** I pulled out the 10 ```text blocks with awk and compared each with `cmp` against `sed -n` of the cited source lines.
```
f1 notes 10,11 IDENTICAL | f2 notes 15 IDENTICAL | f3 notes 19,21;23 IDENTICAL | f4 notes 27;29 IDENTICAL
f5 notes 33 IDENTICAL | f6 brief 34,35 IDENTICAL | f7 notes 37,39 IDENTICAL | f8 notes 43 IDENTICAL
f9 notes 47,48 IDENTICAL | f10 notes 64,69 IDENTICAL
--- negative controls: f3 vs notes 19,23 DIFFER ; f6 vs brief 33,34 DIFFER
```
Inline quotes: all 12 are FOUND at their cited lines (notes :11 :15 :18 :22 :24 :60; DL row 971; DECISIONS :1587 :2482; WF spec :31; Phase 3 :54). Negative control `KEEP: #2 daily loss limit` at :1587 gave NOT-FOUND. The SPEC_RUBRIC F4 quote: `joined-with-one-space count: 1`, `single-line count: 0`. That matches the entry's "two lines joined with one space".

**Attack 2: citations at HEAD.** Every cite says what the entry claims:
- :1583-:1589 is D-2026-11-08-A R8, and :1587 is "KEEP: #1 daily loss limit".
- :1735-:1740 is A4 (80%, MFFU). :2433 is Ruling 3 (loop). :2482 is bar item 3.
- D-2026-11-13-E: item 2 asks for "$4.68 commission", and the commission rule says "MFFU charges $4.68 round trip". True.
- D-2026-11-13-D "UNCLEAR, 36 beads ... 20 agent-harness and guard beads". True.
- WF spec :67 "Arm (a) therefore runs with no added stop. — INFERRED". True. :31 "Revisit if a personal account is used." and :32 MFFU per-window. True.
- Values :51 "m × ATR(14)" and :73 "entry fill price − m × ATR(14)". True.
- Phase 3 :54 (Block 1) "stop-loss + take-profit". :97 and :98 are breakers #1 and #2. :140 "C — Full |Risk-model sizing (0.5% per trade)". True.
- Topology :58 and :59 are breakers #1 and #2. Brief :14 and :35 match. DL HEAD is 949 lines, and the rows are at working-copy :971-:974. True.

**Attack 3: blob against HEAD.**
```
2525 / 2614 ; first 2525 lines == HEAD: IDENTICAL ; line 2526: []
blob ckh heading count: 0 ; HEAD: 0 ; worktree (positive control): 2280:## 2026-11-12 — D-2026-11-12-B: R6 step 2 ...
worktree numstat 181 0 (= 92 ckh + 89 entry) ; HEAD D-2026-11-14-A: 0 ; afa53c6 contained by: parked/Praxis_build-vn4, remotes/origin/parked/Praxis_build-vn4
```

**Attack 4: S8, S2, S5.** No sentence answers Q1-Q6. R8's "Recorded as wait-for-data" is the notes' own wording (notes :64), and the entry keeps Q1 open, so that is not the filer's choice. Live check, `jobs.json` read-only at 15:22:17Z: `{'id': '73d67fad7ec9', ..., 'enabled': False, 'state': 'paused', ...}`. The loop is paused now, but the entry asserts it without its own observation (defect 3). For S5, see defect 1.

**Attack 5: S13.**
```
entry -x:1 (last line) | overnight -x:1 | brief -x:1 | notes -x:1, substring:2
overnight orig 34 / staged 36 prefix-cmp IDENTICAL | notes 71/73 IDENTICAL | brief 49/49 IDENTICAL
notes:71 = "Fills are optimistic; ... assumed (carried from the source brief)."
```

**Attack 6: name sweep, counts only.** `tok len=4`, email non-empty.
```
entry/blob-D/head-D/overnight/brief/notes: email=0 token_ci=0 ; blob-M token_ci=2, head-M token_ci=2 ; new MANIFEST rows token_ci=0
```
One slip to disclose: my own `git diff --cached --name-status` on the real index printed that file's name, which contains the token, in my tool output. It is not repeated in this report.

**Attack 7: scope.** `M DECISIONS.md 89/0`, `M MANIFEST.md 6/0`, `A` three voice files (36, 49, 73). Only the five paths, no deletions.

### Defects
1. **MAJOR (S5 / attribution), blob :2577.** "R5 names it as the starting point (notes :34)." Notes :34 ("The draft rule D-2026-11-14-A ... is the starting point for R5") is the voice agent's text. Amear's only words are :33 ("I accept those as you uh, suggested them"), and the brief he accepted says "Amear has not ruled on it" (brief :34). The sentence credits voice-agent text to a ruling filed as WHO: amear.
2. **MAJOR (S4), blob :2612.** "Written 2026-11-14T15:14:01Z, before any work the rulings govern" is false for R1. The pause ran at 14:49:30Z and was read back at 14:50:10Z, so the work came before this entry. The R4 recheck unit was also dispatched at 15:08:00Z, and `docs/reports/2026-11-14-r3-recheck-worker1.md` now exists (mtime 10:18:57 ET). The entry should say R1 went ahead on the ledger row, before this entry.
3. **MINOR (S1/S2), :2612.** "The search loop stays paused." is stated in the present tense, yet :2538 says "not re-observed by this filer". It is true at 15:22Z by my read, but the filing itself has no observation behind it.
4. **MINOR (attribution), :2598.** "(b) ... proposed to Amear, not self-certified (notes :59)". Notes :59 is the voice agent's handoff, and its source is not labelled. Amear's :48 says only "create a skill".
5. **MINOR (S6), :2603-:2608.** Untested cross-block touches:
   - R5 (Mac Python screens) against the Block 2 spec, :64 and :76 (NinjaTrader Strategy Analyzer, Order Fill Resolution = High). "Block 2" appears 0 times in the entry.
   - R2 against Block 2's MFFU/Rithmic data path (:64).
   - R3 against Block 5 stages A and B, fixed 1 MNQ and 1 NQ (:138-:139). Only :140 is cited.
   - The first-filter change against Ruling 2, which lists "the step 4 search loop and its backtests" as carrying on. The entry groups it with "harness work as UNCLEAR".
6. **MINOR (S4 / MANIFEST).** The staged MANIFEST adds 6 rows, but the dispatch row (DL :974) says "MANIFEST.md (HEAD plus 3 rows)". Three rows point to the manager, worker1 and worker2 reports, which are not in the temp index (they are `??` in the worktree). The entry also cites the worker1 report at :2610. A commit as staged would leave dangling references, and the 3-to-6 deviation has no record.
7. **MINOR.** The bold titles are credited to the voice agent at :2529, but three are copied altered without saying so. R4 drops "five" (notes :26), R5 and R6 are merged into one heading (notes :31-:32), and R9 drops "for the Code session" (notes :46).
8. **MINOR (S13 "once", debatable).** The staged notes now carry the limitation sentence twice: at :71 with a suffix, and exactly at :73.

**Result: FAIL**

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
