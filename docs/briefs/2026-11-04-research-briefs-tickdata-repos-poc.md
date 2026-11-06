# Research briefs — tick data, comparable builds, proof of concept

**Written:** 2026-11-04, Claude.ai Praxis channel, at Amear's request. **Status:** briefs only; nothing dispatched, nothing bought, nothing decided.
**Run as three separate agents.** Each returns one report to `docs/reports/`. They do not read each other's output.
**Standing limitation (carry into every report):** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Rules for all three agents

1. **Research only.** No purchase, no paid sign-up, no download into NinjaTrader, no import, no run, no code change. Any price or licence is a question back to Amear.
2. **Evidence grades on every claim:** OBSERVED (read from a vendor page, repo file, or paper) · INFERRED · UNVERIFIED. Give the URL and the date read.
3. **Sources.** Vendor documentation, exchange documentation, peer-reviewed papers, and public GitHub repositories count. **Forum posts (Reddit, Elite Trader, NinjaTrader forum) may be used as leads only** — every fact taken from one must be confirmed against a vendor page, a repo file, or a paper before it appears in the report. A forum claim that cannot be confirmed is listed in a "leads not confirmed" appendix, not in the findings. (This is Amear's research standard, with forums allowed as leads for this search only.)
4. **No recommendation dressed as a finding.** Rank options by stated criteria; the decision is Amear's.
5. **Do not re-research what the repo already holds.** Read these first and cite them rather than repeating them:
   - `docs/reports/2026-11-02-vm-high-res-plan.md` (Portara $695; what High fill resolution needs; TickPrep)
   - `docs/specs/2026-07-15-block2-backtesting-scope-proposal.md` §data sources table
   - `docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md` (minute vs tick fidelity; the paper used 1-minute data)
   - `DECISIONS.md` D-2026-10-30-A (cost model), D-2026-11-02-A/B/C, D-2026-11-03-A, D-2026-11-04-A
   - Project doc "PHASE 3 — BUILD SPECIFICATION" (pass gates; FirstRate $75–225)

## Project facts the agents need (OBSERVED from the repo unless marked)

- Instrument: NQ (E-mini Nasdaq-100), RTH 09:30–16:00 ET, strategy entries on the 1-minute bar at HH:00/HH:30 checkpoints, market orders only, flat by 16:00.
- Data held: one 1-minute continuous file, 2021-03-07 → 2026-07-20, end-stamped Eastern, imported into NT8 as a Future instrument `NQCONTROW`. No tick data (`db\tick` = 0 files).
- Platform: NinjaTrader 8.1.7.2 on a Windows 11 ARM64 VM (VMware Fusion, Apple silicon). Execution path: TradingView → n8n → NT8 file drop → Rithmic → MyFundedFutures. Automation is permitted by MFFU in writing; no HFT, no sim-fill exploitation.
- Baseline backtest (Standard fill resolution, 2 ticks/side, $2.96 RT): 1,190 trades, PF 1.29, max DD −$45,282, 2021-03 → 2026-07. Two variants run; one strategy retired.
- Walk-forward and circuit breakers are not built yet (`r8j`, the Phase 3 spec import, is the blocker).
- Declined: Portara at $695 (Amear, 2026-11-03). Ruling R-1104-3: no tick-data purchase until Standard-resolution results show proof of concept — "proof of concept" is not yet defined.
- Tool on hand: `tools/tickprep/` (TickPrep.cs, MakeSynth.cs) — converts per-contract tick files to NT8 import format and back-adjusts.

---

## Brief A — Tick data for NQ, 2021-03 → present

**Question:** what are every realistic way to get NQ tick (trades-only is enough; bid/ask is a bonus) data covering 2021-03-08 → 2026-07-17, at what cost, in what format, and what does each one need to become an NT8 tick series on this VM?

**Enumerate, at minimum:** Databento (GLBX.MDP3, trades schema), Kibot, FirstRate Data (confirm whether they sell tick, not just 1-minute), TickData.com / TickWrite, Portara/CQG (already priced — cite, don't redo), IQFeed/DTN (historical tick depth and whether a subscription can be used for a one-time backfill), Kinetick (paid tiers), NinjaTrader's own Continuum/NT data (what the free and paid tiers actually give for historical tick), Rithmic history through an MFFU or NT-sim connection (how many days back), Barchart OnDemand, Polygon.io futures, CME DataMine (Top-of-Book / Time and Sales), and any academic or open dataset (e.g. university-licensed CME data, Kaggle/Zenodo mirrors — note licence).

**For each source, one row:** coverage dates for NQ; per-contract or continuous; trades-only vs bid/ask; timestamp precision and zone; file format; price (one-time vs subscription; cheapest route to *this* window); licence terms on backtest use; export/import path into NT8 (native, via TickPrep, or needs new code); whether the vendor's own back-adjustment is documented; evidence grade and URL.

**Also answer:**
1. Cheapest route to a *partial* tick set — e.g. the most recent 12 months only — if a full-window purchase is deferred. Which sources sell by month or year?
2. Can NT8 run High fill resolution with ticks for *part* of the window and Standard for the rest, or is it all-or-nothing? Cite NT8 documentation.
3. Free collection forward: if an NT8 connection to Rithmic sim or Kinetick is opened today, what tick depth does it store, and does opening it violate Amear's standing "no other connection" condition (D-071)? Flag; do not act.
4. Is 1-second or volume-bar data a cheaper intermediate that gets most of the fill-fidelity benefit? Cite anything quantitative.

**Deliverable:** `docs/reports/2026-11-0X-tick-data-sources.md` — the table, the four answers, a ranked shortlist by (cost, coverage, import effort), and a "leads not confirmed" appendix. No purchase recommendation; a ranking by stated criteria only.

---

## Brief B — Comparable builds on GitHub (and what to adopt)

**Question:** what public repositories implement a retail, automated, intraday futures (preferably index futures) strategy end-to-end — signal → execution on NinjaTrader 8 or a Rithmic/Tradovate/IB bridge → risk controls — and what in them is worth adopting here?

**Search terms to cover (GitHub, GitLab, and papers-with-code):** NinjaScript strategy repos (`NinjaTrader 8 strategy`, `NinjaScript`, `FileSystemWatcher NinjaTrader`, `NinjaTrader webhook`), `n8n trading`, `TradingView webhook futures`, `Rithmic API` wrappers (e.g. `pyrithmic`, `async_rithmic`), `Tradovate API`, intraday momentum / opening-range / noise-area replications (Zarattini, Aziz, Barbon — "intraday momentum" ETF/ES/NQ replications; Quantitativo's replication is already cited in the 08-07 research), walk-forward frameworks for NinjaTrader, prop-firm rule enforcers (daily loss, max contracts, time windows), and "strategy health monitor" / live-vs-backtest divergence tools.

**For each repo (aim for 10–20 that are real, not tutorials):** URL; stars/last commit/licence; language; what it actually does end-to-end (OBSERVED from the code, not the README); how it handles: data source and resolution, rollover/continuous contracts, fill and slippage modelling, walk-forward or OOS validation, circuit breakers / kill switches, prop-firm rule enforcement, logging/journal, live-vs-backtest comparison; evidence of live use (issues, commit history, disclosed results — graded); what is directly adoptable here (name the file and function), what is adaptable with work, what is incompatible (platform, licence, or architecture).

**Specific sub-questions:**
1. Has anyone published a NinjaScript implementation of the Noise-Area / intraday-momentum breakout, or of walk-forward runs driven from outside NT8 (e.g. scripted Strategy Analyzer runs, ATI, or exporting trade lists)?
2. What do the better repos do for the one problem this project has already hit — continuous-contract construction and back-adjustment for NT8 imports? Anything reusable alongside `tools/tickprep/`?
3. What do they do for the proof-of-concept gate — i.e. how do they decide a backtested strategy is worth forward-testing? Quote their criteria.
4. Any repo that models NT8 Standard-vs-High fill resolution differences empirically.

**Deliverable:** `docs/reports/2026-11-0X-comparable-builds.md` — repo table, the four answers, and an "adoptable now / adaptable / not" list with file-level pointers. No code is copied into the repo by this agent; licences noted for Amear.

---

## Brief C — What "proof of concept" means before spending money

**Question:** for a retail systematic intraday futures strategy that has one Standard-resolution 1-minute backtest, what do published practitioners and the academic literature treat as the minimum bar before (a) buying higher-resolution data and (b) forward/paper trading — and how do those bars compare with the gates this project already wrote?

**Sources:** peer-reviewed and SSRN papers on backtest overfitting and deflated performance (Bailey & López de Prado — deflated Sharpe, probability of backtest overfitting, minimum backtest length; Harvey & Liu — multiple testing; White's reality check), walk-forward literature (Pardo), the Zarattini–Aziz–Barbon papers' own validation sections, and practitioner books/docs with stated criteria (NinjaTrader's own walk-forward docs; Quantpedia; institutional research notes). Repos found by Brief B may be cited for their criteria but Brief C must not depend on Brief B's output.

**Answer, with numbers where the source gives them:**
1. Minimum sample: how many trades / how many years / how many OOS windows before a PF or Sharpe is distinguishable from noise at this trade frequency (~230 trades/year)? Apply the formulas to this project's 1,190 trades, PF 1.29 and give the computed result, labelled as Claude's arithmetic.
2. Which gates in the Phase 3 spec (OOS PF ≥ 1.30, Sharpe ≥ 1.0, max DD ≤ 4% of equity, ≥ 250 OOS trades, ≥ 60% windows profitable, WFE ≥ 0.50) are standard, which are stricter or looser than the literature, and which cannot be evaluated without walk-forward.
3. Does the literature support the view (08-07 research) that tick data is a *refinement* for a clock-anchored minute-bar strategy rather than a prerequisite? Under what conditions does it become a prerequisite (bracket width vs bar range, intrabar reversals)? Give a test that can be run on the existing 1-minute trade lists to decide which case this strategy is in.
4. A candidate definition of "proof of concept" for R-1104-3, stated as a checklist Amear can accept, edit, or reject — each item tied to a cited source. Mark it PROPOSED, not decided.
5. Cost-of-being-wrong framing: what does a $695 tick purchase buy in decision quality versus running the walk-forward on minute data first? Facts only.

**Deliverable:** `docs/reports/2026-11-0X-proof-of-concept-standard.md` — the five answers, a sources list, and the PROPOSED checklist in its own section.

---

## Sequencing and dispatch notes (for Code)

- A, B, C are independent; run in parallel if the agent budget allows. Web tools are required for all three (the 08-07 research had to go through a browser because praxis agents had none — check before dispatch).
- Each report goes through the normal audit before it is cited anywhere. The 08-07 research is the precedent for an UNGRADED label if the audit chain can't reach it.
- Amear rules on: lifting the forum exclusion beyond "leads only"; any purchase; the proof-of-concept checklist from C. Nothing else comes back to him.
