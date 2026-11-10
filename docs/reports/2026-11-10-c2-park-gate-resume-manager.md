# C2 park-commit gate exemption, resume unit — manager report (unit 2026-11-10-c2-park-gate-resume, bead Praxis_build-8sw)

Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

(This unit states no backtest or P&L figure; the sentence is carried as house style under S13.)

## Task

Amear's C2 (DECISIONS.md:1826, D-2026-11-08-C), verbatim: "C2  Park rule amendment (made between sessions, per the absolutes rule): a park commit to parked/ branches is exempt from the audit-token gate, because it never touches main. Closes Praxis_build-8sw." D12 (DECISIONS.md:1961-1963, :1986) names "park-commit gate exemption (C2, trip-tested)". Master scoping: DECISION_LOG 2026-11-09T19:22:00Z items (1)-(5), 2026-11-10T05:13:00Z, 05:20:00Z.

The 2026-11-09 unit died (usage limit) leaving an UNAUDITED draft: gate +55/-1, rubric filer's note +22 claiming a trip test no report shows, MANIFEST rows :325-327. This unit verifies, trip-tests, corrects. Bead 8sw stays open (master closes after audit and live trip). Nothing committed, nothing added to the index.

## Rubric criteria addressed

S1, S2, S3, S4, S6, S9, S13 (specs/SPEC_RUBRIC.md :121-133).
- S1: every claim below rests on pasted output in "Verification evidence (command output)" or the final block F. Worker figures that I did not re-run are pasted from the worker's own log and labelled WORKER OUTPUT, NOT RE-RUN.
- S2: level reached = TESTED (synthetic): PreToolUse payloads piped to the hook in throwaway clones. Not live-tripped. **Live trip by the master pending.**
- S3: every arm tripped with the deny observed (T2-T12 below).
- S4: authority is C2/D12 plus the master's 19:22Z row; the design choices made here are labelled "decided by manager under D-2026-11-08-D D1" (they are inside C2's words; nothing wider is built).
- S6: cross-block check below (other PreToolUse hooks, PostToolUse commit-tree-verify.sh, Stop/SessionStart/PreCompact grep).
- S9: toggles: (a) exemption allow block removed from a scratch copy -> T1 flips 0 -> 2, T2 unchanged; (b) X3 block removed -> T11 flips 2 -> 0; (c) pre-edit copy -> T11/T12 allow, final bytes deny.
- S13: the sentence is carried once, at the top.

## Workers dispatched (id, mode, outcome)

| id | agent | mode | outcome |
|---|---|---|---|
| W1 | aaecc207768c1d5f7 | BUILD (trip harness `/tmp/c2trip-w1/harness.sh`) | 127 cases, 0 real mismatches on draft bytes 809a6605...65ac; no defect found; noted re-read asymmetry |
| W2 | a6bb7003a8d78bff2 | ADVERSARIAL | no result: stopped by a safety classifier after 3 tool calls; nothing run |
| W3 | a3e2e25fb2d4f988e | BUILD (observation) | never-touches-main routes, GitHub reads, S6 cross-block; found commit-tree-verify false alarm (B2) |
| W2b | a7537be8e7c830ed5 | ADVERSARIAL (re-dispatch, reworded) | counterexamples X1, X2 (pre-existing class), X3 (new code), T1 race |
| W4 | aae960bbb66b5a45a | BUILD (fix) | X3 fix + symmetric re-read in the gate; harness2 with T11/T12; 0 mismatches |
| W5 | a9defc1948a60b4ee | ADVERSARIAL (final bytes 8471206f...c19f, artifact + criterion only) | counterexamples R01, R01b, R02, R02c, R14, R17b(minor); main/non-parked behaviour IDENTICAL to HEAD gate |

Brief breaches by workers (reported, not hidden): W1 and W3 each wrote under `.claude/agent-memory/praxis-worker/` despite the brief, and each said it reverted. The file is still there (gitignored, so `git status` is silent); see "Open items" and the evidence block. I did not touch that directory (the brief forbids writes there).

## Process log

- 05:21Z baseline: HEAD = origin/main = 02d53c6; real-index fingerprint 5bfab445...bda95; draft gate sha256 809a6605...65ac (block E0).
- Read the full gate and the draft diff. Dispatched W1, W2, W3 in parallel (foreground). W2 returned BLOCKED (classifier); re-dispatched as W2b with a defensive-review framing.
- W2b X3 is a defect of the new code: the hooks-dir check anchors on HEAD, and a parked HEAD is itself unaudited. A first exempt commit (temp index) can record a malicious `.beads/hooks/pre-commit` on the parked branch; the next exempt commit passes "hooks dir == HEAD" and git runs that hook inside it. Decided by manager under D-2026-11-08-D D1: fix it (in-repo hooks dir in HEAD must also equal `refs/heads/main`; no main = deny). Also decided: make the final re-read apply both reads (W1's note). W4 built both; I changed one line myself (the "HEAD moved" deny message now also prints the no-recurse read, since W4 reported it printed "was X, now X"). Final bytes 8471206f...c19f.
- I re-ran the full harness myself on the final bytes (`/tmp/c2trip-w4/run-manager.log`, 3077 lines): MISMATCH 0, NOT-ESTABLISHED 0 (block E1). I re-ran W3's never-touches-main and cross-block scripts myself in a fresh dir `/tmp/c2trip-mgr3` on the final bytes (blocks E3, E4).
- W5 attacked the final bytes. Decided by manager under D-2026-11-08-D D1: R01/R01b/R02/R02c/R14/R17b are NOT fixed here. Each needs the session itself to run an ungated non-commit git write first (`git symbolic-ref`, `git update-ref`, `git replace`, a background HEAD flip, a symlink under `.git/refs`). E3 shows that same session can move `main` directly with `git update-ref`/`git merge`/`git branch -f`, and no hook stops it. So these add no route to main that does not already exist; closing them means gating ref-writing git commands, which is wider than C2. X1/X2 (program-running git config) affect every route at HEAD (PRE-EXISTING). All are listed as open items.
- Rubric paragraph :302-332 (uncommitted, filer's note) rewritten to match what was observed; nothing at or above :301 changed (block F shows the diff is additions only). MANIFEST :325-327 corrected in place, :328 appended.

## Verification evidence (command output)

Blocks are pasted output. E1 and E3/E4 were run by me (the manager). E2 and E5 are WORKER OUTPUT, NOT RE-RUN, labelled as such.

### E0. Baseline at unit start (manager, 05:21Z; first tool call of this unit, output pasted)

```text
$ date -u && git rev-parse HEAD origin/main && git diff --cached --name-only | openssl dgst -sha256 && git diff HEAD --stat -- .claude/hooks/gate-commit.sh specs/SPEC_RUBRIC.md MANIFEST.md && wc -l .claude/hooks/gate-commit.sh MANIFEST.md specs/SPEC_RUBRIC.md && openssl dgst -sha256 .claude/hooks/gate-commit.sh
Tue Nov 10 05:21:15 UTC 2026
02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
SHA2-256(stdin)= 5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95
 .claude/hooks/gate-commit.sh | 56 +++++++++++++++++++++++++++++++++++++++++++-
 MANIFEST.md                  | 11 +++++++++
 specs/SPEC_RUBRIC.md         | 22 +++++++++++++++++
 3 files changed, 88 insertions(+), 1 deletion(-)
     768 .claude/hooks/gate-commit.sh
     327 MANIFEST.md
     438 specs/SPEC_RUBRIC.md
    1533 total
SHA2-256(.claude/hooks/gate-commit.sh)= 809a6605c36feaf4bd47c5a0e41e7718d43d8b6287496bfdb129c137028d65ac
```

### E1. Trip table on the FINAL gate bytes (manager re-run)

Command: `bash /tmp/c2trip-w4/harness2.sh /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh > /tmp/c2trip-w4/run-manager.log 2>&1` (harness built by W1, extended by W4 with T11/T12; full log 3077 lines on disk). Wrapper output:

```text
SHA2-256(/Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh)= 8471206f084b87e2fabae2d7375896d59bc273f6f97c33a89fc7865f7466c19f
harness rc=0
SHA2-256(/Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh)= 8471206f084b87e2fabae2d7375896d59bc273f6f97c33a89fc7865f7466c19f
    3077 run-manager.log
```

E1a. Harness header (log lines 1-18):
```text
### C2 trip harness  started 2026-11-10T05:56:14Z
### gate under test: /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
### gate sha256: 8471206f084b87e2fabae2d7375896d59bc273f6f97c33a89fc7865f7466c19f
### real working-tree gate sha256: 8471206f084b87e2fabae2d7375896d59bc273f6f97c33a89fc7865f7466c19f
### git: git version 2.50.1 (Apple Git-155)   bash: 5.3.15(1)-release
### clone remotes (must be empty): []
### clone core.hooksPath: []  git-path hooks: [.git/hooks]
### main = 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
### staged (git diff --cached --stat):
 c2trip-staged.txt | 1 +
 1 file changed, 1 insertion(+)
### state dir:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
### index copy for T1c: /tmp/c2trip-w4/index-copy (   46095 bytes, regular file: yes)
### pre-check: processes named claude* with cwd in clone:
```

E1b. Full blocks for the brief's arms (1) T1/T1b/T1c allowed; (2) T2 main; (3) T3 detached; (4) T4 look-alikes; (5) T5 symref chains + unborn; (6) T6 GIT_DIR/GIT_WORK_TREE/GIT_COMMON_DIR; (7) T7 agent_id; (8) T8 form; (9) T9 HEAD moved (instrumented scratch copy, diff shown); (10) T10 single-session; T1 control after T10; S9 toggle. Extracted verbatim from the log with an awk filter on the case id; each block runs from its '=====' line to its 'verdict' line.
```text
----
===== [main] T1   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [0]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
----
===== [main] T1b   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [0]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
----
===== [main] T1c   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : GIT_INDEX_FILE=/tmp/c2trip-w4/index-copy git commit -m "x"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "GIT_INDEX_FILE=/tmp/c2trip-w4/index-copy git commit -m \"x\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [0]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
----
===== [main] T2   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/main
symbolic-ref -q HEAD: [refs/heads/main] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/main] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T3   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
symbolic-ref -q HEAD: [] rc=1
symbolic-ref -q --no-recurse HEAD: [] rc=1
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T4a-upperABC   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-ABC
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-ABC] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-ABC] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-ABC 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T4b-lowerP   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/praxis_build-x
symbolic-ref -q HEAD: [refs/heads/parked/praxis_build-x] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/praxis_build-x] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/praxis_build-x 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T4c-slash   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-x/y
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-x/y] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-x/y] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-x/y 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T4d-parkedX   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parkedX/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parkedX/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parkedX/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parkedX/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T4h-foldalias   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-ABC 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T5a-HEAD-wip-parked   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/wip
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/wip] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
  refs/heads/wip 02d53c6 symref=[refs/heads/parked/Praxis_build-abc]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T5b-HEAD-parked-main   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/main] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[refs/heads/main]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T5c-unborn   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-zzz
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-zzz] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-zzz] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T6a-GIT_DIR   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [GIT_DIR=/tmp/c2trip-w4/clone/.git]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T6b-GIT_WORK_TREE   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [GIT_WORK_TREE=/tmp/c2trip-w4/clone]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T6c-GIT_COMMON_DIR   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [GIT_COMMON_DIR=/tmp/c2trip-w4/clone/.git]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T7a-id-str   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master", "agent_id": "abc123"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T7b-id-null   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master", "agent_id": null}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [main] T8a-cd   expect: exit 2 + stderr contains: the stack master commits with exactly
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : cd /tmp/c2trip-w4/clone && git commit -m x
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "cd /tmp/c2trip-w4/clone && git commit -m x", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=<absolute path>) as the whole Bash command — the command is not [GIT_INDEX_FILE=<abs path> ]git commit ... as the whole command (no cd/&&/;/git -C/other prefix). No pathspec, no other flags, no cd/&&/;, no git -C, no $(...)/backticks; outside quotes only [A-Za-z0-9 ._/+=,:@%-] (no $ * ? [ ] { } ~ # ^, no invisible or non-ASCII characters). Token NOT consumed; re-issue the clean form.
verdict   : MATCH
----
===== [main] T8b-andecho   expect: exit 2 + stderr contains: the stack master commits with exactly
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m x && echo hi
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m x && echo hi", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=<absolute path>) as the whole Bash command — character '&' (U+0026) outside quotes is not in [A-Za-z0-9 \t._/+=,:@%-]. No pathspec, no other flags, no cd/&&/;, no git -C, no $(...)/backticks; outside quotes only [A-Za-z0-9 ._/+=,:@%-] (no $ * ? [ ] { } ~ # ^, no invisible or non-ASCII characters). Token NOT consumed; re-issue the clean form.
verdict   : MATCH
----
===== [main] T8c-pathspec   expect: exit 2 + stderr contains: the stack master commits with exactly
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m x somefile
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m x somefile", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=<absolute path>) as the whole Bash command — arguments are not -m <message> pairs (odd count 3). No pathspec, no other flags, no cd/&&/;, no git -C, no $(...)/backticks; outside quotes only [A-Za-z0-9 ._/+=,:@%-] (no $ * ? [ ] { } ~ # ^, no invisible or non-ASCII characters). Token NOT consumed; re-issue the clean form.
verdict   : MATCH
----
===== [main] T8i-cwd-subdir   expect: exit 2 + stderr contains: must commit from the repo root
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone/docs", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: the stack master must commit from the repo root — payload cwd '/tmp/c2trip-w4/clone/docs' (resolved '/private/tmp/c2trip-w4/clone/docs') is not the project root '/private/tmp/c2trip-w4/clone'. The gate checks the root's index; a commit from another directory or worktree would record a different one. Run `cd "/tmp/c2trip-w4/clone"` in its own Bash call, then re-issue the commit. Token NOT consumed.
verdict   : MATCH
----
===== [main] T9-moved   expect: exit 2 + stderr contains: HEAD moved during the park-commit check
gate      : /tmp/c2trip-w4/gate-t9-instrumented.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
[T9 bg] HEAD moved to refs/heads/main at 00:56:42
exit      : 2
stdout    : []
stderr    :
  | Commit denied: HEAD moved during the park-commit check (was 'refs/heads/parked/Praxis_build-abc', now 'refs/heads/main', named directly 'refs/heads/main'). Re-issue the commit.
verdict   : MATCH
----
===== [main] T9-ctl-unmoved   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /tmp/c2trip-w4/gate-t9-instrumented.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
----
===== [main] T10-session   expect: exit 2 + stderr contains: another live claude session
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: another live claude session (pid 74587) has its cwd inside this repo — it can pollute the shared .git/index between audit and commit (2026-07-10 incident)
  | Single-session rule: exactly ONE Claude session per repo working tree (docs/runbooks/2026-07-10-single-session-rule.md). Close the other session (or move it to its own git worktree) and re-run the commit.
verdict   : MATCH
----
===== [main] T1-control-after-T10   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
----
===== [s9-noexempt] T1   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /tmp/c2trip-w4/gate-noexempt.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----
===== [s9-noexempt] T2   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /tmp/c2trip-w4/gate-noexempt.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/main
symbolic-ref -q HEAD: [refs/heads/main] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/main] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
```

E1c. T9 instrumentation diff, T10 fake-process proof, S9 toggle diff (log lines 1276-1278, 1345-1349, 1417-1427):
```text
### T9 instrumented copy diff (real gate vs /tmp/c2trip-w4/gate-t9-instrumented.sh):
656a657
> : > /tmp/c2trip-w4/t9-reached; sleep 3   # C2TRIP-T9 instrumentation: hook point before the re-read block
### T10 fake pid: [74587]
  PID  PPID COMMAND
74587     1 claude-fake 120
COMMAND   PID  USER   FD   TYPE DEVICE SIZE/OFF     NODE NAME
sleep   74587 admin  cwd    DIR   1,14     1024 41551719 /private/tmp/c2trip-w4/clone
### S9 diff (gate under test vs /tmp/c2trip-w4/gate-noexempt.sh):
657,666d656
< if [ "$PARK" = 1 ]; then
<   _pk_ref2=$(cd "$ROOT" 2>/dev/null && env -u GIT_INDEX_FILE git symbolic-ref -q HEAD 2>/dev/null) || _pk_ref2=""
<   _pk_nr2=$(cd "$ROOT" 2>/dev/null && env -u GIT_INDEX_FILE git symbolic-ref -q --no-recurse HEAD 2>/dev/null) || _pk_nr2=""
<   if [ -n "$_pk_ref2" ] && [ -n "$_pk_nr2" ] && [ "$_pk_ref2" = "$_pk_ref" ] && [ "$_pk_nr2" = "$_pk_ref" ]; then
<     echo "Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch '${_pk_ref#refs/heads/}'. No token consumed." >&2
<     exit 0
<   fi
<   echo "Commit denied: HEAD moved during the park-commit check (was '${_pk_ref}', now '${_pk_ref2:-unresolvable}', named directly '${_pk_nr2:-unresolvable}'). Re-issue the commit." >&2
<   exit 2
```

E1d. Regression baseline vs the gate at git HEAD (main HEAD), T11 (X3 fix) and T12 (re-read symmetry), with the X3 toggle diff and pre-edit comparisons (log lines 2505-2930, verbatim):
```text
### regression baseline: diff -r of stderr+rc, HEAD gate vs gate under test, HEAD on main
IDENTICAL: all 66 files (T2, T2b, T8 x2 callers; stderr, stdout, rc) byte-identical
----------------------------------------------------------------------
### T11: clone core.hooksPath=[.beads/hooks]  git-path hooks=[.beads/hooks]
### T11: pre-edit gate copy /tmp/c2trip-w4/gate-pre-edit.sh sha256 809a6605c36feaf4bd47c5a0e41e7718d43d8b6287496bfdb129c137028d65ac
----------------------------------------------------------------------
### T11 toggle diff (gate under test vs /tmp/c2trip-w4/gate-nox1.sh):
328,335d327
<       # C2 X3: a parked HEAD is itself unaudited (park commits skip the token),
<       # so "matches HEAD" is no anchor there; also require HEAD == main for the dir.
<       if [ "$PARK" = 1 ]; then
<         _pk_main=$(env -u GIT_INDEX_FILE git -C "$_root_rp" rev-parse -q --verify 'refs/heads/main^{commit}' 2>/dev/null) || _pk_main=""
<         [ -n "$_pk_main" ] || deny_hooks "park commit: refs/heads/main does not resolve to a commit, so the hooks dir in the (unaudited) parked HEAD cannot be checked against it"
<         env -u GIT_INDEX_FILE git --literal-pathspecs -C "$_root_rp" diff --quiet --no-ext-diff --no-textconv "$_pk_main" HEAD -- "$_hrel" >/dev/null 2>&1 \
<           || deny_hooks "park commit: the hooks dir in HEAD differs from refs/heads/main, or the comparison failed (a parked HEAD is unaudited)"
<       fi
### x3_setup .beads/hooks/pre-commit: parked tip f50158f4ba0385173da92df9246b587c84fb7158 (main 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5)
    diff --name-status main HEAD -- .beads/hooks: [M	.beads/hooks/pre-commit ]
    git status --porcelain --ignored -- .beads/hooks: []
    staged vs HEAD: [A	c2trip-staged.txt A	c2trip-t11.txt ]
----------------------------------------------------------------------
===== [t11] T11-x3   expect: exit 2 + stderr contains: park commit: the hooks dir in HEAD differs from refs/heads/main
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc f50158f symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: git hooks dir '/private/tmp/c2trip-w4/clone/.beads/hooks' — park commit: the hooks dir in HEAD differs from refs/heads/main, or the comparison failed (a parked HEAD is unaudited). A git hook runs inside the commit after this gate has allowed it, so the stack master commits only while the effective hooks dir (core.hooksPath, else .git/hooks) matches HEAD. Revert or remove the hook change in its own Bash call, then re-issue the commit. Token NOT consumed.
verdict   : MATCH
----------------------------------------------------------------------
===== [t11] T11-x3-noat   expect: exit 2 + stderr contains: park commit: the hooks dir in HEAD differs from refs/heads/main
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc f50158f symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: git hooks dir '/private/tmp/c2trip-w4/clone/.beads/hooks' — park commit: the hooks dir in HEAD differs from refs/heads/main, or the comparison failed (a parked HEAD is unaudited). A git hook runs inside the commit after this gate has allowed it, so the stack master commits only while the effective hooks dir (core.hooksPath, else .git/hooks) matches HEAD. Revert or remove the hook change in its own Bash call, then re-issue the commit. Token NOT consumed.
verdict   : MATCH
----------------------------------------------------------------------
===== [t11] T11-noexempt-toggle   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /tmp/c2trip-w4/gate-nox1.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc f50158f symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
----------------------------------------------------------------------
===== [t11] T11-x3-PREEDIT   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /tmp/c2trip-w4/gate-pre-edit.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc f50158f symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
Warning: /private/tmp/c2trip-w4/clone/.beads has permissions 0755 (recommended: 0700). Run: chmod 700 /private/tmp/c2trip-w4/clone/.beads
### x3_undo: hooks status [] staged [A	c2trip-staged.txt ]
### x3_setup .beads/hooks/commit-msg: parked tip 7dc9d22aa2b53242e0f83f1886e02310b2361059 (main 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5)
    diff --name-status main HEAD -- .beads/hooks: [A	.beads/hooks/commit-msg ]
    git status --porcelain --ignored -- .beads/hooks: []
    staged vs HEAD: [A	c2trip-staged.txt A	c2trip-t11.txt ]
----------------------------------------------------------------------
===== [t11] T11b-newhook   expect: exit 2 + stderr contains: park commit: the hooks dir in HEAD differs from refs/heads/main
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 7dc9d22 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: git hooks dir '/private/tmp/c2trip-w4/clone/.beads/hooks' — park commit: the hooks dir in HEAD differs from refs/heads/main, or the comparison failed (a parked HEAD is unaudited). A git hook runs inside the commit after this gate has allowed it, so the stack master commits only while the effective hooks dir (core.hooksPath, else .git/hooks) matches HEAD. Revert or remove the hook change in its own Bash call, then re-issue the commit. Token NOT consumed.
verdict   : MATCH
----------------------------------------------------------------------
===== [t11] T11b-noexempt-toggle   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /tmp/c2trip-w4/gate-nox1.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 7dc9d22 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
Warning: /private/tmp/c2trip-w4/clone/.beads has permissions 0755 (recommended: 0700). Run: chmod 700 /private/tmp/c2trip-w4/clone/.beads
### x3_undo: hooks status [] staged [A	c2trip-staged.txt ]
### T11-ctl: parked tip b0b530b51ead0be43d5f6a856b7d7cb93d76b167; diff main HEAD (all): [A	c2trip-ctl.txt ]; hooks-dir diff: []
----------------------------------------------------------------------
===== [t11] T11-ctl   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc b0b530b symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
----------------------------------------------------------------------
===== [t11] T11-ctl-noat   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc b0b530b symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
----------------------------------------------------------------------
===== [t11] T11-ctl-headeqmain   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
### T11-main: main moved to 237f82e03107d624cf224ffb6fbbf5563b7e3ecd; HEAD=refs/heads/main; hooks status []
----------------------------------------------------------------------
===== [t11] T11-main   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/main
symbolic-ref -q HEAD: [refs/heads/main] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/main] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 237f82e symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
----------------------------------------------------------------------
===== [t11-pre] T11-main   expect: exit 2 + stderr contains: Commit denied: no audit PASS token
gate      : /tmp/c2trip-w4/gate-pre-edit.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/main
symbolic-ref -q HEAD: [refs/heads/main] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/main] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 237f82e symref=[]
packed-refs heads: [1]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
verdict   : MATCH
### T11-main edited vs pre-edit (rc, stdout, stderr):
  T11-main.rc IDENTICAL
  T11-main.stdout IDENTICAL
  T11-main.stderr IDENTICAL
Warning: /private/tmp/c2trip-w4/clone/.beads has permissions 0755 (recommended: 0700). Run: chmod 700 /private/tmp/c2trip-w4/clone/.beads
### T11-main restored: main=02d53c66ccfa3105f8c8bba812678e9e77d1cbe5 hooks status []
### T11-nomain: rev-parse refs/heads/main^{commit}: [] rc=1
----------------------------------------------------------------------
===== [t11] T11-nomain   expect: exit 2 + stderr contains: park commit: refs/heads/main does not resolve to a commit
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [0]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: git hooks dir '/private/tmp/c2trip-w4/clone/.beads/hooks' — park commit: refs/heads/main does not resolve to a commit, so the hooks dir in the (unaudited) parked HEAD cannot be checked against it. A git hook runs inside the commit after this gate has allowed it, so the stack master commits only while the effective hooks dir (core.hooksPath, else .git/hooks) matches HEAD. Revert or remove the hook change in its own Bash call, then re-issue the commit. Token NOT consumed.
verdict   : MATCH
----------------------------------------------------------------------
===== [t11] T11-nomain-noat   expect: exit 2 + stderr contains: park commit: refs/heads/main does not resolve to a commit
gate      : /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [0]
audit-pass-* tokens in clone state before run: 0
exit      : 2
stdout    : []
stderr    :
  | Commit denied: git hooks dir '/private/tmp/c2trip-w4/clone/.beads/hooks' — park commit: refs/heads/main does not resolve to a commit, so the hooks dir in the (unaudited) parked HEAD cannot be checked against it. A git hook runs inside the commit after this gate has allowed it, so the stack master commits only while the effective hooks dir (core.hooksPath, else .git/hooks) matches HEAD. Revert or remove the hook change in its own Bash call, then re-issue the commit. Token NOT consumed.
verdict   : MATCH
----------------------------------------------------------------------
===== [t11] T11-nomain-PREEDIT   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /tmp/c2trip-w4/gate-pre-edit.sh
command   : git commit -m park2
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m park2", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [0]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
### T11 done: core.hooksPath now []
----------------------------------------------------------------------
### T12 instrumented diffs:
656a657
> : > /tmp/c2trip-w4/t12-reached; sleep 3   # C2TRIP-T12 instrumentation: hook point before the re-read block
646a647
> : > /tmp/c2trip-w4/t12-reached; sleep 3   # C2TRIP-T12 instrumentation: hook point before the re-read block
----------------------------------------------------------------------
===== [t12] T12-chain   expect: exit 2 + stderr contains: HEAD moved during the park-commit check
gate      : /tmp/c2trip-w4/gate-t12-edited.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [0]
audit-pass-* tokens in clone state before run: 0
[T12 bg] HEAD -> ref: refs/heads/wip ; recurse=[refs/heads/parked/Praxis_build-abc] no-recurse=[refs/heads/wip] at 00:57:26
exit      : 2
stdout    : []
stderr    :
  | Commit denied: HEAD moved during the park-commit check (was 'refs/heads/parked/Praxis_build-abc', now 'refs/heads/parked/Praxis_build-abc', named directly 'refs/heads/wip'). Re-issue the commit.
verdict   : MATCH
----------------------------------------------------------------------
===== [t12] T12-chain-PREEDIT   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /tmp/c2trip-w4/gate-t12-preedit.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [0]
audit-pass-* tokens in clone state before run: 0
[T12 bg] HEAD -> ref: refs/heads/wip ; recurse=[refs/heads/parked/Praxis_build-abc] no-recurse=[refs/heads/wip] at 00:57:30
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
----------------------------------------------------------------------
===== [t12] T12-ctl-unmoved   expect: exit 0 + stderr contains: Commit allowed without an audit token: park-commit exemption
gate      : /tmp/c2trip-w4/gate-t12-edited.sh
command   : git commit -m "park wip"
payload   : {"session_id": "c2trip-session", "transcript_path": "/tmp/c2trip-w4/transcript.jsonl", "hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "git commit -m \"park wip\"", "description": "c2trip"}, "cwd": "/tmp/c2trip-w4/clone", "agent_type": "praxis-master"}
extra env : [none]
HEAD file           : ref: refs/heads/parked/Praxis_build-abc
symbolic-ref -q HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
symbolic-ref -q --no-recurse HEAD: [refs/heads/parked/Praxis_build-abc] rc=0
for-each-ref refs/heads (on-disk names):
  refs/heads/main 02d53c6 symref=[]
  refs/heads/parked/Praxis_build-abc 02d53c6 symref=[]
packed-refs heads: [0]
audit-pass-* tokens in clone state before run: 0
exit      : 0
stdout    : []
stderr    :
  | Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
state dir after ALLOW:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
last-allowed: absent
verdict   : MATCH
----------------------------------------------------------------------
### final: tokens in clone state: 0; state dir:
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:43 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:43 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:43 orchestrator-active
### gate sha256 at end: 8471206f084b87e2fabae2d7375896d59bc273f6f97c33a89fc7865f7466c19f
----------------------------------------------------------------------
```

E1e. Summary table of every case in the run (log lines 2931-3077, verbatim):
```text
### SUMMARY (label | id | verdict | expected | exit | first stderr line)
main         T1                        MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
main         T1b                       MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
main         T1c                       MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
main         T1-mm                     MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
main         T1d-packed                MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
main         T2                        MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T2b                       MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T3                        MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T3b                       MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4a-upperABC              MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4a-upperABC-noat         MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4b-lowerP                MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4b-lowerP-noat           MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4c-slash                 MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4c-slash-noat            MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4d-parkedX               MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4d-parkedX-noat          MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4e-emptyid               MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4e-emptyid-noat          MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4f-hyphen                MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4f-hyphen-noat           MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4g-xparked               MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4g-xparked-noat          MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4h-foldalias             MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4h-foldalias-noat        MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T4i-packedalias           MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T5a-HEAD-wip-parked       MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T5a-noat                  MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T5b-HEAD-parked-main      MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T5b-noat                  MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T5c-unborn                MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T5c-noat                  MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T6a-GIT_DIR               MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T6b-GIT_WORK_TREE         MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T6c-GIT_COMMON_DIR        MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T6d-GIT_DIR-empty         MATCH  exit 2: Commit denied: repo toplevel 'unresolvable' is not the project root  2  Commit denied: repo toplevel 'unresolvable' is not the project root '/private/tmp/c2trip-w4/clone' (core.worktree or similar config moves the work tre
main         T6e-GIT_DIR-noat          MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T7a-id-str                MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T7b-id-null               MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T7c-id-5                  MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T7d-id-empty              MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T7e-id-str-noat           MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T7f-id-null-noat          MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
main         T8a-cd                    MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
main         T8b-andecho               MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
main         T8c-pathspec              MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
main         T8d-dashdash              MATCH  exit 2: pathspec after ' -- '                                                2  Commit denied: a pathspec after ' -- ' commits a different set than what was audited
main         T8e-am                    MATCH  exit 2: '-a'-style short flag                                                2  Commit denied: a '-a'-style short flag sweeps unstaged working-tree changes into the commit
main         T8f-gitC                  MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
main         T8g-amend                 MATCH  exit 2: --all/--include/--amend                                              2  Commit denied: --all/--include/--amend changes the committed set out from under the audit
main         T8h-dollar-paren          MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
main         T8i-cwd-subdir            MATCH  exit 2: must commit from the repo root                                       2  Commit denied: the stack master must commit from the repo root — payload cwd '/tmp/c2trip-w4/clone/docs' (resolved '/private/tmp/c2trip-w4/clone/docs'
main         T8j-cwd-missing           MATCH  exit 2: must commit from the repo root                                       2  Commit denied: the stack master must commit from the repo root — payload cwd 'missing' (resolved 'unresolvable') is not the project root '/private/tmp
main         T8a-cd-noat               MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
main         T8b-andecho-noat          MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
main         T8c-pathspec-noat         MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
main         T8d-dashdash-noat         MATCH  exit 2: pathspec after ' -- '                                                2  Commit denied: a pathspec after ' -- ' commits a different set than what was audited
main         T8e-am-noat               MATCH  exit 2: '-a'-style short flag                                                2  Commit denied: a '-a'-style short flag sweeps unstaged working-tree changes into the commit
main         T8f-gitC-noat             MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
main         T8g-amend-noat            MATCH  exit 2: --all/--include/--amend                                              2  Commit denied: --all/--include/--amend changes the committed set out from under the audit
main         T8h-dollar-paren-noat     MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
main         T8i-cwd-subdir-noat       MATCH  exit 2: must commit from the repo root                                       2  Commit denied: the stack master must commit from the repo root — payload cwd '/tmp/c2trip-w4/clone/docs' (resolved '/private/tmp/c2trip-w4/clone/docs'
main         T8j-cwd-missing-noat      MATCH  exit 2: must commit from the repo root                                       2  Commit denied: the stack master must commit from the repo root — payload cwd 'missing' (resolved 'unresolvable') is not the project root '/private/tmp
main         T9-moved                  MATCH  exit 2: HEAD moved during the park-commit check                              2  Commit denied: HEAD moved during the park-commit check (was 'refs/heads/parked/Praxis_build-abc', now 'refs/heads/main', named directly 'refs/heads/ma
main         T9-ctl-unmoved            MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
main         T9-moved-to-other-parked  MATCH  exit 2: HEAD moved during the park-commit check                              2  Commit denied: HEAD moved during the park-commit check (was 'refs/heads/parked/Praxis_build-abc', now 'refs/heads/parked/Praxis_build-def', named dire
main         T10-session               MATCH  exit 2: another live claude session                                          2  Commit denied: another live claude session (pid 74587) has its cwd inside this repo — it can pollute the shared .git/index between audit and commit (2
main         T10-session-noat          MATCH  exit 2: another live claude session                                          2  Commit denied: another live claude session (pid 74587) has its cwd inside this repo — it can pollute the shared .git/index between audit and commit (2
main         T1-control-after-T10      MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
s9-noexempt  T1                        MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
s9-noexempt  T2                        MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
head         T1                        MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
head         T1b                       MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
head-parked  T8a-cd                    MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
head-parked  T8b-andecho               MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
head-parked  T8c-pathspec              MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
head-parked  T8d-dashdash              MATCH  exit 2: pathspec after ' -- '                                                2  Commit denied: a pathspec after ' -- ' commits a different set than what was audited
head-parked  T8e-am                    MATCH  exit 2: '-a'-style short flag                                                2  Commit denied: a '-a'-style short flag sweeps unstaged working-tree changes into the commit
head-parked  T8f-gitC                  MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
head-parked  T8g-amend                 MATCH  exit 2: --all/--include/--amend                                              2  Commit denied: --all/--include/--amend changes the committed set out from under the audit
head-parked  T8h-dollar-paren          MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
head-parked  T8i-cwd-subdir            MATCH  exit 2: must commit from the repo root                                       2  Commit denied: the stack master must commit from the repo root — payload cwd '/tmp/c2trip-w4/clone/docs' (resolved '/private/tmp/c2trip-w4/clone/docs'
head-parked  T8j-cwd-missing           MATCH  exit 2: must commit from the repo root                                       2  Commit denied: the stack master must commit from the repo root — payload cwd 'missing' (resolved 'unresolvable') is not the project root '/private/tmp
head-main    T2                        MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
head-main    T2b                       MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
head-main    T8a-cd                    MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
head-main    T8b-andecho               MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
head-main    T8c-pathspec              MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
head-main    T8d-dashdash              MATCH  exit 2: pathspec after ' -- '                                                2  Commit denied: a pathspec after ' -- ' commits a different set than what was audited
head-main    T8e-am                    MATCH  exit 2: '-a'-style short flag                                                2  Commit denied: a '-a'-style short flag sweeps unstaged working-tree changes into the commit
head-main    T8f-gitC                  MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
head-main    T8g-amend                 MATCH  exit 2: --all/--include/--amend                                              2  Commit denied: --all/--include/--amend changes the committed set out from under the audit
head-main    T8h-dollar-paren          MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
head-main    T8i-cwd-subdir            MATCH  exit 2: must commit from the repo root                                       2  Commit denied: the stack master must commit from the repo root — payload cwd '/tmp/c2trip-w4/clone/docs' (resolved '/private/tmp/c2trip-w4/clone/docs'
head-main    T8j-cwd-missing           MATCH  exit 2: must commit from the repo root                                       2  Commit denied: the stack master must commit from the repo root — payload cwd 'missing' (resolved 'unresolvable') is not the project root '/private/tmp
head-main    T8a-cd-noat               MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
head-main    T8b-andecho-noat          MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
head-main    T8c-pathspec-noat         MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
head-main    T8d-dashdash-noat         MATCH  exit 2: pathspec after ' -- '                                                2  Commit denied: a pathspec after ' -- ' commits a different set than what was audited
head-main    T8e-am-noat               MATCH  exit 2: '-a'-style short flag                                                2  Commit denied: a '-a'-style short flag sweeps unstaged working-tree changes into the commit
head-main    T8f-gitC-noat             MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
head-main    T8g-amend-noat            MATCH  exit 2: --all/--include/--amend                                              2  Commit denied: --all/--include/--amend changes the committed set out from under the audit
head-main    T8h-dollar-paren-noat     MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
head-main    T8i-cwd-subdir-noat       MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
head-main    T8j-cwd-missing-noat      MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
wt-main      T2                        MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
wt-main      T2b                       MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
wt-main      T8a-cd                    MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
wt-main      T8b-andecho               MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
wt-main      T8c-pathspec              MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
wt-main      T8d-dashdash              MATCH  exit 2: pathspec after ' -- '                                                2  Commit denied: a pathspec after ' -- ' commits a different set than what was audited
wt-main      T8e-am                    MATCH  exit 2: '-a'-style short flag                                                2  Commit denied: a '-a'-style short flag sweeps unstaged working-tree changes into the commit
wt-main      T8f-gitC                  MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
wt-main      T8g-amend                 MATCH  exit 2: --all/--include/--amend                                              2  Commit denied: --all/--include/--amend changes the committed set out from under the audit
wt-main      T8h-dollar-paren          MATCH  exit 2: the stack master commits with exactly                                2  Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=
wt-main      T8i-cwd-subdir            MATCH  exit 2: must commit from the repo root                                       2  Commit denied: the stack master must commit from the repo root — payload cwd '/tmp/c2trip-w4/clone/docs' (resolved '/private/tmp/c2trip-w4/clone/docs'
wt-main      T8j-cwd-missing           MATCH  exit 2: must commit from the repo root                                       2  Commit denied: the stack master must commit from the repo root — payload cwd 'missing' (resolved 'unresolvable') is not the project root '/private/tmp
wt-main      T8a-cd-noat               MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
wt-main      T8b-andecho-noat          MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
wt-main      T8c-pathspec-noat         MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
wt-main      T8d-dashdash-noat         MATCH  exit 2: pathspec after ' -- '                                                2  Commit denied: a pathspec after ' -- ' commits a different set than what was audited
wt-main      T8e-am-noat               MATCH  exit 2: '-a'-style short flag                                                2  Commit denied: a '-a'-style short flag sweeps unstaged working-tree changes into the commit
wt-main      T8f-gitC-noat             MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
wt-main      T8g-amend-noat            MATCH  exit 2: --all/--include/--amend                                              2  Commit denied: --all/--include/--amend changes the committed set out from under the audit
wt-main      T8h-dollar-paren-noat     MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
wt-main      T8i-cwd-subdir-noat       MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
wt-main      T8j-cwd-missing-noat      MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
t11          T11-x3                    MATCH  exit 2: park commit: the hooks dir in HEAD differs from refs/heads/main      2  Commit denied: git hooks dir '/private/tmp/c2trip-w4/clone/.beads/hooks' — park commit: the hooks dir in HEAD differs from refs/heads/main, or the com
t11          T11-x3-noat               MATCH  exit 2: park commit: the hooks dir in HEAD differs from refs/heads/main      2  Commit denied: git hooks dir '/private/tmp/c2trip-w4/clone/.beads/hooks' — park commit: the hooks dir in HEAD differs from refs/heads/main, or the com
t11          T11-noexempt-toggle       MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
t11          T11-x3-PREEDIT            MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
t11          T11b-newhook              MATCH  exit 2: park commit: the hooks dir in HEAD differs from refs/heads/main      2  Commit denied: git hooks dir '/private/tmp/c2trip-w4/clone/.beads/hooks' — park commit: the hooks dir in HEAD differs from refs/heads/main, or the com
t11          T11b-noexempt-toggle      MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
t11          T11-ctl                   MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
t11          T11-ctl-noat              MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
t11          T11-ctl-headeqmain        MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
t11          T11-main                  MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
t11-pre      T11-main                  MATCH  exit 2: Commit denied: no audit PASS token                                   2  Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thre
t11          T11-nomain                MATCH  exit 2: park commit: refs/heads/main does not resolve to a commit            2  Commit denied: git hooks dir '/private/tmp/c2trip-w4/clone/.beads/hooks' — park commit: refs/heads/main does not resolve to a commit, so the hooks dir
t11          T11-nomain-noat           MATCH  exit 2: park commit: refs/heads/main does not resolve to a commit            2  Commit denied: git hooks dir '/private/tmp/c2trip-w4/clone/.beads/hooks' — park commit: refs/heads/main does not resolve to a commit, so the hooks dir
t11          T11-nomain-PREEDIT        MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
t12          T12-chain                 MATCH  exit 2: HEAD moved during the park-commit check                              2  Commit denied: HEAD moved during the park-commit check (was 'refs/heads/parked/Praxis_build-abc', now 'refs/heads/parked/Praxis_build-abc', named dire
t12          T12-chain-PREEDIT         MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
t12          T12-ctl-unmoved           MATCH  exit 0: Commit allowed without an audit token: park-commit exemption         0  Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
### MISMATCH count: 0   NOT-ESTABLISHED: 0
### finished 2026-11-10T05:57:36Z
```

### E2. W2b adversarial rows X1, X2, X3, T1 race on the DRAFT bytes 809a6605...65ac — WORKER OUTPUT, NOT RE-RUN (X3 is re-observed by me as T11-x3-PREEDIT / T11-x3 in E1d)

Source: /tmp/c2trip-w2b/review.log lines 300-397, verbatim.
```text
## ROOT=main wt (parked) cwd=main wt (expect allow)
Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc1'. No token consumed.
exit=0

=================== ROW G2 (rerun): repo config core.worktree=/tmp/c2trip-w2b (parent of ROOT) on parked
toplevel: /private/tmp/c2trip-w2b HEAD: refs/heads/parked/Praxis_build-abc1
Commit denied: repo toplevel '/private/tmp/c2trip-w2b' is not the project root '/private/tmp/c2trip-w2b/clone' (core.worktree or similar config moves the work tree; the audited diff would not cover the whole commit). Remove the override in its own Bash call, then re-issue the commit. Token NOT consumed.
exit=2

=================== ROW G3 (rerun): includeIf onbranch:parked/** -> core.hooksPath evilhooks (outside ROOT, executable pre-commit)
effective hooks: /tmp/c2trip-w2b/evilhooks
Commit denied: git hooks dir '/private/tmp/c2trip-w2b/evilhooks' — it is outside the work tree (or in the git dir) and holds an executable non-.sample hook 'pre-commit'. A git hook runs inside the commit after this gate has allowed it, so the stack master commits only while the effective hooks dir (core.hooksPath, else .git/hooks) matches HEAD. Revert or remove the hook change in its own Bash call, then re-issue the commit. Token NOT consumed.
exit=2

=================== ROW S3 (rerun): parked ref = fs symlink to ../main (read as regular ref)
recurse: refs/heads/parked/Praxis_build-lnk2 no-recurse: refs/heads/parked/Praxis_build-lnk2 fer: 
Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
exit=2
## ref update via HEAD (same files-backend transaction as commit's). main before: 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
main after: 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5 lnk2: b3c1efe01b1f590a885fca9fe20f408eb95602aa
-rw-r--r--@ 1 admin  wheel  41 Nov 10 00:36 Praxis_build-lnk2

=================== ROW C1b (rerun): directory case alias: only refs/heads/PARKED/ on disk, HEAD -> refs/heads/parked/...
total 0
drwxr-xr-x@ 2 admin  wheel   64 Nov 10 00:36 .
drwxr-xr-x@ 5 admin  wheel  160 Nov 10 00:34 ..
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:36 .
drwxr-xr-x@ 5 admin  wheel  160 Nov 10 00:34 ..
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:36 PARKED
symref: refs/heads/parked/Praxis_build-dir1 rev: 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5 fer(exact): [] fer(all parked/PARKED): [refs/heads/PARKED/Praxis_build-dir1 refs/heads/parked/Praxis_build-abc1 refs/heads/parked/Praxis_build-pk1 ]
Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
exit=2
## what name does a ref update via HEAD record? (main before 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5)
main after: 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
total 8
drwxr-xr-x@ 3 admin  wheel  96 Nov 10 00:36 .
drwxr-xr-x@ 3 admin  wheel  96 Nov 10 00:36 ..
-rw-r--r--@ 1 admin  wheel  41 Nov 10 00:36 Praxis_build-dir1
refs/heads/PARKED/Praxis_build-dir1 b3c1efe
HEAD restored: refs/heads/parked/Praxis_build-abc1
HEAD=refs/heads/parked/Praxis_build-x3 main=02d53c66ccfa3105f8c8bba812678e9e77d1cbe5

=================== ROW X1: core.fsmonitor=<script> on a parked branch: gate allows; program runs inside the commit and moves main
Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-x3'. No token consumed.
exit=0
fsm.log after gate:
fsmonitor ran: parent=/Library/Developer/CommandLineTools/usr/bin/git --literal-pathspecs -C /private/tmp/c2trip-w2b/clone status --porcelain --untracked-files=all --ignored -- .beads/hooks
fsmonitor ran: parent=/Library/Developer/CommandLineTools/usr/bin/git --literal-pathspecs -C /private/tmp/c2trip-w2b/clone status --porcelain --untracked-files=all --ignored -- .beads/hooks
main after gate: 7f3590e1a556f80808c733ce30466e25004413e7
## commit-time: git commit --dry-run (same index refresh as the real commit; creates no commit)
dry-run exit=0
fsm.log after commit dry-run:
fsmonitor ran: parent=/Library/Developer/CommandLineTools/usr/bin/git commit --dry-run -m park
fsmonitor ran: parent=/Library/Developer/CommandLineTools/usr/bin/git commit --dry-run -m park
main now: 7f3590e1a556f80808c733ce30466e25004413e7 (was 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5)
HEAD-gate exit=2 (Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the stag)

=================== ROW X2: commit.gpgSign + gpg.program=<script> on a parked branch
Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-x3'. No token consumed.
exit=0
gpg.log after gate: []  main: 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
## signing path exercised via commit-tree -S (dangling object only; no ref update by git itself)
commit-tree -S exit=1
gpg.log: gpg.program ran: --status-fd=2 -bsau t <t@t>
main now: 7f3590e1a556f80808c733ce30466e25004413e7 (was 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5)
HEAD-gate exit=2 (Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the stag)

=================== ROW X3: hooks-dir check anchored to an UNAUDITED parked HEAD: commit a malicious tracked hook via temp index, then the next park commit runs it
hooksPath=/tmp/c2trip-w2b/clone/.beads/hooks
?? README_scratch.txt
temp index diff vs HEAD: M	.beads/hooks/pre-commit 
## step 1: gate on 'GIT_INDEX_FILE=/tmp/c2trip-w2b/tidx git commit -m park1' (no token)
Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-x3'. No token consumed.
exit=0
HEAD-gate exit=2 (Commit denied: no audit PASS token for this exact staged diff under index '/private/tmp/c2)
## step 2: the commit that command makes (simulated with plumbing: write-tree under tidx, commit-tree, update-ref HEAD)
parked tip now a105b25b839b5b5b2e51a01b2f1a20d80f217a2f; HEAD tree has evil hook: echo EVIL-HOOK-RAN >&2
## step 3: plain file write + 'git add' (neither is gated: no 'commit' in the text) to align worktree/index
status of hooks dir: []
## step 4: gate on plain 'git commit -m park2' (no token)
Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-x3'. No token consumed.
exit=0
## step 5: the hook git would run inside that commit (git hook run pre-commit); main before: 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
EVIL-HOOK-RAN
hook exit=0
main after: a105b25b839b5b5b2e51a01b2f1a20d80f217a2f (parked tip a105b25b839b5b5b2e51a01b2f1a20d80f217a2f)
## same final state against the HEAD gate:
HEAD-gate exit=2 (Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the stag)

=================== ROW T1: post-allow race: HEAD re-pointed at main after the gate's last HEAD read
Warning: /private/tmp/c2trip-w2b/clone/.beads has permissions 0755 (recommended: 0700). Run: chmod 700 /private/tmp/c2trip-w2b/clone/.beads
Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-t1'. No token consumed.
exit=0
On branch main
last-allowed present? 0 -> commit-tree-verify.sh exits 0 silently with no record
post-hook exit=0

```

### E3. Task C: what does and does not stop a parked commit reaching main (manager re-run of W3's scripts in a fresh dir /tmp/c2trip-mgr3, final gate bytes copied into the clone)

Command: `bash /tmp/c2trip-mgr3bin/main.sh; bash /tmp/c2trip-mgr3bin/part2.sh` (W3's scripts with the work dir rewritten to /tmp/c2trip-mgr3; the clone's origin is removed in SETUP and the only remote is the bare /tmp/c2trip-mgr3/remote.git). Observations log lines 1-359 (setup, hook inventory, routes 1-7) and 704-721 (GitHub, read-only GET), verbatim:
```text

==================================================================
== SETUP
==================================================================
$ git clone -q /Volumes/Sensidine/Praxis.build /tmp/c2trip-mgr3/clone
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone remote remove origin
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone remote -v
[exit=0]
$ git init -q --bare /tmp/c2trip-mgr3/remote.git
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone remote add scratch /tmp/c2trip-mgr3/remote.git
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone remote -v
scratch	/tmp/c2trip-mgr3/remote.git (fetch)
scratch	/tmp/c2trip-mgr3/remote.git (push)
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone config user.name c2trip
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone config user.email c2trip@example.invalid
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone config --get core.hooksPath
[exit=1]
$ git -C /tmp/c2trip-mgr3/clone rev-parse --git-path hooks
.git/hooks
[exit=0]
$ ls /tmp/c2trip-mgr3/clone/.git/hooks
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
sendemail-validate.sample
update.sample
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone push -q scratch main
[exit=0]
$ git --git-dir=/tmp/c2trip-mgr3/remote.git log --oneline -1 main
02d53c6 docs: C7 fresh-session probe (Amear D-2026-11-08-C C7, bead gjj) - a praxis-manager spawned after b3c1efe reports no persistent-memory section; agent definitions read at session start; MANIFEST row 316; DECISION_LOG flush through 19:18:30Z
[exit=0]

-- Hook scripts: the clone holds HEAD's committed copies; the real WORKING-TREE copies are copied in so
-- that the registered command "$CLAUDE_PROJECT_DIR"/... resolves to the working-tree text (C2 exemption).
  before: 991b4a48057552952b1a093b62cc36833c31ee96f1dc6521f20db66194654abd  clone/scripts/no-commit-guard.sh (HEAD copy)
  after : 991b4a48057552952b1a093b62cc36833c31ee96f1dc6521f20db66194654abd  clone/scripts/no-commit-guard.sh ; real working tree: 991b4a48057552952b1a093b62cc36833c31ee96f1dc6521f20db66194654abd
  before: a2e4ff9d7f489bb8f06c4122bd5ecc64229c99347d35986cabd427aa530d456c  clone/.claude/hooks/gate-commit.sh (HEAD copy)
  after : 8471206f084b87e2fabae2d7375896d59bc273f6f97c33a89fc7865f7466c19f  clone/.claude/hooks/gate-commit.sh ; real working tree: 8471206f084b87e2fabae2d7375896d59bc273f6f97c33a89fc7865f7466c19f
  before: 2dd67afcaefb84136a460d02cb7380acaf64c4f6bcce181f9850c02dfbb63101  clone/scripts/master-bash-guard.sh (HEAD copy)
  after : 2dd67afcaefb84136a460d02cb7380acaf64c4f6bcce181f9850c02dfbb63101  clone/scripts/master-bash-guard.sh ; real working tree: 2dd67afcaefb84136a460d02cb7380acaf64c4f6bcce181f9850c02dfbb63101
  before: fdfc67995df99a8a207511d27121595c3a906932c866b141ad938a78f95e8d93  clone/scripts/mint-guard.sh (HEAD copy)
  after : fdfc67995df99a8a207511d27121595c3a906932c866b141ad938a78f95e8d93  clone/scripts/mint-guard.sh ; real working tree: fdfc67995df99a8a207511d27121595c3a906932c866b141ad938a78f95e8d93
  before: 781af62e74862c684012caa27bc1e72189deb309af19dd78085f5da77ba6abc6  clone/scripts/commit-tree-verify.sh (HEAD copy)
  after : 781af62e74862c684012caa27bc1e72189deb309af19dd78085f5da77ba6abc6  clone/scripts/commit-tree-verify.sh ; real working tree: 781af62e74862c684012caa27bc1e72189deb309af19dd78085f5da77ba6abc6
  before: 9c2f14e1184fe95e088f91e728c44960bfc1fd3ce839c2942922fc73b6501266  clone/.claude/hooks/audit-provenance.sh (HEAD copy)
  after : 9c2f14e1184fe95e088f91e728c44960bfc1fd3ce839c2942922fc73b6501266  clone/.claude/hooks/audit-provenance.sh ; real working tree: 9c2f14e1184fe95e088f91e728c44960bfc1fd3ce839c2942922fc73b6501266
  before: 479d08e47ecf24903fa52c75203dfb09ded58b5745c61485beb13581b7eddef8  clone/.claude/settings.json (HEAD copy)
  after : 98ac1ec8802cd6c02a04d8f24382c72a53162bfac41ca41ccff13bf199d92115  clone/.claude/settings.json ; real working tree: 98ac1ec8802cd6c02a04d8f24382c72a53162bfac41ca41ccff13bf199d92115
$ grep -c 'park-commit exemption' /tmp/c2trip-mgr3/clone/.claude/hooks/gate-commit.sh
2
[exit=0]
$ ls -la /tmp/c2trip-mgr3/clone/.claude/state
total 0
drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:58 .
drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:58 ..
-rw-r--r--@ 1 admin  wheel    0 Nov 10 00:58 orchestrator-active
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone status --porcelain
 M .claude/hooks/gate-commit.sh
 M .claude/settings.json
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone checkout -q -b parked/Praxis_build-abc
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone add park1.txt
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone commit -q -m 'park commit 1 (setup)'
[exit=0]
M0(main)=02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
P1(parked/Praxis_build-abc)=a7913d4d9f96ab79cf5e2c4b6ade98e124320f33
$ git -C /tmp/c2trip-mgr3/clone log --oneline -3 --all --graph
* a7913d4 park commit 1 (setup)
* 02d53c6 docs: C7 fresh-session probe (Amear D-2026-11-08-C C7, bead gjj) - a praxis-manager spawned after b3c1efe reports no persistent-memory section; agent definitions read at session start; MANIFEST row 316; DECISION_LOG flush through 19:18:30Z
* b3c1efe agents: praxis-manager memory field removed (Amear D-2026-11-08-C C7, bead gjj) - WRITTEN only; control and test probes both still show the memory section in this session; fresh-run probe decides; MANIFEST rows 312-315; DECISION_LOG flush through 18:45Z
[exit=0]

==================================================================
== HOOK INVENTORY (working-tree settings.json, PreToolUse, matcher matches 'Bash')
==================================================================
$ jq -r '.hooks.PreToolUse[] | select(.matcher as $m | "Bash" | test("^(" + $m + ")$")) | {matcher, command: .hooks[].command}' /Volumes/Sensidine/Praxis.build/.claude/settings.json
{
  "matcher": "Bash",
  "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/no-commit-guard.sh"
}
{
  "matcher": "Bash",
  "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/gate-commit.sh"
}
{
  "matcher": "Bash",
  "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/master-bash-guard.sh"
}
{
  "matcher": "Bash|Write|Edit|NotebookEdit",
  "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/mint-guard.sh"
}
[exit=0]
count=4
$ jq -r '.hooks.PostToolUse[] | select(.matcher as $m | "Bash" | test("^(" + $m + ")$")) | {matcher, command: .hooks[].command}' /Volumes/Sensidine/Praxis.build/.claude/settings.json
{
  "matcher": "Bash",
  "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/commit-tree-verify.sh"
}
[exit=0]

==================================================================
== Q1 ROUTE 1: git checkout main ; git merge --ff-only parked/Praxis_build-abc
==================================================================
(reset: local main=02d53c6 remote main=02d53c6 HEAD=parked/Praxis_build-abc)
--- PreToolUse hooks for command: git checkout main
  [caller=master] payload identity: {"agent_type":"praxis-master","agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=plain] payload identity: {"agent_type":null,"agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=sub] payload identity: {"agent_type":"praxis-worker","agent_id":"a1"}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
--- PreToolUse hooks for command: git merge --ff-only parked/Praxis_build-abc
  [caller=master] payload identity: {"agent_type":"praxis-master","agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=plain] payload identity: {"agent_type":null,"agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=sub] payload identity: {"agent_type":"praxis-worker","agent_id":"a1"}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=2 stderr=BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
$ cd /tmp/c2trip-mgr3/clone && git checkout main
Switched to branch 'main'
M	.claude/hooks/gate-commit.sh
M	.claude/settings.json
[exit=0]
$ cd /tmp/c2trip-mgr3/clone && git merge --ff-only parked/Praxis_build-abc
Updating 02d53c6..a7913d4
Fast-forward
 park1.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 park1.txt
[exit=0]
  local main : a7913d4 park commit 1 (setup)
  remote main: 02d53c6 docs: C7 fresh-session probe (Amear D-2026-11-08-C C7, bead gjj) - a praxis-manager spawned after b3c1efe reports no persistent-memory section; agent definitions read at session start; MANIFEST row 316; DECISION_LOG flush through 19:18:30Z
  main contains park1.txt? YES; remote main contains park1.txt? no

==================================================================
== Q1 ROUTE 2: git merge parked/Praxis_build-abc (non-ff; main diverged first)
==================================================================
(reset: local main=02d53c6 remote main=02d53c6 HEAD=parked/Praxis_build-abc)
$ cd /tmp/c2trip-mgr3/clone && git checkout -q main
[exit=0]
  setup: main now 3ed264b main diverging commit (setup)
--- PreToolUse hooks for command: git merge parked/Praxis_build-abc
  [caller=master] payload identity: {"agent_type":"praxis-master","agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=plain] payload identity: {"agent_type":null,"agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=sub] payload identity: {"agent_type":"praxis-worker","agent_id":"a1"}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=2 stderr=BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
$ cd /tmp/c2trip-mgr3/clone && git merge parked/Praxis_build-abc
Merge made by the 'ort' strategy.
 park1.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 park1.txt
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone log --oneline --graph -4 main
*   636bd5b Merge branch 'parked/Praxis_build-abc'
|\  
| * a7913d4 park commit 1 (setup)
* | 3ed264b main diverging commit (setup)
|/  
* 02d53c6 docs: C7 fresh-session probe (Amear D-2026-11-08-C C7, bead gjj) - a praxis-manager spawned after b3c1efe reports no persistent-memory section; agent definitions read at session start; MANIFEST row 316; DECISION_LOG flush through 19:18:30Z
[exit=0]
  local main : 636bd5b Merge branch 'parked/Praxis_build-abc'
  remote main: 02d53c6 docs: C7 fresh-session probe (Amear D-2026-11-08-C C7, bead gjj) - a praxis-manager spawned after b3c1efe reports no persistent-memory section; agent definitions read at session start; MANIFEST row 316; DECISION_LOG flush through 19:18:30Z
  main contains park1.txt? YES; remote main contains park1.txt? no

==================================================================
== Q1 ROUTE 3: git push scratch parked/Praxis_build-abc:main
==================================================================
(reset: local main=02d53c6 remote main=02d53c6 HEAD=parked/Praxis_build-abc)
--- PreToolUse hooks for command: git push scratch parked/Praxis_build-abc:main
  [caller=master] payload identity: {"agent_type":"praxis-master","agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=plain] payload identity: {"agent_type":null,"agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=sub] payload identity: {"agent_type":"praxis-worker","agent_id":"a1"}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=2 stderr=BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
$ cd /tmp/c2trip-mgr3/clone && git push scratch parked/Praxis_build-abc:main
To /tmp/c2trip-mgr3/remote.git
   02d53c6..a7913d4  parked/Praxis_build-abc -> main
[exit=0]
  local main : 02d53c6 docs: C7 fresh-session probe (Amear D-2026-11-08-C C7, bead gjj) - a praxis-manager spawned after b3c1efe reports no persistent-memory section; agent definitions read at session start; MANIFEST row 316; DECISION_LOG flush through 19:18:30Z
  remote main: a7913d4 park commit 1 (setup)
  main contains park1.txt? no; remote main contains park1.txt? YES

==================================================================
== Q1 ROUTE 4: git cherry-pick <P1> onto main
==================================================================
(reset: local main=02d53c6 remote main=02d53c6 HEAD=parked/Praxis_build-abc)
$ cd /tmp/c2trip-mgr3/clone && git checkout -q main
[exit=0]
--- PreToolUse hooks for command: git cherry-pick a7913d4d9f96ab79cf5e2c4b6ade98e124320f33
  [caller=master] payload identity: {"agent_type":"praxis-master","agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=plain] payload identity: {"agent_type":null,"agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=sub] payload identity: {"agent_type":"praxis-worker","agent_id":"a1"}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
$ cd /tmp/c2trip-mgr3/clone && git cherry-pick a7913d4d9f96ab79cf5e2c4b6ade98e124320f33
[main 91e7551] park commit 1 (setup)
 Date: Tue Nov 10 00:58:11 2026 -0500
 1 file changed, 1 insertion(+)
 create mode 100644 park1.txt
[exit=0]
  local main : 91e7551 park commit 1 (setup)
  remote main: 02d53c6 docs: C7 fresh-session probe (Amear D-2026-11-08-C C7, bead gjj) - a praxis-manager spawned after b3c1efe reports no persistent-memory section; agent definitions read at session start; MANIFEST row 316; DECISION_LOG flush through 19:18:30Z
  main contains park1.txt? YES; remote main contains park1.txt? no

==================================================================
== Q1 ROUTE 5: git branch -f main parked/Praxis_build-abc (HEAD on parked)
==================================================================
(reset: local main=02d53c6 remote main=02d53c6 HEAD=parked/Praxis_build-abc)
--- PreToolUse hooks for command: git branch -f main parked/Praxis_build-abc
  [caller=master] payload identity: {"agent_type":"praxis-master","agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=plain] payload identity: {"agent_type":null,"agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=sub] payload identity: {"agent_type":"praxis-worker","agent_id":"a1"}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
$ cd /tmp/c2trip-mgr3/clone && git branch -f main parked/Praxis_build-abc
[exit=0]
  local main : a7913d4 park commit 1 (setup)
  remote main: 02d53c6 docs: C7 fresh-session probe (Amear D-2026-11-08-C C7, bead gjj) - a praxis-manager spawned after b3c1efe reports no persistent-memory section; agent definitions read at session start; MANIFEST row 316; DECISION_LOG flush through 19:18:30Z
  main contains park1.txt? YES; remote main contains park1.txt? no

==================================================================
== Q1 ROUTE 6: git update-ref refs/heads/main <P1>
==================================================================
(reset: local main=02d53c6 remote main=02d53c6 HEAD=parked/Praxis_build-abc)
--- PreToolUse hooks for command: git update-ref refs/heads/main a7913d4d9f96ab79cf5e2c4b6ade98e124320f33
  [caller=master] payload identity: {"agent_type":"praxis-master","agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=plain] payload identity: {"agent_type":null,"agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=sub] payload identity: {"agent_type":"praxis-worker","agent_id":"a1"}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
$ cd /tmp/c2trip-mgr3/clone && git update-ref refs/heads/main a7913d4d9f96ab79cf5e2c4b6ade98e124320f33
[exit=0]
  local main : a7913d4 park commit 1 (setup)
  remote main: 02d53c6 docs: C7 fresh-session probe (Amear D-2026-11-08-C C7, bead gjj) - a praxis-manager spawned after b3c1efe reports no persistent-memory section; agent definitions read at session start; MANIFEST row 316; DECISION_LOG flush through 19:18:30Z
  main contains park1.txt? YES; remote main contains park1.txt? no

==================================================================
== Q1 ROUTE 7: git push scratch parked/Praxis_build-abc (parked branch only)
==================================================================
(reset: local main=02d53c6 remote main=02d53c6 HEAD=parked/Praxis_build-abc)
--- PreToolUse hooks for command: git push scratch parked/Praxis_build-abc
  [caller=master] payload identity: {"agent_type":"praxis-master","agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=plain] payload identity: {"agent_type":null,"agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=sub] payload identity: {"agent_type":"praxis-worker","agent_id":"a1"}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=2 stderr=BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
$ cd /tmp/c2trip-mgr3/clone && git push scratch parked/Praxis_build-abc
To /tmp/c2trip-mgr3/remote.git
 * [new branch]      parked/Praxis_build-abc -> parked/Praxis_build-abc
[exit=0]
$ git --git-dir=/tmp/c2trip-mgr3/remote.git branch -a -v
* main                    02d53c6 docs: C7 fresh-session probe (Amear D-2026-11-08-C C7, bead gjj) - a praxis-manager spawned after b3c1efe reports no persistent-memory section; agent definitions read at session start; MANIFEST row 316; DECISION_LOG flush through 19:18:30Z
  parked/Praxis_build-abc a7913d4 park commit 1 (setup)
[exit=0]
  local main : 02d53c6 docs: C7 fresh-session probe (Amear D-2026-11-08-C C7, bead gjj) - a praxis-manager spawned after b3c1efe reports no persistent-memory section; agent definitions read at session start; MANIFEST row 316; DECISION_LOG flush through 19:18:30Z
  remote main: 02d53c6 docs: C7 fresh-session probe (Amear D-2026-11-08-C C7, bead gjj) - a praxis-manager spawned after b3c1efe reports no persistent-memory section; agent definitions read at session start; MANIFEST row 316; DECISION_LOG flush through 19:18:30Z
  main contains park1.txt? no; remote main contains park1.txt? no

==================================================================

== GITHUB (read-only GET)
==================================================================
$ git -C /Volumes/Sensidine/Praxis.build remote -v
origin	https://github.com/amear238/praxis.build.git (fetch)
origin	https://github.com/amear238/praxis.build.git (push)
[exit=0]
$ gh api repos/amear238/praxis.build/branches/main/protection
{"message":"Branch not protected","documentation_url":"https://docs.github.com/rest/branches/branch-protection#get-branch-protection","status":"404"}gh: Branch not protected (HTTP 404)
[exit=1]
$ gh api repos/amear238/praxis.build/branches/main --jq '.protected'
false
[exit=0]
$ gh api repos/amear238/praxis.build/rulesets
[][exit=0]
$ gh api repos/amear238/praxis.build/rules/branches/main
[][exit=0]
$ gh api repos/amear238/praxis.build/rules/branches/parked/Praxis_build-abc
[][exit=0]
```

### E4. S6 cross-block: the park payload through every PreToolUse Bash hook, and PostToolUse commit-tree-verify.sh after a real park commit (same manager re-run, log lines 360-703, verbatim)
```text
== Q2(i): park commit payload, HEAD on parked/Praxis_build-abc, staged park2.txt
==================================================================
(reset: local main=02d53c6 remote main=02d53c6 HEAD=parked/Praxis_build-abc)
$ git -C /tmp/c2trip-mgr3/clone add park2.txt
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone symbolic-ref HEAD
refs/heads/parked/Praxis_build-abc
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone diff --cached --stat
 park2.txt | 1 +
 1 file changed, 1 insertion(+)
[exit=0]
--- PreToolUse hooks for command: git commit -m "park wip"
  [caller=master] payload identity: {"agent_type":"praxis-master","agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=plain] payload identity: {"agent_type":null,"agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=0 stderr=Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=sub] payload identity: {"agent_type":"praxis-worker","agent_id":"a1"}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=2 stderr=BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=2 stderr=Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>

-- CONTROL: same payload with HEAD on main (expect the gate to deny on the token route)
$ git -C /tmp/c2trip-mgr3/clone symbolic-ref HEAD
refs/heads/main
[exit=0]
--- PreToolUse hooks for command: git commit -m "park wip"
  [caller=master] payload identity: {"agent_type":"praxis-master","agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=2 stderr=Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=plain] payload identity: {"agent_type":null,"agent_id":null}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=2 stderr=Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
  [caller=sub] payload identity: {"agent_type":"praxis-worker","agent_id":"a1"}
    "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh exit=2 stderr=BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
    "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh exit=2 stderr=Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
    "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh exit=0 stderr=<empty>
    "$CLAUDE_PROJECT_DIR"/scripts/mint-guard.sh      exit=0 stderr=<empty>
$ git -C /tmp/c2trip-mgr3/clone symbolic-ref HEAD
refs/heads/parked/Praxis_build-abc
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone diff --cached --stat
 park2.txt | 1 +
 1 file changed, 1 insertion(+)
[exit=0]
PostToolUse Bash hook command as registered: "$CLAUDE_PROJECT_DIR"/scripts/commit-tree-verify.sh

==================================================================
== Q2(ii) CASE A: real park commit, NO last-allowed file present
==================================================================
$ git -C /tmp/c2trip-mgr3/clone symbolic-ref HEAD
refs/heads/parked/Praxis_build-abc
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone diff --cached --stat
 park2.txt | 1 +
 1 file changed, 1 insertion(+)
[exit=0]
  -- .claude/state:
     total 0
     drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:58 .
     drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:58 ..
     -rw-r--r--@ 1 admin  wheel    0 Nov 10 00:58 orchestrator-active
  (notify.sh present in clone hooks dir)
  gate({agent_type:"praxis-master"}) on 'git commit -m "park wip"': exit=0 stderr=Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
$ cd /tmp/c2trip-mgr3/clone && git commit -m "park wip"
[parked/Praxis_build-abc f5be720] park wip
 1 file changed, 1 insertion(+)
 create mode 100644 park2.txt
[exit=0]
$ git -C /tmp/c2trip-mgr3/clone log --oneline -2
f5be720 park wip
a7913d4 park commit 1 (setup)
[exit=0]
  PostToolUse payload: {"session_id":"c2trip-w3","transcript_path":"/tmp/c2trip-mgr3/fake-transcript.jsonl","cwd":"/tmp/c2trip-mgr3/clone","permission_mode":"bypassPermissions","hook_event_name":"PostToolUse","tool_name":"Bash","tool_input":{"command":"git commit -m \"park wip\"","description":"probe"},"tool_response":{"stdout":"[parked/Praxis_build-abc f5be720] park wip\n 1 file changed, 1 insertion(+)\n create mode 100644 park2.txt","stderr":"","interrupted":false,"isImage":false},"tool_use_id":"toolu_c2trip","agent_type":"praxis-master"}
  "$CLAUDE_PROJECT_DIR"/scripts/commit-tree-verify.sh exit=0
  stderr: <empty>
  -- .claude/state:
     total 0
     drwxr-xr-x@ 3 admin  wheel   96 Nov 10 00:58 .
     drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:58 ..
     -rw-r--r--@ 1 admin  wheel    0 Nov 10 00:58 orchestrator-active
  (notify.sh present in clone hooks dir)

==================================================================
== Q2(ii) CASE B1: stale last-allowed from an earlier token commit with DIFFERENT command text
==================================================================
  setup: on main, staged tokfile.txt hash=68c3672bd951f97fc3d4d561414bd9da310b3bcfb3200263522c6f21548a75c8 tree=bac70f7585b49a7f26712be4e9c4bde7603119d1; scratch token + AUDIT_LOG row written in the clone
  gate({}) on 'git commit -m "audited change"': exit=0 stderr=<empty>
  (the token-route commit is NOT executed and no PostToolUse is delivered for it -> record left behind,
   e.g. a co-registered PreToolUse hook denied the call after the gate allowed it)
  -- .claude/state:
     total 8
     drwxr-xr-x@ 4 admin  wheel  128 Nov 10 00:58 .
     drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:58 ..
     -rw-r--r--@ 1 admin  wheel  270 Nov 10 00:58 last-allowed
     -rw-r--r--@ 1 admin  wheel    0 Nov 10 00:58 orchestrator-active
  -- /tmp/c2trip-mgr3/clone/.claude/state/last-allowed:
     tree=bac70f7585b49a7f26712be4e9c4bde7603119d1
     index=REAL
     hash=68c3672bd951f97fc3d4d561414bd9da310b3bcfb3200263522c6f21548a75c8
     head_before=02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
     ts=1794290301
     cmd_sha256=b9d0217ed1f60dc94eb43673fd6c0e7c2e08036a345a7bac570a7f85f29b2947
  (notify.sh present in clone hooks dir)
$ git -C /tmp/c2trip-mgr3/clone symbolic-ref HEAD
refs/heads/parked/Praxis_build-abc
[exit=0]
  gate({agent_type:"praxis-master"}) on 'git commit -m "park wip 3"': exit=0 stderr=Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
$ cd /tmp/c2trip-mgr3/clone && git commit -m "park wip 3"
[parked/Praxis_build-abc 7e53422] park wip 3
 1 file changed, 1 insertion(+)
 create mode 100644 park3.txt
[exit=0]
  PostToolUse payload: {"session_id":"c2trip-w3","transcript_path":"/tmp/c2trip-mgr3/fake-transcript.jsonl","cwd":"/tmp/c2trip-mgr3/clone","permission_mode":"bypassPermissions","hook_event_name":"PostToolUse","tool_name":"Bash","tool_input":{"command":"git commit -m \"park wip 3\"","description":"probe"},"tool_response":{"stdout":"[parked/Praxis_build-abc 7e53422] park wip 3\n 1 file changed, 1 insertion(+)\n create mode 100644 park3.txt","stderr":"","interrupted":false,"isImage":false},"tool_use_id":"toolu_c2trip","agent_type":"praxis-master"}
  "$CLAUDE_PROJECT_DIR"/scripts/commit-tree-verify.sh exit=0
  stderr: <empty>
  -- .claude/state:
     total 8
     drwxr-xr-x@ 4 admin  wheel  128 Nov 10 00:58 .
     drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:58 ..
     -rw-r--r--@ 1 admin  wheel  270 Nov 10 00:58 last-allowed
     -rw-r--r--@ 1 admin  wheel    0 Nov 10 00:58 orchestrator-active
  -- /tmp/c2trip-mgr3/clone/.claude/state/last-allowed:
     tree=bac70f7585b49a7f26712be4e9c4bde7603119d1
     index=REAL
     hash=68c3672bd951f97fc3d4d561414bd9da310b3bcfb3200263522c6f21548a75c8
     head_before=02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
     ts=1794290301
     cmd_sha256=b9d0217ed1f60dc94eb43673fd6c0e7c2e08036a345a7bac570a7f85f29b2947
  (notify.sh present in clone hooks dir)

==================================================================
== Q2(ii) CASE B2: stale last-allowed from an earlier token commit with IDENTICAL command text
==================================================================
  setup: on main, staged tokfile.txt hash=12a76824c49ec3510271ad025ad705f3dd196eb02a33f8a96d23e7ac88ae3669 tree=5fc9ad20db8d6435406c8fc49d701136296888e3; scratch token + AUDIT_LOG row written in the clone
  gate({}) on 'git commit -m "park wip"': exit=0 stderr=<empty>
  (the token-route commit is NOT executed and no PostToolUse is delivered for it -> record left behind,
   e.g. a co-registered PreToolUse hook denied the call after the gate allowed it)
  -- .claude/state:
     total 8
     drwxr-xr-x@ 4 admin  wheel  128 Nov 10 00:58 .
     drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:58 ..
     -rw-r--r--@ 1 admin  wheel  270 Nov 10 00:58 last-allowed
     -rw-r--r--@ 1 admin  wheel    0 Nov 10 00:58 orchestrator-active
  -- /tmp/c2trip-mgr3/clone/.claude/state/last-allowed:
     tree=5fc9ad20db8d6435406c8fc49d701136296888e3
     index=REAL
     hash=12a76824c49ec3510271ad025ad705f3dd196eb02a33f8a96d23e7ac88ae3669
     head_before=02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
     ts=1794290302
     cmd_sha256=336ff26e3319cb3a38d58751651fa21494ac3f62aeff24b65e06582ce7737b32
  (notify.sh present in clone hooks dir)
$ git -C /tmp/c2trip-mgr3/clone symbolic-ref HEAD
refs/heads/parked/Praxis_build-abc
[exit=0]
  gate({agent_type:"praxis-master"}) on 'git commit -m "park wip"': exit=0 stderr=Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-abc'. No token consumed.
$ cd /tmp/c2trip-mgr3/clone && git commit -m "park wip"
[parked/Praxis_build-abc 37857c4] park wip
 1 file changed, 1 insertion(+)
 create mode 100644 park4.txt
[exit=0]
  PostToolUse payload: {"session_id":"c2trip-w3","transcript_path":"/tmp/c2trip-mgr3/fake-transcript.jsonl","cwd":"/tmp/c2trip-mgr3/clone","permission_mode":"bypassPermissions","hook_event_name":"PostToolUse","tool_name":"Bash","tool_input":{"command":"git commit -m \"park wip\"","description":"probe"},"tool_response":{"stdout":"[parked/Praxis_build-abc 37857c4] park wip\n 1 file changed, 1 insertion(+)\n create mode 100644 park4.txt","stderr":"","interrupted":false,"isImage":false},"tool_use_id":"toolu_c2trip","agent_type":"praxis-master"}
  "$CLAUDE_PROJECT_DIR"/scripts/commit-tree-verify.sh exit=2
  stderr: COMMIT TREE MISMATCH: the gate allowed tree 5fc9ad20db8d6435406c8fc49d701136296888e3 (index REAL, hash 12a76824c49ec3510271ad025ad705f3dd196eb02a33f8a96d23e7ac88ae3669) but the new HEAD 37857c4b23624aeee01fb816c9773882d86dcdde has tree b7e79cd20edc23c858ab1cb6c554ba61c0c6bd30
git diff --stat 5fc9ad20db8d6435406c8fc49d701136296888e3 HEAD^{tree}:
 park1.txt   | 1 +
 park2.txt   | 1 +
 park3.txt   | 1 +
 park4.txt   | 1 +
 tokfile.txt | 1 -
 5 files changed, 4 insertions(+), 1 deletion(-)
This hook cannot undo the commit. Something changed the index after the gate allowed it (git pre-commit hook, background job). Do not push; report to the trader and revert the unaudited content.
  -- .claude/state:
     total 8
     drwxr-xr-x@ 4 admin  wheel  128 Nov 10 00:58 .
     drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:58 ..
     -rw-r--r--@ 1 admin  wheel  298 Nov 10 00:58 mint-log
     -rw-r--r--@ 1 admin  wheel    0 Nov 10 00:58 orchestrator-active
  -- /tmp/c2trip-mgr3/clone/.claude/state/mint-log:
     2026-11-10T05:58:23Z COMMIT TREE MISMATCH: the gate allowed tree 5fc9ad20db8d6435406c8fc49d701136296888e3 (index REAL, hash 12a76824c49ec3510271ad025ad705f3dd196eb02a33f8a96d23e7ac88ae3669) but the new HEAD 37857c4b23624aeee01fb816c9773882d86dcdde has tree b7e79cd20edc23c858ab1cb6c554ba61c0c6bd30
  (notify.sh present in clone hooks dir)

==================================================================
== Q2(ii) CASE B3: stale record lingering (B1-style) then the NEXT ordinary Bash call
==================================================================
  setup: on main, staged tokfile.txt hash=d65febba10cbe5889b159928f1f78d7d481be141c071b7d5a0e3ff9e43ab0eae tree=6d7eccebb6949f7a38a9924a9b14eb88411440ae; scratch token + AUDIT_LOG row written in the clone
  gate({}) on 'git status': exit=0 stderr=<empty>
  (the token-route commit is NOT executed and no PostToolUse is delivered for it -> record left behind,
   e.g. a co-registered PreToolUse hook denied the call after the gate allowed it)
  -- .claude/state:
     total 16
     drwxr-xr-x@ 5 admin  wheel  160 Nov 10 00:58 .
     drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:58 ..
     -rw-r--r--@ 1 admin  wheel   46 Nov 10 00:58 audit-pass-d65febba10cbe5889b159928f1f78d7d481be141c071b7d5a0e3ff9e43ab0eae
     -rw-r--r--@ 1 admin  wheel  298 Nov 10 00:58 mint-log
     -rw-r--r--@ 1 admin  wheel    0 Nov 10 00:58 orchestrator-active
  -- /tmp/c2trip-mgr3/clone/.claude/state/mint-log:
     2026-11-10T05:58:23Z COMMIT TREE MISMATCH: the gate allowed tree 5fc9ad20db8d6435406c8fc49d701136296888e3 (index REAL, hash 12a76824c49ec3510271ad025ad705f3dd196eb02a33f8a96d23e7ac88ae3669) but the new HEAD 37857c4b23624aeee01fb816c9773882d86dcdde has tree b7e79cd20edc23c858ab1cb6c554ba61c0c6bd30
  (notify.sh present in clone hooks dir)
  note: the gate pre-filter only reaches token route for commit text; 'git status' never writes a record.
  setup: on main, staged tokfile.txt hash=106e5d57ae2760c6df93488478183b91e03220dabc9e3063abd47703c9587085 tree=862aeb838cb71fc07fb1401b17f31856315dd9c9; scratch token + AUDIT_LOG row written in the clone
  gate({}) on 'git commit -m "later audited"': exit=0 stderr=<empty>
  (the token-route commit is NOT executed and no PostToolUse is delivered for it -> record left behind,
   e.g. a co-registered PreToolUse hook denied the call after the gate allowed it)
  -- .claude/state:
     total 24
     drwxr-xr-x@ 6 admin  wheel  192 Nov 10 00:58 .
     drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:58 ..
     -rw-r--r--@ 1 admin  wheel   46 Nov 10 00:58 audit-pass-d65febba10cbe5889b159928f1f78d7d481be141c071b7d5a0e3ff9e43ab0eae
     -rw-r--r--@ 1 admin  wheel  270 Nov 10 00:58 last-allowed
     -rw-r--r--@ 1 admin  wheel  298 Nov 10 00:58 mint-log
     -rw-r--r--@ 1 admin  wheel    0 Nov 10 00:58 orchestrator-active
  -- /tmp/c2trip-mgr3/clone/.claude/state/last-allowed:
     tree=862aeb838cb71fc07fb1401b17f31856315dd9c9
     index=REAL
     hash=106e5d57ae2760c6df93488478183b91e03220dabc9e3063abd47703c9587085
     head_before=02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
     ts=1794290304
     cmd_sha256=7c60b5431476c23774fa5b075e5ec7695f3a07ca16e4c6936d235614347b741f
  -- /tmp/c2trip-mgr3/clone/.claude/state/mint-log:
     2026-11-10T05:58:23Z COMMIT TREE MISMATCH: the gate allowed tree 5fc9ad20db8d6435406c8fc49d701136296888e3 (index REAL, hash 12a76824c49ec3510271ad025ad705f3dd196eb02a33f8a96d23e7ac88ae3669) but the new HEAD 37857c4b23624aeee01fb816c9773882d86dcdde has tree b7e79cd20edc23c858ab1cb6c554ba61c0c6bd30
  (notify.sh present in clone hooks dir)
  PostToolUse payload: {"session_id":"c2trip-w3","transcript_path":"/tmp/c2trip-mgr3/fake-transcript.jsonl","cwd":"/tmp/c2trip-mgr3/clone","permission_mode":"bypassPermissions","hook_event_name":"PostToolUse","tool_name":"Bash","tool_input":{"command":"ls","description":"probe"},"tool_response":{"stdout":"","stderr":"","interrupted":false,"isImage":false},"tool_use_id":"toolu_c2trip","agent_type":"praxis-master"}
  "$CLAUDE_PROJECT_DIR"/scripts/commit-tree-verify.sh exit=0
  stderr: <empty>
  -- .claude/state:
     total 24
     drwxr-xr-x@ 6 admin  wheel  192 Nov 10 00:58 .
     drwxr-xr-x@ 7 admin  wheel  224 Nov 10 00:58 ..
     -rw-r--r--@ 1 admin  wheel   46 Nov 10 00:58 audit-pass-d65febba10cbe5889b159928f1f78d7d481be141c071b7d5a0e3ff9e43ab0eae
     -rw-r--r--@ 1 admin  wheel  270 Nov 10 00:58 last-allowed
     -rw-r--r--@ 1 admin  wheel  298 Nov 10 00:58 mint-log
     -rw-r--r--@ 1 admin  wheel    0 Nov 10 00:58 orchestrator-active
  -- /tmp/c2trip-mgr3/clone/.claude/state/last-allowed:
     tree=862aeb838cb71fc07fb1401b17f31856315dd9c9
     index=REAL
     hash=106e5d57ae2760c6df93488478183b91e03220dabc9e3063abd47703c9587085
     head_before=02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
     ts=1794290304
     cmd_sha256=7c60b5431476c23774fa5b075e5ec7695f3a07ca16e4c6936d235614347b741f
  -- /tmp/c2trip-mgr3/clone/.claude/state/mint-log:
     2026-11-10T05:58:23Z COMMIT TREE MISMATCH: the gate allowed tree 5fc9ad20db8d6435406c8fc49d701136296888e3 (index REAL, hash 12a76824c49ec3510271ad025ad705f3dd196eb02a33f8a96d23e7ac88ae3669) but the new HEAD 37857c4b23624aeee01fb816c9773882d86dcdde has tree b7e79cd20edc23c858ab1cb6c554ba61c0c6bd30
  (notify.sh present in clone hooks dir)

==================================================================
== Q2(iii) grep: last-allowed | audit-pass | AUDIT_LOG | mint-log in real .claude/hooks and scripts (read-only)
==================================================================
$ cd /Volumes/Sensidine/Praxis.build && grep -rn -E 'last-allowed|audit-pass|AUDIT_LOG|mint-log' .claude/hooks scripts
.claude/hooks/audit-approve.sh:31:printf 'tree=%s\n' "$TREE" > "$STATE/audit-pass-$HASH"
.claude/hooks/audit-approve.sh:32:printf '%s %s %s PASS\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$BEAD" "$HASH" >> "$ROOT/AUDIT_LOG.md"
.claude/hooks/gate-commit.sh:4:# AUDIT_LOG PASS row proves the orchestrator-auditor minted it. Armed only while
.claude/hooks/gate-commit.sh:74:#   E. at ALLOW the gate writes .claude/state/last-allowed (tree, index, hash,
.claude/hooks/gate-commit.sh:92:#   token consumed, no last-allowed record, nothing appended to the mint log
.claude/hooks/gate-commit.sh:277:  # allows, and can stage extra content and rewrite last-allowed so the
.claude/hooks/gate-commit.sh:668:# --- Token + AUDIT_LOG checks: only a fresh token whose hash also appears as a
.claude/hooks/gate-commit.sh:669:# PASS row in AUDIT_LOG.md is honored (a bare `touch`ed token is forgery). ---
.claude/hooks/gate-commit.sh:672:find "$STATE" -name 'audit-pass-*' -mmin +30 -exec rm -f {} + 2>/dev/null
.claude/hooks/gate-commit.sh:679:TOKEN="$STATE/audit-pass-$HASH"
.claude/hooks/gate-commit.sh:712:  if ! grep -q "$HASH PASS" "$ROOT/AUDIT_LOG.md" 2>/dev/null; then
.claude/hooks/gate-commit.sh:714:    echo "Commit denied: token has no AUDIT_LOG PASS row — forged or corrupted; re-dispatch the auditor." >&2
.claude/hooks/gate-commit.sh:767:  _la="$STATE/last-allowed"
.claude/hooks/auditor-mint.sh:3:# Mints a single-use commit token .claude/state/audit-pass-<hash> when a
.claude/hooks/auditor-mint.sh:15:# appends one line to $ROOT/.claude/state/mint-log (MINTED or REFUSED).
.claude/hooks/auditor-mint.sh:35:MLOG="$STATE/mint-log"
.claude/hooks/auditor-mint.sh:152:TOKEN="$STATE/audit-pass-$CLAIM_HASH"
.claude/hooks/auditor-mint.sh:162:printf '%s praxis-auditor:%s %s PASS index=%s\n' "$TS" "$AID" "$CLAIM_HASH" "$INDEX" >> "$ROOT/AUDIT_LOG.md" 2>/dev/null \
.claude/hooks/auditor-mint.sh:163:  || { rm -f "$TOKEN" 2>/dev/null; refuse "could not append AUDIT_LOG row"; }
scripts/commit-tree-verify.sh:16:# Protocol: when the gate ALLOWS a commit it writes .claude/state/last-allowed:
scripts/commit-tree-verify.sh:21:#   - no last-allowed file                        -> exit 0, silent
scripts/commit-tree-verify.sh:27:#                              stderr, same line appended to mint-log (exit 2)
scripts/commit-tree-verify.sh:34:# allow overwrites it. Every actor runs as the same uid: deleting last-allowed
scripts/commit-tree-verify.sh:40:LA="$ST/last-allowed"
scripts/commit-tree-verify.sh:58:logline() { mkdir -p "$ST" 2>/dev/null; printf '%s %s\n' "$TS" "$1" >> "$ST/mint-log" 2>/dev/null; }
scripts/audit-log-flush-verify.sh:2:# Machine verification for AUDIT_LOG "flush" commits (bead 30h).
scripts/audit-log-flush-verify.sh:7:# is a dedicated flush commit that stages ONLY AUDIT_LOG.md; the auditor runs
scripts/audit-log-flush-verify.sh:13:#   * staged set is exactly AUDIT_LOG.md
scripts/audit-log-flush-verify.sh:14:#   * the staged AUDIT_LOG diff is append-only (no removed/edited lines)
scripts/audit-log-flush-verify.sh:44:# --- flush shape: exactly AUDIT_LOG.md staged, append-only ---
scripts/audit-log-flush-verify.sh:46:[ -n "$STAGED_SET" ] || die "nothing is staged — stage AUDIT_LOG.md alone, then re-run"
scripts/audit-log-flush-verify.sh:47:[ "$STAGED_SET" = "AUDIT_LOG.md" ] || die "flush staged set must be EXACTLY AUDIT_LOG.md; got: $(printf '%s' "$STAGED_SET" | tr '\n' ' ')"
scripts/audit-log-flush-verify.sh:48:REMOVED=$(git diff --cached -- AUDIT_LOG.md | grep -cE '^-([^-]|$)')
scripts/audit-log-flush-verify.sh:50:ADDED=$(git diff --cached -- AUDIT_LOG.md | grep -E '^\+([^+]|$)' | cut -c2-)
scripts/audit-log-flush-verify.sh:51:[ -n "$ADDED" ] || die "staged AUDIT_LOG.md diff adds no lines — nothing to flush"
scripts/audit-log-flush-verify.sh:53:STAGED_LOG=$(git show :AUDIT_LOG.md)
scripts/mint-guard.sh:7:#           audit-pass-; or naming AUDIT_LOG together with a write form.
scripts/mint-guard.sh:8:#   Write/Edit/NotebookEdit — a path ending AUDIT_LOG.md or containing
scripts/mint-guard.sh:9:#           .claude/state/audit-pass-
scripts/mint-guard.sh:12:#           naming last-allowed or mint-log together with a write form (the
scripts/mint-guard.sh:13:#           AUDIT_LOG forms, plus rm/unlink/shred/touch/rmdir).
scripts/mint-guard.sh:15:#           under .claude/state/ named last-allowed* or mint-log*.
scripts/mint-guard.sh:18:#   `.claude/./state/last-allowed`, `.claude/hooks/../state/audit-pass-x`,
scripts/mint-guard.sh:19:#   `.claude//state/mint-log` used to pass): a relative path is joined to the
scripts/mint-guard.sh:27:#   or delete form (same forms as last-allowed / mint-log).
scripts/mint-guard.sh:36:# `>> audit_log.md` writes the real AUDIT_LOG.md.
scripts/mint-guard.sh:57:  echo "BLOCKED: mint-guard: $AGENT ($TOOL) $1 — audit tokens and AUDIT_LOG are written only by the minter, and the gate's state files (orchestrator-active, last-allowed, mint-log) only by the hooks (D-2026-11-04-B)." >&2
scripts/mint-guard.sh:62:# write_form: 0 if $CMD contains a write form (shared by AUDIT_LOG and the
scripts/mint-guard.sh:63:# fix-F state files). `|` alone is NOT one (cat AUDIT_LOG.md | head passes).
scripts/mint-guard.sh:65:# redirections to /dev/null are dropped first so `grep x AUDIT_LOG.md 2>/dev/null` passes.
scripts/mint-guard.sh:74:  #   cluster starting or ending in i; so `grep -i x AUDIT_LOG.md` is a
scripts/mint-guard.sh:78:# AUDIT_LOG's set is unchanged).
scripts/mint-guard.sh:83:  if grep -qiE 'audit-approve|auditor-mint|audit-provenance|audit-pass-' <<<"$CMD"; then
scripts/mint-guard.sh:86:  if grep -qi 'AUDIT_LOG' <<<"$CMD"; then
scripts/mint-guard.sh:88:      deny "command writes AUDIT_LOG"
scripts/mint-guard.sh:96:  if grep -qiE 'last-allowed|mint-log' <<<"$CMD"; then
scripts/mint-guard.sh:98:      deny "command writes or deletes a commit-gate state file (last-allowed / mint-log)"
scripts/mint-guard.sh:133:        *.claude/state/audit-pass-*) deny "targets $P" ;;
scripts/mint-guard.sh:135:        *.claude/state/last-allowed*|*.claude/state/mint-log*) deny "targets $P" ;;
scripts/audit-log-annotate.sh:2:# audit-log-annotate.sh — the ONLY sanctioned writer of AUDIT_LOG.md besides
scripts/audit-log-annotate.sh:3:# audit-approve.sh (bead 30h; standing rule: AUDIT_LOG.md is never edited by
scripts/audit-log-annotate.sh:20:LOG="$ROOT/AUDIT_LOG.md"
scripts/audit-log-annotate.sh:41:[ "$COUNT" = "1" ] || die "row-hash-prefix must match exactly ONE PASS row in AUDIT_LOG.md (matched $COUNT)"
scripts/test-gate-hardening.sh:63:TOKENS=$(ls "$SREPO/.claude/state"/audit-pass-* 2>/dev/null | wc -l | tr -d ' ')
scripts/test-gate-hardening.sh:100:touch "$SREPO/.claude/state/audit-pass-$HASH"          # old-format token: no tree=
scripts/test-gate-hardening.sh:101:echo "2026-07-10T00:00:00Z legacy $HASH PASS" >> "$SREPO/AUDIT_LOG.md"
[exit=0]

==================================================================
== Q2(iii) Stop / SessionStart / PreCompact / Subagent* hook files: same grep, per file
==================================================================
.claude/hooks/stop-gate.sh: 1
.claude/hooks/inject-handoff.sh: 0
.claude/hooks/precompact-handoff.sh: 1
scripts/dispatch-log-writeahead.sh: 0
scripts/dispatch-log-close.sh: 0
scripts/gate-manager-output.sh: 0
.claude/hooks/auditor-mint.sh: 7
.claude/hooks/notify.sh: 0
$ cd /Volumes/Sensidine/Praxis.build && grep -n -E 'commit|AUDIT|audit' scripts/dispatch-log-writeahead.sh .claude/hooks/stop-gate.sh .claude/hooks/inject-handoff.sh .claude/hooks/precompact-handoff.sh scripts/dispatch-log-close.sh scripts/gate-manager-output.sh
.claude/hooks/stop-gate.sh:34:  printf '{"decision":"block","reason":"Autonomous run incomplete: %s unblocked task(s) in bd ready (iteration %s/%s). Continue the dispatch->audit->commit loop on the next bd ready item. Consult RUN_DECISIONS.md before considering any question for the user."}\n' \
.claude/hooks/precompact-handoff.sh:20:  echo "You are mid-orchestrator-run. Re-read RUN_DECISIONS.md (if autonomous) and HANDOFF.md, then continue the dispatch->audit->commit loop from the bd ready queue above."
[exit=0]

==================================================================
```

### E5. W5 adversarial rows on the FINAL bytes 8471206f...c19f — WORKER OUTPUT, NOT RE-RUN

Source: /tmp/c2trip-w5/review.log, rows R01, R01b, R02, R02c (lines 173-368), R14 (589-623), R17b (668-727), and the main/non-parked comparison rows M1-M13/MT/M101-M112 (728-end), verbatim.
```text
w5 adversarial review of gate-commit.sh (C2 park exemption), 2026-11-10T05:55:47Z
artifact sha256 at start: 8471206f084b87e2fabae2d7375896d59bc273f6f97c33a89fc7865f7466c19f (checked before any row)
git: git version 2.50.1 (Apple Git-155)

################################ SCRIPT lib.sh ################################
#!/bin/bash
# shared helpers for the w5 review. Sourced by row scripts.
W=/tmp/c2trip-w5
GATE=/Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
GATEH=$W/gate-HEAD.sh
LOG=$W/review.log
export GIT_AUTHOR_NAME=w5 GIT_AUTHOR_EMAIL=w5@x GIT_COMMITTER_NAME=w5 GIT_COMMITTER_EMAIL=w5@x
[...]
=================== ROW R01: refs/heads/main is a symref to the parked branch; parked HEAD adds an evil pre-commit hook ===================
+ git -C /tmp/c2trip-w5/r01 switch -q parked/Praxis_build-w5a
Warning: /private/tmp/c2trip-w5/r01/.beads has permissions 0755 (recommended: 0700). Run: chmod 700 /private/tmp/c2trip-w5/r01/.beads
+ git -C /tmp/c2trip-w5/r01 stash list
++ git -C /tmp/c2trip-w5/r01 rev-parse HEAD
+ T0=02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
+ GIT_INDEX_FILE=/tmp/c2trip-w5/r01.idx
+ git -C /tmp/c2trip-w5/r01 read-tree HEAD
+ printf '#!/bin/sh\necho W5-EVIL-HOOK-RAN >&2\ntouch /tmp/c2trip-w5/r01.PWNED\n'
+ chmod 755 /tmp/c2trip-w5/r01/.beads/hooks/pre-commit
+ GIT_INDEX_FILE=/tmp/c2trip-w5/r01.idx
+ git -C /tmp/c2trip-w5/r01 update-index --add .beads/hooks/pre-commit
++ GIT_INDEX_FILE=/tmp/c2trip-w5/r01.idx
++ git -C /tmp/c2trip-w5/r01 write-tree
+ TR=031317af0e06152e7af8a60f30b1817ed7ac9f37
++ git -C /tmp/c2trip-w5/r01 commit-tree 031317af0e06152e7af8a60f30b1817ed7ac9f37 -p 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5 -m evil-hook
+ NC=cb204b9e1990aa1f12a43c4e59f57560c18cbe12
+ git -C /tmp/c2trip-w5/r01 update-ref refs/heads/parked/Praxis_build-w5a cb204b9e1990aa1f12a43c4e59f57560c18cbe12
+ git -C /tmp/c2trip-w5/r01 update-index --add .beads/hooks/pre-commit
+ git -C /tmp/c2trip-w5/r01 status --porcelain
A  README.w5
+ echo '-- control: main is a plain ref -> X3 should deny'
-- control: main is a plain ref -> X3 should deny
+ rungate /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh /tmp/c2trip-w5/r01 /tmp/c2trip-w5/p00.json
+ local g=/Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh root=/tmp/c2trip-w5/r01 pf=/tmp/c2trip-w5/p00.json
++ basename /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
+ local rc=2
+ echo exit=2
exit=2
++ basename /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
+ cat /tmp/c2trip-w5/p00.json.err.gate-commit.sh
+ cd /tmp/c2trip-w5/r01
+ env -u GIT_INDEX_FILE CLAUDE_PROJECT_DIR=/tmp/c2trip-w5/r01 bash /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
Commit denied: git hooks dir '/private/tmp/c2trip-w5/r01/.beads/hooks' — park commit: the hooks dir in HEAD differs from refs/heads/main, or the comparison failed (a parked HEAD is unaudited). A git hook runs inside the commit after this gate has allowed it, so the stack master commits only while the effective hooks dir (core.hooksPath, else .git/hooks) matches HEAD. Revert or remove the hook change in its own Bash call, then re-issue the commit. Token NOT consumed.
+ echo '-- attack: make refs/heads/main a symref to the parked branch'
-- attack: make refs/heads/main a symref to the parked branch
+ git -C /tmp/c2trip-w5/r01 symbolic-ref refs/heads/main refs/heads/parked/Praxis_build-w5a
+ git -C /tmp/c2trip-w5/r01 symbolic-ref HEAD
refs/heads/parked/Praxis_build-w5a
+ git -C /tmp/c2trip-w5/r01 symbolic-ref --no-recurse HEAD
refs/heads/parked/Praxis_build-w5a
+ git -C /tmp/c2trip-w5/r01 rev-parse refs/heads/main
cb204b9e1990aa1f12a43c4e59f57560c18cbe12
+ rungate /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh /tmp/c2trip-w5/r01 /tmp/c2trip-w5/p00.json
+ local g=/Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh root=/tmp/c2trip-w5/r01 pf=/tmp/c2trip-w5/p00.json
++ basename /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
+ local rc=0
+ echo exit=0
exit=0
++ basename /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
+ cat /tmp/c2trip-w5/p00.json.err.gate-commit.sh
+ cd /tmp/c2trip-w5/r01
+ env -u GIT_INDEX_FILE CLAUDE_PROJECT_DIR=/tmp/c2trip-w5/r01 bash /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-w5a'. No token consumed.
+ echo '-- run the actual commit to see the hook execute'
-- run the actual commit to see the hook execute
+ rm -f /tmp/c2trip-w5/r01.PWNED
+ cd /tmp/c2trip-w5/r01
+ git commit -q -m 'w5 park'
W5-EVIL-HOOK-RAN
Warning: /private/tmp/c2trip-w5/r01/.beads has permissions 0755 (recommended: 0700). Run: chmod 700 /private/tmp/c2trip-w5/r01/.beads
+ echo 'commit rc=0'
commit rc=0
+ ls -l /tmp/c2trip-w5/r01.PWNED
-rw-r--r--@ 1 admin  wheel  0 Nov 10 00:50 /tmp/c2trip-w5/r01.PWNED
+ git -C /tmp/c2trip-w5/r01 log --oneline -2 refs/heads/parked/Praxis_build-w5a
abcc294 w5 park
cb204b9 evil-hook

################################ SCRIPT r02.sh ################################
#!/bin/bash
. /tmp/c2trip-w5/lib.sh
chmod 755 $W/bin/bd
P=$W/p02.json
# fresh parked repo helper
park() { mkrepo $1 >/dev/null; git -C $1 switch -q -c parked/Praxis_build-w5a; payload $1 > $P; }

row R01b "refs/heads/main moved (plain update-ref, not symref) to the evil parked tip"
C=$W/r01b; park $C
plumb_add $C .beads/hooks/pre-commit 100755 $EVIL
rungate $GATE $C $P
git -C $C update-ref refs/heads/main refs/heads/parked/Praxis_build-w5a
rungate $GATE $C $P

row R02 "git replace: replace main's commit object with the evil parked tip"
C=$W/r02; park $C
M=$(git -C $C rev-parse main)
plumb_add $C .beads/hooks/pre-commit 100755 $EVIL
T=$(git -C $C rev-parse HEAD)
rungate $GATE $C $P
git -C $C replace $M $T
echo "rev-parse main=$(git -C $C rev-parse main) (orig $M); tree via replace=$(git -C $C rev-parse 'main^{tree}') tip tree=$(git -C $C rev-parse 'HEAD^{tree}')"
rungate $GATE $C $P
rm -f $W/PWNED; ( cd $C && git commit -q -m "w5 park" ); echo "commit rc=$?"; ls -l $W/PWNED 2>&1
echo "-- R02 at git-HEAD gate (token route) for comparison:"; rungate $GATEH $C $P

row R02c "git replace: replace main's hooks-dir TREE object only"
C=$W/r02c; park $C
MH=$(git -C $C rev-parse 'main:.beads/hooks')
plumb_add $C .beads/hooks/pre-commit 100755 $EVIL
TH=$(git -C $C rev-parse 'HEAD:.beads/hooks')
git -C $C replace $MH $TH
rungate $GATE $C $P

row R12 "parked ref is itself a symref to main (HEAD -> parked -> main)"
C=$W/r12; park $C
git -C $C symbolic-ref refs/heads/parked/Praxis_build-w5a refs/heads/main
echo "HEAD=$(git -C $C symbolic-ref -q HEAD) norec=$(git -C $C symbolic-ref -q --no-recurse HEAD)"
rungate $GATE $C $P

row R03 "core.hooksPath='.' (repo root); staged real index change; then temp-index form with clean real index and root-level hook only on parked"
C=$W/r03; park $C
git -C $C config core.hooksPath .
rungate $GATE $C $P
git -C $C rm -q --cached README.w5; rm -f $C/README.w5
plumb_add $C pre-commit 100755 $EVIL
git -C $C status --porcelain --ignored | head
cp $C/.git/index $W/r03.tidx; echo t > $W/r03.f
GIT_INDEX_FILE=$W/r03.tidx git -C $C update-index --add --cacheinfo 100644,$(git -C $C hash-object -w $W/r03.f),tfile
payload $C "{}" "GIT_INDEX_FILE=$W/r03.tidx git commit -m w5" > $W/p03.json
rungate $GATE $C $W/p03.json

row R04 "core.hooksPath = subdir of a tracked dir (absent everywhere), then created untracked, then committed only on parked"
C=$W/r04; park $C
git -C $C config core.hooksPath .beads/hooks/sub
rungate $GATE $C $P
mkdir -p $C/.beads/hooks/sub; cp $EVIL $C/.beads/hooks/sub/pre-commit
rungate $GATE $C $P
rm -rf $C/.beads/hooks/sub
plumb_add $C .beads/hooks/sub/pre-commit 100755 $EVIL
rungate $GATE $C $P

row R05 "hooks dir absent on main, present (committed) on parked; includeIf onbranch sets hooksPath only on parked"
C=$W/r05; park $C
printf '[core]\n\thooksPath = newhooks\n' > $W/r05.inc
git -C $C config 'includeIf.onbranch:parked/**.path' $W/r05.inc
git -C $C rev-parse --git-path hooks
plumb_add $C newhooks/pre-commit 100755 $EVIL
rungate $GATE $C $P

row R06 "hooks dir path with spaces and glob chars, identical on main, modified on parked"
C=$W/r06; park $C
HD='h k[*]?'
git -C $C switch -q main; plumb_add $C "$HD/pre-commit" 100755 $W/bin/bd; git -C $C switch -q parked/Praxis_build-w5a; git -C $C reset -q --hard 2>/dev/null
git -C $C merge -q --ff-only main 2>&1 | tail -1
git -C $C add README.w5 2>/dev/null; echo w5 >> $C/README.w5; git -C $C add README.w5
git -C $C config core.hooksPath "$HD"
echo "-- identical to main:"; rungate $GATE $C $P
plumb_add $C "$HD/pre-commit" 100755 $EVIL
echo "-- evil on parked:"; rungate $GATE $C $P
mkdir -p "$C/h k[x]"; echo "-- sibling dir matching the glob literally:"; ls -d $C/h*

row R07 "hooks dir is a tracked symlink on parked: .beads/hooks -> evilhooks (in-repo, parked only); then -> a main dir with identical content"
C=$W/r07; park $C
plumb_add $C evilhooks/pre-commit 100755 $EVIL
git -C $C rm -r -q --cached .beads/hooks; rm -rf $C/.beads/hooks
idx=$W/r07.idx; rm -f $idx; GIT_INDEX_FILE=$idx git -C $C read-tree HEAD; GIT_INDEX_FILE=$idx git -C $C rm -r -q --cached .beads/hooks
plumb_add $C .beads/hooks 120000 ../evilhooks
ls -l $C/.beads/ | grep hooks; git -C $C rev-parse --git-path hooks
git -C $C status --porcelain | head
rungate $GATE $C $P
echo "-- symlink to a dir that also exists, identical, on main (.claude/hooks):"
plumb_add $C .beads/hooks 120000 ../.claude/hooks
rungate $GATE $C $P

row R08 "in-repo hooks dir inside .git (core.hooksPath=.git/myhooks) holding an executable hook"
C=$W/r08; park $C
mkdir -p $C/.git/myhooks; cp $EVIL $C/.git/myhooks/pre-commit
git -C $C config core.hooksPath .git/myhooks
rungate $GATE $C $P

################################ OUTPUT r02.out ################################

=================== ROW R01b: refs/heads/main moved (plain update-ref, not symref) to the evil parked tip ===================
exit=2
Commit denied: git hooks dir '/private/tmp/c2trip-w5/r01b/.beads/hooks' — park commit: the hooks dir in HEAD differs from refs/heads/main, or the comparison failed (a parked HEAD is unaudited). A git hook runs inside the commit after this gate has allowed it, so the stack master commits only while the effective hooks dir (core.hooksPath, else .git/hooks) matches HEAD. Revert or remove the hook change in its own Bash call, then re-issue the commit. Token NOT consumed.
exit=0
Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-w5a'. No token consumed.

=================== ROW R02: git replace: replace main's commit object with the evil parked tip ===================
exit=2
Commit denied: git hooks dir '/private/tmp/c2trip-w5/r02/.beads/hooks' — park commit: the hooks dir in HEAD differs from refs/heads/main, or the comparison failed (a parked HEAD is unaudited). A git hook runs inside the commit after this gate has allowed it, so the stack master commits only while the effective hooks dir (core.hooksPath, else .git/hooks) matches HEAD. Revert or remove the hook change in its own Bash call, then re-issue the commit. Token NOT consumed.
rev-parse main=02d53c66ccfa3105f8c8bba812678e9e77d1cbe5 (orig 02d53c66ccfa3105f8c8bba812678e9e77d1cbe5); tree via replace=f6db5066fb7cdc24a2fe3d6495da17870b372b83 tip tree=f6db5066fb7cdc24a2fe3d6495da17870b372b83
exit=0
Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-w5a'. No token consumed.
W5-EVIL-HOOK-RAN
commit rc=0
-rw-r--r--@ 1 admin  wheel  0 Nov 10 00:51 /tmp/c2trip-w5/PWNED
-- R02 at git-HEAD gate (token route) for comparison:
exit=2
Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.

=================== ROW R02c: git replace: replace main's hooks-dir TREE object only ===================
exit=0
Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-w5a'. No token consumed.

[...]
=================== ROW R14: race: background job armed earlier flips HEAD to main after the gate's final re-read ===================
exit=0
Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-w5a'. No token consumed.
[bg] HEAD flipped to main
commit rc=0
main before=02d53c66ccfa3105f8c8bba812678e9e77d1cbe5 after=89a553489d2ac58ca99f0ea63a1194462dae3687
89a5534 w5 park
orchestrator-active

################################ SCRIPT r04.sh ################################
#!/bin/bash
. /tmp/c2trip-w5/lib.sh
P=$W/p04.json
park() { mkrepo $1 >/dev/null; git -C $1 switch -q -c parked/Praxis_build-w5a; payload $1 > $P; }

row R16 "(redo) loose parked ref is a FILE SYMLINK to the loose refs/heads/main file (target ../main)"
C=$W/r16b; park $C
MB=$(git -C $C rev-parse refs/heads/main)
rm -f $C/.git/refs/heads/main; echo $MB > $C/.git/refs/heads/main
grep -c main $C/.git/packed-refs 2>/dev/null
rm -f $C/.git/refs/heads/parked/Praxis_build-w5a; ln -s ../main $C/.git/refs/heads/parked/Praxis_build-w5a
ls -l $C/.git/refs/heads/ $C/.git/refs/heads/parked/
echo "HEAD=$(git -C $C symbolic-ref -q HEAD) norec=$(git -C $C symbolic-ref -q --no-recurse HEAD) fer=$(git -C $C for-each-ref --format='%(refname)' refs/heads/parked/Praxis_build-w5a) tip=$(git -C $C rev-parse HEAD)"
rungate $GATE $C $P
( cd $C && git commit -q -m "w5 park" ); echo "commit rc=$?"
echo "main before=$MB after=$(git -C $C rev-parse refs/heads/main)"; ls -l $C/.git/refs/heads/main $C/.git/refs/heads/parked/

row R17 "refs/heads/parked DIRECTORY is a symlink to refs/heads/zz (physical alias)"
C=$W/r17; park $C
mkdir -p $C/.git/refs/heads/zz; mv $C/.git/refs/heads/parked/Praxis_build-w5a $C/.git/refs/heads/zz/; rmdir $C/.git/refs/heads/parked; ln -s zz $C/.git/refs/heads/parked
git -C $C for-each-ref --format='%(refname)' refs/heads/
rungate $GATE $C $P

################################ OUTPUT r04.out ################################

[...]
=================== ROW R17b: refs/heads/parked DIRECTORY is a symlink to ../tags: the park commit physically moves refs/tags/Praxis_build-w5a ===================
total 8
-rw-r--r--@ 1 admin  wheel  41 Nov 10 00:53 main
lrwxr-xr-x@ 1 admin  wheel   7 Nov 10 00:53 parked -> ../tags
refs/heads/main 02d53c6
refs/heads/parked/Praxis_build-w5a 02d53c6
refs/tags/Praxis_build-w5a 02d53c6
exit=0
Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch 'parked/Praxis_build-w5a'. No token consumed.
commit rc=0
refs/heads/main 02d53c6
refs/heads/parked/Praxis_build-w5a a4ff369
refs/tags/Praxis_build-w5a a4ff369

################################ SCRIPT r06.sh ################################
#!/bin/bash
. /tmp/c2trip-w5/lib.sh
C=$W/m; mkrepo $C
echo "HEAD=$(git -C $C symbolic-ref -q HEAD)"
cp $C/.git/index $W/m.tidx
GIT_INDEX_FILE=$W/m.tidx git -C $C update-index --add --cacheinfo 100644,$(git -C $C hash-object -w $W/bin/bd),tfile
i=0
t() { i=$((i+1)); row "M$i" "$1"; payload $C "$2" "$3" > $W/pm$i.json; python3 -I -c 'import json,sys;d=json.load(open(sys.argv[1]));print("payload cmd:",repr(d["tool_input"]["command"]),"extra:",{k:v for k,v in d.items() if k in("agent_type","agent_id")})' $W/pm$i.json; cmpgates $C $W/pm$i.json; }
suite() {
t "plain caller, clean form" "{}" 'git commit -m "w5"'
t "praxis-master, clean form" "{'agent_type':'praxis-master'}" 'git commit -m "w5"'
t "plain caller, temp-index form" "{}" "GIT_INDEX_FILE=$W/m.tidx git commit -m w5"
t "praxis-master, temp-index form" "{'agent_type':'praxis-master'}" "GIT_INDEX_FILE=$W/m.tidx git commit -m w5"
t "form violation -am" "{'agent_type':'praxis-master'}" 'git commit -am "w5"'
t "praxis-master pathspec without --" "{'agent_type':'praxis-master'}" 'git commit -m w5 README.w5'
t "plain caller cd && git commit" "{}" "cd $C && git commit -m w5"
t "praxis-master cd && git commit" "{'agent_type':'praxis-master'}" "cd $C && git commit -m w5"
t "subagent caller (agent_id)" "{'agent_type':'praxis-worker','agent_id':'a123'}" 'git commit -m "w5"'
t "praxis-master, payload cwd elsewhere" "{'agent_type':'praxis-master','cwd':'/tmp'}" 'git commit -m "w5"'
t "non-commit command" "{}" 'git status'
t "praxis-master --amend" "{'agent_type':'praxis-master'}" 'git commit --amend -m w5'
}
suite
row MH "praxis-master on main with an untracked file in the hooks dir"
touch $C/.beads/hooks/post-commit; t "praxis-master, dirty hooks dir" "{'agent_type':'praxis-master'}" 'git commit -m "w5"'; rm -f $C/.beads/hooks/post-commit
row MT "legacy token PASS on main (allow path); compare exit/stderr and last-allowed minus ts"
H=$(cd $C && git diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative | shasum -a 256 | awk '{print $1}')
mint() { printf 'tree=%s\n' "$(git -C $C write-tree)" > $C/.claude/state/audit-pass-$H; grep -q "$H PASS" $C/AUDIT_LOG.md || echo "$H PASS w5-test" >> $C/AUDIT_LOG.md; }
payload $C "{}" 'git commit -m "w5"' > $W/pmt.json
mint; ( cd $C && env -u GIT_INDEX_FILE CLAUDE_PROJECT_DIR=$C bash $GATE < $W/pmt.json ) 2>$W/pmt.new; a=$?; grep -v '^ts=' $C/.claude/state/last-allowed > $W/la.new; ls $C/.claude/state/
mint; ( cd $C && env -u GIT_INDEX_FILE CLAUDE_PROJECT_DIR=$C bash $GATEH < $W/pmt.json ) 2>$W/pmt.old; b=$?; grep -v '^ts=' $C/.claude/state/last-allowed > $W/la.old
echo "new exit=$a HEAD-gate exit=$b"; cmp $W/pmt.new $W/pmt.old && echo "stderr IDENTICAL ($(wc -c < $W/pmt.new) bytes)"; cmp $W/la.new $W/la.old && echo "last-allowed (minus ts) IDENTICAL"; cat $W/la.new
git -C $C add -A .claude/state 2>/dev/null; git -C $C reset -q AUDIT_LOG.md 2>/dev/null; git -C $C checkout -q AUDIT_LOG.md

for B in detached feature-x 'parked/Praxis_build-X' 'parked/Praxis_build-w5a/sub' 'parked/praxis_build-w5a' 'Parked/Praxis_build-w5a'; do
  if [ $B = detached ]; then git -C $C switch -q --detach main; else git -C $C switch -q -c "$B" main; fi
  echo; echo "########## non-parked HEAD: $B ($(git -C $C symbolic-ref -q HEAD || echo detached))"
  i=100; suite 2>&1 | grep -E '^(=====|new exit|IDENTICAL|DIFFERENT)'
  git -C $C switch -q main
done

################################ OUTPUT r06.out ################################
remotes after remove: []
HEAD=refs/heads/main

=================== ROW M1: plain caller, clean form ===================
payload cmd: 'git commit -m "w5"' extra: {}
new exit=2  HEAD-gate exit=2
new stderr:
Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
IDENTICAL (exit + stderr bytes)

=================== ROW M2: praxis-master, clean form ===================
payload cmd: 'git commit -m "w5"' extra: {'agent_type': 'praxis-master'}
new exit=2  HEAD-gate exit=2
new stderr:
Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
IDENTICAL (exit + stderr bytes)

=================== ROW M3: plain caller, temp-index form ===================
payload cmd: 'GIT_INDEX_FILE=/tmp/c2trip-w5/m.tidx git commit -m w5' extra: {}
new exit=2  HEAD-gate exit=2
new stderr:
Commit denied: no audit PASS token for this exact staged diff under index '/private/tmp/c2trip-w5/m.tidx' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
IDENTICAL (exit + stderr bytes)

=================== ROW M4: praxis-master, temp-index form ===================
payload cmd: 'GIT_INDEX_FILE=/tmp/c2trip-w5/m.tidx git commit -m w5' extra: {'agent_type': 'praxis-master'}
new exit=2  HEAD-gate exit=2
new stderr:
Commit denied: no audit PASS token for this exact staged diff under index '/private/tmp/c2trip-w5/m.tidx' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
IDENTICAL (exit + stderr bytes)

=================== ROW M5: form violation -am ===================
payload cmd: 'git commit -am "w5"' extra: {'agent_type': 'praxis-master'}
new exit=2  HEAD-gate exit=2
new stderr:
Commit denied: a '-a'-style short flag sweeps unstaged working-tree changes into the commit
Commit exactly the staged diff with a plain `git commit -m "..."` — no -a/--all/--include/--amend, no pathspec after ' -- ', and run it as the sole command in its own Bash call.
IDENTICAL (exit + stderr bytes)

=================== ROW M6: praxis-master pathspec without -- ===================
payload cmd: 'git commit -m w5 README.w5' extra: {'agent_type': 'praxis-master'}
new exit=2  HEAD-gate exit=2
new stderr:
Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=<absolute path>) as the whole Bash command — arguments are not -m <message> pairs (odd count 3). No pathspec, no other flags, no cd/&&/;, no git -C, no $(...)/backticks; outside quotes only [A-Za-z0-9 ._/+=,:@%-] (no $ * ? [ ] { } ~ # ^, no invisible or non-ASCII characters). Token NOT consumed; re-issue the clean form.
IDENTICAL (exit + stderr bytes)

=================== ROW M7: plain caller cd && git commit ===================
payload cmd: 'cd /tmp/c2trip-w5/m && git commit -m w5' extra: {}
new exit=2  HEAD-gate exit=2
new stderr:
Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
IDENTICAL (exit + stderr bytes)

=================== ROW M8: praxis-master cd && git commit ===================
payload cmd: 'cd /tmp/c2trip-w5/m && git commit -m w5' extra: {'agent_type': 'praxis-master'}
new exit=2  HEAD-gate exit=2
new stderr:
Commit denied: the stack master commits with exactly `git commit -m "<message>"` (optionally repeated -m pairs, optionally prefixed by GIT_INDEX_FILE=<absolute path>) as the whole Bash command — the command is not [GIT_INDEX_FILE=<abs path> ]git commit ... as the whole command (no cd/&&/;/git -C/other prefix). No pathspec, no other flags, no cd/&&/;, no git -C, no $(...)/backticks; outside quotes only [A-Za-z0-9 ._/+=,:@%-] (no $ * ? [ ] { } ~ # ^, no invisible or non-ASCII characters). Token NOT consumed; re-issue the clean form.
IDENTICAL (exit + stderr bytes)

=================== ROW M9: subagent caller (agent_id) ===================
payload cmd: 'git commit -m "w5"' extra: {'agent_type': 'praxis-worker', 'agent_id': 'a123'}
new exit=2  HEAD-gate exit=2
new stderr:
Commit denied: no audit PASS token for this exact staged diff under index 'REAL' (the staged set may have changed since mint). Stack master (main-thread praxis-master): dispatch praxis-auditor; its PASS (COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) mints the token. Any other caller: dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself.
IDENTICAL (exit + stderr bytes)

=================== ROW M10: praxis-master, payload cwd elsewhere ===================
payload cmd: 'git commit -m "w5"' extra: {'agent_type': 'praxis-master'}
new exit=2  HEAD-gate exit=2
new stderr:
Commit denied: the stack master must commit from the repo root — payload cwd '/tmp' (resolved '/private/tmp') is not the project root '/private/tmp/c2trip-w5/m'. The gate checks the root's index; a commit from another directory or worktree would record a different one. Run `cd "/tmp/c2trip-w5/m"` in its own Bash call, then re-issue the commit. Token NOT consumed.
IDENTICAL (exit + stderr bytes)

=================== ROW M11: non-commit command ===================
payload cmd: 'git status' extra: {}
new exit=0  HEAD-gate exit=0
new stderr:
IDENTICAL (exit + stderr bytes)

=================== ROW M12: praxis-master --amend ===================
payload cmd: 'git commit --amend -m w5' extra: {'agent_type': 'praxis-master'}
new exit=2  HEAD-gate exit=2
new stderr:
Commit denied: --all/--include/--amend changes the committed set out from under the audit
Commit exactly the staged diff with a plain `git commit -m "..."` — no -a/--all/--include/--amend, no pathspec after ' -- ', and run it as the sole command in its own Bash call.
IDENTICAL (exit + stderr bytes)

=================== ROW MH: praxis-master on main with an untracked file in the hooks dir ===================

=================== ROW M13: praxis-master, dirty hooks dir ===================
payload cmd: 'git commit -m "w5"' extra: {'agent_type': 'praxis-master'}
new exit=2  HEAD-gate exit=2
new stderr:
Commit denied: git hooks dir '/private/tmp/c2trip-w5/m/.beads/hooks' — it is inside the repo and differs from HEAD (git status: ?? .beads/hooks/post-commit). A git hook runs inside the commit after this gate has allowed it, so the stack master commits only while the effective hooks dir (core.hooksPath, else .git/hooks) matches HEAD. Revert or remove the hook change in its own Bash call, then re-issue the commit. Token NOT consumed.
IDENTICAL (exit + stderr bytes)

=================== ROW MT: legacy token PASS on main (allow path); compare exit/stderr and last-allowed minus ts ===================
last-allowed
orchestrator-active
new exit=0 HEAD-gate exit=0
stderr IDENTICAL (       0 bytes)
last-allowed (minus ts) IDENTICAL
tree=d894baa0aff08cbc085f09808cb788e9f1ea191f
index=REAL
hash=5c5d67c3a55562bbdb663cac36b297ac67041cdff03caf5e82ce9b314424294a
head_before=02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
cmd_sha256=527e54e5c69dbcd7bd21d202ce554c7b860f8a12122fcd2df6d7794d925d47d2

########## non-parked HEAD: detached (detached)
=================== ROW M101: plain caller, clean form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M102: praxis-master, clean form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M103: plain caller, temp-index form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M104: praxis-master, temp-index form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M105: form violation -am ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M106: praxis-master pathspec without -- ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M107: plain caller cd && git commit ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M108: praxis-master cd && git commit ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M109: subagent caller (agent_id) ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M110: praxis-master, payload cwd elsewhere ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M111: non-commit command ===================
new exit=0  HEAD-gate exit=0
IDENTICAL (exit + stderr bytes)
=================== ROW M112: praxis-master --amend ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)

########## non-parked HEAD: feature-x (refs/heads/feature-x)
=================== ROW M101: plain caller, clean form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M102: praxis-master, clean form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M103: plain caller, temp-index form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M104: praxis-master, temp-index form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M105: form violation -am ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M106: praxis-master pathspec without -- ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M107: plain caller cd && git commit ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M108: praxis-master cd && git commit ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M109: subagent caller (agent_id) ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M110: praxis-master, payload cwd elsewhere ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M111: non-commit command ===================
new exit=0  HEAD-gate exit=0
IDENTICAL (exit + stderr bytes)
=================== ROW M112: praxis-master --amend ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)

########## non-parked HEAD: parked/Praxis_build-X (refs/heads/parked/Praxis_build-X)
=================== ROW M101: plain caller, clean form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M102: praxis-master, clean form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M103: plain caller, temp-index form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M104: praxis-master, temp-index form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M105: form violation -am ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M106: praxis-master pathspec without -- ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M107: plain caller cd && git commit ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M108: praxis-master cd && git commit ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M109: subagent caller (agent_id) ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M110: praxis-master, payload cwd elsewhere ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M111: non-commit command ===================
new exit=0  HEAD-gate exit=0
IDENTICAL (exit + stderr bytes)
=================== ROW M112: praxis-master --amend ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)

########## non-parked HEAD: parked/Praxis_build-w5a/sub (refs/heads/parked/Praxis_build-w5a/sub)
=================== ROW M101: plain caller, clean form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M102: praxis-master, clean form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M103: plain caller, temp-index form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M104: praxis-master, temp-index form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M105: form violation -am ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M106: praxis-master pathspec without -- ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M107: plain caller cd && git commit ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M108: praxis-master cd && git commit ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M109: subagent caller (agent_id) ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M110: praxis-master, payload cwd elsewhere ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M111: non-commit command ===================
new exit=0  HEAD-gate exit=0
IDENTICAL (exit + stderr bytes)
=================== ROW M112: praxis-master --amend ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
fatal: cannot lock ref 'refs/heads/parked/praxis_build-w5a': there is a non-empty directory '.git/refs/heads/parked/praxis_build-w5a' blocking reference 'refs/heads/parked/praxis_build-w5a'

########## non-parked HEAD: parked/praxis_build-w5a (refs/heads/main)
=================== ROW M101: plain caller, clean form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M102: praxis-master, clean form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M103: plain caller, temp-index form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M104: praxis-master, temp-index form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M105: form violation -am ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M106: praxis-master pathspec without -- ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M107: plain caller cd && git commit ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M108: praxis-master cd && git commit ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M109: subagent caller (agent_id) ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M110: praxis-master, payload cwd elsewhere ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M111: non-commit command ===================
new exit=0  HEAD-gate exit=0
IDENTICAL (exit + stderr bytes)
=================== ROW M112: praxis-master --amend ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
fatal: cannot lock ref 'refs/heads/Parked/Praxis_build-w5a': there is a non-empty directory '.git/refs/heads/Parked/Praxis_build-w5a' blocking reference 'refs/heads/Parked/Praxis_build-w5a'

########## non-parked HEAD: Parked/Praxis_build-w5a (refs/heads/main)
=================== ROW M101: plain caller, clean form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M102: praxis-master, clean form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M103: plain caller, temp-index form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M104: praxis-master, temp-index form ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M105: form violation -am ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M106: praxis-master pathspec without -- ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M107: plain caller cd && git commit ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M108: praxis-master cd && git commit ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M109: subagent caller (agent_id) ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M110: praxis-master, payload cwd elsewhere ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)
=================== ROW M111: non-commit command ===================
new exit=0  HEAD-gate exit=0
IDENTICAL (exit + stderr bytes)
=================== ROW M112: praxis-master --amend ===================
new exit=2  HEAD-gate exit=2
IDENTICAL (exit + stderr bytes)

artifact sha256 at end: 8471206f084b87e2fabae2d7375896d59bc273f6f97c33a89fc7865f7466c19f  /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
```

## Adversarial findings

All rows come from W2b (draft bytes) and W5 (final bytes). Each row cites the evidence block where its output is pasted.

| id | finding | introduced by C2 code? | disposition |
|---|---|---|---|
| X3 (W2b) | The hooks-dir check anchors on HEAD, and a parked HEAD is unaudited. A first exempt commit records an evil hook on the parked branch; the second exempt commit runs it | YES | FIXED. A park commit with an in-repo hooks dir now needs HEAD's hooks dir == `refs/heads/main`'s, and no main = deny. T11-x3 deny; T11-x3-PREEDIT and T11-noexempt-toggle allow (S9); T11-ctl allow; T11-main token route unchanged (E1d) |
| re-read (W1) | The final re-read repeated only the followed read | YES | FIXED. Both reads are re-applied. T12-chain deny vs T12-chain-PREEDIT allow (E1d) |
| X1/X2 (W2b) | `core.fsmonitor` / `gpg.program` config runs a program during the gate's own git calls or inside the commit | root cause PRE-EXISTING (no route inspects program-running config); new only in that no token is needed | NOT FIXED, open item 2 |
| T1 (W2b) / R14 (W5) | HEAD flipped to main by the session's own background job after the gate's final read. The commit lands on main and commit-tree-verify stays silent (no last-allowed record) | the race window is new for park commits; the class (allow-then-run) already exists on the token route (A1/A3, detection only) | NOT FIXED, open item 1 |
| R01/R01b (W5) | `refs/heads/main` made a symref to, or moved onto, the evil parked tip before the park commit. The X3 anchor then agrees with HEAD | anchor weakness of the X3 fix; needs an ungated ref write first, which by itself already moves main (E3 route 6) | NOT FIXED, open item 1 |
| R02/R02c (W5) | `git replace` makes main's commit or tree look like the evil parked one to the X3 diff | same as R01; W5 notes it may also affect the HEAD-anchored check on main (UNVERIFIED) | NOT FIXED, open item 1 |
| R17b (W5) | `.git/refs/heads/parked` as a directory symlink to `../tags`, so a park commit moves a tag | YES (minor) | NOT FIXED. It cannot reach main (name pattern); open item 1 |
| M rows (W5) | main, detached, feature-x, look-alike parked names: exit code and stderr byte-identical to the gate at git HEAD | — | HELD. Also my E1d regression: 66 files identical |
| W5 note | a non-master token holder on a parked HEAD now also gets the stricter stack-master form check | YES | accepted. This fails closed, and it happens only on parked HEADs |

Decided by manager under D-2026-11-08-D D1 (open items 1 and 2): these are reported, not built. Closing them means gating ref-writing git commands or inspecting git config on every route, and that is wider than C2's words. E3 shows that without the exemption the same session can already move `main` by `git update-ref`, `git branch -f` or `git merge`, and no hook stops it.

## S6 cross-block check

These are the other blocks the exemption touches. All results are pasted in E3/E4 and come from the manager's own re-run.
- Other PreToolUse Bash hooks (`scripts/no-commit-guard.sh`, `scripts/master-bash-guard.sh`, `scripts/mint-guard.sh`) on the clean park payload: master and plain session pass every hook (gate prints the exemption line); the subagent caller is denied by no-commit-guard and by the gate (E4 Q2(i)). No conflict.
- PostToolUse `scripts/commit-tree-verify.sh` after a real park commit: case A (no last-allowed) and B1 (stale record, different command text) give exit 0 and stay silent. Case B2 is a stale record from an earlier token allow that never ran, with IDENTICAL command text. It gives exit 2, "COMMIT TREE MISMATCH", and tells the model to revert. That is a false alarm on a legitimate park commit (E4). CONFLICT, NOT FIXED (open item 3). It fails loud, not open.
- Stop/SessionStart/PreCompact hooks and `scripts/dispatch-log-writeahead.sh`: no reference to last-allowed/audit-pass/AUDIT_LOG/mint-log (E4 Q2(iii) grep). No conflict.
- Park rule (rubric :246-260) and A11: the rubric edit is the uncommitted filer's paragraph only, and it cites C2 (block F diff is additions only).
- Settings: `.claude/settings.json` was not touched. The hook inventory in E3 reads its working-tree copy.

## Open items (for the master; I file nothing and close nothing)

1. Ungated ref writes defeat the exemption's conditions and also move main directly: R14 race, R01/R01b, R02/R02c, R17b. E3 shows `git update-ref`, `git branch -f`, `git merge`, `git cherry-pick` and `git push <remote> parked/x:main` move main for a master or plain session, with no hook denying. Branch protection on GitHub `main` is off, and there are no rulesets. Recommended bead: decide whether ref-writing git commands and pushes to main get gated, and whether a park allow writes a record for the PostToolUse check. Needs Amear only if it widens C2.
2. X1/X2: program-running git config (`core.fsmonitor`, `gpg.program`/`commit.gpgSign`) is not inspected on any route. PRE-EXISTING. Recommended bead.
3. commit-tree-verify.sh B2 false alarm after a park commit when a stale same-command last-allowed exists. Recommended fix: the exemption removes a stale last-allowed, or the checker compares `head_before` with the landed HEAD's parent. That is a cross-block change, not built.
4. Worker brief breach: `.claude/agent-memory/praxis-worker/project_gate-harness-fake-process.md`, born 2026-11-10T00:29:22-0500 during this unit, plus an index line 10 in that dir's MEMORY.md. W1 and W3 each claimed to have reverted. Both are still present (block F). The directory is gitignored. I left it untouched because the brief forbids writes there; the master decides whether to delete it.
5. Live trip by the master pending (19:22Z item (3)). Real-repo note: the real repo uses an absolute `core.hooksPath` = `/Volumes/Sensidine/Praxis.build/.beads/hooks` (observed this unit). A live park commit therefore also needs `.beads/hooks` on the throwaway parked branch to equal main's.
6. W2 (adversarial) returned nothing (classifier stop). W2b replaced it.

## Files staged

Nothing staged (the brief forbids `git add`; the real index fingerprint is unchanged, block F). Working-tree changes from this unit:
- `.claude/hooks/gate-commit.sh`: the draft plus fixes X3 and re-read; final sha256 8471206f084b87e2fabae2d7375896d59bc273f6f97c33a89fc7865f7466c19f. The bytes I trip-tested (E1) equal the final bytes (block F).
- `specs/SPEC_RUBRIC.md`: only the uncommitted filer's note paragraph was rewritten (now :302-332). Nothing at or above :301 changed.
- `MANIFEST.md`: rows :325-327 corrected in place; row :328 appended for this report.
- `docs/reports/2026-11-10-c2-park-gate-resume-manager.md`: this report (new).
Not touched: `docs/reports/2026-11-09-c2-park-gate-manager.md`, `.claude/settings.json`, the walk-forward spec/values files, U7/diq files.

Level reached: TESTED (synthetic). Live trip by the master pending.

Result: PASS

## Final evidence block F (pasted last, after every edit)

```text
$ date -u
Tue Nov 10 06:02:27 UTC 2026
[exit=0]
$ openssl dgst -sha256 .claude/hooks/gate-commit.sh
SHA2-256(.claude/hooks/gate-commit.sh)= 8471206f084b87e2fabae2d7375896d59bc273f6f97c33a89fc7865f7466c19f
[exit=0]
(tested bytes, E1 harness header and wrapper: 8471206f084b87e2fabae2d7375896d59bc273f6f97c33a89fc7865f7466c19f)
$ git rev-parse HEAD origin/main
02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
02d53c66ccfa3105f8c8bba812678e9e77d1cbe5
[exit=0]
$ git diff HEAD --stat
 .claude/hooks/gate-commit.sh                       |   67 +-
 .claude/settings.json                              |   10 +
 AUDIT_LOG.md                                       |   24 +
 DECISION_LOG.md                                    |    4 +
 DISPATCH_LOG.md                                    |  294 +++
 HANDOFF.md                                         |  191 ++
 ISSUE_REGISTER.md                                  |   41 +
 MANIFEST.md                                        |   12 +
 STATUS.md                                          |   26 +
 .../2026-08-06-session42-r8j-phase3-import.md      | 1882 ++++++++++++++++++++
 .../2026-08-07-f4-mffu-compliance-evidence.md      |  776 ++++++++
 ...-session44-r8j-offset-correction-adversarial.md |  546 ++++++
 ...8-07-session44-r8j-offset-correction-worker1.md |  195 ++
 .../2026-08-07-session44-r8j-offset-correction.md  |  301 ++++
 docs/reports/2026-10-28-f4-davi-reply-filing.md    |  465 +++++
 .../2026-10-28-nightly-checks-plan-review-note.md  |  184 ++
 ...026-10-28-nightly-checks-plan-review-rebuild.md | 1400 +++++++++++++++
 .../2026-10-28-mffu-davi-reply-transcript.md       |   71 +
 .../evidence/2026-10-28-mffu-davi-reply.png        |  Bin 0 -> 254350 bytes
 docs/specs/2026-08-08-ledger-compaction-spec.md    |   14 +-
 docs/specs/2026-11-05-walk-forward-spec.md         |   10 +-
 docs/specs/2026-11-06-walk-forward-values.md       |   42 +-
 scripts/dispatch-log-writeahead.sh                 |  104 +-
 specs/SPEC_RUBRIC.md                               |   31 +
 24 files changed, 6659 insertions(+), 31 deletions(-)
[exit=0]
$ git diff HEAD -- .claude/hooks/gate-commit.sh specs/SPEC_RUBRIC.md
diff --git a/.claude/hooks/gate-commit.sh b/.claude/hooks/gate-commit.sh
index 9ea7308..23a1292 100755
--- a/.claude/hooks/gate-commit.sh
+++ b/.claude/hooks/gate-commit.sh
@@ -75,6 +75,24 @@
 #      head_before, ts, cmd_sha256); scripts/commit-tree-verify.sh (PostToolUse)
 #      compares the landed HEAD^{tree} with it. Detection only (A1/A3: a git
 #      pre-commit hook or background job can still change the index after allow).
+#
+# D-2026-11-08-C C2 (2026-11-09, unit 2026-11-09-c2-park-gate): park-commit
+#   exemption. The audit-token requirement is skipped ONLY when HEAD of ROOT is
+#   exactly refs/heads/parked/Praxis_build-<[a-z0-9]+>, named by HEAD directly
+#   (no symref chain; git symbolic-ref -q must equal --no-recurse) (read with git
+#   symbolic-ref -q; detached HEAD or any error = no exemption; no exemption
+#   either when GIT_DIR/GIT_WORK_TREE/GIT_COMMON_DIR is set in the hook's env
+#   or the payload has an agent_id key, or the ref does not exist under that
+#   exact name), AND the command
+#   passes every stack-master check below (whole-command form
+#   [GIT_INDEX_FILE=<abs path> ]git commit -m ..., payload cwd == ROOT, toplevel
+#   == ROOT, hooks dir == HEAD), AND every other check (form, index selection,
+#   single-session) passes, AND HEAD is unchanged when re-read just before the
+#   token lookup. On exemption: one stderr line naming the branch, exit 0, no
+#   token consumed, no last-allowed record, nothing appended to the mint log
+#   (this gate never writes it). Any other branch takes the token route below.
+#   X3 (unit 2026-11-10-c2-park-gate-resume, adversarial finding X3): a parked HEAD is unaudited, so for an
+#   in-repo hooks dir a park commit also needs `git diff --quiet refs/heads/main HEAD -- <dir>` to pass (no main = deny).
 set -uo pipefail
 INPUT=$(cat)
 CMD=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null || true)
@@ -144,6 +162,31 @@ CALLER_TYPE=$(pj agent_type)
 CALLER_ID=$(pj agent_id)
 STACK_MASTER=0
 [ "$CALLER_TYPE" = "praxis-master" ] && [ -z "$CALLER_ID" ] && STACK_MASTER=1
+# --- C2 park-commit candidate (D-2026-11-08-C C2). HEAD of ROOT must be EXACTLY
+# refs/heads/parked/Praxis_build-[a-z0-9]+ (explicit class, no locale ranges).
+# symbolic-ref failure (detached HEAD, error) leaves PARK=0 = no exemption.
+# No exemption either when GIT_DIR / GIT_WORK_TREE / GIT_COMMON_DIR is set in
+# this hook's own environment (the HEAD read would not be ROOT's; adversarial
+# case G1, 2026-11-09), or for a subagent caller (agent_id KEY present in the
+# payload, any value of any type incl. null, or a payload parse error; subagents
+# never commit — scripts/no-commit-guard.sh). Those cases take the token route.
+# The ref must also exist under exactly that name (for-each-ref): no unborn HEAD, no case-folded alias.
+PARK=0
+_pk_ref=$(cd "$ROOT" 2>/dev/null && env -u GIT_INDEX_FILE git symbolic-ref -q HEAD 2>/dev/null) || _pk_ref=""
+# HEAD must name the parked ref DIRECTLY: the unfollowed read must equal the
+# followed one (a symref chain HEAD -> WIP|main -> parked/... gets no exemption).
+_pk_nr=$(cd "$ROOT" 2>/dev/null && env -u GIT_INDEX_FILE git symbolic-ref -q --no-recurse HEAD 2>/dev/null) || _pk_nr=""
+[ -n "$_pk_nr" ] && [ "$_pk_nr" = "$_pk_ref" ] || _pk_ref=""
+_pk_noid=$(printf '%s' "$INPUT" | python3 -c 'import json,sys
+d=json.load(sys.stdin)
+print("yes" if isinstance(d, dict) and "agent_id" not in d else "no")' 2>/dev/null) || _pk_noid=""
+if [[ "$_pk_ref" =~ ^refs/heads/parked/Praxis_build-[abcdefghijklmnopqrstuvwxyz0123456789]+$ ]] \
+   && [ -z "${GIT_DIR+x}" ] && [ -z "${GIT_WORK_TREE+x}" ] && [ -z "${GIT_COMMON_DIR+x}" ] \
+   && [ -z "$CALLER_ID" ] && [ "$_pk_noid" = "yes" ]; then
+  # the branch must exist under EXACTLY this name (no unborn HEAD, no case-folded alias)
+  _pk_have=$(cd "$ROOT" 2>/dev/null && env -u GIT_INDEX_FILE git for-each-ref --format='%(refname)' "$_pk_ref" 2>/dev/null) || _pk_have=""
+  [ "$_pk_have" = "$_pk_ref" ] && PARK=1
+fi
 
 # --- Stack-master exact form (W4 fix, 2026-11-04). `git commit -m x somefile`
 # (a pathspec WITHOUT ' -- ') commits somefile's WORKING-TREE content, not the
@@ -159,7 +202,7 @@ STACK_MASTER=0
 # quotes too ("$@" / "${a[@]}" expand to several words) — put a literal $ in
 # single quotes. Runs BEFORE token lookup so a form denial never consumes the
 # token. Non-stack callers are NOT narrowed by this block.
-if [ "$STACK_MASTER" = 1 ]; then
+if [ "$STACK_MASTER" = 1 ] || [ "$PARK" = 1 ]; then   # C2: a park candidate gets every stack-master check
   _sm=$(printf '%s' "$CMD" | python3 -c '
 import re, shlex, sys
 # Fix B: strip ONLY ASCII space/tab (str.strip() also drops VT/FF/NBSP/...,
@@ -282,6 +325,14 @@ print("OK")
         [ "$_hnow" = "$_hsha" ] || deny_hooks "entry '${_hf##*/}' content differs from HEAD"
         if [ -x "$_hf" ] && [ "$_hmode" != 100755 ]; then deny_hooks "entry '${_hf##*/}' is executable but HEAD mode is $_hmode"; fi
       done
+      # C2 X3: a parked HEAD is itself unaudited (park commits skip the token),
+      # so "matches HEAD" is no anchor there; also require HEAD == main for the dir.
+      if [ "$PARK" = 1 ]; then
+        _pk_main=$(env -u GIT_INDEX_FILE git -C "$_root_rp" rev-parse -q --verify 'refs/heads/main^{commit}' 2>/dev/null) || _pk_main=""
+        [ -n "$_pk_main" ] || deny_hooks "park commit: refs/heads/main does not resolve to a commit, so the hooks dir in the (unaudited) parked HEAD cannot be checked against it"
+        env -u GIT_INDEX_FILE git --literal-pathspecs -C "$_root_rp" diff --quiet --no-ext-diff --no-textconv "$_pk_main" HEAD -- "$_hrel" >/dev/null 2>&1 \
+          || deny_hooks "park commit: the hooks dir in HEAD differs from refs/heads/main, or the comparison failed (a parked HEAD is unaudited)"
+      fi
     else
       for _hf in "$_hd_rp"/* "$_hd_rp"/.[!.]* "$_hd_rp"/..?*; do
         [ -e "$_hf" ] || [ -L "$_hf" ] || continue
@@ -600,6 +651,20 @@ if [ -n "$FOREIGN" ]; then
   deny_session "another live claude session (pid$FOREIGN) has its cwd inside this repo — it can pollute the shared .git/index between audit and commit (2026-07-10 incident)"
 fi
 
+# --- C2 park-commit exemption (D-2026-11-08-C C2). Reached only after every
+# check above passed for a PARK candidate. HEAD is re-read and must be the same
+# parked ref; any change or error denies (fail closed).
+if [ "$PARK" = 1 ]; then
+  _pk_ref2=$(cd "$ROOT" 2>/dev/null && env -u GIT_INDEX_FILE git symbolic-ref -q HEAD 2>/dev/null) || _pk_ref2=""
+  _pk_nr2=$(cd "$ROOT" 2>/dev/null && env -u GIT_INDEX_FILE git symbolic-ref -q --no-recurse HEAD 2>/dev/null) || _pk_nr2=""
+  if [ -n "$_pk_ref2" ] && [ -n "$_pk_nr2" ] && [ "$_pk_ref2" = "$_pk_ref" ] && [ "$_pk_nr2" = "$_pk_ref" ]; then
+    echo "Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch '${_pk_ref#refs/heads/}'. No token consumed." >&2
+    exit 0
+  fi
+  echo "Commit denied: HEAD moved during the park-commit check (was '${_pk_ref}', now '${_pk_ref2:-unresolvable}', named directly '${_pk_nr2:-unresolvable}'). Re-issue the commit." >&2
+  exit 2
+fi
+
 # --- Token + AUDIT_LOG checks: only a fresh token whose hash also appears as a
 # PASS row in AUDIT_LOG.md is honored (a bare `touch`ed token is forgery). ---
 # Sweep orphaned tokens first: a token whose staged diff drifted (re-audit minted
diff --git a/specs/SPEC_RUBRIC.md b/specs/SPEC_RUBRIC.md
index 3f3510a..290102b 100644
--- a/specs/SPEC_RUBRIC.md
+++ b/specs/SPEC_RUBRIC.md
@@ -299,6 +299,37 @@ absolute park rule has no sanctioned commit path". The gate change is the later,
 trip-tested unit (D-2026-11-08-D D12: "park-commit gate exemption (C2,
 trip-tested)"). So the exemption is RULED and NOT YET BUILT.
 
+Filer's note, not a ruling (2026-11-09, corrected 2026-11-10, under C2 and
+A11): the exemption is written in `.claude/hooks/gate-commit.sh`: the
+audit-token requirement is skipped only when HEAD of the project root is
+exactly `refs/heads/parked/Praxis_build-<[a-z0-9]+>`, named by HEAD directly
+(no symref chain), and that ref exists under exactly that name, no GIT_DIR,
+GIT_WORK_TREE or GIT_COMMON_DIR is set in the hook's environment, the payload
+has no agent_id key, the command passes every stack-master check (the whole
+command is `[GIT_INDEX_FILE=<abs path> ]git commit -m ...`, payload cwd and git
+toplevel equal the root, the git hooks dir matches HEAD and, for a park commit
+with an in-repo hooks dir, also matches `refs/heads/main`, because a parked
+HEAD is unaudited) and every other existing check (form, temp-index,
+single-session), and HEAD is unchanged on both reads when re-read before the
+token lookup. Level: TESTED (synthetic): PreToolUse payloads piped to the hook
+in a throwaway clone, unit `2026-11-10-c2-park-gate-resume`, report
+`docs/reports/2026-11-10-c2-park-gate-resume-manager.md` (the 2026-11-09 unit
+`2026-11-09-c2-park-gate` did not finish and its report shows no trip test).
+Live trip by the master pending. Known gaps, observed in that report and not
+closed: a session that moves HEAD to `main` after the hook allows, or that
+rewrites `refs/heads/main` or adds `refs/replace/` refs before a park commit,
+defeats the exemption's conditions, and git config that runs programs
+(`core.fsmonitor`, `gpg.program`) is not inspected on any route. On "because
+it never touches main": in a scratch clone a commit on a `parked/` branch
+reached `main` by `git merge --ff-only`, `git merge`, `git cherry-pick`,
+`git branch -f`, `git update-ref` and `git push <remote> parked/<x>:main`; no
+hook registered in `.claude/settings.json` denied any of these command texts
+for a plain session or a main-thread praxis-master (only
+`scripts/no-commit-guard.sh` denies the merge and push forms, and only for
+subagent callers); and GitHub reports the remote's `main` branch as not
+protected, with no rulesets. So "never touches main" is held by the park
+procedure, not by any enforced mechanism (observed in that report).
+
 Filer's note, not a ruling: this ruling lands under Amear's C8, "The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written." (D-2026-11-08-C; DECISION_LOG 2026-11-08T19:12:30Z, WHO: amear; docs/reports/2026-11-08-amear-answers-park-card.md :38).
 
 **No-verdict returns — R-A / R-B / R-C, ruled 2026-07-27. Source: DECISION_LOG
[exit=0]
$ sed -n '325,330p' MANIFEST.md
| /.claude/hooks/gate-commit.sh | Config | 2 | 2026-11-10 | UPDATE ROW 2026-11-09, corrected 2026-11-10 (append-only registry; adds to the earlier rows for this path). C2 park-commit exemption (Amear D-2026-11-08-C C2, bead Praxis_build-8sw; draft from unit 2026-11-09-c2-park-gate, verified and corrected in unit 2026-11-10-c2-park-gate-resume): the audit token is skipped only when ROOT's HEAD names refs/heads/parked/Praxis_build-[a-z0-9]+ directly (no symref chain) and that ref exists under exactly that name, no GIT_DIR/GIT_WORK_TREE/GIT_COMMON_DIR is set in the hook env, the payload has no agent_id key, every stack-master and other existing check passes, an in-repo hooks dir in HEAD equals refs/heads/main's (fix X3, 2026-11-10), and both HEAD reads are unchanged on re-read; TESTED (synthetic payloads in a throwaway clone, final bytes sha256 8471206f...c19f); live trip by the master pending; ungraded at time of row |
| /specs/SPEC_RUBRIC.md | Spec | 2 | 2026-11-10 | UPDATE ROW 2026-11-09, corrected 2026-11-10 (append-only registry; adds to the earlier rows for this path). Units 2026-11-09-c2-park-gate and 2026-11-10-c2-park-gate-resume (C2, A11): one filer's note paragraph appended after the paragraph ending "So the exemption is RULED and NOT YET BUILT." - exemption written in .claude/hooks/gate-commit.sh with its conditions, TESTED (synthetic) per docs/reports/2026-11-10-c2-park-gate-resume-manager.md, live trip pending, known gaps, and the never-touches-main finding; no existing line changed |
| /docs/reports/2026-11-09-c2-park-gate-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-c2-park-gate (Amear D-2026-11-08-C C2, bead Praxis_build-8sw); corrected 2026-11-10: the unit died at the weekly usage limit, the report is 21 lines marked "(in progress)" with no Result line and no trip table; the work is verified in docs/reports/2026-11-10-c2-park-gate-resume-manager.md; left as written (append-only) |
| /docs/reports/2026-11-10-c2-park-gate-resume-manager.md | Report | 2 | 2026-11-10 | Manager report for unit 2026-11-10-c2-park-gate-resume (Amear D-2026-11-08-C C2, bead Praxis_build-8sw): verification of the on-disk C2 draft, trip table T1-T12 with S9 toggles on the final gate bytes, five adversarial passes, fixes X3 and re-read symmetry, never-touches-main observations (no hook or branch protection stops a parked commit reaching main), S6 cross-block check; ungraded at time of row |
[exit=0]
$ wc -l MANIFEST.md
     328 MANIFEST.md
[exit=0]
$ git diff --cached --name-only | openssl dgst -sha256
SHA2-256(stdin)= 5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95
[exit=0]
$ git status --short -- docs/reports/2026-11-09-c2-park-gate-manager.md .claude/settings.json docs/specs/2026-11-05-walk-forward-spec.md docs/specs/2026-11-06-walk-forward-values.md
 M .claude/settings.json
 M docs/specs/2026-11-05-walk-forward-spec.md
 M docs/specs/2026-11-06-walk-forward-values.md
?? docs/reports/2026-11-09-c2-park-gate-manager.md
[exit=0]
$ git diff HEAD --stat -- docs/reports/2026-11-09-c2-park-gate-manager.md
[exit=0]
$ wc -l docs/reports/2026-11-09-c2-park-gate-manager.md
      21 docs/reports/2026-11-09-c2-park-gate-manager.md
[exit=0]
$ stat -f '%SB %N' -t '%FT%T%z' .claude/agent-memory/praxis-worker/project_gate-harness-fake-process.md
2026-11-10T00:29:22-0500 .claude/agent-memory/praxis-worker/project_gate-harness-fake-process.md
[exit=0]
$ grep -n 'gate-harness' .claude/agent-memory/praxis-worker/MEMORY.md
10:- [Gate harness fake process](project_gate-harness-fake-process.md) — use exec -a claude-fake /bin/sleep (a copied binary is SIGKILLed); split setup, mint-guard trips on hook paths
[exit=0]
$ git check-ignore -v .claude/agent-memory/praxis-worker/MEMORY.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/MEMORY.md
[exit=0]
$ grep -c 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed[.]' docs/reports/2026-11-10-c2-park-gate-resume-manager.md
1
[exit=0]
$ grep -n '^Result: ' docs/reports/2026-11-10-c2-park-gate-resume-manager.md
2803:Result: PASS
[exit=0]
$ wc -l docs/reports/2026-11-10-c2-park-gate-resume-manager.md
    3034 docs/reports/2026-11-10-c2-park-gate-resume-manager.md
[exit=0]
(the wc -l above counts the report before its own output line, the [exit] line and the closing fence: +3 lines)
```
