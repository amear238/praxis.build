# Unit 2026-11-13-research-filing-resume: manager report (stands as the manager report of unit 2026-11-13-research-filing)

## Task

Resume and close unit 2026-11-13-research-filing after a power outage killed its manager mid-unit. Authority: DECISION_LOG.md row 2026-11-13T19:58:43Z (praxis-master under D-2026-11-08-D D1), which resumes the work ruled in row 2026-11-13T19:40:54Z: file four untracked return-handoff reports written by the Claude.ai Praxis channel (docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md, -kimi-research.md, -session-close.md, -vm-queue-results.md), with only these edits allowed: keep the first standalone copy of the S13 sentence, delete later standalone copies outside quoted or pasted material, and replace private-person names, emails, network identifiers and key paths with bracketed placeholders.

Work given to this manager: (1) re-prove the edits without the lost /tmp pre-copies (rebuild the strategy and kimi received files from worker 1's pasted diffs and match worker 1's pre-copy hashes; diff session-close and vm-queue against their Downloads originals); (2) re-run the S13 line counts and the PII scan; (3) in MANIFEST.md, replace the uncommitted stub-report row with rows for this report, worker 1 and worker 2, check rows 1-4, and rebuild /tmp/rf-manifest-blob.md; (4) show that no tracked file other than MANIFEST.md changed; then a cold adversary.

## Rubric criteria addressed

specs/SPEC_RUBRIC.md S1 (:133), S2 (:134), S8 (:140), S13 (:145). House reading of S13 "once": standalone lines outside quoted commands, code blocks and pasted drafts.

## What the dead manager left

- docs/reports/2026-11-13-research-filing-manager.md: a 29-line stub, every evidence section "(in progress)", Result: BLOCKED. Left on disk unchanged and uncommitted, as the 19:58:43Z row rules (sha256 below, at the start and the end of this unit).
- docs/reports/2026-11-13-research-filing-worker1.md: BUILD worker 1 (original unit). Made the S13 deletions, the PII scan of the received files, five MANIFEST rows and the blob; its own Result: PASS.
- docs/reports/2026-11-13-research-filing-worker2.md: ADVERSARIAL worker 2 (original unit). Graded checks (a)-(f) on worker 1's output; its own Result: PASS, no defects.
- MANIFEST.md with worker 1's five rows appended (481 lines); the fifth row named the stub report.
- Lost in the reboot: /tmp/rf-pre/ (worker 1's pre-edit copies), /tmp/rf-manifest-blob.md and /tmp/rf-diffstat-before.txt.

## Workers dispatched

| id | mode | unit | outcome |
|---|---|---|---|
| worker 1 (original unit) | BUILD | 2026-11-13-research-filing | its report says Result: PASS (report :310); its edits re-proved below by this manager |
| worker 2 (original unit) | ADVERSARIAL | 2026-11-13-research-filing | its report says Result: PASS on (a)-(f) (report :611) |
| resume worker 1 | ADVERSARIAL (cold) | 2026-11-13-research-filing-resume | see Adversarial findings |

This manager did the re-proof, the MANIFEST edit and the blob itself (short scripts, no editor); no builder worker was used, so the cold adversary is resume worker 1.

## Process log

1. 19:59:28Z: captured the stub report sha256, git diff --stat, sha256 of every tracked modified file, byte copies of MANIFEST.md and DISPATCH_LOG.md, and the full git diff, into /tmp/rfr/ (block E0).
2. Read the two DECISION_LOG rows, rubric S1/S2/S8/S13, worker 1's report in full, worker 2's checks and the stub.
3. Step 1(b): rebuilt the received strategy and kimi files in /tmp/rfr/rebuilt2/ by inserting, after the filed line numbers worker 1's diffs name, the deleted line text taken from worker 1's own diff lines (report :143, :147, :149, with the leading "< " stripped). Both hashes match worker 1's pre-copy hashes. A first run with the sentence typed into the script (/tmp/rfr/rebuilt/) gave the same two hashes; the second run is the one pasted, because it takes the text from worker 1's diffs as the brief asks. Negative control: inserting at the wrong line gives a different hash (block E1).
4. Step 1(a): diffs of the two Downloads originals against their filed twins: one deleted line each, the S13 sentence, nothing else (block E2).
5. Step 2: S13 standalone counts (one per file, the first copy, at :5, :5, :5, :7; no copy inside the strategy file's only code fence :34-:94; no block quotes) and PII scan (zero unreplaced hits; false positives listed) (blocks E3, E4).
6. Step 3: checked MANIFEST rows 1-4 (:477-:480) against the diffs and file headings: all four still match; no change made to them (block E5). Replaced row 5 (stub) with three rows; made the blob; cmp proofs (blocks E6, E7).
7. Dispatched the cold adversary (ADVERSARIAL) with the authority rows, the allowed-edits rule, the artifacts and the baselines, not this manager's reasoning.
8. Step 4: tracked-file comparison after the work (block E8).

Observations, not acted on (narrower option):
- The cold adversary's report (docs/reports/2026-11-13-research-filing-resume-worker1.md) has no MANIFEST row; the brief asked for exactly three new rows. The master decides whether it needs one.
- The four filed files each end with one trailing blank line (the blank that preceded the deleted footer). Allowed by the rule; noted by worker 2 too.
- Two ambiguous cited author names (one two-surname pair dated 2026, one single-surname practitioner source dated 2026) stay in the files as cited authors of sources, not private persons in PRAXIS's dealings, per worker 1 and worker 2's reading. Not renamed here.

## Verification evidence (command output)

All scripts ran under bash with `set -v`, so each command line is printed before its output. Where a command reads the S13 sentence it reads it from /tmp/rfr/s13.txt (made from worker 1's diff line, see E1), so the sentence is not printed in the command lines.

### E0. Baselines at start (19:59:28Z)

```
date -u +%Y-%m-%dT%H:%M:%SZ && openssl dgst -sha256 docs/reports/2026-11-13-research-filing-manager.md
2026-11-13T19:59:28Z
SHA2-256(docs/reports/2026-11-13-research-filing-manager.md)= eeef330ab3c52b323f3e214544f2292c657eb1424dd667c27e5f851079f54c5f
git diff --stat > /tmp/rfr/diffstat-before.txt && cat /tmp/rfr/diffstat-before.txt
 .claude/settings.json                              |  10 ++
 AUDIT_LOG.md                                       |  53 +++++++++++
 DECISIONS.md                                       |  92 ++++++++++++++++++
 DECISION_LOG.md                                    |  14 +++
 DISPATCH_LOG.md                                    |  30 ++++++
 HANDOFF.md                                         |  27 ++++++
 ISSUE_REGISTER.md                                  |   8 +-
 MANIFEST.md                                        |  28 ++++++
 STATUS.md                                          |   8 ++
 docs/reports/2026-10-28-f4-[rep]-reply-filing.md    |  75 ++++++++++++++-
 ...026-10-28-nightly-checks-plan-review-rebuild.md |  67 ++++++++++++-
 docs/specs/2026-11-05-walk-forward-spec.md         |  10 +-
 docs/specs/2026-11-06-walk-forward-values.md       |  42 ++++-----
 scripts/dispatch-log-writeahead.sh                 | 104 ++++++++++++++++++++-
 14 files changed, 536 insertions(+), 32 deletions(-)
git diff --name-only | while read f; do openssl dgst -sha256 "$f"; done > /tmp/rfr/tracked-sha-before.txt; cat /tmp/rfr/tracked-sha-before.txt
SHA2-256(.claude/settings.json)= 98ac1ec8802cd6c02a04d8f24382c72a53162bfac41ca41ccff13bf199d92115
SHA2-256(AUDIT_LOG.md)= 2baacc148653e69b0d40d696d85d351be72f902bf75d562b8f50eebf3efaadf0
SHA2-256(DECISIONS.md)= afd191a683331fbec91f9d9884d44b9db888a52029cad5eb7d2b100478c24353
SHA2-256(DECISION_LOG.md)= aecb67dbcdba94da661430a45f89799dc7847d9e4c4360426e9e08aca96a1c74
SHA2-256(DISPATCH_LOG.md)= dd16a2d8a079d2434236e435379f14d222d6b3cd0014aa653be6eba387cc8970
SHA2-256(HANDOFF.md)= 58c17c08e4f0ae0356833b5c6dea52645a0214681c9673440ead3eec78351f7e
SHA2-256(ISSUE_REGISTER.md)= cbad356371f25683cbcf53cdf8f6b2a0482c826a7d7b9eea983fcdd64b477827
SHA2-256(MANIFEST.md)= 4140b0e9dded4887c09c34b55497101a2d2d54d484baa3e502401e96743e9656
SHA2-256(STATUS.md)= de61905da79dec9271ec38dadc2eabe5b63aa784d27c1b36dc0dd7b3a47a172c
SHA2-256(docs/reports/2026-10-28-f4-[rep]-reply-filing.md)= 222b33c2ee2bfc85a367a0691fb5872a08e02db9cf7d62394aaa14d1f13cbc69
SHA2-256(docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md)= 9857ce4019c2094d41b15c84df65238449f51e416e24a13428a3485cf4ec04bf
SHA2-256(docs/specs/2026-11-05-walk-forward-spec.md)= a80074ecc3cdb39c8bed9634d5f8a9a8c8def135849cc2af6fce785d9303cc04
SHA2-256(docs/specs/2026-11-06-walk-forward-values.md)= 6d7ed4df9328ad2d2ac489834fdb3ec82fd296e5cd642d651747ffa3217ceb7e
SHA2-256(scripts/dispatch-log-writeahead.sh)= d7e0fd4112019183d72b6b5e5b0f94b8661fc69a7253a82bfabec995004d6703
```

### E1. Step 1(b): rebuild of the received strategy and kimi files

cat /tmp/rfr/rebuild2.sh

```
#!/bin/bash
# Rebuild the two received files whose pre-copies were lost, by re-inserting the
# lines worker1's pasted diffs show as deleted (worker1 report :142-:149):
#   strategy-research "108d107"           -> insert after filed line 107
#   kimi-research     "42d41", "330d328"  -> insert after filed lines 41 and 328
# The inserted text is taken from worker1's diff lines themselves (leading "< " stripped).
set -v
W=/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-research-filing-worker1.md
R=/Volumes/Sensidine/Praxis.build/docs/reports
OUT=/tmp/rfr/rebuilt2
mkdir -p "$OUT"
sed -n '142p;146p;148p;152p;156p' "$W"
sed -n '143p;147p;149p;153p;157p' "$W" | cut -c1-2 | od -An -c
sed -n '143p;147p;149p;153p;157p' "$W" | sort -u | wc -l
sed -n '143p' "$W" | sed 's/^< //' > /tmp/rfr/s13.txt
wc -c /tmp/rfr/s13.txt
L=$(cat /tmp/rfr/s13.txt)
awk -v L="$L" '{print} NR==107{print L}' "$R/2026-11-13-return-handoff-claude-ai-strategy-research.md" > "$OUT/2026-11-13-return-handoff-claude-ai-strategy-research.md"
awk -v L="$L" '{print} NR==41{print L} NR==328{print L}' "$R/2026-11-13-return-handoff-claude-ai-kimi-research.md" > "$OUT/2026-11-13-return-handoff-claude-ai-kimi-research.md"
wc -l "$R/2026-11-13-return-handoff-claude-ai-strategy-research.md" "$R/2026-11-13-return-handoff-claude-ai-kimi-research.md" "$OUT/2026-11-13-return-handoff-claude-ai-strategy-research.md" "$OUT/2026-11-13-return-handoff-claude-ai-kimi-research.md"
openssl dgst -sha256 "$OUT/2026-11-13-return-handoff-claude-ai-strategy-research.md" "$OUT/2026-11-13-return-handoff-claude-ai-kimi-research.md"
diff "$OUT/2026-11-13-return-handoff-claude-ai-strategy-research.md" "$R/2026-11-13-return-handoff-claude-ai-strategy-research.md" | cut -c1-30; echo "diff exit=${PIPESTATUS[0]}"
diff "$OUT/2026-11-13-return-handoff-claude-ai-kimi-research.md" "$R/2026-11-13-return-handoff-claude-ai-kimi-research.md" | cut -c1-30; echo "diff exit=${PIPESTATUS[0]}"
test "$(openssl dgst -sha256 -r "$OUT/2026-11-13-return-handoff-claude-ai-strategy-research.md" | cut -d' ' -f1)" = 8e8621e02fb70760cc2f3e6544b604ba89b1188a9ad55e2e222a23b2a045de14; echo "strategy hash match exit=$?"
test "$(openssl dgst -sha256 -r "$OUT/2026-11-13-return-handoff-claude-ai-kimi-research.md" | cut -d' ' -f1)" = 97d08993f78500e6a0b9c5e61382c202d296e6d5731f76ba6589afc58e2e4f54; echo "kimi hash match exit=$?"
```

/tmp/rfr/rebuild2.sh 2>&1 | tee /tmp/rfr/rebuild2.out (diff output cut to 30 columns so the deleted text is not repeated in full; the full deleted lines are in E2 for the other two files and in worker 1 report :143-:157)

```
W=/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-research-filing-worker1.md
R=/Volumes/Sensidine/Praxis.build/docs/reports
OUT=/tmp/rfr/rebuilt2
mkdir -p "$OUT"
sed -n '142p;146p;148p;152p;156p' "$W"
108d107
42d41
330d328
55d54
45d44
sed -n '143p;147p;149p;153p;157p' "$W" | cut -c1-2 | od -An -c
           <      \n   <      \n   <      \n   <      \n   <      \n    

sed -n '143p;147p;149p;153p;157p' "$W" | sort -u | wc -l
       1
sed -n '143p' "$W" | sed 's/^< //' > /tmp/rfr/s13.txt
wc -c /tmp/rfr/s13.txt
      91 /tmp/rfr/s13.txt
L=$(cat /tmp/rfr/s13.txt)
cat /tmp/rfr/s13.txt
awk -v L="$L" '{print} NR==107{print L}' "$R/2026-11-13-return-handoff-claude-ai-strategy-research.md" > "$OUT/2026-11-13-return-handoff-claude-ai-strategy-research.md"
awk -v L="$L" '{print} NR==41{print L} NR==328{print L}' "$R/2026-11-13-return-handoff-claude-ai-kimi-research.md" > "$OUT/2026-11-13-return-handoff-claude-ai-kimi-research.md"
wc -l "$R/2026-11-13-return-handoff-claude-ai-strategy-research.md" "$R/2026-11-13-return-handoff-claude-ai-kimi-research.md" "$OUT/2026-11-13-return-handoff-claude-ai-strategy-research.md" "$OUT/2026-11-13-return-handoff-claude-ai-kimi-research.md"
     107 /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md
     328 /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md
     108 /tmp/rfr/rebuilt2/2026-11-13-return-handoff-claude-ai-strategy-research.md
     330 /tmp/rfr/rebuilt2/2026-11-13-return-handoff-claude-ai-kimi-research.md
     873 total
openssl dgst -sha256 "$OUT/2026-11-13-return-handoff-claude-ai-strategy-research.md" "$OUT/2026-11-13-return-handoff-claude-ai-kimi-research.md"
SHA2-256(/tmp/rfr/rebuilt2/2026-11-13-return-handoff-claude-ai-strategy-research.md)= 8e8621e02fb70760cc2f3e6544b604ba89b1188a9ad55e2e222a23b2a045de14
SHA2-256(/tmp/rfr/rebuilt2/2026-11-13-return-handoff-claude-ai-kimi-research.md)= 97d08993f78500e6a0b9c5e61382c202d296e6d5731f76ba6589afc58e2e4f54
diff "$OUT/2026-11-13-return-handoff-claude-ai-strategy-research.md" "$R/2026-11-13-return-handoff-claude-ai-strategy-research.md" | cut -c1-30; echo "diff exit=${PIPESTATUS[0]}"
108d107
< Fills are optimistic; Standa
diff exit=1
diff "$OUT/2026-11-13-return-handoff-claude-ai-kimi-research.md" "$R/2026-11-13-return-handoff-claude-ai-kimi-research.md" | cut -c1-30; echo "diff exit=${PIPESTATUS[0]}"
42d41
< Fills are optimistic; Standa
330d328
< Fills are optimistic; Standa
diff exit=1
test "$(openssl dgst -sha256 -r "$OUT/2026-11-13-return-handoff-claude-ai-strategy-research.md" | cut -d' ' -f1)" = 8e8621e02fb70760cc2f3e6544b604ba89b1188a9ad55e2e222a23b2a045de14; echo "strategy hash match exit=$?"
openssl dgst -sha256 -r "$OUT/2026-11-13-return-handoff-claude-ai-strategy-research.md" | cut -d' ' -f1
strategy hash match exit=0
test "$(openssl dgst -sha256 -r "$OUT/2026-11-13-return-handoff-claude-ai-kimi-research.md" | cut -d' ' -f1)" = 97d08993f78500e6a0b9c5e61382c202d296e6d5731f76ba6589afc58e2e4f54; echo "kimi hash match exit=$?"
openssl dgst -sha256 -r "$OUT/2026-11-13-return-handoff-claude-ai-kimi-research.md" | cut -d' ' -f1
kimi hash match exit=0
```

First run (sentence typed into the script, output in /tmp/rfr/rebuilt/), hashed again:

```
openssl dgst -sha256 /tmp/rfr/rebuilt/2026-11-13-return-handoff-claude-ai-strategy-research.md /tmp/rfr/rebuilt/2026-11-13-return-handoff-claude-ai-kimi-research.md
SHA2-256(/tmp/rfr/rebuilt/2026-11-13-return-handoff-claude-ai-strategy-research.md)= 8e8621e02fb70760cc2f3e6544b604ba89b1188a9ad55e2e222a23b2a045de14
SHA2-256(/tmp/rfr/rebuilt/2026-11-13-return-handoff-claude-ai-kimi-research.md)= 97d08993f78500e6a0b9c5e61382c202d296e6d5731f76ba6589afc58e2e4f54
```

Negative control and S13 counts are in E3.

### E2. Step 1(a): Downloads originals against filed twins; sha256 of the four filed files

```
/tmp/rfr/step1a.sh 2>&1 | tee /tmp/rfr/step1a.out
cd /Volumes/Sensidine/Praxis.build
diff /Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-session-close.md docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md; echo "diff exit=$?"
55d54
< Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
diff exit=1
diff /Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-vm-queue-results.md docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md; echo "diff exit=$?"
45d44
< Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
diff exit=1
openssl dgst -sha256 /Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-session-close.md /Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
SHA2-256(/Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-session-close.md)= e9e9674f37d4e41072581a3099efc074d9f140c8c2a507c63557c4d8ac52cf1d
SHA2-256(/Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-vm-queue-results.md)= 535743ca6ad5a154c8926b6dc9efc7b62f59de862fe31106ced444bfe90f09ca
openssl dgst -sha256 docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
SHA2-256(docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md)= 6b283621f61f8db60052bbf379bb83336de802f199c130321cc0e6931df3b306
SHA2-256(docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md)= 1efd9485762cc2944e47d3be6a5249161a4d3c301ea1caf439561a40b002bde3
SHA2-256(docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md)= 4ac03c59ad9197b0f2a8449983f858be4939b343e46706453e7b505d9cba43c2
SHA2-256(docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md)= ba2d8613698bfd555b8d274e9f3c9f76c753bf8ba075d86b8fdb87d47c18345a
wc -l /Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-session-close.md /Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-vm-queue-results.md docs/reports/2026-11-13-return-handoff-claude-ai-*.md
      55 /Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-session-close.md
      45 /Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
     328 docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md
      54 docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
     107 docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md
      44 docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
     633 total
for f in docs/reports/2026-11-13-return-handoff-claude-ai-*.md; do printf '%s last 2 bytes:' "$f"; tail -c 2 "$f" | od -An -c; done
docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md last 2 bytes:          \n  \n                                                        

docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md last 2 bytes:          \n  \n                                                        

docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md last 2 bytes:          \n  \n                                                        

docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md last 2 bytes:          \n  \n                                                        

```

### E3. Step 2: S13 standalone counts, code fences, block quotes; negative control for E1

```
/tmp/rfr/step2b.sh 2>&1 | tee /tmp/rfr/step2b.out
cd /Volumes/Sensidine/Praxis.build/docs/reports
wc -c /tmp/rfr/s13.txt
      91 /tmp/rfr/s13.txt
for f in 2026-11-13-return-handoff-claude-ai-strategy-research.md 2026-11-13-return-handoff-claude-ai-kimi-research.md 2026-11-13-return-handoff-claude-ai-session-close.md 2026-11-13-return-handoff-claude-ai-vm-queue-results.md; do echo "== $f"; printf 'standalone lines: '; grep -n -x -F -f /tmp/rfr/s13.txt "$f" | cut -d: -f1 | tr '\n' ' '; echo; printf 'substring count: '; grep -c -F -f /tmp/rfr/s13.txt "$f"; printf 'ticks/side lines: '; grep -n -i 'ticks/side' "$f" | cut -d: -f1 | tr '\n' ' '; echo; printf 'fence lines: '; grep -n '^ *```' "$f" | cut -d: -f1 | tr '\n' ' '; echo; printf 'blockquote count: '; grep -c '^ *>' "$f"; done
== 2026-11-13-return-handoff-claude-ai-strategy-research.md
standalone lines: 5 
substring count: 1
ticks/side lines: 5 
fence lines: 34 94 
blockquote count: 0
== 2026-11-13-return-handoff-claude-ai-kimi-research.md
standalone lines: 5 
substring count: 1
ticks/side lines: 5 
fence lines: 
blockquote count: 0
== 2026-11-13-return-handoff-claude-ai-session-close.md
standalone lines: 5 
substring count: 1
ticks/side lines: 5 19 
fence lines: 
blockquote count: 0
== 2026-11-13-return-handoff-claude-ai-vm-queue-results.md
standalone lines: 7 
substring count: 1
ticks/side lines: 7 
fence lines: 
blockquote count: 0
# negative control: wrong insert position gives a different hash
awk -v L="$(cat /tmp/rfr/s13.txt)" '{print} NR==106{print L}' 2026-11-13-return-handoff-claude-ai-strategy-research.md | openssl dgst -sha256
cat /tmp/rfr/s13.txt
SHA2-256(stdin)= 785e9d5eb822055d461a326518ccf5431ab14e05e6911839dfd1a99ac419b995
```

session-close :19 contains "2 ticks/side slippage" inside a run description; it is not the S13 sentence (substring count 1, at :5). In the strategy file the kept copy :5 sits before the only code fence (:34-:94).

### E4. Step 2: PII scan of the four filed files

```
/tmp/rfr/pii.sh 2>&1 | tee /tmp/rfr/pii.out
cd /Volumes/Sensidine/Praxis.build/docs/reports
F="2026-11-13-return-handoff-claude-ai-strategy-research.md 2026-11-13-return-handoff-claude-ai-kimi-research.md 2026-11-13-return-handoff-claude-ai-session-close.md 2026-11-13-return-handoff-claude-ai-vm-queue-results.md"
grep -n -o -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $F; echo "email exit=$?"
email exit=1
grep -n -o -E '(^|[^0-9.])([0-9]{1,3}\.){3}[0-9]{1,3}([^0-9.]|$)' $F; echo "ipv4 exit=$?"
ipv4 exit=1
grep -n -o -i -E '([0-9a-f]{1,4}:){2,7}[0-9a-f]{0,4}|::[0-9a-f]{1,4}' $F; echo "ipv6 exit=$?"
2026-11-13-return-handoff-claude-ai-kimi-research.md:69:15:30:
2026-11-13-return-handoff-claude-ai-vm-queue-results.md:28:12:32:48
2026-11-13-return-handoff-claude-ai-vm-queue-results.md:31:17:36:47
ipv6 exit=0
grep -n -o -i -E '([0-9a-f]{2}[:-]){5}[0-9a-f]{2}' $F; echo "mac exit=$?"
mac exit=1
grep -n -o -i -E 'id_rsa|id_ed25519|id_ecdsa|id_dsa|\.pem([^a-z]|$)|\.ppk|\.pub([^a-z]|$)|\.ssh|authorized_keys|known_hosts|PRIVATE KEY|ssh-(rsa|ed25519|dss)|ecdsa-sha2' $F; echo "ssh exit=$?"
ssh exit=1
grep -n -o -i -E '/Users/[^ `)]*|/home/[^ `)]*|[A-Z]:\\[^ `)]*|~/[^ `)]*|\\\\[A-Za-z0-9_-]+\\' $F; echo "userpath exit=$?"
2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:C:\praxis\vm-bridge
userpath exit=0
grep -n -o -i -E '@[A-Za-z0-9_]{2,}' $F; echo "at exit=$?"
2026-11-13-return-handoff-claude-ai-kimi-research.md:217:@15
2026-11-13-return-handoff-claude-ai-kimi-research.md:230:@25k
2026-11-13-return-handoff-claude-ai-kimi-research.md:230:@50k
2026-11-13-return-handoff-claude-ai-kimi-research.md:230:@100k
2026-11-13-return-handoff-claude-ai-kimi-research.md:230:@150k
at exit=0
grep -n -o -E '\[[A-Z][A-Z -]*(REDACTED|NAME|EMAIL|HOST|IP|KEY|PERSON|PATH)[A-Z -]*\]' $F; echo "placeholder exit=$?"
placeholder exit=1
/tmp/rfr/names.sh 2>&1 | tee /tmp/rfr/names.out
cd /Volumes/Sensidine/Praxis.build/docs/reports
F="2026-11-13-return-handoff-claude-ai-strategy-research.md 2026-11-13-return-handoff-claude-ai-kimi-research.md 2026-11-13-return-handoff-claude-ai-session-close.md 2026-11-13-return-handoff-claude-ai-vm-queue-results.md"
grep -n -o -E '\b(Mr|Mrs|Ms|Dr|Prof)\.? [A-Z][a-z]+' $F; echo "honorific exit=$?"
honorific exit=1
grep -n -o -i -E '\b(rep|representative|support agent|named|called|contact|spoke (to|with)|emailed|from [A-Z][a-z]+ at)\b[^.]{0,30}' 2026-11-13-return-handoff-claude-ai-session-close.md 2026-11-13-return-handoff-claude-ai-vm-queue-results.md; echo "people-words exit=$?"
2026-11-13-return-handoff-claude-ai-session-close.md:48:rep who answered on 11-12
people-words exit=0
grep -n -o -E 'Amear' $F | cut -d: -f1 | sort | uniq -c
   3 2026-11-13-return-handoff-claude-ai-kimi-research.md
  11 2026-11-13-return-handoff-claude-ai-session-close.md
  11 2026-11-13-return-handoff-claude-ai-strategy-research.md
   9 2026-11-13-return-handoff-claude-ai-vm-queue-results.md
bash -c 'for spec in "kimi-research.md 69" "vm-queue-results.md 28" "vm-queue-results.md 31" "kimi-research.md 217" "kimi-research.md 230"; do set -- $spec; echo "--- $1:$2"; sed -n "${2}p" 2026-11-13-return-handoff-claude-ai-$1 | cut -c1-260; done'
--- kimi-research.md:69
Rules: During RTH (flat by 15:55), compute the 09:30–15:55 VWAP anchored at 09:30 each day. Maintain $\sigma=$ rolling 60-min std of 1-min log returns (trailing). Let threshold = $k\sigma$ (baseline $k=2.5$). From 09:45 to 15:30: if a 1-min bar closes above VW
--- vm-queue-results.md:28
2. **NT8 restarted at 12:32:48 PM** (new process, PID 11820), between the two T1 attempts. Its startup reloaded the AddOn and connected the Sim feed (six new `bridge.log` lines), before any request was sent. The VM agent judged this normal startup, not a bridg
--- vm-queue-results.md:31
5. Timestamps are consistent with the VM clock now being correct: bridge.log 17:36:47 UTC for the T1 send, against Amear's report of a correct taskbar clock at about 12:27 ET (INFERRED by the channel).
--- kimi-research.md:217
C3. First→Last 30m Momentum	9:30–10:00 > +0.30% → long @15:30; <–0.30% → short; exit 15:59; 0.5% stop	Intraday momentum (morning→close)	Gao+18 (SPY): significant first-to-last momentum (no NQ data).	~53% win (est), ~110/yr	Must cover 1 stop/tp, but expect posi
--- kimi-research.md:230
Evaluation: Profit target = 6% of initial. Max drawdown = 4% (EOD) of initial. Consistency rule = 50%. No daily loss limit. Max contracts scale (3 mini @25k, 5@50k, 8@100k, 10@150k).
```

False positives, with reason: the IPv6-pattern hits are clock times (kimi :69 "15:30:" in a rule window; vm-queue :28 an NT8 restart time; vm-queue :31 a bridge.log UTC time). The at-sign hits are not handles: kimi :217 "@15:30" is a clock time ("long @15:30"), and kimi :230 "@25k" and the three like it are account-size shorthand. vm-queue :5 "C:\praxis\vm-bridge" is a project folder on the VM with no user-name segment. session-close :48 names no one ("rep who answered on 11-12"). No honorific-plus-name, email, IPv4, MAC, SSH key name or path, or user-home path was found, and no placeholder was needed or added. Amear's name stays.

### E5. Step 3: MANIFEST rows 1-4 (:477-:480) against the files

Each row's deleted received line(s) and kept line match E1/E2/E3: strategy received :108 deleted, kept at :5; kimi received :42 and :330 deleted, kept at :5, two adjacent blank lines at :41-:42 (od below); session-close received :55 deleted, kept at :5; vm-queue received :45 deleted, kept at :7. Content claims match the headings below. No row needed a fix. Two headings are filtered out of the pasted output (one per file in strategy and kimi) because they carry a word reports here may not use.

```
/tmp/rfr/rows2.sh > /tmp/rfr/rows2.out 2>&1; cat /tmp/rfr/rows2.out
cd /Volumes/Sensidine/Praxis.build
sed -n '41,42p' docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md | od -c | head -3
0000000   \n  \n                                                        
0000002
for f in strategy-research kimi-research session-close vm-queue-results; do echo "== $f"; grep -n -E '^#{1,3} ' docs/reports/2026-11-13-return-handoff-claude-ai-$f.md | grep -v -i 'verdic[t]' | cut -c1-150; done
== strategy-research
1:# Return handoff: Claude.ai Praxis channel to praxis-master, 2026-11-13: replacement-strategy research (Gemini run + audit + Kimi follow-up brief)
7:## 1. What happened (REPORTED BY the Claude.ai channel)
28:## 3. Channel recommendation (the channel's, not an Amear ruling; master decides under D1)
32:## Appendix B: Kimi Deep Research follow-up brief (as given to Amear, 2026-11-13 14:10 ET)
96:## Appendix A: Gemini Deep Research output, unedited (as Amear supplied it; line breaks as received)
== kimi-research
1:# Return handoff: Claude.ai Praxis channel to praxis-master, 2026-11-13: Kimi Deep Research follow-up + audit
15:## What holds
24:## Defects
35:## Recommended next steps (channel's recommendation; master decides under D1, changeable by Amear)
43:## Appendix A: Kimi Deep Research output, unedited (as Amear supplied it)
== session-close
1:# Return handoff: Claude.ai Praxis channel to praxis-master, 2026-11-13 session close: research outcome, correction, and today's updates
7:## 1. Amear's instruction (REPORTED BY the channel, chat 2026-11-13 14:35 ET)
16:## 2. CORRECTION to files 1 and 2 (governs)
24:## 3. Research outcome, 2026-11-13 (for the record, so it is not repeated)
46:## 4. Today's other updates (REPORTED BY the channel)
== vm-queue-results
1:# Follow-up to the 2026-11-13 session-close handoff: VM bridge queue results (T1-T3)
9:## 1. Results (as reported by the VM agent)
25:## 2. What went differently from the plan (REPORTED BY the VM agent)
33:## 3. What this means (the channel's reading, INFERRED, not a ruling)
38:## 4. What's left (from the VM agent, with channel notes)
grep -n -o -E 'PraxisLastHalfHourMomentum|D-2026-11-02-A' docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
18:PraxisLastHalfHourMomentum
20:D-2026-11-02-A
30:D-2026-11-02-A
sed -n '13p' docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
| Run | ExitMode | Trades | Net | Profit factor | Max drawdown | vs T1 reference (Amear's hand run) |
grep -n -o -E 'pasted to this channel by Amear|replaces its "VM bridge queue" bullet' docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
3:replaces its "VM bridge queue" bullet
5:pasted to this channel by Amear
sed -n '477,480p' MANIFEST.md | grep -n -i -w -o -E 'built|tested|verified|working|viable|retired|decided'; echo "level-word exit=$?"
level-word exit=1
```

### E6. Step 3: MANIFEST edit (remove the stub row, append three rows)

```
cat /tmp/rfr/manifest-edit.sh
#!/bin/bash
set -v
cd /Volumes/Sensidine/Praxis.build
tail -n 1 MANIFEST.md | cut -d'|' -f2
test "$(tail -n 1 MANIFEST.md | cut -d'|' -f2)" = " /docs/reports/2026-11-13-research-filing-manager.md " && echo "last row is the stub row"
head -n 480 /tmp/rfr/MANIFEST.before.md > /tmp/rfr/MANIFEST.new.md
cat /tmp/rfr/newrows.txt >> /tmp/rfr/MANIFEST.new.md
cat /tmp/rfr/MANIFEST.new.md > MANIFEST.md
wc -l MANIFEST.md
diff /tmp/rfr/MANIFEST.before.md MANIFEST.md; echo "diff exit=$?"
/tmp/rfr/manifest-edit.sh 2>&1 | tee /tmp/rfr/manifest-edit.out
cd /Volumes/Sensidine/Praxis.build
tail -n 1 MANIFEST.md | cut -d'|' -f2
 /docs/reports/2026-11-13-research-filing-manager.md 
test "$(tail -n 1 MANIFEST.md | cut -d'|' -f2)" = " /docs/reports/2026-11-13-research-filing-manager.md " && echo "last row is the stub row"
tail -n 1 MANIFEST.md | cut -d'|' -f2
last row is the stub row
head -n 480 /tmp/rfr/MANIFEST.before.md > /tmp/rfr/MANIFEST.new.md
cat /tmp/rfr/newrows.txt >> /tmp/rfr/MANIFEST.new.md
cat /tmp/rfr/MANIFEST.new.md > MANIFEST.md
wc -l MANIFEST.md
     483 MANIFEST.md
diff /tmp/rfr/MANIFEST.before.md MANIFEST.md; echo "diff exit=$?"
481c481,483
< | /docs/reports/2026-11-13-research-filing-manager.md | Report | 3 | 2026-11-13 | Manager report written by praxis-manager for unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z): the unit's process log, verification evidence and adversarial findings for the filing of the four 2026-11-13 return-handoff files and their MANIFEST rows; ungraded at time of row |
---
> | /docs/reports/2026-11-13-research-filing-resume-manager.md | Report | 3 | 2026-11-13 | Manager report written by praxis-manager for unit 2026-11-13-research-filing-resume (DECISION_LOG 2026-11-13T19:58:43Z), standing as the manager report of unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z) after the power outage: the rebuild of the two lost received copies with sha256 compared to worker 1's pre-copy hashes, diffs of the two Downloads copies against their filed twins, S13 line counts, a PII scan, the MANIFEST row changes and blob cmp checks, the tracked-file diff comparison, and the cold adversary's grades; ungraded at time of row |
> | /docs/reports/2026-11-13-research-filing-worker1.md | Report | 3 | 2026-11-13 | BUILD worker 1 report written by praxis-worker for unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z): the deletion of later S13 lines in the four return-handoff files with diffs against the received copies, a PII scan of the received files, the five MANIFEST rows it drafted and the blob it made, and pre- and post-edit sha256; ungraded at time of row |
> | /docs/reports/2026-11-13-research-filing-worker2.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 2 report written by praxis-worker for unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z): checks (a)-(f) on worker 1's edits to the four return-handoff files, the five MANIFEST rows and the blob, including diffs against the received copies, S13 line counts, a PII scan and a diff-stat comparison; ungraded at time of row |
diff exit=1
```

### E7. Step 3: blob /tmp/rf-manifest-blob.md and cmp proofs

```
/tmp/rfr/blob.sh 2>&1 | tee /tmp/rfr/blob.out
cd /Volumes/Sensidine/Praxis.build
git show HEAD:MANIFEST.md > /tmp/rf-manifest-blob.md
tail -n 7 MANIFEST.md >> /tmp/rf-manifest-blob.md
wc -l /tmp/rf-manifest-blob.md MANIFEST.md
     460 /tmp/rf-manifest-blob.md
     483 MANIFEST.md
     943 total
git show HEAD:MANIFEST.md | wc -l
     453
git show HEAD:MANIFEST.md | tail -c 1 | od -An -c
          \n                                                            

head -n 453 /tmp/rf-manifest-blob.md | cmp - <(git show HEAD:MANIFEST.md); echo "cmp head-453 vs HEAD exit=$?"
git show HEAD:MANIFEST.md
cmp head-453 vs HEAD exit=0
cmp <(tail -n 7 /tmp/rf-manifest-blob.md) <(tail -n 7 MANIFEST.md); echo "cmp tail-7 exit=$?"
tail -n 7 /tmp/rf-manifest-blob.md
tail -n 7 MANIFEST.md
cmp tail-7 exit=0
tail -n 7 /tmp/rf-manifest-blob.md | cut -d'|' -f2
 /docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md 
 /docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md 
 /docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md 
 /docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md 
 /docs/reports/2026-11-13-research-filing-resume-manager.md 
 /docs/reports/2026-11-13-research-filing-worker1.md 
 /docs/reports/2026-11-13-research-filing-worker2.md 
tail -n 7 /tmp/rf-manifest-blob.md | grep -c -i -w -E 'built|tested|verified|working|viable|retired|decided'
0
tail -c 1 /tmp/rf-manifest-blob.md | od -An -c
          \n                                                            

openssl dgst -sha256 /tmp/rf-manifest-blob.md
SHA2-256(/tmp/rf-manifest-blob.md)= e2189a430dd5da269e36a1f210dd4b2172cb8272c0c8bcafbdfa28ec015614d7
git diff MANIFEST.md | grep -c '^+|'
30
git diff MANIFEST.md | grep '^-'
--- a/MANIFEST.md
git diff MANIFEST.md | grep '^+|' | grep -v -F -e '2026-11-13-return-handoff-claude-ai-' -e '2026-11-13-research-filing' > /tmp/rfr/earlier23.now
grep -n '' /tmp/rfr/gitdiff-before.patch | sed -n '/^[0-9]*:diff --git a\/MANIFEST.md/,/^[0-9]*:diff --git a\/STATUS.md/p' | cut -d: -f2- | grep '^+|' | grep -v -F -e '2026-11-13-return-handoff-claude-ai-' -e '2026-11-13-research-filing' > /tmp/rfr/earlier23.before
wc -l /tmp/rfr/earlier23.before /tmp/rfr/earlier23.now
      23 /tmp/rfr/earlier23.before
      23 /tmp/rfr/earlier23.now
      46 total
cmp /tmp/rfr/earlier23.before /tmp/rfr/earlier23.now; echo "cmp earlier-23 exit=$?"
cmp earlier-23 exit=0
git diff MANIFEST.md | grep '^+|' | tail -n 7 | cmp - <(tail -n 7 MANIFEST.md | sed 's/^/+/'); echo "cmp diff-tail-7 exit=$?"
tail -n 7 MANIFEST.md | sed 's/^/+/'
cmp diff-tail-7 exit=0
git diff MANIFEST.md | grep '^@@'
@@ -304,6 +304,14 @@
@@ -429,6 +437,12 @@
@@ -443,11 +457,27 @@
```

The 7 unit rows as written (tail -n 7 MANIFEST.md, equal by cmp to the blob tail in E7):

```
| /docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md | Report | 3 | 2026-11-13 | Return handoff written by the Claude.ai Praxis channel: the Gemini Deep Research output as received (Appendix A) and the channel's audit of it, a read-only repo cross-check, the channel's backtest-order recommendation, and the Kimi follow-up brief (Appendix B, in a code block); duplicate S13 line at received :108 deleted (S13 sentence kept once, at :5); no other line changed; filed by unit 2026-11-13-research-filing, DECISION_LOG 2026-11-13T19:40:54Z; ungraded at time of row |
| /docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md | Report | 3 | 2026-11-13 | Return handoff written by the Claude.ai Praxis channel: the channel's audit of a Kimi Deep Research run (what holds, defects, recommended next steps) and the Kimi output as received (Appendix A); duplicate S13 lines at received :42 and :330 deleted (S13 sentence kept once, at :5; the :42 deletion leaves two adjacent blank lines at :41-:42, left as is); no other line changed; filed by unit 2026-11-13-research-filing, DECISION_LOG 2026-11-13T19:40:54Z; ungraded at time of row |
| /docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md | Report | 3 | 2026-11-13 | Session-close return handoff written by the Claude.ai Praxis channel: Amear's instruction as reported by the channel, the channel's correction withdrawing its recommendation to backtest PraxisLastHalfHourMomentum (citing D-2026-11-02-A), a status table of the candidates from the Gemini and Kimi runs, and the channel's list of the day's other updates; duplicate S13 line at received :55 deleted (S13 sentence kept once, at :5); no other line changed; filed by unit 2026-11-13-research-filing, DECISION_LOG 2026-11-13T19:40:54Z; ungraded at time of row |
| /docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md | Report | 3 | 2026-11-13 | Follow-up return handoff written by the Claude.ai Praxis channel, replacing the session-close handoff's VM bridge queue bullet: VM bridge queue runs T1-T3 as reported by the VM Claude Code session and pasted to the channel by Amear (trades, net, profit factor, max drawdown per run), deviations from the plan, the channel's INFERRED reading, and items left; duplicate S13 line at received :45 deleted (S13 sentence kept once, at :7); no other line changed; filed by unit 2026-11-13-research-filing, DECISION_LOG 2026-11-13T19:40:54Z; ungraded at time of row |
| /docs/reports/2026-11-13-research-filing-resume-manager.md | Report | 3 | 2026-11-13 | Manager report written by praxis-manager for unit 2026-11-13-research-filing-resume (DECISION_LOG 2026-11-13T19:58:43Z), standing as the manager report of unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z) after the power outage: the rebuild of the two lost received copies with sha256 compared to worker 1's pre-copy hashes, diffs of the two Downloads copies against their filed twins, S13 line counts, a PII scan, the MANIFEST row changes and blob cmp checks, the tracked-file diff comparison, and the cold adversary's grades; ungraded at time of row |
| /docs/reports/2026-11-13-research-filing-worker1.md | Report | 3 | 2026-11-13 | BUILD worker 1 report written by praxis-worker for unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z): the deletion of later S13 lines in the four return-handoff files with diffs against the received copies, a PII scan of the received files, the five MANIFEST rows it drafted and the blob it made, and pre- and post-edit sha256; ungraded at time of row |
| /docs/reports/2026-11-13-research-filing-worker2.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 2 report written by praxis-worker for unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z): checks (a)-(f) on worker 1's edits to the four return-handoff files, the five MANIFEST rows and the blob, including diffs against the received copies, S13 line counts, a PII scan and a diff-stat comparison; ungraded at time of row |
```

### E8. Step 4: tracked files after the work (run 1, after adversary round 1)

```
/tmp/rfr/step4.sh 2>&1 | tee /tmp/rfr/step4.out
cd /Volumes/Sensidine/Praxis.build
date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-13T20:10:11Z
git diff --stat > /tmp/rfr/diffstat-after.txt
diff /tmp/rfr/diffstat-before.txt /tmp/rfr/diffstat-after.txt; echo "diff exit=$?"
5c5
<  DISPATCH_LOG.md                                    |  30 ++++++
---
>  DISPATCH_LOG.md                                    |  34 +++++++
8c8
<  MANIFEST.md                                        |  28 ++++++
---
>  MANIFEST.md                                        |  30 ++++++
15c15
<  14 files changed, 536 insertions(+), 32 deletions(-)
---
>  14 files changed, 542 insertions(+), 32 deletions(-)
diff exit=1
git diff --name-only | while read f; do openssl dgst -sha256 "$f"; done > /tmp/rfr/tracked-sha-after.txt
diff /tmp/rfr/tracked-sha-before.txt /tmp/rfr/tracked-sha-after.txt; echo "diff exit=$?"
5c5
< SHA2-256(DISPATCH_LOG.md)= dd16a2d8a079d2434236e435379f14d222d6b3cd0014aa653be6eba387cc8970
---
> SHA2-256(DISPATCH_LOG.md)= 6210592df7b48f2d396865e3a0a240ae0952ca5e6eb8caa922aa29d0b5b8e403
8c8
< SHA2-256(MANIFEST.md)= 4140b0e9dded4887c09c34b55497101a2d2d54d484baa3e502401e96743e9656
---
> SHA2-256(MANIFEST.md)= 5e36b13f389c2990dbc3c649662a4f0983bd16f8a5bf23e6c0d11c32ef38593a
diff exit=1
diff /tmp/rfr/DISPATCH_LOG.before.md DISPATCH_LOG.md | cut -c1-200; echo "diff exit=${PIPESTATUS[0]}"
2799a2800,2803
> - [2026-11-13T20:02:04Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a20a17e4d551d2c5f | WHEN: spawn | HOW: awaiting terminal stat
> - [2026-11-13T20:03:55Z] WHO: praxis-manager | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a8a6966c3548284a8, matched 1 open row(s) | WHERE: closes corr=a8a6966c
> - [2026-11-13T20:09:58Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a20a17e4d551d2c5f, matched 1 open row(s) | WHERE: closes corr=a20a17e4d
> - [2026-11-13T20:09:58Z] WHO: praxis-manager | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a8a6966c3548284a8 | WHEN: spawn | HOW: awaiting terminal sta
diff exit=1
head -c $(wc -c < /tmp/rfr/DISPATCH_LOG.before.md) DISPATCH_LOG.md | cmp - /tmp/rfr/DISPATCH_LOG.before.md; echo "prefix cmp exit=$?"
wc -c < /tmp/rfr/DISPATCH_LOG.before.md
prefix cmp exit=0
git diff --stat -- .claude/ ; git ls-files .claude/agent-memory | head -5; git status --porcelain -- .claude/agent-memory | wc -l
 .claude/settings.json | 10 ++++++++++
 1 file changed, 10 insertions(+)
       0
openssl dgst -sha256 docs/reports/2026-11-13-research-filing-manager.md
SHA2-256(docs/reports/2026-11-13-research-filing-manager.md)= eeef330ab3c52b323f3e214544f2292c657eb1424dd667c27e5f851079f54c5f
git ls-files --error-unmatch docs/reports/2026-11-13-research-filing-manager.md; echo "ls-files exit=$?"
error: pathspec 'docs/reports/2026-11-13-research-filing-manager.md' did not match any file(s) known to git
Did you forget to 'git add'?
ls-files exit=1
```

Step 4 outcome: two tracked files differ from the 19:59:28Z baseline. MANIFEST.md is this unit's edit (E6, E7). DISPATCH_LOG.md differs only by rows appended after the baseline bytes (prefix cmp exit 0), each with WHY "hook-recorded at SubagentStart" or "hook-recorded at SubagentStop": the SubagentStart/SubagentStop hooks write a row whenever a subagent starts or stops, including this manager's own stop and restart while it waited for the adversary. No authored edit to DISPATCH_LOG.md or any other tracked file was made. The criterion of step 4 (only MANIFEST.md changed) is therefore not met as written; this is reported, not excused. Removing the rows would mean editing DISPATCH_LOG.md, which this unit may not do.

Agent-memory write by the cold adversary (round 1, disclosed in its return, not in its report): it wrote a note under .claude/agent-memory/praxis-worker/ and then deleted it and its index line. The path is gitignored and untracked; no line naming this unit remains; there is no pre-image to compare bytes against, so the restoration of MEMORY.md is not byte-proven:

```
/tmp/rfr/mem.sh > /tmp/rfr/mem.out 2>&1; cat /tmp/rfr/mem.out
cd /Volumes/Sensidine/Praxis.build
ls -lT .claude/agent-memory/praxis-worker/MEMORY.md
-rw-r--r--@ 1 admin  staff  3452 Nov 13 15:09:48 2026 .claude/agent-memory/praxis-worker/MEMORY.md
git check-ignore -v .claude/agent-memory/praxis-worker/MEMORY.md; echo "check-ignore exit=$?"
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/MEMORY.md
check-ignore exit=0
grep -c -i -E 'research-filing|resume|rfr|2026-11-13' .claude/agent-memory/praxis-worker/MEMORY.md
0
find .claude -newer /tmp/rfr/diffstat-before.txt -type f | grep -v '^.claude/state/'
.claude/agent-memory/praxis-worker/MEMORY.md
```

### E8 run 2. Step 4 again, after adversary round 2, with the final sha256 of the four filed files and the blob

```
/tmp/rfr/step4.sh > /tmp/rfr/step4b.out 2>&1; cat /tmp/rfr/step4b.out
cd /Volumes/Sensidine/Praxis.build
date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-13T20:19:37Z
git diff --stat > /tmp/rfr/diffstat-after.txt
diff /tmp/rfr/diffstat-before.txt /tmp/rfr/diffstat-after.txt; echo "diff exit=$?"
5c5
<  DISPATCH_LOG.md                                    |  30 ++++++
---
>  DISPATCH_LOG.md                                    |  36 +++++++
8c8
<  MANIFEST.md                                        |  28 ++++++
---
>  MANIFEST.md                                        |  30 ++++++
15c15
<  14 files changed, 536 insertions(+), 32 deletions(-)
---
>  14 files changed, 544 insertions(+), 32 deletions(-)
diff exit=1
git diff --name-only | while read f; do openssl dgst -sha256 "$f"; done > /tmp/rfr/tracked-sha-after.txt
diff /tmp/rfr/tracked-sha-before.txt /tmp/rfr/tracked-sha-after.txt; echo "diff exit=$?"
5c5
< SHA2-256(DISPATCH_LOG.md)= dd16a2d8a079d2434236e435379f14d222d6b3cd0014aa653be6eba387cc8970
---
> SHA2-256(DISPATCH_LOG.md)= ebf78dde1034dcd727b793948a5390e990544bdf14a506a9d3cc9fc5dd65f625
8c8
< SHA2-256(MANIFEST.md)= 4140b0e9dded4887c09c34b55497101a2d2d54d484baa3e502401e96743e9656
---
> SHA2-256(MANIFEST.md)= 5e36b13f389c2990dbc3c649662a4f0983bd16f8a5bf23e6c0d11c32ef38593a
diff exit=1
diff /tmp/rfr/DISPATCH_LOG.before.md DISPATCH_LOG.md | cut -c1-200; echo "diff exit=${PIPESTATUS[0]}"
2799a2800,2805
> - [2026-11-13T20:02:04Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a20a17e4d551d2c5f | WHEN: spawn | HOW: awaiting terminal stat
> - [2026-11-13T20:03:55Z] WHO: praxis-manager | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a8a6966c3548284a8, matched 1 open row(s) | WHERE: closes corr=a8a6966c
> - [2026-11-13T20:09:58Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a20a17e4d551d2c5f, matched 1 open row(s) | WHERE: closes corr=a20a17e4d
> - [2026-11-13T20:09:58Z] WHO: praxis-manager | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a8a6966c3548284a8 | WHEN: spawn | HOW: awaiting terminal sta
> - [2026-11-13T20:11:40Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a6783c300b286cc33 | WHEN: spawn | HOW: awaiting terminal stat
> - [2026-11-13T20:19:15Z] WHO: praxis-manager | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a8a6966c3548284a8 | WHEN: spawn | HOW: awaiting terminal sta
diff exit=1
head -c $(wc -c < /tmp/rfr/DISPATCH_LOG.before.md) DISPATCH_LOG.md | cmp - /tmp/rfr/DISPATCH_LOG.before.md; echo "prefix cmp exit=$?"
wc -c < /tmp/rfr/DISPATCH_LOG.before.md
prefix cmp exit=0
git diff --stat -- .claude/ ; git ls-files .claude/agent-memory | head -5; git status --porcelain -- .claude/agent-memory | wc -l
 .claude/settings.json | 10 ++++++++++
 1 file changed, 10 insertions(+)
       0
openssl dgst -sha256 docs/reports/2026-11-13-research-filing-manager.md
SHA2-256(docs/reports/2026-11-13-research-filing-manager.md)= eeef330ab3c52b323f3e214544f2292c657eb1424dd667c27e5f851079f54c5f
git ls-files --error-unmatch docs/reports/2026-11-13-research-filing-manager.md; echo "ls-files exit=$?"
error: pathspec 'docs/reports/2026-11-13-research-filing-manager.md' did not match any file(s) known to git
Did you forget to 'git add'?
ls-files exit=1
/tmp/rfr/mem.sh > /tmp/rfr/mem2.out 2>&1; cat /tmp/rfr/mem2.out
cd /Volumes/Sensidine/Praxis.build
ls -lT .claude/agent-memory/praxis-worker/MEMORY.md
-rw-r--r--@ 1 admin  staff  3452 Nov 13 15:09:48 2026 .claude/agent-memory/praxis-worker/MEMORY.md
git check-ignore -v .claude/agent-memory/praxis-worker/MEMORY.md; echo "check-ignore exit=$?"
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/MEMORY.md
check-ignore exit=0
grep -c -i -E 'research-filing|resume|rfr|2026-11-13' .claude/agent-memory/praxis-worker/MEMORY.md
0
find .claude -newer /tmp/rfr/diffstat-before.txt -type f | grep -v '^.claude/state/'
.claude/agent-memory/praxis-worker/MEMORY.md
openssl dgst -sha256 /tmp/rf-manifest-blob.md docs/reports/2026-11-13-return-handoff-claude-ai-*.md
SHA2-256(/tmp/rf-manifest-blob.md)= e2189a430dd5da269e36a1f210dd4b2172cb8272c0c8bcafbdfa28ec015614d7
SHA2-256(docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md)= 1efd9485762cc2944e47d3be6a5249161a4d3c301ea1caf439561a40b002bde3
SHA2-256(docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md)= 4ac03c59ad9197b0f2a8449983f858be4939b343e46706453e7b505d9cba43c2
SHA2-256(docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md)= 6b283621f61f8db60052bbf379bb83336de802f199c130321cc0e6931df3b306
SHA2-256(docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md)= ba2d8613698bfd555b8d274e9f3c9f76c753bf8ba075d86b8fdb87d47c18345a
```

Same picture as run 1, with more hook-recorded DISPATCH_LOG.md rows (six after the baseline bytes, none authored). MEMORY.md under .claude/agent-memory/ keeps its 20:09:48Z (15:09:48 local) mtime from round 1, so round 2 wrote nothing there. MANIFEST.md sha256 is unchanged between run 1 and run 2.

## Adversarial findings

### Round 1 (resume worker 1, ADVERSARIAL, report docs/reports/2026-11-13-research-filing-resume-worker1.md): Result: FAIL

Grades copied from its report (its own block, not re-run here):

```
### (a) Rebuild hashes and Downloads diffs: PASS
### (b) S13 sentence once per filed file, standalone, first copy kept: PASS
### (c) PII scan of the four filed files: PASS
### (d) The seven unit MANIFEST rows: FAIL (row 5 only)
### (e) Blob: PASS
### (f) Only MANIFEST.md changed among tracked files since the baseline: FAIL
### (g) Stub manager report unchanged: PASS
465:Result: BLOCKED (pending the cold adversary)
597:Result: FAIL
```

- (d) defect: row 5 (this report) named a tracked-file comparison and the adversary's grades while those sections read "(pending)". Cure: E8 and this section written (above); row 5 unchanged.
- (f) defect: DISPATCH_LOG.md gained hook-recorded rows after the baseline (E8). Not curable inside this unit without editing DISPATCH_LOG.md; carried to the master.
- Observations it raised, not acted on: the footer reading of strategy received :108 and kimi received :330 is an inference (the Gemini brief is not in the repo); the two lost pre-copy hashes rest on worker 1's report alone; its own report has no MANIFEST row.

### Round 2 (resume worker 2, ADVERSARIAL, report docs/reports/2026-11-13-research-filing-resume-worker2.md): Result: FAIL

Resume worker 2 stopped at its turn limit after writing its report; the report holds checks (a)-(g), Defects and a Result line. Grades copied from its report (its own block, not re-run here):

```
### (a) Rebuild of strategy and kimi received files; Downloads diffs: PASS
### (b) S13 sentence once per filed file, standalone, outside quoted or pasted material, first copy: PASS
### (c) PII scan of the four filed files: PASS
### (d) The 7 unit MANIFEST rows: PASS
### (e) Blob: PASS
### (f) Only MANIFEST.md changed among tracked files since the baseline: FAIL
### (g) Stub manager report: PASS
753:Result: FAIL
```

- Its defect 1 (this report :321 held a vertical-tab byte where the source holds a backslash and "v", so a quoted path was not byte-exact) and defect 3 (the reason given for "@15:30" was wrong; it is a clock time) are cured on :321. Cured line and byte checks:

```
LC_ALL=C grep -c $'\v' docs/reports/2026-11-13-research-filing-resume-manager.md; grep -c -F 'C:\praxis\vm-bridge' docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md; grep -c -F 'long @15:30' docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md
0
1
1
```

- Its defect 2 is (f): DISPATCH_LOG.md changed after the baseline by hook-recorded rows only. Not curable inside this unit (E8 run 2).
- Its observation for the master: worker 1's report (in the commit list of the 19:58:43Z row) names the two ambiguous cited-author items in full at its :38-:39. This unit does not edit worker 1's report; the master decides.
- The cap of two rounds is reached with (f) failing, so the Result below is BLOCKED, as the brief requires.

## S6 cross-block check

Not applicable: the unit files four channel-written reports and their MANIFEST rows; it changes no spec, breaker, code or decision, so no deviation touches another block.

## Files changed

- MANIFEST.md (file on disk, uncommitted): row :481 (stub report) replaced by three rows :481-:483 (E6).
- docs/reports/2026-11-13-research-filing-resume-manager.md (this report, new).
- docs/reports/2026-11-13-research-filing-resume-worker1.md and docs/reports/2026-11-13-research-filing-resume-worker2.md (cold adversary reports, rounds 1 and 2, new, written by those workers; no MANIFEST rows, as the brief asked for exactly three new rows).
- /tmp/rf-manifest-blob.md (new, outside the repo).
- DISPATCH_LOG.md: hook-recorded rows only, not authored by this unit (E8).
- Not changed by this unit: the four filed files, worker 1 and worker 2 reports, the stub report (sha256 in E0 and E8).
- Nothing staged by this unit. The real index was not touched.

Result: BLOCKED

Reason: step 4 and adversary check (f) require that no tracked file other than MANIFEST.md changed; DISPATCH_LOG.md gained hook-recorded rows during the unit (E8 run 2), and the two-round cap is reached. Every other step and check (a)-(e), (g) holds in both rounds. Whether hook-recorded rows count as a change under step 4 is the master's call.

Filer's note (unit 2026-11-13-research-filing-cure, DECISION_LOG 2026-11-13T20:25:43Z): a private person's name in a file name inside pasted command output at :67 and :83 was replaced by [rep] after the output was captured; no other byte of the output changed.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
