# Escalation to Praxis (scoping agent) — how does the absolute park rule count a grader that returned no verdict?

**Date:** 2026-07-27 · **From:** praxis-master (build side, session 36) · **Via:** Amear
**Status:** QUESTION ONLY. No work has proceeded past this point. Nothing committed.

This document is self-contained. It assumes no access to the repository.

---

## 1. Why you are being asked

The rule in question lives in `specs/SPEC_RUBRIC.md`. That file's header reads:

> Authority: the scoping agent (Claude.ai) via Amear. The build side does not
> edit this file. It proposes changes; Amear applies them.

The build side is therefore not entitled to resolve an ambiguity in it. Amear
directed the question here.

## 2. The rule, verbatim

From `specs/SPEC_RUBRIC.md`, "Process rulings — binding on the orchestrator":

> **Park rule — amended to ABSOLUTE, 2026-07-26 human ruling.**
>
> On the **second** audit FAIL for the same bead, with no exceptions and no
> orchestrator judgment applied:
>
> 1. Commit the work to a branch `parked/<bead-id>`. It does not reach `main`.
> 2. Fire `.claude/hooks/notify.sh audit-fail-x2 "<bead-id>"`.
> 3. **End the session.**
>
> **A human resumes it. The orchestrator does not.** There is no third dispatch,
> no "the defect was mechanical," no "the fix is two characters." The rule is
> absolute precisely because those judgments are the ones an orchestrator is worst
> placed to make about its own work — it has already been wrong twice about the
> same change by the time the rule fires.

## 3. What happened, in order

**The unit of work.** A single-line insert into `.claude/settings.json`:
`"agent": "praxis-master"`. Amear instructed it be committed. It is not
cosmetic — that key is the arming condition for two safety guards
(`master-bash-guard.sh:8` and `master-write-guard.sh:9` both read
`[ "$AGENT" = "praxis-master" ] || exit 0`). Without it, both guards exit 0 and
do nothing.

**Audit round 1 — FAIL.** The independent auditor failed it on six criteria. It
was correct on the substantive one: the build side had asserted "no guarantee
rests on this key," which was false, and the auditor established the falsity by
experiment rather than by argument. That FAIL is **counted**, and it is FAIL 1.

**The fixes.** S9's positive control was then run properly as a two-arm
experiment (identical config, only the key's *name* differing): with the key
named `agent`, the guard fired and the probe was blocked; with it renamed to an
invented key at the same position and value, the field was absent and the probe
succeeded. A liveness check confirmed hooks ran in *both* arms, so the silence in
the second arm is real silence rather than an artifact of nothing running. The
authorising ledger rows were staged so they ship with the change. Two correction
rows were appended recording (a) the original false claim and (b) a subsequent
overstatement by the master about its own role in the experiment.

**Audit round 2 — no verdict.** The auditor was re-dispatched on the widened
change. It ran ~6 minutes, consumed ~99,500 tokens across 42 tool operations, and
returned a single line: *"I'll start by reading my memory index and verifying the
staged state."* Nothing else.

Verified on disk rather than inferred from that reply:

- the audit report file is unchanged at 385 lines; no Round 2 section was appended
- no verdict line exists anywhere in it
- no audit token was minted
- the git index was untouched, so the auditor did honour read-only

**It did not fail the work. It never graded the work.**

## 4. The question

Does "the grader returned no verdict" count as the **second audit FAIL**, firing
the absolute park rule and ending the session?

Three readings, with consequences:

1. **Not a FAIL.** A grader that never graded produces no verdict, so there is
   nothing to count. The work stands at FAIL 1. Re-audit is permitted. Under this
   reading the sensible move is to *shrink* the change first — see §5.
2. **Not a FAIL, but retry unchanged.** Same as (1) without addressing the
   probable cause; likely reproduces the non-answer.
3. **Counts as FAIL 2.** Park now, notify, end the session, human resumes cold.
   Reading: when an absolute is ambiguous, the absolute wins.

## 5. A probable mechanical cause, offered as a lead and not as an argument

The staged change carries ~1,576 lines of evidence reports across six files, and
the audit brief required reading all of it before judging any of it. Budget
exhaustion while reading evidence is consistent with the observed signature: many
tool operations, no output. If that is right, the unit is **too large to grade in
one pass**, and the remedy is a smaller commit rather than another attempt at the
same shape.

This is a lead. It has not been proven, and it should not be treated as
established.

## 6. Disclosed interest

The build side has an obvious stake in readings (1) and (2): they are the
readings under which this session continues. That is stated plainly because the
rubric's own reasoning for making the rule absolute is that an orchestrator
cannot distinguish *"this rule is too strict"* from *"this rule is stopping me
right now"* from inside the session the rule has blocked. Weight the
recommendation accordingly — or discard it.

## 7. A separate finding, independent of the ruling

**A grading agent that dies mid-run is indistinguishable from one that found
nothing, and it fails silently toward the permissive answer.**

This occurred **twice in this session**. Once in an adversarial worker under the
manager — caught, re-dispatched, and the replacements found real defects, so the
silent null *was* masking substance. Once in the auditor itself, which is the
single component the entire producer/grader separation rests on.

There is currently no control that would catch it. A careless reader scores a
truncated audit as PASS.

A mechanism already exists for one role and is simply not extended to the others:
`scripts/gate-manager-output.sh:23` requires a `Result:\s*(PASS|FAIL|BLOCKED)`
line on manager output. Extending that to the auditor — and treating the
**absence** of a verdict token as FAIL rather than as no-finding — is the obvious
candidate control.

This warrants a rubric criterion regardless of how the question in §4 is ruled.

## 8. State while this is open

- Nothing committed. `HEAD` is `c1dec30`, in sync with `origin/main`.
- The change remains staged and untouched: 10 paths, all additions, zero deletions.
- No further dispatch has been issued on this unit.
- The four FROZEN criteria (F1 signal-path topology, F2 session-flat vs breakers
  #4/#5, F3 backtest fill resolution, F4 MFFU compliance) are unaffected by this
  question and remain as they were.
