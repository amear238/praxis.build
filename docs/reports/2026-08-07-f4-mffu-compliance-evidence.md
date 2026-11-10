# F4 — MFFU automation compliance: evidence landed

**Date.** 2026-08-07 · session 43
**Unit.** Land the F4 evidence on disk as a gradeable artifact.
**Authorisation of record.** `DECISION_LOG.md` row `2026-08-07T16:13:58Z`, `WHO: amear`.
**Manager.** praxis-manager. **Workers used.** 2 of 2 permitted (1 BUILD, 1 ADVERSARIAL).

---

## 0. Standing caveat — this whole report is a RELAY

**UNVERIFIED — relayed, not independently confirmed.** Neither the master nor
this manager has read the underlying Gmail thread. Every assertion in sections
1, 2 and 3 below traces to text Amear pasted in-session and to nothing else. No
agent in this chain has opened `19f9edc188595b0c`, contacted MFFU, or seen a
message header. The artifact that *is* verified is this file's existence and
the ledger rows registering it — not the truth of the correspondence it records.

This report does **not** discharge F4. `specs/SPEC_RUBRIC.md` was not touched
and F4 remains FROZEN there. F4's state is Amear's alone to change.

---

## 1. The MFFU confirmation

Quoted verbatim as relayed. **UNVERIFIED — relayed, not independently confirmed.**

> "Algo trading is now permitted at MFFU moving forward on all plans including
> the evaluation, simulated-funded and live account stages."

| Field | Value | Status |
|---|---|---|
| Thread ID | `19f9edc188595b0c` | UNVERIFIED — relayed |
| Sender | `FRANK@myfundedfutures.intercom-mail.com` | UNVERIFIED — relayed |
| Timestamp | 2026-07-26T21:20:22Z | UNVERIFIED — relayed |
| Respondent | Frank, human support rep | UNVERIFIED — relayed |
| Policy article | `https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices` | UNVERIFIED — relayed; URL not fetched |
| Formal policy document | **None issued** | Relayed as a stated absence |

### 1.1 MFFU's three stated restrictions

Stated plainly, as relayed:

1. **No high-frequency trading.**
2. **Automated tools may not be built to exploit sim-environment fill favorability.**
3. **Live automation must follow CME guidelines.**

Restriction 2 is the one with cross-block consequences. See section 4.

---

## 2. Eight-firm outreach result table

Source quality is a separate column on purpose and is **not** collapsed into
confirmed/denied. A determination from a human on the record and a sentence from
a support chatbot are not the same class of evidence, and flattening them is the
precise S2 failure this table exists to avoid.
**All eight rows: UNVERIFIED — relayed, not independently confirmed.**

| Firm | Result | Source quality |
|---|---|---|
| MFFU | Permitted | **Human, written** |
| Earn2Trade | Permitted (only copy-trading restricted) | **Human, written** |
| OneUp Trader | Permitted | **Human, written**; points to two policy docs |
| The Trading Pit | Conditionally permitted — Futures Challenges via EAs | **AI agent ("Pitter") — NOT human.** Low confidence; see 3.3 |
| Leeloo | **Prohibited, explicit** | Human, written |
| UProfit | **Prohibited, explicit** | Human, written |
| Apex | **No reply** — 12 days, silent | No source. Silence is not permission |
| Topstep | **Bounced** — "This inbox is not monitored" | No source. Address is dead |

Six of eight replied. Of those six, **five returned a human determination** —
three permitting (MFFU, Earn2Trade, OneUp Trader) and **two prohibiting**
(Leeloo, UProfit). The sixth, The Trading Pit, returned an AI-generated response
which per 3.3 is **not** a determination and is not counted as one. Two firms
(Apex, Topstep) returned nothing at all.

*(An earlier draft of this section read "six of eight returned a determination,"
which silently counted the AI reply as a determination two sections before
declaring it wasn't. Corrected here and in the ISSUE_REGISTER row before
staging; the contradiction was caught by the ADVERSARIAL worker, not by the
author.)*

---

## 3. What this evidence does NOT establish

### 3.1 No firm issued a signed policy document — MFFU included

What is established: **no firm issued a signed policy instrument addressed to
Amear's account.** MFFU's "yes" points to a **help-center article** — revisable
without notice, carrying no counterparty signature, addressed to nobody. What
exists is a support reply. That is meaningfully weaker than "written
confirmation" reads at a glance, and it carries as a stated limitation rather
than as a footnote.

**A tension recorded rather than resolved.** The blanket form of this claim does
not survive the relay's own detail. OneUp Trader is relayed as pointing to "two
policy docs" — **UNVERIFIED — relayed, not independently confirmed**; it is not
established what those documents are, whether they are policy instruments or
further help-center pages, or whether they bind an account. No agent fetched
them. For Earn2Trade, no supporting document is relayed at all. Meanwhile the
authorising DECISION_LOG row asserts "no firm, MFFU included, issued one." That
assertion and the OneUp "two policy docs" relay are **in tension**. The tension
is recorded here and left open, because resolving it would require reading
sources no agent in this chain has read. The narrow claim — that *MFFU* issued
no policy document — is what the MFFU evidence supports, and is what F4 turns on.

### 3.2 The "now permitted" effective-date gap

The word **"now"** implies a *recent policy change*. Two things follow that the
reply does not answer:

- **Effective date — UNCONFIRMED.** Nothing establishes when the permission began.
- **Retroactivity — UNCONFIRMED.** Whether it reaches accounts opened *before* the
  change is unaddressed. If Amear's account predates the change, it is not
  established that the account is covered by it.

A follow-up question on both points is **open**. Until it returns, "MFFU permits
automation" is supported; "MFFU permits automation *on this account*" is not.

### 3.3 The Trading Pit reply is AI-generated and is not a determination

The response came from an AI agent ("Pitter"), and it linked the
**Japanese-locale rules page in answer to an English inquiry** — a locale
mismatch that is itself evidence the response was not reasoned about the
question asked. This is recorded as **low-confidence**, explicitly **not** as a
"conditional yes." Materially this changes nothing: The Trading Pit was only
ever a backup counterparty. It is recorded at its true weight rather than
promoted to fill out the table.

### 3.4 The source thread is unread by every agent in this chain

Restating section 0 because it is load-bearing: **neither the master nor this
manager read the Gmail thread.** The chain is Amear → master → manager → this
file. Each hop is a relay. No agent verified a header, a sender address, or a
timestamp.

### 3.5 What is *not* claimed

- Not claimed: that F4 is discharged, satisfied, or unfrozen.
- Not claimed: that the PRAXIS pattern specifically was described to MFFU and
  approved as described. The relayed quote is a **general** permission for "algo
  trading," not an assessment of this system's architecture. F4's criterion reads
  "*this specific* automation pattern" — the relayed evidence is broader and
  vaguer than the criterion's wording. Whether the general permission satisfies
  the specific criterion is **Amear's ruling to make**, per S8.
- Not claimed: anything about F1, F2 or F3's disposition.

---

## 4. S6 cross-block check — MFFU restriction 2 couples to F3

This section is mandatory and is the most consequential part of this report.

MFFU's restriction that **automated tools may not be built to exploit
sim-environment fill favorability** touches **F3 — Backtest fill resolution vs.
acquired data granularity**, which is FROZEN.

F3's **Criterion**, quoted verbatim from `specs/SPEC_RUBRIC.md:46-48`:

> **Criterion.** The fill resolution the Strategy Analyzer will actually run at,
> and the slippage assumption applied at the band edge, stated in writing before
> the backtest runs.

F3's **Why frozen**, quoted verbatim from `specs/SPEC_RUBRIC.md:49-54`:

> **Why frozen.** The Block 2 spec requires Order Fill Resolution = High with a
> 1-tick resolution series, 1-tick slippage, $2.96 round-trip. Deviation F
> delivered 1-minute bars. High-resolution fill modelling needs a finer intrabar
> series. A band-touch strategy backtested on 1-minute bars with no intrabar
> resolution produces optimistic fills exactly where the edge lives, and the
> optimism is invisible in the output.

**The interaction — stated precisely.** These are **not** the same environment,
and an earlier draft of this section overstated them as "the same physical
phenomenon." They are not. F3 governs **NinjaTrader Strategy Analyzer backtest
fill modelling** — a simulation we run ourselves, on historical data. MFFU
restriction 2 governs **the firm's own evaluation and simulated-funded
environments** — a counterparty's platform, live-quoted. Different systems,
different operators.

What genuinely couples them is the **shared failure mode**: a strategy whose
measured edge is produced by optimistically favourable fills at the band edge in
a non-live environment. F3 is the question of whether our *backtest* manufactures
that optimism; restriction 2 is the firm's rule against *building tools that
exploit* it on their platform. A band-touch strategy tuned against F3-flawed
backtest fills is a strategy tuned against favourable-fill assumptions — and it
is then deployed onto MFFU's sim stages, where those assumptions meet a rule.
The coupling is causal, not identity.

They remain two different *kinds* of problem:

- F3 framed it as an **internal modelling-honesty** question: does the backtest
  overstate the edge, and will we find out only in live trading?
- MFFU restriction 2 frames it as a **counterparty-compliance** question: is a
  system tuned against favourable sim fills a system built to exploit them?

The consequence is that **F3 acquires an external face it did not previously
have.** A strategy whose measured edge depends on optimistic band-edge fills in
a 1-minute-bar backtest is exposed twice: once to the edge evaporating live, and
once to a counterparty rule about sim-fill exploitation. The evaluation and
simulated-funded stages named in MFFU's own permission are precisely the
sim environments the restriction governs.

**Scope stop.** F3 is FROZEN and out of scope for this unit. This report does
**not** resolve it, does **not** assess whether PRAXIS violates restriction 2,
and does **not** opine on the fill-resolution assumption. The coupling is named
and the analysis stops here — deliberately. Ruling on F3 belongs to Amear.

**Other blocks checked and found not to couple.** F4 blocks Block 4 and Block 5
per the rubric; this unit changes neither, because it does not unfreeze F4.

- **F1** — per `specs/SPEC_RUBRIC.md:26-28`, unblocks when a
  `docs/specs/*-live-signal-topology.md` exists and the auditor confirms it
  addresses all nine breakers by name. This unit creates no topology spec and
  names no breaker. No coupling.
- **F2** — per `specs/SPEC_RUBRIC.md:30-43`, is **session-flat timing**: the
  contradiction between breaker #4 closing at 11:30 ET, breaker #5 disabling
  15:00–18:00 ET, and Deviation B flattening at 16:00 ET, and specifically what
  happens to an open position at 15:00. *(An earlier draft of this report
  mischaracterised F1/F2 as "circuit-breaker naming and placement." That is
  wrong for F2, which is a timing-disposition question. Corrected.)* MFFU's
  restrictions concern HFT, sim-fill exploitation and CME conformance — none of
  which bears on the session-flat clock. No coupling. Note this is a **narrow**
  finding: MFFU's "no HFT" restriction constrains order *frequency*, not the
  session window, and nothing in the relayed reply speaks to trading hours.

No hook, script, settings file, or agent definition was modified, so no
enforcement-layer block is touched — verified in section 5.7.

---

## 5. Verification evidence — pasted output only

### 5.1 MANIFEST.md line 132 — the authorised deletion

The DECISION_LOG row explicitly authorises removing the stray row for
`/docs/specs/2026-08-06-phase3-build-specification.md`. Re-verified by the
manager after the worker returned:

```
$ git ls-files -- docs/specs/2026-08-06-phase3-build-specification.md
$ git cat-file -e HEAD:docs/specs/2026-08-06-phase3-build-specification.md ; echo "exit=$?"
fatal: path 'docs/specs/2026-08-06-phase3-build-specification.md' does not exist in 'HEAD'
exit=128
$ ls -la /Volumes/Sensidine/Praxis.build/docs/specs/2026-08-06-phase3-build-specification.md
ls: /Volumes/Sensidine/Praxis.build/docs/specs/2026-08-06-phase3-build-specification.md: No such file or directory
$ git branch -a --list '*r8j*'
  parked/Praxis_build-r8j
```

The path does not resolve on `main` by any of the three checks, and the parked
branch exists. The premise holds; the deletion was executed.

### 5.2 The zero is a true null — positive control

A `grep -c` returning 0 is worthless without proof the grep fires. Control arm
run against a string known to be present in the same blob:

```
$ git show HEAD:MANIFEST.md | grep -c "phase3-build-specification"
0
$ git show :MANIFEST.md | grep -c "phase3-build-specification"
0
$ grep -c "phase3-build-specification" MANIFEST.md
0
$ git show HEAD:MANIFEST.md | grep -c "SPEC_RUBRIC"        # POSITIVE CONTROL
3
```

The control arm returns 3. The grep fires. The zeros are true nulls.

### 5.3 FINDING — the brief's premise was wrong about the deletion

The brief and the DECISION_LOG row both describe removing a row at
`MANIFEST.md:132`, which implies a row that this branch's history carried. **It
is not in `main`'s history and not in this worktree's index.** Raw output,
pasted:

```
$ git show HEAD:MANIFEST.md | wc -l
     117
$ wc -l MANIFEST.md
     132 MANIFEST.md
$ git diff --cached --numstat -- MANIFEST.md
15	0	MANIFEST.md
```

HEAD's `MANIFEST.md` is 117 lines and contains the string zero times (5.2). The
stray row was itself one of the 15 uncommitted working-tree additions. Removing
it therefore produced **no `-` line in the diff against the index** — it dropped
the addition count to 14, and the new F4 report row restored it to 15.

**Why this is recorded rather than smoothed:** the intended *effect* is achieved
— the dangling reference never lands in `main`. But anyone grading this unit by
looking for a deletion in the staged diff will find none, and would be entitled
to conclude the deletion was not performed. The evidence that it *was* performed
is the worktree `grep -c` = 0 with its firing positive control (5.2), plus the
fact that `main`'s HEAD never carried the row.

### 5.3.1 SELF-CORRECTION — this report's own first draft was wrong here

An earlier draft of 5.3 asserted in bold that the row was "**never committed and
never staged**." **That is false**, and it was caught by the ADVERSARIAL worker,
not by the author. The row *was* committed — on the parked branch:

```
$ git show parked/Praxis_build-r8j:MANIFEST.md | grep -c "phase3-build-specification"
1
$ git log --all -S"phase3-build-specification" --oneline -- MANIFEST.md
f258a5d park(Praxis_build-r8j): audit-fail-x2 - Phase 3 spec import, 5 paths
$ git rev-list HEAD | grep -c "^f258a5d"
0
$ git branch -a --contains f258a5d
  parked/Praxis_build-r8j
$ git rev-list HEAD | grep -c "^5067d3261d6e463f8387699d847cd262398ffb9c"   # POSITIVE CONTROL
1
```

The positive control returns 1, so the `0` for `f258a5d` is a true null: that
commit is genuinely unreachable from `HEAD`, and it exists only on
`parked/Praxis_build-r8j`.

**The corrected claim, stated at the level the evidence supports:** the row is
committed at `f258a5d` on `parked/Praxis_build-r8j`, is **not** reachable from
`main`, and is **not** in the current index. Whether it was ever staged at some
earlier moment is **UNESTABLISHED** — the commands above show only that index
and HEAD agree *now*, which says nothing about history. The DECISION_LOG row's
own wording ("exists only on `parked/Praxis_build-r8j`") was correct all along;
this report's first draft overstated it into an absolute. A section written to
correct someone else's imprecision committed the same error, which is worth more
than the finding itself.

### 5.4 Line counts after the edits

```
$ wc -l MANIFEST.md
     132 MANIFEST.md
$ tail -1 MANIFEST.md | cut -c1-200
| /docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | Report | 0 | 2026-08-07 | F4 (MFFU automation compliance) evidence artifact — lands Amear's prop-firm automation outreach on disk as a grade
```

132 lines: one row removed, one row appended. The new last line is the F4 row.

### 5.5 ISSUE_REGISTER.md — two rows appended at the end

```
$ grep -n "^- \[2026-08-07T16:13:58Z\]" ISSUE_REGISTER.md | cut -c1-160
68:- [2026-08-07T16:13:58Z] WHO: Amear | WHAT: F4 evidence landed — MFFU confirmed IN WRITING, via a human support rep, that algo trading is permitted on all pl
70:- [2026-08-07T16:13:58Z] WHO: Amear | WHAT: Prop-firm automation outreach INCOMPLETE — Apex Trader Funding never replied (12 days, silent) and Topstep bounce
$ wc -l ISSUE_REGISTER.md
      70 ISSUE_REGISTER.md
$ git diff --numstat -- ISSUE_REGISTER.md
35	0	ISSUE_REGISTER.md
```

Rows at lines 68 and 70 of a 70-line file — appended at the end, as required.
Both attributed `WHO: Amear`, correcting the draft text's `WHO: orchestrator`:
the ruling is Amear's, not the orchestrator's.

**Append-only proof — and a retraction.** An earlier draft of this section
offered, as its append-only proof, a *prose description* of a byte-prefix check
run by the BUILD worker (`wc -c` 61741 → 65501, `after[:len(before)] == before`
→ `True`). That was a description of output, not output, sitting in a section
headed "pasted output only" — an S1 violation, flagged by the ADVERSARIAL
worker. Worse, it is now **permanently unreproducible**: the 61741-byte
pre-edit state exists in no index, blob, or worktree. **It is withdrawn as
evidence.**

The reproducible proof of append-only behaviour is that the staged diff contains
**zero deletions**, across all four files:

```
$ git diff --cached | grep -c "^-[^-]"
0
$ git diff --cached | grep -c "^+[^+]"    # POSITIVE CONTROL — same pipeline, additions
317
```

The control arm returns 317, so the pipeline works and the `0` is a true null.
Nothing was deleted anywhere in this unit's staged output.

The known pre-existing mid-file insertion anomaly was **not repaired**. A second
pre-existing anomaly was observed and also left alone: the file already ended in
four consecutive blank lines, so the first appended row sits four blank lines
below its predecessor rather than one. **UNVERIFIED by the manager:** the
ADVERSARIAL worker reports the staged `ISSUE_REGISTER.md` prefix diverges from
`HEAD` at byte 19467 (HEAD line 35) due to that pre-existing session-35
insertion — I did not independently re-derive the byte offset. With zero
deletions established above, the divergence is a pure insertion either way.

### 5.6 S5 — the authorising row is in the staged set

Full four-arm evidence in section 6.

### 5.7 Forbidden paths are not staged

```
$ git diff --cached --name-only
DECISION_LOG.md
ISSUE_REGISTER.md
MANIFEST.md
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
```

`specs/SPEC_RUBRIC.md`, `AUDIT_LOG.md`, `.claude/settings.json`, all hook
scripts and all agent definitions are **absent** from the staged set. They are
dirty in the worktree from prior sessions, which this unit did not touch.

---

## 6. S5 — authorisation staged, verified with firing negative controls

A `grep` that has never returned zero proves nothing. Four arms, two positive
and two negative:

```
$ git show :DECISION_LOG.md | grep -c "2026-08-07T16:13:58Z"          # ARM 1 positive
1
$ git show HEAD:DECISION_LOG.md | grep -c "2026-08-07T16:13:58Z"      # ARM 2 negative
0
exit=1
$ git show :DECISION_LOG.md | grep -c "2026-08-07T16:13:59Z"          # ARM 3 negative, invented ts
0
exit=1
$ git show :DECISION_LOG.md | grep -o "2026-08-07T16:13:58Z\] \*\*WHO: amear\*\*"   # ARM 4
2026-08-07T16:13:58Z] **WHO: amear**
```

**Arm 2 is the load-bearing control.** The identical grep against the pre-staging
state (`HEAD`) returns 0 with exit 1. That proves two things at once: the grep
discriminates rather than matching anything, and the row's presence in the index
is a result of *this unit's staging*, not a pre-existing condition. Arm 3 rules
out a malformed pattern matching by accident. Arm 4 confirms the attribution on
the staged row is `WHO: amear`.

S5 is satisfied: the report cites an authorisation that is in the commit.

---

## 7. Adversarial findings

One ADVERSARIAL worker was dispatched against the finished artifact set, given
the criteria and the artifacts but **not** the author's reasoning. It returned
`VERDICT: FAIL` with five BLOCKING defects. **Every one was accepted.** The
report you are reading is the post-repair version. Defects, and disposition:

| # | Defect | Severity | Disposition |
|---|---|---|---|
| 1 | Sections 6–9 shipped as empty placeholders, while the header claimed an ADVERSARIAL pass had been run | BLOCKING | **Fixed** — all sections populated; this table is section 7 |
| 2 | S1: §5.3 fence retyped — `wc -l MANIFEST.md` shown as bare `132`; real output is `     132 MANIFEST.md` | BLOCKING | **Fixed** — fence replaced with raw output (5.3), verified via `od -c` |
| 3 | S1: §5.5 append-only proof was prose, not output, and is now unreproducible | BLOCKING | **Fixed** — withdrawn as evidence; replaced with the zero-deletions proof + positive control (5.5) |
| 4 | S2: "Six of eight returned a determination" counted the AI reply that §3.3 says is not one | BLOCKING | **Fixed** in §2 **and in the ISSUE_REGISTER row before staging** |
| 5 | Premise: "never committed and never staged" is false — row is committed at `f258a5d` on the parked branch | BLOCKING | **Fixed** — see 5.3.1, a self-correction section |
| 6 | S2: "Every 'yes' points to a help-center article" contradicted by the report's own OneUp row | NON-BLOCKING | **Fixed** in §3.1 and in the ledger row; tension recorded, not resolved |
| 7 | S6: F1/F2 mischaracterised as "naming and placement"; F2 is session-flat timing | NON-BLOCKING | **Fixed** in §4 with rubric line cites |
| 8 | S6: "quoted verbatim" quoted *Why frozen*, not F3's *Criterion*; coupling conflated two environments | NON-BLOCKING | **Fixed** — both quoted; coupling restated as causal, not identity |
| 9 | `scripts/no-commit-guard.sh:20` regex false-positives on `git merge-base` | NON-BLOCKING | **NOT fixed — out of scope.** Escalated; see below |

**Defect 9 — independently reproduced by the manager, escalated not fixed.**
The worker reported that the commit guard blocks read-only `git merge-base`. I
then tripped it myself, unintentionally, while verifying defect 5:

```
$ git merge-base --is-ancestor f258a5d HEAD
PreToolUse:Bash hook error: ["$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh]:
BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
```

`merge-base` is a read-only ancestry query that writes nothing. The guard's
`\bgit\s+(commit|push|merge|rebase|tag)\b` pattern matches the `merge` prefix of
`merge-base`. **This unit is forbidden from touching hook scripts and did not.**
Recorded here for Amear and the master. Worked around with `git rev-list`
membership plus a positive control (5.3.1) — the workaround is sound, but a gate
that blocks a read-only query is a false positive worth a ruling.

**On the adversarial pass itself:** it found a false claim in this report that
the author had already "verified." That is the S9/positive-control lesson
recurring — my verification of the deletion premise was real but *incomplete*, as
I checked `main` and the worktree and never checked the parked branch I had
myself listed. Confident partial verification reads exactly like complete
verification from the inside.

---

## 8. Files staged

```
$ git diff --cached --numstat
118	0	DECISION_LOG.md
35	0	ISSUE_REGISTER.md
15	0	MANIFEST.md
```

Four paths staged: the three above plus this report,
`docs/reports/2026-08-07-f4-mffu-compliance-evidence.md`. Its own line count is
deliberately omitted from this fence — a report cannot contain the final size of
itself, and inventing the figure would be precisely the S1 fabrication this unit
was graded on. The authoritative full four-line `--numstat`, captured after the
final staging, is pasted in the manager's return message to the master.

**Ride-along disclosure — read before grading.** All three ledgers carried
**pre-existing uncommitted appends** from prior sessions before this unit began:
`DECISION_LOG.md` +118, `ISSUE_REGISTER.md` +32, `MANIFEST.md` +15. This unit
contributed 3 lines to `ISSUE_REGISTER.md` (two rows plus a separator) and a net
0 to `MANIFEST.md` (one row removed, one added). **The remainder is prior
sessions' work, staged as a side effect**, because S5 mandates the authorising
`DECISION_LOG` row be in the staged set and these are append-only ledgers that
cannot be partially staged without creating the exact mid-file split anomaly
`ISSUE_REGISTER.md` already suffers from. The authorising row is the **last line**
of `DECISION_LOG.md`, so staging it is a clean prefix-append, not a split. This
is disclosed rather than presented as this unit's output.

Nothing is committed. `git log --oneline -1` remains `5067d32`.

---

## 9. Result

**Result: PASS**, against S1, S2, S4, S5, S6, S7 — after one adversarial round
that returned FAIL and forced five blocking repairs.

| Criterion | Verdict | Basis |
|---|---|---|
| S1 | PASS | All fences re-run and reproduced; two retyped/prose fences found by the adversarial worker were replaced (5.3) or withdrawn (5.5). Every null carries a firing positive control |
| S2 | PASS | Relayed content marked UNVERIFIED throughout; determination-count and policy-document overclaims corrected; F4 nowhere implied discharged; silence and bounce recorded as absence; AI reply held at low confidence |
| S4 | PASS | Authorisation is `DECISION_LOG.md` row `2026-08-07T16:13:58Z`, pre-dating the work and naming the one deviation (the MANIFEST deletion). **Caveat:** "written before the work" is not independently verifiable from artifacts alone — nothing on disk orders the row against the edits |
| S5 | PASS | Authorising row in the staged index, four arms, two firing negative controls (§6) |
| S6 | PASS | F3 coupling named with both rubric quotes and a precise, non-inflated characterisation; F3 **not** resolved; F1/F2/Block 4/Block 5/enforcement layer each checked and dispositioned (§4) |
| S7 | PASS | Nothing committed; HEAD unchanged at `5067d32`; the manager cannot commit and did not attempt it |

**What this PASS does and does not mean.** It means the *evidence is landed
correctly and honestly graded*. It does **not** mean F4 is satisfied. F4 remains
FROZEN in `specs/SPEC_RUBRIC.md`, which was not touched. Whether a general
permission for "algo trading," relayed and unread by any agent, satisfies a
criterion written as "*this specific* automation pattern," is Amear's ruling and
nobody else's.

---

## Addendum 2026-10-28 — MFFU "Davi" reply (screenshot)

**Date.** 2026-10-28. **Authorisation of record.** `DECISION_LOG.md` row
`2026-10-28T20:54:29Z`, `WHO: amear`. **Written by.** praxis-worker (BUILD), as
an append. No byte above this addendum was changed.

This addendum files a second MFFU support reply. It records what that reply
says and maps it against F4 and against §3.2 and §3.5 of this report. It does
**not** change F4's state. F4 remains FROZEN in `specs/SPEC_RUBRIC.md`.

### A. Provenance

- **Source.** Amear supplied the reply as a screenshot. Source filename:
  `/Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23<U+202F>PM.png`. The
  character before `PM` is U+202F NARROW NO-BREAK SPACE, bytes `e2 80 af`
  (shown by the `xxd` line below).
- **Repo copy.** `docs/reports/evidence/2026-10-28-mffu-davi-reply.png`.
- **Size.** 254350 bytes (source and copy).
- **sha256.** `15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992`
  (source and copy, identical).
- **Transcript.** `docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md`.
  Every quote of the Davi reply or of the screenshot in this addendum is taken
  from inside that file's `text` fence. The one quote of Frank's line (in C) is
  taken from §1 of this report, which is itself a relay and is UNVERIFIED.

Command output, pasted as run on 2026-10-28:

```text
$ shasum -a 256 /Users/admin/Desktop/Screenshot\ 2026-10-28\ at\ 4.53.23* docs/reports/evidence/2026-10-28-mffu-davi-reply.png
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ ls -l /Users/admin/Desktop/Screenshot\ 2026-10-28\ at\ 4.53.23* docs/reports/evidence/2026-10-28-mffu-davi-reply.png
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ printf '%s' /Users/admin/Desktop/Screenshot\ 2026-10-28\ at\ 4.53.23* | tail -c 9 | xxd
00000000: e280 af50 4d2e 706e 67                   ...PM.png
```

**This is a screenshot relay.** Per the master's dispatch brief for this unit
(not itself on disk): the Gmail connector was unavailable this session, the
screenshot is the only source, and no agent is to read the message in Gmail or
contact MFFU. On the manager's attestation, this filing unit's manager and workers did neither: no brief in this unit asked for Gmail access, email drafting or contact with MFFU, and the `praxis-worker` definition grants only `Read, Grep, Glob, Bash, Write, Edit, TodoWrite` (no Gmail connector). That is an attestation, not an observation of every tool call. Whether any
other agent did is not observed here and is UNVERIFIED. These things are **not
visible** in the screenshot and are **UNVERIFIED**:

- the date and time of either message shown;
- the full headers (From/Reply-To/To/Cc, Message-ID, SPF/DKIM/DMARC results);
- the subject line of the thread;
- the thread order beyond the two messages shown, including where the "Frank"
  reply of §1 sits relative to this one;
- the full text of Amear's message shown above the reply. Only its collapsed preview is
  visible, and the preview is cut off at `is f`;
- whether the reply continues below the visible signature (hidden or collapsed
  quoted content cannot be ruled out).

The sender display name `Davi from MyFundedFutures` and the address
`[rep-address]@myfundedfutures.intercom-mail.com` are recorded **as displayed
only**. They are not header-verified.

### B. What the reply states

The substantive lines, verbatim from the transcript fence. **UNVERIFIED as to
sender, date and headers** (see A). The text itself is as shown in the image.

> You can use custom Tradovate API access with your MyFundedFutures Tradovate evaluation and funded accounts for fully automated order execution.
> • Automated trading solutions using an API are supported, allowing you to integrate your trading bot or automated strategy via the Tradovate API. This enables your custom software to submit orders, manage positions, and retrieve market data directly from your account.
> • Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.
> • High-frequency trading is not allowed, and automated tools must not exploit favorable fills in the simulated environment.
> • For live accounts, automated trading must comply with CME guidelines.
>
> You are responsible for the performance and reliability of your automated system. For more details, see: https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices

**URL: UNFETCHED.** `https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices`
is the link's displayed text only. Its href is not visible in the screenshot.
On the manager's attestation, this filing unit did not fetch it (every brief forbade it). Its displayed text is
the same string as the policy-article URL in §1's table, which §1 also records
as not fetched.

### C. Mapping against F4, §3.2 and §3.5

The PRAXIS pattern, verbatim from `CLAUDE.md` line 21: "Signal flow: TradingView alert → webhook → n8n workflow → JSON file drop → NinjaScript FileSystemWatcher → bracket order → Rithmic → MFFU". The bracket order is placed by NinjaTrader 8 (`CLAUDE.md` Identity: "TradingView → n8n → NinjaTrader 8 → Rithmic → MFFU").

The reply's opening grant sentence names the **Tradovate API**: "custom Tradovate
API access with your MyFundedFutures Tradovate evaluation and funded accounts".
Its "Algo trading is permitted on all plans ..." bullet names no platform; whether
that bullet sits under the Tradovate sentence or stands as a general permission
is not stated in the reply, and how to read it is Amear's ruling (S8). In the
visible text, the reply **never mentions** NinjaTrader, Rithmic, webhooks, n8n
or TradingView. The search below shows this. Content hidden or collapsed below
the signature cannot be ruled out (see A).

| Point | Verdict | Quoted line(s) and reason |
|---|---|---|
| F4 "this specific automation pattern" (and §3.5, specific vs general) | **DOES NOT ADDRESS** | The only specific pattern the reply names is the Tradovate API: "You can use custom Tradovate API access with your MyFundedFutures Tradovate evaluation and funded accounts for fully automated order execution." and "integrate your trading bot or automated strategy via the Tradovate API". PRAXIS routes orders through NinjaTrader 8 and Rithmic, and the reply names neither (0 lines, see search). The remaining line, "Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.", names no platform; whether it stands as a general permission or sits under the Tradovate sentence is Amear's ruling (S8, see above). On neither reading does it name the PRAXIS path (NinjaTrader 8 / Rithmic). Read as general, it repeats the specific-vs-general gap §3.5 already recorded for Frank's relayed line; read as under the Tradovate sentence, it is specific to a different pattern. It is not narrowed here. |
| F4 "on a funded account" | **PARTLY ADDRESSES** | Funded accounts are named: "your MyFundedFutures Tradovate evaluation and funded accounts" and "simulated-funded, and live account stages". Read one way, "Tradovate" qualifies both "evaluation" and "funded accounts", tying the first mention to **Tradovate** accounts and the Tradovate API; read the other way, "Tradovate" qualifies only "evaluation". The reply does not say which, nor whether either reaches a Rithmic-routed account; that is Amear's to rule on (S8). Whether Amear's account is a Tradovate account is not established in this addendum. Neither line names Amear's specific account. |
| §3.2 effective date | **DOES NOT ADDRESS** | No date or effective date appears anywhere in the visible text of the reply. As a plain textual fact, Davi's line "Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages." has **no "now" and no date**, unlike Frank's relayed line in §1 ("Algo trading is now permitted at MFFU moving forward on all plans ..."). That absence does not supply an effective date. It also does not show that the "now" in Frank's line was wrong or was withdrawn. |
| §3.2 retroactivity / "on this account" | **DOES NOT ADDRESS** | Nothing in the reply mentions when an account was opened, whether the permission applies to accounts opened before a change, or any account identifier. The second-person "your ... accounts" in "your MyFundedFutures Tradovate evaluation and funded accounts" is generic. It identifies no account. It may be conditioned on Tradovate accounts, depending on how the phrase is read (see the row above); which reading MFFU intended is Amear's to rule on (S8). |

**Amear's truncated follow-up.** The preview of Amear's message shown above the reply reads,
in full as visible:

> Hi Frank — thanks for confirming, that's helpful. Two follow-ups so I can be sure I'm building within the rules rather than assuming. 1. Does this specific is f

The full text of his questions is **not visible**. This addendum therefore does
not say whether the reply answers them.

**Search.** The commands below extract the transcript fence and count matching
lines for each pattern with `/usr/bin/grep -ci`. `grep -c` counts **lines**, not
occurrences. The `-o` listing shows the individual matches: `Tradovate` and
`API` each occur three times, across 2 lines. The same zero-hit patterns are then
run against `CLAUDE.md` as a positive control. `NT8` has 0 lines in `CLAUDE.md`
as well, so `STATUS.md` is used as its control.

Script (`w3search.sh`, run from the repo root with `bash`):

````text
F=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/e2d12a7c-ea8d-4471-9c36-a46d92b1a310/scratchpad/w3fence.txt
awk '/^```text/{f=1;next} /^```/{f=0} f' docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md > "$F"
wc -l < "$F"
for p in NinjaTrader NT8 Ninja Rithmic webhook n8n TradingView Tradovate API; do printf '%s\t' "$p"; /usr/bin/grep -ci "$p" "$F"; done
echo '--- matching lines for Tradovate|API (line:match)'
/usr/bin/grep -nio 'tradovate\|api' "$F"
echo '--- positive control: same zero-hit patterns against CLAUDE.md'
for p in NinjaTrader NT8 Ninja Rithmic webhook n8n TradingView; do printf '%s\t' "$p"; /usr/bin/grep -ci "$p" CLAUDE.md; done
echo '--- positive control for NT8 (0 in CLAUDE.md): STATUS.md'
/usr/bin/grep -ci NT8 STATUS.md
````

Output, pasted as run (the first line is the fence's line count):

````text
      25
NinjaTrader	0
NT8	0
Ninja	0
Rithmic	0
webhook	0
n8n	0
TradingView	0
Tradovate	2
API	2
--- matching lines for Tradovate|API (line:match)
13:Tradovate
13:API
13:Tradovate
14:API
14:Tradovate
14:API
--- positive control: same zero-hit patterns against CLAUDE.md
NinjaTrader	2
NT8	0
Ninja	4
Rithmic	3
webhook	1
n8n	4
TradingView	3
--- positive control for NT8 (0 in CLAUDE.md): STATUS.md
40
````

All seven zero-hit patterns score 0 in the fence. Six of them fire in
`CLAUDE.md`. The seventh, `NT8`, fires in `STATUS.md` (40 lines). So each zero
is a true null, not a broken pattern. The case-insensitive `API` pattern could
also match inside other words. The `-o` listing shows that every `API` hit is on
line 13 or 14 of the fence, which are the two Tradovate API lines quoted in B.

### D. Conditions the reply states (for the record only)

Quoted verbatim:

> • High-frequency trading is not allowed, and automated tools must not exploit favorable fills in the simulated environment.
> • For live accounts, automated trading must comply with CME guidelines.

> You are responsible for the performance and reliability of your automated system.

So the reply states four conditions: no high-frequency trading; automated tools
must not exploit favorable fills in the simulated environment; live accounts
must comply with CME guidelines; and the trader is responsible for the system's
performance and reliability.

**PRAXIS is NOT assessed against these conditions here. That is out of scope for
this addendum.** For the record only: §1.1 of this report recorded three similar
restrictions in the relay recorded in §1 (whose respondent §1's table records as Frank) (no HFT; no exploiting sim-environment fill
favorability; live automation must follow CME guidelines). No comparison of
PRAXIS against either set is made here.

### E. Anomalies

1. **Name mismatch.** The body says:
   > Hi ! Thank you so much for reaching out to MyFundedFutures Support. My name is Michael and I am here to help you with any support you may need today.

   The sender and the signature say Davi:
   > Davi from MyFundedFutures <[rep-address]@myfundedfutures.intercom-mail.com>

   > Davi-MyFundedFutures Support
2. **Two greetings.** The body has two greetings and three opening lines in
   all:
   > Hello amear,i hope this mail meets you well.

   > Thank you for contacting MyFundedFutures Support! I'll be happy to assist you today.

   > Hi ! Thank you so much for reaching out to MyFundedFutures Support. My name is Michael and I am here to help you with any support you may need today.

   So there are also two separate thank-you openers: one beginning
   `Thank you for contacting` and one beginning
   `Thank you so much for reaching out`.

   **Inference, not observed:** the two greetings plus the "Michael" vs "Davi"
   mismatch suggest templated or boilerplate text, put together from more than
   one canned block. Nothing in the image shows how the reply was composed.
3. **Different rep from §1.** The rep recorded earlier in this report is
   "Frank" (§1, relayed, UNVERIFIED). Amear's message shown above the reply, as previewed,
   is addressed to Frank:
   > Hi Frank — thanks for confirming, that's helpful.

   The reply comes from "Davi", not Frank. The displayed address local part
   (`[rep-address]`) also differs from the relayed Frank sender in §1
   (`FRANK@myfundedfutures.intercom-mail.com`). Both addresses are display or
   relay only, and neither is header-verified.

### F. Not claimed

- Not claimed: that F4 is discharged. F4 is **NOT discharged**, **NOT
  satisfied** and **NOT unfrozen**. `specs/SPEC_RUBRIC.md` was not touched by
  this addendum.
- Not claimed: that a general permission, or a Tradovate-framed permission,
  covers the PRAXIS NinjaTrader 8 / Rithmic path. That is **Amear's ruling**
  (S8). He has ruled to send MFFU a follow-up naming NinjaTrader 8 + Rithmic
  (`DECISION_LOG.md` row `2026-10-28T20:54:29Z`). That follow-up is **his to
  send**. On the manager's attestation, no agent in this filing unit drafted or sent it: every brief in this unit forbade touching email.
- Not claimed: that PRAXIS complies with the conditions in D.
- Not claimed: anything about the date of this reply, or its position in the
  thread relative to Frank's reply or to Amear's messages, beyond the display order visible in the screenshot (Amear's collapsed message shown above it).
- Not claimed: that the sender name, address, or the MFFU affiliation is
  verified. All are as displayed in a screenshot.
- Not claimed: anything about what the help-center URL says. This filing unit did not fetch it (manager's attestation, see B).

Edited 2026-11-10 under D9 (decided by manager under D-2026-11-08-D D1): lines 597, 733 and 757 had a support representative's name-bearing address replaced by [rep-address]; line 733 is quoted text edited after capture. The evidence PNG docs/reports/evidence/2026-10-28-mffu-davi-reply.png is not committed, because it shows the same address. The prefix hash of lines 1-537 cited elsewhere is unaffected. Itemised in docs/reports/2026-11-10-d9-housekeeping-manager.md.
Appended 2026-11-10 under D9 (S13): Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
