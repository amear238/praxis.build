# PROJECT-KIT — v0.2 gap list

**Opened session 45 · 2026-08-08 · from Praxis retrofit #1 · author: praxis-master**

Deliverable 3 of 3. Gaps are **recorded, never fixed here.** Each traces to the adoption
report `docs/reports/2026-08-08-session45-project-kit-adoption.md` and to a CONFORMANCE
entry in `docs/specs/2026-08-08-ledger-compaction-spec.md`, so the v0.2 change log has a
source for every line.

| Gap | Template locus | CONFORMANCE | Status |
|---|---|---|---|
| (a) | §4 — state mapping | C-5 | pre-confirmed by A2 |
| (b) | §3 — STATE.md contents | C-6 | pre-confirmed by A2 |
| (c) | Acceptance Suite mode rule | C-7 | **new, surfaced during amendment** |
| (d) | §-structure ("three sections") | C-4 | **new, UNDERDETERMINED** |

---

## (a) Template §4 has no rule for the DISPATCHED state

The §4 mapping covers CLOSED, RESOLVED, SUPERSEDED, OPEN, BLOCKED, DEFERRED and
IN-PROGRESS. **DISPATCHED is absent.** It is not a Praxis-only state: any project whose
ledger is written by a spawn-time hook will accumulate rows that no agent survives to
close. Supplied for this retrofit by operative A2. v0.2 should carry a first-class rule.

## (b) Template §3 has no home for a regenerated counter line

§3's STATE.md contents list is closed — SPEC pointer, F1–F4, open beads, next 3
dispatches, quota/session window. The abandonment counter `S12: <N> rows abandoned at
dispatched` has nowhere to sit. Placed in §2.1 of the Praxis spec by author's choice.
v0.2 should either admit a "counters" slot or state that regenerated metrics live
elsewhere.

## (c) The acceptance-suite mode rule is not whitespace-safe — NEW, MEASURED

Suite v3 mandates flattening with `tr '\n' ' '` before every literal grep, on the stated
reasoning that multi-word phrases are wrap-fragile.

**`tr '\n' ' '` replaces the newline but preserves the continuation line's indentation.** A
phrase that wraps into an indented line therefore flattens to *multiple* consecutive
spaces, and a single-space literal still misses it.

Measured on the unamended spec, where the phrase was split across lines 39–40:

```
flat 'abandoned at dispatched'   = 0
```

S45-2 asserts that flattening alone re-nulls that check. **It does not** — the check
returns 0 in both modes. The literal was correctly retired for a different reason, so the
conclusion held, but the stated mechanism was wrong.

**Repair for v0.2:** squeeze whitespace as well — `tr '\n' ' ' | tr -s ' '` — and say so in
the mode rule. Until then, any suite literal is implicitly a formatting assertion about the
file under test. In this retrofit C2 and C4 pass only because their phrases were kept
unwrapped by hand, which is a property of the author's formatting, not of the suite.

## (d) "Three sections" is unnamed — NEW, UNDERDETERMINED

The adoption brief mandates a three-section spec structure but does not name the three.
The partition used here — Context and baseline · Design · Constraints and acceptance — is
the author's, flagged at C-4, and is **not template content.** v0.2 should name them, or
state that the count is binding and the names are free.

---

## Not gaps — recorded so they are not re-raised

- **Byte-only ceiling enforcement** is a deliberate deviation with a ratified rationale
  (C-1), not a template defect.
- **Environment subtraction deferred for Praxis** is an exception under D-7 (C-3), not a
  gap; the template default for greenfield stands.

---

## ERRATA — UNGRADED, appended 2026-08-08 (session 46)

**Explicitly UNGRADED, master-authored, not evidence.** Body above is byte-unchanged and the
audit verdict stands unaltered. Grade:
`docs/reports/2026-08-08-session46-adoption-and-gaplist-audit.md` — `Result: FAIL` on S1, S2,
S3 and S9(R3), covering this document jointly with the adoption report.

**Two corrections specific to this file:**

1. **Gap (c)'s proposed repair is insufficient as written.** This document proposes
   `tr '\n' ' ' | tr -s ' '`. Measured: that returns **0** against a tab-indented
   continuation. The correct repair is whitespace-class normalization
   `tr -s '[:space:]' ' '`, because `tr -s ' '` squeezes the space character only and leaves
   a tab intact. Spec `C-7` carries the same insufficient form.

2. **The exposure is narrower than gap (c) states, and the master over-stated it too.**
   Measured gradient, controls run twice independently:

   ```
   C2 reflow COL1    (tr only)      : 1   survives — column-1 wrap is safe
   C2 reflow 2-SPACE (tr only)      : 0   dies
   C2 reflow 2-SPACE (tr -s ' ')    : 1   repaired by the weaker fix
   C2 reflow TAB     (tr only)      : 0   dies
   C2 reflow TAB     (tr -s ' ')    : 0   NOT repaired by the weaker fix
   C2 reflow TAB     (-s [:space:]) : 1   repaired
   negative control 'since the last compression' : 0
   ```

   So only a **tab** continuation requires the character class. "Reflowing the line silently
   kills the check" is true for indented continuations, not for reflow in general.

**Also recorded:** this document's single pasted figure, `flat 'abandoned at dispatched' = 0`,
was taken against a file version that no longer exists. Run against the spec as it stands
today the same literal returns **1**. The figure is not reproducible and carries no command
and no file version.

**Disposition.** Not repaired here. `Praxis_build-f5f` is at **FAIL 1 of 2, shot BANKED**
(Amear, session 46); repair is producer work and **Step 2 is gated on it**. Per the same
ruling, "suite mode v3.1" is **not** adopted as a standing convention — the measurement above
is live, the project-wide rule is not.
