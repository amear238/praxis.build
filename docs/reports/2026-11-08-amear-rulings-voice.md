# RULINGS — 2026-11-08 voice session (WHO: amear)

Filed verbatim by praxis-master at 2026-11-08T14:02Z from the message Amear pasted into the Claude Code session (`date -u` read 14:02:11Z on receipt). Evidence grade: OBSERVED (the text in the fenced block is the message as received in this session, copied without edits; nothing has been acted on at the time of filing). The rulings were given in Amear's voice session with the Claude.ai Praxis channel on 2026-11-08; the pasted text is that channel's record of them, so the words are REPORTED BY the Claude.ai channel and pasted by Amear. They answer `docs/reports/2026-11-07-return-handoff-claude-ai-2.md` §4 items 1 and 3, and §6 of `docs/reports/2026-11-08-strategy-filter-audit.md` (questions 1–4).

Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

---

The paste, verbatim (lines 13–83 of this file are the message; nothing in them is the master's):

```text
PRAXIS — RULINGS FROM AMEAR, VOICE SESSION 2026-11-08 (Claude.ai channel)
WHO: amear. File each as a DECISIONS.md entry citing this session.
These answer return handoff 2026-11-07-return-handoff-claude-ai-2.md §4
items 1 and 3, plus the strategy filter audit dated 2026-11-08.

RULINGS
R1  RTH = 09:30–16:00 ET (answers §4 item 1, B1). Arms (a) and (b)
    anchor at the 09:30 ET cash open. VM step 0 reads the live
    "CME US Index Futures RTH" template hours (T7 readback). If the
    live template starts 08:30 ET, the 2026-11-01 baselines are
    suspect and are re-run at 09:30 ET before either arm counts.
R2  GO requires arm (a) to pass. Arm (b) can only add confidence or
    block a GO; it can never carry a GO on its own (§4 item 3).
R3  Gate 6 (WFE) applies to arm (b) only (§4 item 3).
R4  Scoring, hybrid (§4 item 3, gate 2):
    - Win rate: no-trade days excluded; a break-even trade counts as
      half a loss.
    - Sharpe: daily returns, every trading day counted (no-trade
      days = 0), equity base = the account size actually traded.
    Check against the values-spec §6/§8 wording; flag any conflict
    back to Amear, do not resolve it.
R5  The fixed R:R shape filter (3:1 partial plus runner; 1.5:1) is
    retired for all automated-strategy research, including the
    higher-win-rate brief. A strategy qualifies if it is fully
    rule-based, net positive after costs, and survives every MFFU
    condition, including the EOD trailing drawdown and the
    consistency rule.
R6  Research and backtest, on the existing 1-minute data only,
    nothing bought (R-1104-3 stands):
    - Pre-Announcement Drift (Hu, Pan, Wang & Zhu 2022), evening-
      entry variant, exit before the release.
    - Macroeconomic Announcement-Day Premium (Savor–Wilson; Ai 2024).
    Runs in parallel with the walk-forward, not queued behind it.
    Before any build, read MFFU's current T1 news rule and confirm
    whether an evening entry counts as the same trading day.
R7  Parallel work runs in a separate git worktree on its own branch,
    never in the same working directory (v6y). NT8 runs on the VM
    take turns.
R8  F2 unfreezes. Breaker values set for manual trading are redone
    for the automated book: #2 max 2 trades/day, #3 two-and-done,
    #4 flat at 11:30, #5 as a disable of the system's own trading
    15:00–18:00, #8 inter-trade interval under 5 minutes.
    KEEP: #1 daily loss limit; #5 as a lockout on Amear's own
    interaction 15:00–18:00. New values come back to Amear as
    PROPOSED.
R9  FOMC-Cycle Even-Week stays parked while trading on MFFU
    (multi-day hold breaks flat-by-close). Revisit only if own
    capital is ever used.

HOUSEKEEPING (Code's job, not Amear's)
- The index holds 12 stale staged files from July–October (2026-08
  reports, the F4 evidence PNG, the ledger-compaction spec). Unstage
  or land them deliberately; never commit without a pathspec.
- Stray untracked file "F" (2026-07-28, contents "# DISPATCH LOG"):
  investigate, then remove or log.
- Audit-ledger flush still owed: surgical, nine 2026-11-07 lines,
  the three July/August as-is lines stay out.
- MFFU flat time is 16:10 in one doc and 16:59 in another: read
  MFFU's current terms and record which is right.
- HANDOFF.md line 7 says the bd remember save failed, but
  master-gate-route-2026-11-07 is in the beads store. Correct it
  append-only.
- Stale bead title on Praxis_build-867.

STILL OPEN FOR AMEAR (next session)
§4 items 2 and 4–12 of the 2026-11-07 return handoff, starting with
item 4 (the July SPEC_RUBRIC hunk, R-A/R-B/R-C). Bring a plain-
language summary of what those lines do.
```

---

## Master's filing notes (not rulings; the master's readings, changeable by Amear)

1. **R8 and the rubric file.** `specs/SPEC_RUBRIC.md:3-4`: "The build side does not edit this file. It proposes changes; Amear applies them." F2's unblock condition (`:41-42`) is "A DECISIONS.md entry names the governing rule and the 15:00 disposition, and breaker specs #4 and #5 are amended to match." R8 orders the redo and says the new values come back PROPOSED. Reading: R8 authorises the WORK (a proposal unit on breakers #2, #3, #4, #5-system, #8); the F2 state line in the rubric file changes by Amear's hand, and the unblock artifact (the DECISIONS entry with the governing rule and the 15:00 disposition) does not exist yet. Until it does, the master treats F2 as still blocking Block 3 and Block 4 work, and treats the proposal unit as unblocked. Amear may override explicitly.
2. **R1 and the rescued template.** `docs/reports/2026-10-31-o78-worker4-report-adversarial.md:208-219` (committed `29c3e13`) prints a RESCUED copy of `CME US Index Futures RTH.xml` as Monday–Friday `830`–`1600`, TimeZone `Eastern Standard Time` (REPORTED BY that worker). The live VM template is UNVERIFIED. If the T7 readback shows 08:30, R1's re-run clause fires for the three 2026-11-01 runs.
3. **R4 and the values spec.** `docs/specs/2026-11-06-walk-forward-values.md:92` defines Sharpe as the IN-SAMPLE SELECTION objective only (daily net P&L in dollars at 1 NQ, 0 on no-trade sessions, √252, n − 1, rf 0, "needs no equity base"); `:93` and `:132` say the gate "OOS Sharpe ≥ 1.0" definition and its equity base were OPEN under ruling 9. R4 fills the gate definition. Whether R4's "equity base = the account size actually traded" also changes the §6 selection statistic, and where R4's win-rate rule applies (the spec's six gates at `:121-127` carry no win-rate gate; win rate appears in the Block 4 ±15% gate, `specs/SPEC_RUBRIC.md:96-97`, O4), is for the filing unit to check and FLAG, not resolve — R4's own instruction.
4. **R6 and R7 vs the one-manager rule.** Parallel means a separate worktree and branch (R7). Dispatch stays serial: one praxis-manager at a time (bug `Praxis_build-9lj`), and no dispatch while a `vm/replies/<ts>-STATUS.md` holds `STARTED` without `FINISHED` (settlement 9).
5. **Sequencing.** The DECISIONS.md entry for these rulings is written and verified on disk before any unit that depends on them is dispatched (`bd memories master-s4-entry-before-code`).

---

**Correction 1 (praxis-master, 2026-11-08 ~14:30Z, append-only).** Line 9 above says the paste occupies "lines 13–83 of this file". That was a hand count made while writing and is WRONG. OBSERVED after writing: `wc -l` = 90; the fence lines are 11 and 80 (`grep -n '^\`\`\`'`); the paste body is lines **12–79** (68 lines); `sed -n '12,79p' … | openssl dgst -sha256` = `73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263`. Line 9 is left as written. The same wrong range appears in DECISION_LOG rows `2026-11-08T14:02:11Z` and `14:22:00Z` and DISPATCH_LOG row `14:24:00Z`; a correction row follows them in DECISION_LOG. The pasted text itself is unchanged.
