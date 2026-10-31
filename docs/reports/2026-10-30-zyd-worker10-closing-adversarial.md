# Praxis_build-zyd — worker10 closing ADVERSARIAL attack (after fix pass 4)

## Task
This is the closing attack on the artifact after fix pass 4. It covers DECISIONS.md D-2026-10-30-A (50 lines), the `config/backtest-cost-model.json` diff, and the MANIFEST.md rows added after line 132. The run was read-only. The only file written is this report. `docs/reports/2026-10-30-zyd-f3-artifact.md` is not on disk yet; that is expected and not graded.

## Mode
ADVERSARIAL.

## Criterion
- Bead `Praxis_build-zyd` acceptance (a)(b)(c). For (c), the check is whether the entry's disclosure that it does not establish (c) in full is accurate and consistent.
- Rubric F3 `specs/SPEC_RUBRIC.md:45-57`.
- S2, S4/S5, S6 and S8.

## Sentence-by-sentence table
Line numbers of the form E<n> are lines of the entry as printed by `awk '/D-2026-10-30-A: F3/{f=1} f' DECISIONS.md | cat -n`.

| # | Claim (entry line) | Source | Pasted source text (trimmed) | Grade |
|---|---|---|---|---|
| 1 | E4: the conditional form was ruled by Amear at 00:10:00Z | DECISION_LOG:347 | `[2026-08-29T00:10:00Z] WHO: praxis-master … APPROVED BY: amear … THE RULED FORM, transcribed from Amear's answer` | HOLDS |
| 2 | E4: [N]=2 LOCKED by Amear at 21:36:30Z | :442 | `**WHO: amear** … F3 \`[N]\` IS SET: band-edge slippage = 2 ticks per side … does not change the locked number` | HOLDS |
| 3 | E4/E8/E21: reaffirmed at 22:22:00Z (WHO: amear) | :450, not :446 (the master row) | `[2026-10-30T22:22:00Z] **WHO: amear** … \`[N]\` STAYS 2 ticks — locked before results.` | HOLDS (the shared timestamp is correctly disambiguated) |
| 4 | E4/E21: the commit is Amear's | :442 | `the commit is Amear's` | HOLDS |
| 5 | E8: Q5 locked "1 tick/side slippage + High fill resolution" | DECISIONS:185 | `Q5 cost model: $2.96 round-turn commission + 1 tick/side slippage + High fill resolution. Applies to ALL P&L / SHM distributions.` | HOLDS |
| 6 | E8: 00:35:00Z recorded a market order OnBarClose filled at the next bar's open (INFERRED per 3gm D2(a) :710) | :353; 3gm:710 | `The order is a market order submitted \`OnBarClose\` at a semi-hourly stamp and filled at the next bar's open`; 3gm:710 `DECISION_LOG:353's "filled at the next bar's open" is likewise INFERRED, not observed.` | HOLDS (the label is lower than the row's own "Verified", which is allowed under S2) |
| 7 | E11 (a): 1-min NQCONT, Python-stitched, volume-only crossover + Difference back-adjust (D-2026-07-17-A / D-2026-07-21-A) | DECISIONS:203, :222 | `D-2026-07-17-A … Vol/OI-crossover roll + Difference back-adjustment`; `D-2026-07-21-A … volume-only crossover roll trigger AUTHORIZED` | HOLDS |
| 8 | E11: END-STAMPED, INFERRED from row counts (notes :25); Amear's 9:31/9:32 read REPORTED (notes :23); PASS (notes :22-27); notes file untracked | notes:23,25,27; `git ls-files` | `Amear read the 9:31 bar Open as **28605.25** and the 9:32 bar Open as **28644.25**`; `Source convention: the file is **end-stamped**. It has 1,302 \`17:00:00\` rows…`; `Bar times: **PASS.**`; `error: pathspec … did not match any file(s) known to git` | HOLDS |
| 9 | E11: import file first row `20210307 180100`, last `20260720 112700`, 1,857,362 lines (OBSERVED) | head/tail/wc this session | `20210307 180100;16120.5;…`, `20260720 112700;29005.5;…`, `1857362`; the file ends in `0a` | HOLDS |
| 10 | E11: run-4 range 2021-03-08 → 2026-07-17 (REPORTED) | :450; notes:53 | `2021-03-08 → 2026-07-17 · NQCONT 1-min · BandOrVWAP · 1 contract · Slippage 2 · Standard` | HOLDS |
| 11 | E12 (b): Standard, OBSERVED on run 3 as "Standard (Fastest)" at 22:17:00Z, REPORTED for run 4 | :449; :450 | `Order fill resolution "Standard (Fastest)", Slippage 2` | HOLDS for the value. "set explicitly" comes from Amear's report at :442 (`set EXPLICITLY … REPORTED BY AMEAR`), not from the screenshot. See F-3. |
| 12 | E12: 2 ticks/side = $10/side, 4 ticks / $20 RT, + $2.96 = $22.96 / 4.592 ticks | python3 | `22.96 4.592` | HOLDS |
| 13 | E12: $20 point value on NQCONT is UNVERIFIED per 3gm :949 | 3gm:949 | `Its dollar effect also depends on the UNVERIFIED NQCONT point value.` | HOLDS |
| 14 | E12: whether 2 ticks are applied on every market fill is UNCONFIRMED (22:22 amear) | :450 | `He asks the build side to CONFIRM the unit and that slippage is applied on every market fill.` | HOLDS |
| 15 | E13: sha 35393823…2752265, commit 719ab11 | shasum; git log | `35393823e9bc…2242752265`; `719ab11 Praxis_build-4uu …`; working tree clean | HOLDS |
| 16 | E13: six call sites at :211 :219 :227 :229 :288 :290, none with a price argument; no Set*/Submit*/limit/stop call | sed; grep | `ExitLong("XL", "")`, `ExitShort("XS", "")`, `EnterLong(Contracts, "L")`, `EnterShort(Contracts, "S")`, `ExitLong("FlatEOD", "")`, `ExitShort("FlatEOD", "")`; the call-site count is 6; the negative grep for `Set(StopLoss\|ProfitTarget\|TrailStop)\|SubmitOrder\|Limit\(\|StopMarket\|…` returns rc=1 | HOLDS |
| 17 | E13: :108 IsExitOnSessionCloseStrategy = true | sed | `IsExitOnSessionCloseStrategy              = true;   // backstop` | HOLDS |
| 18 | E13: checkpoint gate :196-198; FlatEOD on mod >= CloseMod :189 | sed | `bool isCheckpoint = (Time[0].Minute == 0 \|\| Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;` / `if (!isCheckpoint \|\| !haveBand) return;`; `if (mod >= CloseMod) { FlattenAll(…); return; }`; `CloseMod = 16 * 60` | HOLDS |
| 19 | E13: OnBarClose at :105; Close[0] at :200 | sed | `Calculate = Calculate.OnBarClose;`; `double price = Close[0];` | HOLDS |
| 20 | E13: section ranges D3 :737-773, Audit-1 §5 :1164-1173, §7 :1185-1207, D2 :688-735, §1 :1032-1083 | 3gm headers | `737:## D3`, `774:## D4`; `1164:### 5.`, `1175:### 6.`; `1185:### 7.`, `1209:### 8.`; `688:## D2`; `1032:### 1.`, `1084:### 2.` | HOLDS |
| 21 | E13: hypothesis 5 at :784 (INFERRED) says High vs Standard could change same-bar exit+reverse and 16:00 resolution | 3gm:779,784 | `Ranked hypotheses, all INFERRED:` / `5. **Order fill resolution** High vs Standard. This could change how same-bar exit+reverse pairs and the 16:00 orders resolve.` | HOLDS |
| 22 | E13: Position.MarketPosition at :201 :226 :228 :287 :289 (3gm §1) | code grep; 3gm §1 | `201: MarketPosition mp = Position.MarketPosition;` … `289: else if (Position.MarketPosition == …` | HOLDS |
| 23 | **E13: "a different resolution of those fills would change later position state and, through it, which later entries fire (3gm `:780`, `:784`, INFERRED …)"** | 3gm:780, :781 | `780: 1. **Trading-hours template** was not CME US Index Futures RTH in run 1 …` / `781: 2. **Exit on session close** or **Time in force** differed. … A position carried overnight changes the next day's \`Position.MarketPosition\` at checkpoints, which changes whether entries fire.` | **BREAKS**: the position-state → later-entries text is at :781. :780 is hypothesis 1 (trading-hours template) and says nothing about position state. See F-1. |
| 24 | E13: "(c) therefore holds only for the checkpoint decision given a position state … does not establish the bead's (c) in full; R3 … would settle it" | :355 | `if the two runs agree, fill resolution is proven inert for this strategy … if they disagree, that disagreement is itself the finding` | HOLDS. The disclosure is accurate and matches the E13 heading, NEEDS AMEAR 5, E50 and the config note. |
| 25 | E13: R3 control proposed at 00:40:00Z, open; its disposition is Amear's | :355 | `PROPOSED TO AMEAR; NOT ADOPTED … STATE: open — proposed to Amear` | HOLDS |
| 26 | E13: the master's note in 21:36:30Z (INFERRED, pending 3gm) says 2 ticks prices stamp-to-next-open slippage | :442 | `(INFERRED from source at \`719ab11\`, to be confirmed by \`Praxis_build-3gm\`), so the number prices stamp-to-next-open slippage, not touch adverse selection` | HOLDS |
| 27 | E13: Amear's framing at 00:10 was stop-cluster adverse selection; 00:35 surfaced the mismatch without a re-ruling | :347; :353 | `at exactly the price level where other participants' stops rest`; `SURFACED TO HIM, NOT RE-DECIDED — THE NUMBER REMAINS HIS` | HOLDS |
| 28 | E15-16: 16:00 FlatEOD next bar may be next day's 09:31; same-bar exit+reverse; early-close days, all CANNOT-DETERMINE-STATICALLY | 3gm:716-717, :758, R15/R21/:585 | `(c) Which order actually closes the 16:00 position: CANNOT-DETERMINE-STATICALLY.` / `its "next bar" is the next day's 09:31 (INFERRED)`; `On early-close days FlattenAll never runs.` | HOLDS |
| 29 | E17: chosen 2026-10-28, before any output; first run 2026-10-30; 3-tick stress run allowed | :442; notes:9 | `chosen 2026-10-28, before any backtest output existed (first Analyzer run was 2026-10-30). A later stress run at 3 ticks is ALLOWED and does not change the locked number` | HOLDS |
| 30 | E18: void clause VERBATIM | programmatic | `IDENTICAL True 289 289`, sha256 `f9144cb5…884a79` for both | HOLDS |
| 31 | E18: NOT triggered and NOT retired; Standard set explicitly; no run has set High (REPORTED BY AMEAR) | :442 | `Void-clause status (REPORTED BY AMEAR, not observed by the master): … The clause is NOT triggered; it is also NOT retired, since no run has set High.` | HOLDS |
| 32 | E19: limitation wording PROPOSED; the ruled requirement is only "Fills are optimistic and the report states so" | :347 | `Fills are optimistic and the report states so.` | HOLDS (the config copy of the wording is byte-identical: `limitation identical True`) |
| 33 | E23: authorisation chain timestamps and WHO | :347 :353 :355 :441 :442 :450 :454 | all seven rows exist; 21:36:00Z is `**WHO: amear**` intake; 22:28:00Z is `DISPATCH: the F3 artifact / \`Praxis_build-zyd\` paperwork unit` | HOLDS |
| 34 | E28-30: scope of config change; `amended` added; no key removed; commission, instrument, applies_to, bead and created unchanged | python key diff | `removed set()` `added {'amended'}`; instrument, applies_to, bead and created each `unchanged True`; `commission unchanged True` | HOLDS |
| 35 | E35: SHM-4 at `STRATEGY_HEALTH_MONITOR_SPEC.md:47-50`; band numbers in Q9 | SHM spec; DECISIONS:189 | `48:### SHM-4 — Live-vs-Backtest Divergence`; `Metric: … slippage, entry timing …`; `SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse` | HOLDS (the range starts on the blank line :47; see F-4) |
| 36 | E36: O4 at :94-99, ±15% / ±25% | rubric | `### O4 — Backtest-vs-live configuration parity … within ±15% win rate and ±25% average trade P&L` | HOLDS |
| 37 | E37: Analyzer template already at Slippage 2 / Standard (REPORTED) | notes:33; :450 | `**Slippage 2** · **Order fill resolution Standard**. Saved as template **"Praxis Backtest"**`; `template re-saved as default` | HOLDS |
| 38 | E38: F4 report §4 at :151, restriction 2 at :45 | F4 report | `151:## 4. S6 cross-block check — MFFU restriction 2 couples to F3`; `45: 2. **Automated tools may not be built to exploit sim-environment fill favorability.**` | HOLDS |
| 39 | E42: first ledger writing of [N] is 21:36:00Z; runs 1–3 had already run | :441; :442; grep of rows before :441 | `(3) F3 \`[N]\` = **2 ticks per side**`; the 21:36:30 row already cites `run 3, 1,075 trades`; no `[N] = 2` row before line 441 (grep returned empty) | HOLDS |
| 40 | E43: readback open from 22:22 (amear): slippage on every fill, and the unit of "Total slippage" | :450 | `CONFIRM the unit and that slippage is applied on every market fill` | HOLDS |
| 41 | E46: [N] scope is reserved for Amear (3gm :949); 21:36:30Z states the cost per RT ($22.96) | 3gm:949; :442 | `Whether that lock was meant to cover session-close and stop-out exits as well is Amear's scope question`; `≈ $22.96 per round trip` | HOLDS |
| 42 | E48: Supersedes Q5 slippage/fill terms only; "Applies to ALL P&L / SHM distributions" stands | DECISIONS:185; :442 | `DECISIONS.md D-2026-07-15-B Q5 (to be amended by append, not edited)` | HOLDS |
| 43 | E50: F3 also needs the backtest report to carry the limitation (`:55-56`) | rubric:55-56 | `**Unblocks when.** The assumption is committed and the backtest report carries it as a stated limitation.` | HOLDS |
| C1 | Config `fill_resolution_note`: "3gm D4 hypothesis 5 (INFERRED) holds that fill resolution could still change … and through the resulting position state which later entries fire" | 3gm:784 vs :781 | hypothesis 5 text is quoted in row 21; the position-state mechanism appears only in hypothesis 2 (:781) | PARTLY BREAKS: the second clause is credited to hypothesis 5 but its mechanism is in hypothesis 2. See F-2. |
| C2 | Config: managed Enter*/Exit* with no price argument; checkpoints or minute-of-day >= 16:00; session-close exit INFERRED; no Set*/Submit* (OBSERVED) | code | as in rows 16-18 | HOLDS |
| C3 | Config totals and breakdown note | python3 | `22.96 4.592`; 2.96/5 = 0.592 | HOLDS |
| C4 | Config: CONDITIONAL under the 00:10:00Z void clause; proposed limitation wording | :347 | as in rows 30 and 32 | HOLDS |

## Mechanical checks pasted
```
$ python3 -c "import json;d=json.load(open('config/backtest-cost-model.json'));print('PARSE OK')"
PARSE OK
$ python3 -c "print(2.96+20, 2.96/5+4)"
22.96 4.592
$ git diff DECISIONS.md MANIFEST.md | /usr/bin/grep -c '^-[^-]'
0
void clause: rows 1 / IDENTICAL True 289 289
f9144cb50aab2885e28daecefb4c3e80a900963769bf396d92c3318629884a79
f9144cb50aab2885e28daecefb4c3e80a900963769bf396d92c3318629884a79
2136 copy identical True
limitation identical True
MANIFEST paths: 19 EXISTS; 1 MISSING = /docs/reports/2026-10-30-zyd-f3-artifact.md (excluded by brief)
config key diff: removed set() / added {'amended'} / instrument, applies_to, bead, created, commission unchanged True
```

## Findings ranked
**F-1 MAJOR (broken citation, S2/S4).** Entry line E13 reads: `… which later entries fire (3gm \`:780\`, \`:784\`, INFERRED — fill resolution is listed among the candidate causes …)`. 3gm:780 is hypothesis 1, `**Trading-hours template** was not CME US Index Futures RTH in run 1`, and it does not support the position-state claim. The supporting text is at :781, hypothesis 2: `A position carried overnight changes the next day's \`Position.MarketPosition\` at checkpoints, which changes whether entries fire.` Worker6 (`zyd-worker6-final-adversarial.md:58`) and worker8 (`:81`) both wrote "D4 #2 (`:780`)". The off-by-one passed through two adversarial passes into the fix. `git show HEAD:` gives the same numbering, so the 3gm file did not shift. The substance is supported one line away, but the cited line is the wrong one. The fix is `:780` → `:781`.

**F-2 MINOR, borderline MAJOR (attribution, S2), same root as F-1.** The config `fill_resolution_note` credits "and through the resulting position state which later entries fire" to "3gm D4 hypothesis 5". Hypothesis 5 (:784) says only `This could change how same-bar exit+reverse pairs and the 16:00 orders resolve.` Its place in D4's trade-count list does imply that it could change which trades occur. The position-state mechanism, however, comes from hypothesis 2 (:781). The DECISIONS entry gets this right at its "Contrary hypothesis" sentence, so the config note says more than its source.

**F-3 MINOR (label scope).** E12 says "set explicitly (OBSERVED on the run-3 screenshot as "Standard (Fastest)" …)". A screenshot shows the value, not whether it was set explicitly. Explicitness is REPORTED BY AMEAR (:442), and the entry labels it that way correctly at E18. The OBSERVED parenthetical is worded as covering only the displayed value.

**F-4 MINOR (range).** The SHM-4 citation `:47-50` starts on a blank line (the header is at :48) and leaves out the Interpretation line :51. It still contains the Metric line that mentions slippage, so the citation is not broken.

**F-5 MINOR (stale downstream text, S6, report only).** `docs/specs/2026-07-15-b2-data-acquisition-spec.md:53` still reads `fills, slippage (Q5, 1 tick/side), and the High-resolution intra…`. The text is a rationale in a spec rather than a numeric consumer. The S6 block does not name it. The repo has no code consumer of the config: a grep of *.py, *.sh and *.js for the config keys came back empty.

**F-6 MINOR.** The config note says "evaluated OnBarClose" without the INFERRED-runtime label that the entry carries at E13. Only the code setting is OBSERVED (:105).

**S8:** nothing of Amear's is decided. Each of the eight protected items is either posed as a NEEDS AMEAR question (1 SHM-4, 2 timing, 4 wording, 5 R3/closure, 6 scope) or stated as Amear's (F3 rubric state at E5, the void-clause trigger at E18, bead closure at E50).

**(c) disclosure:** accurate and consistent across E13, NEEDS AMEAR 5, E50 and the config note. The disclosure itself has no break. F-1 sits inside its supporting sentence.

## NOT CHECKED
- The contents of `ninjascript/` beyond the cited lines, and NT8 runtime behaviour (out of scope for a read-only attack).
- The truncated middle MANIFEST rows (3gm worker4/6, run-3 record, evidence webp, voice notes, zyd worker1/2): their paths were checked for existence only, not their description text.
- The notes file's `:9` line beyond its first 250 characters.
- `docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md`: it is cited only inside ledger rows, not by the entry.
- Whether D-2026-07-04-B's content matches "All SHM distributions and threshold derivations": only its header at DECISIONS:43 was located.

## Files staged
None. Read-only; this report is unstaged.

## Result
BREAK FOUND (F-1 MAJOR).

VERDICT: BREAK FOUND
