Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

# Unit 2026-11-09-wf-spec-amendment-resume (U7 resumed, bead Praxis_build-diq): manager report

## Task

U7 (unit `2026-11-08-wf-spec-amendment` and corrections 1–3) amended `docs/specs/2026-11-06-walk-forward-values.md` (v2.2) and `docs/specs/2026-11-05-walk-forward-spec.md` (A4 buffer). Its audit FAIL 2 was on one item: the U7 report's pasted "current diff of record" (`docs/reports/2026-11-08-wf-spec-amendment-manager.md` :521–620) predates correction 3's edit at values :12. Amear C1 (D-2026-11-08-C, DECISIONS.md:1823–1825), verbatim:

```
C1  U7 (Praxis_build-diq) resumes in this new session. One correction:
    replace the stale pasted diff with the diff of the blob being
    committed. One audit. No park branch is landed for diq.
```

Master's reading (filing note 2, DECISIONS.md:1870), changeable by Amear: "C1's "replace the stale pasted diff" is carried out by APPENDING the diff of the blob being committed as the diff of record"; "The stale paste is not deleted."

This unit: (1) freeze check of both specs, no spec edit; (2) MANIFEST relocation (master's decision under D-2026-11-08-D D1); (3) the one correction: the diff of record in this report, and one SUPERSEDED line appended to the U7 report; (4) the diff pasted last; (5) the commit set; (6) an S6 note.

## Rubric criteria addressed

From `specs/SPEC_RUBRIC.md` (:115, :116, :118, :120, :121, :127):

- S1: "Every claim in a report has pasted command output, not a description of output."
- S2: "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure."
- S4: "Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after."
- S6: "Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own."
- S7: "Nothing is committed while any audit box is unchecked."
- S13: "Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: "[the sentence on line 1 of this report; elided here so that it is carried once]" …" (DT4)

This report states no backtest or P&L figure. It carries the sentence once, on line 1, under S13's house-style clause ("Reports with no such figure carry it too").

## Decisions taken (master's brief: "Decide under D-2026-11-08-D D1"; each changeable by Amear)

- **DT1. S13 vs "paste the FULL output".** The full `git diff HEAD -- <both specs>` contains the standing sentence once, in full, as a context line of the values spec (its :7; diff line 62), and a truncated part of it (80 characters) in one hunk header of the WF spec (diff line 5). Pasted unchanged, this report would carry the sentence twice, against the brief ("That sentence appears once only, on line 1") and S13 ("carries, once"). Decision: paste every byte, except that each occurrence is replaced by a bracketed marker naming how many characters of line 1 it stands for. The raw bytes are rebuilt from this file by a pasted snippet, and the rebuilt sha256 is shown to equal the live diff's sha256. U7 did the same kind of thing with a `sed` on hunk headers (U7 report :525–527); this rule changes fewer bytes and can be reversed.
- **DT2. The MANIFEST self-reference edits.** The full list, old and new (E1 and E2). These are the only position-dependent self-references in the six U7 rows:
  - E1, U7 manager-report row (pre-unit :301, now :309): old `MANIFEST rows 299–301` → new `MANIFEST: the U7 amendment rows for the two specs and this report`
  - E2, correction-2 report row (pre-unit :303, now :311): old `MANIFEST rows 302–303` → new `MANIFEST: the U7 correction-1 and correction-2 report rows`
- **DT3. Cross-references kept.** The values-spec row says "adds to rows 254 and 271 for this path", and the WF-spec row says "adds to row 227 for this path". These point at other rows, not at the U7 rows. They sit inside lines 1–306, which equal HEAD byte for byte (A2 below), so they stay correct after the move. They are left unchanged.
- **DT4. The S13 quote is elided.** Quoting S13 verbatim would put the sentence in this report a second time.
- **DT5. One paste of the diff, taken last.** The diff of record and the final evidence block are written by one script run (`/tmp/diq-resume/assemble.py`), after every other edit. The diff is pasted once, not twice, and the final block proves that a live re-run gives the same sha256.
- **DT6. My report's MANIFEST row.** It is the last row (:313). Its exact text is in A5 of the worker's script, which is in `/tmp/diq-resume/manifest_relocate.py`.
- **DT7. S4.** DT1–DT6 depart from the master's dispatch brief, not from a plan line that S4 governs. This unit may not touch DECISIONS.md. The precedent is the master's own reading in DECISION_LOG.md:739 (row `2026-11-08T17:08:00Z`, working tree): brief departures that stay within the brief's latitude need no DECISIONS.md entry. That reading is for the master and the auditor to confirm for this unit. I do not assert it here.

## Workers dispatched (id, mode, outcome)

| # | id | mode | scope | outcome |
|---|---|---|---|---|
| W1 | abc0fed90cdc93e76 | BUILD | MANIFEST relocation script `/tmp/diq-resume/manifest_relocate.py`. It wrote MANIFEST.md and verified it. | Returned `Result: PASS`. Run 1 wrote the correct file but exited 1, because its first A6 assert was wrong: it left out the HEAD rows 299–306 that replace the dropped duplicate block. The worker fixed the assert, not the file. W1 reports that runs 2 (write mode, no write) and 3 (`--verify`) exited 0. The manager did not capture those runs. The manager's own `--verify` run and independent re-check are in the final evidence block. |
| W2 | (see Adversarial findings) | ADVERSARIAL | Attacked the draft report, the generator, MANIFEST.md and the U7 append. It was given the artifacts and the criteria, not W1's reasoning. | See Adversarial findings |

The U7 append (one line) and this report were written by the manager. The append is a single-line change.

## Process log

1. Freeze check (V1). Both specs untouched by this unit.
2. Confirmed the stale-paste claim (V2).
3. Appended the SUPERSEDED line to the U7 report by script, asserting the old bytes are a prefix of the new (V3).
4. W1 rebuilt MANIFEST.md (V4). I re-checked it independently (V5).
5. Wrote the generator. It produced a draft at `/tmp/diq-resume/draft.md`, and W2 attacked the draft.
6. Final run of the generator, as the last edit: the diff of record and the final evidence block.

## Verification evidence (pasted output only)

### V1 — freeze check (start of unit, before any edit)

```
$ git rev-parse HEAD origin/main
f10603a242a7f7b8195caef24712d31c4ca67512
f10603a242a7f7b8195caef24712d31c4ca67512
$ git diff --numstat HEAD -- docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md
5	5	docs/specs/2026-11-05-walk-forward-spec.md
21	21	docs/specs/2026-11-06-walk-forward-values.md
$ shasum -a 256 docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md
6d7ed4df9328ad2d2ac489834fdb3ec82fd296e5cd642d651747ffa3217ceb7e  docs/specs/2026-11-06-walk-forward-values.md
a80074ecc3cdb39c8bed9634d5f8a9a8c8def135849cc2af6fce785d9303cc04  docs/specs/2026-11-05-walk-forward-spec.md
$ wc -l MANIFEST.md; git show HEAD:MANIFEST.md | wc -l
     312 MANIFEST.md
     306
$ python3 -I -c "<split working-tree MANIFEST.md and HEAD:MANIFEST.md on LF; compare>"   # run before W1 was dispatched
313 307 b'' b''
first298 eq True
w305-312 == h299-306 True
```

The pre-unit MANIFEST baseline is `/tmp/diq-resume/MANIFEST.old.md`, sha256 c36921e8…9ed8. W1's script saved it on its first run, before it wrote anything. Before that, the manager captured no hash. Only the line count and the two equalities above were recorded beforehand. The six U7 rows are byte-identical to pre-unit :299–304 on the strength of that copy alone (W2 finding 6).

### V2 — the stale paste lacks correction 3's :12 hunk

```
$ git diff -U0 HEAD -- docs/specs/2026-11-06-walk-forward-values.md | /usr/bin/grep -c '^@@ -12 '
1
$ /usr/bin/grep -c '^@@ -12 ' docs/reports/2026-11-08-wf-spec-amendment-manager.md
0
```

### V3 — the U7 report append

```
$ shasum -a 256 docs/reports/2026-11-08-wf-spec-amendment-manager.md
f78aa3505f9ce01056f7300e769e07f91868f7393a2f4fc1bec305184f7c372a  docs/reports/2026-11-08-wf-spec-amendment-manager.md
$ python3 -I -c "<assert file ends in one LF; append the line; assert new == old + line>" docs/reports/2026-11-08-wf-spec-amendment-manager.md
appended; prefix intact 90673 90872
$ wc -l docs/reports/2026-11-08-wf-spec-amendment-manager.md
     628 docs/reports/2026-11-08-wf-spec-amendment-manager.md
```

The last line, and the proof that lines 1–627 are byte-identical to the pre-append file, are re-captured in the final evidence block.

### V4 — W1's MANIFEST script, run 1 (write) as returned by W1, abridged to its asserts

```
INFO saved current file as old copy /tmp/diq-resume/MANIFEST.old.md (144784 bytes)
PRE old[1..298]==HEAD[1..298] PASS: mismatched=0
PRE E1 once-in-row PASS: count=1
PRE E1 once-in-file PASS: count=1
PRE E2 once-in-row PASS: count=1
PRE E2 once-in-file PASS: count=1
INFO dash in E1/E2 old strings: U+2013 EN DASH bytes=e2 80 93; present in old:301=True, old:303=True
INFO wrote /Volumes/Sensidine/Praxis.build/MANIFEST.md (145371 bytes)
A6 multiset(old - dup block, E1/E2, + new row) == multiset(new) FAIL: lhs=305 rhs=313 extra-in-new=8 missing-from-new=0
A6b new bytes == computed expected PASS: new=145371B expected=145371B
A7 sha256 old  = c36921e8c3627119205435e045404e9d1dd1a9c66c60b5e9a76c1f3bdca89ed8 (144784 B, 312 lines)
A7 sha256 new  = 3dc8bec0b17e1cfe26ef04b563cc68b5fb9c59fcf406e784556beaeacaccffd4 (145371 B, 313 lines)
RESULT FAIL: ['A6 multiset(old - dup block, E1/E2, + new row) == multiset(new)']
exit=1
```

The run-1 A6 failure was a fault in the assert, not in the file. The `--verify` run in the final evidence block shows the corrected A6 and A6x passing on the same bytes (new sha256 3dc8bec0…ffd4 in both runs).

### V5 — manager's independent MANIFEST re-check (not using W1's script)

```
$ git --no-optional-locks diff HEAD -- MANIFEST.md | cut -c1-140
diff --git a/MANIFEST.md b/MANIFEST.md
index ff53c66..4847709 100644
--- a/MANIFEST.md
+++ b/MANIFEST.md
@@ -304,3 +304,10 @@
 | /DECISIONS.md | Log | 2 | 2026-11-09 | Update: D-2026-11-08-C (DECISIONS.md:1808-1889; Amear's answers C1–C10 to the 2026-11-08 park card
 | /docs/reports/2026-11-09-c-d-filing-resume-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-c-d-filing-resume (r
 | /docs/reports/2026-11-09-d6-drawdown-check-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-d6-drawdown-check (A
+| /docs/specs/2026-11-06-walk-forward-values.md | Spec | 2 | 2026-11-08 | AMENDMENT ROW (append-only registry — adds to rows 254 and 271 fo
+| /docs/specs/2026-11-05-walk-forward-spec.md | Spec | 3 | 2026-11-08 | AMENDMENT ROW (append-only registry — adds to row 227 for this path
+| /docs/reports/2026-11-08-wf-spec-amendment-manager.md | Report | 2 | 2026-11-08 | Manager report for unit 2026-11-08-wf-spec-amendment (U
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md | Report | 2 | 2026-11-08 | Manager report for the two-line correction
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md | Report | 2 | 2026-11-08 | Manager report for unit 2026-11-08-wf-spec
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md | Report | 2 | 2026-11-08 | manager report for the one-sentence update
+| /docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-wf-spec-amend
```

A re-run of this check by the generator is in the final evidence block.

## Adversarial findings

W2 (id ab1d5cf4c80e969e5, ADVERSARIAL, read-only) attacked the draft `/tmp/diq-resume/draft.md`, the generator, MANIFEST.md and the U7 append. It returned `VERDICT: DEFECTS FOUND` and `Result: PASS`, with no BLOCKER or MAJOR finding. The output below is W2's as returned, abridged. The manager did not re-capture it.

```
# A: W2's own rebuild of the pasted diff (its code, not the report's snippet) vs live git diff
rebuilt sha b06ee494396805c3cf0abc19314010347850b854c74a3e8f5a3f0226a6d4369e 43982 lines 161
live   sha b06ee494396805c3cf0abc19314010347850b854c74a3e8f5a3f0226a6d4369e 43982
equal True
# B1 negative test: tampered copies of the draft, report's snippet
untampered -> b06ee494…369e bytes: 43982
tamper byte in diff line 228 -> ff953e1a…6ec9 bytes: 43982
tamper marker 80->79 -> 909280ea…b541 bytes: 43981
tamper line-1 sentence -> 28438f2b…f401
drop last diff line -> 87aed14d…3136 bytes: 43464
decoy diff fence earlier -> 73cb3858…c9ac bytes: 2
# B2 negative test: copy of the MANIFEST script pointed at tampered copies
row200 exit 1 … A2 new[1..306] == HEAD[1..306] FAIL: mismatched=1
row310 exit 1 … A3 new[307..312] == old[299..304] FAIL
row313 exit 1 … A5 new line 313 == new row FAIL
# E: independent prefix check of the U7 report (correction-2 report :117-119 recorded this digest)
head -n 448 lines: fee64ca8…a600 recorded, fee64ca8…a600 live
```

Findings and disposition:

| # | sev | finding | disposition |
|---|---|---|---|
| 1 | MINOR | DT1 put the full sentence in the WF spec. It is a context line of the values spec (:7). | Fixed in DT1. |
| 2 | MINOR | The `git diff HEAD` comparison cannot be reproduced after the commit lands. | Fixed. The instruction now names base f10603a. The final block captures `git diff f10603a -- …` as well. |
| 3 | MINOR | Runs 2 and 3 of W1 were claimed without pasted output. | Fixed. They are labelled as W1's report. The manager's own `--verify` run is in the final block. |
| 4 | MINOR | Old MANIFEST row numbers in the four U7 reports (which this unit may not edit) now point at other rows. This was not disclosed. | Disclosed in "Does NOT cover". The list is in the final block. Not fixed: the brief forbids those edits. |
| 5 | NOTE | U7 :199 was misdescribed. | Fixed in "Does NOT cover". |
| 6 | NOTE | The six rows' byte-identity rests on a baseline copy saved mid-unit, with no earlier hash. A forged baseline passes. W2 found rows 299–303 quoted nowhere else. | Disclosed under V1. Not curable now. S2: it is stated at that level. |
| 7 | NOTE | Line 30 said S13 does not bind this report. | Reworded: S13's house-style clause applies. |
| 8 | NOTE | Generator: the adversarial placeholder was not asserted filled; the placeholder-token check ran before the final append; the sentence check was prefix/suffix only. | All three fixed in `assemble.py`. |
| 9 | NOTE | WF NEEDS AMEAR 7 (:202), which is touched by C5 (iv), was not assessed. | Added to the S6 check, with 8 (:203). |
| 10 | NOTE | The index already holds unrelated staged paths. A commit without a pathspec would pull them in. | Disclosed in "Does NOT cover" for the master. |
| 11 | NOTE | The marker paste is not "FULL output" word for word, though it is proven lossless. Meeting R3 to the letter needs a separate evidence file, which means a new path in the commit set and the master's approval. | Kept DT1. The alternative is offered to the master; this unit was not allowed to add the file. |

## S6 cross-block check

This unit changes no spec line. The S6 question here is what in the amended specs D-2026-11-08-C C5 (i)–(iv) (DECISIONS.md:1836–1840) will later change. Changing it is the values-spec unit's job, not this unit's:

- (i) A3 break-even basis: values :135 still carries "NEEDS AMEAR (i) of D-2026-11-08-B". C5 (i) says win/loss is judged by price.
- (ii) A4 limit type and stage: values :135, :136, :330 and WF spec :107, :113, :141, :156 carry NEEDS AMEAR (ii) / NEEDS AMEAR 12 (WF spec NEEDS AMEAR 12 itself is at :207). C5 (ii) says Studio Static rows use the stricter type and stage, both shown. Whether that reaches the Rapid rows is an open reading (DECISIONS.md:1886).
- (iii) A8 annualisation: values :133, :311, :326, :349 still say NEEDS AMEAR (iii). C5 (iii) gives mean net P&L per session × 252. U7 did not edit WF spec NEEDS AMEAR 8 (:203, WFE formula).
- (iv) A2 and the notes-4 Sharpe item: values :93, :132, :310, :325 still say NEEDS AMEAR (iv). C5 (iv) says A2 closes it. U7 did not edit WF spec NEEDS AMEAR 7 (:202, Sharpe definition). The "(i)–(iv) stay OPEN" sentences at values :5, :12, :311 change with all four.

The pointers come from the `grep -n -o -E` run on both working-tree specs, pasted in the final evidence block. This unit changed none of them. Each spec keeps its V1 sha256, shown again in the final evidence block.

## Files staged

None. The brief says to stage nothing. The commit set for the master is:

1. `docs/specs/2026-11-06-walk-forward-values.md` (U7, unchanged by this unit)
2. `docs/specs/2026-11-05-walk-forward-spec.md` (U7, unchanged by this unit)
3. `MANIFEST.md`, the whole working-tree file: HEAD's 306 lines plus 7 rows
4. `docs/reports/2026-11-08-wf-spec-amendment-manager.md` (plus one appended line)
5. `docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md`
6. `docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md`
7. `docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md`
8. `docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md` (this report)

`git status --porcelain` for each is in the final evidence block. S7: per C1 there is one audit, and it is the master's to run. Nothing in this set may be committed before that audit passes.

## Does NOT cover

- Whether the U7 specs are right. They were audited before (FAIL 2 was on the stale paste only), and this unit changed no line of them.
- **Stale MANIFEST row numbers in reports this unit may not edit.** U7's own reports cite MANIFEST row numbers that pointed at the U7 rows before the move. After the move, those numbers point at HEAD's rows 299–306 (the C/D-filing rows). The list is in the final evidence block. The brief forbids editing those lines. The master decides whether a later unit corrects them.
- **Staged paths outside this unit.** The index already holds paths that belong to other units (`git status` at session start shows `A`/`M`/`AM` entries in the first column). The commit for diq has to name its commit set explicitly. That is the master's call, and this unit staged nothing.
- The U7 report carries the first three words of the standing sentence 3 times (line numbers in the final evidence block). Its :1 is the sentence. Its :199 is a truncated hunk header inside U7's first spec-diff paste, which its own :521 section had already replaced. The :521 paste that the new SUPERSEDED line names had its hunk-header text stripped by `sed` (:525–527). Its :536 is a grep pattern. That report was audited before, and this unit edits only its appended last line, so this is not graded here.

## Diff of record (supersedes the pasted diff in docs/reports/2026-11-08-wf-spec-amendment-manager.md)

Amear C1 (D-2026-11-08-C, DECISIONS.md:1823–1825): "replace the stale pasted diff with the diff of the blob being committed." Carried out under the master's filing note 2 (DECISIONS.md:1870): appended here as the diff of record; the stale paste in the U7 report is kept and marked SUPERSEDED by one appended line (its last line). Captured by `/tmp/diq-resume/assemble.py` in the same run as the final evidence block below, after every other edit of this unit.

Command: `git diff HEAD -- docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md` (stdout written to `/tmp/diq-resume/diff_of_record.txt`), then `openssl dgst -sha256` of that file:

```
$ openssl dgst -sha256 /tmp/diq-resume/diff_of_record.txt
SHA2-256(/tmp/diq-resume/diff_of_record.txt)= b06ee494396805c3cf0abc19314010347850b854c74a3e8f5a3f0226a6d4369e
```

**Paste rule (decision DT1).** The paste below is the full output, every byte, except: where the standing sentence occurs in the diff, it is replaced by a bracketed marker so that this report carries the sentence once, on line 1 (brief; S13). Markers placed: 2 (diff line 5: first 80 characters (git truncates hunk-header context); diff line 62: full sentence (90 characters)). Rebuilding the raw bytes from this file, with the snippet below, must give the sha256 above; the final evidence block shows it does, and that a live re-run of the diff gives the same digest.

```python
import hashlib, re
t = open("docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md", encoding="utf-8").read()
s = t.split("\n", 1)[0]
f = chr(96) * 3
a = t.index("\n" + f + "diff\n") + len(f) + 6
b = t.index("\n" + f + "\n", a) + 1
p = t[a:b].replace("[[S13 SENTENCE: the full text of line 1 of this report]]", s)
p = re.sub(r"\[\[S13 SENTENCE: first (\d+) characters of line 1 of this report\]\]", lambda m: s[: int(m.group(1))], p)
print("reconstructed diff sha256:", hashlib.sha256(p.encode("utf-8")).hexdigest(), "bytes:", len(p.encode("utf-8")))
```

Run as `cd /Volumes/Sensidine/Praxis.build && python3 -I - <<'EOF'` … `EOF`. Compare the result with `git diff f10603a -- docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md | openssl dgst -sha256` (f10603a = HEAD = origin/main at capture). After the diq commit `<sha>` lands, use `git diff f10603a <sha> -- docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md`.

```diff
diff --git a/docs/specs/2026-11-05-walk-forward-spec.md b/docs/specs/2026-11-05-walk-forward-spec.md
index e46b452..a1dd229 100644
--- a/docs/specs/2026-11-05-walk-forward-spec.md
+++ b/docs/specs/2026-11-05-walk-forward-spec.md
@@ -2,7 +2,7 @@ [[S13 SENTENCE: first 80 characters of line 1 of this report]]
 
 # Walk-forward test specification — NQ Noise-Area, arms (a) and (b)
 
-**Status: DERIVED — not yet ruled on as a whole by Amear.**
+**Status: DERIVED — not yet ruled on as a whole by Amear.** **Changelog.** 2026-11-08, unit `2026-11-08-wf-spec-amendment` (dispatch DECISION_LOG `2026-11-08T16:12:00Z`, WHO: praxis-master): §6 :107, the per-tier table header :113 and the §8 gate line :156 carry A4's 80% buffer (D-2026-11-08-B, DECISIONS.md:1735–1740). The quotes at :31 and :39 are unchanged and carry a pointer at :28. Lines were edited in place; no line was added or removed.
 Derived 2026-11-05 by praxis-worker, unit `2026-11-05-r8j-phase3-import-and-wf-spec` (bead `Praxis_build-r8j`), under Amear's typed item b (quoted in §1). No design choice is added here. Anything the rulings do not fix is a numbered question in **NEEDS AMEAR** at the end, not a default.
 
 **Sources (every pointer below was taken from `grep -n` / `nl -ba` output in this session):**
@@ -25,7 +25,7 @@ Derived 2026-11-05 by praxis-worker, unit `2026-11-05-r8j-phase3-import-and-wf-s
 
 ## 1. Rulings this spec rests on (verbatim)
 
-**D-2026-11-05-A, the five items** — REPORTED BY the voice agent, pasted by Amear with "file as WHO: amear" (`DECISIONS.md:806`, `:811`); entry Status "RULED by Amear — items 1–5" (`:806`). Quoted from `:812-816`:
+**D-2026-11-05-A, the five items** — REPORTED BY the voice agent, pasted by Amear with "file as WHO: amear" (`DECISIONS.md:806`, `:811`); entry Status "RULED by Amear — items 1–5" (`:806`). Item 3 (:31) and typed item b's "DD gate = lower of 4% …" (:39) are quoted history and stay as written; the Max-DD gate in force is A4's (D-2026-11-08-B, DECISIONS.md:1735–1740), which amends item 3 (his words: "This amends D-2026-11-05-A item 3"); that it also supersedes typed item b's restatement is the editor's reading, not his words, changeable by Amear; see §6 and §8. Quoted from `:812-816`:
 - *"1. Walk-forward runs BOTH ways: (a) paper's fixed rules, nothing optimised; (b) four parameters tuned per window — lookback, noise multiplier, stop-ATR multiplier, exit policy. A stop is added to the strategy for (b) on its own branch; baseline file unchanged."*
 - *"2. Windows per spec: 252-day in-sample / 63-day out-of-sample / 63-day step."*
 - *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used."*
@@ -104,13 +104,13 @@ R-VN4-7's reading says report C's PROPOSED checklist is not adopted. This spec d
 
 ## 6. Max-drawdown gate — base and per-tier table
 
-- Original Block 2 gate wording: "Max drawdown ≤ 4% of equity" (Phase 3 spec `:82`). Item 3 rules its base: "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used." (`:814`). — RULED (D-2026-11-05-A).
+- Original Block 2 gate wording: "Max drawdown ≤ 4% of equity" (Phase 3 spec `:82`). Item 3 rules its base: "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used." (`:814`). — RULED (D-2026-11-05-A). **Amended by A4** (D-2026-11-08-B, DECISIONS.md:1735–1740, joined): "Max-DD gate = backtest max drawdown must stay below 80% of the ruled limit, i.e. below the lower of 3.2% of the MFFU account size and 80% of MFFU's trailing drawdown limit. This amends D-2026-11-05-A item 3 with a safety buffer for model error. Evaluated against every tier row; tier pick stays Q9. Closes the notes-4 DD equity-base item." (OPEN, Q9) The gate in force is A4's. The limit type and stage for the Studio Static rows and for rows whose Eval and Sim-Funded types differ are NEEDS AMEAR (ii) of D-2026-11-08-B (cf. this file's NEEDS AMEAR 12).
 - Item 5 defers the tier: "Account tier: no decision until backtest + paper results exist." (`:816`). — RULED (D-2026-11-05-A). **This spec does not choose a tier.** The table lists every tier read from MFFU's pages. → NEEDS AMEAR 11–12.
 - The imported spec's breaker list carries the figure "MFFU’s $1,500 EOD trailing drawdown" (Phase 3 spec `:102`). D-2026-11-05-A does not adopt it (`DECISIONS.md:820`). The only $1,500 limit on the pages read is Builder 50K with add-on (row below). → NEEDS AMEAR 20.
 
 **Per-tier table.** "Lower" = min(0.04 × size, MFFU limit). Arithmetic is INFERRED (deriver's arithmetic). Size and limit are REPORTED BY MFFU's page named in each row, fetched 2026-11-05 (UTC window 23:58:43Z–00:00:28Z). In the capture, the stage labels on `/plans/*` tables were INFERRED from tab order.
 
-| Plan · size | Account size | 4% of size | MFFU limit (type, stage) | Lower of the two | Grade / source |
+| Plan · size | Account size | 4% of size | MFFU limit (type, stage) | Lower of the two (item 3's ruled limit, arithmetic INFERRED as stated at :111; A4 gate: max DD below 80% of this, D-2026-11-08-B; Static rows and rows whose Eval and Sim-Funded types differ: NEEDS AMEAR (ii)) | Grade / source |
 |---|---|---|---|---|---|
 | Studio #003 · 5K | $5,000 | 0.04 × 5,000 = $200 | $250 (Static, not trailing) | min(200, 250) = **$200** | REPORTED BY MFFU's page https://help.myfundedfutures.com/en/articles/17589665-studio-plans-a-comprehensive-guide, fetched 2026-11-05 |
 | Studio #001 · 10K | $10,000 | $400 | $500 (Static) | min(400, 500) = **$400** | REPORTED BY MFFU's page https://help.myfundedfutures.com/en/articles/17589665-studio-plans-a-comprehensive-guide, fetched 2026-11-05 |
@@ -153,7 +153,7 @@ Also: Studio limits are Static, not trailing. Item 3 says "trailing drawdown lim
 Block 2, "Pass gates (non-negotiable):" (Phase 3 spec `:78`), lines `:80-85` — REPORTED BY the imported Phase 3 spec:
 - OOS profit factor ≥ 1.30
 - OOS Sharpe ≥ 1.0
-- Max drawdown ≤ 4% of equity
+- Max drawdown ≤ 4% of equity — as imported (Phase 3 spec `:82`). Gate in force: A4 (D-2026-11-08-B): "backtest max drawdown must stay below 80% of the ruled limit, i.e. below the lower of 3.2% of the MFFU account size and 80% of MFFU's trailing drawdown limit" (§6 :107). Limit type and stage for the Studio Static rows and for rows whose Eval and Sim-Funded types differ: NEEDS AMEAR (ii) of D-2026-11-08-B.
 - ≥ 250 aggregate OOS trades
 - ≥ 60% of walk-forward windows profitable
 - Walk-forward efficiency ≥ 0.50
diff --git a/docs/specs/2026-11-06-walk-forward-values.md b/docs/specs/2026-11-06-walk-forward-values.md
index af6a4b2..bfc235f 100644
--- a/docs/specs/2026-11-06-walk-forward-values.md
+++ b/docs/specs/2026-11-06-walk-forward-values.md
@@ -1,15 +1,15 @@
-# Walk-forward values and arm (b) code design — version 2.1 (RULED / SETTLED / OPEN)
+# Walk-forward values and arm (b) code design — version 2.2 (RULED / SETTLED / OPEN)
 
-**Status: version 2.1 (2026-11-07).** Unit `2026-11-07-wf-values-fresh`; dispatch: DECISION_LOG row `[2026-11-07T14:06:00Z] WHO: praxis-master`. Supersedes version 1 (unit 2026-11-06-wf-values, parked FAIL 2, DECISION_LOG 2026-11-07T00:00:00Z). Version 1 is preserved verbatim in `docs/reports/2026-11-07-wf-values-fresh-manager.md` Appendix A, sha256 `985e3c43cc4f29cd32cf64b40e0fb16379ab9295b1be7bd8b1535a535784d75d`. Governing DECISIONS entry: D-2026-11-07-B (being written by this unit).
+**Status: version 2.2 (2026-11-08).** (v2.2 changes: unit `2026-11-08-wf-spec-amendment`, changelog :5.) Version 2 by Unit `2026-11-07-wf-values-fresh`; dispatch: DECISION_LOG row `[2026-11-07T14:06:00Z] WHO: praxis-master`. Supersedes version 1 (unit 2026-11-06-wf-values, parked FAIL 2, DECISION_LOG 2026-11-07T00:00:00Z). Version 1 is preserved verbatim in `docs/reports/2026-11-07-wf-values-fresh-manager.md` Appendix A, sha256 `985e3c43cc4f29cd32cf64b40e0fb16379ab9295b1be7bd8b1535a535784d75d`. Governing DECISIONS entry: D-2026-11-07-B (being written by this unit).
 Version 1 was written 2026-11-06 by praxis-manager, unit `2026-11-06-wf-values` (dispatch `[2026-11-06T23:01:17Z] WHO: praxis-master`). Version 2 was written 2026-11-07 (`date -u` 14:12:35Z at the start) under Amear's rulings in DECISIONS.md D-2026-11-07-A (his words: the fenced block, DECISIONS.md:1213–1237). It fills in `docs/specs/2026-11-05-walk-forward-spec.md` (the "WF spec", sha256 `b4341724134b0af1c2b268c7c38952f7f75cc801d84c72c61aad5ec0020d8645`, OBSERVED this unit). No code is written or changed by this file. No NT8 run, import or purchase is authorised or made.
-**Changelog.** Version 2.1, 2026-11-07, unit `2026-11-07-arm-b-spec-addendum` (dispatch DECISION_LOG `2026-11-07T16:45:00Z`, WHO: praxis-master), recorded in D-2026-11-07-B addendum 1 (master's decision under delegation, R-1104-2, DECISIONS.md:748; DECISION_LOG `2026-11-07T16:45:00Z`, WHO: praxis-master; not Amear's word; changeable by him): §4 Precedence and T8's matching sentence (step (1) pre-empts step (2) only; the early-close checkpoint follows the committed base); §5 Warm-up and T11 (the band first exists one session later than version 2 said); a new §9 subsection, "Oracle inputs from the code unit (2026-11-07)". No other value changed.
+**Changelog.** Version 2.1, 2026-11-07, unit `2026-11-07-arm-b-spec-addendum` (dispatch DECISION_LOG `2026-11-07T16:45:00Z`, WHO: praxis-master), recorded in D-2026-11-07-B addendum 1 (master's decision under delegation, R-1104-2, DECISIONS.md:748; DECISION_LOG `2026-11-07T16:45:00Z`, WHO: praxis-master; not Amear's word; changeable by him): §4 Precedence and T8's matching sentence (step (1) pre-empts step (2) only; the early-close checkpoint follows the committed base); §5 Warm-up and T11 (the band first exists one session later than version 2 said); a new §9 subsection, "Oracle inputs from the code unit (2026-11-07)". No other value changed. Version 2.2, 2026-11-08, unit `2026-11-08-wf-spec-amendment` (dispatch DECISION_LOG `2026-11-08T16:12:00Z`, WHO: praxis-master), under Amear's rulings D-2026-11-08-A R1–R3 (DECISIONS.md:1545–1612, committed `19ae6c8`) and D-2026-11-08-B A1–A8 (DECISIONS.md:1721–1762, committed `a2f1067`): §4 and T12(iii) session hours (R1, re-run clause CONDITIONAL); §6 gate 2 (A2) and trading day (A5, first half; second half OPEN); §8 gate sets (A7), judged arm (R2), WFE formula (A8), Max-DD buffer (A4), win rate (A3), O1 state; status cells in lists (C) and (D). D-2026-11-08-B NEEDS AMEAR (i)–(iv) stay OPEN. Lines were edited in place; no line was added or removed.
 
 Standing limitation: [[S13 SENTENCE: the full text of line 1 of this report]]
 
 **Grades used.** Every value in §2–§9 carries exactly one.
 - **RULED** — Amear's words, quoted byte for byte, with a pointer: D-2026-11-07-A ruling 4 Qn (DECISIONS.md:1220–1228) or ruling 9 (:1233); D-2026-11-06-B ruling 4 or ruling 2 ("ruling 4 of 2026-11-06", paste at DECISIONS.md:1063); ruling 1 of 2026-11-05 (DECISION_LOG `2026-11-05T23:50:09Z`, WHO: amear); D-2026-11-05-A items 1–5 (DECISIONS.md:812–816; the voice agent's record, filed as WHO: amear).
 - **SETTLED** — a settlement under R-1104-2 (DECISIONS.md:748), delegated by Q10: "settle under R-1104-2, strictest reasonable choice". The stop values and the `StopAtrMult = 0` input rule were settled by the master in D-2026-11-07-A (:1262). Every other settlement is made by this unit on the master's dispatch and recorded in D-2026-11-07-B. Not Amear's word. Each SETTLED item names its alternative and is changeable by him. **Reach of Q10** — INFERRED (the master's reading, DECISION_LOG `2026-11-07T14:06:00Z`, which settles "for every value that was PROPOSED and for Q10's open items — EXCEPT the items ruling 9 keeps open"): version 1's NEEDS AMEAR question 10 was `**The WF spec's 29 items, mapped.**` (version 1 :146, preserved in the unit report's Appendix A). So Q10 also hands over the WF spec's 29 items, except ruling 9's items and the tier pick (Q9). Not Amear's word.
-- **OPEN** — not decided here: ruling 9's notes-4 items (the O1 gate set among them) and the tier pick (Q9). Nothing else is open (list C).
+- **OPEN** — not decided here: ruling 9's notes-4 items (the O1 gate set among them) and the tier pick (Q9). Nothing else is open (list C). Version 2.2 (2026-11-08): the O1 gate set is now RULED (R2, R3, D-2026-11-08-A; A7, A8, D-2026-11-08-B; §8), and O1 is discharged (A8); OPEN now: D-2026-11-08-B NEEDS AMEAR (i)–(iv), A5's second half (§6 :93) and the tier pick (Q9). The sentence before this one is kept as written for version 2.1.
 - **OBSERVED** (command output; version 1's unit report `docs/reports/2026-11-06-wf-values-manager.md`, or this unit) · **REPORTED BY <who>** · **INFERRED** · **UNVERIFIED**.
 
 ## 0. Authority
@@ -69,7 +69,7 @@ So two of the four tunables have a paper value (14; 1.0). **The stop-ATR multipl
 RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by market order next bar" and "Not a resting stop in the backtest."
 
 - **ATR(14) series** — RULED (Q6: "Q6 ATR(14) = 14 completed RTH sessions (daily ATR).").
-- **ATR computation** — SETTLED: the simple mean of the true ranges of the last 14 completed RTH sessions, TR = max(session high, prior session close) − min(session low, prior session close). It is computed inside the strategy from the 1-minute bars, in the same no-look-ahead store as the band (`PraxisNoiseAreaBreakout.cs:61-95`). No second data series is added. Alternative: a second, daily data series with NT8's own `ATR(14)` on it. Changeable by him.
+- **ATR computation** — SETTLED: the simple mean of the true ranges of the last 14 completed RTH sessions, TR = max(session high, prior session close) − min(session low, prior session close). It is computed inside the strategy from the 1-minute bars, in the same no-look-ahead store as the band (`PraxisNoiseAreaBreakout.cs:61-95`). No second data series is added. Alternative: a second, daily data series with NT8's own `ATR(14)` on it. Changeable by him. **RTH session hours** — RULED (R1, D-2026-11-08-A, DECISIONS.md:1551–1552, joined): "RTH = 09:30–16:00 ET" and "Arms (a) and (b) anchor at the 09:30 ET cash open." This file states R1's hours; nothing here implements or tests them (the code, the oracle's session start and the VM template are not changed here; see evidence (2)). **Baseline re-run — CONDITIONAL** (bd memory `amear-conditional-commitment`: an assumption about an unobserved mechanism is committed as CONDITIONAL with a void clause). R1 (D-2026-11-08-A, DECISIONS.md:1552–1555, joined): "VM step 0 reads the live "CME US Index Futures RTH" template hours (T7 readback). If the live template starts 08:30 ET, the 2026-11-01 baselines are suspect and are re-run at 09:30 ET before either arm counts." The trigger is the VM step-0 T7 readback that R1 names, which has not been run. That readback of the template hours is not yet written into any procedure: HANDOFF.md:17 says "It is not yet in the VM handoff text", and this file's T7 (:193) reads back other settings (commission template, backtest type, fill resolution, slippage), not template hours. Assumption, unobserved: the live template's start time. Voiding observation: that readback; if it shows an 08:30 ET start, R1's re-run applies before either arm counts. R1's words name the 08:30 ET case only; a readback showing any other start is not covered by them and is his to decide. **Evidence so far, graded:** (1) the rescued template copy, REPORTED BY that worker (`docs/reports/2026-10-31-o78-worker4-report-adversarial.md:208–219` at commit `29c3e13`, W4-E6): the "CME US Index Futures RTH" Sessions list reads Monday–Friday '830'–'1600', with TimeZone ['Eastern Standard Time']; (2) oracle finding B1, REPORTED BY `docs/reports/2026-11-07-wf-oracles-manager.md` (E5, heading at :207; finding at :345): the committed NT8 base runs fit sessions starting at the 08:31 bar, not 09:31; (3) the live template's hours: UNVERIFIED.
 - **Level** (WF spec NEEDS AMEAR 27) — SETTLED: fixed at entry. Long: entry fill price − m × ATR(14); short: entry fill price + m × ATR(14), where m = `StopAtrMult` (§3), never the noise multiplier k. ATR is the value at the entry bar. Not trailing. A reversal starts a new level from the new entry. Alternative: measured from the signal bar's close, or a trailing level. Changeable by him.
 - **Evaluation** — SETTLED: on the close of **every** 1-minute bar while in a position, not only at checkpoints. Long: `Close <= level`; short: `Close >= level`. Then `ExitLong`/`ExitShort` (market), which fills on the next bar. No stop order is placed. Alternative: evaluate only at the HH:00/HH:30 checkpoints. Changeable by him.
 - **ATR warm-up** — SETTLED: ATR(14) needs 15 completed sessions (14 true ranges and one prior close). No entry is taken until it exists. This applies to all 81 grid configurations. With the input `StopAtrMult = 0` (T1–T3 only), entries start when the band exists, as in the base. Alternative: entries before ATR exists, with no stop until it does. Changeable by him.
@@ -90,7 +90,7 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
 
 - Objective class — RULED (ruling 4 of 2026-11-06: "in-sample objective = risk-adjusted return with a minimum trade count, never net profit").
 - **Statistic** — SETTLED, **as the in-sample selection objective only**: annualised Sharpe of daily net P&L. For the in-sample sessions i = 1…n: d_i = sum of the net P&L (after commission and slippage) of trades exited in session i, 0 if none. S = mean(d) / sd(d) × √252, sd with n − 1, risk-free rate 0. Reason: it penalises variance; the policies trade at different rates, so daily is fairer than per-trade; dollar P&L at 1 NQ needs no equity base. Alternatives: Sharpe of per-trade returns; Sortino (downside deviation); MAR = CAGR / max drawdown. Changeable by him.
-- **This statistic does NOT define the gate "OOS Sharpe ≥ 1.0".** The gate's Sharpe definition and its equity base stay OPEN under ruling 9: "Notes-4 unruled items stay open; none block anything." They are notes-4 items (D-2026-11-06-B item 18, DECISIONS.md:1101; REPORTED BY `docs/reports/2026-11-07-return-handoff-claude-ai.md:74`; WF spec NEEDS AMEAR 7). The notes-4 source scope, DECISIONS.md:978: "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)" — so the open equity-base item names the 4% DD gate too (list (C)).
+- **Gate 2 "OOS Sharpe ≥ 1.0"** — RULED (A2, D-2026-11-08-B, DECISIONS.md:1726–1729, joined): "Gate 2 "OOS Sharpe >= 1.0" = the §6 formula on out-of-sample sessions: daily net P&L after commission and slippage, 0 on no-trade sessions, sqrt(252), sd n-1, risk-free 0. Fixed base, no compounding; tier pick not needed for this gate." A1 (D-2026-11-08-B, DECISIONS.md:1724): "R4 applies to gate 2 only." Whether A2 also closes the notes-4 item "Sharpe definition (item 4)" (DECISIONS.md:978) is NOT decided here; it is NEEDS AMEAR (iv) of D-2026-11-08-B. **Trading day (arms (a)/(b))** — RULED (A5, first half, D-2026-11-08-B, DECISIONS.md:1741–1742, joined): "For arms (a)/(b), "trading day" = session i of §6 (09:30-16:00 ET per R1)." The second half, for R6 evening-entry research (DECISIONS.md:1742–1743, joined): "For R6 evening-entry research, "trading day" = MFFU's own definition from its current terms." It waits on a later read of MFFU's current terms (master's reading, D-2026-11-08-B filing note 5, changeable by Amear), and nothing is assumed about that definition here. A5's second half: OPEN (waits on a read of MFFU's current terms). was: "**This statistic does NOT define the gate "OOS Sharpe ≥ 1.0".** The gate's Sharpe definition and its equity base stay OPEN under ruling 9: "Notes-4 unruled items stay open; none block anything." They are notes-4 items (D-2026-11-06-B item 18, DECISIONS.md:1101; REPORTED BY `docs/reports/2026-11-07-return-handoff-claude-ai.md:74`; WF spec NEEDS AMEAR 7). The notes-4 source scope, DECISIONS.md:978: "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)" — so the open equity-base item names the 4% DD gate too (list (C))."
 - **Minimum trade count** — SETTLED: 100 trades per 252-session in-sample window. Reason: the baseline's 1,190 trades over 1,352 sessions is about 221.8 per 252 sessions; the committed OppBand run's 810 is about 151.0 (OBSERVED arithmetic, version 1's unit report). 100 is about 45% and 66% of those, so a normal configuration clears it and a rarely-trading one cannot win. A configuration below 100 is ineligible in that window. Alternative: 150 per window. Changeable by him.
 - **Undefined statistic** — SETTLED: a configuration whose daily P&L has zero standard deviation is ineligible. Alternative: score it S = 0. Changeable by him. Eligibility applies to selection only; the ranking in §7 uses all 81.
 - **No eligible configuration** — SETTLED: arm (b) trades nothing in that out-of-sample window, and the window counts as not profitable. Alternative: carry the previous window's configuration forward. Changeable by him.
@@ -118,21 +118,21 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
 
 ## 8. What "counts" means — both arms
 
-- **Gates** — RULED (Q8: "Q8 both arms are judged against all six Phase 3 gates; arm (b) must also pass PBO < 0.05."). The six gates (REPORTED BY `docs/specs/2026-11-05-phase3-build-specification.md:80-85`, under "Pass gates (non-negotiable):" at `:78`):
+- **Gates** — RULED (A7, D-2026-11-08-B, amending Q8; DECISIONS.md:1746–1747, joined): "R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not applicable). Arm (b) on gates 1-6 plus PBO < 0.05." R3 (D-2026-11-08-A, DECISIONS.md:1558): "Gate 6 (WFE) applies to arm (b) only". was: Q8: "Q8 both arms are judged against all six Phase 3 gates; arm (b) must also pass PBO < 0.05.". The six gates (REPORTED BY `docs/specs/2026-11-05-phase3-build-specification.md:80-85`, under "Pass gates (non-negotiable):" at `:78`):
   1. OOS profit factor ≥ 1.30
   2. OOS Sharpe ≥ 1.0
   3. Max drawdown ≤ 4% of equity
   4. ≥ 250 aggregate OOS trades
   5. ≥ 60% of walk-forward windows profitable
   6. Walk-forward efficiency ≥ 0.50
-- **Judged arm = (a)** — RULED (ruling 4 of 2026-11-06: "judged arm = (a) fixed rules"). Q8 says "both arms are judged against all six Phase 3 gates". Both are his words. This file does not reconcile them.
+- **Judged arm = (a)** — RULED (ruling 4 of 2026-11-06: "judged arm = (a) fixed rules"). Q8 says "both arms are judged against all six Phase 3 gates". Both are his words. This file does not reconcile them. R2 (D-2026-11-08-A, DECISIONS.md:1556–1557, joined): "GO requires arm (a) to pass. Arm (b) can only add confidence or block a GO; it can never carry a GO on its own". A7 (D-2026-11-08-B, DECISIONS.md:1746): "R3 amends Q8". His words do not name the tension recorded on this line. That R2 and A7 together resolve this tension (both arms graded against their own gate sets; GO rests on arm (a) alone, arm (b) only as confidence or veto) is the master's reading, DECISION_LOG 2026-11-08T17:01:00Z (WHO: praxis-master), not his words, changeable by Amear.
 - **PBO ≥ 0.05** — RULED (ruling 4 of 2026-11-06: "arm (b) counts only if it also passes PBO < 0.05"): arm (b) is reported as "does not count". Arm (b) is always run and reported next to arm (a), with its PBO — SETTLED (alternative: run arm (b) only after arm (a) passes; changeable by him).
 - **What his words cover of O1** (`specs/SPEC_RUBRIC.md:74`, "a written statement of which gate set applies to the replication arm and whether GO/HOLD/REJECT sits on the replication arm or the later optimisation arm"):
   - His statements, recorded verbatim (RULED as words): which gates apply to each arm — all six to both, plus PBO < 0.05 for arm (b) (Q8); which arm is judged — (a) (ruling 4 of 2026-11-06). Whether they discharge O1 is not decided here (below).
-  - Not covered, OPEN, not resolved here: (i) the equity base and the Sharpe definition of the "OOS Sharpe ≥ 1.0" gate — ruling 9 (notes-4; WF spec NEEDS AMEAR 7); the notes-4 source (DECISIONS.md:978) scopes the equity base as "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)" (list (C)); (ii) whether "Walk-forward efficiency ≥ 0.50" applies to arm (a), which has no optimisation (WF spec NEEDS AMEAR 8) — Q8's words name all six gates for both arms but do not say how WFE is computed with no in-sample step; it is on ruling 9's open list under the label the O1 gate set (label REPORTED BY the return handoff :74); (iii) whether GO / HOLD / REJECT may rest on arm (b) — ruling 9; the O1 gate set, REPORTED BY the return handoff :74 (WF spec NEEDS AMEAR 9).
-  - The WFE formula for arm (b) (WF spec NEEDS AMEAR 8, second half) — OPEN (ruling 9; the O1 gate set, REPORTED BY the return handoff :74): a WFE formula is part of the gate set. Not resolved here.
-  - Whether Q8 discharges O1 is left to the master and the auditor. This file does not resolve O1.
-- **Max-DD gate base** — RULED (D-2026-11-05-A item 3, DECISIONS.md:814: "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit."). It stands as written. Whether it closes the notes-4 item "equity base for the 4% DD gate (item 5)" (DECISIONS.md:978) is NOT decided here; that item stays OPEN (ruling 9; list (C)).
+  - Status after D-2026-11-08-A and D-2026-11-08-B: (i) gate 2's definition — RULED (A2, D-2026-11-08-B; §6 :93); the notes-4 DD equity-base item — closed by A4 (D-2026-11-08-B), in his words "Closes the notes-4 DD equity-base item."; the notes-4 Sharpe-definition item (item 4) — NEEDS AMEAR (iv) of D-2026-11-08-B; (ii) R3 (D-2026-11-08-A, DECISIONS.md:1558): "Gate 6 (WFE) applies to arm (b) only"; A7 (D-2026-11-08-B, DECISIONS.md:1746–1747, joined): "arm (a) is judged on gates 1-5 (WFE not applicable)"; (iii) R2 (D-2026-11-08-A, DECISIONS.md:1556–1557, joined): "GO requires arm (a) to pass. Arm (b) can only add confidence or block a GO; it can never carry a GO on its own"; R2 does not name HOLD or REJECT; A8 (D-2026-11-08-B, DECISIONS.md:1748): "O1 is discharged by R2 + R3 + A7.". was: "Not covered, OPEN, not resolved here: (i) the equity base and the Sharpe definition of the "OOS Sharpe ≥ 1.0" gate — ruling 9 (notes-4; WF spec NEEDS AMEAR 7); the notes-4 source (DECISIONS.md:978) scopes the equity base as "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)" (list (C)); (ii) whether "Walk-forward efficiency ≥ 0.50" applies to arm (a), which has no optimisation (WF spec NEEDS AMEAR 8) — Q8's words name all six gates for both arms but do not say how WFE is computed with no in-sample step; it is on ruling 9's open list under the label the O1 gate set (label REPORTED BY the return handoff :74); (iii) whether GO / HOLD / REJECT may rest on arm (b) — ruling 9; the O1 gate set, REPORTED BY the return handoff :74 (WF spec NEEDS AMEAR 9)."
+  - The WFE formula for arm (b) (WF spec NEEDS AMEAR 8, second half) — RULED (A8, D-2026-11-08-B, DECISIONS.md:1748–1750, joined): "Gate 6 formula (Pardo WFE): annualised OOS net profit / annualised IS net profit of the selected parameter set, pooled across all windows; pass >= 0.50." A8 names no annualisation method; that stays OPEN, NEEDS AMEAR (iii) of D-2026-11-08-B. No method is picked here. was: "OPEN (ruling 9; the O1 gate set, REPORTED BY the return handoff :74): a WFE formula is part of the gate set. Not resolved here."
+  - O1 — discharged (A8, D-2026-11-08-B, DECISIONS.md:1748): "O1 is discharged by R2 + R3 + A7." The rubric marks it `PASSED@a2f1067` (`specs/SPEC_RUBRIC.md:77`, committed `6c4c109`); the PASSED marking and the sha are the master's reading (D-2026-11-08-B filing note 3), changeable by Amear. was: "Whether Q8 discharges O1 is left to the master and the auditor. This file does not resolve O1."
+- **Max-DD gate base** — RULED (A4, D-2026-11-08-B, DECISIONS.md:1735–1740, joined): "Max-DD gate = backtest max drawdown must stay below 80% of the ruled limit, i.e. below the lower of 3.2% of the MFFU account size and 80% of MFFU's trailing drawdown limit. This amends D-2026-11-05-A item 3 with a safety buffer for model error. Evaluated against every tier row; tier pick stays Q9. Closes the notes-4 DD equity-base item." In his words, it amends D-2026-11-05-A item 3 ("This amends D-2026-11-05-A item 3 with a safety buffer for model error.") and closes the notes-4 DD equity-base item ("Closes the notes-4 DD equity-base item."). Tier pick stays Q9 (OPEN, Q9) (his words "tier pick stays Q9"). OPEN: which limit type and stage A4 means for the Studio Static rows, and for rows whose Eval and Sim-Funded limit types differ — NEEDS AMEAR (ii) of D-2026-11-08-B. was: "RULED (D-2026-11-05-A item 3, DECISIONS.md:814: "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit."). It stands as written. Whether it closes the notes-4 item "equity base for the 4% DD gate (item 5)" (DECISIONS.md:978) is NOT decided here; that item stays OPEN (ruling 9; list (C))." **Win rate** — RULED (A3, D-2026-11-08-B, DECISIONS.md:1730–1734, joined): "Win rate is not a Block 2 pass gate. Per trade: W / (W + L + 0.5 x B), B = trade exited at its entry price. No-trade sessions excluded. It is the quantity for O4's Block 4 "within +/-15% win rate" check, computed identically on backtest and paper." Label (the editor's, from A3's words, changeable by Amear): not a Block 2 pass gate; the quantity for O4's Block 4 "within +/-15% win rate" check. Whether W and L are classified by price or by net P&L after commission and slippage: OPEN, NEEDS AMEAR (i) of D-2026-11-08-B.
 - **Per-tier reporting** — RULED (D-2026-11-05-A item 4, :815: "Every window also reports worst drawdown at 1 MNQ and 1 NQ against each MFFU tier's limit."; item 5, :816: "Account tier: no decision until backtest + paper results exist."). The results report gives per-window worst drawdown at 1 MNQ and 1 NQ against EVERY row of the WF spec §6 per-tier table (`docs/specs/2026-11-05-walk-forward-spec.md:105-141`). **Reporting rule** (WF spec NEEDS AMEAR 12, 13) — SETTLED: every row of that table is reported, the Studio Static rows and the Builder 50K add-on row included. Where MFFU's pages contradict each other, both figures are shown and the lower is used as that row's limit. Which tier, plan stage or limit type counts stays OPEN (Q9). Alternative: report the trailing-limit rows only, one figure per row. Changeable by him. **The Phase 3 spec's $1,500** (WF spec NEEDS AMEAR 20) — SETTLED for walk-forward use only: not used as a gate figure. The per-tier table governs; $1,500 appears only as the Builder 50K add-on row. No breaker limit is set here. The figure is also breaker #6's threshold in the imported spec's breaker list (Phase 3 spec `:102`; WF spec `:109`); whether it stands there is not decided here (breaker build; O4). Alternative: adopt $1,500 as the gate figure. Changeable by him.
 - **No tier chosen** — RULED (Q9: "Q9 no tier chosen. Report the per-tier table; I pick after paper results."). **The tier pick is OPEN** — his, after paper results.
 - MNQ round-turn cost — RULED (ruling 2 of 2026-11-06: "MNQ $1.90").
@@ -203,7 +203,7 @@ RULED (ruling 1 of 2026-11-05, quoted in §0): "evaluated on bar close, exit by
   - T12 (ExitPolicy under the stop, the test whose absence parked version 1). Runs: T12a = T4's run (14, 1.0, 1.5, BandOrVWAP), T12b = T5d's run (14, 1.0, 1.5, OppBand), T12c (14, 1.0, 1.5, Flat1559). **Exit names separate Flat1559 from the other two, but not BandOrVWAP from OppBand.** Both name their checkpoint exits `XL`/`XS` and both flatten at 16:00 by `Exit on session close`, so only the level oracle (iii) tells them apart. **OppBand reverses.** At a checkpoint, a long exits on `price <= curLower` (`_OppBand.cs:233-235`), and the same bar's entry code goes short on `price < curLower` (`:254-255`). So an OppBand checkpoint exit is a stop-and-reverse unless the close equals the band exactly (the short side mirrors this: `:241-243`, `:252-253`). In the committed OppBand run, XL 10 and XS 8 sit next to 18 same-timestamp exit → entry pairs (results report `:132`, `:138`, OBSERVED there). That the 18 pairs are those 18 exits is INFERRED; the report does not pair them. Under BandOrVWAP and Flat1559 the same reversal happens whenever the close goes through the opposite band, because that close also meets their trail (`PraxisNoiseAreaBreakout.cs:208-211`, `:226-229`). Pass requires all of the following.
     - (i) T12a, T12b and T12c differ pairwise: each pair has at least one trade row that differs (entry or exit time, price, side or exit name).
     - (ii) Names. An `XL` closes a long and an `XS` a short. In T12a and T12b every exit is `XL`, `XS`, `XStop` or `Exit on session close`, and none is `FlatEOD`. In T12c every trade open at the close of a 15:59-stamped bar exits `FlatEOD` on the 16:00 bar (decided at `mod >= FlattenMod`, `_Flat1559.cs:91`, `:227`), by T8's calibrated `FlatEOD` fill rule. No T12c `Exit on session close` falls on a 16:00 bar; one appears only on an early-close day's last bar. Each of the three runs has at least one `XL` or `XS`.
-    - (iii) Policy-rule oracle, for non-stop exits. For each trade, the script walks the checkpoints after the entry's decision checkpoint, up to and including the exit decision bar d (T8's definition). A checkpoint here is HH:00/HH:30, inside RTH, and not a session-flat bar F. The script finds the first checkpoint c* at which the policy's exit condition holds, recomputing the band at the run's Lookback and k and the session's typical-price VWAP from the 09:30 bar (`PraxisNoiseAreaBreakout.cs:171-176`, `:265`) from the data file. BandOrVWAP and Flat1559: long Close ≤ max(UpperBound, VWAP), short Close ≥ min(LowerBound, VWAP); the band alone while the session's volume is 0 (`:208-219`). OppBand: long Close ≤ LowerBound, short Close ≥ UpperBound (`_OppBand.cs:232-243`). Pass: an `XL`/`XS` exit has c* = d. An `XStop` or session-flat exit has no c* before d; at d the flat and the stop come first (§4 precedence), so the policy's exit is not checked on that bar.
+    - (iii) Policy-rule oracle, for non-stop exits. For each trade, the script walks the checkpoints after the entry's decision checkpoint, up to and including the exit decision bar d (T8's definition). A checkpoint here is HH:00/HH:30, inside RTH, and not a session-flat bar F. The script finds the first checkpoint c* at which the policy's exit condition holds, recomputing the band at the run's Lookback and k and the session's typical-price VWAP from the 09:30 bar (the 09:30 ET cash open anchor is R1's, D-2026-11-08-A; R1 names no bar stamp (the stamp convention is §5 :83; finding B1, §4); specified here, not implemented or tested (§4); the baseline re-run is CONDITIONAL, see §4 RTH session hours) (`PraxisNoiseAreaBreakout.cs:171-176`, `:265`) from the data file. BandOrVWAP and Flat1559: long Close ≤ max(UpperBound, VWAP), short Close ≥ min(LowerBound, VWAP); the band alone while the session's volume is 0 (`:208-219`). OppBand: long Close ≤ LowerBound, short Close ≥ UpperBound (`_OppBand.cs:232-243`). Pass: an `XL`/`XS` exit has c* = d. An `XStop` or session-flat exit has no c* before d; at d the flat and the stop come first (§4 precedence), so the policy's exit is not checked on that bar.
     - (iv) Reversal. At an `XL` whose decision close is below LowerBound (an `XS`: above UpperBound), the next trade is the opposite side and its entry fills on the exit's fill bar. At an `XL`/`XS` whose close does not pass the opposite band, the next entry fills on a later bar.
     - (v) Entry soundness. Each entry's decision bar (the bar before its fill) is a checkpoint in a session at or after s16 where Close > UpperBound (long) or < LowerBound (short). It is not an `XStop` decision bar (T10).
     - (vi) Ties. A check where |Close − level| ≤ 1e-9 × level is listed and not graded, and the count is printed. The band and VWAP are floating-point; the script uses the code's operation order.
@@ -307,8 +307,8 @@ Questions only. Nothing below is answered here.
 2. **Ruling 9's open notes-4 items** ("Notes-4 unruled items stay open; none block anything."; list REPORTED BY `docs/reports/2026-11-07-return-handoff-claude-ai.md:74`):
    - a second Rithmic read-only connection;
    - the CME wiki as a source;
-   - the equity base and the Sharpe definition: the notes-4 source (DECISIONS.md:978) scopes it as "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)"; the WF spec (NEEDS AMEAR 7) and this file read it for the "OOS Sharpe ≥ 1.0" gate. D-2026-11-05-A item 3's DD-base ruling (§8) stands as written; whether it closes the notes-4 DD-gate item is NOT decided here;
-   - the O1 gate set: whether WFE ≥ 0.50 applies to arm (a), the WFE formula for arm (b), and whether GO / HOLD / REJECT may rest on arm (b).
+   - the equity base and the Sharpe definition: the DD equity-base half is closed by A4 (D-2026-11-08-B), his words "Closes the notes-4 DD equity-base item."; the gate-2 Sharpe formula is RULED (A2, D-2026-11-08-B; §6 :93); whether A2 closes the notes-4 Sharpe item (item 4) is NEEDS AMEAR (iv) of D-2026-11-08-B. was: "the notes-4 source (DECISIONS.md:978) scopes it as "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)"; the WF spec (NEEDS AMEAR 7) and this file read it for the "OOS Sharpe ≥ 1.0" gate. D-2026-11-05-A item 3's DD-base ruling (§8) stands as written; whether it closes the notes-4 DD-gate item is NOT decided here";
+   - the O1 gate set: RULED (R2, R3, D-2026-11-08-A; A7, A8, D-2026-11-08-B; §8); R2 does not name HOLD or REJECT (§8 :132); the WFE annualisation method is NEEDS AMEAR (iii) of D-2026-11-08-B. was: "whether WFE ≥ 0.50 applies to arm (a), the WFE formula for arm (b), and whether GO / HOLD / REJECT may rest on arm (b)." D-2026-11-08-B NEEDS AMEAR (i)–(iv) (DECISIONS.md, end of that entry) are Amear's and OPEN: (i) A3 W/L by price or by net; (ii) A4 limit type and stage for the Studio Static rows and for rows whose Eval and Sim-Funded types differ; (iii) A8 annualisation method; (iv) whether A2 closes the notes-4 Sharpe item.
 
 ### (D) The WF spec's 29 NEEDS AMEAR items, mapped
 
@@ -322,12 +322,12 @@ Source: `docs/specs/2026-11-05-walk-forward-spec.md:194-224`. What Q10 hands ove
 | 4 | Exit-policy options | RULED (set: ruling 4 of 2026-11-06; definitions: Q4, Q5) | §3 |
 | 5 | ATR period and series | RULED (period: ruling 4 of 2026-11-06 "ATR 14"; series: Q6); computation SETTLED | §4; (B) 4 |
 | 6 | In-sample objective, ties | RULED (class: ruling 4 of 2026-11-06); statistic, minimum, eligibility, tie-break SETTLED | §6; (B) 13–17 |
-| 7 | Sharpe definition and equity base for "OOS Sharpe ≥ 1.0" | OPEN (ruling 9). The notes-4 source (DECISIONS.md:978) also names the equity base for the 4% DD gate; OPEN in (C) | §6, §8; (C) |
-| 8 | WFE for arm (a); WFE formula for arm (b) | Both halves OPEN (ruling 9; the O1 gate set, REPORTED BY the return handoff :74) | §8; (C) |
-| 9 | Gate set per arm; GO / HOLD / REJECT | Q8 recorded as his statement (§8). As O1 items, the gate set and whether GO / HOLD / REJECT may rest on arm (b): OPEN (ruling 9; the O1 gate set, REPORTED BY the return handoff :74). Whether Q8 discharges O1 is left to the master and the auditor | §8; (C) |
-| 10 | R-1104-3's judged version | Which arm: "judged arm = (a) fixed rules" (ruling 4 of 2026-11-06) recorded as his statement; as an O1 item, OPEN (ruling 9; the O1 gate set, REPORTED BY the return handoff :74). Whether this Standard-resolution, breaker-less run is the judged go/no-go version: SETTLED, a provisional result | §2, §8; (B) 35 |
+| 7 | Sharpe definition and equity base for "OOS Sharpe ≥ 1.0" | Gate-2 Sharpe: RULED (A2, D-2026-11-08-B). The DD equity-base item: closed (A4, D-2026-11-08-B: "Closes the notes-4 DD equity-base item."). The notes-4 Sharpe item: NEEDS AMEAR (iv) of D-2026-11-08-B. was: "OPEN (ruling 9). The notes-4 source (DECISIONS.md:978) also names the equity base for the 4% DD gate; OPEN in (C)" | §6, §8; (C) |
+| 8 | WFE for arm (a); WFE formula for arm (b) | Arm (a): RULED (A7, D-2026-11-08-B: "(WFE not applicable)"; R3, D-2026-11-08-A). Arm (b) formula: RULED (A8, D-2026-11-08-B); its annualisation method: NEEDS AMEAR (iii) of D-2026-11-08-B. was: "Both halves OPEN (ruling 9; the O1 gate set, REPORTED BY the return handoff :74)" | §8; (C) |
+| 9 | Gate set per arm; GO / HOLD / REJECT | Gate set per arm: RULED (A7, D-2026-11-08-B, amending Q8). GO: "GO requires arm (a) to pass" (R2, D-2026-11-08-A); HOLD / REJECT not named in R2. O1: discharged (A8, D-2026-11-08-B). was: "Q8 recorded as his statement (§8). As O1 items, the gate set and whether GO / HOLD / REJECT may rest on arm (b): OPEN (ruling 9; the O1 gate set, REPORTED BY the return handoff :74). Whether Q8 discharges O1 is left to the master and the auditor" | §8; (C) |
+| 10 | R-1104-3's judged version | Which arm: "judged arm = (a) fixed rules" (ruling 4 of 2026-11-06) recorded as his statement; as an O1 item, RULED: "GO requires arm (a) to pass" (R2, D-2026-11-08-A); O1 discharged (A8, D-2026-11-08-B) — was: "OPEN (ruling 9; the O1 gate set, REPORTED BY the return handoff :74)". Whether this Standard-resolution, breaker-less run is the judged go/no-go version: SETTLED, a provisional result | §2, §8; (B) 35 |
 | 11 | MFFU account size / tier | No tier, report every row: RULED (Q9; D-2026-11-05-A items 4–5). The pick: OPEN (Q9) | §8; (C) |
-| 12 | Trailing-limit stage and type; Studio's Static limits | Reporting rule SETTLED: every row reported, Static rows included. Which plan, stage and type counts: OPEN (Q9) | §8; (B) 38; (C) |
+| 12 | Trailing-limit stage and type; Studio's Static limits | Reporting rule SETTLED: every row reported, Static rows included. Which plan, stage and type counts: OPEN (Q9). The A4 gate's limit type and stage for the Static rows and for rows whose Eval and Sim-Funded types differ (D-2026-11-08-B): NEEDS AMEAR (ii) of D-2026-11-08-B | §8; (B) 38; (C) |
 | 13 | MFFU page contradictions; Builder 50K add-on | Reporting rule SETTLED: both figures shown, the lower used; the Builder 50K add-on row reported. The tier choice: OPEN (Q9) | §8; (B) 38; (C) |
 | 14 | Arm (b) branch name | SETTLED | §9; (B) 29 |
 | 15 | Day-count convention | SETTLED | §5; (B) 10 |
@@ -346,4 +346,4 @@ Source: `docs/specs/2026-11-05-walk-forward-spec.md:194-224`. What Q10 hands ove
 | 28 | Lookback warm-up | SETTLED | §5; (B) 11 |
 | 29 | Per-window P&L contract size | SETTLED: 1 NQ and 1 MNQ both reported | §8; (B) 41 |
 
-**Raised to the master:** none remain. The items version 2 first marked so (WF NA 8 second half, 10 second half, 18, 19, 20, 21, 22 method, 24, 25, 29) are now SETTLED in (B) rows 35–41, or OPEN under ruling 9 (item 8). Items 19 and 20 are settled for walk-forward use only; the breaker #6 figure and the Block 4 question are not decided here and go to the breaker build (O4).
+**Raised to the master:** none remain. The items version 2 first marked so (WF NA 8 second half, 10 second half, 18, 19, 20, 21, 22 method, 24, 25, 29) are now SETTLED in (B) rows 35–41, or, for item 8, RULED (R3, D-2026-11-08-A; A7, A8, D-2026-11-08-B), its annualisation method NEEDS AMEAR (iii) of D-2026-11-08-B (was: "or OPEN under ruling 9 (item 8)"). Items 19 and 20 are settled for walk-forward use only; the breaker #6 figure and the Block 4 question are not decided here and go to the breaker build (O4).
```

## Final evidence block (taken last; Verification evidence, part 2)

Captured by the same run that wrote the diff of record above, after every other edit of this unit.

```
$ git diff --numstat HEAD -- docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md
5	5	docs/specs/2026-11-05-walk-forward-spec.md
21	21	docs/specs/2026-11-06-walk-forward-values.md
[exit 0]
$ shasum -a 256 docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md
6d7ed4df9328ad2d2ac489834fdb3ec82fd296e5cd642d651747ffa3217ceb7e  docs/specs/2026-11-06-walk-forward-values.md
a80074ecc3cdb39c8bed9634d5f8a9a8c8def135849cc2af6fce785d9303cc04  docs/specs/2026-11-05-walk-forward-spec.md
[exit 0]
$ openssl dgst -sha256 docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md
SHA2-256(docs/specs/2026-11-06-walk-forward-values.md)= 6d7ed4df9328ad2d2ac489834fdb3ec82fd296e5cd642d651747ffa3217ceb7e
SHA2-256(docs/specs/2026-11-05-walk-forward-spec.md)= a80074ecc3cdb39c8bed9634d5f8a9a8c8def135849cc2af6fce785d9303cc04
[exit 0]
$ git diff HEAD -- docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md | openssl dgst -sha256
SHA2-256(stdin)= b06ee494396805c3cf0abc19314010347850b854c74a3e8f5a3f0226a6d4369e
$ git diff f10603a -- docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md | openssl dgst -sha256
SHA2-256(stdin)= b06ee494396805c3cf0abc19314010347850b854c74a3e8f5a3f0226a6d4369e
$ git diff HEAD --stat -- docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md
 docs/specs/2026-11-05-walk-forward-spec.md   | 10 +++----
 docs/specs/2026-11-06-walk-forward-values.md | 42 ++++++++++++++--------------
 2 files changed, 26 insertions(+), 26 deletions(-)
[exit 0]
$ python3 -I /tmp/diq-resume/manifest_relocate.py --verify
PRE[current] ends-with-single-LF PASS: last2=b'|\n'
PRE[current] no-CR PASS: CR count=0
INFO mode=verify current-lines=313 saved-copy-exists=True
INFO old taken from saved copy /tmp/diq-resume/MANIFEST.old.md
PRE[HEAD] ends-with-single-LF PASS: last2=b'|\n'
PRE[HEAD] no-CR PASS: CR count=0
PRE[old] ends-with-single-LF PASS: last2=b'|\n'
PRE[old] no-CR PASS: CR count=0
PRE head-lines==306 PASS: head=306
PRE old-lines==312 PASS: old=312
PRE old[1..298]==HEAD[1..298] PASS: mismatched=0
PRE old:301 path PASS: row path
PRE old:303 path PASS: row path
PRE E1 once-in-row PASS: count=1
PRE E1 once-in-file PASS: count=1
PRE E2 once-in-row PASS: count=1
PRE E2 once-in-file PASS: count=1
INFO dash in E1/E2 old strings: U+2013 EN DASH bytes=e2 80 93; present in old:301=True, old:303=True
PRE[new] ends-with-single-LF PASS: last2=b'|\n'
PRE[new] no-CR PASS: CR count=0
PRE[old] ends-with-single-LF PASS: last2=b'|\n'
PRE[old] no-CR PASS: CR count=0
A1 new line count == 313 PASS: new=313
A2 new[1..306] == HEAD[1..306] PASS: mismatched=0 head=306
A3 new[307..312] == old[299..304] (+E1@309, +E2@311) PASS: new:307<-old:299(unchanged)=ok; new:308<-old:300(unchanged)=ok; new:309<-old:301(E1)=ok; new:310<-old:302(unchanged)=ok; new:311<-old:303(E2)=ok; new:312<-old:304(unchanged)=ok
A4 old[305..312] == HEAD[299..306] PASS: mismatched=0 old=312
A5 new line 313 == new row PASS: len=509 expected-len=509
A6x multiset(all old lines, E1/E2, + new row) == multiset(new) PASS: lhs=313 rhs=313
A6 multiset(old[1..304] w/ E1/E2 + HEAD[299..306] in place of dropped dup block + new row) == multiset(new) PASS: lhs=313 rhs=313 extra-in-new=0 missing-from-new=0
A6b new bytes == computed expected PASS: new=145371B expected=145371B
A6c new single trailing LF, no CR PASS: format
A7 sha256 old  = c36921e8c3627119205435e045404e9d1dd1a9c66c60b5e9a76c1f3bdca89ed8 (144784 B, 312 lines)
A7 sha256 new  = 3dc8bec0b17e1cfe26ef04b563cc68b5fb9c59fcf406e784556beaeacaccffd4 (145371 B, 313 lines)
A7 sha256 HEAD = 69ffe88714b930ad9d76bbc3b9af5996079c518d3a9ffc172c787e31b40b1409 (142355 B, 306 lines)
A7 HEAD blob id = ff53c66c2d2181bf379c86cf0a459fd9f6a9341c
A7 new != old and new != HEAD PASS: distinct digests
RESULT PASS: all asserts passed
[exit 0]
$ python3 (independent MANIFEST check in assemble.py)
MANIFEST.md lines: 313; HEAD:MANIFEST.md lines: 306
working tree starts with HEAD blob byte for byte: True
rows after HEAD's 306: 7
row 307 vs pre-unit row 299: identical
row 308 vs pre-unit row 300: identical
row 309 vs pre-unit row 301: differs
row 310 vs pre-unit row 302: identical
row 311 vs pre-unit row 303: differs
row 312 vs pre-unit row 304: identical
row 313: | /docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md | Repor …
pre-unit rows 305-312 == HEAD rows 299-306: True
$ git diff --numstat HEAD -- MANIFEST.md
7	0	MANIFEST.md
$ python3 (U7 manager report: prefix and appended line)
lines now: 628; sha256 of lines 1-627: f78aa3505f9ce01056f7300e769e07f91868f7393a2f4fc1bec305184f7c372a; pre-append sha256 (captured before the append this session): f78aa3505f9ce01056f7300e769e07f91868f7393a2f4fc1bec305184f7c372a; match: True
last line: SUPERSEDED 2026-11-09: the pasted current diff of record above predates correction 3; the diff of record is in docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md (Amear C1, D-2026-11-08-C).
$ stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S' <three correction reports> <U7 report>
2026-11-08T12:02:18 docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md
2026-11-08T12:17:52 docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md
2026-11-08T12:19:55 docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md
2026-11-09T01:15:12 docs/reports/2026-11-08-wf-spec-amendment-manager.md
[exit 0]
$ shasum -a 256 <three correction reports>
2e85970749363f378f86002c9713fc687ec3934abc30b921fc74ed644912585b  docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md
2c3644cb10ce6f4733bfbe9b00e8f30d47d4cc4528554d6184e23497ab01f0f8  docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md
2311e13bc86c322c76fe6df274db47ce3ab91bee4055fa0a2076f1c85796cc43  docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md
[exit 0]
$ /usr/bin/grep -n -o -E 'NEEDS AMEAR \((i|ii|iii|iv)\)[^.;]{0,60}|NEEDS AMEAR 12' docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md
docs/specs/2026-11-06-walk-forward-values.md:5:NEEDS AMEAR (i)–(iv) stay OPEN
docs/specs/2026-11-06-walk-forward-values.md:12:NEEDS AMEAR (i)–(iv), A5's second half (§6 :93) and the tier pick (Q9)
docs/specs/2026-11-06-walk-forward-values.md:93:NEEDS AMEAR (iv) of D-2026-11-08-B
docs/specs/2026-11-06-walk-forward-values.md:132:NEEDS AMEAR (iv) of D-2026-11-08-B
docs/specs/2026-11-06-walk-forward-values.md:133:NEEDS AMEAR (iii) of D-2026-11-08-B
docs/specs/2026-11-06-walk-forward-values.md:135:NEEDS AMEAR (ii) of D-2026-11-08-B
docs/specs/2026-11-06-walk-forward-values.md:135:NEEDS AMEAR (i) of D-2026-11-08-B
docs/specs/2026-11-06-walk-forward-values.md:136:NEEDS AMEAR 12
docs/specs/2026-11-06-walk-forward-values.md:310:NEEDS AMEAR (iv) of D-2026-11-08-B
docs/specs/2026-11-06-walk-forward-values.md:311:NEEDS AMEAR (iii) of D-2026-11-08-B
docs/specs/2026-11-06-walk-forward-values.md:311:NEEDS AMEAR (i)–(iv) (DECISIONS
docs/specs/2026-11-06-walk-forward-values.md:325:NEEDS AMEAR (iv) of D-2026-11-08-B
docs/specs/2026-11-06-walk-forward-values.md:326:NEEDS AMEAR (iii) of D-2026-11-08-B
docs/specs/2026-11-06-walk-forward-values.md:330:NEEDS AMEAR (ii) of D-2026-11-08-B | §8
docs/specs/2026-11-06-walk-forward-values.md:349:NEEDS AMEAR (iii) of D-2026-11-08-B (was: "or OPEN under ruling 9 (item 8)")
docs/specs/2026-11-05-walk-forward-spec.md:107:NEEDS AMEAR (ii) of D-2026-11-08-B (cf
docs/specs/2026-11-05-walk-forward-spec.md:107:NEEDS AMEAR 12
docs/specs/2026-11-05-walk-forward-spec.md:113:NEEDS AMEAR (ii)) | Grade / source |
docs/specs/2026-11-05-walk-forward-spec.md:141:NEEDS AMEAR 12
docs/specs/2026-11-05-walk-forward-spec.md:156:NEEDS AMEAR (ii) of D-2026-11-08-B
[exit 0]
$ sed -n '202,203p;207p' docs/specs/2026-11-05-walk-forward-spec.md | cut -c1-150
7. What is the **Sharpe definition** for "OOS Sharpe ≥ 1.0" (daily or per-trade, annualisation, risk-free rate), and what **equity base** does it use 
8. Does **WFE ≥ 0.50** apply to arm (a), which has no in-sample optimisation (O1)? For arm (b), which WFE formula is used?
12. For "MFFU's trailing drawdown limit", which **stage** (Evaluation or Sim-Funded) and which **type** (EOD or intraday trailing) counts? Do Studio's
[exit 0]
$ python3 (MANIFEST row-number references in the four U7 reports; regex MANIFEST[^|`]{0,14}?:?[0-9]{3}([–-][0-9]{3})?)
2026-11-08-wf-spec-amendment-manager.md:492: MANIFEST rows 302–303
2026-11-08-wf-spec-amendment-correction-2-manager.md:49: MANIFEST rows 302–303
2026-11-08-wf-spec-amendment-correction-2-manager.md:145: MANIFEST.md <(head -n 301
2026-11-08-wf-spec-amendment-correction-2-manager.md:231: MANIFEST row 303
2026-11-08-wf-spec-amendment-correction-2-manager.md:289: MANIFEST row 299
2026-11-08-wf-spec-amendment-correction-3-manager.md:6: MANIFEST row after :303
2026-11-08-wf-spec-amendment-correction-3-manager.md:18: MANIFEST :296–303
$ python3 (U7 manager report: lines carrying the first three words of the standing sentence; pattern not quoted here)
lines: [1, 199, 536]; full-sentence occurrences: 1
$ git status --porcelain -- docs/specs/2026-11-06-walk-forward-values.md
 M docs/specs/2026-11-06-walk-forward-values.md
[exit 0]
$ git status --porcelain -- docs/specs/2026-11-05-walk-forward-spec.md
 M docs/specs/2026-11-05-walk-forward-spec.md
[exit 0]
$ git status --porcelain -- MANIFEST.md
 M MANIFEST.md
[exit 0]
$ git status --porcelain -- docs/reports/2026-11-08-wf-spec-amendment-manager.md
?? docs/reports/2026-11-08-wf-spec-amendment-manager.md
[exit 0]
$ git status --porcelain -- docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md
?? docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md
[exit 0]
$ git status --porcelain -- docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md
?? docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md
[exit 0]
$ git status --porcelain -- docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md
?? docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md
[exit 0]
$ git status --porcelain -- docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md
?? docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md
[exit 0]
$ git diff --cached --name-only -- <commit set>
(empty: nothing in the commit set is staged)
[exit 0]
$ git rev-parse HEAD origin/main
f10603a242a7f7b8195caef24712d31c4ca67512
f10603a242a7f7b8195caef24712d31c4ca67512
[exit 0]
```

```
$ python3 (self-checks on this file, as assembled)
reconstructed diff sha256 from this file: b06ee494396805c3cf0abc19314010347850b854c74a3e8f5a3f0226a6d4369e (43982 bytes); equals the diff of record sha256: True
standing sentence occurrences in this file: 1, on line 1: True; occurrences of its first three words: 1
placeholder token present: False; MANIFEST asserts: True; independent MANIFEST check: True; U7 append-only: True
```

Result: PASS

## Addendum — byte-exact diff of record (master decision, D-2026-11-08-D D1)

Appended after line 587; lines 1–587 above are unchanged. Under D-2026-11-08-D D1 the master decided to add a byte-exact copy of the diff of record as an evidence file (the alternative offered in adversarial finding 11 above).

**Evidence file:** `docs/reports/evidence/2026-11-09-u7-diff-of-record.patch`. It holds the exact stdout bytes of `git diff HEAD -- docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md`, written by `/tmp/diq-addendum/t1.py` (python3 `subprocess.run(..., capture_output=True)`, opened in exclusive-create binary mode; no shell redirection). Pasted output:

```
$ python3 /tmp/diq-addendum/t1.py
bytes written: 43982 sha256: b06ee494396805c3cf0abc19314010347850b854c74a3e8f5a3f0226a6d4369e
$ wc -c docs/reports/evidence/2026-11-09-u7-diff-of-record.patch
   43982 docs/reports/evidence/2026-11-09-u7-diff-of-record.patch
$ openssl dgst -sha256 docs/reports/evidence/2026-11-09-u7-diff-of-record.patch
SHA2-256(docs/reports/evidence/2026-11-09-u7-diff-of-record.patch)= b06ee494396805c3cf0abc19314010347850b854c74a3e8f5a3f0226a6d4369e
$ git diff HEAD -- docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md | openssl dgst -sha256
SHA2-256(stdin)= b06ee494396805c3cf0abc19314010347850b854c74a3e8f5a3f0226a6d4369e
$ grep -n 'SHA2-256(/tmp/diq-resume/diff_of_record.txt)' docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md
234:SHA2-256(/tmp/diq-resume/diff_of_record.txt)= b06ee494396805c3cf0abc19314010347850b854c74a3e8f5a3f0226a6d4369e
$ git check-ignore -v docs/reports/evidence/2026-11-09-u7-diff-of-record.patch; echo ci=$?
ci=1
```

The three digests are equal: the file, a live re-run of the diff, and the sha this report records at :234. Size 43982 bytes, the same as recorded at :163. `git check-ignore` exits 1, so the file is not gitignored.

**Status of the two copies.** The evidence file is the diff of record under Amear C1 (D-2026-11-08-C: "the diff of the blob being committed"). The "Diff of record" section above (from :226) is a readable copy. It carries two disclosed markers (decision DT1, :34 and :237) in place of the standing sentence, so this report still carries that sentence once, on line 1 (S13). The evidence file is raw `git diff` bytes and so contains the sentence in full at its diff line 62, and an 80-character part of it at diff line 5. That is by design: S13 governs this report, and the patch is not a report.

**Specs unchanged.** Neither spec was edited by this follow-up. Pasted output:

```
$ openssl dgst -sha256 docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md
SHA2-256(docs/specs/2026-11-06-walk-forward-values.md)= 6d7ed4df9328ad2d2ac489834fdb3ec82fd296e5cd642d651747ffa3217ceb7e
SHA2-256(docs/specs/2026-11-05-walk-forward-spec.md)= a80074ecc3cdb39c8bed9634d5f8a9a8c8def135849cc2af6fce785d9303cc04
```

The line below supersedes the earlier `Result: PASS` line at :587, which is kept.

Result: PASS
