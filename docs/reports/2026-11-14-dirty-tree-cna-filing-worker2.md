# Dirty-tree CNA filing — worker 2 (adversarial)

## Task
Adversarial check of the producer's IN/OUT split of 36 dirty-tree candidates (/tmp/praxis-cna/cands.txt; IN 33, OUT 3) and of its 33 MANIFEST rows (/tmp/praxis-cna/rows.txt), against DECISION_LOG row `2026-11-14T09:06:00Z` (working-tree :956, read in full). HEAD 9a18fde. The IN and OUT lists together equal the candidate list exactly (`diff` of the sorted lists was empty).

## Mode
ADVERSARIAL, read-only. I wrote only this file. Scripts and outputs are in /tmp/praxis-cna-w3/ (a.py, b.py, c.sh, d.sh, e.sh, plus a.out and b.out). I did not touch the real index, /tmp/praxis-cna/idx, or anything under .claude/.

## Check A — exclusion rows

I found every DECISION_LOG row that names a candidate by searching for its basename and for its short `-suffix` form (a.py). I read rows :616, :622, :776, :883, :886, :889, :890, :897, :912, :913, :915, :919 and :925 in full, plus :882, :887, :888, :900, :914 and :923–:924 for context.

| Path (group) | Covering rows, clause verbatim | My call | Producer | Agree? |
|---|---|---|---|---|
| U4 session39-agents-dir-write-path | :121 [2026-07-28T17:15Z] cites it as the report; no exclusion row | IN | IN | agree |
| U9 facts-pack, praxis-assessment | :165 [2026-08-06T19:48:03Z] cites both as evidence; no exclusion row | IN | IN | agree |
| U9 subreport-agent-memory | no row names it | IN | IN | agree |
| U10 f3-fill-resolution-research-UNGRADED | :351/:353/:355 cite it. Its own header (:4) says "must not be cited as a finding", but that is the file's own label, not an exclusion row | IN | IN | agree |
| U13 session53-parallel-handoff | :375, :389 [2026-08-30T19:55:00Z] "Wrote ... (untracked)"; no exclusion | IN | IN | agree |
| U18 nightly-spec-request-review | :433 [2026-10-28T20:49:38Z] "**What survives:** ... (untracked, 20509 bytes)"; no exclusion | IN | IN | agree |
| U18 review-note-delivery | :441 cites :104 PASS. Rule (ii): email count 5 | OUT | OUT | agree |
| U18 voice-handoff-future-row-walkthrough | :632 [2026-10-31T17:05:39Z] "VOICE HANDOFF WRITTEN"; no exclusion | IN | IN | agree |
| U18 csv-analyses-fix-manager-record | :616 [2026-11-01T21:58:19Z] "Commit composition: pathspec — ... Excluded: `2026-11-01-csv-analyses-fix-manager-record.md` (gate artefact), root `F`, the old staged set." | IN (scope) | IN | agree, see note 1 |
| U18 three-strategy-results-s2-fix-manager-record | :622 [2026-11-01T14:12:50Z] "the manager wrote `...s2-fix-manager-record.md` to pass it and said so. File kept on disk (append-only), excluded from the commit and MANIFEST." | IN (scope) | IN | agree |
| U18 c7-probe-fresh-manifest-manager | :776 [2026-11-09T19:18:30Z] "stays out of this commit and untracked (it has no MANIFEST row; it goes to housekeeping D9)" | IN (scope) | IN | agree |
| U19 the four vm/replies files | :818, :819, :823 [2026-11-11T16:00:00Z] "Unit 2 = grade and file the four Hermes VM replies ... all untracked"; no exclusion | IN | IN | agree |
| U21 correction-1-manager | :883 [2026-11-12T18:30:00Z] "still open in the older reports: ... correction-1 manager :23, correction-1 manager :4 "not edited" with no output, defect-6 cures at correction-1 manager :17, :24, :376 unchecked" | OUT (content) | OUT | agree |
| U21 correction-1-worker1 | :882 [2026-11-12T18:02:00Z] "its one adversary (correction-1 worker1, `Result: FAIL`, 7 defects) failed round 1". :883 (b) "stay on disk, uncommitted and unedited, as the record of the failed attempts". No content clause against the worker report itself | IN | IN | agree |
| U21 correction-2-manager | :883 "worker B (a330fe853e38c8306) graded FAIL with 9 gaps; cured by the manager in its own report only, unchecked" | OUT (content: cures nobody checked) | OUT | agree |
| U21 correction-2-worker2 | :883 as above; the row records this file's 9 gaps and says nothing against the file | IN | IN | agree |
| U21 **-evidence.md** | :889 [2026-11-12T22:00:00Z] "Adversary 4 `GRADE: FAIL (7 defects)`, one in entry text ..., six in report wording" and "Master's lesson, recorded: the single evidence report has grown across three in-place regenerations to 165 command blocks and three adversary histories; every cure adds surface" and "the old evidence report stays on disk, unedited from now, uncommitted". :890 [2026-11-12T22:07:39Z] "The seven earlier O3 reports (including `-evidence.md`) stay on disk, unedited, uncommitted." The file itself, :1343: "the other six are report-wording cures for a later round". | **OUT (content; at minimum doubtful)** | IN | **DISAGREE: defect 1** |
| U22 o3-cure3-manager, -worker1 | :897 [2026-11-13T05:20:00Z] "The cure-3 manager and worker reports and the seven earlier O3 reports stay on disk, uncommitted." Also: "the adversary graded with the grade slots at PENDING and the manager filled PASS after". That is a process note, and manager :13 discloses it | IN (scope) | IN | agree |
| U25 parity-worker1..4 | :912 [2026-11-13T13:07:54Z]: the content clause ("ends `Result: RESULT_LINE` (:156), an unfinished report ... it cannot go in the commit") is about `-o4-parity-manager.md`, which is not a candidate. For the rest the row says "The five earlier O4 reports stay on disk, uncommitted." (scope). The four workers have complete Grade lines (:266, :313, :295, :293) and no RESULT_LINE token | IN | IN | agree |
| U25 reduce-manager/-worker1, reduce2-manager/-worker1 | :912 "five earlier O4 reports stay on disk, uncommitted"; :913 [2026-11-13T13:13:15Z] "Out of the commit, on disk: ... the five earlier O4 reports" | IN (scope) | IN | agree |
| U25 repoint-manager/-worker1 | :913 "Out of the commit, on disk: MANIFEST :468 ..., the five earlier O4 reports, `-repoint-manager.md` and `-repoint-worker1.md`" | IN (scope) | IN | agree |
| U25 cure1-manager/-worker1 | :915 [2026-11-13T13:24:23Z] "out of the commit's scope, and the brief's fault ... The cure reports stay on disk, uncommitted." | IN (scope) | IN | agree |
| U27 open-a1-cure-worker1 | :923 [2026-11-13T17:02:02Z] "one cold adversary (`-cure-worker1.md`), whose report stays out of the commit and is not cited by the committed report"; :925 [2026-11-13T17:15:15Z] "Out of the commit, on disk: ... the two old open-a1 reports, `-cure-worker1.md`." Scope only. :919's content clauses (manager :71, worker :7, the 75/78 line count) concern "the two open-a1 reports", not this candidate | IN (scope) | IN | agree (filing defect 3 below) |

Note 1 (csv gate artefact): ":616 (gate artefact)" sits inside a commit-composition list ("Excluded: ..."), so the exclusion is from that commit. The sibling row :622 explains the same kind of file in scope terms: written to pass the stop gate, "excluded from the commit and MANIFEST". The file is not a placeholder. It holds a real pasted diff (:39–:48) and a scoped `Result: PASS (scoped to the mechanical check ...)` at :52, and it calls itself "process record only, excluded from the commit" (:31, :50). I read this as scope, not doubtful.

Defect 1 detail: the rule's content test is "wrong, misleading, placeholder, superseded in a way the row says must not be cited". The file's own last grade lists 7 defects. Six are report wording, and five of those six say a claim has no backing paste (for example "The claims that a run helper re-ran every block in order and pasted its output have no recorded helper command or pasted run"). :889 and :890 freeze the file "unedited", so those six were never cured. That is the same kind of reason the producer accepted for keeping both O3 correction managers OUT (uncured, unbacked claims). It is not a scope or timing reason. At best the case is doubtful, and the rule says "a doubtful case stays out". A doubtful IN is a defect.

## Check B — scans (b.py, counts only)

Counts are per file: name token (case-insensitive), email regex as briefed, and credential-value patterns (AWS key, GitHub token, `sk-`, Slack, PEM private key, Bearer, `password/secret/api_key/token = value`, JWT, Telegram bot token, Google API key, URL with embedded credentials).

- Name token: 0 in all 36 files.
- Email: 0 in 35 files. 5 in docs/reports/2026-10-28-review-note-delivery.md, which is OUT, as the producer has it.
- Credential-value hits: 0 in all 36 files.

Result: Check B agrees with the producer. Only review-note-delivery trips rule (ii).

## Check C — the 33 MANIFEST rows

Facts gathered from the files: line counts, standalone S13 positions (whole-line match), S13 substring counts, the last line, Result/Grade lines with their line numbers, a prefix comparison against /tmp/praxis-cna/pre, and placeholder tokens. For every stamp a row cites, I confirmed it exists in DECISION_LOG (c.sh). The ten appended files are byte-prefix-identical to their pre copies, plus exactly 2 lines. All ten filer's-note lines are identical: "Filer's note (2026-11-14, unit 2026-11-14-dirty-tree-cna-filing, praxis-master under D-2026-11-08-D D1): the limitation sentence below was appended at filing under rubric S13; the text above is unchanged." The S13 sentence follows each one.

c7-probe-fresh-manifest-manager sha256 is now `7719abd07c8fa56c9b11d24cb8000f6cf172ff859e3e769b1943ba4f54de2ba8`, the same as /tmp/praxis-cna/pre/. It has 91 lines, no standalone S13 line, the S13 sentence once inside :3 ("Standing limitation: ..."), and `Result: PASS` at :91 as its last line.

| Row | Path | Verdict |
|---|---|---|
| R1 | session39-agents-dir-write-path | Correct. Result: PASS :430; appended :431–:432; "line 8" matches the file's :18 and :159 |
| R2 | facts-pack | Correct. 115 commits (:45), 92 files (:78), 36 open (:112), "All three P0s are supervision bugs" (:114); appended :236–:237 |
| R3 | praxis-assessment | Correct. Provenance block (:3–:5); no Result line; appended :155–:156 |
| R4 | subreport-agent-memory | Correct. Provenance block; four-hook mentions 3; appended :364–:365 |
| R5 | f3-...-UNGRADED | Correct. Header :4 "does NOT discharge frozen criterion F3 and must not be cited as a finding"; stamps :351–:355; appended :340–:341 |
| R6 | session53-parallel-handoff | Correct. Stamp :389 item (3); Track A/1gd present; appended :279–:280. T1–T3 wording not line-checked |
| R7 | nightly-spec-request-review | Correct. :432 is the approval (the file's :206 names it); :433 "What survives"; D10 at :255; appended :298–:299 |
| R8 | voice-handoff-future-row-walkthrough | Correct. Stamp :632; the clipboard-copy claim matches :6 and :120; appended :124–:125 |
| R9 | csv-analyses-fix-manager-record | Correct as far as it goes. Opens at "## Verification evidence"; Result :52 scoped; appended :53–:54. Omitted, not false: a second, unscoped `Result: PASS` at :33 (fix-1 section) |
| R10 | three-strategy-results-s2-fix-manager-record | Correct. :3 "NOT part of the graded deliverable, and it is untracked"; Result: BLOCKED :64; appended :65–:66 |
| R11 | c7-probe-fresh-manifest-manager | Row text is true (sha confirmed; S13 inside :3; Result :91; no line changed). The filing breaches rule (iii): **defect 2** |
| R12–R15 | vm/replies x4 | Correct. STARTED / FINISHED contents; RESULT: DONE at :4 in both reply files; SSH, items 1, 2, 9, skill loading present; not edited, as rule (iii) requires |
| R16 | correction-1-worker1 (T14 row) | Correct. File checks: edit log vs pre-copies by full diff (check 2), S1 sweep (check 3) and report rules (check 5) on A, B, C, which are three reports |
| R17 | correction-2-worker2 (T14 row) | Correct. Round-1 diffs vs M and W (check 1), 29 items parsed (check 2, "items parsed 29"), format and de-identification scan of "all five files" (check 3), 9 numbered findings (:314–:349), Result: FAIL :350. "S1 sweep": the file mentions S1 14 times; the wording was not line-checked |
| R18 | -evidence.md | Result: FAIL :1341, S13 last line :1345 (the only standalone S13 line) and "no line changed" are true. But "manager report with cure rounds 2 and 3 by BUILD workers" restates the file's opening line, which its own Adversary 4 defect 3 flags: "the opening line's "cure rounds 2 and 3 by BUILD praxis-workers" does not fit it". The file's :165 says "the manager made the two cure-round-3 entry edits": **defect 4**. The filing call itself is defect 1 |
| R19 | o3-cure3-manager | Correct. Result: PASS :48; standalone S13 at :25 and :50 (exactly 2; a third copy sits inside a line); the PENDING clause matches :897 |
| R20 | o3-cure3-worker1 | Correct. Opens at "Check (a): line 251 ..." (:1); `> GRADE: PENDING` :86 (quoted inside a diff); GRADE: PASS :133; S13 last line :135 |
| R21 | o4-parity-worker1 | Correct. :2389–2416 and cae83dc in Task; Grade: FAIL (4 defects) :266; S13 last line :267 |
| R22 | o4-parity-worker2 | Correct. Grade :313; standalone S13 at :264 and :314 |
| R23 | o4-parity-worker3 | Correct. Grade :295; standalone S13 at :251 and :296; "No other o4-parity report was read" in Task |
| R24 | o4-parity-worker4 | Correct. Grade: FAIL (3 defects) :293; the reduce unit cured these three (reduce-manager Task; :900) |
| R25 | o4-reduce-manager | Correct. Stamp 06:06:00Z is :900 and the file's Task cites it; Result: FAIL :69, with "outside this unit's edit scope" |
| R26 | o4-reduce-worker1 | Correct. Checks (a)–(f) at :280–:295; Grade :312 |
| R27 | o4-reduce2-manager | Correct. :904 dispatches round 2; Result: FAIL :58 (as :905 says) |
| R28 | o4-reduce2-worker1 | Correct. `## Result: FAIL (1 defect)` :65 |
| R29 | o4-repoint-manager | Correct. :912 dispatches; :913 lists it as out; Result :64 |
| R30 | o4-repoint-worker1 | Correct. `## Result: PASS` :245 |
| R31 | o4-cure1-manager | Correct. Task :2 cites 13:17:27Z (:914) with the same scope words; Result: FAIL :57; :915 "out of the commit's scope" |
| R32 | o4-cure1-worker1 | Correct. "Overall: FAIL" at :66 (checked with `sed -n '66p'`); checks 6, 7(a), 7(b) named at :3 |
| R33 | open-a1-cure-worker1 | Row text is true (Result: FAIL :328; standalone S13 once at :327; "five edits" matches the file's :5; :925 out). The filing breaches rule (iii): **defect 3** |

## Defects

1. **-evidence.md is IN although its exclusion reasons are about content (at minimum doubtful).** DECISION_LOG :889 [2026-11-12T22:00:00Z] records "Adversary 4 `GRADE: FAIL (7 defects)` ... six in report wording". :889 and :890 [2026-11-12T22:07:39Z] then freeze the file "unedited, uncommitted". The file's own :1343 says "the other six are report-wording cures for a later round", and that round never happened. These are uncured claims without backing paste, the same kind of reason that keeps both O3 correction managers OUT. Rule (i): "a doubtful case stays out." It should be OUT and listed in HANDOFF.
2. **R11 / c7-probe-fresh-manifest-manager: rule (iii) not applied.** Rule (iii) at :956 says "a docs/reports file whose last standalone line is not the S13 sentence gets two lines appended at the end". The file's last line is `Result: PASS` (:91), and it has no standalone S13 line, only the sentence inside :3. The append was made and then reverted on the manager's own reading of rubric S13 "once". The row admits this ("decided by manager, for the master"), but no master row after :956 authorises it. The file count is 956 lines; I searched rows after :956 for `c7-probe-fresh-manifest` and found 0. The "once" reasoning is also applied inconsistently: R19, R22 and R23 file reports that carry two standalone S13 lines, unchanged.
3. **R33 / open-a1-cure-worker1: rule (iii) not applied.** The last line is `Result: FAIL` (:328), not the S13 sentence (which is at :327). By the text of rule (iii), two lines should have been appended. The file was "filed as written", and append10 has no entry for it. The producer appears to have read "last standalone line" as "has a standalone S13 line", which is not what the rule says. If the master meant that reading, it should be written down; as written, this is a breach.
4. **R18 description repeats a claim the file's own final adversary flagged.** "manager report with cure rounds 2 and 3 by BUILD workers": the file's Adversary 4 defect 3 says the opening line's "cure rounds 2 and 3 by BUILD praxis-workers" "does not fit it", and :165 says "the manager made the two cure-round-3 entry edits". Only partly supported (BUILD workers 3 and 5 exist at :163 and :165). Minor.

Not counted as defects: R9 leaves out the earlier unscoped `Result: PASS` at :33; :919 covers no candidate (its content clauses are about the two old open-a1 reports).

## Name-token count of this report

```
$ /usr/bin/grep -ci "$N" docs/reports/2026-11-14-dirty-tree-cna-filing-worker2.md
0
```

The count above was taken on this file before this line was inserted; the inserted text is a digit and a sentence with no name token. A re-run after the insert also returned 0.

Result: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
