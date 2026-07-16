# B2 — Ruleset Source Log

**Project:** PRAXIS | **Date:** 2026-07-16 | **Bead:** Praxis_build-2tm
**Companion spec:** `docs/specs/2026-07-16-b2-noise-area-ruleset.md`

## Paper identity (confirmed)
Zarattini, C.; Aziz, A.; Barbon, A. — *"Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY),"* Swiss Finance Institute Research Paper No. **24-97**. First version **10 May 2024**; obtained version **3 Feb 2025**. SSRN abstract id **4824172**. Authors: Concretum Research (Zarattini); Peak Capital Trading / Bear Bull Traders (Aziz); University of St. Gallen + SFI (Barbon).

## URLs fetched
| # | URL | Result |
|---|---|---|
| 1 | `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4824172` (SSRN abstract) | **HTTP 403 Forbidden** via WebFetch — SSRN blocks the fetcher. Abstract recovered indirectly via WebSearch snippet only. |
| 2 | WebSearch: "Zarattini Aziz Barbon Beat the Market ... 24-97" | Located the paper + open-access mirrors (SFI, RePEc, ResearchGate, unisg Alexandria). |
| 3 | `https://alexandria.unisg.ch/bitstreams/a99aba00-f967-49b3-aceb-f544dc386e0b/download` | WebFetch 405, but **`curl` downloaded the full 43-page PDF (1.9 MB, PDF v1.5)** — this is the authoritative full text. |
| — | PDF read locally (pages 1–18 covering title, abstract, §1 Intro, §2 Data, §3 Strategy Description, §4.1–4.2) | **YIELDED THE RULESET.** §3 (pp. 6–15) contains every entry/exit/band/sizing formula. |

## Paywall / obtainability status
- **SSRN page:** paywalled to the automated fetcher (403). Not needed.
- **Full text:** **FULLY OBTAINED** — open-access St. Gallen repository PDF, the Feb-2025 revision, complete with all equations and figures. No part of the ruleset relied on an abstract-only snippet.

## What was obtainable vs not
- **Obtained (paper-verified):** band formula + 14-day lookback + minute-of-day anchor + overnight-gap adjustment (§3 pp. 6–7); semi-hourly HH:00/HH:30 entry trigger, long/short direction, reverse-on-opposite-cross, multi-position-per-session (§3 p. 9); opposite-band and max/min(band,VWAP) trailing stops with 09:30-anchored market-hours VWAP (§3 pp. 9,13); 16:00 cash-close flat, no profit target (§3 pp. 9,12; abstract); vol-target sizing σ=2%/4×-cap and cost model (§3 pp. 10,15).
- **Not applicable / absent in paper:** no parameter search grid (paper uses fixed values + discrete model variants, no walk-forward); **no ATR-based stop**; **no "noise multiplier"** (band is exactly 1×σ); **no 11:30 time-stop** (only 16:00); **no NQ test** — paper is SPY-only.

## Confidence per extracted item
| Item | Confidence | Basis |
|---|---|---|
| 1. Band construction + gap adj. | **High** | Verbatim equations, §3 pp. 6–7 |
| 2. Breakout trigger + positions/session | **High** | §3 p. 9 prose + Table 4 trade counts |
| 3. Parameters/defaults | **High (defaults) / High (no grid)** | §3 pp. 6–15; confirmed paper runs no optimization |
| 4. Exit + 16:00 flat | **High** | §3 pp. 9,13; Fig. 2/4 captions |
| NQ transfer | **N/A from this paper** | Paper is SPY-only; NQ = third-party replication |

## Key finding for the auditor
The paper was **fully obtained** and all four required items are **paper-verified**. The material gaps are not gaps in the paper but **PRAXIS-vs-paper divergences**: the "one-position-per-session," the "09:30–11:30 / flat-by-11:30" window, and the tunable "noise multiplier / stop-ATR" are **PRAXIS framings absent from the paper** and are logged as trader decisions in the spec §7. The single most consequential one is the **flat time (16:00 paper vs 11:30 PRAXIS)** — it invalidates direct transfer of the paper's Sharpe/DD if truncated.
