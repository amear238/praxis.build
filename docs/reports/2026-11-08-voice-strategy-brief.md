# PRAXIS — strategy brief for Amear's voice session (2026-11-08)

Written by praxis-master at Amear's request ("put together a brief for me to discuss and strategise the next steps and coming close to final step of this build"), while unit U8 (filing D-2026-11-08-C) runs. **For discussion only. Nothing in here is a decision.** Grades: OBSERVED = read by the master today; REPORTED BY = a document or ledger row says so and the master has not re-checked it; INFERRED = the master's arithmetic or reasoning. Every question in §4 is Amear's to answer.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

---

## 1. Where it stands, in one paragraph

The project is in **Block 2 (Backtesting)** of six (Phase 3 spec, `docs/specs/2026-11-05-phase3-build-specification.md:46–152`). Block 1 (the signal pipe) is signed off for the internal path only. Today, three commits landed: your rulings R1–R9, your answers A1–A11, and the rubric change ("Amear decides; agents write"; O1 closed). Your C1–C10 are being filed now. The walk-forward **design** is ruled almost completely. The walk-forward **run** has not happened: none of tests T1–T13 has run, the arm (b) strategy code is written but never compiled, and the VM session has not started. **No component of Blocks 3, 4 or 5 exists in code.** All nine circuit breakers are specified only (`docs/specs/2026-11-05-phase3-build-specification.md:11`).

## 2. The road to the final step, block by block

| Block | What it proves | Status today | What blocks it |
|---|---|---|---|
| 1 Foundation | Signal pipe end to end | Signed off, internal path only (rubric O3, OPEN) | Public ingress deferred to Blocks 4–5 |
| 2 Backtesting | The strategy has an edge that survives walk-forward | Design ruled; nothing run | VM step 0 → T1–T13 on the VM → walk-forward runs → gates |
| 3 Circuit breakers | Each of the 9 breakers blocks orders, tripped on sim | Specified only | **F1 FROZEN**: no live-signal topology doc exists (`ls docs/specs` finds none, OBSERVED). **F2 FROZEN** until you approve the breaker values (A6) |
| 4 Paper trading | Execution quality on MFFU sim, 6 weeks / 25 trades, through FOMC, NFP and a rollover | Not started | Blocks 2 and 3; **F4 FROZEN** |
| 5 Graduated live | 1 MNQ → 1 NQ → full size, with kill criteria | Not started | Block 4; F4; your sign-off |
| 6 Satellites | More strategies, one at a time | Research only (R6) | Block 5 stable |

The Phase 3 spec's own milestones for Blocks 4 and 5 (`:113–151`, OBSERVED): paper is judged on **execution, not P&L**. That means signal ≤ 2 s, order ≤ 250 ms, bracket within 1 s ≥ 99%, live within ±15% win rate and ±25% average trade of backtest, ≥ 90% hands-off sessions, and every breaker tripped on live data. Live goes 1 MNQ (2 weeks + 10 trades), then 1 NQ (4 weeks + 20 trades), then full size. Five kill criteria apply, one of them "account drawdown exceeds 60% of MFFU trailing DD room".

## 3. The strategic question to put first: drawdown against MFFU's limits

This is the master's arithmetic on figures already in the repo. It is INFERRED, not tested, and it is the thing most likely to decide whether the "final step" is reachable on MFFU at all.

- **The backtested baseline's max drawdown** (PraxisNoiseAreaBreakout, BandOrVWAP, 1 NQ, 2021-03-08 → 2026-07-17): **−$45,282.04** (`docs/reports/2026-11-01-three-strategy-results.md:402`, REPORTED BY that report, from NT8's CSVs). The same row gives net $197,327.60, PF 1.29 and win rate 40.67%. OppBand: −$50,748.88. Flat1559: −$40,637.04.
- **Your A4 gate**: backtest max DD must stay **below 80% of the lower of 4% of the account and MFFU's trailing limit**. The largest MFFU limit in the per-tier table is **$4,500** (150K plans; `docs/specs/2026-11-05-walk-forward-spec.md:113–132`, REPORTED BY MFFU's pages, fetched 2026-11-05). That gives an A4 ceiling of **$3,600**.
- **INFERRED:** at 1 NQ, the whole-period baseline drawdown is about 12.6× that ceiling. At 1 MNQ (÷10, before the MNQ commission difference) it is about $4,528, still above $3,600.
- **Caveats that cut both ways.** None of these is resolved:
  1. The gate is judged per walk-forward window, not over the whole five years. A window's worst drawdown can be smaller than the whole-period figure.
  2. The 2026-11-01 runs used the 08:31-stamped session start. R1 says 09:30, and the runs are likely to be re-run (conditional on the template read).
  3. The runs had **no breakers**. Breaker #1 (daily loss limit) and #3 (two-and-done) would truncate losing days and could cut the drawdown materially.
  4. The fills are optimistic, so live drawdown would be worse, not better.
- **Why it matters.** If arm (a) cannot pass gate 3 at any tier, then by your R2 there is no GO, however good the other gates look. That would make the breaker values (F2) and position sizing the real lever, not the walk-forward tuning.

**Suggested first discussion:** do you want a cheap, Mac-only, read-only check before the VM work? It would compute per-window worst drawdown at 1 MNQ on the three committed 2026-11-01 trade lists, with and without a simulated daily-loss cap. The scripts in `scripts/wf/` already compute windows and drawdowns. It would tell you within one unit whether the MFFU route is viable before weeks of VM and breaker work.

## 4. Decisions for the voice session (yours; options listed, none picked)

1. **Drawdown viability check (§3):** run the Mac-only per-window drawdown check now, or wait for the VM walk-forward?
2. **Sizing and venue:** if the per-window drawdown does not fit, which is it?
   - (a) breaker values do the work (F2 proposal designed around the DD ceiling);
   - (b) MNQ only, through paper and live;
   - (c) a larger MFFU tier;
   - (d) own capital, which also reopens FOMC Even-Week (R9).
3. **Order of the remaining Block 2 work.** The committed plan is: VM step 0 → bridge → 2a hand-tab partial pass → T1–T13 → walk-forward. Do you want the VM session started as soon as the handoff carries your step-0 answers (C10)?
4. **F1 (live-signal topology).** It is still frozen and nothing is written. It blocks all of Block 3. Do you want the topology doc drafted next to the breaker proposal (F2), since the two decide where the breakers sit?
5. **F4 (MFFU automation permission).** The two evidence reports, the 2026-08-07 written confirmation via a support rep and the 2026-10-28 "Davi" reply, are **staged since August/October and never committed** (they are among the 12 old staged paths). The rubric still reads F4 FROZEN. Do you want them landed and graded against F4's criterion ("Written confirmation from MFFU that this specific automation pattern is permitted on a funded account")?
6. **The P0 guard bugs.** Five P0 beads are open, all about the producer/grader guarantee being evadable: `hwk` quoting defeats commit guards; `s8g` unguarded write path to `.claude/agents/`; `1ys` spawn-guard bypass; `22q` commit-gate contradiction; `dj2` k7 ratification. Fix before Block 3, or accept as known risk while only docs and specs move?
7. **The VM as a working seat.** Guard hooks cannot run there: no Git Bash (REPORTED BY the VM session). Keep the VM as a hands-only executor with the Mac as the only master (your 15:11Z ruling), or plan for Git for Windows later?
8. **What "final step of this build" means to you:** the end of Block 5 phase B (1 NQ live, promoted), or the end of Block 4 (paper pass)? This decides what the master plans backwards from.

## 5. In flight in Code now (REPORTED BY master, DECISION_LOG `19:12:30Z`)

Serial, one manager at a time, each audited before commit:
1. U8 files D-2026-11-08-C.
2. U7 walk-forward spec amendment resumes (C1).
3. Rubric unit: the C2 park-rule text, C6 O1 section move, and C8 July hunk.
4. Values-spec unit (C5).
5. VM handoff unit: C3, C9 and C10 step-0 answers into §2, R1's template read, and C3(4) on the go-live list.
6. Manager agent memory off (C7).
7. Commit-gate hook exemption for park commits (C2, trip-tested).
8. Then housekeeping (U2), the F2 breaker PROPOSAL (U4, values back to you as PROPOSED) and R6 research (U5, own branch).

## 6. Honest gaps the master would raise if not asked

- **Today's process cost:** two audit failures parked one unit, and the gate's token minter refused one real PASS on a keyword count. Every unit runs a 10–60-turn manager plus an independent auditor. Throughput is about one landed unit per hour on docs. Code units will be slower.
- **Nothing NT8-side has been observed since 2026-11-01.** All of today's work is specification and filing.
- **Four managers wrote to their own memory folder against their briefs.** C7 addresses it. Until then, no brief-only prohibition is a control.
- **The rubric's S9 and the absolutes rule mean the gate change in C2 must be trip-tested** before anyone relies on it.
