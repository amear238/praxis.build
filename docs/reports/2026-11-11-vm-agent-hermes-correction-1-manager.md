# Manager report: 2026-11-11-vm-agent-hermes-correction-1

## Task
Correction 1 (strike 1) for unit 2026-11-10-vm-agent-hermes-ssh after a cold praxis-auditor FAIL on S1, S2, S7 and (ii) personal data. Cures: S1 re-run of every flagged block in a new report; S2 relabel of manager report :79/:81 as a precondition observation (UNTESTED), original lines left on disk; (ii) de-identification of the rep-name token in the evidence PNG path in exactly four lines (decided by the master under D-2026-11-08-D D1, method of commit 18d94a5); MANIFEST rows; adversarial re-check.

## Rubric criteria addressed
- S1, S2, S7, S13 (specs/SPEC_RUBRIC.md lines 124, 125, 130, 136).

## Workers dispatched
| id | mode | scope | outcome |
|---|---|---|---|
| worker 1 | BUILD | de-identify the four named lines; itemise; count proof | done; report -worker1.md |
| worker 2 | BUILD | S1 cure: re-run every flagged check, raw output, verdict per claim | done; report -worker2.md; 68 claim rows: 60 REPRODUCED, 3 NOT REPRODUCED, 5 DIFFERENT (worker 2's own summary table) |
| worker 3 | ADVERSARIAL | re-check of workers 1 and 2 | hit its 40-turn cap; wrote no report; scratch files under /tmp/hermes-corr1-w3/ only; nothing of it is relied on below except the manager's own cmp of its scratch files (shown) |
| worker 4 | ADVERSARIAL | re-check of workers 1 and 2 (fresh, did not reuse worker 3's scratch) | done; report -worker4.md; no BLOCKER; A1, A3, A5, A6 MINOR (S1/S2), A2, A4, A7, A8 NOTE |
| worker 5 | BUILD (fix) | cure A1-A7 in place in -worker1.md and -worker2.md | done; also wrote outside scope under .claude/agent-memory/ (reverted by the manager, see Process log) |
| worker 6 | ADVERSARIAL | re-check of the worker 5 fix | done; report -worker6.md; no BLOCKER; B1-B4 MINOR, B5-B6 NOTE |
| worker 7 | BUILD (fix) | cure B1-B6 in place in -worker1.md and -worker2.md | done; no report of its own (its changes are listed in the Fix log of each worker report) |
| worker 8 | ADVERSARIAL | re-check of the worker 7 fix | done; report -worker8.md; no BLOCKER; C1-C3 MINOR, C4-C7 NOTE |

## Process log
1. Read specs/SPEC_RUBRIC.md lines 124, 125, 130, 136 (S1, S2, S7, S13). Took sha256 baselines of the five 2026-11-10 reports and the protected files, and snapshot copies of the five reports in /tmp/hermes-corr1-mgr-orig/ (output in Verification evidence, block E0).
2. Wrote this skeleton (noclobber).
3. Dispatched worker 1 (de-identification) and worker 2 (S1 re-runs) in parallel. Worker 2 read the flagged blocks from the snapshot copies so line numbers were stable while worker 1 edited four lines.
4. Re-ran worker 1's diffs and count proof myself (blocks E1, E2). Wrote the S2 correction section (by the manager; pure doc text).
5. Worker 3 (adversarial) stopped at its turn cap with no report. Re-dispatched as worker 4 with a turn budget. Worker 4 found MINOR S1/S2 defects in both worker reports; dispatched fix worker 5, then adversarial worker 6 on the fix, which found further MINOR S1/S2 defects (B1-B4); dispatched fix worker 7.
6. Worker 5 wrote a new file .claude/agent-memory/praxis-worker/feedback_grep-is-shell-function.md and inserted one pointer line at MEMORY.md line 10 in the same folder (both gitignored by .gitignore:26). The brief forbids edits under .claude/. The manager deleted the file and the line (block E5). There is no pre-edit baseline of MEMORY.md, so exact restoration to the earlier bytes is not proven; what is shown is that the pointer line and the file are gone and the line count is back to 10.
7. Appended five MANIFEST rows (by the manager; pure doc text) for the new reports -manager, -worker1, -worker2, -worker4, -worker6 (block E6). Worker 3, 5 and 7 wrote no report of their own. Not added: UPDATE rows for the three 2026-11-10 reports edited by worker 1, since the brief scoped rows to new reports; flagged to the master.
8. Re-ran the two NOT REPRODUCED manager-report claims (:45, :65) myself (block E3).
9. Worker 8 found three MINOR defects (C1 a miscount 18 vs 17 in worker 1's fix log; C2 an unevidenced "contains no token" sentence in both reports; C3 "proven by hash" for the index on two-point equality). The manager confirmed C1 by command (block E6) and made six one-line rewordings itself, one line for one line, each tagged in the text "[manager edit 2026-11-11, adversarial finding Cn]"; the diff against a copy taken just before is in block E6. These six manager edits were not re-checked by a further adversarial worker; the diff is the only check on them.
10. Added a sixth MANIFEST row for -worker8.md and amended the two fresh rows for -worker1.md and -worker2.md (written in this session, uncommitted) to name the manager edits.
11. Ran the final verification script (block E6). Nothing staged at any point.

## S2 correction: manager report :79/:81
Manager report `docs/reports/2026-11-10-vm-agent-hermes-ssh.md` line 79 is headed "Negative tests (the gates trip)." and line 81 shows an `ls vm/replies/*-CODE-*.md` with the comment "before placement: Hermes gate 1 stays closed". That was mislabelled. What was observed is a precondition: no CODE- reply existed in vm/replies/ before placement. Hermes was never run in that unit, so Hermes's gate 1 was never tripped. Level of Hermes gate 1 = UNTESTED (specified only, by the handoff and the CODE- reply; not observed under failure). Lines 79 and 81 are not edited; the wrong lines stay on disk beside this correction (append-only rule). The second command in that block (noclobber refusal of a second write to the placed reply, lines 83-84) is a shell-option behaviour observed on the Mac; it is not a Hermes gate either.

The original lines as they stand on disk now:
```
$ sed -n '79p;81p' docs/reports/2026-11-10-vm-agent-hermes-ssh.md
**Negative tests (the gates trip).**
$ ls vm/replies/*-CODE-*.md        # before placement: Hermes gate 1 stays closed
```

## Verification evidence (command output)
In every block below the rep-name token is obtained at runtime and never typed: `f=$(ls docs/reports/evidence/ | grep '^2026-10-28-mffu-.*-reply\.png$'); T=${f#2026-10-28-mffu-}; T=${T%-reply.png}`. Blocks E0, E1, E3 and E5 were run once, earlier in this session; their output is pasted as captured.

E0. Baselines before any dispatch (09:4x local, 2026-11-11):
```
$ mkdir -p /tmp/hermes-corr1-mgr-orig && cp -p docs/reports/2026-11-10-vm-agent-hermes-ssh*.md /tmp/hermes-corr1-mgr-orig/ && shasum -a 256 /tmp/hermes-corr1-mgr-orig/* docs/reports/2026-11-10-vm-agent-hermes-ssh*.md vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md DECISIONS.md vm/2026-11-06-vm-handoff.md MANIFEST.md; wc -l MANIFEST.md
9cd0c5c6342f5f1ca63ee799ff1dfe0fd32c13ad517e7d42a4d25120e6d531ae  /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker1.md
c43da4d78a2833f554a9fd61389efe1de41c712d6d1d1eae353c16129c4cf6b2  /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker2.md
16791c5a1606f4bfb682668f082cb19f9745bdc76e7da70ff0e5e8c76c58e77d  /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md
6ec6224f4121df0f3b42b30b18705eb72942caa810969e02d2debbb35a7e43d6  /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md
07720470a99318d226327708d4592f0a5570c4c08871ac28cbbf5bc602bb9e12  /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md
9cd0c5c6342f5f1ca63ee799ff1dfe0fd32c13ad517e7d42a4d25120e6d531ae  docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md
c43da4d78a2833f554a9fd61389efe1de41c712d6d1d1eae353c16129c4cf6b2  docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md
16791c5a1606f4bfb682668f082cb19f9745bdc76e7da70ff0e5e8c76c58e77d  docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md
6ec6224f4121df0f3b42b30b18705eb72942caa810969e02d2debbb35a7e43d6  docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md
07720470a99318d226327708d4592f0a5570c4c08871ac28cbbf5bc602bb9e12  docs/reports/2026-11-10-vm-agent-hermes-ssh.md
2b729b8e4469a1c3454dadba08ddcd9e48a387f201e583c5e326f66569ce2ed0  vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
39e5ba0c27a1aab9736d6f23ce28efbb663bfcd1bcab5b5f305b2911669bc637  DECISIONS.md
ff4ba4ac512d9f59ed363563e49c88129a3da0864310f8bf6de2f714199c8c42  vm/2026-11-06-vm-handoff.md
3079813cd7c8cff560284e22acb2eefa0c3f6eac1f6bf68f4fb246ca06f0d955  MANIFEST.md
     371 MANIFEST.md
$ shasum -a 256 DECISION_LOG.md DISPATCH_LOG.md HANDOFF.md STATUS.md docs/reports/evidence/2026-10-28-mffu-*-reply.png | sed -E 's/(mffu-)[a-z]+(-reply)/\1<rep>\2/'; git diff --cached --name-only | sed -E 's/(mffu-)[a-z]+(-reply)/\1<rep>\2/'; git ls-files -s | shasum -a 256
b08af05dfe2170fcfebb02f271ce0937961847ba193778000cc6b74a31a233aa  DECISION_LOG.md
afc97f95cd97692e84a7efc85773e6a12c6b6ef2c8f214da5235a5cf3ce77cf2  DISPATCH_LOG.md
71cf456c349ba85b039818b33dc1135218b77ccd78ce37352b5b246ae1cb02a4  HANDOFF.md
c06e4b26120ac3c37607d06d6424b9628aa8bcbf6c67adc62a91cdc74bd92564  STATUS.md
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
5ac1ef7d17ce98a5e256863a10288b12541a502959ffffe3ba79eb282e638ac6  -
```

E1. Manager re-run of the four de-identification edits against the manager's own snapshot (after worker 1 returned):
```
$ O=/tmp/hermes-corr1-mgr-orig; for x in <the five 2026-11-10 report names>; do echo "== $x"; diff -U0 $O/$x docs/reports/$x | sed "s/$T/<the rep-name token>/g"; echo "wc -l orig/new: $(wc -l < $O/$x) $(wc -l < docs/reports/$x)"; done
== 2026-11-10-vm-agent-hermes-ssh.md
--- /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md	2026-11-10 16:18:43
+++ docs/reports/2026-11-10-vm-agent-hermes-ssh.md	2026-11-11 09:53:19
@@ -39 +39 @@
-docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
+docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
@@ -123 +123 @@
-The real index still holds only docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png.
+The real index still holds only docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png.
wc -l orig/new:      138      138
== 2026-11-10-vm-agent-hermes-ssh-worker1.md
--- /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker1.md	2026-11-10 15:54:00
+++ docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md	2026-11-11 09:53:19
@@ -48 +48 @@
-docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
+docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
wc -l orig/new:      108      108
== 2026-11-10-vm-agent-hermes-ssh-worker2.md
wc -l orig/new:      174      174
== 2026-11-10-vm-agent-hermes-ssh-worker3.md
--- /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md	2026-11-10 16:10:11
+++ docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md	2026-11-11 09:53:19
@@ -134 +134 @@
-docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
+docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
wc -l orig/new:      202      202
== 2026-11-10-vm-agent-hermes-ssh-worker4.md
wc -l orig/new:      141      141
```
(The loop ran over the five literal file names 2026-11-10-vm-agent-hermes-ssh.md, -worker1.md, -worker2.md, -worker3.md, -worker4.md; the placeholder in the pasted command line stands for that list only.) The files are untracked, so `git diff -U0 -- <file>` shows nothing for them; `diff -U0` against the snapshot is the diff that shows the change. Itemised, the four changes are:

| file | line | before | after |
|---|---|---|---|
| docs/reports/2026-11-10-vm-agent-hermes-ssh.md | 39 | `docs/reports/evidence/2026-10-28-mffu-`(the rep-name token)`-reply.png` | `docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png` |
| docs/reports/2026-11-10-vm-agent-hermes-ssh.md | 123 | `The real index still holds only docs/reports/evidence/2026-10-28-mffu-`(the rep-name token)`-reply.png.` | `The real index still holds only docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png.` |
| docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md | 48 | `docs/reports/evidence/2026-10-28-mffu-`(the rep-name token)`-reply.png` | `docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png` |
| docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md | 134 | `docs/reports/evidence/2026-10-28-mffu-`(the rep-name token)`-reply.png` | `docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png` |

Caveat (S1/S2, stated plainly): lines 39, 48 and 134 sit inside pasted command-output blocks. After the edit they are a de-identified rendering of that output, not the raw bytes the command printed, and the `<rep>` path does not name a file on disk. This is the cost of the master's D1 decision, same as in the D9 de-identification.

E3. Manager re-run of the two manager-report claims worker 2 found NOT REPRODUCED:
```
$ tail -1 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | command grep -cxF '<the S13 sentence>'
0
$ tail -1 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | command grep -cxF -- "$S13"
1
$ sed -n 66,70p docs/reports/2026-11-10-vm-agent-hermes-ssh.md
vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:2
vm/2026-11-06-vm-handoff.md:1
MANIFEST.md:1
DECISIONS.md:1
$ ls vm/replies
$ echo | command grep -c 20261110T211738Z
0
$ command grep -c 20261110T211738Z vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md DECISIONS.md vm/2026-11-06-vm-handoff.md MANIFEST.md
vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:2
DECISIONS.md:1
vm/2026-11-06-vm-handoff.md:1
MANIFEST.md:1
```
($S13 was set in the same shell to the S13 sentence.) Manager :45 as written gives 0, not 1; the corrected check gives 1. Manager :65 as written (no file argument) prints one bare count; with the four files named, the four counts match lines 66-69.

E4. Manager cmp of worker 3's abandoned scratch files (pasted block vs its re-run), for the record only:
```
$ cd /tmp/hermes-corr1-w3 && for p in *.pasted; do b=${p%.pasted}; if cmp -s $p $b.mine; then echo "$b SAME"; else echo "$b DIFF"; fi; done
mgr-79-81 SAME
w1-1 SAME
w1-4a SAME
w1-4b SAME
w1-4c SAME
w1-4d DIFF
w1-4e SAME
w2-A1 SAME
w2-A3 SAME
w2-A4 SAME
w2-B9 SAME
w2-C1i SAME
w2-setupS13 SAME
$ diff w1-4d.pasted w1-4d.mine; cmp w1-4d.pasted.sectsorted w1-4d.mine.sectsorted && echo sorted-same
5d4
< docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md:0
6a6
> docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md:0
8a9
> docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md:0
12d12
< docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md:0
sorted-same
```

E5. Revert of worker 5's out-of-scope write under .claude/:
```
$ git check-ignore -v .claude/agent-memory/praxis-worker/MEMORY.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/MEMORY.md
$ cd .claude/agent-memory/praxis-worker && wc -l MEMORY.md && tail -2 MEMORY.md | cut -c1-80 && sed -i '' '10{/feedback_grep-is-shell-function\.md/d;}' MEMORY.md && rm feedback_grep-is-shell-function.md && wc -l MEMORY.md && grep -c 'grep-is-shell' MEMORY.md; ls feedback_grep-is-shell-function.md 2>&1
      11 MEMORY.md
- [grep is a shell function](feedback_grep-is-shell-function.md) — tool zsh `gre
- [Gate harness fake process](project_gate-harness-fake-process.md) — use exec -
      10 MEMORY.md
0
ls: feedback_grep-is-shell-function.md: No such file or directory
```
E6. Final verification, run once after every worker had returned and after the manager edits, by a small zsh runner (/tmp/hermes-corr1-mgr/run.sh: for each line of /tmp/hermes-corr1-mgr/cmds.txt it prints "$ " plus the line, then evals it in one shell, stderr folded into stdout). The output below is the runner's output file pasted whole. It re-runs E1 exactly (no placeholder), gives the count proof, the protected-file hashes, the S13 check, the MANIFEST check, the worker 2 tally, the diff of the six manager edits, the memory revert check and numstat. At the time it ran, this report already held its final Result and S13 lines but not this block, which is why its own S13 check reads 1/1 and it is left out of the numstat loop.
```
$ cd /Volumes/Sensidine/Praxis.build
$ f=$(ls docs/reports/evidence/ | command grep '^2026-10-28-mffu-.*-reply\.png$'); T=${f#2026-10-28-mffu-}; T=${T%-reply.png}; echo "token length ${#T}"
token length 4
$ for x in 2026-11-10-vm-agent-hermes-ssh.md 2026-11-10-vm-agent-hermes-ssh-worker1.md 2026-11-10-vm-agent-hermes-ssh-worker2.md 2026-11-10-vm-agent-hermes-ssh-worker3.md 2026-11-10-vm-agent-hermes-ssh-worker4.md; do echo "== $x"; diff -U0 /tmp/hermes-corr1-mgr-orig/$x docs/reports/$x | sed "s/$T/<the rep-name token>/g"; echo "wc -l orig/new: $(wc -l < /tmp/hermes-corr1-mgr-orig/$x) $(wc -l < docs/reports/$x); wc -c orig/new: $(wc -c < /tmp/hermes-corr1-mgr-orig/$x) $(wc -c < docs/reports/$x)"; done
== 2026-11-10-vm-agent-hermes-ssh.md
--- /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md	2026-11-10 16:18:43
+++ docs/reports/2026-11-10-vm-agent-hermes-ssh.md	2026-11-11 09:53:19
@@ -39 +39 @@
-docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
+docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
@@ -123 +123 @@
-The real index still holds only docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png.
+The real index still holds only docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png.
wc -l orig/new:      138      138; wc -c orig/new:    10073    10075
== 2026-11-10-vm-agent-hermes-ssh-worker1.md
--- /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker1.md	2026-11-10 15:54:00
+++ docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md	2026-11-11 09:53:19
@@ -48 +48 @@
-docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
+docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
wc -l orig/new:      108      108; wc -c orig/new:    10107    10108
== 2026-11-10-vm-agent-hermes-ssh-worker2.md
wc -l orig/new:      174      174; wc -c orig/new:    18394    18394
== 2026-11-10-vm-agent-hermes-ssh-worker3.md
--- /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md	2026-11-10 16:10:11
+++ docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md	2026-11-11 09:53:19
@@ -134 +134 @@
-docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
+docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
wc -l orig/new:      202      202; wc -c orig/new:    14731    14732
== 2026-11-10-vm-agent-hermes-ssh-worker4.md
wc -l orig/new:      141      141; wc -c orig/new:    13437    13437
$ git diff -U0 -- docs/reports/2026-11-10-vm-agent-hermes-ssh.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md | wc -l
       0
$ git status --short -- docs/reports/2026-11-10-vm-agent-hermes-ssh.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md
?? docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md
?? docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md
?? docs/reports/2026-11-10-vm-agent-hermes-ssh.md
$ for x in docs/reports/2026-11-10-vm-agent-hermes-ssh.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md; do echo "$x grep-c=$(command grep -c -- "$T" $x) grep-ci=$(command grep -ci -- "$T" $x)"; done
docs/reports/2026-11-10-vm-agent-hermes-ssh.md grep-c=0 grep-ci=0
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md grep-c=0 grep-ci=0
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md grep-c=0 grep-ci=0
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md grep-c=0 grep-ci=0
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md grep-c=0 grep-ci=0
vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md grep-c=0 grep-ci=0
$ command grep -n '^## .*D-2026-11-10-C' DECISIONS.md | cut -c1-60; wc -l < DECISIONS.md
2076:## 2026-11-10 — D-2026-11-10-C: VM agent = Hermes over 
    2099
$ echo "DECISIONS.md:2076-2099 (D-2026-11-10-C) grep-c=$(sed -n '2076,2099p' DECISIONS.md | command grep -c -- "$T") grep-ci=$(sed -n '2076,2099p' DECISIONS.md | command grep -ci -- "$T")"
DECISIONS.md:2076-2099 (D-2026-11-10-C) grep-c=0 grep-ci=0
$ command grep -n 'Amendment 3' vm/2026-11-06-vm-handoff.md | cut -c1-50
23:- **Amendment 3 (2026-11-10):** the VM agent is
$ echo "vm/2026-11-06-vm-handoff.md:23 (Amendment 3) grep-c=$(sed -n '23p' vm/2026-11-06-vm-handoff.md | command grep -c -- "$T") grep-ci=$(sed -n '23p' vm/2026-11-06-vm-handoff.md | command grep -ci -- "$T")"
vm/2026-11-06-vm-handoff.md:23 (Amendment 3) grep-c=0 grep-ci=0
$ for x in docs/reports/2026-11-11-vm-agent-hermes-correction-1-*.md; do echo "$x grep-ci=$(command grep -ci -- "$T" $x)"; done
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md grep-ci=0
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md grep-ci=0
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md grep-ci=0
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker4.md grep-ci=0
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker6.md grep-ci=0
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker8.md grep-ci=0
$ command grep -c -- '<rep>' docs/reports/2026-11-10-vm-agent-hermes-ssh.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md
docs/reports/2026-11-10-vm-agent-hermes-ssh.md:2
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md:1
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md:1
$ shasum -a 256 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md DECISIONS.md vm/2026-11-06-vm-handoff.md HANDOFF.md STATUS.md DECISION_LOG.md DISPATCH_LOG.md
2b729b8e4469a1c3454dadba08ddcd9e48a387f201e583c5e326f66569ce2ed0  vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
39e5ba0c27a1aab9736d6f23ce28efbb663bfcd1bcab5b5f305b2911669bc637  DECISIONS.md
ff4ba4ac512d9f59ed363563e49c88129a3da0864310f8bf6de2f714199c8c42  vm/2026-11-06-vm-handoff.md
71cf456c349ba85b039818b33dc1135218b77ccd78ce37352b5b246ae1cb02a4  HANDOFF.md
c06e4b26120ac3c37607d06d6424b9628aa8bcbf6c67adc62a91cdc74bd92564  STATUS.md
b08af05dfe2170fcfebb02f271ce0937961847ba193778000cc6b74a31a233aa  DECISION_LOG.md
50216d3ade2b5c2488bfabacc07f1f1320ba7aa7a54fbdda1091646893049bb0  DISPATCH_LOG.md
$ shasum -a 256 docs/reports/evidence/$f | sed "s/$T/<rep>/"
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
$ git ls-files -s | shasum -a 256
5ac1ef7d17ce98a5e256863a10288b12541a502959ffffe3ba79eb282e638ac6  -
$ git diff --cached --name-only | sed "s/$T/<rep>/"
docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
$ git rev-parse --short HEAD
55979ee
$ S13='Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'; for x in docs/reports/2026-11-11-vm-agent-hermes-correction-1-*.md; do echo "$x S13-lines=$(command grep -cxF -- "$S13" $x) last-line-is-S13=$(tail -1 $x | command grep -cxF -- "$S13")"; done
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md S13-lines=1 last-line-is-S13=1
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md S13-lines=1 last-line-is-S13=1
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md S13-lines=1 last-line-is-S13=1
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker4.md S13-lines=1 last-line-is-S13=1
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker6.md S13-lines=1 last-line-is-S13=1
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker8.md S13-lines=1 last-line-is-S13=1
$ git diff --numstat -- MANIFEST.md
22	0	MANIFEST.md
$ head -n 371 MANIFEST.md | shasum -a 256; wc -l < MANIFEST.md; tail -n +372 MANIFEST.md | cut -d'|' -f2-5
3079813cd7c8cff560284e22acb2eefa0c3f6eac1f6bf68f4fb246ca06f0d955  -
     377
 /docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md | Report | 3 | 2026-11-11 
 /docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md | Report | 3 | 2026-11-11 
 /docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md | Report | 3 | 2026-11-11 
 /docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker4.md | Report | 3 | 2026-11-11 
 /docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker6.md | Report | 3 | 2026-11-11 
 /docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker8.md | Report | 3 | 2026-11-11 
$ for x in docs/reports/2026-11-11-vm-agent-hermes-correction-1-*.md; do wc -l < $x | tr -d ' '; done | paste -sd' ' -
207 696 1045 410 307 295
$ tail -4 DISPATCH_LOG.md | cut -c1-120
- [2026-11-11T15:33:31Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: sess
- [2026-11-11T15:44:14Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close fo
- [2026-11-11T15:44:33Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: sess
- [2026-11-11T15:50:15Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close fo
$ W2=docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md; S=$(command grep -n '^## Summary table' $W2 | cut -d: -f1); E=$(command grep -n '^## Result' $W2 | cut -d: -f1); echo "summary table lines $S-$E"
summary table lines 801-860
$ sed -n "${S},${E}p" $W2 | command grep -E '^\| [0-9]' | wc -l
      49
$ sed -n "${S},${E}p" $W2 | command grep -E '^\| [0-9]' | awk -F'|' '{print $(NF-1)}' | sed -E 's/^ (REPRODUCED|NOT REPRODUCED|DIFFERENT).*/\1/' | sort | uniq -c
   5 DIFFERENT
   3 NOT REPRODUCED
  41 REPRODUCED
$ sed -n "${S},${E}p" $W2 | command grep -E '^\| 49'  | cut -c1-60
| 49–68 | worker4 :112–131 | 20 citations point where they s
$ sed -n "${S},${E}p" $W2 | command grep '^Totals'
Totals over the 68 rows: **REPRODUCED 60, NOT REPRODUCED 3, DIFFERENT 5.**
$ for x in worker1 worker2; do echo "== $x"; diff -U0 /tmp/hermes-corr1-mgr/pre-c/2026-11-11-vm-agent-hermes-correction-1-$x.md docs/reports/2026-11-11-vm-agent-hermes-correction-1-$x.md; done
== worker1
--- /tmp/hermes-corr1-mgr/pre-c/2026-11-11-vm-agent-hermes-correction-1-worker1.md	2026-11-11 10:43:43
+++ docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md	2026-11-11 10:50:54
@@ -17 +17 @@
-- The index digest (`git ls-files -s | shasum -a 256`) equals the pre-dispatch baseline from the manager's brief (quoted in W7-1, compared by command in W7-2: MATCH), and the cached list is only the PNG. That the PNG was staged before this unit rests on that digest equality; no session-start git status is pasted in this report. HEAD is still 55979ee. So no content was added to the index and nothing was committed.
+- The index digest (`git ls-files -s | shasum -a 256`) equals the pre-dispatch baseline from the manager's brief (quoted in W7-1, compared by command in W7-2: MATCH), and the cached list is only the PNG. That the PNG was staged before this unit rests on that digest equality; no session-start git status is pasted in this report. HEAD is still 55979ee. The digest was equal at two moments; that does not prove the index never changed in between. HEAD unchanged shows nothing was committed [manager edit 2026-11-11, adversarial finding C3].
@@ -476 +476 @@
-- **Index.** The digest is 5ac1ef7d…8ac6, equal to the pre-dispatch baseline from the manager's brief (quoted in W7-1, compared by command in W7-2: MATCH). The cached list is only the PNG, which shows as `A `. That it was staged before this unit follows from the digest equality; the session-start git status is not pasted here. HEAD is still 55979ee. So no content was added to the index and nothing was committed. This is proven by hash.
+- **Index.** The digest is 5ac1ef7d…8ac6, equal to the pre-dispatch baseline from the manager's brief (quoted in W7-1, compared by command in W7-2: MATCH). The cached list is only the PNG, which shows as `A `. That it was staged before this unit follows from the digest equality; the session-start git status is not pasted here. HEAD is still 55979ee. The digest was equal at two moments; that does not prove the index never changed in between. HEAD unchanged shows nothing was committed [manager edit 2026-11-11, adversarial finding C3].
@@ -492 +492 @@
-- No content was added to the index: the digest equals the pre-dispatch baseline from the manager's brief (W7-2: MATCH), and the cached list is only the pre-staged PNG.
+- The index digest was equal at two moments (not proof that it never changed in between) [manager edit 2026-11-11, adversarial finding C3]: it equals the pre-dispatch baseline from the manager's brief (W7-2: MATCH), and the cached list is only the pre-staged PNG.
@@ -649 +649 @@
-Next is the count over the whole of both reports, run in a separate call. It ran after W7-2 was in place and before this W7-3 text and the worker 7 fix-log entries were added. None of that later text contains the token. The re-run after the last edit is in the worker 7 return to the manager.
+Next is the count over the whole of both reports, run in a separate call. It ran after W7-2 was in place and before this W7-3 text and the worker 7 fix-log entries were added. That this later text holds no rep-name token is not shown in this report (an uncaptured statement, not evidence); the count over this file after the last edit is pasted in the manager report, block E6 [manager edit 2026-11-11, adversarial finding C2].
@@ -693 +693 @@
-  - :497-659 (new): the "Worker 7 evidence" section. W7-1 (:501) quotes the brief baselines as text. W7-2 (:523) holds the runner, three chunks of command output (18 MATCH compares, an awk tying the pasted values at :53-57, :66-68, :297, :299, :388, :390, :404, :437-439 and :442 to the baselines, the byte count and locale, the birth time, `type grep` against `zsh -c`, and the untracked count) and its reading (:631). W7-3 (:638) holds the leak-checks.
+  - :497-659 (new): the "Worker 7 evidence" section. W7-1 (:501) quotes the brief baselines as text. W7-2 (:523) holds the runner, three chunks of command output (17 MATCH compares [corrected from 18 by the manager 2026-11-11, adversarial finding C1], an awk tying the pasted values at :53-57, :66-68, :297, :299, :388, :390, :404, :437-439 and :442 to the baselines, the byte count and locale, the birth time, `type grep` against `zsh -c`, and the untracked count) and its reading (:631). W7-3 (:638) holds the leak-checks.
== worker2
--- /tmp/hermes-corr1-mgr/pre-c/2026-11-11-vm-agent-hermes-correction-1-worker2.md	2026-11-11 10:43:51
+++ docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md	2026-11-11 10:50:54
@@ -1003 +1003 @@
-Next is the count over the whole of both reports, run in a separate call. It ran after W7-2 was in place and before this W7-3 text and the worker 7 fix-log entries were added. None of that later text contains the token. The re-run after the last edit is in the worker 7 return to the manager.
+Next is the count over the whole of both reports, run in a separate call. It ran after W7-2 was in place and before this W7-3 text and the worker 7 fix-log entries were added. That this later text holds no rep-name token is not shown in this report (an uncaptured statement, not evidence); the count over this file after the last edit is pasted in the manager report, block E6 [manager edit 2026-11-11, adversarial finding C2].
$ ls -la .claude/agent-memory/praxis-worker/ | command grep -c 'grep-is-shell'; command grep -c 'grep-is-shell' .claude/agent-memory/praxis-worker/MEMORY.md
0
0
$ git status --short --untracked-files=all -- docs/reports/2026-11-11-vm-agent-hermes-correction-1-*.md MANIFEST.md docs/reports/2026-11-10-vm-agent-hermes-ssh*.md
 M MANIFEST.md
?? docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md
?? docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md
?? docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md
?? docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md
?? docs/reports/2026-11-10-vm-agent-hermes-ssh.md
?? docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md
?? docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md
?? docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md
?? docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker4.md
?? docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker6.md
?? docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker8.md
$ git diff --numstat -- MANIFEST.md; for x in docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker*.md; do git diff --no-index --numstat /dev/null $x; done
22	0	MANIFEST.md
696	0	/dev/null => docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md
1045	0	/dev/null => docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md
410	0	/dev/null => docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker4.md
307	0	/dev/null => docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker6.md
295	0	/dev/null => docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker8.md
```
Reading of E6 (manager): the rep-name token count is 0 (case-sensitive and case-insensitive) in the five 2026-11-10 reports, the CODE- reply, D-2026-11-10-C (DECISIONS.md :2076-2099) and Amendment 3 (handoff :23), and in all six correction-1 reports. The protected files other than DISPATCH_LOG.md hash equal to E0; DISPATCH_LOG.md differs by hook-written rows (its tail is shown). Index digest and cached list are as in E0. Worker 2's table tallies 41 REPRODUCED rows (one of them, row 49-68, covers 20 claims), 3 NOT REPRODUCED and 5 DIFFERENT, which matches its own totals line of 60/3/5 over 68.

## Adversarial findings
Worker 4 (on workers 1 and 2), from its report -worker4.md: no BLOCKER. A1 MINOR S1 (worker 1 count proof shown under `$ echo` labels), A2 NOTE (`grep` in the tool shell is a shell function; multi-file output order is unstable; this explains the order-only DIFF in block E4), A3 MINOR S1 (worker 1 "index and /tmp/idx-hermes not edited" with no command), A4 NOTE S2 (PNG "unmodified" on date and size only), A5 MINOR S1 (worker 2 "placement changed only the placeholders" without output), A6 MINOR S2 (worker 2 "unchanged" inferred from mtimes), A7 NOTE (entry cited at :2075, heading is :2076), A8 NOTE out of scope (the rep-name token is still present in other files under docs/reports; see "Open items for the master"). Cured by fix worker 5.

Worker 6 (on the worker 5 fix), from its report -worker6.md: no BLOCKER. B1 MINOR S1 (leak check "printed 0" with no pasted command), B2 MINOR S1 (comparisons to baselines not shown in the report), B3 MINOR S1/S2 (snapshot hashes claimed without re-hash), B4 MINOR S2 (negative controls overstated), B5 and B6 NOTE (wording; time- and environment-dependent outputs). Every one of these was checked true by worker 6 on the substance; the defect is in how the evidence is shown. Sent to fix worker 7.

These summaries are the manager's reading of the two adversarial reports; the findings themselves, with their commands and output, are in those reports.

## S6 cross-block check
The one deviation in this unit is the master's D1 decision to edit four lines of already-written reports. Blocks it touches: (a) the append-only reporting rule: the edits replace text inside three ungraded, untracked 2026-11-10 reports, nothing is deleted or added, and the S2 correction leaves :79/:81 on disk (block E1, section S2 correction); (b) S1: three of the four edited lines are inside pasted-output blocks, so those blocks are now a de-identified rendering, not raw output (caveat under E1); (c) bead rpy (PNG staged alone in the real index): the PNG hash, the index digest and the cached-name list are unchanged (block E6); (d) S13: the edits touch no S13 line; the five 2026-11-10 reports' line counts are unchanged (E6). Tool-shell side effects observed: the SubagentStart/SubagentStop hook (scripts/dispatch-log-writeahead.sh) appended rows to DISPATCH_LOG.md on every dispatch, so its hash differs from E0 (E6); the unit did not edit it by hand. Worker 6 reports one deny by scripts/mint-guard.sh on a command whose text held the shell-snapshot path; it rebuilt the report another way (its report :18).

## Files changed (not staged)
- Edited, four lines only (de-identification): docs/reports/2026-11-10-vm-agent-hermes-ssh.md (:39, :123), docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md (:48), docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md (:134). Untracked files, so numstat against HEAD does not apply; E6 shows each is 1 changed line per edit with line counts unchanged.
- New reports: this report, -worker1.md, -worker2.md, -worker4.md, -worker6.md, -worker8.md (all docs/reports/2026-11-11-vm-agent-hermes-correction-1-*).
- MANIFEST.md: six rows appended at the end (lines 372-377); lines 1-371 byte-identical to their pre-unit state (E6).
- Out-of-scope write by worker 5 under .claude/agent-memory/ (gitignored): reverted (E5, E6).
- DISPATCH_LOG.md: rows appended by the SubagentStart/SubagentStop hook, not by hand (E6).

## Open items for the master
1. The rep-name token is still in other files under docs/reports (worker 4 finding A8), including file names in docs/reports/ and docs/reports/evidence/; out of this unit's scope.
2. No MANIFEST UPDATE rows were added for the three de-identified 2026-11-10 reports (brief scoped rows to new reports).
3. Three of the four de-identified lines are inside pasted-output blocks (caveat under E1).
4. The six manager one-line edits (process log step 9) have had a diff check only, no adversarial re-check.

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
