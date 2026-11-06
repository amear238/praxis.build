# Return handoff to the Claude.ai Praxis chat — 2026-11-04

**From:** Code (Mac), praxis-master. **Status:** `main` = `origin/main` = `87d506f` (OBSERVED via `git ls-remote`, 20:09Z).
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## What was committed (all pushed)

- `b9ba134` (11-02): rulings R-VN3-1..6 filed; `tools/tickprep/` source; VM handoff.
- `a60edf7` + `f29f057` (11-04): the VM High-res plan and VM notes, filed unchanged and hash-matched; D-2026-11-03-A; Amear's 11-03 rulings. (`f29f057` is a ledger-only re-run.)
- `87d506f` (11-04): STATUS.md and HANDOFF.md brought up to date; D-2026-11-04-A files R-1104-1..3 in his words; MANIFEST; ledgers. 8 files, 985 lines added.

Every unit was audited PASS before it was committed. The old staged set (12 paths), root file `F` and the old uncommitted lines are still out of every commit, as ruled ("as is").

## Current state

- Phase: Block 2, backtesting. F1, F2 and F4 are frozen. F3 is frozen with its void clause standing. No High-resolution run exists.
- Instrument: NQCONTROW (09-25 in the CSVs). Baseline BandOrVWAP: 1,190 trades, PF 1.29.
- Runs from 11-01: OppBand (810 trades, PF 1.26) and Flat1559 (1,190 trades, PF 1.28). LastHalfHourMomentum is retired (PF 0.84).
- No tick data is held or bought. Portara at $695 was declined. Under R-1104-3 there's no purchase until Standard-resolution results show proof of concept.
- VM handoff written today (`docs/reports/2026-11-04-vm-handoff-readback-ticksource-exe.md`):
  - read-only readback of the per-contract NQ minute folders
  - research-only search for a cheaper or free tick source
  - upload of TickPrep.exe and MakeSynth.exe by Drive, for a hash-matched commit
- Your screen list for the next VM session: C6 (save the Strategy Analyzer settings as default), C7 (NQCONTROW readback), and reading the Log-tab "ignored" messages.

## Decisions that are only Amear's

1. **The commit gate vs R-1104-1.** Code cannot commit by itself yet. The project's commit hook only accepts a token from an auditor agent this session can't start, so for now Amear types each commit. Making R-1104-1 work means changing a safety hook. That is a code change and needs his word. Related open bead: `Praxis_build-22q`.
2. **What counts as proof of concept** for buying tick data (R-1104-3). Not yet defined.
3. **`r8j` at P0.** Importing the Phase 3 spec (nine breakers, the Block-4 gate, the Block-2 pass gates) was set to P0 by the master. Amear hasn't confirmed it.
4. **When High runs happen.** Deferred by him ("when the time comes ask agaian"). Code will ask again before planning one.

The full open-question lists are pointers only and are not answered here. They are in DECISIONS.md: D-2026-11-02-A/B/C, D-2026-11-03-A §e and D-2026-11-04-A.
