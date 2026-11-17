# Session 36 — MANIFEST rows + stale agent-memory correction

Manager: praxis-manager. Date: 2026-07-26. Baseline HEAD: `c1dec30`.
Append-only. Nothing in this report was committed; the index was never touched.

## Task

Two prerequisites to a commit the master is about to audit.

1. Add one MANIFEST.md row per each of six new session-36 report files, matching
   the existing row format exactly, describing each at the level the evidence
   supports (S2). Three of the six are intermediate working artefacts; one
   (`null-attack`) records the refutation of another (`agent-key-lab`). The master
   is blocked from writing MANIFEST.md (`scripts/master-write-guard.sh:13-16` does
   not list it), which is why this was dispatched.
2. Correct or remove `.claude/agent-memory/praxis-worker/project_agent-type-source.md`,
   which asserted a now-refuted null about what sets `agent_type`, and fix any other
   file in `.claude/agent-memory/` repeating the same claim.

## Rubric criteria addressed

Quoted verbatim from `specs/SPEC_RUBRIC.md`:

- **S1** (line 107): "Every claim in a report has pasted command output, not a description of output."
- **S2** (line 108): "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure."

No criterion was authored by me. The brief cited both; both trace to the rubric file.

## Workers dispatched

| # | id | mode | scope | outcome |
|---|---|---|---|---|
| 1 | a86663fb3c38ff62c | BUILD | draft + write six MANIFEST rows | returned PASS — **overturned**, 8 S2 defects found |
| 2 | a6c127471140a6bcd | BUILD | correct the stale memory | returned PASS — **overturned**, 3 defects (2 HIGH) |
| 3 | a8cfe7b8bece480d9 | ADVERSARIAL | attack the MANIFEST rows | **FAIL** — 10 defects, 3 HIGH |
| 4 | ab14514035d77568e | ADVERSARIAL | attack the memory tree | **FAIL** — 6 defects, 3 HIGH |
| 5 | a5cd2c0468a2f77c1 | BUILD (fix r1) | close MANIFEST defects 1-10 | PASS |
| 6 | abf6fe02c55b56abe | BUILD (fix r1) | close memory defects 1-6 | PASS |
| 7 | aa17f62ed9bc7ef46 | ADVERSARIAL (r2) | recheck both artefacts | **FAIL** — prior defects closed, but **2 HIGH regressions introduced** |
| 8 | adf803d672fe5b25d | BUILD (fix r2) | close the regressions | PASS |
| 9 | a7312849826c9e3d1 | ADVERSARIAL (r3) | full recheck | **no verdict** — exhausted budget mid-run; re-dispatched as 10+11 |
| 10 | a1569df83cc920dd9 | ADVERSARIAL (r3a) | MANIFEST citation/quote audit | **FAIL** — 2 quotation-fidelity defects |
| 11 | a9e28bc5c8ba9b6d0 | ADVERSARIAL (r3b) | memory tree audit | PASS with 3 accuracy nits, 1 MED |
| 12 | a938007698c7412cb | BUILD (fix r3) | close the 6 remaining nits | PASS, reported 1 residual |

Manager direct edit: one line in `project_agent_type_mechanism.md:59-60` (a non-resolving
quotation cut) — single-line doc fix, within the permitted write scope, made rather than
dispatched a thirteenth worker.

## Process log

Round 1 produced two artefacts that both workers self-graded PASS. Both were wrong.
The adversarial pass found 16 defects across them, 6 of them HIGH. The most
consequential class was S2 overclaim: characterising a hedged or unverified source
statement as an observed fact, and misattributing who did what.

Round 2's fix then **over-corrected** — it took a hedge that is true inside one
report's scope (`agent-key-s9-control.md` §9: "Confirmed by reading, **not**
separately trip-tested") and rendered it as a repo-wide universal negative
("never tripped"). That negative is false: two other reports and a sibling memory
in the same directory record live trip tests. Underclaim is an S2 violation exactly
as much as overclaim, and it briefly put two files in one memory directory into
direct contradiction.

Round 3 closed that, and a final pass closed six quotation-fidelity nits. Three
adversarial rounds were needed; the artefact did not converge until round 4.

**Process note for the master:** worker 9 (adversarial r3) terminated after 48 tool
calls and 122k tokens having emitted only "Now the critical line-cite verification."
— no verdict. A silent budget death in an *adversarial* role is a false-PASS hazard:
had I treated a missing verdict as no findings, both remaining defect classes would
have shipped. It was re-dispatched as two narrower checks.

## Verification evidence

All output below is pasted, not described.

Baseline staged index, captured before any dispatch:

```
$ git diff --cached --numstat
1	0	.claude/settings.json
$ git rev-parse --short HEAD
c1dec30
```

Final staged index, after all twelve workers and my own edit:

```
$ git diff --cached --numstat
1	0	.claude/settings.json
```

Unchanged. No `git add`, `commit`, `restore`, `reset`, or any other index or history
operation was run by me or by any worker.

MANIFEST.md is a pure append; no existing row was altered, reordered, or reformatted:

```
$ cmp <(head -117 MANIFEST.md) <(git show HEAD:MANIFEST.md) && echo LINES-1-117-IDENTICAL
LINES-1-117-IDENTICAL
$ git diff --numstat MANIFEST.md
6	0	MANIFEST.md
$ tail -6 MANIFEST.md | awk -F'|' '{print NR": fields="NF}'
1: fields=7
2: fields=7
3: fields=7
4: fields=7
5: fields=7
6: fields=7
```

Every new row's path resolves on disk and appears exactly once:

```
session36-agent-key-audit.md rows=1        EXISTS docs/reports/2026-07-26-session36-agent-key-audit.md
session36-agent-key-s9-control.md rows=1   EXISTS docs/reports/2026-07-26-session36-agent-key-s9-control.md
session36-agent-key-lab.md rows=1          EXISTS docs/reports/2026-07-26-session36-agent-key-lab.md
session36-adversarial-actor-hunt.md rows=1 EXISTS docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
session36-null-attack.md rows=1            EXISTS docs/reports/2026-07-26-session36-null-attack.md
session36-worker-trigger-probe.md rows=1   EXISTS docs/reports/2026-07-26-session36-worker-trigger-probe.md
```

Refuted claim is dead across the whole memory tree:

```
$ grep -rn "asserts the opposite\|re-verified by the master\|never tripped\|no observed block" .claude/agent-memory/
.claude/agent-memory/praxis-worker/feedback_scoped-hedge-vs-universal-negative.md:3:description: Never promote a report-scoped hedge ("not separately trip-tested in THIS control") into a repo-wide universal negative ("never tripped") — underclaim fails rubric S2 exactly as hard as overclaim.
.claude/agent-memory/praxis-worker/feedback_scoped-hedge-vs-universal-negative.md:11:"never tripped" is a new, stronger, and usually false claim.
```

Both remaining hits are inside the new feedback memory, which quotes the phrase as
the anti-pattern to avoid. No file asserts it.

Claims I re-derived myself rather than accepting from a worker report:

```
$ sed -n '107,108p' specs/SPEC_RUBRIC.md
| S1 | Every claim in a report has pasted command output, not a description of output. |
| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |

$ sed -n '142p' docs/reports/2026-07-26-agent-stack-v2-triptests.md
Verdict: **PASS** — `master-write-guard.sh` fires on the `Write` tool with the

$ sed -n '54p' docs/reports/2026-07-26-agent-stack-v2-triptests.md
PreToolUse:Edit hook error: ["$CLAUDE_PROJECT_DIR"/scripts/master-write-guard.sh]: BLOCKED: praxis-master may only write ledgers, specs, and reports. Dispatch praxis-manager for '/Volumes/Sensidine/Praxis.build/src/thing.cs'.

$ sed -n '1313,1316p' docs/reports/2026-07-26-agent-stack-v2-triptests.md
>
> ```
> PreToolUse:Agent hook error: ["$CLAUDE_PROJECT_DIR"/scripts/agent-spawn-guard.sh]: BLOCKED: praxis-manager may not spawn the auditor. The master spawns praxis-auditor independently.
> ```

$ sed -n '201,204p' docs/agent-spawn-guard.md
######## FIELD 3: .tool_input.subagent_type ########
P  subagent_type=praxis-auditor     (mgr->auditor, FIRE)   exit=2 stderr_bytes=99
    stderr: BLOCKED: praxis-manager may not spawn the auditor. The master spawns praxis-auditor independently.
C  subagent_tyme=praxis-auditor     (invented, SILENT)     exit=0 stderr_bytes=0

$ sed -n '191p' docs/reports/2026-07-26-session36-agent-key-s9-control.md
- **`scripts/agent-spawn-guard.sh`** reads `agent_type` too; unexamined here.

$ grep -cF 'Harness fed synthetic payloads to' docs/agent-spawn-guard.md
1
$ grep -cF 'the guard on stdin.' docs/agent-spawn-guard.md
1
```

Final worktree status:

```
$ git status --porcelain
M  .claude/settings.json
 M AUDIT_LOG.md
 M DECISION_LOG.md
 M DISPATCH_LOG.md
 M ISSUE_REGISTER.md
 M MANIFEST.md
?? .claude/agent-memory/
?? docs/reports/2026-07-26-session34-manifest-amendment.md
?? docs/reports/2026-07-26-session34-p0-flush-audit.md
?? docs/reports/2026-07-26-session35-8sw-audit-round1.md
?? docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
?? docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
?? docs/reports/2026-07-26-session36-agent-key-audit.md
?? docs/reports/2026-07-26-session36-agent-key-lab.md
?? docs/reports/2026-07-26-session36-agent-key-s9-control.md
?? docs/reports/2026-07-26-session36-null-attack.md
?? docs/reports/2026-07-26-session36-worker-trigger-probe.md
```

`AUDIT_LOG.md`, `DECISION_LOG.md`, `ISSUE_REGISTER.md` were already dirty at session
start and were **not** touched by this unit. `DISPATCH_LOG.md` grew during the unit,
written by the registered `SubagentStart` hook `./scripts/dispatch-log-writeahead.sh`
(`.claude/settings.json:118`) — not by me and not by any worker:

```
$ tail -1 DISPATCH_LOG.md
- [2026-07-26T22:27:05Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session c1dec30 | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
```

Those rows are `STATE: dispatched` and are never closed — the S12 violation already
recorded in `specs/SPEC_RUBRIC.md`. This unit adds to the stranded set. Not repaired;
out of scope.

## Adversarial findings

Sixteen defects were found by adversarial workers across three rounds and all were
closed. The ones that would have shipped false claims:

1. **HIGH.** A MANIFEST row told readers the derived memory `project_agent-type-source.md`
   was false — 92 seconds *after* that memory had been corrected. The row steered
   readers away from the one file holding correct guidance.
2. **HIGH.** A row claimed SIGPIPE truncation "manufactured two false nulls in this task."
   Three distinct failure modes were merged. The one SIGPIPE (actor-hunt §4.4) produced a
   truncated transcript, not a null; the two actual false nulls came from an unresolvable
   agent name and macOS lacking a `timeout` binary.
3. **HIGH.** A row asserted a probe's own `agent_type` was `praxis-worker` three clauses
   after quoting that same report's "Payload shape remains UNVERIFIED." No session-36
   report observed it. The actual short-circuit is `scripts/master-bash-guard.sh:7`
   (`[ -n "$AGENT_ID" ] && exit 0`), which runs before the `agent_type` test on line 8.
4. **HIGH.** The manager memory described the corrected worker memory as still wrong —
   the last path by which the refuted claim read as a live competing position.
5. **HIGH.** The memory attributed the two-arm control's re-verification to "the master."
   `grep -ic "re-verified by the master"` on the source report returns 0; the report
   attributes it to praxis-manager (`**Manager:** praxis-manager`, §6 "run by me, not
   delegated", §10 "flagged for the master, not edited by me"). The dispatching brief
   asserted a master re-verification; that assertion is not in the report, and the memory
   now marks it as asserted-in-brief only.
6. **HIGH (regression, round 2).** The fix generalised a report-scoped hedge into
   "never tripped" for `master-write-guard.sh` and `agent-spawn-guard.sh`. Both are false —
   see the S6 section below.

Two adversarial claims were themselves checked and one brief premise was corrected: the
report's own header cross-reference to "§7" for its scope caveat is wrong; the caveat is
in §12 (§7 is *Adversarial findings*). Both memory files now cite §12 and flag the bad
cross-reference.

## S6 cross-block check

`specs/SPEC_RUBRIC.md` S6 is the criterion that already failed once in this project —
six deviations approved in isolation broke four downstream components. This unit
reproduced that failure mode in miniature and it is the most important finding here.

The round-2 fix was correct *within the scope of the one report it was reading*.
`agent-key-s9-control.md` §9 says of `master-write-guard.sh`: "Confirmed by reading,
**not** separately trip-tested" — a true statement about that control run. The fix
promoted it to a property of the guard: "never tripped." Cross-block, that is false:

- `docs/reports/2026-07-26-agent-stack-v2-triptests.md:54,128` — live in-repo `PreToolUse`
  Edit and Write denials naming the guard, verdict at `:142`.
- `docs/reports/2026-07-26-session34-manifest-amendment.md:198-206` — S9 invented-key
  control, `agent_type` exit 2 / 142 B vs `agent_typeX` exit 0 / 0 B.
- `.claude/agent-memory/praxis-manager/project_master_write_guard_routing.md` — a sibling
  memory in the same directory reading "Trip-tested under control 2026-07-26".

The same error hit `agent-spawn-guard.sh`, described as "unexamined ... no observed block"
while `docs/agent-spawn-guard.md` §5 records it firing `exit=2` under an S9 positive
control on all three fields it reads.

Two files in one memory directory were left in direct contradiction. That is exactly the
S6 failure: locally-valid, globally false. All three guards are now reported at three
distinct levels, with the genuinely-untested item narrowed to what it actually is —
whether the *settings* `agent` key, as opposed to the `--agent` flag, arms the write guard.
A cross-check between `project_master_write_guard_routing.md` and
`project_agent_type_mechanism.md` confirms they now agree.

**Negative test / S3:** not applicable and not claimed. This unit built no gate and
tripped none. No circuit-breaker claim appears in this report. The gate that *did* fire
during the unit is `dispatch-log-writeahead.sh`, observed by its own appended rows above.

## Files staged

**None.** The index is exactly as found: `1	0	.claude/settings.json`.

Modified in the worktree, unstaged, for the master to stage and commit:

- `/Volumes/Sensidine/Praxis.build/MANIFEST.md` — six appended rows, lines 118-123.
- `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/project_agent-type-source.md` — corrected in place.
- `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/MEMORY.md` — index hook rewritten.
- `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/feedback_scoped-hedge-vs-universal-negative.md` — new.
- `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-manager/project_agent_type_mechanism.md` — stale cross-reference removed, per-guard evidence levels split.
- `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-manager/MEMORY.md` — index hook rewritten.

The whole `.claude/agent-memory/` tree is untracked (`??`); the master decides whether it
is committed.

## For the master — not repaired, out of scope

1. `docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md` was staged (`M `) in the
   session-start snapshot and is untracked (`??`) now. The transition predates my first
   command — my baseline capture already showed the index as `1 0 .claude/settings.json`
   only. No worker ran an index operation. Three session-36 reports independently record
   the same anomaly. Unexplained.
2. This unit appended `STATE: dispatched` rows to `DISPATCH_LOG.md` that nothing closes
   (S12, already registered).
3. `docs/reports/2026-07-26-session36-agent-key-s9-control.md` header line 4 cites "§7"
   for its scope caveat; the caveat is §12. The report is an existing artefact and was
   not edited. Both memory files flag the error instead.
4. A subagent's final message can be lost to budget exhaustion with no error surfaced
   (worker 9). In an adversarial role this is indistinguishable from a clean pass unless
   the caller requires an explicit verdict token. Worth a standing rule.

## Result

Twelve workers, four adversarial rounds, sixteen defects found and closed, every
remaining claim traced to pasted output from this session. Both tasks are complete and
the index is provably untouched.

**Result: PASS**

This verdict is the manager's grade of the *workers'* output against S1 and S2, which is
the manager's job. It is not a grade of this report. Per the no-self-grade rule, the
authority on this unit is the independent audit the master runs next; I cannot and did
not spawn `praxis-auditor`.

---

## Appendix A — the six MANIFEST rows, verbatim

Reproduced below by `tail -6 MANIFEST.md` at the time of writing, not retyped.

```
| /docs/reports/2026-07-26-session36-agent-key-s9-control.md | Report | 0 | 2026-07-26 | HIGHEST-STANDING SESSION-36 ARTEFACT and the record of the session's one established finding — praxis-manager's S9 positive control on the root `"agent"` key in `.claude/settings.json`, verdict DECISIVE POSITIVE, re-run directly by the manager rather than accepted on worker report (§3 records worker 4's finding as re-run by the manager directly, per §6, and not accepted on report — paraphrase, not a quotation). Two-arm control in a lab replica, `--agent` never passed in either arm, `.claude/agents/praxis-master.md` present in BOTH arms (the precondition the earlier lab omitted): ARM X first root key `agent` → dumped payload, reproduced from the source bytes at report line 96 rather than re-rendered: `{"agent_type_present":true,"agent_type":"praxis-master","agent_id_present":false,"cmd":"echo hello > …/probeX.txt"}` (the `…` is the report's own elision), real `scripts/master-bash-guard.sh` denied 3x with the verbatim string "BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.", probe file never created; ARM Y identical position and value with the key renamed `zzz_bogus_agent_key` → `agent_type` absent, 0 BLOCKED, probe file written. Both halves of S9 discharged, and ARM Y's silence is informative ONLY because a content-independent liveness hook (`HOOK_RAN`) fired in both arms and stream-line counts (10 vs 11, empty stderr) rule out TRUNCATION — a separate failure mode that looks identical to a hook that never fired. Three distinct things, not one: the task's only SIGPIPE is a `head -c` recorded in /docs/reports/2026-07-26-session36-adversarial-actor-hunt.md §4.4, and it produced a truncated transcript, not a null; the task's two ACTUAL false nulls (§7.4, "Two of the four workers hit a false null in this one task") came from worker 3's unresolvable agent name (§7.1) and from macOS having no `timeout` binary (/docs/reports/2026-07-26-session36-null-attack.md §8.3). FINDING: the key IS a mechanism that sets `agent_type` in PreToolUse payloads on CC 2.1.220 (version verified in-session), CONDITIONAL on the name resolving to an existing `.claude/agents/<name>.md`; a missing definition makes the key a silent no-op — no warning, no stderr, exit 0. Supersedes the confounded null in /docs/reports/2026-07-26-session36-agent-key-lab.md and adopts the refutation in /docs/reports/2026-07-26-session36-null-attack.md. S2 CAVEAT CARRIED, NOT DISCHARGED (§12, "Scope caveat (S2)" — §7 is Adversarial findings): shown in a lab replica with cwd OUTSIDE the repo plus read-only confirmation that the repo holds both halves; behaviour in the repo's own directory is INFERRED, never directly observed, because CLAUDE.md:30 forbids a second session against this tree — closing it needs a human session or a `git worktree`. `master-write-guard.sh` armed by the same field was NOT separately re-tripped by THIS control (§9 verbatim: "Confirmed by reading, **not** separately trip-tested") — that is a statement about this control run's scope, NOT the guard's overall level: the guard is separately trip-tested live on Edit and Write (/docs/reports/2026-07-26-agent-stack-v2-triptests.md:54, :128, verdict :142) and S9 invented-key-controlled at script level (/docs/reports/2026-07-26-session34-manifest-amendment.md:198-206). Repo settings sha256 unchanged (eed25e67…), staged diff still `1 0`, nothing staged by the task; §10 flags `.claude/agent-memory/praxis-worker/project_agent-type-source.md` as now-false guidance, deliberately not edited — that describes the REPORT'S state at time of writing, not current repo state: the memory was corrected later in session 36 and now opens "This file previously recorded the opposite claim. That claim is REFUTED." and agrees with this report |
| /docs/reports/2026-07-26-session36-null-attack.md | Report | 0 | 2026-07-26 | ADVERSARIAL worker report that REFUTED the null result of /docs/reports/2026-07-26-session36-agent-key-lab.md — headline "RESULT: THE NULL IS FALSE. COUNTEREXAMPLE PRODUCED", result line "BREAK FOUND". Standing: a genuine break whose causal claim was independently re-run by praxis-manager before being relied on, so it is evidence of record rather than an unreviewed sub-report — but the authoritative write-up of the finding is /docs/reports/2026-07-26-session36-agent-key-s9-control.md, not this file. Twelve arms in a fresh lab, all payloads dumped raw and verbatim: arm 0 baseline `agent_type` genuinely absent; ARM 2 THE COUNTEREXAMPLE — project `.claude/settings.json` `"agent": "labmaster"` with NO `--agent` flag → `"agent_type":"labmaster"`; arms 3/4 unresolvable names (`ghostagent`; `praxis-master` with no definition in that lab) → absent, arm 4 exactly reproducing the earlier null AND explaining it; arms 8/9 the decisive A/B/A causal isolation — settings file byte-identical, the ONLY variable being whether `praxis-master.md` exists → absent then present, so toggled by a file and not by key spelling; arms 10/11 the chain run out to the real `master-bash-guard.sh` BLOCK; arms 6/7 the same key working from `.claude/settings.local.json` and from `--settings`, so the claimed flag-vs-settings asymmetry does not exist. Mechanism = key AND resolvable definition; an unresolvable name is dropped silently, which is the perfect null-manufacturing condition. The lead came from `claude --help` read in-session — "Overrides the 'agent' setting". Records the near-miss where macOS has no `timeout` binary, the first arm produced zero dumps, and only an independent liveness log stopped it reading as another confirming null. Own limits kept intact: real-repo behaviour INFERRED from the replica plus read-only config inspection, not observed (CLAUDE.md:30); user-level settings scope and the `agentType` / `defaultAgent` / `agent`-as-object spellings UNVERIFIED; malformed-but-present definitions never separated from absent ones |
| /docs/reports/2026-07-26-session36-agent-key-audit.md | Report | 0 | 2026-07-26 | Cold praxis-auditor grade of the staged one-path index at HEAD c1dec30 — the `"agent": "praxis-master"` insert in `.claude/settings.json`, producer reasoning deliberately not read. AUTHORITATIVE AS AN AUDIT VERDICT: report line 5 verbatim — "**Result: FAIL** — S1, S2, S4, S5, S7, S9. No token minted." QUOTATION CONVENTION, this row: quotations reproduce the source bytes exactly, `**` emphasis preserved rather than stripped or added, and where a quote is cut from a line-wrapped source sentence the wrap is flagged. Nothing was edited, fixed, staged or committed by it, and `.claude/state/` carries no token. Independent checks that PASS and are credited: JSON valid (`jq` exit 0), `agent` purely additive at root position 0 with `env`/`hooks`/`permissions` byte-unchanged, column-0 indentation cosmetic and also a provenance tell, the 8sw report confirmed `??` and out of the index, and S4's timing sub-claim VERIFIED TRUE from pasted mtimes (ledger written 5s before the index). Fails: S1 — no producer report existed and the claim-bearing DECISION_LOG row describes rather than pastes, citing `git diff .claude/settings.json` (empty by construction, worktree-vs-index) for a staged-content claim only `git diff --cached` can establish; S5/S4 — the authorising 21:36Z row is neither staged nor in HEAD, so the commit would carry the act without the authorisation and against committed HANDOFF.md:5 and :18, with both PROPOSED BY and APPROVED BY filled from one transcribed verbal; S2 — the producer's "no guarantee here rests on the key" falsified by toggle, `master-bash-guard.sh` and `master-write-guard.sh` moving exit 0 → exit 2 on that field alone; S7 — 8sw at FAIL, Praxis_build-sk8 P1 open, 599885e disposition open, `parked/Praxis_build-37h` unresolved (the auditor itself marks S7 least clear-cut and does not rest the verdict on it). SUPERSEDED IN ONE PART ONLY, AND ONLY AT LAB LEVEL: its §1.4 "The positive control has not been run, by anyone" was true when written and is now discharged IN A LAB REPLICA by /docs/reports/2026-07-26-session36-agent-key-s9-control.md — §1.4 asked for "a live main-thread session with the key installed and a hook trip observed", while the control ran with cwd OUTSIDE the repo (its §12 scope caveat), so IN-REPO sufficiency remains the open spec question. Reported at the level the evidence supports: given a resolvable definition the key arms `master-bash-guard.sh`, which was TRIP-TESTED through the real hook path (ARM X denied 3x, probe file never created), while `master-write-guard.sh` keys on the same field and was not re-tripped by that control — s9-control §9 verbatim, "Confirmed by reading, **not** separately trip-tested", a hedge scoped to THAT control run (§9 contains no "never"). THE GUARD ITSELF IS TRIP-TESTED LIVE: PreToolUse denials naming scripts/master-write-guard.sh on Edit (/docs/reports/2026-07-26-agent-stack-v2-triptests.md:54) and on Write (:128, verdict :142, quoted as that line's leading fragment because the verdict sentence wraps onto :143 — "**PASS** — `master-write-guard.sh` fires on the `Write` tool"), armed in both by `--agent praxis-master`; plus a direct-stdin trip carrying the S9 invented-key control at /docs/reports/2026-07-26-session34-manifest-amendment.md:198-206 (`agent_type` exit 2 / 142 B stderr vs `agent_typeX` exit 0 / 0 B). CAVEAT CARRIED from triptests:61 — only the last hook to finish surfaces its message, so a live trip alone cannot show master-write-guard.sh was the ONLY denier; the session-34 stdin invocation is what makes attribution unambiguous — the source phrase is line-wrapped across session-34-manifest-amendment.md:163-164, so only the fragment that resolves on a single line is quoted, "no other hook was in", with "the path" carried onto :164. What session 36 did NOT separately re-test is whether the SETTINGS `agent` key, as opposed to the `--agent` flag, arms THIS guard — only `master-bash-guard.sh` was tripped through the key. Every other finding stands ungraded and unrepaired |
| /docs/reports/2026-07-26-session36-agent-key-lab.md | Report | 0 | 2026-07-26 | SUPERSEDED INTERMEDIATE — worker sub-report (worker 3) whose headline result was REFUTED; it is NOT an authoritative finding and must be read only alongside /docs/reports/2026-07-26-session36-null-attack.md, which broke it, and /docs/reports/2026-07-26-session36-agent-key-s9-control.md, which replaces it. Its headline reads "NULL RESULT. The hypothesis is refuted by direct measurement" and its result line records "PASS" on what it calls a decisive negative answer; arms A (`"agent"`), B (`"zzz_bogus_agent_key"`) and C (key absent) came back indistinguishable on every measured dimension with `agent_type` absent in all three. THE NULL WAS CONFOUNDED: the lab held no `.claude/agents/praxis-master.md`, so the name could not resolve and the key was dropped silently — a state indistinguishable on disk from an ignored key. That defect was reproduced as arm 4 of the null-attack and broken by its arms 8/9 definition-file A/B/A, and the opposite result was then obtained in the manager's two-arm control. Its own limits item 1 named ONLY the directory difference (a different project directory, so the result "does not transfer automatically"); the confounder itself — the missing agent-definition file — is never mentioned in this report at all (grep for definition/resolve/praxis-master.md returns zero matches). The judgment that a hedge named "the confounder without recognizing it as one" belongs to /docs/reports/2026-07-26-session36-null-attack.md §8.4, where it is made about a different artefact and quotes a sentence that does not appear here. What survives is method, not conclusion: harness self-tests run BEFORE any arm, an arm-differs-only-in-key-name diff, and an ARM P wrapper control proving the second hooks-array entry executes and the real guard denies with the probe file uncreated. THIS REPORT'S OWN MECHANISM CONCLUSION IS FALSE AND MUST NOT BE CITED — and that falsity is scoped to the report. The memory derived from it, `.claude/agent-memory/praxis-worker/project_agent-type-source.md`, was CORRECTED later in session 36: it now opens "This file previously recorded the opposite claim. That claim is REFUTED." and agrees with /docs/reports/2026-07-26-session36-agent-key-s9-control.md, so it is current guidance to be read, not avoided. Also the first artefact to record the concurrent-index anomaly on the 8sw report path (staged at snapshot, untracked later, no index op run by it) |
| /docs/reports/2026-07-26-session36-adversarial-actor-hunt.md | Report | 0 | 2026-07-26 | INTERMEDIATE WORKING ARTEFACT — adversarial worker sub-report (worker 2). NOT superseded as a finding: /docs/reports/2026-07-26-session36-agent-key-s9-control.md ADOPTED it rather than replacing it — that report's §5 rests one of its three "Observed, not inferred" bullets on worker 2's dumped payloads, and §7.5 credits it — and the question worker 2 answers is a different one, still unrefuted. Its lasting contributions are that finding plus the nested-`claude` harness the later control reused. Result line: FAIL (claim broken), "The claim's conclusion is falsified; its premise is not." Established live: a subagent's Bash tool CAN launch a nested main-thread session running as `praxis-master` whose PreToolUse dispatch executes the real `scripts/master-bash-guard.sh` (sha256 2dd67afc…) and emits the real BLOCKED string at exit 2 with `probeF.txt` never created, against a payload observed in the same dispatch to carry `agent_type == "praxis-master"` and NO `agent_id`; and the repo's own settings PreToolUse/Bash block does dispatch on subagent calls (`no-commit-guard.sh` fired on a free-text probe). NOT established, and the report says so: the attacked premise SURVIVED — every subagent shape it could build, depth-1 and depth-2 with `agent_type` exactly `praxis-master`, carried a non-empty 17-hex `agent_id` and produced byte-identical silence, which it records as "I could not find one", not "none exists"; it never observed its own payload; `--bg`, `--resume`/`--fork-session`, SDK/stream-json input and MCP-initiated calls untested; no run combined the real script WITH the repo's real registration; and the S9 second half was NOT run at config-key level — its Attack-D silences are field-VALUE controls, not invented-KEY controls. Attack E stopped rather than worked around, on CLAUDE.md:30. LEAVES AN OPEN SPEC-INTERPRETATION QUESTION FOR THE MASTER, unanswered here: whether an out-of-tree harness executing the real script under a real PreToolUse dispatch satisfies S9, or whether S9 demands the in-repo registration. Surprises recorded: hook denials surface as `"non_execution_kind":"permission-rule"` and fire even under `bypassPermissions`; `--settings` will execute a hook script outside the session's project dir, so the guard is not bound to the repo it lives in; a `head -c` SIGPIPE truncation looks exactly like "the hook never fired" |
| /docs/reports/2026-07-26-session36-worker-trigger-probe.md | Report | 0 | 2026-07-26 | LOWEST-STANDING SESSION-36 ARTEFACT — purely observational worker sub-report (worker 1), four Bash probes with output pasted verbatim; NOT an authoritative finding about `agent_type` or about the settings key, and it makes no such claim. It answers one narrow question — did `scripts/master-bash-guard.sh` emit its BLOCKED string on this worker's calls — with NO: both write probes returned `exit=0`, no hook deny text, files written. ITS SILENCE IS UNINFORMATIVE BY CONSTRUCTION and the report disclaims it in its own scope note — the hook payload itself (`agent_id`, `agent_type`) was not captured in this probe, call 3 is shell environment only, and "Payload shape remains UNVERIFIED." (the full sentence is line-wrapped in the source, so only this fragment is quoted). THE PROBE'S OWN `agent_type` WAS NOT OBSERVED — not in this report, and worker 2 records the same limit of ITSELF ("I never observed **this** session's own PreToolUse payload."). Scoped to the dispatched workers' OWN payloads: worker-shaped payloads WERE captured in session 36 — s9-control §5 pastes worker 2's dumps of subagents it spawned whose `agent_type` was exactly `praxis-master`, each with a non-empty 17-hex `agent_id` (`a530cc121d2d37552`, `aea6ef2edb28e8096`), so what is missing is the capturing agent's own payload, not any subagent payload. The short-circuit that IS isolated is `scripts/master-bash-guard.sh:7`, `[ -n "$AGENT_ID" ] && exit 0`, which fires on the non-empty `agent_id` observed on every subagent shape examined and runs BEFORE the `agent_type` test on line 8 (s9-control §5). /docs/reports/2026-07-26-session36-agent-key-s9-control.md logs this probe as worker 1, "Guard silent, exit 0. Payload not observed", and that silence is ONE OF THREE "Observed, not inferred" observations behind the manager's refusal to run the briefed control on the real settings file — the refusal rests principally on worker 2's dumped payloads, not on this silence. Residual value is environmental, captured live and not inferred: `CLAUDE_CODE_VERSION=2.1.220 (Claude Code)`, `CLAUDE_CODE_CHILD_SESSION=1`, `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=2`, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS=8`, session id `2488feec-…`, and a parent process of `claude --dangerously-skip-permissions` |
```
