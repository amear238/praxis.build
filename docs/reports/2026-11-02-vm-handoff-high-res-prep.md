# VM-agent handoff — continue the High fill-resolution preparation (2026-11-02)

Written by Claude Code (praxis-master, on the Mac) for the agent working on the Fusion VM. Assume the reader has seen nothing from the Mac side. Amear asked for it with "give me a handoff for the VM agent to continue the build".

## 0. Rules for the VM agent (hard limits — Amear's ruling R-VN3-2)

- **Prepare only. No purchases. No imports into NinjaTrader. No backtest runs** — not even a "quick check" — **without Amear's explicit approval, given in words for that specific step.** Preparation means: files, plans, measurements on data already on the VM, and questions.
- **No changes to strategy code, trading-hours templates, instrument definitions, or NT8 config.** F2 is frozen (session-flat time / early-close rows): do not touch the template even to "fix" the 12:15 early-close stamps.
- **Delete nothing.** Not on the VM, not in NT8's database, not in the data folders.
- **Don't decide for Amear.** Where a choice is his (what data to buy, whether to import, whether a run happens, whether `.exe` files go in the repo), write the question and stop.
- **Every file you send back gets a SHA-256 printed on the VM** (PowerShell: `Get-FileHash <file> -Algorithm SHA256`, or `certutil -hashfile <file> SHA256`). Paste the hash lines into your notes. The Mac side cannot see the VM, so a file without a VM-side hash stays graded UNVERIFIED.
- Every backtest-related document carries this sentence verbatim: **"Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."** Until a High-resolution run exists and is reported, that is the standing limitation (F3, D-2026-10-30-A; the void clause stands).
- Grade what you write: OBSERVED (you ran it and pasted it) / INFERRED / REPORTED BY AMEAR / UNVERIFIED. A claim about how NT8 behaves is graded by running it, not by reading docs — but running a strategy backtest needs Amear's approval (first bullet).

## 1. Where things stand on the Mac side (as of 2026-11-02 22:10Z)

- `main` = `origin/main` = `cb1a9a5`. The 2026-11-01 four-run readback and the CSV-only analyses are committed (`docs/reports/2026-11-01-three-strategy-results.md`, `docs/reports/2026-11-01-csv-analyses.md`).
- Your `praxis-tickprep` folder arrived via Google Drive (folder `1YaM4I3BKt_nNKWdUnOkj4kJzCeBEwLe_`) — **four files only**: `README.md`, `TickPrep.cs`, `MakeSynth.cs`, `nt-implied-offsets.csv`. The two `.exe` files were not uploaded. The four files are filed at `tools/tickprep/` with a `SHA256SUMS` file (uncommitted at the time of writing; audit pending). Hashes as received on the Mac:
  - `TickPrep.cs` 18,785 B — `104dc9d9135d3e27cab2d35019606ca8f112d7586cdcbe98a32ee0e4d13e6545`
  - `MakeSynth.cs` 3,732 B — `398868cfdfb10b0774606af7481066b3faf3ecdf7c984c644d19173b357a1507`
  - `README.md` 2,219 B — `81534da86c2ecec38506a3a78ac2f1d283a7fa1ab15648b2f74930a10e95aeb5`
  - `nt-implied-offsets.csv` 645 B — `69e1a00975cf84c22d3918600b0912d1fc042a0d8f291e614d446fd8ee8220d9` (reported 24 bytes smaller than your copy — line endings; see §3.2)
  - The VM-side originals have never been hashed, so the transfer is UNVERIFIED until you do §3.2.
- Nothing from tickprep has been run, compiled or imported on the Mac. The README's self-test result (offsets 3400 / 3390.25 / 3380.5; 99,705 bars matched) is on file as REPORTED BY the VM agent, not reproduced.
- **Your High-resolution plan document has not reached the Mac.** The brief named it only as `<FILENAME>`. See §3.1.

## 2. Amear's rulings that shape the work (his words are in `docs/reports/2026-11-01-voice-session-notes-3.md`)

| Ruling | What it means for you |
|---|---|
| **R-VN3-1** — Last-Half-Hour Momentum: *"We're gonna scrap that."* | Retired, not deleted. Do not build on it or re-run it. Whether it appears in a High-resolution comparison at all is an open question for Amear — do not include it unless he says so. |
| **R-VN3-2** — *"get whatever is needed to … run the highest quality back test with those high fill resolution tests."* | This is your mandate, under the limits in §0. |
| **R-VN3-3** — data holes: *"I would just proceed as it is."* | Use the existing data as is. The two 17-day holes (2021-09-09→09-27, 2025-12-14→2026-01-01) and the three wider gaps (2024-07-19 09:58–10:07, 2024-08-02 11:55–12:02, 2026-07-17 10:59–12:06), plus 2023-04-05, are carried as a **stated limitation** in every report. Nothing is re-sourced for them. `TickPrep build` is already strict about this (minutes missing from the 1-min file are not written) — keep it that way. |
| **R-VN3-4** — Flat1559: *"Uh, yeah."* (after the 15:59-price / 4:00 PM-label explanation) | Flat1559 stays as built. Do not change the exit. |
| **R-VN3-5** — breakers: *"Yeah, once uh, once it goes through."* | The judged backtest runs **with the circuit breakers on, once they are built**. The breaker definitions live in the Phase 3 spec, which is **not yet in the repo** (bead `r8j`, being raised in priority). **Do not invent breaker logic on the VM.** Until `r8j` lands, the High-resolution preparation is data and settings only. |
| **R-VN3-6** — go/no-go: *"one that is closest to live execution."* | The voice agent read that to him as High fill resolution + breakers on; he did not contradict it, and he is being asked to confirm it (D-2026-11-02-C, NEEDS AMEAR 14). Treat that reading as the working target, not as his ruling. Which of the six pass gates apply is still open (needs `r8j`). Don't pick gates. |

Frozen and unchanged: F1 (signal-path topology), F2 (session-flat / early-close), F4 (MFFU written confirmation). F3's conditional decision stands with its void clause.

## 3. What the Mac side needs from you, in order

### 3.1 The High-resolution plan — one file, named, with hashes
Put it in the same Drive folder. Name it plainly (e.g. `2026-11-02-vm-high-res-plan.md`) and tell Amear the exact filename. It will be copied into `docs/reports/` unchanged and checked against the R-VN3-2 limits. The plan should cover, with every number graded:
1. **What High resolution needs** — the Block 2 spec line is: Order Fill Resolution = High, a 1-tick resolution series, 1-tick slippage, $2.96 round trip (`specs/SPEC_RUBRIC.md` F3). State exactly which Analyzer fields change vs the locked Standard settings (Standard (Fastest), slippage 2 ticks, 1-minute Last, etc.) and what each new field's value would be. Don't run it.
2. **Data** — the per-contract tick data the plan relies on ("option C", Portara). Which contracts, which date range (the 1-min file spans 2021-03-08 → 2026-07-17), expected size, price, licence terms, and how it would be delivered. **A purchase is Amear's decision; present it as a question with the number.**
3. **The build chain** — `TickPrep measure → build → verify` on the real data, step by step, with what each step's acceptance looks like (offsets must equal `nt-implied-offsets.csv`; `verify` exit 0; the unmatched-minute report). What happens at the 2021-06-10 cut-short roll and at DST changes. Which time zone the tick files come in.
4. **The instrument** — the result is a tick file for `NQCONTROW 09-25` (the Future row: $20/pt, tick 0.25, rollover 2021-03-01, Do not merge). Say how a tick import would sit beside the existing 1-min data without touching it, as a plan only — **no import**.
5. **The 0-H control** — Standard vs High on the same strategy, same settings, same dates, to measure the fill-optimism gap. Design only.
6. **Risks and open questions for Amear** — a numbered list. Don't answer them.

### 3.2 Close the hash chain
Run `Get-FileHash` on all **six** original tickprep files on the VM (`TickPrep.cs`, `TickPrep.exe`, `MakeSynth.cs`, `MakeSynth.exe`, `README.md`, `nt-implied-offsets.csv`) and paste the output. Also paste the `csc.exe` version line (first line of its banner). Note the `.csv` byte count on the VM so the 24-byte difference is explained. If the `.cs` hashes differ from §1, say so — the Mac copy is then suspect.

The `.exe` question (commit the binaries, or source only with rebuild steps) is Amear's. If he rules "binaries too", they need a route to the Mac that preserves bytes (Drive upload of the `.exe` files themselves, with VM-side hashes) — not retyped text.

### 3.3 Only if Amear rules it (open items from the 2026-11-01 report)
- Hash-check the three strategy files installed on the VM against the repo copies (`PraxisNoiseAreaBreakout_OppBand.cs`, `_Flat1559.cs`, `PraxisLastHalfHourMomentum.cs`).
- Read-only readback of the trading-hours template's early-close rows (the 12:15-on-13:15-days finding). **Read only.** F2 is frozen.

## 4. Facts about the existing data you can rely on (from the Mac's analysis, OBSERVED on the exported CSVs and the 1-min file copy)
- 1-min file: `NQCONTROW 09-25.Last.txt`, format `yyyyMMdd HHmmss;O;H;L;C;V`, bar END-stamped; 2021-03-08 → 2026-07-17; RTH session CME US Index Futures RTH.
- Exit-on-session-close fills at the close of the 16:00-stamped bar; Flat1559 fills at the open of the 16:00-stamped bar (15:59 price). The grid prints 4:00:00 PM for both.
- 48 weekdays carry no RTH bars (holidays; nine near quarterly rolls — inferred).
- Early-close days: session-close exits are stamped 12:15 on 13:15 days, and 12:00 on 2025-01-20 and 2025-06-19. Recorded only; F2.
- Known-gap days: 2023-04-05, 2024-07-19, 2024-08-02, 2026-07-17 (see R-VN3-3).

## 5. What to bring back
A Drive upload containing: the plan file (§3.1); a short `vm-notes` file with the hash block (§3.2), anything Amear said to you in words (quoted, graded REPORTED BY AMEAR), and your open questions. Then tell Amear: "Tell Code to read the VM plan file and the vm-notes first."

## 6. Do not
- Buy data. Import anything into NT8. Run a backtest. Compile and run `TickPrep` against real data (the self-test on synthetic data is already on record; another run adds nothing until the real data exists and Amear has approved it).
- Edit the trading-hours template, the instrument, the commission template, or any strategy `.cs`.
- Write breaker code or pass-gate rules. Both wait for `r8j`.
- Send files without VM-side hashes.
