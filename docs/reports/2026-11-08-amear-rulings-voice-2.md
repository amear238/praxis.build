# AMEAR'S RULINGS D1–D12 — VOICE SESSION 2, 2026-11-08 (WHO: amear)

Filed verbatim by praxis-master on 2026-11-08 from the message Amear pasted into the Claude Code session while unit U8 (filing D-2026-11-08-C) was running. Evidence grade: OBSERVED — the fenced block is the message as received, copied without edits. The heading names the Claude.ai channel, so the words are REPORTED BY the Claude.ai channel and pasted by Amear; his approval line is inside the block. They answer §4 of `docs/reports/2026-11-08-voice-strategy-brief.md` and set standing rules.

Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

---

The paste, verbatim. The exact line range and sha256 are recorded in the DECISION_LOG row after an `openssl dgst -sha256` read, not counted by hand.

```text
PRAXIS — AMEAR'S RULINGS, VOICE SESSION 2 (2026-11-08, Claude.ai channel)
WHO: amear. Agents write every repo file (A11). File as D-2026-11-08-D.
Sending this message is my approval of D1-D12 as written.

STANDING RULE CHANGE — AUTONOMY
D1  Default-decide. When a unit or the master reaches a question that
    would otherwise go to Amear, it takes the recommended option, logs
    it as "decided by master under D-2026-11-08-D D1", and continues.
    Amear may reverse any such decision later; the reversal is filed
    like any ruling. No unit waits on Amear except for D2 items.
D2  Only four things stop and wait for Amear's word: (a) spending
    money; (b) switching live trading on, or any order path to a
    funded account; (c) changing circuit-breaker values while real
    money is at stake; (d) installing keys, credentials or agent
    permissions. Everything else is D1.
D3  The Telegram commit-approval step in the Hermes setup is removed.
    Commits land on an audit PASS. Telegram informs; it does not ask.
D4  Loop: a Hermes timer starts a fresh Code session every four hours.
    Each run reads HANDOFF.md, executes the next unit(s), and ends with
    one Telegram message in plain English: what was done, what was
    decided under D1, what is blocked under D2. No code names (F1, O1,
    bead IDs) without a plain-language gloss. Rough weekly review with
    Amear in the Claude.ai channel; nothing waits on it.
D5  A message to Amear that asks a question with a recommendation
    attached, on a non-D2 item, is a defect under D1. Log it, bead it,
    take the recommendation.

WORK ORDER
D6  FIRST: drawdown viability check, Mac-only, read-only, no VM, no
    purchase. On the three committed 2026-11-01 trade lists, compute
    per-walk-forward-window worst drawdown at 1 MNQ (MFFU MNQ
    commission per cost model v1.2.0), with and without a simulated
    daily-loss cap (breaker #1 at its spec value). Compare to the A4
    ceiling per tier row (80% of the lower of 4% of account and the
    trailing limit). If scripts/wf can regenerate the trade list from
    the 09:30 ET session start (R1), run that too and label it
    UNVERIFIED against NT8. Report: pass/fail per tier at 1 MNQ and
    1 NQ.
D7  If D6 fails at every tier at 1 MNQ: do not design breaker values
    to fit the drawdown ceiling (that is curve-fitting). Report it, and
    pull R6's research (higher-win-rate, steadier-equity strategies)
    forward to P0. The Noise-Area baseline continues through the VM
    tests for the record, but a GO on MFFU is not expected from it.
D8  Brief §4 decisions: (3) start the VM session as soon as the VM
    handoff carries the step-0 answers (C3, C9, C10). (4) draft the F1
    live-signal topology doc alongside the F2 breaker PROPOSAL. (5) land
    the two staged MFFU evidence reports (2026-08-07, 2026-10-28) and
    grade them against F4's criterion. (6) the five P0 guard beads are
    accepted as known risk while only docs/specs move; fixed before any
    Block 3 code that can place orders. (7) the VM stays a hands-only
    executor; Mac is the only master. (8) "final step of this build" =
    Block 4 paper pass on MFFU sim (the standing proof-of-concept
    ruling). Block 5 live is a separate sign-off under D2(b).
D9  The 12 old staged paths are landed properly (audited) rather than
    unstaged. Root file "F" is traced, then removed and logged.
D10 Messages to Amear are plain English. Account figures are shown in
    dollars at the contract size, not in points or percent alone.
D11 Once per run, the master checks for any waiting question older
    than one run that is not a D2 item, and closes it under D1.
D12 Sequence after D6: U7 resume (C1), rubric unit (C2, C6, C8, and
    D1-D5 as a new "Autonomy" section), values spec (C5), VM handoff
    (C3, C9, C10), manager memory off (C7), park-commit gate exemption
    (C2, trip-tested), housekeeping (D9), F1 topology + F2 PROPOSAL,
    F4 grading, R6 research on its own worktree.
```

---

## Master's filing notes (not rulings; the master's readings, changeable by Amear)

1. **D1 vs rubric S8.** The committed rubric S8 reads "No question that belongs to Amear is answered on his behalf." D1 narrows what belongs to Amear: only the D2 items, while everything else is decided by the master and logged "decided by master under D-2026-11-08-D D1". The rubric unit (D12) writes D1–D5 into the rubric as an "Autonomy" section. Until it lands, auditors are told that D-2026-11-08-D governs S8's scope.
2. **D2(d) and the Hermes work in D3/D4.** Setting up the Hermes timer and Telegram may install keys, a bot token, or agent permissions. That includes a Code session launched unattended with its own permission mode. Each such step is a D2(d) item and stops for Amear's word when it is reached. Everything else in D3/D4 proceeds under D1.
3. **D4 and the single-session rule.** A timer-started session must not run while another Claude session has this working tree open (CLAUDE.md Do-Not; `docs/runbooks/2026-07-10-single-session-rule.md`). Decided by master under D-2026-11-08-D D1: each timer run checks for a live session on the tree and exits without work if it finds one. Changeable by Amear.
4. **Order now in force.**
   - (a) U8, filing D-2026-11-08-C, which is in flight.
   - (b) U9 files D-2026-11-08-D, on disk.
   - (c) One audit of both entries, then a commit.
   - (d) D6 drawdown check.
   - (e) The D12 sequence.
   
   D7 is applied to D6's result as written.
5. **D6 inputs the master will name in the brief**, read when the unit runs, not assumed now:
   - breaker #1's spec value, from `docs/specs/2026-11-05-phase3-build-specification.md` near :95–105;
   - the cost model `config/backtest-cost-model.json` v1.2.0 MNQ $1.90 round turn;
   - the per-tier table, WF spec :113–132;
   - A4's ceiling;
   - the three committed trade lists, found from `scripts/wf/oracle/tests/test_baseruns.py`, which reads them from the Desktop.
