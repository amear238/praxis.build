# 2026-11-10 f4-grading, correction 1, manager report

**Unit.** `2026-11-10-f4-grading`, correction 1 (the unit's only correction). **Role.** praxis-manager. **HEAD.** `d30ab4d`. **Started.** 2026-11-10T17:38:16Z (first `date -u`, pasted at the top of Verification evidence; the C1-V0 re-capture shows 17:44:58).

## Task

Cure the seven findings of the unit's first audit, which failed it. This is evidence form only. No element-table label and no coverage reading is changed, and F4 is not graded. Every change is an append: in each in-scope file, a section `## Correction 1 (2026-11-10, after audit fail 1)` is inserted immediately before the file's last line, the S13 sentence. No original text was changed, and no pointer lines were added (they would shift the line numbers that the audit and the corrections cite).

## Rubric criteria addressed

- S1 (specs/SPEC_RUBRIC.md :124), "Every claim in a report has pasted command output, not a description of output." This is audit findings 1 to 5.
- S2 (:125), "No component is reported at a higher level than the evidence supports." This is audit finding 6.
- S13 (:136), the standing sentence once as the last line, kept in every file.
- Audit finding 7 (de-identification claim made true) is cured under S1 and S2: the claim at manager :8 is narrowed to what the counts show.

## Workers dispatched

| Id | Mode | Scope | Outcome | Report |
|---|---|---|---|---|
| first dispatch | ADVERSARIAL | the six files, all seven findings | Stopped at its 40-turn cap; 29-line skeleton, no findings. Overwritten by adversary A as instructed | (same path as adversary A) |
| adversary A | ADVERSARIAL | manager report findings 1, 2, 3, 7; this report's C1-V0 and table | FAIL: 1 blocking, 6 minor; all fixed | `docs/reports/2026-11-10-f4-grading-correction-1-worker1.md` |
| adversary B | ADVERSARIAL | worker 2, 3, 4 and manifest-manager sections, findings 4, 5, 6 | FAIL: 2 blocking, 5 minor; all fixed | `docs/reports/2026-11-10-f4-grading-correction-1-worker2.md` |

No BUILD worker was used. The re-runs are manager commands, and the edits are appends of their pasted output. The brief assigns this correction to the manager.

## Process log

- 17:38Z. Baseline: HEAD `d30ab4d` (first-run capture under Verification evidence); index state in Final checks. Read the rubric S lines and the five in-scope files in full.
- Built the runner `/tmp/f4c1/run.sh`, which prints `$ ` plus each command line and then evals that exact line. Built the pattern file `/tmp/f4c1-pat.txt` (trader surname, three support names, thread id), extracted from the HEAD transcript and DECISION_LOG.md :177 with counts-only output. Built the redaction filter `/tmp/f4c1/redact.pl`, the banned-word file `/tmp/f4c1-bw.txt` and the S13 file `/tmp/f4c1-s13.txt`, which is extracted from rubric :136 so that the sentence is never typed in a command (C1-V0).
- One redaction slip, caught before anything was written to a file: the first version of the filter replaced names before addresses, which turned the 2026-08-07 report :34 address into `[patN]@domain`. The order was swapped (addresses first) and every block was re-run with the new filter. The pasted blocks all come from the second version, shown in C1-V0. Separately, while finding the transcript line layout, a manager terminal command printed raw transcript lines. That output went to the terminal only, and none of it is in any file.
- Re-ran manager V2, V7, V3, the :40 search, the [trader] use, the worker 2 Blocks 1 to 8, the worker 3 and worker 4 probes, the MANIFEST numstat and a scratch demonstration of the numstat blind spot. The blocks were assembled into the sections with `/tmp/f4c1/build.pl`, which copies whole command-plus-output chunks from the capture files (C1-V0), and inserted before each file's last line.
- Two disagreements with worker figures were found and are stated plainly in the corrections: worker 2 Block 7's `-w F4` = 634 (the re-run gives 496; 634 is the `-i` count), and worker 2 Block 3's line numbers (six off by one, not four).
- Dispatched one ADVERSARIAL worker with the six files and the seven findings only. It stopped at its turn cap with a skeleton. Dispatched two scoped ADVERSARIAL workers in parallel (A: the manager-file findings; B: the worker and manifest findings), each with a 25-call budget. Both returned FAIL (A: 1 blocking, 6 minor; B: 2 blocking, 5 minor). All findings were fixed by changing the command files and section templates and rebuilding the sections with `/tmp/f4c1/replace.sh` (Final checks), which replaces only the lines from the Correction 1 heading to the line before the last line. The outputs that read the edited files were re-run after a rebuild and rebuilt again, until a fresh re-run equalled the pasted capture.
- Ran the final checks after the last edit to every file (Final checks).

## Verification evidence (command output)

First run of the setup commands (terminal capture, before the C1-V0 re-capture), and the first command of this correction, which measured the in-scope files before any edit:

~~~text
$ date -u; git rev-parse --short HEAD
Tue Nov 10 17:38:16 UTC 2026
d30ab4d
$ cd /Volumes/Sensidine/Praxis.build && git rev-parse --short HEAD && wc -l docs/reports/2026-11-10-f4-grading-*.md specs/SPEC_RUBRIC.md 2>&1; ls specs docs/specs | head -50
d30ab4d
     460 docs/reports/2026-11-10-f4-grading-manager.md
      98 docs/reports/2026-11-10-f4-grading-manifest-manager.md
      28 docs/reports/2026-11-10-f4-grading-worker1.md
     148 docs/reports/2026-11-10-f4-grading-worker2.md
     153 docs/reports/2026-11-10-f4-grading-worker3.md
      85 docs/reports/2026-11-10-f4-grading-worker4.md
     461 specs/SPEC_RUBRIC.md
    1433 total
~~~

(The `ls` part of the second command listed the specs directories; that output is left out here, and nothing rests on it.)

### C1-V0. Setup: runner, pattern file, redaction filter, banned-word and S13 files

~~~text
$ date -u; git rev-parse --short HEAD
Tue Nov 10 17:44:58 UTC 2026
d30ab4d
$ T=$(git ls-tree -r --name-only HEAD docs/reports/evidence/ | grep -- '-reply-transcript.md$'); echo "$T" | sed 's/-[a-z]*-reply/-[name]-reply/'
docs/reports/evidence/2026-10-28-mffu-[name]-reply-transcript.md
$ git show "HEAD:$T" | sed -n 15p | awk '{print $2}' > /tmp/f4c1-pat.txt
$ git show "HEAD:$T" | sed -n 16p | awk '{print $2}' >> /tmp/f4c1-pat.txt
$ git show "HEAD:$T" | sed -n 25p | grep -o 'My name is [A-Za-z]*' | awk '{print $4}' >> /tmp/f4c1-pat.txt
$ git show "HEAD:$T" | sed -n 36p | cut -d- -f1 >> /tmp/f4c1-pat.txt
$ git show HEAD:DECISION_LOG.md | sed -n 177p | grep -oE '[0-9a-f]{16}' | sort -u >> /tmp/f4c1-pat.txt
$ wc -l < /tmp/f4c1-pat.txt; sort -u /tmp/f4c1-pat.txt | wc -l; awk '{print NR, length($0)}' /tmp/f4c1-pat.txt
       5
       5
1 10
2 5
3 7
4 4
5 16
$ git show "HEAD:$T" | sed -n '1p;18p' | grep -c -i -w -F -f <(sed -n 4p /tmp/f4c1-pat.txt)
2
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | sed -n 36p | grep -c -i -w -F -f <(sed -n 2p /tmp/f4c1-pat.txt)
1
$ git show HEAD:DECISION_LOG.md | sed -n 435p | grep -o 'The greeting names.\{0,40\}' | perl -p /tmp/f4c1/redact.pl
The greeting names "[pat3]" but it is signed "[pat4]" (boil
$ cat /tmp/f4c1/redact.pl
BEGIN { open(P, "<", "/tmp/f4c1-pat.txt") or die "no pattern file"; chomp(@p = <P>); close P }
s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/[address]/g;
for my $i (0 .. $#p) { my $n = $i + 1; s/\b\Q$p[$i]\E\b/[pat$n]/gi }
$ printf '%s\n' "ver""dict" "COMMIT-""INDEX" "COMMIT-DIFF-""SHA256" > /tmp/f4c1-bw.txt; wc -l < /tmp/f4c1-bw.txt
       3
$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n 136p | grep -o '"Fills are optimistic[^"]*"' | tr -d '"' > /tmp/f4c1-s13.txt; wc -l < /tmp/f4c1-s13.txt; wc -c < /tmp/f4c1-s13.txt
       1
      91
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | sed -n 34p | grep -oE '[A-Za-z0-9._%+-]+@' | tr -d '@' > /tmp/f4c1-lp.txt; wc -l < /tmp/f4c1-lp.txt; git grep -c -i -w -F -f /tmp/f4c1-lp.txt HEAD -- DECISION_LOG.md HANDOFF.md | wc -l
       1
       1
~~~
~~~text
$ cat /tmp/f4c1/run.sh
#!/bin/bash
# prints each command line with a "$ " prefix, then runs that exact line (eval) in one bash shell
cd /Volumes/Sensidine/Praxis.build || exit 1
while IFS= read -r line <&3; do
  [ -z "$line" ] && continue
  printf '$ %s\n' "$line"
  eval "$line" 2>&1
done 3< "$1"
$ cat /tmp/f4c1/build.pl
# usage: perl build.pl template > section ; replaces each line "@@BLK name RANGES@@" with those chunks of /tmp/f4c1/out-name.txt (a chunk is one "$ " command line plus its output)
sub chunks { my $f = shift; open(my $h, "<", "/tmp/f4c1/out-$f.txt") or die "no $f"; my @c; while (<$h>) { if (/^\$ /) { push @c, $_ } else { die "orphan in $f" unless @c; $c[-1] .= $_ } } return @c }
while (<>) {
  if (/^\@\@BLK (\S+) (.+)\@\@$/) { my ($f, $spec) = ($1, $2); my @c = chunks($f); my @out;
    for my $r (split / /, $spec) { my ($a, $b) = split /-/, $r; $b = $a unless defined $b; die "range $f $r" if $b > @c; push @out, @c[$a-1 .. $b-1] }
    print "~~~text\n", @out, "~~~\n"; }
  else { print }
}
~~~

Reading. The pattern file has 5 distinct lines. Line 1 is the surname (10 characters), lines 2 to 4 are the three support names, and line 5 is the 16-hex thread id. The checks after it show that line 4 (the signature name) is also the sender name on transcript :1 and :18. Line 2 (the preview addressee) is the reply-1 respondent at the 2026-08-07 report :36. DECISION_LOG.md :435's greeting/signature pair is lines 3 and 4. The banned-word file holds the three strings the brief bans, typed so that none of them appears whole in this file. The S13 file is one 90-character line plus a newline. `/tmp/f4c1-lp.txt` holds the reply-1 address local part, for the per-file checks.

All other re-run blocks are in the in-scope files' Correction 1 sections (table below).

## Finding, cure, where

| # | Audit finding | Cure | Where (file : lines) |
|---|---|---|---|
| 1 | Manager report: V2, V7, V3 and V11 lines describe commands instead of showing them | V2, V7 and V3 are re-run with literal commands and unedited output, including V2's two placeholder-path lines. V11's byte-presence and grading-phrase lines are re-run. V11's per-file loop and index check are re-run after the last edit, in this report's Final checks | manager :466–502 (C1-V2), :503–539 (C1-V7), :540–596 (C1-V3), :713–748 (C1-V11); this report, Final checks |
| 2 | Manager V3: the echo-rc line with no exit-code variable, the annotated rc=0 line, and 779 plus eleven N: lines with no command | `git diff --quiet HEAD -- docs/reports/2026-08-07-f4-mffu-compliance-evidence.md; echo "rc=$?"` gives `rc=0`, and `wc -l` gives 779. A `grep -n` with `-i` gives the eleven lines plus 716. A case-sensitive `grep -n` prints exactly the eleven | manager :540–596 |
| 3 | Manager :40 negative has no pasted search | Twelve phrase probes over HEAD (`git grep -l -i -F`), the hit lines, the myfundedfutures files and their outgoing-phrase counts, three positive controls, and a working-tree search | manager :597–671 |
| 4 | Worker 2: no block shows a command; Block 3 line numbers off by one (25, 638, 641, 643) | Blocks 1 to 8 are re-run by the manager and labelled as the manager's. A table of corrected Block 3 numbers from `grep -n` shows six off by one (25→26, 638→639, 639→640, 641→642, 643→644, 644→645), and the Q1 answer's :641 and :643 are corrected to :642 and :644. Disagreements are stated plainly: Block 7's `-w F4` gives 496, not 634; Block 6's "remaining hits" note is only partly borne out; one Block 8 citation (r8j-wf-spec-manager :233) does not reproduce | worker2 :148–363 (C1-W3 :190–232; C1-W6 :267–290; C1-W7 :291–313; C1-W8 :314–363) |
| 5 | Workers 3 and 4 state probe results without output | Every item under "Checks that found nothing" is either re-run by the manager (labelled as such) or listed under "Not re-run" with the reason: draft-side evidence that no longer exists, or a reading rather than a probe. Differences of method are stated (worker 3's eight-word filter re-run in full). One disagreement is stated: a20 :487 has no F4 | worker3 :153–349; worker4 :85–238 |
| 6 | Manifest-manager: "unchanged" and the numstat claim are false for uncommitted rows | Both sentences are retracted. Numstat `13 0` (also against HEAD directly) and the two added hunks are pasted, with a scratch demonstration that an in-place edit of an uncommitted row leaves numstat unchanged. The 8 rows' unchanged state and the "8 0" pre-edit figure are marked UNVERIFIED | manifest-manager :98–157 |
| 7 | Manager :8 says the trader's name is replaced by `[trader]`, but the first name appears elsewhere | :8 is narrowed. `[trader]` is applied at :234, :393, :394, :400 and :402. The first name is used at :47, :55, :154, :188, :220, :290, :327–:329 and :412 (case-insensitive search), as the rubric uses it (rubric :3, :4, :13). What is withheld is the surname, the support names, the thread id and the addresses | manager :672–696 |

The manager section also corrects the :152 figure (C1-W, :697–712). No original count or line number was changed in place. Each correction says what the re-run shows.

## Adversarial findings and fixes

Three ADVERSARIAL dispatches were made. Each was given only the artifact files, the rubric lines and the audit findings, not the manager's reasoning.

1. **First dispatch** (all six files, all seven findings). It stopped at its 40-turn cap and left a 29-line skeleton, with `Result: pending` and no findings, at `docs/reports/2026-11-10-f4-grading-correction-1-worker1.md`. Its only partial output was that check C (labels and grading) "finds nothing". Nothing here rests on it.
2. **Adversary A** (manager report findings 1, 2, 3 and 7, plus this report's C1-V0 and table). It overwrote that skeleton, as instructed. FAIL: 1 blocking, 6 minor.
3. **Adversary B** (worker 2, 3 and 4 and manifest-manager, findings 4, 5 and 6). Report `docs/reports/2026-11-10-f4-grading-correction-1-worker2.md`. FAIL: 2 blocking, 5 minor.

The split into two scoped adversaries departs from the brief's "one ADVERSARIAL praxis-worker". It was made because the single worker could not finish the scope inside its turn cap.

| # | From | Severity | Finding | Fix |
|---|---|---|---|---|
| A1 | A | BLOCKING | Manager C1-V3 said 716 was extra "because the re-run uses `-i`"; without `-i`, 46 drops out too, so no shown command gave V3's eleven lines | A case-sensitive command added that prints exactly 28, 29, 34, 35, 36, 37, 44, 45, 46, 636 and 724. The reading now states the role of `-i` correctly (manager C1-V3) |
| A2 | A | MINOR | The first-name list missed :412 (lower case); the search was case-sensitive | Re-run with `-i -w`, plus a lower-case-only list. :412 added, and the lower-case lines named (manager C1-T) |
| A3 | A | MINOR | The V11 per-file loop and index check pointed to a placeholder | Filled: Final checks below |
| A4 | A | MINOR | Two outputs went stale after insertion: C1-V11's grading grep matched its own pasted output line, and `wc -l` gave 726 | The grading greps now print line numbers only (`cut -d: -f1`), so a pasted result cannot match itself. They were re-run after the sections were rebuilt, and the output is stable (`diff` of a fresh re-run against the pasted capture is empty, Final checks). The `wc -l` 460 is explained in the reading |
| A5 | A | MINOR | V2's `:250` placeholder line was not re-run literally | Re-run with the path held in `$T` (manager C1-V2, last command) |
| A6 | A | MINOR | Claims with no output in the section: the notes-3 :44 first name, the C1-W figures, "no label rests on either figure", and "only reports that quote the preview" | The notes-3 grep was added (C1-T). The C1-W block was pasted with a check that the element table holds neither "634" nor "Block 8". The "only reports that quote" wording was replaced by what the search shows (manager C1-V40) |
| A7 | A | MINOR | This report cited C1-V0 for a 17:38:16Z start and for the index state | The first-run `date -u` capture is pasted under Verification evidence. The index state points to Final checks |
| B1 | B | BLOCKING | Some "Checks that found nothing" items were neither re-run nor listed as not re-run: worker 4 :72–75; worker 3 :143, :144, and the :141 entries DECISIONS :285, a20 :487 and kit list :28 | Added worker 4 C1-Y6 (CONTRADICTED, Conditions, Grading check, Rows 4 and 14b) and worker 3 C1-X6 (row labels, scope-table quotes, grading sentences). The :141 entries are re-run in C1-X2: a20 :487 has no F4, which disagrees with worker 3, and this is said. The reading-only items are listed under "Not re-run". This report's table row 5 was reworded |
| B2 | B | BLOCKING | Worker 2 C1-W5 said the HANDOFF :784 span was in C1-W1, but C1-W1 cuts lines at 140 characters | Added a `grep -o` of both :784 spans to C1-W5 |
| B3 | B | MINOR | Worker 3 :141 does list eight words; the re-run used four | Re-run with all eight (12 hits) and the matched spans printed. None of the six extra hits claims closure of F4 (C1-X2) |
| B4 | B | MINOR | "names F4 once" — the command counts lines | Reworded: each line "contains F4", shown "at least once" (worker 2 C1-W8) |
| B5 | B | MINOR | Multi-string greps do not show each string; worker 2 Block 6 :90 and Block 8 :126, :130 and :133 were not re-run; worker 4 "byte-equal" was not compared; manifest "diff against HEAD" was not run as such; this report's start time | Per-string loops were added (worker 4 C1-Y2). Block 6's "remaining hits" were re-run and found only partly borne out, which is said. Block 8's :126, :130 and :133 references were re-run, and one (r8j-wf-spec-manager :233) does not reproduce, which is said. A `diff` was added for worker 4's byte-equal preview, and `git diff HEAD --numstat` for the manifest. The start time is as in A7 |

Both adversaries found that every other pasted figure reproduces, that no label, coverage reading or F4 grade was changed, and that personal data, banned strings and S13 placement were clean in the files they read. Both noted that the original text above each section cannot be compared byte for byte, because no copy from before the correction exists. See Final checks for the line-count check that does exist.

No third adversarial pass was run on these fixes.

## Observation for the master (outside this unit, not acted on)

The :40 search (manager C1-V40, last command) counted 48 lines in the HEAD report `docs/reports/2026-11-10-d9-housekeeping-manager.md` that match the pattern file of support names, surname and thread id. That report is committed and outside this unit's scope. It has not been read further or edited. Whether those lines are intended (that report records a "Kept, decided by manager under D1" choice) is for the master.

## S6 cross-block check

No deviation is approved or proposed. The correction changes evidence form in five untracked reports and touches no spec, ledger or block. The F3 and Block 4/5 couplings named in the manager report's S6 section are unchanged.

## Final checks

These checks were run after the last edit to every file of this unit: the five corrected reports, the untouched worker 1 report, the two adversary reports, and this report up to (but not including) the insertion of this block. The block adds no pattern-file hit, address, banned string, S13 line or grading phrase. A re-run after the insertion gave the same output from its fourth line on (the first three lines are the date and HEAD); the `diff` is pasted under the block. Per file, the loop shows: `pat`, lines matching any pattern-file entry (trader surname, three support names, thread id); `p1` to `p5`, the same for each entry; `lp`, the reply-1 address local part; `email`, lines matching an address regex; `bw`, lines with any of the three banned strings; `s13any`, lines containing the S13 sentence; `s13exact`, lines equal to it; `lastIsS13`, whether the last line equals it. The S13 sentence is read from `/tmp/f4c1-s13.txt` (extracted from rubric :136, C1-V0), so it is not typed here. The `correction-heading-lines` and `first-at` columns show one Correction 1 heading per corrected file, at the line equal to that file's length before any edit (460, 148, 153, 85 and 98, first-run capture above), so the original lines above each section kept their count. Byte-for-byte identity of that original text cannot be shown, because no copy from before the edit was kept. Every edit went through the head/tail script pasted below, which writes only between the heading and the last line. The grading-phrase hits outside this report are listed with `F4` printed as `F_4`, so that the pasted spans cannot match the search when it is re-run. They are the manager report's own V11 command line (:427), questions ("which HEAD documents say F4 is closed"), quoted search patterns, and the adversaries' quotes of those. The `for c` loop re-runs every command file whose output is pasted in the Correction 1 sections and compares each with its pasted capture.

~~~text
$ date -u; git rev-parse --short HEAD
Tue Nov 10 18:17:58 UTC 2026
d30ab4d
$ for f in manager worker1 worker2 worker3 worker4 manifest-manager correction-1-manager correction-1-worker1 correction-1-worker2; do p=docs/reports/2026-11-10-f4-grading-$f.md; printf '%-22s pat=%s' "$f" "$(grep -c -i -w -F -f /tmp/f4c1-pat.txt "$p")"; i=0; while IFS= read -r q; do i=$((i+1)); printf ' p%s=%s' "$i" "$(grep -c -i -w -F -- "$q" "$p")"; done < /tmp/f4c1-pat.txt; printf ' lp=%s email=%s bw=%s s13any=%s s13exact=%s lastIsS13=%s\n' "$(grep -c -i -w -F -f /tmp/f4c1-lp.txt "$p")" "$(grep -c -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$p")" "$(grep -c -i -F -f /tmp/f4c1-bw.txt "$p")" "$(grep -c -F -f /tmp/f4c1-s13.txt "$p")" "$(grep -c -x -F -f /tmp/f4c1-s13.txt "$p")" "$(tail -n 1 "$p" | grep -c -x -F -f /tmp/f4c1-s13.txt)"; done
manager                pat=0 p1=0 p2=0 p3=0 p4=0 p5=0 lp=0 email=0 bw=0 s13any=1 s13exact=1 lastIsS13=1
worker1                pat=0 p1=0 p2=0 p3=0 p4=0 p5=0 lp=0 email=0 bw=0 s13any=1 s13exact=1 lastIsS13=1
worker2                pat=0 p1=0 p2=0 p3=0 p4=0 p5=0 lp=0 email=0 bw=0 s13any=1 s13exact=1 lastIsS13=1
worker3                pat=0 p1=0 p2=0 p3=0 p4=0 p5=0 lp=0 email=0 bw=0 s13any=1 s13exact=1 lastIsS13=1
worker4                pat=0 p1=0 p2=0 p3=0 p4=0 p5=0 lp=0 email=0 bw=0 s13any=1 s13exact=1 lastIsS13=1
manifest-manager       pat=0 p1=0 p2=0 p3=0 p4=0 p5=0 lp=0 email=0 bw=0 s13any=1 s13exact=1 lastIsS13=1
correction-1-manager   pat=0 p1=0 p2=0 p3=0 p4=0 p5=0 lp=0 email=0 bw=0 s13any=1 s13exact=1 lastIsS13=1
correction-1-worker1   pat=0 p1=0 p2=0 p3=0 p4=0 p5=0 lp=0 email=0 bw=0 s13any=1 s13exact=1 lastIsS13=1
correction-1-worker2   pat=0 p1=0 p2=0 p3=0 p4=0 p5=0 lp=0 email=0 bw=0 s13any=1 s13exact=1 lastIsS13=1
$ for f in manager worker2 worker3 worker4 manifest-manager; do p=docs/reports/2026-11-10-f4-grading-$f.md; printf '%-17s correction-heading-lines=%s first-at=%s\n' "$f" "$(grep -c '^## Correction 1 (2026-11-10, after audit fail 1)$' "$p")" "$(grep -n '^## Correction 1 (2026-11-10, after audit fail 1)$' "$p" | head -1 | cut -d: -f1)"; done
manager           correction-heading-lines=1 first-at=460
worker2           correction-heading-lines=1 first-at=148
worker3           correction-heading-lines=1 first-at=153
worker4           correction-heading-lines=1 first-at=85
manifest-manager  correction-heading-lines=1 first-at=98
$ ls docs/reports/2026-11-10-f4-grading-*.md | grep -v correction-1-manager | xargs grep -n -E 'F4 (passes|is closed|is satisfied)|satisfie[s] F4' | cut -d: -f1,2 | sed 's/-[a-z]*-reply/-[name]-reply/'
docs/reports/2026-11-10-f4-grading-correction-1-worker1.md:52
docs/reports/2026-11-10-f4-grading-correction-1-worker1.md:90
docs/reports/2026-11-10-f4-grading-correction-1-worker2.md:90
docs/reports/2026-11-10-f4-grading-correction-1-worker2.md:116
docs/reports/2026-11-10-f4-grading-manager.md:427
docs/reports/2026-11-10-f4-grading-manifest-manager.md:36
docs/reports/2026-11-10-f4-grading-manifest-manager.md:45
docs/reports/2026-11-10-f4-grading-worker2.md:4
docs/reports/2026-11-10-f4-grading-worker3.md:237
docs/reports/2026-11-10-f4-grading-worker3.md:245
$ ls docs/reports/2026-11-10-f4-grading-*.md | grep -v correction-1-manager | xargs grep -n -o -E '.{0,40}(F4 (passes|is closed|is satisfied)|satisfie[s] F4).{0,10}' | cut -c1-150 | sed 's/-[a-z]*-reply/-[name]-reply/' | sed 's/F4/F_4/g'
docs/reports/2026-11-10-f4-grading-correction-1-worker1.md:52: -E "F_4 (passes|is closed|is satisfied)|satisfies F_4" manager 
docs/reports/2026-11-10-f4-grading-correction-1-worker1.md:90: -E "F_4 (passes|is closed|is satisfied)|satisfies F_4" manager 
docs/reports/2026-11-10-f4-grading-correction-1-worker2.md:90:its, in the excerpts below, states that F_4 is closed in its ow
docs/reports/2026-11-10-f4-grading-correction-1-worker2.md:116: | der]|effectively|confirms the PRAXIS|satisfies F_4|F_4 is (me
docs/reports/2026-11-10-f4-grading-manager.md:427: -E "F_4 (passes|is closed|is satisfied)|satisfies F_4" manager 
docs/reports/2026-11-10-f4-grading-manifest-manager.md:36:ed at HEAD and which HEAD documents say F_4 is closed, answered
docs/reports/2026-11-10-f4-grading-manifest-manager.md:45:ed at HEAD and which HEAD documents say F_4 is closed, answered
docs/reports/2026-11-10-f4-grading-worker2.md:4:t covered? Q2: which HEAD documents say F_4 is closed, satisfie
docs/reports/2026-11-10-f4-grading-worker3.md:237:28-f4-[name]-reply-filing.md:232:PRAXIS|satisfies F_4|F_4 is (me
docs/reports/2026-11-10-f4-grading-worker3.md:245: the span is part of a search pattern ("satisfies F_4|F_4 is (me
$ grep -c -E 'F4 (passes|is closed|is satisfied)|satisfie[s] F4' docs/reports/2026-11-10-f4-grading-correction-1-manager.md
0
$ git diff --cached --name-only | sed 's/-[a-z]*-reply/-[name]-reply/'; git diff --cached --name-only | wc -l
docs/reports/evidence/2026-10-28-mffu-[name]-reply.png
       1
$ git status --porcelain -- 'docs/reports/2026-11-10-f4-grading-*' MANIFEST.md
 M MANIFEST.md
?? docs/reports/2026-11-10-f4-grading-correction-1-manager.md
?? docs/reports/2026-11-10-f4-grading-correction-1-worker1.md
?? docs/reports/2026-11-10-f4-grading-correction-1-worker2.md
?? docs/reports/2026-11-10-f4-grading-manager.md
?? docs/reports/2026-11-10-f4-grading-manifest-manager.md
?? docs/reports/2026-11-10-f4-grading-worker1.md
?? docs/reports/2026-11-10-f4-grading-worker2.md
?? docs/reports/2026-11-10-f4-grading-worker3.md
?? docs/reports/2026-11-10-f4-grading-worker4.md
$ cat /tmp/f4c1/replace.sh
#!/bin/bash
# replace.sh FILE SECTION: replaces lines from the Correction 1 heading to the line before the last line with SECTION
f=$1; s=$2
k=$(grep -n '^## Correction 1 (2026-11-10, after audit fail 1)$' "$f" | head -1 | cut -d: -f1); n=$(wc -l < "$f")
{ head -n $((k-1)) "$f"; cat "$s"; tail -n 1 "$f"; } > /tmp/f4c1/new.md && cat /tmp/f4c1/new.md > "$f"
printf '%s heading-at=%s lines=%s\n' "$(basename "$f")" "$k" "$(wc -l < "$f")"
$ for c in c2 c3 c7 c40 cv11b cw2 cw3 cw4 cm; do bash /tmp/f4c1/run.sh /tmp/f4c1/$c.txt > /tmp/f4c1/rerun-$c.txt 2>&1; printf '%s %s\n' "$c" "$(cmp -s /tmp/f4c1/rerun-$c.txt /tmp/f4c1/out-$c.txt && echo same-as-pasted || echo DIFFERS)"; done
c2 same-as-pasted
c3 same-as-pasted
c7 same-as-pasted
c40 same-as-pasted
cv11b same-as-pasted
cw2 same-as-pasted
cw3 same-as-pasted
cw4 same-as-pasted
cm same-as-pasted
$ for c in c40; do diff /tmp/f4c1/out-$c.txt /tmp/f4c1/rerun-$c.txt | sed "s/-[a-z]*-reply/-[name]-reply/"; done
~~~

## Files staged

None by this unit. The six edited or new reports, and the adversary's report, are untracked. The index holds only the one PNG path (Final checks).

Result: PASS

This result is about whether correction 1 put pasted command output behind every claim the first audit named, and narrowed or retracted the two claims it named. It is not a result for F4, which is not graded here and stays FROZEN. The fixes for the adversaries' findings were not attacked by a further adversarial pass.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
