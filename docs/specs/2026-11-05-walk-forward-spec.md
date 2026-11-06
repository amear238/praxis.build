Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

# Walk-forward test specification — NQ Noise-Area, arms (a) and (b)

**Status: DERIVED — not yet ruled on as a whole by Amear.**
Derived 2026-11-05 by praxis-worker, unit `2026-11-05-r8j-phase3-import-and-wf-spec` (bead `Praxis_build-r8j`), under Amear's typed item b (quoted in §1). No design choice is added here. Anything the rulings do not fix is a numbered question in **NEEDS AMEAR** at the end, not a default.

**Sources (every pointer below was taken from `grep -n` / `nl -ba` output in this session):**
1. `DECISIONS.md:803` — `## 2026-11-05 — D-2026-11-05-A`, five items at `:812-816` (REPORTED BY the voice agent, filed WHO: amear, `:806`, `:811`).
2. `DECISION_LOG.md` row prefix `[2026-11-05T23:50:09Z] WHO: amear` (typed by Amear, "verbatim"). Cited by prefix only, because rows shift.
3. `DECISION_LOG.md` row prefix `[2026-11-05T23:51:21Z] WHO: amear` (R-VN4-1..14, REPORTED BY the voice agent from notes-4). Cited by prefix only.
4. `docs/specs/2026-11-05-phase3-build-specification.md` (188 lines, sha256 `cd02d34ae635626e674f4316bdfd9ac14d96f819aaf28d39b7d651607be69b83`): import note `:3`, STATUS note `:11`, Block 2 heading `:62`, config `:76`, "Pass gates (non-negotiable):" `:78`, gates `:80-85`, "No partial passes" `:87`, milestone `:89`, breaker 6 `:102`.
5. `specs/SPEC_RUBRIC.md` F3 `:45-57`, O1 `:74-79`, O4 `:94-99`.
6. `docs/reports/2026-11-04-proof-of-concept-standard.md` (report C) §2 `:118-143` and NEEDS AMEAR `:245-257` — context only.
7. MFFU tier capture, fetched 2026-11-05T23:58:43Z .. 2026-11-06T00:00:28Z UTC (local date 2026-11-05) by another worker in this unit, scratchpad file `r8j/w2-mffu-tiers.txt` (not in the repo).
8. Data file `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt` (outside the repo), named at `DECISIONS.md:257`.
9. Baseline `ninjascript/PraxisNoiseAreaBreakout.cs`.
10. `DECISIONS.md:485` — `D-2026-11-02-C` (Status "RULED by Amear — R-VN3-3..6", `:488`): R-VN3-3 `:494-499`, R-VN3-5 `:508-513`, R-VN3-6 `:515-521`, its NEEDS AMEAR `:530-544`.
11. `DECISIONS.md:736` — `D-2026-11-04-A`; R-1104-3 at `:752-757`.
12. `DECISION_LOG.md` row prefix `[2026-11-05T23:53:32Z] WHO: praxis-master` — the master's dispatch of step (d), the MFFU fee check. Cited by prefix only.

**Evidence grades used:** RULED (Amear's own typed words, or a ledger entry with Status RULED) · REPORTED BY <who> (a record made by someone other than Amear, or an outside page) · INFERRED (worked out by the deriver; not a ruling) · UNVERIFIED (not checked). Readings by the voice agent or the master are labelled as readings, not as his words.

**"RULED (D-2026-11-05-A)"** is used below for any of the five D-2026-11-05-A items. It means: entry Status "RULED by Amear — items 1–5", graded there REPORTED BY the voice agent, filed WHO: amear (`DECISIONS.md:806`). The words are the voice agent's record, not a transcript of his speech.

## 1. Rulings this spec rests on (verbatim)

**D-2026-11-05-A, the five items** — REPORTED BY the voice agent, pasted by Amear with "file as WHO: amear" (`DECISIONS.md:806`, `:811`); entry Status "RULED by Amear — items 1–5" (`:806`). Quoted from `:812-816`:
- *"1. Walk-forward runs BOTH ways: (a) paper's fixed rules, nothing optimised; (b) four parameters tuned per window — lookback, noise multiplier, stop-ATR multiplier, exit policy. A stop is added to the strategy for (b) on its own branch; baseline file unchanged."*
- *"2. Windows per spec: 252-day in-sample / 63-day out-of-sample / 63-day step."*
- *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used."*
- *"4. Every window also reports worst drawdown at 1 MNQ and 1 NQ against each MFFU tier's limit."*
- *"5. Account tier: no decision until backtest + paper results exist."*

**Typed ruling 1** — RULED (DECISION_LOG `[2026-11-05T23:50:09Z] WHO: amear`, "typed, verbatim"):
> "Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest. Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands."

**Typed item b** — RULED (same row):
> "derive the walk-forward spec from the 2026-11-05 addendum (both arms, 252/63/63, DD gate = lower of 4% of MFFU account or MFFU trailing limit, per-window DD at 1 MNQ and 1 NQ vs every MFFU tier)"

**Typed item c** — RULED (same row):
> "c. Walk-forward build: arm (a) on the unchanged baseline; arm (b) on its own branch with the four tunables and the bar-close stop. Build and test on existing minute data only."

**Typed item d (cost)** — RULED (same row):
> "d. Cost model: read MFFU's fee page; if $5.76 RT all-in is confirmed, amend by new DECISIONS entry. If the page can't be read, log it and keep $2.96 — do not guess."

**D-2026-11-02-C — R-VN3-3, R-VN3-5, R-VN3-6** — entry Status "RULED by Amear — R-VN3-3..6" (`DECISIONS.md:488`). Amear's words are as notes-3 records them; every other part keeps the grade the entry gives it:
- R-VN3-3 (`:494-499`): Amear's words "I would just proceed as it is." (`:495`). Settles (`:498`): "the 1-minute data (date range 2021-03-08 → 2026-07-17, results report line 88) is used as it is; no re-sourcing or re-import of the holes or gaps; future backtest reports on this data carry them as a stated limitation." — RULED. Applied in §5.
- R-VN3-5 (`:508-513`): Amear's words "If they're not live, then they're not live." … "Yeah, once uh, once it goes through." (`:509`). The outcome, that the backtest runs "with the breakers on, once they are built", is graded in the entry as the "Agent's reading, confirmed by Amear in voice only" (`:510`; Settles, `:512`). Applied in §9.
- R-VN3-6 (`:515-521`): Amear's words "one that is closest to live execution." (`:516`). The agent's reading "meaning High fill resolution and breakers on" (`:517`) is recorded "as the agent's reading and not as Amear's ruling" (`:520`). It names no arm. Applied in §8.

**D-2026-11-04-A — R-1104-3** (`DECISIONS.md:752-757`): Amear's word is "Yeah" (`:753`). The meaning is the brief's framing, not his words (REPORTED BY the brief): "= High fill resolution with circuit breakers on as the judged go/no-go version, confirming R-VN3-6. The row does not record the question he answered." (`:753`). The entry also says it "Does not clear O1." (`:757`). It names no arm. The entry's Status as written: "RULED by Amear — R-1104-1..3, graded REPORTED BY AMEAR." (`DECISIONS.md:739`). The R-1104-3 block also says: "Closes D-2026-11-02-C NEEDS AMEAR 14 (DECISIONS.md:544). That closure label is in the ledger row's framing. Amear's own word is "Yeah"." (`DECISIONS.md:754`).

**R-VN4 items** — REPORTED BY the voice agent (DECISION_LOG `[2026-11-05T23:51:21Z] WHO: amear`; his words column from notes-4; text in parentheses is the voice agent's reading, not his words):
- R-VN4-2 breakers as resting stops?: "Until the account is live … resting stops." Asked which: "The latter."
- R-VN4-3 walk-forward on minute data: "Yes."
- R-VN4-5 data gaps: "As long as the data that I generated came back similar to … what is found online, I'm happy to move on."
- R-VN4-7 proof of concept: "Proof of concept is having the full trading pipeline existing and having it run in real live markets on a sim account." / "We're just gonna proceed without that [historical tick data]." (reading: R-1104-3 defined as Block 4 on sim; no tick purchase; report C's PROPOSED checklist not adopted)
- **Not ruled (stay open, from the notes):** past GitHub-login use (no remedy requested); second Rithmic read-only connection; CME wiki as a source; equity base and Sharpe definition; O1 gate set / WFE with no optimisation.

R-VN4-7's reading says report C's PROPOSED checklist is not adopted. This spec does not use that checklist (report C `:180`).

## 2. Arm (a) — the paper's fixed rules, nothing optimised

- What: the paper's fixed rules, nothing optimised (item 1a, `DECISIONS.md:812`). — RULED (D-2026-11-05-A). It runs on the unchanged baseline (typed item c). — RULED (typed).
- Code: `ninjascript/PraxisNoiseAreaBreakout.cs`, sha256 `35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265`, last git revision touching it `719ab11` (`719ab11f89623f9fb33eaac79ac36f839eec75de`, 2026-07-16 15:41:01 -0400). `git status --short` on the file was empty, so the working copy matches that revision. — OBSERVED this session (pasted in the unit report `docs/reports/2026-11-05-r8j-phase3-import-and-wf-spec-manager.md` (section "Verification evidence")).
- Item 1 adds the stop for arm (b): "A stop is added to the strategy for (b) on its own branch; baseline file unchanged." (`:812`). — RULED (D-2026-11-05-A). Arm (a) therefore runs with no added stop. — INFERRED (from item 1).
- In arm (a), no parameter is tuned in-sample. How arm (a) uses the 252/63/63 windows is not stated, for example whether results are reported only on the out-of-sample windows. → NEEDS AMEAR 17.

## 3. Arm (b) — four tunables plus a bar-close stop

- Tunables, tuned per window: lookback, noise multiplier, stop-ATR multiplier, exit policy (item 1b, `:812`; Block 2 config, Phase 3 spec `:76` names the same four). — RULED (D-2026-11-05-A).
- In-sample / out-of-sample use: parameters are tuned on each in-sample window and applied to the next out-of-sample window. This is the standard meaning of "Rolling walk-forward optimization" (Phase 3 spec `:76`). — INFERRED from Phase 3 spec `:76` together with item 1b. The ledger rulings do not use the words "applied to the following out-of-sample window". → NEEDS AMEAR 23.
- Stop: "evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest." (typed ruling 1). — RULED.
- Branch: arm (b) is built "on its own branch with the four tunables and the bar-close stop" (typed item c). The baseline file stays unchanged (item 1). — RULED (typed item c; item 1 is RULED (D-2026-11-05-A)). The branch name is not ruled. → NEEDS AMEAR 14.
- The candidate set for each tunable, the exit-policy options, the ATR period behind the stop-ATR multiplier and the in-sample objective are not ruled. → NEEDS AMEAR 1–6.
- Held fixed: the Block 2 config says "Session window and clock times held fixed." (Phase 3 spec `:76`). — REPORTED BY the imported Phase 3 spec. It is not restated in any 2026-11-05 ruling.

## 4. Windows — 252 / 63 / 63

- "252-day in-sample / 63-day out-of-sample / 63-day step" (item 2, `:813`; same figures at Phase 3 spec `:76`). — RULED (D-2026-11-05-A).
- **Day-count convention used here: one "day" = one trading session present in the data file, counted as a Monday–Friday calendar date that has at least one bar stamped 09:31:00–16:00:00 (inclusive; file times are treated as bar-end stamps (INFERRED by Claude, `DECISIONS.md:257`)).** — **INFERRED.** No ruling states the convention. Calendar days, or an exchange calendar (which would count sessions missing from the file and drop weekday exchange holidays), are the alternatives. → NEEDS AMEAR 15, 26.
- Measured session counts (commands and output in the unit report `docs/reports/2026-11-05-r8j-phase3-import-and-wf-spec-manager.md` (section "Verification evidence")):
  - whole file: 1,494 dates with a bar in 09:31–16:00. Of these, **141 are Saturday or Sunday dates** (44 Saturdays, 97 Sundays), carrying 201 bars stamped 09:31–16:00; the first three are 2021-03-14, 2021-03-20 and 2021-03-28. — OBSERVED data fact; no explanation for them is claimed here. → NEEDS AMEAR 26.
  - whole file, Monday–Friday dates only (the convention above): **1,353** (first 2021-03-08, last 2026-07-20).
  - All distinct dates in the file, including evening-only stamps: 1,712 (not used, because evening-only dates are not trading sessions under the convention above).
  - inside the run-4 range 2021-03-08 → 2026-07-17 (`DECISIONS.md:257`, REPORTED; the same range R-VN3-3 settles, `DECISIONS.md:498`), Monday–Friday dates only: **1,352**.
  - Whether weekday exchange holidays appear among these dates was not checked (no exchange calendar is on the ledger). → NEEDS AMEAR 26.
- Window arithmetic (INFERRED; rolling, so window k's in-sample is sessions 63(k−1)+1 … 63(k−1)+252 and its out-of-sample is the next 63):
  - full windows = floor((N − 252) / 63)
  - N = 1,353 (whole file): (1,353 − 252) / 63 = 1,101 / 63 = 17 remainder 30 → **17 full windows**, 17 × 63 = 1,071 out-of-sample sessions, 30 sessions left over
  - N = 1,352 (run-4 range): 1,100 / 63 = 17 remainder 29 → **17 full windows**, 1,071 out-of-sample sessions, 29 left over
  - These counts hold only under the INFERRED convention; treating the weekend-dated bars or weekday holidays another way changes them (→ NEEDS AMEAR 26). An earlier draft of this spec counted all dates, weekend dates included; that count is withdrawn.
  - Whether a partial last out-of-sample window (29 or 30 sessions) counts is not ruled. → NEEDS AMEAR 16.

## 5. Data — the existing 1-minute file, as is

- R-VN4-3 "Yes." to walk-forward on minute data (REPORTED BY the voice agent). Typed ruling 1: "Minute data is sufficient for arm (b). No tick purchase." (RULED). Typed item c: "Build and test on existing minute data only." (RULED). **Nothing is bought.**
- File: `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt`, 95,900,139 bytes, sha256 `307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454`, 1,857,362 lines, first row `20210307 180100`, last row `20260720 112700`. — OBSERVED this session. This matches the first row, last row and line count recorded at `DECISIONS.md:257`.
- Series name: the ledger names it `NQCONT`, "the Python-stitched continuous series (volume-only crossover roll + Difference back-adjustment, D-2026-07-17-A / D-2026-07-21-A)" (`DECISIONS.md:257`). The NT8 import record: the file was imported as "NQCONTROW 09-25.Last.txt" (95,900,139 bytes, confirmed on VM) (`docs/reports/2026-10-31-voice-session-notes-2.md:16`), and typing "NQCONTROW 09-25" loaded bars (`:18`), with the line's own qualifier: "but only from 2025-12-01. VM agent read the MasterInstruments copy: one contract month, 09-25, rollover 2025-12-01, merge = global (MergeBackAdjusted)." (`:18`) — REPORTED BY AMEAR (via the voice agent's summary, pasted by Amear; notes header `:3-6`; also DECISION_LOG row prefix `[2026-10-31T18:19:03Z] **WHO: amear**`). The byte count equals the file above; that is a size match only (INFERRED). That the NT8 database copy holds exactly this file's bars is UNVERIFIED here (no NT8 access in this unit).
- **Data holes and gaps — R-VN3-3, RULED** (D-2026-11-02-C, `DECISIONS.md:494-499`; quoted in §1): "I would just proceed as it is." The data is used as it is; nothing is re-sourced or re-imported for the holes or gaps (`:498`).
- **Stated limitation (carried by this spec, and by every walk-forward report on this data, per R-VN3-3 `:498`):** the data contains, unrepaired, the two 17-day holes "2021-09-09 → 2021-09-27 and 2025-12-14 → 2026-01-01" and the three gaps "**Three known gaps are wider than recorded**": "2024-07-19 09:58–10:07 (line 59), 2024-08-02 11:55–12:02 (line 60), 2026-07-17 10:59–12:06 (line 61)" (all `DECISIONS.md:497`, as recorded in `docs/reports/2026-11-01-three-strategy-results.md`). The entry notes that "The known-gap day 2023-04-05 (line 62) is not one of the three and is not named by the ruling." (`:497`).
- Not settled by R-VN3-3 (quoted, not answered): report C NEEDS AMEAR 7 (report C `:253`) also names "the 12:15 early-close template"; R-VN3-4 states "the early-close stamp question (handoff §5 item 1) is separate and not ruled" (`DECISIONS.md:506`). That these two are the same item is INFERRED (the deriver's reading that these are the same item). D-2026-11-02-C NEEDS AMEAR 7 (`DECISIONS.md:537`) asks whether "proceed as it is" covers each hole's effect on the 14-day lookback. The master's reading at `DECISIONS.md:822` counts "33 missing sessions"; the ledger does not say whether those are the holes R-VN3-3 covers. R-VN4-5 (quoted in §1) was said later and is conditional ("As long as the data that I generated came back similar to … what is found online"). → NEEDS AMEAR 18.

## 6. Max-drawdown gate — base and per-tier table

- Original Block 2 gate wording: "Max drawdown ≤ 4% of equity" (Phase 3 spec `:82`). Item 3 rules its base: "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used." (`:814`). — RULED (D-2026-11-05-A).
- Item 5 defers the tier: "Account tier: no decision until backtest + paper results exist." (`:816`). — RULED (D-2026-11-05-A). **This spec does not choose a tier.** The table lists every tier read from MFFU's pages. → NEEDS AMEAR 11–12.
- The imported spec's breaker list carries the figure "MFFU’s $1,500 EOD trailing drawdown" (Phase 3 spec `:102`). D-2026-11-05-A does not adopt it (`DECISIONS.md:820`). The only $1,500 limit on the pages read is Builder 50K with add-on (row below). → NEEDS AMEAR 20.

**Per-tier table.** "Lower" = min(0.04 × size, MFFU limit). Arithmetic is INFERRED (deriver's arithmetic). Size and limit are REPORTED BY MFFU's page named in each row, fetched 2026-11-05 (UTC window 23:58:43Z–00:00:28Z). In the capture, the stage labels on `/plans/*` tables were INFERRED from tab order.

| Plan · size | Account size | 4% of size | MFFU limit (type, stage) | Lower of the two | Grade / source |
|---|---|---|---|---|---|
| Studio #003 · 5K | $5,000 | 0.04 × 5,000 = $200 | $250 (Static, not trailing) | min(200, 250) = **$200** | REPORTED BY MFFU's page https://help.myfundedfutures.com/en/articles/17589665-studio-plans-a-comprehensive-guide, fetched 2026-11-05 |
| Studio #001 · 10K | $10,000 | $400 | $500 (Static) | min(400, 500) = **$400** | REPORTED BY MFFU's page https://help.myfundedfutures.com/en/articles/17589665-studio-plans-a-comprehensive-guide, fetched 2026-11-05 |
| Studio #002 · 20K | $20,000 | $800 | $1,000 (Static) | min(800, 1,000) = **$800** | REPORTED BY MFFU's page https://help.myfundedfutures.com/en/articles/17589665-studio-plans-a-comprehensive-guide, fetched 2026-11-05 |
| Rapid · 25K | $25,000 | $1,000 | $1,000 (Eval EOD; Sim-Funded intraday trailing) | min(1,000, 1,000) = **$1,000** (equal) | REPORTED BY MFFU's page https://myfundedfutures.com/plans/rapid, fetched 2026-11-05 |
| Rapid EOD · 25K | $25,000 | $1,000 | $1,000 (EOD trailing) | **$1,000** (equal) | REPORTED BY MFFU's page https://myfundedfutures.com/plans/rapid-eod, fetched 2026-11-05 |
| Builder · 25K | $25,000 | $1,000 | $1,000 (EOD trailing) | **$1,000** (equal) | REPORTED BY MFFU's page https://myfundedfutures.com/plans/builder, fetched 2026-11-05 |
| Rapid · 50K | $50,000 | $2,000 | $2,000 (Eval EOD; Sim-Funded intraday trailing) | **$2,000** (equal) | REPORTED BY MFFU's page https://myfundedfutures.com/plans/rapid, fetched 2026-11-05 |
| Rapid EOD · 50K | $50,000 | $2,000 | $2,000 (EOD trailing) | **$2,000** (equal) | REPORTED BY MFFU's page https://myfundedfutures.com/plans/rapid-eod and https://help.myfundedfutures.com/en/articles/16158363-rapid-eod-50k-a-comprehensive-look, fetched 2026-11-05 |
| Pro · 50K | $50,000 | $2,000 | $2,000 (EOD trailing) | **$2,000** (equal) | REPORTED BY MFFU's page https://myfundedfutures.com/plans/pro, fetched 2026-11-05 |
| Builder · 50K | $50,000 | $2,000 | $2,000; $1,500 with add-on (EOD trailing) | **$2,000**; with add-on min(2,000, 1,500) = **$1,500** | REPORTED BY MFFU's page https://myfundedfutures.com/plans/builder, fetched 2026-11-05 |
| Rapid · 100K | $100,000 | $4,000 | $3,000 (Eval EOD; Sim-Funded intraday trailing) | min(4,000, 3,000) = **$3,000** | REPORTED BY MFFU's page https://myfundedfutures.com/plans/rapid, fetched 2026-11-05 |
| Pro · 100K | $100,000 | $4,000 | $3,000 (EOD trailing) | **$3,000** | REPORTED BY MFFU's page https://myfundedfutures.com/plans/pro, fetched 2026-11-05 |
| Builder · 100K | $100,000 | $4,000 | $3,000 (EOD trailing) | **$3,000** | REPORTED BY MFFU's page https://myfundedfutures.com/plans/builder, fetched 2026-11-05 |
| Rapid · 150K | $150,000 | $6,000 | $4,500 (Eval EOD; Sim-Funded intraday trailing) | min(6,000, 4,500) = **$4,500** | REPORTED BY MFFU's page https://myfundedfutures.com/plans/rapid, fetched 2026-11-05 |
| Pro · 150K | $150,000 | $6,000 | $4,500 (EOD trailing) | **$4,500** | REPORTED BY MFFU's page https://myfundedfutures.com/plans/pro, fetched 2026-11-05 |
| Builder · 150K | $150,000 | $6,000 | $4,500 (EOD trailing) | **$4,500** | REPORTED BY MFFU's page https://myfundedfutures.com/plans/builder, fetched 2026-11-05 |
| Flex | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED — product group "Flex" present with 0 products in the home page JSON (https://myfundedfutures.com/); no page read |

Contradictions and oddities the capture noted (REPORTED BY the capture; not resolved here, → NEEDS AMEAR 13):
1. Rapid EOD 50K contracts: 3/30 for Eval and Sim-Funded (page and help article), but the third table on `/plans/rapid-eod` shows 4/40.
2. Rapid EOD 50K Sim-Funded "Drawdown Type" cell is "—" on the plan page. The help article says End-of-Day (EOD) Trailing.
3. The Rapid EOD 25K size card renders the literal placeholder "contractLimits".
4. Builder 50K: the card says "Max Drawdown 1.5k or 2k", the table says "$2,000 ($1,500 with add-on)", and the JSON says 2000 with public name "Builder 2.0K".
5. Builder size labels look swapped (cosmetic).
6. Rapid: Eval is EOD and Sim-Funded is intraday trailing. These are two stages, not a contradiction.
7. Studio "Maximum size 5 contracts" (no unit) vs the help article's "5 micros (no minis)".
Also: Studio limits are Static, not trailing. Item 3 says "trailing drawdown limit". → NEEDS AMEAR 12.

## 7. Per-window reporting

- "Every window also reports worst drawdown at 1 MNQ and 1 NQ against each MFFU tier's limit." (item 4, `:815`). Typed item b: "per-window DD at 1 MNQ and 1 NQ vs every MFFU tier". — RULED (D-2026-11-05-A) (item 4); RULED (typed item b).
- Report-row template (columns only; **no results exist**). The columns are INFERRED from item 4 and the six gates; the drawdown measurement basis is open (→ NEEDS AMEAR 21–22):

| Window # | Arm | IS first session | IS last session | OOS first session | OOS last session | Arm (b) chosen lookback / noise mult / stop-ATR mult / exit policy | OOS trades | OOS net P&L ($; contract size → NEEDS AMEAR 29) | OOS PF | IS objective value (arm b) | OOS profitable (Y/N) | Worst DD @ 1 NQ ($) | Worst DD @ 1 MNQ ($) | then, for EACH row of the §6 table: tier limit ($) · DD@1 NQ ≤ limit (Y/N) · DD@1 MNQ ≤ limit (Y/N) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 8. Pass gates (verbatim) and what is open

Block 2, "Pass gates (non-negotiable):" (Phase 3 spec `:78`), lines `:80-85` — REPORTED BY the imported Phase 3 spec:
- OOS profit factor ≥ 1.30
- OOS Sharpe ≥ 1.0
- Max drawdown ≤ 4% of equity
- ≥ 250 aggregate OOS trades
- ≥ 60% of walk-forward windows profitable
- Walk-forward efficiency ≥ 0.50

Phase 3 spec `:87`: "If it doesn’t pass, the strategy doesn’t deploy. No partial passes. No “close enough.”"

Phase 3 spec `:89`: "Milestone: Walk-forward validation report complete. GO / HOLD / REJECT decision made on NQ Noise-Area with your own data, on your own machine, verified by your own eyes."

**Open under rubric O1** (`specs/SPEC_RUBRIC.md:74-79`, OPEN per `DECISIONS.md:819`):
> Walk-forward efficiency ≥ 0.50 is one of six non-negotiable Block 2 pass gates
> and is undefined without an in-sample optimisation step. Deviation D removed
> optimisation from the first pass. **Required:** a written statement of which
> gate set applies to the replication arm and whether GO/HOLD/REJECT sits on the
> replication arm or the later optimisation arm.

Open items, with no answer given here:
- Which of the six gates apply to arm (a) and which to arm (b). The ledger "does not say which gates apply to which arm" (`DECISIONS.md:819`). → NEEDS AMEAR 9.
- Whether "Walk-forward efficiency ≥ 0.50" applies to arm (a), which has no in-sample optimisation. "O1 gate set / WFE with no optimisation" is on R-VN4's "Not ruled" list. The master's reading "(a) has no optimisation step, (b) does" (`:819`) is a reading, not a ruling. → NEEDS AMEAR 8.
- Whether GO / HOLD / REJECT and "No partial passes" sit on arm (a), arm (b) or both. → NEEDS AMEAR 9.
- Which version is judged — context, not an arm choice: R-VN3-6, Amear's words "one that is closest to live execution." (`DECISIONS.md:516`; RULED, D-2026-11-02-C). The agent's reading "meaning High fill resolution and breakers on" (`:517`) is recorded "as the agent's reading and not as Amear's ruling" (`:520`). R-1104-3: Amear's word "Yeah"; the brief's framing "= High fill resolution with circuit breakers on as the judged go/no-go version, confirming R-VN3-6." (`DECISIONS.md:753`). Neither names arm (a) or arm (b). This walk-forward is Standard resolution on minute data (line 1; typed ruling 1) and no breaker is built (§9). → NEEDS AMEAR 25.
- Which arm is R-1104-3's judged version is D-2026-11-05-A NEEDS AMEAR 4 (`DECISIONS.md:832`), still open. The voice agent's R-VN4-7 reading ("R-1104-3 defined as Block 4 on sim") is a reading. → NEEDS AMEAR 10.
- "OOS Sharpe ≥ 1.0": the Sharpe definition and its equity base are on R-VN4's "Not ruled" list (also report C NEEDS AMEAR 2, report C `:248`, for the equity base; report C NEEDS AMEAR 3, report C `:249`, for the Sharpe definition). → NEEDS AMEAR 7.
- Context only, not adopted: report C §2 (`docs/reports/2026-11-04-proof-of-concept-standard.md:118-143`) compares each gate with the literature. Examples: no PF threshold found in the sources it read (`:135`); "Looser than the statistics" for ≥ 250 trades (`:138`); TradeStation's 50% WFE rule of thumb (`:140`). Its PROPOSED checklist (`:180`) is not adopted (R-VN4-7 reading).

## 9. Cross-block (S6), breakers, fills and cost

- **O4** (`specs/SPEC_RUBRIC.md:94-99`):
  > Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end
  > the session after two consecutive losers. Block 4's gate compares live to
  > backtest within ±15% win rate and ±25% average trade P&L. **Required:** a
  > written statement of whether the Block 2 backtest runs with breakers applied,
  > without them, or both — and how the Block 4 gate is satisfiable if they differ.
  **R-VN3-5** (D-2026-11-02-C, `DECISIONS.md:508-513`; quoted in §1): the backtest runs "with the breakers on, once they are built" — graded in the entry as the "Agent's reading, confirmed by Amear in voice only" (`:510`; Settles, `:512`). That O4 asks this of the Block 2 backtest is the entry's "Filer's mapping, not part of the ruling" (`:512`), so that R-VN3-5 covers this walk-forward, and both arms, is INFERRED here. Still open (`:513`): "whether a without-breakers run is also kept (the "or both" option); how the Block 4 gate is satisfiable if the backtest and live configurations differ — the ruling does not address it" (also D-2026-11-02-C NEEDS AMEAR 3, `DECISIONS.md:533`). `:513` also records the breakers as not defined in the repo (…) and not built; they are now specified but not built — the imported Phase 3 spec says "the nine circuit breakers below are SPECIFIED ONLY." and "zero implemented, zero tested, zero tested under failure." (Phase 3 spec `:11`). What the walk-forward runs with while no breaker is built is not ruled (D-2026-11-02-C NEEDS AMEAR 4, `DECISIONS.md:534`, asks a related question). Typed ruling 1 fixes only how breakers and the arm-(b) stop are modelled if present (bar-close evaluation, market exit next bar). → NEEDS AMEAR 19, 24.
- **F3** (`specs/SPEC_RUBRIC.md:45-57`): the Block 2 config (Phase 3 spec `:76`) states "Order Fill Resolution = High, 1-tick resolution series, 1-tick slippage on entries". D-2026-10-30-A (`DECISIONS.md:247`; Status CONDITIONAL, void clause live, `:250`) states Standard resolution on 1-minute bars (`:257`, `:258`) and band-edge slippage [N] = 2 ticks/side (`:258`; the [N] value LOCKED by Amear, `:250`). It supersedes D-2026-07-15-B Q5's "1 tick/side slippage" and "High fill resolution" terms ONLY (`:295`); it does not edit the imported Phase 3 spec, whose import note says the difference "is open under rubric F3" and "this import does not resolve it" (Phase 3 spec `:3`). The standing limitation on line 1 reflects D-2026-10-30-A. — REPORTED from a CONDITIONAL entry (the [N] lock itself RULED by Amear, `:250`). F3 stays as the rubric records it. **This spec does not discharge F3, F1, F2 or F4**, and changes no code, template or config.
- **Cost:** the ledger's current figure is the $2.96 round-turn commission per NQ contract (D-2026-07-15-B Q5, kept by `DECISIONS.md:295`), with $22.96 RT including the 2-tick/side slippage (`DECISIONS.md:258`). The check of MFFU's fee page is the master's dispatch to another unit (DECISION_LOG row prefix `[2026-11-05T23:53:32Z] WHO: praxis-master`, step (d) `2026-11-05-mffu-fee-check`). Amear's own instruction is typed item d (quoted in §1): "If the page can't be read, log it and keep $2.96 — do not guess." **This spec does not change the figure and does not decide it.** The MNQ per-contract cost is not on the ledger. → NEEDS AMEAR 22.
- No NT8 run, import or purchase is authorised or made by this spec.

## NEEDS AMEAR

1. What is the candidate set (values or range and step) for **lookback** in arm (b)?
2. What is the candidate set for the **noise multiplier** in arm (b)?
3. What is the candidate set for the **stop-ATR multiplier** in arm (b)?
4. What are the **exit-policy options** arm (b) chooses among (D-2026-11-05-A NEEDS AMEAR 3, `DECISIONS.md:831`)?
5. What **ATR period**, and on which bar series, does the stop-ATR multiplier use?
6. What is the **in-sample optimisation objective** that picks arm (b)'s parameters each window, and how are ties broken?
7. What is the **Sharpe definition** for "OOS Sharpe ≥ 1.0" (daily or per-trade, annualisation, risk-free rate), and what **equity base** does it use (R-VN4 "Not ruled"; equity base: report C NEEDS AMEAR 2, report C `:248`; Sharpe: report C NEEDS AMEAR 3, report C `:249`)?
8. Does **WFE ≥ 0.50** apply to arm (a), which has no in-sample optimisation (O1)? For arm (b), which WFE formula is used?
9. What is the **full gate set for each arm**, and does **GO / HOLD / REJECT** (with "No partial passes") sit on arm (a), arm (b) or both (O1; D-2026-11-02-C NA 1–2, `DECISIONS.md:531-532`)? Context only: R-VN3-6, "one that is closest to live execution." (`DECISIONS.md:516`), names no arm.
10. Which arm is **R-1104-3's judged version**: arm (a), arm (b) or both (D-2026-11-05-A NEEDS AMEAR 4, `DECISIONS.md:832`)? Context only: R-VN3-6, "one that is closest to live execution." (`DECISIONS.md:516`); R-1104-3's framing "= High fill resolution with circuit breakers on as the judged go/no-go version, confirming R-VN3-6." (`DECISIONS.md:753`). Neither names an arm.
11. Which **MFFU account size / tier** sets the max-DD gate under items 3 and 5, given that item 5 defers the tier until backtest and paper results exist (D-2026-11-05-A NA 1, `DECISIONS.md:829`)? Until then, is the gate judged against every row of the §6 table?
12. For "MFFU's trailing drawdown limit", which **stage** (Evaluation or Sim-Funded) and which **type** (EOD or intraday trailing) counts? Do Studio's **Static** limits count?
13. How should the **MFFU page contradictions** in §6 (items 1–4 and 7) be treated? Is the Builder 50K add-on figure ($1,500) a separate tier?
14. What is the **arm (b) branch name**?
15. What **day-count convention** defines the days in "252-day in-sample / 63-day out-of-sample / 63-day step" (item 2, `DECISIONS.md:813`): Monday–Friday dates in the data file with a bar in 09:31–16:00 (this spec's INFERRED convention), an exchange session calendar, or calendar days?
16. Is a **partial last out-of-sample window** (29–30 sessions at the measured Monday–Friday counts, §4) included or dropped?
17. How does **arm (a)** use the windows: reported only on the same 63-session out-of-sample windows as arm (b), or also on the first 252-session span?
18. **What R-VN3-3 does not settle:** R-VN3-3 settles that the holes and gaps are used as they are (`DECISIONS.md:498`). Not ruled: is report C's 12:15 early-close template (report C `:253`) the same item as R-VN3-4's "early-close stamp question (handoff §5 item 1)", which is "separate and not ruled" (`DECISIONS.md:506`)? That they are the same is INFERRED (the deriver's reading that these are the same item). Whichever it is, is it settled before results are judged? Does "proceed as it is" cover each hole's effect on the 14-day lookback (D-2026-11-02-C NA 7, `DECISIONS.md:537`)? Are the master's "33 missing sessions" (`DECISIONS.md:822`) within R-VN3-3? Does R-VN4-5's condition ("came back similar to … what is found online") add anything to R-VN3-3?
19. **What R-VN3-5 leaves open:** R-VN3-5 runs the backtest "with the breakers on, once they are built" (agent's reading, confirmed by Amear in voice only, `DECISIONS.md:510`, `:512`). Open at `:513` (and D-2026-11-02-C NA 3, `DECISIONS.md:533`): is a without-breakers run also kept (the "or both" option), and how is the Block 4 gate satisfiable if the backtest and live configurations differ? Does R-VN3-5 apply to arm (a), arm (b) or both?
20. Does the spec's "**$1,500** EOD trailing drawdown" figure (Phase 3 spec `:102`) still stand, given that the MFFU pages read on 2026-11-05 show $1,500 only for Builder 50K with add-on?
21. How is **worst drawdown per window** measured: closed-trade, end-of-day or intrabar equity, and from the window start or carried across windows?
22. Is the **1 MNQ** drawdown taken from its own run with MNQ point value and MNQ cost, or scaled from the 1 NQ run? Which MNQ cost applies, given that the ledger carries no MNQ figure?
23. Are arm (b)'s four parameters chosen on each 252-day in-sample window and then applied unchanged to the following 63-day out-of-sample window, or in some other way? (§3 marks the first reading INFERRED.)
24. **Breakers not yet built:** R-VN3-5 is "once they are built" (`DECISIONS.md:510`), and the Phase 3 spec says "zero implemented, zero tested, zero tested under failure." (Phase 3 spec `:11`). Until breakers are built, does the walk-forward run without them as a provisional result, wait for them, or something else (related: D-2026-11-02-C NA 4, `DECISIONS.md:534`)?
25. **Is this walk-forward the judged version?** R-VN3-6's agent reading and R-1104-3's framing name High fill resolution and breakers on (`DECISIONS.md:517`, `:753`); this walk-forward is Standard resolution on minute data with no breaker built. Is its result the go/no-go judgement, or a provisional result until a run closer to live exists?
26. **Weekend-dated bars and holidays:** the file has 141 Saturday/Sunday dates carrying 201 bars stamped 09:31–16:00 (§4, OBSERVED). Are those bars excluded (this spec's INFERRED convention), kept, or treated another way? Do weekday exchange holidays and early closes need an exchange calendar rather than the file's own dates?
27. **Arm (b) stop reference:** what is the stop-ATR distance measured from (for example the entry fill, the signal bar's close, or the band edge), and is the stop fixed at entry or trailing?
28. **Lookback warm-up:** before each in-sample window, how is the lookback warmed up (bars from before the window, or the window's own first sessions), and in arm (b) does the warm-up follow each candidate lookback?
29. **Per-window P&L contract size:** is the "OOS net P&L" column in the §7 template reported at 1 NQ, 1 MNQ or both?
