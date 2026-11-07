# RULINGS — 2026-11-07 morning (WHO: amear)

Filed verbatim by praxis-master at 2026-11-07T12:55Z from Amear's typed message in the Claude Code session. Evidence grade: OBSERVED (the text below is the message as received in this session; nothing has been acted on). Amear interrupted immediately after pasting with "close here and i. clear contextg" — the session was closed on his instruction before any of the loop below ran. **Nothing in this file has been executed.** The next session starts from this file.

Answers to `docs/reports/2026-11-07-return-handoff-claude-ai.md` §4.

---

RULINGS — 2026-11-07 morning (WHO: amear). Answers to the 11-07 return handoff §4.

1. Addendum 5 timing: RATIFIED. Unpark/close uqb on a fresh audit.
2. Item 19: commit docs/reports/2026-10-28-voice-session-notes.md as a one-file exception to the as-is rule — it is the source of a ruling. Fix MANIFEST.md:244 to match.
3. Guard vs trailer: no guard change. Keep the attribution line in the form the guard accepts. Don't loosen a guard to fit a format.
4. Walk-forward values (Q1–Q10):
   Q2 yes, lookback {10,14,18} x multiplier {0.8,1.0,1.2} is the small grid.
   Q3 Off is NOT a stop value — I ruled "add the stop, tune all four". Three finite stop-ATR multipliers; you propose them, inside 1.5–3.0 ATR.
   Q4 yes, OppBand = the paper's opposite band, as in _OppBand.cs.
   Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar, as in _Flat1559.cs.
   Q6 ATR(14) = 14 completed RTH sessions (daily ATR).
   Q7 NT8 full-span runs per configuration through the bridge, window selection and PBO on the Mac from NT8's trade lists. That keeps one copy of the strategy (NT8); only the selection maths runs on the Mac.
   Q8 both arms are judged against all six Phase 3 gates; arm (b) must also pass PBO < 0.05.
   Q9 no tier chosen. Report the per-tier table; I pick after paper results.
   Q10 and every remaining PROPOSED value in the file: settle under R-1104-2, strictest reasonable choice. Add the missing ExitPolicy/Contracts test that parked 867, re-audit, commit.
5. 2a run: YES, covered by my lift. A test that needs a run includes the run.
6. Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". It does NOT count as "driven from the terminal". The full in-VM automation lift needs a run whose settings come from the bridge/config, not my hands. Log it as a partial pass until then.
7. Bridge items: (4) playbackrun/reconnect/flatten/strategies/ghostorders/AutoReconnect stay forbidden until live-trading design says otherwise. (5) NT8 Guard out. (7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; the VM's installed copy must hash-match HEAD, or STOP. (11) pip may download only the bridge's pinned requirements, into its own venv under C:\praxis\. (12) you propose how each arm runs through the bridge after 2a passes.
8. Snapshot is my hand step: confirmed.
9. Notes-4 unruled items stay open; none block anything.
10. Go-live checklist additions: remove the unauthenticated bridge request folders (or add auth) before real money; unmap Z: and turn off the SMB share.

Then loop: finish 867, build arm (a) and (b) Mac-side, and tell me when the VM session can start. Return handoff here at the end, only decisions that are genuinely mine.

---

## Master's filing notes (not rulings)

- Ruling 1 unblocks `Praxis_build-uqb`: next session files addendum 6 (ratification, WHO: amear) in DECISIONS.md, then a fresh auditor dispatch on the gate batch, then close.
- Ruling 2 is a named one-file exception to "old as-is set out of every commit" — applies only to `docs/reports/2026-10-28-voice-session-notes.md`; the rest of the as-is set stays out.
- Ruling 3 closes return-handoff §4 item 3 with no code change.
- Ruling 4 changes the parked spec: the stop axis becomes three finite ATR multipliers in [1.5, 3.0] (master proposes), grid therefore stays 3×3×3×3 = 81 only if three stops are kept; Q7 moves the walk-forward run model to NT8-full-span-per-config via the bridge with window selection + CSCV/PBO on the Mac. This is a DECISIONS-level change to D-2026-11-06-D's design; per `master-s4-entry-before-code`, the amended entry goes on disk BEFORE any code or spec unit is dispatched.
- Ruling 6 defines a "partial pass" state for the in-VM automation lift (Oct 28 ruling): 2a via hand-set Strategy Analyzer tab = baseline reproduced, NOT terminal-driven. Needs a DECISIONS addendum to D-2026-11-06-A.
- Ruling 7(7) is a hard STOP condition for the VM session: installed `PraxisNoiseAreaBreakout.cs` must hash-match HEAD. Must be added to `vm/2026-11-06-vm-handoff.md` before the VM session starts.
- Ruling 10 extends the go-live checklist (two items). Needs a DECISIONS/checklist edit.
- The loop (finish 867 → arms (a)/(b) Mac-side → tell Amear when the VM session can start → return handoff) has NOT started.
---
*Addendum by unit 2026-11-07-rulings-filing-correction-1 (S13 house style; not part of Amear's rulings; DECISION_LOG 2026-11-07T13:36:00Z): Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.*
