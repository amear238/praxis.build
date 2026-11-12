# Unit 2026-11-12-fgd-part-b — fix worker 2

## Task

Cure two evidence-rule defects in `docs/reports/2026-11-12-fgd-part-b-worker1.md` (bead `Praxis_build-fgd` part B), keeping its findings and Result line: (1) medication names at old :434 and :477 in E10; (2) quoted text cut with an ellipsis character at old :47, :52, :496, and a regex written with that character at old :476.

## Mode

BUILD (narrow fix). I edited only the worker1 report and created only this report. Scratch files are under `/tmp/fgdb-neg/`. Nothing staged, committed or pushed.

## Edits made

Old line numbers are those of the worker1 report before this cure. New line numbers are the ones the marker check in the evidence below prints.

1. After old :23 (last Process log item): new item 8 with the dispatched text (new :24).
2. Old :47: the cut heading quote is replaced by the full heading text of entry D-2026-11-12-B, and the evidence cite is now (E5, E7, E12) (new :48).
3. Old :52: the cut F3 quote is replaced by the full rubric line :28 at `5467031`, and the cite is now (E3, E12) (new :53).
4. Old :420: the E10 heading now names `/tmp/fgdb-neg/final2.sh` (new :421).
5. Old :423–444: the E10 script listing is replaced by the literal content of `final2.sh`. `final2.sh` is `final.sh` with 2 lines changed: the inline list variable and the grep that used it are replaced by a line that prints `wc -l < /tmp/fgdb/meds.txt` and a line that counts with `/usr/bin/grep -c -i -f /tmp/fgdb/meds.txt /tmp/fgdb-neg/added.txt`.
6. Old :450–471: the E10 output block is replaced by the literal output of `bash /tmp/fgdb-neg/final2.sh`. It has one more line than before: the list size, 63.
7. Old :476: the regex now reads `(F1|F2)[^|]{0,20}PASSED@`.
8. Old :477: the note is replaced by the dispatched sentence that names the outside-repo list file and no drug.
9. After old :486 (end of E11): new section E12, with the command and output that give the full texts used in edits 2, 3 and 10.
10. Old :496: the cut heading quote is replaced by the full heading text of entry D-2026-11-12-B, citing E12.

Findings item 9 is unchanged: the new E10 run gives medication names 0, the count item 9 already states.

## Verification evidence (command output)

### Run of final2.sh

The literal output of `bash /tmp/fgdb-neg/final2.sh` is pasted into the worker1 report as E10; the medication lines of that output are re-printed from the worker1 file by the last check below.

### Final checks — `/tmp/fgdb-neg/checks.sh` (run with `bash /tmp/fgdb-neg/checks.sh`)

The ellipsis check builds the character with `printf` so that this report holds no literal ellipsis character; it is the dispatched `grep -c` ellipsis check, run on both reports. The S13-sentence and banned-word patterns are split across quotes so that the listing itself does not match them.

```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build
W1=docs/reports/2026-11-12-fgd-part-b-worker1.md; W2=docs/reports/2026-11-12-fgd-part-b-worker2.md
echo "--- final2.sh vs final.sh: changed-line count, list-variable mentions in final2.sh"
diff /tmp/fgdb-neg/final.sh /tmp/fgdb-neg/final2.sh | /usr/bin/grep -c '^[<>]'; /usr/bin/grep -c 'MEDS' /tmp/fgdb-neg/final2.sh
echo "--- medication list hits (must be 0 each)"; /usr/bin/grep -c -i -f /tmp/fgdb/meds.txt $W1 $W2
echo "--- medication list positive control (expect 1)"; sed -n 1p /tmp/fgdb/meds.txt | sed 's/^/x /' > /tmp/fgdb-neg/med-pos.txt; /usr/bin/grep -c -i -f /tmp/fgdb/meds.txt /tmp/fgdb-neg/med-pos.txt; rm -f /tmp/fgdb-neg/med-pos.txt
echo "--- ellipsis character count (must be 0 each)"; E=$(printf '\342\200\246'); grep -c "$E" $W1 $W2
echo "--- S13 sentence count (must be 1 each)"; S='Fills are'' optimistic'; /usr/bin/grep -c "$S" $W1 $W2
echo "--- last line is the S13 sentence (1 = yes)"; L13='Fills are'' optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'; for f in $W1 $W2; do printf '%s: ' $f; tail -n 1 $f | /usr/bin/grep -cxF "$L13"; done
echo "--- banned words (must be 0 each)"; /usr/bin/grep -ci -e 'ver''dict' -e 'COMMIT-''INDEX' -e 'COMMIT-DIFF-''SHA256' $W1 $W2
echo "--- email regex (must be 0 each)"; /usr/bin/grep -c -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $W1 $W2
echo "--- Result lines"; /usr/bin/grep -n '^Result: ' $W1 $W2
echo "--- edit markers in worker1 (line:match)"; /usr/bin/grep -n -o -F -e '8. Cure by fix worker 2' -e 'authorised, first pass only' -e 'in the output.", then' -e '### E10 — `/tmp/fgdb-neg/final2.sh`' -e 'medication list size (lines)' -e '`(F1|F2)[^|]{0,20}PASSED@`' -e 'held outside the repo' -e '### E12' $W1
echo "--- worker1 Findings item 9 and E10 output medication counts"; /usr/bin/grep -n -o -E '^   - Email addresses: 0\. Medication names: 0|^medication names: 0$|^medication list size \(lines\): +63$' $W1
```

Output:

```
--- final2.sh vs final.sh: changed-line count, list-variable mentions in final2.sh
4
0
--- medication list hits (must be 0 each)
docs/reports/2026-11-12-fgd-part-b-worker1.md:0
docs/reports/2026-11-12-fgd-part-b-worker2.md:0
--- medication list positive control (expect 1)
1
--- ellipsis character count (must be 0 each)
docs/reports/2026-11-12-fgd-part-b-worker1.md:0
docs/reports/2026-11-12-fgd-part-b-worker2.md:0
--- S13 sentence count (must be 1 each)
docs/reports/2026-11-12-fgd-part-b-worker1.md:1
docs/reports/2026-11-12-fgd-part-b-worker2.md:1
--- last line is the S13 sentence (1 = yes)
docs/reports/2026-11-12-fgd-part-b-worker1.md: 1
docs/reports/2026-11-12-fgd-part-b-worker2.md: 1
--- banned words (must be 0 each)
docs/reports/2026-11-12-fgd-part-b-worker1.md:0
docs/reports/2026-11-12-fgd-part-b-worker2.md:0
--- email regex (must be 0 each)
docs/reports/2026-11-12-fgd-part-b-worker1.md:0
docs/reports/2026-11-12-fgd-part-b-worker2.md:0
--- Result lines
docs/reports/2026-11-12-fgd-part-b-worker1.md:504:Result: FAIL
docs/reports/2026-11-12-fgd-part-b-worker2.md:106:Result: PASS
--- edit markers in worker1 (line:match)
24:8. Cure by fix worker 2
48:authorised, first pass only
53:in the output.", then
366:authorised, first pass only
421:### E10 — `/tmp/fgdb-neg/final2.sh`
435:medication list size (lines)
464:medication list size (lines)
478:`(F1|F2)[^|]{0,20}PASSED@`
479:held outside the repo
490:### E12
494:authorised, first pass only
506:authorised, first pass only
--- worker1 Findings item 9 and E10 output medication counts
55:   - Email addresses: 0. Medication names: 0
464:medication list size (lines):       63
465:medication names: 0
```

## Result

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
