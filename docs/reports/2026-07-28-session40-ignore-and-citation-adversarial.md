# Session 40 — Adversarial: `.gitignore` scope + agent-memory citation enumeration

**Task:** attack two claims (gitignore scope; "exactly two files cite a path under
`.claude/agent-memory/`") and characterise the rhetorical role of the two named citations.
**Mode:** ADVERSARIAL. Read-only except this file.
**Date of observation:** 2026-07-28.
**Report path:** `/Volumes/Sensidine/Praxis.build/docs/reports/2026-07-28-session40-ignore-and-citation-adversarial.md`

---

## 1. Claim 1 attack

> "`.gitignore` now ignores everything under `.claude/agent-memory/`, and it ignores NOTHING ELSE
> that was previously visible."

### 1.1 What actually changed

```
$ git diff -- .gitignore
diff --git a/.gitignore b/.gitignore
index b2f75d1..280f86e 100644
--- a/.gitignore
+++ b/.gitignore
@@ -16,3 +16,11 @@ signals/*.json
 # ...except the version-controlled canonical schema template (bead 6h7)
 !signals/signal-template.json
 .claude/state/
+
+# Agent memory — LOCAL ONLY, deliberately never committed (human ruling
+# 2026-07-28, Praxis_build-cbf). Auto-loaded into the context of each agent type.
+# Held out of the repo because this repo is PUBLIC and these notes carry working
+# guard-evasion detail. Consequence, accepted knowingly: any report citing a path
+# under here cites a DECLARED LOCAL-ONLY artifact — it will not resolve for
+# anyone who clones this repo, by design, not by accident.
+.claude/agent-memory/
```

Exactly one new *pattern* (line 26); the other seven added lines are a blank line and six `#`
comments. So the entire behavioural delta is line 26.

```
$ grep -n 'agent-memory' .gitignore
26:.claude/agent-memory/
$ wc -l < .gitignore
      26
```

### 1.2 HIGHEST-VALUE ATTACK — is anything under that directory already TRACKED?

A tracked file is unaffected by `.gitignore`, which would make the "unpublished" intent false for
that file. **Attack fails: nothing is tracked, and nothing ever was.**

```
$ git ls-files -- '.claude/agent-memory'
---EXIT:0---
=== ls-files count ===
       0

$ git ls-tree -r HEAD --name-only | grep -i 'agent-memory'
tree-grep-exit=1          # 1 = no match: absent from the HEAD tree

$ git log --all --oneline --diff-filter=A -- '.claude/agent-memory' '*agent-memory*'
log-exit=0                # no output: never added on any ref
```

Corroborating, the global "tracked-but-ignored" check returns empty:

```
$ git ls-files -i -c --exclude-standard
exit=0 / count=0
$ git ls-files | wc -l
     186
$ git ls-files -- .claude
.claude/agents/orchestrator-auditor.md
.claude/agents/praxis-auditor.md
.claude/agents/praxis-manager.md
.claude/agents/praxis-master.md
.claude/agents/praxis-tutor.md
.claude/agents/praxis-worker.md
.claude/hooks/audit-approve.sh
.claude/hooks/gate-commit.sh
.claude/hooks/inject-handoff.sh
.claude/hooks/notify.sh
.claude/hooks/precompact-handoff.sh
.claude/hooks/stop-gate.sh
.claude/settings.json
.claude/skills/praxis-build-manager/SKILL.md
```

No index entry under `.claude/agent-memory/`. The tracked-file escape hatch does not exist here.

### 1.3 Half A — does it reach *everything* under the directory?

Exhaustive: every path in the worktree (571, `.git/` excluded) fed to `check-ignore`, filtered to
matches of line 26. All 26 matches are the directory itself or its contents; the enumeration also
shows nothing under it escapes.

```
$ find . -mindepth 1 -not -path '*/.git/*' | git check-ignore -v --no-index --stdin | grep ':26:'
.gitignore:26:.claude/agent-memory/	.claude/agent-memory
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-master
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-auditor
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/feedback_scoped-hedge-vs-universal-negative.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/project_agent-type-source.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/MEMORY.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/project_s9-positive-control-harness.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/project_commit_guard_bypass.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/project_false_null_hazard.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/project_agent_type_mechanism.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/feedback_workers_write_to_agent_memory.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/project_master_write_guard_routing.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/project_s13_task_vs_agent.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/MEMORY.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/project_manager_report_contract_gate.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/feedback_verdict_token_required.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/project_park_commit_paste_hazard.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/project_8sw_park_gate_boundary.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-auditor/audit_evidence_standards.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-auditor/audit_ledger_claims_vs_beads.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-auditor/grading_verdict_discipline.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-auditor/MEMORY.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-auditor/project_flush_shape_conflict.md
```

Hypothetical paths that do not yet exist — dotfiles inside, nested dotdirs, arbitrary depth — are
also caught:

```
IGNORED   	.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/MEMORY.md
IGNORED   	.gitignore:26:.claude/agent-memory/	.claude/agent-memory/.hidden-dotfile
IGNORED   	.gitignore:26:.claude/agent-memory/	.claude/agent-memory/a/b/c/deep.md
IGNORED   	.gitignore:26:.claude/agent-memory/	.claude/agent-memory/.config/.secret
```

No re-including `!` rule follows line 26 (it is the last line), and there is no nested `.gitignore`
inside the directory that could interact:

```
$ find .claude/agent-memory -name '.gitignore'
(no output)
```

### 1.4 Half B — over-reach / collateral. Near-miss names

```
NOT-IGNORED	.claude/agent-memory-backup/x.md
NOT-IGNORED	.claude/agent-memory.md
NOT-IGNORED	.claude/agent-memoryX/x.md
NOT-IGNORED	.claude/agentmemory/x.md
NOT-IGNORED	docs/.claude/agent-memory/x.md
NOT-IGNORED	agent-memory/x.md
NOT-IGNORED	.claude/settings.json
NOT-IGNORED	.claude/agents/praxis-worker.md
NOT-IGNORED	docs/reports/2026-07-26-session36-null-attack.md
```

The pattern contains a `/`, so it is anchored to the repo root: `docs/.claude/agent-memory/x.md`
and a bare `agent-memory/` elsewhere are untouched. Trailing `/` makes it directory-only, so
`.claude/agent-memory.md` (a file) is untouched. No prefix bleed onto `-backup`/`X`/`agentmemory`.

Full ignored-set audit — every ignored path in the repo, with its source rule. Only one line-26
entry; everything else predates this change (root `.gitignore` lines 4/5/7/18, `.beads/.gitignore`):

```
$ git status --ignored --short | grep '^!!' | while read p; do git check-ignore -v --no-index "$p"; done
.gitignore:5:.DS_Store	.DS_Store
.gitignore:5:.DS_Store	.beads/.DS_Store
.beads/.gitignore:28:.local_version	.beads/.local_version
.beads/.gitignore:57:backup/	.beads/backup/
.beads/.gitignore:3:embeddeddolt/	.beads/embeddeddolt/
.beads/.gitignore:38:export-state.json	.beads/export-state.json
.beads/.gitignore:16:interactions.jsonl	.beads/interactions.jsonl
.beads/.gitignore:9:last-touched	.beads/last-touched
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/
.gitignore:18:.claude/state/	.claude/state/
.gitignore:7:Redemtion/	Redemtion/
.gitignore:5:.DS_Store	docs/.DS_Store
.gitignore:4:__pycache__/	scripts/__pycache__/
.gitignore:4:__pycache__/	scripts/tests/__pycache__/
```

### 1.5 Subdirectory cwd and absolute paths

```
=== from subdir cwd (docs/) ===
.gitignore:26:.claude/agent-memory/	../.claude/agent-memory/praxis-worker/MEMORY.md
exit=0
=== from deeper subdir (docs/reports) ===
.gitignore:26:.claude/agent-memory/	../../.claude/agent-memory/praxis-manager/MEMORY.md
exit=0
=== absolute path ===
.gitignore:26:.claude/agent-memory/	/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/project_agent-type-source.md
exit=0
```

Holds from nested cwd (relative `../` and `../../` forms) and for the absolute path form.

### 1.6 Observations that do NOT break Claim 1 but are material

**O1 — the rule is NOT STAGED.** `.gitignore` is worktree-modified only:

```
$ git status --short -- .gitignore
 M .gitignore
$ git diff --cached -- .gitignore
(empty)
$ git diff --cached --name-only
docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
docs/reports/2026-07-26-session36-agent-key-audit.md
docs/reports/2026-07-26-session36-agent-key-lab.md
docs/reports/2026-07-26-session36-agent-key-s9-control.md
docs/reports/2026-07-26-session36-null-attack.md
docs/reports/2026-07-26-session36-worker-trigger-probe.md
```

Ignore behaviour observed above is real *in this worktree* (git reads the worktree `.gitignore`),
so the claim's present tense is true here. But the rule is in neither the index nor any ref — a
clone or a second `git worktree` today would not carry it. RECOMMENDATION only; I staged nothing.

**O2 — `src/` reports as ignored but matches no ignore rule.** Pre-existing, unrelated to line 26.

```
$ git status --ignored --short | grep src
!! src/
$ git check-ignore -v --no-index src/foo.txt
src-probe-exit=1          # no rule matched
$ ls -la src
-rw-r--r--  .DS_Store
drwxr-xr-x  file-drop
```

`src/` contains only ignorable/empty content, so git collapses it. Not collateral of the new rule.
Reported, not fixed.

**O3 — pre-existing near-miss in `.git/info/exclude`:** `**/.claude/agent-memory-local`. Different
name; does not cover `.claude/agent-memory/` and is not affected by it.

### 1.7 Claim 1 verdict

**HOLDS.** Both halves survive. Every path under the directory is caught, including dotfiles and
arbitrary nesting, from subdir cwd and via absolute path; nothing else in the repo is newly ignored
(the only behavioural delta is line 26, and its complete match set is the target directory); and the
highest-value attack — an already-tracked file inside the directory — is empirically dead:
`git ls-files` returns zero, `git ls-tree HEAD` returns zero, and no ref ever added such a file.

---

## 2. Claim 2 sweep

> "Exactly two files in this repository cite a path under `.claude/agent-memory/`:
> `docs/reports/2026-07-26-session36-null-attack.md:313` and
> `docs/reports/2026-07-26-session36-agent-key-s9-control.md:196`."

**BROKEN.** Not two files — **14 files outside the memory directory, carrying 40 path citations**
(plus 3 more files inside the memory directory itself). Sweep tool and command:

```
$ rg --version
ripgrep 15.1.0
$ rg -c --hidden --no-ignore --glob '!.git/**' 'agent-memory/[A-Za-z0-9_.\-]' . | sort
./.claude/agent-memory/praxis-auditor/audit_evidence_standards.md:1
./.claude/agent-memory/praxis-manager/project_agent_type_mechanism.md:1
./.claude/agent-memory/praxis-worker/project_agent-type-source.md:1
./DECISION_LOG.md:7
./DISPATCH_LOG.md:1
./docs/reports/2026-07-26-session36-agent-key-s9-control.md:1
./docs/reports/2026-07-26-session36-manifest-and-memory.md:11
./docs/reports/2026-07-26-session36-null-attack.md:1
./docs/reports/2026-07-27-session37-restage-audit.md:1
./docs/reports/2026-07-27-session37-restage-split.md:2
./docs/reports/2026-07-27-session38-guard-evasion-test.md:3
./docs/reports/2026-07-28-session39-dispatch-log-closer.md:1
./docs/reports/2026-07-28-session40-memory-correction-adversarial.md:4
./HANDOFF.md:2
./ISSUE_REGISTER.md:3
./MANIFEST.md:2
./STATUS.md:1
```

Status source used for the table below:

```
$ git status --short
 M .claude/settings.json
 M .gitignore
 M AUDIT_LOG.md
 M DECISION_LOG.md
 M DISPATCH_LOG.md
 M HANDOFF.md
 M ISSUE_REGISTER.md
 M MANIFEST.md
 M STATUS.md
A  docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
A  docs/reports/2026-07-26-session36-agent-key-audit.md
A  docs/reports/2026-07-26-session36-agent-key-lab.md
A  docs/reports/2026-07-26-session36-agent-key-s9-control.md
A  docs/reports/2026-07-26-session36-null-attack.md
A  docs/reports/2026-07-26-session36-worker-trigger-probe.md
 M scripts/dispatch-log-writeahead.sh
?? F
?? docs/reports/2026-07-26-session34-manifest-amendment.md
?? docs/reports/2026-07-26-session34-p0-flush-audit.md
?? docs/reports/2026-07-26-session35-8sw-audit-round1.md
?? docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
?? docs/reports/2026-07-26-session36-manifest-and-memory.md
?? docs/reports/2026-07-27-session36-park-rule-escalation.md
?? docs/reports/2026-07-27-session37-restage-audit.md
?? docs/reports/2026-07-27-session37-restage-split.md
?? docs/reports/2026-07-27-session38-guard-evasion-test.md
?? docs/reports/2026-07-28-session39-agents-dir-write-path.md
?? docs/reports/2026-07-28-session39-closer-negative-tests.md
?? docs/reports/2026-07-28-session39-dispatch-log-closer-adversarial.md
?? docs/reports/2026-07-28-session39-dispatch-log-closer-build.md
?? docs/reports/2026-07-28-session39-dispatch-log-closer.md
?? docs/reports/2026-07-28-session39-live-vs-piped-attack.md
?? docs/reports/2026-07-28-session40-memory-correction-adversarial.md
?? scripts/dispatch-log-close.sh
?? scripts/tests/test-dispatch-log-close.sh
```

### 2.1 FULL HIT TABLE — every citation of a path under `.claude/agent-memory/`

Windowed extract per hit (`…` marks truncation of a long ledger row); status per file from the two
commands above. `A ` = STAGED, ` M` = UNSTAGED-tracked, `??` = UNTRACKED.

| # | file:line | status | citing sentence (windowed) |
|---|---|---|---|
| 1 | `ISSUE_REGISTER.md:41` | UNSTAGED-tracked | …READ-ONLY CONSTRAINT VIOLATED BY A SPAWNED WORKER — an adversarial `praxis-worker`, briefed read-only inside the project repo, wrote two files into the working tree: `` `.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md` `` (new) and `` `.claude/agent-memory/praxis-worker/MEMORY.md` `` (modified) \| WHY: this is not a tidiness issue. `` `.claude/agent-memory/praxis-worker/` `` is DURABLE and… |
| 2 | `ISSUE_REGISTER.md:43` | UNSTAGED-tracked | …AGGRAVATING FACTOR: the evasion recipe is currently written into `` `.claude/agent-memory/praxis-worker/` ``, auto-loaded into every future worker context — see the F1 row above; the two are one remediation unit \| STATE: open… |
| 3 | `ISSUE_REGISTER.md:45` | UNSTAGED-tracked | **THE MASTER CANNOT WRITE ITS OWN PERSISTENT MEMORY.** `` `scripts/master-write-guard.sh` `` blocks every path under `` `.claude/agent-memory/praxis-master/` ``, so the one agent in the stack that survives across sessions by design has no durable memory… |
| 4 | `HANDOFF.md:12` | UNSTAGED-tracked | **▶ WHY C1 FAILED…** A **fifth dangling citation outside `docs/`** that the declared enumeration missed: `` `.claude/agent-memory/praxis-worker/project_agent-type-source.md` ``, cited at `…session36-null-attack.md:313` (absolute-path form) and `…session36-agent-key-s9-control.md:196`. Verified at source: `git ls-files` empty, not in `HEAD`… |
| 5 | `HANDOFF.md:46` | UNSTAGED-tracked | **F1** — an adversarial worker violated its read-only brief and wrote `` `.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md` `` + that dir's `MEMORY.md`. **CORRECT, do not delete**… |
| 6 | `DISPATCH_LOG.md:107` | UNSTAGED-tracked | …Disclosed two worker scope breaches: a build worker wrote into `` `.claude/agent-memory/praxis-worker/` `` unbidden and deleted the original false sentence before the manager restored it… |
| 7 | `STATUS.md:11` | UNSTAGED-tracked | **Why C1 failed:** a fifth dangling citation *outside* `docs/` — `` `.claude/agent-memory/praxis-worker/project_agent-type-source.md` `` — which no commit in the 3-commit plan lands, making it unbounded rather than transient… |
| 8 | `DECISION_LOG.md:81` | UNSTAGED-tracked | …(2) correct the stale worker memory `` `.claude/agent-memory/praxis-worker/project_agent-type-source.md` ``, which asserts the null that the S9 two-arm control REFUTED… |
| 9 | `DECISION_LOG.md:95` | UNSTAGED-tracked | …F1 — the adversarial praxis-worker VIOLATED its read-only constraint and wrote `` `.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md` `` plus that directory's `MEMORY.md` into the working tree… |
| 10 | `DECISION_LOG.md:97` | UNSTAGED-tracked | …(2) The poisoned worker memory at `` `.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md` `` is AUTO-LOADED into every future worker context… |
| 11 | `DECISION_LOG.md:107` | UNSTAGED-tracked | …the decisive defect is a FIFTH dangling citation that my declared enumeration missed — `` `.claude/agent-memory/praxis-worker/project_agent-type-source.md` ``, cited by two of the six staged reports… |
| 12 | `DECISION_LOG.md:115` | UNSTAGED-tracked | …\| WHERE: `` `.claude/agent-memory/praxis-worker/` ``; `` `.gitignore` `` \| WHEN: session 39, 2026-07-28 \| HOW: **DELETION WAS REJECTED ON THE 22:55Z PRECEDENT**… |
| 13 | `DECISION_LOG.md:119` | UNSTAGED-tracked | …(2) session 37 recorded an adversarial worker writing into `` `.claude/agent-memory/praxis-worker/` `` against a read-only brief; this session praxis-manager wrote into `` `.claude/agent-memory/praxis-manager/` `` against an explicit written prohibition… |
| 14 | `DECISION_LOG.md:125` | UNSTAGED-tracked | …\| WHERE: bead `Praxis_build-cbf`; `` `.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md` ``; `` `.gitignore` ``; report `docs/reports/2026-07-28-session40-agent-memory-disposition.md`… |
| 15 | `MANIFEST.md:118` | UNSTAGED-tracked | …§10 flags `` `.claude/agent-memory/praxis-worker/project_agent-type-source.md` `` as now-false guidance, deliberately not edited — that describes the REPORT'S state at time of writing, not current repo state: the memory was corrected later in session 36… |
| 16 | `MANIFEST.md:121` | UNSTAGED-tracked | …The memory derived from it, `` `.claude/agent-memory/praxis-worker/project_agent-type-source.md` ``, was CORRECTED later in session 36: it now opens "This file previously recorded the opposite claim. That claim is REFUTED."… |
| 17 | **`docs/reports/2026-07-26-session36-agent-key-s9-control.md:196`** | **STAGED** | `` `.claude/agent-memory/praxis-worker/project_agent-type-source.md` `` records the refuted null and… *(one of the two named; see §3)* |
| 18 | **`docs/reports/2026-07-26-session36-null-attack.md:313`** | **STAGED** | `` `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/project_agent-type-source.md` `` *(one of the two named; see §3)* |
| 19 | `docs/reports/2026-07-26-session36-manifest-and-memory.md:16` | UNTRACKED | 2. Correct or remove `` `.claude/agent-memory/praxis-worker/project_agent-type-source.md` ``, |
| 20 | `…session36-manifest-and-memory.md:128` | UNTRACKED | `.claude/agent-memory/praxis-worker/feedback_scoped-hedge-vs-universal-negative.md:3:description: Never promote a report-scoped hedge…` |
| 21 | `…session36-manifest-and-memory.md:129` | UNTRACKED | `.claude/agent-memory/praxis-worker/feedback_scoped-hedge-vs-universal-negative.md:11:"never tripped" is a new, stronger, and usually false claim.` |
| 22 | `…session36-manifest-and-memory.md:254` | UNTRACKED | - `` `.claude/agent-memory/praxis-manager/project_master_write_guard_routing.md` `` — a sibling |
| 23 | `…session36-manifest-and-memory.md:279` | UNTRACKED | - `` `/Volumes/…/.claude/agent-memory/praxis-worker/project_agent-type-source.md` `` — corrected in place. |
| 24 | `…session36-manifest-and-memory.md:280` | UNTRACKED | - `` `/Volumes/…/.claude/agent-memory/praxis-worker/MEMORY.md` `` — index hook rewritten. |
| 25 | `…session36-manifest-and-memory.md:281` | UNTRACKED | - `` `/Volumes/…/.claude/agent-memory/praxis-worker/feedback_scoped-hedge-vs-universal-negative.md` `` — new. |
| 26 | `…session36-manifest-and-memory.md:282` | UNTRACKED | - `` `/Volumes/…/.claude/agent-memory/praxis-manager/project_agent_type_mechanism.md` `` — stale cross-reference removed, per-guard evidence levels split. |
| 27 | `…session36-manifest-and-memory.md:283` | UNTRACKED | - `` `/Volumes/…/.claude/agent-memory/praxis-manager/MEMORY.md` `` — index hook rewritten. |
| 28 | `…session36-manifest-and-memory.md:324` | UNTRACKED | *(embedded MANIFEST row, duplicate of hit 15)* …§10 flags `` `.claude/agent-memory/praxis-worker/project_agent-type-source.md` `` as now-false guidance… |
| 29 | `…session36-manifest-and-memory.md:327` | UNTRACKED | *(embedded MANIFEST row, duplicate of hit 16)* …The memory derived from it, `` `.claude/agent-memory/praxis-worker/project_agent-type-source.md` ``, was CORRECTED later in session 36… |
| 30 | `docs/reports/2026-07-27-session37-restage-audit.md:70` | UNTRACKED | confounder the lab itself never names. The `` `.claude/agent-memory/praxis-worker/project_agent-type-source.md` `` |
| 31 | `docs/reports/2026-07-27-session37-restage-split.md:260` | UNTRACKED | `` `.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md` `` |
| 32 | `docs/reports/2026-07-27-session37-restage-split.md:261` | UNTRACKED | (new) and `` `.claude/agent-memory/praxis-worker/MEMORY.md` `` (modified). Both sit under |
| 33 | `docs/reports/2026-07-27-session38-guard-evasion-test.md:284` | UNTRACKED | `` `.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md` `` |
| 34 | `docs/reports/2026-07-27-session38-guard-evasion-test.md:368` | UNTRACKED | - `` `.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md` `` |
| 35 | `docs/reports/2026-07-27-session38-guard-evasion-test.md:370` | UNTRACKED | - `` `.claude/agent-memory/praxis-worker/MEMORY.md` `` — index entry updated to match. |
| 36 | `docs/reports/2026-07-28-session39-dispatch-log-closer.md:841` | UNTRACKED | `` `.claude/agent-memory/praxis-manager/MEMORY.md` ``. That was a direct violation of |
| 37 | `docs/reports/2026-07-28-session40-memory-correction-adversarial.md:5` | UNTRACKED | **Artifact:** `` `/Volumes/…/.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md` `` |
| 38 | `…session40-memory-correction-adversarial.md:6` | UNTRACKED | plus its index `` `/Volumes/…/.claude/agent-memory/praxis-worker/MEMORY.md` `` |
| 39 | `…session40-memory-correction-adversarial.md:63` | UNTRACKED | `` `.claude/agent-memory/praxis-manager/feedback_workers_write_to_agent_memory.md:11-15` ``: |
| 40 | `…session40-memory-correction-adversarial.md:320` | UNTRACKED | `` `.claude/agent-memory/praxis-manager/project_8sw_park_gate_boundary.md:31-35` `` carries an overlapping |

**Additionally, 3 path citations inside the memory directory itself** (self-referential; listed for
completeness — these files are themselves untracked and now ignored):

```
.claude/agent-memory/praxis-auditor/audit_evidence_standards.md:72:`.claude/agent-memory/praxis-worker/project_agent-type-source.md`, cited by two
.claude/agent-memory/praxis-manager/project_agent_type_mechanism.md:84:worker memory at `.claude/agent-memory/praxis-worker/project_agent-type-source.md` originally
.claude/agent-memory/praxis-worker/project_agent-type-source.md:77:(`.claude/agent-memory/praxis-manager/project_agent_type_mechanism.md`) — read that rather than
```

### 2.2 Wikilink-style references resolving into the directory

```
$ rg -n --hidden --no-ignore --glob '!.git/**' --glob '!.claude/agent-memory/**' '\[\[[a-z0-9_\-]+\]\]' .
./docs/runbooks/2026-07-23-cowork-agent-delegation-brief.md:29:   automated deploy. (See [[vm-cs-crlf-hash-gate]] for the CRLF gotcha itself.)
./docs/reports/2026-07-28-session40-memory-correction-adversarial.md:161:(`[[scoped-hedge-vs-universal-negative]] — the original error here was exactly a universal negative`).
```

Resolution check:

```
$ grep -rn '^name:' .claude/agent-memory/*/*.md | grep -E 'scoped-hedge|vm-cs-crlf'
.claude/agent-memory/praxis-worker/feedback_scoped-hedge-vs-universal-negative.md:2:name: scoped-hedge-vs-universal-negative
$ grep -rln 'vm-cs-crlf-hash-gate' .claude/agent-memory/
exit=1
```

- `docs/reports/2026-07-28-session40-memory-correction-adversarial.md:161` — **UNTRACKED** — a
  wikilink that DOES resolve into the ignored directory
  (`.claude/agent-memory/praxis-worker/feedback_scoped-hedge-vs-universal-negative.md`). Counts as a
  reference into the directory even though it is not a path string.
- `docs/runbooks/2026-07-23-cowork-agent-delegation-brief.md:29` — `[[vm-cs-crlf-hash-gate]]` does
  **not** resolve into that directory (no such slug). Not a hit.

### 2.3 Bare-directory mentions (mention the dir but no child path)

Recorded separately because "cite a path *under*" is arguably narrower. 31 further lines across 16
files, including three STAGED reports (`…session36-agent-key-audit.md:42`,
`…session36-agent-key-lab.md:259` — both `?? .claude/agent-memory/` inside a pasted `git status`)
and `.gitignore:26` itself. Representative extract:

```
./HANDOFF.md:24:… (2) decide whether `.claude/agent-memory/` gets committed, gitignored, or excluded…
./docs/reports/2026-07-26-session36-agent-key-audit.md:42:?? .claude/agent-memory/
./docs/reports/2026-07-26-session36-agent-key-lab.md:259:?? .claude/agent-memory/
./docs/reports/2026-07-28-session39-dispatch-log-closer.md:622:  anything into `.claude/agent-memory/`, and do not cite any path inside it."
./docs/reports/2026-07-28-session39-dispatch-log-closer.md:630:- **No writes to `.claude/agent-memory/` occurred this session**…
./docs/reports/2026-07-28-session39-dispatch-log-closer-adversarial.md:509:was written under `.claude/agent-memory/`.
./docs/reports/2026-07-25-agent-stack-install.md:73:… 'user' - ~/.claude/agent-memory/<agentType>/ …
./.gitignore:26:.claude/agent-memory/
```

### 2.4 `specs/`, `scripts/`, `.claude/` (outside the memory dir) — clean

```
$ rg -n --hidden --no-ignore 'agent-memory' specs/ scripts/
exit=1                     # no matches in either tree
```

Note: `ISSUE_REGISTER.md:45` states `scripts/master-write-guard.sh` "blocks every path under
`.claude/agent-memory/praxis-master/`" — but the literal string does not appear in `scripts/`. The
guard's own text does not name the directory. **Not investigated further; out of scope. Reported,
not fixed.**

### 2.5 Are any of these citations already published (present at HEAD)?

```
ISSUE_REGISTER.md  HEAD_path_citations=0  WORKTREE_path_citations=3
HANDOFF.md         HEAD_path_citations=0  WORKTREE_path_citations=2
DISPATCH_LOG.md    HEAD_path_citations=0  WORKTREE_path_citations=1
STATUS.md          HEAD_path_citations=0  WORKTREE_path_citations=1
DECISION_LOG.md    HEAD_path_citations=0  WORKTREE_path_citations=7
MANIFEST.md        HEAD_path_citations=0  WORKTREE_path_citations=2
AUDIT_LOG.md       HEAD_path_citations=0  WORKTREE_path_citations=0
```

No path citation is committed yet. All 40 sit in unstaged ledger edits, untracked reports, or the
two staged reports. Materially: the two named STAGED citations are the only ones currently on a path
to being committed by the staged set.

### 2.6 Claim 2 verdict

**BROKEN.** The enumeration is off by 12 files / 38 citations. The falsifier does not require an
exotic case: `DECISION_LOG.md:81`, `STATUS.md:11`, `HANDOFF.md:12` and `MANIFEST.md:118` all cite the
same file the two named reports cite — and `HANDOFF.md:12` and `DECISION_LOG.md:107` explicitly call
that citation "a fifth dangling citation *outside* `docs/`", i.e. the repo's own ledgers already
record that the two-file enumeration is incomplete.

A defensible narrower reading — "exactly two **STAGED** files cite a path under
`.claude/agent-memory/`" — **is true** on the evidence above (hits 17 and 18 are the only STAGED
ones). If that is what was meant, the claim as written omits the scope qualifier that carries it.

---

## 3. Claim 3 characterisation

### 3.1 `docs/reports/2026-07-26-session36-null-attack.md:313` — STAGED

Section heading and full surrounding text, verbatim:

```
## 9. Stale artifact flagged (NOT edited — outside my write scope)

`/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/project_agent-type-source.md`
records the now-refuted null as a project memory and advises "do not propose the settings
key as a way to set `agent_type`." That guidance is wrong and should be corrected by
whoever owns write access to it. Same for
`docs/reports/2026-07-26-session36-agent-key-lab.md`, cited there as the evidence base.
```

**Rhetorical role: (ii) DEFECT POINTER.** The section is titled "Stale artifact flagged (NOT edited
— outside my write scope)"; the operative sentence is "That guidance is wrong and **should be
corrected by whoever owns write access to it**." Nothing in the report's argument rests on this
file — the refutation is carried by the report's own two-arm evidence. Removing the citation would
not weaken any claim in the report; it would only drop a work item.

### 3.2 `docs/reports/2026-07-26-session36-agent-key-s9-control.md:196` — STAGED

```
## 10. Stale artifact flagged, NOT edited

`.claude/agent-memory/praxis-worker/project_agent-type-source.md` records the refuted null and
advises "do not propose the settings key as a way to set `agent_type`." **That guidance is now
false.** It is another agent's memory namespace; flagged for the master, not edited by me.
`docs/reports/2026-07-26-session36-agent-key-lab.md` is its cited evidence base and carries the
same confounded conclusion — it should be read only alongside this report.
```

**Rhetorical role: (ii) DEFECT POINTER.** Same shape: section titled "Stale artifact flagged, NOT
EDITED", operative sentence "**That guidance is now false.** … flagged for the master, not edited by
me." The file is the *object* of the complaint, not the support for it.

**Qualification, because it is not purely (ii):** each citation embeds a factual assertion *about*
the cited file's contents ("records the refuted null and advises '…'"). That sub-claim is
verification-bearing — a reader can only check it by opening the file. So the consequence of an
unresolvable path differs by layer: the *argument* survives (nothing evidential is lost), but the
*assertion about the file* becomes uncheckable. And the work item it points at is, per §3.3, already
discharged.

Both citations are in the STAGED blobs, not merely the worktree:

```
$ git show :docs/reports/2026-07-26-session36-null-attack.md | grep -n 'agent-memory'
313:`/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/project_agent-type-source.md`
$ git show :docs/reports/2026-07-26-session36-agent-key-s9-control.md | grep -n 'agent-memory'
196:`.claude/agent-memory/praxis-worker/project_agent-type-source.md` records the refuted null and
$ git diff --name-only -- docs/reports/2026-07-26-session36-null-attack.md docs/reports/2026-07-26-session36-agent-key-s9-control.md
(end)                     # empty: index == worktree for both
```

### 3.3 Does the cited file still contain what the two reports attribute to it? **NO.**

Both reports say it "records the refuted null and advises 'do not propose the settings key as a way
to set `agent_type`.'" **That description is INACCURATE as of 2026-07-28.** The attributed advice is
not in the file at all:

```
$ grep -n "do not propose" .claude/agent-memory/praxis-worker/project_agent-type-source.md
grep-exit=1               # 1 = string ABSENT
$ grep -in "propose" .claude/agent-memory/praxis-worker/project_agent-type-source.md
grep-exit=1               # no occurrence of "propose" in any case
$ stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M' .claude/agent-memory/praxis-worker/project_agent-type-source.md
2026-07-26T19:17 …/project_agent-type-source.md
```

What it actually says now — frontmatter and opening, quoted verbatim (lines 2-14):

```
name: agent-type-source
description: CORRECTED — the root `agent` key in .claude/settings.json DOES set agent_type in PreToolUse payloads (CC 2.1.220), but only when the name resolves to .claude/agents/<name>.md; demonstrated in an out-of-repo lab replica, in-repo behaviour inferred; an earlier "it does nothing" null recorded here was confounded and is withdrawn
metadata:
  type: project
---

**This file previously recorded the opposite claim. That claim is REFUTED. Do not act on it.**

On Claude Code 2.1.220 (`claude --version` re-checked 2026-07-26), a root-level
`"agent": "<name>"` key in `.claude/settings.json` **does** set `agent_type` in PreToolUse hook
payloads — **but only if `<name>` resolves to an existing agent definition, e.g.
`.claude/agents/<name>.md`.**
```

And line 44-46:

```
**The old null ALSO came from an out-of-repo lab.** So does the corrected positive. The variable
that changed between them is the presence of a resolvable `.claude/agents/praxis-master.md`
— **not** lab-vs-repo. Do not read this file as "the lab was wrong, the repo is right."
```

The file was corrected in place during session 36 (mtime 2026-07-26T19:17 — later the same day the
reports were written), and `MANIFEST.md:121` already records this: "The memory derived from it … was
CORRECTED later in session 36: it now opens 'This file previously recorded the opposite claim. That
claim is REFUTED.'"

**Consequence for the defect-pointer reading:** both staged reports point at a defect that no longer
exists and describe file contents that no longer exist. The pointer is stale in *two* independent
ways — the path will not resolve for a cloner (by design, per the `.gitignore` comment), and even
locally the described content is gone. A reader cannot discover that the work item is discharged from
the reports alone; only `MANIFEST.md:121` records the discharge, and that line is UNSTAGED.
I did not edit the memory file, the reports, or the ledgers. **RECOMMENDATION only.**

---

## 4. Files written

Exactly one:

- `/Volumes/Sensidine/Praxis.build/docs/reports/2026-07-28-session40-ignore-and-citation-adversarial.md` (this report)

Nothing under `.claude/agent-memory/` was created, edited, appended to, or deleted. No `git add`,
no index operation, no checkout/reset/stash, no edits to `.gitignore`, `.claude/settings.json`,
`.claude/hooks/*`, `scripts/*`, or any other file under `docs/reports/`.

## 5. Verdict per claim

- **CLAIM 1 — HOLDS.** Reaches everything under the directory (incl. dotfiles, nesting, subdir cwd,
  absolute paths); reaches nothing else (only line 26 is behavioural, and its full match set is the
  target dir); zero tracked files inside it, at HEAD, or in any ref. Caveats O1-O3 recorded, none
  falsifying.
- **CLAIM 2 — BROKEN.** 14 files / 40 path citations outside the memory dir (+3 inside, +1 resolving
  wikilink), not 2. True only under an unstated "STAGED files only" restriction.
- **CLAIM 3 — recorded.** Both citations are (ii) DEFECT POINTERS ("Stale artifact flagged, NOT
  edited"), each carrying an embedded factual sub-claim about the file's contents. That sub-claim is
  **now false**: the attributed advice ("do not propose the settings key…") is absent; the file was
  corrected in place on 2026-07-26 and now opens "This file previously recorded the opposite claim.
  That claim is REFUTED."

VERDICT: CLAIM1=HOLDS CLAIM2=BROKEN CLAIM3=recorded
