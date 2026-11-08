Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

# Unit 2026-11-08-rubric-a11-o1 (U6) — manager report

## Task
Two edits to `specs/SPEC_RUBRIC.md`, made by an agent under A11, with nothing else changed:
(1) replace lines 3–4 ("The build side does not edit this file. It proposes changes; Amear applies them.") with A11's rule, cited inline;
(2) add a state line under `### O1 —` marking O1 `PASSED@a2f1067` under A8, cited inline.
Also: a unified patch of only those two edits against `HEAD:specs/SPEC_RUBRIC.md`, which keeps the uncommitted July R-A/R-B/R-C hunk (Amear's, return handoff §4 item 4) out, plus one appended MANIFEST row.
Dispatch row: DISPATCH_LOG `2026-11-08T15:53:00Z` (WHO: praxis-master). Nothing staged, nothing committed.

## Rubric criteria addressed
S1, S2, S4, S5, S8, S13, and A11's own rule ("cites a logged Amear approval inline and passes the auditor before commit"). The brief quotes all of these verbatim.
- **S13:** the standing sentence appears once, on line 1. This report states no backtest or P&L figure.
- **S5:** the authorisation is the ledger row DECISION_LOG `2026-11-08T15:05:00Z`, **WHO: amear** (:723), pasted below. No approval is inferred from the brief.
- **S8:** both edits quote or point to his words. The parts that are not his words are labelled in the rubric text as "master's reading (filing note 3), changeable by Amear". The open annualisation method is pointed to D-2026-11-08-B NEEDS AMEAR (iii); this unit does not answer it.

## Workers dispatched (id, mode, outcome)
| id | mode | outcome |
|---|---|---|
| a80a659f9e0486f3a | BUILD | Drafted and applied both edits with one script, to a HEAD copy and to the working tree, and built the patch. Its closing line was `GRADE: REFUTED` *against my draft of edit 1*: my draft's parenthetical "(DECISION_LOG stamp, WHO: amear, DECISIONS entry)" says what a logged approval contains, and A11 does not say that. The worker removed it. Every constraint held on what it applied. |
| accdc9c65562849b2 | ADVERSARIAL (patch v1) | `GRADE: NOT REFUTED`, with minor findings M1–M4. I acted on M1 (see Process log). |
| a5c7b46dae6eaa51a | ADVERSARIAL (final patch) | `GRADE: NOT REFUTED`, with minor findings M1–M5. Its closing block is pasted verbatim below. |

## Process log
1. Baseline captured (pasted below). Read A8, A11, R2, R3, NEEDS AMEAR (iii) and filing note 3 by `sed -n` / `grep -n`. Observed: the D-2026-11-08-B heading is at DECISIONS.md:**1710**, not the brief's :1709.
2. Worker 1 (BUILD) built the patch with this method:
   - `git show HEAD:specs/SPEC_RUBRIC.md > u6/head.md` and `cp` to `u6/edited.md`;
   - ran one `python3 -I` script (each old text asserted to occur exactly once; the A8 sentence extracted from DECISIONS.md:1748 by regex) on `edited.md` and on the working-tree rubric;
   - `git diff --no-index --no-color u6/head.md u6/edited.md`, with the header paths rewritten by `sed` to `a/specs/SPEC_RUBRIC.md` / `b/specs/SPEC_RUBRIC.md`.
3. **Deviations from the brief's wording (S4), each resolved toward the brief's rule "Do not paraphrase A11 into anything it does not say":**
   - (a) Edit 1 leaves out the brief's parenthetical on the form of the citation.
   - (b) Edit 1 says "the auditor" (A11's word), not the brief's "independent auditor".
   - (c) After adversary 1's M1, the O1 block's last two lines were changed by the same scripted method (single-occurrence assert, applied to both copies, patch regenerated). They no longer label only the sha as the master's reading. They now say "Marking O1 PASSED, and the sha as the commit that lands D-2026-11-08-B, are the master's reading (filing note 3), changeable by Amear." The DECISION_LOG `15:05:00Z` row itself lists "O1 → `PASSED@<sha of B's commit>`" under the master's readings (adversary 1, M1).
   - (d) MANIFEST row 298 was changed to match (c).

   This unit wrote no DECISIONS.md entry for (a)–(d), because the brief forbids touching DECISIONS.md. Whether these need one is the master's.
4. I ran every proof again myself after the final patch (pasted below). The adversary got the artifact and the criteria only, never worker 1's reasoning.
5. MANIFEST row appended by a `python3 -I` append, then edited in place by a single-occurrence replace on the last line only. Lines 1–297 are byte-identical to HEAD (pasted).
6. Negative tests: the patch FAILS `--check` against the already-edited rubric, and a HEAD→working-tree diff DOES carry `R-A` (count 1). The gate discriminates.

## Verification evidence (pasted output only)
**Masking note.** The July hunk contains a word that the token-minting script reads, so every output that shows it is piped through `sed 's/erdict/*rdict/g'`, and that is the only change. The auditor should re-run the commands unmasked.

**Sources** (`sed -n`, this session):
```
$ sed -n 1748p;1756,1762p DECISIONS.md
A8  O1 is discharged by R2 + R3 + A7. Gate 6 formula (Pardo WFE):
A11 Amear no longer edits any repo file by hand, including
    specs/SPEC_RUBRIC.md. Amear decides; agents write. Every rubric
    edit cites a logged Amear approval inline and passes the auditor
    before commit. Replace the rubric's "The build side does not edit
    this file. It proposes changes; Amear applies them." accordingly,
    citing this ruling. Do not hand Amear paste-in steps for repo
    files.
$ sed -n 1710p DECISIONS.md | cut -c1-60
## 2026-11-08 — D-2026-11-08-B: Amear's answers A1–A11 t
$ sed -n 1556p;1558p DECISIONS.md
R2  GO requires arm (a) to pass. Arm (b) can only add confidence or
R3  Gate 6 (WFE) applies to arm (b) only (§4 item 3).
$ sed -n 723p DECISION_LOG.md | cut -c1-48
- [2026-11-08T15:05:00Z] **WHO: amear** | WHAT: 
```

**Before** (first command of the unit; it was a single chained command, run as `git rev-parse --short HEAD && git diff --cached --stat | tail -1 && git diff --numstat HEAD -- specs/SPEC_RUBRIC.md MANIFEST.md && wc -l MANIFEST.md && git status --porcelain | grep -E 'SPEC_RUBRIC|MANIFEST|2026-11-08-rubric'`):
```
a2f1067
 12 files changed, 5726 insertions(+), 2 deletions(-)
10	0	specs/SPEC_RUBRIC.md
     297 MANIFEST.md
 M specs/SPEC_RUBRIC.md
```
Before this unit, MANIFEST had no line in the numstat, meaning 0 lines changed against HEAD. I did not capture the full pre-edit `git diff HEAD -- specs/SPEC_RUBRIC.md` separately. Proof (e) below shows that the working tree now equals HEAD + the July hunk as committed in dangling WIP `9c47b1a` (2026-08-15) + this patch, byte for byte. Each scripted edit asserted that it replaced exactly one occurrence. So the July hunk was the same before and after this unit; that step is INFERRED from (e) plus those asserts.

**Proofs (a)–(g)**, `bash scratchpad/u6p/proofs.sh`, final patch, masked:
```
$ cat <patch>
diff --git a/specs/SPEC_RUBRIC.md b/specs/SPEC_RUBRIC.md
index d53d1cf..e1963d6 100644
--- a/specs/SPEC_RUBRIC.md
+++ b/specs/SPEC_RUBRIC.md
@@ -1,7 +1,9 @@
 # PRAXIS — SPEC RUBRIC
 
-Authority: the scoping agent (Claude.ai) via Amear. The build side does not
-edit this file. It proposes changes; Amear applies them.
+Authority: the scoping agent (Claude.ai) via Amear. Amear decides; agents write.
+Amear does not edit this file by hand. Every edit cites a logged Amear approval
+inline and passes the auditor before commit (D-2026-11-08-B A11; DECISION_LOG
+2026-11-08T15:05:00Z, WHO: amear).
 
 This file exists because context windows compact and reasoning held only in a
 session is reasoning that will be lost. Every criterion below is graded, not
@@ -72,6 +74,12 @@ closure states it has not been confirmed by direct inquiry.
 ## OPEN — gradeable now
 
 ### O1 — Walk-forward gate set for the replication arm
+**State:** PASSED@a2f1067. Amear's ruling A8, D-2026-11-08-B (DECISION_LOG
+2026-11-08T15:05:00Z, WHO: amear): "O1 is discharged by R2 + R3 + A7."
+R2 and R3 are in D-2026-11-08-A (DECISIONS.md:1556, :1558); the gate set per arm
+is A7; the gate-6 formula is A8 (annualisation method: D-2026-11-08-B NEEDS AMEAR
+(iii)). Marking O1 PASSED, and the sha as the commit that lands D-2026-11-08-B,
+are the master's reading (filing note 3), changeable by Amear.
 Walk-forward efficiency ≥ 0.50 is one of six non-negotiable Block 2 pass gates
 and is undefined without an in-sample optimisation step. Deviation D removed
 optimisation from the first pass. **Required:** a written statement of which
--- (a1) scratch index from HEAD, apply --check --cached
read-tree rc=0
apply --check --cached rc=0
--- (a2) scratch checkout dir, apply --check
apply --check (non-repo dir) rc=0
--- (b) +/- lines of the patch (excluding headers)
-Authority: the scoping agent (Claude.ai) via Amear. The build side does not
-edit this file. It proposes changes; Amear applies them.
+Authority: the scoping agent (Claude.ai) via Amear. Amear decides; agents write.
+Amear does not edit this file by hand. Every edit cites a logged Amear approval
+inline and passes the auditor before commit (D-2026-11-08-B A11; DECISION_LOG
+2026-11-08T15:05:00Z, WHO: amear).
+**State:** PASSED@a2f1067. Amear's ruling A8, D-2026-11-08-B (DECISION_LOG
+2026-11-08T15:05:00Z, WHO: amear): "O1 is discharged by R2 + R3 + A7."
+R2 and R3 are in D-2026-11-08-A (DECISIONS.md:1556, :1558); the gate set per arm
+is A7; the gate-6 formula is A8 (annualisation method: D-2026-11-08-B NEEDS AMEAR
+(iii)). Marking O1 PASSED, and the sha as the commit that lands D-2026-11-08-B,
+are the master's reading (filing note 3), changeable by Amear.
count: 12
--- (c) apply patch to HEAD copy with patch(1), diff vs working tree
patch rc=0
273a274,283
> 
> **No-v*rdict returns — R-A / R-B / R-C, ruled 2026-07-27. Source: DECISION_LOG
> row `2026-07-27T18:15Z`.**
> 
> A grading agent that returns no explicit v*rdict has not graded. Absence of a
> v*rdict is treated as FAIL for the commit decision and never as PASS or as
> no-finding. It does NOT count toward the park rule's two-strike limit, which
> counts adverse v*rdicts on the work. A no-v*rdict unit may be re-dispatched only
> after material reduction, stated in the dispatch row; a second consecutive
> no-v*rdict return on the same bead counts as the second FAIL.
diff rc=1
--- (c2) applied copy vs worker's edited copy
cmp rc=0
--- (d) grep -c 'R-A' <patch>
0
--- patch path counts
1
--- (e) containment: HEAD + July hunk (9c47b1a) + U6 patch vs working tree
july patch rc=0
u6 patch rc=0
cmp rc=0
--- (f) negative: patch --check against the already-edited working tree
error: patch failed: specs/SPEC_RUBRIC.md:1
error: specs/SPEC_RUBRIC.md: patch does not apply
apply --check on edited tree rc=1
--- (g) negative: a HEAD->worktree patch DOES carry the July hunk
1
```

**After:**
```
$ git diff --numstat HEAD -- specs/SPEC_RUBRIC.md MANIFEST.md
1	0	MANIFEST.md
20	2	specs/SPEC_RUBRIC.md
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ git status --porcelain | grep -E 'SPEC_RUBRIC|MANIFEST|2026-11-08-rubric'
 M MANIFEST.md
 M specs/SPEC_RUBRIC.md
?? docs/reports/2026-11-08-rubric-a11-o1-manager.md
$ cmp <(git show HEAD:MANIFEST.md) <(head -n 297 MANIFEST.md); echo rc=$?
rc=0
$ git diff HEAD -- specs/SPEC_RUBRIC.md | sed 's/erdict/*rdict/g'
diff --git a/specs/SPEC_RUBRIC.md b/specs/SPEC_RUBRIC.md
index d53d1cf..fa31f03 100644
--- a/specs/SPEC_RUBRIC.md
+++ b/specs/SPEC_RUBRIC.md
@@ -1,7 +1,9 @@
 # PRAXIS — SPEC RUBRIC
 
-Authority: the scoping agent (Claude.ai) via Amear. The build side does not
-edit this file. It proposes changes; Amear applies them.
+Authority: the scoping agent (Claude.ai) via Amear. Amear decides; agents write.
+Amear does not edit this file by hand. Every edit cites a logged Amear approval
+inline and passes the auditor before commit (D-2026-11-08-B A11; DECISION_LOG
+2026-11-08T15:05:00Z, WHO: amear).
 
 This file exists because context windows compact and reasoning held only in a
 session is reasoning that will be lost. Every criterion below is graded, not
@@ -72,6 +74,12 @@ closure states it has not been confirmed by direct inquiry.
 ## OPEN — gradeable now
 
 ### O1 — Walk-forward gate set for the replication arm
+**State:** PASSED@a2f1067. Amear's ruling A8, D-2026-11-08-B (DECISION_LOG
+2026-11-08T15:05:00Z, WHO: amear): "O1 is discharged by R2 + R3 + A7."
+R2 and R3 are in D-2026-11-08-A (DECISIONS.md:1556, :1558); the gate set per arm
+is A7; the gate-6 formula is A8 (annualisation method: D-2026-11-08-B NEEDS AMEAR
+(iii)). Marking O1 PASSED, and the sha as the commit that lands D-2026-11-08-B,
+are the master's reading (filing note 3), changeable by Amear.
 Walk-forward efficiency ≥ 0.50 is one of six non-negotiable Block 2 pass gates
 and is undefined without an in-sample optimisation step. Deviation D removed
 optimisation from the first pass. **Required:** a written statement of which
@@ -264,6 +272,16 @@ blocked, move on" wording. It is outside this repository and affects other
 projects, so it is **not** edited from here. This section is the binding text for
 PRAXIS work.
 
+**No-v*rdict returns — R-A / R-B / R-C, ruled 2026-07-27. Source: DECISION_LOG
+row `2026-07-27T18:15Z`.**
+
+A grading agent that returns no explicit v*rdict has not graded. Absence of a
+v*rdict is treated as FAIL for the commit decision and never as PASS or as
+no-finding. It does NOT count toward the park rule's two-strike limit, which
+counts adverse v*rdicts on the work. A no-v*rdict unit may be re-dispatched only
+after material reduction, stated in the dispatch row; a second consecutive
+no-v*rdict return on the same bead counts as the second FAIL.
+
 **Absolutes are amended between sessions only — 2026-07-26 human ruling.**
 
 A rule declared absolute is **never amended inside the session that hits it.**
```

## Adversarial findings
Final adversary (a5c7b46dae6eaa51a), closing block verbatim from `scratchpad/u6adv2/closing.md`:
```
GRADE: NOT REFUTED
Attacks run, and why each one failed:
A1 Scope. diff(HEAD rubric, HEAD+patch) is exactly 3,4c3,6 plus 74a77,82 (six lines directly under "### O1", which is HEAD line 74). No other +/- lines. No CR (grep -c $'\r' = 0). No trailing whitespace on + lines. Both files end in a newline (0a). The O1 body, F1-F4, O2-O4, S1-S13 and the process rulings are untouched.
A2 Leak. grep -c 'R-A' on the patch = 0. diff(HEAD+patch, working tree) = 273a274,283, the July hunk only.
A3 Apply. GIT_INDEX_FILE=scratch idx: read-tree HEAD, then apply --check --cached gives rc=0. The patch's index line d53d1cf..e1963d6 equals hash-object of HEAD's rubric and of HEAD+patch.
A4 Containment. patch(1) -o: HEAD + July hunk (git diff 9c47b1a^ 9c47b1a, 10/0) + patch gives a file cmp-identical to the working-tree rubric, in both orders. No .rej files. HEAD..WT numstat = 20/2 = 10/0 + 10/2.
A5 Wording. The quote "O1 is discharged by R2 + R3 + A7." is word for word from A8 (DECISIONS.md:1748). The A11 lines match A11's words (:1756-1759). The ledger row 2026-11-08T15:05:00Z is WHO: amear (DECISION_LOG.md:723). R2 is at :1556 and R3 at :1558 at HEAD, and DECISIONS.md has no uncommitted changes. a2f1067 adds D-2026-11-08-B (its parent has 0 matches; log -S gives a2f1067). The PASSED marking and the sha are labelled master's reading, with filing note 3 cited, matching note 3 (answers :66) and the row's own "MASTER'S READINGS". The annualisation gap points to NEEDS AMEAR (iii) (:1803), so S8 is not breached. I found no master's reading presented as Amear's.
A6 MANIFEST :298. Accurate: it is the 4th amendment row (rows 115/116/117/247 come before it), phase 2 matches rows 290-297, and it is the only change MANIFEST has against HEAD (1/0).
Minor, non-refuting:
M1 The cited approval row 15:05:00Z is not in HEAD's DECISION_LOG.md (0 matches; HEAD has 715 lines, the row is at WT :723, uncommitted append 19/0). The rubric commit must land with a DECISION_LOG flush, or the inline citation points at a row that history does not have. B at HEAD already has the same dependency.
M2 Note 3 and the ledger row make PASSED conditional ("after the rubric unit's auditor confirms the statement exists" at the sha). The state block leaves that condition out and does not record who confirmed it. That is fine before commit only if this audit is that confirmation.
M3 O1 now reads PASSED but still sits under "## OPEN — gradeable now", and "**State:**" is a new convention in this rubric (no other item has it). A reader who goes by section headings sees O1 as OPEN.
M4 "Amear's ruling A8": B files A1-A10 as his "answers", and only A11 is called a rule change. The label is a slight relabel, not a change of substance.
M5 "(filing note 3)" names no file. The note is answers file :66, which a reader reaches only through B.
```
First adversary (accdc9c65562849b2, on patch v1, which is identical except for the last two O1 lines), closing block verbatim from `scratchpad/u6adv/closing.md`:
```
GRADE: NOT REFUTED

Attacks run, and why each failed:
1. Scope rebuild. HEAD rubric + July hunk (from 9c47b1a, via patch -o) + u6 patch -> cmp vs working tree = CMP_IDENTICAL; sha256 2f17442f... both. Reverse order also CMP2_IDENTICAL. Worktree vs HEAD = 20/2 = July 10/0 + patch 10/2. 3 hunks (@@ -1,7, @@ -72,6, @@ -264,6 = July). Patch has 2 hunks, 12 +/- lines, all inside the two edits. No CR in either file. Both end in 0a. Only whitespace hits are the blank context lines.
2. Apply. Scratch index from HEAD: `git apply --check --cached` exit 0. Against the edited worktree: exit 1 ("patch does not apply"). Reverse-check on worktree: exit 0. --whitespace=error: exit 0. Patch preimage index d53d1cf = `git rev-parse HEAD:specs/SPEC_RUBRIC.md`; postimage 1104686 = hash-object(HEAD+patch).
3. Leak. No July-hunk line in the patch (grep -F of every non-blank July + line: none). 'R-A' count in the patch: 0.
4. Wording / pointers. "Amear decides; agents write." is verbatim A11. "Every edit cites a logged Amear approval inline and passes the auditor before commit" matches A11. A8 quote "O1 is discharged by R2 + R3 + A7." is verbatim (DECISIONS.md:1748). DECISIONS.md:1556 = R2, :1558 = R3, both inside D-2026-11-08-A (heading :1534). DECISION_LOG.md:723 = 15:05:00Z, **WHO: amear**, and it carries A8 and A11. a2f1067 is the commit that adds the B heading (count 0 at a2f1067^, 1 at a2f1067). NEEDS AMEAR (iii) exists (:1803) and is only pointed to, not answered (S8 holds). A7 does give the gate set per arm.
5. MANIFEST :298. "AMENDMENT ROW 4" is right: earlier rows are :115, :116, :117 (ROW 2) and :247 (ROW 3). Every clause matches the patch.

MINOR findings that do not refute the claim:
M1. The PASSED state itself is a master's reading. The cited row DECISION_LOG:723 lists, under "MASTER'S READINGS ... changeable by him": "O1 -> PASSED@<sha of B's commit> after the rubric unit's auditor confirms the statement exists". B's A8 bullet (:1776) labels it the same way. The O1 block labels only "The sha" as the master's reading. Mapping "discharged" to PASSED is left unlabelled, and it sits next to "Amear's ruling A8". The block also leaves out the auditor-confirmation condition. The pre-commit audit required by A11 covers that condition, but the text does not say so.
M2. O1 now says PASSED@a2f1067 but still sits under "## OPEN — gradeable now". The section says OPEN and the inline line says PASSED. The claim keeps O1 in OPEN on purpose, and A8 does not say where O1 goes.
M3. The cited approval row (DECISION_LOG 15:05:00Z) is in no commit. `git log --all -S` finds nothing, and a2f1067:DECISION_LOG.md has 0 hits. It exists only in the uncommitted working tree (+19 lines). If the rubric is committed before the ledger flush, the commit's inline citation points to a row that is not in the repo. D-2026-11-08-B at HEAD already has the same issue (:1794 cites DECISION_LOG.md:723).
M4. Process, not wording. Filing note 2, the A8 bullet ("listed apart") and the 15:05 row ("rubric unit's blob = HEAD rubric + the :3-4 change") each describe the :3-4 change alone. The patch combines it with the O1 edit. Master row DECISION_LOG 15:52:00Z and DISPATCH_LOG 15:53:00Z authorise the combined unit U6. The master's reading was revised by the master.
```
What I did with the minor findings:
- v1 M1: fixed (Process log 3c).
- v1 M2 / v2 M3 (O1 sits under the OPEN heading): left as is, because the brief says not to move O1. Routed below.
- v1 M3 / v2 M1 (the 15:05:00Z row is not committed): routed to the master.
- v1 M4: the master authorised the combined unit (DISPATCH_LOG `15:53:00Z`).
- v2 M2 (the auditor-confirmation condition): the pre-commit audit is that confirmation. That is master's reading (filing note 3), changeable by Amear.
- v2 M4 ("ruling" vs "answers"): the term is the brief's. Routed.
- v2 M5 (filing note 3 names no file): routed.

## S6 cross-block check
- F1–F4, O2–O4, S1–S13 and the process rulings are untouched. The adversary's scope attack found only `3,4c3,6` and `74a77,82` against HEAD.
- F2 stays FROZEN: A6, "F2's state changes when Amear approves the proposed values".
- O1 interacts with the values spec :132–:134 and the WF spec gate-6 text. Neither is edited here; that amendment is a later unit under B.
- The A8 annualisation method stays open as B's NEEDS AMEAR (iii).
- The July R-A/R-B/R-C hunk is untouched and absent from the patch.

## Files staged
None by this unit; the brief forbids `git add`. Staged count unchanged: `12 files changed, 5726 insertions(+), 2 deletions(-)`.
- Changed in the working tree: `specs/SPEC_RUBRIC.md` (the two edits, on top of the July hunk) and `MANIFEST.md` (+1 row, :298).
- Created: this report, and the patch at `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dac8a676-3ed6-4fca-96a1-deecc90b3c48/scratchpad/u6-rubric.patch`.
- Nothing was written to `.claude/` or to any ledger.

## Result
Result: PASS at level WRITTEN. This is the manager's stress-test outcome, not the auditor's grade. The edits are written and the patch is proven; nothing has been graded by the auditor or committed. Under A11, the rubric edit is not complete until the auditor passes it before commit.

## Does NOT cover
- The values-spec / WF-spec amendments for A2/A4/A5/A7/A8.
- Moving O1 out of "## OPEN".
- Any decision on the July hunk.
- The DECISION_LOG flush of the `15:05:00Z` row.
- Any ledger row, DECISIONS entry, commit, or audit.

## Still the master's
- Accepting deviations 3(a)–(d), and whether they need a DECISIONS.md entry (S4).
- Committing through a temp index built from HEAD + this patch + MANIFEST :298 + this report, so that the July hunk stays out.
- Flushing DECISION_LOG `15:05:00Z` (and `15:52:00Z`) with or before the rubric commit, so the inline citation resolves in history.
- Whether "(filing note 3)" should name `docs/reports/2026-11-08-amear-answers-flags.md:66`.
- Whether "Amear's ruling A8" should read "Amear's answer A8".

## Questions only Amear can answer
1. Is O1's discharge recorded as `PASSED@a2f1067`, with the sha being the commit that lands D-2026-11-08-B? That is the master's filing note 3, changeable by him.
2. Once O1 is PASSED, should it move out of "## OPEN — gradeable now", or stay there with its state line?
3. The July R-A/R-B/R-C hunk (return handoff §4 item 4): commit, revise, or drop?
4. B's NEEDS AMEAR (iii): which annualisation method A8 means.
