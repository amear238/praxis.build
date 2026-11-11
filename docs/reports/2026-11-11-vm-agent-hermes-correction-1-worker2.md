# Unit 2026-11-11-vm-agent-hermes-correction-1 — worker 2 (BUILD, S1 cure: re-run of every flagged evidence line)

## Task
The cold auditor graded unit 2026-11-10-vm-agent-hermes-ssh FAIL on S1. It flagged the manager report (`docs/reports/2026-11-10-vm-agent-hermes-ssh.md` :45, :53, :62, :65), worker 3 (:171–185 and the V6 block) and worker 4 (:72–132). For each flagged line or block, this report:
- quotes the original line;
- states my reading of the check it meant to show;
- re-runs a real command and pastes the raw output;
- gives a verdict: REPRODUCED, NOT REPRODUCED or DIFFERENT.

Mode: BUILD. My intent was to edit no file except this report, stage nothing, leave the git index and /tmp/idx-hermes alone, and only read `~/.hermes` (one `grep -c` and one `ls -l`). What can be shown is in "Fix-time evidence (worker 5)" below, and only at that level:
- the index digest equals the pre-dispatch value (a baseline from the manager's brief, not observed by this worker; quoted in "Worker 7 evidence" W7-1 and compared by command in W7-2: MATCH);
- the cached list is only the pre-staged PNG;
- the reply, DECISIONS.md and the handoff equal their pre-dispatch sha256 values (baselines from the manager's brief, W7-1; compared by command, W7-2: MATCH);
- HEAD is unchanged.

That /tmp/idx-hermes and `~/.hermes` were untouched is **not proven**, because there is no baseline for either. That no other file was edited by this worker cannot be shown from mtimes.

How the blocks below were produced. One bash script (`/bin/bash`, cwd `/Volumes/Sensidine/Praxis.build`) wrote this report.
- Every `$ ` line is the exact string the script ran. The lines under it are its raw stdout and stderr.
- The script's runner was `run(){ printf '$ %s\n' "$1"; eval "$1" 2>&1 | sed "s/$T/<the rep-name token>/g"; }`. Here `$T` is the rep-name token, taken by parameter expansion from the 2026-10-28 PNG filename and never typed. The sed only masks that token; it changes nothing else.
- Variable assignments (`SP`, `S13`, `IP`, `H`, `H4`, `H4e`) were run without the pipe so that they persist. They are pasted as `$ ` lines too.
- Original lines are quoted with an `awk` command that prefixes each line with `orig:<line number>: `. A quoted line that itself begins with `$ ` is the original report's text, not a command I ran.
- Code blocks use four-backtick fences, because some quoted lines are three-backtick fences.

Line numbers refer to the original files. The quotes come from the pre-edit snapshot copies in `/tmp/hermes-corr1-mgr-orig/`, because another worker is editing four lines of these reports at the same time.

Today is 2026-11-11. A re-run today shows what the files hold today. It is not proof of what a worker observed on 2026-11-10.

## Setup evidence
````
$ shasum -a 256 /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
07720470a99318d226327708d4592f0a5570c4c08871ac28cbbf5bc602bb9e12  /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md
16791c5a1606f4bfb682668f082cb19f9745bdc76e7da70ff0e5e8c76c58e77d  /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md
6ec6224f4121df0f3b42b30b18705eb72942caa810969e02d2debbb35a7e43d6  /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
$ git rev-parse HEAD; git log -1 --format=%cI HEAD
55979ee78b7bd6436c27d24c518f80b7a110f165
2026-11-10T13:27:44-05:00
$ stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S%z' vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md DECISIONS.md MANIFEST.md vm/2026-11-06-vm-handoff.md DECISION_LOG.md /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
2026-11-10T16:17:38-0500 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
2026-11-10T16:17:38-0500 DECISIONS.md
2026-11-10T16:17:38-0500 MANIFEST.md
2026-11-10T16:17:38-0500 vm/2026-11-06-vm-handoff.md
2026-11-11T09:50:52-0500 DECISION_LOG.md
2026-11-10T16:18:43-0500 /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md
2026-11-10T16:10:11-0500 /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md
2026-11-10T16:17:13-0500 /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
$ SP=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/af9aea76-b226-4610-b3fb-538269d1a642/scratchpad
$ ls -l $SP/CODE-vm-agent-hermes.draft.md $SP/s13.txt $SP/w4-entry.txt $SP/w4-am3.txt $SP/w4-man.txt | sed "s|$SP/|SP/|"
-rw-r--r--@ 1 admin  wheel  12815 Nov 10 16:07 SP/CODE-vm-agent-hermes.draft.md
-rw-r--r--@ 1 admin  wheel     91 Nov 10 16:02 SP/s13.txt
-rw-r--r--@ 1 admin  wheel    887 Nov 10 16:14 SP/w4-am3.txt
-rw-r--r--@ 1 admin  wheel   7643 Nov 10 16:14 SP/w4-entry.txt
-rw-r--r--@ 1 admin  wheel   2929 Nov 10 16:14 SP/w4-man.txt
$ S13="$(sed -n 136p specs/SPEC_RUBRIC.md | grep -o '"Fills [^"]*"' | head -1 | tr -d '"')"
$ printf '%s' "$S13" | wc -c; printf '%s\n' "$S13" | cmp - $SP/s13.txt && echo 'S13 var == SP/s13.txt'
      90
S13 var == SP/s13.txt
$ IP='([0-9]{1,3}\.){3}[0-9]{1,3}'
````
What the setup shows:
- The snapshot hashes match the ones in the brief (07720470…, 16791c5a…, 6ec6224f…). The brief's values are quoted in W7-1 as a baseline from the manager's brief (not observed by this worker), and W7-2 compares each snapshot file with them by command: MATCH.
- HEAD is `55979ee`, dated 2026-11-10T13:27-05:00. The reflog in "Fix-time evidence (worker 5)" has no HEAD movement after that commit. So "HEAD" today is the same revision that was HEAD throughout the 2026-11-10 workers' run. (The snapshot reports never name the hash, so this rests on the reflog, not on what they wrote.)
- The placed reply, DECISIONS.md, MANIFEST.md and the handoff all show mtime 2026-11-10T16:17:38-05:00, the placement time (21:17:38Z).
  - The manager report's snapshot mtime is 16:18:43, after placement. The inference is that its checks ran on the same file state as today. This is **inferred from mtimes, not proven**. An mtime is the time of the last write, and it says nothing about when the checks ran.
  - What hashes show covers only a narrower span. The reply, DECISIONS.md and the handoff equal their pre-dispatch sha256 baselines for correction-1 (from the manager's brief, W7-1; compared by command, W7-2: MATCH), both in the worker 5 block and at worker 7's run. That is equal content at those instants; two-point equality does not show that nothing changed in between. There is no baseline for MANIFEST.md.
  - Worker 3 (16:10:11) and worker 4 (16:17:13) last wrote their reports before the placement mtime. The inference is that when they ran, the reply was still the scratchpad draft with `__TS__` placeholders. This is inferred from mtimes, not proven.

Fix-time evidence (worker 5, 2026-11-11). It was run in the zsh tool shell, cwd repo root, with `SP` and `$T` as above:
- Each command went through `run(){ printf '$ %s\n' "$1"; eval "$1" 2>&1; }`, so each `$ ` line is the exact string run and the lines under it are its own raw output.
- The batch was piped through `sed "s/$T/<the rep-name token>/g"`. Worker 5 states that a case-insensitive leak-check of the masked output printed 0 before display, but that command and its output were not captured, so the statement is not evidence. Worker 7's leak-check commands and raw output (over this whole report, which contains this block, and over worker 7's own masked batches) are pasted in W7-3.
- `grep` in this shell is a function (`type grep` prints `grep is a shell function from /Users/admin/.claude/shell-snapshots/snapshot-zsh-1794408303558-icmlpi.sh`; `whence -p grep` prints `/usr/bin/grep`), so `command grep` (= /usr/bin/grep) is used. The `type grep` output depends on the environment: the function exists only in the interactive tool shell, and a non-interactive `zsh -c "type grep"` prints `grep is /usr/bin/grep` (W7-2). Also time-dependent in the block below: the stat mtimes and the reflog.
- `git status` runs with `--no-optional-locks`.
- The scratchpad path in `cmp` messages is shortened to `SP/` by the `sed` shown in the command.
````
$ type grep
grep is a shell function from /Users/admin/.claude/shell-snapshots/snapshot-zsh-1794408303558-icmlpi.sh
$ whence -p grep
/usr/bin/grep
$ git reflog -6 --date=iso | cut -c1-90
55979ee HEAD@{2026-11-10 13:27:44 -0500}: commit: docs: F4 comparison of MFFU written repl
d30ab4d HEAD@{2026-11-10 08:46:32 -0500}: commit: rubric: F1 PASSED@b4c3291 and D-2026-11-
b4c3291 HEAD@{2026-11-10 08:32:54 -0500}: commit: docs: F1 live-signal topology and F2 ses
a587a27 HEAD@{2026-11-10 05:23:36 -0500}: commit: docs: housekeeping 2b (D11 G18, G30; bea
16c7bfe HEAD@{2026-11-10 04:39:04 -0500}: commit: docs: scrub-forward of the withheld term
0eea766 HEAD@{2026-11-10 02:34:30 -0500}: commit: ledgers: housekeeping 2a (Amear D-2026-1
$ command grep -c 55979ee /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md:0
/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md:0
/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md:0
$ shasum -a 256 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md DECISIONS.md vm/2026-11-06-vm-handoff.md MANIFEST.md
2b729b8e4469a1c3454dadba08ddcd9e48a387f201e583c5e326f66569ce2ed0  vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
39e5ba0c27a1aab9736d6f23ce28efbb663bfcd1bcab5b5f305b2911669bc637  DECISIONS.md
ff4ba4ac512d9f59ed363563e49c88129a3da0864310f8bf6de2f714199c8c42  vm/2026-11-06-vm-handoff.md
3079813cd7c8cff560284e22acb2eefa0c3f6eac1f6bf68f4fb246ca06f0d955  MANIFEST.md
$ git ls-files -s | shasum -a 256
5ac1ef7d17ce98a5e256863a10288b12541a502959ffffe3ba79eb282e638ac6  -
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
$ stat -f "%Sm %N" -t "%Y-%m-%dT%H:%M:%S%z" /tmp/idx-hermes /tmp/hermes-corr1-mgr-orig /tmp/hermes-corr1-w1-orig vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md DECISIONS.md vm/2026-11-06-vm-handoff.md MANIFEST.md
2026-11-11T09:45:57-0500 /tmp/idx-hermes
2026-11-11T09:52:06-0500 /tmp/hermes-corr1-mgr-orig
2026-11-11T09:53:09-0500 /tmp/hermes-corr1-w1-orig
2026-11-10T16:17:38-0500 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
2026-11-10T16:17:38-0500 DECISIONS.md
2026-11-10T16:17:38-0500 vm/2026-11-06-vm-handoff.md
2026-11-10T16:17:38-0500 MANIFEST.md
$ awk "NR>=2075 && NR<=2076 {print NR\": \" substr(\$0,1,50)}" DECISIONS.md
2075: 
2076: ## 2026-11-10 — D-2026-11-10-C: VM agent = Herme
$ head -c 2 $SP/w4-am3.txt | od -c | head -1
0000000    +   -                                                        
$ cmp $SP/w4-am3.txt <(sed -n "23p" vm/2026-11-06-vm-handoff.md) 2>&1 | sed "s|$SP/|SP/|"; echo "rc=${pipestatus[1]}"
SP/w4-am3.txt /dev/fd/11 differ: char 1, line 1
rc=1
$ sed -e "s/^+//" -e "s/__TS__/20261110T211738Z/g" $SP/w4-am3.txt | cmp - <(sed -n "23p" vm/2026-11-06-vm-handoff.md); echo "rc=$?"
rc=0
$ cmp $SP/w4-entry.txt <(sed -n "2075,\$p" DECISIONS.md) 2>&1 | sed "s|$SP/|SP/|"; echo "rc=${pipestatus[1]}"
SP/w4-entry.txt /dev/fd/11 differ: char 2484, line 13
rc=1
$ sed "s/__TS__/20261110T211738Z/g" $SP/w4-entry.txt | cmp - <(sed -n "2075,\$p" DECISIONS.md); echo "rc=$?"; wc -l < $SP/w4-entry.txt; sed -n "2075,\$p" DECISIONS.md | wc -l
rc=0
      25
      25
$ sed "s/__TS__/20261110T211738Z/g" $SP/w4-man.txt | cmp - <(sed -n "364,371p" MANIFEST.md); echo "rc=$?"; wc -l < $SP/w4-man.txt
rc=0
       8
````
What the fix-time block shows:
- **HEAD.** It did not move after 2026-11-10 13:27:44 (reflog).
- **Protected files.** The reply, DECISIONS.md and the handoff equal their pre-dispatch hashes (2b729b8e…, 39e5ba0c…, ff4ba4ac…), which are baselines from the manager's brief (W7-1), compared by command in W7-2: MATCH. There is no baseline for MANIFEST.md.
- **Index.** The digest is 5ac1ef7d…8ac6, equal to the pre-dispatch baseline from the manager's brief (W7-1; W7-2: MATCH), and the cached list is only the PNG.
- **/tmp/idx-hermes.** There is no baseline, so its being untouched is **not proven**. Only its mtime (09:45:57) and current hash (`002b890c…2896`, from worker 5's run, pasted in worker 1's Step 5) are observable.
- **D-2026-11-10-C.** The heading is DECISIONS.md:2076, and :2075 is the blank line before it. The commands in this report use `2075,$`, which includes that one blank line. So entry-relative line 8 is :2082 and line 13 is :2087.
- **Placement-only-`__TS__`.** Worker 4's 16:14 pre-placement extracts were compared with today's files. Each compares equal once `__TS__` is replaced by `20261110T211738Z`, with rc=0 for all three:
  - `w4-entry.txt` vs DECISIONS.md :2075–2099, 25 lines each;
  - `w4-am3.txt` vs handoff :23, once the leading `+` is stripped (the extract holds the diff `+` line, as `od -c` shows);
  - `w4-man.txt` vs MANIFEST.md :364–371.

  The controls at fix time were weaker than first described (correction by worker 7). Without the substitution the entry differs (rc=1, char 2484, line 13). The Amendment 3 compare at :112–114 differs at char 1 because of the extract's diff `+`, so it is not a control for `__TS__`. MANIFEST had no control. Worker 7 ran both missing controls in W7-2: Amendment 3 with only the `+` stripped, and MANIFEST without substitution. W7-2 also prints the six bytes at each control's first difference, and all three are `__TS__`. The controls show the substitution is needed. The rc=0 positive compares show it is sufficient. So between those extracts and today, the only change in these ranges is `__TS__` → `20261110T211738Z`. The extracts are worker 4's copies from 16:14. They are not proof of worker 3's state at about 16:10.
- The draft still exists at `SP/CODE-vm-agent-hermes.draft.md` (mtime 16:07). Whether 16:07 is after all of worker 3's edits is not shown: worker 3's report was last written at 16:10:11 (setup :45), and an mtime records only the last write (correction by worker 7). The draft-only checks below are run against that file.
- `S13` is taken from the rubric line, so the sentence is not typed out in this report. It is byte-equal to `SP/s13.txt`, the pattern file worker 3 says it used (worker 3 :108).

## Per-claim re-runs

### A. Manager report `docs/reports/2026-11-10-vm-agent-hermes-ssh.md`

#### A1. :45–46
````
$ awk 'NR>=45 && NR<=46 {print "orig:" NR ": " $0}' /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md
orig:45: $ tail -1 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | grep -cxF '<the S13 sentence>'
orig:46: 1
````
Reading (worker 2): the placed reply's last line is exactly the S13 sentence (whole-line fixed-string match, count 1).

The literal pattern, as written on the line:
````
$ tail -1 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | grep -cxF '<the S13 sentence>'; echo "exit=$?"
0
exit=1
````
The corrected check, with the sentence in a variable:
````
$ tail -1 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | grep -cxF "$S13"
1
````
Verdict:
- **NOT REPRODUCED as written.** The literal command prints `0` and exits 1, not `1`. The line pasted a placeholder in place of the pattern it ran.
- **REPRODUCED with the corrected command.** The reply's last line is the S13 sentence (count 1).

#### A2. :53–61 (S13 counts)
````
$ awk 'NR>=53 && NR<=61 {print "orig:" NR ": " $0}' /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md
orig:53: $ S13 counts (grep -cF)
orig:54: vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md 1
orig:55: vm/2026-11-06-vm-handoff.md 1
orig:56: docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md 1
orig:57: docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md 1
orig:58: docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md 1
orig:59: docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md 1
orig:60: HEAD handoff 1
orig:61: DECISIONS :2075-end 1
````
Reading (worker 2): `grep -cF "$S13"` on each named file.
- "HEAD handoff" is the handoff at HEAD.
- "DECISIONS :2075-end" is DECISIONS.md from line 2075 to the end. :2075 is the blank line before the entry; the D-2026-11-10-C heading is :2076 (worker 5 block).
- The worker1–4 reports are run twice: as they are now in the working tree, and from the snapshot copies. Another worker is editing the working-tree copies, but on lines that do not hold the sentence (shown in correction-1-worker1 Step 4b, not in this report).
````
$ grep -cF "$S13" vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
1
$ grep -cF "$S13" vm/2026-11-06-vm-handoff.md
1
$ grep -cF "$S13" docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md:1
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md:1
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md:1
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md:1
$ grep -cF "$S13" /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker1.md /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker2.md /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker1.md:1
/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker2.md:1
/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md:1
/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md:1
$ git show HEAD:vm/2026-11-06-vm-handoff.md | grep -cF "$S13"
1
$ sed -n '2075,$p' DECISIONS.md | grep -cF "$S13"
1
````
Verdict: **REPRODUCED** on all eight rows (:54–:61). Each count is 1. The original rows showed no command; the commands above are my reading of what was meant.

#### A3. :62–64 (IPv4 grep on new reply + entry)
````
$ awk 'NR>=62 && NR<=64 {print "orig:" NR ": " $0}' /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md
orig:62: $ IPv4 grep on new reply + entry
orig:63:    1 /dev/fd/11:8:127.0.0.1
orig:64:    2 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:56:127.0.0.1
````
Reading (worker 2): an IPv4 `grep -noE`, numbered by `cat -n`. The entry was given by process substitution (hence a `/dev/fd/N` name) and the reply as a file. The claim is that the only address found is 127.0.0.1, at entry line 8 and reply line 56.
````
$ grep -noE "$IP" <(sed -n '2075,$p' DECISIONS.md) vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | cat -n
     1	/dev/fd/63:8:127.0.0.1
     2	vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:56:127.0.0.1
     3	vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:56:127.0.0.1
$ sed -n '56p' vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | grep -oE '.{0,12}127\.0\.0\.1.{0,6}'
 of `http://127.0.0.1:5678/
sing http://127.0.0.1:5678/
````
Verdict: **DIFFERENT**, in two ways.
- The fd number differs. That is cosmetic.
- The row count differs. `grep -noE` prints reply line 56 twice, because that line has two `127.0.0.1` matches, both `http://127.0.0.1:5678/`. The original block shows one row for line 56 and two rows in all. I cannot recover the command that gave two rows (a de-duplication is one possibility). That is UNVERIFIED.

The substantive finding is reproduced: the only IPv4 address in the entry and the reply is loopback 127.0.0.1, at entry line 8 (DECISIONS.md:2082) and reply line 56.

#### A4. :65–69 (timestamp count)
````
$ awk 'NR>=65 && NR<=69 {print "orig:" NR ": " $0}' /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md
orig:65: $ grep -c 20261110T211738Z
orig:66: vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:2
orig:67: vm/2026-11-06-vm-handoff.md:1
orig:68: MANIFEST.md:1
orig:69: DECISIONS.md:1
````
Reading (worker 2): a per-file count of lines holding `20261110T211738Z` in the reply, the handoff, MANIFEST.md and DECISIONS.md.

As written there is no file argument, so grep reads stdin. I gave it `/dev/null` as stdin so that the as-written form ends:
````
$ grep -c 20261110T211738Z </dev/null; echo "exit=$?"
0
exit=1
````
With the four file arguments explicit:
````
$ grep -c 20261110T211738Z vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md vm/2026-11-06-vm-handoff.md MANIFEST.md DECISIONS.md
vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:2
vm/2026-11-06-vm-handoff.md:1
MANIFEST.md:1
DECISIONS.md:1
````
Verdict:
- **NOT REPRODUCED as written.** The pasted command cannot print per-file counts. With no file argument it prints one bare count for stdin.
- **REPRODUCED with explicit files.** The output matches :66–69 exactly. For the reply, the handoff and DECISIONS.md, the content is the same at the correction-1 dispatch and at this fix: sha256 equals the pre-dispatch baselines from the manager's brief (worker 5 block; quoted in W7-1, compared by command in W7-2: MATCH). Two-point equality does not show that nothing changed in between. That they are unchanged since placement on 2026-11-10 is **inferred from mtimes, not proven**. MANIFEST.md has no hash baseline, so for it this rests on mtime only.

### B. Worker 3 `docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md`, V6 block :155–187 (contains the flagged :171–185)
````
$ awk 'NR>=155 && NR<=187 {print "orig:" NR ": " $0}' /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md
orig:155: V6. S13 counts, placeholders, IPs and hygiene. The pattern was read from a file so that this block does not repeat the sentence.
orig:156: ```
orig:157: S13 draft:
orig:158: 1
orig:159: draft last line is S13:
orig:160: 1
orig:161: S13 handoff WC:
orig:162: 1
orig:163: S13 handoff HEAD:
orig:164: 1
orig:165: S13 Amendment 3 line:
orig:166: 0
orig:167: S13 entry:          (sed -n '2075,$p' DECISIONS.md | grep -c)
orig:168: 1
orig:169: entry last line is S13:
orig:170: 1
orig:171: $ grep -n __TS__ (counts per line shown)
orig:172: draft:3:__TS__
orig:173: draft:8:__TS__
orig:174: draft:8:__TS__
orig:175: vm/2026-11-06-vm-handoff.md:23:__TS__
orig:176: vm/2026-11-06-vm-handoff.md:23:__TS__
orig:177: MANIFEST.md:364:__TS__
orig:178: DECISIONS.md:2087:__TS__
orig:179: $ IP grep draft
orig:180:    2 127.0.0.1
orig:181: $ IP grep entry
orig:182:    1 127.0.0.1
orig:183: $ IP grep Amendment 3
orig:184: 0
orig:185: $ hygiene: key path / fingerprint / user@host / launchctl / helper / breaker 5
orig:186: ```
orig:187: (The hygiene grep, `\.ssh|SHA256:|amear@|@praxis|launchctl|vmps|tunnel\.plist|#5|breaker 5` over the draft, the entry, Amendment 3 and MANIFEST :364–end, printed nothing.)
````
Which files these checks meant:
- Worker 3 ran before placement (see setup).
- "draft" was the scratchpad draft, which still exists at `SP/CODE-vm-agent-hermes.draft.md`.
- "entry" is DECISIONS.md :2076–end (heading at :2076). The commands use `2075,$`, which adds the one blank line :2075.
- "Amendment 3" is handoff :23.

The draft checks below are run on the draft. Where it matters, the placed reply is checked as well.

#### B1. :157–158 "S13 draft: 1"
Reading (worker 2): `grep -cF "$S13"` on the draft.
````
$ grep -cF "$S13" $SP/CODE-vm-agent-hermes.draft.md
1
````
Verdict: **REPRODUCED** (1).

#### B2. :159–160 "draft last line is S13: 1"
Reading (worker 2): `tail -1 draft | grep -cxF "$S13"`.
````
$ tail -1 $SP/CODE-vm-agent-hermes.draft.md | grep -cxF "$S13"
1
````
Verdict: **REPRODUCED** (1).

#### B3. :161–162 "S13 handoff WC: 1"
Reading (worker 2): the S13 count in the working-copy handoff.
````
$ grep -cF "$S13" vm/2026-11-06-vm-handoff.md
1
````
Verdict: **REPRODUCED** (1). It was run today, after placement. The worker 5 block shows that handoff :23 today equals worker 4's 16:14 pre-placement extract `w4-am3.txt`, once its diff `+` is stripped and `__TS__` is replaced by `20261110T211738Z` (cmp rc=0). That covers line 23 only. For the rest of the handoff, the only evidence is `git diff --numstat` (+1/−0, C2).

#### B4. :163–164 "S13 handoff HEAD: 1"
````
$ git show HEAD:vm/2026-11-06-vm-handoff.md | grep -cF "$S13"
1
````
Verdict: **REPRODUCED** (1).

#### B5. :165–166 "S13 Amendment 3 line: 0"
Reading (worker 2): the S13 count on handoff line 23 alone.
````
$ sed -n '23p' vm/2026-11-06-vm-handoff.md | grep -cF "$S13"; echo "exit=$?"
0
exit=1
````
Verdict: **REPRODUCED** (0).

#### B6. :167–168 "S13 entry: (sed -n '2075,$p' DECISIONS.md | grep -c) 1"
Reading (worker 2): the partial command on the line, completed with the pattern. It is run as written, as a regex (`grep -c`, no `-F`), and also as a fixed string.
````
$ sed -n '2075,$p' DECISIONS.md | grep -c "$S13"
1
$ sed -n '2075,$p' DECISIONS.md | grep -cF "$S13"
1
````
Verdict: **REPRODUCED** (1 both ways).

#### B7. :169–170 "entry last line is S13: 1"
Reading (worker 2): the entry runs to the end of DECISIONS.md (2099 lines; entry heading :2076, entry :2076–2099), so this is `tail -1 DECISIONS.md | grep -cxF`.
````
$ wc -l DECISIONS.md
    2099 DECISIONS.md
$ tail -1 DECISIONS.md | grep -cxF "$S13"
1
````
Verdict: **REPRODUCED** (1).

#### B8. :171–174 `grep -n __TS__` on the draft: 3, 8, 8
Reading (worker 2): the output form `file:line:__TS__`, with line 8 printed twice, is what `grep -no` gives (one row per match). "draft" is the scratchpad draft.
````
$ grep -no __TS__ $SP/CODE-vm-agent-hermes.draft.md
3:__TS__
8:__TS__
8:__TS__
````
Verdict: **REPRODUCED**: draft :3 once and :8 twice. The draft is the file worker 3 named.

#### B9–B11. :175–178 `__TS__` at handoff:23 (twice), MANIFEST.md:364, DECISIONS.md:2087
Reading (worker 2): the same `grep -no __TS__`, on the three live files, run before placement.
````
$ grep -no __TS__ vm/2026-11-06-vm-handoff.md MANIFEST.md DECISIONS.md; echo "exit=$?"
exit=1
$ grep -no 20261110T211738Z vm/2026-11-06-vm-handoff.md MANIFEST.md DECISIONS.md
vm/2026-11-06-vm-handoff.md:23:20261110T211738Z
vm/2026-11-06-vm-handoff.md:23:20261110T211738Z
MANIFEST.md:364:20261110T211738Z
DECISIONS.md:2087:20261110T211738Z
````
Worker 4 made scratch copies at 16:14, after worker 3's edits and before placement. They are extracts, so their line numbers are relative:
- `w4-am3.txt` line 1 is handoff :23.
- `w4-man.txt` line 1 is MANIFEST :364.
- `w4-entry.txt` line 1 is DECISIONS :2075, so its line 13 is :2087.
````
$ grep -no __TS__ $SP/w4-am3.txt $SP/w4-man.txt $SP/w4-entry.txt | sed "s|$SP/||"
w4-am3.txt:1:__TS__
w4-am3.txt:1:__TS__
w4-man.txt:1:__TS__
w4-entry.txt:13:__TS__
$ sed -n '1p' $SP/w4-entry.txt | cmp - <(sed -n '2075p' DECISIONS.md) && echo 'w4-entry line 1 == DECISIONS:2075'; sed -n '2p' $SP/w4-entry.txt | cmp - <(sed -n '2076p' DECISIONS.md) && echo 'w4-entry line 2 == DECISIONS:2076'
w4-entry line 1 == DECISIONS:2075
w4-entry line 2 == DECISIONS:2076
$ sed -n '1p' $SP/w4-man.txt | sed 's/__TS__/20261110T211738Z/g' | cmp - <(sed -n '364p' MANIFEST.md) && echo 'w4-man line 1 (TS substituted) == MANIFEST:364'
w4-man line 1 (TS substituted) == MANIFEST:364
````
Verdict: **DIFFERENT** on all three: B9 handoff:23 ×2, B10 MANIFEST:364, B11 DECISIONS:2087.
- Today the live files hold no `__TS__`; grep exits 1 with no output. At exactly the positions claimed, they now hold `20261110T211738Z`: handoff :23 twice, MANIFEST :364, DECISIONS :2087. Placement swapped each placeholder for the timestamp.
- Worker 4's 16:14 extracts still show `__TS__` at the matching positions.
- This is consistent with worker 3's claim. It is not proof of what worker 3 saw at about 16:10 on 2026-11-10: the extracts are another worker's copies, made about 4 minutes later.

#### B12. :179–180 "IP grep draft → 2 127.0.0.1"
Reading (worker 2): `grep -oE "$IP" draft | sort | uniq -c`.
````
$ grep -oE "$IP" $SP/CODE-vm-agent-hermes.draft.md | sort | uniq -c
   2 127.0.0.1
````
Verdict: **REPRODUCED** (2 × 127.0.0.1, both on line 56; see C1a).

#### B13. :181–182 "IP grep entry → 1 127.0.0.1"
````
$ sed -n '2075,$p' DECISIONS.md | grep -oE "$IP" | sort | uniq -c
   1 127.0.0.1
````
Verdict: **REPRODUCED**.

#### B14. :183–184 "IP grep Amendment 3 → 0"
````
$ sed -n '23p' vm/2026-11-06-vm-handoff.md | grep -cE "$IP"; echo "exit=$?"
0
exit=1
````
Verdict: **REPRODUCED** (0).

#### B15. :185 and :187 hygiene grep "printed nothing"
Reading (worker 2): the pattern given at :187, over the draft, the entry, Amendment 3 and MANIFEST :364–end; the placed reply is added. The counts are run first. The printing form is run only because every count is 0, so it can print no file contents.
````
$ H='\.ssh|SHA256:|amear@|@praxis|launchctl|vmps|tunnel\.plist|#5|breaker 5'
$ grep -cE "$H" $SP/CODE-vm-agent-hermes.draft.md vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | sed "s|$SP/|SP/|"
SP/CODE-vm-agent-hermes.draft.md:0
vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:0
$ sed -n '2075,$p' DECISIONS.md | grep -cE "$H"
0
$ sed -n '23p' vm/2026-11-06-vm-handoff.md | grep -cE "$H"
0
$ sed -n '364,$p' MANIFEST.md | grep -cE "$H"
0
$ { grep -nE "$H" $SP/CODE-vm-agent-hermes.draft.md; sed -n '2075,$p' DECISIONS.md | grep -nE "$H"; sed -n '23p' vm/2026-11-06-vm-handoff.md | grep -nE "$H"; sed -n '364,$p' MANIFEST.md | grep -nE "$H"; } | wc -l
       0
````
Verdict: **REPRODUCED**: zero matching lines in every file. The entry, Amendment 3 and MANIFEST rows checked are today's files (after placement). The worker 5 block compares worker 4's 16:14 pre-placement extracts against today's DECISIONS.md :2075–2099, handoff :23 (after stripping the extract's diff `+`) and MANIFEST.md :364–371. Each is equal once `__TS__` → `20261110T211738Z` (cmp rc=0 for all three). Neither string matches the pattern: `printf` of both strings through `command grep -cE "$H"` prints 0 (W7-2, run by worker 7; it was not run at fix time). This shows the extracts and today differ only in that string. It does not prove worker 3's state at about 16:10, because the extracts are another worker's copies made about 4 minutes later.

### C. Worker 4 `docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md` :72–132

#### C1. Block :71–89 (S13, IP, minus-lines, prefix, DL count)
````
$ awk 'NR>=71 && NR<=89 {print "orig:" NR ": " $0}' /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
orig:71: S13 counts, IP and key grep, minus-lines, DECISIONS prefix, DL line count:
orig:72: ```
orig:73: == CODE-vm-agent-hermes.draft.md: S13=1 IPs:
orig:74: 56:127.0.0.1
orig:75: == w4-entry.txt: S13=1 IPs:
orig:76: 8:127.0.0.1
orig:77: == w4-am3.txt: S13=0 IPs:
orig:78: == w4-man.txt: S13=0 IPs:
orig:79: == diff minus lines:
orig:80: 0
orig:81: == DECISIONS 1-2074 vs HEAD:
orig:82: IDENTICAL
orig:83:     2074
orig:84: == DL at HEAD:
orig:85:      810
orig:86: == handoff S13 in diff:
orig:87: 0
orig:88: ```
orig:89: (The grep for `.ssh|praxis_vm|SHA256:|fingerprint|user amear|amear@|@praxis-vm|192.168` printed nothing for all four files.)
````
Reading (worker 2):
- The four `==` rows are four scratch files, named in the block, each with an S13 `grep -cF` and an IPv4 `grep -noE`. They are the draft and worker 4's extracts `w4-entry.txt` (entry), `w4-am3.txt` (Amendment 3) and `w4-man.txt` (MANIFEST rows). All four still exist (setup `ls -l`), with mtimes from before worker 4's report.
- Four diff/HEAD checks follow.

C1a. :73–74 draft S13=1, IPs `56:127.0.0.1`
````
$ grep -cF "$S13" $SP/CODE-vm-agent-hermes.draft.md
1
$ grep -noE "$IP" $SP/CODE-vm-agent-hermes.draft.md
56:127.0.0.1
56:127.0.0.1
````
Verdict:
- S13=1: **REPRODUCED**.
- IPs: **DIFFERENT**. `grep -noE` prints `56:127.0.0.1` twice (two matches on line 56); the block shows it once. The distinct line:address pairs are the same. The command worker 4 ran is not shown, and is UNVERIFIED.

C1b. :75–76 w4-entry.txt S13=1, IPs `8:127.0.0.1`
````
$ grep -cF "$S13" $SP/w4-entry.txt
1
$ grep -noE "$IP" $SP/w4-entry.txt
8:127.0.0.1
````
Verdict: **REPRODUCED** (both). This runs on worker 4's own scratch file (mtime 16:14, before its report). The live entry gives the same IP result (A3 row 1).

C1c. :77 w4-am3.txt S13=0, no IPs
````
$ grep -cF "$S13" $SP/w4-am3.txt; grep -noE "$IP" $SP/w4-am3.txt; echo "exit=$?"
0
exit=1
````
Verdict: **REPRODUCED**.

C1d. :78 w4-man.txt S13=0, no IPs
````
$ grep -cF "$S13" $SP/w4-man.txt; grep -noE "$IP" $SP/w4-man.txt; echo "exit=$?"
0
exit=1
````
Verdict: **REPRODUCED**.

C1e. :79–80 "diff minus lines: 0"
Reading (worker 2): the count of removed lines in the working-tree diff of the three artifact files.
````
$ git diff -- DECISIONS.md MANIFEST.md vm/2026-11-06-vm-handoff.md | grep -c '^-[^-]'; echo "exit=$?"
0
exit=1
````
Verdict: **REPRODUCED** (0). It was run today, after placement. That placement changed only text inside added lines rests on two things:
- the zero minus-line count here, plus numstat (C2);
- the worker 5 extract comparisons, which cover the entry, handoff :23 and MANIFEST :364–371 only.

C1f. :81–83 "DECISIONS 1-2074 vs HEAD: IDENTICAL / 2074"
````
$ cmp <(git show HEAD:DECISIONS.md) <(head -2074 DECISIONS.md) && echo IDENTICAL
IDENTICAL
$ git show HEAD:DECISIONS.md | wc -l
    2074
````
Verdict: **REPRODUCED**.

C1g. :84–85 "DL at HEAD: 810"
````
$ git show HEAD:DECISION_LOG.md | wc -l
     810
````
Verdict: **REPRODUCED** (810).

C1h. :86–87 "handoff S13 in diff: 0"
Reading (worker 2): no added line in the handoff diff holds the S13 sentence.
````
$ git diff -- vm/2026-11-06-vm-handoff.md | grep '^+' | grep -cF "$S13"; echo "exit=$?"
0
exit=1
````
Verdict: **REPRODUCED** (0).

C1i. :89 "The grep for `.ssh|praxis_vm|SHA256:|fingerprint|user amear|amear@|@praxis-vm|192.168` printed nothing for all four files."
Reading (worker 2): an extended-regex grep with the pattern exactly as written, over this block's four files. Only counts and the matched tokens (`-o`) are printed, never line contents.
````
$ H4='.ssh|praxis_vm|SHA256:|fingerprint|user amear|amear@|@praxis-vm|192.168'
$ grep -cE "$H4" $SP/CODE-vm-agent-hermes.draft.md $SP/w4-entry.txt $SP/w4-am3.txt $SP/w4-man.txt | sed "s|$SP/||"
CODE-vm-agent-hermes.draft.md:3
w4-entry.txt:1
w4-am3.txt:1
w4-man.txt:8
$ grep -noE "$H4" $SP/CODE-vm-agent-hermes.draft.md $SP/w4-entry.txt $SP/w4-am3.txt $SP/w4-man.txt | sed "s|$SP/||"
CODE-vm-agent-hermes.draft.md:2:-ssh
CODE-vm-agent-hermes.draft.md:30:-ssh
CODE-vm-agent-hermes.draft.md:33:-ssh
w4-entry.txt:13:-ssh
w4-am3.txt:1:-ssh
w4-man.txt:1:-ssh
w4-man.txt:1:-ssh
w4-man.txt:2:-ssh
w4-man.txt:3:-ssh
w4-man.txt:4:-ssh
w4-man.txt:4:-ssh
w4-man.txt:5:-ssh
w4-man.txt:5:-ssh
w4-man.txt:6:-ssh
w4-man.txt:6:-ssh
w4-man.txt:7:-ssh
w4-man.txt:7:-ssh
w4-man.txt:8:-ssh
w4-man.txt:8:-ssh
````
The same files, with the dots escaped (`\.ssh`, `192\.168`). This is not what the line says; it is run only to locate the difference:
````
$ H4e='\.ssh|praxis_vm|SHA256:|fingerprint|user amear|amear@|@praxis-vm|192\.168'
$ grep -cE "$H4e" $SP/CODE-vm-agent-hermes.draft.md $SP/w4-entry.txt $SP/w4-am3.txt $SP/w4-man.txt | sed "s|$SP/||"
CODE-vm-agent-hermes.draft.md:0
w4-entry.txt:0
w4-am3.txt:0
w4-man.txt:0
````
Verdict: **NOT REPRODUCED.** The pattern as written matches in all four files: draft 3 lines, w4-entry 1, w4-am3 1, w4-man 8. The unescaped `.ssh` matches `-ssh`, which comes from names such as `praxis-vm-over-ssh` and `vm-agent-hermes-ssh`. So "printed nothing" is false for the pattern stated.
- With the dots escaped, every file gives 0. That is consistent with no key path, fingerprint, user@host or 192.168 address being present.
- Possible explanations: worker 4 ran an escaped or fixed-string form and wrote it down unescaped, or it did not run this grep. I cannot tell which; that is UNVERIFIED. The claim as written is not reproduced.

#### C2. :91–96 numstat block (no command shown)
````
$ awk 'NR>=91 && NR<=96 {print "orig:" NR ": " $0}' /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
orig:91: Numstat (additions only; Amendment 3 is +1/-0):
orig:92: ```
orig:93: 25	0	DECISIONS.md
orig:94: 16	0	MANIFEST.md
orig:95: 1	0	vm/2026-11-06-vm-handoff.md
orig:96: ```
````
Reading (worker 2): `git diff --numstat` over the three artifact files.
````
$ git diff --numstat -- DECISIONS.md MANIFEST.md vm/2026-11-06-vm-handoff.md
25	0	DECISIONS.md
16	0	MANIFEST.md
1	0	vm/2026-11-06-vm-handoff.md
````
Verdict: **REPRODUCED**.

#### C3. :97 MANIFEST hunks
````
$ awk 'NR>=97 && NR<=97 {print "orig:" NR ": " $0}' /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
orig:97: MANIFEST hunks: `@@ -306,0 +307,8 @@` (not this unit's) and `@@ -355,0 +364,8 @@` (this unit's rows 364–371).
````
Reading (worker 2): the zero-context hunk headers of the MANIFEST diff.
````
$ git diff -U0 -- MANIFEST.md | grep '^@@'
@@ -306,0 +307,8 @@
@@ -355,0 +364,8 @@
````
Verdict: **REPRODUCED**.

#### C4. Quote checks :99–108
````
$ awk 'NR>=99 && NR<=108 {print "orig:" NR ": " $0}' /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
orig:99: Quote checks:
orig:100: ```
orig:101: DECISIONS quote: EXACT substring of DL:813
orig:102: DL hits for [If you accept, write a CODE- r]: 1
orig:103: DL hits for [set up outside this session]: 1
orig:104: 1   (handoff: "the two SKILL.md copies into your skills directory (steps 2 and 4)")
orig:105: 1   (skill: "the file's wording wins")
orig:106: 1   (DECISIONS:1090 "VM agent reads and reports the NT8 version")
orig:107: 1   (handoff:173 "If he does it by hand")
orig:108: ```
````
C4a. :101 "DECISIONS quote: EXACT substring of DL:813"

Reading (worker 2):
- DL is DECISION_LOG.md, the working copy. At HEAD it has 810 lines, so :813 exists only in the working copy.
- "DECISIONS quote" is the text block in D-2026-11-10-C that holds Amear's words, "copied by script from that line". That block is DECISIONS.md:2082.
- The test: is line 2082 a substring of DECISION_LOG.md:813?
````
$ awk 'NR>=2079 && NR<=2083 {print "DECISIONS:" NR ": " substr($0,1,60)}' DECISIONS.md
DECISIONS:2079: **Authority:** Amear's proposal, DECISION_LOG.md:813 (row 20
DECISIONS:2080: 
DECISIONS:2081: ```text
DECISIONS:2082: The Mac's Hermes agent can now drive the Windows VM over SSH
DECISIONS:2083: ```
$ sed -n '813p' DECISION_LOG.md | cut -c1-60
- [2026-11-10T20:42:00Z] WHO: amear | WHAT: **Amear proposes
$ python3 -I - <<'EOF'
d = open("DECISIONS.md", encoding="utf-8").read().split("\n")
l = open("DECISION_LOG.md", encoding="utf-8").read().split("\n")
q, t = d[2081], l[812]
print("quote=DECISIONS.md:2082 len", len(q), "| DL:813 len", len(t))
print("substring:", q in t, "| occurrences:", t.count(q), "| equal:", q == t)
EOF
quote=DECISIONS.md:2082 len 754 | DL:813 len 1262
substring: True | occurrences: 1 | equal: False
````
Verdict: **REPRODUCED.** DECISIONS.md:2082 (754 characters) is an exact substring of DECISION_LOG.md:813 (1262 characters), once. It is a substring, not the whole line.

C4b. :102 `DL hits for [If you accept, write a CODE- r]: 1`
````
$ grep -cF 'If you accept, write a CODE- r' DECISION_LOG.md
1
````
Verdict: **REPRODUCED** (1).

C4c. :103 `DL hits for [set up outside this session]: 1`
````
$ grep -cF 'set up outside this session' DECISION_LOG.md
1
$ grep -nF 'set up outside this session' DECISION_LOG.md | cut -d: -f1; wc -l DECISION_LOG.md
813
     820 DECISION_LOG.md
````
Verdict: **REPRODUCED** (1, at :813). DECISION_LOG.md has grown to 820 lines since 2026-11-10 (mtime 2026-11-11), and the count is still 1.

C4d. :104 `1 (handoff: "the two SKILL.md copies into your skills directory (steps 2 and 4)")`
````
$ grep -cF 'the two SKILL.md copies into your skills directory (steps 2 and 4)' vm/2026-11-06-vm-handoff.md
1
````
Verdict: **REPRODUCED** (1).

C4e. :105 `1 (skill: "the file's wording wins")`

Reading (worker 2): "skill" is Hermes's skill `~/.hermes/skills/devops/praxis-vm-over-ssh/SKILL.md`, the file worker 4 calls "Hermes skill" at :41. The two repo VM skills are checked too.
````
$ ls -l ~/.hermes/skills/devops/praxis-vm-over-ssh/SKILL.md
-rw-r--r--@ 1 admin  staff  6625 Nov 10 15:13 /Users/admin/.hermes/skills/devops/praxis-vm-over-ssh/SKILL.md
$ grep -cF "the file's wording wins" ~/.hermes/skills/devops/praxis-vm-over-ssh/SKILL.md vm/skills/praxis-vm-reporter/SKILL.md vm/skills/praxis-nt8-bridge-backtest/SKILL.md
/Users/admin/.hermes/skills/devops/praxis-vm-over-ssh/SKILL.md:1
vm/skills/praxis-vm-reporter/SKILL.md:0
vm/skills/praxis-nt8-bridge-backtest/SKILL.md:0
````
Verdict: **REPRODUCED** (1, in Hermes's skill only). The Hermes skill's mtime (2026-11-10 15:13) is before the unit's reports.

C4f. :106 `1 (DECISIONS:1090 "VM agent reads and reports the NT8 version")`
````
$ sed -n '1090p' DECISIONS.md | grep -cF 'VM agent reads and reports the NT8 version'
1
$ git show HEAD:DECISIONS.md | sed -n '1090p' | grep -cF 'VM agent reads and reports the NT8 version'
1
````
Verdict: **REPRODUCED** (1, in the working copy and at HEAD).

C4g. :107 `1 (handoff:173 "If he does it by hand")`
````
$ sed -n '173p' vm/2026-11-06-vm-handoff.md | grep -cF 'If he does it by hand'
1
````
Verdict: **REPRODUCED** (1).

#### C5. Citation spot-checks :110–132 ("sed -n; 20 checked, all point where they say")
````
$ awk 'NR>=110 && NR<=132 {print "orig:" NR ": " $0}' /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
orig:110: Citation spot-checks (sed -n; 20 checked, all point where they say):
orig:111: ```
orig:112: --- D:1086  | 3 — "the VM's Cowork agent" | none given | The master adopts a working definition: the Claude agent running inside the Windows VM …
orig:113: --- D:1090  | 7 — who reads the NT8 version | "VM agent reads and reports the NT8 version" | …
orig:114: --- D:1092  | 9 — VM agent on Z: | "VM agent on Z: while Code runs = second session, coordinate" | …
orig:115: --- D:1231  7. Bridge items: (4) playbackrun/… (11) pip may download only the bridge's pinned requirements, into its own venv under C:\praxis\. …
orig:116: --- D:2047  ## 2026-11-10 — D-2026-11-10-B: live-signal topology adopted as the working design …
orig:117: --- D:1907  D1  Default-decide. …
orig:118: --- D:1919  D4  Loop: a Hermes timer starts a fresh Code session every four hours.
orig:119: --- D:1912  D2  Only four things stop and wait for Amear's word: (a) spending
orig:120: --- D:1916      permissions. Everything else is D1.
orig:121: --- D:1230  6. Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". …
orig:122: --- topology:78  … So option 1 is recommended, and option 3 is the fallback
orig:123: --- topology:89  | B4 | n8n down or Redis unreachable. | …
orig:124: --- topology:90  | B5 | Anything that can POST to the webhook. | … **waits for Amear (D2(d))** …
orig:125: --- topology:98  | OPEN-T1 | Can an NT8 strategy in the VM reach the Mac's n8n webhook over HTTP? | …
orig:126: --- W:27  - [ ] before real money: isolate the VM — remove the shared folder …
orig:127: --- W:35  - [ ] **Go-live checklist, his words:** "unmap Z: and turn the share off before real money" …
orig:128: --- W:38  - [ ] **Go-live checklist addendum 2026-11-07, his words (ruling 10):** "remove the unauthenticated bridge request folders …
orig:129: --- W:39  - [ ] **Go-live checklist addendum 2026-11-09, his words (C3 (4)):** …
orig:130: --- DL:813  [2026-11-10T20:42:00Z] WHO: amear | WHAT: **Amear proposes Hermes over SSH as the VM agent …
orig:131: --- DL:814  [2026-11-10T20:43:00Z] WHO: praxis-master | WHAT: **Accept Hermes over SSH as the VM agent, decided by master under D-2026-11-08-D D1 …
orig:132: ```
````
Reading (worker 2): each `--- KEY:N  text` row claims that line N of the file KEY holds the shown text, where "…" marks text left out. The keys are:
- D = DECISIONS.md.
- topology = `docs/specs/2026-11-10-live-signal-topology.md`, the F1 topology doc (it holds B4, B5 and OPEN-T1).
- W = `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md`. Worker 2's report (:67) calls it "walkthrough :26–27, :35, :38, :39".
- DL = DECISION_LOG.md.

The script below reads the 20 rows from the snapshot, so nothing is retyped. It splits each shown text on "…" and checks that every non-empty segment occurs in the cited line, in order.
````
$ python3 -I - <<'EOF'
import re
m = {"D": "DECISIONS.md", "topology": "docs/specs/2026-11-10-live-signal-topology.md",
     "W": "docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md", "DL": "DECISION_LOG.md"}
src = open("/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md", encoding="utf-8").read().split("\n")
n = ok = 0
for i in range(111, 131):
    g = re.match(r"^--- (\w+):(\d+)  (.*)$", src[i])
    if not g:
        print("w4:%d UNPARSED" % (i + 1)); continue
    k, ln, shown = g.group(1), int(g.group(2)), g.group(3)
    line = open(m[k], encoding="utf-8").read().split("\n")[ln - 1]
    pos, good = 0, True
    for seg in [x.strip() for x in shown.split("…")]:
        if not seg: continue
        j = line.find(seg, pos)
        if j < 0: good = False; break
        pos = j + len(seg)
    n += 1; ok += good
    print("w4:%d %s:%d match=%s | %s" % (i + 1, k, ln, good, line[:60]))
print("rows parsed:", n, "| all segments found:", ok)
EOF
w4:112 D:1086 match=True | | 3 — "the VM's Cowork agent" | none given | The master adop
w4:113 D:1090 match=True | | 7 — who reads the NT8 version | "VM agent reads and report
w4:114 D:1092 match=True | | 9 — VM agent on Z: | "VM agent on Z: while Code runs = sec
w4:115 D:1231 match=True | 7. Bridge items: (4) playbackrun/reconnect/flatten/strategie
w4:116 D:2047 match=True | ## 2026-11-10 — D-2026-11-10-B: live-signal topology adopted
w4:117 D:1907 match=True | D1  Default-decide. When a unit or the master reaches a ques
w4:118 D:1919 match=True | D4  Loop: a Hermes timer starts a fresh Code session every f
w4:119 D:1912 match=True | D2  Only four things stop and wait for Amear's word: (a) spe
w4:120 D:1916 match=True |     permissions. Everything else is D1.
w4:121 D:1230 match=True | 6. Strategy Analyzer tab: a hand-set tab may be used for 2a 
w4:122 topology:78 match=True | Option 3 has the fewest unbuilt parts, because NT8 already h
w4:123 topology:89 match=True | | B4 | n8n down or Redis unreachable. | Not applicable: no f
w4:124 topology:90 match=True | | B5 | Anything that can POST to the webhook. | Yes, it pass
w4:125 topology:98 match=True | | OPEN-T1 | Can an NT8 strategy in the VM reach the Mac's n8
w4:126 W:27 match=True | - [ ] before real money: isolate the VM — remove the shared 
w4:127 W:35 match=True | - [ ] **Go-live checklist, his words:** "unmap Z: and turn t
w4:128 W:38 match=True | - [ ] **Go-live checklist addendum 2026-11-07, his words (ru
w4:129 W:39 match=True | - [ ] **Go-live checklist addendum 2026-11-09, his words (C3
w4:130 DL:813 match=True | - [2026-11-10T20:42:00Z] WHO: amear | WHAT: **Amear proposes
w4:131 DL:814 match=True | - [2026-11-10T20:43:00Z] WHO: praxis-master | WHAT: **Accept
rows parsed: 20 | all segments found: 20
````
Verdict: **REPRODUCED** for all 20 rows (`match=True` on each), and the count claim "20 checked" matches `rows parsed: 20`. The D rows below :2075 are identical to HEAD (C1f). DL:813 and :814 exist only in the working copy.

## Summary table

| # | file:line (original) | claim | verdict |
|---|---|---|---|
| 1 | manager :45–46 | as written: `tail -1 reply \| grep -cxF '<the S13 sentence>'` → 1 | NOT REPRODUCED (literal gives 0, exit 1) |
| 2 | manager :45–46 | intended: reply last line is the S13 sentence | REPRODUCED (with `$S13`) |
| 3 | manager :54 | S13 count reply = 1 | REPRODUCED |
| 4 | manager :55 | S13 count handoff = 1 | REPRODUCED |
| 5 | manager :56 | S13 count worker1 = 1 | REPRODUCED |
| 6 | manager :57 | S13 count worker2 = 1 | REPRODUCED |
| 7 | manager :58 | S13 count worker3 = 1 | REPRODUCED |
| 8 | manager :59 | S13 count worker4 = 1 | REPRODUCED |
| 9 | manager :60 | S13 count handoff at HEAD = 1 | REPRODUCED |
| 10 | manager :61 | S13 count DECISIONS :2075–end = 1 | REPRODUCED |
| 11 | manager :62–64 | IPv4 rows: entry :8, reply :56 (2 rows) | DIFFERENT (reply :56 has 2 matches, so 3 rows; fd number differs; only address is 127.0.0.1) |
| 12 | manager :65 | as written: `grep -c 20261110T211738Z` (no file) → 4 per-file counts | NOT REPRODUCED (no file arg gives one stdin count) |
| 13 | manager :66–69 | per-file counts 2/1/1/1 | REPRODUCED (explicit files) |
| 14 | worker3 :157–158 | S13 draft = 1 | REPRODUCED |
| 15 | worker3 :159–160 | draft last line is S13 = 1 | REPRODUCED |
| 16 | worker3 :161–162 | S13 handoff WC = 1 | REPRODUCED |
| 17 | worker3 :163–164 | S13 handoff HEAD = 1 | REPRODUCED |
| 18 | worker3 :165–166 | S13 Amendment 3 = 0 | REPRODUCED |
| 19 | worker3 :167–168 | S13 entry = 1 | REPRODUCED |
| 20 | worker3 :169–170 | entry last line is S13 = 1 | REPRODUCED |
| 21 | worker3 :171–174 | `__TS__` draft :3, :8, :8 | REPRODUCED |
| 22 | worker3 :175–176 | `__TS__` handoff :23 ×2 | DIFFERENT (live file now has timestamp there; pre-placement state seen only in worker 4's 16:14 extract) |
| 23 | worker3 :177 | `__TS__` MANIFEST :364 | DIFFERENT (same reason) |
| 24 | worker3 :178 | `__TS__` DECISIONS :2087 | DIFFERENT (same reason) |
| 25 | worker3 :179–180 | IP draft: 2 × 127.0.0.1 | REPRODUCED |
| 26 | worker3 :181–182 | IP entry: 1 × 127.0.0.1 | REPRODUCED |
| 27 | worker3 :183–184 | IP Amendment 3 = 0 | REPRODUCED |
| 28 | worker3 :185, :187 | hygiene grep printed nothing | REPRODUCED (0 in every file, today's files) |
| 29 | worker4 :73 | draft S13 = 1 | REPRODUCED |
| 30 | worker4 :74 | draft IPs `56:127.0.0.1` (once) | DIFFERENT (`grep -noE` prints it twice) |
| 31 | worker4 :75–76 | w4-entry S13 = 1, IP `8:127.0.0.1` | REPRODUCED |
| 32 | worker4 :77 | w4-am3 S13 = 0, no IP | REPRODUCED |
| 33 | worker4 :78 | w4-man S13 = 0, no IP | REPRODUCED |
| 34 | worker4 :79–80 | diff minus lines = 0 | REPRODUCED |
| 35 | worker4 :81–83 | DECISIONS 1–2074 identical to HEAD; HEAD 2074 lines | REPRODUCED |
| 36 | worker4 :84–85 | DL at HEAD 810 lines | REPRODUCED |
| 37 | worker4 :86–87 | handoff S13 in diff = 0 | REPRODUCED |
| 38 | worker4 :89 | hygiene grep (pattern as written) printed nothing for all four files | NOT REPRODUCED (matches `-ssh` in all four: 3/1/1/8) |
| 39 | worker4 :91–96 | numstat 25/16/1, 0 deletions | REPRODUCED |
| 40 | worker4 :97 | MANIFEST hunks `-306,0 +307,8` and `-355,0 +364,8` | REPRODUCED |
| 41 | worker4 :101 | DECISIONS quote is exact substring of DL:813 | REPRODUCED |
| 42 | worker4 :102 | DL hits "If you accept, write a CODE- r" = 1 | REPRODUCED |
| 43 | worker4 :103 | DL hits "set up outside this session" = 1 | REPRODUCED |
| 44 | worker4 :104 | handoff quote count = 1 | REPRODUCED |
| 45 | worker4 :105 | skill quote count = 1 | REPRODUCED (Hermes skill) |
| 46 | worker4 :106 | DECISIONS:1090 quote = 1 | REPRODUCED |
| 47 | worker4 :107 | handoff:173 quote = 1 | REPRODUCED |
| 48 | worker4 :110 | 20 citations checked | REPRODUCED (20 rows parsed) |
| 49–68 | worker4 :112–131 | 20 citations point where they say (D:1086, 1090, 1092, 1231, 2047, 1907, 1919, 1912, 1916, 1230; topology:78, 89, 90, 98; W:27, 35, 38, 39; DL:813, 814) | REPRODUCED (20 of 20 `match=True`) |

Totals over the 68 rows: **REPRODUCED 60, NOT REPRODUCED 3, DIFFERENT 5.**
- NOT REPRODUCED: manager :45 (as written), manager :65 (as written), worker4 :89.
- DIFFERENT: manager :62–64, worker3 :175–176, :177, :178, worker4 :74.
- Manager :45 and :65 each have two rows: one for the command as written, one for the intended check.

## Result
Result: PASS for this unit of work. Every flagged line and block now has a real command with raw output, and a verdict that is not softened.

The verdicts do not all reproduce the original claims, and this report does not cure them:
- Three claims fail as written: manager :45, manager :65, worker4 :89.
- Five show different output: manager :62–64, worker3 :175–178 (three rows), worker4 :74.
- In every NOT REPRODUCED and DIFFERENT case, the substantive property still holds today:
  - the S13 placement is correct;
  - the timestamp counts are right;
  - the only IP present is loopback;
  - no key path, fingerprint, user@host or 192.168 address is present under the escaped pattern.

How the original reports are amended is for the manager.

No figure in this report is a backtest or P&L figure. The S13 sentence is carried below as house style.

## Worker 7 evidence (2026-11-11)

Worker 7 added this section after the Result, so that the line numbers cited by worker 5's fix log and by worker 6 stay valid. Every reworded line above was replaced one line for one line. The section cures worker 6's findings B1-B6. No verdict, row or total was changed.

### W7-1. Baselines from the manager's brief (not observed by this worker)
These are quoted as text from the manager's brief to worker 7. They are not command output:
````
baseline from the manager's brief (not observed by this worker):
  2026-11-10-vm-agent-hermes-ssh.md          07720470a99318d226327708d4592f0a5570c4c08871ac28cbbf5bc602bb9e12
  2026-11-10-vm-agent-hermes-ssh-worker3.md  16791c5a1606f4bfb682668f082cb19f9745bdc76e7da70ff0e5e8c76c58e77d
  2026-11-10-vm-agent-hermes-ssh-worker4.md  6ec6224f4121df0f3b42b30b18705eb72942caa810969e02d2debbb35a7e43d6
  CODE- reply                                2b729b8e4469a1c3454dadba08ddcd9e48a387f201e583c5e326f66569ce2ed0
  DECISIONS.md                               39e5ba0c27a1aab9736d6f23ce28efbb663bfcd1bcab5b5f305b2911669bc637
  vm/2026-11-06-vm-handoff.md                ff4ba4ac512d9f59ed363563e49c88129a3da0864310f8bf6de2f714199c8c42
  HANDOFF.md                                 71cf456c349ba85b039818b33dc1135218b77ccd78ce37352b5b246ae1cb02a4
  STATUS.md                                  c06e4b26120ac3c37607d06d6424b9628aa8bcbf6c67adc62a91cdc74bd92564
  PNG                                        15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992
  git ls-files -s | shasum -a 256            5ac1ef7d17ce98a5e256863a10288b12541a502959ffffe3ba79eb282e638ac6
````

### W7-2. Compares, controls and probes, run by command
How it was run:
- The shell was the zsh tool shell, not this report's /bin/bash, with cwd /Volumes/Sensidine/Praxis.build.
- Each command went through `run(){ printf '$ %s\n' "$1"; eval "$1" 2>&1 </dev/null; }`. So each `$ ` line is the exact string run, and the lines under it are its own raw output.
- The batch was piped through `sed "s/$T/<the rep-name token>/g"` into `$OUT`. Its leak-check is in W7-3.
- The last command, `zsh -c "type grep"`, ran in the same call outside the masked batch. Its output cannot hold the token.

Some outputs depend on time or environment:
- the `date` line and the stat times;
- the `/dev/fd/N` names;
- `type grep`, which shows the function only in the interactive tool shell, against `zsh -c "type grep"`.

The awk reads lines 1-127 of this report. Those lines hold the setup and worker 5's pasted output, and worker 7's one-for-one rewording did not change their numbers.
````
$ f=$(ls docs/reports/evidence/ | command grep '^2026-10-28-mffu-.*-reply\.png$'); T=${f#2026-10-28-mffu-}; T=${T%-reply.png}
$ M=/tmp/hermes-corr1-mgr-orig; W2=docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md; SP=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/af9aea76-b226-4610-b3fb-538269d1a642/scratchpad
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-11T15:41:58Z
$ git rev-parse HEAD
55979ee78b7bd6436c27d24c518f80b7a110f165
$ shasum -a 256 $M/2026-11-10-vm-agent-hermes-ssh.md; [ "$(shasum -a 256 < $M/2026-11-10-vm-agent-hermes-ssh.md | cut -d" " -f1)" = 07720470a99318d226327708d4592f0a5570c4c08871ac28cbbf5bc602bb9e12 ] && echo MATCH || echo MISMATCH
07720470a99318d226327708d4592f0a5570c4c08871ac28cbbf5bc602bb9e12  /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md
MATCH
$ shasum -a 256 $M/2026-11-10-vm-agent-hermes-ssh-worker3.md; [ "$(shasum -a 256 < $M/2026-11-10-vm-agent-hermes-ssh-worker3.md | cut -d" " -f1)" = 16791c5a1606f4bfb682668f082cb19f9745bdc76e7da70ff0e5e8c76c58e77d ] && echo MATCH || echo MISMATCH
16791c5a1606f4bfb682668f082cb19f9745bdc76e7da70ff0e5e8c76c58e77d  /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md
MATCH
$ shasum -a 256 $M/2026-11-10-vm-agent-hermes-ssh-worker4.md; [ "$(shasum -a 256 < $M/2026-11-10-vm-agent-hermes-ssh-worker4.md | cut -d" " -f1)" = 6ec6224f4121df0f3b42b30b18705eb72942caa810969e02d2debbb35a7e43d6 ] && echo MATCH || echo MISMATCH
6ec6224f4121df0f3b42b30b18705eb72942caa810969e02d2debbb35a7e43d6  /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
MATCH
$ shasum -a 256 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md; [ "$(shasum -a 256 < vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | cut -d" " -f1)" = 2b729b8e4469a1c3454dadba08ddcd9e48a387f201e583c5e326f66569ce2ed0 ] && echo MATCH || echo MISMATCH
2b729b8e4469a1c3454dadba08ddcd9e48a387f201e583c5e326f66569ce2ed0  vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
MATCH
$ shasum -a 256 DECISIONS.md; [ "$(shasum -a 256 < DECISIONS.md | cut -d" " -f1)" = 39e5ba0c27a1aab9736d6f23ce28efbb663bfcd1bcab5b5f305b2911669bc637 ] && echo MATCH || echo MISMATCH
39e5ba0c27a1aab9736d6f23ce28efbb663bfcd1bcab5b5f305b2911669bc637  DECISIONS.md
MATCH
$ shasum -a 256 vm/2026-11-06-vm-handoff.md; [ "$(shasum -a 256 < vm/2026-11-06-vm-handoff.md | cut -d" " -f1)" = ff4ba4ac512d9f59ed363563e49c88129a3da0864310f8bf6de2f714199c8c42 ] && echo MATCH || echo MISMATCH
ff4ba4ac512d9f59ed363563e49c88129a3da0864310f8bf6de2f714199c8c42  vm/2026-11-06-vm-handoff.md
MATCH
$ shasum -a 256 HANDOFF.md; [ "$(shasum -a 256 < HANDOFF.md | cut -d" " -f1)" = 71cf456c349ba85b039818b33dc1135218b77ccd78ce37352b5b246ae1cb02a4 ] && echo MATCH || echo MISMATCH
71cf456c349ba85b039818b33dc1135218b77ccd78ce37352b5b246ae1cb02a4  HANDOFF.md
MATCH
$ shasum -a 256 STATUS.md; [ "$(shasum -a 256 < STATUS.md | cut -d" " -f1)" = c06e4b26120ac3c37607d06d6424b9628aa8bcbf6c67adc62a91cdc74bd92564 ] && echo MATCH || echo MISMATCH
c06e4b26120ac3c37607d06d6424b9628aa8bcbf6c67adc62a91cdc74bd92564  STATUS.md
MATCH
$ shasum -a 256 "docs/reports/evidence/$f"; [ "$(shasum -a 256 < "docs/reports/evidence/$f" | cut -d" " -f1)" = 15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992 ] && echo MATCH || echo MISMATCH
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
MATCH
$ git ls-files -s | shasum -a 256; [ "$(git ls-files -s | shasum -a 256 | cut -d" " -f1)" = 5ac1ef7d17ce98a5e256863a10288b12541a502959ffffe3ba79eb282e638ac6 ] && echo MATCH || echo MISMATCH
5ac1ef7d17ce98a5e256863a10288b12541a502959ffffe3ba79eb282e638ac6  -
MATCH
$ awk 'NR<=127 && /^(07720470a99318d226327708d4592f0a5570c4c08871ac28cbbf5bc602bb9e12|16791c5a1606f4bfb682668f082cb19f9745bdc76e7da70ff0e5e8c76c58e77d|6ec6224f4121df0f3b42b30b18705eb72942caa810969e02d2debbb35a7e43d6|2b729b8e4469a1c3454dadba08ddcd9e48a387f201e583c5e326f66569ce2ed0|39e5ba0c27a1aab9736d6f23ce28efbb663bfcd1bcab5b5f305b2911669bc637|ff4ba4ac512d9f59ed363563e49c88129a3da0864310f8bf6de2f714199c8c42|5ac1ef7d17ce98a5e256863a10288b12541a502959ffffe3ba79eb282e638ac6)  / {print NR": " substr($0,1,8) "... " substr($0,67)}' $W2
32: 07720470... /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md
33: 16791c5a... /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md
34: 6ec6224f... /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
91: 2b729b8e... vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
92: 39e5ba0c... DECISIONS.md
93: ff4ba4ac... vm/2026-11-06-vm-handoff.md
96: 5ac1ef7d... -
$ sed -e "s/^+//" $SP/w4-am3.txt | cmp - <(sed -n "23p" vm/2026-11-06-vm-handoff.md); echo "rc=$?"
stdin /dev/fd/14 differ: char 156, line 1
rc=1
$ sed -e "s/^+//" $SP/w4-am3.txt | head -c 161 | tail -c 6; echo
__TS__
$ cmp $SP/w4-man.txt <(sed -n "364,371p" MANIFEST.md) 2>&1 | sed "s|$SP/|SP/|"; echo "rc=${pipestatus[1]}"
SP/w4-man.txt /dev/fd/11 differ: char 15, line 1
rc=1
$ head -c 20 $SP/w4-man.txt | tail -c 6; echo
__TS__
$ cmp $SP/w4-entry.txt <(sed -n "2075,\$p" DECISIONS.md) 2>&1 | sed "s|$SP/|SP/|"; echo "rc=${pipestatus[1]}"
SP/w4-entry.txt /dev/fd/11 differ: char 2484, line 13
rc=1
$ head -c 2489 $SP/w4-entry.txt | tail -c 6; echo
__TS__
$ command grep -c __TS__ $SP/w4-am3.txt $SP/w4-entry.txt $SP/w4-man.txt | sed "s|$SP/|SP/|"
SP/w4-am3.txt:1
SP/w4-entry.txt:1
SP/w4-man.txt:1
$ H='\.ssh|SHA256:|amear@|@praxis|launchctl|vmps|tunnel\.plist|#5|breaker 5'
$ printf "%s\n" __TS__ 20261110T211738Z | command grep -cE "$H"; echo "exit=$?"
0
exit=1
$ stat -f "%Sm %N" -t "%Y-%m-%dT%H:%M:%S%z" $SP/CODE-vm-agent-hermes.draft.md $M/2026-11-10-vm-agent-hermes-ssh-worker3.md | sed "s|$SP/|SP/|"
2026-11-10T16:07:56-0500 SP/CODE-vm-agent-hermes.draft.md
2026-11-10T16:10:11-0500 /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md
$ type grep
grep is a shell function from /Users/admin/.claude/shell-snapshots/snapshot-zsh-1794408303558-icmlpi.sh
$ zsh -c "type grep"
grep is /usr/bin/grep
````
What W7-2 shows:
- **Baselines (B2).** The three manager snapshot files, the reply, DECISIONS.md, the handoff, HANDOFF.md, STATUS.md, the PNG and the index digest each MATCH the W7-1 baseline. The awk shows that the values pasted at :32-34, :91-93 and :96 are the same baseline strings. This is equality at the dispatch and at 15:41Z; it does not show that nothing changed in between.
- **Controls (B4).** Each control is an extract compared with today's file without the `__TS__` substitution:
  - Amendment 3, with only the diff `+` stripped, differs at char 156 (rc=1).
  - MANIFEST differs at char 15 (rc=1).
  - The entry differs at char 2484 (rc=1).

  The six bytes at each first difference are `__TS__`, and each extract has `__TS__` on exactly one line (`grep -c` counts lines, not occurrences). So each control fails where the substitution acts, and the rc=0 compares at :115-116, :120-121 and :124-125 pass with it. cmp reports only the first difference. That the substitution is the only change rests on the rc=0 compares, not on the controls.
- **B5, :447.** Neither `__TS__` nor `20261110T211738Z` matches `$H`: the count is 0 and the exit status is 1.
- **B5, :140.** The draft's mtime is 16:07:56. Worker 3's report was last written at 16:10:11. An mtime records only the last write, so neither time shows the order of worker 3's edits.
- **B6.** `type grep` depends on the environment, as shown by the last two commands.

### W7-3. Leak-check (B1)
The W7-2 batch (all lines before `zsh -c`) was masked into `$OUT`. It was counted for the token, case-insensitive, before display. Command and output:
````
$ print -r -- "$OUT" | command grep -ci -- "$T"
0
````
Next is the count over the whole of both reports, run in a separate call. It ran after W7-2 was in place and before this W7-3 text and the worker 7 fix-log entries were added. That this later text holds no rep-name token is not shown in this report (an uncaptured statement, not evidence); the count over this file after the last edit is pasted in the manager report, block E6 [manager edit 2026-11-11, adversarial finding C2].
````
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-11T15:43:04Z
$ command grep -ci -- "$T" docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md:0
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md:0
````
This replaces worker 5's uncaptured leak-check at :70 as the evidence for "no token in the pasted output" (B1). Worker 5's own leak-check output remains not shown.

## Fix log (worker 5, 2026-11-11)
- :10–16 (was :10): this worker's claims about itself (no other file edited, index and /tmp/idx-hermes untouched, `~/.hermes` read only) are reworded to the observed level. /tmp/idx-hermes and `~/.hermes` are marked not proven (scan finding, same class as A3).
- :62 (was :56): "same HEAD" is now backed by the reflog. It also notes that the snapshot reports do not name the hash (scan finding).
- :64–66 (was :58–59): the mtime-based claims (manager checks ran on today's state; worker 3 and worker 4 ran before placement) are marked "inferred from mtimes, not proven". The span that hashes do prove is stated (A6).
- :68–141 (new fix-time evidence block) (A5, A6, A7):
  - `type grep` and `whence -p grep`, and the reflog;
  - sha256 of the reply, DECISIONS.md, the handoff and MANIFEST.md, against the pre-dispatch values;
  - the index digest, the cached list, and stat;
  - DECISIONS.md :2075 (blank) and :2076 (heading);
  - worker 4's three pre-placement extracts compared with today's entry, handoff :23 and MANIFEST :364–371. Correction by worker 7: there was one real negative control, for the entry. The Amendment 3 "control" differs at char 1, on the diff `+`, and MANIFEST had none. The proper controls are in W7-2.
- :185 (was :105), :301 (was :221), :357 (was :277): the D-2026-11-10-C heading is now cited as :2076. The `2075,$` in the commands is explained as adding one blank line. No command or output was changed (A7).
- :186 (was :106): the claim that the other worker edits "lines that do not hold the sentence" now cites its source (scan finding).
- :259 (was :179): "unchanged since placement" is reworded. It is hash-proven since the correction-1 dispatch for three files and inferred from mtimes since placement; MANIFEST rests on mtime only (A6).
- :328 (was :248): "placement changed only `__TS__` on handoff :23" is now backed by the worker 5 cmp, rc=0 (A5).
- :447 (was :367): the same claim for the entry, Amendment 3 and the MANIFEST rows is backed by the worker 5 cmps, with the limit that the extracts are worker 4's 16:14 copies (A5).
- :522–524 (was :442): "placement changed only text inside added lines" is tied to the evidence it rests on, and its coverage is stated (scan finding).
- No verdict was changed. The summary table and totals are unchanged.
- worker 7, 2026-11-11 (cures worker 6's B1-B6). Every reworded line above :876 was replaced one line for one line, so all earlier line citations, including worker 5's above, still hold:
  - :11, :13 (B2): "equals the pre-dispatch value" now names the source, a baseline from the manager's brief, with the quote (W7-1) and the MATCH compare (W7-2).
  - :61 (B2): "match the ones in the brief" now points to the quoted baselines and the by-command compare.
  - :65 (B2, B5): two-point hash equality is no longer called "unchanged from that dispatch to this fix". It now says equal content at two instants, with nothing shown in between.
  - :70 (B1): worker 5's "leak-check printed 0" is marked as an uncaptured statement, not evidence. The pasted leak-checks are in W7-3.
  - :71 (B6): the `type grep` output is marked environment-dependent, with `zsh -c` in W7-2. The stat mtimes and the reflog are named as time-dependent.
  - :130, :131 (B2): the protected-file and index claims name the brief baseline and the W7-2 compare.
  - :139 (B4): the description of the controls is corrected. Only the entry had a real control at fix time; the Amendment 3 one differs at char 1, on the `+`; MANIFEST had none. The proper controls are in W7-2.
  - :140 (B5): "after worker 3's edits" is withdrawn as not shown.
  - :259 (B2, B5): the baseline source is named, and two-point equality is no longer called "unchanged".
  - :447 (B5): "Neither string matches the pattern" is now backed by the command in W7-2, with the note that it was not run at fix time.
  - :1022 (was :885 before this section was inserted; worker 5's fix-log entry) (B4): "with negative controls" is corrected to what the controls show.
  - :876-1011 (new): the "Worker 7 evidence" section. W7-1 (:880) quotes the brief baselines as text. W7-2 (:896) holds the runner and the command output: 10 MATCH compares; an awk tying the pasted values at :32-34, :91-93 and :96 to the baselines; the Amendment 3 (`+` stripped) and MANIFEST controls, with the entry control re-run, and the six bytes at each first difference; the `$H` check; the draft and worker 3 mtimes; `type grep` against `zsh -c`. Its reading is at :985. W7-3 (:997) holds the leak-checks.
  - No verdict, row, total or pasted output of worker 2 or worker 5 was changed.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
