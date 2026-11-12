# B2 — Noise-Area Breakout: Canonical Ruleset Spec

**Project:** PRAXIS | **Date:** 2026-07-16 | **Bead:** Praxis_build-2tm
**Purpose:** Pin the entry/exit ruleset for the baseline NQ strategy to its academic source, so Block-2 re-implementation (NinjaScript / Strategy Analyzer) is faithful and auditable.
**Source paper:** Zarattini, C., Aziz, A., Barbon, A., *"Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY),"* Swiss Finance Institute Research Paper No. 24-97. First version 10 May 2024; **this version 3 Feb 2025**. SSRN abstract id 4824172.
**Version obtained:** Full open-access PDF, 43 pp., 3 Feb 2025 revision, via University of St. Gallen Alexandria repository (see source log `docs/reports/2026-07-16-b2-ruleset-source.md`). SSRN page itself was 403-blocked; the unisg PDF is the authoritative full text and all citations below are to it.

> **Scope note.** The paper studies **SPY** (the ETF), NOT NQ futures, and trades **all day** (every half-hour, flat at the 16:00 cash close). PRAXIS applies it to **NQ** inside a **09:30–11:30 ET** window. Every place where the PRAXIS framing departs from the paper is flagged below — those departures are trader decisions, not paper-derived facts.

---

## 1. Noise-Area / band construction — PAPER-VERIFIED (§3, pp. 6–7)

The Noise Area is the equilibrium band around the day's Open; the strategy only trades when price leaves it. Construction on day *t*, for each time-of-day `HH:MM` (paper §3, eqs. on pp. 6–7):

1. **Per-day absolute move from Open** (14-day lookback, `i = 1..14`):
   `move_{t-i, 9:30→HH:MM} = | Close_{t-i, HH:MM} / Open_{t-i, 9:30} − 1 |`
2. **Average move (the band half-width σ) at that minute-of-day:**
   `σ_{t, 9:30→HH:MM} = (1/14) · Σ_{i=1..14} move_{t-i, 9:30→HH:MM}`
3. **Boundaries (base form):**
   `UpperBound = Open_{t,9:30} · (1 + σ_{t,9:30→HH:MM})`
   `LowerBound = Open_{t,9:30} · (1 − σ_{t,9:30→HH:MM})`
4. **Noise Area** = `[LowerBound, UpperBound]`.

**Overnight-gap adjustment (PAPER-VERIFIED, §3 p. 7).** To fold in the overnight gap, the reference price is the more extreme of today's Open and yesterday's Close:
`UpperBound = max(Open_{t,9:30}, Close_{t-1,16:00}) · (1 + σ)`
`LowerBound = min(Open_{t,9:30}, Close_{t-1,16:00}) · (1 − σ)`
(After a gap-down the Upper Bound is pushed up by the gap; after a gap-up the Lower Bound is pushed down — see paper prose p. 7.)

- **Clock/time anchor:** session Open = 09:30 ET; σ is indexed by *minute-of-day* elapsed from the open. Bands **widen through the day** (Fig. 1, p. 8), peaking at 16:00.
- **Lookback window:** **14 trading days**, fixed (`i = [1,14]`). No lookback grid is tested in the paper.
- **Noise "multiplier":** there is **NO free multiplier** in the paper — the half-width is exactly `1 × σ` (the raw 14-day average absolute move). A tunable multiplier is a PRAXIS addition, not a paper parameter (see discrepancy table).

## 2. Breakout trigger — PAPER-VERIFIED (§3, p. 9)

- **Entry condition:** at a **semi-hourly checkpoint only** — `HH:00` and `HH:30` — if price is **above** the Upper Boundary → **go long**; if **below** the Lower Boundary → **go short**. Checking only at the half-hour (not tick-by-tick) is deliberate, to avoid acting on transient spikes; the paper shows a breach a few minutes before 10:30 is not acted on until the 10:30 stamp (Fig. 2, p. 9).
- **Direction rule:** long above the band, short below — trend-following the breakout side (p. 8–9).
- **Positions per session:** **NOT capped at one.** A position is held until the close or until price crosses to the **opposite** boundary, at which point it is closed **and reversed** into a new position that direction (p. 9). Realized average trade frequency is **1.3 trades/day** (base opp-band stop) rising to **1.8 trades/day** with the VWAP stop (Table 4, p. 16). Stops, too, are evaluated only at the semi-hourly stamps (p. 9).

## 3. Parameters — defaults the paper uses (NO search grid) (§3–§4)

The paper does **not** run a parameter optimization / walk-forward. It reports fixed values and a few discrete model *variants*:

| Item | Paper value | Cite |
|---|---|---|
| Lookback | **14 days**, fixed | §3 p. 6 |
| Band half-width | `1 × σ` (no multiplier) | §3 p. 7 |
| Checkpoint grid | every `HH:00` / `HH:30` | §3 p. 9 |
| Stop / exit variants tested | (a) opposite band; (b) `max(VWAP, band)`; (c) = (b) + vol-target sizing | Tables 1–3, pp. 11–15 |
| Stop-ATR | **not used** — there is no ATR-based stop anywhere in the paper | — |
| Profit target | **none** (unlimited upside by design; abstract p. 2) | Abstract |
| Vol-target sizing | `σ_target = 2%` daily, leverage capped **4×** | §3 p. 15 |
| Costs assumed | $0.0035/share commission + $0.001/share slippage (IBKR, SPY) | §3 p. 10 |

Sizing formula (§3 p. 15): `Shares_t = ⌊ AUM_{t-1} · min(4, σ_target/σ_SPY,t) / Open_{t,9:30} ⌋`, with `σ_SPY,t` the 14-day daily-return stdev.

## 4. Exit policy + session-flat — PAPER-VERIFIED (§3, pp. 9–14)

- **Base stop:** trailing stop at the **opposite** Noise-Area boundary (long stops at Lower/Upper as it trails; base model = "Stop @ Opp. Band", Table 1). Evaluated only at semi-hourly stamps.
- **Improved stop (paper's preferred model):** trailing stop at **band-or-VWAP**, whichever is tighter to price:
  `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.
- **Reversal:** a cross to the opposite boundary closes and reverses (see §2).
- **Profit target:** none.
- **Session flat:** **all positions closed at the market Close = 16:00 ET** (cash close), never held overnight (Fig. 2 caption p. 9; Fig. 4 p. 12). The paper has **no intraday time-stop** — the only time-based exit is 16:00.

---

## 5. Discrepancy table — paper vs in-repo prose

| # | Rule | Paper (24-97, Feb-2025) | In-repo prose | Verdict |
|---|---|---|---|---|
| D1 | Band half-width | `1 × σ`, no multiplier (p. 7) | RTF: "avg return-from-open over 14-day lookback" — **matches** (no multiplier stated) | ✅ RTF correct; the "noise **multiplier**" in Phase-3 spec / b2-q1 is a **PRAXIS add-on**, not from paper |
| D2 | Lookback | 14 days fixed (p. 6) | RTF: 14-day — matches | ✅ Agree |
| D3 | Gap adjustment | `max/min(Open, prevClose)·(1±σ)` (p. 7) | RTF: "overnight gap adjustments" (direction unspecified) | ✅ Consistent; paper is the precise form |
| D4 | Checkpoint | every `HH:00` and `HH:30`, all day (p. 9) | RTF: "clock half-hour/hour" — matches cadence | ✅ Agree on cadence |
| D5 | Positions/session | **multiple** (reverse on opposite cross; 1.3–1.8/day) (p. 9, Table 4) | RTF & b2-q1 & scope: **"one position/session" / "one bracket/session"** | ❌ **CONFLICT** — paper permits reversal/re-entry; PRAXIS "one per session" is a **deliberate constraint**, not the paper |
| D6 | Exit stop | opposite band, or `max/min(band, VWAP)` (pp. 9,13) | RTF: "VWAP trailing stop" | ⚠️ Partial — paper's stop is band-**or**-VWAP (whichever tighter), not VWAP alone |
| D7 | Session flat | **16:00 ET cash close** (p. 9,12) | RTF: "flat at 16:00 cash close" | ✅ RTF correct |
| D8 | Flat time | **16:00** — no 11:30 stop in paper | b2-q1 report notes a **"flat-by-11:30-ET baseline"** | ❌ **CONFLICT** — 11:30 is a **PRAXIS window choice** (09:30–11:30 active hours), NOT the paper. The paper's edge is measured on full-day holds to 16:00; truncating at 11:30 is untested by the paper and changes expectancy |
| D9 | Instrument | **SPY ETF** (title, §2) | PRAXIS: **NQ futures** | ⚠️ Paper never tests NQ; NQ results in repo prose come from third-party replications (Quantitativo), not this paper |
| D10 | Profit target | none (p. 2) | RTF: none | ✅ Agree |
| D11 | Sizing | `σ_target=2%`, 4× cap (p. 15) | RTF: "2% daily vol target capped at 4× notional" | ✅ RTF correct |

**Net:** The RTF prose is a faithful summary of the paper on band/gap/sizing/16:00-flat, but three PRAXIS framings are **NOT paper-derived and need trader decisions**: (a) "one position per session" (D5), (b) the 09:30–11:30 window / 11:30 flat (D8), and (c) a tunable "noise multiplier" and "stop-ATR" (D1, §3 — the paper has neither).

---

## 6. NinjaScript-implementation notes (param mapping)

Phase-3 spec optimizes four params `{lookback, noise multiplier, stop-ATR mult, exit policy}`. Mapping to the paper:

| Phase-3 param | Paper analog | Implementation note |
|---|---|---|
| **lookback** | `N = 14` (fixed) | Input `Lookback` (default 14). σ = mean of \|Close_{HH:MM}/Open_{9:30} − 1\| over prior N days at each minute-of-day. Needs a per-minute-of-day store keyed to session-elapsed time. |
| **noise multiplier** | **no paper analog** (`k = 1.0`) | Input `NoiseMult` (default **1.0** to match paper): `UB = ref·(1 + k·σ)`. Any k≠1 is a PRAXIS extension, not validated by 24-97. |
| **stop-ATR mult** | **no paper analog** | Paper uses band/VWAP stops, not ATR. If Block-2 insists on an ATR stop it is a **new, untested variant** — flag for trader (§7). Faithful port = disable ATR, use the band/VWAP trailing stop. |
| **exit policy** | discrete: {opp-band ; max/min(band,VWAP) ; +vol-target} | Enum input `ExitMode` ∈ {OppBand, BandOrVWAP}. Paper's preferred = **BandOrVWAP**. |

Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = max/min(Open_{9:30}, PrevClose)`; VWAP anchored at 09:30, market-hours only; **flat at 16:00** (or the trader-chosen 11:30 — see D8). Entry via `EnterLongStopMarket`/`EnterShortStopMarket` at the boundary is a reasonable NT8 realization of "act at the next HH:00/HH:30 stamp if price is outside the band," but note the paper acts on the **stamp**, not on an intrabar stop-touch — a stop-market order can fill mid-bar and diverge slightly; reconcile in b2-signal-repro.

---

## 7. NOT pinned down by paper — needs trader decision

- **T1 (highest priority): session-flat time — 16:00 (paper) vs 11:30 (PRAXIS window).** The paper's entire performance record is full-day-to-16:00. A 09:30–11:30 NQ variant is a different strategy the paper does not evaluate. Trader must decide the flat time AND accept that paper Sharpe/DD numbers do not transfer if truncated. (Resolves D8 + the b2-q1 conflict.)
- **T2: one-position-per-session vs paper's reverse-on-cross.** PRAXIS's cascade-control rationale wants one/session; the paper reverses. Decide (affects trade count, WFA sample size, SHM-5 frequency band).
- **T3: whether to expose a `noise multiplier` and/or `stop-ATR` at all.** Faithful port has neither. If Block-2 optimizes them, they are PRAXIS extensions beyond the paper (label as such in DECISIONS.md).
- **T4: exit mode** — OppBand vs BandOrVWAP (paper prefers the latter).
- **T5: instrument transfer** — SPY→NQ is unvalidated by this paper; NQ evidence is third-party (Quantitativo). Confirm the NQ port is treated as requiring its own Block-2 validation, not inheriting the paper's SPY numbers.

*End ruleset spec. All numbered §1–§4 rules carry paper citations; all open items are isolated in §7.*

## Amendment note — 2026-11-12 (D-2026-11-12-A alignment)

> ***Added 2026-11-12; not part of the text above.*** Body lines 1–111 above are unchanged. Unit `2026-11-12-fgd-doc-alignment` (bead `Praxis_build-fgd`, part A), decided by master under D-2026-11-08-D D1, changeable by Amear. This note carries out D-2026-11-12-A (DECISIONS.md:2205) and Amendment 1 at the end of `docs/specs/2026-11-05-phase3-build-specification.md` (amended #4 at its line :212, amended #5 at :224). It makes no new design choice and writes no DECISIONS.md entry; where an aligned reading would need a choice that D-2026-11-12-A and Rule F2-1 do not make, the item is listed as OPEN below with both readings. Each old line below is copied by script from this file at HEAD, byte-identical.

**Level.** Unchanged: the nine breakers, #4 and #5 included, remain SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure. This note changes how lines are read; it builds nothing.

**What governs the 11:30 framing now.** Two records, both made before this unit:

1. Amear's lock of the Block-2 strategy definition, DECISION_LOG.md:42 (row 2026-07-16T19:29Z, WHO: trader (Amear) + orchestrator), item (1), copied by script: "(1) session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window)". Its item (3), copied by script: "(3) FIRST build = pure paper replication with FIXED params".
2. D-2026-11-12-A / Amendment 1: breaker #4 no longer closes positions at 11:30 ET; it is the 16:00 ET session flat gate, and amended #5 does not disable system trading 15:00–18:00 ET. No breaker now forces an 11:30 cut.

R1 (DECISIONS.md:1551) reads "RTH = 09:30–16:00 ET".

### :8 — scope note (follow-up F-3)

```text
> **Scope note.** The paper studies **SPY** (the ETF), NOT NQ futures, and trades **all day** (every half-hour, flat at the 16:00 cash close). PRAXIS applies it to **NQ** inside a **09:30–11:30 ET** window. Every place where the PRAXIS framing departs from the paper is flagged below — those departures are trader decisions, not paper-derived facts.
```

Aligned reading: the "09:30–11:30 ET window" is no longer the PRAXIS framing of the replication strategy: its session flat is 16:00 ET (lock item (1)), and no breaker cuts it at 11:30 (amended #4). On the flat time the PRAXIS replication and the paper now agree; the instrument difference (SPY vs NQ, D9, T5) stands.

### :79 — discrepancy D8 (F-3)

```text
| D8 | Flat time | **16:00** — no 11:30 stop in paper | b2-q1 report notes a **"flat-by-11:30-ET baseline"** | ❌ **CONFLICT** — 11:30 is a **PRAXIS window choice** (09:30–11:30 active hours), NOT the paper. The paper's edge is measured on full-day holds to 16:00; truncating at 11:30 is untested by the paper and changes expectancy |
```

Aligned reading: D8 is resolved toward the paper for the replication strategy: flat at 16:00 ET (lock item (1)); and the breaker-side 11:30 close is removed (amended #4). The "flat-by-11:30-ET baseline" in the b2-q1 report is a superseded framing, not edited.

### :84 — "Net" item (b) (F-3)

```text
**Net:** The RTF prose is a faithful summary of the paper on band/gap/sizing/16:00-flat, but three PRAXIS framings are **NOT paper-derived and need trader decisions**: (a) "one position per session" (D5), (b) the 09:30–11:30 window / 11:30 flat (D8), and (c) a tunable "noise multiplier" and "stop-ATR" (D1, §3 — the paper has neither).
```

Aligned reading: item (b), "the 09:30–11:30 window / 11:30 flat (D8)", has its trader decision: lock item (1). Items (a) and (c) are outside this note.

### :99 — implementation facts (F-3)

```text
Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = max/min(Open_{9:30}, PrevClose)`; VWAP anchored at 09:30, market-hours only; **flat at 16:00** (or the trader-chosen 11:30 — see D8). Entry via `EnterLongStopMarket`/`EnterShortStopMarket` at the boundary is a reasonable NT8 realization of "act at the next HH:00/HH:30 stamp if price is outside the band," but note the paper acts on the **stamp**, not on an intrabar stop-touch — a stop-market order can fill mid-bar and diverge slightly; reconcile in b2-signal-repro.
```

Aligned reading: "flat at 16:00" stands; the parenthesis "(or the trader-chosen 11:30 — see D8)" is withdrawn for the replication strategy (lock item (1)); no breaker supplies an 11:30 flat either (amended #4). The rest of the line is unchanged.

### :105 — open item T1 (F-3)

```text
- **T1 (highest priority): session-flat time — 16:00 (paper) vs 11:30 (PRAXIS window).** The paper's entire performance record is full-day-to-16:00. A 09:30–11:30 NQ variant is a different strategy the paper does not evaluate. Trader must decide the flat time AND accept that paper Sharpe/DD numbers do not transfer if truncated. (Resolves D8 + the b2-q1 conflict.)
```

Aligned reading: T1 is decided for the replication strategy: 16:00 (lock item (1)). The safety-layer side of the conflict (breaker #4 at 11:30) is removed by D-2026-11-12-A.

### OPEN

| ID | Open item | The two readings |
|---|---|---|
| OPEN-A2 | Whether a strategy-level stop at 11:30 (a strategy rule, not a breaker) is still available to a later Noise-Area arm (the walk-forward tunables arm or the live emitter), now that no breaker forces it. D-2026-11-12-A and Rule F2-1 do not decide this. | (a) No: lock item (1) sets the session flat at 16:00 ET, "NOT the 11:30 PRAXIS window", and under Rule F2-1 system entries are allowed until 16:00 (proposal :30), so the full-day window carries to every Noise-Area arm. (b) Yes, as a choice for that arm: lock item (3) scopes the "FIRST build" to paper replication, and Rule F2-1 sets only the latest flat ("Strategies may flat earlier than 16:00 by their own rules", proposal :24), so an earlier strategy stop stays a design choice for the unit that specifies that arm. Not chosen here. |
