# 2026-11-11 vm-agent-hermes correction-1, worker 4 (ADVERSARIAL)

## Task
Unit 2026-11-11-vm-agent-hermes-correction-1, worker 4, mode ADVERSARIAL. Working dir /Volumes/Sensidine/Praxis.build, HEAD 55979ee. The job was to break the claims in correction-1-worker1.md (the de-identification of four lines) and correction-1-worker2.md (re-runs of flagged checks), against S1, S2 and S13. I edited nothing except this report. I staged nothing. I did not touch the git index, /tmp/idx-hermes, /tmp/hermes-corr1-w3/ or the PNG (the PNG was hashed only). Scratch outputs are in /tmp/hermes-corr1-w4/.

The rep-name token is never typed here. Every command gets it at runtime into `$T` with `f=$(ls docs/reports/evidence/ | grep '^2026-10-28-mffu-.*-reply\.png$'); T=${f#2026-10-28-mffu-}; T=${T%-reply.png}`. Every output was masked case-insensitively (`sed "s/$T/<the rep-name token>/gI"`, or the same in python with re.I). This report was put together by a python script that inserts the saved output files verbatim, after masking.

## Checks

### C1 — de-identification limited to exactly four lines
Command as run (zsh, repo root):
```
D=/tmp/hermes-corr1-w4; f=$(ls docs/reports/evidence/ | grep '^2026-10-28-mffu-.*-reply\.png$'); T=${f#2026-10-28-mffu-}; T=${T%-reply.png}; echo "token len ${#T}";
O=/tmp/hermes-corr1-mgr-orig; {
echo '$ shasum -a 256 snapshots'; (cd $O && shasum -a 256 *);
echo '$ shasum -a 256 live'; shasum -a 256 docs/reports/2026-11-10-vm-agent-hermes-ssh*.md;
echo '$ wc -l -c snapshot'; (cd $O && wc -l -c *);
echo '$ wc -l -c live'; wc -l -c docs/reports/2026-11-10-vm-agent-hermes-ssh*.md;
for n in ssh ssh-worker1 ssh-worker2 ssh-worker3 ssh-worker4; do fn=2026-11-10-vm-agent-hermes-$n.md; echo "\$ diff -U0 $O/$fn docs/reports/$fn"; diff -U0 $O/$fn docs/reports/$fn; echo "rc=$?"; done;
echo '$ cmp worker2 / worker4'; cmp $O/2026-11-10-vm-agent-hermes-ssh-worker2.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md; echo rc=$?; cmp $O/2026-11-10-vm-agent-hermes-ssh-worker4.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md; echo rc=$?;
echo '$ grep -ci TOKEN live five + new reports'; grep -ci "$T" docs/reports/2026-11-10-vm-agent-hermes-ssh*.md docs/reports/2026-11-11-vm-agent-hermes-correction-1-*.md;
echo '$ grep -ci TOKEN snapshots'; grep -ci "$T" $O/*;
echo '$ grep -n "<rep>" live five'; grep -n '<rep>' docs/reports/2026-11-10-vm-agent-hermes-ssh*.md;
echo '$ grep -rli TOKEN docs/reports (excluding evidence dir)'; grep -rli "$T" docs/reports --exclude-dir=evidence | head -50;
} > $D/c1.out 2>&1; sed "s/$T/<the rep-name token>/gI" $D/c1.out > $D/c1.masked; cat $D/c1.masked
```
Raw output (stdout line `token len 4`, then /tmp/hermes-corr1-w4/c1.masked):
```
token len 4
$ shasum -a 256 snapshots
9cd0c5c6342f5f1ca63ee799ff1dfe0fd32c13ad517e7d42a4d25120e6d531ae  2026-11-10-vm-agent-hermes-ssh-worker1.md
c43da4d78a2833f554a9fd61389efe1de41c712d6d1d1eae353c16129c4cf6b2  2026-11-10-vm-agent-hermes-ssh-worker2.md
16791c5a1606f4bfb682668f082cb19f9745bdc76e7da70ff0e5e8c76c58e77d  2026-11-10-vm-agent-hermes-ssh-worker3.md
6ec6224f4121df0f3b42b30b18705eb72942caa810969e02d2debbb35a7e43d6  2026-11-10-vm-agent-hermes-ssh-worker4.md
07720470a99318d226327708d4592f0a5570c4c08871ac28cbbf5bc602bb9e12  2026-11-10-vm-agent-hermes-ssh.md
$ shasum -a 256 live
5c16c0f6a9f5a8b214a047a0ea9e8ce9ccc053f5d7a9e8b9fc44ddc85827c4bc  docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md
c43da4d78a2833f554a9fd61389efe1de41c712d6d1d1eae353c16129c4cf6b2  docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md
27968c3f67b745b7ff64b642361437f5ee26cf0efa27e1fbcc58a2f8d23ec357  docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md
6ec6224f4121df0f3b42b30b18705eb72942caa810969e02d2debbb35a7e43d6  docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md
e0e648c41c8965524a98f342a29f224a706f9285672aa324489f6b64c32cb560  docs/reports/2026-11-10-vm-agent-hermes-ssh.md
$ wc -l -c snapshot
     108   10107 2026-11-10-vm-agent-hermes-ssh-worker1.md
     174   18394 2026-11-10-vm-agent-hermes-ssh-worker2.md
     202   14731 2026-11-10-vm-agent-hermes-ssh-worker3.md
     141   13437 2026-11-10-vm-agent-hermes-ssh-worker4.md
     138   10073 2026-11-10-vm-agent-hermes-ssh.md
     763   66742 total
$ wc -l -c live
     108   10108 docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md
     174   18394 docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md
     202   14732 docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md
     141   13437 docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md
     138   10075 docs/reports/2026-11-10-vm-agent-hermes-ssh.md
     763   66746 total
$ diff -U0 /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md docs/reports/2026-11-10-vm-agent-hermes-ssh.md
--- /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md	2026-11-10 16:18:43
+++ docs/reports/2026-11-10-vm-agent-hermes-ssh.md	2026-11-11 09:53:19
@@ -39 +39 @@
-docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
+docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
@@ -123 +123 @@
-The real index still holds only docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png.
+The real index still holds only docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png.
rc=1
$ diff -U0 /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker1.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md
--- /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker1.md	2026-11-10 15:54:00
+++ docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md	2026-11-11 09:53:19
@@ -48 +48 @@
-docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
+docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
rc=1
$ diff -U0 /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker2.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md
rc=0
$ diff -U0 /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md
--- /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md	2026-11-10 16:10:11
+++ docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md	2026-11-11 09:53:19
@@ -134 +134 @@
-docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
+docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
rc=1
$ diff -U0 /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md
rc=0
$ cmp worker2 / worker4
rc=0
rc=0
$ grep -ci TOKEN live five + new reports
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md:0
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md:0
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md:0
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md:0
docs/reports/2026-11-10-vm-agent-hermes-ssh.md:0
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker4.md:0
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md:0
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md:0
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md:0
$ grep -ci TOKEN snapshots
/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker3.md:1
/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker2.md:0
/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker1.md:1
/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh-worker4.md:0
/tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md:2
$ grep -n "<rep>" live five
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md:134:docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md:48:docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
docs/reports/2026-11-10-vm-agent-hermes-ssh.md:39:docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
docs/reports/2026-11-10-vm-agent-hermes-ssh.md:123:The real index still holds only docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png.
$ grep -rli TOKEN docs/reports (excluding evidence dir)
docs/reports/2026-10-28-f4-<the rep-name token>-reply-adversarial-final.md
docs/reports/2026-11-10-d9-housekeeping-manager.md
docs/reports/2026-11-10-housekeeping-2b-adversarial.md
docs/reports/2026-10-28-f4-<the rep-name token>-reply-adversarial-confirm.md
docs/reports/2026-11-02-r-vn3-1-filing-manager.md
docs/reports/2026-10-28-f4-<the rep-name token>-reply-adversarial-recheck.md
docs/reports/2026-11-09-c7-manager-memory-off-manager.md
docs/reports/2026-11-01-csv-analyses-manager.md
docs/reports/2026-11-10-housekeeping-2b-worker1.md
docs/reports/2026-10-30-zyd-rulings-append.md
docs/reports/2026-11-10-housekeeping-2a-manager.md
docs/reports/2026-11-10-scrub-forward-adversarial.md
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
docs/reports/2026-10-28-f4-<the rep-name token>-reply-worker3.md
docs/reports/2026-11-04-proof-of-concept-standard.md
docs/reports/2026-11-10-scrub-forward-manager.md
docs/reports/2026-11-10-c2-park-gate-resume-manager.md
docs/reports/2026-10-28-f4-<the rep-name token>-reply-worker1.md
docs/reports/2026-11-07-wf-mac-side-maths-manager.md
docs/reports/2026-11-10-housekeeping-2b-manager.md
docs/reports/2026-10-28-f4-<the rep-name token>-reply-adversarial-addendum.md
docs/reports/2026-11-02-tickprep-intake-manager.md
docs/reports/2026-11-06-post-commit-refresh-manager.md
docs/reports/2026-11-10-scrub-forward-c1-adversarial.md
docs/reports/2026-10-28-f4-<the rep-name token>-reply-worker9-fix.md
docs/reports/2026-10-28-f4-<the rep-name token>-reply-worker5-fix.md
docs/reports/2026-11-10-f1-f2-proposal-manager.md
docs/reports/2026-10-28-f4-<the rep-name token>-reply-adversarial-transcript.md
docs/reports/2026-10-28-f4-<the rep-name token>-reply-worker7-fix.md
docs/reports/2026-10-28-f4-<the rep-name token>-reply-filing.md
docs/reports/2026-11-08-voice-strategy-brief.md
docs/reports/2026-10-31-7zq-m3-append.md
docs/reports/2026-11-06-status-handoff-evening-manager.md
docs/reports/2026-10-31-7zq-m1-variants.md
docs/reports/2026-11-10-scrub-forward-worker1.md
docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md
```
Verdict: **HOLDS.**
- The snapshot hashes equal the five pre-edit hashes in the brief.
- diff -U0 shows exactly four changed lines: ssh.md :39 and :123, worker1 :48, worker3 :134. Each changes only the token to `<rep>`.
- worker2 and worker4: cmp rc=0, and the live sha256 is unchanged.
- The line counts are unchanged. The byte deltas are +2, +1 and +1, which fits a 4-character token replaced by the 5-character `<rep>`.
- The case-insensitive token count is 0 in all five live files and in all four correction-1 reports (manager, worker1, worker2 and this skeleton at the time).
- The snapshots held 2/1/1/0/0, which equals the four replaced lines.

Note (out of scope): the token is still present in 36 other files under docs/reports, including in filenames (see A8).

### C2 — byte-for-byte re-runs (4 worker1 blocks, 8 worker2 blocks)
Each pasted block was taken with `sed -n 'A,Bp' <report> > /tmp/hermes-corr1-w4/<id>.pasted`. The line ranges are below; the line numbers are the reports' own.
- worker1: w1-4b :143–174 (diff block), w1-4c :181–198 (wc), w1-4d :243–267 (the count proof), w1-4e :276–280 (sha256).
- worker2: w2-A1 :78–79 (NOT REPRODUCED), w2-A3 :139–144 (DIFFERENT), w2-A4a :166–167 (NOT REPRODUCED), w2-A4b :172–175, w2-B9 :300–305 (DIFFERENT), w2-C1i :474–497 (NOT REPRODUCED), w2-C1ie :503–506, w2-C1a :403–404 (DIFFERENT).

The worker1 commands were run in zsh, as worker1 states (Step 4a). They were exactly as pasted, with `O=/tmp/hermes-corr1-w1-orig; R=docs/reports` and `$T` set at runtime. For 4d, the `<same five files>` shorthand was expanded to the five paths, as worker1's :270 says it ran them. The `$ echo` labels were run as the echo commands they are:
```
for x in 2026-11-10-vm-agent-hermes-ssh.md 2026-11-10-vm-agent-hermes-ssh-worker1.md 2026-11-10-vm-agent-hermes-ssh-worker2.md 2026-11-10-vm-agent-hermes-ssh-worker3.md 2026-11-10-vm-agent-hermes-ssh-worker4.md; do echo; echo "\$ diff -U0 $O/$x $R/$x | sed mask"; diff -U0 $O/$x $R/$x | sed "s/$T/<the rep-name token>/g"; echo "[diff exit ${pipestatus[1]:-$PIPESTATUS}]"; done > $D/w1-4b.raw 2>&1
tail -n +2 $D/w1-4b.raw > $D/w1-4b.mine
for x in 2026-11-10-vm-agent-hermes-ssh.md 2026-11-10-vm-agent-hermes-ssh-worker1.md 2026-11-10-vm-agent-hermes-ssh-worker3.md; do echo "before:"; wc -l $O/$x; wc -c $O/$x; echo "after:"; wc -l $R/$x; wc -c $R/$x; done > $D/w1-4c.mine 2>&1
{ echo "== five reports: grep -c"; grep -c -- "$T" $R/2026-11-10-vm-agent-hermes-ssh.md $R/2026-11-10-vm-agent-hermes-ssh-worker1.md $R/2026-11-10-vm-agent-hermes-ssh-worker2.md $R/2026-11-10-vm-agent-hermes-ssh-worker3.md $R/2026-11-10-vm-agent-hermes-ssh-worker4.md
echo "== five reports: grep -ci"; grep -ci -- "$T" $R/2026-11-10-vm-agent-hermes-ssh.md $R/2026-11-10-vm-agent-hermes-ssh-worker1.md $R/2026-11-10-vm-agent-hermes-ssh-worker2.md $R/2026-11-10-vm-agent-hermes-ssh-worker3.md $R/2026-11-10-vm-agent-hermes-ssh-worker4.md
echo "== CODE- reply: -c / -ci"; grep -c -- "$T" vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md; grep -ci -- "$T" vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
echo "== DECISIONS.md D-2026-11-10-C lines 2076-2099: -c / -ci"; sed -n '2076,2099p' DECISIONS.md | grep -c -- "$T"; sed -n '2076,2099p' DECISIONS.md | grep -ci -- "$T"
echo "== vm handoff Amendment 3 line 23: -c / -ci"; sed -n '23p' vm/2026-11-06-vm-handoff.md | grep -c -- "$T"; sed -n '23p' vm/2026-11-06-vm-handoff.md | grep -ci -- "$T"
echo "== <rep> placeholder count in edited reports"; grep -c -- '2026-10-28-mffu-<rep>-reply\.png' $R/2026-11-10-vm-agent-hermes-ssh.md $R/2026-11-10-vm-agent-hermes-ssh-worker1.md $R/2026-11-10-vm-agent-hermes-ssh-worker3.md; } > $D/w1-4d.mine 2>&1
shasum -a 256 $R/2026-11-10-vm-agent-hermes-ssh*.md > $D/w1-4e.mine 2>&1
```
(The `tail -n +2` drops the leading blank line that the loop's first `echo` prints. In the pasted block that blank line falls outside the fence, so it is not part of :143–174.)

Worker2's commands were run in /bin/bash, as worker2 states (:12). The script is /tmp/hermes-corr1-w4/w2run.sh, verbatim:
```
D=/tmp/hermes-corr1-w4
cd /Volumes/Sensidine/Praxis.build
f=$(ls docs/reports/evidence/ | grep '^2026-10-28-mffu-.*-reply\.png$'); T=${f#2026-10-28-mffu-}; T=${T%-reply.png}
SP=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/af9aea76-b226-4610-b3fb-538269d1a642/scratchpad
S13="$(sed -n 136p specs/SPEC_RUBRIC.md | grep -o '"Fills [^"]*"' | head -1 | tr -d '"')"
IP='([0-9]{1,3}\.){3}[0-9]{1,3}'
H4='.ssh|praxis_vm|SHA256:|fingerprint|user amear|amear@|@praxis-vm|192.168'
H4e='\.ssh|praxis_vm|SHA256:|fingerprint|user amear|amear@|@praxis-vm|192\.168'
m(){ sed "s/$T/<the rep-name token>/g"; }
{ tail -1 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | grep -cxF '<the S13 sentence>'; echo "exit=$?"; } 2>&1 | m > $D/w2-A1.mine
{ grep -noE "$IP" <(sed -n '2075,$p' DECISIONS.md) vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | cat -n; echo '$ sed -n '"'"'56p'"'"' vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | grep -oE '"'"'.{0,12}127\.0\.0\.1.{0,6}'"'"''; sed -n '56p' vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | grep -oE '.{0,12}127\.0\.0\.1.{0,6}'; } 2>&1 | m > $D/w2-A3.mine
{ grep -c 20261110T211738Z </dev/null; echo "exit=$?"; } 2>&1 | m > $D/w2-A4a.mine
grep -c 20261110T211738Z vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md vm/2026-11-06-vm-handoff.md MANIFEST.md DECISIONS.md 2>&1 | m > $D/w2-A4b.mine
{ grep -no __TS__ vm/2026-11-06-vm-handoff.md MANIFEST.md DECISIONS.md; echo "exit=$?"; echo '$ grep -no 20261110T211738Z vm/2026-11-06-vm-handoff.md MANIFEST.md DECISIONS.md'; grep -no 20261110T211738Z vm/2026-11-06-vm-handoff.md MANIFEST.md DECISIONS.md; } 2>&1 | m > $D/w2-B9.mine
{ grep -cE "$H4" $SP/CODE-vm-agent-hermes.draft.md $SP/w4-entry.txt $SP/w4-am3.txt $SP/w4-man.txt | sed "s|$SP/||"; echo '$ grep -noE "$H4" $SP/CODE-vm-agent-hermes.draft.md $SP/w4-entry.txt $SP/w4-am3.txt $SP/w4-man.txt | sed "s|$SP/||"'; grep -noE "$H4" $SP/CODE-vm-agent-hermes.draft.md $SP/w4-entry.txt $SP/w4-am3.txt $SP/w4-man.txt | sed "s|$SP/||"; } 2>&1 | m > $D/w2-C1i.mine
grep -cE "$H4e" $SP/CODE-vm-agent-hermes.draft.md $SP/w4-entry.txt $SP/w4-am3.txt $SP/w4-man.txt 2>&1 | sed "s|$SP/||" | m > $D/w2-C1ie.mine
grep -noE "$IP" $SP/CODE-vm-agent-hermes.draft.md 2>&1 | m > $D/w2-C1a.mine
for i in w2-A1 w2-A3 w2-A4a w2-A4b w2-B9 w2-C1i w2-C1ie w2-C1a; do echo "== cmp $i"; cmp $D/$i.pasted $D/$i.mine; echo "cmp rc=$?"; diff $D/$i.pasted $D/$i.mine; done
echo "== extra: placement-only-__TS__ claim (w4 extracts, TS substituted, vs live)"
sed 's/__TS__/20261110T211738Z/g' $SP/w4-entry.txt | cmp - <(sed -n '2075,$p' DECISIONS.md); echo "w4-entry vs DECISIONS 2075-end rc=$?"; wc -l < $SP/w4-entry.txt; sed -n '2075,$p' DECISIONS.md | wc -l
sed 's/__TS__/20261110T211738Z/g' $SP/w4-am3.txt | cmp - <(sed -n '23p' vm/2026-11-06-vm-handoff.md); echo "w4-am3 vs handoff:23 rc=$?"
sed 's/__TS__/20261110T211738Z/g' $SP/w4-man.txt | cmp - <(sed -n '364,371p' MANIFEST.md); echo "w4-man vs MANIFEST 364-371 rc=$?"; wc -l < $SP/w4-man.txt
echo "== DECISIONS 2075/2076 first 40 chars"; sed -n '2075,2076p' DECISIONS.md | cut -c1-40 | cat -A 2>/dev/null || sed -n '2075,2076p' DECISIONS.md | cut -c1-40
echo "== DECISIONS lines 2086-2088 contain TS?"; grep -n 20261110T211738Z DECISIONS.md
```
`/bin/bash /tmp/hermes-corr1-w4/w2run.sh` printed (first part; the "extra" part belongs to C4/A5):
```
== cmp w2-A1
cmp rc=0
== cmp w2-A3
cmp rc=0
== cmp w2-A4a
cmp rc=0
== cmp w2-A4b
cmp rc=0
== cmp w2-B9
cmp rc=0
== cmp w2-C1i
cmp rc=0
== cmp w2-C1ie
cmp rc=0
== cmp w2-C1a
cmp rc=0
== extra: placement-only-__TS__ claim (w4 extracts, TS substituted, vs live)
w4-entry vs DECISIONS 2075-end rc=0
      25
      25
stdin /dev/fd/63 differ: char 1, line 1
w4-am3 vs handoff:23 rc=1
w4-man vs MANIFEST 364-371 rc=0
       8
== DECISIONS 2075/2076 first 40 chars

## 2026-11-10 — D-2026-11-10-C: VM agent
== DECISIONS lines 2086-2088 contain TS?
2087:**What it decides.** The VM agent for every step of `vm/2026-11-06-vm-handoff.md` is Hermes, driving the VM over SSH from the Mac (host alias `praxis-vm`) under its skill `praxis-vm-over-ssh`. The terms are in the CODE- reply `vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md`, made part of the handoff for Hermes by its Amendment 3 (handoff §0, :23). By pointer only: T1 who the VM agent is, every §1 limit unchanged; T2 screen reads are Amear's, and in step 1 items 0 and 6 are not on their own a STOP; T3 Z: reads and writes use the Mac folder, the swap stated in each reply; T4 a same-user check before step 1 item 1; T5 the one-session rule binds Hermes's four-hour Code timer (D4, DECISIONS.md:1919), and T5(a) no Code session Hermes started may still be running when it writes STARTED; T6 one read-only GET of n8n's `/healthz` from the VM, for OPEN-T1; T7 approvals stay manual. The reply's sub-points settle the clashes between the handoff and the skill (step 1 order, the skills-directory copies and their use only under the skill's gates, intended differences against the skill's stop-on-disagreement rule, reading Amendment 3 at the start of every run, the item 1 answer, item 8's overlap with T4, Z: paths inside the two VM skills, one fresh shell per command with folder and venv paths in full, which clock gives `<ts>`, who sets the step 4.3 tab, step 3.3 not being a screen read, a later go-2a reply's precedence on step 4.3, Code sessions still running before STARTED), each marked as the master's reading under D1, changeable by Amear.
```
The comparison commands for the worker1 blocks, re-run while assembling this report:
```
for i in w1-4b w1-4c w1-4d w1-4e; do echo "== cmp $i"; cmp $D/$i.pasted $D/$i.mine; echo "cmp rc=$?"; diff $D/$i.pasted $D/$i.mine; echo "sorted-equal:"; cmp <(sort $D/$i.pasted) <(sort $D/$i.mine) && echo yes; done
```
```
== cmp w1-4b
cmp rc=0
sorted-equal:
yes
== cmp w1-4c
cmp rc=0
sorted-equal:
yes
== cmp w1-4d
/tmp/hermes-corr1-w4/w1-4d.pasted /tmp/hermes-corr1-w4/w1-4d.mine differ: char 69, line 2
cmp rc=1
2d1
< docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md:0
5c4
< docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md:0
---
> docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md:0
6a6
> docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md:0
7a8
> docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md:0
9d9
< docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md:0
10a11
> docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md:0
12d12
< docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md:0
23d22
< docs/reports/2026-11-10-vm-agent-hermes-ssh.md:2
25a25
> docs/reports/2026-11-10-vm-agent-hermes-ssh.md:2
sorted-equal:
yes
== cmp w1-4e
cmp rc=0
sorted-equal:
yes
```
Why the w1-4d order differs: `type grep` in this zsh tool shell prints
```
grep is a shell function from /Users/admin/.claude/shell-snapshots/snapshot-zsh-1794408303558-icmlpi.sh
grep
/usr/bin/grep
```
So the `grep` that worker1 ran in zsh is not /usr/bin/grep. Its multi-file output order is not the argument order and is not stable between runs. My own C1 output shows the same scrambling: the snapshot counts came out in the order worker3, worker2, worker1, worker4, ssh.

Verdict:
- **worker2: all 8 blocks byte-identical (cmp rc=0).** That includes the two NOT REPRODUCED verdicts (A1, A4a), C1i, and the DIFFERENT A3, B9 and C1a.
- **worker1: 3 of 4 byte-identical.** w1-4d differs in line ORDER only; the sorted contents are equal. This is not a time-dependent difference. It is the tool's nondeterministic file ordering, which worker1 did not disclose (A2). The diff headers in w1-4b carry the live mtime 2026-11-11 09:53:19. They match because the files have not been written since.

### C3 — S1 scan
- worker1 :236–242, :270. The "count proof" commands are pasted as six `$ echo ...` lines, with all their output batched below them, so no output is tied to its own command. One of the six (:238) is not the command as run (`<same five files>`); the report admits this at :270. The output itself reproduces (C2 w1-4d, as a multiset). → A1.
- worker1 :15 ("The git index and /tmp/idx-hermes were not edited by this worker") and :291 ("No other file was edited"). No command is pasted for either claim. → A3.
- worker1 :19, :54. "The three hashes the manager recorded matched" compares against values that are not pasted from any command in that report. The values do equal the brief's hashes (my C1). NOTE only.
- worker2 :248 (B3) "placement ... changed only `__TS__` on handoff :23 (see B9)". The cited B9 (:298–305) shows only grep match positions. It does not show line equality. No comparison of the pre-placement extract against handoff:23 was run; one was run only for MANIFEST:364 (:320). → A5.
- worker2 :367 (B15) "differs from worker 3's pre-placement state only in `__TS__` vs `20261110T211738Z`" for the entry, Amendment 3 and the MANIFEST rows. This is also unevidenced in the report for the entry and Amendment 3. → A5.
- worker2's other blocks are all `$ `-prefixed commands with raw output, and 8 of 8 re-ran byte-identical. I found no labels standing in for commands except the quoted originals, which worker2 marks as quotes (:16).

### C4 — S2 scan
- worker2 :58: "its checks ran on the same file state as today". worker2 :179: "The files are unchanged since placement (setup `stat`)". Both are inferred from mtimes alone. An mtime is the time of the last write. It proves neither the content, nor when the manager's checks ran. This contradicts worker2's own caveat at :21. → A6.
- worker1 :101: "the PNG ... was not modified" is based on mtime and size only. Today's sha256 equals the pre-dispatch value (C6), so the claim holds; the evidence offered for it was weaker than the claim. → A4.
- worker2 B9–B11, B15, C1b and C4c carry explicit today-vs-yesterday qualifiers. I found no re-run presented as proof of the 2026-11-10 state.
- My test of the A5 claims. Same /bin/bash script, "extra" section above, plus a second check of handoff:23 after I found that w4-am3.txt holds the diff `+` line:
```
w4-am3 bytes 887 lines 1 ends-with-newline True
TS-subst len 904 | handoff:23 len 902
TS-subst (newline-stripped) == handoff:23: False
first diff index 0
w4: '+- **Amendment 3 (2026-11-10):** the VM '
hf: '- **Amendment 3 (2026-11-10):** the VM a'
```
```
$ sed -e s/^+// -e s/__TS__/20261110T211738Z/g w4-am3.txt | cmp - <(sed -n 23p handoff)
rc=0
```
Result: the claims in A5 are TRUE (the entry is cmp rc=0 over 25 lines; MANIFEST 364–371 is rc=0; handoff:23 is rc=0 once the diff `+` is stripped). They are true but were not evidenced in worker2's report.

### C5 — S13 in worker1 and worker2 reports
Command as run. In the python below, the S13 assignment held the sentence literally (`S13='...'`). Here it is replaced by `<the S13 sentence>`, so that this report carries the sentence only once. The value used is proved by hash:
```
$ printf '%s' '<the S13 sentence>' | shasum -a 256; sed -n 136p specs/SPEC_RUBRIC.md | grep -o '"Fills [^"]*"' | head -1 | tr -d '"' | tr -d '\n' | shasum -a 256
816836b085174d186c602ff95da9035d47853b4ca4e4447c6c4d4b711afcce30  -
816836b085174d186c602ff95da9035d47853b4ca4e4447c6c4d4b711afcce30  -
```
```
python3 -I - docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md <<'EOF'
import sys,re
S13='<the S13 sentence>'
for p in sys.argv[1:]:
    L=open(p,encoding="utf-8").read().split("\n")
    fence=None; inside=[]; outside_exact=[]; anyhit=[]
    for i,l in enumerate(L,1):
        m=re.match(r"^(`{3,})",l)
        if m:
            if fence is None: fence=m.group(1); continue
            elif l.strip()==fence: fence=None; continue
        if S13 in l: anyhit.append(i); (inside if fence else outside_exact).append(i) if True else None
    ne=[i for i,l in enumerate(L,1) if l.strip()]
    last=ne[-1]
    print(p.split("/")[-1],"| substring hits:",anyhit,"| in-code:",inside,"| last non-empty line:",last,"== S13 exactly:",L[last-1]==S13,"| trailing newline:",L[-1]=="", "| fence open at EOF:",fence is not None)
EOF
```
```
2026-11-11-vm-agent-hermes-correction-1-worker1.md | substring hits: [293] | in-code: [] | last non-empty line: 293 == S13 exactly: True | trailing newline: True | fence open at EOF: False
2026-11-11-vm-agent-hermes-correction-1-worker2.md | substring hits: [794] | in-code: [] | last non-empty line: 794 == S13 exactly: True | trailing newline: True | fence open at EOF: False
```
Verdict: **HOLDS** for both reports. Each has exactly one occurrence. It is the last non-empty line, it is an exact whole-line match, and it is outside any code fence.

### C6 — protected files and the index
Command as run (part of the same batch as C5; output masked):
```
shasum -a 256 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md DECISIONS.md vm/2026-11-06-vm-handoff.md HANDOFF.md STATUS.md "docs/reports/evidence/$f"
git ls-files -s | shasum -a 256
git diff --cached --name-only
find . -path ./.git -prune -o -type f -newermt '2026-11-11 09:00' -print | sort
```
```
$ C6 shasum protected
2b729b8e4469a1c3454dadba08ddcd9e48a387f201e583c5e326f66569ce2ed0  vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
39e5ba0c27a1aab9736d6f23ce28efbb663bfcd1bcab5b5f305b2911669bc637  DECISIONS.md
ff4ba4ac512d9f59ed363563e49c88129a3da0864310f8bf6de2f714199c8c42  vm/2026-11-06-vm-handoff.md
71cf456c349ba85b039818b33dc1135218b77ccd78ce37352b5b246ae1cb02a4  HANDOFF.md
c06e4b26120ac3c37607d06d6424b9628aa8bcbf6c67adc62a91cdc74bd92564  STATUS.md
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
$ git ls-files -s | shasum -a 256
5ac1ef7d17ce98a5e256863a10288b12541a502959ffffe3ba79eb282e638ac6  -
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-<the rep-name token>-reply.png
$ files modified since 2026-11-11 09:00 (outside .git)
./.beads/backup/backup_state.json
./.beads/backup/kt9ibikl006ji4cdoep7ssam4s0v7o93.darc
./.beads/backup/manifest
./.beads/embeddeddolt/Praxis_build/.dolt/noms/journal.idx
./.beads/embeddeddolt/Praxis_build/.dolt/noms/manifest
./.beads/embeddeddolt/Praxis_build/.dolt/noms/vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
./.beads/embeddeddolt/Praxis_build/.dolt/repo_state.json
./.claude/state/mint-log
./DECISION_LOG.md
./DISPATCH_LOG.md
./docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md
./docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md
./docs/reports/2026-11-10-vm-agent-hermes-ssh.md
./docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md
./docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md
./docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md
./docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker4.md
```
Verdict: **HOLDS.**
- All six sha256 values equal the pre-dispatch values in the brief.
- The index digest is 5ac1ef7d…8ac6, unchanged.
- The cached list is only the PNG.
- The files written since 09:00 are the three edited reports, the correction-1 reports, DECISION_LOG.md, DISPATCH_LOG.md, .beads state and .claude/state/mint-log. None of them is a protected file. These mtimes cannot show which agent wrote what.

## Findings
- **A1 MINOR (S1)**, correction-1-worker1.md :236–242 and :270. In the count proof, the commands are shown as `$ echo` labels with their output batched together, and :238 is shorthand, not the command as run. It is disclosed, and the output reproduces as a multiset (C2 w1-4d).
- **A2 NOTE (S1 reproducibility)**, worker1 :66–76 and :244–254. In worker1's zsh, `grep` is a shell function wrapping the Claude Code binary, not /usr/bin/grep. Multi-file output order is not the argument order and does not reproduce byte for byte (cmp rc=1; the sorted contents are equal). It is undisclosed. The cause is tool nondeterminism, not time dependence.
- **A3 MINOR (S1)**, worker1 :15 and :291. "Index and /tmp/idx-hermes not edited" and "No other file was edited" are stated without a command. My C6 confirms that the index digest and the cached list are unchanged. I did not check /tmp/idx-hermes (I was told not to touch it). Who edited which files cannot be shown from mtimes.
- **A4 NOTE (S2)**, worker1 :101. "PNG not modified" rests on mtime and size only. It is confirmed today by sha256 (C6).
- **A5 MINOR (S1)**, correction-1-worker2.md :248 and :367. The claim that placement changed only `__TS__` (handoff :23, the entry, MANIFEST) rests on nothing in that report for handoff :23 and the entry. The cited B9 shows match positions, not line equality. I tested it: the claim is TRUE (cmp rc=0 for all three, once the diff `+` prefix in w4-am3.txt is stripped).
- **A6 MINOR (S2)**, worker2 :58 and :179. The claims that the checks ran on the same file state and that the files are unchanged since placement are presented as fact, but are inferred from mtimes. This contradicts the report's own :21 caveat.
- **A7 NOTE**, worker2 :106, :221 and :277 ("entry :2075–2099"). DECISIONS.md :2075 is blank; the D-2026-11-10-C heading is :2076 (the "extra" output above shows the blank line, then the heading). This is cosmetic. Every count and offset (entry line 8 = :2082, line 13 = :2087) is consistent with a 2075 start.
- **A8 NOTE (scope)**. The rep-name token is still present in 36 other files under docs/reports, in names and in text (C1). The `<rep>` path in the four lines no longer names a file that exists on disk. Neither breaks the four-line mandate, which was the scope.

## Result
**FAIL at MINOR severity only. No BLOCKER.**
- C1 (exactly four lines de-identified, nothing else changed), C5 and C6 HOLD.
- C2: 11 of 12 re-run blocks are byte-identical; the 12th differs in line order only (A2).
- S1 is broken at MINOR in A1, A3 and A5 (A5's claim is true but unevidenced). S2 is broken at MINOR in A6.
- Nothing found contradicts a verdict that either worker report gives.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
