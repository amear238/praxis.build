# AMEAR'S ANSWERS C1–C10 TO THE 2026-11-08 PARK CARD (WHO: amear)

Filed verbatim by praxis-master on 2026-11-08 from the message Amear pasted into the Claude Code session after the park (the third message after the park at DECISION_LOG `2026-11-08T17:25:00Z`; the ruling C10 alone arrived first and is on the ledger at `19:04:00Z`). Evidence grade: OBSERVED — the fenced block is the message as received, copied without edits. The heading line names the Claude.ai channel as its origin, so the words are REPORTED BY the Claude.ai channel and pasted by Amear. His own approval line is inside the block. They answer the HANDOFF.md 2026-11-08 resume card's "For Amear" list (items 1–6) and the C10 premise question of DECISION_LOG `19:04:00Z`.

Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

---

The paste, verbatim. The exact line range of the block and its sha256 are recorded in the DECISION_LOG row after an `openssl dgst -sha256` read, not counted by hand.

```text
PRAXIS — AMEAR'S ANSWERS TO THE 2026-11-08 PARK CARD (Claude.ai channel)
WHO: amear. Agents write every repo file (A11). File as D-2026-11-08-C.
Sending this message is my approval of C1-C10 as written.

C1  U7 (Praxis_build-diq) resumes in this new session. One correction:
    replace the stale pasted diff with the diff of the blob being
    committed. One audit. No park branch is landed for diq.
C2  Park rule amendment (made between sessions, per the absolutes
    rule): a park commit to parked/ branches is exempt from the
    audit-token gate, because it never touches main. Closes
    Praxis_build-8sw.
C3  Step 0, items 2-6: (2) anonymous HTTPS clone, step 3.1;
    (3) only the two AddOn files of step 3.2; (4) unauthenticated
    request folders acceptable for sim tests only, closed before real
    money (go-live list); (5) Sim101; (6) Amear presses Compile in the
    NinjaScript Editor by hand.
C4  One entry satisfies "File each" for D-2026-11-08-A.
C5  D-2026-11-08-B (i) win/loss judged by price, consistent with
    B = exit at entry price; (ii) Studio Static rows use the stricter
    limit type and stage, both shown; (iii) A8 annualisation = mean net
    P&L per session x 252, for IS and OOS alike; (iv) A2 closes the
    notes-4 Sharpe item.
C6  "Discharged" recorded as PASSED@a2f1067 is correct. O1 moves out of
    the OPEN section.
C7  Praxis_build-gjj: disable memory in the praxis-manager agent
    definition. Code makes the edit; auditor checks it.
C8  The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written.
C9  Step 0, item 1: snapshot taken, named pre-cli-nt-bridge-2026-11-06.
    The Claude session on the VM is closed.
C10 Code writes the filed step-0 answers into vm/2026-11-06-vm-handoff.md
    §2 so the VM session reads them from the file. Amear does not repeat
    them to the VM session.
```

---

## Master's filing notes (not rulings; the master's readings, changeable by Amear)

1. **Session.** The park was hit in this same Claude Code conversation (DECISION_LOG `17:25:00Z`). C1 calls this "this new session". C2 says the amendment was "made between sessions, per the absolutes rule", in the Claude.ai channel, which is not the session the rule blocked. The resumption is recorded as his explicit decision (WHO: amear); the master does not argue it.
2. **C1 "replace".** The master's standing rule is that reports are append-only, so a wrong paste stays on disk beside its correction. Reading: C1's "replace the stale pasted diff" is carried out by APPENDING the diff of the blob being committed as the diff of record, and marking the earlier paste SUPERSEDED in that appended section. The stale paste is not deleted. Changeable by him: if he means the bytes are to be removed, he says so.
3. **Order (S4; one manager at a time).** (a) D-2026-11-08-C is filed and OBSERVED on disk before any unit it authorises is dispatched. (b) U7 resumes under C1: one correction and one audit, committed with a MANIFEST blob built from HEAD plus U7's own rows. (c) D-2026-11-08-C is committed. (d) Then, one at a time, citing C: the rubric unit (C2 text, C6 O1 section move, C8 July hunk); the values-spec unit (C5 (i)–(iv)); the VM-handoff unit (C3, C9, C10, with R1's live-template read and C3(4)'s go-live line); the agent-definition unit (C7); the gate-hook unit implementing C2's exemption, which is a change to the commit gate and is trip-tested under S3 and S9 before commit. After that come U2 housekeeping, U4 F2 proposal and U5 R6 research.
4. **C2 needs code.** The exemption is a rubric text change AND a change to the commit-gate hook. `Praxis_build-8sw` closes when both are in and trip-tested. C1 says no park branch is landed for diq, so nothing waits on it now.
5. **C3 (4)** adds an item to the go-live list ("closed before real money"). That list is in `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md` (:35, :38). The VM-handoff unit carries the line there by append.
