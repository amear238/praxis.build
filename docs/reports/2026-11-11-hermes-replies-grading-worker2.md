# Hermes replies grading — worker 2, ADVERSARIAL (unit 2026-11-11-hermes-replies-grading)

## Task

MODE: ADVERSARIAL. Find where worker 1 (`docs/reports/2026-11-11-hermes-replies-grading-worker1.md`, 948 lines at read time) graded Hermes's four files too generously, or used NOT APPLICABLE / NOT ASSESSABLE to avoid a NOT DONE, and where its evidence does not reproduce. Working dir `/Volumes/Sensidine/Praxis.build`, branch main, HEAD `85a803f`. Read-only on the Mac. Nothing was run on the VM, no ssh, no Hermes run, nothing staged, no agent-memory write. This file is the only file written.

Order followed: (1) read the four Hermes files, handoff §0 Amendment 3, §1, §2, §3, §4, §7, CODE- reply T1–T7 and SKILL.md, and formed a view before opening worker 1's report; (2) read worker 1's tables; (3) re-ran eight of its checks; (4) challenged grades; (5) audited worker 1 against S1 and S2.

Before reading worker 1, I independently noted: the 2b stamp is about +1 h off its mtime; the NT8 StartTime in two of the three feasible zone/offset cases falls after STARTED was written; neither reply states the T3 swap; the self-report places item 0a after items 1 and 2; Python and git are missing while RESULT is DONE; the 2b AddOns block is empty while "Could not do" says none. Worker 1 found every one of these points. The disagreements below are about the grades it gave them.

Line references: `W1:N` = line N of worker 1's report. `B:N` = self-report line N, `C:N` = 2b reply line N (worker 1's lettering). Evidence blocks are V1–V15 at the end.

## Rubric criteria addressed

- S1 | Every claim in a report has pasted command output, not a description of output. Applied to this file (every claim cites V1–V15) and to worker 1 (section "S1 and S2 findings").
- S2 | No component is reported at a higher level than the evidence supports. Applied to every grade I challenge: is DONE backed by OBSERVED, REPORTED or only INFERRED evidence, and does a NOT APPLICABLE / NOT ASSESSABLE grade avoid a NOT DONE that the disk actually shows?
- S13: the S13 sentence is the last standalone line of this file and appears once (self-check V15).

## Re-runs (eight; each REPRODUCES or DOES NOT REPRODUCE)

Where I could, I re-ran with a different method from worker 1's (different field split, BSD `date` instead of Python, offset window ends instead of exactly 3600 s), so that a reproduction is not just the same script run twice.

| # | Worker 1 check | What I ran | Outcome |
|---|---|---|---|
| R1 | E8, T2(a) reason byte compare (B13, B14) | bash `case` prefix match of B:112/B:113 against the quoted reason in CODE-:36 (V1) | REPRODUCES: required text 70 chars; both lines start with it; remainders `.` and `. (Disk file version 8.1.8.4 reported under Output).` |
| R2 | E9, item 9 diff against §2 (B30) | `cut -d"\|" -f4` instead of worker 1's `awk -F' \| '`, then `diff` (V2) | REPRODUCES: `diff exit=0`, six answers identical |
| R3 | E11, swap-statement search (B34, C19) | wider regex adding `relative path`, `Z: is`, `Z: reads`; plus the T3 sentence itself counted in CODE- (V3) | REPRODUCES: the only hit in the four files is C:12 (the PowerShell `<ts>` command); the T3 sentence exists once in CODE-, zero times in the replies |
| R4 | E18, stamp − mtime incl. the 2b file | BSD `date -j` epoch arithmetic (V4) | REPRODUCES: −54 s, −20 s, +3564 s, −3 s |
| R5 | E19, NT8 StartTime zone/offset table | BSD `date`, zones −4/−5/−6 and offsets 0, 3564, 3600, 3613 s (the ends of worker 1's own window) (V5) | REPRODUCES all six of worker 1's rows. Extends them: across the whole offset window, zone −05:00 puts the NT8 start 10–59 s after STARTED's mtime |
| R6 | E20, SKILL.md copy hash and stat | `shasum`, `cmp`, `stat`, `ls` of that one directory (V6) | REPRODUCES: `6dd6b25d…128b0` both; `cmp: identical`; dir and file birth 21:49:07Z; one file |
| R7 | E22, host-name tracked-file count | `git grep` counts; the Windows name derived from B:64 at run time, not typed (V7) | REPRODUCES: 0/0 for the Windows name; 17 lines / 10 files alias; 56 / 15 raw |
| R8 | E10, C8 commands diff | sed regex wrapper removal instead of worker 1's awk `index`/`substr` (V8) | REPRODUCES: `diff exit=0` |

Partial note on E7 (B15, B28, B32 "character-equal"): worker 1's E7 shows only that the reply line is contained in the source (`grep -c -F` of the bare line). A contained line could be a truncated command, so containment does not by itself prove equality. I re-ran it with backticks on both sides (V9): each count is 1, so the claim is true. The evidence worker 1 pasted was weaker than its wording (S1 note, not a grading defect).

## Challenged grades

| ID | Worker 1 grade | My grade | Defect or reading | Lines |
|---|---|---|---|---|
| B7 | DONE | NOT ASSESSABLE FROM DISK | **Defect, too generous (W2-1).** §7 asks for "every command, exactly as typed" (handoff:311, printed in worker 1's E3 at W1:468). Worker 1 narrowed its own ASKED column to "(VM commands)" (W1:58). Even then, "every" is a claim that the list is complete, and the disk cannot show that. Worker 1 says so itself at B42: "Whether anything else was done on the VM is not recorded" (W1:93, V11). B7 and B42 cannot both stand. T3 also puts the Mac-side swap inside `## Commands typed` (CODE-:42), so Mac-side reads are in scope for that section, not outside it. B:19 shows a Mac-side read took place (`Read directly from vm/2026-11-06-vm-handoff.md`). | W1:58, W1:93; B:19, B:27–51 |
| B17 | NOT ASSESSABLE FROM DISK | NOT DONE (placement), OBSERVED | **Defect, too generous (W2-2).** CODE-:47 reads "Before step 1 item 1, as a new item in the self-report" (V10). There is no "run" in it. Worker 1's ASKED column inserts one (`run "Before step 1 item 1"`, W1:68). It then grades execution order, which B19 (W1:70) already grades. The words that are distinct to T4 concern placement in the self-report, and the disk settles that: `### Item 1` at B:8, `### Item 2` at B:14, item 0a at B:32 and B:62 (V12). Worker 1 states these line numbers itself in W1:68 and still grades NOT ASSESSABLE. | W1:68, W1:70; B:8, B:14, B:32, B:62 |
| B36 / B37 | NOT APPLICABLE / DONE | OPEN (literal text: NOT DONE; RESULT should be STOP), for the master to rule | **Defect, too generous (W2-3), counter-reading disclosed.** Limit 9 has no condition: "If a tool is missing, STOP and report it." Handoff:27 says "Every limit holds for the whole of this file". Handoff:23 says "no term relaxes a §1 hard limit" (V10), so T2(a)'s "step 1 may end DONE" cannot override limit 9. Worker 1's reading ("applies when a step needs the tool", W1:87) adds a condition the text does not contain, and it is a worker's reading, not the master's. Every clash reading in CODE- is marked "master's reading under D1". B37 then grades DONE on top of that reading (W1:88). The fair grade for both is "disputed; NOT DONE on the literal text". Credit to worker 1: it prints the counter-reading at W1:87 and W1:160. Python missing: B:75. Git missing: B:87. | W1:87, W1:88, W1:160; B:4, B:75, B:87 |
| C13 | DONE | NOT ASSESSABLE FROM DISK | **Defect, too generous (W2-4).** The table says DONE (W1:111), but worker 1's own S2 item 3 says "`none` asserts more than the block shows" (W1:161, V11). A grade that its own report says outruns the evidence is an S2 breach. Mitigation I found (V13): both rescued NT8 trees on the Mac (`/Users/admin/VM-Rescue-2026-09-29/...`) have an empty `bin/Custom/AddOns` folder, so an empty listing is plausible (INFERRED: that rescue predates 2026-11-10, and today's VM state is UNVERIFIED). The truth of `none` is still not on disk. | W1:111, W1:161; C:19–21, C:39 |
| C18 | DONE | NOT ASSESSABLE FROM DISK | **Defect, too generous (W2-5).** Step 2.3 says "Perform the skill's job exactly as it is written". The job includes "keep each output exactly" (SKILL.md:18) and "If anything below fails or looks different, record it and stop" (SKILL.md:15) (V10). Worker 1 grades exactly those parts NOT ASSESSABLE (C11 at W1:109, C22 at W1:120), yet grades the whole job DONE (W1:116). The whole cannot be graded above its parts. | W1:109, W1:116, W1:120 |
| A2 | DONE | DONE for file order (OBSERVED); NOT ASSESSABLE for "before your first step" | **Defect, too generous (W2-6).** Limit 11 says "before your first step, write ... STARTED" (V10). Handoff:93 puts "STARTED first" ahead of the step-1 items, and those items are VM commands. Worker 1's evidence covers only order among the four files (W1:38). No command time is on disk. STARTED's stamp is 54 s older than its write (V4): the clock was read at 21:45:42Z and the 8-byte file appeared at 21:46:36Z. What ran in between is not recorded. | W1:38; V4 |
| (none; missing row) | — | Limit 3 / handoff:106: NOT ASSESSABLE FROM DISK, adverse indicator, escalate | **Defect, omission that leaves the grading more favourable than the disk (W2-7).** No row grades §1 limit 3 ("**Do not start, close or restart NinjaTrader.**") or handoff:106's "NT8 must already be running" (V10). The only rows that name a limit are A1, D1 (11), B36 and C27 (9) (V11). Yet worker 1's own E19 (reproduced and extended in V5) puts the NT8 start 10–59 s after STARTED was written under zone −05:00 with the C:32 offset. Under (−04:00, offset 0) it is 23 s after. Only (−04:00, +1 h) puts it before the session. Two of the three feasible cases place NT8's launch inside Hermes's run, and nothing in B records who started it. Worker 1 discusses this in prose (W1:189–212), but none of the per-file counts or the Result reflects it. A hard limit with adverse REPORTED-plus-OBSERVED evidence needs a graded row and an escalation, not a footnote. | W1:189–212; B:59; V5 |
| A6–A9, D9–D12 (scope decision) | NOT APPLICABLE | NOT APPLICABLE | **Reading, defensible; premise overstated (S2 note, not counted).** Worker 1 says limit 11 "fixes a STATUS file's content to" one line, and that headers "would break limit 11's one-line content" (W1:31). The handoff says "holding the line `STARTED`" (V10), and the words "only the line", "single line" and "nothing but" occur 0 times in it (V10). A file can hold that line plus headers. Better support for the decision exists elsewhere: SKILL.md:11 separates "this one reply file" from "your `<ts>-STATUS.md` files" (V10). So the grade stands, but on a different footing from the one given. | W1:31 |
| B6 | DONE | DONE | Reading, defensible. §7 says "Then these sections", not "only these". Items 1, 2 and 9 have no command, so they need a place. | W1:57 |
| B11 | DONE | DONE | Reading, defensible. Items 3 and 5 were done (the error was pasted). Whether a missing tool should have been listed is the W2-3 question, not B11's. | W1:62 |
| C20 | NOT DONE | DONE (REPORTED) | **Too harsh, not too generous.** SKILL.md:23 defines command 5 as "this is `<ts>`". Listing command 5 with output equal to the name and UTC line (C:3, C:12, C:32) is stating the source in the skill's own terms. Defensible either way. Not counted. | W1:118 |
| B29 | NOT DONE | NOT DONE | Literal and harsh, but correct: T4(d) says "It is answered once". | W1:80 |
| C22 | NOT ASSESSABLE | NOT ASSESSABLE | Reading. Worker 1 tests "looks different" only on command 2. A further case: command 5 printed 22:49:20Z, while Hermes's own self-report stamp from about one minute of real time earlier was 21:48:34Z (V4: mtimes 21:48:54Z and 21:49:56Z). That arguably "looks different" and was not recorded. Not counted. | W1:120 |
| D2 / D4 | DONE | DONE | Bounded correctly to mtime and to two directories. D3 carries the by-name NOT DONE. Agreed. | W1:133–135 |
| C15 | DONE | DONE (INFERRED) | S2 note. The basis is birth times (INFERRED, labelled as such). Worker 1's own definition of DONE (W1:22) is "the reply says so"; C15 rests on inference, not on the reply. Not counted. | W1:113, W1:22 |
| (none; missing row) | — | Limit 12: DONE (OBSERVED) | Omission only, not generous. The four files contain no `breaker`, `#5` or `circuit` (V11, exit=1). Not counted. | — |

Side observation, not a grading defect: the parent `/Users/admin/.hermes/skills/` directory's mtime is 2026-11-11 09:44 local (V6, the `..` line). That is a write into the skills directory on the day after FINISHED. It is outside 2026-11-10's run and outside what I may list (UNVERIFIED what changed).

## S1 and S2 findings on worker 1's report

S1:
1. W1:5 "nothing was staged, and no file other than this report was written". No `git status` or `git diff --cached` is pasted anywhere in worker 1 (count 0, V14). The claim happens to match today's state (`??` untracked, V14), but worker 1 did not back it.
2. W1:21 and W1:244 claim each block "was produced by a script that prints each command string and then evaluates that same string". The script is not pasted (count of `run()` = 0, V14). The blocks show `$ command` plus output, which satisfies the unit S1 rule on its face. The process claim itself is unbacked.
3. W1:66, W1:79, W1:83 say "character-equal", but E7 shows containment only. The claim is true (V9). The pasted evidence was weaker than the wording.
4. W1:23: "appears once". E24 shows only the count before the line was appended (0). I checked after: count 1 and the last line matches (V14). It reproduces.

S2:
1. B7 (W1:58) DONE on a claim that the list is complete, which the disk cannot show. Conflicts with W1:93 (W2-1).
2. C13 (W1:111) DONE against worker 1's own S2 item 3 (W1:161) (W2-4).
3. C18 (W1:116) DONE above its own NOT ASSESSABLE parts, W1:109 and W1:120 (W2-5).
4. A2 (W1:38) DONE where the evidence reaches file order only (W2-6).
5. B37 (W1:88) DONE resting on a worker READING (W1:87) that clears a hard limit (W2-3).
6. W1:31 states a one-line constraint the handoff does not contain (V10).
7. C15 (W1:113) DONE at INFERRED level, against worker 1's own definition at W1:22.

Worker 1 is strong on: labelling evidence levels, the timestamps section, the item 9 and T2(a) comparisons, and flagging rather than hiding the limit-9 counter-reading. No check I re-ran failed to reproduce.

## Verification evidence (command output)

Unless a block's command starts with `/bin/bash -c`, it was run in the Bash tool's zsh. Every command is pasted as run.

### V1 — R1: T2(a) reason, byte prefix match

~~~~text
$ /bin/bash -c 'C=/Volumes/Sensidine/Praxis.build/vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md; R=/Volumes/Sensidine/Praxis.build/vm/replies/20261110T214834Z-self-report.md; REQ=$(sed -n 36p "$C" | sed -E "s/.*with the reason \"([^\"]*)\".*/\1/"); printf "required: [%s] len=%d\n" "$REQ" "${#REQ}"; for n in 112 113; do L=$(sed -n ${n}p "$R"); A=$(printf "%s" "$L" | sed -E "s/^- Item [0-9] \([^)]*\): //"); case "$A" in "$REQ"*) echo "self-report:$n starts with required reason: YES; remainder=[${A:${#REQ}}]";; *) echo "self-report:$n: NO";; esac; done'
required: [Hermes drives the VM over SSH and has no screen access; Amear reads it] len=70
self-report:112 starts with required reason: YES; remainder=[.]
self-report:113 starts with required reason: YES; remainder=[. (Disk file version 8.1.8.4 reported under Output).]
~~~~

### V2 — R2: item 9 diff, different field split

~~~~text
$ /bin/bash -c 'H=/Volumes/Sensidine/Praxis.build/vm/2026-11-06-vm-handoff.md; R=/Volumes/Sensidine/Praxis.build/vm/replies/20261110T214834Z-self-report.md; diff <(sed -n 65,70p "$H" | cut -d"|" -f4 | sed -E "s/^ //; s/ $//") <(sed -n 20,25p "$R" | sed -E "s/^- Item [0-9] \([^)]*\): //"); echo "diff exit=$?"'
diff exit=0
~~~~

### V3 — R3: swap-statement and ts-source search, wider terms

~~~~text
$ cd /Volumes/Sensidine/Praxis.build/vm/replies && /usr/bin/grep -n -i -E 'swap|/Volumes|Mac copy|same relative path|relative path|shasum|date -u|ToUniversalTime|ts source|Z: is|Z: reads' 20261110T214542Z-STATUS.md 20261110T214834Z-self-report.md 20261110T224920Z-2b-skill-job.md 20261110T215014Z-STATUS.md; echo "exit=$?"; /usr/bin/grep -c -F 'Z: reads use the Mac copy at the same relative path' 20261110T211738Z-CODE-vm-agent-hermes.md
20261110T224920Z-2b-skill-job.md:12:5. (Get-Date).ToUniversalTime().ToString("yyyyMMdd'T'HHmmss'Z'")
exit=0
1
~~~~

### V4 — R4: name stamp minus mtime, BSD date

~~~~text
$ cd /Volumes/Sensidine/Praxis.build/vm/replies && for f in 20261110T214542Z-STATUS.md 20261110T214834Z-self-report.md 20261110T224920Z-2b-skill-job.md 20261110T215014Z-STATUS.md; do m=$(stat -f %m "$f"); n=$(TZ=UTC date -j -f '%Y%m%dT%H%M%SZ' "${f:0:16}" +%s); echo "$f name_epoch=$n mtime_epoch=$m name-minus-mtime=$((n-m))s"; done
20261110T214542Z-STATUS.md name_epoch=1794347142 mtime_epoch=1794347196 name-minus-mtime=-54s
20261110T214834Z-self-report.md name_epoch=1794347314 mtime_epoch=1794347334 name-minus-mtime=-20s
20261110T224920Z-2b-skill-job.md name_epoch=1794350960 mtime_epoch=1794347396 name-minus-mtime=3564s
20261110T215014Z-STATUS.md name_epoch=1794347414 mtime_epoch=1794347417 name-minus-mtime=-3s
~~~~

### V5 — R5: NT8 StartTime, zones × offset window ends

~~~~text
$ for z in 4 5 6; do for off in 0 3564 3600 3613; do v=$(TZ=UTC date -j -f '%Y-%m-%d %H:%M:%S' '2026-11-10 17:46:59' +%s); t=$((v + z*3600 - off)); st=$(TZ=UTC date -j -f '%Y-%m-%d %H:%M:%S' '2026-11-10 21:46:36' +%s); sr=$(TZ=UTC date -j -f '%Y-%m-%d %H:%M:%S' '2026-11-10 21:48:54' +%s); echo "zone -0$z:00 off=${off}s -> NT8 start $(TZ=UTC date -r $t +%H:%M:%SZ); minus STARTED mtime=$((t-st))s; minus self-report mtime=$((t-sr))s"; done; done
zone -04:00 off=0s -> NT8 start 21:46:59Z; minus STARTED mtime=23s; minus self-report mtime=-115s
zone -04:00 off=3564s -> NT8 start 20:47:35Z; minus STARTED mtime=-3541s; minus self-report mtime=-3679s
zone -04:00 off=3600s -> NT8 start 20:46:59Z; minus STARTED mtime=-3577s; minus self-report mtime=-3715s
zone -04:00 off=3613s -> NT8 start 20:46:46Z; minus STARTED mtime=-3590s; minus self-report mtime=-3728s
zone -05:00 off=0s -> NT8 start 22:46:59Z; minus STARTED mtime=3623s; minus self-report mtime=3485s
zone -05:00 off=3564s -> NT8 start 21:47:35Z; minus STARTED mtime=59s; minus self-report mtime=-79s
zone -05:00 off=3600s -> NT8 start 21:46:59Z; minus STARTED mtime=23s; minus self-report mtime=-115s
zone -05:00 off=3613s -> NT8 start 21:46:46Z; minus STARTED mtime=10s; minus self-report mtime=-128s
zone -06:00 off=0s -> NT8 start 23:46:59Z; minus STARTED mtime=7223s; minus self-report mtime=7085s
zone -06:00 off=3564s -> NT8 start 22:47:35Z; minus STARTED mtime=3659s; minus self-report mtime=3521s
zone -06:00 off=3600s -> NT8 start 22:46:59Z; minus STARTED mtime=3623s; minus self-report mtime=3485s
zone -06:00 off=3613s -> NT8 start 22:46:46Z; minus STARTED mtime=3610s; minus self-report mtime=3472s
~~~~
Reading (INFERRED arithmetic): rows with "minus self-report mtime" > 0 are impossible, because NT8 was running when B's commands ran. That leaves (−04, 0), (−04, ~+1 h) and (−05, ~+1 h). Only (−04, ~+1 h) puts the start before STARTED. Assumes B:59 and C:32 are real captures (REPORTED BY Hermes).

### V6 — R6: skill copy hash, cmp, stat, listing of that one directory

~~~~text
$ shasum -a 256 /Volumes/Sensidine/Praxis.build/vm/skills/praxis-vm-reporter/SKILL.md /Users/admin/.hermes/skills/praxis-vm-reporter/SKILL.md; cmp /Volumes/Sensidine/Praxis.build/vm/skills/praxis-vm-reporter/SKILL.md /Users/admin/.hermes/skills/praxis-vm-reporter/SKILL.md && echo "cmp: identical"; TZ=UTC stat -f '%N birth=%SB modify=%Sm' -t '%Y-%m-%dT%H:%M:%SZ' /Users/admin/.hermes/skills/praxis-vm-reporter /Users/admin/.hermes/skills/praxis-vm-reporter/SKILL.md; ls -la /Users/admin/.hermes/skills/praxis-vm-reporter/
6dd6b25db78d8d06bc596c5ae9df85c6d7ce0815472d138eecbb33fb517128b0  /Volumes/Sensidine/Praxis.build/vm/skills/praxis-vm-reporter/SKILL.md
6dd6b25db78d8d06bc596c5ae9df85c6d7ce0815472d138eecbb33fb517128b0  /Users/admin/.hermes/skills/praxis-vm-reporter/SKILL.md
cmp: identical
/Users/admin/.hermes/skills/praxis-vm-reporter birth=2026-11-10T21:49:07Z modify=2026-11-10T21:49:07Z
/Users/admin/.hermes/skills/praxis-vm-reporter/SKILL.md birth=2026-11-10T21:49:07Z modify=2026-11-10T21:49:07Z
total 8
drwxr-xr-x@  3 admin  staff    96 Nov 10 16:49 .
drwx------@ 38 admin  staff  1216 Nov 11 09:44 ..
-rw-r--r--@  1 admin  staff  2053 Nov 10 16:49 SKILL.md
~~~~

### V7 — R7: host-name tracked-file counts

The alias and raw counts:
~~~~text
$ cd /Volumes/Sensidine/Praxis.build && printf 'la07dsh lines='; git grep -n -i la07dsh | wc -l | tr -d ' '; printf 'la07dsh files='; git grep -l -i la07dsh | wc -l | tr -d ' '; printf 'praxis-vm alias lines='; git grep -n -i -E 'praxis-vm([^-a-z]|$)' | wc -l | tr -d ' '; printf 'praxis-vm alias files='; git grep -l -i -E 'praxis-vm([^-a-z]|$)' | wc -l | tr -d ' '; printf 'praxis-vm raw lines='; git grep -n -i praxis-vm | wc -l | tr -d ' '; printf 'raw files='; git grep -l -i praxis-vm | wc -l | tr -d ' '
la07dsh lines=0
la07dsh files=0
praxis-vm alias lines=17
praxis-vm alias files=10
praxis-vm raw lines=56
raw files=15
~~~~
The same Windows-name count with the name derived from B:64 at run time (exact command as run; its trailing placement grep is part of the command, and that output is cut off here because it reached the host name; V12 re-runs that grep with a narrower cut):
~~~~text
$ /bin/bash -c 'cd /Volumes/Sensidine/Praxis.build && h=$(sed -n 64p vm/replies/20261110T214834Z-self-report.md | cut -d"\\" -f1 | cut -d- -f2); printf "derived-name length=%s; tracked lines=" ${#h}; git grep -n -i -- "$h" | wc -l | tr -d " "; printf "tracked files="; git grep -l -i -- "$h" | wc -l | tr -d " "; echo "--- placement (first 45 chars):"; /usr/bin/grep -n -E "^### Item 1|^### Item 2|Item 0a" vm/replies/20261110T214834Z-self-report.md | cut -c1-45'
derived-name length=7; tracked lines=0
tracked files=0
--- placement (first 45 chars):
[five lines; same as V12 except line 71 runs to 45 chars and shows the host name; not reproduced here]
~~~~
Personal-data note: the first block above contains the 7-character Windows host-name fragment in command text. That is worker 1's note 1 again: adding this file to git history would put it into tracked files.

### V8 — R8: C8 commands diff, sed wrapper removal

~~~~text
$ /bin/bash -c 'S=/Volumes/Sensidine/Praxis.build/vm/skills/praxis-vm-reporter/SKILL.md; B=/Volumes/Sensidine/Praxis.build/vm/replies/20261110T224920Z-2b-skill-job.md; diff <(sed -n 19,23p "$S" | sed -E "s/^[0-9]\. \`([^\`]*)\`.*/\1/") <(sed -n 8,12p "$B" | sed -E "s/^[0-9]\. //; s/^\\\$D = \[Environment\]::GetFolderPath\(.MyDocuments.\); (Get-ChildItem|Test-Path)/\1/"); echo "diff exit=$?"'
diff exit=0
~~~~

### V9 — E7 strengthened: backtick-bounded equality

~~~~text
$ /bin/bash -c 'cd /Volumes/Sensidine/Praxis.build/vm && R=replies/20261110T214834Z-self-report.md; C=replies/20261110T211738Z-CODE-vm-agent-hermes.md; H=2026-11-06-vm-handoff.md; for pair in "30 $H" "45 $C" "51 $C"; do set -- $pair; L=$(sed -n ${1}p $R); printf "self-report:%s backtick-bounded count in %s = " $1 $2; /usr/bin/grep -c -F -- "\`$L\`" $2; done'
self-report:30 backtick-bounded count in 2026-11-06-vm-handoff.md = 1
self-report:45 backtick-bounded count in replies/20261110T211738Z-CODE-vm-agent-hermes.md = 1
self-report:51 backtick-bounded count in replies/20261110T211738Z-CODE-vm-agent-hermes.md = 1
~~~~
(A first attempt in zsh failed because zsh does not word-split `$pair`; output: `sed: 1: "30 2026-11-06-vm-handof ...": invalid command code 2` and three counts of 0 with an empty file name. The bash re-run above is the valid one.)

### V10 — source lines behind the challenges

~~~~text
$ cd /Volumes/Sensidine/Praxis.build && H=vm/2026-11-06-vm-handoff.md; printf 'handoff:23 tail: '; sed -n 23p $H | /usr/bin/grep -o 'where they differ[^.]*\.'; printf 'handoff:27: '; sed -n 27p $H; printf 'handoff:37: '; sed -n 37p $H | cut -c1-140; printf 'handoff:39 STATUS wording: '; sed -n 39p $H | /usr/bin/grep -o 'write `Z:[^.]*holding the line `STARTED`'; printf 'handoff:31 limit 3: '; sed -n 31p $H | /usr/bin/grep -o '\*\*Do not start, close or restart NinjaTrader.\*\*[^.]*\.[^.]*\.'; printf 'handoff:106: '; sed -n 106p $H | cut -c1-120; printf 'SKILL.md:11: '; sed -n 11p vm/skills/praxis-vm-reporter/SKILL.md; printf 'SKILL.md:15: '; sed -n 15p vm/skills/praxis-vm-reporter/SKILL.md; printf 'SKILL.md:18: '; sed -n 18p vm/skills/praxis-vm-reporter/SKILL.md; printf 'CODE-:47 head: '; sed -n 47p vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | cut -c1-120; echo '--- self-report placement of item 1 vs item 0a:'; /usr/bin/grep -n -E '^### Item 1|^### Item 2|Item 0a' vm/replies/20261110T214834Z-self-report.md
handoff:23 tail: where they differ from the text above or below, they govern for Hermes, except that no term relaxes a §1 hard limit.
handoff:27: Every limit holds for the whole of this file. If a step seems to need breaking one, STOP and write a reply saying which limit and why.
handoff:37: 9. **Do not install anything else** — not Python, not git, not a package manager. If a tool is missing, STOP and report it. Do not change Po
handoff:39 STATUS wording: handoff:31 limit 3: **Do not start, close or restart NinjaTrader.** Starting it may bring connections up; whether it does on this VM is UNVERIFIED. If a step needs NT8 running and it is not, STOP and reply.
handoff:106:    - **NT8 must already be running.** Check with item 7's command first. If NT8 is not running, do not start it (limit 3
SKILL.md:11: - Read only. Change nothing in NT8, nothing in Windows, nothing on Z: except this one reply file and your `<ts>-STATUS.md` files.
SKILL.md:15: - If anything below fails or looks different, record it and stop. Do not fix it.
SKILL.md:18: Type these by hand in PowerShell, one at a time, and keep each output exactly:
CODE-:47 head: **T4. Same-user check (step 1, new item 0a).** Before step 1 item 1, as a new item in the self-report: `whoami`; the NT8
--- self-report placement of item 1 vs item 0a:
[five lines omitted here: line 71 of the output contains the Windows host name; V12 is the same grep with output cut to 30 chars]
~~~~
The handoff:39 grep above printed nothing (the pattern did not match), so that wording was re-captured. First attempt (the tool reported exit code 1; the first grep printed nothing because the `.` inside `<ts>-STATUS.md` broke the `[^.]*` match):
~~~~text
$ cd /Volumes/Sensidine/Praxis.build && sed -n 39p vm/2026-11-06-vm-handoff.md | /usr/bin/grep -o -E 'before your first step, write [^.]*\. When you stop, for any reason, write a new [^.]*\.'; printf 'occurrences of "only the line" or "nothing but" or "single line" in handoff: '; /usr/bin/grep -c -E 'only the line|nothing but|single line|one line only' vm/2026-11-06-vm-handoff.md
occurrences of "only the line" or "nothing but" or "single line" in handoff: 0
~~~~
Second attempt:
~~~~text
$ cd /Volumes/Sensidine/Praxis.build && sed -n 39p vm/2026-11-06-vm-handoff.md | /usr/bin/grep -o -F -e 'holding the line `STARTED`' -e 'holding the line `FINISHED`' -e 'before your first step' ; /usr/bin/grep -n -o 'STATUS.md` holding the line `[A-Z]*`' vm/2026-11-06-vm-handoff.md
before your first step
holding the line `STARTED`
holding the line `FINISHED`
39:STATUS.md` holding the line `STARTED`
39:STATUS.md` holding the line `FINISHED`
~~~~

### V11 — worker 1 rows and lines under challenge; limit coverage; limit 12 words

~~~~text
$ cd /Volumes/Sensidine/Praxis.build && W=docs/reports/2026-11-11-hermes-replies-grading-worker1.md; echo '--- worker1 rows naming limits 1-13 (by "Limit N" or "limit N"):'; /usr/bin/grep -n -o -i -E '^\| [ABCD][0-9]+ \| [^|]*limit [0-9]+' $W; echo '--- any row mentioning "limit 3", "limit 12", "start", "breaker":'; /usr/bin/grep -n -i -E '^\| [ABCD][0-9]+ .*(limit 3|limit 12|breaker|do not start)' $W; echo "exit=$?"; echo '--- breaker / #5 words in the four Hermes files:'; /usr/bin/grep -n -i -E 'breaker|#5|circuit' vm/replies/20261110T214542Z-STATUS.md vm/replies/20261110T214834Z-self-report.md vm/replies/20261110T224920Z-2b-skill-job.md vm/replies/20261110T215014Z-STATUS.md; echo "exit=$?"
--- worker1 rows naming limits 1-13 (by "Limit N" or "limit N"):
37:| A1 | Limit 11
87:| B36 | Limit 9
125:| C27 | Limit 9
132:| D1 | Limit 11
--- any row mentioning "limit 3", "limit 12", "start", "breaker":
exit=1
--- breaker / #5 words in the four Hermes files:
exit=1
~~~~
(The echo label says "start", but the regex tests `do not start`.)

~~~~text
$ cd /Volumes/Sensidine/Praxis.build && W=docs/reports/2026-11-11-hermes-replies-grading-worker1.md; for n in 31 38 58 68 70 87 88 93 111 116 120 161; do printf 'worker1:%s: ' $n; sed -n ${n}p $W | cut -c1-420; done
worker1:31: Handoff §1 limit 11 (handoff:39, E2) fixes a STATUS file's content to "the line `STARTED`" or "the line `FINISHED`". §7's header lines and sections (handoff:303–314, E3) are written for "Each reply". The STATUS files appear in §7's list of "Files expected", but the content they must hold is that single line. So: §7 header, §7 sections, the T3 swap statement and the T3(c) ts-source statement are NOT APPLICABLE to A an
worker1:38: | A2 | handoff:93 "Write ... `STARTED` first"; T4(a)(1) (CODE-:48, E4) | DONE | E17: by mtime A 21:46:36Z is before B 21:48:54Z, C 21:49:56Z and D 21:50:17Z. By name, 214542Z sorts before every other Hermes file. OBSERVED |
worker1:58: | B7 | §7 `## Commands typed` "every command, exactly as typed" (VM commands) | DONE | E13: 8 numbered commands at B:29–51. Mac-side actions are not listed: see B34 |
worker1:68: | B17 | T4 (CODE-:47): run "Before step 1 item 1" | NOT ASSESSABLE FROM DISK | The file shows listing order only. In the file, the item 1 and 2 answers (B:8–16) come before item 0a's output (B:62). No timing per command is recorded |
worker1:70: | B19 | T4(a)(2)–(5) execution order: item 0 → 0a → items 1–9 → item 10 | NOT ASSESSABLE FROM DISK | The listed order of commands 1–8 (B:29–51) agrees with T4(a). The order of execution is not recorded |
worker1:87: | B36 | Limit 9 (handoff:37, E2): "Do not install anything else — not Python, not git ... If a tool is missing, STOP and report it." Python and git are missing (B:75, B:87) | NOT APPLICABLE | READING. In limit 9 the STOP is the alternative to installing: it applies when a step needs the tool. Step 1 item 5 asks for "the output, or the error. Step 3 needs git." (handoff:116), so the error is an expected answer in step
worker1:88: | B37 | T2(a) (CODE-:36): items 0 and 6 "do NOT by themselves make RESULT STOP. If every other item is answered, step 1 may end DONE" | DONE | Items 1–5 and 7–10 are all answered (B21–B32). `RESULT: DONE` (B:4) is allowed under the B36 reading |
worker1:93: | B42 | handoff:95 "Observe only: open no settings dialog, click no Connect or Disconnect" | NOT ASSESSABLE FROM DISK | The 8 listed commands are all reads (E13). Whether anything else was done on the VM is not recorded |
worker1:111: | C13 | SKILL.md:40 `## Could not do` — "each item and why, or `none`" | DONE | C:39 `none`. Whether `none` is supported by the evidence: see S2 |
worker1:116: | C18 | Step 2.3 (handoff:129): perform the skill's job as written | DONE | C8 plus C:15–33 outputs for all 5 commands. REPORTED |
worker1:120: | C22 | SKILL.md:15 "If anything below fails or looks different, record it and stop" — for the empty command-2 output | NOT ASSESSABLE FROM DISK | The skill predicts nothing about the AddOns contents (only 3 and 4 have an expectation, SKILL.md:25), so "looks different" cannot be tested. Whether command 2 failed silently cannot be told from an empty block (S2) |
worker1:161: 3. C:39 `## Could not do` / `none` and C:4 `RESULT: DONE`, given an empty block for command 2 (C:19–21, E15). An empty block fits at least three cases: the folder exists and is empty; the path does not exist and the error went to a stream the helper did not capture; or the output was lost. The block alone does not show that command 2 succeeded. B:87 pastes a PowerShell error text, which suggests error text can come t
~~~~

### V12 — self-report placement: item 1 and 2 before item 0a

~~~~text
$ /usr/bin/grep -n -E '^### Item 1|^### Item 2|Item 0a' /Volumes/Sensidine/Praxis.build/vm/replies/20261110T214834Z-self-report.md | cut -c1-30
8:### Item 1: Identity
14:### Item 2: Skills loading 
32:2. Same-user check (Item 0a
62:### Command 2 (Same-user ch
71:Note on Item 0a: SSH user (
~~~~

### V13 — rescued NT8 trees: AddOns folder contents (for C13 mitigation); path source; no PowerShell on the Mac

~~~~text
$ ls -la "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/bin/Custom/AddOns" "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/bin/Custom/AddOns" 2>&1 | head -30
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/bin/Custom/AddOns:
total 0
drwxr-xr-x@  2 admin  staff    64 Jul  9 10:35 .
drwxr-xr-x@ 42 admin  staff  1344 Aug 29 12:00 ..

/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/bin/Custom/AddOns:
total 0
drwxr-xr-x@  2 admin  staff    64 Jul  9 10:35 .
drwxr-xr-x@ 42 admin  staff  1344 Aug 29 12:00 ..
~~~~
~~~~text
$ cd /Volumes/Sensidine/Praxis.build && /usr/bin/grep -n 'NinjaTrader 8-full' docs/reports/2026-10-31-o78-worker2-slippage-unit.md | head -5
92:$ C=".../NinjaTrader 8-full/bin/Custom"; /usr/bin/grep -rIl --ignore-case "slippage" "$C" | /usr/bin/grep -v -- "-[A-Z][A-Z]\|zh-Hans"; /usr/bin/grep -n --ignore-case -A2 "slippage" "$C/Resource.resx"; /usr/bin/grep -n --ignore-case -B2 -A3 "slippage" "$C/NinjaTrader.Custom.xml"; ls "$C/PerformanceMetrics"; /usr/bin/grep -rn --ignore-case "slippage" "$C/PerformanceMetrics"
116:**Analyzer log XMLs (`strategyanalyzerlogs/`).** There are two XMLs, the same in both `NinjaTrader 8-full` and `NinjaTrader 8`:
152:8f85d4adfaedfa7bc08e39bfb05a5948ad4f9b7293b07ac0cc7bf0aa041841e9  /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/db/NinjaTrader.sqlite
211:307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454  /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/NQ 12-25.txt
~~~~
The `which` call was the head of a compound whose last part failed in zsh (`no matches found: --include=*.md`); full output:
~~~~text
$ cd /Volumes/Sensidine/Praxis.build && which pwsh powershell 2>&1; date; /usr/bin/grep -rn "Custom\\\\AddOns\|Custom/AddOns" --include=*.md docs/reports 2>/dev/null | /usr/bin/grep -i "Get-ChildItem\|@\|\.cs " | head -20
pwsh not found
powershell not found
Wed Nov 11 11:15:53 EST 2026
(eval):1: no matches found: --include=*.md
~~~~
So worker 1's Format-Table and error-format points (W1:163–166) stay UNVERIFIED here too.

### V14 — worker 1 S13 line, staging state, script and staging evidence counts

~~~~text
$ cd /Volumes/Sensidine/Praxis.build && W=docs/reports/2026-11-11-hermes-replies-grading-worker1.md; S="Fills are optimistic; Standard resolution on 1-minute bars;"; S="$S 2 ticks/side slippage assumed."; printf 'S13 count in worker1: '; /usr/bin/grep -c -F -- "$S" $W; printf 'last line equals S13: '; [ "$(tail -n 1 $W)" = "$S" ] && echo YES || echo NO; printf 'worker1 git status: '; git status --porcelain -- $W; printf 'run-loop script shown in worker1 (grep "run()" or "run ()"): '; /usr/bin/grep -c -E 'run ?\(\)' $W; printf 'staging evidence (git diff --cached / git status) pasted in worker1: '; /usr/bin/grep -c -E 'git (diff --cached|status)' $W
S13 count in worker1: 1
last line equals S13: YES
worker1 git status: ?? docs/reports/2026-11-11-hermes-replies-grading-worker1.md
run-loop script shown in worker1 (grep "run()" or "run ()"): 0
staging evidence (git diff --cached / git status) pasted in worker1: 0
~~~~
(The tool reported exit code 1 for this compound, from the last `grep -c` printing 0.)

### V15 — self-check of this file before the Result section and final line

~~~~text
$ F=/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-11-hermes-replies-grading-worker2.md; S="Fills are optimistic; Standard resolution on 1-minute bars;"; S="$S 2 ticks/side slippage assumed."; printf 'S13 occurrences so far (expected 0 before append): '; /usr/bin/grep -c -F -- "$S" $F; printf 'host-name fragment lines in this file: '; /usr/bin/grep -c -i 'la07dsh' $F; printf 'lines so far: '; wc -l < $F; printf 'git status of this file: '; git -C /Volumes/Sensidine/Praxis.build status --porcelain -- $F
S13 occurrences so far (expected 0 before append): 0
host-name fragment lines in this file: 3
lines so far:      305
git status of this file: ?? docs/reports/2026-11-11-hermes-replies-grading-worker2.md
~~~~
The three fragment lines are 155–157 (the V7 command and its two output labels), as listed by `/usr/bin/grep -n -i 'la07dsh' <this file> | cut -d: -f1` → `155`, `156`, `157`. The file is untracked and unstaged.

## Result

Result: FAIL

All eight re-runs REPRODUCE (R1–R8). No evidence block of worker 1's failed to reproduce. The failure is in grade levels: seven grades or omissions are more generous than the disk evidence.

- W2-1: B7 DONE should be NOT ASSESSABLE FROM DISK. "Every command" is a completeness claim, the ASKED column was narrowed to "(VM commands)", and it contradicts worker 1's own B42 (W1:58 vs W1:93).
- W2-2: B17 NOT ASSESSABLE should be NOT DONE (OBSERVED). T4 asks for placement "Before step 1 item 1 ... in the self-report"; the file has item 1 at B:8 and 0a at B:32/B:62. Worker 1 inserted "run" into the ASKED text (W1:68).
- W2-3: B36 NOT APPLICABLE and B37 DONE rest on a worker's own reading that adds a condition to §1 limit 9. Handoff:23 says no term relaxes a §1 limit. The grade should be OPEN (NOT DONE on the literal text), routed to the master. The counter-reading was disclosed (W1:87–88, W1:160).
- W2-4: C13 DONE contradicts worker 1's own S2 item 3 (W1:111 vs W1:161). It should be NOT ASSESSABLE. Mitigation: the rescued NT8 AddOns folders are empty (V13).
- W2-5: C18 DONE sits above its own NOT ASSESSABLE parts C11 and C22 (W1:116 vs W1:109, W1:120).
- W2-6: A2 DONE is backed by file order only. Limit 11's "before your first step" is not on disk, and the 54 s gap between stamp and write is unexplained (W1:38, V4).
- W2-7: There is no graded row for §1 limit 3 / handoff:106. Worker 1's own E19 (extended in V5) places NT8's start 10–59 s (zone −05:00) or 23 s (−04:00, offset 0) after STARTED in two of the three feasible cases. That calls for a NOT ASSESSABLE row with an escalation, not prose only (W1:189–212).

Not counted, as defensible readings or S1/S2 notes: the STATUS scope decision (its premise is overstated at W1:31); C20 (too harsh); C15 (DONE at INFERRED level); E7 containment versus equality (true by V9); W1:5's unbacked "nothing was staged"; and W1:21's script, which is not pasted.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
