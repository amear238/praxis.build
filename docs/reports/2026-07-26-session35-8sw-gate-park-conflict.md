# Session 35 — `Praxis_build-8sw`: gate-commit vs. absolute park rule

**Date:** 2026-07-26 · **Bead:** `Praxis_build-8sw` (P1, OPEN) · **Manager:** praxis-manager
**Repo:** `/Volumes/Sensidine/Praxis.build` · **Branch:** `main`
**HEAD at unit start:** `c1dec30` · **HEAD now:** `599885e` — this report file was
committed to `main` by a human terminal paste *during its own audit*. Round 1 of this
document carried `**HEAD:** c1dec30` here, which is no longer true on disk. Full pasted
evidence and disposition in **"Files staged"** below. Reported, not repaired.
**Mode:** INVESTIGATION ONLY. No agent unit — the original investigation or the round-1
repair — edited, staged, committed, branched, checked out, or reset anything in this repo.
The one exception is this file, which the repair unit edits in place and leaves unstaged.
`599885e` was not made by any agent in this chain; see "Files staged".

---

## Task

Bead `Praxis_build-8sw` asserts that the ABSOLUTE park rule
(`specs/SPEC_RUBRIC.md`, "Process rulings") and `.claude/hooks/gate-commit.sh`
are in direct conflict, and that consequently *"session 34 could not complete
step 1 of the park. Work left STAGED BUT UNCOMMITTED on branch
parked/Praxis_build-37h."*

That last sentence is false on disk — the park commit exists. This unit
establishes, **by experiment**, which of two mutually exclusive mechanisms
produced it:

- **(A)** `gate-commit.sh` contains a path that ADMITS the commit (branch
  exemption / matcher miss / env condition / early exit) → the commit gate has
  a hole, a more serious finding than the park conflict.
- **(B)** The commit was made from a **human terminal**, where a `PreToolUse`
  hook has no reach → the gate is intact and 8sw's real content is that park-rule
  step 1 is **unexecutable by the orchestrator**.

Sub-question: does `gate-commit.sh` distinguish a `parked/*` branch from `main`
in any way at all?

**Nothing here recommends a remediation or ranks the options. That is Amear's
ruling (S8).**

---

## Rubric criteria addressed

Traced to `specs/SPEC_RUBRIC.md`, "Standing criteria — graded on every dispatch":

| # | Criterion (verbatim) | Where discharged |
|---|---|---|
| S1 | "Every claim in a report has pasted command output, not a description of output." | §2 Verification evidence, §3 and §4 — each claim carries its own fenced transcript. **Two blocks carry no `rc`, and the reason is the harness, not a gap:** a *live* hook denial (§2.1, §2.4) is refused by Claude Code before a shell exists, so the harness returns `PreToolUse:Bash hook error: [<hook path>]: …` **instead of** a shell exit code. Those blocks are evidenced by the block text and the hook-naming bracket. Every *copy*-driven block carries a command and an `rc`. Round 1 **FAILED** this criterion; a round-2 adversarial pass found 16 further defects — both rounds are recorded in "Audit corrections" |
| S2 | "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure." | §6 UNVERIFIED; each finding labelled OBSERVED vs INFERRED; every copy-driven result capped at "the script exited N" in §7 |
| S3 | "Every gate claimed working has been deliberately tripped at least once, with the block observed." | §2.1 and §2.4 — live deny against the **real registered hook**, observed first-hand by the manager, full text pasted |
| S8 | "No question that belongs to Amear is answered on his behalf." | §5 — options enumerated, **unranked**, no recommendation |
| S9 | "Any config field a guarantee depends on is positive-controlled: confirm a visible script fires at that field, then confirm an invented key at the same position produces byte-identical silence. A field that parses is not a field that is honoured." | §3.2 + §2.4 — arming-marker control **DISCHARGED** on two independently built harnesses. Hook **registration** field (`hooks.PreToolUse[].matcher` / the hook `command` path in `.claude/settings.json`) **UNVERIFIED** — the invented-key control can only run at the one position hard limit 1 forbids. Round 1 additionally asserted that this limit was **TOTAL** (that no equivalent-position control existed anywhere else); that totality was asserted, never established — nobody enumerated the alternative positions before concluding there were none. Carried as `Praxis_build-sk8` (P1, OPEN), which holds the toggle experiment. See §6 item 1 and Result item 3 |

No rubric gap: every acceptance criterion handed to a worker is quoted from an
existing rubric line. None was authored here.

---

## Workers dispatched

| id | mode | scope | outcome |
|---|---|---|---|
| `a3c0a49f29bc01b3b` | BUILD | Documentary forensics on the origin of `104c58e` (transcripts, ledgers, reflog) | returned; **verified independently by manager** |
| `ad4327f0a21f0e33d` | BUILD | Throwaway-repo experiments on a byte-identical COPY of `gate-commit.sh`: branch distinguishability, S9 arming control, command-shape sweep, token path | returned; spot-verified |
| `aaa33d93a70a36f12` | BUILD | LIVE trip tests against this session's REAL registered hooks: deny-isolation lever, masking, reach boundary, settings-scope control | returned; **reproduced first-hand by manager** |
| `a603b53ec1bda096a` | ADVERSARIAL | Handed the three claims as bare artifact, no producer reasoning. Instructed to falsify | returned; **weakened C2 and C3 wording — corrections folded in below** |

The adversarial worker was given the claims and the criteria only. It never saw
the BUILD workers' reasoning.

---

## 1. Verdict on (A) vs (B)

### **(B). Observed, not inferred.**

The deciding experiment is not a hook test — it is the pair of records that
bracket the commit. Both were re-derived first-hand by the manager, not accepted
from a worker summary.

**(i) The orchestrator DID attempt the park commit as a tool call, and was
DENIED, 13m16s before the commit that exists.**

`~/.claude/projects/**/089e9560-4424-403c-a098-81c955349e1e.jsonl`, line 231,
`2026-07-26T18:32:35.298Z`, `type=assistant`, content block `tool_use`:

```
  name= Bash
  input= {"command": "git commit -m \"park(Praxis_build-37h): audit-fail-x2, session ended per absolute park rule\n\nTwo audit FAILs on this bead. Not on main.\n\nFAIL 1 (S7, S4): flush staged 4 files; audit-log-flush-verify.sh\nrequires exactly AUDIT_LOG.md. Observed exit 1.\n\nFAIL 2 (S1, S2): the 18:10:37Z DECISION_LOG row claimed the bead\ndescription was corrected in place. It was not. bd show still returns\n'four DECISION_LOG rows' and still describes the abandoned\nsingle-commit shape. An out-of-diff completion claim.\n\nNo third dispatch. specs/SPEC_RUBRIC.md:263-267 forecloses the\n'mechanical defect' exemption. Bead 37h left uncorrected so the\nhuman who resumes sees the divergence the auditor found.\n\nP1, P2, P4 not started.\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>\" 2>&1 | tail -20", "description": "Commit parked work to park branch"}
```

Line 232, `2026-07-26T18:32:35.710Z`, `type=user`, content block `tool_result`,
`is_error= True`:

```
PreToolUse:Bash hook error: ["$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh]: Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
```

**(ii) The commit that exists was typed by a human into zsh.** Manager-run,
first-hand:

```
$ git log -1 --format="%at %ct %H" 104c58e
1785091551 1785091551 104c58eb46e41f0ab301ef2eed5bf97e11681ed2

$ awk 'NR>=1496 && NR<=1508 {print NR": "$0}' ~/.zsh_history
1496: : 1785091530:0;cd '..'
1497: : 1785091533:0;cd '..'
1498: : 1785091535:0;cd '..'
1499: : 1785091537:0;cd '..'
1500: : 1785091551:0;cd /Volumes/Sensidine/Praxis.build\
1501: git branch --show-current          # must say parked/Praxis_build-37h\
1502: git add HANDOFF.md\
1503: git status --short                 # .claude/settings.json must NOT be staged\
1504: git commit -m "park(Praxis_build-37h): audit-fail-x2, session ended per absolute park rule"\
1505: git checkout main                  # main stays at c1dec30
1506: : 1785091624:0;claude --dangerously-skip-permissions
```

The `EXTENDED_HISTORY` epoch on line 1500 is **`1785091551`**, which equals the
commit's `%at` and `%ct` **exactly**. Line 1506 shows a `claude` process started
73 seconds later — i.e. the commit was executed in an interactive shell, and a
Claude session was (re)started afterwards.

**(iii) The commit's own shape matches the human paste, not the agent's
attempt.** The denied tool call carried a long body and a `Co-Authored-By`
trailer. The commit on disk carries a subject line and an **empty** body. That
contrast — long body + trailer versus empty body — is the part that does the work.
The paragraph count is stated only because round 1 got it wrong; counted
mechanically off the transcript record itself, the message is **7 blank-line-separated
blocks** of which **5 are body paragraphs** (the other two being the subject and the
`Co-Authored-By` trailer). Round 1 said "seven-paragraph body", which double-counted
the subject and the trailer as body:

```
$ python3 <scratchpad>/f4/paras.py
commit-message source : transcript line 231, tool_input.command
blank-line-separated blocks, INCLUDING subject and Co-Authored-By trailer:
  block 1: 'park(Praxis_build-37h): audit-fail-x2, session ended per absolut'
  block 2: 'Two audit FAILs on this bead. Not on main.'
  block 3: 'FAIL 1 (S7, S4): flush staged 4 files; audit-log-flush-verify.sh'
  block 4: 'FAIL 2 (S1, S2): the 18:10:37Z DECISION_LOG row claimed the bead'
  block 5: "No third dispatch. specs/SPEC_RUBRIC.md:263-267 forecloses the\n'"
  block 6: 'P1, P2, P4 not started.'
  block 7: 'Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>'
total blocks                                : 7
blocks that are the subject line             : 1
blocks that are the Co-Authored-By trailer   : 1
BODY paragraphs (blocks minus subject minus trailer): 5
rc=0
```

The commit on disk:

```
$ git show --stat --format="%H%n%B" 104c58e | head -30
104c58eb46e41f0ab301ef2eed5bf97e11681ed2
park(Praxis_build-37h): audit-fail-x2, session ended per absolute park rule


 DECISION_LOG.md      |  8 ++++++++
 DISPATCH_LOG.md      |  7 +++++++
 HANDOFF.md           | 33 +++++++++++++++++++++++++++++++++
 MANIFEST.md          |  1 +
 specs/SPEC_RUBRIC.md | 16 ++++++++++++++++
 5 files changed, 65 insertions(+)
```

Five files, including `HANDOFF.md` — which is staged by `git add HANDOFF.md` at
zsh_history line 1502, a command the agent never issued.

**(iv) The positive artifact in the transcript.** Line 288,
`2026-07-26T18:46:02.192Z`, `type=user`, `message.content` a **plain string**
(not a `tool_use`, not a `tool_result`) — the human pasting his terminal
session back into the conversation:

```
cd /Volumes/Sensidine/Praxis.build
git branch --show-current          # must say parked/Praxis_build-37h
git add HANDOFF.md
git status --short                 # .claude/settings.json must NOT be staged
git commit -m "park(Praxis_build-37h): audit-fail-x2, session ended per absolute park rule"
git checkout main                  # main stays at c1dec30
parked/Praxis_build-37h
 M .claude/settings.json
 M AUDIT_LOG.md
M  DECISION_LOG.md
M  DISPATCH_LOG.md
M  HANDOFF.md
M  MANIFEST.md
M  specs/SPEC_RUBRIC.md
?? .claude/agent-memory/
?? docs/reports/2026-07-26-session34-manifest-amendment.md
?? docs/reports/2026-07-26-session34-p0-flush-audit.md
[parked/Praxis_build-37h 104c58e] park(Praxis_build-37h): audit-fail-x2, session ended per absolute park rule
 5 files changed, 65 insertions(+)
M    .claude/settings.json
M    AUDIT_LOG.md
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

The `5 files changed, 65 insertions(+)` in this paste matches `git show --stat`
byte-for-byte.

**(v) The (A)-shaped alternatives were hunted and came back empty.** Two of them,
labelled separately because they were closed by different parties at different times.

**(v-a) `--dangerously-skip-permissions` — the most obvious bypass hypothesis, and
round 1 never named it.** If that flag disarmed `PreToolUse` hooks, an agent tool call
could have made the commit and (B) would collapse. It does not, and the proof is that
*the very session `gate-commit.sh` denied was itself launched with the flag.*

Stated plainly about provenance: **this hole was closed by the round-1 AUDITOR, not by
the round-1 report.** The report asserted the alternatives "came back empty" without ever
naming this one. The evidence below was re-derived first-hand in the repair unit rather
than copied out of the audit.

The flagged launch, and a method note that matters:

```
$ LC_ALL=C awk 'NR==1494 {printf "%d\t%s\n", NR, $0}' ~/.zsh_history
1494	: 1785088326:0;claude --dangerously-skip-permissions
rc=0
```

A naive read returns **nothing at all** — `~/.zsh_history` contains bytes `grep` treats
as binary, so a reader who reruns the obvious form and gets silence must not conclude the
line is absent:

```
$ grep -n '' ~/.zsh_history > /tmp/naive.txt 2>&1
grep rc=1
$ wc -l < /tmp/naive.txt
       0
```

`LC_ALL=C awk` (above) reads it. Epoch → UTC, computed not estimated:

```
$ for e in 1785088326 1785095491; do printf "%s -> %s\n" "$e" "$(date -u -r $e +%Y-%m-%dT%H:%M:%SZ)"; done
1785088326 -> 2026-07-26T17:52:06Z
1785095491 -> 2026-07-26T19:51:31Z
rc=0
```

The denied session's transcript is `089e9560-4424-403c-a098-81c955349e1e.jsonl`. `head -1`
is **not** sufficient: records 1-3 are untimestamped session-header records
(`last-prompt`, `agent-setting`, `mode`), so the first *timestamped* record is line 6.

```
$ head -3 "$F" | python3 -c 'import sys,json
for i,l in enumerate(sys.stdin,1):
    r=json.loads(l); print(i,"type=",r.get("type"),"timestamp=",r.get("timestamp"))'
1 type= last-prompt timestamp= None
2 type= agent-setting timestamp= None
3 type= mode timestamp= None

$ python3 -c 'import json
f=".../089e9560-4424-403c-a098-81c955349e1e.jsonl"
for i,l in enumerate(open(f),1):
    r=json.loads(l)
    if r.get("timestamp"):
        print("line",i,"type",r.get("type"),"timestamp",r["timestamp"],"sessionId",r.get("sessionId")); break'
line 6 type attachment timestamp 2026-07-26T17:52:07.796Z sessionId 089e9560-4424-403c-a098-81c955349e1e
```

The gap is computed, not eyeballed:

```
$ python3 -c '
from datetime import datetime, timezone
epoch=1785088326
launch=datetime.fromtimestamp(epoch, tz=timezone.utc)
first=datetime.fromisoformat("2026-07-26T17:52:07.796Z".replace("Z","+00:00"))
print("zsh_history L1494 epoch :", epoch, "->", launch.isoformat().replace("+00:00","Z"))
print("transcript first ts     :", first.isoformat().replace("+00:00","Z"))
print("gap (seconds)           :", (first-launch).total_seconds())
prev=datetime.fromtimestamp(1785087105, tz=timezone.utc)
print("gap from L1493 (seconds):", (first-prev).total_seconds())'
zsh_history L1494 epoch : 1785088326 -> 2026-07-26T17:52:06Z
transcript first ts     : 2026-07-26T17:52:07.796Z
gap (seconds)           : 1.796
gap from L1493 (seconds): 1222.796
```

**1.796 s.** The nearest competing launch is 1222.796 s away — three orders of magnitude
worse. A 1.8 s gap only identifies the launch if nothing else started nearby, so the
window was swept: exactly **one** transcript in this project directory begins between
17:52:00Z and 18:40:00Z.

```
$ python3 (glob ~/.claude/projects/-Volumes-Sensidine-Praxis-build/*.jsonl, first record bearing a timestamp, sorted)
2026-07-26T17:20:58.437Z   f329ae39-bb7d-4dcd-8e10-5c4bdac973d8.jsonl
2026-07-26T17:23:47.052Z   247ddc7f-f2ba-49eb-a7a6-0793286417d8.jsonl
2026-07-26T17:28:53.126Z   9c7d716f-c187-44ec-9e1e-f8f78d0bf23c.jsonl
2026-07-26T17:29:57.440Z   ed9aabc8-fc4d-4139-bcc2-07221f6dc918.jsonl
2026-07-26T17:31:05.066Z   374c6f3d-b58f-46a3-9f29-e5352f7e83dd.jsonl
2026-07-26T17:52:07.796Z   089e9560-4424-403c-a098-81c955349e1e.jsonl
2026-07-26T18:47:05.675Z   188b62c3-51e2-40e3-9dc1-586332ee3a18.jsonl

--- sessions whose first record falls in 2026-07-26T17:52:00Z..18:40:00Z ---
2026-07-26T17:52:07.796Z   089e9560-4424-403c-a098-81c955349e1e.jsonl
count in window: 1
```

The launch→transcript offset is stable and 1:1 across the whole afternoon, which is what
licenses reading a ~1.8 s gap as an identity rather than a coincidence:

| zsh_history | epoch → UTC | transcript first record | gap |
|---|---|---|---|
| L1491 `claude -p …` | 1785086996 → 17:29:56Z | `ed9aabc8…` 17:29:57.440Z | 1.44 s |
| L1492 `claude` | 1785087064 → 17:31:04Z | `374c6f3d…` 17:31:05.066Z | 1.07 s |
| L1493 `claude -r --dangerously-skip-permissions` | 1785087105 → 17:31:45Z | (resume — correctly creates no new file) | — |
| **L1494 `claude --dangerously-skip-permissions`** | **1785088326 → 17:52:06Z** | **`089e9560…` 17:52:07.796Z** | **1.80 s** |
| L1506 `claude --dangerously-skip-permissions` | 1785091624 → 18:47:04Z | `188b62c3…` 18:47:05.675Z | 1.68 s |

And that same file carries the deny, with the `sessionId` on both records and a
`tool_use_id` linking attempt to refusal — so this is one call, not two adjacent records:

```
$ python3 -c '
import json
f=".../089e9560-4424-403c-a098-81c955349e1e.jsonl"
for i,l in enumerate(open(f),1):
    if i in (231,232):
        r=json.loads(l)
        print("line",i,"| type",r.get("type"),"| timestamp",r.get("timestamp"),"| sessionId",r.get("sessionId"))
        for b in (r["message"]["content"] if isinstance(r["message"]["content"],list) else []):
            if b.get("type")=="tool_result":
                print("   is_error:",b.get("is_error")); print("   content:",str(b.get("content"))[:300])'
line 231 | type assistant | timestamp 2026-07-26T18:32:35.298Z | sessionId 089e9560-4424-403c-a098-81c955349e1e
line 232 | type user | timestamp 2026-07-26T18:32:35.710Z | sessionId 089e9560-4424-403c-a098-81c955349e1e
   is_error: True
   content: PreToolUse:Bash hook error: ["$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh]: Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
```

The `tool_use_id` is `toolu_01VH9uR3gh3LQHccqFon8MMz` on both the `tool_use` at line 231
and its `tool_result` at line 232.

**Conclusion, capped exactly:** *the session denied at 18:32:35Z was itself launched with
`--dangerously-skip-permissions`, therefore that flag does not disarm `gate-commit.sh`.*
It is **not** a finding that the flag disarms no hooks, nor that the flag does nothing.
Neither was tested.

**(v-b) The hook-script backdoor.** The
adversarial worker's highest-value attack was the *hook-script backdoor*: a
script invoked BY a hook is an ordinary child process and is not itself gated,
so a `Stop` / `SubagentStop` / `PreCompact` / `SessionStart` hook that commits
internally would falsify (B) without needing a human.

**Round 1 and the round-1 repair both stated the six facts below in prose with no
pasted output at all.** Each is now re-run first-hand with its transcript. Two of
them came back **narrower than they were stated**, and are corrected here rather
than repeated.

*Fact 1 — the registered hook set, read out of `.claude/settings.json` rather than
assumed.* SOURCE-READ:

```
$ python3 -c '
import json
s=json.load(open(".claude/settings.json"))
for ev,arr in s.get("hooks",{}).items():
    for entry in arr:
        for hk in entry.get("hooks",[]):
            print("%-16s matcher=%-24s command=%s" % (ev, entry.get("matcher",""), hk.get("command","")))
'
PreCompact       matcher=                         command=bd prime
PreCompact       matcher=                         command="$CLAUDE_PROJECT_DIR"/.claude/hooks/precompact-handoff.sh
SessionStart     matcher=                         command=bd prime
SessionStart     matcher=compact|clear            command="$CLAUDE_PROJECT_DIR"/.claude/hooks/inject-handoff.sh
PreToolUse       matcher=Bash                     command="$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh
PreToolUse       matcher=Bash                     command="$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh
PreToolUse       matcher=Write|Edit|NotebookEdit  command="$CLAUDE_PROJECT_DIR"/scripts/master-write-guard.sh
PreToolUse       matcher=Bash                     command="$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh
PreToolUse       matcher=Agent                    command="$CLAUDE_PROJECT_DIR"/scripts/agent-spawn-guard.sh
Stop             matcher=                         command="$CLAUDE_PROJECT_DIR"/.claude/hooks/stop-gate.sh
SubagentStart    matcher=                         command=./scripts/dispatch-log-writeahead.sh
SubagentStop     matcher=^praxis-manager$         command=./scripts/gate-manager-output.sh
rc=0
```

*Fact 2 — CORRECTED. "Every `git` call in the registered hooks is read-only" is
imprecise.* SOURCE-READ, exhaustive over the ten registered hook scripts — every
line containing the string `git`, comment-only lines excluded, so the reader can
see the whole match set and not a filtered one:

```
$ /usr/bin/grep -n 'git' scripts/no-commit-guard.sh scripts/master-write-guard.sh \
    scripts/master-bash-guard.sh scripts/agent-spawn-guard.sh \
    scripts/dispatch-log-writeahead.sh scripts/gate-manager-output.sh \
    .claude/hooks/precompact-handoff.sh .claude/hooks/inject-handoff.sh \
    .claude/hooks/gate-commit.sh .claude/hooks/stop-gate.sh \
  | /usr/bin/grep -vE ':[0-9]+:[[:space:]]*#'
scripts/no-commit-guard.sh:20:if echo "$CMD" | grep -qE '\bgit\s+(commit|push|merge|rebase|tag)\b'; then
scripts/dispatch-log-writeahead.sh:9:echo "- [$TS] WHO: $AGENT | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session $(git -C "${CLAUDE_PROJECT_DIR:-.}" rev-parse --short HEAD 2>/dev/null || echo no-git) | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched" >> "$LOG"
.claude/hooks/gate-commit.sh:31:  *git*commit*) ;;   # cheap pre-filter only; precise command-position check below
.claude/hooks/gate-commit.sh:51:GITCOMMIT="${BINPRE}"'git[[:space:]]+([^;&|`]*[[:space:]])?commit([[:space:];&|)`]|$)'
.claude/hooks/gate-commit.sh:65:  echo "Commit exactly the staged diff with a plain \`git commit -m \"...\"\` — no -a/--all/--include/--amend, no pathspec after ' -- ', and run it as the sole command in its own Bash call." >&2
.claude/hooks/gate-commit.sh:79:if printf '%s' "$CMD" | grep -Eq 'git[[:space:]]+add'; then
.claude/hooks/gate-commit.sh:80:  echo "Commit denied: one git commit per Bash call — stage in a separate call first." >&2
.claude/hooks/gate-commit.sh:83:if [ "$(printf '%s' "$CMD" | grep -oE 'git[[:space:]]+commit' | wc -l | tr -d ' ')" -gt 1 ]; then
.claude/hooks/gate-commit.sh:84:  echo "Commit denied: one git commit per Bash call — stage in a separate call first." >&2
.claude/hooks/gate-commit.sh:94:  echo "Single-session rule: exactly ONE Claude session per repo working tree (docs/runbooks/2026-07-10-single-session-rule.md). Close the other session (or move it to its own git worktree) and re-run the commit." >&2
.claude/hooks/gate-commit.sh:144:  deny_session "another live claude session (pid$FOREIGN) has its cwd inside this repo — it can pollute the shared .git/index between audit and commit (2026-07-10 incident)"
.claude/hooks/gate-commit.sh:152:HASH=$(cd "$ROOT" && git diff --cached | shasum -a 256 | awk '{print $1}')
.claude/hooks/gate-commit.sh:170:  NOW_TREE=$(cd "$ROOT" && git write-tree 2>/dev/null)
rc=0
```

Exactly **three** of those lines start a `git` process: `git -C … rev-parse --short
HEAD`, `git diff --cached` (line 152) and `git write-tree` (line 170). The rest are
string literals in deny messages or grep patterns. **"Read-only" is the wrong word
for `git write-tree`** — it writes tree objects into the object database. The claim
that survives is narrower and is the one the argument actually needs: *no `git`
invocation in any registered hook creates a commit or moves a ref.* Corrected, not
dropped. Caveat on method: this is a `grep` for the literal string `git`, so it
cannot exclude a commit reached through a variable, an alias, or a `PATH` shadow;
it is corroboration, not a proof of impossibility.

*Fact 3 — `scripts/test-gate-hardening.sh` is NOT registered, and its git writes
target a scratch repo.* SOURCE-READ. `rc=1` from `grep` over `.claude/settings.json`
**is** the evidence of non-registration — the file name occurs nowhere in it:

```
$ /usr/bin/grep -n 'test-gate-hardening' .claude/settings.json; echo "rc=$?"
rc=1

$ /usr/bin/grep -nE 'git (commit|add|init)|^SCRATCH=|^SREPO=|/tmp' scripts/test-gate-hardening.sh | head -8
15:SCRATCH="${1:-${TMPDIR:-/tmp}/v6y-gate-test}"
17:JSON='{"tool_input":{"command":"git commit -m \"test\""}}'
28:    && git init -q \
30:    && echo base > base.txt && git add base.txt \
31:    && git commit -qm "base" )
57:( cd "$SREPO" && echo a1 > a.txt && git add a.txt )
64:( cd "$SREPO" && git commit -qm "gated commit" )
76:( cd "$SREPO" && git commit -qm "gated commit" )
rc=0
```

Every write is inside `$SREPO`, which descends from `SCRATCH` at line 15, defaulting
to `${TMPDIR:-/tmp}/v6y-gate-test`.

*Fact 4 — `.git/hooks/` contains only `.sample` files.* The `rc=1` on the second
command is the evidence of absence; the listing alone would not be:

```
$ ls -1 .git/hooks
applypatch-msg.sample
commit-msg.sample
fsmonitor-watchman.sample
post-update.sample
pre-applypatch.sample
pre-commit.sample
pre-merge-commit.sample
pre-push.sample
pre-rebase.sample
pre-receive.sample
prepare-commit-msg.sample
push-to-checkout.sample
update.sample
rc=0
$ ls -1 .git/hooks | /usr/bin/grep -v '\.sample$'; echo "rc=$?"
rc=1
```

*Fact 5 — CORRECTED. The transcript count is 579, not 566, and "exactly one
`tool_use` bearing the commit" is now four records, of which exactly one is a commit
attempt.* The 566 figure was round 1's and is not re-derivable: the transcript
directory grows continuously, and this very investigation adds to it. Measured
first-hand:

```
$ python3 <scratchpad>/f4/scan2.py
transcript files scanned          : 579
unparseable json lines            : 0

ALL tool_use records whose tool_input.command contains the park subject:
  timestamp                 file / line                                   git-commit-shape?  command head
  2026-07-26T18:32:35.298Z  089e9560-4424-403c-a098-81c955349e1e.jsonl L231   True               git commit -m "park(Praxis_build-37h): audit-fail-x2, session ended pe
  2026-07-26T20:43:07.911Z  agent-af313af079be5a8e3.jsonl L37    False              cat > /tmp/advA/findings.md <<'ADVEOF'\n# ADVERSARIAL grade — S1 (SPEC_
  2026-07-26T20:51:55.234Z  agent-a33e32145708867f5.jsonl L31    False              mkdir -p /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/188b6
  2026-07-26T20:52:19.588Z  agent-a33e32145708867f5.jsonl L37    False              cat > /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/188b62c3
  total records: 4
  of which git-commit-shaped: 1
  of which timestamped at or before 2026-07-26T18:46:00Z: 1
rc=0
```

Read that table honestly. Four records now quote the park subject; **one** of them
is a `git commit` invocation, and it is the denied one at 18:32:35Z. The other
three are 20:43Z–20:52Z investigation commands — an adversarial grader writing its
findings file, and this repair unit writing the very scan script that produced the
table. **Like the `DISPATCH_LOG` row count in "Files staged", this quantity is not
stable and any report quoting it must timestamp the observation.** The load-bearing
statement, which is stable, is: *no `git commit` tool call other than the denied one
at 18:32:35Z exists in any transcript on this machine.*

*Fact 6 — zero Bash `tool_use` records between 18:41:00Z and 18:46:00Z.* The window
is not merely empty of Bash calls; it is empty of `tool_use` blocks of any tool, and
the five records that do fall inside it are named:

```
$ python3 <scratchpad>/f4/window.py
files scanned: 579
window       : 2026-07-26T18:41:00Z .. 2026-07-26T18:46:00Z
records of ANY type timestamped inside the window: 5
    ('2026-07-26T18:41:06.735Z', '089e9560-4424-403c-a098-81c955349e1e.jsonl', 283, 'assistant')
    ('2026-07-26T18:41:07.186Z', '089e9560-4424-403c-a098-81c955349e1e.jsonl', 284, 'attachment')
    ('2026-07-26T18:41:07.187Z', '089e9560-4424-403c-a098-81c955349e1e.jsonl', 285, 'system')
    ('2026-07-26T18:41:07.189Z', '089e9560-4424-403c-a098-81c955349e1e.jsonl', 286, 'system')
    ('2026-07-26T18:44:16.319Z', '089e9560-4424-403c-a098-81c955349e1e.jsonl', 287, 'system')
tool_use blocks of ANY tool inside the window: 0
Bash tool_use blocks inside the window       : 0
rc=0
```

Per §6 item 8 this is an **absence of evidence**: it corroborates (B), it does not
carry it.

**(vi) A fourth artifact, and it is INSIDE the repo.** The verdict above leans on
`~/.zsh_history`, which §6 item 9 correctly flags as not tamper-evident. There is an
artifact that carries the same claim and is under version control — committed inside
`104c58e` itself. Manager-verified first-hand:

```
$ git show 104c58e:HANDOFF.md | sed -n '5p'
**⚠️ FIRST ACTION, BEFORE ANYTHING ELSE — the parked work is fragile.** `DECISION_LOG.md`, `DISPATCH_LOG.md`, `MANIFEST.md`, `specs/SPEC_RUBRIC.md` are staged on the park branch and will be destroyed by a careless `git checkout` / `git reset`. **Amear commits it by hand in his own terminal** — `gate-commit.sh` is a Claude Code PreToolUse hook and does NOT bind a human shell:
rc=0
```

**What this line is, stated exactly.** `HANDOFF.md:5` was written **before** the commit it
describes — it is part of the tree that `104c58e` records. It is therefore in-repo evidence
of **intent and instruction**: it shows that the mechanism (human executor, hook does not
bind a human shell) was the *planned* mechanism, written down by the session that set the
stage. It **corroborates** the mechanism. It does **not witness the act**. A plan committed
alongside an outcome is not an observation of the outcome, and this report does not treat it
as one.

Consequently the earlier framing of this paragraph is **withdrawn**: the phrase "four
mutually independent artifacts converge" over-claimed on two counts, and the claim that the
(B) verdict "no longer depends on any file outside version control" is also withdrawn — it
still does. What the four artifacts actually are:

| Artifact | What it is | Independent of? |
|---|---|---|
| Denied `tool_use`/`tool_result` pair | Direct observation: the agent attempt was blocked | Independent of the other three |
| Plain-string paste at 18:46:02Z (transcript) | Observation of a terminal block pasted into the session | **Same terminal session** as the `zsh_history` entry |
| `~/.zsh_history` epoch match | Observation of a shell-history line | **Same terminal session** as the pasted block |
| `HANDOFF.md:5`, in-repo | Pre-written instruction — intent, not act | Independent in *location*, but evidentially weaker in kind |

So: **not four independent witnesses.** Two of them (the 18:46:02Z pasted block and the
`~/.zsh_history` epoch) originate in the *same terminal session* and are therefore not
independent of one another — a single tampered or mis-attributed session would move both.
The third is a plan, not an observation. Only the denial is a first-class independent
observation, and it establishes what did *not* happen (the agent did not commit), not who
did. §6 item 9's caveat stays live in full force: `~/.zsh_history` is not tamper-evident,
so authorship of `104c58e` remains **corroborated, never proven**.

The wrinkle, recorded rather than smoothed over: the same `HANDOFF.md` says the work is
`STAGED BUT UNCOMMITTED`, which was true when written and was made false by the human
commit that carried it.

```
$ git show 104c58e:HANDOFF.md | grep -n 'STAGED BUT UNCOMMITTED'
3:**HEAD:** `main` unmoved at `c1dec30`. Repo is left **on branch `parked/Praxis_build-37h`** with work **STAGED BUT UNCOMMITTED**. Read the two ⚠️ items below before running any git command.
grep rc=0
```

That is not a contradiction. It is the handoff instruction and its own execution captured
in a single git object: line 3 describes the state at the moment of writing, line 5 names
the human who was about to change it.

### What this means for the bead, stated without ranking

The two rules do not collide inside the gate. They collide at the **executor
boundary**: the park rule's step 1 issues an instruction to the orchestrator
that the orchestrator is structurally incapable of carrying out, because the
commit is by construction un-audited and the gate that stops it is the gate
working as designed. Session 34 did not fail to park — it parked **by handing
the commit to a human**, which is not written down anywhere in the rule.

8sw's factual claim *"Work left STAGED BUT UNCOMMITTED"* is **FALSIFIED**.

**S1/S2 defect found in passing, and it is inside the park commit itself.**
The `DECISION_LOG.md` 18:32:04Z row committed in `104c58e` asserts *"Work
committed to branch `parked/Praxis_build-37h`"*. It was written **31 seconds
before** the denial at 18:32:35Z, and was **false at the moment it was written**.
No ledger in this repo records who actually ran the commit; only the transcript
and `~/.zsh_history` do — and both are outside the repo.

---

## 2. Verification evidence — trip-test transcripts (S3)

Every claim in this section carries the transcript that produced it, with the
command and its exit code. Where a result is recovered from a stored artifact
rather than re-run, the block is labelled `RECOVERED` with its path.
(Round 1 carried "Pasted command output only. Nothing in this section is a
description of output" at this position while §2.3 below it contained no
output at all. See "Round-1 audit corrections".)

### 2.1 Manager first-hand — live deny, real registered hook

Isolation lever: `no-commit-guard.sh` matches `\bgit\s+(commit|push|…)\b`, which
`git -C <dir> commit` **misses** (the `-C <dir>` sits between), while
`gate-commit.sh`'s looser `git[[:space:]]+([^;&|`]*[[:space:]])?commit`
**matches**. This isolates gate-commit as the sole denier and defuses the
parallel-deny masking trap. The lever was confirmed by worker
`aaa33d93a70a36f12`, which additionally isolated `no-commit-guard.sh` with a
`push`-shaped command and **observed it fire separately**
(`BLOCKED: subagents leave work staged.`).

Setup (scratchpad throwaway, on a branch named exactly like the park branch):

```
$ git init -q . && git config user.email m@x && git config user.name m
$ echo hello > f.txt && git add f.txt
$ git checkout -q -b parked/Praxis_build-37h
$ git branch --show-current
parked/Praxis_build-37h
SETUP OK
```

Trip:

```
$ git -C <scratchpad>/mgr-trip commit -m "manager first-hand trip test"; echo "shell-exit=$?"
PreToolUse:Bash hook error: ["$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh]: Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
```

The tool call was blocked before execution, so no shell exit code was produced —
the harness returned the hook error in its place. **The harness names the
producing hook in brackets**, which is what makes this attributable rather than
inferred. Note the gate denied a commit aimed at `/tmp`: it resolves
`ROOT=$CLAUDE_PROJECT_DIR`, hashed the **real** repo's staged diff, and denied.
Fail-closed for the armed repo, exactly as its header comment claims.

**Being on a `parked/*` branch changed nothing.** See §4.

### 2.2 Manager first-hand — the reach boundary

A script whose own path contains neither `git` nor `commit`, invoked directly
(no `bash` prefix), commits with no hook interaction:

```
$ chmod +x <scratchpad>/mgr-trip/do.sh && <scratchpad>/mgr-trip/do.sh; echo "outer-exit=$?"
[parked/Praxis_build-37h (root-commit) 02b9280] indirection reach probe
 1 file changed, 1 insertion(+)
 create mode 100644 f.txt
inner-exit=0
outer-exit=0

$ git -C <scratchpad>/mgr-trip log --oneline --all
02b9280 indirection reach probe
```

**Stated precisely:** both guards inspect `tool_input.command` and never
introspect what that command executes. This is evidence about the **gate's reach
surface**. It is *not* a matcher weakness — the matcher was never handed the
text — and it is *not*, on its own, a proof about human terminals.

### 2.3 Copy-driven sweep (worker `ad4327f0a21f0e33d`, re-run fresh in the repair unit)

**Scope cap that governs every block in §2.3 (S2).** Each cell invokes a *copy* of the
hook directly, with a synthetic `PreToolUse` payload on stdin and `CLAUDE_PROJECT_DIR`
pointed at a throwaway harness root. What is proven is exactly: **the script exited with
code N and wrote this stderr, given that payload and that on-disk state.** None of it
proves Claude Code blocked a tool call. Harness root `/tmp/praxis-s35-repair/root`; copy
under test `/tmp/praxis-s35-repair/hookcopy.sh`.

#### 2.3(a) The copy is byte-identical to the live hook

**Two separate copies exist, and each was proven identical to the live hook independently.**
Naming them, because the two fences below are about *different files* and round 1 left that
implicit:

| Copy | Provenance | What it drove |
|---|---|---|
| `/tmp/praxis-s35-adv/gate-commit.copy.sh` | **RECOVERED** from the earlier adversarial worker's harness directory `/tmp/praxis-s35-adv/` — not created by the repair unit | The §4 sweep (`a4_driver.sh`) and the §3.1.6 malformed-payload work |
| `/tmp/praxis-s35-repair/hookcopy.sh` | Built fresh by the repair unit's `setup.sh` | **Every cell of §2.3(b)/(c)/(d), §3.2 and §3.3** |

Both carry the same `sha256`, `b3de1137…c330ef`, which is also the live hook's — so the
logic results transfer from either. The fence immediately below is the **RECOVERED** one,
labelled as such per this section's own convention; the second fence is the copy actually
under test for §2.3.

**RECOVERED — `/tmp/praxis-s35-adv/gate-commit.copy.sh`:**

```
$ shasum -a 256 /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh /tmp/praxis-s35-adv/gate-commit.copy.sh
b3de1137bff3b05a259d11b65eedd69681823626d290d68916e144fef3c330ef  /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
b3de1137bff3b05a259d11b65eedd69681823626d290d68916e144fef3c330ef  /tmp/praxis-s35-adv/gate-commit.copy.sh
rc=0
$ cmp /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh /tmp/praxis-s35-adv/gate-commit.copy.sh
rc=0
```

The harness copy used for every cell below was made from that file and re-hashed at
harness-build time:

```
$ bash /tmp/praxis-s35-repair/setup.sh
--- sha256 of harness copy vs live hook ---
b3de1137bff3b05a259d11b65eedd69681823626d290d68916e144fef3c330ef  /tmp/praxis-s35-repair/hookcopy.sh
b3de1137bff3b05a259d11b65eedd69681823626d290d68916e144fef3c330ef  /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
rc=0
--- harness tree ---
/tmp/praxis-s35-repair/root
/tmp/praxis-s35-repair/root/.claude
/tmp/praxis-s35-repair/root/.claude/state
/tmp/praxis-s35-repair/root/AUDIT_LOG.md
/tmp/praxis-s35-repair/root/seed.txt
rc=0
```

#### 2.3(b) Armed, no token: eight command shapes, each exit 2

Precondition held constant for all eight: arming marker present, **no** `audit-pass-*`
token on disk. Driver `/tmp/praxis-s35-repair/drv_b.sh`.

```
$ bash /tmp/praxis-s35-repair/drv_b.sh
### arming state
orchestrator-active
rc=0
```

**b1 — `git commit -m "x"`**

```
--- payload (stdin) ---
{"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"x\"", "description": "harness"}}
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh  >/tmp/praxis-s35-repair/out/b1.out 2>/tmp/praxis-s35-repair/out/b1.err
rc=2
--- stderr ---
Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
--- stderr byte count ---
     214
rc=0
```

**b2 — `git -C <dir> commit`**

```
--- payload (stdin) ---
{"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git -C /tmp/praxis-s35-repair/root commit", "description": "harness"}}
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh  >/tmp/praxis-s35-repair/out/b2.out 2>/tmp/praxis-s35-repair/out/b2.err
rc=2
--- stderr ---
Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
--- stderr byte count ---
     214
rc=0
```

**b3 — `git --work-tree=… --git-dir=… commit`**

```
--- payload (stdin) ---
{"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git --work-tree=/tmp/praxis-s35-repair/root --git-dir=/tmp/praxis-s35-repair/root/.git commit -m \"x\"", "description": "harness"}}
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh  >/tmp/praxis-s35-repair/out/b3.out 2>/tmp/praxis-s35-repair/out/b3.err
rc=2
--- stderr ---
Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
--- stderr byte count ---
     214
rc=0
```

**b4 — `git checkout -b parked/foo && git commit`**

```
--- payload (stdin) ---
{"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git checkout -b parked/foo && git commit -m \"x\"", "description": "harness"}}
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh  >/tmp/praxis-s35-repair/out/b4.out 2>/tmp/praxis-s35-repair/out/b4.err
rc=2
--- stderr ---
Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
--- stderr byte count ---
     214
rc=0
```

**b5 — `git commit --no-verify`**

```
--- payload (stdin) ---
{"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit --no-verify -m \"x\"", "description": "harness"}}
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh  >/tmp/praxis-s35-repair/out/b5.out 2>/tmp/praxis-s35-repair/out/b5.err
rc=2
--- stderr ---
Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
--- stderr byte count ---
     214
rc=0
```

**b6 — `VAR=x git commit`**

```
--- payload (stdin) ---
{"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "VAR=x git commit -m \"x\"", "description": "harness"}}
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh  >/tmp/praxis-s35-repair/out/b6.out 2>/tmp/praxis-s35-repair/out/b6.err
rc=2
--- stderr ---
Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
--- stderr byte count ---
     214
rc=0
```

**b7 — `/usr/bin/git commit`**

```
--- payload (stdin) ---
{"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "/usr/bin/git commit -m \"x\"", "description": "harness"}}
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh  >/tmp/praxis-s35-repair/out/b7.out 2>/tmp/praxis-s35-repair/out/b7.err
rc=2
--- stderr ---
Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
--- stderr byte count ---
     214
rc=0
```

**b8 — `bash -c 'git commit -m x'`**

```
--- payload (stdin) ---
{"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "bash -c 'git commit -m x'", "description": "harness"}}
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh  >/tmp/praxis-s35-repair/out/b8.out 2>/tmp/praxis-s35-repair/out/b8.err
rc=2
--- stderr ---
Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
--- stderr byte count ---
     214
rc=0
```

**Observed: 8 / 8 shapes exited 2 with the identical 214-byte token-denial stderr.**
Which internal branch each shape took — form matcher vs. nested-shell matcher — is **not**
established by these transcripts. Only the exit code and the stderr are. That distinction
is a source-reading inference and is deliberately not asserted as observed fact.

#### 2.3(c) `git commit -am "x"` denies with the FORM message, not the token message

Same harness state; one character of payload difference (`-m` → `-am`) changes the message.
Driver `/tmp/praxis-s35-repair/drv_c.sh`. This is the one 2.3(b)-family cell where the
internal branch *is* observable, because the differing stderr text is itself the
observation.

```
$ cat /tmp/praxis-s35-repair/out/c1.err   # payload command: git commit -am "x"
Commit denied: a '-a'-style short flag sweeps unstaged working-tree changes into the commit
Commit exactly the staged diff with a plain `git commit -m "..."` — no -a/--all/--include/--amend, no pathspec after ' -- ', and run it as the sole command in its own Bash call.
rc=0

$ cat /tmp/praxis-s35-repair/out/b1.err   # payload command: git commit -m "x"
Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
rc=0

$ diff /tmp/praxis-s35-repair/out/c1.err /tmp/praxis-s35-repair/out/b1.err
1,2c1
< Commit denied: a '-a'-style short flag sweeps unstaged working-tree changes into the commit
< Commit exactly the staged diff with a plain `git commit -m "..."` — no -a/--all/--include/--amend, no pathspec after ' -- ', and run it as the sole command in its own Bash call.
---
> Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
rc=1

$ cmp /tmp/praxis-s35-repair/out/c1.err /tmp/praxis-s35-repair/out/b1.err
/tmp/praxis-s35-repair/out/c1.err /tmp/praxis-s35-repair/out/b1.err differ: char 16, line 1
rc=1

$ head -c 60 /tmp/praxis-s35-repair/out/c1.err ; echo ; head -c 60 /tmp/praxis-s35-repair/out/b1.err
Commit denied: a '-a'-style short flag sweeps unstaged worki
Commit denied: no audit PASS token for this exact staged dif
rc=0
```

The `-am` cell exits 2 as well, and its stderr is 272 bytes rather than 214:

```
=== SHAPE: c1
--- payload (stdin) ---
{"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -am \"x\"", "description": "harness"}}
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh  >/tmp/praxis-s35-repair/out/c1.out 2>/tmp/praxis-s35-repair/out/c1.err
rc=2
--- stderr ---
Commit denied: a '-a'-style short flag sweeps unstaged working-tree changes into the commit
Commit exactly the staged diff with a plain `git commit -m "..."` — no -a/--all/--include/--amend, no pathspec after ' -- ', and run it as the sole command in its own Bash call.
--- stderr byte count ---
     272
rc=0
```

#### 2.3(d) Token path — tripped, not read. Four cells.

The fake `ROOT` carries `.claude/state/orchestrator-active`, a fake `AUDIT_LOG.md`, and a
fake token at `.claude/state/audit-pass-<sha256-of-staged-diff>`. Driver
`/tmp/praxis-s35-repair/drv_d.sh`. One payload is reused across all four cells, so the only
variable is token/ledger state.

```
$ bash /tmp/praxis-s35-repair/drv_d.sh
### harness facts
staged-diff sha256 HASH = a8c4eaa4532c47057b66a5751a6c84589685e071fc33650ae2958b1f836b95c7
git write-tree      TREE = 94a764e4f3d7b835de19974269756e7c738d58b3
token path              = /tmp/praxis-s35-repair/root/.claude/state/audit-pass-a8c4eaa4532c47057b66a5751a6c84589685e071fc33650ae2958b1f836b95c7
rc=0
--- staged set ---
A	work.txt
rc=0

### payload used for ALL four cells (stdin)
{"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"harness\"", "description": "harness"}}
```

**d1 — token present, no `<hash> PASS` row in `AUDIT_LOG.md` → exit 2**

```
=== CELL d1: token present, no "<hash> PASS" row in AUDIT_LOG.md -> expect DENY
--- AUDIT_LOG.md content ---
# AUDIT_LOG (fake harness)
--- grep for the hash in AUDIT_LOG.md ---
0
grep rc=1
--- token content ---
tree=94a764e4f3d7b835de19974269756e7c738d58b3
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh 2>/tmp/praxis-s35-repair/out/d1.err
rc=2
--- stderr ---
Commit denied: token has no AUDIT_LOG PASS row — forged or corrupted; re-dispatch the orchestrator-auditor.
--- stderr bytes ---
     110
--- token still on disk after the call? ---
0
(count of audit-pass-* files) rc=1
```

The token count is `0` after the call — the script removed the token in this branch.

**d2 — PASS row present, token missing its `tree=` line → exit 2, message reads
`minted tree=missing/legacy-token`**

The PASS row **is** present here (grep count 1), so the failure is isolated to the missing
`tree=` line.

```
=== CELL d2: PASS row present, token has NO tree= line -> expect DENY, minted tree=missing/legacy-token
--- AUDIT_LOG.md content ---
# AUDIT_LOG (fake harness)
2026-07-26T00:00:00Z harness-bead a8c4eaa4532c47057b66a5751a6c84589685e071fc33650ae2958b1f836b95c7 PASS
--- grep for the hash in AUDIT_LOG.md ---
1
grep rc=0
--- token content ---
legacy token body with no tree line
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh 2>/tmp/praxis-s35-repair/out/d2.err
rc=2
--- stderr ---
Commit denied: staged tree no longer matches the tree the audit token was minted against (minted tree=missing/legacy-token, current tree=94a764e4f3d7b835de19974269756e7c738d58b3). Something changed the index after mint — re-stage exactly the audited set and re-dispatch the orchestrator-auditor.
--- stderr bytes ---
     298
--- token still on disk after the call? ---
0
(count of audit-pass-* files) rc=1
```

The literal substring `minted tree=missing/legacy-token` is present in that stderr.

**d3 — matching hash + PASS row + matching `tree=` → exit 0 (ALLOW)**

```
=== CELL d3: matching hash + PASS row + matching tree= -> expect ALLOW (exit 0)
--- AUDIT_LOG.md content ---
# AUDIT_LOG (fake harness)
2026-07-26T00:00:00Z harness-bead a8c4eaa4532c47057b66a5751a6c84589685e071fc33650ae2958b1f836b95c7 PASS
--- token content ---
tree=94a764e4f3d7b835de19974269756e7c738d58b3
--- current git write-tree ---
94a764e4f3d7b835de19974269756e7c738d58b3
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh 2>/tmp/praxis-s35-repair/out/d3.err
rc=0
--- stderr ---
--- stderr bytes ---
       0
--- token still on disk after the call? ---
0
(count of audit-pass-* files) rc=1
```

Exit 0, stderr proven empty by `wc -c` = 0 rather than by absence of visible text, and the
token file is gone — consumed at allow time.

**d4 — immediate replay of the same token → exit 2 (single-use consumption)**

Nothing changed between d3 and d4: same payload, same staged set, same PASS row. Only the
token is gone, because d3 consumed it.

```
=== CELL d4: immediate REPLAY of the same call, token not re-minted -> expect DENY (single-use consumed)
--- .claude/state listing before the replay ---
orchestrator-active
rc=0
--- AUDIT_LOG.md unchanged, still carries the PASS row ---
# AUDIT_LOG (fake harness)
2026-07-26T00:00:00Z harness-bead a8c4eaa4532c47057b66a5751a6c84589685e071fc33650ae2958b1f836b95c7 PASS
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh 2>/tmp/praxis-s35-repair/out/d4.err
rc=2
--- stderr ---
Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
--- stderr bytes ---
     214
--- token still on disk after the call? ---
0
(count of audit-pass-* files) rc=1
```

The `ls -1 .claude/state` before the replay shows only `orchestrator-active` — the token is
verifiably absent, not merely rejected. Single-use consumption is therefore observed, not
assumed.

**Harness-construction defect, disclosed rather than buried (S1).** The first run of the
d-driver wrote the fake PASS row as `| <hash> | PASS |`, and all three PASS-dependent cells
took the "no AUDIT_LOG PASS row" branch. That was a defect in the *fake ledger*, not in the
hook: the real rows are `<ts> <bead> <hash> PASS`, so the literal `<hash> PASS` substring
the script greps for was absent from the fake. It was verified against the live ledger, and
the driver was then corrected and re-run.

```
$ grep -n "PASS" /Volumes/Sensidine/Praxis.build/AUDIT_LOG.md | head -3
1:2026-07-08T15:12:20Z verify-0 8bcf117c4625653394c3b034c46361cb431489f6ad7816a8466888624c33a1dc PASS
2:2026-07-08T15:20:40Z setup-scaffold-2026-07-08 7225f081d29ea9f7c20da7522cca2e28f5e93e7432bbc7386996f276f9acfc1b PASS
3:2026-07-08T15:25:00Z Praxis_build-8jq f7f2bf9e918d9a45fcf0890957b1420952a1ccd0471c7972b357d9abaed7716f PASS
rc=0
```

A harness that silently produces the expected answer for the wrong reason is the single
most dangerous artifact in this kind of work. The near-miss is recorded because it was
caught by checking the instrument against the real thing.

Armed, no token, exits **0** on a family of shapes — see §3.3.

### 2.4 Manager's independent re-run, repair unit (S3 + S9, first-hand)

Built by the manager without reusing any worker driver — a separate harness, separately
written. Two harnesses arriving at the same bytes is a stronger result than one harness run
twice.

**Which hook each half ran against, stated correctly (S2).** Round 1 said this subsection ran
"against the same live hook"; that is wrong for the S9 cells and is corrected here. The
S9/discriminator cells below invoke a **copy** — that is what the block's own `copy sha256`
line reports — so every one of their results means "the script exited N". Only the trip test
at the end of this subsection ran against the **live registered hook**. The harness source is
`/tmp/mgr-verify-s35/verify.py`; it builds its own throwaway root at
`/tmp/mgr-verify-s35/root`, independent of every worker driver. Its invocation:

```
$ python3 /tmp/mgr-verify-s35/verify.py
live sha256 = b3de1137bff3b05a259d11b65eedd69681823626d290d68916e144fef3c330ef
copy sha256 = b3de1137bff3b05a259d11b65eedd69681823626d290d68916e144fef3c330ef
cmp rc=0
plain commit  rc=2  stderr 214 bytes
brace group   rc=0  stderr 0 bytes
DISCRIMINATES: True  (deny rc=2, admit rc=0)
armed     len=214  sha256=3f364cda2467c2c07dd6d1f1ee4d1aa6273917ad44c4e7f2ffc207334dc09e8c
invented  len=0    sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
disarmed  len=0    sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
S9 ARMING-MARKER CONTROL: HOLDS
```

The manager's armed-stderr sha256 `3f364cda…9e8c` independently equals the worker's
(§3.2) — two harnesses built separately, byte-for-byte the same denial.

**What the `invented` row is, named rather than left as a verdict.** The S9 negative control
is not "no marker": it is a marker file with a **wrong name at the right position** —
`verify.py` created `orchestrator-activee` (a trailing `e`) in the *same* directory,
`<root>/.claude/state/`, alongside nothing else, i.e. exactly where the real
`orchestrator-active` marker would sit. The script then produced empty stderr and exit 0,
sha256 `e3b0c442…b855` (the sha256 of zero bytes) — identical to the `disarmed` row. So the
gate keys on the marker's exact filename at that path, not on the directory being non-empty.
This mirrors §3.2's Cell C, which used the same invented name independently.

**And the live trip test against the real registered hook, this session (S3 — the gate
deliberately tripped, the block observed):**

```
$ git -C /tmp/mgr-verify-s35/root commit -m "manager live trip test"; echo "shell-exit=$?"
PreToolUse:Bash hook error: ["$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh]: Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
```

Two properties of that block matter. First, the isolation lever described in §2.1 was in
force, so `gate-commit.sh` is the sole possible denier. Second, the deny text matched the
expected `gate-commit.sh` string exactly, so no cross-hook print race masked the
attribution. Unlike everything in §2.3, this is an **enforcement** observation: the tool
call did not reach a shell.

---

## 3. What `gate-commit.sh` actually keys on — by experiment

Derived from the sweep and the S9 controls, **not** from reading the source.

Read the list as a whole: item 1 describes the **command-matching step**, items 2-5 describe
the **conditions the gate evaluates once that step has matched**. Item 1 is not a statement
about the gate as a whole.

1. **The command-matching step reads exactly one thing: the literal
   `tool_input.command` string.** That step alone does not consult the git
   operation, the target repo or the cwd — §2.2 is the evidence: the same
   underlying `git commit` runs untouched when the command *string* does not
   contain a matching shape. **This does not mean the gate keys on nothing else.**
   It plainly does — see items 2-5, and see §3.2, where the *identical* command
   string yields exit 2 armed and exit 0 disarmed. The earlier wording here
   ("Nothing else") was false of the gate and is withdrawn; it is true only of
   the matcher.
2. **Presence of `$CLAUDE_PROJECT_DIR/.claude/state/orchestrator-active`.**
   Positive-controlled both directions (§3.2).
3. **`sha256(git diff --cached)` of the repo at `$CLAUDE_PROJECT_DIR`**, used as
   the token filename. Observed in §2.3(d) cells **d1** and **d3**: the same hash
   appears as the `<hash>` in the `AUDIT_LOG.md` PASS row and as the key the
   script looks up, and d3 shows the `audit-pass-*` token file consumed on allow.
   **UNVERIFIED:** the contrast clause — that the hash is of the
   `$CLAUDE_PROJECT_DIR` repo and *not* of the repo the command targets — is
   **not** established by experiment in this document. Every cell in §2.3(d) used
   a command with no `-C`, so the two repos coincided; and every `-C`-bearing
   shape swept in §4 took the tokenless deny path, which never computes the
   lookup. This clause is a SOURCE-READ of the script, not a tested result.
4. **A `<hash> PASS` row in `AUDIT_LOG.md`.** Observed to deny in its absence —
   §2.3(d) cell **d1**: exit 2, stderr `Commit denied: token has no AUDIT_LOG
   PASS row — forged or corrupted; re-dispatch the orchestrator-auditor.`
5. **A `tree=` line in the token matching `git write-tree`.** Observed to deny
   when absent — §2.3(d) cell **d2**, which denies quoting `minted
   tree=missing/legacy-token`. The matching case is the positive control:
   §2.3(d) cell **d3**, `tree=` present and equal to `git write-tree` → exit 0,
   token consumed; and cell **d4**, immediate replay of the same call → exit 2,
   single-use consumption. Cells d1-d4 all ran against the **copy**
   `/tmp/praxis-s35-repair/hookcopy.sh`, so each result is "the script exited N",
   not "the tool call was blocked".
6. **Not** payload `cwd`, **not** `agent_id`, **not** `agent_type` — and not
   `session_id` or `hook_event_name` either. See §3.1.6 immediately below: the claim
   **holds**, but the provenance round 1 gave for it was **false**, and it is re-evidenced
   here on a purpose-built well-formed-payload sweep.

### 3.1.6 The payload-field claim, re-evidenced (item 6)

**Round 1's stated basis for item 6 did not exist.** Item 6 was attributed to the §4
sweep in `/tmp/praxis-s35-adv/a4_driver.sh`. That driver never varied `agent_id` or
`agent_type` at all, and never varied `cwd`:

```
$ for k in agent_id agent_type; do printf -- "-- grep -c %s a4_driver.sh: " "$k"; grep -c "$k" /tmp/praxis-s35-adv/a4_driver.sh; echo "grep rc=$?"; done
-- grep -c agent_id a4_driver.sh: 0
grep rc=1
-- grep -c agent_type a4_driver.sh: 0
grep rc=1

$ grep -n 'cwd' /tmp/praxis-s35-adv/a4_driver.sh; echo "grep rc=$?"
47:print(json.dumps({"session_id":"s","cwd":sys.argv[2],"hook_event_name":"PreToolUse",
111:    p={"session_id":"s","cwd":repo,"hook_event_name":"PreToolUse","tool_name":"Bash",
grep rc=0
```

Both `cwd` occurrences pin it to the harness repo. Item 6 as written described a sweep
that does not exist. The **conclusion** survives — on the new evidence below, not on the
old sweep.

**Why a re-test was necessary rather than a re-assertion — the fail-open hazard.** The
hook exits 0 with empty stderr on any payload that does not parse (§3.3-B). So
"byte-identical stderr" between two malformed payloads is trivially true and says nothing
about whether a field is honoured. Reproduced directly, two payloads differing in `cwd`,
`session_id`, `hook_event_name` **and** `agent_type`:

```
---------- malformed-A ----------
payload verbatim:
{"session_id":"x","cwd":"/tmp/praxis-s35-payloadfields/harness","hook_event_name":"PreToolUse","tool_name":"Bash","tool_input":{"command":"git commit -m "probe payload field sweep""}}  <cat rc=0>
json.load: json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1 column 155 (char 154)
json.load rc=1
gate rc=0
stderr wc -c: 0
stderr sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

---------- malformed-B ----------
payload verbatim:
{"session_id":"DIFFERENT","cwd":"/nonexistent/zz","hook_event_name":"PostToolUse","agent_type":"praxis-master","tool_name":"Bash","tool_input":{"command":"git commit -m "probe payload field sweep""}}  <cat rc=0>
json.load: json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1 column 171 (char 170)
json.load rc=1
gate rc=0
stderr wc -c: 0
stderr sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

-- cmp malformed-A vs malformed-B stderr: cmp rc=0
-- cmp malformed-A vs WELL-FORMED base stderr: cmp: EOF on /tmp/praxis-s35-payloadfields/err/malformed-A.err
cmp rc=1
-- harness still armed?
test -f rc=0
-- token count still 0?
       0
rc=0
SCRIPT rc=0
```

`cmp` rc=0 — perfectly byte-identical output — purely because neither parses. Any sweep
whose payloads did not parse is disqualified as evidence for item 6.

**The replacement evidence: 25 well-formed variants, every one proven to parse.** One
armed, tokenless throwaway harness; every payload emitted via `json.dumps` and then
independently re-validated with `json.load`.

```
=== S3.2  well-formedness gate: every payload must parse as JSON ===
-- 00-base : json.load rc=0
-- cwd-tmp-realdir : json.load rc=0
-- cwd-nonexistent : json.load rc=0
-- cwd-real-praxis-repo : json.load rc=0
-- cwd-empty-string : json.load rc=0
-- cwd-absent : json.load rc=0
-- cwd-wrong-type-number : json.load rc=0
-- agentid-worker : json.load rc=0
-- agentid-master : json.load rc=0
-- agentid-empty-string : json.load rc=0
-- agentid-null : json.load rc=0
-- agenttype-empty : json.load rc=0
-- agenttype-praxis-master : json.load rc=0
-- agenttype-praxis-manager : json.load rc=0
-- agenttype-praxis-worker : json.load rc=0
-- agenttype-general-purpose : json.load rc=0
-- sessionid-different : json.load rc=0
-- sessionid-empty : json.load rc=0
-- sessionid-absent : json.load rc=0
-- event-PostToolUse : json.load rc=0
-- event-Stop : json.load rc=0
-- event-empty : json.load rc=0
-- event-absent : json.load rc=0
-- event-nonsense : json.load rc=0
-- allfour-varied : json.load rc=0
-- CONTROL-noncommit-command : json.load rc=0
-- CONTROL-invented-key-at-same-position : json.load rc=0
DISQUALIFIED (failed to parse): none
```

The command string is held constant by hash, so nothing but the field under test varies:

```
=== S3.4  confirm the command string is held constant across the sweep ===
-- sha256 of tool_input.command per payload:
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  00-base
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  cwd-tmp-realdir
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  cwd-nonexistent
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  cwd-real-praxis-repo
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  cwd-empty-string
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  cwd-absent
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  cwd-wrong-type-number
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  agentid-worker
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  agentid-master
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  agentid-empty-string
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  agentid-null
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  agenttype-empty
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  agenttype-praxis-master
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  agenttype-praxis-manager
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  agenttype-praxis-worker
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  agenttype-general-purpose
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  sessionid-different
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  sessionid-empty
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  sessionid-absent
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  event-PostToolUse
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  event-Stop
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  event-empty
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  event-absent
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  event-nonsense
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  allfour-varied
584a331fd6b02dcb1ecbe2eba731f609a2e1e3dac0bb73ae998dfad14c309a77  CONTROL-noncommit-command
c1d54f6987680d12f2d3adb3ffe2f6a813056fd11fe41627c852ae271b26199b  CONTROL-invented-key-at-same-position
rc=0
```

Every variant denies, and only the deliberately-labelled non-commit control does not:

```
=== S5.1  rc table ===
2 00-base
2 cwd-tmp-realdir
2 cwd-nonexistent
2 cwd-real-praxis-repo
2 cwd-empty-string
2 cwd-absent
2 cwd-wrong-type-number
2 agentid-worker
2 agentid-master
2 agentid-empty-string
2 agentid-null
2 agenttype-empty
2 agenttype-praxis-master
2 agenttype-praxis-manager
2 agenttype-praxis-worker
2 agenttype-general-purpose
2 sessionid-different
2 sessionid-empty
2 sessionid-absent
2 event-PostToolUse
2 event-Stop
2 event-empty
2 event-absent
2 event-nonsense
2 allfour-varied
0 CONTROL-noncommit-command
2 CONTROL-invented-key-at-same-position
rc=0
```

`cmp` against the base capture, all 25:

```
=== S5.2  cmp every variant's stderr against the base ===
-- cmp base vs 00-base : cmp rc=0
-- cmp base vs cwd-tmp-realdir : cmp rc=0
-- cmp base vs cwd-nonexistent : cmp rc=0
-- cmp base vs cwd-real-praxis-repo : cmp rc=0
-- cmp base vs cwd-empty-string : cmp rc=0
-- cmp base vs cwd-absent : cmp rc=0
-- cmp base vs cwd-wrong-type-number : cmp rc=0
-- cmp base vs agentid-worker : cmp rc=0
-- cmp base vs agentid-master : cmp rc=0
-- cmp base vs agentid-empty-string : cmp rc=0
-- cmp base vs agentid-null : cmp rc=0
-- cmp base vs agenttype-empty : cmp rc=0
-- cmp base vs agenttype-praxis-master : cmp rc=0
-- cmp base vs agenttype-praxis-manager : cmp rc=0
-- cmp base vs agenttype-praxis-worker : cmp rc=0
-- cmp base vs agenttype-general-purpose : cmp rc=0
-- cmp base vs sessionid-different : cmp rc=0
-- cmp base vs sessionid-empty : cmp rc=0
-- cmp base vs sessionid-absent : cmp rc=0
-- cmp base vs event-PostToolUse : cmp rc=0
-- cmp base vs event-Stop : cmp rc=0
-- cmp base vs event-empty : cmp rc=0
-- cmp base vs event-absent : cmp rc=0
-- cmp base vs event-nonsense : cmp rc=0
-- cmp base vs allfour-varied : cmp rc=0
-- cmp base vs CONTROL-noncommit-command : cmp: EOF on /tmp/praxis-s35-payloadfields/err/CONTROL-noncommit-command.err
cmp rc=1
-- cmp base vs CONTROL-invented-key-at-same-position : cmp rc=0

=== S5.3  sha256 table of all stderr captures ===
3f364cda2467c2c07dd6d1f1ee4d1aa6273917ad44c4e7f2ffc207334dc09e8c  00-base
[… 24 further variants, all 3f364cda…9e8c …]
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  CONTROL-noncommit-command
3f364cda2467c2c07dd6d1f1ee4d1aa6273917ad44c4e7f2ffc207334dc09e8c  CONTROL-invented-key-at-same-position
rc=0
-- distinct stderr sha256 count:
       2
rc=0
```

**Distinct stderr sha256 count across all 27 runs = 2:** the 214-byte denial
`3f364cda…9e8c`, and the empty capture `e3b0c442…b855` belonging to the non-commit
control. And the arming marker is what produces the rc=2, not an unconditional deny:

```
=== S6.1  positive control: same base payload, arming marker REMOVED ===
rc=0
rc=1
rc=0
stderr wc -c: 0
<cat rc=0>
rc=0
rc=0

=== S6.2  re-run base AFTER re-arming (determinism / idempotence check) ===
rc=2
rc=0
```

**Mechanism, which is the real reason the negative is robust.** The script reads no
top-level payload field at all — only `tool_input.command` (line 29) and the *environment*
variable `CLAUDE_PROJECT_DIR` (line 57):

```
=== S7  what the copy actually references (grep, for the mechanism claim) ===
-- grep -n for payload field names inside the hook source:
12:#      process (outside this session's own process tree) has its cwd inside
89:# session's own process tree) is cwd'd inside this repo. Runs BEFORE token lookup
122:# every process with a cwd, as -Fpn records (p<pid> / n<path>); command names are
124:LSOF_OUT=$(lsof -a -d cwd -Fpn 2>/dev/null)
144:  deny_session "another live claude session (pid$FOREIGN) has its cwd inside this repo — it can pollute the shared .git/index between audit and commit (2026-07-10 incident)"
grep rc=0
-- grep -n for what it DOES read out of the payload:
29:CMD=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null || true)
57:ROOT="${CLAUDE_PROJECT_DIR:-.}"
grep rc=0
```

**The absence claim needs the grep itself, and round 1 did not paste it.** The fence above
prints a label, five `cwd` match lines and `grep rc=0` — but never the grep command or its
pattern, and **a fence of matches cannot demonstrate an absence.** The claim is nonetheless
true; here is the grep that carries it, re-run first-hand in this session against the **live**
hook (a SOURCE-READ, not a behavioural result):

```
$ grep -nE 'agent_id|agent_type|session_id|hook_event_name' /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh; echo "rc=$?"
rc=1
```

**`rc=1` from `grep` — no output, no match in the whole file — is the evidence of absence.**
That single exit code, not the earlier fence, is what supports "appear **nowhere** in the
source". The same correction applies to the "only line 29 and line 57" claim above: showing
two matching lines does not establish that they are the *only* two. The pattern-complete form,
also re-run first-hand:

```
$ grep -nE 'tool_input|CLAUDE_PROJECT_DIR' /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh; echo "rc=$?"
29:CMD=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null || true)
57:ROOT="${CLAUDE_PROJECT_DIR:-.}"
rc=0
$ grep -cE 'tool_input|CLAUDE_PROJECT_DIR' /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh; echo "rc=$?"
2
rc=0
```

The count `2` matching the two printed line numbers is what makes "only" defensible.
The only `cwd` hits are prose comments and the `lsof -a -d cwd -Fpn` process scan,
which reads live process cwds from the OS — not from the payload.

**Defensible restatement of item 6, narrower than round 1 worded it:** *for a plain
`git commit -m "..."` command in an armed, tokenless repo, `gate-commit.sh` produced exit
code 2 and byte-identical stderr (214 bytes, sha256 `3f364cda…9e8c`) across 25 well-formed
payloads varying `cwd`, `agent_id`, `agent_type`, `session_id` and `hook_event_name`,
individually and all at once. The script reads no top-level payload field.*

**`hook_event_name` scoped carefully.** Five values (`PostToolUse`, `Stop`, `""`, absent,
`NotAnEventAtAll`) all denied with byte-identical stderr, and the string does not occur in
the source. That is a claim about **the script**. It is **not** a claim that the live
runtime would route a `PostToolUse` event to this hook — event routing happens in Claude
Code's dispatcher *before* the script runs, and this experiment invokes the script
directly. Untested.

**Unchanged gap:** a REAL live payload has still never been captured in this project. The
field names above are constructed guesses. See §6 item 7 and §7.

### 3.2 S9 positive control — the arming marker (DISCHARGED)

Rubric S9: *"Any config field a guarantee depends on is positive-controlled: confirm a
visible script fires at that field, then confirm an invented key at the same position
produces byte-identical silence. A field that parses is not a field that is honoured."*

The field under control is the existence of `.claude/state/orchestrator-active` inside
`CLAUDE_PROJECT_DIR`. Three cells, one payload held constant, everything else identical.
Driver `/tmp/praxis-s35-repair/drv_s9.sh`.

```
$ bash /tmp/praxis-s35-repair/drv_s9.sh
### single payload held constant across all three cells
{"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"s9\"", "description": "s9"}}

### held-constant staged set
A	work.txt
rc=0
### held-constant token state (expect no audit-pass-* files)
0
(count) rc=1
```

**Cell A — marker present, correct name → exit 2 (the field fires)**

```
=== CELL A: marker PRESENT, correct name 'orchestrator-active' -> expect DENY exit 2
--- .claude/state contents for this cell ---
orchestrator-active
(ls rc=0)
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh >/tmp/praxis-s35-repair/out/s9-armed.out 2>/tmp/praxis-s35-repair/out/s9-armed.err
rc=2
--- stderr ---
Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
--- stderr byte count (wc -c) ---
     214
(wc rc=0)
```

**Cell B — marker absent (fully disarmed) → exit 0, empty stderr.** Emptiness is proven by
`wc -c` = 0, not by the absence of visible text.

```
=== CELL B: marker ABSENT (fully disarmed) -> expect exit 0, EMPTY stderr
--- .claude/state contents for this cell ---
(ls rc=0)
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh >/tmp/praxis-s35-repair/out/s9-disarmed.out 2>/tmp/praxis-s35-repair/out/s9-disarmed.err
rc=0
--- stderr ---
--- stderr byte count (wc -c) ---
       0
(wc rc=0)
```

**Cell C — invented key at the same position (`orchestrator-activee`) → exit 0, empty
stderr.** Same directory, same everything else; only the filename gains one character.

```
=== CELL C: INVENTED key at the same position — same dir, file named 'orchestrator-activee'
--- .claude/state contents for this cell ---
orchestrator-activee
(ls rc=0)
--- invocation ---
printf '%s' "$PAYLOAD" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair/root /tmp/praxis-s35-repair/hookcopy.sh >/tmp/praxis-s35-repair/out/s9-invented.out 2>/tmp/praxis-s35-repair/out/s9-invented.err
rc=0
--- stderr ---
--- stderr byte count (wc -c) ---
       0
(wc rc=0)
```

**Both `cmp` invocations S9 requires, with their exit codes, plus a third for the
load-bearing direction:**

```
=== S9 COMPARISONS ===
-- rc values --
armed rc=2
disarmed rc=0
invented rc=0

$ cmp /tmp/praxis-s35-repair/out/s9-invented.err /tmp/praxis-s35-repair/out/s9-disarmed.err
rc=0   # 0 => invented key is BYTE-IDENTICAL to fully-disarmed

$ cmp /tmp/praxis-s35-repair/out/s9-invented.err /tmp/praxis-s35-repair/out/s9-armed.err
cmp: EOF on /tmp/praxis-s35-repair/out/s9-invented.err
rc=1   # non-zero => invented key DIFFERS from the armed case

$ cmp /tmp/praxis-s35-repair/out/s9-disarmed.err /tmp/praxis-s35-repair/out/s9-armed.err
cmp: EOF on /tmp/praxis-s35-repair/out/s9-disarmed.err
rc=1   # non-zero => disarmed differs from armed (the field is load-bearing)

-- sha256 of the three stderr captures --
3f364cda2467c2c07dd6d1f1ee4d1aa6273917ad44c4e7f2ffc207334dc09e8c  /tmp/praxis-s35-repair/out/s9-armed.err
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /tmp/praxis-s35-repair/out/s9-disarmed.err
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  /tmp/praxis-s35-repair/out/s9-invented.err
rc=0
```

`e3b0c442…b855` is the sha256 of the **empty byte string**, so the disarmed and invented-key
captures are not merely equal to each other — they are both provably empty. The exact name
fires the script (exit 2, 214 bytes); a one-character variant at the same position is
byte-identical to having no marker at all (exit 0, 0 bytes). **The field is honoured, not
merely parsed.** Independently reproduced by the manager's separate harness — §2.4, same
`3f364cda…9e8c`.

This discharges S9 for the **arming marker**. It does not discharge S9 for the hook
**registration** field; that remains UNVERIFIED — §6 item 1, `Praxis_build-sk8`.

### 3.3 Admitted shapes — a separate defect from 8sw

Instrument provenance for every block in §3.3 and §4, and the environment it ran in:

```
$ cp /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh /tmp/praxis-s35-repair2/gate.copy.sh
$ cmp /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh /tmp/praxis-s35-repair2/gate.copy.sh
cmp rc=0
$ shasum -a 256 /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh /tmp/praxis-s35-repair2/gate.copy.sh
b3de1137bff3b05a259d11b65eedd69681823626d290d68916e144fef3c330ef  /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
b3de1137bff3b05a259d11b65eedd69681823626d290d68916e144fef3c330ef  /tmp/praxis-s35-repair2/gate.copy.sh
rc=0
$ /usr/bin/git --version ; bash --version | head -1 ; python3 --version
git version 2.50.1 (Apple Git-155)
GNU bash, version 5.3.15(1)-release (aarch64-apple-darwin25.4.0)
Python 3.14.3
```

#### 3.3-A Eight shapes exit 0, and the same harness exits 2 on a plain commit

The sweep runs against one ARMED, tokenless throwaway repo. **Two contrasting DENY cases
run through the identical code path in the same invocation**, so the sweep is demonstrably
discriminating rather than returning 0 for everything.

```
$ python3 /tmp/praxis-s35-repair2/shapes.py
rc=0
REPO           = /tmp/praxis-s35-repair2/repo-shapes
HEAD branch    = main
state dir      = orchestrator-active
audit tokens   = 0  (tokenless)
staged         = work.txt

---- D1 CONTRAST deny  plain commit
payload  : {"session_id": "s35", "cwd": "/tmp/praxis-s35-repair2/repo-shapes", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"x\"", "description": "d"}}
invoke   : printf '%s' "$payload" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair2/repo-shapes bash /tmp/praxis-s35-repair2/gate.copy.sh
rc=2   (DENY)
stderr   : 214 bytes
  | Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
stdout   : 0 bytes

---- D2 CONTRAST deny  chained commit
payload  : {"session_id": "s35", "cwd": "/tmp/praxis-s35-repair2/repo-shapes", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "cd /tmp/praxis-s35-repair2 && git commit -m \"y\"", "description": "d"}}
invoke   : printf '%s' "$payload" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair2/repo-shapes bash /tmp/praxis-s35-repair2/gate.copy.sh
rc=2   (DENY)
stderr   : 214 bytes
  | Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
stdout   : 0 bytes

---- A1 brace group
payload  : {"session_id": "s35", "cwd": "/tmp/praxis-s35-repair2/repo-shapes", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "{ git commit -q -m \"S-brace\"; }", "description": "d"}}
invoke   : printf '%s' "$payload" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair2/repo-shapes bash /tmp/praxis-s35-repair2/gate.copy.sh
rc=0   (ADMIT / does NOT deny)
stderr   : 0 bytes
  | <empty>
stdout   : 0 bytes

---- A2 if/then/fi
payload  : {"session_id": "s35", "cwd": "/tmp/praxis-s35-repair2/repo-shapes", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "if true; then git commit -q -m \"S-if\"; fi", "description": "d"}}
invoke   : printf '%s' "$payload" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair2/repo-shapes bash /tmp/praxis-s35-repair2/gate.copy.sh
rc=0   (ADMIT / does NOT deny)
stderr   : 0 bytes
  | <empty>
stdout   : 0 bytes

---- A3 for/do/done
payload  : {"session_id": "s35", "cwd": "/tmp/praxis-s35-repair2/repo-shapes", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "for f in one; do git commit -q -m \"S-for\"; done", "description": "d"}}
invoke   : printf '%s' "$payload" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair2/repo-shapes bash /tmp/praxis-s35-repair2/gate.copy.sh
rc=0   (ADMIT / does NOT deny)
stderr   : 0 bytes
  | <empty>
stdout   : 0 bytes

---- A4 while/do/done
payload  : {"session_id": "s35", "cwd": "/tmp/praxis-s35-repair2/repo-shapes", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "while read -r l; do git commit -q -m \"S-while\"; done < /tmp/praxis-s35-repair2/one.txt", "description": "d"}}
invoke   : printf '%s' "$payload" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair2/repo-shapes bash /tmp/praxis-s35-repair2/gate.copy.sh
rc=0   (ADMIT / does NOT deny)
stderr   : 0 bytes
  | <empty>
stdout   : 0 bytes

---- A5 negation prefix
payload  : {"session_id": "s35", "cwd": "/tmp/praxis-s35-repair2/repo-shapes", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "! git commit -q -m \"S-neg\"", "description": "d"}}
invoke   : printf '%s' "$payload" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair2/repo-shapes bash /tmp/praxis-s35-repair2/gate.copy.sh
rc=0   (ADMIT / does NOT deny)
stderr   : 0 bytes
  | <empty>
stdout   : 0 bytes

---- A6 func def then call
payload  : {"session_id": "s35", "cwd": "/tmp/praxis-s35-repair2/repo-shapes", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "f(){ git commit -q -m \"S-fn\"; }; f", "description": "d"}}
invoke   : printf '%s' "$payload" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair2/repo-shapes bash /tmp/praxis-s35-repair2/gate.copy.sh
rc=0   (ADMIT / does NOT deny)
stderr   : 0 bytes
  | <empty>
stdout   : 0 bytes

---- A7 backslash-newline before 'commit'
payload  : {"session_id": "s35", "cwd": "/tmp/praxis-s35-repair2/repo-shapes", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git \\\n  commit -q -m \"S-bsnl\"", "description": "d"}}
invoke   : printf '%s' "$payload" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair2/repo-shapes bash /tmp/praxis-s35-repair2/gate.copy.sh
rc=0   (ADMIT / does NOT deny)
stderr   : 0 bytes
  | <empty>
stdout   : 0 bytes

---- A8 direct script path (no git/commit in path)
payload  : {"session_id": "s35", "cwd": "/tmp/praxis-s35-repair2/repo-shapes", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "/tmp/praxis-s35-repair2/bin/do-the-thing.sh", "description": "d"}}
invoke   : printf '%s' "$payload" | CLAUDE_PROJECT_DIR=/tmp/praxis-s35-repair2/repo-shapes bash /tmp/praxis-s35-repair2/gate.copy.sh
rc=0   (ADMIT / does NOT deny)
stderr   : 0 bytes
  | <empty>
stdout   : 0 bytes
```

**Observed: 8/8 shapes rc=0, 2/2 contrasts rc=2. The sweep discriminates.**

The `bash -x` trace shows *where* an admitted shape exits: after the two form greps fail,
at the `exit 0` on line 55 — before `ROOT`, `STATE`, the token lookup or any `git` are ever
reached.

```
$ bash /tmp/praxis-s35-repair2/trace2.sh
gate rc=0
--- full -x trace (admitted shape) ---
+ set -uo pipefail
++ cat
+ INPUT='{"session_id": "s", "cwd": "/tmp/praxis-s35-repair2/repo-main", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "{ git commit -m \"x\"; }", "description": "d"}}'
++ printf %s '{"session_id": "s", "cwd": "/tmp/praxis-s35-repair2/repo-main", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "{ git commit -m \"x\"; }", "description": "d"}}'
++ python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))'
+ CMD='{ git commit -m "x"; }'
+ case "$CMD" in
++ printf %s '{ git commit -m "x"; }'
++ sed -e 's/'\''[^'\'']*'\''//g' -e 's/"[^"]*"//g'
+ SCRUB='{ git commit -m ; }'
+ ANCHOR='(^|[;&|(`])[[:space:]]*'
+ PRE='([A-Za-z_][A-Za-z_0-9]*=[^[:space:]]*[[:space:]]+)*((command|builtin|exec|env|sudo|nohup|nice|time|xargs)([[:space:]]+[^;&|`]*)?[[:space:]]+)?'
+ BINPRE='(\\|[^[:space:];&|`]*/)?'
+ GITCOMMIT='(\\|[^[:space:];&|`]*/)?git[[:space:]]+([^;&|`]*[[:space:]])?commit([[:space:];&|)`]|$)'
+ NESTSHELL='(\\|[^[:space:];&|`]*/)?(sh|bash|zsh|dash|ksh|eval)([[:space:]]|$)'
+ printf %s '{ git commit -m ; }'
+ grep -Eq '(^|[;&|(`])[[:space:]]*([A-Za-z_][A-Za-z_0-9]*=[^[:space:]]*[[:space:]]+)*((command|builtin|exec|env|sudo|nohup|nice|time|xargs)([[:space:]]+[^;&|`]*)?[[:space:]]+)?(\\|[^[:space:];&|`]*/)?git[[:space:]]+([^;&|`]*[[:space:]])?commit([[:space:];&|)`]|$)'
+ printf %s '{ git commit -m ; }'
+ grep -Eq '(^|[;&|(`])[[:space:]]*([A-Za-z_][A-Za-z_0-9]*=[^[:space:]]*[[:space:]]+)*((command|builtin|exec|env|sudo|nohup|nice|time|xargs)([[:space:]]+[^;&|`]*)?[[:space:]]+)?(\\|[^[:space:];&|`]*/)?(sh|bash|zsh|dash|ksh|eval)([[:space:]]|$)'
+ exit 0
--- lines in trace ---
      20 /tmp/praxis-s35-repair2/out/trace2.err
--- any git invocation? ---
grep rc=1  (rc=1 == no git ran at all)
script rc=0
```

The admit path is 20 trace lines and runs **no `git` at all** (`grep rc=1`). It never reads
the arming marker.

#### 3.3-B Malformed / missing-field payloads exit 0 — the parser FAILS OPEN

Same ARMED, tokenless repo, so any payload the parser *did* understand as a `git commit`
would produce rc=2. A well-formed commit payload is included as contrast and does.

```
$ python3 /tmp/praxis-s35-repair2/malformed.py
rc=0
REPO = /tmp/praxis-s35-repair2/repo-shapes (ARMED, tokenless)

---- empty stdin
stdin bytes (0): b''
rc=0
stderr (0 bytes): b''
stdout (0 bytes): b''

---- truncated JSON
stdin bytes (59): b'{"tool_name":"Bash","tool_input":{"command":"git commit -m '
rc=0
stderr (0 bytes): b''
stdout (0 bytes): b''

---- truncated JSON (2)
stdin bytes (33): b'{"tool_name":"Bash","tool_input":'
rc=0
stderr (0 bytes): b''
stdout (0 bytes): b''

---- non-JSON text
stdin bytes (15): b'not json at all'
rc=0
stderr (0 bytes): b''
stdout (0 bytes): b''

---- non-JSON binary-ish
stdin bytes (14): b'\x00\x01\x02git commit\x00'
rc=0
stderr (105 bytes): b'/tmp/praxis-s35-repair2/gate.copy.sh: line 28: warning: command substitution: ignored null byte in input\n'
stdout (0 bytes): b''

---- empty object
stdin bytes (2): b'{}'
rc=0
stderr (0 bytes): b''
stdout (0 bytes): b''

---- no tool_input key
stdin bytes (20): b'{"tool_name":"Bash"}'
rc=0
stderr (0 bytes): b''
stdout (0 bytes): b''

---- tool_input, no command key
stdin bytes (36): b'{"tool_name":"Bash","tool_input":{}}'
rc=0
stderr (0 bytes): b''
stdout (0 bytes): b''

---- command null
stdin bytes (50): b'{"tool_name":"Bash","tool_input":{"command":null}}'
rc=0
stderr (0 bytes): b''
stdout (0 bytes): b''

---- command int
stdin bytes (49): b'{"tool_name":"Bash","tool_input":{"command":123}}'
rc=0
stderr (0 bytes): b''
stdout (0 bytes): b''

---- command array
stdin bytes (62): b'{"tool_name":"Bash","tool_input":{"command":["git","commit"]}}'
rc=0
stderr (0 bytes): b''
stdout (0 bytes): b''

---- JSON array not object
stdin bytes (46): b'[{"tool_input":{"command":"git commit -m x"}}]'
rc=0
stderr (0 bytes): b''
stdout (0 bytes): b''

---- CONTRAST: well-formed commit payload
stdin bytes (67): b'{"tool_name":"Bash","tool_input":{"command":"git commit -m \\"x\\""}}'
rc=2
stderr (214 bytes): b'Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.\n'
stdout (0 bytes): b''

---- a4_driver's 'minimal-valid-commit' string, verbatim
stdin bytes (65): b'{"tool_name":"Bash","tool_input":{"command":"git commit -m "x""}}'
rc=0
stderr (0 bytes): b''
stdout (0 bytes): b''
```

**Observed: 13/13 malformed cases rc=0; the one well-formed commit payload rc=2.** The
parser **fails OPEN**, which contradicts the script's own header comments claiming
fail-closed behaviour.

**CORRECTION to round 1.** Round 1 wrote that every malformed payload exits 0
*silently*. That is **wrong for one case.** The NUL-containing payload
(`b'\x00\x01\x02git commit\x00'`) exits 0 but is **not silent** — bash emits a **105-byte
warning** on stderr from line 28: `warning: command substitution: ignored null byte in
input`. The exit code claim holds; the silence claim does not.

**Three sweep cases must NOT be read as "a valid payload was admitted."** The cases
`mal-minimal-valid-commit`, `mal-toolname-Write` and `mal-event-PostToolUse` in
`/tmp/praxis-s35-adv/a4_driver.sh` lines 88-90 interpolate `CM='git commit -m "x"'` into
hand-built JSON, so their inner double quotes are never escaped and **the payloads do not
parse**:

```
$ grep -n 'minimal-valid-commit\|toolname-Write\|event-PostToolUse' /tmp/praxis-s35-adv/a4_driver.sh; echo "grep rc=$?"
88:mal_one "{\"tool_name\":\"Bash\",\"tool_input\":{\"command\":\"$CM\"}}" "minimal-valid-commit"
89:mal_one "{\"tool_input\":{\"command\":\"$CM\"},\"tool_name\":\"Write\"}" "toolname-Write"
90:mal_one "{\"tool_input\":{\"command\":\"$CM\"},\"hook_event_name\":\"PostToolUse\"}" "event-PostToolUse"
grep rc=0

$ grep -n 'CM=' /tmp/praxis-s35-adv/a4_driver.sh; echo "grep rc=$?"
79:CM='git commit -m "x"'
grep rc=0
```

Their rc=0 is therefore a **fail-open** result, not evidence that a valid commit payload was
admitted. The label `minimal-valid-commit` is itself misleading and is flagged as such: it
names the intent of the case, not what the case actually fed the script.

**RECOVERED — `/tmp/praxis-s35-adv/stderr-mal-*.txt`.** The claim being checked is that the
1-byte size of those stale artifacts means *empty stderr*. It does: the byte is `0x0a`, and
`68b329da9893e34099c7d8ad5cb9c940` is the md5 of a lone newline, written by the driver's
`printf '%s\n' "$err"` around an empty `$err`.

```
$ cd /tmp/praxis-s35-adv && ls -l stderr-mal-*.txt
-rw-r--r--@ 1 admin  wheel  1 Jul 26 15:06 stderr-mal-command-array.txt
[… 9 further files, each 1 byte …]
-rw-r--r--@ 1 admin  wheel  1 Jul 26 15:06 stderr-mal-toolname-Write.txt
rc=0
$ for f in stderr-mal-*.txt; do printf '%-45s ' "$f"; xxd "$f"; done
stderr-mal-command-array.txt                  00000000: 0a                                       .
[… identical for all 11 …]
rc=0
$ md5 -q stderr-mal-*.txt | sort -u
68b329da9893e34099c7d8ad5cb9c940
rc=0
```

#### 3.3-C "and each of them really commits" — evidenced

Evidenced in a **throwaway** `/tmp` git repo (`/tmp/praxis-s35-repair2/repo-live`), never
the real repo. Per shape the harness (1) stages a unique file, (2) runs the gate copy and
records rc, (3) if rc=0 executes that *same* command string with cwd in the throwaway repo,
(4) prints `git log --oneline`.

```
$ python3 /tmp/praxis-s35-repair2/live.py
rc=0
REPO         = /tmp/praxis-s35-repair2/repo-live   (throwaway)
ARMED        = True
audit tokens = 0
$ /usr/bin/git -C /tmp/praxis-s35-repair2/repo-live log --oneline   (before)
38cffc4 base
rc=0

---- A1 brace group
staged   : f1.txt
gate rc=0  stderr=0 bytes
exec rc=0  stdout=''  stderr=''
$ git log --oneline -1  ->  10a5342 S-brace   rc=0

---- A2 if/then/fi
staged   : f2.txt
gate rc=0  stderr=0 bytes
exec rc=0  stdout=''  stderr=''
$ git log --oneline -1  ->  8a19d7d S-if   rc=0

---- A3 for/do/done
staged   : f3.txt
gate rc=0  stderr=0 bytes
exec rc=0  stdout=''  stderr=''
$ git log --oneline -1  ->  7ff5e95 S-for   rc=0

---- A4 while/do/done
staged   : f4.txt
gate rc=0  stderr=0 bytes
exec rc=0  stdout=''  stderr=''
$ git log --oneline -1  ->  93d6668 S-while   rc=0

---- A5 negation prefix
staged   : f5.txt
gate rc=0  stderr=0 bytes
exec rc=1  stdout=''  stderr=''
$ git log --oneline -1  ->  6439851 S-neg   rc=0

---- A6 func def then call
staged   : f6.txt
gate rc=0  stderr=0 bytes
exec rc=0  stdout=''  stderr=''
$ git log --oneline -1  ->  5e441fd S-fn   rc=0

---- A7 backslash-newline
staged   : f7.txt
gate rc=0  stderr=0 bytes
exec rc=0  stdout=''  stderr=''
$ git log --oneline -1  ->  f4daecc S-bsnl   rc=0

---- A8 direct script path
staged   : f8.txt
gate rc=0  stderr=0 bytes
exec rc=0  stdout=''  stderr=''
$ git log --oneline -1  ->  c3231d8 S-script   rc=0

=== FINAL: $ /usr/bin/git -C /tmp/praxis-s35-repair2/repo-live log --oneline ===
c3231d8 S-script
f4daecc S-bsnl
5e441fd S-fn
6439851 S-neg
93d6668 S-while
7ff5e95 S-for
8a19d7d S-if
10a5342 S-brace
38cffc4 base
rc=0
commit count: 9
$ git status --porcelain (clean == everything staged got committed)
'?? .claude/\n'
```

1 base + 8 shape commits = 9, index left clean (the only residue is the untracked
`.claude/` arming marker). **A5's `exec rc=1` is the `!` prefix inverting the shell's
status — the commit `6439851 S-neg` still landed.** A8 is not a separate trick: the
executing script `/tmp/praxis-s35-repair2/bin/do-the-thing.sh` *is* the "path containing
neither `git` nor `commit`" case, and its commit `c3231d8 S-script` is in the log.

**Bounded restatement (S2).** What is proven: *the gate script exits 0 on these shapes, and
these shapes, when executed, produce commits.* What is **not** proven: that Claude Code
would dispatch the shape to a shell after the hook returned 0. That step was not exercised
here.

**None of these produced `104c58e`.** The commands actually recorded in
`~/.zsh_history` (lines 1501–1505) **do** deny when replayed through the hook. The pasted
evidence for that is cells **p1** and **p2** of the §4.2 table, which are exactly those
shapes and both return rc=2:

```
  1   2  DENY     p1                        'git commit -m "park(x): y"'
  2   2  DENY     p2                        'git commit -m "park(x): y" && git checkout main'
```

Capped as §7 requires: that is "the script exited 2", not "the tool call was blocked". So
the (A)-finding and the (B)-origin are independent facts. Stated at the level the evidence
supports, and *not* as "the gate has holes" — that phrasing is withdrawn, because it
asserted end-to-end enforcement failure fourteen lines after this section capped itself
against exactly that: **the gate *script* exits 0 on shapes that, when executed, produce
commits.** That is a script-logic result about `gate-commit.sh` run as a program on
constructed stdin. Whether a live Claude Code tool call carrying one of those shapes
completes end-to-end — hook returns 0, runtime dispatches, shell commits — **was not
tested here**, and nothing in this report shows it. The (B) half is unaffected: this commit
did not go through any admitted shape, because it did not go through the gate at all.
Reporting
this as a finding for the master to file; **not** repairing it here — hard
limit 1 forbids touching the hook, and it is outside 8sw's scope.

---

## 4. Is a `parked/*` branch distinguishable to the gate today?

**No. Not in any way.** Three throwaway repos built with byte-identical content and an
identical staged diff; the *only* difference is the name `HEAD` points at.

### 4.1 The three repos differ only in HEAD

```
$ python3 /tmp/praxis-s35-repair2/sweep52.py main                       # head of transcript
branch arg      : main
repo            : /tmp/praxis-s35-repair2/repo-main
$ git rev-parse --abbrev-ref HEAD -> main
$ git symbolic-ref HEAD           -> refs/heads/main
armed marker    : ['orchestrator-active']
audit tokens    : 0
staged diff sha : fa59e94359e96a8cef4494dfe743e32aaf127fc79df8e82cd57a043331b85dad

$ python3 /tmp/praxis-s35-repair2/sweep52.py parked/Praxis_build-37h    # head of transcript
branch arg      : parked/Praxis_build-37h
repo            : /tmp/praxis-s35-repair2/repo-parked_Praxis_build-37h
$ git rev-parse --abbrev-ref HEAD -> parked/Praxis_build-37h
$ git symbolic-ref HEAD           -> refs/heads/parked/Praxis_build-37h
armed marker    : ['orchestrator-active']
audit tokens    : 0
staged diff sha : fa59e94359e96a8cef4494dfe743e32aaf127fc79df8e82cd57a043331b85dad
```

**The third repo, which round 1 argued over in §4.3/§4.4 without ever pasting.** `§4.1` showed
two repos while "on these three HEADs" and the `cmp(main,parked/anything-else)` column below
depend on a third. Its artifacts do still exist under `/tmp/praxis-s35-repair2/`, so they are
pasted here rather than the claim narrowed — re-read first-hand in this session:

```
$ R=/tmp/praxis-s35-repair2/repo-parked_anything-else
repo            : /tmp/praxis-s35-repair2/repo-parked_anything-else
$ git rev-parse --abbrev-ref HEAD -> parked/anything-else
$ git symbolic-ref HEAD           -> refs/heads/parked/anything-else
armed marker    : orchestrator-active
audit tokens    : 0
staged diff sha : fa59e94359e96a8cef4494dfe743e32aaf127fc79df8e82cd57a043331b85dad
```

Same `fa59e943…5dad` staged-diff sha, same arming state, same zero token count as the two
above.

**"Byte-identical content" was also never carried by any content comparison.** It is now:

```
$ for b in repo-main repo-parked_Praxis_build-37h repo-parked_anything-else; do printf '%s: ' $b; git -C $b ls-files -s | shasum -a 256 | awk '{print $1}'; done
repo-main: 6d376595d3f19a0f1ea67e06f3a855da0d97ff2a9c6a931e26fa0593b6c619b7
repo-parked_Praxis_build-37h: 6d376595d3f19a0f1ea67e06f3a855da0d97ff2a9c6a931e26fa0593b6c619b7
repo-parked_anything-else: 6d376595d3f19a0f1ea67e06f3a855da0d97ff2a9c6a931e26fa0593b6c619b7
$ diff -r --exclude=.git repo-main repo-parked_anything-else; echo "diff rc=$?"
diff rc=0
$ diff -r --exclude=.git repo-main repo-parked_Praxis_build-37h; echo "diff rc=$?"
diff rc=0
```

Identical index (`ls-files -s`, which covers mode + blob sha + stage + path) and `diff -r`
rc=0 on the working trees with `.git` excluded. The staged-diff sha is identical across all
three HEADs, so any difference in gate behaviour could only come from the branch name.

Scope note (S2): `diff -r --exclude=.git` compares tracked *and* untracked files outside
`.git`, and the `ls-files -s` hash compares the index. It does not compare the object stores
or the reflogs, which necessarily differ — the branch names live there. That is the intended
difference, not an uncontrolled one.

### 4.2 The vector is 52 cases — COUNT VERIFIED CORRECT

Round 1's "full 52-case exit-code vector" figure was checked and is **right**: 28 payloads
from `payloads.txt` + 11 raw malformed strings + 13 unicode/edge cases taken from the
original `a4_driver.sh` heredoc.

The composition is evidenced, with one discrepancy stated rather than smoothed over:

```
$ wc -l /tmp/praxis-s35-adv/payloads.txt
      28 /tmp/praxis-s35-adv/payloads.txt
rc=0
$ grep -nE "payloads.txt|a4_driver" /tmp/praxis-s35-repair2/sweep52.py
42:# ---- case list: 28 payloads.txt + 11 raw malformed + 13 driver python cases -
44:for i, line in enumerate(open("/tmp/praxis-s35-adv/payloads.txt").read().split("\n"), 1):
62:# lift the 13 unicode/edge cases verbatim out of the original a4_driver heredoc
63:src = open("/tmp/praxis-s35-adv/a4_driver.sh", encoding="utf-8").read()
rc=0
$ grep -c "^mal_one" /tmp/praxis-s35-adv/a4_driver.sh
12
rc=0
```

`payloads.txt` really does carry 28 lines, and the sweep harness really does read it and
really does lift from `a4_driver.sh`. **But the driver defines 12 `mal_one` cases while the
vector carries 11** (table rows 29-39). So the group sizes 28 + 11 + 13 describe the vector
that was run — which is what the 52 figure is about, and it is recountable from the table —
while the word **"verbatim" is the harness's own comment (line 62), not a byte-for-byte
identity this report established.** One malformed case present in the driver is absent from
the vector, and which one, and why, was not determined. `UNVERIFIED:` the exact
case-by-case correspondence between `a4_driver.sh` and the 52-case vector. The count and the
contrasting admit/deny split stand on the pasted table itself, not on this provenance.

```
$ wc -l /tmp/praxis-s35-adv/rc-main.txt /tmp/praxis-s35-adv/rc-parked.txt
      52 /tmp/praxis-s35-adv/rc-main.txt
      52 /tmp/praxis-s35-adv/rc-parked.txt
     104 total
rc=0
$ wc -l /tmp/praxis-s35-repair2/out/rc-main.txt /tmp/praxis-s35-repair2/out/rc-parked_Praxis_build-37h.txt /tmp/praxis-s35-repair2/out/rc-parked_anything-else.txt
      52 rc-main.txt
      52 rc-parked_Praxis_build-37h.txt
      52 rc-parked_anything-else.txt
     156 total
rc=0
```

Full fresh sweep on `main` (the `parked/*` runs are line-for-line identical — proven in
§4.3):

```
$ python3 /tmp/praxis-s35-repair2/sweep52.py main
idx  rc  verdict  label                     command/stdin
  1   2  DENY     p1                        'git commit -m "park(x): y"'
  2   2  DENY     p2                        'git commit -m "park(x): y" && git checkout main'
  3   0  ADMIT    p3                        '{ git commit -m "x"; }'
  4   0  ADMIT    p4                        'if true; then git commit -m "x"; fi'
  5   0  ADMIT    p5                        'for f in a; do git commit -m "x"; done'
  6   0  ADMIT    p6                        'while read l; do git commit -m "x"; done'
  7   2  DENY     p7                        'git\tcommit -m "x"'
  8   0  ADMIT    p8                        'then git commit -m "x"'
  9   0  ADMIT    p9                        'do git commit -m "x"'
 10   0  ADMIT    p10                       '} git commit -m "x"'
 11   0  ADMIT    p11                       '! git commit -m "x"'
 12   2  DENY     p12                       'git -C /tmp/x commit -m "x"'
 13   2  DENY     p13                       '/usr/bin/git commit -m "x"'
 14   2  DENY     p14                       '\\git commit -m "x"'
 15   2  DENY     p15                       'GIT_AUTHOR_NAME=x git commit -m "x"'
 16   2  DENY     p16                       'env git commit -m "x"'
 17   2  DENY     p17                       "sh -c 'git commit -m x'"
 18   2  DENY     p18                       'eval "git commit -m x"'
 19   0  ADMIT    p19                       "echo 'git commit -m x'"
 20   2  DENY     p20                       'git --git-dir=.git --work-tree=. commit -m "x"'
 21   2  DENY     p21                       'git -c user.name=z commit -m "x"'
 22   2  DENY     p22                       'time git commit -m "x"'
 23   2  DENY     p23                       'nohup git commit -m "x"'
 24   2  DENY     p24                       'xargs git commit'
 25   2  DENY     p25                       'git commit --no-verify -m "x"'
 26   2  DENY     p26                       'git commit -F /tmp/msg'
 27   2  DENY     p27                       'git commit'
 28   0  ADMIT    p28                       'git status'
 29   0  ADMIT    mal-empty-stdin           ''
 30   0  ADMIT    mal-not-json              'not json at all'
 31   0  ADMIT    mal-empty-object          '{}'
 32   0  ADMIT    mal-no-tool_input         '{"tool_name":"Bash"}'
 33   0  ADMIT    mal-no-command            '{"tool_name":"Bash","tool_input":{}}'
 34   0  ADMIT    mal-command-null          '{"tool_name":"Bash","tool_input":{"command":null}}'
 35   0  ADMIT    mal-command-int           '{"tool_name":"Bash","tool_input":{"command":123}}'
 36   0  ADMIT    mal-command-array         '{"tool_name":"Bash","tool_input":{"command":["git","com...'
 37   0  ADMIT    mal-minimal-valid-commit  '{"tool_name":"Bash","tool_input":{"command":"git commit...'
 38   0  ADMIT    mal-toolname-Write        '{"tool_input":{"command":"git commit -m "x""},"tool_nam...'
 39   0  ADMIT    mal-event-PostToolUse     '{"tool_input":{"command":"git commit -m "x""},"hook_eve...'
 40   2  DENY     x-unicode-nbsp            'git\xa0commit -m x'
 41   0  ADMIT    x-unicode-fullwidth       'ｇit commit -m x'
 42   2  DENY     x-newline-before          'echo hi\ngit commit -m "x"'
 43   2  DENY     x-heredoc-mention         "cat <<'EOF'\ngit commit -m x\nEOF"
 44   2  DENY     x-longcmd                 'echo aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...'
 45   0  ADMIT    x-brace-group             '{ git commit -m "x"; }'
 46   0  ADMIT    x-nested-func             'f(){ git commit -m x; }; f'
 47   0  ADMIT    x-backslash-newline       'git \\\n commit -m "x"'
 48   2  DENY     x-unbalanced-quote        'echo "unclosed && git commit -m x'
 49   2  DENY     x-dollar-paren            '$(git commit -m x)'
 50   2  DENY     x-gitdir-flag             'git --git-dir=/tmp/r/.git commit -m x'
 51   2  DENY     x-c-config                'git -c commit.gpgsign=false commit -m x'
 52   2  DENY     x-alias-shellexec         'git nope; git commit -m x'

TOTAL CASES RUN: 52
rc vector written to /tmp/praxis-s35-repair2/out/rc-main.txt
```

The vector is not degenerate — **25 admits, 27 denies**:

```
$ sort rc-main.txt | uniq -c
  25 rc=0
  27 rc=2
rc=0
```

**Cases 37, 38 and 39 must not be read as "valid payloads were admitted."** They are the
three malformed-JSON cases documented in §3.3-B; their rc=0 is **fail-open**. The `ADMIT`
verdict in the table is the driver's word for "did not deny", not a claim that the script
understood the payload.

### 4.3 Exit-code vectors identical across three HEADs

```
$ cd /tmp/praxis-s35-repair2/out
$ diff rc-main.txt rc-parked_Praxis_build-37h.txt ; echo "rc=$?"
rc=0
$ diff rc-main.txt rc-parked_anything-else.txt ; echo "rc=$?"
rc=0
$ cmp rc-main.txt rc-parked_Praxis_build-37h.txt ; echo "rc=$?"
rc=0
$ cmp rc-main.txt rc-parked_anything-else.txt ; echo "rc=$?"
rc=0
$ diff rc-main.txt /tmp/praxis-s35-adv/rc-main.txt ; echo "rc=$?"      # fresh vs stale artifact
rc=0
$ cmp /tmp/praxis-s35-adv/rc-main.txt /tmp/praxis-s35-adv/rc-parked.txt ; echo "rc=$?"
rc=0
```

All `diff`/`cmp` families return rc=0 with no output, and the fresh vector reproduces the
stale session-35 artifact exactly — so the two runs are the same experiment, not two
different ones agreeing by luck.

### 4.4 Captured stderr byte-identical across three HEADs — 104 comparisons, 0 differing

Every one of the 52 cases had its stderr captured per HEAD (`out/err-NNN-<slug>.bin`).

```
$ for n in $(seq -f "%03g" 1 52); do
    A="err-$n-main.bin"; B="err-$n-parked_Praxis_build-37h.bin"; C="err-$n-parked_anything-else.bin"
    cmp -s "$A" "$B"; r1=$?; cmp -s "$A" "$C"; r2=$?
    printf 'case %s  size=%-4s  cmp(main,parked/Praxis_build-37h) rc=%d  cmp(main,parked/anything-else) rc=%d\n' \
      "$n" "$(wc -c < "$A" | tr -d ' ')" "$r1" "$r2"
  done
case 001  size=214   cmp(main,parked/Praxis_build-37h) rc=0  cmp(main,parked/anything-else) rc=0
case 002  size=214   cmp(main,parked/Praxis_build-37h) rc=0  cmp(main,parked/anything-else) rc=0
case 003  size=0     cmp(main,parked/Praxis_build-37h) rc=0  cmp(main,parked/anything-else) rc=0
[… cases 004-051, every line rc=0 / rc=0; sizes 0 or 214 …]
case 052  size=214   cmp(main,parked/Praxis_build-37h) rc=0  cmp(main,parked/anything-else) rc=0
comparisons=104  differing=0
rc=0
```

Aggregate check over all 52 captures per HEAD:

```
$ for s in main parked_Praxis_build-37h parked_anything-else; do printf '%-26s ' "$s"; cat $(ls err-*-$s.bin | sort) | shasum -a 256; done
main                       6e5486ed58a111d91478b06e77aba8af19fabd1792a2fc6f31a085e3a77d4706  -
parked_Praxis_build-37h    6e5486ed58a111d91478b06e77aba8af19fabd1792a2fc6f31a085e3a77d4706  -
parked_anything-else       6e5486ed58a111d91478b06e77aba8af19fabd1792a2fc6f31a085e3a77d4706  -
rc=0
```

Note the deny message is a fixed **214 bytes** and never names a branch, a ref, or the
repo — so there is not even a channel through which a branch name could leak into the
output.

### 4.5 "No branch-reading construct executes anywhere in the script's path" — layered

This is a claim about **MECHANISM**, and it must not rest on a source read. It is carried
by behavioural evidence first; the grep is corroboration only.

**(a) Behavioural — PRIMARY.** §4.3 and §4.4 *are* the evidence: across three different
HEADs with byte-identical payloads, all 52 exit codes and all 52 stderr captures are
byte-identical, aggregate sha256 `6e5486ed…d4706` for all three. If any construct in the
executed path read the branch name, these would have to differ.

**(b) Behavioural — EXECUTION TRACE.** The `bash -x` trace of the DENY path shows the
complete set of `git` invocations that actually run: exactly one, `git diff --cached`.

```
$ bash /tmp/praxis-s35-repair2/trace.sh
gate rc=2
$ grep -nE '^\+{1,3} (cd [^ ]* && )?git ' /tmp/praxis-s35-repair2/out/trace.err
6204:++ git diff --cached
rc=0
$ grep -cE 'abbrev-ref|symbolic-ref|refs/|for-each-ref|rev-parse|--branch' trace.err
1
rc=0
$ grep -nE 'abbrev-ref|symbolic-ref|refs/|for-each-ref|rev-parse|--branch' trace.err | cut -c1-120
68:+ _c='/bin/zsh -c source /Users/admin/.claude/shell-snapshots/snapshot-zsh-1785091652314-qt344v.sh 2>/dev/null || tru
rc=0
$ grep -nE 'abbrev-ref|symbolic-ref|refs/|for-each-ref|rev-parse|--branch' trace.err | grep -v '_c='
rc=1  (rc=1 == none)
```

The single raw match is **not** a git invocation: it is the `_c=` variable in
`is_claude_pid()` holding the output of `ps -o command=`, i.e. the outer harness command
line echoed into the trace. Excluding those `ps`-capture lines leaves zero matches (rc=1).
For an admitted shape the trace is 20 lines and runs no `git` at all (§3.3-A, `grep rc=1`).
So the deny path reaches git exactly once; the admit path never reaches it.

**(c) SOURCE-READ — corroborating only, not an observation.** Grep of the live 180-line
script, run first-hand in the repair unit against the real file rather than the copy:

```
$ shasum -a 256 .claude/hooks/gate-commit.sh
b3de1137bff3b05a259d11b65eedd69681823626d290d68916e144fef3c330ef  .claude/hooks/gate-commit.sh
rc=0
$ wc -l < .claude/hooks/gate-commit.sh
     180
rc=0
$ grep -nE 'branch|abbrev-ref|symbolic-ref|refs/|HEAD|parked|for-each-ref|rev-parse' .claude/hooks/gate-commit.sh
grep rc=1
```

`rc=1` — no match anywhere in the 180 lines. There is no bead-id special-casing and no
`parked/` prefix handling.

**Bounded conclusion (S2).** *For every input in this 52-case vector, on these three HEADs,
the gate's exit code and stderr are invariant under the branch name.* That is the strongest
statement the method supports; it is **not** a proof over all possible inputs. Within that
bound, the gate cannot tell a park commit from a `main` commit, and therefore cannot be the
component that admitted one.

### 4.6 The "22 differing cases" correction, itself CORRECTED

Round 1 recorded that an earlier parked-branch run "appeared to show 22 differing cases",
and blamed a `| head -20` SIGPIPE truncating the driver. **The mechanism reproduces. The
number does not.**

```
$ bash a4_driver.copy.sh parked/Praxis_build-37h > a4/full.out 2>&1; echo "driver rc=$?"
driver rc=0
$ grep -oE "^rc=[0-9]+" a4/full.out > a4/rc-full.txt; wc -l a4/rc-full.txt
      52 a4/rc-full.txt
rc=0

$ bash a4_driver.copy.sh parked/Praxis_build-37h 2>&1 | head -20 > a4/head20.out
$ echo "PIPESTATUS: driver=${PIPESTATUS[0]}  head=${PIPESTATUS[1]}"
PIPESTATUS: driver=141  head=0   (141 = 128+13 = SIGPIPE)
$ grep -oE "^rc=[0-9]+" a4/head20.out > a4/rc-head20.txt; wc -l a4/rc-head20.txt
       6 a4/rc-head20.txt
rc=0

clean cases : 52
piped cases : 6
missing     : 46

$ diff a4/rc-full.txt a4/rc-head20.txt | grep -c "^[<>]"
46
diff-count rc=1
```

**The stray `rc=1` explained, since it otherwise looks like an inconsistency:** `grep -c`
printed 46 and therefore exited **0**, so the `rc=1` cannot be grep's. It is the *pipeline's*
status: with `pipefail` in effect the pipeline takes the upstream `diff`, which exits 1
whenever the two files differ — as they do here, by 46 lines. That is the only reading
consistent with both numbers, and it is offered as an **inference** about the harness shell's
options rather than a captured `set -o` dump. Either way the `rc` does not qualify the count
of 46; readers who prefer not to rely on the inference should treat the `rc` as stray and
disregard it.

`driver=141` is SIGPIPE (128+13): `head -20` closes the pipe, the driver's next `printf`
kills it mid-sweep, and a naive `diff` then reports the unreported cases as "differing".
The **mechanism is confirmed** as instrumentation truncation, not gate behaviour.

**But the figure is 46, not 22.** On re-run only **6 of 52** cases are reported, i.e. **46**
missing. 22 was a function of how much output that one particular run emitted before the
pipe closed, and is not a reproducible quantity. It is therefore attributed here to that
single run and carried no further. **This does not weaken the correction — it strengthens
it: 22 was never a measurement of the gate at all**, and neither is 46; both are
measurements of a pipe.

The clean, unpiped re-run is identical between HEADs:

```
$ bash a4_driver.copy.sh main > a4/full-main.out 2>&1; echo "driver rc=$?"
driver rc=0
$ wc -l a4/rc-full-main.txt a4/rc-full.txt
      52 a4/rc-full-main.txt
      52 a4/rc-full.txt
     104 total
rc=0
$ cmp a4/rc-full-main.txt a4/rc-full.txt ; echo "rc=$?"
rc=0
$ diff a4/rc-full-main.txt a4/rc-full.txt ; echo "rc=$?"
rc=0
```

Recorded at this length because a suppressed near-miss is exactly the kind of thing that
later gets cited as evidence.

---

## 5. Option space for Amear — enumerated, UNRANKED, no recommendation (S8)

These are the mechanically possible shapes, with what each costs and what each
weakens. **The choice is Amear's.** They are listed in arbitrary order and the
ordering carries no meaning. Some are combinable; that too is Amear's call.

**O1 — Ratify the human-executor step.** Amend park-rule step 1 to state
explicitly that the park commit is performed by a human in a terminal, and that
the orchestrator's obligation ends at *stage + branch + notify + stop*.
*Cost:* a rubric edit in a cold session (the between-sessions rule applies).
*Weakens:* nothing in the gate. *Note:* this ratifies what session 34 already
did — the paste at 18:46:02Z and `HANDOFF.md` on the park branch both already
describe this flow, so the rule would be catching up to practice. It leaves the
park un-completable while the human is absent, i.e. a session that hits
audit-fail-x2 unattended stops with work staged and unbranched.

**O2 — Give the gate a park-mode exemption.** Add a branch/subject-scoped
allowance so an armed orchestrator can commit to `parked/*` without a token.
*Cost:* an edit to an enforcement hook, plus trip tests for the exemption and
for its boundary. *Weakens:* the invariant that every commit in an armed repo
carries an audit token. `parked/*` is cheap to name — an orchestrator that can
commit un-audited to *some* branch has a shape it can be wrong about, and the
gate would then need to prove `parked/*` never merges to `main` by some other
mechanism, which does not exist today.

**O3 — Let the auditor mint a park-specific token.** Introduce a distinct
grade (e.g. PARK) that mints a token whose scope is a `parked/*` commit only.
*Cost:* changes to `audit-approve.sh`, `AUDIT_LOG.md` row schema, and the
auditor's contract; S12 applies — the writer would need its flushing counterpart
in the same change. *Weakens:* the current one-bit meaning of an `AUDIT_LOG`
PASS row; a log grep would no longer answer "was this audited" without also
reading the grade.

**O4 — Drop step 1's commit requirement.** Park = stage + branch + notify +
stop, with the work left staged and the branch created but empty.
*Cost:* trivial rubric edit. *Weakens:* durability. Staged-but-uncommitted work
survives nothing — not a crash, not `git checkout`, not another session
touching the shared index (the exact 2026-07-10 incident the single-session rule
exists for). This is the state 8sw *believed* session 34 was left in.

**O5 — Close 8sw as mis-stated and file the real defects separately.** The bead's
premise ("in direct conflict", "left staged but uncommitted") is falsified; the
underlying facts are (a) step 1 is unexecutable by the orchestrator and (b) the
gate has admitted shapes unrelated to parking.
*Cost:* bead hygiene only. *Weakens:* nothing, but it defers rather than
resolves — (a) still needs one of O1–O4.

**O6 — Do nothing.** *Cost:* zero now. *Weakens:* the park rule stays a rule
whose step 1 fails every time it fires, and the workaround stays undocumented in
committed text, surviving only in a transcript and a shell history file — both
outside the repo, neither backed up, both of which this investigation had to
reach outside version control to find.

**Explicitly not answered here:** which of these Amear should take, whether the
admitted shapes in §3.3 are urgent, and whether the false `DECISION_LOG` row
noted in §1 warrants a correcting append. All four are his.

---

## 6. UNVERIFIED — stated plainly

1. **S9 on the hook *registration* is only half-done. UNVERIFIED. Carried as
   `Praxis_build-sk8` (P1, OPEN).** The arming marker was positive-controlled in both
   directions on two independently built harnesses (§3.2, §2.4) and that half is
   **discharged**. The **registration field** — `hooks.PreToolUse[].matcher` and the hook
   `command` path in `.claude/settings.json` — was **not** given an invented-key negative
   control, because hard limit 1 forbids editing `settings.json`. What *was* observed: a
   `PreToolUse` hook registered in a throwaway repo's own `.claude/settings.json` produced
   **byte-identical silence** for a tool call with cwd inside that repo, while the same
   sentinel script fired correctly when invoked directly. That establishes hooks come from
   the **session's** project settings, not the cwd's. It does not substitute for the
   invented-key control on the real file.
   Two further admissions round 1 did not make:
   - **The totality of the obstruction was asserted, not established.** Round 1 said the
     control could not be run *at all*. Nobody enumerated the alternative positions at
     which an equivalent-position control might have run before concluding there were
     none. The honest statement is: *the only position we identified for the control is
     the file the brief forbade*, which is weaker than "no such position exists."
   - It is undischarged because of the **brief's limit**, not because of an absence of
     method. The method is known and is written into `Praxis_build-sk8`, which carries the
     toggle experiment; it needs a unit with authority to touch `settings.json`, or
     Amear's hand. **No attempt was made here, and `.claude/settings.json` was not
     edited.**
2. **Exclusivity of the 18:32:35Z denial.** The `tool_result` names
   `gate-commit.sh` and carries its line-179 string, and path↔text pairing was
   shown faithful by instrumented dual-deny probes. What is **not** established
   is that no *other* hook also denied and lost the print race. Per the standing
   masking rule, the attribution is sound; the exclusivity is not.
3. **"The very same park commit" is imprecise.** The denied tool call and
   `104c58e` share a subject line but are different commits — the denied one
   carried a long body and a `Co-Authored-By` trailer; `104c58e`'s body is empty.
   The gate denied *an attempt at the same park*, not the byte-identical object.
4. **Deny semantics in the copy harness.** Direct invocation proves the script
   *exits 2*. It does **not** prove exit 2 blocks anything — that is proven only
   by the live tests in §2.1/§2.2, which used the real registration.
5. **Never tripped, therefore untested:** the single-session `lsof` check (it
   passed vacuously in every run), the 30-minute token expiry, and the
   orphaned-token sweep. `S2` applies: these are *specified and implemented*,
   not *tested*, and certainly not *tested under failure*.
6. **`notify.sh` delivery.** It POSTs and exits 0 unconditionally and writes no
   local artifact, so an `exit=0` in a session log proves **execution, not
   delivery**. Whether the `audit-fail-x2` notification actually reached Amear
   on 2026-07-26 is unverified from inside this repo.
7. **The literal `agent_type` value** in a live payload was never captured this
   session. Only "non-empty and not main-thread `praxis-master`" is proven from
   observed behaviour.
8. **Transcript completeness.** The 18:41:08Z–18:46:01Z tool-use gap is an
   absence of evidence. It corroborates (B); it does not carry it. The finding
   rests on the **positive** artifacts: the plain-string record at 18:46:02Z and
   the `~/.zsh_history` epoch match.
9. **`~/.zsh_history` is not tamper-evident.** It is a plaintext file any
   process can append to. The epoch match with `%at`/`%ct` is strong
   corroboration, not proof of human authorship.
10. **`HANDOFF.md:5` is a plan, not a witness.** It was written *before* the
   commit it describes and committed inside `104c58e`. It evidences **intent and
   instruction** — that a human executor was the planned mechanism — and it
   corroborates that mechanism. It does not observe the act. §1(vi)'s earlier
   "four mutually independent artifacts" framing is withdrawn there; two of the
   four (the 18:46:02Z pasted terminal block and the `~/.zsh_history` epoch)
   originate in the **same terminal session** and are not independent of each
   other. Authorship of `104c58e` is **corroborated, never proven**, and the (B)
   verdict does still rest partly on a file outside version control.
11. **The token-present code path of `gate-commit.sh` was never traced in the
   real repo.** §4.5(b)'s branch-name-invariance result covers the 52 swept
   inputs, none of which carried a valid token; line 170 runs a second `git`
   (`git write-tree`) on the token-present path, and that path's invariance is
   **not** established. See §4.5(b).
12. **"A `PreToolUse` hook does not bind a human shell" was NOT tested.** This
   premise carries the (B) verdict and the `599885e` disposition, so it is named
   here rather than left implicit. It is **highly plausible** — indeed it is the
   standard reading of what a `PreToolUse` hook *is*: it fires on Claude Code
   tool-use events, and a command typed into the user's own terminal is not a
   tool-use event. Nothing in this report contradicts it, and the live trip tests
   in §2.1 and §2.4 do show the hook binding **agent Bash tool calls**.
   **But plausible is not tested.** No experiment in this document runs a commit
   from a human shell with the gate armed and observes it succeed; §2.2, which
   round 1 cited as establishing the boundary, explicitly disclaims itself on the
   point ("it is *not*, on its own, a proof about human terminals"). This
   project's own rubric holds that a mechanism named in a comment or in a report
   is a **claim to be graded by experiment, not by inspection** — and by that
   standard this one is ungraded. Every place the premise is used is now labelled
   an inference (§1(vi), the S6 cross-block section, the `599885e` subsection,
   "Files staged" item 4). Closing it needs one live test with the gate armed, run
   from Amear's own terminal, which this unit has no authority to perform.

---

## 7. Fidelity gap — `/tmp` reproduction vs. the real registration

**The single load-bearing gap: a `/tmp` throwaway repo cannot reproduce the real
registration at all — only the hook's internal logic.** Observed in R4: hooks are
loaded from the **session's** project settings (`$CLAUDE_PROJECT_DIR`), so a
`PreToolUse` hook registered in a throwaway repo's own `.claude/settings.json`
never fires for tool calls made with cwd inside it. Whether it is "never
consulted" or "loaded once at session start" was not separable; the conclusion
holds either way, but the **mechanism is UNVERIFIED**.

Consequences, stated so no claim is read above its evidence:

- Every "DENY" in the copy-driven sweep (§2.3, §3.3, §4) means precisely **"the
  script exited 2"**. It does not mean "the tool call was blocked".
- **The cap runs in both directions.** Every "ADMIT"/"ALLOW" in the copy-driven
  sweep means precisely **"the script exited 0"**. It does **not** mean "the tool
  call was permitted", "the commit went through", or "the gate has a hole" in the
  end-to-end sense. A hook returning 0 is a necessary but not sufficient
  condition for the runtime to dispatch the command to a shell, and that
  dispatch step was **never exercised** in this report — for any shape, admitted
  or denied. §3.3's admitted shapes are therefore reported as *script-logic*
  results only. Round 1 stated this cap for DENY results alone; the asymmetry let
  an over-claim ("the gate has holes") through, and is corrected here.
- The copy is proven byte-identical by `sha256` + `cmp`, so the **logic** results
  transfer with confidence. The **enforcement** results do not.
- The payload shape used to drive the copy was taken from the dispatch brief, not
  captured from a live hook invocation. Hard limit 1 forbade adding a
  raw-stdin capture line to the real hooks, which is the project's standing
  remedy for exactly this.
  **Mitigation, stated on the right basis.** No conclusion in this report depends on a
  payload field because **the script reads no top-level payload field at all** — only
  `tool_input.command` (line 29) and the *environment* variable `CLAUDE_PROJECT_DIR`
  (line 57), shown by the `grep` in §3.1.6. The 25-variant well-formed field sweep then
  confirms that behaviourally. The ordering matters: "byte-identical output" is **not** the
  load-bearing argument, and on its own it is a weak one, because two payloads that merely
  fail to parse produce byte-identical output for free (§3.1.6, `cmp` rc=0 on two malformed
  payloads differing in four fields). Round 1 rested this mitigation on byte-identical
  output alone, and cited a sweep that had never varied the fields; both are corrected.
  `hook_event_name` is scoped the same way — it does not matter **to the script** and does
  not appear in its source, which is not a claim about the runtime's event routing.
  **What is still missing is unchanged:** a real live payload has never been captured in
  this project. The field names tested are constructed guesses, so the sweep cannot rule
  out a field the runtime sends under a name nobody guessed. The reason the negative
  survives that gap is mechanical, not statistical — the script reads no top-level field,
  so an unguessed name would be ignored exactly as the guessed ones were.
- What closes the gap: §2.1 and §2.2 were run against the **real** registration
  in this live session. The deny in §2.1 and the non-deny in §2.2 are enforcement
  observations, not logic simulations. Those two, plus the two transcript
  records and the `zsh_history` epoch match, are what the (B) verdict rests on.
  The `/tmp` work supports §3 and §4 only.

---

## S6 cross-block check

`specs/SPEC_RUBRIC.md` S6: *"every approved deviation is tested against the specs
of every other block it touches, not only its own."*

No deviation was approved or executed in this unit — it is read-only
investigation. Checked for collateral impact anyway:

- **Park rule (Process rulings) ↔ S7** (*"Nothing is committed while any audit box
  is unchecked"*): these are the two rules genuinely in tension. The gate is S7's
  enforcement. Any option that lets the orchestrator commit un-audited to
  `parked/*` (O2, O3) is an S7 amendment whether or not it is written as one.
  Flagged, not decided.
- **Park rule ↔ "Absolutes are amended between sessions only"**: 8sw is being
  investigated in a session that is *not* blocked on the parked work, and this
  report proposes no amendment. Compliant.
- **↔ single-session rule** (`docs/runbooks/2026-07-10-single-session-rule.md`):
  the gate's `lsof` check passed in every observation, but it was never tripped —
  see §6 item 5. Untested, not broken.
- **↔ S12**: option O3 would add an `AUDIT_LOG` writer variant and therefore
  inherits S12's requirement that the flushing counterpart ship in the same
  change. Noted in §5.
- **↔ S10/S11**: untouched. No frontmatter, allowlist, or nesting change.
- **↔ Blocks 1–5 (trading path)**: no signal-path, breaker, or NinjaScript
  artifact was read or modified. No impact.
- **↔ S7, via commit `599885e`** (*"Nothing is committed while any audit box is
  unchecked"*): this is the cross-block item S6 exists to catch, and it arose **during**
  this report's own audit. This report file was committed to `main` as `599885e` by a
  human terminal paste while the audit box on it was unchecked — the audit had returned
  FAIL, and a second audit round was in progress. That is an **S7** matter on its face. It
  is **not** an S6 deviation-test failure, and on an explicitly labelled **inference** it is
  not a gate hole either: the gate was armed, and a `PreToolUse` hook is inferred not to bind
  a human shell. That inference is **untested here** — the live trip tests show the hook
  binding *agent tool calls* only, no experiment in this document exercises a human shell,
  and §2.2 disclaims itself on the point. Recorded as §6 item 12. Full pasted evidence and the explicit
  non-repair are in **"Files staged"**. Flagged across blocks here because an S7 breach
  reached `main` while this document was the artifact under audit, and because it is
  live *evidence* bearing on §5's option space. Disposition is the master's and Amear's.

---

## Files staged

**Round 1 of this section said the staged set was this one report file. That is no longer
true, and the reason is a new finding.** Observed present state, pasted:

```
$ git -C /Volumes/Sensidine/Praxis.build status --short
 M .claude/settings.json
 M AUDIT_LOG.md
 M DECISION_LOG.md
 M DISPATCH_LOG.md
?? .claude/agent-memory/
?? docs/reports/2026-07-26-session34-manifest-amendment.md
?? docs/reports/2026-07-26-session34-p0-flush-audit.md
?? docs/reports/2026-07-26-session35-8sw-audit-round1.md
rc=0

$ git -C /Volumes/Sensidine/Praxis.build diff --cached --name-only
(no output)
rc=0
```

The staged set is **empty**. This report file appears in neither the staged nor the
untracked set, because it is now tracked at `HEAD`. The repair unit's edits to it leave it
as an unstaged working-tree modification; **the repair unit staged nothing.**

The four ` M` ledger entries are pre-existing and were not touched:
`scripts/dispatch-log-writeahead.sh` appends to `DISPATCH_LOG.md` automatically on
`SubagentStart`, and the `DECISION_LOG.md` delta is the **master's** own 18:52Z dispatch
row. **No worker in this unit, in round 1 or in the repair, edited any repo file** other
than this report. They wrote to `/tmp` and to the session scratchpad only.

### The DISPATCH_LOG row count: round 1 said four, it was five

The mechanical count, and the diff:

```
$ git diff -- DISPATCH_LOG.md | grep -c '^+[^+]'
13
rc=0
$ git diff -- DISPATCH_LOG.md | grep -c '^+.*WHAT: subagent spawned'
12
rc=0
$ git diff -- DISPATCH_LOG.md | grep '^+.*WHAT: subagent spawned' | sed -E 's/^\+- \[([^]]*)\] WHO: ([^|]*)\|.*/\1  \2/'
2026-07-26T18:52:19Z  praxis-manager
2026-07-26T18:54:49Z  praxis-worker
2026-07-26T18:55:27Z  praxis-worker
2026-07-26T18:56:00Z  praxis-worker
2026-07-26T19:02:08Z  praxis-worker
2026-07-26T19:18:30Z  praxis-auditor
2026-07-26T19:48:35Z  praxis-manager
2026-07-26T19:50:08Z  praxis-worker
2026-07-26T19:50:37Z  praxis-worker
2026-07-26T19:51:04Z  praxis-worker
2026-07-26T20:04:19Z  praxis-worker
2026-07-26T20:11:41Z  praxis-worker
rc=0
```

The report's own mtime pins what the count was when round 1 was written:

```
$ ls -lT docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
-rw-r--r--@ 1 admin  staff  32020 Jul 26 15:16:40 2026 docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
rc=0
```

Local offset is `-0400`, established from git's own record of a commit made in this same
window (`authored=2026-07-26T15:51:31-04:00`, below). So round 1 was last written at
**19:16:40Z**, and the spawn rows at or before that moment are five, not four:

```
2026-07-26T18:52:19Z  praxis-manager   <-- the fifth row round 1 did not count
2026-07-26T18:54:49Z  praxis-worker
2026-07-26T18:55:27Z  praxis-worker
2026-07-26T18:56:00Z  praxis-worker
2026-07-26T19:02:08Z  praxis-worker
```

**The uncounted fifth row is the `praxis-manager`'s own `18:52:19Z SubagentStart` row.**
Round 1 counted the four `praxis-worker` spawns and omitted the manager, because the
manager is the thing that *did* the dispatching and so was not thought of as itself having
been dispatched. The hook makes no such distinction — it fires on every `SubagentStart` and
reads `.agent_type` off the payload with no filter:

```
$ cat -n scripts/dispatch-log-writeahead.sh
     1	#!/bin/bash
     2	# SubagentStart hook: writes the DISPATCH_LOG row mechanically.
     3	# Write-ahead discipline stops depending on the agent remembering.
     4	INPUT=$(cat)
     5	AGENT=$(echo "$INPUT" | jq -r '.agent_type // "unknown"')
     6	TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
     7	LOG="${CLAUDE_PROJECT_DIR:-.}/DISPATCH_LOG.md"
     8	[ -f "$LOG" ] || echo "# DISPATCH LOG" > "$LOG"
     9	echo "- [$TS] WHO: $AGENT | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session $(git -C "${CLAUDE_PROJECT_DIR:-.}" rev-parse --short HEAD 2>/dev/null || echo no-git) | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched" >> "$LOG"
    10	exit 0
rc=0
```

`praxis-master` runs on the main thread and is not a subagent, so it emits no write-ahead
row — which is why the master's presence in the ledger is the separate, hand-written 18:52Z
outcome row (the one non-`subagent spawned` added line, hence 13 added lines vs 12 spawn
rows).

**THE COUNT IS NOT A STABLE QUANTITY, and any report quoting it must timestamp the
observation.** It was 4 as claimed, 5 in fact at 19:16:40Z, 10 spawn rows when the repair
unit's forensic worker measured it, 11 at the manager's own later count, and **12 spawn
rows / 13 added lines at the moment the block above was run**. The ledger grows because
this session keeps spawning workers and every spawn appends a row — including the
`19:18:30Z praxis-auditor` row, whose own spawn appended a line to the very file whose row
count it was auditing.

One further honesty note: the `18:52Z` master outcome row is *timestamped* 18:52Z but was
**written later**. Its text quotes the auditor verdict, which cannot predate the 19:18:30Z
auditor spawn. It carries the dispatch time, not the write time.

`DISPATCH_LOG.md` was **not** staged, edited, or reverted by this unit.

### The report was committed to main during its own audit

```
$ git rev-parse HEAD
599885e9a381310ec023600a560b1455f5468974
rc=0
$ git status -sb | head -1
## main...origin/main [ahead 1]
rc=0
$ git diff --cached --name-only
(empty)
rc=0
$ git log -1 --format='author=%an <%ae>%nauthored=%aI%nsubject=%s%nBODY>>>%b<<<END' 599885e
author=Amear Bani-Ahmad <amear238@users.noreply.github.com>
authored=2026-07-26T15:51:31-04:00
subject=park(<bead-id>): audit-fail-x2, session ended per absolute park rule
BODY>>><<<END
rc=0
$ git show --stat --format='%h %s' 599885e
599885e park(<bead-id>): audit-fail-x2, session ended per absolute park rule

 .../2026-07-26-session35-8sw-gate-park-conflict.md | 611 +++++++++++++++++++++
 1 file changed, 611 insertions(+)
rc=0
```

The 611-line report — the file the brief says must be the sole staged item — is committed
on `main`, one commit ahead of `origin/main`, unpushed. The session started at `c1dec30`;
`main` has moved.

Facts, each pasted, none inferred:

- **The commit subject carries an unfilled literal placeholder** — `park(<bead-id>)`, not a
  bead id — **and an empty body** (`BODY>>><<<END` above encloses nothing).
- The `~/.zsh_history` epoch matches the commit's `%at`/`%ct` exactly, and line 1510 is
  that exact `git commit -m` string, placeholder and all:

```
$ git log -1 --format='%at %ct' 599885e
1785095491 1785095491
rc=0
$ date -u -r 1785095491 +%Y-%m-%dT%H:%M:%SZ
2026-07-26T19:51:31Z
rc=0
$ LC_ALL=C awk 'NR>=1500 && NR<=1512 {printf "%d\t%s\n", NR, $0}' ~/.zsh_history
1500	: 1785091551:0;cd /Volumes/Sensidine/Praxis.build\
1501	git branch --show-current          # must say parked/Praxis_build-37h\
1502	git add HANDOFF.md\
1503	git status --short                 # .claude/settings.json must NOT be staged\
1504	git commit -m "park(Praxis_build-37h): audit-fail-x2, session ended per absolute park rule"\
1505	git checkout main                  # main stays at c1dec30
1506	: 1785091624:0;claude --dangerously-skip-permissions
1507	: 1785095491:0;Volumes/Sensidine/Praxis.build\
1508	branch --show-current      # MUST print parked/<bead-id>  � if it says main, stop\
1509	status --short             # read this before committing, not after\
1510	git commit -m "park(<bead-id>): audit-fail-x2, session ended per absolute park rule"\
1511	git log -1 --format=%H main    # confirm main did NOT move\
1512	git checkout main
rc=0
```

(The `�` on line 1508 is an em dash the `LC_ALL=C` read could not decode — a byte artefact
of the reading method, not of the file.)

- **The paste was mangled.** Line 1507 reads `Volumes/Sensidine/Praxis.build\` — the
  leading `cd /` was **eaten**, so the block's first command failed and every subsequent
  line ran in whatever directory the shell was already in, which was the repo root on
  `main`. Lines 1508 and 1509 lost their leading `git` (`branch --show-current`,
  `status --short`), so **the guard never executed.** Compare the intact paste at lines
  1500-1505, where `cd` and both `git` prefixes survived.
- **The guard was in the paste and did not stop it.** Line 1508 reads
  `MUST print parked/<bead-id> — if it says main, stop`. The branch **was** `main`. A
  comment in a pasted block is not a check.
- **The gate WAS armed at the time**, verified first-hand, so this is not a case of a
  disarmed hook:

```
$ test -f .claude/state/orchestrator-active && echo "present"
present
rc=0
$ ls -lT .claude/state/orchestrator-active
-rw-r--r--@ 1 admin  staff  0 Jul 26 09:53:55 2026 .claude/state/orchestrator-active
rc=0
```

**This is not a gate hole — on an explicitly labelled INFERENCE, not a tested result.**
The inference is: `gate-commit.sh` is registered as a `PreToolUse` hook, and a `PreToolUse`
hook binds Claude Code **tool calls**, so it has no reach into a human's own shell. What
actually supports that: the live trip tests in §2.1 and §2.4 show the hook binding **agent
Bash tool calls** (deny text returned, no shell exit code). **No experiment anywhere in this
document exercises a human shell.** §2.2 is often cited for this and does not carry it — §2.2
disclaims itself in its own text ("it is *not*, on its own, a proof about human terminals");
what §2.2 establishes is matcher behaviour on the command string, which is a different
claim. The premise is recorded as **§6 item 12 (UNVERIFIED)**. On that inference, an armed
gate and a human-executed commit are not in contradiction; that is the finding of §1.

Stated without ranking or recommendation (S8):

- This is a **second live instance** — on `main` rather than a park branch — of the
  human-executor step that §1 found to be undocumented anywhere in the park rule. It
  occurred **while the report describing it was being audited**, and it reproduces the same
  signature: empty body, a subject no transcript contains, a `zsh_history` epoch equal to
  the commit timestamp, and no `PreToolUse` hook in the path.
- It means an **un-audited artifact reached `main`**, which is an **S7** matter (*"Nothing
  is committed while any audit box is unchecked"*). Cross-referenced in the S6 section.
- **Reported, not repaired.** This unit did not stage, edit, revert, reset, amend,
  cherry-pick, branch, check out, or move anything. `main` is left one commit ahead of
  `origin/main`, unpushed, exactly as found. Whether `599885e` stands, is amended, or is
  moved off `main` is **the master's and Amear's call, not this unit's** (S8).
- It bears on §5's option space as **evidence** — notably O1's human-executor ratification
  and O6's "do nothing", since the undocumented workaround has now fired twice in one day,
  the second time onto `main` with an unfilled placeholder. The ranking remains Amear's;
  nothing here ranks it.

Worker evidence files (outside the repo, not staged):
- `<scratchpad>/w1-forensics.md`
- `/tmp/praxis-s35-gatelogic/w2-findings.md`
- `/tmp/praxis-s35-reach/w3-findings.md`
- `/tmp/praxis-s35-adv/w4-adversarial.md`

Repair-unit evidence files (outside the repo, not staged):
- `/tmp/praxis-s35-repair/` — §2.3 and §3.2 drivers and captures
- `/tmp/praxis-s35-repair2/` — §3.3 and §4 drivers and captures
- `/tmp/praxis-s35-payloadfields/` — §3.1.6 well-formed payload-field sweep

---

## Round-1 audit corrections

Round 1 of this document was audited and returned **FAIL on S1 and S9**. The auditor's
summary was: *"Substantive finding is sound; evidentiary discipline is not."* The (B)
verdict in §1 passed audit and was independently re-verified; it is not relitigated here.

This project's ledgers are append-only on purpose — a wrong call stays on disk beside its
correction, so nobody has to reconstruct from a clean surface what was actually believed
and when. The same rule is applied to this report. Each item below gives **what round 1
said → what it says now → why it was wrong.**

**The five audit findings.**

1. **§2.3, §3.2, §3.3 and §4 carried zero pasted command output.**
   *Round 1:* those sections summarised results in prose — "`cmp` clean", "exits 2",
   "byte-identical" — with no transcript, no command, no exit code.
   *Now:* each carries the fenced transcript that produced it, with the invocation and its
   rc. §2.3 has the 8/8 deny cells with payload + rc + stderr + byte count, the `-am` FORM
   vs TOKEN contrast with `diff` rc=1 and `cmp` rc=1, and all four token-path cells. §3.2
   has all three S9 cells and all three `cmp` invocations with rc. §3.3 has the 8/8 admits
   against 2/2 contrast denies plus the `bash -x` traces. §4 has the 52-case table, the 104
   stderr comparisons and the aggregate sha256s.
   *Why it was wrong:* S1 is not a request for accurate summaries. A description of output
   cannot be checked by a reader; a transcript can. The investigation had been done — the
   artifact simply did not carry it.

2. **The sentence "Pasted command output only. Nothing in this section is a description of
   output" was FALSE AS WRITTEN.**
   *Round 1:* it sat at the head of §2, immediately above a §2.3 that contained no output
   at all.
   *Now:* replaced with a claim that is true of the repaired section, and the error is
   pointed at rather than deleted.
   *Why it was wrong:* it was a compliance assertion standing in for compliance. That is a
   worse defect than the missing transcripts, because it would have deterred a reader from
   checking.

3. **S9 registration control: declared satisfied-in-part, with its obstruction asserted
   rather than shown.**
   *Round 1:* marked the registration field UNVERIFIED — correctly — but stated the hard
   limit made the control impossible, full stop.
   *Now:* still UNVERIFIED, carried as `Praxis_build-sk8`, and with the second half
   admitted: the **totality** of the obstruction was asserted, never established. Nobody
   enumerated the alternative positions before concluding there were none.
   *Why it was wrong:* "we could not do it" and "it cannot be done" are different claims,
   and only the first was evidenced. The arming-marker half is genuinely discharged and is
   now reproduced on two independently built harnesses (§3.2, §2.4).

4. **§1(v) omitted `--dangerously-skip-permissions`.**
   *Round 1:* claimed the (A)-shaped alternatives "were hunted and came back empty" while
   never naming the single most obvious bypass hypothesis.
   *Now:* closed in-report as §1(v-a), first-hand, with the launch→transcript linkage at
   1.796 s, the uniqueness sweep over the window, the offset table, the `sessionId` and
   `tool_use_id` linkage, and the `LC_ALL=C` method note.
   *Why it was wrong:* an exhaustiveness claim that has not enumerated its own most likely
   counterexample is not an exhaustiveness claim. **This hole was closed by the round-1
   AUDITOR, not by the round-1 report** — and the evidence in §1(v-a) was re-derived
   first-hand here rather than copied out of the audit.

5. **The DISPATCH_LOG delta was stated as four rows, with no diff pasted.**
   *Round 1:* "four rows, one per worker dispatched here."
   *Now:* it was **five** at report time (mtime 19:16:40Z); the diff and the mechanical
   counts are pasted; the uncounted fifth row is identified as the `praxis-manager`'s own
   `18:52:19Z SubagentStart` row; the write-ahead hook is pasted showing it reads
   `.agent_type` with no filter; and the drift to 12 spawn rows is stated with its cause.
   *Why it was wrong:* the number was reasoned about (one row per worker) rather than
   counted, and the reasoning omitted the manager — the agent doing the dispatching does
   not think of itself as having been dispatched. The hook does not share that blind spot.

**Four defects found during the repair itself — a different and more uncomfortable class.**

6. **NEW — §4's "22 differing cases" is not reproducible.** *Round 1:* an earlier
   parked-branch run "appeared to show 22 differing cases", explained as a `| head -20`
   SIGPIPE. *Now:* the **mechanism reproduces exactly** (driver `rc=141` = 128+13), but the
   figure does not — a fresh run leaves **6 of 52** reported, i.e. **46** missing.
   *Why it was wrong:* 22 was a function of how much output that one run emitted before the
   pipe closed. This does not weaken the correction, it strengthens it: **22 was never a
   measurement of the gate**, and neither is 46.

7. **NEW — §3.1 item 6's stated provenance was FALSE.** *Round 1:* attributed the
   payload-field negative to the §4 sweep. *Now:* that driver contains **zero** occurrences
   of `agent_id` and **zero** of `agent_type` (`grep -c` = 0), and never varies `cwd` (both
   occurrences pin it to the harness repo). Item 6 described a sweep that does not exist.
   The claim is re-evidenced on 25 well-formed payloads, every one proven to parse, and it
   **HOLDS** — on the new evidence, not the old.
   *Why it was wrong:* the conclusion was right and the citation was invented. Worse, the
   original method was structurally incapable of supporting it: the hook fails open, so
   byte-identical silence from non-parsing payloads is free.

8. **NEW — "every malformed payload exits 0 silently" is wrong for one case.** *Now:* the
   NUL-containing payload exits 0 but emits a **105-byte bash warning** on stderr from line
   28 (`ignored null byte in input`). The exit-code claim survives; the silence claim does
   not.
   *Why it was wrong:* "silently" was inferred from the aggregate, not read off each case.

9. **NEW — three sweep cases labelled as valid payloads are malformed JSON.**
   `mal-minimal-valid-commit`, `mal-toolname-Write` and `mal-event-PostToolUse` interpolate
   `CM='git commit -m "x"'` into hand-built JSON, so their inner quotes are unescaped and
   the payloads do not parse. Their rc=0 is **fail-open**, not "a valid payload was
   admitted". The label `minimal-valid-commit` names the intent of the case, not what it
   fed the script, and is flagged as misleading.
   *Why it was wrong:* the case name was trusted as a description of the case.

**The pattern, and it is worth stating plainly.** In every one of the **five audit
findings**, the underlying work had actually been done and the artifact did not carry it.
The defect was evidentiary form, not investigation — which is exactly why it was survivable
and exactly why it should not have shipped. **Items 6-9 are a different and more
uncomfortable class:** claims whose *stated basis* did not survive being checked, even where
the conclusion did. A conclusion that is right for a reason that turns out to be fictional
is not a small problem, because the fiction is what a future reader would rely on. Items 7
and 9 in particular were only caught by re-running the instrument against the real thing —
the same move that caught the fake-ledger defect disclosed in §2.3(d).

## Result: BLOCKED

**Read this line precisely — it is not a claim that the investigation failed.**

`Result: BLOCKED` is the honest token here, and it is forced by a real conflict
between two instructions in the same chain:

- The dispatch brief directs: *"do not grade your own work, and do not assert a
  PASS."*
- `scripts/gate-manager-output.sh` (SubagentStop, matcher `^praxis-manager$`)
  denies the manager's return unless the report carries
  `Result:\s*(PASS|FAIL|BLOCKED)`. Observed live this session:
  `BLOCKED: '…-8sw-gate-park-conflict.md' has no explicit Result:
  PASS|FAIL|BLOCKED line.`

`PASS` is forbidden by the brief. `FAIL` would be false — every experiment the
brief specified was run and every deliverable section is answered. `BLOCKED` is
the only remaining token, and it under-claims rather than over-claims, which is
the direction S2 requires.

**Read `BLOCKED` here as meaning: complete, and submitted for independent grading.** The
gate's vocabulary has no token for that state, and that vocabulary gap is filed as
`Praxis_build-fpg` (P3, OPEN). `BLOCKED` is therefore the closest available token, not a
description of the work.

**What is actually blocked, and on whom:**

1. **Grading.** This manager may not certify its own output, and cannot spawn
   `praxis-auditor` (tool-blocked, and structurally so). The master re-runs the
   verification and dispatches the auditor on the staged diff.
2. **The substantive question.** Which of the six options in §5 to take is
   Amear's cold ruling under S8. Nothing here decides it.
3. **One acceptance criterion is genuinely unmet and cannot be met from inside
   this unit — `Praxis_build-sk8` (P1, OPEN).** S9's invented-key negative control on the
   hook *registration* (`hooks.PreToolUse[].matcher` and the hook `command` path) can only
   run at one position: `.claude/settings.json`, which hard limit 1 forbids editing. No
   attempt was made. It is marked UNVERIFIED in §6 item 1 rather than papered over, and
   §6 item 1 additionally records that round 1's claim of a **total** obstruction was
   asserted rather than established. `Praxis_build-sk8` carries the toggle experiment. If
   the master wants S9 discharged on the registration field, that needs a unit with
   authority to touch settings, or Amear's hand. The arming-marker half **is** discharged
   (§3.2, §2.4).
4. **An un-audited artifact is on `main` and this unit will not move it.** Round 1 of this
   report was committed to `main` as `599885e` by a human terminal paste at 19:51:31Z,
   during its own audit, with an unfilled literal placeholder subject `park(<bead-id>)` and
   an empty body. The gate was armed; this is not a gate hole **on the inference** that a
   `PreToolUse` hook does not bind a human shell — an inference this document does not test
   (§6 item 12). It is an **S7** matter, evidenced in full in "Files staged"
   and cross-referenced in the S6 section. `main` is left one commit ahead of
   `origin/main`, unpushed, exactly as found. **Disposition — stand, amend, or move off
   `main` — is reserved to the master and Amear (S8). This unit did not repair it and did
   not stage anything.**

**Process defect surfaced by this line — filed as `Praxis_build-fpg` (P3, OPEN), not fixed
here.** The manager report contract and a brief that forbids self-grading are
mutually unsatisfiable as written: the Stop gate's vocabulary has no token
meaning *"complete, submitted for independent grading."* Every future
investigation-only manager unit will hit this and will have to choose between
asserting a PASS it was told not to assert and declaring a BLOCKED that
overstates the obstruction. The gate is deterministic and correct at what it
checks; the vocabulary is the gap. Hot-patching the hook is forbidden and was
not attempted.

Contract note for the auditor: the verdict in §1 is (B), stated as an
**observation**, resting on the live enforcement tests in §2.1/§2.2/§2.4, the two
transcript records, the `~/.zsh_history` epoch match, and the in-repo `HANDOFF.md` line at
§1(vi). The claims in §3.3
(admitted shapes) and §4 (branch indistinguishability) rest on a byte-identical
copy driven by direct invocation — **logic, not enforcement** — and are labelled
as such in §7. The only enforcement observations in this document are §2.1, §2.2 and the
manager's live trip test in §2.4; every copy-driven result is capped at "the script exited
N" and none is upgraded to "the tool call was blocked".

Repair-unit note: this round fixed **evidence form**, not the verdict. The nine items in
"Round-1 audit corrections" are the complete list of what changed and why. `599885e` is
reported and deliberately not repaired.
