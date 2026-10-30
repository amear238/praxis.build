# 3gm — Worker 1, D1: fidelity checklist for `PraxisNoiseAreaBreakout.cs` against the paper-derived spec

> **Post-adversarial status (2026-10-30, manager-adjudicated).** The adversarial review `docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md` (VERDICT: FAIL on F1) regraded R17 and R23 from DEVIATION (unauthorised) to SPEC-SILENT and corrected several labels. **Final counts: FAITHFUL 15 · DEVIATION (authorised) 0 · DEVIATION (unauthorised) 1 (R14) · BUG 2 (R25, R26) · SPEC-SILENT 6 (R17, R20, R22, R23, R28, R29) · CANNOT-DETERMINE-STATICALLY 5 (R12, R15, R21, R24, R27) = 29.** The summary table below keeps the original grades. Where the two differ, the "Post-adversarial corrections" section at the end is authoritative.

**Task:** Praxis_build-3gm, deliverable D1 (checklist table). **Mode:** BUILD (read-only analysis; one output file). **Date:** 2026-10-30.
**Criterion:** one row for each of the 17 §A rows and 7 §C bullets of `docs/reports/2026-07-16-4uu-noise-area-strategy.md`, plus coverage rows. Each row carries a verdict from the fixed set, with pasted code.
**Inputs:** `ninjascript/PraxisNoiseAreaBreakout.cs` (hash below), `docs/specs/2026-07-16-b2-noise-area-ruleset.md` (the spec, used as a proxy for the paper; the paper PDF is not on disk), `DECISION_LOG.md:42`, `DECISIONS.md` (grepped), `docs/reports/2026-10-28-voice-session-notes.md:22-27` and `:29-44`.

**Evidence labels.** OBSERVED means a static read of a file in this session. INFERRED means a claim about how NT8 behaves at runtime that no on-disk observation supports. REPORTED BY AMEAR means a hand-run on the VM, recorded in the voice notes. Amear's observations are cited by file and line. Neither I nor any other Claude has seen them.

**Method.** I wrote one capture script, `scratchpad/w1/capture.sh`, and ran it once. Every fenced block below is that script's output, inserted with `cat`. Nothing in the blocks was retyped. "Spec L*n*" means the line number in the ruleset spec file. "Report L*n*" means the line number in the 4uu implementation report.

## Hash gate (matches brief: 35393823…2752265, 312 lines)
```text
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs

$ wc -l ninjascript/PraxisNoiseAreaBreakout.cs
     312 ninjascript/PraxisNoiseAreaBreakout.cs

$ git rev-parse --short HEAD
fc77f36

```

## Summary

| Row | Rule (source line) | Code lines | Verdict |
|---|---|---|---|
| R1 | No look-ahead via OnBarClose (report L16) | 104–105 | FAITHFUL |
| R2 | Lookback fixed at 14 (report L17) | 73–74 | FAITHFUL |
| R3 | Half-width = 1×σ, no multiplier (report L18) | 75–76 | FAITHFUL |
| R4 | ExitMode enum, default BandOrVWAP (report L19) | 44–51, 118 | FAITHFUL |
| R5 | σ = mean abs move-from-open per minute-of-day over 14 completed days (report L20) | 244–260 | FAITHFUL |
| R6 | Max/Min(todayOpen, prevClose)·(1±σ) anchoring (report L21) | 261–264 | FAITHFUL |
| R7 | History holds completed days only; CommitDay on first bar (report L22; candidate ix) | 145–149, 274–283 | FAITHFUL |
| R8 | Per-minute close store keyed by minute-of-day (report L23) | 143, 166–167 | FAITHFUL |
| R9 | Session VWAP reset at the open, RTH only (report L24) | 87–89, 158–159, 171–176 | FAITHFUL |
| R10 | Checkpoints at HH:00/HH:30 only, OpenMod<mod<CloseMod (report L25) | 57–58, 195–198 | FAITHFUL |
| R11 | Entry: long above Upper, short below Lower (report L26) | 222–229 | FAITHFUL |
| R12 | Reversal via NT8 managed reverse (report L27) | 106–107, 222–229 | CANNOT-DETERMINE-STATICALLY |
| R13 | BandOrVWAP exit: max(Upper,VWAP) / min(Lower,VWAP) at the stamp (report L28) | 203–220 | FAITHFUL |
| R14 | OppBand exit (report L29; candidate i) | 44–46, 205–220, 299 | DEVIATION (unauthorised) |
| R15 | 16:00 ET flat, no entry at/after close (report L30) | 108–109, 188–193, 285–291 | CANNOT-DETERMINE-STATICALLY |
| R16 | No ATR stop, no profit target (report L31) | (absence; grep) | FAITHFUL |
| R17 | Sizing: fixed Contracts, vol-target not ported (report L32; candidate viii) | 119, 302–305 | DEVIATION (unauthorised) |
| R18 | §C: bar timestamping assumed close-stamped (report L50) | 143, 150–153 | FAITHFUL |
| R19 | §C: prevClose = Close[1] on first bar of session (report L51; candidate v) | 140–141, 154–156, 168–169 | FAITHFUL |
| R20 | §C: full-sample Lookback requirement; walk-back over up to 29 days (report L52; candidate iv) | 79, 246–258 | SPEC-SILENT |
| R21 | §C: reversal by managed reverse; same-bar Exit and reverse (report L53) | 203–229 | CANNOT-DETERMINE-STATICALLY |
| R22 | §C: VWAP definition, typical price (report L54) | 171–176, 265 | SPEC-SILENT |
| R23 | §C: sizing / vol-target not ported (report L55) | 119 | DEVIATION (unauthorised) |
| R24 | §C: session-flat mechanism, explicit check plus backstop (report L56) | 108–109, 188–193 | CANNOT-DETERMINE-STATICALLY |
| R25 | Instrument comment "$5.00 / point" (candidate ii) | 36–37 | BUG (comment only, no runtime effect) |
| R26 | VWAP plot when no band is built (candidate iii) | 178–186, 257–266 | BUG (plot only, no trade effect) |
| R27 | Order realisation: market orders vs stamp price / spec L99 stop-market (coverage) | 211, 219, 227, 229, 288, 290 | CANNOT-DETERMINE-STATICALLY |
| R28 | 09:30 excluded as a checkpoint (candidate vi) | 196 | SPEC-SILENT |
| R29 | Ties: exits use <=/>=, entries use strict >/< (candidate vii) | 210, 218, 226, 228 | SPEC-SILENT |

**Counts (29 rows):** FAITHFUL 15 · DEVIATION (authorised) 0 · DEVIATION (unauthorised) 3 (R14, R17, R23) · BUG 2 (R25, R26) · SPEC-SILENT 4 (R20, R22, R28, R29) · CANNOT-DETERMINE-STATICALLY 5 (R12, R15, R21, R24, R27).

No row is graded "DEVIATION (authorised)". The trader locks in `DECISION_LOG.md:42` (16:00 flat, reverse on opposite cross, Lookback 14, 1×σ, no multiplier, no ATR) all coincide with what the spec says the paper does. They confirm the paper rules rather than authorise a departure from them. The appendix pastes the full row.

---

### R1 — No look-ahead: `Calculate.OnBarClose`
**Rule:** σ uses the prior days `i = 1..14` only (spec L16, spec §1, citing paper §3 pp. 6–7). Report L16 calls this a "guard-rail", not a paper rule.
```text
$ sed -n '104,105p' ninjascript/PraxisNoiseAreaBreakout.cs
				// OnBarClose is REQUIRED for the no-look-ahead guarantee: σ reads only closed bars.
				Calculate                                 = Calculate.OnBarClose;

$ sed -n '39,40p' ninjascript/PraxisNoiseAreaBreakout.cs
// NO LOOK-AHEAD: Calculate.OnBarClose + the 14-day σ lookback reads only COMPLETED prior sessions
// (the current day is never in the history store until its session ends). See BuildBand().

$ sed -n '16p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `Calculate = Calculate.OnBarClose` (SetDefaults) | No look-ahead — σ reads only closed bars | §1; guard-rail |

```
**Verdict: FAITHFUL.** OBSERVED: `Calculate = Calculate.OnBarClose`, so `Close[0]` is the close of a finished bar. Look-ahead in σ is handled by the history store (R7), not by this setting. Under OnBarClose, the decision bar's own data is legitimately available at its stamp. That matches the paper evaluating "at the stamp" (spec L36).

### R2 — Lookback = 14, fixed
**Rule:** "14 trading days, fixed (`i = [1,14]`). No lookback grid" (spec L31, spec §1, paper §3 p. 6). Table row: spec L46.
```text
$ sed -n '73,74p' ninjascript/PraxisNoiseAreaBreakout.cs
		// spec §1/§3 p.6 — FIXED 14 trading days. paper-fixed, not optimizable this pass (DECISION_LOG 2026-07-16).
		private const int Lookback = 14;

$ sed -n '295,296p' ninjascript/PraxisNoiseAreaBreakout.cs
		// Lookback and BandSigmaMult are paper-fixed, not optimizable this pass (DECISION_LOG 2026-07-16).
		// They live as private consts (see field region) so the Strategy Analyzer cannot vary them.

$ sed -n '17p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `Lookback` = `private const int 14` (not an Input; not optimizable) | 14-day fixed lookback | §1/§3 p.6 |

$ sed -n '31p;46p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Lookback window:** **14 trading days**, fixed (`i = [1,14]`). No lookback grid is tested in the paper.
| Lookback | **14 days**, fixed | §3 p. 6 |

```
**Verdict: FAITHFUL.** OBSERVED: `private const int Lookback = 14`, not an input. This matches the spec, and `DECISION_LOG.md:42` (3) "lookback=14" confirms it.

### R3 — Band half-width = 1×σ
**Rule:** "NO free multiplier … exactly `1 × σ`" (spec L32, spec §1, paper §3 p. 7). Table row: spec L47.
```text
$ sed -n '75,76p' ninjascript/PraxisNoiseAreaBreakout.cs
		// spec §1 p.7 / §5 D1 — paper half-width is EXACTLY 1xσ. paper-fixed, not optimizable this pass (DECISION_LOG 2026-07-16).
		private const double BandSigmaMult = 1.0;

$ sed -n '18p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `BandSigmaMult` = `private const double 1.0` (not an Input; not optimizable) | Band half-width = 1×σ, no free multiplier | §1 p.7 / §5 D1 |

$ sed -n '32p;47p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Noise "multiplier":** there is **NO free multiplier** in the paper — the half-width is exactly `1 × σ` (the raw 14-day average absolute move). A tunable multiplier is a PRAXIS addition, not a paper parameter (see discrepancy table).
| Band half-width | `1 × σ` (no multiplier) | §3 p. 7 |

```
**Verdict: FAITHFUL.** OBSERVED: `const double BandSigmaMult = 1.0`, used as `1.0 + 1.0·σ` at lines 263–264 (R6). Confirmed by `DECISION_LOG.md:42` (3) "band=1×σ, no noise-multiplier".

### R4 — ExitMode enum, default BandOrVWAP
**Rule:** exit variants (a) opposite band, (b) max/min(band,VWAP). The paper prefers BandOrVWAP (spec L97 §6, spec L108 T4, citing paper §3 p. 13).
```text
$ sed -n '44,51p' ninjascript/PraxisNoiseAreaBreakout.cs
	// Exit form — the ONLY tunable this pass (spec §6 param-map row "exit policy"; §4 p.9,13).
	// OppBand    = base model, trailing stop at the same-side band the breakout came through.
	// BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). DEFAULT.
	public enum PraxisNoiseExitMode
	{
		OppBand,
		BandOrVWAP
	}

$ sed -n '118p' ninjascript/PraxisNoiseAreaBreakout.cs
				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec §4 p.13 — paper's PREFERRED exit. The only knob.

$ sed -n '19p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `ExitMode` enum default `BandOrVWAP` | Selectable exit; paper-preferred default | §4 p.13 / §6 param-map |

$ sed -n '97p;108p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| **exit policy** | discrete: {opp-band ; max/min(band,VWAP) ; +vol-target} | Enum input `ExitMode` ∈ {OppBand, BandOrVWAP}. Paper's preferred = **BandOrVWAP**. |
- **T4: exit mode** — OppBand vs BandOrVWAP (paper prefers the latter).

```
**Verdict: FAITHFUL** for the enum and the default. OBSERVED: the default is `BandOrVWAP`, the paper-preferred variant. Spec T4 (L108) left the choice to the trader, and `DECISION_LOG.md:42` says only "exit=opposite-band/VWAP". The *content* of the OppBand branch is graded separately in R14. REPORTED BY AMEAR: all three hand runs used BandOrVWAP (`docs/reports/2026-10-28-voice-session-notes.md:33`).

### R5 — σ math: mean absolute move-from-open per minute-of-day over 14 completed days
**Rule:** `move = |Close_{t-i,HH:MM}/Open_{t-i,9:30} − 1|` and `σ = (1/14)·Σ_{i=1..14} move` (spec L16–19, spec §1 steps 1–2, paper §3 eqs. pp. 6–7).
```text
$ sed -n '244,260p' ninjascript/PraxisNoiseAreaBreakout.cs
			double sumAbs = 0.0;
			int cnt = 0;
			// Walk newest->oldest completed days; take up to Lookback that recorded this minute-of-day.
			for (int d = history.Count - 1; d >= 0 && cnt < Lookback; d--)
			{
				DayRecord rec = history[d];
				double c;
				if (rec.Open > 0 && rec.Closes.TryGetValue(mod, out c))
				{
					sumAbs += Math.Abs(c / rec.Open - 1.0);     // spec §1 step 1
					cnt++;
				}
			}
			if (cnt < Lookback)                                 // require a full 14-day sample (spec §3 fixed N)
				return;

			curSigma = sumAbs / cnt;                            // spec §1 step 2

$ sed -n '20p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `BuildBand()` — `sumAbs += Abs(c/rec.Open − 1)`, `/cnt` | σ = 14-day mean absolute move-from-open at that minute-of-day | §1 steps 1–2, pp.6–7 |

$ sed -n '16,19p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
1. **Per-day absolute move from Open** (14-day lookback, `i = 1..14`):
   `move_{t-i, 9:30→HH:MM} = | Close_{t-i, HH:MM} / Open_{t-i, 9:30} − 1 |`
2. **Average move (the band half-width σ) at that minute-of-day:**
   `σ_{t, 9:30→HH:MM} = (1/14) · Σ_{i=1..14} move_{t-i, 9:30→HH:MM}`

```
**Verdict: FAITHFUL.** OBSERVED: line 253 is `Math.Abs(c / rec.Open - 1.0)`, where `c` is the stored close at this minute-of-day and `rec.Open` is that day's 09:30 open (R18). Line 260 is `sumAbs / cnt`, and `cnt == Lookback == 14` is guaranteed by the return at 257–258, so the divisor is always 14. Which 14 days are used is graded separately in R20.

### R6 — Max/Min(todayOpen, prevClose) anchoring
**Rule:** `Upper = max(Open_{t,9:30}, Close_{t-1,16:00})·(1+σ)` and `Lower = min(…)·(1−σ)` (spec L25–28, spec §1 gap adjustment, paper §3 p. 7).
```text
$ sed -n '261,264p' ninjascript/PraxisNoiseAreaBreakout.cs
			double refUpper = Math.Max(todayOpen, prevClose);   // spec §1 p.7 gap adjustment
			double refLower = Math.Min(todayOpen, prevClose);
			curUpper = refUpper * (1.0 + BandSigmaMult * curSigma);
			curLower = refLower * (1.0 - BandSigmaMult * curSigma);

$ sed -n '21p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `BuildBand()` — `Max/Min(todayOpen, prevClose)·(1 ± k·σ)` | Overnight-gap-adjusted Upper/Lower bounds | §1 step 3 p.7 |

$ sed -n '25,28p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
**Overnight-gap adjustment (PAPER-VERIFIED, §3 p. 7).** To fold in the overnight gap, the reference price is the more extreme of today's Open and yesterday's Close:
`UpperBound = max(Open_{t,9:30}, Close_{t-1,16:00}) · (1 + σ)`
`LowerBound = min(Open_{t,9:30}, Close_{t-1,16:00}) · (1 − σ)`
(After a gap-down the Upper Bound is pushed up by the gap; after a gap-up the Lower Bound is pushed down — see paper prose p. 7.)

```
**Verdict: FAITHFUL.** OBSERVED: these are exact formula matches. The correctness of `todayOpen` and `prevClose` themselves is graded in R18 and R19.

### R7 — History holds completed sessions only (candidate ix: look-ahead)
**Rule:** σ uses days `t-1 … t-14` only (spec L16, paper §3 pp. 6–7).
```text
$ sed -n '145,149p' ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- Session rollover: on the first bar of a new RTH session, close out the prior
			// day into history (so σ sees it ONLY once complete — no look-ahead), then reset. ----
			if (Bars.IsFirstBarOfSession)
			{
				CommitDay();                    // push yesterday into history

$ sed -n '274,283p' ninjascript/PraxisNoiseAreaBreakout.cs
		private void CommitDay()
		{
			if (today != null && today.Open > 0 && today.Closes.Count > 0)
			{
				history.Add(today);
				while (history.Count > HistoryCap)
					history.RemoveAt(0);
			}
			today = null;
		}

$ sed -n '22p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `history` = completed days only; `CommitDay()` on first bar of session | σ never sees the in-progress day (no look-ahead) | §1; guard-rail |

$ sed -n '16p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
1. **Per-day absolute move from Open** (14-day lookback, `i = 1..14`):

```
**Verdict: FAITHFUL. Candidate (ix) is refuted.** OBSERVED: `CommitDay()` (line 149) runs on the first bar of a new session, *before* `today` is replaced (line 151), and it pushes the record of the day that just ended. `today` (the in-progress day) is never added to `history` until the next session's first bar. `BuildBand` reads only `history` (line 249). So no in-progress-day close enters σ. The first-bar ordering is: commit yesterday (which includes its 16:00 bar), then reset `today`, then record the current bar into the new `today` (line 167), then BuildBand. So the current bar is excluded too.

### R8 — Per-bar close store keyed by minute-of-day
**Rule:** σ is indexed by minute-of-day elapsed from the open and needs a per-minute-of-day store (spec L30 §1; spec L94 §6).
```text
$ sed -n '143p' ninjascript/PraxisNoiseAreaBreakout.cs
			int mod = Time[0].Hour * 60 + Time[0].Minute;   // minute-of-day of THIS (closed) bar

$ sed -n '166,167p' ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- Per-bar bookkeeping: record this minute's close + advance session VWAP. ----
			today.Closes[mod] = Close[0];       // minute-of-day -> close (spec §1: Close_{t,HH:MM})

$ sed -n '23p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| Per-bar `today.Closes[mod] = Close[0]`; `mod = H*60+M` | Minute-of-day close store keyed to session-elapsed time | §1; §6 note |

$ sed -n '30p;94p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Clock/time anchor:** session Open = 09:30 ET; σ is indexed by *minute-of-day* elapsed from the open. Bands **widen through the day** (Fig. 1, p. 8), peaking at 16:00.
| **lookback** | `N = 14` (fixed) | Input `Lookback` (default 14). σ = mean of \|Close_{HH:MM}/Open_{9:30} − 1\| over prior N days at each minute-of-day. Needs a per-minute-of-day store keyed to session-elapsed time. |

```
**Verdict: FAITHFUL.** OBSERVED: the key is `Time[0].Hour*60+Minute` of the bar's stamp. REPORTED BY AMEAR (`voice-session-notes.md:23-25`): bars on this install are end-stamped, so the bar stamped HH:MM closes at HH:MM, and `Close` at key HH:MM is `Close_{HH:MM}` as the spec defines it.

### R9 — Session VWAP reset at the open, RTH-only
**Rule:** "VWAP is computed from market-hours data only, anchored at the 09:30 open" (spec L61, spec §4, paper §3 p. 13 fn. 2).
```text
$ sed -n '87,89p' ninjascript/PraxisNoiseAreaBreakout.cs
		// Session-anchored VWAP (spec §4 p.13, footnote 2: RTH data only, anchored at 09:30 open).
		private double vwapCumPV;
		private double vwapCumVol;

$ sed -n '158,159p' ninjascript/PraxisNoiseAreaBreakout.cs
				vwapCumPV  = 0.0;              // re-anchor VWAP at the 09:30 open (spec §4 p.13 fn.2)
				vwapCumVol = 0.0;

$ sed -n '171,176p' ninjascript/PraxisNoiseAreaBreakout.cs
			double vol = Volume[0];
			if (vol > 0)
			{
				vwapCumPV  += ((High[0] + Low[0] + Close[0]) / 3.0) * vol;   // typical-price VWAP
				vwapCumVol += vol;
			}

$ sed -n '24p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| VWAP accum reset on `IsFirstBarOfSession`; typical-price×vol | Session VWAP, RTH-only, anchored 09:30 | §4 p.13 fn.2 |

$ sed -n '61p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
  `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.

```
**Verdict: FAITHFUL** (anchoring). OBSERVED: the accumulators reset in the `IsFirstBarOfSession` block. REPORTED BY AMEAR (`voice-session-notes.md:23,25`): that first bar is the 09:31 end-stamped bar covering 09:30–09:31, and the 09:30:00 pre-open row is excluded by the RTH template. So accumulation starts at the 09:30 open and uses RTH bars only. The price proxy (typical price) is graded SPEC-SILENT in R22.

### R10 — Checkpoints HH:00/HH:30 only; OpenMod/CloseMod bounds
**Rule:** act "at a semi-hourly checkpoint only — HH:00 and HH:30" (spec L36, spec §2, paper §3 p. 9). Stops are also evaluated only at stamps (spec L38).
```text
$ sed -n '57,58p' ninjascript/PraxisNoiseAreaBreakout.cs
		private const int OpenMod  = 9 * 60 + 30;   // 570
		private const int CloseMod = 16 * 60;       // 960

$ sed -n '195,198p' ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- Act ONLY at semi-hourly checkpoints HH:00 / HH:30, strictly inside RTH (spec §2 p.9). ----
			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
			if (!isCheckpoint || !haveBand)
				return;

$ sed -n '25p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `isCheckpoint = (min==0 || min==30) && OpenMod<mod<CloseMod` | Act only at HH:00 / HH:30 stamps | §2 p.9 |

$ sed -n '36p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Entry condition:** at a **semi-hourly checkpoint only** — `HH:00` and `HH:30` — if price is **above** the Upper Boundary → **go long**; if **below** the Lower Boundary → **go short**. Checking only at the half-hour (not tick-by-tick) is deliberate, to avoid acting on transient spikes; the paper shows a breach a few minutes before 10:30 is not acted on until the 10:30 stamp (Fig. 2, p. 9).

```
**Verdict: FAITHFUL.** OBSERVED: `isCheckpoint` requires minute 0 or 30 and `570 < mod < 960`, and it gates both the exit block and the entry block (line 197). The checkpoints are therefore 10:00, 10:30, …, 15:30 (12 per day). Under end-stamping (R8), the 10:00 bar's `Close[0]` is the 10:00 price. 16:00 is handled by the flat (R15), and the exclusion of 09:30 is graded in R28.

### R11 — Entry rule
**Rule:** "if price is above the Upper Boundary → go long; if below the Lower Boundary → go short" at a checkpoint (spec L36–37, spec §2, paper §3 pp. 8–9).
```text
$ sed -n '222,229p' ninjascript/PraxisNoiseAreaBreakout.cs
			// (2) ENTRY / REVERSAL — long above the Upper Bound, short below the Lower Bound (spec §2 p.9).
			//     A cross to the OPPOSITE bound while holding flips the position (NT8 managed reverse:
			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)

$ sed -n '26p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `price > curUpper → EnterLong`; `price < curLower → EnterShort` | Long above band / short below band | §2 p.9 |

$ sed -n '36,37p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Entry condition:** at a **semi-hourly checkpoint only** — `HH:00` and `HH:30` — if price is **above** the Upper Boundary → **go long**; if **below** the Lower Boundary → **go short**. Checking only at the half-hour (not tick-by-tick) is deliberate, to avoid acting on transient spikes; the paper shows a breach a few minutes before 10:30 is not acted on until the 10:30 stamp (Fig. 2, p. 9).
- **Direction rule:** long above the band, short below — trend-following the breakout side (p. 8–9).

```
**Verdict: FAITHFUL** (decision logic). OBSERVED: `price = Close[0]` at the stamp (line 200). Comparisons are strict (ties are graded in R29), and the guards skip a redundant same-direction entry. OBSERVED side-effect, SPEC-SILENT: in BandOrVWAP mode the following cycle can occur when price stays above Upper but below VWAP. The long exits at stamp N (R13). Re-entry is blocked at N because the pre-fill position still reads Long. The long re-enters at N+1 and exits again at N+2. The spec does not say whether the paper re-enters on the same stamp after a VWAP stop.

### R12 — Reversal via NT8 managed reverse
**Rule:** "A position is held until the close or until price crosses to the opposite boundary, at which point it is closed and reversed" (spec L38, spec §2, paper §3 p. 9; also spec L62). Trader-locked in `DECISION_LOG.md:42` (2).
```text
$ sed -n '106,107p' ninjascript/PraxisNoiseAreaBreakout.cs
				EntriesPerDirection                       = 1;
				EntryHandling                             = EntryHandling.AllEntries;

$ sed -n '222,229p' ninjascript/PraxisNoiseAreaBreakout.cs
			// (2) ENTRY / REVERSAL — long above the Upper Bound, short below the Lower Bound (spec §2 p.9).
			//     A cross to the OPPOSITE bound while holding flips the position (NT8 managed reverse:
			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)

$ sed -n '27p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `Position.MarketPosition != Long/Short` guard on entries → NT8 managed reverse | Reverse & re-enter on opposite-band cross | §2 p.9; trader lock |

$ sed -n '38p;62p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Positions per session:** **NOT capped at one.** A position is held until the close or until price crosses to the **opposite** boundary, at which point it is closed **and reversed** into a new position that direction (p. 9). Realized average trade frequency is **1.3 trades/day** (base opp-band stop) rising to **1.8 trades/day** with the VWAP stop (Table 4, p. 16). Stops, too, are evaluated only at the semi-hourly stamps (p. 9).
- **Reversal:** a cross to the opposite boundary closes and reverses (see §2).

```
**Verdict: CANNOT-DETERMINE-STATICALLY.** OBSERVED: the code's *intent* matches the rule. When a position is long and `price < curLower`, line 229 calls `EnterShort` with `EntriesPerDirection=1` and `EntryHandling.AllEntries`. INFERRED: NT8's managed approach turns an opposite-direction Enter into "close + open". No document on disk records an observed reversal in a trade list. The hand-run notes record only aggregate trade counts (`voice-session-notes.md:36-40`). The same-bar interaction with the exit block makes this worse; see R21.

### R13 — BandOrVWAP exit
**Rule:** "`Long TrailingStop = max(UpperBound, VWAP)`; `Short TrailingStop = min(LowerBound, VWAP)` … closes as soon as price crosses the current band or the VWAP" (spec L60–61, spec §4, paper §3 p. 13). Evaluated only at stamps (spec L38, L59).
```text
$ sed -n '203,220p' ninjascript/PraxisNoiseAreaBreakout.cs
			// (1) TRAILING-STOP / EXIT — evaluated ONLY at the stamp (spec §4 p.9). Reversal (2) below
			//     handles the opposite-band cross; this closes to FLAT on the same-side band/VWAP trail.
			if (mp == MarketPosition.Long)
			{
				// Long trailing stop = max(UpperBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Max(curUpper, curVwap) : curUpper;
				if (price <= stop)
					ExitLong("XL", "");
			}
			else if (mp == MarketPosition.Short)
			{
				// Short trailing stop = min(LowerBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Min(curLower, curVwap) : curLower;
				if (price >= stop)
					ExitShort("XS", "");
			}

$ sed -n '28p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| Long stop `Max(curUpper, curVwap)`; Short `Min(curLower, curVwap)`; evaluated only at checkpoint | Trailing stop = band-or-VWAP (whichever tighter), at the stamp | §4 p.9,13 |

$ sed -n '60,61p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Improved stop (paper's preferred model):** trailing stop at **band-or-VWAP**, whichever is tighter to price:
  `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.

```
**Verdict: FAITHFUL.** OBSERVED: when `ExitMode == BandOrVWAP && vwapCumVol > 0`, the long stop is `Math.Max(curUpper, curVwap)` and the short stop is `Math.Min(curLower, curVwap)`. The check runs only at checkpoints (R10) and only when a band exists, in which case `curVwap` was refreshed on this bar (R26). If no volume has accumulated, the stop degrades silently to band-only. The spec says nothing about that case, and it is unlikely on NQ RTH.

### R14 — OppBand exit (candidate i)
**Rule:** "Base stop: trailing stop at the **opposite** Noise-Area boundary (long stops at Lower/Upper as it trails; base model = 'Stop @ Opp. Band', Table 1)" (spec L59, spec §4, paper §3 p. 9 / Table 1). Spec L38 says a position is held "until price crosses to the **opposite** boundary", where it is reversed. Spec L49 lists variant (a) as "opposite band". `DECISION_LOG.md:42` (3) says "exit=opposite-band/VWAP".
```text
$ sed -n '44,46p' ninjascript/PraxisNoiseAreaBreakout.cs
	// Exit form — the ONLY tunable this pass (spec §6 param-map row "exit policy"; §4 p.9,13).
	// OppBand    = base model, trailing stop at the same-side band the breakout came through.
	// BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). DEFAULT.

$ sed -n '205,220p' ninjascript/PraxisNoiseAreaBreakout.cs
			if (mp == MarketPosition.Long)
			{
				// Long trailing stop = max(UpperBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Max(curUpper, curVwap) : curUpper;
				if (price <= stop)
					ExitLong("XL", "");
			}
			else if (mp == MarketPosition.Short)
			{
				// Short trailing stop = min(LowerBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Min(curLower, curVwap) : curLower;
				if (price >= stop)
					ExitShort("XS", "");
			}

$ sed -n '299p' ninjascript/PraxisNoiseAreaBreakout.cs
		[Display(Name = "Exit mode (ONLY tunable)", Description = "OppBand = trailing stop at same-side band; BandOrVWAP = max/min(band, VWAP), the paper's PREFERRED model (spec §4 p.13). Default BandOrVWAP.", GroupName = "02. Praxis (tunable)", Order = 1)]

$ sed -n '29p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `ExitMode==OppBand` → stop = band only | Base "Stop @ Opp. Band" variant | §4 p.9 / Table 1 |

$ sed -n '38p;49p;59p;97p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Positions per session:** **NOT capped at one.** A position is held until the close or until price crosses to the **opposite** boundary, at which point it is closed **and reversed** into a new position that direction (p. 9). Realized average trade frequency is **1.3 trades/day** (base opp-band stop) rising to **1.8 trades/day** with the VWAP stop (Table 4, p. 16). Stops, too, are evaluated only at the semi-hourly stamps (p. 9).
| Stop / exit variants tested | (a) opposite band; (b) `max(VWAP, band)`; (c) = (b) + vol-target sizing | Tables 1–3, pp. 11–15 |
- **Base stop:** trailing stop at the **opposite** Noise-Area boundary (long stops at Lower/Upper as it trails; base model = "Stop @ Opp. Band", Table 1). Evaluated only at semi-hourly stamps.
| **exit policy** | discrete: {opp-band ; max/min(band,VWAP) ; +vol-target} | Enum input `ExitMode` ∈ {OppBand, BandOrVWAP}. Paper's preferred = **BandOrVWAP**. |

```
**Verdict: DEVIATION (unauthorised).** OBSERVED: in OppBand mode the long stop is `curUpper`, the *same-side* band, and the short stop is `curLower`. Comment lines 45 and 299 say "same-side band" explicitly, so this is deliberate. Under the spec's plain wording (L38, L49, L59 "opposite"), a long should exit only on a cross of the Lower band. That event is already the reversal trigger (line 229), so a faithful OppBand mode would have no separate exit to flat. The code instead flattens a long whenever the stamp close falls back to or below Upper. **Stated ambiguity:** the parenthetical on spec L59, "long stops at Lower/Upper as it trails", is garbled and could be read as naming Upper. The same-side band does appear inside the *improved* stop on L61, which is max(**Upper**Band, VWAP). Report L29 describes this branch as the base "Stop @ Opp. Band" variant, but it does not implement the opposite band. No DECISION_LOG/DECISIONS row authorises the same-side reading (grep in the appendix and in the process log). Impact on the hand runs: none, because all three ran BandOrVWAP (`voice-session-notes.md:33`).

### R15 — 16:00 ET flat; no entry at/after the close
**Rule:** "all positions closed at the market Close = 16:00 ET … never held overnight. The paper has no intraday time-stop" (spec L64, spec §4, paper Fig. 2 caption p. 9, Fig. 4 p. 12). Trader-locked in `DECISION_LOG.md:42` (1).
```text
$ sed -n '108,109p' ninjascript/PraxisNoiseAreaBreakout.cs
				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
				ExitOnSessionCloseSeconds                 = 30;

$ sed -n '188,193p' ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close
			}

$ sed -n '285,291p' ninjascript/PraxisNoiseAreaBreakout.cs
		private void FlattenAll(string reason)
		{
			if (Position.MarketPosition == MarketPosition.Long)
				ExitLong("FlatEOD", "");
			else if (Position.MarketPosition == MarketPosition.Short)
				ExitShort("FlatEOD", "");
		}

$ sed -n '30p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `mod >= CloseMod → FlattenAll(); return` | 16:00 ET cash-close flat, no new entry at/after close | §4 p.9,12; trader lock |

$ sed -n '64p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Session flat:** **all positions closed at the market Close = 16:00 ET** (cash close), never held overnight (Fig. 2 caption p. 9; Fig. 4 p. 12). The paper has **no intraday time-stop** — the only time-based exit is 16:00.

```
**Verdict: CANNOT-DETERMINE-STATICALLY.** OBSERVED: on the 16:00 bar (`mod >= 960`) the code calls `ExitLong/ExitShort("FlatEOD")` and returns, so no entry happens at or after 16:00. That decision logic is faithful. The fill is the open question. INFERRED: a managed market exit submitted on a bar's close under OnBarClose fills at the *next* bar's open. REPORTED BY AMEAR (`voice-session-notes.md:23`): on this install the 16:00 bar is followed directly by the next day's 09:31 bar. So if the explicit exit were the only mechanism, the position would be held overnight and filled at the next day's open. Whether the backstop on line 108, `IsExitOnSessionCloseStrategy = true` (30 s), fills it at the 16:00 bar's close instead is NT8 runtime behaviour (INFERRED), and nothing on disk records it. To resolve this, read a trade list and check the exit timestamps and prices of positions open at 15:30.

### R16 — No ATR stop, no profit target
**Rule:** "Stop-ATR — not used"; "Profit target — none" (spec L50–51, spec §3; spec L63, spec §4; paper abstract p. 2).
```text
$ /usr/bin/grep -n -i -E 'atr|target|profit' ninjascript/PraxisNoiseAreaBreakout.cs
10:using NinjaTrader.Cbi;
11:using NinjaTrader.Data;
12:using NinjaTrader.Gui;
13:using NinjaTrader.Gui.Chart;
14:using NinjaTrader.NinjaScript;
15:using NinjaTrader.Core.FloatingPoint;
34://     multiplier as a tunable), NO ATR stop. The ONLY selectable knob is the exit form (ExitMode).
42:namespace NinjaTrader.NinjaScript.Strategies
119:				Contracts     = 1;                  // position sizing only (NOT a rule knob); paper uses vol-target sizing (§3 p.15) not ported here.
304:		[Display(Name = "Contracts", Description = "Position size in NQ contracts (sizing only, NOT a rule knob). Paper uses 2% vol-target sizing (§3 p.15), not ported this pass.", GroupName = "02. Praxis (tunable)", Order = 2)]

$ sed -n '31p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| No ATR field; no profit target | Paper has neither | §3 p.50 / §5 D10 |

$ sed -n '50,51p;63p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| Stop-ATR | **not used** — there is no ATR-based stop anywhere in the paper | — |
| Profit target | **none** (unlimited upside by design; abstract p. 2) | Abstract |
- **Profit target:** none.

```
**Verdict: FAITHFUL.** OBSERVED: the case-insensitive grep for `atr|target|profit` matches only `using`/`namespace` lines (the substring "aTr" in "NinjaTrader"), comment line 34, and the sizing comments on 119 and 304. There is no ATR, SetStopLoss, or SetProfitTarget code. R27's grep for order methods shows only Enter/Exit market calls. Report L31 cites "§3 p.50", but spec L50 is a *file line*, not a paper page. That is a citation slip in the report, not in the code.

### R17 — Sizing: fixed `Contracts`, vol-target not ported (candidate viii)
**Rule:** "Vol-target sizing `σ_target = 2%` daily, leverage capped 4×" with formula `Shares_t = ⌊AUM·min(4, σ_target/σ_SPY,t)/Open⌋` (spec L52, L55, spec §3, paper §3 p. 15). Exit variant (c) = (b) + vol-target sizing (spec L49, paper Tables 1–3, pp. 11–15).
```text
$ sed -n '119p' ninjascript/PraxisNoiseAreaBreakout.cs
				Contracts     = 1;                  // position sizing only (NOT a rule knob); paper uses vol-target sizing (§3 p.15) not ported here.

$ sed -n '302,305p' ninjascript/PraxisNoiseAreaBreakout.cs
		[NinjaScriptProperty]
		[Range(1, 20)]
		[Display(Name = "Contracts", Description = "Position size in NQ contracts (sizing only, NOT a rule knob). Paper uses 2% vol-target sizing (§3 p.15), not ported this pass.", GroupName = "02. Praxis (tunable)", Order = 2)]
		public int Contracts { get; set; }

$ sed -n '32p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
| `Contracts` input (sizing only, comment) | Fixed sizing; paper's 2% vol-target NOT ported | §3 p.15 (noted as out-of-scope) |

$ sed -n '49p;52p;55p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| Stop / exit variants tested | (a) opposite band; (b) `max(VWAP, band)`; (c) = (b) + vol-target sizing | Tables 1–3, pp. 11–15 |
| Vol-target sizing | `σ_target = 2%` daily, leverage capped **4×** | §3 p. 15 |
Sizing formula (§3 p. 15): `Shares_t = ⌊ AUM_{t-1} · min(4, σ_target/σ_SPY,t) / Open_{t,9:30} ⌋`, with `σ_SPY,t` the 14-day daily-return stdev.

$ /usr/bin/grep -n -i -E 'vol-target|vol target|volatility target|sizing' DECISIONS.md
186:- **Q6 sizing (RoR basis):** MFFU account + trailing-drawdown. P&L held in R-multiples throughout. SUB-INPUT PENDING: exact MFFU account size + trailing-DD limit numbers needed before b2-refdist RoR can compute — captured as a trader-input gap on that bead, not a blocker to b2-data/b2-wfa.

```
**Verdict: DEVIATION (unauthorised).** OBSERVED: sizing is a fixed integer `Contracts` (default 1), and the code comment admits the vol-target sizing is "not ported". Neither `DECISION_LOG.md:42` nor `DECISIONS.md` explicitly authorises dropping it. The `DECISIONS.md:186` Q6 hit concerns the RoR basis (R-multiples, MFFU), not the strategy's position sizing. Mitigating reading for the master: L42's "exit=opposite-band/VWAP" names variants (a)/(b) of spec L49 and omits (c), which *implies* that unsized variants are the baseline. That is an implication, not a stated authorisation. A ruling is needed.

### R18 — §C: bar timestamping (assumed "close-stamped")
**Rule:** the band is anchored at `Open_{t,9:30}`, and closes are taken at `HH:MM` (spec L16–17, L30, paper §3 pp. 6–7).
```text
$ sed -n '143p' ninjascript/PraxisNoiseAreaBreakout.cs
			int mod = Time[0].Hour * 60 + Time[0].Minute;   // minute-of-day of THIS (closed) bar

$ sed -n '150,153p' ninjascript/PraxisNoiseAreaBreakout.cs

				today     = new DayRecord();
				todayOpen = Open[0];            // Open_{t,09:30} (spec §1) — first RTH bar's open
				today.Open = todayOpen;

$ sed -n '50p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
- **Bar timestamping.** Assumed NT8 1-min bars are **close-stamped** (RTH first bar ≈ 09:31 whose `Open[0]` is the 09:30 open; the 16:00-stamped bar is the session's last). If this install is open-stamped, the minute-of-day mapping and `prevClose = Close[1]` shift by one bar — verify in step 4/5.

$ sed -n '22,27p' docs/reports/2026-10-28-voice-session-notes.md
## 2026-10-30 — Bar-time check (NT8 read by Amear; file read by Claude)
- NT8 on Fusion, NQCONT 1-minute, 2026-07-17, RTH template. Amear read the 9:31 bar Open as **28605.25** and the 9:32 bar Open as **28644.25**. No 9:30 bar is shown: the 16:00 bar is followed by 9:31.
- Import file `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt` has `20260717 093100;28605.25;…;4963` and `20260717 093200;28644.25;…`. **NT8 matches the file bar for bar. There is no hour shift and no minute shift.**
- Source convention: the file is **end-stamped**. It has 1,302 `17:00:00` rows and 1,354 `18:01:00` rows, but only one `18:00:00` row. The opening-minute volume (4,963) sits on the 09:31 row. That is the same convention NT8 uses. So the `09:30:00` row (Open 28608.75) is the 9:29–9:30 pre-open minute, and the RTH template is right to exclude it.
- **The old expectation that "09:30 Open 28608.75 is the first RTH bar"** (session-52 walkthrough v2 `:219`, 4uu brief) **assumed start-stamped bars and was wrong.** The true first RTH bar is NT8's 9:31, Open 28605.25.
- Bar times: **PASS.**

```
**Verdict: FAITHFUL.** REPORTED BY AMEAR (`voice-session-notes.md:23-27`): bars are end-stamped, the first RTH bar is 09:31, its Open (28605.25 on 2026-07-17) is the 09:30 opening price, and there is no in-session 09:30 bar. OBSERVED: line 152 sets `todayOpen = Open[0]` on that first bar, which is `Open_{t,9:30}`. Line 143 keys closes by end-time (R8). The author's §C assumption (report L50) matches what Amear observed, so the "shift by one bar" contingency does not apply.

### R19 — §C: `prevClose = Close[1]` on the first bar of the session (candidate v)
**Rule:** the reference uses `Close_{t-1,16:00}` (spec L26, spec §1, paper §3 p. 7).
```text
$ sed -n '140,141p' ninjascript/PraxisNoiseAreaBreakout.cs
			if (CurrentBar < 1)
				return;

$ sed -n '154,156p' ninjascript/PraxisNoiseAreaBreakout.cs
				// prevClose = last bar of the prior session (its 16:00 close). Close[1] is that bar.
				prevClose = (CurrentBar >= 1) ? Close[1] : todayOpen;
				if (prevClose <= 0) prevClose = todayOpen;

$ sed -n '168,169p' ninjascript/PraxisNoiseAreaBreakout.cs
			if (mod == CloseMod)
				today.Close1600 = Close[0];

$ /usr/bin/grep -n 'Close1600' ninjascript/PraxisNoiseAreaBreakout.cs
68:			public double Close1600;                             // Close_{t,16:00} (prev-close ref, spec §1 p.7)
169:				today.Close1600 = Close[0];

$ sed -n '51p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
- **`prevClose` source.** Taken as `Close[1]` on the first bar of a session (= prior session's last/16:00 bar). Robust once ≥1 session of warm-up exists; the very first session falls back to `todayOpen` (band symmetric that day).

$ sed -n '26p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
`UpperBound = max(Open_{t,9:30}, Close_{t-1,16:00}) · (1 + σ)`

```
**Verdict: FAITHFUL.** OBSERVED: on the first bar of a session, `Close[1]` is the last bar of the prior session. REPORTED BY AMEAR (`voice-session-notes.md:23`): on this install that bar is the 16:00 bar, so `Close[1] = Close_{t-1,16:00}`. **Candidate (v) confirmed:** `Close1600` is written (line 169) and never read. The grep shows only the declaration (68) and the write (169), so it is dead state. OBSERVED secondary finding: the `(CurrentBar >= 1) ? … : todayOpen` fallback on line 155 cannot be reached, because lines 140–141 return whenever `CurrentBar < 1`. So report L51's "the very first session falls back to `todayOpen`" is inaccurate. If bar 0 is a session's first bar, that session is skipped entirely (`haveDay` stays false until the next session) and is never committed. This is harmless for trading, because warm-up needs 14 days anyway. SPEC-SILENT edge: on an early-close day, `Close[1]` the next morning is that day's last bar, not a 16:00 close.

### R20 — §C: full-sample Lookback requirement; walk-back up to HistoryCap = 29 days (candidate iv)
**Rule:** `σ = (1/14)·Σ_{i=1..14}`, the last 14 trading days (spec L16–19, L31, paper §3 pp. 6–7).
```text
$ sed -n '79p' ninjascript/PraxisNoiseAreaBreakout.cs
		private int HistoryCap { get { return Lookback + 15; } }           // keep a small surplus over Lookback

$ sed -n '246,258p' ninjascript/PraxisNoiseAreaBreakout.cs
			// Walk newest->oldest completed days; take up to Lookback that recorded this minute-of-day.
			for (int d = history.Count - 1; d >= 0 && cnt < Lookback; d--)
			{
				DayRecord rec = history[d];
				double c;
				if (rec.Open > 0 && rec.Closes.TryGetValue(mod, out c))
				{
					sumAbs += Math.Abs(c / rec.Open - 1.0);     // spec §1 step 1
					cnt++;
				}
			}
			if (cnt < Lookback)                                 // require a full 14-day sample (spec §3 fixed N)
				return;

$ sed -n '52p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
- **Full-sample σ requirement.** `BuildBand()` requires a **complete `Lookback` sample** for the exact minute-of-day, else it skips trading that checkpoint. This is stricter than "average whatever is available" and means early-close/holiday minutes-of-day may not trade until 14 clean samples exist. Conservative and faithful to the fixed-N paper; flag if the trader wants graceful degradation.

$ sed -n '16,19p;31p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
1. **Per-day absolute move from Open** (14-day lookback, `i = 1..14`):
   `move_{t-i, 9:30→HH:MM} = | Close_{t-i, HH:MM} / Open_{t-i, 9:30} − 1 |`
2. **Average move (the band half-width σ) at that minute-of-day:**
   `σ_{t, 9:30→HH:MM} = (1/14) · Σ_{i=1..14} move_{t-i, 9:30→HH:MM}`
- **Lookback window:** **14 trading days**, fixed (`i = [1,14]`). No lookback grid is tested in the paper.

```
**Verdict: SPEC-SILENT.** OBSERVED: the loop walks newest to oldest through up to `history.Count ≤ 29` committed days and takes the first 14 that *contain this minute-of-day*. If fewer than 14 are found, it builds no band and skips the checkpoint. **When this equals spec i = 1..14:** whenever each of the last 14 committed days has a bar at `mod`. **When it differs:** (a) early-close sessions, which have no bars after the early close (INFERRED for the CME RTH template's holiday handling). For later minutes, such a day is skipped and day 15, 16, … is substituted. (b) A minute with no trades, where no bar exists (INFERRED for imported minute data; rare in NQ RTH). (c) More than 15 such gaps within 29 days, which suppresses the checkpoint entirely. The spec does not say how the paper treats missing minutes or half-days, so a strict reading (always days t-1..t-14) and the code's reading cannot be distinguished from the spec.

### R21 — §C: reversal by managed reverse; Exit and reverse on the same bar
**Rule:** on an opposite-boundary cross the position is "closed and reversed" (spec L38, L62, paper §3 p. 9).
```text
$ sed -n '203,229p' ninjascript/PraxisNoiseAreaBreakout.cs
			// (1) TRAILING-STOP / EXIT — evaluated ONLY at the stamp (spec §4 p.9). Reversal (2) below
			//     handles the opposite-band cross; this closes to FLAT on the same-side band/VWAP trail.
			if (mp == MarketPosition.Long)
			{
				// Long trailing stop = max(UpperBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Max(curUpper, curVwap) : curUpper;
				if (price <= stop)
					ExitLong("XL", "");
			}
			else if (mp == MarketPosition.Short)
			{
				// Short trailing stop = min(LowerBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Min(curLower, curVwap) : curLower;
				if (price >= stop)
					ExitShort("XS", "");
			}

			// (2) ENTRY / REVERSAL — long above the Upper Bound, short below the Lower Bound (spec §2 p.9).
			//     A cross to the OPPOSITE bound while holding flips the position (NT8 managed reverse:
			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)

$ sed -n '53p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
- **Reversal via NT8 managed reverse.** `EnterLong` while short auto-closes and flips (EntriesPerDirection=1, AllEntries). I did NOT hand-code Exit+Enter for reversals. The same-side trailing stop (`ExitLong/ExitShort`) is what takes a position to *flat*; the opposite-band cross is what *reverses*. On a bar where a long both stops out and price is below Lower, the pre-fill `Position.MarketPosition` still reads Long so the short reversal fires — intended, but confirm fill behavior in the Analyzer trade list.

```
**Verdict: CANNOT-DETERMINE-STATICALLY.** OBSERVED, and it applies to *every* reversal: when a position is long and `price < curLower`, the exit block also fires, because `price < curLower < curUpper ≤ stop` in both modes. So on the same bar the code submits `ExitLong("XL")` (line 211) **and** `EnterShort(Contracts,"S")` (line 229). The short case mirrors this. Comment lines 224–225 and report L53 assert that this "still reverses correctly". That assertion is INFERRED and untested: NT8's managed internal-order-handling rules decide whether the result is a 1-lot short, a flat position (entry ignored), or an over-fill. No trade list on disk shows which. The hand-run notes record an *unexplained* 48→41 trade-count change and only aggregates (`voice-session-notes.md:38-40,43`). This is the single most consequential runtime unknown in D1.

### R22 — §C: VWAP definition (typical price)
**Rule:** VWAP "from market-hours data only, anchored at the 09:30 open" (spec L61, paper §3 p. 13 fn. 2). The price proxy is not stated.
```text
$ sed -n '171,176p' ninjascript/PraxisNoiseAreaBreakout.cs
			double vol = Volume[0];
			if (vol > 0)
			{
				vwapCumPV  += ((High[0] + Low[0] + Close[0]) / 3.0) * vol;   // typical-price VWAP
				vwapCumVol += vol;
			}

$ sed -n '265p' ninjascript/PraxisNoiseAreaBreakout.cs
			curVwap  = (vwapCumVol > 0) ? vwapCumPV / vwapCumVol : Close[0];

$ sed -n '54p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
- **VWAP definition.** Typical-price ((H+L+C)/3) × volume, cumulative from 09:30. Paper says "VWAP … market-hours only, anchored at the 09:30 open" (fn.2 p.13) without pinning the price proxy; typical-price VWAP is the standard reading. Swap to close-based if the reference feed differs.

$ sed -n '61p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
  `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.

```
**Verdict: SPEC-SILENT.** OBSERVED: the code uses `(H+L+C)/3 × Volume`, cumulative from the session's first bar, and falls back to `Close[0]` when volume is zero. The spec does not pin the price proxy. The author flagged this himself (report L54).

### R23 — §C: sizing / vol-target not ported
**Rule:** as in R17 (spec L49, L52, L55, paper §3 p. 15).
```text
$ sed -n '119p' ninjascript/PraxisNoiseAreaBreakout.cs
				Contracts     = 1;                  // position sizing only (NOT a rule knob); paper uses vol-target sizing (§3 p.15) not ported here.

$ sed -n '55p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
- **Sizing / vol-target NOT ported.** Paper's `σ_target=2%`, 4× cap sizing (§3 p.15) is out of scope for a pure signal-replication pass; fixed `Contracts` used. Flagged, not implemented.

$ sed -n '49p;52p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| Stop / exit variants tested | (a) opposite band; (b) `max(VWAP, band)`; (c) = (b) + vol-target sizing | Tables 1–3, pp. 11–15 |
| Vol-target sizing | `σ_target = 2%` daily, leverage capped **4×** | §3 p. 15 |

```
**Verdict: DEVIATION (unauthorised)**, the same finding as R17 and listed here because §C bullet L55 requires its own row. Report L55 calls the omission "out of scope for a pure signal-replication pass". That is the author's framing. It does not cite a DECISION_LOG or DECISIONS row, and I found none (grep in R17).

### R24 — §C: session-flat mechanism (explicit check plus backstop)
**Rule:** flat at the 16:00 cash close (spec L64, paper p. 9, p. 12).
```text
$ sed -n '108,109p' ninjascript/PraxisNoiseAreaBreakout.cs
				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
				ExitOnSessionCloseSeconds                 = 30;

$ sed -n '188,193p' ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close
			}

$ sed -n '56p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
- **Session-flat mechanism.** Explicit `mod >= 16:00 → flatten` is primary; `IsExitOnSessionCloseStrategy=true` (30s) is a backstop. On a strict RTH template these coincide; on a template extending past 16:00 the explicit check governs.

$ sed -n '33p' docs/reports/2026-10-28-voice-session-notes.md
- **Strategy Analyzer settings:** PraxisNoiseAreaBreakout · NQCONT · Last · Minute 1 · trading hours CME US Index Futures RTH · ExitMode BandOrVWAP · Contracts 1 · Include commission True · Account Sim101 · **Slippage 2** · **Order fill resolution Standard**. Saved as template **"Praxis Backtest"** and as default.

```
**Verdict: CANNOT-DETERMINE-STATICALLY.** This is the same unknown as R15. REPORTED BY AMEAR (`voice-session-notes.md:33`): the Analyzer ran with trading hours "CME US Index Futures RTH". The bar-time check (`:23`) saw 16:00 followed by 09:31, which is consistent with the session ending at 16:00. Report L56 says the explicit check and the backstop "coincide" on a strict RTH template. That is INFERRED, not observed. Additional edge, OBSERVED from the code: on an early-close session no bar reaches `mod >= 960`, so `FlattenAll` never runs. Only the backstop (INFERRED: if the template knows the early close) would flatten. Otherwise the position would carry overnight.

### R25 — Instrument comment "$5.00 / point (=$1.25 / tick)" (candidate ii)
**Rule:** not a paper rule. The project's own record is "Point value `20` (so tick value is $5)".
```text
$ sed -n '36,37p' ninjascript/PraxisNoiseAreaBreakout.cs
// INSTRUMENT: NQ futures. TickSize 0.25, $5.00 / point (=$1.25 / tick). Add this strategy to a
// 1-MINUTE NQ series with an RTH (09:30-16:00 ET) session template in the Strategy Analyzer.

$ /usr/bin/grep -n -E '5\.0|1\.25|PointValue|MasterInstrument|TickSize' ninjascript/PraxisNoiseAreaBreakout.cs
36:// INSTRUMENT: NQ futures. TickSize 0.25, $5.00 / point (=$1.25 / tick). Add this strategy to a

$ /usr/bin/grep -n 'Point value' docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md
docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md:62:| Point value | `20` (so tick value is $5) |
docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:94:| Point value | `20` |

```
**Verdict: BUG (comment only, no runtime effect). Candidate (ii) confirmed as a wrong comment and refuted as a runtime problem.** OBSERVED: the comment is wrong for NQ. The project records point value 20 (`docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md:62`, `…-v2.md:94`); the comment's $5.00/point ($1.25/tick) is not NQ. Where that figure came from is not recorded on disk. From general knowledge, UNVERIFIED on disk, it matches the Micro E-mini S&P (MES), not MNQ ($2/point). The grep for `5.0|1.25|PointValue|MasterInstrument|TickSize` matches only line 36, the comment. The code never uses a point or tick value: P&L is computed by NT8 from the instrument definition. The comment should be corrected; that change is outside my write scope.

### R26 — VWAP plot when no band is built (candidate iii)
**Rule:** not a paper rule. Report §B step 4 (report L41) uses the plot for the visual reconcile ("VWAP should start at the open").
```text
$ sed -n '178,186p' ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- Build the band for THIS bar's minute-of-day (for plots every bar; orders only at checkpoints). ----
			BuildBand(mod);
			if (haveBand)
			{
				Values[0][0] = curUpper;
				Values[1][0] = curLower;
			}
			if (vwapCumVol > 0)
				Values[2][0] = curVwap;

$ sed -n '257,266p' ninjascript/PraxisNoiseAreaBreakout.cs
			if (cnt < Lookback)                                 // require a full 14-day sample (spec §3 fixed N)
				return;

			curSigma = sumAbs / cnt;                            // spec §1 step 2
			double refUpper = Math.Max(todayOpen, prevClose);   // spec §1 p.7 gap adjustment
			double refLower = Math.Min(todayOpen, prevClose);
			curUpper = refUpper * (1.0 + BandSigmaMult * curSigma);
			curLower = refLower * (1.0 - BandSigmaMult * curSigma);
			curVwap  = (vwapCumVol > 0) ? vwapCumPV / vwapCumVol : Close[0];
			haveBand = true;

$ /usr/bin/grep -n 'curVwap' ninjascript/PraxisNoiseAreaBreakout.cs
93:		private double curUpper, curLower, curVwap, curSigma;
186:				Values[2][0] = curVwap;
209:					? Math.Max(curUpper, curVwap) : curUpper;
217:					? Math.Min(curLower, curVwap) : curLower;
265:			curVwap  = (vwapCumVol > 0) ? vwapCumPV / vwapCumVol : Close[0];

```
**Verdict: BUG (plot only, no trade effect). Candidate (iii) confirmed for the plot and refuted for trading.** OBSERVED: `curVwap` is assigned only at line 265, *after* the `cnt < Lookback` early return at 257–258. Line 186 plots `curVwap` whenever `vwapCumVol > 0`, including on bars with no band. Those bars are the warm-up sessions (plot value 0.0, the field's default) and any minute that lacks a full 14-day sample (plot holds the last value computed, possibly from an earlier bar or day). No trade decision is affected: the exits that read `curVwap` (209, 217) run only past the `!haveBand` return on line 197, and `haveBand == true` means line 265 ran on this same bar.

### R27 — Order realisation: market orders vs the stamp price (spec L99 stop-market suggestion)
**Rule:** the paper "acts on the **stamp**". Spec L99 (spec §6, an implementation note, not a paper rule) offers `EnterLongStopMarket/EnterShortStopMarket` as "a reasonable NT8 realization" and warns that it diverges as well.
```text
$ /usr/bin/grep -n -E 'Enter(Long|Short)|Exit(Long|Short)|StopMarket|Limit' ninjascript/PraxisNoiseAreaBreakout.cs
211:					ExitLong("XL", "");
219:					ExitShort("XS", "");
224:			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
225:			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
227:				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
229:				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
288:				ExitLong("FlatEOD", "");
290:				ExitShort("FlatEOD", "");

$ sed -n '99p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = max/min(Open_{9:30}, PrevClose)`; VWAP anchored at 09:30, market-hours only; **flat at 16:00** (or the trader-chosen 11:30 — see D8). Entry via `EnterLongStopMarket`/`EnterShortStopMarket` at the boundary is a reasonable NT8 realization of "act at the next HH:00/HH:30 stamp if price is outside the band," but note the paper acts on the **stamp**, not on an intrabar stop-touch — a stop-market order can fill mid-bar and diverge slightly; reconcile in b2-signal-repro.

$ sed -n '43p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
6. **Stamp-vs-fill divergence.** NT8 fills managed market entries at the **next bar's open**, whereas the paper acts *at* the stamp price. Quantify the per-trade slippage vs the stamp Close; if material, consider a stop-market-at-boundary realization (spec §6 p.99 flags this) — but that is a separate decision, not this pass.

$ /usr/bin/grep -n -i -E 'stop-market|stopmarket|market order' DECISIONS.md

$ /usr/bin/grep -c -i -E 'StopMarket' DECISION_LOG.md
1

```
**Verdict: CANNOT-DETERMINE-STATICALLY.** OBSERVED: every order is a managed market order (`EnterLong/EnterShort/ExitLong/ExitShort` with no price). There are no StopMarket or Limit calls. The decision uses the stamp bar's `Close[0]`. INFERRED (report L43 states it too, as an expectation, not an observation): fills happen at the next bar's open, one minute after the stamp. How large the stamp-to-fill gap is depends on runtime and data. **Authorisation:** spec L99 is permissive, so choosing market orders over stop-market does not contradict a spec rule. Still, no DECISION_LOG or DECISIONS row selects it. The `DECISIONS.md` grep for `stop-market|stopmarket|market order` returns nothing, and the single `DECISION_LOG.md` "StopMarket" hit (line 351) is a grep record of this file's order calls, not a decision. REPORTED BY AMEAR (`voice-session-notes.md:33`): Slippage 2 was set. INFERRED: NT8 applies it to market fills, so all fills here would carry it.

### R28 — 09:30 excluded as a checkpoint (candidate vi)
**Rule:** checkpoints at "HH:00 and HH:30" (spec L36, paper §3 p. 9). The spec does not say whether 09:30, the open itself, is a checkpoint.
```text
$ sed -n '196p' ninjascript/PraxisNoiseAreaBreakout.cs
			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;

$ sed -n '36p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Entry condition:** at a **semi-hourly checkpoint only** — `HH:00` and `HH:30` — if price is **above** the Upper Boundary → **go long**; if **below** the Lower Boundary → **go short**. Checking only at the half-hour (not tick-by-tick) is deliberate, to avoid acting on transient spikes; the paper shows a breach a few minutes before 10:30 is not acted on until the 10:30 stamp (Fig. 2, p. 9).

```
**Verdict: SPEC-SILENT.** OBSERVED: `mod > OpenMod` excludes 09:30. REPORTED BY AMEAR (`voice-session-notes.md:23,25`): on this install no in-session bar is stamped 09:30 (the 09:30:00 row is pre-open and excluded by the RTH template), so the clause has no effect here. The spec gives no instruction for a 09:30 decision. The spec's worked example (L36) mentions only the 10:30 stamp.

### R29 — Ties: exits `<=`/`>=`, entries strict `>`/`<` (candidate vii)
**Rule:** entry when price is "above"/"below" the boundary (spec L36). The exit fires when price "crosses" the band or VWAP (spec L61). Neither says what happens at equality.
```text
$ sed -n '210p;218p;226p;228p' ninjascript/PraxisNoiseAreaBreakout.cs
				if (price <= stop)
				if (price >= stop)
			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)

$ sed -n '36p;61p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Entry condition:** at a **semi-hourly checkpoint only** — `HH:00` and `HH:30` — if price is **above** the Upper Boundary → **go long**; if **below** the Lower Boundary → **go short**. Checking only at the half-hour (not tick-by-tick) is deliberate, to avoid acting on transient spikes; the paper shows a breach a few minutes before 10:30 is not acted on until the 10:30 stamp (Fig. 2, p. 9).
  `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.

```
**Verdict: SPEC-SILENT.** OBSERVED: the code is internally consistent. A long at exactly `price == curUpper` exits (210), and the same-stamp re-entry is blocked by the strict `>` (226). "Above"/"below" reads naturally as strict, so the entry side fits the spec. The exit side's inclusive `<=` is a choice the spec does not make. Practical incidence is low: `price` is on the 0.25 tick grid, while `curUpper`, `curLower`, and `curVwap` are real-valued products, so exact equality is rare.

---

## Appendix — authorisation sources (full row and DECISIONS grep)
```text
$ sed -n '42p' DECISION_LOG.md
| 2026-07-16T19:29Z | WHO: trader (Amear) + orchestrator (session 16) | WHAT: Block-2 strategy definition LOCKED paper-faithful after Zarattini SSRN 4824172 sourced (commit 2a3f192, spec docs/specs/2026-07-16-b2-noise-area-ruleset.md) — (1) session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window); (2) positions/session = reverse & re-enter on opposite-band cross (NOT one-position/session); (3) FIRST build = pure paper replication with FIXED params (lookback=14, band=1×σ, no noise-multiplier, no ATR stop, exit=opposite-band/VWAP) — NO optimization grid on the first pass | WHY: paper's entire Sharpe/DD record is full-day-to-16:00 SPY; the scout-flagged 'gaps' were PRAXIS-vs-paper divergences (auditor-confirmed, no fabricated cites); a clean paper-faithful baseline must exist before any PRAXIS deviation is characterized. SUPERSEDES the optimize-set framing of D-2026-07-15-B Q7 ({lookback,noise,stop-ATR,exit}) — noise-mult & stop-ATR have no paper analog; WFA optimization (252/63/63) is deferred to a later, separate arm on top of the replication baseline | WHERE: DECISIONS spec §5/§6, block2-backtesting-scope-proposal.md Q7, bead 4uu (now fully specified/unblocked), this row | WHEN: 2026-07-16 session 16 | HOW: in-session AskUserQuestion (3 Qs) on audited ruleset spec 2a3f192; orchestrator pure-doc ledger update (exception logged, no code) | STATE: open (b2-signal-repro 4uu buildable) |

$ /usr/bin/grep -n -i -E 'noise|4uu|zarattini' DECISIONS.md
187:- **Q7 optimize:** OPTIMIZE {lookback, noise multiplier, stop-ATR multiplier, exit policy} inside rolling WFA (252 IS / 63 OOS / 63 step). OOS windows guard against curve-fit. (Larger scope than validation-only, chosen deliberately.)
231:**Decision:** The continuous NQ series roll trigger is changed to a **volume-only daily crossover** (roll to the back contract when the back month's daily volume strictly exceeds the front month's, per the tool's confirm-day logic). **The Difference (Panama / back-adjusted) adjustment is UNCHANGED** — it still removes the price gap at each seam so absolute point distances (what the Noise-Area breakout strategy measures) are preserved. This is the ONLY change: OI is dropped from the roll-trigger test; nothing else about the convention moves. Path (B) — sourcing OI elsewhere — was declined in favor of unblocking Block-2 now.
243:**Unblocks:** Praxis_build-6bw real-data validate+run (in volume-only mode, once raw/ is fully populated) → NT8 re-import → 4uu reconcile → zi1 (WFA) → ajj (MC) → xdr (refdist).

```

## Process log
1. Re-hashed the strategy file. The hash matches the brief (block above).
2. Read the full source, the 4uu report (§A L16–32, §C L50–56), the spec (all 111 lines), `DECISION_LOG.md:42` and `:443`, `voice-session-notes.md:18-44`, and `DECISIONS.md:180-190`.
3. Grepped DECISION_LOG/DECISIONS for vol-target, sizing, market/stop-market, same-side/opposite-band/OppBand, and noise/4uu/zarattini. No authorisation row was found for R14, R17/R23, or R27.
4. Wrote `capture.sh`, ran it once (31 blocks), and inserted the blocks with an awk/`cat` include step.

## Out-of-scope observations (reported, not acted on)
- `DECISIONS.md:231` says the Panama/difference back-adjustment preserves "absolute point distances (what the Noise-Area breakout strategy measures)". OBSERVED in R5: the strategy measures a **ratio** (`c/rec.Open − 1`), not a point distance. Under a difference adjustment the ratio for older data is scaled by `raw/(raw+offset)`. Whether that matters numerically is NOT CHECKED. It is a data-convention question for the master.
- Report L31 cites "§3 p.50", which is a spec file line, not a paper page (R16).
- Hand-run trade frequency (`voice-session-notes.md:40`: 1,075 trades from 2021-03-08 to 2026-07-17, roughly 0.8/day) is below the paper's 1.3–1.8/day for SPY (spec L38). The instrument differs and the reversal behaviour in R21 is unresolved, so this is only a tripwire.

## Files staged
None. Read-only analysis; no git add. The only file written is this report.

## Result: PASS (D1 delivered: 29 rows, every row with pasted code and a verdict)

## Post-adversarial corrections (manager-adjudicated, 2026-10-30)

- **C1 (F1, MAJOR). R17 and R23 → SPEC-SILENT.** Spec L49 places vol-target sizing in variant (c), defined as (b) + sizing. Spec L97 maps `ExitMode` to {OppBand, BandOrVWAP} only. `DECISION_LOG.md:42` selects "exit=opposite-band/VWAP". But spec L52 and L55 list vol-target sizing as a paper default. The spec is internally ambiguous about whether the replication target is variant (b) or variant (c). "Unauthorised" cannot be supported. "Authorised" cannot either: rubric S5 forbids inferring an approval from DECISION_LOG:42's silence on sizing. Whether the replication target includes sizing is Amear's question (S8). P1 output, the DECISION_LOG grep the original asserted but did not paste:

```
$ /usr/bin/grep -niE "vol-target|vol target|sizing|same-side|oppband|opposite-band" DECISION_LOG.md | cut -c1-160
42:| 2026-07-16T19:29Z | WHO: trader (Amear) + orchestrator (session 16) | WHAT: Block-2 strategy definition LOCKED paper-faithful after Zarattini SSRN 4824172 
46:| 2026-07-25 (session 30) | WHO: Claude.ai master/scoping agent (directive, relayed by trader Amear) + orchestrator (session 30) | WHAT: HARD PHASE-GATE rais
```

- **C2 (F2).** R25 explanation corrected in place (see above). Verdict unchanged: BUG, comment only.
- **C3 (F3). R4 and R14.** Read "all three hand runs used BandOrVWAP" as: runs 2 and 3 used BandOrVWAP (REPORTED BY AMEAR, voice-session-notes.md:33). Run 1's settings were not read back, so its ExitMode is INFERRED from the code default (line 118) only. R14's "runs not affected" holds for runs 2–3 and is INFERRED for run 1. R9's RTH-only VWAP likewise depends on run 1's unverified trading-hours template.

```
$ sed -n '36,40p' docs/reports/2026-10-28-voice-session-notes.md
| Run | Range | Trades | Net profit | Commission | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| 1 (settings not verified; may have reset) | 2026-04-01 → 2026-07-17 | 48 | $225.64 | $0 (not included) | — | — |
| 2 (all fields read back by Amear) | 2026-04-01 → 2026-07-17 | 41 | $599.08 | $121.36 (= 41 × 2.96) | — | — |
| 3 (full history, same settings) | 2021-03-08 → 2026-07-17 | **1,075** | **$1,281.61** | — | **1.04** | **$4,051.57** |
```

- **C4 (F4).** See C1 for the DECISION_LOG grep. The conclusion "no authorising row" for R14 holds on that output.
- **C5 (F5). R8, R10 and R15 depend on NT8's display time zone being ET.** The constants OpenMod = 570 and CloseMod = 960 assume Time[0] is in ET. The REPORTED 09:31 first bar and 16:00 last bar on the CME RTH template support ET display (INFERRED): a CT display would show 08:31 and 15:00. Grades unchanged.
- **C6 (F6). R15 and R24 omit TimeInForce.Day.** A Day-TIF FlatEOD market exit submitted on the 16:00 bar's close may expire at the session end instead of filling at the next day's 09:31 (INFERRED). This adds an outcome to the existing CANNOT-DETERMINE-STATICALLY. The trade-list readback must resolve it.

```
$ sed -n '111p' ninjascript/PraxisNoiseAreaBreakout.cs
				TimeInForce                               = TimeInForce.Day;
```

- **C7 (F7). Citation pages.** R8: spec L30 sits under spec §1, headed "(§3, pp. 6–7)", and cites Fig. 1 p. 8. R29: spec L36 → paper §3 p. 9; spec L61 → paper §3 p. 13.

WORKER STATUS: COMPLETE
