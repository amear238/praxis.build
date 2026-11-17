# AUDIT GRADE — unit `dj2` (rescoped) — session 48, 2026-08-09

> **PROVENANCE BANNER — READ FIRST.**
> **This file was NOT written by `praxis-auditor`.** The auditor graded the unit and returned a
> complete verdict, then reported that its operating instructions prohibit it from writing
> findings/report `.md` files. Its verdict below is a **producer-side transcription by
> `praxis-master`**.
>
> This is the interim measure recorded at `ISSUE_REGISTER.md` `[2026-08-03T21:20Z]`, option (c):
> master transcription with a mandatory provenance banner. **Its cost is stated rather than
> hidden — nothing on disk independently attests that the auditor authored this text, and an
> agent-written attribution is indistinguishable in the file from a real one.** That is the same
> limitation `specs/SPEC_RUBRIC.md` already records for `APPROVED BY:`.
>
> The file exists at all because a FAIL verdict has no writable home: `audit-approve.sh` writes
> PASS rows only, the auditor cannot write `AUDIT_LOG.md`, and the master is denied that file.
> Session 47 landed `c41a969` specifically to stop a grade of this kind from being cited by
> committed reports while existing nowhere in the repo.

---

## Verdict

**`Result: FAIL`**

**Per-criterion:** S1 **FAIL** · S2 PASS · S3 PASS · S6 PASS · S7 PASS

**Lineage:** `dj2` stands at **FAIL 1 of 2**. One shot remains. The absolute park rule fires on the
second FAIL for the same bead.

**Scope of the failure, in the auditor's own framing:** *"The artifact itself carries no defect I
could find. Every hard constraint holds, the halted attempt's cap-gaming defect did not recur, and
the compression is honest. The failure is confined to the report's evidence discipline under S1."*

---

## Step 0 — null-diff self-check

```
$ git diff --cached -- docs/specs/2026-08-08-ledger-compaction-spec.md | grep -c '^+| K7 |'
1
```

Artifact staged; grading proceeded.

## Hard constraints — all hold

| Constraint | Observed | Verdict |
|---|---|---|
| body ≤60 | `CONF=61`, body `60` | OK |
| C1 ≥6, case-sensitive | `6` | OK |
| C2 / C3a / C3b / neg / C4 | `1 · 1 · 1 · 0 · 1` | OK |
| §3 acceptance paragraph byte-unchanged | `c1d0c8c4…84948d`, 237 bytes, located by content at L=58 | OK |
| blank line after `## 3. Constraints` (H=46) | `sed -n 47p \| wc -c` → `1` | OK |
| **zero blank deletions — the halt defect** | two deleted lines, both prose; `grep -c '^-$'` → `0` | **did not recur** |
| C-7 byte-identity | HEAD `974a4797…` == worktree `974a4797…` | OK |
| no tag flipped | tag-token diff shows additions only; K3 retains `[BINDING — …]` | OK |
| K7 wording unaltered | `od -c` of line 56 shows the mandated bytes exactly | OK |
| K7 directly after K6 | K6 line 55, K7 line 56 | OK |
| C-9 after C-8, two residuals | C-8 line 98, C-9 line 103 | OK |
| stale figures stay stale | `101 files` lines 11, 39; `26 untracked` line 41 | OK |
| staged at content level | `12 2` numstat; blob `55b417ee…`, not the empty blob | OK |
| index undisturbed | 9 paths; other 8 at `118/35/15/1882/537/546/195/301` | OK |
| nothing committed | HEAD `c41a969` | OK |

## S3 — PASS. Three trips re-derived by the auditor rather than trusted

Trip 3 (the halt defect) independently reconstructed: real artifact `0`, mutated copy `1` —
*"the zero is a true null, not a dead check."* Trip 1 `body on mutated = 61`. Trip 5
`neg with phrase injected = 1`.

Residual 1 re-derived in the auditor's own throwaway repo, producing its own blob
`78981922613b2afb6025042ff6bd878ac1994e85`. It further confirmed the producer's cited hash
`ce013625…464a` is the genuine blob for `hello\n` via `printf 'hello\n' | git hash-object --stdin`
— *"their file content, not fabrication."* Residual 2's `gate-commit.sh:167-176` citation resolves
verbatim.

## S2 — PASS, "but it was close"

Candidate over-claim: C-9 says a compact.sh run *"denies that commit"* and S6 says the block
*"fails cleanly,"* yet `gate-commit.sh` was never tripped and `compact.sh` does not exist yet.
What saved it: the report discloses its method as source reading, pastes the source, and
self-flags C-9 as over-strong on a related axis. *"A reader is not misled into thinking a trip
occurred. Level disclosed = level reached."*

## S1 — FAIL. Three defects, all confirmed independently by the master

The prior audit's failure mode (zero pasted output across 172 lines) did **not** recur — this
report pastes extensively, 30 fenced blocks, and every figure the auditor re-derived reproduced.
S1 is nonetheless literal, and specific load-bearing claims are delivered as descriptions of
output with none pasted.

1. **`…-rescoped.md:328-352`, the entire Adversarial findings section.** Asserts ~8 distinct
   command-based verifications with **zero pasted output**. *Master re-verification:* the section
   spans lines 328–354 and contains **0** fenced blocks, against **30** in the report as a whole.
   The source output exists at `scratchpad/w2-adversarial.md`, **20,549 bytes**, and none was
   carried into the report.
2. **`…-rescoped.md:39-40`.** Worker-count/cap compliance claimed against hook-written
   `SubagentStart` rows with no pasted grep — *"'checkable' is an invitation, not evidence."*
   *Master re-verification:* the rows exist at `DISPATCH_LOG.md:312-315` carrying
   `corr=a828c806e8bf79a3e` and `corr=ad4a783f9fa880d7c`. **Regression note, master's own
   observation:** the HALTED first attempt *did* paste its hook rows; attempt 2 dropped the one
   evidentiary practice attempt 1 got right.
3. **`…-rescoped.md:136-137, 213-215, 414`.** Three further relayed measurements — *"same object
   hash," "21 → 22," "`git diff --name-only` returns empty"* — given as prose descriptions.

*"Every one of these is true and cheaply pasteable. That does not convert a description into
pasted output."*

## S6 — PASS. Two genuine conflicts surfaced rather than absorbed

- **`spec:41`** — "The 26 untracked reports are `git add`-ed in the archive commit" **directly
  contradicts the K7 row this unit inserted.** Routed to ratification rather than edited.
- **`spec:75-77`** — C-2's legality argument does not extend to `gate-commit.sh`, which binds on
  the resulting tree and is indifferent to the command string.

## S7 — PASS

HEAD `c41a969`, unchanged. Staged only. Incidentally corroborated: the auditor's own scratch
commit in a throwaway repo was denied by this repo's live commit guard, **so the gate is armed
in-session.**

## The adversarial question — the auditor's own conclusion

Measured word-level loss: `is · open; · it · is · handled` — five content words, all from one
bullet.

**No normative content was lost.** *"'Retain OPEN, BLOCKED, DEFERRED and IN-PROGRESS as open
items' is an imperative with a coordinated four-member list and a single predicate complement,
'as open items.' That complement distributes over every member; there is no grammatical reading
in which it attaches to a proper subset."*

**The one real cost is emphasis, not claim.** The original's "DEFERRED is open; it does not
vanish" reads as a deliberate guard against treating DEFERRED as terminal — *"a live misreading
given D-7 parks environment subtraction in exactly that state."* Removing the emphatic
restatement is a rhetorical loss. *"Emphasis is not a claim. The compression is legitimate and is
not cap-gaming."*

---

## Master's disposition note

**Not committed.** S7 forbids committing while an audit box is unchecked, and this box is
unchecked. The artifact is independently verified clean by four parties — build worker,
adversarial worker, manager, auditor — plus the master's own re-run of all seven checks. **That
does not convert a FAIL into a PASS**, and the master does not treat it as doing so.

Disposition of the remaining shot is Amear's.
