# 3gm — Fidelity check of `PraxisNoiseAreaBreakout.cs` against the Zarattini–Aziz–Barbon ruleset (manager report)

**Bead:** Praxis_build-3gm (P1) · **Date:** 2026-10-30 · **Manager:** praxis-manager · **Code under test:** `ninjascript/PraxisNoiseAreaBreakout.cs`, 312 lines, sha256 `35393823…2752265`, last changed `719ab11`, HEAD `fc77f36` · **READ-ONLY on code. No code was changed.**

**Evidence labels used throughout.**
- **OBSERVED**: read from a file in this session; the output is pasted.
- **REPORTED BY AMEAR**: from his hand-run on the Fusion VM, recorded in `docs/reports/2026-10-28-voice-session-notes.md`. No Claude has seen his screens.
- **INFERRED**: NT8 runtime behaviour, or reasoning that no on-disk observation supports.

The paper PDF is not on disk. The spec `docs/specs/2026-07-16-b2-noise-area-ruleset.md` (committed `2a3f192`, auditor-PASS) stands in for it. "Spec L*n*" means a line in that spec file.

## Task
Grade every §A row and every §C bullet of `docs/reports/2026-07-16-4uu-noise-area-strategy.md` against the spec (D1). Then:
- **D2:** walk the code's clock logic under the end-stamped bars Amear confirmed on 2026-10-30.
- **D3:** inventory order types and judge the ≈$21,500 slippage formula.
- **D4:** enumerate why run 1 (48 trades) and run 2 (41 trades) differ.
- **D5:** give a plain verdict with line numbers, plus a NEEDS AMEAR list of recommended changes. No change is applied.

## Rubric criteria addressed (`specs/SPEC_RUBRIC.md`)
- **S1** (line 107): every claim has pasted command output.
- **S2** (line 108): nothing is reported above its evidence.
- **S8** (line 114): Amear's questions are not answered for him.
- **S9 note / ruling R3** (lines 159–201): a mechanism named in a comment is graded by experiment. The reversal-implies-exit claim is tested by fuzzing a port, with a mutant positive arm. NT8 runtime claims stay INFERRED because NT8 cannot be run here.
- **S5** (line 111): no approval is inferred. This criterion drove the R17/R23 regrade.
- **S6** (line 112): see the cross-block check below.
- **Unit criterion (Amear):** no code change; the verdict carries line numbers.
- **F2 and F3** (FROZEN, lines 30–57) are touched by findings, not addressed; see S6.

## Workers dispatched
| Id | Mode | Scope | Outcome |
|---|---|---|---|
| W1 `a7de0df62c6613ffd` | BUILD | D1 checklist → `docs/reports/2026-10-30-3gm-worker1-checklist.md` | COMPLETE, 29 rows. Two grades and several labels later corrected (W3) |
| W2 `a70cb09a30a59f770` | BUILD | D2–D4 → `docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md` | COMPLETE. Two labels later corrected (W4) |
| W3 `ae328d23b555e4ef4` | ADVERSARIAL | attack W1 → `docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md` | `VERDICT: FAIL`: 1 MAJOR (R17/R23 graded above evidence), 6 MINOR. All 112 re-run commands identical |
| W4 `a18118c4dc1279c15` | ADVERSARIAL | attack W2 → `docs/reports/2026-10-30-3gm-worker4-adversarial-d2d4.md` | `VERDICT: FAIL`: 2 MAJOR (S2 label upgrades), 6 MINOR. 34/36 re-runs identical; 2 drifted by observer effect only |
| W5 `a42e888968ec76fda` | BUILD (fix) | Apply manager-adjudicated exact text to W1 and W2 | Applied. Verified by diff (Process log) |
| W6 (see Process log) | ADVERSARIAL | attack this manager report | see Adversarial findings |

## Process log
1. **Hash gate.** Re-hashed the code at unit start; it matched `35393823…2752265`.
2. **Read inputs.** Read the rubric, the full source, the 4uu report, the spec, DECISION_LOG lines 42 / 353 / 441–444, and the voice notes lines 20–46.
3. **Dispatched W1 and W2 in parallel.** They wrote separate files and were read-only on code, so no worktree was needed.
4. **Read both worker report files**, not their summaries. Spotted an unsupported "MNQ-style" explanation in W1 R25, which W3 later raised independently.
5. **Dispatched W3 and W4 (adversarial)** with the artifact and the criterion only. Both returned `VERDICT: FAIL`, and the tokens were confirmed in the files (`tail -1`).
6. **Adjudicated all 15 findings and accepted all 15.**
   - R17/R23 regraded to SPEC-SILENT. Spec L49 (sizing = variant (c)) conflicts with spec L52/L55 (sizing as default), and S5 forbids reading an approval from DECISION_LOG:42's silence.
   - W2's two OBSERVED labels became INFERRED.
7. **W5 applied the corrections** using exact replacement text: banners plus appended sections, and one in-place strike in W1 R25. I checked with `diff` against the backups.
   - W1: 36 added, 1 removed (the R25 line). Counts pasted under Addendum E-W6.
   - W2: 45 added, 0 removed.
   - `WORKER STATUS: COMPLETE` is still the last line of both.
   - W5's P1 grep found no authorising row for R14 or sizing; it is pasted in W1's corrections C1.
   - W5 flagged C3's citation `voice-session-notes.md:33`. I checked it: line 33 is the settings line (pasted below), so the citation is correct.
8. **Re-ran the key evidence myself** (Verification evidence): hash, order grep, null search with a positive control, dead-field and session-close grep, checkpoint enumeration, cost arithmetic. Every figure matches the workers' pastes.
9. **Ran two trips.**
   - Tamper trip: one appended byte changes the hash, so the hash gate fires.
   - Fuzz of my own python port of lines 205–229 and 261–264: 0 of 129,174 reversals lack the exit condition. In the mutant arm with the exit disabled, the detector fires on 129,174 of 129,174, so the zero is informative.
10. **Generated the D1 table mechanically** from a row file with a script that runs `sed -n` for every spec and code range, so no paste is retyped. Verdict counts were checked by grep.


## D1 — Checklist (final grades after adversarial adjudication)

**Final counts (29 rows): FAITHFUL 15 · DEVIATION (authorised) 0 · DEVIATION (unauthorised) 1 (R14) · BUG 2 (R25, R26) · SPEC-SILENT 6 (R17, R20, R22, R23, R28, R29) · CANNOT-DETERMINE-STATICALLY 5 (R12, R15, R21, R24, R27).**

- Rows R1–R24 cover the 17 §A rows (report L16–32) and the 7 §C bullets (report L50–56).
- Rows R25–R29 are extra coverage rows.
- Fuller per-row reasoning is in W1's report. Its corrections section (C1–C7) is authoritative where it differs from W1's original table.
- Spec ranges are printed whole, so long spec lines are pasted in full.

| Row | Rule (source) | Spec line · paper page | Code lines | Final verdict |
|---|---|---|---|---|
| R1 | §A L16 — no look-ahead via OnBarClose | spec L16 · §3 pp. 6–7 (spec §1) | 104,105 | FAITHFUL |
| R2 | §A L17 — Lookback 14, fixed | spec L31, L46 · §3 p. 6 | 73,74 | FAITHFUL |
| R3 | §A L18 — half-width 1×σ, no multiplier | spec L32, L47 · §3 p. 7 | 75,76 | FAITHFUL |
| R4 | §A L19 — ExitMode enum, default BandOrVWAP | spec L97, L108 · §3 p. 13; spec §6/§7 T4 | 44,51; 118,118 | FAITHFUL |
| R5 | §A L20 — σ = mean \|Close_HH:MM/Open_9:30 − 1\| over 14 completed days | spec L16,19 · §3 pp. 6–7 | 244,260 | FAITHFUL |
| R6 | §A L21 — Max/Min(todayOpen, prevClose)·(1±σ) | spec L25,28 · §3 p. 7 | 261,264 | FAITHFUL |
| R7 | §A L22 — history holds completed days only (look-ahead) | spec L16 · §3 pp. 6–7 | 145,161; 274,283 | FAITHFUL |
| R8 | §A L23 — minute-of-day close store | spec L30, L94 · §3 pp. 6–7, Fig. 1 p. 8 | 143,143; 166,167 | FAITHFUL |
| R9 | §A L24 — session VWAP reset at open, RTH only | spec L61 · §3 p. 13 fn. 2 | 87,89; 158,159; 171,176 | FAITHFUL |
| R10 | §A L25 — checkpoints HH:00/HH:30 only, OpenMod < mod < CloseMod | spec L36 · §3 p. 9 | 57,58; 195,198 | FAITHFUL |
| R11 | §A L26 — entry: long above Upper, short below Lower | spec L36,37 · §3 pp. 8–9 | 222,229 | FAITHFUL |
| R12 | §A L27 — reversal via NT8 managed reverse | spec L38 · §3 p. 9 | 106,107; 222,229 | CANNOT-DETERMINE-STATICALLY |
| R13 | §A L28 — BandOrVWAP exit max(Upper,VWAP)/min(Lower,VWAP) at stamp | spec L60,61 · §3 p. 13 | 203,220 | FAITHFUL |
| R14 | §A L29 — OppBand exit | spec L38, L49, L59 · §3 p. 9 / Table 1 | 44,46; 205,220 | DEVIATION (unauthorised) |
| R15 | §A L30 — 16:00 flat, no entry at/after close | spec L64 · Fig. 2 p. 9, Fig. 4 p. 12 | 108,111; 188,193; 285,291 | CANNOT-DETERMINE-STATICALLY |
| R16 | §A L31 — no ATR stop, no profit target | spec L50,51 · abstract p. 2 | — | FAITHFUL |
| R17 | §A L32 — fixed Contracts; vol-target sizing not ported | spec L49, L52, L55 · §3 p. 15; Tables 1–3 pp. 11–15 | 119,119; 302,305 | SPEC-SILENT |
| R18 | §C L50 — bar timestamping assumed close-stamped | spec L16,17, L30 · §3 pp. 6–7 | 143,143; 150,153 | FAITHFUL |
| R19 | §C L51 — prevClose = Close[1] on first bar of session | spec L26 · §3 p. 7 | 140,141; 154,156; 168,169 | FAITHFUL |
| R20 | §C L52 — full-sample Lookback; walk-back up to 29 days | spec L16,19, L31 · §3 pp. 6–7 | 79,79; 246,258 | SPEC-SILENT |
| R21 | §C L53 — reversal; exit + reverse on the same bar | spec L38, L62 · §3 p. 9 | 203,229 | CANNOT-DETERMINE-STATICALLY |
| R22 | §C L54 — VWAP typical price | spec L61 · §3 p. 13 fn. 2 | 171,176; 265,265 | SPEC-SILENT |
| R23 | §C L55 — sizing / vol-target not ported | spec L49, L52, L55 · §3 p. 15 | 119,119 | SPEC-SILENT |
| R24 | §C L56 — session-flat: explicit check + ExitOnSessionClose backstop | spec L64 · pp. 9, 12 | 108,111; 188,193 | CANNOT-DETERMINE-STATICALLY |
| R25 | line 36 instrument comment | spec L— · not a paper rule | 36,37 | BUG |
| R26 | VWAP plot with no band | spec L— · not a paper rule | 178,186; 257,266 | BUG |
| R27 | order realisation: market vs spec L99 stop-market note | spec L99 · spec §6 implementation note | 211,211; 219,219; 227,229; 288,290 | CANNOT-DETERMINE-STATICALLY |
| R28 | 09:30 excluded as checkpoint | spec L36 · §3 p. 9 | 196,196 | SPEC-SILENT |
| R29 | ties: exits <=/>=, entries strict >/< | spec L36, L61 · §3 p. 9; §3 p. 13 | 210,210; 218,218; 226,226; 228,228 | SPEC-SILENT |

#### R1 — §A L16 — no look-ahead via OnBarClose
**Verdict: FAITHFUL.** OnBarClose means Close[0] is a finished bar; σ look-ahead is handled by the history store (R7).

```text
$ sed -n '16,16p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
1. **Per-day absolute move from Open** (14-day lookback, `i = 1..14`):
$ sed -n '104,105p' ninjascript/PraxisNoiseAreaBreakout.cs
				// OnBarClose is REQUIRED for the no-look-ahead guarantee: σ reads only closed bars.
				Calculate                                 = Calculate.OnBarClose;
```

#### R2 — §A L17 — Lookback 14, fixed
**Verdict: FAITHFUL.** private const 14, not an input; matches spec and DECISION_LOG.md:42 (3).

```text
$ sed -n '31,31p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Lookback window:** **14 trading days**, fixed (`i = [1,14]`). No lookback grid is tested in the paper.
$ sed -n '46,46p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| Lookback | **14 days**, fixed | §3 p. 6 |
$ sed -n '73,74p' ninjascript/PraxisNoiseAreaBreakout.cs
		// spec §1/§3 p.6 — FIXED 14 trading days. paper-fixed, not optimizable this pass (DECISION_LOG 2026-07-16).
		private const int Lookback = 14;
```

#### R3 — §A L18 — half-width 1×σ, no multiplier
**Verdict: FAITHFUL.** const 1.0, used at lines 263–264.

```text
$ sed -n '32,32p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Noise "multiplier":** there is **NO free multiplier** in the paper — the half-width is exactly `1 × σ` (the raw 14-day average absolute move). A tunable multiplier is a PRAXIS addition, not a paper parameter (see discrepancy table).
$ sed -n '47,47p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| Band half-width | `1 × σ` (no multiplier) | §3 p. 7 |
$ sed -n '75,76p' ninjascript/PraxisNoiseAreaBreakout.cs
		// spec §1 p.7 / §5 D1 — paper half-width is EXACTLY 1xσ. paper-fixed, not optimizable this pass (DECISION_LOG 2026-07-16).
		private const double BandSigmaMult = 1.0;
```

#### R4 — §A L19 — ExitMode enum, default BandOrVWAP
**Verdict: FAITHFUL.** Default is the paper-preferred variant. Runs 2–3 used it (REPORTED, notes:33); run 1 INFERRED from the default only.

```text
$ sed -n '97,97p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| **exit policy** | discrete: {opp-band ; max/min(band,VWAP) ; +vol-target} | Enum input `ExitMode` ∈ {OppBand, BandOrVWAP}. Paper's preferred = **BandOrVWAP**. |
$ sed -n '108,108p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **T4: exit mode** — OppBand vs BandOrVWAP (paper prefers the latter).
$ sed -n '44,51p' ninjascript/PraxisNoiseAreaBreakout.cs
	// Exit form — the ONLY tunable this pass (spec §6 param-map row "exit policy"; §4 p.9,13).
	// OppBand    = base model, trailing stop at the same-side band the breakout came through.
	// BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). DEFAULT.
	public enum PraxisNoiseExitMode
	{
		OppBand,
		BandOrVWAP
	}
$ sed -n '118,118p' ninjascript/PraxisNoiseAreaBreakout.cs
				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec §4 p.13 — paper's PREFERRED exit. The only knob.
```

#### R5 — §A L20 — σ = mean |Close_HH:MM/Open_9:30 − 1| over 14 completed days
**Verdict: FAITHFUL.** Line 253 is the exact move; line 257 forces cnt = 14, so the divisor is always 14. Which 14 days: R20.

```text
$ sed -n '16,19p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
1. **Per-day absolute move from Open** (14-day lookback, `i = 1..14`):
   `move_{t-i, 9:30→HH:MM} = | Close_{t-i, HH:MM} / Open_{t-i, 9:30} − 1 |`
2. **Average move (the band half-width σ) at that minute-of-day:**
   `σ_{t, 9:30→HH:MM} = (1/14) · Σ_{i=1..14} move_{t-i, 9:30→HH:MM}`
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
```

#### R6 — §A L21 — Max/Min(todayOpen, prevClose)·(1±σ)
**Verdict: FAITHFUL.** Exact formula match.

```text
$ sed -n '25,28p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
**Overnight-gap adjustment (PAPER-VERIFIED, §3 p. 7).** To fold in the overnight gap, the reference price is the more extreme of today's Open and yesterday's Close:
`UpperBound = max(Open_{t,9:30}, Close_{t-1,16:00}) · (1 + σ)`
`LowerBound = min(Open_{t,9:30}, Close_{t-1,16:00}) · (1 − σ)`
(After a gap-down the Upper Bound is pushed up by the gap; after a gap-up the Lower Bound is pushed down — see paper prose p. 7.)
$ sed -n '261,264p' ninjascript/PraxisNoiseAreaBreakout.cs
			double refUpper = Math.Max(todayOpen, prevClose);   // spec §1 p.7 gap adjustment
			double refLower = Math.Min(todayOpen, prevClose);
			curUpper = refUpper * (1.0 + BandSigmaMult * curSigma);
			curLower = refLower * (1.0 - BandSigmaMult * curSigma);
```

#### R7 — §A L22 — history holds completed days only (look-ahead)
**Verdict: FAITHFUL.** CommitDay pushes yesterday before `today` is reset; BuildBand reads only `history`. Look-ahead refuted by W1 and attacked without success by W3.

```text
$ sed -n '16,16p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
1. **Per-day absolute move from Open** (14-day lookback, `i = 1..14`):
$ sed -n '145,161p' ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- Session rollover: on the first bar of a new RTH session, close out the prior
			// day into history (so σ sees it ONLY once complete — no look-ahead), then reset. ----
			if (Bars.IsFirstBarOfSession)
			{
				CommitDay();                    // push yesterday into history

				today     = new DayRecord();
				todayOpen = Open[0];            // Open_{t,09:30} (spec §1) — first RTH bar's open
				today.Open = todayOpen;
				// prevClose = last bar of the prior session (its 16:00 close). Close[1] is that bar.
				prevClose = (CurrentBar >= 1) ? Close[1] : todayOpen;
				if (prevClose <= 0) prevClose = todayOpen;

				vwapCumPV  = 0.0;              // re-anchor VWAP at the 09:30 open (spec §4 p.13 fn.2)
				vwapCumVol = 0.0;
				haveDay    = true;
			}
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
```

#### R8 — §A L23 — minute-of-day close store
**Verdict: FAITHFUL.** Key = end-stamp minute; history and checkpoint use the same key. Depends on NT8 display TZ = ET (INFERRED from the REPORTED 09:31 / 16:00 stamps).

```text
$ sed -n '30,30p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Clock/time anchor:** session Open = 09:30 ET; σ is indexed by *minute-of-day* elapsed from the open. Bands **widen through the day** (Fig. 1, p. 8), peaking at 16:00.
$ sed -n '94,94p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| **lookback** | `N = 14` (fixed) | Input `Lookback` (default 14). σ = mean of \|Close_{HH:MM}/Open_{9:30} − 1\| over prior N days at each minute-of-day. Needs a per-minute-of-day store keyed to session-elapsed time. |
$ sed -n '143,143p' ninjascript/PraxisNoiseAreaBreakout.cs
			int mod = Time[0].Hour * 60 + Time[0].Minute;   // minute-of-day of THIS (closed) bar
$ sed -n '166,167p' ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- Per-bar bookkeeping: record this minute's close + advance session VWAP. ----
			today.Closes[mod] = Close[0];       // minute-of-day -> close (spec §1: Close_{t,HH:MM})
```

#### R9 — §A L24 — session VWAP reset at open, RTH only
**Verdict: FAITHFUL.** Reset on the first session bar (09:31, covering 09:30–09:31). RTH-only depends on the template (run 1 unknown).

```text
$ sed -n '61,61p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
  `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.
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
```

#### R10 — §A L25 — checkpoints HH:00/HH:30 only, OpenMod < mod < CloseMod
**Verdict: FAITHFUL.** 12 checkpoints, 10:00–15:30 (enumeration in Verification evidence).

```text
$ sed -n '36,36p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Entry condition:** at a **semi-hourly checkpoint only** — `HH:00` and `HH:30` — if price is **above** the Upper Boundary → **go long**; if **below** the Lower Boundary → **go short**. Checking only at the half-hour (not tick-by-tick) is deliberate, to avoid acting on transient spikes; the paper shows a breach a few minutes before 10:30 is not acted on until the 10:30 stamp (Fig. 2, p. 9).
$ sed -n '57,58p' ninjascript/PraxisNoiseAreaBreakout.cs
		private const int OpenMod  = 9 * 60 + 30;   // 570
		private const int CloseMod = 16 * 60;       // 960
$ sed -n '195,198p' ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- Act ONLY at semi-hourly checkpoints HH:00 / HH:30, strictly inside RTH (spec §2 p.9). ----
			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
			if (!isCheckpoint || !haveBand)
				return;
```

#### R11 — §A L26 — entry: long above Upper, short below Lower
**Verdict: FAITHFUL.** Decision logic matches. Re-entry cycling after a VWAP stop is spec-silent (W1 R11).

```text
$ sed -n '36,37p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Entry condition:** at a **semi-hourly checkpoint only** — `HH:00` and `HH:30` — if price is **above** the Upper Boundary → **go long**; if **below** the Lower Boundary → **go short**. Checking only at the half-hour (not tick-by-tick) is deliberate, to avoid acting on transient spikes; the paper shows a breach a few minutes before 10:30 is not acted on until the 10:30 stamp (Fig. 2, p. 9).
- **Direction rule:** long above the band, short below — trend-following the breakout side (p. 8–9).
$ sed -n '222,229p' ninjascript/PraxisNoiseAreaBreakout.cs
			// (2) ENTRY / REVERSAL — long above the Upper Bound, short below the Lower Bound (spec §2 p.9).
			//     A cross to the OPPOSITE bound while holding flips the position (NT8 managed reverse:
			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
```

#### R12 — §A L27 — reversal via NT8 managed reverse
**Verdict: CANNOT-DETERMINE-STATICALLY.** Intent matches. The NT8 close-and-reverse is INFERRED; no trade list on disk.

```text
$ sed -n '38,38p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Positions per session:** **NOT capped at one.** A position is held until the close or until price crosses to the **opposite** boundary, at which point it is closed **and reversed** into a new position that direction (p. 9). Realized average trade frequency is **1.3 trades/day** (base opp-band stop) rising to **1.8 trades/day** with the VWAP stop (Table 4, p. 16). Stops, too, are evaluated only at the semi-hourly stamps (p. 9).
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
```

#### R13 — §A L28 — BandOrVWAP exit max(Upper,VWAP)/min(Lower,VWAP) at stamp
**Verdict: FAITHFUL.** Exact match, evaluated only at checkpoints. curVwap is fresh whenever haveBand.

```text
$ sed -n '60,61p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Improved stop (paper's preferred model):** trailing stop at **band-or-VWAP**, whichever is tighter to price:
  `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.
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
```

#### R14 — §A L29 — OppBand exit
**Verdict: DEVIATION (unauthorised).** Code uses the SAME-side band (lines 209, 217; comment line 45). Spec says "opposite" (L38, L49, L59); L59's parenthetical is garbled. No authorising row (P1 grep, W1 C1). Runs 2–3 did not use this mode.

```text
$ sed -n '38,38p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Positions per session:** **NOT capped at one.** A position is held until the close or until price crosses to the **opposite** boundary, at which point it is closed **and reversed** into a new position that direction (p. 9). Realized average trade frequency is **1.3 trades/day** (base opp-band stop) rising to **1.8 trades/day** with the VWAP stop (Table 4, p. 16). Stops, too, are evaluated only at the semi-hourly stamps (p. 9).
$ sed -n '49,49p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| Stop / exit variants tested | (a) opposite band; (b) `max(VWAP, band)`; (c) = (b) + vol-target sizing | Tables 1–3, pp. 11–15 |
$ sed -n '59,59p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Base stop:** trailing stop at the **opposite** Noise-Area boundary (long stops at Lower/Upper as it trails; base model = "Stop @ Opp. Band", Table 1). Evaluated only at semi-hourly stamps.
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
```

#### R15 — §A L30 — 16:00 flat, no entry at/after close
**Verdict: CANNOT-DETERMINE-STATICALLY.** Decision is faithful: flatten on the 16:00 bar, entries blocked. The fill is unknown: the market exit's "next bar" is the next day's 09:31; ExitOnSessionClose(30 s) and Day TIF compete (D2c).

```text
$ sed -n '64,64p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Session flat:** **all positions closed at the market Close = 16:00 ET** (cash close), never held overnight (Fig. 2 caption p. 9; Fig. 4 p. 12). The paper has **no intraday time-stop** — the only time-based exit is 16:00.
$ sed -n '108,111p' ninjascript/PraxisNoiseAreaBreakout.cs
				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
				ExitOnSessionCloseSeconds                 = 30;
				StartBehavior                             = StartBehavior.WaitUntilFlat;
				TimeInForce                               = TimeInForce.Day;
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
```

#### R16 — §A L31 — no ATR stop, no profit target
**Verdict: FAITHFUL.** The order grep (Verification evidence) shows no Set* calls and only market Enter/Exit.

```text
$ sed -n '50,51p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| Stop-ATR | **not used** — there is no ATR-based stop anywhere in the paper | — |
| Profit target | **none** (unlimited upside by design; abstract p. 2) | Abstract |
```

#### R17 — §A L32 — fixed Contracts; vol-target sizing not ported
**Verdict: SPEC-SILENT.** Regraded from W1's DEVIATION (unauthorised) after W3 F1. Spec L49 makes sizing variant (c); L52/L55 call it a default. Ambiguous → NEEDS AMEAR Q1.

```text
$ sed -n '49,49p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| Stop / exit variants tested | (a) opposite band; (b) `max(VWAP, band)`; (c) = (b) + vol-target sizing | Tables 1–3, pp. 11–15 |
$ sed -n '52,52p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| Vol-target sizing | `σ_target = 2%` daily, leverage capped **4×** | §3 p. 15 |
$ sed -n '55,55p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
Sizing formula (§3 p. 15): `Shares_t = ⌊ AUM_{t-1} · min(4, σ_target/σ_SPY,t) / Open_{t,9:30} ⌋`, with `σ_SPY,t` the 14-day daily-return stdev.
$ sed -n '119,119p' ninjascript/PraxisNoiseAreaBreakout.cs
				Contracts     = 1;                  // position sizing only (NOT a rule knob); paper uses vol-target sizing (§3 p.15) not ported here.
$ sed -n '302,305p' ninjascript/PraxisNoiseAreaBreakout.cs
		[NinjaScriptProperty]
		[Range(1, 20)]
		[Display(Name = "Contracts", Description = "Position size in NQ contracts (sizing only, NOT a rule knob). Paper uses 2% vol-target sizing (§3 p.15), not ported this pass.", GroupName = "02. Praxis (tunable)", Order = 2)]
		public int Contracts { get; set; }
```

#### R18 — §C L50 — bar timestamping assumed close-stamped
**Verdict: FAITHFUL.** The assumption matches what Amear observed (end-stamped, first bar 09:31, Open = 09:30 price).

```text
$ sed -n '16,17p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
1. **Per-day absolute move from Open** (14-day lookback, `i = 1..14`):
   `move_{t-i, 9:30→HH:MM} = | Close_{t-i, HH:MM} / Open_{t-i, 9:30} − 1 |`
$ sed -n '30,30p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Clock/time anchor:** session Open = 09:30 ET; σ is indexed by *minute-of-day* elapsed from the open. Bands **widen through the day** (Fig. 1, p. 8), peaking at 16:00.
$ sed -n '143,143p' ninjascript/PraxisNoiseAreaBreakout.cs
			int mod = Time[0].Hour * 60 + Time[0].Minute;   // minute-of-day of THIS (closed) bar
$ sed -n '150,153p' ninjascript/PraxisNoiseAreaBreakout.cs

				today     = new DayRecord();
				todayOpen = Open[0];            // Open_{t,09:30} (spec §1) — first RTH bar's open
				today.Open = todayOpen;
```

#### R19 — §C L51 — prevClose = Close[1] on first bar of session
**Verdict: FAITHFUL.** Close[1] on the 09:31 bar is the prior 16:00 bar (REPORTED 16:00→09:31). Close1600 is dead state. The line-155 fallback is unreachable (line 140), so §C L51's "first session falls back" is inaccurate.

```text
$ sed -n '26,26p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
`UpperBound = max(Open_{t,9:30}, Close_{t-1,16:00}) · (1 + σ)`
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
```

#### R20 — §C L52 — full-sample Lookback; walk-back up to 29 days
**Verdict: SPEC-SILENT.** It takes the 14 most recent days that HAVE this minute, which differs from i = 1..14 when a day lacks the minute (e.g. early close). The spec does not cover missing data.

```text
$ sed -n '16,19p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
1. **Per-day absolute move from Open** (14-day lookback, `i = 1..14`):
   `move_{t-i, 9:30→HH:MM} = | Close_{t-i, HH:MM} / Open_{t-i, 9:30} − 1 |`
2. **Average move (the band half-width σ) at that minute-of-day:**
   `σ_{t, 9:30→HH:MM} = (1/14) · Σ_{i=1..14} move_{t-i, 9:30→HH:MM}`
$ sed -n '31,31p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Lookback window:** **14 trading days**, fixed (`i = [1,14]`). No lookback grid is tested in the paper.
$ sed -n '79,79p' ninjascript/PraxisNoiseAreaBreakout.cs
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
```

#### R21 — §C L53 — reversal; exit + reverse on the same bar
**Verdict: CANNOT-DETERMINE-STATICALLY.** Every reversal also meets the exit condition (OBSERVED in code; fuzz 0/129,174 here, 0/305,112 by W4). NT8's resolution is INFERRED: clean reverse, double close, or entry ignored.

```text
$ sed -n '38,38p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Positions per session:** **NOT capped at one.** A position is held until the close or until price crosses to the **opposite** boundary, at which point it is closed **and reversed** into a new position that direction (p. 9). Realized average trade frequency is **1.3 trades/day** (base opp-band stop) rising to **1.8 trades/day** with the VWAP stop (Table 4, p. 16). Stops, too, are evaluated only at the semi-hourly stamps (p. 9).
$ sed -n '62,62p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Reversal:** a cross to the opposite boundary closes and reverses (see §2).
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
```

#### R22 — §C L54 — VWAP typical price
**Verdict: SPEC-SILENT.** The price proxy is not pinned by the spec.

```text
$ sed -n '61,61p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
  `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.
$ sed -n '171,176p' ninjascript/PraxisNoiseAreaBreakout.cs
			double vol = Volume[0];
			if (vol > 0)
			{
				vwapCumPV  += ((High[0] + Low[0] + Close[0]) / 3.0) * vol;   // typical-price VWAP
				vwapCumVol += vol;
			}
$ sed -n '265,265p' ninjascript/PraxisNoiseAreaBreakout.cs
			curVwap  = (vwapCumVol > 0) ? vwapCumPV / vwapCumVol : Close[0];
```

#### R23 — §C L55 — sizing / vol-target not ported
**Verdict: SPEC-SILENT.** Same as R17.

```text
$ sed -n '49,49p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| Stop / exit variants tested | (a) opposite band; (b) `max(VWAP, band)`; (c) = (b) + vol-target sizing | Tables 1–3, pp. 11–15 |
$ sed -n '52,52p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
| Vol-target sizing | `σ_target = 2%` daily, leverage capped **4×** | §3 p. 15 |
$ sed -n '55,55p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
Sizing formula (§3 p. 15): `Shares_t = ⌊ AUM_{t-1} · min(4, σ_target/σ_SPY,t) / Open_{t,9:30} ⌋`, with `σ_SPY,t` the 14-day daily-return stdev.
$ sed -n '119,119p' ninjascript/PraxisNoiseAreaBreakout.cs
				Contracts     = 1;                  // position sizing only (NOT a rule knob); paper uses vol-target sizing (§3 p.15) not ported here.
```

#### R24 — §C L56 — session-flat: explicit check + ExitOnSessionClose backstop
**Verdict: CANNOT-DETERMINE-STATICALLY.** "Coincide on strict RTH" is the author's assumption, not an observation. On early-close days FlattenAll never runs.

```text
$ sed -n '64,64p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Session flat:** **all positions closed at the market Close = 16:00 ET** (cash close), never held overnight (Fig. 2 caption p. 9; Fig. 4 p. 12). The paper has **no intraday time-stop** — the only time-based exit is 16:00.
$ sed -n '108,111p' ninjascript/PraxisNoiseAreaBreakout.cs
				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
				ExitOnSessionCloseSeconds                 = 30;
				StartBehavior                             = StartBehavior.WaitUntilFlat;
				TimeInForce                               = TimeInForce.Day;
$ sed -n '188,193p' ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close
			}
```

#### R25 — line 36 instrument comment
**Verdict: BUG.** Comment only: "$5.00 / point (=$1.25 / tick)" is not NQ ($20/pt per project records). The code never uses it.

```text
$ sed -n '36,37p' ninjascript/PraxisNoiseAreaBreakout.cs
// INSTRUMENT: NQ futures. TickSize 0.25, $5.00 / point (=$1.25 / tick). Add this strategy to a
// 1-MINUTE NQ series with an RTH (09:30-16:00 ET) session template in the Strategy Analyzer.
```

#### R26 — VWAP plot with no band
**Verdict: BUG.** Plot only: curVwap is refreshed after the full-sample return, so the plot is 0 or stale when there is no band. No trade effect.

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
```

#### R27 — order realisation: market vs spec L99 stop-market note
**Verdict: CANNOT-DETERMINE-STATICALLY.** All orders are managed market orders (INFERRED type). The spec L99 stop-market idea is permissive, not a rule. The stamp-vs-fill gap is a runtime quantity.

```text
$ sed -n '99,99p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = max/min(Open_{9:30}, PrevClose)`; VWAP anchored at 09:30, market-hours only; **flat at 16:00** (or the trader-chosen 11:30 — see D8). Entry via `EnterLongStopMarket`/`EnterShortStopMarket` at the boundary is a reasonable NT8 realization of "act at the next HH:00/HH:30 stamp if price is outside the band," but note the paper acts on the **stamp**, not on an intrabar stop-touch — a stop-market order can fill mid-bar and diverge slightly; reconcile in b2-signal-repro.
$ sed -n '211,211p' ninjascript/PraxisNoiseAreaBreakout.cs
					ExitLong("XL", "");
$ sed -n '219,219p' ninjascript/PraxisNoiseAreaBreakout.cs
					ExitShort("XS", "");
$ sed -n '227,229p' ninjascript/PraxisNoiseAreaBreakout.cs
				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
$ sed -n '288,290p' ninjascript/PraxisNoiseAreaBreakout.cs
				ExitLong("FlatEOD", "");
			else if (Position.MarketPosition == MarketPosition.Short)
				ExitShort("FlatEOD", "");
```

#### R28 — 09:30 excluded as checkpoint
**Verdict: SPEC-SILENT.** No 09:30-stamped in-session bar exists here anyway (REPORTED).

```text
$ sed -n '36,36p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Entry condition:** at a **semi-hourly checkpoint only** — `HH:00` and `HH:30` — if price is **above** the Upper Boundary → **go long**; if **below** the Lower Boundary → **go short**. Checking only at the half-hour (not tick-by-tick) is deliberate, to avoid acting on transient spikes; the paper shows a breach a few minutes before 10:30 is not acted on until the 10:30 stamp (Fig. 2, p. 9).
$ sed -n '196,196p' ninjascript/PraxisNoiseAreaBreakout.cs
			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
```

#### R29 — ties: exits <=/>=, entries strict >/<
**Verdict: SPEC-SILENT.** Equality is not addressed by the spec; incidence is low.

```text
$ sed -n '36,36p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Entry condition:** at a **semi-hourly checkpoint only** — `HH:00` and `HH:30` — if price is **above** the Upper Boundary → **go long**; if **below** the Lower Boundary → **go short**. Checking only at the half-hour (not tick-by-tick) is deliberate, to avoid acting on transient spikes; the paper shows a breach a few minutes before 10:30 is not acted on until the 10:30 stamp (Fig. 2, p. 9).
$ sed -n '61,61p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
  `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.
$ sed -n '210,210p' ninjascript/PraxisNoiseAreaBreakout.cs
				if (price <= stop)
$ sed -n '218,218p' ninjascript/PraxisNoiseAreaBreakout.cs
				if (price >= stop)
$ sed -n '226,226p' ninjascript/PraxisNoiseAreaBreakout.cs
			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
$ sed -n '228,228p' ninjascript/PraxisNoiseAreaBreakout.cs
			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
```

## D2 — End-stamped bars vs the author's §C assumption

**Premise (REPORTED BY AMEAR, notes:23–27).** Bars are end-stamped. The first RTH bar is stamped 09:31; it covers 09:30–09:31, and its Open is the 09:30 price. The 16:00 bar is followed directly by the next day's 09:31.

**Template hours were never captured.** Reference line 156 (pasted below) records this gap. The dispatch brief's "8:30–16:00 Central = 09:30–16:00 ET" is internally inconsistent: 16:00 CT is 17:00 ET. It is not relied on.

The author assumed "close-stamped" bars (§C L50). That is the same convention as end-stamped, so the one-bar-shift contingency does not arise.

| Mechanism | Lines | Holds under end-stamping? |
|---|---|---|
| `mod = H*60+M` | 143 | **Yes.** The key is the bar's end minute. σ's history and today's checkpoint use the same key (R8). This requires NT8 to display ET (INFERRED from the REPORTED 09:31/16:00 stamps). |
| `IsFirstBarOfSession` | 147 | **Yes.** It is NT8's session flag, true on the 09:31 bar (INFERRED from NT8 semantics plus the REPORTED absence of a 09:30 bar). |
| `todayOpen = Open[0]` | 152 | **Yes.** It is the 09:30 opening price (28605.25 on 2026-07-17, REPORTED). |
| `prevClose = Close[1]` | 155 | **Yes on normal days.** It is the prior 16:00 bar's close. On the day after an early close it is the early-close price, which the spec does not address. The fallback on line 155 is unreachable because of line 140 (R19). |
| `CommitDay()` | 149, 274–283 | **Yes.** It pushes yesterday on the 09:31 bar; there is no look-ahead (R7; W3 attacked it without success). |
| VWAP reset and accumulation | 158–159, 171–176 | **Yes.** It resets before the 09:31 bar accumulates, so it covers 09:30:00 to now (R9). |
| `isCheckpoint` | 196 | **Yes.** Checkpoints are 10:00 … 15:30, 12 per day (enumeration pasted). |
| `mod >= CloseMod → FlattenAll; return` | 188–193 | **The decision holds; the fill is unknown.** See (b) and (c). |

**(a) The 10:00-stamped bar.**
- **Checkpoint fires?** Yes. mod = 600 lies in (570, 960) with Minute = 0. It also needs `haveBand`, i.e. 14 committed days with minute 600 (OBSERVED, lines 196–198 and 257).
- **Stamp price?** The price used is `Close[0]` (line 200), the last trade in 09:59–10:00, which is the 10:00:00 price the paper's `Close_HH:MM` means. The paper's own bar convention is not stated in the spec.
- **Fill?** The resulting market order is expected to fill at the Open of the 10:01-stamped bar, the first trade at or after 10:00:00 (INFERRED; no fill observation is recorded on disk). DECISION_LOG:353's "filled at the next bar's open" is likewise INFERRED, not observed.

**(b) The 16:00-stamped bar.**
- **Flatten triggered?** Yes, by `mod >= 960`.
- **Entry at 16:00 blocked?** Yes, twice over: the `return` on line 192, and `mod < CloseMod` on line 196 (OBSERVED).

**(c) Which order actually closes the 16:00 position: CANNOT-DETERMINE-STATICALLY.**

FlattenAll (lines 288/290) submits a managed market exit on the close of the session's **last** bar, so its "next bar" is the next day's 09:31 (INFERRED). Three settings compete:
- `IsExitOnSessionCloseStrategy = true` (line 108)
- `ExitOnSessionCloseSeconds = 30` (line 109)
- `TimeInForce.Day` (line 111)

The scenarios below are all INFERRED and unranked:

| # | What happens | Trades-tab signature |
|---|---|---|
| S1 | NT8's session-close exit closes the position at 16:00 | exit name "Exit on session close", exit time 16:00 |
| S2 | FlatEOD fills at the next day's 09:31 Open | an overnight hold, which breaks spec L64 |
| S3 | The Day-TIF FlatEOD expires; the position carries into the next session | entry date earlier than the exit date |
| S4 | Both S1 and FlatEOD fire | a spurious extra row |
| S5 | The template actually ends after 16:00 ET; FlatEOD fills the same day at 16:01 | contradicted only for the one date Amear read |

**Early-close days.** No bar reaches `mod >= 960`, so FlattenAll never runs. If the early close falls on a :00 or :30 stamp, the last bar is also a checkpoint, so an entry can be placed whose next bar is the next session.

**Settle it with the readback in NEEDS AMEAR R1.**

## D3 — Order-type inventory

From the order grep (Verification evidence): 8 matching lines. Lines 224–225 are comments, which leaves **6 call sites**.

| Line | Call | NT8 order type |
|---|---|---|
| 211 | `ExitLong("XL","")` | managed market exit (INFERRED) |
| 219 | `ExitShort("XS","")` | managed market exit (INFERRED) |
| 227 | `EnterLong(Contracts,"L")` | managed market entry; a managed reverse when short (INFERRED) |
| 229 | `EnterShort(Contracts,"S")` | managed market entry; a managed reverse when long (INFERRED) |
| 288 | `ExitLong("FlatEOD","")` | managed market exit (INFERRED) |
| 290 | `ExitShort("FlatEOD","")` | managed market exit (INFERRED) |
| (108) | platform "Exit on session close" | market exit (INFERRED) |

- **No other order methods** (OBSERVED by the grep): no `Set*`, no `Submit*`, no Limit/StopMarket/StopLimit variants.
- **Exit evaluation:** "trailing stops" are clock-sampled conditions that send market orders, not resting stop orders. This is consistent with spec L38.
- **On-disk sources:** no file on disk records an observation of NT8 order types, and none mentions "managed approach" (searched by W2, re-checked by W4). The market-order classification is NT8 documentation knowledge and therefore **INFERRED**.

**Every reversal also meets the exit condition (OBSERVED in code; fuzz-confirmed).**
- From lines 263–264, `curLower ≤ curUpper`. A long is reversed only when `price < curLower`, and its stop is ≥ `curUpper`, so the exit on line 211 is also reached. The short case mirrors this.
- Fuzz: 0 of 129,174 reversals here and 0 of 305,112 in W4's run lacked the exit. The mutant arm fires.
- Whether NT8 submits both orders, and whether it then reverses cleanly, double-closes, or ignores the entry, is **INFERRED / CANNOT-DETERMINE-STATICALLY**.
- Run 2's commission identity ($121.36 = 41 × 2.96 = 82 × 1.48) does **not** discriminate between these outcomes. A double close booked as extra Qty-1 rows gives the same identity (W4 F2). The notes also print the figure as "(= 41 × 2.96)", so it may have been computed rather than read off the screen.

**The 2-tick slippage and the $21,500 formula.**
- Every strategy-originated order is a market order, so if the Analyzer slips market fills (INFERRED; Amear's framing, no on-disk observation), every fill in run 3 is slipped.
- The arithmetic is right: 1,075 × 2 × 2 × $5 = 21,500 (pasted).
- The figure holds only if all of the following hold:
  1. Every row is Qty 1 with two fills, and no row is a spurious double-close row.
  2. Slippage hits both sides, including platform session-close exits (INFERRED).
  3. NT8 does not clamp slippage to the bar's high/low (UNVERIFIED).
  4. NQCONT's $20 point value and 0.25 tick size are honoured on a non-Future instrument type. That is UNVERIFIED per `docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:224`. If it fails, every dollar figure in all three runs is wrong by the same factor.
  5. Run 3 really used Slippage 2. Its commission was not read back.
- **Verdict:** the formula is the right *shape* and an **upper bound** under conditions 1–5. It is not a measured figure.

**ExitOnSessionClose in addition to FlattenAll?** Yes. Both can act on the 16:00 bar; that is scenario S4 (INFERRED).

## D4 — Run 1 (48 trades) vs run 2 (41 trades): NOT resolved

- **Costs cannot change the trade count (OBSERVED).** No decision reads a fill price or P&L: the null arm is 0 and the positive control `Position.MarketPosition` matches 6 in the same file. Commission and slippage therefore cannot change which orders are sent; they change only fill prices and dollars.
- **The trade set differed, not just costs (INFERRED).** Run 2 added $121.36 of commission and still had a higher net ($599.08 vs $225.64), and the counts differ. Adding costs to an identical set of trades can only lower net.

Ranked hypotheses, all INFERRED:
1. **Trading-hours template** was not CME US Index Futures RTH in run 1 (`<Use instrument settings>`, ETH, or 24×7). That moves `IsFirstBarOfSession` to the evening open, so `todayOpen`, σ's anchor, `prevClose` and VWAP all change, and `mod >= 960` fires every evening. The trade set changes wholesale. **Largest.**
2. **Exit on session close** or **Time in force** differed. Both are Analyzer-editable, and they decide D2(c). A position carried overnight changes the next day's `Position.MarketPosition` at checkpoints, which changes whether entries fire.
3. **Instrument or data series** differed, e.g. a dated NQ contract with partial data (W4 F4). The effect is unbounded.
4. **Date range, warm-up, or data state.** The 14-session σ warm-up (line 257) is a large share of a 3.5-month window.
5. **Order fill resolution** High vs Standard. This could change how same-bar exit+reverse pairs and the 16:00 orders resolve.
6. **ExitMode = OppBand.** For the code's OppBand, `stop = curUpper ≤ max(curUpper, VWAP)`, so OppBand exits less often and should give **fewer** trades, not more (W4 path fuzz 0/200,000). The default is BandOrVWAP (line 118). Low.
7. Entries per direction / Entry handling, Price based on (Bid/Ask), bar type/value, Bars required to trade, Break at EOD. Low.
8. Contracts / Set order quantity: quantity, not count. ~0.
9. Slippage / commission: **0** (OBSERVED null above).

**Fields for Amear to read back** (for run 1, if NT8 still lists it; otherwise re-run run 2 changing one field at a time):
- Instrument
- Trading hours
- Exit on session close (and seconds)
- Time in force
- Order fill resolution
- Slippage
- Include commission
- Start date / End date
- Price based on
- Type / Value
- Break at EOD
- ExitMode
- Contracts
- Entries per direction
- Entry handling
- Bars required to trade
- Set order quantity

## D5 — Plain verdict

**Verdict:** the code's decisions are a faithful copy of the *spec's* rules for full 09:30–16:00 sessions in the configuration of runs 2–3 (ExitMode BandOrVWAP, RTH template). Within that scope, no bug was found that changes a trade decision.

**Evidence levels for this verdict.**
- The code text is OBSERVED.
- The runtime premises are not observed:
  - end-stamped bars and 16:00 → 09:31 are REPORTED BY AMEAR (R18, R19);
  - NT8 displaying ET is INFERRED (R8, R10);
  - RTH-only VWAP depends on the template (R9);
  - run 1's configuration is unknown.
- The paper itself was not read; the spec is its proxy.

For ExitMode = BandOrVWAP, the following match the spec's text (code OBSERVED; premises as above; D1 R1–R11, R13, R16, R18, R19):
- the σ math (lines 244–260)
- the gap-adjusted bands (261–264)
- the no-look-ahead history (149, 274–283)
- the VWAP anchor (158–159, 171–176)
- the HH:00/HH:30 checkpoints (196)
- entry (226–229)
- the band-or-VWAP exit (205–220)
- the 16:00 flatten decision (189–193)

**Defects and deviations found, with line numbers:**
1. **DEVIATION (unauthorised), R14.** The OppBand mode stops at the same-side band (lines 209, 217; comment line 45), where the spec says the opposite band (spec L38, L49, L59). Not used in runs 2–3. Run 1's mode is unknown.
2. **BUG (comment only), R25.** Line 36 says "$5.00 / point (=$1.25 / tick)", which is not NQ.
3. **BUG (plot only), R26.** The VWAP plot (lines 185–186) shows 0 or a stale value when no band is built, because curVwap is refreshed only at line 265.
4. **Dead or inaccurate code, not a behaviour defect.** `Close1600` (lines 68, 168–169) is never read. The fallback on line 155 is unreachable because of line 140. The author's §C L51 claim about it is therefore wrong.

**What this verdict does NOT cover.** Four items cannot be settled from source, and any of them could make the backtest's *executed* trades diverge from the rules:
- **D2(c), R15/R24:** how the 16:00 exit is filled (lines 108–111, 188–193, 285–291).
- **D3, R21, R12:** how NT8 resolves the same-bar exit plus reverse (lines 106–107, 211/219 with 227/229).
- **R27:** the gap between the stamp price and the fill (market orders at lines 211, 219, 227, 229, 288, 290; INFERRED next-bar-open fill).
- **Early-close days.** The 16:00 cut-off is hard-coded (lines 58, 189, 196), so on a session that ends early the code never decides to flatten. If the early close falls on a :00/:30 stamp, the code can also enter on the last bar. Unless NT8's session-close exit acts, this conflicts with spec L64, "never held overnight". That depends on the template's early-close rows (INFERRED). Strictly, this is a decision-level gap; see NEEDS AMEAR R6.

Until Amear reads them back, the backtest numbers are reported, not validated. Holding the walk-forward stays Amear's ruling. This report neither lifts it nor extends it.

## NEEDS AMEAR — recommended, NOT applied

**Readbacks** (no code change; these settle the CANNOT-DETERMINE rows):
- **R1. 16:00 exits.** Run 2's Trades tab: tally the Exit-name column (FlatEOD / Exit on session close / XL / XS / Close position / other). For each end-of-day row, read the exit time (16:00 or 09:31) and whether the entry date equals the exit date.
- **R2. Reversals.** Trades tab: any Qty > 1, and any two exit rows with the same timestamp. Executions tab: the number of executions at one reversal timestamp. Log tab: any "ignored" order messages.
- **R3. Point value.** Recompute one run-2 trade's Profit as (exit − entry) × 20 × direction − $2.96. Compare the fill prices with the next bar's Open to see whether slippage is clamped.
- **R4. Template hours.** `Tools > Trading Hours > CME US Index Futures RTH`: the printed session hours and holiday/early-close rows. This closes reference line 156.
- **R5. Run 1.** The D4 field list above.
- **R6. Early-close days.** In run 3's Trades tab, find rows whose entry falls on an early-close date listed in the RTH template (see R4). Read each row's exit name, exit date and exit time. This shows whether those positions were flattened the same day.

**Questions that are his** (S8):
- **Q1. Sizing.** Is the replication target paper variant (b), which is unsized and what the code is, or (c) = (b) + 2% vol-target sizing? (R17/R23; spec L49 vs L52/L55)
- **Q2. OppBand.** Should OppBand mean the paper's opposite band? Options:
  - change lines 209 and 217 to `curLower` / `curUpper`. With that change, the OppBand exit coincides with the reversal trigger, so OppBand becomes "reverse or hold to 16:00";
  - keep it and rename the mode;
  - drop it.

**Code changes that would follow from his answers** (line numbers only; none applied):
- **C1.** Line 36: correct the comment to $20/point, $5/tick.
- **C2.** Lines 185–186 and 265: compute curVwap before the full-sample return at 257, so the plot is right.
- **C3.** If R1 shows FlatEOD filling at the next day's 09:31 or carried positions: change how the 16:00 flat is realised (lines 108–111, 189–193). For example, flatten on the 15:59 bar, or rely on ExitOnSessionClose explicitly. This changes "act at the stamp" semantics, so it is his call.
- **C4.** If R2 shows double closes or ignored reversals: skip the exit block when the reversal condition holds (lines 205–229).
- **C5.** Diagnostic only: `TraceOrders = true` in SetDefaults (around line 113), so the Output window shows NT8's order handling.
- **C6.** Cosmetic: remove the dead `Close1600` (lines 68, 168–169) and the unreachable guard on line 155, and correct report §C L51.
- **C7.** Out of scope, flagged by W1: `DECISIONS.md:231` says the strategy measures point distances, but it measures a ratio (line 253). Whether the back-adjustment matters numerically is NOT CHECKED.

## Verification evidence
Manager-run, this session. The scratch paths are shortened to `mgr/` in the command echoes.
```text
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
$ git diff --stat HEAD -- ninjascript/PraxisNoiseAreaBreakout.cs | wc -l
       0
$ /usr/bin/grep -nE "Enter(Long|Short)|Exit(Long|Short)|Set(StopLoss|ProfitTarget|TrailStop)|Submit" ninjascript/PraxisNoiseAreaBreakout.cs
211:					ExitLong("XL", "");
219:					ExitShort("XS", "");
224:			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
225:			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
227:				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
229:				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
288:				ExitLong("FlatEOD", "");
290:				ExitShort("FlatEOD", "");
$ /usr/bin/grep -cE "AveragePrice|SystemPerformance|Account|GetProfitLoss|OnExecutionUpdate|OnOrderUpdate|Execution" ninjascript/PraxisNoiseAreaBreakout.cs   # null arm
0
$ /usr/bin/grep -c "Position.MarketPosition" ninjascript/PraxisNoiseAreaBreakout.cs   # positive control, same file
6
$ /usr/bin/grep -n "Close1600\|TraceOrders\|IsExitOnSessionClose\|ExitOnSessionCloseSeconds\|TimeInForce" ninjascript/PraxisNoiseAreaBreakout.cs
68:			public double Close1600;                             // Close_{t,16:00} (prev-close ref, spec §1 p.7)
108:				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
109:				ExitOnSessionCloseSeconds                 = 30;
111:				TimeInForce                               = TimeInForce.Day;
169:				today.Close1600 = Close[0];
$ python3 -c "print([f\"{m//60:02d}:{m%60:02d}\" for m in range(571,960) if m%60 in (0,30)])"
['10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30']
$ python3 -c "print(41*2.96, 82*1.48, 1075*2*2*5, 1075*2.96, 41*2*2*5)"
121.36 121.36 21500 3182.0 820
$ python3 -I mgr/fuzz.py          # real port
mutant=False cases=500000 reversals=129174 reversal_without_exit=0
$ python3 -I mgr/fuzz.py mutant   # positive arm: exit disabled, detector must fire
mutant=True cases=500000 reversals=129174 reversal_without_exit=129174
$ cp ninjascript/PraxisNoiseAreaBreakout.cs mgr/t.cs && printf " " >> mgr/t.cs && shasum -a 256 mgr/t.cs   # tamper trip of the hash gate
157de48c7076a5d5f849f91fab890e13df9f9472233c8f7755b4a6dcb60f096e  t.cs
[manager annotation, outside the captured output: the path on the line above was shortened by a `sed` in the capture. The raw, unedited re-run is under Addendum E-W6.]
$ sed -n "33p;36,40p" docs/reports/2026-10-28-voice-session-notes.md | cut -c1-150
- **Strategy Analyzer settings:** PraxisNoiseAreaBreakout · NQCONT · Last · Minute 1 · trading hours CME US Index Futures RTH · ExitMode BandOrVW
| Run | Range | Trades | Net profit | Commission | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| 1 (settings not verified; may have reset) | 2026-04-01 → 2026-07-17 | 48 | $225.64 | $0 (not included) | — | — |
| 2 (all fields read back by Amear) | 2026-04-01 → 2026-07-17 | 41 | $599.08 | $121.36 (= 41 × 2.96) | — | — |
| 3 (full history, same settings) | 2021-03-08 → 2026-07-17 | **1,075** | **$1,281.61** | — | **1.04** | **$4,051.57** |
$ sed -n "156p" docs/reference/2026-07-24-nt8-windows-reference.md | cut -c1-200
- 🔲 **TODO (residual gap):** the **"CME US Index Futures RTH"** template's exact printed session hours were **not** captured. Verify **09:30–16:00 ET** equivalence via `Tools > Trading Hours` and
```

The `git diff --stat` count of 0 shows the code is unmodified against HEAD. The hash at the end of the unit is the same as at the start.

## Adversarial findings
- **W3 against D1: `VERDICT: FAIL`.**
  - F1 MAJOR: R17/R23 "unauthorised" graded above the evidence. **Accepted** and regraded to SPEC-SILENT.
  - F2–F7 MINOR, all **accepted** and corrected through W1's C2–C7:
    - the MNQ explanation struck;
    - the run-1 ExitMode caveat added;
    - the DECISION_LOG grep pasted;
    - the ET display-time dependency stated;
    - Day TIF added;
    - paper pages added.
  - W3 also found no break in: off-by-one minute-of-day, look-ahead, pre-RTH VWAP contamination, R14, R19's unreachable fallback, R20, R21, R27, or coverage.
- **W4 against D2–D4: `VERDICT: FAIL`.**
  - F1 MAJOR: "OBSERVED" for both orders being submitted. **Accepted**: the code-level condition stays OBSERVED; NT8 submission becomes INFERRED.
  - F2 MAJOR: the commission identity was over-read. **Accepted**: it no longer discriminates.
  - F3–F8 MINOR, all **accepted** and corrected through W2's C3–C8:
    - tick size UNVERIFIED;
    - Instrument hypothesis added;
    - scenario S5 added;
    - paper ratio no longer used as corroboration;
    - TraceOrders and checkpoint evidence pasted;
    - the 56/20 counts annotated as an observer effect, figures not edited.
  - W4 also found no break in: OppBand-fewer-trades, the "trade set differed" argument, D4 non-resolution, and S8.
- **W6 against this manager report: `VERDICT: FAIL`** (3 MAJOR, 8 MINOR). See the Addendum.

## S6 cross-block check
This unit approves no deviation, so there is nothing new to test across blocks. Its findings do touch other blocks' criteria, and are named here so they are not lost:
- **F2 (FROZEN, session-flat vs breakers #4/#5).** D2(c) shows the 16:00 flat's realisation in the backtest is unknown. If positions carry overnight (S2/S3), the backtest violates the very rule F2 is trying to settle. F2 stays FROZEN. This unit does not touch it.
- **F3 (FROZEN, fill resolution and slippage).** D3 shows every fill is a market fill (INFERRED type), so the Analyzer's 2-tick setting is applied to every market fill (INFERRED). DECISION_LOG:442 locks `[N]` as **band-edge** slippage. Whether that lock was meant to cover session-close and stop-out exits as well is Amear's scope question; it is not decided here (pasted under Addendum E-W6). Its dollar effect also depends on the UNVERIFIED NQCONT point value.
- **O4 (backtest/live parity).** If NT8 double-closes on reversals (R21), the backtest trade count is inflated. That count feeds the breaker #2/#3 and Block 4 win-rate parity comparisons.
- **F1 (signal topology).** This strategy computes its signal inside NT8, with no file-drop or n8n gate (code lines 25–27). That is a known input to F1, not new here.

## Addendum: W6 findings and disposition
W6 (`af49857e96bd6793b`) wrote `docs/reports/2026-10-30-3gm-worker6-adversarial-manager.md`. I accepted all 11 findings and edited this report in place; the pre-edit copy is kept in scratch as `mgr/report.pre-w6.md`.

**MAJOR:**
- **F1:** D5 overclaimed and omitted early-close days, R27 and R12. Fixed: D5's scope is narrowed, four items are now uncovered, and NEEDS AMEAR R6 is added.
- **F2:** "OBSERVED" was applied to premises that are REPORTED or INFERRED, and the verdict said "paper" for the spec. Fixed: D5 now carries evidence levels and says "spec".
- **F3:** "Files staged" was false at the time W6 read it. Fixed: the files are now staged, and the `git diff --cached` output is pasted below.

**MINOR:**
- **F4:** the W1 diff count was wrong. Fixed to 36 added, 1 removed (pasted below).
- **F5:** the R5 table row broke on unescaped pipes. Fixed.
- **F6:** the Verdict claimed D2 (a)–(e). Fixed to (a)–(c) plus early-close days.
- **F7:** this Addendum was referenced but missing. Added.
- **F8:** the 2-tick scope was stated as fact. Now INFERRED, and its scope is put to Amear.
- **F9:** the tamper-trip output had been edited. Annotated, with the raw re-run below.
- **F10:** the $20/pt source is now pasted below.
- **F11:** the fuzz port's omissions are now noted under Self-grade limits.

W6 found no break in: all 93 D1 `sed` pastes (byte-identical), the 15/0/1/2/6/5 counts, the R17/R23 grade, every evidence-block command including the fuzz, and S8 (apart from F8).

**E-W6, evidence for F4/F9/F10/F8 (manager-run):**
```text
$ diff w5/A.orig worker1-checklist.md | /usr/bin/grep -c "^<" ; ... -c "^>"  (A = W1)
1
36
$ same for B = W2 (removed, added)
0
45
$ tail -1 (verdict / status tokens of worker files)
docs/reports/2026-10-30-3gm-worker1-checklist.md: WORKER STATUS: COMPLETE
docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md: WORKER STATUS: COMPLETE
docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md: VERDICT: FAIL
docs/reports/2026-10-30-3gm-worker4-adversarial-d2d4.md: VERDICT: FAIL
docs/reports/2026-10-30-3gm-worker6-adversarial-manager.md: VERDICT: FAIL
$ cp ninjascript/PraxisNoiseAreaBreakout.cs $S/mgr/t.cs && printf " " >> $S/mgr/t.cs && shasum -a 256 $S/mgr/t.cs   (raw, unedited)
157de48c7076a5d5f849f91fab890e13df9f9472233c8f7755b4a6dcb60f096e  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/mgr/t.cs
$ sed -n "62p" docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md
| Point value | `20` (so tick value is $5) |
$ sed -n "442p" DECISION_LOG.md | cut -c1-330
- [2026-10-30T21:36:30Z] **WHO: amear** | PROPOSED BY: amear | APPROVED BY: amear, 2026-10-28 (voice session), reaffirmed in this session's opening message | WHAT: **F3 `[N]` IS SET: band-edge slippage = 2 ticks per side ($10/side at $5/tick; with $2.96 commission ≈ $22.96 per round trip). Fill resolution = Standard, on 1-minu
```

## Files staged
Report files only, via `git add`. Nothing else. Output captured after staging:
```text
$ git diff --cached --name-status -- docs/reports/2026-10-30-3gm-* ninjascript/
A	docs/reports/2026-10-30-3gm-fidelity-check.md
A	docs/reports/2026-10-30-3gm-worker1-checklist.md
A	docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md
A	docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md
A	docs/reports/2026-10-30-3gm-worker4-adversarial-d2d4.md
A	docs/reports/2026-10-30-3gm-worker6-adversarial-manager.md
```
- `docs/reports/2026-10-30-3gm-fidelity-check.md` (this report)
- `docs/reports/2026-10-30-3gm-worker1-checklist.md`
- `docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md`
- `docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md`
- `docs/reports/2026-10-30-3gm-worker4-adversarial-d2d4.md`
- W6's report, if written (see Addendum)

## Self-grade limits
- **NT8 was not run.** Every claim about fills, reversal resolution, session-close exits, TIF expiry, slippage application and point value is INFERRED. The "no bug that changes a trade decision" verdict covers the code's decisions, not NT8's execution of them.
- **The paper was not read.** The spec stands in for it. Where the spec is ambiguous (L59's parenthetical; sizing L49 vs L52/L55), I graded down, not up.
- **Amear's VM facts are REPORTED.** End-stamping, 16:00 → 09:31, and the run settings and results all come from his hand-run, which no Claude has seen.
- **Coverage gaps.** I did not check `~/praxis-signals/` or any file outside the repo for NT8 observations, nor whether the paper's own data is start- or end-stamped (spec-silent).
- **Fuzz scope.** The fuzz tests a python port of the decision logic. The port's fidelity rests on reading lines 205–229 and 261–264, not on a compile.
- **Fuzz port limits.** The port omits the `vwapCumVol > 0` guard, so it always uses the VWAP branch in BandOrVWAP mode. It also hard-codes the assumption that the position is read before any fill. Neither changes the result for the claim tested (W6 F11).
- **W6 was not re-run on the fixes.** Its 11 findings were applied by me, not re-attacked. The auditor is the next independent check.
- **I graded my own synthesis.** The auditor's grade governs.

## Verdict
D1–D5 are delivered: 29 rows with pasted `sed` evidence, D2 (a)–(c) plus early-close days, the D3 inventory with a conditional formula, D4 ranked and unresolved, D5 with line numbers, and NEEDS AMEAR. Two adversaries failed the first drafts. All 15 findings were accepted, corrected, and checked by diff. The code is unmodified (hash unchanged; diff count 0). Nothing was decided for Amear. On my reading of S1, S2, S5, S8, R3 and the unit criterion, the unit meets its bar, W6's 11 findings are applied (Addendum).

Result: PASS

## Audit-1 corrections (2026-10-30)

This is the correction pass for audit 1 (strike one). praxis-master dispatched it at 2026-10-30T22:16:00Z. The section is appended; everything above it is byte-unchanged (proof at the end). Where a sentence above conflicts with a correction here, the correction governs. The manager captured all the output below in this pass, in `/Volumes/Sensidine/Praxis.build` at HEAD `fc77f36`. In command echoes, `$S` is the session scratchpad `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad`; `ls` and `shasum` print it in full. `$R` is this report. No worker was dispatched in this pass.

### 1. Costs and the trade count (BLOCKING; S2, S9/R3)

The two lines as they stand above (unchanged):
```text
$ sed -n '776p;788p' docs/reports/2026-10-30-3gm-fidelity-check.md
- **Costs cannot change the trade count (OBSERVED).** No decision reads a fill price or P&L: the null arm is 0 and the positive control `Position.MarketPosition` matches 6 in the same file. Commission and slippage therefore cannot change which orders are sent; they change only fill prices and dollars.
9. Slippage / commission: **0** (OBSERVED null above).
```

The code-level evidence. The null arm returns 0. The positive control finds the position reads in the same file. The widened arm's hits are all `//` comments or `[Display]` attribute strings, so none is executable code:
```text
$ /usr/bin/grep -cE "AveragePrice|SystemPerformance|Account|GetProfitLoss|OnExecutionUpdate|OnOrderUpdate|Execution" ninjascript/PraxisNoiseAreaBreakout.cs
0
$ /usr/bin/grep -c "Position.MarketPosition" ninjascript/PraxisNoiseAreaBreakout.cs
6
$ /usr/bin/grep -n "Position.MarketPosition" ninjascript/PraxisNoiseAreaBreakout.cs | cut -c1-110
201:			MarketPosition mp = Position.MarketPosition;
224:			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
226:			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
228:			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
287:			if (Position.MarketPosition == MarketPosition.Long)
289:			else if (Position.MarketPosition == MarketPosition.Short)
$ /usr/bin/grep -niE "ProfitLoss|Commission|Slippage|Performance|Trades|AveragePrice|Account|Execution|Fill|Order" ninjascript/PraxisNoiseAreaBreakout.cs | cut -c1-100
25:// This is NOT the file-drop signal consumer (PraxisSignalConsumer.cs) — it carries no order
26:// pipeline, no JSON, no share watcher. It computes the band itself from bar history and trades
92:		// order actions still fire ONLY at HH:00/HH:30 checkpoints — spec §2 p.9).
178:			// ---- Build the band for THIS bar's minute-of-day (for plots every bar; orders only at chec
225:			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correc
299:		[Display(Name = "Exit mode (ONLY tunable)", Description = "OppBand = trailing stop at same-sid
304:		[Display(Name = "Contracts", Description = "Position size in NQ contracts (sizing only, NOT a 
```

**Corrected statement.** The bullet at :776 joins two claims that have different evidence. Split, they read:

- **(a) Code level, OBSERVED.** No order decision reads a fill price, a P&L, the account or an execution event (null arm 0; widened arm has no code hits). The code does read position state (positive control 6: lines 201, 226, 228, 287, 289, plus the comment at 224). Commission and slippage are therefore not inputs to any order decision.
- **(b) Runtime level, INFERRED.** Position state is set by fills, and lines 201, 226, 228, 287 and 289 branch on it. So "costs cannot change the trade count" also needs an NT8 premise: *NT8's Include-commission and Slippage settings alter fill prices and P&L only, and do not alter whether, when or at what quantity a managed market order fills; no observation of this on this install exists on disk.* The no-observation clause is the master's wording. This pass did not search the disk for such an observation, so the negative is UNVERIFIED. The premise was set by inspection, not by experiment.
- **Readback that settles (b), in R3 toggle form:** re-run run 2 with Slippage 0 and Include commission off, hold every other field, and compare the trade count with run 2's 41 (REPORTED). The same count is consistent with the premise. A different count falsifies it, and D4 #9 returns to the ranking.
- **Corrected :776:** "Costs are not an input to any order decision (OBSERVED, code level). Whether costs can change the trade count through NT8's fill handling is INFERRED (premise above) and untested."
- **Corrected D4 item 9 (:788):** "Slippage / commission: 0 at the code level (OBSERVED); runtime invariance INFERRED."

**Bearing on D4 hypothesis #1 (not analysed further).** The master's run-3 record, `docs/reports/2026-10-30-run3-backtest-screenshot-record.md`, section "(A)", transcribes run 3's trading-hours template as `CME FX Futures RTH`. The voice notes report `CME US Index Futures RTH`:
```text
$ sed -n '22p' docs/reports/2026-10-30-run3-backtest-screenshot-record.md
| Time frame | Trading hours | **CME FX Futures RTH** |
$ sed -n '93p' docs/reports/2026-10-30-run3-backtest-screenshot-record.md | cut -c1-230
**(A) Trading hours = `CME FX Futures RTH`.** The notes (`:33`) report the saved template "Praxis Backtest" as `trading hours CME US Index Futures RTH`. The screenshot shows a different template selected for the run on screen. The
$ sed -n '33p' docs/reports/2026-10-28-voice-session-notes.md | cut -c1-150
- **Strategy Analyzer settings:** PraxisNoiseAreaBreakout · NQCONT · Last · Minute 1 · trading hours CME US Index Futures RTH · ExitMode BandOrVW
```

Labels: the template is OBSERVED-in-image for run 3 (the master transcribed it from `docs/reports/evidence/2026-10-30-run3-strategy-analyzer-summary.webp`), and UNKNOWN for runs 1 and 2. This supports hypothesis #1 only in one respect: the template can differ between runs on this install. It does not say which template runs 1 and 2 used.

### 2. E-W6 diff commands (MINOR; S1)

The real commands, with full paths. `A.orig` and `B.orig` are the scratch copies that the body's E-W6 diff used. They cannot be recreated from git, because neither blob is in the object store (the `git cat-file` lines below). Their hashes are pasted so they can be identified. The worker files have no unstaged edits, so the working-tree file is the staged one.
```text
$ ls -la $S/w5/A.orig $S/w5/B.orig
-rw-r--r--@ 1 admin  wheel  68759 Oct 30 17:57 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/w5/A.orig
-rw-r--r--@ 1 admin  wheel  65569 Oct 30 17:57 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/w5/B.orig
$ shasum -a 256 $S/w5/A.orig $S/w5/B.orig
c62a0e6de719fa02f00568bfb0f0c7f5bcf53510f3b5b75d3f1e65c33051d326  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/w5/A.orig
4f3b06f8f63999e9fffbf5975e8f982f8b770f841502d412ba4a6e037b481cde  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/w5/B.orig
$ for f in A B; do h=$(git hash-object $S/w5/$f.orig); print -r -- "$f.orig blob $h: $(git cat-file -t $h 2>&1)"; done
A.orig blob 5dd8d763a4640722f9308b9f4b2c3786cf28461f: fatal: git cat-file: could not get object info
B.orig blob 45b94a3784926e576048c4c5d0cd99e31cf3e699: fatal: git cat-file: could not get object info
$ git diff --quiet -- docs/reports/2026-10-30-3gm-worker1-checklist.md docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md; print -r -- "unstaged-diff exit=$?"
unstaged-diff exit=0
$ diff $S/w5/A.orig docs/reports/2026-10-30-3gm-worker1-checklist.md | /usr/bin/grep -c "^<"
1
$ diff $S/w5/A.orig docs/reports/2026-10-30-3gm-worker1-checklist.md | /usr/bin/grep -c "^>"
36
$ diff $S/w5/B.orig docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md | /usr/bin/grep -c "^<"
0
$ diff $S/w5/B.orig docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md | /usr/bin/grep -c "^>"
45
```

Result: A (W1) removed 1, added 36. B (W2) removed 0, added 45. This matches E-W6 and the auditor's re-run. Limit: the scratch originals are session-local and are not part of the artifact.

### 3. D1 verdict counts (MINOR; S1)

The count over the D1 table rows (lines 61–101). Each row's last cell is the verdict. The escaped pipes in R5 do not move the last cell.
```text
$ sed -n '61,101p' docs/reports/2026-10-30-3gm-fidelity-check.md | /usr/bin/grep -c '^| R[0-9]'
29
$ sed -n '61,101p' docs/reports/2026-10-30-3gm-fidelity-check.md | /usr/bin/grep '^| R[0-9]' | awk -F'|' '{v=$(NF-1); gsub(/^ +| +$/,"",v); print v}' | sort | uniq -c
   2 BUG
   5 CANNOT-DETERMINE-STATICALLY
   1 DEVIATION (unauthorised)
  15 FAITHFUL
   6 SPEC-SILENT
```

29 rows: FAITHFUL 15 · DEVIATION (unauthorised) 1 · BUG 2 · SPEC-SILENT 6 · CANNOT-DETERMINE-STATICALLY 5. 15+1+2+6+5 = 29. DEVIATION (authorised) has no row, which is 0. This matches the counts line at :63.

### 4. Fuzz port (MINOR; S1)

**Option taken: the full source is pasted inline (below), with its invocation and output.** It is also **downgraded to illustration**. The claim (a reversal at a checkpoint is always preceded by an exit on the same bar) rests on the inequality argument alone. The mutant arm (`exit_ = False`) only shows that the counter fires. It does not test the port's fidelity, which rests on reading lines 205–229 and 261–264 (Self-grade limits).
```text
$ cat $S/mgr/fuzz.py
# Port of PraxisNoiseAreaBreakout.cs lines 205-229 + 261-264 (decision logic only).
import random, sys
MUTANT = len(sys.argv) > 1 and sys.argv[1] == "mutant"   # mutant: exit block never fires
def step(price, up, lo, vwap, pos, mode):
    exit_ = False
    if pos == "L":
        stop = max(up, vwap) if mode == "BandOrVWAP" else up
        exit_ = price <= stop
    elif pos == "S":
        stop = min(lo, vwap) if mode == "BandOrVWAP" else lo
        exit_ = price >= stop
    if MUTANT: exit_ = False
    rev = (price > up and pos == "S") or (price < lo and pos == "L")
    return exit_, rev
random.seed(1); n = rev_n = bad = 0
for _ in range(500000):
    o = random.uniform(1e4, 3e4); pc = o * random.uniform(0.97, 1.03); s = random.uniform(0, 0.03)
    up = max(o, pc) * (1 + s); lo = min(o, pc) * (1 - s)
    price = o * random.uniform(0.9, 1.1); vwap = o * random.uniform(0.95, 1.05)
    pos = random.choice("LSF"); mode = random.choice(["OppBand", "BandOrVWAP"])
    e, r = step(price, up, lo, vwap, pos, mode); n += 1
    if r: rev_n += 1; bad += (not e)
print(f"mutant={MUTANT} cases={n} reversals={rev_n} reversal_without_exit={bad}")
```
```text
$ shasum -a 256 $S/mgr/fuzz.py
c767d2c9c246d6d9d75e9682f57612fb8560039ed8889596a4713a5108c31eb1  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/mgr/fuzz.py
$ cd $S/mgr && python3 -I fuzz.py; python3 -I fuzz.py mutant; cd /Volumes/Sensidine/Praxis.build
mutant=False cases=500000 reversals=129174 reversal_without_exit=0
mutant=True cases=500000 reversals=129174 reversal_without_exit=129174
```

### 5. :103 OnBarClose semantics (MINOR; S9/R3)
```text
$ sed -n '103p' docs/reports/2026-10-30-3gm-fidelity-check.md
**Verdict: FAITHFUL.** OnBarClose means Close[0] is a finished bar; σ look-ahead is handled by the history store (R7).
$ sed -n '39p;105p' ninjascript/PraxisNoiseAreaBreakout.cs | cut -c1-110
// NO LOOK-AHEAD: Calculate.OnBarClose + the 14-day σ lookback reads only COMPLETED prior sessions
				Calculate                                 = Calculate.OnBarClose;
```

**Corrected :103:** "**Verdict: FAITHFUL.** The code sets `Calculate = Calculate.OnBarClose` (line 105, OBSERVED). That `Close[0]` is then the close of a finished bar is NT8 runtime semantics (INFERRED; not observed on this install). σ look-ahead is handled by the history store (R7)." The FAITHFUL grade is for the code's choice against spec L16. The runtime half is INFERRED.

### 6. :395 R15 "next bar" (MINOR; S9/R3)
```text
$ sed -n '395p' docs/reports/2026-10-30-3gm-fidelity-check.md
**Verdict: CANNOT-DETERMINE-STATICALLY.** Decision is faithful: flatten on the 16:00 bar, entries blocked. The fill is unknown: the market exit's "next bar" is the next day's 09:31; ExitOnSessionClose(30 s) and Day TIF compete (D2c).
$ sed -n '718p' docs/reports/2026-10-30-3gm-fidelity-check.md
FlattenAll (lines 288/290) submits a managed market exit on the close of the session's **last** bar, so its "next bar" is the next day's 09:31 (INFERRED). Three settings compete:
```

**Corrected :395 (fill sentence):** "The fill is unknown: the market exit's 'next bar' is the next day's 09:31 (INFERRED; this rests on NT8 filling a managed market order at the bar after the one it is submitted on, which is NT8 runtime behaviour, and on the REPORTED premise at :690 that the 16:00 bar is followed directly by the next day's 09:31). ExitOnSessionClose(30 s) and Day TIF compete (D2c)."

### 7. :752 and :762 "market orders" (MINOR; S9/R3)
```text
$ sed -n '752p;762p' docs/reports/2026-10-30-3gm-fidelity-check.md
- **Exit evaluation:** "trailing stops" are clock-sampled conditions that send market orders, not resting stop orders. This is consistent with spec L38.
- Every strategy-originated order is a market order, so if the Analyzer slips market fills (INFERRED; Amear's framing, no on-disk observation), every fill in run 3 is slipped.
$ /usr/bin/grep -nE "Enter(Long|Short)|Exit(Long|Short)|Set(StopLoss|ProfitTarget|TrailStop)|Submit" ninjascript/PraxisNoiseAreaBreakout.cs | /usr/bin/grep -v "^22[45]:"
211:					ExitLong("XL", "");
219:					ExitShort("XS", "");
227:				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
229:				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
288:				ExitLong("FlatEOD", "");
290:				ExitShort("FlatEOD", "");
$ sed -n '196,198p;210,211p' ninjascript/PraxisNoiseAreaBreakout.cs
			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
			if (!isCheckpoint || !haveBand)
				return;
				if (price <= stop)
					ExitLong("XL", "");
```

**Corrected :752:** "'Trailing stops' are conditions evaluated only at checkpoint bars (lines 196–198). When one triggers, the code calls `ExitLong("XL", "")` / `ExitShort("XS", "")` (lines 211, 219) and places no resting stop order (no `Set*` or `Submit*` call). All of this is OBSERVED. That NT8 realises these calls as market orders is INFERRED (NT8 runtime behaviour). This is consistent with spec L38."

**Corrected :762:** "Every strategy-originated order call is a managed `Enter*`/`Exit*` call with no price argument (6 call sites, OBSERVED). That NT8 submits each as a market order is INFERRED (NT8 runtime behaviour). So if the Analyzer slips market fills (INFERRED; Amear's framing, no on-disk observation), every strategy-originated fill in run 3 is slipped (INFERRED)."

### 8. :585 and :733 early-close days (MINOR; S9/R3)
```text
$ sed -n '585p;733p' docs/reports/2026-10-30-3gm-fidelity-check.md
**Verdict: CANNOT-DETERMINE-STATICALLY.** "Coincide on strict RTH" is the author's assumption, not an observation. On early-close days FlattenAll never runs.
**Early-close days.** No bar reaches `mod >= 960`, so FlattenAll never runs. If the early close falls on a :00 or :30 stamp, the last bar is also a checkpoint, so an entry can be placed whose next bar is the next session.
$ sed -n '842p' docs/reports/2026-10-30-3gm-fidelity-check.md | cut -c1-120
- **Early-close days.** The 16:00 cut-off is hard-coded (lines 58, 189, 196), so on a session that ends early the code n
$ sed -n '58p;189,192p' ninjascript/PraxisNoiseAreaBreakout.cs
		private const int CloseMod = 16 * 60;       // 960
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close
```

**Corrected :585 (last sentence) and :733 (first sentence):** "The flatten branch fires only on a bar with `mod >= 960` (lines 58, 189–192, OBSERVED). If the trading-hours template ends an early-close session before 16:00, no such bar exists and FlattenAll never runs. That condition depends on the template's early-close rows (INFERRED, as at :842)." The rest of :733 (an entry on a :00/:30 last bar) holds only under the same INFERRED condition.

### 9. :709 what the paper means (MINOR; spec, not paper)
```text
$ sed -n '709p' docs/reports/2026-10-30-3gm-fidelity-check.md
- **Stamp price?** The price used is `Close[0]` (line 200), the last trade in 09:59–10:00, which is the 10:00:00 price the paper's `Close_HH:MM` means. The paper's own bar convention is not stated in the spec.
$ sed -n '200p' ninjascript/PraxisNoiseAreaBreakout.cs | cut -c1-60
			double price = Close[0];             // the checkpoint st
```

**Corrected :709:** "The price used is `Close[0]` (line 200, OBSERVED). Under the REPORTED end-stamp premise (:690), it is the last trade in 09:59–10:00. Whether that is the price the paper's `Close_HH:MM` denotes is SPEC-SILENT: the spec does not state the paper's bar convention, and the paper was not read."

### 10. Agent-memory write outside `docs/reports/` (MINOR; unit writes)

Disclosure: in the prior pass, the manager wrote `.claude/agent-memory/praxis-manager/project_adversary_on_manager_report.md` (new, born 2026-10-30 18:08:13) and added an index line to `.claude/agent-memory/praxis-manager/MEMORY.md` (modified 18:08:13; the line is in the `grep` below). The report did not say so. The path is gitignored, so `git status` cannot show it. It has not been deleted.
```text
$ ls -laT .claude/agent-memory/praxis-manager/
total 232
drwxr-xr-x@ 28 admin  staff   896 Oct 30 18:08:13 2026 .
drwxr-xr-x@  6 admin  staff   192 Jul 26 10:18:39 2026 ..
-rw-r--r--@  1 admin  staff  5922 Oct 30 18:08:13 2026 MEMORY.md
-rw-r--r--@  1 admin  staff  2224 Aug  9 11:28:17 2026 feedback_cap_means_compression.md
-rw-r--r--@  1 admin  staff  2156 Jul 26 19:20:31 2026 feedback_verdict_token_required.md
-rw-r--r--@  1 admin  staff  1730 Aug  7 12:30:41 2026 feedback_verify_all_branches.md
-rw-r--r--@  1 admin  staff  2067 Jul 27 16:29:54 2026 feedback_workers_write_to_agent_memory.md
-rw-r--r--@  1 admin  staff  2259 Jul 26 15:15:30 2026 project_8sw_park_gate_boundary.md
-rw-r--r--@  1 admin  staff  1417 Oct 30 18:08:13 2026 project_adversary_on_manager_report.md
-rw-r--r--@  1 admin  staff  6703 Jul 26 19:18:13 2026 project_agent_type_mechanism.md
-rw-r--r--@  1 admin  staff  1693 Oct 20 14:51:56 2026 project_byte_cap_and_zsh_cleanup.md
-rw-r--r--@  1 admin  staff  2259 Aug  4 14:41:00 2026 project_citation_vs_pasted_evidence.md
-rw-r--r--@  1 admin  staff  7286 Aug  3 17:09:05 2026 project_commit_guard_bypass.md
-rw-r--r--@  1 admin  staff  1951 Jul 26 18:21:13 2026 project_false_null_hazard.md
-rw-r--r--@  1 admin  staff  1484 Oct 20 12:32:09 2026 project_grep_wrapper_skips_ignored.md
-rw-r--r--@  1 admin  staff  1446 Aug  7 12:30:31 2026 project_guard_merge_base_false_positive.md
-rw-r--r--@  1 admin  staff  1621 Oct 28 17:07:50 2026 project_heredoc_commit_text_denied.md
-rw-r--r--@  1 admin  staff  3638 Oct 20 10:28:21 2026 project_manager_report_contract_gate.md
-rw-r--r--@  1 admin  staff  1763 Jul 26 14:20:23 2026 project_master_write_guard_routing.md
-rw-r--r--@  1 admin  staff  2133 Jul 26 16:38:09 2026 project_park_commit_paste_hazard.md
-rw-r--r--@  1 admin  staff  1284 Oct 28 17:28:15 2026 project_plan_rule_vs_code_fact.md
-rw-r--r--@  1 admin  staff  1834 Jul 26 14:20:13 2026 project_s13_task_vs_agent.md
-rw-r--r--@  1 admin  staff  1561 Aug  9 12:09:23 2026 project_self_matching_evidence.md
-rw-r--r--@  1 admin  staff  1409 Oct 28 17:25:59 2026 project_stop_gate_newest_file_race.md
-rw-r--r--@  1 admin  staff  1579 Aug  7 10:04:58 2026 project_surgical_staging_manifest.md
-rw-r--r--@  1 admin  staff  2566 Aug  3 17:12:30 2026 project_transcript_recovery.md
-rw-r--r--@  1 admin  staff  1828 Aug  9 13:16:33 2026 project_untracked_containment_proof.md
-rw-r--r--@  1 admin  staff  1794 Oct 20 13:22:49 2026 project_worker_turn_cap_and_cr.md
$ stat -f "%N birth=%SB mod=%Sm" -t "%Y-%m-%d %H:%M:%S" .claude/agent-memory/praxis-manager/project_adversary_on_manager_report.md .claude/agent-memory/praxis-manager/MEMORY.md
.claude/agent-memory/praxis-manager/project_adversary_on_manager_report.md birth=2026-10-30 18:08:13 mod=2026-10-30 18:08:13
.claude/agent-memory/praxis-manager/MEMORY.md birth=2026-10-28 17:28:17 mod=2026-10-30 18:08:13
$ /usr/bin/grep -n "adversary_on_manager_report" .claude/agent-memory/praxis-manager/MEMORY.md | cut -c1-120
29:- [Adversary on manager report](project_adversary_on_manager_report.md) — attack my own synthesis before return; st
$ git check-ignore -v .claude/agent-memory/praxis-manager/MEMORY.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/MEMORY.md
```

This pass wrote no agent memory. The re-check after the last write is under the byte-unchanged proof.

### 11. Untracked premise and citation sources (MINOR; citation)

Acknowledged. All three are pre-existing inputs, not this unit's files. They exist on disk but git does not track them:
```text
$ git ls-files --error-unmatch docs/reports/2026-10-28-voice-session-notes.md; print -r -- "exit=$?"
error: pathspec 'docs/reports/2026-10-28-voice-session-notes.md' did not match any file(s) known to git
Did you forget to 'git add'?
exit=1
$ git ls-files --error-unmatch docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md; print -r -- "exit=$?"
error: pathspec 'docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md' did not match any file(s) known to git
Did you forget to 'git add'?
exit=1
$ git ls-files --error-unmatch docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md; print -r -- "exit=$?"
error: pathspec 'docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md' did not match any file(s) known to git
Did you forget to 'git add'?
exit=1
$ ls -la docs/reports/2026-10-28-voice-session-notes.md docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md
-rw-r--r--@ 1 admin  staff  13475 Aug 29 10:06 docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
-rw-r--r--@ 1 admin  staff  11215 Aug 29 07:30 docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md
-rw-r--r--  1 admin  staff   8268 Oct 30 18:20 docs/reports/2026-10-28-voice-session-notes.md
```

The voice notes' mtime in the listing above is Oct 30 18:20, later than the agent-memory write in item 10 (18:08:13). This pass did not check what changed in them after the body cited them. Line :33 still reads as the body quotes it (pasted under item 1).

### Byte-unchanged proof

Captured after items 1–11 were appended. Appending cannot change the first 72,931 bytes, so the head hash also holds for the final file. Baseline at the start of this pass: `wc -c` = 72931, `shasum -a 256` = `33ec1b1eec40a98f2f0d6c9c79df7a3d42a7bd8e4a3ff3c1aa15341c420f4dd0`. The head slice ends on the body's last line. The code hash matches the unit's reference. The worker reports and `ninjascript/` show no unstaged edits. No agent-memory file is newer than the 18:08:13 write disclosed in item 10.
```text
$ head -c 72931 docs/reports/2026-10-30-3gm-fidelity-check.md | shasum -a 256
33ec1b1eec40a98f2f0d6c9c79df7a3d42a7bd8e4a3ff3c1aa15341c420f4dd0  -
$ head -c 72931 docs/reports/2026-10-30-3gm-fidelity-check.md | tail -c 13
Result: PASS
$ wc -c docs/reports/2026-10-30-3gm-fidelity-check.md
   95877 docs/reports/2026-10-30-3gm-fidelity-check.md
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
$ git status --short -- ninjascript/ docs/reports/2026-10-30-3gm-worker1-checklist.md docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md docs/reports/2026-10-30-3gm-worker4-adversarial-d2d4.md docs/reports/2026-10-30-3gm-worker6-adversarial-manager.md
A  docs/reports/2026-10-30-3gm-worker1-checklist.md
A  docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md
A  docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md
A  docs/reports/2026-10-30-3gm-worker4-adversarial-d2d4.md
A  docs/reports/2026-10-30-3gm-worker6-adversarial-manager.md
$ git diff --quiet -- docs/reports/2026-10-30-3gm-worker1-checklist.md docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md docs/reports/2026-10-30-3gm-worker4-adversarial-d2d4.md docs/reports/2026-10-30-3gm-worker6-adversarial-manager.md ninjascript/; print -r -- "unstaged-diff exit=$?"
unstaged-diff exit=0
$ ls -laT .claude/agent-memory/praxis-manager/MEMORY.md .claude/agent-memory/praxis-manager/project_adversary_on_manager_report.md
-rw-r--r--@ 1 admin  staff  5922 Oct 30 18:08:13 2026 .claude/agent-memory/praxis-manager/MEMORY.md
-rw-r--r--@ 1 admin  staff  1417 Oct 30 18:08:13 2026 .claude/agent-memory/praxis-manager/project_adversary_on_manager_report.md
$ find .claude/agent-memory/praxis-manager -newer .claude/agent-memory/praxis-manager/MEMORY.md | wc -l
       0
```

### Self-grade

This grades only the eleven audit-1 items. The auditor's grade governs.

| # | What was done | Where |
|---|---|---|
| 1 | Split into code level (OBSERVED: null arm 0, control 6, widened arm with no code hits) and runtime (INFERRED, premise stated, R3 toggle readback named). :776 and D4 #9 restated. Run-3 template cited: OBSERVED-in-image for run 3, UNKNOWN for runs 1–2 | item 1 |
| 2 | Real commands with full paths; 1/36 and 0/45 | item 2 |
| 3 | `awk` count of the verdict column: 15/1/2/6/5 = 29 | item 3 |
| 4 | Source inline, invocation and output; downgraded to illustration | item 4 |
| 5–9 | Each line pasted; each corrected sentence labelled | items 5–9 |
| 10 | Memory write disclosed; `ls -laT` pasted; nothing deleted | item 10 |
| 11 | Three `--error-unmatch` failures pasted | item 11 |

Residual limits: item 1(b) remains INFERRED until Amear runs the toggle readback. The item-2 originals and `fuzz.py` live in session scratch, not in the artifact. The fuzz source is pasted in full.

Result: PASS
