# 7zq M3 — worker1 ADVERSARIAL: D-2026-10-31-A append (DECISIONS.md 305–364) + MANIFEST rows (154–174)

## Task
Unit `Praxis_build-7zq`, phase M3, mode ADVERSARIAL. Try to break the claim that the unstaged appends to `DECISIONS.md` (lines 305–364) and `MANIFEST.md` (lines 154–174) are (a) the M1 draft entry (`docs/reports/2026-10-31-7zq-decisions-scope.md:18-65`) transferred verbatim except permitted changes (i)–(v), (b) correct MANIFEST rows, (c) append-only, and (d) S8-clean. Criteria: `specs/SPEC_RUBRIC.md` S1, S4, S5, S8. I edited nothing except this report. Nothing staged, nothing committed.

Scratch scripts: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/` (`draft.txt`, `appended.txt`, `chk1.py`–`chk4.py`).

## Commands and pasted output per check

### Check 1 — Verbatim diff

```
$ sed -n '18,65p' docs/reports/2026-10-31-7zq-decisions-scope.md | tee $S/draft.txt | wc -l
      48
$ sed -n '308,364p' DECISIONS.md | tee $S/appended.txt | wc -l
      57
$ wc -l DECISIONS.md MANIFEST.md
     364 DECISIONS.md
     174 MANIFEST.md
$ diff $S/draft.txt $S/appended.txt ; echo "diff rc=$?"
4c4
< **Status:** PROPOSED — authorised by DECISION_LOG `2026-10-31T00:46:43Z` (WHO: amear): *"RULING REVERSED BY AMEAR: ... "* Third file, same row: *"Build the top-ranked one (Recommended)"*. Amear may swap after reading the shortlist.
---
> **Status:** AUTHORISED by Amear — R-7zq-1, DECISION_LOG `2026-10-31T11:04:20Z` (WHO: amear): *"Yes — append it now, then commit."* Appended 2026-10-31 by M3. The three files are research-only backtest material (R-7zq-4, DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear): *"Research-only backtest material"*). Originally PROPOSED — authorised by DECISION_LOG `2026-10-31T00:46:43Z` (WHO: amear): *"RULING REVERSED BY AMEAR: ... "* Third file, same row: *"Build the top-ranked one (Recommended)"*. Amear may swap after reading the shortlist; he kept #1 as built (R-7zq-3, `2026-10-31T11:45:29Z`).
26c26
< - **Third file — one new researched NQ intraday strategy, built in milestone M2:** `[M2 fills: strategy name, source]`. The research manager ranks ...
---
> - **Third file — one new researched NQ intraday strategy, built in milestone M2:** **`PraxisLastHalfHourMomentum`** (...) ... **Amear may swap to #2 or #3 after reading the shortlist.**. The research manager ranks ...
48a49,57
> 
> **Rulings (Amear, 2026-10-31):**
> - **R-7zq-1 — S4 ordering (answers NEEDS AMEAR 5 above), DECISION_LOG `2026-10-31T11:04:20Z` (WHO: amear):** *"Yes — append it now, then commit."* ...
> - **R-7zq-2 — Flat1559 fill (answers NEEDS AMEAR 7 above), DECISION_LOG `2026-10-31T11:04:20Z` (WHO: amear):** *"Yes — test it as built."* ...
> - **R-7zq-3 — third file (answers NEEDS AMEAR 6 above), DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear):** *"Keep #1 (as built)"* — ...
> - **R-7zq-4 — breaker #5, DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear):** *"Research-only backtest material"* — ...
> - **R-7zq-5 — 15:59 exit of the third file, DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear):** *"Yes — same ruling"* — R-7zq-2 extends to `PraxisLastHalfHourMomentum`.
> - **Still open (NEEDS AMEAR):** 3gm Q1 sizing (b) vs (c) (item 2 above); 3gm Q2, ... (item 1 above); early-close handling (item 3 above); adoption of the 15:59 decision into the base ... (3gm C3, item 4 above; R-7zq-2 rules the backtest fill of the variant, not this); Step 0, the values for High's extra fields and what counts as "identical" (`docs/reports/2026-10-31-7zq-m1-variants.md:148`; `docs/reports/2026-10-31-7zq-handtest-checklist.md:293`); and, for the third file (M2 addendum §(e), left open by DECISION_LOG `2026-10-31T11:45:29Z`): r = 0 → short; the previous-close rule; the missing-15:30 fallback; the 15:30 reference price; the η(r_ONFH, r_ROD) variant; the roll convention. Addendum §(e) item 9 (the first session of the series has no prior close; the design skips it) is not in that row's list and has not been ruled either.
> - **Note:** DECISION_LOG line numbers quoted above were taken at draft time and have shifted; row stamps are the stable key. (This entry cites DECISION_LOG by row stamp; its `:NNN` citations point into other files and are left as drafted.)
diff rc=1
```
(Long quoted lines are cut with `...` here only. The full diff is in the tool output of this session and can be reproduced from the scratch files.)

So exactly three hunks: entry line 4 (= DECISIONS:311), entry line 26 (= DECISIONS:333), and lines 49–57 added (= DECISIONS:356–364). Draft lines 1–3, 5–25, 27–48 match byte-for-byte.

**(i) byte-for-byte** (`chk1.py`):
```
addendum39 startswith "> ": True
placeholder count in d43: 1
DECISIONS line 333 equals expected: True
len expected 1947 len actual 1947
d43 prefix: '- **Third file — one new researched NQ intraday strategy, built in milestone M2:** '
d43 suffix: '. The research manager ranks a shortlist of three; #1 is built; Amear may swap in the morning, and the other two survive as written specs (`2026-10-31T00:46:43Z`).'
a39 tail: ' **Amear may swap to #2 or #3 after reading the shortlist.**'
trailing ws a39? False
```
DECISIONS:333 == draft:43 with the placeholder replaced by addendum:39 minus `> `. The `**.` artefact ("…shortlist.**. The research…") comes from the draft's own `.` after the placeholder. That is exactly what the rule says to do, so it is permitted.

**(ii) status line** (`chk4.py`):
```
orig body (minus trailing .) in new: True | orig ends with .: True
new before: '**Status:** AUTHORISED by Amear — R-7zq-1, DECISION_LOG `2026-10-31T11:04:20Z` (WHO: amear): *"Yes — append it now, then commit."* Appended 2026-10-31 by M3. The three files are research-only backtest material (R-7zq-4, DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear): *"Research-only backtest material"*). Originally PROPOSED'
new after: '; he kept #1 as built (R-7zq-3, `2026-10-31T11:45:29Z`).'
```
The original status text is kept whole. Only three things changed: `PROPOSED` became `Originally PROPOSED`, the final `.` became `;`, and new text was added before and after. Nothing was dropped or reworded. The added clauses are "Appended 2026-10-31 by M3" (a (iv)-type marker) and "he kept #1 as built (R-7zq-3…)". The second one goes beyond what (ii) lists, but the ledger supports it (see F2).

**(iii) quoted rulings vs ledger** (`chk2.py`):
```
rows found 1 1
'Yes — append it now, then commit.' log bold-quoted: True | dec lines containing *"q"*: 2
'Yes — test it as built.' log bold-quoted: True | dec lines containing *"q"*: 1
'Keep #1 (as built)' log bold-quoted: True | dec lines containing *"q"*: 1
'Research-only backtest material' log bold-quoted: True | dec lines containing *"q"*: 2
'Yes — same ruling' log bold-quoted: True | dec lines containing *"q"*: 1
```
(The counts of 2 are the status line plus the bullet.) Ledger rows, verbatim:
```
464:- [2026-10-31T11:45:29Z] **WHO: amear** | PROPOSED BY: praxis-master (three questions lifted from M2's NEEDS AMEAR 1, 5, 9) | APPROVED BY: amear, AskUserQuestion this turn | WHAT: **THREE RULINGS.** (R-7zq-3) Third file: **"Keep #1 (as built)"** — `PraxisLastHalfHourMomentum.cs` (Baltussen et al. 2021) stands; TORB and ORB remain written specs in the shortlist. (R-7zq-4) Breaker #5: **"Research-only backtest material"** — tested today; breaker #5 and F2 untouched; any move toward live is a separate decision. (R-7zq-5) 15:59 exit: **"Yes — same ruling"** — R-7zq-2 extends to this file. M2's remaining NEEDS AMEAR items (r = 0 → short; previous-close rule; missing-15:30 fallback; 15:30 reference price; the η(r_ONFH, r_ROD) variant; roll convention) stay open and unanswered — they are readback-dependent and do not block a hand test of the file as built. | WHY: S8. | STATE: closed — ruled.
467:- [2026-10-31T11:04:20Z] **WHO: amear** | PROPOSED BY: praxis-master (two questions lifted from M1's NEEDS AMEAR 5 and 7) | ... (R-7zq-1) S4 ordering: **"Yes — append it now, then commit."** The draft-alongside-the-.cs ordering, with the 00:46:43Z ledger row as authorisation, satisfies his 22:58Z "before any .cs" rule; `D-2026-10-31-A` is appended to DECISIONS.md (M2's name filled in) before any 7zq commit; the files stand. (R-7zq-2) Flat1559 fill: **"Yes — test it as built."** The 15:59-bar submission / 16:00-bar-open fill (~15:59 price, flat by 16:00) is accepted as the backtest realisation; the Trades-tab readback decides whether the base's own flat was landing next-day. Master's sequencing of R-7zq-1: ... "Now" is read as "before the commit", which the sequencing honours; if Amear meant before M2 finishes, he can say so and the append goes first. ...
```
All five quotes match character for character, em dashes included. The explanatory text after each quote follows the ledger WHAT text closely, with no change of meaning.

**"answers NEEDS AMEAR n" vs the draft's numbered list** (draft:58–65, pasted):
```
5. **S4 timing:** row `2026-10-30T22:58:00Z` required this entry "written and staged BEFORE any `.cs` line". ... Does that arrangement meet his constraint?
6. **Third file:** the M2 pick is #1 of the shortlist by his ruling. The swap stays his after he reads the shortlist.
7. **Flat1559 fill price:** is a fill at the 16:00 bar's Open (~15:59 price) acceptable as the backtest realisation of the 16:00 flat, ...
```
R-7zq-1→5, R-7zq-2→7 and R-7zq-3→6 are correct against the draft's numbering ("above"). The ledger uses M1's *manager-report* numbering ("M1's NEEDS AMEAR 5 and 7"), where `m1-variants.md` has 5 = Flat1559 and 7 = S4 ordering, the reverse of the draft's. Both sets of numbers are internally right, but a reader comparing the two could be confused (Observation O1).

**Stamps cited in the entry all resolve** (`chk2.py`): every backticked stamp maps to 1 row, except `2026-10-31T11:45:29Z` → `rows in log: 2` (line 464 amear, line 465 praxis-master "M2 AUDITOR RETURNED NO VERDICT"). See F1.

**Draft markers / DECISION_LOG line cites:** `chk2.py` regex `DECISION_LOG[^`\s]*:\d+|M2 fills|DRAFT|NOT APPENDED|TBD` over DECISIONS:308–364 printed **no hits**, and `chk4.py` found no DRAFT/NOT APPENDED marker in draft 18–65. So (iv) had nothing to remove. The Note's parenthetical ("cites DECISION_LOG by row stamp; its `:NNN` citations point into other files") is true.

**Separator and end of file:**
```
$ sed -n '300,308p' DECISIONS.md | cut -c1-100 | cat -vet
...  (300–304: last bullets of D-2026-10-30-A)
$
---$
$
## 2026-10-31 M-bM-^@M-^T D-2026-10-31-A: 7zq scope extension ...
$ git show HEAD:DECISIONS.md | wc -l
     304
$ tail -c 200 DECISIONS.md | od -c | tail -5
... d   .   )  \n
```
Lines 305/306/307 are blank / `---` / blank, matching the earlier entries (e.g. DECISIONS:244–247 is `$ ---$ $ ## 2026-10-30 …`). The file is 364 lines and ends with the Note bullet plus one `\n`. Nothing follows line 364.

### Check 2 — MANIFEST paths (`chk3.py`)
```
L154 cols=5 lead/=True exists=True date=2026-10-31 type=Source phase=2 path=/ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
   draft scope:71 wholerow_equal=True cols_equal=True
L155 cols=5 lead/=True exists=True date=2026-10-31 type=Source phase=2 path=/ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
   draft scope:72 wholerow_equal=True cols_equal=True
L156 cols=5 lead/=True exists=True date=2026-10-31 type=Report phase=2 path=/docs/reports/2026-10-31-7zq-handtest-checklist.md
   draft scope:73 wholerow_equal=True cols_equal=True
L157 cols=5 lead/=True exists=True date=2026-10-31 type=Report phase=2 path=/docs/reports/2026-10-31-7zq-decisions-scope.md
   draft scope:74 wholerow_equal=False cols_equal=False
   col 4 DIFF
      insert '' -> ' — transferred by M3 2026-10-31 (entry appended to DECISIONS.md, rows to MANIFEST.md)'
L158 cols=5 lead/=True exists=True date=2026-10-31 type=Report phase=2 path=/docs/reports/2026-10-31-7zq-m1-variants.md
   draft scope:75 wholerow_equal=False cols_equal=False
   col 4 DIFF
      insert '' -> '; audited PASS at DECISION_LOG 2026-10-31T10:47:43Z (row appended by M3)'
L159 ... m1-worker1-build-variants.md   draft scope:76 wholerow_equal=True
L160 ... m1-worker3-adversarial.md      draft scope:77 wholerow_equal=True
L161 ... m1-worker4-fix.md              draft scope:78 wholerow_equal=True
L162 ... m1-worker5-readversarial.md    draft scope:79 wholerow_equal=True
L163 cols=5 lead/=True exists=True date=2026-10-30 type=Report phase=2 path=/docs/reports/2026-10-30-zyd-rulings-append.md
   draft scope:80 wholerow_equal=True cols_equal=True
L164 ... /ninjascript/PraxisLastHalfHourMomentum.cs   draft addendum:62 wholerow_equal=True
L165 ... m2-shortlist.md           draft addendum:63 wholerow_equal=True
L166 ... m2-worker1-research.md    draft addendum:64 wholerow_equal=True
L167 ... m2-worker2-build.md       draft addendum:65 wholerow_equal=True
L168 ... m2-worker3-docs.md        draft addendum:66 wholerow_equal=True
L169 ... m2-worker4-adversarial.md draft addendum:67 wholerow_equal=True
L170 ... m2-worker5-fix.md         draft addendum:68 wholerow_equal=True
L171 ... m2-handtest-checklist.md  draft addendum:69 wholerow_equal=True
L172 cols=5 lead/=True exists=True date=2026-10-31 type=Report phase=2 path=/docs/reports/2026-10-31-7zq-m2-decisions-addendum.md
   draft addendum:70 wholerow_equal=False cols_equal=False
   col 4 DIFF
      insert '' -> ' — transferred by M3 2026-10-31'
L173 cols=5 lead/=True exists=True date=2026-10-31 type=Report phase=2 path=/docs/reports/2026-10-31-7zq-m2-new-strategy.md
   draft addendum:71 wholerow_equal=False cols_equal=False
   col 4 DIFF
      insert '' -> '; audited PASS at DECISION_LOG 2026-10-31T11:49:28Z (row appended by M3)'
L174 cols=5 lead/=True exists=True date=2026-10-31 type=Report phase=2 path=/docs/reports/2026-10-31-7zq-m3-append.md
   NO DRAFT ROW
draft paths not in appended rows: []
dups within appended: []
required with no row: []
total rows in manifest for each path: {}
```
(Lines L159–L171 are cut here only, as marked with `...`. Every one printed `cols=5 lead/=True exists=True date=2026-10-31`, type Report or Source, phase 2, `wholerow_equal=True`.) There are no mentions of these paths in pre-existing MANIFEST lines 1–153, because the script printed no `PRE-EXISTING mention` line.

`ls -l` of every path in rows 154–174:
```
-rw-r--r--@ 1 admin  staff  15658 Oct 30 19:25 docs/reports/2026-10-30-zyd-rulings-append.md
-rw-r--r--@ 1 admin  staff  16755 Oct 31 06:37 docs/reports/2026-10-31-7zq-decisions-scope.md
-rw-r--r--@ 1 admin  staff  18509 Oct 31 06:25 docs/reports/2026-10-31-7zq-handtest-checklist.md
-rw-r--r--@ 1 admin  staff  33743 Oct 31 06:40 docs/reports/2026-10-31-7zq-m1-variants.md
-rw-r--r--@ 1 admin  staff  33198 Oct 31 06:14 docs/reports/2026-10-31-7zq-m1-worker1-build-variants.md
-rw-r--r--@ 1 admin  staff  16264 Oct 31 06:23 docs/reports/2026-10-31-7zq-m1-worker3-adversarial.md
-rw-r--r--@ 1 admin  staff  30634 Oct 31 06:28 docs/reports/2026-10-31-7zq-m1-worker4-fix.md
-rw-r--r--@ 1 admin  staff  15863 Oct 31 06:37 docs/reports/2026-10-31-7zq-m1-worker5-readversarial.md
-rw-r--r--@ 1 admin  staff  15066 Oct 31 07:15 docs/reports/2026-10-31-7zq-m2-decisions-addendum.md
-rw-r--r--@ 1 admin  staff   5412 Oct 31 07:12 docs/reports/2026-10-31-7zq-m2-handtest-checklist.md
-rw-r--r--@ 1 admin  staff  17956 Oct 31 07:18 docs/reports/2026-10-31-7zq-m2-new-strategy.md
-rw-r--r--@ 1 admin  staff  21734 Oct 31 06:51 docs/reports/2026-10-31-7zq-m2-shortlist.md
-rw-r--r--@ 1 admin  staff  12924 Oct 31 06:52 docs/reports/2026-10-31-7zq-m2-worker1-research.md
-rw-r--r--@ 1 admin  staff  11576 Oct 31 06:57 docs/reports/2026-10-31-7zq-m2-worker2-build.md
-rw-r--r--@ 1 admin  staff   5350 Oct 31 06:58 docs/reports/2026-10-31-7zq-m2-worker3-docs.md
-rw-r--r--@ 1 admin  staff  13362 Oct 31 07:08 docs/reports/2026-10-31-7zq-m2-worker4-adversarial.md
-rw-r--r--@ 1 admin  staff  12574 Oct 31 07:14 docs/reports/2026-10-31-7zq-m2-worker5-fix.md
-rw-r--r--@ 1 admin  staff    140 Oct 31 07:52 docs/reports/2026-10-31-7zq-m3-append.md
-rw-r--r--@ 1 admin  staff  15318 Oct 31 07:15 ninjascript/PraxisLastHalfHourMomentum.cs
-rw-r--r--@ 1 admin  staff  17921 Oct 31 06:29 ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
-rw-r--r--@ 1 admin  staff  17153 Oct 31 06:25 ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
```
`ls -1 docs/reports/2026-10-31-7zq-*.md` lists 17 files, and every one has a row ("required with no row: []").

Checking the added Purpose text against the ledger:
```
468:- [2026-10-31T10:47:43Z] WHO: praxis-master | WHAT: **7zq M1 AUDIT: PASS. No BLOCKING finding. ...
462:- [2026-10-31T11:49:28Z] WHO: praxis-master | WHAT: **7zq M2 REDUCED AUDIT: PASS. No BLOCKING finding; ...
463:- [2026-10-31T11:49:28Z] WHO: praxis-master | WHAT: **7zq M3 (DECISIONS/MANIFEST APPEND) DISPATCHED.** ...
```
- L157 / L172 "transferred by M3 2026-10-31": TRUE (the transfer is the artefact under test).
- L158 "audited PASS at DECISION_LOG 2026-10-31T10:47:43Z": TRUE (row 468).
- L173 "audited PASS at DECISION_LOG 2026-10-31T11:49:28Z": TRUE, with two gaps. The ledger calls it a **REDUCED** audit, which the row leaves out, and stamp 11:49:28Z has two rows (462 and 463). See F3.
- L174 (m3-append.md, no draft row): the file exists (140 bytes, a stub) and the purpose ends "ungraded at time of row". That is accurate. The brief allows extra rows for existing 7zq files.

### Check 3 — Zero deletions
```
$ git diff --numstat -- DECISIONS.md MANIFEST.md
60	0	DECISIONS.md
21	0	MANIFEST.md
$ git diff -- DECISIONS.md MANIFEST.md | grep '^-' | grep -v '^---'; echo "grep rc=$?"
grep rc=1
$ git diff -U0 -- DECISIONS.md MANIFEST.md | grep '^@@'
@@ -304,0 +305,60 @@ Q1 was closed session 14 (re-implement in NT8, D 21:10Z). The remaining Block-2
@@ -153,0 +154,21 @@
```
Append-only: two pure-insert hunks at EOF (HEAD DECISIONS = 304 lines, HEAD MANIFEST ends at 153), zero deletions. `git diff --cached` for both files printed nothing (unstaged, as the brief states). `git log --oneline --all | grep -c 7zq` → `0`: no 7zq commit exists yet, so "appended before any 7zq commit" (R-7zq-1 bullet) currently holds.

### Check 4 — S8

Draft NEEDS AMEAR 1–7 (draft:58–65):
| # | Item | Disposition in appended entry | Evidence |
|---|------|------|------|
| 1 | 3gm Q2 OppBand meaning | named open ("item 1 above") | DECISIONS:363 |
| 2 | 3gm Q1 sizing | named open ("item 2 above") | DECISIONS:363 |
| 3 | early-close handling | named open ("item 3 above") | DECISIONS:363 |
| 4 | 3gm C3 15:59 adoption into base | named open ("item 4 above"), explicitly not covered by R-7zq-2 | DECISIONS:363 |
| 5 | S4 timing | answered: R-7zq-1, 11:04:20Z, "Yes — append it now, then commit." | ledger :467 |
| 6 | third file swap | answered: R-7zq-3, 11:45:29Z, "Keep #1 (as built)" | ledger :464 |
| 7 | Flat1559 fill price | answered: R-7zq-2, 11:04:20Z, "Yes — test it as built." | ledger :467 |

Addendum §(e) 1–10 (addendum:105–130):
| # | Item | Disposition | Evidence |
|---|------|------|------|
| 1 | swap | R-7zq-3 "Keep #1 (as built)" | :464 |
| 2 | r = 0 → short | open | DECISIONS:363; :464 stay-open list |
| 3 | prior close (D3) | open ("previous-close rule") | same |
| 4 | missing 15:30 fallback | open | same |
| 5 | 15:59 exit realisation | R-7zq-5 "Yes — same ruling" | :464 |
| 6 | 15:30 reference price | open | same |
| 7 | η(r_ONFH, r_ROD) variant | open | same |
| 8 | roll convention | open | same |
| 9 | first session, no prior close | named as not ruled ("not in that row's list and has not been ruled either") | DECISIONS:363 |
| 10 | breaker #5 overlap | R-7zq-4 "Research-only backtest material" | :464 |

Step 0 (High fields / "identical"), required by the brief: named open. The cites resolve:
```
$ sed -n '146,149p' docs/reports/2026-10-31-7zq-m1-variants.md
...
6. **Step 0.** What value for High's extra fields, and what counts as "identical"?
...
$ sed -n '291,294p' docs/reports/2026-10-31-7zq-handtest-checklist.md
...
4. **Step 0 — High's extra fields.** If `High` shows a secondary-series type/value: which value do you
```
The "Still open" bullet against the 11:45:29Z stay-open list: the ledger list is (r = 0 → short; previous-close rule; missing-15:30 fallback; 15:30 reference price; η(r_ONFH, r_ROD) variant; roll convention). All six appear in DECISIONS:363 in the same order. All 11 items the brief requires are present. Every one of the 17 NEEDS AMEAR items is either answered by an Amear row or named as open. I found no sentence that decides anything Amear has not ruled.

## Findings
None of these is a BREAK of the stated criteria. They are listed so the auditor can judge them.

1. **F1 — the "stable key" isn't unique for one stamp (minor, S1/traceability).** DECISIONS:363 Note says "row stamps are the stable key". But `2026-10-31T11:45:29Z` matches 2 DECISION_LOG rows (`chk2.py`: `rows in log: 2`; :464 amear, :465 praxis-master "M2 AUDITOR RETURNED NO VERDICT"). Most cites add `(WHO: amear)`, which tells them apart. Two do not: DECISIONS:311 "(R-7zq-3, `2026-10-31T11:45:29Z`)" and DECISIONS:363 "left open by DECISION_LOG `2026-10-31T11:45:29Z`". In both, the ruling content points to :464, so there is no misattribution, only a key that doesn't pick one row on its own.
2. **F2 — additions beyond the literal (ii)/(iii) specification (classified, not unpermitted in effect).** DECISIONS:311 adds "Appended 2026-10-31 by M3" and "; he kept #1 as built (R-7zq-3 …)". DECISIONS:363 adds the "Addendum §(e) item 9 … has not been ruled either" sentence and the parenthetical "what counts as 'identical'". DECISIONS:364 adds the Note's parenthetical. Each one is true against the ledger or the source files cited above, and each names something as open rather than deciding it. Strictly, they are text beyond what the five permitted changes enumerate. I classify them as within (ii)/(iii)/(v) in substance; the auditor may rule otherwise.
3. **F3 — MANIFEST Purpose additions beyond the draft text (4 rows).** MANIFEST:157, :158, :172 and :173 append text not in the draft rows (diffs pasted in Check 2). All are factually true. One gap: :173 says "audited PASS" where the ledger :462 says "REDUCED AUDIT: PASS". It cites stamp 11:49:28Z, which has 2 rows (:462 audit, :463 M3 dispatch).
4. **O1 — numbering clash between entry and ledger (observation).** Entry: R-7zq-1 "answers NEEDS AMEAR 5", R-7zq-2 "answers 7" (draft numbering, correct). Ledger :467: "lifted from M1's NEEDS AMEAR 5 and 7" (m1-variants numbering, where 5 = Flat1559 and 7 = S4, i.e. reversed). Both are right in their own frame. The entry does not say which frame it uses beyond "above".
5. **O2 — ledger mislabel outside scope (second bug, reported, not fixed).** DECISION_LOG:464 says "three questions lifted from M2's NEEDS AMEAR 1, 5, 9". By content, the rulings answer addendum §(e) items 1 (swap), 5 (15:59 exit) and **10** (breaker #5), not 9. The appended entry's claim that item 9 "has not been ruled" is correct by content. It does not mention the ledger's "9" label, which a reader could take as item 9 having been ruled.
6. **O3 — a master reading is not carried into the entry (observation, S5/S8 edge).** Ledger :467 records the master's reading that "Now" means "before the commit", adding "if Amear meant before M2 finishes, he can say so". The entry's R-7zq-1 bullet leaves out that caveat. The caveat is the master's sequencing note, not an Amear ruling, and it is not one of the 17 NEEDS AMEAR items. The entry does not claim Amear ruled on it. I'm reporting it as an observation only.
7. **O4 — stale text kept verbatim (permitted).** DECISIONS:333 (from addendum:39) still says "**Amear may swap to #2 or #3 after reading the shortlist.**". R-7zq-3 has since resolved this, and the status line and rulings block say so. Keeping the text is required by the verbatim rule.

VERDICT: CLEAN
