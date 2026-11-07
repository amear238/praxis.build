# Manager report — unit `2026-11-06-wf-values`

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Task

Propose exact walk-forward values under Amear's ruling 4, plus the arm (b) code design, for his confirmation. Deliverables: `docs/specs/2026-11-06-walk-forward-values.md` (new), entry D-2026-11-06-D appended to DECISIONS.md, two MANIFEST rows, this report. No code. Nothing staged.

## Authorisation (S5), quoted

- Ruling 4 (D-2026-11-06-B; DECISION_LOG `2026-11-06T20:08:28Z`, WHO: amear): "4. Walk-forward arm (b) and spec NEEDS AMEAR, under "We're not here to fuck around" — strictest reasonable defaults: small grid around the paper's published values (no wide search); ATR 14; exit policies BandOrVWAP / OppBand / Flat1559; in-sample objective = risk-adjusted return with a minimum trade count, never net profit; partial last window dropped; judged arm = (a) fixed rules; arm (b) counts only if it also passes PBO < 0.05. Report the exact values chosen back to me." Loop step d: "Arm (a) and (b) build per the spec, Mac side, ready to run through the bridge once 2a passes."
- Ruling 1 (DECISION_LOG `2026-11-05T23:50:09Z`, WHO: amear, line 549): "Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest. Minute data is sufficient for arm (b)."
- D-2026-11-06-A item 2 (DECISIONS.md:1003): "Direction: the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy."
- Dispatch, DECISION_LOG line 463, `[2026-11-06T23:01:17Z] WHO: praxis-master`, WHAT (excerpt): "DISPATCH DECISION — step d begins with the SPEC/FILING unit `2026-11-06-wf-values` (values + arm (b) design on disk BEFORE any code unit — the 22:25Z lesson)." … "(1) THIS unit writes `docs/specs/2026-11-06-walk-forward-values.md` (DERIVED; every value a PROPOSAL under ruling 4's delegated defaults, for Amear's confirmation …) and DECISIONS entry D-2026-11-06-D … (2) ONLY THEN the code unit on its own branch."

## Rubric criteria addressed (verbatim, `specs/SPEC_RUBRIC.md:107-108,114`)

- S1 | Every claim in a report has pasted command output, not a description of output.
- S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure.
- S8 | No question that belongs to Amear is answered on his behalf.

## Workers dispatched

| # | id | mode | outcome |
|---|---|---|---|
| A1 | a55d4187f909fd22c | ADVERSARIAL, read-only, spec + entry draft | BLOCKING FINDINGS (1) + 5 MINOR; all fixed |
| A2 | aa57c1dcd4de029be | ADVERSARIAL, fix check | BLOCKING FINDINGS (3) + minors; all fixed |
| A3 | a3d38484633aec85d | ADVERSARIAL, fix check | BLOCKING FINDINGS (1) + minors; fixed |
| A4 | adba2a8328a4dc8fd | ADVERSARIAL, fix check (tests only) | BLOCKING FINDINGS (2) + 3 MINOR; blocking 1–2 and minor 2 fixed after its pass, **not re-attacked** |

No BUILD worker. The manager wrote the spec, the entry and the rows himself (pure doc edits). **Deviation from the brief:** the brief asked for ONE adversarial worker. Four were run because each pass found blocking defects. All four returns are pasted in full below.

## Process log

1. Read rubric, rulings, WF spec (224 lines), strategy and both variant files, bridge code read, cost model.
2. Computed sessions and windows from the data file (scratchpad awk).
3. Wrote the spec; drafted the entry in the scratchpad.
4. A1 → fixes: T5 added; CS0101 graded INFERRED; question 10 remapped; CSCV ranking, ties and no-eligible case; tie-break direction; ATR warm-up; report path named.
5. A2 → fixes: stop multiplier renamed m (k is the noise multiplier); T5 rewritten (all inputs in every run, readback print, T5e); items 3/5/6 reclassified; trade-list limits and the net-of-commission UNVERIFIED added; quantity source; question 1 widened.
6. Entry inserted ONCE at DECISIONS.md:1191 (cmp against the draft rc=0); MANIFEST rows appended.
7. A3 → T6 (static wiring check and band oracle) and T7 (Contracts, tab readback); minors fixed. **The entry's acceptance paragraph was edited in place after insertion** (lines 1191+ only; this unit's own uncommitted text; lines 1–1190 hash unchanged, below).
8. A4 → T6(i) reworded (code lines only; excludes comments, Description, SetDefaults); oracle extended to the stop level at every entry, and two runs (T6c, T6d) added that use the stop under Flat1559 and OppBand at k ≠ 1.0; entry sentence corrected. Budget then ran out, so this fix has had no adversary pass.

## Verification evidence (pasted output)

Paper's values, and the committed constants:
```
$ /usr/bin/grep -n -i "lookback window:\|NO free multiplier\|not used\*\* — there is no ATR" docs/specs/2026-07-16-b2-noise-area-ruleset.md | cut -c1-160
31:- **Lookback window:** **14 trading days**, fixed (`i = [1,14]`). No lookback grid is tested in the paper.
32:- **Noise "multiplier":** there is **NO free multiplier** in the paper — the half-width is exactly `1 × σ` (the raw 14-day average absolute move). A tuna
50:| Stop-ATR | **not used** — there is no ATR-based stop anywhere in the paper | — |
$ sed -n '74p;76p;118p' ninjascript/PraxisNoiseAreaBreakout.cs
		private const int Lookback = 14;
		private const double BandSigmaMult = 1.0;
				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec §4 p.13 — paper's PREFERRED exit. The only knob.
```

Baseline and file state:
```
$ git rev-parse --short HEAD
e9f668c
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs docs/specs/2026-11-05-walk-forward-spec.md
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
b4341724134b0af1c2b268c7c38952f7f75cc801d84c72c61aad5ec0020d8645  docs/specs/2026-11-05-walk-forward-spec.md
$ git status --short ninjascript/; echo rc=$?
rc=0
```

Windows. The scratchpad script is `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wf/sessions.awk`; it counts Mon–Fri dates in 20210308..20260717 that have a bar at 093100..160000. The data file's sha256 is `307c5e8a…e454`. Weekday control first:
```
$ date -j -f %Y%m%d 20210308 +%a; date -j -f %Y%m%d 20260717 +%a
Mon
Fri
$ LC_ALL=C awk -f .../scratchpad/wf/sessions.awk ~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt
N=1352 first=20210308 last=20260717
K=17 remainder=29 dropped=29 oos_total=1071
W01 IS 20210308..20220316 (s1-s252) OOS 20220317..20220615 (s253-s315)
W02 IS 20210604..20220615 (s64-s315) OOS 20220616..20220913 (s316-s378)
W03 IS 20210902..20220913 (s127-s378) OOS 20220914..20221209 (s379-s441)
W04 IS 20211216..20221209 (s190-s441) OOS 20221212..20230310 (s442-s504)
W05 IS 20220317..20230310 (s253-s504) OOS 20230313..20230608 (s505-s567)
W06 IS 20220616..20230608 (s316-s567) OOS 20230609..20230905 (s568-s630)
W07 IS 20220914..20230905 (s379-s630) OOS 20230906..20231201 (s631-s693)
W08 IS 20221212..20231201 (s442-s693) OOS 20231204..20240301 (s694-s756)
W09 IS 20230313..20240301 (s505-s756) OOS 20240304..20240530 (s757-s819)
W10 IS 20230609..20240530 (s568-s819) OOS 20240531..20240827 (s820-s882)
W11 IS 20230906..20240827 (s631-s882) OOS 20240828..20241122 (s883-s945)
W12 IS 20231204..20241122 (s694-s945) OOS 20241125..20250225 (s946-s1008)
W13 IS 20240304..20250225 (s757-s1008) OOS 20250226..20250527 (s1009-s1071)
W14 IS 20240531..20250527 (s820-s1071) OOS 20250528..20250822 (s1072-s1134)
W15 IS 20240828..20250822 (s883-s1134) OOS 20250825..20251120 (s1135-s1197)
W16 IS 20241125..20251120 (s946-s1197) OOS 20251121..20260309 (s1198-s1260)
W17 IS 20250226..20260309 (s1009-s1260) OOS 20260310..20260605 (s1261-s1323)
DROPPED s1324-s1352 20260608..20260717
CSCV rows s12-s1323 = 1312 = 16 x 82
$ awk 'BEGIN{printf "%.1f %.1f %d\n",1190/1352*252,810/1352*252,3^4}'
221.8 151.0 81
```
(`...` here stands for the scratchpad path named above it.) A1 recomputed the same figures independently with its own script (its return is below).

DECISIONS.md lines 1–1190, before and after (the after hash was taken after every edit, the last one included):
```
before: 0ba9af57078bd0ce6b41589e5781c427c73bafa4749fcb6a79804989b008339f  -
after:  0ba9af57078bd0ce6b41589e5781c427c73bafa4749fcb6a79804989b008339f  -
$ wc -l < DECISIONS.md
    1232
$ /usr/bin/grep -n '^## 2026-11-06 — D-2026-11-06-D' DECISIONS.md
1192:## 2026-11-06 — D-2026-11-06-D: walk-forward values proposed under ruling 4 and arm (b) code design (PROPOSAL — awaiting Amear's confirmation)
$ tail -n +1191 DECISIONS.md | cmp - "$S"; echo rc=$?     # at insertion, before step 7's edits
rc=0
```

MANIFEST: the prefix is unchanged and two rows were appended:
```
daf1caabcf78cbba96abf04af0c02ee568c752850e74ffa8f231fec453c6f2a6  -   (head -n 253 MANIFEST.md, before)
daf1caabcf78cbba96abf04af0c02ee568c752850e74ffa8f231fec453c6f2a6  -   (git show HEAD:MANIFEST.md)
     255
daf1caabcf78cbba96abf04af0c02ee568c752850e74ffa8f231fec453c6f2a6  -   (head -n 253 MANIFEST.md, after)
 1 file changed, 2 insertions(+)
```

Limitation-sentence count, after the edits:
```
$ /usr/bin/grep -c "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed." docs/specs/2026-11-06-walk-forward-values.md
1
$ sed -n 1191,1232p DECISIONS.md | /usr/bin/grep -c "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."
1
```
Spec at the time of writing: sha256 `da17a675054318877b9b80b86a450ce899ff4e2b38a91b7f5594e2f2e8cccda3`, 142 lines.

## Adversarial findings — full returns

### A1 (a55d4187f909fd22c)
```text
I found one blocking problem, in the acceptance tests in §9. Everything else checks out apart from five minor issues. Full report: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wf-adv/report.md`. My session-count script: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wf-adv/count.py`.

**What holds (checked this session)**
- **Hashes:** `PraxisNoiseAreaBreakout.cs` = `35393823e9bc…2265` (last revision `719ab11`); the WF spec = `b4341724134b…8645`. Both match the artifacts.
- **Citations:** every file:line citation in the brief says what it is claimed to say.
- **Quotes:** ruling 4, ruling 1, the "Direction:" sentence and D-2026-11-05-A items 1–2 are verbatim.
- **Window arithmetic:** my own script, after the weekday control (`date -j` gives 20210308 = Mon, 20260717 = Fri, 20260606 = Sat; Python weekday gives `0 4 5`), prints:
    N 1352 s1 20210308 sN 20260717 ... 141 ; K 17 OOS 1071 used 1323 dropped 29
    dropped first/last 20260608 20260717 29
    win 1 IS 20210308 20220316 OOS 20220317 20220615
    win 17 IS 20250226 20260309 OOS 20260310 20260605
    span s12..s1323 1312 82.0 ; C(16,8) 12870 ; 221.8 ; 150.98 ; 3^4 81
- **Variant files:** with comments stripped, the OppBand and Flat1559 files differ from the base only at the cited lines (enum, name, default, the two stop lines, `FlattenMod`). So the T2/T3 equivalence design is sound.
- **Ruling 4:** every value fits its words. The grid is 81 points, ATR is 14, the three exit policies are exactly the named ones, net profit is used nowhere in selection or tie-break, the partial window is dropped, the judged arm is (a), and PBO < 0.05 is strict. Ruling 1 is followed: the stop is checked on bar close, exits by market order on the next bar, and places no resting order.
- **S8:** no question is answered for Amear. O1, the MFFU tier, the branch name, the OppBand/Flat1559 definitions and the bridge-versus-Python reading are all labelled PROPOSED and asked.
- **Spec vs draft entry:** no value differs between them.
- **S13:** the limitation sentence appears exactly once in each artifact.
- **De-identification:** both artifacts comply.

**Findings**
- **B1 BLOCKING (attack e; S9/S2): the acceptance tests cannot catch dead Lookback or NoiseMult inputs.** T1–T4 never set either to a non-default value. T1 runs entirely at the defaults; T2/T3 change only the exit policy; T4 changes only the stop multiplier. No test requires the values to arrive through the bridge's `params`. A code unit where Lookback stays hard-coded at 14, or where injection silently fails, passes all four tests. Then 54 of the 81 grid columns are duplicates, and both the window selection and PBO are corrupted. Evidence, spec lines 117–120: "T1: ArmB at (14, 1.0, Off, BandOrVWAP)… T2… (14, 1.0, Off, OppBand)… T3… (14, 1.0, Off, Flat1559)… T4 (stop trips): at StopAtrMult 0.5".
- **M1 MINOR (S1/S2): the "unit report" doesn't exist.** The measurements are graded "OBSERVED, unit report", but no 2026-11-06 wf-values report is in `docs/reports` (`ls` lists only the bridge/gate/handoff reports). The numbers are correct; their cited source is missing.
- **M2 MINOR (S2): an INFERRED claim is stated as fact.** §9 says a second enum declaration "does not compile (CS0101, as both variant headers state)". Both headers actually say "(INFERRED, not compiled)" (`_OppBand.cs:39,72`, `_Flat1559.cs:47,80`).
- **M3 MINOR: question 10 classifies WF items 9, 10 and 25 wrongly.** It lists them as untouched by ruling 4. But "judged arm = (a)" directly answers D-2026-11-05-A NEEDS AMEAR 4 ("Is R-1104-3's judged version arm (a), arm (b) or both?" — the same question as WF item 10). The new spec's own §2 cites it as RULED. This errs toward leaving things open, so it isn't an S8 breach, but the classification is wrong.
- **M4 MINOR: "the oldest 11 warm-up sessions" is a misleading label.** Dropping 11 rows is a trim to make 1,312 = 16 × 82. Lookback-18 configurations still have no trades in s12–s18, and lookback-10 configurations can trade on s11.
- **M5 MINOR: some "exact values" aren't exact.** Unspecified:
  - which way PBO ranks run, and how ties are handled;
  - what happens when no configuration is eligible in a CSCV training half;
  - how a stop-on configuration behaves before ATR(14) has its 15 sessions (it can trade from s11 with lookback 10);
  - which direction the lexicographic tie-break runs.
- **Notes:**
  - The draft entry's "(all PROPOSED)" table includes items that are already RULED. This is an underclaim.
  - The `[Range]` limits on the §9 inputs are wider than the grid. That is input validation, not a search.
  - The whole §7/§9 run plan rests on the question 7 reading of the Direction sentence. It is labelled PROPOSED and asked.
  - T4 doesn't say which exit policy it uses.

VERDICT: BLOCKING FINDINGS (1)
```
Manager's disposition of A1's M3: item 10 is now "partly covered". Item 25 stays open, because ruling 4 does not say whether this walk-forward is the judged go/no-go version.

### A2 (aa57c1dcd4de029be)
```text
# Adversarial pass 2 on unit `2026-11-06-wf-values`: 3 blocking findings

Conditions 1, 4 and 9 fail. The other six hold, two of them with minor findings.

## Per condition

**C1 — FAILS (B1, B2).**

**B1 (BLOCKING): T5 does not catch a hard-coded `NoiseMult`.**
- **The faulty build:** the `NoiseMult` property exists, but the code still uses the constant `BandSigmaMult` (1.0).
- **Why it passes:** each T5 run sends only the key it changes. `InjectParams` writes onto the tab's own template object, which stays set between runs, so the second run `{"NoiseMult":1.2}` still runs with Lookback 18. Its trade list differs from T1's, so check (ii) passes.
- **Check (i) cannot catch it either:** the `backtest` response is `{id, status, strategy, metrics, trades}`, with no parameter readback (bridge report `:65`).
- **Same path for bridge failures:** a bridge that fails to set 1.2 also passes. Conversion errors are swallowed with a log line only (`InjectParams`, `NT8BridgeServer.cs:2678-2691` as quoted in the report).
- That the template keeps values between runs is INFERRED from the quoted code; I did not run it.

**B2 (BLOCKING, also C9): `k` means two things.**
- §3 and §6 define k as the noise multiplier. §4 sets the stop at "entry fill price − k × ATR(14)", and the entry says "± k × ATR(14)".
- A literal build therefore uses `NoiseMult` for the stop distance, and `StopAtrMult` only switches the stop on or off.
- That build passes T1–T5, because T4 and T5 only ever use 0.5. The 0.5 and 1.0 grid points would give identical results.

**C2 — HOLDS (M1, minor).** §2 line 31 grades the sha256 "(OBSERVED)" but names no report; the path first appears at §5 line 69. The hash itself matches:
    35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
    b4341724…8645  docs/specs/2026-11-05-walk-forward-spec.md

**C3 — HOLDS (M3, minor).** The CS0101 sentence matches how both variant files grade it:
    _OppBand.cs:39,72 / _Flat1559.cs:47,80: "…would be CS0101 (INFERRED, not compiled)."
M3: §7 has the Mac side compute daily P&L "after commission and slippage" from the bridge's trade lists. Whether the bridge's P&L is net of commission is UNVERIFIED (bridge report `:68`), and the spec doesn't mark it.

**C4 — FAILS (B3).**
- All 29 numbers appear exactly once: 7 covered + 2 partly + 7 proposed + 13 not touched. "Judged arm = (a)" is credited at items 9 and 10.
- **B3 (BLOCKING):** items 5 and 6 are listed as "Covered by ruling 4", but ruling 4 only partly answers them.
  - Item 5 asks for the ATR period and its bar series. Ruling 4 gives only "ATR 14"; the series is proposed (§4) and asked (question 6).
  - Item 6 asks for the objective and the tie-break. Ruling 4 gives neither the statistic nor the tie-break.
  - Both belong under "Partly covered", the same standard the spec uses for 9 and 10. Item 3 is weaker still: the paper has no stop value, so "around the paper's published values" gives no candidate set.

**C5 — HOLDS.** Rank direction, average-rank ties, ω = rank/(81+1), λ, the no-eligible case, the s12–s1323 trim and its effect on s11, the §6 tie-break direction and the §4 warm-up are all specified. Arithmetic checked:
    K 17 oos 1071 last 1323 dropped 29 / span 1323 trim 11 rows 1312 82.0 / 12870 / 221.80 150.98 260.32
- Note: Sharpe is undefined when the standard deviation is zero.
- Note: the spec doesn't say whether the minimum trade count applies to the test-side ranking.

**C6 — HOLDS.** Every listed value agrees between the spec and the entry. The entry repeats B2's k wording.

**C7 — HOLDS (M2, minor).** Question 1's list leaves out the §9 branch, file, class, enum and inputs, the §2 arm (a) windows, and the §5 warm-up and in-sample → out-of-sample rule. Question 10 still sends WF items 14, 17, 23 and 28 to "question 1". The opening clause "every PROPOSED value" does cover them.

**C8 — HOLDS (compliance only).** The limitation sentence appears exactly once in each artifact (`grep -c` = 1 and 1). Neither artifact mentions or hints at breaker #5's source.

**C9 — FAILS (B2).** Every cited line resolves to the quoted text, and all tables are well-formed. No value falls outside ruling 4's words.

## Notes
- **T1 compares "quantity":** the bridge's trade list has no quantity field (bridge report `:66`), so T1 has to be checked from NT8's own trade list.
- **Trade-list cap:** the bridge caps the list at 5,000 trades. The spec doesn't address this for the 81 full-span runs.
- **WF item 22:** ruling 2's MNQ $1.90 partly answers it. Listing 22 as "not touched by ruling 4" is literally true.
- **Entry grading:** measured facts (N, K, the 29 dropped sessions) sit under "PROPOSED unless marked RULED", which grades them lower than they are.

Report: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wf-adv2/adversarial-report.md`

VERDICT: BLOCKING FINDINGS (3)
```

### A3 (a3d38484633aec85d)
```text
I found one blocking break, in C1: a half-wired input passes every test from T1 to T5. C2, C3, C6 and C7 hold. C4, C5 and C8 have minor findings only. I made no edits, and the only file I wrote is the report in the scratchpad.

**Prefix checks:** `head -n 1190 DECISIONS.md | shasum -a 256` prints `0ba9af57…339f`, which matches. MANIFEST lines 1–253 are the same as `git show HEAD:MANIFEST.md` (diff empty; HEAD has 253 lines).

**C1 — FAILS (BLOCKING).**
- **(a) and (b):** if the input is used nowhere, T5a or T5b catches it, because the run equals T1. But T5(ii) only checks that the trade list "differs", not that the band uses the value. Two faulty builds pass all five tests:
  - **(b):** `NoiseMult` is used at `PraxisNoiseAreaBreakout.cs:263` only, and `:264` keeps `BandSigmaMult`. T1–T4 run at k=1.0, so they pass. T5b at 1.2 differs from T1, since only the upper band moves. The strategy's printout (readback) shows 1.2. The lower band still uses 1.0.
  - **(a):** the gate at `:257` uses the `Lookback` property, but the averaging loop at `:247` keeps a literal 14. At 18 the count never reaches 18, so T5a has zero trades. Zero trades still "differs" from T1, so it passes. The band still uses 14.
- **(c):** caught by T5c ≠ T4. Both run at k=1.0, so the faulty stop is 1.0×ATR in both and the two runs come out the same.
- **(d):** caught by T5c ≠ T4.
- **(e):** caught by T5(i), the printout at `State.DataLoaded` compared with the values sent (the bridge has no readback, `:65`). One gap (MINOR): `Contracts` is 1 in every run, which is also its default, so a failed set of `Contracts` is never seen.
- **(f):** caught for the five inputs by T5e = T1 together with the printout. Gap (MINOR): settings held on the tab itself are not tested. The tests run at $2.96 commission and the walk-forward runs need $4.68, and the backtest type also stays on the tab (bridge `:64`). Nothing checks that either is reset.

**C2 — HOLDS.** The stop multiplier is m and the noise multiplier is k throughout; the entry uses only m = `StopAtrMult`. NOTE: the spec also uses k for the window index (`:68`, `:71`), and S for both the Sharpe value (`:75`) and the number of PBO blocks (`:87`).

**C3 — HOLDS.** All 29 items appear exactly once. Only item 16 is listed as fully answered, which matches ruling 4. Items 3, 5 and 6 are listed as "defaults ruled, values proposed". Both artifacts' quotes of ruling 4 appear word for word in DECISIONS.md lines 1–1190 (python check returned True).

**C4 — MINOR.** The spec contradicts itself on how many inputs are sent: `:90` says "all four inputs", `:125` says "all five inputs", and the `:118` example has four keys. The entry just says "all inputs". All other values agree.

**C5 — MINOR.** Bridge report `:69` is a blank line; the "net of commission UNVERIFIED" sentence is at `:68`. Every other citation resolves: results report `:73` and `:402-405`; bridge report `:28`, `:65`, `:66`, `:72`, `:83`, `:113`; the code lines in §3 and §9; ruleset lines; fidelity check `:85`; `DECISIONS.md:501-505`; cost model `:19` (4.68, v1.2.0).

**C6 — HOLDS.** The limitation sentence appears once in the spec and once in lines 1191–1232. Nothing mentions or hints at breaker #5's source.

**C7 — HOLDS.** O1, the MFFU tier, value confirmation, branch, OppBand/Flat1559 meanings and the NT8-vs-Mac reading are each marked PROPOSED and asked (questions 1, 4, 5, 7, 8, 9). Nothing is claimed as implemented or tested; the spec says WRITTEN at most before 2a.

**C8 — MINOR.**
- `docs/reports/2026-11-06-wf-values-manager.md` does not exist. The spec cites it as the evidence for its OBSERVED values, and MANIFEST row 255 registers it.
- I re-ran those values myself and they all match: sha256 `35393823…2265`, N=1352, 17 windows, 29 sessions dropped from 2026-06-08, the window 1 and window 17 dates, and s12=2021-03-23 / s1323=2026-06-05.
- No broken tables (spec rows 5 pipes, entry rows 3) and no duplicated or cut-off lines.

Report: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wf-adv3/report.md`

VERDICT: BLOCKING FINDINGS (1)
```

### A4 (adba2a8328a4dc8fd)
```text
I found 2 blocking findings. All ten faulty builds you listed are caught as described, but variants of (c), (i) and (j) pass every test, and one check fails on a build that is correct. The hash matches: `head -n 1190 DECISIONS.md | shasum -a 256` gives `0ba9af57078bd0ce6b41589e5781c427c73bafa4749fcb6a79804989b008339f`. I also opened every cited line and each one says what the spec claims: base `:74 :76 :79 :247 :257 :263 :264 :300 :305`, results `:73` and `:402-404`, bridge `:65 :66 :68`.

**Per build**
- **(a) literal 14 at :247:** caught by T6(i), through the "only literal `14` is `AtrPeriod`" rule and the line-by-line diff, and by T6(ii)'s band oracle at T5a. T5a alone does not catch it: with Lookback 18 the build makes 0 trades, and that still "differs from T1". If the loop uses `AtrPeriod` instead of a literal, the grep passes and only the manual diff and T6(ii) catch it.
- **(b) NoiseMult on the upper band only:** caught by T6(ii) (LowerBound at T5b against the oracle) and by the T6(i) diff of `:264`. T5b passes, because the trades still differ.
- **(c) stop uses k instead of m:** caught. At T5c and T4 k is 1.0 in both, so T5c equals T4, which breaks "T5c differs from both T1 and T4". **A stop of m × k × ATR is not caught**, because no test sets k ≠ 1.0 with the stop on.
- **(d) StopAtrMult only switches the stop on or off:** caught by T5c ≠ T4.
- **(e) bridge silently fails to set a value:** caught by T5(i); the values printed at `State.DataLoaded` must equal those sent.
- **(f) value persists on the template:** caught by T5e = T1, and by T5(i).
- **(g) Contracts ignored:** caught by T7 (T5f must give exactly 2 × T1's net at twice the quantity).
- **(h) $2.96 left on for a walk-forward:** caught only by procedure: T7 reads the tab back "before every batch … walk-forward runs the $4.68 one". Nothing in the walk-forward output would show it, since the bridge's trades carry no commission.
- **(i) Flat1559 behaves as BandOrVWAP:** caught by T3 (expects $193,017.60; the faulty build gives $197,327.60). **Not caught if it only happens with the stop on.**
- **(j) resting stop order:** caught by T4 ("the order list holds no stop order", fill on the next bar). **Not caught if it only happens under OppBand or Flat1559.**

**BLOCKING**
1. **Nothing checks the stop level.** T4 checks timing and order type only. T5c versus T4 only shows that m = 0.5 and m = 1.0 give different results. T6(ii) prints ATR but not the level. These builds pass every test: m × k × ATR; a level taken from the signal close instead of the entry fill; a stop on σ or on a 14-minute ATR while the printout shows the session ATR. So the sentence "a stop that uses the noise multiplier … fails T5", in both the spec and the entry, is false for m × k.
2. **T6(i) fails on a correct build.** The §9 table sets Lookback's default to 14, so SetDefaults needs `Lookback = 14;`. That line breaks the "only literal `14` is `AtrPeriod`" rule, and so does the base Description string at `:101` ("14-day"). The `BandSigmaMult` grep has no comment filter, and the base comments at `:237` and `:295` name it.

**MINOR**
1. No test runs the stop with OppBand or Flat1559 (36 of the 81 grid points). §4's rules are untested too: the session flat taking precedence over the stop, no re-entry on the stop bar, and no entry until ATR exists.
2. The entry says "A dead or hard-coded input … fails T5". A dead Contracts input fails T7, not T5. A partly hard-coded value, as in (a) or (b), passes T5. The spec limits the sentence to Lookback and NoiseMult. This is the only place the entry and the spec disagree.
3. The "differs from T1" checks are weak: a build that makes 0 trades passes them, and T5c ≠ T1 is guaranteed by the ATR warm-up alone.

**NOTE**
1. The spec says `params` does "enum and number conversion", but bridge report `:113` says "enum and int". Setting doubles through `params` is not shown; T5(i) would catch a failure.
2. No number in the entry differs from the spec, and neither claims anything was implemented or run (S2 holds).

Report written to `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wf-adv4/report.md`

VERDICT: BLOCKING FINDINGS (2)
```
After A4, the manager made these changes. Blocking 1: the oracle now prints and recomputes the stop level at every entry (level = fill ∓ m × ATR). Two runs were added, T6c (18, 1.2, 1.0, Flat1559) and T6d (14, 0.8, 0.5, OppBand): they put the stop on with k ≠ 1.0 under the other two exit policies, and each must place no stop order. Blocking 2: T6(i) now checks code lines only, excluding comments, the Description string and the SetDefaults `Lookback = 14`. Minor 2: the entry sentence is corrected. **Still open:** minor 1's §4 rules (flat precedence, no re-entry on the stop bar, the ATR warm-up gate) and minor 3 (weak "differs" checks). No adversary has attacked these fixes. Note 1: the spec cites bridge `:72` ("generic enum/bool/number conversion") as well as `:113`; setting a double is still unproven and is left to T5(i).

## S6 cross-block check

- F1–F4: untouched. No code, hook, config or template was edited (`git status --short ninjascript/` is empty, rc=0, above). F3's fill and slippage terms are used as D-2026-10-30-A sets them.
- O1 and O4: OPEN. O1's gate set is asked as question 8; this unit makes no breaker claim.
- Cost model: read only. WF runs use $4.68 (D-2026-11-06-C, `config/backtest-cost-model.json:19`); the acceptance tests use the committed $2.96 so that the reference figures apply.
- Test 2a: no interaction. The acceptance tests run only after 2a passes.
- De-identification: neither artifact mentions breaker #5's source (A1–A4 report compliance).

## Files staged

None. The index was already populated before this unit, and the unit did not change it:
```
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
```
Working tree, this unit: `docs/specs/2026-11-06-walk-forward-values.md` (untracked, new); DECISIONS.md lines 1191–1232 (appended); MANIFEST.md lines 254–255 (appended); this report (untracked, new).

**Result: FAIL**

Why: the last adversary pass (A4) returned `VERDICT: BLOCKING FINDINGS (2)`. Both were fixed afterwards, but no adversary has re-attacked the fix, and A4's minors 1 and 3 are still open. The values themselves (grid, windows, objective, PBO), the S8 handling and the S13 count passed A1–A4. The failing part is the code-unit acceptance-test design in §9 and the entry's matching paragraph. Next step: one read-only adversary over spec §9 and DECISIONS.md:1191–1232. Then close minors 1 and 3 (add stop-rule tests: flat precedence, stop-bar re-entry, ATR warm-up gate; replace "differs from T1" with oracle-backed checks).

## Correction 1 (2026-11-06, after audit FAIL 1; appended, nothing above edited)

### Task

Fix audit FAIL 1 of unit `2026-11-06-wf-values`: BLOCKING 1 (S2) and MINORs 2–6, in the spec's §9, the entry D-2026-11-06-D (DECISIONS.md 1192–1232 only), MANIFEST.md row 254 and this report (append only). No code, no branch, nothing staged.

### Authorisation

DECISION_LOG.md row `[2026-11-06T23:40:00Z] WHO: praxis-master`. Its WHAT is quoted in full by the first command in the evidence block below (line 463). It names BLOCKING 1 (S2), "entry line "a partly wired input or a wrong stop level fails T6" unsupported", and MINORs 2–6. Its correction scope is: "spec §9 — add an oracle-backed stop-exit test …, tests for the three §4 rules (T8–T10 or listed as deferred WITH the gap stated in the spec), fix :125's T5 claim, restate what each test does and does not catch; entry D-2026-11-06-D's corresponding sentence fixed in place …; MANIFEST row 254 corrected; report Correction 1 …".

### Rubric criteria addressed (verbatim, `specs/SPEC_RUBRIC.md:107`, `:108`, `:114`)

| S1 | Every claim in a report has pasted command output, not a description of output. |
| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
| S8 | No question that belongs to Amear is answered on his behalf. |

### Workers dispatched

| id | mode | outcome |
|---|---|---|
| a78eed1e144a9ba16 | ADVERSARIAL, read-only, over spec §9 and DECISIONS.md 1192–1232 | `VERDICT: BLOCKING FINDINGS (2)`; both fixed (see dispositions) |

The edits are doc text, made by the manager with two scripts (`/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/edit.py`, then `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/edit2.py` after the adversary). Each script replaces exact strings that must occur exactly once, and it splits DECISIONS.md at line 1191 and rewrites only the tail. No production code was written.

### Process log

1. Before the edits I copied the spec, DECISIONS.md, MANIFEST.md and this report to `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/{spec,dec,man,rep}.before`. Their hashes, in the block below, equal the ones I captured before any edit: spec `da17a675…`, DECISIONS `709decd6…`, MANIFEST `35d1ccc2…`, `head -n 1191` `328b2c8d…`, report `head -n 327` `9f60254d…`.
2. `edit.py` made these changes. BLOCKING 1: it added T8 and wrote T9–T11 as tests (MINOR 3), not as deferred items. MINOR 2: it fixed the T5 sentence. It corrected the entry sentence and changed MANIFEST row 254 to T1-T11 (MINOR 4). It also made two consistency edits outside §9 (a deviation in letter, disclosed here): the WRITTEN line now names T8–T11, and NEEDS AMEAR question 1 now reads T1–T11 instead of T1–T7. If question 1 still said T1–T7, it would leave out the new tests.
3. After `edit.py` the spec's sha256 was `823487245615e623acf522946f5cdd163290ca511db234d4d5ed2249aaed673e`. The adversary attacked that state.
4. `edit2.py` fixed the adversary's two BLOCKING findings and minors M1–M5 (dispositions below). It also changed question 1 to cover T8's bar order, which is new PROPOSED text. **The text `edit2.py` changed was not re-attacked by an adversary.**

### Verification evidence

All commands were run from `/Volumes/Sensidine/Praxis.build` with `bash`, which echoes each command as `$ <cmd>` before its output. The `diff` outputs are complete.

~~~~
$ grep -n '2026-11-06T23:40:00Z] WHO: praxis-master' DECISION_LOG.md
463:- [2026-11-06T23:40:00Z] WHO: praxis-master | WHAT: **UNIT `2026-11-06-wf-values` — AUDIT FAIL 1 (S2 BLOCKING + S1; S8 PASS, fidelity to ruling 4 PASS); ONE correction dispatched (strike 1 of 2).** Auditor (REPORTED BY auditor, 20 tool uses, ~89k tokens): composition/hash `2bf8bf16…` equal; surgical DECISIONS blob verified (prefix = HEAD 1–1163, tail = working 1191–1232; addendum 5 absent); ruling 4 quoted word-for-word; the ruleset's values confirmed (`2026-07-16-b2-noise-area-ruleset.md:31` "14 trading days, fixed", `:32` "exactly 1 × σ", `:50` "no ATR-based stop"); base-file lines (`:74`, `:76`, `:118`, `:205–220`, `:263–264`) and variants (OppBand `:233/:241`; Flat1559 `:91 FlattenMod = CloseMod − 1`) check out; grid 3⁴ = 81; window count re-run `N=1352 K=17 remainder=29 dropped=29 oos_total=1071` (dropped sessions 2026-06-08..07-17); CSCV C(16,8) = 12,870 correct; objective daily-P&L Sharpe ≥100 trades, never net profit; judged arm (a); T1 against the committed baseline 1190 / $197,327.60 at $2.96; WF runs $4.68. S8 PASS — every value PROPOSED; O1 (Q8), MFFU tier/size (Q9), untouched WF items (Q10) asked. **BLOCKING 1 (S2):** entry line "a partly wired input or a wrong stop level fails T6" unsupported — T6 compares only values the strategy PRINTS (entry fill, ATR, stop level) against the oracle; no test checks that actual stop EXITS occur where/when a 1-minute close crosses the oracle's level; so a build that prints the session ATR but stops on σ or a 14-minute ATR, or checks the stop only at HH:00/HH:30 checkpoints, still passes — the gap the fourth adversary named, and it is not in the "still open" list. MINOR 2: spec :125's T5 claim ("a stop that uses the noise multiplier fails T5") false for an m×k×ATR stop at k=1.0 (the entry sentence was corrected, the spec's was not). MINOR 3: §4's three stop rules (session flat before stop; no entry on the stop bar; no entry until ATR exists) have no tests, said only in the report. MINOR 4: MANIFEST row 254 says "tests T1-T5" vs T1–T7. MINOR 5 (S1): report :310 "no code, hook, config or template was edited" rests on a code-only `git status`; the windows command pasted with an elided path. MINOR 6: the report's limitation count (3, two inside pasted greps) unstated. De-identification clean (the one non-dictionary hit is the git author's first name). Correction scope: spec §9 — add an oracle-backed stop-exit test (every stop exit on the bar after the FIRST 1-minute close beyond the oracle's level; no stop exit where the oracle predicts none; both directions; at k = 0.5 and 1.0), tests for the three §4 rules (T8–T10 or listed as deferred WITH the gap stated in the spec), fix :125's T5 claim, restate what each test does and does not catch; entry D-2026-11-06-D's corresponding sentence fixed in place (the unit's own uncommitted text, before/after pasted); MANIFEST row 254 corrected; report Correction 1 with `git status --porcelain` over `.claude/ scripts/ config/ specs/` pasted for the :310 claim, the windows command verbatim, the limitation-count statement, and one fresh read-only adversary on the revised §9 (FULL return pasted). | WHY: park rule; S2 — a test design must not claim coverage it lacks (S9/R3 spirit) | WHERE: spec, DECISIONS 1192–1232, MANIFEST row 254, report | WHEN: ~23:40Z (estimate; last `date -u` 23:31:28Z) | HOW: praxis-manager correction | STATE: open — correction dispatching
$ shasum -a 256 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/spec.before docs/specs/2026-11-06-walk-forward-values.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/dec.before DECISIONS.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/man.before MANIFEST.md
da17a675054318877b9b80b86a450ce899ff4e2b38a91b7f5594e2f2e8cccda3  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/spec.before
985e3c43cc4f29cd32cf64b40e0fb16379ab9295b1be7bd8b1535a535784d75d  docs/specs/2026-11-06-walk-forward-values.md
709decd6cf4e97e07c0536d78717e041e1d962d003cdba009b01f7ca6c59a3d9  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/dec.before
f24286f8ca5e09f7d3e54e976db59bc661193004396f37654773a8b02e15c635  DECISIONS.md
35d1ccc284713d0b67eb454edddd2403a0f997cbaedf96e4f191eb0121fd9e22  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/man.before
f1e3eda87b732f1018deee0099088de653840d3bab2c2e03c86809134d75a5c6  MANIFEST.md
$ head -n 1191 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/dec.before | shasum -a 256; head -n 1191 DECISIONS.md | shasum -a 256
328b2c8d7604bd60fa7c86e28220bf1ddecd4b59f7ba17cb590adeb7560e7a98  -
328b2c8d7604bd60fa7c86e28220bf1ddecd4b59f7ba17cb590adeb7560e7a98  -
$ cmp <(head -n 1191 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/dec.before) <(head -n 1191 DECISIONS.md); echo rc=$?
rc=0
$ cmp <(sed -n 1164,1190p /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/dec.before) <(sed -n 1164,1190p DECISIONS.md); echo rc=$?
rc=0
$ shasum -a 256 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/rep.before; head -n 327 docs/reports/2026-11-06-wf-values-manager.md | shasum -a 256; wc -l < docs/reports/2026-11-06-wf-values-manager.md
9f60254d57e83f88d4c8fe6f01ff6d8f9750b28898470cae9b1b4777c9e56eba  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/rep.before
9f60254d57e83f88d4c8fe6f01ff6d8f9750b28898470cae9b1b4777c9e56eba  -
     327
$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/spec.before docs/specs/2026-11-06-walk-forward-values.md; echo rc=$?
125c125
<   - T5 (every input is live, set through the bridge): every run sends all five inputs in `params`, never only the changed one. T5a (18, 1.0, Off, BandOrVWAP); T5b (14, 1.2, Off, BandOrVWAP); T5c (14, 1.0, 1.0, BandOrVWAP); T5d (14, 1.0, Off, OppBand); then T5e = T1's values again. Checks: (i) the strategy prints its five input values once at `State.DataLoaded` to the NT8 Output window, and each printed set equals the set sent (the bridge's `backtest` response has no parameter readback, bridge report `:65`); (ii) T5a and T5b each differ from T1's trade list, T5c differs from both T1 and T4 (so the two finite stop values are distinct), T5d equals T2, and T5e equals T1 (no value left over from an earlier run). A `Lookback` or `NoiseMult` left hard-coded, a stop that uses the noise multiplier, or a value the bridge fails to set fails T5. (T1–T4 alone cannot catch these.)
---
>   - T5 (every input is live, set through the bridge): every run sends all five inputs in `params`, never only the changed one. T5a (18, 1.0, Off, BandOrVWAP); T5b (14, 1.2, Off, BandOrVWAP); T5c (14, 1.0, 1.0, BandOrVWAP); T5d (14, 1.0, Off, OppBand); then T5e = T1's values again. Checks: (i) the strategy prints its five input values once at `State.DataLoaded` to the NT8 Output window, and each printed set equals the set sent (the bridge's `backtest` response has no parameter readback, bridge report `:65`); (ii) T5a and T5b each differ from T1's trade list, T5c differs from both T1 and T4 (so the two finite stop values are distinct), T5d equals T2, and T5e equals T1 (no value left over from an earlier run). A `Lookback` or `NoiseMult` left hard-coded at its default, two finite stop values that act the same, or a value the bridge fails to set fails T5. (T1–T4 alone cannot catch these.) T5 does not catch a stop that uses the noise multiplier k in place of m: T5c runs k = 1.0 and m = 1.0, where the two stops are the same. That build fails T8 in whichever of T4 (k 1.0, m 0.5), T6c (k 1.2, m 1.0) and T6d (k 0.8, m 0.5) the k-for-m rule changes a predicted stop exit; T8's power check requires at least one such trade, or T8 is not passed. It also fails T6(ii) at T6c and T6d if it prints the level it uses.
128c128,132
<   - Before 2a passes, the code unit can only reach WRITTEN (static diff against the base, no compile, no run). T6(i) can run on the Mac; T1–T5, T6(ii) and T7 run on the VM after 2a. Specified ≠ implemented ≠ tested.
---
>   - T8 (stop exits against the oracle — T6 checks only the values the strategy prints, not where it exits). Runs: T4 and T6d (m = 0.5), T5c and T6c (m = 1.0), and, before §7 uses them, the full-span trade lists of all 54 stop-on walk-forward configurations. Stop exits carry the signal name `XStop`. **Session-flat bar F (from the committed runs):** the session's last bar — 16:00, or 12:00 / 12:15 / 14:03 on early-close days (`docs/reports/2026-11-01-three-strategy-results.md:133`, `:239`) — where NT8's `Exit on session close` fills at the bar's close; under Flat1559 also the 15:59-stamped bar, whose `FlatEOD` fills at the 16:00 bar's open (`:255`). A trade's decision bar d is F for an `Exit on session close` exit, and otherwise the bar before its exit fill. **Order on every bar (PROPOSED; §4's rules in one sequence):** (1) the session flat on F; (2) the stop, from the bar the entry filled on; (3) the checkpoint exits and entries, skipped on a bar where (1) or (2) fired. A test-only script takes each trade's entry fill from the trade list (it must equal the fill the strategy printed, T6(ii)), computes the level L = fill − m × ATR(14) (long) or fill + m × ATR(14) (short) with its own ATR(14) (§4's session definition, from the data file), and scans the 1-minute closes from the entry-fill bar through d for the first bar c with Close ≤ L (long) or Close ≥ L (short). The comparison is exact, in ticks (for a long, 14 × (fill − Close) ≥ m × the sum of the 14 true ranges), and a close equal to L is a crossing (§4's `<=`/`>=`); a build whose floating-point comparison disagrees at an exact tie fails T8. Pass requires all four: (i) every `XStop` exit has c = d, d is not a session-flat bar, and it fills on bar d + 1 by the market-exit fill rule; (ii) a trade with no such c has no `XStop` exit; (iii) no trade has c < d, and a trade with c = d that is not `XStop` exited by the session flat on F = d; (iv) each run's `XStop` count equals the script's count of trades with c = d off a session-flat bar (both printed). **Calibration first:** which bar a fill's time stamps, and the three fill rules — market exit: next bar's open, 2 ticks adverse, clipped to the bar's range; `Exit on session close`: F's close; `FlatEOD`: the 16:00 bar's open, 2 ticks adverse, clipped (`:255`, OBSERVED there) — are refitted from T1's `XL`/`XS`/`Exit on session close` exits and T3's `FlatEOD` exits; if they do not fit, T8 is not graded. **Power checks, all required:** at each m, the T8 runs hold at least one long and one short `XStop`; and for each named wrong stop — ATR of the last 14 one-minute bars, m × the entry bar's band half-width in place of ATR, k in place of m, and the stop checked only at HH:00/HH:30 — the script, recomputing its predictions on the trade lists under test with that rule, finds at least one trade whose predicted stop exit (c, or none) differs from the correct rule's. A build that used that rule would then fail (i)–(iii) on that trade; if no trade differs, T8 is not passed. For k in place of m the difference must come from T4, T6c or T6d, since T5c runs k = m. **T8 catches what T6 cannot:** a build that prints the session ATR and the right level but exits on σ, on a 14-minute ATR or on k, and a build that checks the stop only at the checkpoints. **It cannot catch:** a wrong rule outside the four named that moves no exit in the runs checked (it then changed none of their results); wrong entries in any run not compared with a committed file (T1–T3, T5d, T5e) — T8 takes the build's entries as given, and no test re-simulates a run end to end; a wrong checkpoint exit that closes a trade before the oracle's crossing (the scan ends at the trade's own exit, and T1–T3 check the checkpoint logic only with the stop Off); High-resolution or live fills.
>   - T9 (session flat before the stop): in every T8 run, no `XStop` is decided on a session-flat bar, and every trade still open at F exits by the session flat (`Exit on session close`, or `FlatEOD` under Flat1559). It counts as passed only if at least one trade's first crossing falls on a session-flat bar; without one, T9 is reported UNTESTED.
>   - T10 (no entry on the stop bar): in every T8 run, no entry fills on an `XStop` exit's fill bar (no reversal out of a stop). It counts as passed only if at least one `XStop` decision bar is a checkpoint where the oracle's band rule (T6(ii)) would enter; without one, T10 is reported UNTESTED.
>   - T11 (no entry until ATR exists): in every stop-on run (T4, T5c, T6c, T6d and the 54), no entry fills before s16 (§5's session numbering; ATR(14) needs 15 completed sessions, §4). It counts as passed only if a stop-Off twin with the same lookback (T1, or a walk-forward (10, k, Off, policy) run) has an entry in a session where the band exists and ATR does not (s15 at lookback 14; s11–s15 at lookback 10); without one, T11 is reported UNTESTED.
>   - Before 2a passes, the code unit can only reach WRITTEN (static diff against the base, no compile, no run). T6(i) can run on the Mac; T1–T5, T6(ii), T7 and the runs T8–T11 read run on the VM after 2a (T8–T11's scripts run on the Mac over the exported trade lists and the data file). Specified ≠ implemented ≠ tested.
133c137
< 1. **Confirm or change every PROPOSED value** (ruling 4: "Report the exact values chosen back to me"): grid §3 (81 points); ATR, ATR warm-up and stop rules §4; objective, minimum trade count, no-eligible rule and tie-break §6; CSCV S = 16, rows, ranking and no-eligible rule §7; day-count convention, warm-up and IS → OOS rule §5; arm (a) windows §2; branch, file, class, enum, inputs, readback and acceptance tests T1–T7 §9.
---
> 1. **Confirm or change every PROPOSED value** (ruling 4: "Report the exact values chosen back to me"): grid §3 (81 points); ATR, ATR warm-up and stop rules §4 and T8's bar order §9; objective, minimum trade count, no-eligible rule and tie-break §6; CSCV S = 16, rows, ranking and no-eligible rule §7; day-count convention, warm-up and IS → OOS rule §5; arm (a) windows §2; branch, file, class, enum, inputs, readback and acceptance tests T1–T11 §9.
rc=1
$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/dec.before DECISIONS.md; echo rc=$?
1226c1226
< **Acceptance test for the code unit.** At the committed runs' settings ($2.96 commission, so the reference figures apply): T1 ArmB (14, 1.0, Off, BandOrVWAP) = the base run row for row, 1,190 trades / $197,327.60; T2 with OppBand = the `_OppBand.cs` run, 810 / $210,182.40; T3 with Flat1559 = the `_Flat1559.cs` run, 1,190 / $193,017.60 (`docs/reports/2026-11-01-three-strategy-results.md:402-404`); T4 at (14, 1.0, 0.5, BandOrVWAP), a stop exit fills on the bar after the crossing close, with no stop order placed; T5 five runs through the bridge, each sending all inputs: (18, 1.0, Off, BandOrVWAP) and (14, 1.2, Off, BandOrVWAP) must differ from T1; (14, 1.0, 1.0, BandOrVWAP) must differ from T1 and T4; (14, 1.0, Off, OppBand) must equal T2; T1's values again must equal T1; each run's input values, printed by the strategy at `State.DataLoaded`, must equal those sent. A dead input fails T5, T6 or T7; a partly wired input or a wrong stop level fails T6. T6 checks every use is wired: a static diff showing each base use of `Lookback`/`BandSigmaMult` (`:79`, `:247`, `:257`, `:263`, `:264`) reads the property, and an oracle (σ, bands and ATR at three named 10:00 checkpoints, and the entry fill, ATR and stop level at every entry, recomputed by a test-only script to a relative 1e-9, including two runs with the stop on under Flat1559 and OppBand at k ≠ 1.0). T7: `Contracts` 2 gives exactly 2 × T1's net, and the tab settings (commission template, backtest type, fill resolution, slippage) are read back before every batch. T6's static part can run on the Mac; the rest runs on the VM only after test 2a passes. Before then the code unit reaches WRITTEN at most.
---
> **Acceptance test for the code unit.** At the committed runs' settings ($2.96 commission, so the reference figures apply): T1 ArmB (14, 1.0, Off, BandOrVWAP) = the base run row for row, 1,190 trades / $197,327.60; T2 with OppBand = the `_OppBand.cs` run, 810 / $210,182.40; T3 with Flat1559 = the `_Flat1559.cs` run, 1,190 / $193,017.60 (`docs/reports/2026-11-01-three-strategy-results.md:402-404`); T4 at (14, 1.0, 0.5, BandOrVWAP), a stop exit fills on the bar after the crossing close, with no stop order placed; T5 five runs through the bridge, each sending all inputs: (18, 1.0, Off, BandOrVWAP) and (14, 1.2, Off, BandOrVWAP) must differ from T1; (14, 1.0, 1.0, BandOrVWAP) must differ from T1 and T4; (14, 1.0, Off, OppBand) must equal T2; T1's values again must equal T1; each run's input values, printed by the strategy at `State.DataLoaded`, must equal those sent. A dead input fails at least one of T2–T7 (a dead `StopAtrMult` fails T4, a dead `Contracts` T7). A partly wired input fails T6: its static check, and its printed values where the wrong value reaches them. A stop that exits off the oracle's level — one that prints the session ATR but exits on σ or on a 14-minute ATR, or checks the stop only at the HH:00/HH:30 checkpoints — fails T8, which checks every stop exit against the first 1-minute close beyond a level the test script computes from the entry fill and its own ATR(14); T8 is not passed unless each named wrong rule would change at least one predicted stop exit in the runs. T9–T11 check the session flat before the stop, no entry on a stop exit's fill bar, and no entry before ATR exists; each is reported UNTESTED if the runs hold no case it could fail on. No test checks the entries of a run not compared with a committed file (T1–T3, T5d, T5e). T6 checks every use is wired: a static diff showing each base use of `Lookback`/`BandSigmaMult` (`:79`, `:247`, `:257`, `:263`, `:264`) reads the property, and an oracle (σ, bands and ATR at three named 10:00 checkpoints, and the entry fill, ATR and stop level at every entry, recomputed by a test-only script to a relative 1e-9, including two runs with the stop on under Flat1559 and OppBand at k ≠ 1.0). T7: `Contracts` 2 gives exactly 2 × T1's net, and the tab settings (commission template, backtest type, fill resolution, slippage) are read back before every batch. T6's static part can run on the Mac; the rest runs on the VM only after test 2a passes. Before then the code unit reaches WRITTEN at most.
rc=1
$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/man.before MANIFEST.md; echo rc=$?
254c254
< | /docs/specs/2026-11-06-walk-forward-values.md | Spec | 2 | 2026-11-06 | Walk-forward values PROPOSED under ruling 4 (D-2026-11-06-D): 81-point arm (b) grid, bar-close ATR(14) stop, daily-Sharpe IS objective with 100-trade minimum, 17 windows, CSCV PBO S=16, arm (b) code design and tests T1-T5; awaiting Amear; no code |
---
> | /docs/specs/2026-11-06-walk-forward-values.md | Spec | 2 | 2026-11-06 | Walk-forward values PROPOSED under ruling 4 (D-2026-11-06-D): 81-point arm (b) grid, bar-close ATR(14) stop, daily-Sharpe IS objective with 100-trade minimum, 17 windows, CSCV PBO S=16, arm (b) code design and tests T1-T11; awaiting Amear; no code |
rc=1
$ git status --porcelain .claude/ scripts/ config/ specs/ ninjascript/ | grep -v '^??'; echo rc=$?
 M .claude/settings.json
 M scripts/dispatch-log-writeahead.sh
 M specs/SPEC_RUBRIC.md
rc=0
$ git status --porcelain ninjascript/ config/; echo rc=$?
rc=0
$ stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S%z' .claude/settings.json scripts/dispatch-log-writeahead.sh specs/SPEC_RUBRIC.md
2026-11-05T19:33:46-0500 .claude/settings.json
2026-07-28T12:46:11-0400 scripts/dispatch-log-writeahead.sh
2026-11-06T15:19:10-0500 specs/SPEC_RUBRIC.md
$ git log -1 --format='%h %cI %s' -- config/backtest-cost-model.json | cut -c1-90
69ec506 2026-11-06T17:08:54-05:00 D-2026-11-06-B: Amear's evening rulings 1-5 and loop a-e
$ LC_ALL=C awk -f /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wf/sessions.awk /Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt
N=1352 first=20210308 last=20260717
K=17 remainder=29 dropped=29 oos_total=1071
W01 IS 20210308..20220316 (s1-s252) OOS 20220317..20220615 (s253-s315)
W02 IS 20210604..20220615 (s64-s315) OOS 20220616..20220913 (s316-s378)
W03 IS 20210902..20220913 (s127-s378) OOS 20220914..20221209 (s379-s441)
W04 IS 20211216..20221209 (s190-s441) OOS 20221212..20230310 (s442-s504)
W05 IS 20220317..20230310 (s253-s504) OOS 20230313..20230608 (s505-s567)
W06 IS 20220616..20230608 (s316-s567) OOS 20230609..20230905 (s568-s630)
W07 IS 20220914..20230905 (s379-s630) OOS 20230906..20231201 (s631-s693)
W08 IS 20221212..20231201 (s442-s693) OOS 20231204..20240301 (s694-s756)
W09 IS 20230313..20240301 (s505-s756) OOS 20240304..20240530 (s757-s819)
W10 IS 20230609..20240530 (s568-s819) OOS 20240531..20240827 (s820-s882)
W11 IS 20230906..20240827 (s631-s882) OOS 20240828..20241122 (s883-s945)
W12 IS 20231204..20241122 (s694-s945) OOS 20241125..20250225 (s946-s1008)
W13 IS 20240304..20250225 (s757-s1008) OOS 20250226..20250527 (s1009-s1071)
W14 IS 20240531..20250527 (s820-s1071) OOS 20250528..20250822 (s1072-s1134)
W15 IS 20240828..20250822 (s883-s1134) OOS 20250825..20251120 (s1135-s1197)
W16 IS 20241125..20251120 (s946-s1197) OOS 20251121..20260309 (s1198-s1260)
W17 IS 20250226..20260309 (s1009-s1260) OOS 20260310..20260605 (s1261-s1323)
DROPPED s1324-s1352 20260608..20260717
CSCV rows s12-s1323 = 1312 = 16 x 82
$ pat=$(sed -n 6p docs/specs/2026-11-06-walk-forward-values.md | sed 's/^Standing limitation: //'); /usr/bin/grep -cF "$pat" docs/specs/2026-11-06-walk-forward-values.md; sed -n 1192,1232p DECISIONS.md | /usr/bin/grep -cF "$pat"; /usr/bin/grep -nF "$pat" docs/reports/2026-11-06-wf-values-manager.md | cut -d: -f1
1
1
3
124
126
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
~~~~

The intermediate spec state the adversary attacked was captured right after `edit.py` ran. That state has since been overwritten, so the capture cannot be re-run. Its output, as pasted then:
~~~~
823487245615e623acf522946f5cdd163290ca511db234d4d5ed2249aaed673e  docs/specs/2026-11-06-walk-forward-values.md
d673d2672515ba119dabf6695af8866087275a0f8f9812acfad1f1b844152c08  DECISIONS.md
f1e3eda87b732f1018deee0099088de653840d3bab2c2e03c86809134d75a5c6  MANIFEST.md
328b2c8d7604bd60fa7c86e28220bf1ddecd4b59f7ba17cb590adeb7560e7a98  -
~~~~

**MINOR 5: "no code, hook, config or template edited by this unit".** The `git status --porcelain .claude/ scripts/ config/ specs/ ninjascript/ | grep -v '^??'` output above has three lines. All three were already modified before this unit was dispatched (DECISION_LOG `2026-11-06T23:01:17Z`, which is 18:01:17 at −0500):
- `.claude/settings.json`: mtime 2026-11-05T19:33:46−0500, a day before the dispatch. Not touched by this unit.
- `scripts/dispatch-log-writeahead.sh`: mtime 2026-07-28T12:46:11−0400. Not touched.
- `specs/SPEC_RUBRIC.md`: mtime 2026-11-06T15:19:10−0500, 2 h 42 m before the dispatch. Not touched.
- The cost model `config/backtest-cost-model.json` does not appear. It is committed at `69ec506` (2026-11-06T17:08:54−05:00, before the dispatch), and `git status --porcelain ninjascript/ config/` is empty (rc=0 above).

An mtime shows only that a file has not been written since then. This unit's scripts write only the four files it owns; see `edit.py` / `edit2.py` in the scratchpad.

**MINOR 5: windows command.** It is now pasted with its full path and no `...`: the `LC_ALL=C awk -f /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wf/sessions.awk /Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt` line in the block above. Its output is unchanged: N=1352, K=17, 29 dropped, 1,071 out-of-sample sessions.

**MINOR 6: limitation-sentence count.** This report contains the standing limitation sentence **3 times**: once as a statement (line 3) and twice inside pasted greps (lines 124 and 126). The last command in the block shows this; it prints the line numbers 3, 124 and 126. This Correction 1 section adds none, because its grep reads the sentence from spec line 6 into `$pat` and never writes it out. The spec still has it once and the entry once (`1`, `1` above).

### Adversarial findings

The adversary's full return, verbatim:
~~~~
I found two blocking problems and five minor ones. Neither named wrong build can pass T8 if T8 can be graded, but as written it may not be gradable at all.

**BLOCKING 1 — T8's calibration and T9 rely on a `FlatEOD` exit that the reference runs don't produce.**
- Spec :128 says the fill rule is "fixed from T1's `XL`/`XS`/`FlatEOD` exits … if they do not fit T1, T8 is not graded". T1 must match the baseline, which has no `FlatEOD` exits: its session flat is "Exit on session close 429, XS 429, XL 332" (three-strategy-results :67).
- Those 429 exits fill at the **close** of the 16:00 bar (results :255), not the next bar's open. So the calibration either has nothing to fit or doesn't fit, and T8 can't be graded for any build.
- T9 (:129) says "every trade still open at that bar's close exits `FlatEOD`". A correct copy of the base exits "Exit on session close" under BandOrVWAP and OppBand (results :67, :132). So T9 fails a correct build in T4, T5c, T6d and 36 of the 54 configurations.
- The bar-order rule defines the session flat only at the 16:00 bar (15:59 under Flat1559). Early-close days flatten at 12:00, 12:15 or 14:03 (results :133, :239), and T8(i), (iii), (iv) and T9 are undefined there. The "cannot catch" list doesn't mention this.

**BLOCKING 2 — spec :125 claims "That build fails T8 at T4 (k 1.0, m 0.5), T6c (k 1.2, m 1.0) and T6d (k 0.8, m 0.5)".**
- T8's power checks don't include the k-for-m stop, and they pool results across runs at each m.
- In T6c, if no trade's close reaches 1.0×ATR against the position, T6c passes. The pooled m = 1.0 check can then be satisfied by T5c, where k = m. The claim states a data-dependent result as fact.

**Minor:**
- **M1 (:128):** ties at L are "reported, not graded", but it's unclear whether those trades leave (i)–(iv) and the count. Exact ties aren't rare: by my arithmetic, about 1 in 28 trades at m 0.5 and 1 in 14 at m 1.0.
- **M2 (:128):** "§4's rules in one sequence" adds a new same-bar rule (the stop beats XL/XS) that §4 :62 doesn't state. It is marked PROPOSED, but question 1 covers it only through the test list.
- **M3 (DECISIONS 1226):** it drops T9–T11's UNTESTED conditions and T8's power-check precondition.
- **M4:** stop-Off entries away from the anchor values aren't checked against any oracle. The "cannot catch" list and 1226 imply they are.
- **M5:** T6(ii) never compares the printed fill with the trade list's fill.

**Answers:**
- **Q1:** If T8 can be graded, both builds fail it. The divergent-print build fails (ii) if its level is tighter and (iii) if looser. The checkpoint-only build fails (iii), or the off-checkpoint power check if it never crosses off a checkpoint.
- **Q2:** T11's session arithmetic is correct against base :247/:257 and CommitDay. T11 tests nothing for lookback-18 runs, because the band only exists from s19. T10 is coherent; T9 has BLOCKING 1.
- **Q3:** "A dead input fails at least one of T2–T7" holds.
- **Q4:** No S8 breach. Everything is PROPOSED and covered by question 1.
- **Q5:** clean.
- **Q6:** consistent.

Report: /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/wfc1/adv/report.md

VERDICT: BLOCKING FINDINGS (2)
~~~~

I checked the adversary's evidence for BLOCKING 1 myself. Output, as pasted at the time (`docs/reports/2026-11-01-three-strategy-results.md`):
~~~~
Exit on session close 429, XS 429, XL 332
133: - Exit on session close by time: 16:00 784, 12:15 5, 12:00 2, 14:03 1. XL and XS exits are spread over 7 distinct times each [K03].
239: - FlatEOD by time: 16:00 on all 423. Exit on session close by time: 12:15 5, 14:03 1. XS and XL exits are spread over 11 distinct times each [K03 `[5]`] (OBSERVED).
255: - **Plain words.** The FlatEOD prices equal the OPEN of the 16:00-stamped bar, 2 ticks adverse, clipped to the bar range (OBSERVED). If the bars are end-stamped, that is the price at 15:59:00 wall clock (INFERRED, from the bar-clock section). The baseline's session-close prices equal the CLOSE of the same bar (OBSERVED). The grid records the exit time as 16:00:00 for both [K12], written `4:00:00 P
~~~~

**Dispositions (all made by `edit2.py`; none re-attacked):**

| Finding | Disposition |
|---|---|
| BLOCKING 1 | FIXED. T8 now defines the session-flat bar F as the session's last bar (16:00, or 12:00/12:15/14:03 on early-close days, citing `:133`, `:239`), where NT8's `Exit on session close` fills at the bar's close; under Flat1559, F is also the 15:59 bar, whose `FlatEOD` fills at the 16:00 bar's open (`:255`). d = F for an `Exit on session close` exit. Calibration now refits three fill rules, from T1's `XL`/`XS`/`Exit on session close` exits and T3's `FlatEOD` exits. T9 now accepts `Exit on session close` or `FlatEOD`. |
| BLOCKING 2 | FIXED. "k in place of m" is now a named wrong rule in T8's power checks, and its difference must come from T4, T6c or T6d. Each power check is now stated over the trade lists under test: at least one trade's predicted stop exit must differ under the wrong rule, or T8 is not passed. The T5 sentence now says the build "fails T8 in whichever of T4 …, T6c … and T6d … the k-for-m rule changes a predicted stop exit; T8's power check requires at least one such trade, or T8 is not passed." |
| M1 | FIXED. The comparison is exact, in ticks. A close equal to L counts as a crossing (§4's `<=`/`>=`). The "within 1e-9, not graded" clause is removed. |
| M2 | FIXED. NEEDS AMEAR question 1 now names "T8's bar order §9". |
| M3 | FIXED. The entry now states T8's power-check precondition and T9–T11's UNTESTED conditions. |
| M4 | FIXED. The "cannot catch" list and the entry now say that no test checks the entries of a run that is not compared with a committed file (T1–T3, T5d, T5e). |
| M5 | FIXED. T8 takes the entry fill from the trade list, and that fill must equal the fill the strategy printed (T6(ii)). |
| Q2 note: T11 is vacuous at lookback 18 | ACCEPTED, no edit. T11's power condition already limits it to lookbacks 14 and 10. At lookback 18 the band (s19) gates entries later than ATR (s16). |

The adversary answered Q4 (S8) and Q5 (de-identification) "clean", against the pre-`edit2.py` text. `edit2.py` added one PROPOSED item, which is covered by question 1, and answered no question.

### S6 cross-block check

- F1–F4: untouched. No code, hook, config or template was edited by this correction (MINOR 5 evidence above). F3's fill and slippage terms are used as D-2026-10-30-A sets them. T8's fill rules are cited from committed OBSERVED runs, not changed.
- O1 and O4 stay OPEN. Breakers: no claim.
- Cost model: read only.
- Test 2a: no interaction. T8–T11 need the VM runs after 2a.
- DECISIONS.md lines 1164–1190 (addendum 5) are byte-identical (`cmp` rc=0 above).

### Files staged

None. The index was already populated before this unit, and the unit did not change it (pasted above):
~~~~
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
~~~~
Working tree, this correction: `docs/specs/2026-11-06-walk-forward-values.md` (untracked; 142 → 146 lines); DECISIONS.md line 1226 (one sentence replaced in place, inside the unit's own uncommitted entry); MANIFEST.md row 254; this section (appended).

**Result (Correction 1): PASS**

Every finding in the audit row has been addressed: BLOCKING 1 by T8; MINOR 2 by the T5 sentence; MINOR 3 by T9–T11; MINOR 4 by MANIFEST row 254; MINORs 5 and 6 by the evidence above. The one adversary's two BLOCKING findings and five minors are fixed. Caveat, stated plainly: the `edit2.py` text (T8's session-flat definition, calibration, power checks and tie rule; T9's exit names; the T5 k-for-m sentence; the entry's added clauses) was **not re-attacked**. The brief allows one adversary. The Result above was FAIL for the same reason and also had A4's minors 1 and 3 open; those are now closed by T9–T11. Everything here is specified, not implemented and not tested (S2).
