# 2026-11-13 strategy-review-index — worker3 (Q3: indicator-based approaches)

## Task

Unit 2026-11-13-strategy-review-index, worker3, MODE: BUILD (read-only research). Authority: DECISION_LOG.md last row `2026-11-13T20:36:45Z`. HEAD `9ff8a48` on `main` (OBSERVED, `git rev-parse --short HEAD`).

Question Q3: has the record ever considered INDICATOR-based approaches? Searched areas: `docs/` (split into non-reports and `docs/reports/`), the four root ledgers (DECISIONS.md, DECISION_LOG.md, STATUS.md, HANDOFF.md), `specs/`, `vm/`, the code directories (`ninjascript/`, `scripts/`, `tools/`, `src/`, *.cs/*.py/*.js/*.pine), and `Redemtion/` (39 text-bearing files converted to plain text in the scratchpad: .rtf via `textutil`, .pdf via `pdftotext`, .md/.jsx/.tsx copied). `docs/research/` does not exist (the `ls docs` listing below shows no such directory). The 2026-10-28 F4 reply-filing report and `docs/reports/evidence/` were excluded from every grep.

Working-tree note: `docs/specs/2026-11-05-walk-forward-spec.md` and `docs/specs/2026-11-06-walk-forward-values.md` show ` M` in git status at session start, so the counts read the working-tree versions of those two files, not the committed ones.

## Term-count table

The figures count matching LINES (`grep -h ... | wc -l`), case-insensitive. `-w` was used for SMA, EMA, RSI, MACD, ATR, ADX, delta and ORB. All other terms use the `-E` patterns shown in the script under Evidence E2. Zeros are included.

| term | docs (non-reports) | docs/reports | root ledgers | specs/ | vm/ | code | Redemtion |
|---|---|---|---|---|---|---|---|
| moving average | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SMA | 1 | 2 | 0 | 0 | 0 | 0 | 0 |
| EMA | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| crossover | 7 | 50 | 25 | 0 | 0 | 33 | 2 |
| RSI | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| MACD | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Bollinger | 0 | 1 | 0 | 0 | 0 | 0 | 5 |
| Keltner | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| VWAP (any) | 40 | 687 | 47 | 0 | 3 | 197 | 10 |
| VWAP band | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| ATR | 57 | 198 | 53 | 0 | 0 | 55 | 41 |
| ADX | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| stochastic | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Supertrend | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| volume profile | 0 | 2 | 0 | 0 | 0 | 0 | 1 |
| order flow | 1 | 1 | 0 | 0 | 0 | 0 | 6 |
| footprint | 0 | 12 | 0 | 0 | 0 | 0 | 1 |
| delta (word) | 1 | 70 | 8 | 0 | 0 | 15 | 3 |
| cumulative delta | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ichimoku | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Donchian | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| opening range | 1 | 21 | 0 | 0 | 0 | 0 | 14 |
| ORB | 0 | 43 | 4 | 0 | 0 | 0 | 12 |
| pivot | 0 | 6 | 3 | 0 | 0 | 0 | 5 |
| indicator | 6 | 46 | 2 | 0 | 0 | 0 | 39 |

Noise in the counts, checked:
- **crossover:** in code, every hit shown is the Vol/OI contract-roll crossover in `scripts/b2_stitch.py` and its self-test (Evidence E5). In docs and the ledgers, the non-roll residue is the NT8 bundled "Sample MA crossover" in a UI list, plus stitch prose (Evidence E9).
- **delta:** the code hits are numeric (`delta=1e-12`, minute gaps, seam deltas) (Evidence E5). In docs and the ledgers, only 1 line pairs delta with volume/bid/ask/order/cumulative/footprint, and it is not an order-flow use (Evidence E9).
- **footprint:** all the docs hits shown are "install/disk/unit footprint" (Evidence E7).
- **pivot:** the hits are NT8 bundled indicator file names (`@Pivots.cs` and others) in a directory listing, plus "pivot" meaning a change of plan (Evidence E7).
- **SMA:** the docs non-report hit is a binary PNG match. The 2 report hits are a `private double Sma(int period, int barsAgo)` helper inside a quoted third-party GitHub file in `docs/reports/2026-11-04-comparable-builds.md:695,840` (Evidence E7, E9).
- **volume profile:** the hits are an observed 1-minute volume-by-timestamp table (`docs/reports/2026-11-01-three-strategy-results.md:49`), not a volume-profile indicator (Evidence E7).

## (a) Indicators used inside existing strategies

1. **Session VWAP as the trailing-stop/exit component of Noise-Area (CODED).**
   - `ninjascript/PraxisNoiseAreaBreakout.cs:46`: "// BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). DEFAULT."
   - `:87`: "// Session-anchored VWAP (spec §4 p.13, footnote 2: RTH data only, anchored at 09:30 open)."
   - `:118`: "ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec §4 p.13 — paper's PREFERRED exit. The only knob."
   - The ruleset `docs/specs/2026-07-16-b2-noise-area-ruleset.md:60-61` gives the source: "trailing stop at **band-or-VWAP**, whichever is tighter to price".
   - VWAP hits also appear in the `_OppBand` and `_Flat1559` variants (28 and 26 lines) and in the `scripts/wf/` oracles and tests (Evidence E4).
   - Status: CODED. I did not establish which exit mode each recorded Strategy Analyzer run used (see Gaps).
2. **ATR(14) stop as an added tunable in walk-forward arm (b) of Noise-Area (WRITTEN, not compiled, not run, as of the STATUS card I read).**
   - DECISIONS.md:812 quotes the ruling: "(b) four parameters tuned per window — lookback, noise multiplier, stop-ATR multiplier, exit policy. A stop is added to the strategy for (b) on its own branch".
   - DECISIONS.md:1224: "Q6 ATR(14) = 14 completed RTH sessions (daily ATR)."
   - DECISIONS.md:1339: "| Stop-ATR multipliers | {1.5, 2.25, 3.0} × ATR(14) |".
   - The ruleset `:96` flags it as non-paper: "Paper uses band/VWAP stops, not ATR. If Block-2 insists on an ATR stop it is a **new, untested variant**". The main-branch `.cs:34` reads "NO ATR stop".
   - Status, STATUS.md:192: "Arm (b): `.cs` WRITTEN only — not compiled, not run; on `arm-b/wf-tunables` only". The test oracle `scripts/wf/oracle/atr.py` is described at STATUS.md:194 as "WRITTEN + TESTED on synthetic fixtures (59 tests)" and "UNVERIFIED against NT8 arm (b)".
   - The branch commit `c16f85f` subject reads "(WRITTEN, not compiled, not run)" (Evidence E8). I did not check whether any later record changes this status (see Gaps).
3. **Indicator mentions inside other strategy candidates (research text only, not coded).**
   - Redemtion "Systematic, Higher-Frequency NQ Strategies…" (converted-text line 80) lists LHHM as "**Low** (1 time-trigger, 1 indicator)" and TC-FHM as "Low–Medium (ATR, σ20, r1)".
   - The Phase 2 table marks TC-FHM "**DEFERRED** — correlated with Strategy #1, testing as regime filter only" (Evidence E3).
   - The `PraxisLastHalfHourMomentum.cs` grep for vwap/ATR/indicator/SMA/EMA shows no indicator terms. The only hits are substrings of "schema"/"geometry" in PraxisSignalConsumer.cs (Evidence E4).

## (b) Indicator-driven strategies

Each item is listed at the strongest status the record shows. Nothing is upgraded.

1. **Standalone VWAP/Bollinger mean reversion on NQ: EXCLUDED at Phase 2 (research table; source docs in Redemtion/).**
   - Redemtion "PRAXIS PHASE 2 — EXPANDED STRATEGY SEARCH" (converted-text line 47), also in the Research Prompts .md at line 47: "| Standalone VWAP/Bollinger reversion on NQ | **EXCLUDED** — no peer-reviewed NQ evidence post-2018 | — |".
   - "Systematic, Higher-Frequency…" (line 19): "**Standalone VWAP-reversion, Bollinger-band reversion, opening-range breakout, and opening-gap fade lack peer-reviewed validation specifically on NQ futures over 2018–2025 with sample size ≥200 and full cost accounting.**"
   - The same document, line 106: "Properly excluded by the user."
   - In-repo restatement: `docs/reports/2026-11-08-strategy-filter-audit.md:119` lists "VWAP/Bollinger reversion" among the "ELIMINATED, EXCLUDED or DEFERRED" entries.
   - Status: MENTIONED and EXCLUDED on evidence grounds. Never coded or backtested.
2. **Volatility-weighted VWAP σ-band mean reversion ("C1"): PROPOSED by external research on 2026-11-13, rated low, channel-recommended for backtest, with no ledger decision found.**
   - `docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:68`: "C1. Volatility-Weighted VWAP Mean Reversion".
   - `:81`: "Post-2018 evidence: None found."
   - `:85`: "Fit: Low."
   - `:20`: "Gap fade (C2), VWAP (C1), London close (C4) and new C6 rated low; C4 and C6 dropped. Agreed."
   - `:39`: "Only then code a contrasting strategy (gap fade or VWAP) and test the combination."
   - `docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md:30`: "Backtest order: (1) PraxisLastHalfHourMomentum, already written; (2) Candidate 1 VWAP mean reversion; (3) Candidate 2 opening-gap fade; Candidate 4 parked."
   - The section heading at `:28` reads "(the channel's, not an Amear ruling; master decides under D1)".
   - A grep of the four root ledgers for `vwap (mean|reversion)|mean[ -]reversion|gap fade` returned no lines (Evidence E6).
   - Status: PROPOSED/RECOMMENDED only. No .cs or .pine file for it among the 34 tracked code files (Evidence E1).
3. **Opening range breakout (ORB / TORB): EVALUATED repeatedly. Never coded. Shortlisted as written specs.** Note that an opening range is a price level rather than a classic oscillator or average. It is listed here because the brief names it.
   - Redemtion Phase 2 table (line 38): "| 5-Minute Opening Range Breakout on NQ (standalone) | **ELIMINATED** — no robust standalone edge on NQ without filters | Multiple replications |".
   - The shortlist (line 162): "Useful as a **secondary execution overlay** … Not recommended as a stan…" (line truncated by my `cut`).
   - The Gemini/Kimi brief (`…strategy-research.md:74`) lists "unfiltered opening range breakout" under "Already rejected (do not re-propose without new post-2020 evidence)".
   - The 7zq M2 shortlist ranked TORB #2 and ORB #3 (`docs/reports/2026-10-31-7zq-m2-new-strategy.md:19-20`). Amear kept LHHM (DECISIONS.md:360): "*"Keep #1 (as built)"* — `PraxisLastHalfHourMomentum` … stands; TORB and ORB remain written specs in the shortlist."
   - `docs/reports/2026-11-08-strategy-filter-audit.md:115`: "ORB on Stocks in Play (D2 #5) | Deprioritized".
4. **Order-flow imbalance / deep-OFI: EXCLUDED at Phase 2.**
   - Redemtion table (line 45): "| Order-flow imbalance / deep-OFI | **EXCLUDED** — 2-price-change horizon, requires co-location | Kolm-Turiel-Westray 2023 |".
   - There are no footprint or cumulative-delta strategies anywhere (0 cumulative-delta hits in every area).
5. **Passing mentions only (not proposals):**
   - NT8 bundled "SampleMACrossover" used as a practice exercise in the Video-First Learning Resources doc (line 390). The same bundled sample appears in an NT8 UI list in docs.
   - Pine `indicator()` vs `strategy()` teaching text.
   - "technical indicators" as LLM-context examples in Redemtion `Research Results/report.md` (lines 134, 150, 302, 304).
   - Phase 0 summary (line 96): "A subscription algo or black-box indicator will not survive his neurology". This is a constraint statement. Quoted, not interpreted.

## Plain conclusion

The record does consider indicators, but only in three ways:
- Inside the Noise-Area strategy: the session VWAP is CODED as the default exit, and an ATR(14) stop is WRITTEN for walk-forward arm (b).
- As a handful of indicator-driven candidates, which were screened out or left at proposal stage: standalone VWAP/Bollinger reversion was EXCLUDED, ORB was ELIMINATED as a standalone and parked as written specs, OFI was EXCLUDED, and VWAP σ-band reversion was PROPOSED and channel-recommended on 2026-11-13 with no ledger ruling found.

The classic oscillator and moving-average families appear nowhere as strategies. Moving average, RSI, MACD, Keltner, ADX, stochastic, Supertrend, cumulative delta, Ichimoku and Donchian have 0 hits in every area. SMA, EMA and "MA crossover" occur only as incidental text.

There is no record of a systematic look at indicator-driven strategies. The screening that did happen was organised around peer-reviewed post-2018 NQ evidence. The exclusion reason quoted for the indicator-style entries is "no peer-reviewed NQ evidence post-2018". No indicator-driven strategy has been coded or backtested.

## Evidence (command output)

**E1. HEAD, authority row, directories, code files**
```
$ git rev-parse --short HEAD && tail -1 DECISION_LOG.md | cut -c1-400 && ls -d */ | head -50 && git ls-files | grep -E '\.(cs|py|js|pine)$' | ... | head -50 && git ls-files | grep -E '\.(cs|py|js|pine)$' | wc -l
9ff8a48
- [2026-11-13T20:36:45Z] WHO: praxis-master | WHAT: **Unit 2026-11-13-research-filing COMMITTED `9ff8a48`, pushed ...
config/ deploy/ docs/ n8n-workflows/ ninjascript/ phases/ plugins/ Redemtion/ scripts/ signals/ specs/ src/ tests/ tools/ vm/ workflows/
ninjascript/PraxisLastHalfHourMomentum.cs
ninjascript/PraxisNoiseAreaBreakout.cs
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
ninjascript/PraxisSignalConsumer.cs
scripts/b2_stitch.py
scripts/b2data_raw_validate.py
scripts/tests/b2-stitch-selftest.py
scripts/wf/oracle/atr.py  band.py  grade.py  market.py  policy.py  t6ii.py  (+ oracle/tests/*.py)
scripts/wf/pbo.py report.py select.py sessions.py tradelist.py (+ wf/tests/*.py)
tools/tickprep/MakeSynth.cs
tools/tickprep/TickPrep.cs
      34
$ ls docs
agent-spawn-guard.md briefs design presentations reference reports runbooks specs
$ ls specs ; find Redemtion -type f | wc -l ; which pdftotext textutil
SPEC_RUBRIC.md
      42
/opt/homebrew/bin/pdftotext
/usr/bin/textutil
```
The directory list and the code-file list above are condensed onto fewer lines. The file names are verbatim. Redemtion: 42 files, of which 3 are `.DS_Store`. 39 were converted (the `ls | wc -l` of the scratchpad shows `39`, total `12137` lines). The PDF converted to 824 lines.

**E2. Count script and output (the source of the table)**
```
$ cat scratchpad/count.sh   (key lines)
EX=(--exclude='2026-10-28-f4-*' --exclude-dir=evidence --exclude='2026-11-13-strategy-review-index-worker3.md')
 docs-nonreports) /usr/bin/grep -r -h -i "${EX[@]}" --exclude-dir=reports "${@:2}" $R/docs ;;
 docs-reports) /usr/bin/grep -r -h -i "${EX[@]}" "${@:2}" $R/docs/reports ;;
 root-ledgers) /usr/bin/grep -h -i "${@:2}" $R/DECISIONS.md $R/DECISION_LOG.md $R/STATUS.md $R/HANDOFF.md ;;
 specs) /usr/bin/grep -r -h -i "${@:2}" $R/specs ;;
 vm) /usr/bin/grep -r -h -i "${@:2}" $R/vm ;;
 code) /usr/bin/grep -r -h -i --include='*.cs' --include='*.py' --include='*.js' --include='*.pine' "${@:2}" $R/ninjascript $R/scripts $R/tools $R/src ;;
 redemtion) /usr/bin/grep -r -h -i "${@:2}" $RT ;;
TERMS: moving[ -]averages? | -w SMA | -w EMA | cross-?overs?|crosses (above|below) | -w RSI | -w MACD | bollinger | keltner
 | vwap | vwap[ -]?bands? | -w ATR | -w ADX | stochastic | super[ -]?trend | volume[ -]profile | order[ -]?flow | footprint
 | -w delta | cumulative[ -]delta | ichimoku | donchian | opening[ -]range | -w ORB | pivot | indicators?
(count per cell = matching lines | wc -l)

$ bash scratchpad/count.sh
term               docs-nonreports    docs-reports    root-ledgers           specs              vm            code       redemtion
moving average                   0               0               0               0               0               0               0
SMA                              1               2               0               0               0               0               0
EMA                              0               0               0               0               0               0               1
crossover                        7              50              25               0               0              33               2
RSI                              0               0               0               0               0               0               0
MACD                             0               0               0               0               0               0               0
Bollinger                        0               1               0               0               0               0               5
Keltner                          0               0               0               0               0               0               0
VWAP (any)                      40             687              47               0               3             197              10
VWAP band                        0               1               0               0               0               0               0
ATR                             57             198              53               0               0              55              41
ADX                              0               0               0               0               0               0               0
stochastic                       0               0               0               0               0               0               0
Supertrend                       0               0               0               0               0               0               0
volume profile                   0               2               0               0               0               0               1
order flow                       1               1               0               0               0               0               6
footprint                        0              12               0               0               0               0               1
delta (word)                     1              70               8               0               0              15               3
cumulative delta                 0               0               0               0               0               0               0
Ichimoku                         0               0               0               0               0               0               0
Donchian                         0               0               0               0               0               0               0
opening range                    1              21               0               0               0               0              14
ORB                              0              43               4               0               0               0              12
pivot                            0               6               3               0               0               0               5
indicator                        6              46               2               0               0               0              39
```
The Redemtion EMA=1 cell is the Video-First doc line 300, a Pine teaching line. The match is isolated below:
```
$ /usr/bin/grep -n -o -i -E '.{20}\bema\b.{20}' *Video-First*
300: boilerplate for an EMA-cross alert with we
```
This is a passing mention, a Pine alert tutorial example. It is not a strategy proposal.

**E3. Redemtion (converted text) key hits**
```
$ /usr/bin/grep -n -i -E 'moving[ -]average|\bSMA\b|\bEMA\b|cross-?over|bollinger|volume[ -]profile|order[ -]?flow|footprint|cumulative|opening[ -]range|\bORB\b|pivot|\bdelta\b' * | cut -c1-330   (selected lines)
..._EXPANDED_STRATEGY_SEARCH__THREE-AGENT_DEEP_RESEARCH.rtf.txt:38:| 5-Minute Opening Range Breakout on NQ (standalone) | **ELIMINATED** — no robust standalone edge on NQ without filters | Multiple replications |
..._EXPANDED_STRATEGY_SEARCH__THREE-AGENT_DEEP_RESEARCH.rtf.txt:45:| Order-flow imbalance / deep-OFI | **EXCLUDED** — 2-price-change horizon, requires co-location | Kolm-Turiel-Westray 2023 |
..._EXPANDED_STRATEGY_SEARCH__THREE-AGENT_DEEP_RESEARCH.rtf.txt:47:| Standalone VWAP/Bollinger reversion on NQ | **EXCLUDED** — no peer-reviewed NQ evidence post-2018 | — |
..._Systematic,_Higher-Frequency_NQ_Strategies_to_Pair_with_the_Noise-Area_Breakout_.rtf.txt:19:1. **Standalone VWAP-reversion, Bollinger-band reversion, opening-range breakout, and opening-gap fade lack peer-reviewed validation specifically on NQ futures over 2018–2025 with sample size ≥200 and full cost
..._Systematic,_Higher-Frequency_NQ_Strategies_to_Pair_with_the_Noise-Area_Breakout_.rtf.txt:106:1. **Pre-FOMC drift, opening gap fade, and pure VWAP/Bollinger reversion** lack peer-reviewed evidence of survival on NQ post-2018. Properly excluded by the user.
..._Verified_Trading-Strategy_Shortlist_for_NQ___Index_Futures.rtf.txt:162:- *Net recommendation:* Useful as a **secondary execution overlay** layered on top of #3 or #4 (i.e., use the announcement-day filter to define a "trade day" and the ORB to define entry timing on that day). Not recommended as a stan
..._Video-First_Learning_Resources_for_an_Automated_NQ_Futures_Trading_Stack.rtf.txt:390:- **Day 6–7**: ... Try enabling/disabling NinjaTrader’s bundled “SampleMACrossover” strategy on a
$ sed -n '28,50p' "..._EXPANDED_STRATEGY_SEARCH....rtf.txt"   (table rows, selected)
| Noise-Area Intraday Momentum Breakout (Zarattini–Aziz–Barbon 2024) | **SELECTED** as baseline. ...
| Threshold-Conditioned First-Half-Hour Momentum (Rosa 2022) | **DEFERRED** — correlated with Strategy #1, testing as regime filter only | *Journal of Futures Markets* |
$ sed -n '74,82p' "..._Systematic,_Higher-Frequency....rtf.txt"   (row 80)
|Automation complexity       |**Low** (1 time-trigger, 1 indicator)               |Low–Medium (ATR, σ20, r1)                                 |Medium (needs VIX feed) ...
$ sed -n '94,98p' Intitialization-April_2026_PHASE_0_OUTPUT_SUMMARY.md.txt
**Context:** The trader cannot execute what he doesn\'92t understand. A subscription algo or black-box indicator will not survive his neurology \'97 he\'92ll either override it or abandon it within weeks. ...
```
In E3, the "(selected lines)" and "(table rows, selected)" markers mean only some output lines are shown. File-name prefixes are shortened with "...". The lines shown are byte-exact. The full outputs are in this session's transcript.

**E4. VWAP/ATR usage in code**
```
$ /usr/bin/grep -r -c -i vwap (code dirs) | grep -v ':0$'
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:28
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:26
ninjascript/PraxisNoiseAreaBreakout.cs:26
scripts/wf/oracle/band.py:9   t6ii.py:4   market.py:6   policy.py:10   grade.py:2   (+ oracle/tests, wf/*.py, wf/tests)
$ /usr/bin/grep -r -c -i -w ATR (code dirs) | grep -v ':0$'
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:1
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:1
ninjascript/PraxisNoiseAreaBreakout.cs:1
scripts/wf/oracle/t6ii.py:5  market.py:3  atr.py:8  policy.py:2  grade.py:11  (+ oracle/tests)
$ /usr/bin/grep -n -i -w ATR ninjascript/PraxisNoiseAreaBreakout.cs
34://     multiplier as a tunable), NO ATR stop. The ONLY selectable knob is the exit form (ExitMode).
$ /usr/bin/grep -n -i vwap ninjascript/PraxisNoiseAreaBreakout.cs | head -14
46:	// BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). DEFAULT.
87:		// Session-anchored VWAP (spec §4 p.13, footnote 2: RTH data only, anchored at 09:30 open).
118:				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec §4 p.13 — paper's PREFERRED exit. The only knob.
174:				vwapCumPV  += ((High[0] + Low[0] + Close[0]) / 3.0) * vol;   // typical-price VWAP
$ sed -n '1,25p' scripts/wf/oracle/atr.py
"""atr.py — the arm (b) daily ATR(14) and bar-close stop, as ninjascript/PraxisNoiseAreaBreakoutArmB.cs
(origin/arm-b/wf-tunables) computes them (unit 2026-11-07-wf-oracles, W1). Test oracle only.
$ /usr/bin/grep -n -i -E 'vwap|\bATR\b|indicator|SMA|EMA' ninjascript/PraxisLastHalfHourMomentum.cs ninjascript/PraxisSignalConsumer.cs | head
ninjascript/PraxisLastHalfHourMomentum.cs:23:// SOURCE: Baltussen, G., Da, Z., Lammers, S., Martens, M. (2021), "Hedging demand and market intraday
ninjascript/PraxisSignalConsumer.cs:32:// GEOMETRY GATE ...   (all remaining hits: "schema"/"geometry" substrings; no indicator use)
```
The multi-file count lines in E4 are condensed onto fewer lines. In the head -14 VWAP listing, only selected lines are shown.

**E5. Code crossover and delta hits are non-indicator**
```
$ /usr/bin/grep -r -n -i -E 'cross-?overs?|crosses (above|below)' (code dirs) | head -12
scripts/tests/b2-stitch-selftest.py:7:#   1. the Vol/OI-crossover ROLL DATES are detected exactly, and
scripts/b2_stitch.py:3:# Continuous NQ 1-min series builder: Vol/OI-crossover roll + Difference
scripts/b2_stitch.py:6:# (DECISIONS.md 2026-07-15): Volume/OI-crossover roll trigger + Difference
$ /usr/bin/grep -r -n -i -w delta (code dirs)
scripts/b2_stitch.py:752:        delta = (cur["ts"] - prev["ts"]).total_seconds() / 60.0
scripts/wf/tests/test_select.py:104:        self.assertAlmostEqual(s, math.sqrt(945), delta=1e-12)
```
E5 shows representative lines. All 12 crossover lines shown in the session were in `b2_stitch.py` or its self-test. All delta lines were numeric or seam deltas.

**E6. 2026-11-13 external research (VWAP σ-band C1) and ledger check**
```
$ /usr/bin/grep -n -i -E '^#|vwap|indicator|\bATR\b|strateg(y|ies) [0-9A-Z]' docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md
20:4. Gap fade (C2), VWAP (C1), London close (C4) and new C6 rated low; C4 and C6 dropped. Agreed.
39:3. Only then code a contrasting strategy (gap fade or VWAP) and test the combination.
68:C1. Volatility-Weighted VWAP Mean Reversion
81:Post-2018 evidence: None found. We are not aware of any academic test of this exact VWAP+volatility band strategy on NQ or other indices. ...
83:Tunable parameters: $;k$ (VWAP band multiplier, e.g. 2.5); stop-multiplier (4); VWAP anchor (09:30); $\sigma$ lookback (60-min). At least 1–2.
85:Fit: Low. The profile is low win rate. ...
$ sed -n '28,31p' docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md
## 3. Channel recommendation (the channel's, not an Amear ruling; master decides under D1)
Backtest order: (1) PraxisLastHalfHourMomentum, already written; (2) Candidate 1 VWAP mean reversion; (3) Candidate 2 opening-gap fade; Candidate 4 parked. ...
$ grep ... strategy-research.md   (line 74)
74:Already rejected (do not re-propose without new post-2020 evidence): pre-FOMC drift; trading the macro release itself; post-earnings drift; short volatility; single-instrument CTA trend; unfiltered opening range breakout; ...
$ /usr/bin/grep -n -i -E 'vwap (mean|reversion)|mean[ -]reversion|gap fade' DECISION_LOG.md DECISIONS.md STATUS.md HANDOFF.md | cut -c1-300
(no output)
```
In E6, the Kimi grep output is shown for selected lines only, and line 74 is from the same grep run against the strategy-research file.

**E7. ORB / opening-range, low-count term hits in docs and ledgers**
```
$ /usr/bin/grep -n -i -E '\bORB\b|opening[ -]range' DECISIONS.md DECISION_LOG.md docs/reports/2026-10-31-7zq-m2-*.md docs/reports/2026-11-08-strategy-filter-audit.md
DECISIONS.md:360:- **R-7zq-3 — third file (answers NEEDS AMEAR 6 above), DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear):** *"Keep #1 (as built)"* — `PraxisLastHalfHourMomentum` (Baltussen, Da, Lammers & Martens 2021) stands; TORB and ORB remain written specs in the shortlist.
docs/reports/2026-10-31-7zq-m2-new-strategy.md:19:| 2 | Timely Opening Range Breakout (TORB) | Tsai et al. 2019, *IEEE Access* | ...
docs/reports/2026-10-31-7zq-m2-new-strategy.md:20:| 3 | 5-min ORB on QQQ | Zarattini & Aziz 2023 (SSRN) | abstract only; rules from a GitHub README → **UNVERIFIED-from-secondary** | 2/2/2/2/2 | 10 |
docs/reports/2026-11-08-strategy-filter-audit.md:115:| ORB on Stocks in Play (D2 #5) | Deprioritized: not the preferred class, fails cascade resistance, weak narrative | ...
docs/reports/2026-11-08-strategy-filter-audit.md:119:| The other 13 resolved NQ/ES entries (D4 table: ORB standalone, Pre-FOMC drift, PEAD, VRP/short-VIX, End-of-Day Reversal, OFI, 0DTE gamma, VWAP/Bollinger reversion, gap fade, ML/GBM, TC-FHM; Noise-Area SELECTED and LHHM covered above) | ELIMINATED, EXCLUDED or DEFERRED | ...
$ (bollinger / volume profile / footprint / vwap band / pivot greps over docs + ledgers, selected)
docs/reports/2026-11-01-three-strategy-results.md:49:- **Volume profile** [K11] (OBSERVED): on weekdays the largest mean 1-minute volumes are at stamps 1600 ...
docs/reports/2026-10-31-a9d-future-row-plan.md:55:6. Footprint: 1,710 files, about 16-19 MB, ...
docs/reports/2026-10-31-7zq-m1-worker1-build-variants.md:150:./NinjaTrader 8/bin/Custom/Indicators/@Pivots.cs
docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:83:Tunable parameters: $;k$ (VWAP band multiplier, e.g. 2.5); ...
Binary file docs/reference/assets/nt8-2026-07-24/11-strategy-analyzer.png matches   (the SMA docs-nonreports hit)
docs/reports/2026-11-04-comparable-builds.md:695:167:        private double Sma(int period, int barsAgo)
```
In E7, the 7zq-m2 glob stands for the three files I named on the actual command line, and the second block is selected lines only.

**E8. Arm (b) ATR status**
```
$ /usr/bin/grep -n -i -w ATR DECISIONS.md | head -20   (selected)
812:- *"1. Walk-forward runs BOTH ways: (a) paper's fixed rules, nothing optimised; (b) four parameters tuned per window — lookback, noise multiplier, stop-ATR multiplier, exit policy. A stop is added to the strategy for (b) on its own branch; ...
1224:   Q6 ATR(14) = 14 completed RTH sessions (daily ATR).
1339:| Stop-ATR multipliers | {1.5, 2.25, 3.0} × ATR(14) | SETTLED (the master, D-2026-11-07-A :1262); ...
$ /usr/bin/grep -n -i -E 'vwap|\bATR\b' docs/specs/2026-07-16-b2-noise-area-ruleset.md   (selected)
50:| Stop-ATR | **not used** — there is no ATR-based stop anywhere in the paper | — |
96:| **stop-ATR mult** | **no paper analog** | Paper uses band/VWAP stops, not ATR. If Block-2 insists on an ATR stop it is a **new, untested variant** — flag for trader (§7). ...
$ /usr/bin/grep -n -i -E 'arm[ -]?\(?b\)?' STATUS.md | head -8   (selected)
192:- Arm (b): `.cs` WRITTEN only — not compiled, not run; on `arm-b/wf-tunables` only (`18:12:00Z`). There is no C# compiler on the Mac (`16:04:00Z`).
194:- Oracles: WRITTEN + TESTED on synthetic fixtures (59 tests); values COMPUTED on the real file at both session starts; UNVERIFIED against NT8 arm (b); ...
$ git log --oneline -3 origin/arm-b/wf-tunables
c16f85f ninjascript: add PraxisNoiseAreaBreakoutArmB.cs, walk-forward arm (b) tunable variant (WRITTEN, not compiled, not run)
```

**E9. Noise checks (crossover non-roll residue, order-flow delta, technical-analysis supplement)**
```
$ /usr/bin/grep -r -h -i -E "cross-?overs?|crosses (above|below)" docs + ledgers | /usr/bin/grep -v -i -E "roll|/OI|vol\+oi|volume|open interest"
2. In **"Available"**, select the strategy → add ... `PraxisNoiseAreaBreakout`, `PraxisSignalConsumer`, Sample ATM, Sample MA crossover, Sample multi
  ATM strategy, Sample MA crossover, Sample multi-instrument, Sample
| l | "all 8 crossovers fell on the Monday of expiry week" (line 99) | NARROWED | see below |
- If **no** crossover exists in the overlap → `StitchError` (flag loudly; do not guess a date).
   (4 further stitch-prose lines)
$ ... -w delta ... | /usr/bin/grep -i -E "(volume|bid|ask|order|cumulative|footprint)[ -]+delta|delta[ -]+(volume|bid|ask)" | wc -l
       1
   (the one line: DECISION_LOG.md:34, a 2026-07-15 bracket-incident row; not an order-flow/delta indicator)
$ grep -c "technical (analysis|indicator)|chart pattern|price action" docs specs vm ninjascript scripts + ledgers | grep -v ':0$'
docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md:1
```
In E9, "(4 further stitch-prose lines)" stands in for four omitted output lines. The DECISION_LOG.md:34 note is my reading of that line, not output.

**E10. De-identification check (run on this file before finishing)**
```
$ grep -c -i -w "$(ls /Volumes/Sensidine/Praxis.build/docs/reports | grep '^2026-10-28-f4-' | head -1 | sed 's/^2026-10-28-f4-//; s/-.*//')" /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-strategy-review-index-worker3.md
0
```

## Gaps

- **Not checked:** which exit mode each recorded Strategy Analyzer run of `PraxisNoiseAreaBreakout` used. The 2026-11-01 results report maps a CSV to `PraxisNoiseAreaBreakout` at `:41`, but I did not verify that run's ExitMode. "VWAP exit was backtested" is therefore UNVERIFIED here.
- **Arm (b) status is as of the STATUS card I read** (lines 192/194, the 2026-11-07 evening section), plus the branch commit subject. I did not search every later DECISION_LOG/HANDOFF row for a compile or run of arm (b).
- **Code greps covered the `main` working tree only.** `PraxisNoiseAreaBreakoutArmB.cs` lives on `origin/arm-b/wf-tunables` and was not grepped (only its commit subject was read).
- **Untracked reports were included.** `docs/reports` on disk includes untracked files, so the docs/reports counts reflect the working tree, not HEAD.
- **Redemtion conversion:** counts come from `textutil`/`pdftotext` output. RTF escape sequences (e.g. `\'97`) remain in some converted .md text, so a term split by an escape would be missed. The one PDF converted to 824 lines; its layout fidelity was not checked.
- **Count definition:** the counts are matching LINES, not occurrences.
  - `-w` on BSD grep 2.6.0-FreeBSD treats `.` and `_` differently from GNU grep in edge cases. This is UNVERIFIED for this corpus.
  - ATR, VWAP, delta and indicator counts include non-strategy uses (oracle tests, spec prose, plot names, numeric deltas). Only the hits quoted above were classified. The remaining ATR (198 reports / 53 ledgers) and VWAP (687 reports) lines were not read one by one. They were attributed to Noise-Area internals and arm (b) on the basis of the per-file distribution, not line-by-line reading. That attribution is an inference.
- **Searched but not quoted:** the `docs/reports` "indicator" hits (46, spread over 25 files, Evidence in transcript). Apart from `…strategy-research.md` (4) I did not open them. The file names are grading, connection, NT8 reference and build-variant reports, which suggests non-strategy use, but that is not verified.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
