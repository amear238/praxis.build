# Unit `2026-11-06-gate-addendum-5` — manager report

## Task

Append one entry to DECISIONS.md: D-2026-11-04-B addendum 5. It records the third hand-back shape (task-notification) that `933ef70` added to `handback_check`. It states plainly that it was written AFTER the work, that S4 timing is NOT met, and that ratification is requested from Amear. No other file is edited: MANIFEST, ledgers, STATUS, HANDOFF, specs, scripts, `.claude/` and the index are untouched. Nothing is staged.

## Authorisation (S5, quoted)

- DECISION_LOG.md `[2026-11-06T22:25:00Z] WHO: praxis-master`, WHAT (verbatim, bold head): "**`uqb` FRESH AUDIT — FAIL 1 on S4 (new cycle after the ratification; S1/S2/S3/S9 PASS): the W-TN hook change (`933ef70`) has no DECISIONS.md entry written before the work. The park's own fault (addendum 1 timing) IS cured by addendum 4. MASTER'S FAULT; one correction = write addendum 5 honestly (after the fact) and put its timing to Amear for ratification; `uqb` stays open, not parked; loop continues.**" The same row names this unit: "unit `2026-11-06-gate-addendum-5` writes `D-2026-11-04-B addendum 5`".
- DECISION_LOG.md `[2026-11-06T20:08:28Z] **WHO: amear**`, ruling 3(b), pasted from `sed -n 479p DECISION_LOG.md | /usr/bin/grep -oE '.{0,80}APPROVE the hook change.{0,160}'`:
```
RATIFY D-2026-11-04-B addendum 1's timing — unpark uqb for a fresh audit; (b) APPROVE the hook change so the gate accepts the auditor's async hand-back. First commit through it is the test; on failure, revert and I keep typing commits. 4. Walk-forward arm (b) a
```
- DECISIONS.md:1076 (D-2026-11-06-B, ruling 3) says the hook change is in "its own unit (`2026-11-06-gate-async-handback`), whose DECISIONS addendum is the master's later step and is not written here."

## Rubric criteria addressed (verbatim from specs/SPEC_RUBRIC.md)

```
107:| S1 | Every claim in a report has pasted command output, not a description of output. |
110:| S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after. |
114:| S8 | No question that belongs to Amear is answered on his behalf. |
```
S13 (limitation sentence once, house style) is also applied to the entry.

**S4 for this entry is NOT met, and the entry says so.** This unit cannot cure S4 timing. Only Amear's ratification can, which is what the entry requests.

## Workers dispatched

| id | mode | outcome |
|---|---|---|
| `a2eb07cb7aa6f3e02` | ADVERSARIAL, read-only, over the scratch draft | `VERDICT: DEFECTS FOUND (1 blocking, 5 minor)`. All 6 were fixed in the draft before the single insert. |

## Process log

1. Captured the time, the commit facts, the DECISIONS.md baseline and the rubric rows.
2. Read the cited DECISION_LOG rows, the W-TN block (`gate-commit.sh:477–539`), the older shapes (`:451–476`), the report's V5/V6 output and the test file's case comments.
3. Recomputed the function identity sha myself.
4. Drafted the entry in the scratchpad: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/addendum5.md`.
5. Dispatched one adversarial worker over that draft.
6. Verified its toolUseId, stub-line and guard findings against the code. Applied the 9 replacements with a script (`fix1.py`, same scratchpad); the `v1` copy is kept beside it.
7. Stamped the time and appended once.
8. My first attempt to run the fix script inline was DENIED by the commit gate. The command text held the words "git commit" and a " -- " pathspec inside a quoted string, so the gate matched it. I moved the script to a file and nothing was written by the denied call.

## Verification evidence

Time, commit time, baseline (OBSERVED):
```
2026-11-06T22:20:08Z
234e4bc
2026-11-06T17:01:47-05:00
 .claude/hooks/gate-commit.sh                       |   97 +-
 .../2026-11-06-gate-async-handback-manager.md      | 1039 ++++++++++++++++++++
 scripts/tests/test-gate-handback.sh                |  284 ++++++
 3 files changed, 1415 insertions(+), 5 deletions(-)
    1163 DECISIONS.md
fb45b25648c66ea15158223c8bc40113291dde32  -
```
(`git diff --numstat HEAD DECISIONS.md` printed nothing before the append.)

Trees (OBSERVED):
```
18462b5810a302f9b53a4e96a1e7074bc13f739f
7cb366b93bedd7a8aca4e964ddbb8e5a02deac64
```
(`69ec506^{tree}`, `234e4bc^{tree}`.)

Function identity outside the W-TN block: HEAD minus 477–539, then `933ef70^`, then the hook diff 933ef70..HEAD (OBSERVED):
```
4f1ef67112dcf0d3e4a181f590238f9c42d9732d12e49243dbf84156752589a8  -
4f1ef67112dcf0d3e4a181f590238f9c42d9732d12e49243dbf84156752589a8  -
hook changed since 933ef70? rc=0
```

toolUseId source and stub lines, from `gate-commit.sh` (OBSERVED, excerpt):
```
   429	  meta="$(dirname "$at_rp")/agent-$aid.meta.json"
   430	  tuid=$(jq -r '(.toolUseId // "") | strings' "$meta" 2>/dev/null)
   441	  [ -n "$trs" ] || { echo "parent transcript has no tool_result for $tuid"; return 1; }
   444	      | if ($b | length) == 0 then "NOBIND"
   445	        elif any($b[]; split("\n") | any(.[]; gsub("^\\s+|\\s+$"; "") == $line)) then "SYNC"
   446	        else "BOUND" end' 2>/dev/null)
```

The append and the append-only proof (OBSERVED):
```
TS=2026-11-06T22:25:14Z
0
fb45b25648c66ea15158223c8bc40113291dde32  -
    1190 DECISIONS.md
fb45b25648c66ea15158223c8bc40113291dde32  -
27	0	DECISIONS.md
0
appended-bytes-match
1165:## 2026-11-06 — D-2026-11-04-B addendum 5: third hand-back shape (task-no
1
 12 files changed, 5726 insertions(+), 2 deletions(-)
```
Reading the lines in order:
- `0` = no `@@TS@@` placeholder is left.
- The sha of lines 1–1163 is the same before and after (`fb45b256…`).
- numstat is 27 added, 0 removed. `0` = no removed lines in the diff.
- The appended bytes match the final draft.
- The heading is at line 1165.
- The limitation sentence appears once.
- The staged stat is unchanged.

**Appended entry: DECISIONS.md lines 1164–1190.** Line 1164 is the blank separator and the heading is at line 1165.

## Adversarial findings

Worker `a2eb07cb7aa6f3e02`, FULL return as received (pasted from its hand-back, harness indentation removed):

I found one blocking defect and five minor ones. The S4 failure is stated plainly in the title and the first paragraph, and every quoted sentence matches its source exactly. The blocking defect is a git command quoted with an exit code it does not give.

**1. BLOCKING (S1): the command named for "file unchanged" returns rc=1, not rc=0.** At addendum5.md:11 the draft says "the file is unchanged since `933ef70`, OBSERVED with `git diff --quiet 933ef70 HEAD`, rc=0". That command has no path, so it compares the whole tree, and `69ec506` and `234e4bc` changed other files:
```
$ git diff --quiet 933ef70 HEAD; echo "nopath rc=$?"
nopath rc=1
$ git diff --quiet 933ef70 HEAD -- .claude/hooks/gate-commit.sh; echo rc=$?
rc=0
```
The fact itself is true, but the evidence as written gives the opposite result. Fix: add `-- .claude/hooks/gate-commit.sh`.

**2. MINOR (b): "the token's toolUseId" is wrong.** addendum5.md:16 says that, but the code takes the toolUseId from the meta.json file next to the agent transcript, not from the token (gate-commit.sh:429–431: `meta=".../agent-$aid.meta.json"`, `tuid=$(jq -r '(.toolUseId // "") | strings' "$meta")`). Only the agent id comes from the token (`T_AID=$(tok agent_id)`, :663). This matters because it misstates where the trust comes from: meta.json can be forged, which is why the binding check exists.

**3. MINOR (b): wrong line range for the stub check.** addendum5.md:18 says the stub is "checked first (lines 444–452)". The extraction is at :433–441 and the classification at :442–446; 444–452 starts in the middle of the classification.

**4. MINOR (b): two test cases are mislabelled.** addendum5.md:21 lists N3b as "the frame inside a `tool_result`", but test-gate-handback.sh:151 says `# N3b: notification text as a text block beside a tool_result block, origin removed`. It also lists N16 as "an injected description", but :267 says `# N16: two tool_use records with the same id and different descriptions`. The counts are right: 5 positives and 27 negatives.

**5. MINOR (d): wrong source label on the operational consequences.** The heading at addendum5.md:22 marks them "OBSERVED by the unit". But the bash-guard and parenthesised-trailer point (:25) is the master's own observation (DECISION_LOG row 22:07:11Z, line 468, "OBSERVED this turn: the Bash call was blocked by `scripts/master-bash-guard.sh`"). "So the master ends its turn" (:23) is the master's own procedure, not something the unit observed. The heading also sits awkwardly with :26, which marks the mid-turn denial in a live run UNVERIFIED.

**6. MINOR (S8/d): the guard is overstated and Amear's question is narrowed.**
- addendum5.md:25 says "The master bash-guard rejects `>`". The regex is narrower: `(^|[^>])>{1,2}[[:space:]]*[^&]`, with path exemptions (master-bash-guard.sh:12–14). For example, `>&2` passes.
- The draft calls the open question "a new hook change". The source row (468) names two options: "either the guard exempts `git commit` messages or the attribution line keeps the parenthesised form". The second option is not a hook change, and the draft already treats it as current practice. So the question goes to Amear with one option dropped.

**What I tried that held:**
- **(a) S4 and the authorisation chain:** S4 timing NOT met is stated in the title and first paragraph. The chain 20:08:28Z (WHO: amear) → 20:12:00Z dispatch → unit is real (DECISION_LOG lines 479, 478). Leaving D-2026-11-06-B out of the "before" chain is correct, because the filing unit ran 20:13–20:33Z, alongside the hook work (hook workers at 20:18Z, per row 463).
- **Quotes:** ruling 3(b) (`grep -c -F` = 1 in row 479 and 1 in the draft), "I repeated the exact fault class the unit was parked for." (= 1), and DECISIONS.md:1076 "is the master's later step and is not written here" (= 1) are all exact.
- **Git facts:** `933ef70` commit time `2026-11-06T17:01:47-05:00` and `69ec506^{tree}` = `18462b5810a302f9b53a4e96a1e7074bc13f739f` both reproduce.
- **(b) The rest of the code claims:** lines 477–539, 491–504, 498, 503, 505–537 and 453–476 match the code. The function-identity hash reproduced: both sides gave `4f1ef67112dcf0d3e4a181f590238f9c42d9732d12e49243dbf84156752589a8`. Report lines :53, :60, :188–189, :325–360, :362–400, :515 and :554 match.
- **(c) S8:** the draft ratifies nothing and does not extend 3(b).
- **(e) Limitation sentence:** it appears exactly once (count = 1 at line 8), in the same "**Standing limitation:**" form as DECISIONS.md:1111 and :1122.

I wrote no report file. Scratch output is in /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/adv/.

VERDICT: DEFECTS FOUND (1 blocking, 5 minor)

**Disposition:**
- Defect 1: the command now carries the path.
- Defect 2: the entry now says `toolUseId` comes from `meta.json` (lines 429–431), and that only the agent id comes from the token.
- Defect 3: the entry now cites lines 433–441, 442–446 and 447–452.
- Defect 4: N3, N3b and N16 are now labelled from the test comments.
- Defect 5: each consequence is now graded on its own line, and the master's practice is attributed to row 22:07:11Z.
- Defect 6: the entry now quotes the guard regex. It quotes BOTH options from row 468 and states that the parenthesised form is current practice, not chosen.
- Fix application output (OBSERVED): `ok 9`, `8` changed lines, `1` limitation sentence, `1` quoted fault sentence.
- **Not done:** a second adversarial pass over the fixed text. The fixes were checked against the code by the manager only (excerpts above).

## S6 cross-block check

The one deny this unit saw came from hook 2 (the commit gate). Its message, "Commit denied: a pathspec after ' -- ' …", matched the trigger I expected: my python heredoc's command text contained a quoted "git commit" string and a " -- " path. No parallel-deny masking is suspected. I re-ran the work from a script file and it was allowed.

## Files staged

None. This unit staged nothing. DECISIONS.md and this report are left unstaged, as the brief asked. The pre-existing staged set is unchanged:
```
 12 files changed, 5726 insertions(+), 2 deletions(-)
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Result: PASS**. The deliverable is filed in the honest form. S4 timing for addendum 5 itself is NOT met, and that is stated. It awaits Amear's ratification, and `Praxis_build-uqb` stays at FAIL 1.
