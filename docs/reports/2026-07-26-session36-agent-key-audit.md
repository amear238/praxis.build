# Session 36 audit — `agent` key insert in `.claude/settings.json`

**Date:** 2026-07-26 (UTC) · **Auditor:** praxis-auditor (cold; producer reasoning not read)
**HEAD:** `c1dec30` · **Artifact under grade:** the staged index, one path
**Result: FAIL** — S1, S2, S4, S5, S7, S9. No token minted.

---

## 0. What is actually staged

```
$ git diff --cached --name-only
.claude/settings.json

$ git diff --cached
diff --git a/.claude/settings.json b/.claude/settings.json
index 4521f90..5ba14e1 100644
--- a/.claude/settings.json
+++ b/.claude/settings.json
@@ -1,4 +1,5 @@
 {
+"agent": "praxis-master",
   "env": {
     "ORCH_N8N_WEBHOOK": "https://n8n.myzerker626.win/webhook/praxis-orch-notify",
     "CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH": "2",

$ git diff --cached --numstat
1	0	.claude/settings.json
```

One path, one added line, zero deletions. Matches the brief.

The 8sw report is confirmed **absent from the index**:

```
$ git status --porcelain
M  .claude/settings.json
 M AUDIT_LOG.md
 M DECISION_LOG.md
 M DISPATCH_LOG.md
 M ISSUE_REGISTER.md
?? .claude/agent-memory/
?? docs/reports/2026-07-26-session34-manifest-amendment.md
?? docs/reports/2026-07-26-session34-p0-flush-audit.md
?? docs/reports/2026-07-26-session35-8sw-audit-round1.md
?? docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
```

`2026-07-26-session35-8sw-gate-park-conflict.md` carries `??` — untracked, not in the index. That check passes.

## 0.1 Independent checks requested

**JSON validity — VALID.**

```
$ jq . .claude/settings.json > /dev/null && echo "JQ_EXIT=$?"
JQ_EXIT=0
```

**Key ordering / collisions — no existing key touched.**

```
$ git show :.claude/settings.json | jq -r 'keys_unsorted[]'
agent
env
hooks
permissions

$ git show HEAD:.claude/settings.json | jq -r 'keys_unsorted[]'
env
hooks
permissions
```

`agent` is purely additive at position 0. `env`, `hooks`, `permissions` are byte-unchanged (the diff shows no other hunk). No hook reads top-level ordering — the hooks block is addressed by path (`.hooks.PreToolUse[].command`), not by index into the root object.

**Indentation — cosmetic, not load-bearing.** The line sits at column 0 while its siblings are at column 2. `jq` parses it (above), and JSON has no significant whitespace. It is a legibility defect only. Worth recording that it is also a *provenance tell*: this line was not written by whatever formatted the rest of the file, which is consistent with the stated history that praxis-master did not author it.

**Provenance — confirmed as stated.**

```
$ git show HEAD:.claude/settings.json | jq '.agent'
null
$ jq '.agent' .claude/settings.json
"praxis-master"
$ git show :.claude/settings.json | jq '.agent'
"praxis-master"
$ git diff .claude/settings.json
(no output — worktree and index agree)
```

---

## 1. S9 — FAIL. The producer's premise is false on the artifact.

> **S9:** "Any config field a guarantee depends on is positive-controlled: confirm a visible script fires at that field, then confirm an invented key at the same position produces byte-identical silence. A field that parses is not a field that is honoured."

The producer's position, recorded in the `21:36Z` `DECISION_LOG` row, is: *"S9's positive control has not been run and no guarantee here rests on the key."*

The first clause is true. **The second clause is false**, and I established that by experiment rather than by accepting it.

### 1.1 Three guards branch on exactly this identity

```
$ grep -rn "praxis-master" scripts/ .claude/settings.json
scripts/master-write-guard.sh:5:# Scope: agent_id is present ONLY for subagents, so empty agent_id + agent_type=praxis-master == the main thread running as praxis-master.
scripts/master-write-guard.sh:9:[ "$AGENT" = "praxis-master" ] || exit 0
scripts/master-write-guard.sh:18:echo "BLOCKED: praxis-master may only write ledgers, specs, and reports. Dispatch praxis-manager for '$FILE'." >&2
scripts/agent-spawn-guard.sh:8:# Consequence: praxis-manager spawned by praxis-master can reach praxis-auditor,
scripts/agent-spawn-guard.sh:13:#   .agent_type               -> the CALLER's agent type ("praxis-master" main
scripts/master-bash-guard.sh:4:# Scope: agent_id is present ONLY for subagents, so empty agent_id + agent_type=praxis-master == the main thread running as praxis-master.
scripts/master-bash-guard.sh:8:[ "$AGENT" = "praxis-master" ] || exit 0
scripts/no-commit-guard.sh:7:#   `--agent praxis-master`     -> agent_id ABSENT, agent_type "praxis-master"
scripts/no-commit-guard.sh:18:[ "$AGENT" = "praxis-master" ] && [ -z "$AGENT_ID" ] && exit 0
.claude/settings.json:2:"agent": "praxis-master",
```

`master-write-guard.sh:9` and `master-bash-guard.sh:8` are **arming conditions**. Those guards do nothing at all unless the caller is identified as `praxis-master`.

### 1.2 Toggle experiment — the behaviour changes

Everything held constant, only the identity field toggled:

```
$ printf '{"tool_input":{"command":"echo hi > /tmp/x"}}' | ./scripts/master-bash-guard.sh; echo "EXIT=$?"
EXIT=0

$ printf '{"agent_type":"praxis-master","tool_input":{"command":"echo hi > /tmp/x"}}' | ./scripts/master-bash-guard.sh; echo "EXIT=$?"
BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.
EXIT=2

$ printf '{"tool_input":{"file_path":"/Volumes/Sensidine/Praxis.build/scripts/foo.sh"}}' | ./scripts/master-write-guard.sh; echo "EXIT=$?"
EXIT=0

$ printf '{"agent_type":"praxis-master","tool_input":{"file_path":"/Volumes/Sensidine/Praxis.build/scripts/foo.sh"}}' | ./scripts/master-write-guard.sh; echo "EXIT=$?"
BLOCKED: praxis-master may only write ledgers, specs, and reports. Dispatch praxis-manager for '/Volumes/Sensidine/Praxis.build/scripts/foo.sh'.
EXIT=2
```

`no-commit-guard.sh` re-routes on the same field (payloads written to files first, because the literal string trips the live gate against my own shell):

```
$ ./scripts/no-commit-guard.sh < p_absent.json; echo "EXIT=$?"     # agent_type ABSENT
EXIT=0
$ ./scripts/no-commit-guard.sh < p_master.json; echo "EXIT=$?"     # agent_type=praxis-master, no agent_id
EXIT=0
$ ./scripts/no-commit-guard.sh < p_mgr.json; echo "EXIT=$?"        # agent_type=praxis-manager + agent_id
BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
EXIT=2
```

Absent and `praxis-master` both exit 0 — but at **different lines**. Absent exits at `:16` (`[ -z "$AGENT" ] && exit 0`, "ordinary session, not the agent stack, untouched"). `praxis-master` exits at `:18`, the main-thread-committer exemption. Same outcome for a `git commit`; different classification for every other Bash call, and a different security story.

Two guards flip from **inert to live**. That is a guarantee depending on a config field. S9 is triggered.

### 1.3 The project's own documentation says this field is load-bearing

```
$ sed -n '104,106p' docs/agent-spawn-guard.md
Note what is **absent**: there is no `agent_type` key on a main thread. That is
load-bearing for §4.
```

The observed main-thread payload has **no** `agent_type`. The entire fail-open analysis in §4 of that document rests on it. Installing `"agent": "praxis-master"` is an attempt to change precisely that observed fact, and it is being committed without re-observing it.

### 1.4 The positive control has not been run, by anyone

The only mechanism ever observed to produce `agent_type: "praxis-master"` is the **CLI flag**, documented from live payloads at `scripts/no-commit-guard.sh:7`:

```
#   `--agent praxis-master`     -> agent_id ABSENT, agent_type "praxis-master"
```

The `settings.json` `agent` key is a **different mechanism** asserted to produce the same result. Neither half of S9 has been performed on it:

- Not done: confirm a visible script fires when the key is set — requires a live main-thread session with the key installed and a hook trip observed.
- Not done: confirm an invented key at the same position (e.g. `"agnt"`, `"agent_type"`) produces byte-identical silence.

```
$ claude --version
2.1.220 (Claude Code)
```

Same binary and same class of assumption behind all four prior incidents the ledger row itself names: the nesting default, the stale binary read, frontmatter `hooks:`, and `Agent(<type>)` allowlist scoping. In every one of those the field parsed and was silently ignored. The tests in §1.2 prove the **scripts** read `agent_type`; they prove nothing about whether the **settings key** produces it.

**S9: FAIL.** The change either silently arms two never-trip-tested guard paths, or silently does nothing while both the file and the ledger assert an identity. Which of those is true is unknown, and it is knowable by one experiment that was not run.

---

## 2. S5 — FAIL. The append is a transcript, and it is not in the commit.

> **S5:** "No approval is inferred from a verbal or in-session exchange. The ledger append is the authorisation."

### 2.1 The authorising row is not in the index and not in history

```
$ git diff --cached --name-only -- DECISION_LOG.md
(no output — NOT staged)

$ git show HEAD:DECISION_LOG.md | grep -c "21:36Z"
0

$ git diff --stat -- DECISION_LOG.md
 DECISION_LOG.md | 10 ++++++++++
 1 file changed, 10 insertions(+)
```

S5 states that *the ledger append is the authorisation*. The staged commit contains the authorised act and **not the authorisation**. After this commit nothing reachable from `git log` authorises the change. The authorisation exists only as uncommitted working-tree text.

That is not a technicality here, because the committed state actively contradicts it:

```
$ git status --porcelain HANDOFF.md
(no output — clean, identical to HEAD)

$ grep -n "agent. key" HANDOFF.md
5:...The `agent` key is deliberately NOT installed.
18:- P2: STOP. The `agent` key is NOT the orchestrator's to install. Report evidence, hold the key, wait for Amear.
```

`HANDOFF.md` is committed at HEAD and says the key is not installed and is not the orchestrator's to install. This commit installs it and lands **no committed record** reversing that. A reader of history after this commit sees an unexplained identity key inserted directly against two standing committed instructions.

### 2.2 Proposer and approver are one verbal utterance, transcribed by the executor

```
$ grep -n "21:36Z" DECISION_LOG.md
69:- [2026-07-26T21:36Z] PROPOSED BY: amear (direct in-session instruction, verbatim: "commit the agent key") | APPROVED BY: amear, same instruction, session 36 | WHO: praxis-master (execution) | ...
```

Both authorisation slots are filled by the *same* spoken sentence, transcribed into the ledger by the agent that then executed it. The rubric forecloses treating that as discharge:

```
$ sed -n '322,336p' specs/SPEC_RUBRIC.md
**What this fix is, and what it is not — read this before relying on it.** It is
a **legibility** fix. It is **not verification, and it is not authentication.**
Nothing prevents an orchestrator from authoring both fields; an agent-written
`APPROVED BY: Amear` is indistinguishable in the file from a real one.
...
**The threat model is drift, not forgery.** ... It does
not make the answer trustworthy — for that, the authorisation chain in S4 and
S5 (the ledger append *is* the authorisation) remains the only control, and it
too is a record rather than a proof.
```

I weigh the "threat model is drift, not forgery" clause in the producer's favour: the instruction is same-day, same-session, quoted verbatim, and the row is candid that its source is a verbal. That candour is real and I credit it. But if an agent may transcribe a verbal into the ledger and thereby self-authorise, S5's first sentence has no force whatsoever — every verbal becomes an authorisation by the act of writing it down, and the rule nullifies itself. That reading cannot be right.

**S5: FAIL.** Hard ground: the authorisation is not in the commit, so the commit carries none (§2.1). Reinforcing ground: the append is a self-transcript filling both slots from one utterance, which the rubric's own ruling says is not authentication (§2.2).

---

## 3. S4 — FAIL on traceability. Timing sub-claim PASSES.

> **S4:** "Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after."

**"Written before the work" — verified TRUE, and I credit it.** Filesystem mtimes; `date +%z` returns `-0400`:

```
$ stat -f '%m %N' DECISION_LOG.md .git/index
1785101788 DECISION_LOG.md
1785101793 .git/index

$ echo $(( $(stat -f '%m' .git/index) - $(stat -f '%m' DECISION_LOG.md) ))
5
```

The ledger was written 5 seconds before the index. Ordering is correct. The row's `21:36Z` stamp matches (`17:36:28` local at `-0400` = `21:36:28Z`).

**"Traceable authorisation chain" — FAIL.** The chain has one link, a verbal with no independent record, and the entry recording it is excluded from the commit (§2.1). Nothing in committed history traces this deviation to an authorisation.

**Noted, not decisive:** the rubric names `DECISIONS.md`; the entry is in `DECISION_LOG.md`. Both files exist (`DECISIONS.md` last modified Jul 21; `DECISION_LOG.md` Jul 26). Established repo practice is plainly `DECISION_LOG.md`, and I do not hang the verdict on the naming.

---

## 4. S1 — FAIL. No report exists; the claim-bearing row describes rather than pastes, and cites a command that proves nothing.

> **S1:** "Every claim in a report has pasted command output, not a description of output."

```
$ ls -1 docs/reports/ | grep -i "session36\|session-36"
NO session-36 producer report exists
```

No producer report accompanies this change. The only claim-bearing artifact is the `21:36Z` `DECISION_LOG` row, and every verification claim in it is a **description** of output: *"reflog showing `reset: moving to HEAD~1`"*, *"single-writer confirmed by `lsof -a -p 70788,56458 -d cwd`"*, *"confirmed by `git diff .claude/settings.json`"*. Zero pasted transcripts.

Worse, one cited command **cannot support the claim it is cited for**. The row states: *"(3) staged diff is exactly one added line, confirmed by `git diff .claude/settings.json`"*.

```
$ git diff .claude/settings.json
[no output, exit 0]

$ git diff --cached --numstat
1	0	.claude/settings.json
```

`git diff <path>` compares **worktree to index**. It is empty here, and it would be empty whether one line or a thousand were staged. The command that establishes the claim is `git diff --cached`. The claim happens to be true; the cited evidence does not establish it. That is exactly the failure S1 exists to catch — a plausible-sounding citation nobody read back.

The other two preconditions I verified independently and they hold: the reflog confirms the reset (`c1dec30 HEAD@{0}: reset: moving to HEAD~1`, `599885e HEAD@{1}`), and `main` == `origin/main` == `c1dec30`.

**S1: FAIL.**

---

## 5. S2 — FAIL. A mechanism claim asserted by inspection and falsified by experiment.

> **S2:** "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure."

The row does two things, one good and one disqualifying.

**Good, and I credit it explicitly:** it marks the honouring of the key `UNVERIFIED`, names the four prior silently-ignored-field incidents, and states plainly that S9's positive control has not been run. That is correct S2 discipline and it is rare.

**Disqualifying:** in the same sentence it asserts *"no guarantee here rests on the key."* That is a claim of the form ruling R3 governs:

```
$ sed -n '158,165p' specs/SPEC_RUBRIC.md
**S9 note — ruling R3, 2026-07-26. Positive control extends to claims about
mechanism, not only to config keys.** S9 as written tests a *field*: make the
script fire at it, then show an invented key at the same position produces
byte-identical silence. That is not enough. A claim of the form *"X is covered
by mechanism Y"* gets the same treatment — toggle Y, hold everything else
constant, and show the behaviour changes. If it does not change, Y was never the
mechanism.
```

The negative form — *"no mechanism depends on this field"* — is the same class of claim and takes the same treatment. It was asserted by inspection. I toggled it (§1.2) and the behaviour changed: two guards go from exit 0 to exit 2. **The claim is false.**

Second S2 defect: precondition (3) is labelled `PRECONDITIONS VERIFIED IN-SESSION, NOT RECALLED` while resting on a command that verifies nothing (§4). "Verified" is reported above the level the evidence supports.

**S2: FAIL.**

---

## 6. S7 — FAIL.

> **S7:** "Nothing is committed while any audit box is unchecked."

Unstaging the 8sw report keeps that artifact out of the commit. It does not check the box. Open audit boxes at this moment:

**(a) The 8sw report is at an unresolved audit FAIL.** From the report itself:

```
49:...Round 1 **FAILED** this criterion; a round-2 adversarial pass found 16 further defects...
2851:Round 1 of this document was audited and returned **FAIL on S1 and S9**...
```

**(b) `Praxis_build-sk8` — P1, OPEN**, holding the S9 toggle experiment, per line 53 of that report.

**(c) A misfired un-audited commit on `main` is still open.** `ISSUE_REGISTER.md`, `[2026-07-26T19:51Z]`, ends: `STATE: open — awaiting Amear's disposition on 599885e`. That row's own words: *"an artifact carrying an auditor FAIL reached `main` with no token."*

**(d) A parked bead at audit-fail-x2 is unresolved:**

```
$ git branch | cat
* main
  parked/Praxis_build-37h
```

**(e) No audit token exists:**

```
$ ls .claude/state/
current-bead   iteration-count   max-iterations   orchestrator-active   run-mode
```

I acknowledge the narrower reading — that S7 governs the artifact whose own audit is incomplete, and that this one-line change is separately gradeable, which is the reasoning the ledger row gives. I do not accept it. The rubric text is "**Nothing** is committed while **any** audit box is unchecked," and this repo has already ruled against orchestrator carve-outs of exactly this shape: *"with no exceptions and no orchestrator judgment applied"*, *"no 'the defect was mechanical'"* (`specs/SPEC_RUBRIC.md:240-251`). Splitting a commit out from under an open audit is a judgment call of that family.

**S7: FAIL.** This is the least clear-cut of the six and it does not carry the verdict. S5 and S9 do.

---

## 7. Verdict

| Criterion | Verdict | Evidence / gap |
|---|---|---|
| **S1** — every claim has pasted output | **FAIL** | No session-36 report exists. The `21:36Z` row describes output and pastes none; its cited proof `git diff .claude/settings.json` returns empty and cannot establish the staged-content claim (§4) |
| **S2** — no over-reporting | **FAIL** | *"No guarantee here rests on the key"* asserted by inspection, falsified by toggle: two guards move exit 0 → exit 2 (§1.2, §5). Precondition (3) labelled "VERIFIED" on a command that verifies nothing |
| **S4** — pre-written entry, traceable chain | **FAIL** | Timing **passes** — ledger written 5s before staging, mtimes pasted (§3). Traceability fails: entry not staged, not in HEAD; nothing in committed history authorises the change |
| **S5** — ledger append is the authorisation | **FAIL** | `git diff --cached --name-only -- DECISION_LOG.md` → empty; `git show HEAD:DECISION_LOG.md \| grep -c "21:36Z"` → `0`. Commit carries the act without the authorisation, against committed `HANDOFF.md:5,:18`. Both authorisation slots filled by one transcribed verbal (§2) |
| **S7** — nothing committed with an audit box open | **FAIL** | 8sw at FAIL round 1/2; `Praxis_build-sk8` P1 OPEN; `599885e` disposition open; `parked/Praxis_build-37h` unresolved; no token in `.claude/state/` (§6) |
| **S9** — config field positive-controlled | **FAIL** | Two guards' arming condition **is** this identity; toggle changes behaviour (§1.2). `docs/agent-spawn-guard.md:105` calls main-thread `agent_type` absence "load-bearing". Only the `--agent` CLI flag was ever observed to set it; the settings key is untested on 2.1.220 in both S9 directions (§1.4) |

**Overall: FAIL** — S1, S2, S4, S5, S7, S9.

Independent checks: JSON **valid**; no existing key, ordering assumption, or hook-read schema broken; indentation **cosmetic**, not load-bearing.

**No token minted.** `.claude/hooks/audit-approve.sh` was not invoked and `.claude/state/` carries no audit token. Nothing was edited, fixed, staged, or committed by this audit.
