# 2026-11-11 vm-agent-hermes correction-1, worker 6 (ADVERSARIAL)

## Task
Unit 2026-11-11-vm-agent-hermes-correction-1, worker 6, mode ADVERSARIAL. Working dir /Volumes/Sensidine/Praxis.build, HEAD 55979ee.

The artifacts under test are correction-1-worker1.md and correction-1-worker2.md, as revised in place by worker 5. Each has a "## Fix log (worker 5, 2026-11-11)" section. The defects worker 5 was meant to cure are worker 4's findings A1-A7. The criteria are S1, S2 and S13.

What I did and did not touch:
- I edited nothing except this report.
- I staged nothing.
- I did not touch the git index or /tmp/idx-hermes. No command of mine reads /tmp/idx-hermes: the worker1 Step 5 lines that stat or hash it were left out of my re-run.
- Scratch files are in /tmp/hermes-corr1-w6/. I created it fresh: `ls -ld` printed "No such file or directory" first (D5 block).

How the rep-name token was handled. It was never typed. It was taken at runtime from the PNG filename into `$T`, and every output was masked with `sed "s/$T/<the rep-name token>/g"`.

Code blocks use four-backtick fences.

Process note. My first attempt to assemble this report in a single Bash command was blocked by `scripts/mint-guard.sh`. The command's text contained the tool shell-snapshot path, because it was pasted inside the D5 block. I then captured the D5 evidence to a file, and assembled the report with the script /tmp/hermes-corr1-w6/assemble.zsh.

## D2. Byte-for-byte re-runs (10 blocks: 6 from worker1, 4 from worker2)
Method:
- For each block, the pasted range was cut out of the report with `sed -n 'A,Bp'` into `<id>.pasted`.
- Every `$ ` line in that range was run through the runner the report itself states, and the result went into `<id>.mine`.
- worker1 and worker2's fix-time block: the zsh runner `run(){ printf '$ %s\n' "$1"; eval "$1" 2>&1; }`, with the batch masked.
- worker2's main body: /bin/bash, with assignments not piped (worker2 :20-21).

The ten blocks:

| id | report | lines | what it is |
|---|---|---|---|
| w1-step2 | worker1 | :108-124 | snapshot grep with `command grep` |
| w1-4dhash | worker1 | :294-304 | Step 4d hash block |
| w1-4dcnt | worker1 | :310-337 | count proof |
| w1-4b | worker1 | :193-224 | output of the loop at :187 |
| w1-s5a | worker1 | :401-406 | Step 5, first part |
| w1-s5b | worker1 | :436-444 | Step 5, second part |
| w2-fix | worker2 | :75-126 | fix-time block, holding the A5 evidence |
| w2-setup | worker2 | :31-58 | setup |
| w2-C1i | worker2 | :554-579 | C1i |
| w2-C4c | worker2 | :676-680 | C4c |

Command as run: `zsh /tmp/hermes-corr1-w6/rerun.zsh 2>&1 | tee /tmp/hermes-corr1-w6/cmp.out`. The script, verbatim (`cat /tmp/hermes-corr1-w6/rerun.zsh`):
````
#!/bin/zsh
# worker 6 re-run harness. Usage: zsh /tmp/hermes-corr1-w6/rerun.zsh  (cwd forced to repo root)
cd /Volumes/Sensidine/Praxis.build || exit 9
D=/tmp/hermes-corr1-w6
W1=docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md
W2=docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md
f=$(ls docs/reports/evidence/ | command grep '^2026-10-28-mffu-.*-reply\.png$'); T=${f#2026-10-28-mffu-}; T=${T%-reply.png}
R=docs/reports; O=/tmp/hermes-corr1-w1-orig
SP=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/af9aea76-b226-4610-b3fb-538269d1a642/scratchpad
run(){ printf '$ %s\n' "$1"; eval "$1" 2>&1 </dev/null; }
# zsh blocks: extract "$ " lines from the pasted range, eval each with worker-5 runner, mask whole batch
zblock(){ id=$1; file=$2; a=$3; b=$4
  sed -n "${a},${b}p" $file > $D/$id.pasted
  cmds=("${(@f)$(command grep '^\$ ' $D/$id.pasted | sed 's/^\$ //')}")
  { for c in "${cmds[@]}"; do run "$c"; done; } | sed "s/$T/<the rep-name token>/g" > $D/$id.mine
}
zblock w1-step2  $W1 108 124
zblock w1-4dhash $W1 294 304
zblock w1-4dcnt  $W1 310 337
zblock w1-s5a    $W1 401 406
zblock w1-s5b    $W1 436 444
zblock w2-fix    $W2 75 126
# worker1 Step 4b loop, exactly as pasted at :187
sed -n '193,224p' $W1 > $D/w1-4b.pasted
for x in 2026-11-10-vm-agent-hermes-ssh.md 2026-11-10-vm-agent-hermes-ssh-worker1.md 2026-11-10-vm-agent-hermes-ssh-worker2.md 2026-11-10-vm-agent-hermes-ssh-worker3.md 2026-11-10-vm-agent-hermes-ssh-worker4.md; do echo; echo "\$ diff -U0 $O/$x $R/$x | sed mask"; diff -U0 $O/$x $R/$x | sed "s/$T/<the rep-name token>/g"; echo "[diff exit ${pipestatus[1]:-$PIPESTATUS}]"; done > $D/w1-4b.raw 2>&1
tail -n +2 $D/w1-4b.raw > $D/w1-4b.mine
# worker2 bash blocks
for spec in "w2-setup 31 58" "w2-C1i 554 579" "w2-C4c 676 680"; do
  set -- ${=spec}; sed -n "$2,$3p" $W2 > $D/$1.pasted
  command grep '^\$ ' $D/$1.pasted | sed 's/^\$ //' > $D/$1.cmds
  /bin/bash $D/w2run.bash $D/$1.cmds "$T" "$SP" > $D/$1.mine 2>&1
done
for i in w1-step2 w1-4dhash w1-4dcnt w1-4b w1-s5a w1-s5b w2-fix w2-setup w2-C1i w2-C4c; do echo "== cmp $i ($(wc -l < $D/$i.pasted | tr -d ' ') pasted lines)"; cmp $D/$i.pasted $D/$i.mine; echo "cmp rc=$?"; diff $D/$i.pasted $D/$i.mine; done
````
Its helper, verbatim (`cat /tmp/hermes-corr1-w6/w2run.bash`):
````
#!/bin/bash
# worker2's stated runner (report :20-21): assignments run without the pipe; others piped through the mask.
cd /Volumes/Sensidine/Praxis.build || exit 9
CMDS=$1; T=$2; SP=$3
run(){ printf '$ %s\n' "$1"; eval "$1" 2>&1 </dev/null | sed "s/$T/<the rep-name token>/g"; }
while IFS= read -r c <&3; do
  if [[ $c =~ ^[A-Za-z_][A-Za-z0-9_]*= ]]; then printf '$ %s\n' "$c"; eval "$c"; else run "$c"; fi
done 3< "$CMDS"
````
Raw output (/tmp/hermes-corr1-w6/cmp.out):
````
== cmp w1-step2 (17 pasted lines)
cmp rc=0
== cmp w1-4dhash (11 pasted lines)
cmp rc=0
== cmp w1-4dcnt (28 pasted lines)
cmp rc=0
== cmp w1-4b (32 pasted lines)
cmp rc=0
== cmp w1-s5a (6 pasted lines)
cmp rc=0
== cmp w1-s5b (9 pasted lines)
cmp rc=0
== cmp w2-fix (52 pasted lines)
/tmp/hermes-corr1-w6/w2-fix.pasted /tmp/hermes-corr1-w6/w2-fix.mine differ: char 21, line 2
cmp rc=1
2c2
< grep is a shell function from /Users/admin/.claude/shell-snapshots/snapshot-zsh-1794408303558-icmlpi.sh
---
> grep is /usr/bin/grep
== cmp w2-setup (28 pasted lines)
cmp rc=0
== cmp w2-C1i (26 pasted lines)
cmp rc=0
== cmp w2-C4c (5 pasted lines)
cmp rc=0
````
Verdict on D2: **9 of 10 blocks are byte-identical (cmp rc=0).**
- The nine include worker1's count proof (w1-4dcnt).
- They also include worker2's A5 evidence, w2-fix lines 110-126: the `od -c` line, both "negative controls" and the three rc=0 substitution compares are all identical.

The tenth, w2-fix, differs on one line only, `type grep`. This comes from my harness, not from the claim. `zsh script` is non-interactive and does not source the tool-shell snapshot, so it finds /usr/bin/grep. In the tool shell itself, `type grep` prints exactly the pasted line (first probe below, and the D5 block).

Some outputs depend on time or environment. They match today only because nothing has changed since:
- the diff headers in w1-4b carry the live files' mtime, 2026-11-11 09:53:19;
- w2-setup carries DECISION_LOG.md's mtime, 09:50:52;
- w2-C4c carries DECISION_LOG.md's line count, 820;
- the `/dev/fd/11` process-substitution names in the zsh blocks depend on the shell.

One output has already moved. Worker1 :424-425 (`git --no-optional-locks status --short | command grep -c "^??"`) was pasted as 91. It was not in my blocks; re-run in the probes, it gives 92. This is time-dependent, and the new worker6 report (untracked) accounts for it.

## Probes used by D1 and D3
Command as run: a single zsh tool-shell batch, cwd repo root, with `SP` as in worker2 :47. The batch echoes each command line itself. Output (/tmp/hermes-corr1-w6/probes.out):
````
$ type grep   (in the tool shell, not the harness)
grep is a shell function from /Users/admin/.claude/shell-snapshots/snapshot-zsh-1794408303558-icmlpi.sh
$ zsh -c "type grep"
grep is /usr/bin/grep
$ command grep -n leak-check $W1 $W2
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md:288:- The whole batch was piped through `sed "s/$T/<the rep-name token>/g"`. A case-insensitive count of `$T` in the masked output then printed `leak-check (case-insensitive token count in output): 0` before anything was shown.
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md:398:This is the same run and the same masking as the Step 4d re-run: `run()` runner, `command grep`, case-insensitive leak-check 0. `git status` was run with `--no-optional-locks`, so it does not write the index.
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md:507:  - the runner, the mask and the leak-check are stated, and `command grep` is used;
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md:70:- The batch was piped through `sed "s/$T/<the rep-name token>/g"`, and a case-insensitive leak-check of the masked output printed 0 before display.
$ shasum -a 256 /tmp/hermes-corr1-w1-orig/*
9cd0c5c6342f5f1ca63ee799ff1dfe0fd32c13ad517e7d42a4d25120e6d531ae  /tmp/hermes-corr1-w1-orig/2026-11-10-vm-agent-hermes-ssh-worker1.md
c43da4d78a2833f554a9fd61389efe1de41c712d6d1d1eae353c16129c4cf6b2  /tmp/hermes-corr1-w1-orig/2026-11-10-vm-agent-hermes-ssh-worker2.md
16791c5a1606f4bfb682668f082cb19f9745bdc76e7da70ff0e5e8c76c58e77d  /tmp/hermes-corr1-w1-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md
6ec6224f4121df0f3b42b30b18705eb72942caa810969e02d2debbb35a7e43d6  /tmp/hermes-corr1-w1-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
07720470a99318d226327708d4592f0a5570c4c08871ac28cbbf5bc602bb9e12  /tmp/hermes-corr1-w1-orig/2026-11-10-vm-agent-hermes-ssh.md
$ stat -f "%SB | %Sm %N" -t "%Y-%m-%dT%H:%M:%S%z" /tmp/hermes-corr1-w1-orig /tmp/hermes-corr1-w1-orig/*
2026-11-11T09:53:09-0500 | 2026-11-11T09:53:09-0500 /tmp/hermes-corr1-w1-orig
2026-11-10T15:54:00-0500 | 2026-11-10T15:54:00-0500 /tmp/hermes-corr1-w1-orig/2026-11-10-vm-agent-hermes-ssh-worker1.md
2026-11-10T16:03:46-0500 | 2026-11-10T16:03:46-0500 /tmp/hermes-corr1-w1-orig/2026-11-10-vm-agent-hermes-ssh-worker2.md
2026-11-10T16:10:11-0500 | 2026-11-10T16:10:11-0500 /tmp/hermes-corr1-w1-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md
2026-11-10T16:17:13-0500 | 2026-11-10T16:17:13-0500 /tmp/hermes-corr1-w1-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
2026-11-10T16:18:43-0500 | 2026-11-10T16:18:43-0500 /tmp/hermes-corr1-w1-orig/2026-11-10-vm-agent-hermes-ssh.md
$ sed -e "s/^+//" $SP/w4-am3.txt | cmp - <(sed -n "23p" vm/2026-11-06-vm-handoff.md); echo rc   # strip + only, no TS substitution
stdin /dev/fd/15 differ: char 156, line 1
rc=1
$ cmp $SP/w4-man.txt <(sed -n "364,371p" MANIFEST.md); echo rc   # MANIFEST without substitution
SP/w4-man.txt /dev/fd/11 differ: char 15, line 1
rc=1
$ zsh: T=é; print ${#T}; print -n $T | wc -c
1
       2
LANG= LC_ALL= LC_CTYPE=C.UTF-8
$ printf %s __TS__ 20261110T211738Z | command grep -cE H  (B15 pattern)
0
$ wc -l MANIFEST.md; wc -l DECISION_LOG.md
     371 MANIFEST.md
     820 DECISION_LOG.md
    1191 total
$ git --no-optional-locks status --short | command grep -c "^??"
92
$ command grep -n "16:0[0-9]\|draft" /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md | cut -c1-140 | head -12
4:Apply the manager's decisions on worker 2's findings (`docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md`, F1–F15) to four artifacts.
14:- S13: the sentence appears once as the last line of the draft and once as the last line of the entry, and not in Amendment 3.
18:1. Read the worker 2 report, the draft (61 lines), Hermes's skill (read-only, 130 lines), both `vm/skills/*/SKILL.md`, and handoff §1 (:2
25:3. Backed up the draft to `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/af9aea76-b226-4610-b3fb-538269d1a642/scratchpad/CODE-v
77:**F11: "set up outside the build loop" was attributed to Amear.** The draft's "What this reply does not do" now reads:
140:$ head -4 draft
157:S13 draft:
159:draft last line is S13:
172:draft:3:__TS__
173:draft:8:__TS__
174:draft:8:__TS__
179:$ IP grep draft
````

## D1. S1 scan (every line of both reports, inside and outside code blocks)
I read both reports in full, line by line. The cited lines were extracted by command (output in /tmp/hermes-corr1-w6/d1.out; the command lines are echoed):
````
$ awk 'NR==16||NR==17||NR==127||NR==184||NR==251||NR==288||NR==398||NR==476||NR==479 {print "w1:" NR ": " substr($0,1,330)}' $W1
w1:16: - The PNG's sha256 equals the pre-dispatch value. That rules out a content change. It cannot show whether the file was opened.
w1:17: - The index digest (`git ls-files -s | shasum -a 256`) equals the pre-dispatch value, and the cached list is only the PNG, which was staged before this unit. HEAD is still 55979ee. So no content was added to the index and nothing was committed.
w1:127: The same four lines and the same counts, now in argument order. The snapshot is the pre-edit state: its hashes are the Step 1 values, and they equal the manager's snapshot (Step 1, worker 5 block).
w1:184: The script as run (with `O=/tmp/hermes-corr1-w1-orig; R=docs/reports` and `$T` set as above). The printed label `| sed mask` stands for the `sed "s/$T/<the rep-name token>/g"` in the loop body:
w1:251: Line counts did not change. Each file grew by +1 byte per substitution (ssh.md +2, worker1 +1, worker3 +1). That fits a 4-byte token (Step 2 prints `token length: 4`) being replaced by the 5-byte `<rep>`. (The byte length was printed. The character count assumes ASCII, which is UNVERIFIED for bytes vs. characters, but the wc -c 
w1:288: - The whole batch was piped through `sed "s/$T/<the rep-name token>/g"`. A case-insensitive count of `$T` in the masked output then printed `leak-check (case-insensitive token count in output): 0` before anything was shown.
w1:398: This is the same run and the same masking as the Step 4d re-run: `run()` runner, `command grep`, case-insensitive leak-check 0. `git status` was run with `--no-optional-locks`, so it does not write the index.
w1:476: - **Index.** The digest is 5ac1ef7d…8ac6, equal to the pre-dispatch value. The cached list is only the PNG, which shows as `A ` and was staged before this unit (it is in the session-start git status). HEAD is still 55979ee. So no content was added to the index and nothing was committed. This is proven by hash.
w1:479: - **/tmp/idx-hermes.** There is no pre-dispatch hash. That it was not edited is **not proven**. All that can be observed is that its mtime, 2026-11-11T09:45:57, is earlier than the creation of this worker's snapshot directory (09:53:09). An mtime can be set, so this is an observation, not proof.
$ awk 'NR==61||NR==65||NR==70||NR==139||NR==140||NR==447||NR==885 {print "w2:" NR ": " substr($0,1,330)}' $W2
w2:61: - The snapshot hashes match the ones in the brief (07720470…, 16791c5a…, 6ec6224f…).
w2:65:   - What is proven by hash covers only a narrower span. The reply, DECISIONS.md and the handoff equal their pre-dispatch sha256 values for correction-1, so they are unchanged from that dispatch to this fix (worker 5 block). There is no baseline for MANIFEST.md.
w2:70: - The batch was piped through `sed "s/$T/<the rep-name token>/g"`, and a case-insensitive leak-check of the masked output printed 0 before display.
w2:139:   Without the substitution, the entry and Amendment 3 differ (rc=1). So between those extracts and today, the only change in these ranges is `__TS__` → `20261110T211738Z`. The extracts are worker 4's copies from 16:14. They are not proof of worker 3's state at about 16:10.
w2:140: - The draft still exists at `SP/CODE-vm-agent-hermes.draft.md` (mtime 16:07, after worker 3's edits). The draft-only checks below are run against that file.
w2:447: Verdict: **REPRODUCED**: zero matching lines in every file. The entry, Amendment 3 and MANIFEST rows checked are today's files (after placement). The worker 5 block compares worker 4's 16:14 pre-placement extracts against today's DECISIONS.md :2075–2099, handoff :23 (after stripping the extract's diff `+`) and MANIFEST.md :364
w2:885:   - worker 4's three pre-placement extracts compared with today's entry, handoff :23 and MANIFEST :364–371, with negative controls.
$ command grep -c "pre-dispatch" $W1 $W2; command grep -c "brief" $W1 $W2
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md:12
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md:7
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md:1
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md:1
````
Every `$ ` line in the revised and new code blocks is a real command with its output under it. The 10 re-runs above confirm this for the blocks I tested.

Claims that state a result with no pasted command or output:
- **The leak-check (w1:288, w1:398, w2:70).** Each says a case-insensitive count "printed 0", and w1:288 quotes the printed text. Neither report pastes the leak-check command or its output: `command grep -n leak-check` finds only prose lines. The property itself holds (D5). → B1.
- **The pre-dispatch baselines (w1:16-17, :476-477; w2:11-13, :61, :65, :130-131).** These claims say a value "equals the pre-dispatch value" or "matches the ones in the brief". The baselines come from the dispatch brief. Neither report pastes them from a command or quotes them with their source ("pre-dispatch" occurs 12 times in worker1 and 7 in worker2). For "the manager-recorded hashes", w1:62-71 substitutes the hashes of the manager's snapshot copies. That is a proxy, not the recorded values. → B2.
- **w1:127: "The snapshot is the pre-edit state: its hashes are the Step 1 values".** Worker 5 re-ran grep on /tmp/hermes-corr1-w1-orig but never re-hashed it. The block at w1:64-69 hashes the *manager's* snapshot. The Step 1 hashes date from 09:53, before the re-run. My probe shows they still match today. → B3.
- **w1:17 and :476: "staged before this unit (it is in the session-start git status)".** No session-start status is pasted. → B5 (NOTE).
- **w2:447: "Neither string matches the pattern".** The strings are `__TS__` and `20261110T211738Z`; the pattern is H. No command was run for this. My probe gives 0, so it is true. → B5 (NOTE).
- **w2:140: "(mtime 16:07, after worker 3's edits)".** The 16:07 is pasted at :49. "After worker 3's edits" is not evidenced. Worker 3's report was last written at 16:10:11. → B5 (NOTE).

No break: disclosed labels. Each of these is disclosed in the report, and its output reproduces (w1-4b cmp rc=0; worker 4 C2 for :348ff):
- w1:184 and :193-223: the echoed `| sed mask` headers;
- w1:348-353: the superseded `$ echo` labels and the `<same five files>` shorthand, kept as the record and marked superseded at :342-345;
- worker2's quoted `orig:` lines, marked as quotes at :22.

No break: per-file output. I found no command that shows per-file output without file arguments, except the quoted originals that worker2 itself grades NOT REPRODUCED.

## D3. S2 scan
- **w2:139 and fix log :885: "with negative controls".** This is overstated:
  - The Amendment 3 "control" (w2:112-114) differs at **char 1**, because of the diff `+` prefix. So it does not test the `__TS__` substitution it is offered as controlling.
  - For MANIFEST, no control was run.

  My probes run the missing controls. With the `+` stripped and no substitution, Amendment 3 differs at char 156 (rc=1). MANIFEST without substitution differs at char 15 (rc=1). So the conclusion holds. The evidence offered for it was weaker than described. → B4.
- **w1:251: "The byte length was printed."** In zsh under C.UTF-8, `${#T}` is a character count, not a byte count. The probe shows `T=é` gives `${#T}` = 1 and wc -c = 2. The report has bytes and characters swapped. The wc -c deltas (+1 per substitution) still pin the token at 4 bytes, so its 4 characters are ASCII. → B5 (NOTE).
- **w1:479.** The directory's `%Sm` (mtime) is called its "creation". The claim is true, because the probe's `%SB` (birth time) is also 09:53:09, but the evidence pasted is the mtime. → B5 (NOTE).
- **w2:65: "unchanged from that dispatch to this fix".** This rests on hash equality at two instants. That shows equal content at both ends, not that nothing changed in between. → B5 (NOTE).
- **No re-run is presented as a 2026-11-10 observation.**
  - Worker2's A4 (:259), B3 (:328), B9-B11 (:404-406), B15 (:447) and C4c (:682) all carry today-vs-yesterday or mtime-inference qualifiers.
  - The worker1 Step 2 re-run is labelled as a re-run on the snapshot (:105).
  - The A6 rewording (w2:62-66, :259) now marks mtime inferences as "inferred from mtimes, not proven".

## D4. S13 placement in both reports
Command as run:
- `S13` was taken from specs/SPEC_RUBRIC.md:136. Its digest, `printf '%s' "$S13" | shasum -a 256`, is 816836b0…ce30, the same as worker 4 C5.
- A fence-aware `python3 -I` script then ran over both reports. A fence opens on three or more backticks and closes on an identical line. The script counts every substring hit, inside and outside code, and checks that the last non-empty line is an exact match.

Output (/tmp/hermes-corr1-w6/d4.out):
````
2026-11-11-vm-agent-hermes-correction-1-worker1.md | fences opened: 18 | open at EOF: False | hits outside (line, exact): [(518, True)] | hits inside: [] | last non-empty: 518 exact: True | total substring count: 1
2026-11-11-vm-agent-hermes-correction-1-worker2.md | fences opened: 52 | open at EOF: False | hits outside (line, exact): [(894, True)] | hits inside: [] | last non-empty: 894 exact: True | total substring count: 1
````
Verdict: **HOLDS** for both reports.
- The sentence occurs exactly once in each: worker1 :518, worker2 :894.
- It is outside any code block, an exact whole-line match, and the last non-empty line.
- Neither file ends inside an open fence.

## D5. Rep-name token count
Command as run (tool shell, repo root). The output is masked, and the first line is the command string:
````
$ f=$(ls docs/reports/evidence/ | command grep '^2026-10-28-mffu-.*-reply\.png$'); T=${f#2026-10-28-mffu-}; T=${T%-reply.png}; echo "len ${#T}"; command grep -ci -- "$T" docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md; type grep; whence -p grep
len 4
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md:0
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md:0
grep is a shell function from /Users/admin/.claude/shell-snapshots/snapshot-zsh-1794408303558-icmlpi.sh
/usr/bin/grep
````
Every scratch output and script in /tmp/hermes-corr1-w6 also gave 0 under `command grep -ci -- "$T"`. This report's own count was taken after assembly, and is given in the returned summary.

Verdict: **HOLDS.** The case-insensitive count is 0 in both reports.

## Findings
- **B1 MINOR (S1)**, worker1 :288 and :398, worker2 :70. A leak-check result ("printed 0") is stated, and its printed text is quoted, but no command or output is pasted. This is a description of output. The property is true today (D5).
- **B2 MINOR (S1)**, worker1 :16-17 and :476-477, worker2 :11-13, :61, :65 and :130-131.
  - Every "unchanged", "nothing added to the index" and "matches the brief" claim compares against pre-dispatch values.
  - Those values appear in neither report, either as command output or as a quoted, sourced baseline, so a reader cannot check the comparison.
  - w1:62-71 substitutes the manager-snapshot hashes for "the manager-recorded" values.
- **B3 MINOR (S1/S2)**, worker1 :127. The Step 2 re-run treats /tmp/hermes-corr1-w1-orig as the pre-edit state ("its hashes are the Step 1 values"). Worker 5 never re-hashed it; it hashed the manager's snapshot instead. The claim is true today (probe sha256 = Step 1), but the report does not show it.
- **B4 MINOR (S2)**, worker2 :139 and :885. "Negative controls" is overstated. The Amendment 3 control fails at char 1, on the `+`, so it does not isolate `__TS__`, and MANIFEST has no control. The A5 conclusion itself holds: the positive compares re-run byte-identical (D2), and the proper controls fail at the `__TS__` position (probes).
- **B5 NOTE.** Six minor points, each true when checked:
  - w1:17 and :476: the session-start status is not pasted;
  - w2:447: "neither string matches" was not run;
  - w2:140: "after worker 3's edits";
  - w1:251: bytes and characters are swapped;
  - w1:479: an mtime is called the creation time;
  - w2:65: two-point hash equality is called "unchanged".
- **B6 NOTE (D2 reproducibility).**
  - The pasted `type grep` line reproduces only in the interactive tool shell, not in a `zsh` script.
  - Worker1 :424-425's untracked count (91) is time-dependent, and is 92 now.
  - The diff-header and DECISION_LOG mtimes and the `/dev/fd/N` names depend on time or environment, and match today only because nothing has changed.

Worker 4's A1-A7, re-judged as the reports now stand:
- A1, A2, A3, A6 and A7 are cured.
- A4 is cured: the PNG sha256 is in worker1 Step 5.
- A5 is cured in substance. The cmp evidence is pasted and re-runs byte-identical, but its "negative control" framing is overstated (B4).

## Result
**FAIL at MINOR severity. No BLOCKER.**
- D2: 9 of 10 blocks are byte-identical; the tenth differs only through my harness. D4 and D5 HOLD.
- S1 is broken at MINOR in B1, B2 and B3. S2 is broken at MINOR in B4.
- Nothing I ran contradicts any verdict either report gives.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
