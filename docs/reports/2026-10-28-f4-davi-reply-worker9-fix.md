# F4 Davi-reply addendum — worker9 fix

## Task
Six wording fixes in the 2026-10-28 addendum of `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` (lines 541 and later), plus a header-line fix in `docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md` (line 6, outside the `text` fence). No verdict changed.

## Mode
BUILD (fix). Not added, not committed.

## Criterion
F4 (frozen, `specs/SPEC_RUBRIC.md`). The addendum makes no discharge claim. These edits narrow wording only: the grant phrasing, a verbatim CLAUDE.md quote, a heading, Frank's attribution, and the attestation status of the no-Gmail and no-draft claims.

## Process log
1. Took the baseline: the head-537 hash matched ffda2e09…84cb1. Extracted the B fence to scratchpad `fence_before.txt` (25 lines).
2. Checked both proposed CLAUDE.md strings with `grep -Fc` before editing. Both are byte-exact (1 each), so the brief's text was used unchanged.
3. Applied the edits with Edit and exact old strings:
   (1) grant sentence, ~625;
   (2) pattern sentence, 3 wrapped lines → 1 line at 621;
   (3) heading D;
   (4) "from Frank's relay" → "in the relay recorded in §1 (whose respondent §1's table records as Frank)";
   (5) attestation sentence in A, ~582;
   (6) attestation in F, ~772;
   B: line 6 gets ", on the manager's attestation".
4. Ran every check below.

Notes:
- The numstat for A went from 241/0 before the edit to 239/0 after. A is staged (`AM`), so the addendum is unstaged against the index. Edit 2 joined 3 lines into 1, which accounts for the -2.
- B is untracked (`??`), so `git diff` shows nothing for B. The fence `cmp` is the proof for B.
- Edit 2 now writes the pattern as a single long line (as specified). The rest of the addendum wraps at about 80 columns. This is cosmetic.

## Verification evidence (pasted as run)

```text
$ head -n 537 A | shasum -a 256
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -
$ git diff --numstat -- A
239	0	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
$ CLAUDE.md substring checks
1
1
$ same two strings present in A (post-537)
621:The PRAXIS pattern, verbatim from `CLAUDE.md` line 21: "
621:The PRAXIS pattern, verbatim from `CLAUDE.md` line 21: "
$ /usr/bin/grep -n ^tools .claude/agents/praxis-worker.md
6:tools: Read, Grep, Glob, Bash, Write, Edit, TodoWrite
$ fence cmp
cmp: identical (exit 0)
8e14a6904fbdcdc85cc3b264a462c3a474fa309ca26942fa7430cfbcd7932dd3  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/e2d12a7c-ea8d-4471-9c36-a46d92b1a310/scratchpad/fence_before.txt
8e14a6904fbdcdc85cc3b264a462c3a474fa309ca26942fa7430cfbcd7932dd3  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/e2d12a7c-ea8d-4471-9c36-a46d92b1a310/scratchpad/fence_after.txt
$ B header line 6
- Transcribed by praxis-worker from the image only; Gmail not read by this filing unit's manager or workers, on the manager's attestation (per the master's dispatch brief, not on disk: the Gmail connector was unavailable this session).
$ quote checks (line > 537, "> " lines, prefix stripped, grep -Fc against fence)
605	1	You can use custom Tradovate API access with your MyFundedFu
606	1	• Automated trading solutions using an API are supported, al
607	1	• Algo trading is permitted on all plans, including evaluati
608	1	• High-frequency trading is not allowed, and automated tools
609	1	• For live accounts, automated trading must comply with CME 
611	1	You are responsible for the performance and reliability of y
642	1	Hi Frank — thanks for confirming, that's helpful. Two follow
711	1	• High-frequency trading is not allowed, and automated tools
712	1	• For live accounts, automated trading must comply with CME 
714	1	You are responsible for the performance and reliability of y
730	1	Hi ! Thank you so much for reaching out to MyFundedFutures S
733	1	Davi from MyFundedFutures <eda.daniel.david@myfundedfutures.
735	1	Davi-MyFundedFutures Support
738	1	Hello amear,i hope this mail meets you well.
740	1	Thank you for contacting MyFundedFutures Support! I'll be ha
742	1	Hi ! Thank you so much for reaching out to MyFundedFutures S
754	1	Hi Frank — thanks for confirming, that's helpful.
$ stale-phrase grep (expect empty)
$ forbidden sweep (expect empty)
$ git diff --stat B
```

Every `> ` quote after line 537 (17 lines) returns `grep -Fc` = 1 against the fence. The stale-phrase grep and the forbidden sweep are both empty.

## Files changed (not staged, per brief)
- `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` (addendum only)
- `docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md` (line 6 only)
- `docs/reports/2026-10-28-f4-davi-reply-worker9-fix.md` (this report)

## Result: PASS
