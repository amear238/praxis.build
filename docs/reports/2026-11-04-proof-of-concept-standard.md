# What "proof of concept" means before spending money — Brief C

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

- **Date:** 2026-11-04 · **Unit:** `2026-11-04-proof-of-concept-standard` · **Grade:** UNGRADED at time of writing (the audit has not run)
- **Scope:** Brief C of `docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md` (sha256 `4c115d0382c571487ce2c249c34aa533d8330ba9454c283c7bdeee3312059980`). Amear: "Run these briefs". Briefs A and B were not done and not read.
- **Author:** praxis-manager, with workers R1, T1, T2, L2, L3, F1, F2 and Q1 (see Process log). Research only. No purchase, no sign-up, no import, no NinjaTrader run, no repo code change. Nothing staged.
- **Grades:** OBSERVED = read this session from a fetched source, a repo file or pasted output · INFERRED = reasoning, basis stated · UNVERIFIED = not checked. **"Claude's arithmetic"** = computed by a script in this unit; the inputs, formula and pasted output are shown.
- **Scratch root** (machine-local, not in the repo): `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/` (below: `SP/`). Worker notes: `SP/out-C/*.md`. Fetched sources: `SP/research-C/`.

## Summary

1. On Standard-resolution minute data, R0's edge is statistically distinguishable from zero on most tests. The per-trade t is 2.63, the PF 95% interval is [1.08, 1.54] (iid) or [1.12, 1.46] (month blocks), and PSR(0) is 0.999. It is not distinguishable from a Sharpe of 1.0: PSR(SR*=1.0) = 0.67. The edge is concentrated: without the top 20 of 1,190 trades, PF is 1.02. All of this is Claude's arithmetic.
2. The deflated Sharpe depends on the trial count N and the spread across trials V, and both are Amear's to set. It ranges from 0.9985 to 0.0001 across the table. The example case used here (N=4, V from R0–R3) gives 0.62.
3. The 250-OOS-trade gate is looser than the statistics. At R0's edge, 250 trades give t = 1.20. The OOS PF ≥ 1.30 gate is stricter than R0's own in-sample PF: an OOS sample drawn from R0's trades passes it about 47% of the time.
4. Five of the six gates (OOS PF, OOS Sharpe, OOS trades, % windows profitable, WFE) cannot be evaluated without walk-forward. The 4% drawdown gate has no equity base in the repo. The Sharpe gate has no stated periodicity.
5. For the strategy as coded, tick data is a refinement (INFERRED; untested in NinjaTrader). Every order is a market order decided on bar close, and the 1-minute data reproduces all 2,380 fills (T2's notes; I re-ran its 1,891 and 60 counts). Tick data becomes a prerequisite once a resting stop or target exists, which would include breakers built as resting stops (R-1104-3's judged version has breakers on).
6. One issue was found outside the brief's question: the 1-minute data has about 32 missing RTH sessions, and the session template closes early-close days at 12:15. Tick data fixes neither (T2).
7. The PROPOSED checklist has two tiers: before buying data, and before forward trading. It is a proposal only. The definition is Amear's (R-1104-3).

## Answers

### 1. Minimum sample — how much is enough at ~225 trades/year

**What the sources say (OBSERVED unless marked):**
- **Bailey, Borwein, López de Prado & Zhu, *Pseudo-Mathematics and Financial Charlatanism*** (Notices AMS 2014; PDF p.11, Thm 3.1). MinBTL ≈ ( [(1−γ)Z⁻¹(1−1/N) + γZ⁻¹(1−1/(N·e))] / E[max_N] )², with the bound < 2 ln N / E[max_N]². Worked example: "if only 5 years of data are available, no more than 45 independent model configurations should be tried". They also write: "MinBTL should be considered a necessary, non-sufficient condition". The formula is a transcription of mangled pdftotext math, so the transcription is INFERRED. Q1 confirmed both quotes verbatim on PDF p.11 (L2 had cited pp.10–11).
- **Bailey & López de Prado, *The Deflated Sharpe Ratio*** (JPM 2014; Snippet 1). The code line `maxZ=(1-emc)*ss.norm.ppf(1-1./numTrials)+emc*ss.norm.ppf(1-1./(numTrials*np.e))` with `emc=0.5772156649` is OBSERVED. The worked example says "only a 90% chance that the true SR ... is greater than zero", and that "after running only N=46 independent trials ... [DSR] would have been 0.9505". Q1 confirmed these. The text also says "not a legitimate empirical discovery at a 95% confidence level". The paper states PSR comes from Bailey & López de Prado [2012a]. I did **not** fetch that 2012 paper, so the PSR and MinTRL forms below are standard forms, UNVERIFIED against their primary source. The DSR form is checked by the positive control below.
- **Harvey, Liu & Zhu (RFS 2016):** "a newly discovered factor today should have a t-statistic that exceeds 3.0", "(which corresponds to a p-value of 0.27%)", and "a t-statistic of 2.0 is no longer appropriate". The paper is about cross-sectional equity factors. Applying the threshold to one futures strategy is INFERRED.
- **Lo (2002)** iid SE of the Sharpe ratio: not fetched. The formula √((1+½SR²)/T) is UNVERIFIED against the source.

**Positive control: my DSR code reproduces the paper's printed values** (inputs N=100, V=½ annualised, T=1250, skew −3, kurtosis 10, SR 2.5 annualised; these inputs are glyph-lost in pdftotext and are taken as the commonly cited ones, so they are INFERRED. Their reproducing the printed 0.9505 and the "90%" is the check):
```
$ python3 -I SP/scripts-C/dsr_control.py
N=100 skew=-3 kurt=10 SR0d=0.1132 SR0ann=1.7894 DSR=0.9004
N=46 skew=-3 kurt=10 SR0d=0.1004 SR0ann=1.5869 DSR=0.9505
N=88 skew=0 kurt=3 SR0d=0.1111 SR0ann=1.7574 DSR=0.9505
N=100 skew=0 kurt=3 SR0d=0.1132 SR0ann=1.7894 DSR=0.9428
```
Q1 read the rendered PDF page 10 and found "(γ̂₃=0, γ̂₄=3), DSR = 0.9505 after N=88". That matches line 3.

**Input file:** R0 = `$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv`. R1–R3 are the 07-57, 07-59 and 08-00 files (machine-local, read-only). Gate 0 reproduces the baseline.

**Claude's arithmetic:** `SP/scripts-C/a1.py`, sha256 `f47ecb7b5ff8c0b8970f34534c510811c3022898b4ae439d0629b617c0dcfbef`. Excerpt of its output, verbatim from `SP/out-C/a1-output.txt`:
```
R0 sha256=421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd trades=1190
[0] R0 net=197327.60 PF=1.2897 maxDD=-45282.04
GATE0 MATCH
[1] per-trade n=1190 mean=165.8215 sd=2178.8675 skew=4.9899 kurt(non-excess)=67.9242 excess=64.9242
    t=2.6253 PF=1.2897 winrate=0.4067 span_years=5.2950 trades/yr=224.74
    R0 allweekdays T=1383 SRd=0.07363 SRann=1.1689 skew=3.9492 kurt=50.0703
    R1 allweekdays T=1383 SRd=0.06129 SRann=0.9730 skew=2.0383 kurt=40.9604
    R2 allweekdays T=1383 SRd=0.07257 SRann=1.1520 skew=4.0718 kurt=53.9081
    R3 allweekdays T=1399 SRd=-0.05700 SRann=-0.9048 skew=-0.7035 kurt=7.5188
[3] Lo iid allweekdays SE_d=0.02693 SRann=1.1689 CI95ann=[0.3311, 2.0067]
[4] PSR(0) allweekdays = 0.999058
[5] MinTRL allweekdays z=1.645 SR*=0 = 388.1 days = 1.54 yrs (have 1383 obs = 5.49 yrs)
[5] MinTRL allweekdays z=1.645 SR*=1.0ann = 18539.9 days = 73.57 yrs (have 1383 obs = 5.49 yrs)
[5] MinTRL allweekdays z=1.960 SR*=0 = 550.6 days = 2.18 yrs (have 1383 obs = 5.49 yrs)
[4b] PSR(SR*=1.0ann) allweekdays = 0.673333
[6] DSR allweekdays  (sqrtV annualised: R0-R2=0.1085, R0-R3=1.0053, sdAnn0.5=0.5000, sdAnn1.0=1.0000)
    N   emax   R0-R2               R0-R3               sdAnn0.5            sdAnn1.0
    2   0.5198 SR0a=0.056 DSR=0.9985  SR0a=0.523 DSR=0.9572  SR0a=0.260 DSR=0.9922  SR0a=0.520 DSR=0.9578
    4   1.0521 SR0a=0.114 DSR=0.9975  SR0a=1.058 DSR=0.6163  SR0a=0.526 DSR=0.9563  SR0a=1.052 DSR=0.6219
    10  1.5746 SR0a=0.171 DSR=0.9960  SR0a=1.583 DSR=0.1355  SR0a=0.787 DSR=0.8449  SR0a=1.575 DSR=0.1404
    20  1.9007 SR0a=0.206 DSR=0.9948  SR0a=1.911 DSR=0.0243  SR0a=0.950 DSR=0.7194  SR0a=1.901 DSR=0.0258
    100 2.5306 SR0a=0.275 DSR=0.9913  SR0a=2.544 DSR=0.0001  SR0a=1.265 DSR=0.3989  SR0a=2.531 DSR=0.0001
[7] MinBTL allweekdays E[max_N]=SRann=1.1689 ; sample=5.30 yrs
    N=4   MinBTL=0.810 yrs  bound 2lnN/E^2=2.029 yrs
    N=10  MinBTL=1.815 yrs  bound 2lnN/E^2=3.370 yrs
    N=100 MinBTL=4.687 yrs  bound 2lnN/E^2=6.741 yrs
[8a] iid bootstrap PF p2.5=1.0801 p50=1.2885 p97.5=1.5378 P(PF<=1)=0.0023
[8b] month-block bootstrap (65 months) PF p2.5=1.1177 p50=1.2903 p97.5=1.4646 P(PF<=1)=0.0004
[8c] OOS n=250 P(PF>=1.30)=0.4692 P(PF>1.0)=0.8952
[8c] OOS n=1000 P(PF>=1.30)=0.4666 P(PF>1.0)=0.9946
    z=1.960 n=663 trades = 2.95 yrs
    z=3.000 n=1554 trades = 6.91 yrs
```
The table rows for N = 3, 5 and 50, and the trade-days-only calendar, are in the full file.

**Assumptions** (stated, not decided):
- (a) **Calendar.** Daily P&L is by exit date on every weekday, with zero on no-trade days. Holidays are not removed. R1 measured the effect: removing the full NYSE holiday list moves the annualised SR from 1.1689 to 1.1907, so leaving holidays in is slightly conservative. The trade-days-only calendar annualised by √252 overstates SR by about 30%, because R0 has 149.6 trade days a year. R1 found this; it is shown only in the full file and not used.
- (b) **rf = 0, dollar P&L, one contract.**
- (c) **Trial count N.** Ten Strategy Analyzer runs are on record, with four distinct strategy logics and **no optimisation or sweep** (F2: a grep found none; F2 grades the run count as INFERRED, since the record holds only runs Amear reported). The published strategy's authors explored 8 lookbacks, a band-width sweep and 3–4 stop and sizing variants (L3, from the paper). Whether any of these count as trials is **Amear's**. The example case used in the Summary (N=4, the four logics, with V from R0–R3) is one row of the table, not a decision. Reading across the table: with V from the near-duplicate R0–R2, DSR stays ≥ 0.99 for all N. With V from R0–R3, DSR is 0.96 at N=2, 0.62 at N=4 and 0.14 at N=10.

**Independent re-computation (worker R1, ADVERSARIAL).** R1 wrote its own code and did not see a1.py. Its final message reported 64/64 MATCH with 0 mismatches, and the largest bootstrap gap was 0.4569 against 0.4666. The grep counts of R1's notes file are pasted in Verification evidence; the 64 is R1's own count and was not re-counted by me. I re-ran R1's script myself, and the output was identical to R1's saved output:
```
$ python3 -I r1_indep.py > M-rerun-r1.txt; diff (rerun) (R1-output.txt)
exit=0
(no diff lines)
```
R1's extra checks (re-run by me):
```
net without top 5 trades: 111367.40 PF 1.1635
net without top 10 trades: 74752.20 PF 1.1097
net without top 20 trades: 12796.80 PF 1.0188
iid-day bootstrap SE_d 0.024118 (Lo 0.026926, nonnormal 0.023692); CI95 ann pct [0.3856, 1.8835]; P(SR<=0) 0.0019
month-block bootstrap SE_d 0.020240 CI95 ann pct [0.5132, 1.7780] P(SR<=0) 0.0002
lag1 autocorr daily -0.0871
```

**Answer to item 1 (Claude's arithmetic):**
- **Mean trade.** At R0's mean and sd, telling the mean trade apart from zero takes **663 trades at z=1.96** and **1,554 trades (6.9 years) at the Harvey–Liu–Zhu t=3.0 hurdle**. R0 has 1,190 trades with t = 2.63: past 1.96, short of 3.0.
- **Sharpe ratio.** Telling the Sharpe apart from 0 takes 1.5–2.2 years (MinTRL), and R0 has 5.5. Telling it apart from a Sharpe of 1.0 takes **74 years**. The 95% CI on the annualised Sharpe is [0.33, 2.01] (Lo iid; non-normal [0.43, 1.91]; bootstrap [0.39, 1.88]).
- **MinBTL** for N ≤ 100 is at most 4.7 years (approximation). The sample is 5.3 years. That is necessary, not sufficient.
- **Concentration.** PF falls to 1.02 without the top 20 trades (1.7% of trades).
- **OOS windows.** The spec's walk-forward is 252-day IS, 63-day OOS, 63-day step (F1, spec text). On this span that gives about 17 windows, about 1,071 OOS days and about 955 OOS trades:
```
$ python3 -I SP/scripts-C/m_extra.py
per-trade SR=0.07610
t at n=250 trades = 1.203
t at n=500 trades = 1.702
t at n=955 trades = 2.352
t at n=1190 trades = 2.625
approx trading days=1335 ; WF windows (252 IS/63 OOS/63 step)=17.2 ; OOS days=1071 ; OOS trades at 0.8918 trades/day=955
```
  The trading-day count assumes about 9 holidays a year. At R0's edge, the ~955 pooled OOS trades would give t ≈ 2.35.

### 2. The Phase 3 gates against the literature

**Where the gate text lives.** The text is OBSERVED in the de-identified spec import on branch `parked/Praxis_build-r8j` (commit f258a5d) and in the gitignored local RTF. It is not on main. F1 pasted (from `git show f258a5d:docs/specs/2026-08-06-phase3-build-specification.md`):
```
67:Pass gates (non-negotiable):
69:- OOS profit factor ≥ 1.30
70:- OOS Sharpe ≥ 1.0
71:- Max drawdown ≤ 4% of equity
72:- ≥ 250 aggregate OOS trades
73:- ≥ 60% of walk-forward windows profitable
74:- Walk-forward efficiency ≥ 0.50
91:6. Trailing drawdown proximity — account approaches MFFU’s $1,500 EOD trailing drawdown → reduce size or halt
```
The spec is not imported (bead r8j), so this report treats these values as stated in the brief; they match the parked text. The gate set for the version being judged is still open: D-2026-11-02-C NEEDS AMEAR 1–2, `DECISIONS.md:531-532`, and rubric O1, `specs/SPEC_RUBRIC.md:74-79`.

| Gate | What the sources read here say | Compared with the literature | Needs walk-forward? |
|---|---|---|---|
| OOS PF ≥ 1.30 | No paper or vendor document read gives a PF threshold (absence, among the sources read). The gitignored research input calls it "no edge after slippage/commission noise" (F1; local only, UNVERIFIED). | **Stricter than R0's own IS PF.** If R0's edge were true, a 250-trade OOS sample passes about 47% of the time (8c), and 46.7% at n=1000. INFERRED: the published OOS decay (below) would lower that. | Yes |
| Sharpe ≥ 1.0 | Periodicity and risk-free rate not stated (F1 A2). Harvey & Liu 2015: the haircut is "at most 25%" when SR > 1.0; 50% is "generally considered the industry standard". Quantpedia: mean IS Sharpe 1.574 across 417 strategies; L3 reports a 33% mean and 44% median OOS decline (OBSERVED by L3, not re-checked by Q1). | No source gives 1.0 as a threshold. R0's IS SR 1.17 after a 25/33/44/50% haircut is 0.877/0.783/0.655/0.584 (Claude's arithmetic, m_extra.py, pasted in Verification evidence). PSR(SR*=1.0) = 0.67. | OOS version: yes |
| Max DD ≤ 4% of equity | No equity base in the repo (F1 A3, absence by grep). The only dollar figure is the spec's "MFFU's $1,500 EOD trailing drawdown". | No literature threshold was found. R0's maxDD of $45,282 implies $1,132,051 of equity at 4% (a1.py [10]), and is 30.2× the $1,500 trailing DD (m_extra.py). Intratrade DD from MAE is about −$48,657 (R1). | Can be computed IS; the gate's IS/OOS scope is unstated |
| ≥ 250 OOS trades | — | **Looser than the statistics.** 250 trades at R0's edge give t = 1.20, while 663 are needed for t = 1.96 (Claude's arithmetic). | Yes |
| ≥ 60% windows profitable | No source read gives this. | Descriptive IS only (not walk-forward): 17/23 quarters and 9/12 halves positive. Full periods only: 16/21 and 8/10. Both of the last two halves are negative (R1). | Yes |
| WFE ≥ 0.50 | TradeStation WFO help: "As a rule of thumb, a Walk-Forward Efficiency of 50% or more is considered a measure of a successful walk-forward analysis" (L3; vendor document). Pardo's primary text was not reached. NT8's WFO page has no efficiency metric and no threshold (L2; Q1 notes L2's pasted count was 1 but is actually 2, and the finding holds). | Matches the one vendor rule of thumb found. It is undefined without an IS optimisation step (O1), and R0 has none. | Yes |

**What the literature has that the gates lack** (OBSERVED in the sources): a disclosed trial count, since "a backtest which does not report the number of trials N ... makes it impossible to assess the risk of overfitting" (Pseudo-Mathematics, Fig. 2 text); DSR/PSR; MinBTL; PBO via CSCV, where the authors write "a customary approach would be to reject models for which PBO is estimated to be greater than 0.05"; White's Reality Check and Hansen's SPA (abstract level; no numeric threshold); and a multiple-testing t-hurdle (HLZ 3.0).

### 3. Is tick data a refinement or a prerequisite?

**Findings (OBSERVED unless marked):**
- **Code.** Every order is a market order (`EnterLong`, `EnterShort`, `ExitLong`, `ExitShort`) under `Calculate.OnBarClose`. There is no `SetStopLoss`, `SetProfitTarget`, `SetTrailStop`, stop order, limit order or `AddDataSeries`. T1 found this and T2 confirmed it independently. Decisions happen only at HH:00/HH:30 (`.cs:196`). The paper's own rule is the same: "specifically at HH:00 and HH:30" (Zarattini et al., p9, L3).
- **NT8 vendor document** ("Understanding Historical Fill Processing", L2, confirmed by Q1). Standard resolution splits each bar into "three virtual bars". Slippage "is only applied to market, stop-market and Market-if-touched orders", and "you cannot have more slippage then the high/low price of the next bar".
- **Fill reproduction.** I re-ran T2's script against the 1-minute file `/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt` (sha256 `307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454`):
```
== K3 ==
  MKT:ref+2adverse 1891
== K4 ==
per extra tick/side $11900.00; base net 197327.60; +1 185427.60; +4 149727.60; breakeven extra ticks 16.58
== K6 ==
stop 20 / tgt 20: ambiguous 19/1190 = 1.60% (excl. entry bar: 6 = 0.50%); single-side resolved 1147
stop 40 / tgt 80: ambiguous 0/1190 = 0.00% (excl. entry bar: 0 = 0.00%); single-side resolved 861
stop 10 / tgt 10: ambiguous 101/1190 = 8.49% (excl. entry bar: 44 = 3.70%); single-side resolved 1088
stop 30 / tgt 30: ambiguous 4/1190 = 0.34% (excl. entry bar: 1 = 0.08%); single-side resolved 1091
stop 20 / tgt 40: ambiguous 2/1190 = 0.17% (excl. entry bar: 0 = 0.00%); single-side resolved 1131
```
  Of the 1,951 market fills, 1,891 are the next bar's open ±2 ticks against the trade. The other 60 sit at the bar's high or low, consistent with the vendor document's cap. T1 and T2 agree.
- **Literature.** Zarattini et al. used "1-minute ... data from IQFeed, covering the period from May 2007 to April 2024" (p6, L3). The repo's 08-07 research (UNGRADED) reached the same refinement view. T2 objects that its "should be identical" claim goes too far.

**Answer (INFERRED from the code, the vendor document and the reproduction; untested in NinjaTrader because no High run exists):**
- For this code, Standard-versus-High sequencing **cannot change which trades occur**. Only resting stop or limit orders are sequence-sensitive, and the code has none. Tick data can change three things:
  - (i) fill prices at the next-bar open;
  - (ii) the slippage cap. T2 objects that under High on a 1-tick series, the 2-tick slippage may cap to about zero, worth up to $23,800 in total (m_extra.py: 1190×2×2×$5). That is the forum-reported risk in the VM plan (UNVERIFIED);
  - (iii) session-close timing. For scale, the Flat1559 change moved net by −$4,310 (R2 net minus R0 net; m_extra.py prints R0−R2 = +4,310).
- Tick data becomes a **prerequisite** when the judged version contains a resting stop or target. Circuit breakers built as resting price stops would count; R-1104-3's judged version has breakers on, and whether they are resting stops is not defined (`DECISIONS.md` R-VN3-5). Tick data is also a prerequisite if Calculate changes to per-tick, or if the checkpoint rule is dropped.

**PROPOSED decision test.** It runs on the existing trade list plus the 1-minute file. The thresholds are Claude's proposals; no source gives them.
- **T-a.** Count resting-order fills in the judged version (code grep plus fill minutes). If zero, go to T-b and T-c only. If nonzero, run T-d.
- **T-b.** Share of market fills that equal next-bar open ± modelled slippage. If ≥ 95%, the minute model is mechanically explained. Now: 1,891/1,951 = 96.9%, plus 60 capped.
- **T-c.** Break-even extra adverse slippage. Now 16.6 ticks/side against 2 modelled. Report it; the acceptable level is Amear's.
- **T-d.** With brackets: the share of trades where one 1-minute bar touches both levels before either is touched alone. Below 1% = refinement, ≥ 1% = prerequisite. A 20/20-point bracket gives 1.60% (0.50% excluding the entry bar), 10/10 gives 8.49%, and 40/80 gives 0%.

**Data issues found (T2, OBSERVED by T2 from the 1-minute file; I re-ran only the K2–K6 lines).** About 32 weekdays have no RTH data (T2 marks its holiday calendar UNVERIFIED), including long gaps on 2021-09-10..09-24 and 2025-12-15..12-31. Five early-close session exits sit at 12:15, which T2 reads as an hour before the file's last trading bar. The exit at 14:03 on 2023-04-05 falls on a data hole (T2 notes line 276: no bars 14:04–20:00 on a normal Wednesday). Tick data from the same pipeline may share the gaps (UNVERIFIED).

## PROPOSED checklist — candidate definition of "proof of concept" for R-1104-3

**PROPOSED, not decided.** Amear accepts, edits or rejects each item and each threshold. Tier A = before buying higher-resolution data. Tier B = before forward or paper trading. Where the cell says so, a threshold is Claude's proposal and no source gives it.

| # | Tier | Item | Source | R0 now (Claude's arithmetic or observed) |
|---|---|---|---|---|
| P1 | A | The trade list reproduces from the data file, and data holes and the session template are listed and fixed or accepted | Project evidence (T2); no literature source | 2,380/2,380 fills reproduce. ~32 missing sessions; 12:15 early closes |
| P2 | A | The trial count N and the cross-trial V are disclosed and fixed by Amear | Bailey et al. 2014 (Pseudo-Math, Fig. 2 text) | Not fixed (NEEDS AMEAR 1) |
| P3 | A | DSR ≥ 0.95 at Amear's N and V | Bailey & López de Prado 2014 (95% confidence level in their example) | 0.0001 to 0.9985 across the table; 0.62 at N=4 with V from R0–R3 |
| P4 | A | Sample length ≥ MinBTL at N ("necessary, non-sufficient") | Bailey et al. 2014 Thm 3.1 | 5.3 years against ≤ 4.7 years for N ≤ 100: meets |
| P5 | A | Per-trade t ≥ 3.0 (or ≥ 2.0 with a stated first-principles reason) | Harvey, Liu & Zhu 2016 (transfer INFERRED) | 2.63: meets 2.0, misses 3.0 |
| P6 | A | Month-block bootstrap PF 2.5th percentile > 1.0 | Bootstrap method as in White 2000 (abstract level); threshold PROPOSED | 1.12: meets |
| P7 | A | Edge survives the cost stress: break-even extra slippage ≥ k ticks/side (k is Amear's) | Zarattini et al. ran cost sensitivity (Kissell model, p36–37, L3) | 16.6 ticks/side |
| P8 | A | The item-3 test (T-a to T-d) is run on the judged version | NT8 fill-processing document | T-a = 0 resting orders now; the breakers are undefined |
| P9 | A | Concentration: PF without the top 1–2% of trades > 1.0 | No source (PROPOSED; Amear may drop it) | 1.02 without the top 20: above 1.0 by 0.02 |
| P10 | B | Walk-forward (252/63/63 per spec; on minute data or under High, per NEEDS AMEAR 11) passes the spec's OOS gates as Amear rules on them (O1) | Phase 3 spec (parked); TradeStation WFE ≥ 50% rule of thumb; NT8 WFO document | Not run (r8j blocker) |
| P11 | B | If any optimisation is run: PBO < 0.05 | Bailey et al., PBO paper §3.1 ("customary approach") | No optimisation run yet |
| P12 | B | Forward test of at least 6 weeks or 25 trades, spanning an FOMC day, an NFP day and a rollover | Phase 3 spec (F1: local RTF line 59) | Not started |

## 5. Cost of being wrong — facts only

- **What the $695 buys.** Portara/CQG trades-only ticks as individual NinjaTrader-format contract files, 2014 to present, $695 flat. 23 contracts cover 2021-03 to 2026-07. The licence is not published. All of this is REPORTED in `docs/reports/2026-11-02-vm-high-res-plan.md` (VM agent read Portara 2026-11-02) and was not re-checked here (F1 C1). Amear declined it on 2026-11-03 and set R-1104-3.
- **What a High run requires:** the imported tick data, the TickPrep build, and a High/Tick fill-resolution run. NT8 cannot build ticks from 1-minute data (VM plan lines 25–28, F1).
- **What a High run can change for the current code.** Fill prices at the next-bar open, the slippage cap and session-close timing; not which trades occur (item 3, INFERRED, untested). The dollar scales measured on the current trade list:
  - total modelled slippage $23,800;
  - $11,900 per extra tick per side;
  - break-even at 16.6 extra ticks per side;
  - the one session-close timing change already run (Flat1559) moved net by −$4,310 (R2 minus R0).
- **What walk-forward on minute data requires.** The spec's backtest sentence specifies "Order Fill Resolution = High, 1-tick resolution series" and optimises a stop-ATR multiplier (F1, spec text line 30). A minute-data walk-forward departs from that sentence. Under item 3, an optimised stop would make tick data a prerequisite. Whether a minute-data walk-forward is acceptable is Amear's (NEEDS AMEAR 11). If it is run on minute data, it needs no data purchase. It does need the r8j spec import (parked), the O1 gate-set ruling, and, if WFE applies (NEEDS AMEAR 6), an optimisation arm. The spec windows give about 17 OOS windows and about 955 OOS trades (Claude's arithmetic). Circuit breakers are not built (R-VN3-5).
- **Things neither path fixes.** The data holes and the session template (T2).
- **Recent-period figures.** Zarattini et al.'s own table shows 2025 (Jan–Aug) at +1.0% against 24–37% a year in 2020–2024 (L3). R0's PF by exit year is 1.106 for 2025 and 0.970 for 2026 (a1.py [11], pasted in Verification evidence).
- **R-1104-3** names the judged go/no-go version as High fill resolution with breakers on. Its words: *"if the high fill resolution costs $700 for the data, I'm not going to pay that right now until there's proof of concept."*

## Sources (all read 2026-11-04 unless noted)

| Source | URL | Reached | Fetched by |
|---|---|---|---|
| Bailey & López de Prado, The Deflated Sharpe Ratio (JPM 2014), sha256 ca4a1e83…d10b5 | https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf | full text | manager |
| Bailey et al., Probability of Backtest Overfitting, sha256 d8bfbada…a63d | https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf | full text | manager |
| Bailey et al., Pseudo-Mathematics and Financial Charlatanism (Notices AMS 2014), sha256 6e790c41…0f3e | https://www.davidhbailey.com/dhbpapers/backtest-pseudo.pdf | full text (AMS URL 403) | L2 |
| Harvey & Liu, Backtesting (JPM 2015), sha256 b32ec2e9…f02f | https://people.duke.edu/~charvey/Research/Published_Papers/P120_Backtesting.PDF | full text | L2 |
| Harvey, Liu & Zhu, …and the Cross-Section (RFS 2016), sha256 15e407e3…bf | https://people.duke.edu/~charvey/Research/Published_Papers/P118_and_the_cross.PDF | full text | L2 |
| White (2000), A Reality Check for Data Snooping, sha256 675eb322…3a9743 | https://www.ssc.wisc.edu/~bhansen/718/White2000.pdf | full text, third-party course copy; abstract quoted | L2 |
| Hansen (2005), SPA, sha256 e6f45856…1d | https://cdr.lib.unc.edu/downloads/zp38wf793 | full text, university repository copy (Q1: grade caveat) | L2 |
| Zarattini, Aziz & Barbon, Beat the Market (rev. 2025-09-22), sha256 865010df…6ebb | https://concretumgroup.com/wp-content/uploads/2026/02/Beat-the-Market.pdf | full text, author-firm copy, revised version | L3 |
| Chuk (2026), Noise-band Intraday Momentum in Nasdaq-100 Futures | https://api.crossref.org/works/10.2139/ssrn.7609644 | **abstract only**, not peer-reviewed, no sha recorded | L2 |
| NinjaTrader 8 Help: Walk Forward Optimization | https://ninjatrader.com/support/helpGuides/nt8/walk_forward_optimize_a_strate.htm | full page, no sha recorded | L2 |
| NinjaTrader 8 Help: Understanding Historical Fill Processing | https://ninjatrader.com/support/helpGuides/nt8/understanding_historical_fill_.htm | full page, no sha recorded | L2 |
| NinjaTrader 8 Help: Historical Order Backfill Logic | https://ninjatrader.com/support/helpguides/nt8/historical_order_backfill_logic.htm | full page, no sha recorded | L2 |
| TradeStation WFO help: Walk-Forward Summary (Out-of-Sample), sha256 8b40054f…5a9a | https://help.tradestation.com/09_01/tswfo/topics/walk-forward_summary_out-of-sample.htm | full page | L3 |
| Quantpedia, In-Sample vs. Out-Of-Sample Analysis of Trading Strategies (page dated 2 June 2023) | https://quantpedia.com/in-sample-vs-out-of-sample-analysis-of-trading-strategies/ | full page | L3 |
| Quantpedia, From Backtest to Benchmark (page dated 27 July 2026) | https://quantpedia.com/from-backtest-to-benchmark-validating-new-strategies-with-quantpedia-api/ | full page | L3 |
| Repo: DECISIONS.md D-2026-10-30-A, D-2026-11-02-C, D-2026-11-04-A; VM high-res plan; parked spec f258a5d; `ninjascript/PraxisNoiseAreaBreakout*.cs` | (repo) | read | F1, F2, T1, T2, manager |

**Not reached:** Bailey & López de Prado 2012 (PSR and MinTRL primary); Lo 2002; Pardo 2008 (Google Books 429, Wiley 403); SSRN pages (403 to curl).

## Leads not confirmed

- Pardo's WFE definition (Ch. 11, pp. 256/260) and the claim that "0.3/0.5/0.7 bands do not appear in Pardo". Source: Tradelyze vendor blog (https://tradelyze.io/learn/walk-forward-efficiency/); not checked against the book.
- "TradeStation pass with distinction at 100%": not seen on a TradeStation page (L3).
- An NT staff forum post saying slippage applies only under Standard. Cited in the VM plan line 28; UNVERIFIED; a forum lead only.
- Two 2026 SSRN papers that independently replicate or test the Zarattini strategy: Delgado (doi 10.2139/ssrn.7323419) and Paz (doi 10.2139/ssrn.7290621). Titles only.
- Chuk's abstract: "one of two survivors among 144 preregistered tests", daily Sharpe 1.14, and "1 index point slippage on stop fills removes 22% of edge". Abstract only; full text not read.
- The gitignored research input (`Redemtion/.../compass_artifact...md`) defines WFE = OOS PF / IS PF as "Pardo's classic test". Local only, UNVERIFIED.

## NEEDS AMEAR

1. Which runs, variants and published-author choices count as trials (N), and which runs give V, for DSR and MinBTL.
2. The equity base for "max DD ≤ 4% of equity" (account size; how the MFFU $1,500 EOD trailing DD relates to it).
3. The Sharpe definition for the gate: daily or per-trade, annualisation, risk-free rate.
4. Accept, edit or reject each PROPOSED checklist item, its tier and its threshold (k in P7; the 1% and 95% cut-offs in item 3).
5. Whether Tier A alone is the R-1104-3 purchase condition.
6. O1, already open: the gate set for the replication arm, and whether WFE applies with no optimisation.
7. Whether the data holes and the 12:15 early-close template are fixed before results are judged.
8. Whether the $2.96 round turn is meant to include exchange, clearing and NFA fees (the export shows $0 for those).
9. Whether the r8j circuit breakers are resting price stops; if so, tick data becomes a prerequisite (item 3).
10. Any purchase of Pardo's book to check the primary WFE text.
11. Whether a walk-forward on minute data is acceptable as Tier B. The spec's backtest sentence names High resolution, a 1-tick series and an optimised stop-ATR multiplier; a stop is a resting order, which item 3 says makes tick data a prerequisite.

## Process log

- **Concurrency.** The first five dispatches failed with "Concurrent subagent limit reached" (the sibling A and B units were holding slots). **Deviation:** the manager wrote and ran the arithmetic script (a1.py, dsr_control.py, m_extra.py) and fetched the two Bailey PDFs. R1 then independently recomputed every a1.py figure without seeing the script. m_extra.py was not independently recomputed; it is simple arithmetic on pasted inputs.
- **Workers dispatched** (mode → outcome):
  - R1 ADVERSARIAL recompute → DONE, 64/64 MATCH
  - L2 BUILD literature → hit the 40-turn cap with its notes written (A–J)
  - T1 BUILD item 3 → DONE
  - F1 BUILD repo facts → hit the 40-turn cap with notes A and C written; B and D missing
  - L3 BUILD gap-fill → PARTIAL (Pardo not reached)
  - F2 BUILD gap-fill for B and D → DONE
  - Q1 ADVERSARIAL quote check on L2 and the DSR claims → DONE (39 confirmed, 4 altered, 1 grade overclaim, 4 hash gaps, 0 not found)
  - T2 ADVERSARIAL on T1 → DONE (K2 partly refuted: the early-close detail; K3 label corrected)
- **Not adversarially re-checked:** L3's quotes (Zarattini, TradeStation, Quantpedia) and F1/F2 repo facts beyond what the manager re-grepped. This report has not been graded.

## Verification evidence

Additional pasted output (verbatim file `SP/out-C/M-evidence-block.txt`, built by redirecting the commands shown):
```
$ python3 -I SP/scripts-C/m_extra.py   (full output)
per-trade SR=0.07610
t at n=250 trades = 1.203
t at n=500 trades = 1.702
t at n=955 trades = 2.352
t at n=1190 trades = 2.625
approx trading days=1335 ; WF windows (252 IS/63 OOS/63 step)=17.2 ; OOS days=1071 ; OOS trades at 0.8918 trades/day=955
IS SRann 1.1689 haircut 25% -> 0.877
IS SRann 1.1689 haircut 33% -> 0.783
IS SRann 1.1689 haircut 44% -> 0.655
IS SRann 1.1689 haircut 50% -> 0.584
modelled slippage total = 1190*2 sides*2 ticks*$5 = 23800.00
R0-R2 net diff = 4310.00
MFFU $1,500 trailing DD vs R0 maxDD 45282.04 = 30.2x

$ grep -n "^\[10\]\|equity=\|^\[11\]\|year:\|half:\|quarter:\|  202[0-9] n=" SP/out-C/a1-output.txt
92:[10] implied equity for DD<=4%: 1132051.00
93:    equity=50000 DD%=90.56%
94:    equity=100000 DD%=45.28%
95:    equity=150000 DD%=30.19%
97:[11] descriptive sub-period profitability (exit date)
98:    year: 5/6 positive = 0.833
99:      2021 n=146 net=13557.84 PF=1.254
100:      2022 n=245 net=81034.80 PF=1.544
101:      2023 n=225 net=39829.00 PF=1.458
102:      2024 n=232 net=48603.28 PF=1.403
103:      2025 n=213 net=17454.52 PF=1.106
104:      2026 n=129 net=-3151.84 PF=0.970
105:    half: 9/12 positive = 0.750
106:    quarter: 17/23 positive = 0.739

$ grep -n -i "2380\|2,380\|capped\|60 " SP/out-C/T2-notes.md | head -6
123:  MKT:capped_at_extreme 60
125:  SC:capped_at_extreme 6
128:capped examples:
137:capped: open-to-extreme distance distribution Counter({0.0: 36, 1.0: 24})
270:**Same data as backtest?** — CONFIRMED (INFERRED, strong): every one of 2,380 fills reproduces exactly from the file under the rule "reference ± 2 ticks adverse, capped at bar high/low" (MKT 1891+60=1951; SC 423+6=429; 0 "other", 0 m
278:**K3 CONFIRMED with a wording error.** 1891 = open ± 2 ticks adverse; 60 at bar extreme (36 where open == extreme, i.e. 0 ticks slippage applied; 24 at 1 tick) — matches doc text: "you cannot have more slippage then the high/low pric

$ grep -n -i "MATCH" SP/out-C/R1-notes.md | head -4
52:R0 trade T=792 first 2021-03-29 last 2026-07-15 SRd(ddof1) 0.09748 SRd(ddof0) 0.09754 SRann 1.5474 skew g1 2.8818 G1 2.8873 kurt b2 28.4164 b2(sd1) 28.3447 tradeDays 792
56:R2 trade T=792 first 2021-03-29 last 2026-07-15 SRd(ddof1) 0.09606 SRd(ddof0) 0.09612 SRann 1.5248 skew g1 2.9764 G1 2.9821 kurt b2 30.6166 b2(sd1) 30.5393 tradeDays 792
104:z=1.96 n=663.27 ceil 664 yrs 2.95
125:quarters: [((2021, 1), 2, 164.0), ((2021, 2), 39, 10240.0), ((2021, 3), 48, -3472.0), ((2021, 4), 57, 6626.0), ((2022, 1), 66, 31430.0), ((2022, 2), 57, 38456.0), ((2022, 3), 62, 13466.0), ((2022, 4), 60, -2318.0), ((2023, 1), 62, 6606.

$ grep -n "14:03\|hole" SP/out-C/T2-notes.md | head -3
44:  early-close: 454 2023-04-05 14:03:00
204:  short day 2023-04-05 273 last RTH bar 14:03
276:- REFUTED: "429 session-close fills at 16:00 except 6 early-close days". Output: 423@16:00, 5@12:15, 1@14:03. 2023-04-05 is a normal Wednesday: the 14:03 exit is a **data hole** (14:04–20:00 missing), not an early close. And the 5 gen

$ grep -c "| MATCH\|MATCH |\|: MATCH\| MATCH$" SP/out-C/R1-notes.md ; grep -c "MISMATCH" SP/out-C/R1-notes.md
19
1
160:TOTAL: 64 MATCH, 0 MISMATCH, 0 CANNOT-CHECK.
```
Pasted in place above: a1.py output with gate 0 MATCH; the dsr_control.py positive control; the R1 rerun diff (empty); r1_extra.py; the t2.py rerun; m_extra.py. There is no gate in this unit. S3 (negative test) does not apply to a research report; the closest equivalent is the DSR positive control against the paper's printed 0.9505.

## Adversarial findings folded in

- From R1: the trade-days calendar is invalid (not used); intratrade DD; partial-period counts; fees at $0.
- From Q1: the MinBTL page is p.11; the NT8 count is 2, not 1; Hansen's grade carries a caveat; hashes are missing for some pages.
- From T2: 12:15 early closes, the 14:03 exit, ~32 missing sessions, and the High slippage-cap risk.
- From X1 (ADVERSARIAL on this report): nine defects. All are corrected in this version: the DSR range, 5 of 6 gates, dropped grades, the 14:03 explanation, the minute-data walk-forward versus the spec's High/stop-ATR sentence (now NEEDS AMEAR 11), pasted output for the derived figures, the R2−R0 sign, the 0.655 haircut and the P9 wording. Not re-checked by X1 after the fixes.

## S6 cross-block check

This report changes no block. It reads Block 2 (gates, walk-forward), F3 (fill resolution; the D-2026-10-30-A void clause is untouched and F3 stays FROZEN) and the breaker spec (r8j). It proposes nothing that alters those; the checklist is PROPOSED for Amear.

## Files staged

None. Written: this report only (untracked). Scratch: `SP/scripts-C/`, `SP/out-C/`, `SP/research-C/`.

## Result

Result: PASS

This is the producer's claim, not a grade; it is subject to audit for the five answers and the PROPOSED checklist. **Missing:** primary text for Pardo, Lo 2002 and Bailey & López de Prado 2012; independent re-check of L3's quotes.

## Correction 1 (2026-11-04, after audit FAIL 1)

Lines 1–353 above are unchanged. This section corrects them where it says so. Where the two disagree, this section wins. The audit failed S1 only: *"Every claim in a report has pasted command output, not a description of output."* Each block below is the live output of the command shown in it. All blocks were regenerated in one run by `SP/corr-C-scripts/ev.sh`. `SP` stands for the session scratchpad `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad`. The scripts are in `SP/corr-C-scripts/`, and they open the data files read-only. Fetched web pages are in `SP/corr-C/`. Those pages were treated as untrusted data: they were parsed as text by `python3 -I` from outside that directory, and nothing in them was executed. No NinjaTrader run and no backtest were done.

### C1. "~32 missing RTH sessions" (Summary item 6, :178, checklist P1)

**The file.** It is the 1-minute file T2 used, as cited in T2's notes line 8.
```
$ shasum -a 256 "$M"; grep -n "NQCONTROW" $S/out-C/T2-notes.md | cut -c1-120
307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454  /Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt
8:307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454  /Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.
```
**Weekdays with no RTH bar.** RTH here means end-stamped bars from 09:31 to 16:00 ET, which is T2's timestamp convention (T2 notes line 268, INFERRED by T2). The weekday range runs from the file's first date to its last.
```
$ python3 -I $X/gaps.py "$M" > $X/gaps.out; head -3 $X/gaps.out
file first date 2021-03-07 last date 2026-07-20
weekdays in range 1401 weekdays with >=1 RTH bar 1353 weekdays with ZERO RTH bars 48
MISSING 2021-04-02 Fri
```
**Holiday source.** NYSE's published "Holidays & Trading Hours" page, `https://www.nyse.com/markets/hours-calendars`. Each version of the page shows three years. 2026–2027 come from the live page. 2021–2025 come from Wayback Machine captures of the same URL: 20210531122307, 20221204100459, 20240529214655 and 20250202023059. The 2022 capture is the one that lists Juneteenth for 2022 and 2023. Fetches used `curl -sSL --max-time 20 -A "Mozilla/5.0"`; each returned http=200. The file hashes and an excerpt follow:
```
$ shasum -a 256 $H; ls -l $S/corr-C/ice-carter.html
4cfa639149b66e41a5fec097a6f3e8e50bbce8ab8c47cacd2fba4167666fbb6c  SP/corr-C/nyse-2021.html
78234ecc8183052f6d008e7c6d2178e24cd4625243246f47b340f78828ae0f12  SP/corr-C/nyse-2022.html
7705e638fcc49c4403d04a252930ed0d15c8e314a52e5943020c302a8b38d268  SP/corr-C/nyse-2024.html
b17c7e0c1f4d3336e6574c5f3f9b81c8f689301756d1ba3f85b5f9e0d67d4ecc  SP/corr-C/nyse-2025.html
3960e64cd7c9581c2e7a6d3f602342344eba1fac7b7476d51ddabb32b343fe11  SP/corr-C/nyse-now.html
-rw-r--r--@ 1 admin  wheel  5911 Nov  4 17:24 SP/corr-C/ice-carter.html
```
```
$ python3 -I $X/hol.py $S/corr-C/nyse-2021.html $S/corr-C/nyse-2024.html | grep -E "^(==|Holiday|New Year|Good Friday|Christmas)"
== SP/corr-C/nyse-2021.html rows 47
Holiday | 2021 | 2022 | 2023
New Years Day | Friday, January 1 | — | Monday, January 2 (New Year's holiday observed)
Good Friday | Friday, April 2 | Friday, April 15 | Friday, April 7
Christmas Day | Friday, December 24 (Christmas holiday observed) | Monday, December 26 (Christmas holiday observed) | Monday, December 25
== SP/corr-C/nyse-2024.html rows 20
Holiday | 2024 | 2025 | 2026
New Year’s Day | Monday, January 1 | Wednesday, January 1 | Thursday, January 1
Good Friday | Friday, March 29 | Friday, April 18 | Friday, April 3
Christmas Day | Wednesday, December 25*** | Thursday, December 25*** | Friday, December 25***
```
**Classification of the 48 dates.** A date counts as a holiday only if it appears in the NYSE tables above.
```
$ python3 -I $X/classify.py $X/gaps.out $H | grep -v "^KW"
NYSE holiday dates parsed (2021-2026): 58
missing weekdays 48 | on a NYSE-published holiday 15 | NOT on a NYSE-published holiday 33
HOL  2021-04-02 Good Friday [nyse-2021.html]
HOL  2021-12-24 Christmas Day [nyse-2021.html]
HOL  2022-04-15 Good Friday [nyse-2021.html]
HOL  2022-12-26 Christmas Day [nyse-2021.html]
HOL  2023-01-02 New Years Day [nyse-2021.html]
HOL  2023-04-07 Good Friday [nyse-2021.html]
HOL  2023-12-25 Christmas Day [nyse-2021.html]
HOL  2024-01-01 New Years Day [nyse-2022.html]
HOL  2024-03-29 Good Friday [nyse-2022.html]
HOL  2024-12-25 Christmas Day [nyse-2022.html]
HOL  2025-01-01 New Year’s Day [nyse-2024.html]
HOL  2025-04-18 Good Friday [nyse-2024.html]
HOL  2025-12-25 Christmas Day [nyse-2024.html]
HOL  2026-01-01 New Year’s Day [nyse-2024.html]
HOL  2026-04-03 Good Friday [nyse-2024.html]
GAP  2021-06-10 Thu
GAP  2021-09-10 Fri
GAP  2021-09-13 Mon
GAP  2021-09-14 Tue
GAP  2021-09-15 Wed
GAP  2021-09-16 Thu
GAP  2021-09-17 Fri
GAP  2021-09-20 Mon
GAP  2021-09-21 Tue
GAP  2021-09-22 Wed
GAP  2021-09-23 Thu
GAP  2021-09-24 Fri
GAP  2021-12-09 Thu
GAP  2022-03-10 Thu
GAP  2022-06-09 Thu
GAP  2022-09-08 Thu
GAP  2024-12-16 Mon
GAP  2025-01-09 Thu
GAP  2025-03-17 Mon
GAP  2025-09-15 Mon
GAP  2025-12-15 Mon
GAP  2025-12-16 Tue
GAP  2025-12-17 Wed
GAP  2025-12-18 Thu
GAP  2025-12-19 Fri
GAP  2025-12-22 Mon
GAP  2025-12-23 Tue
GAP  2025-12-24 Wed
GAP  2025-12-26 Fri
GAP  2025-12-29 Mon
GAP  2025-12-30 Tue
GAP  2025-12-31 Wed
GAP  2026-06-12 Fri
```
**Result.**
- Raw weekday gaps: **48**.
- On an NYSE-published holiday: **15**. All 15 are Good Friday, Christmas or New Year.
- Not on an NYSE-published holiday: **33**.
- 2025-01-09 is the national day of mourning for President Carter. It is not in any NYSE table fetched, and the ICE press-release URL tried returned HTTP 403 (5,911 bytes; `ice-carter.html` in block 1c). Its closure is therefore **UNVERIFIED** in this session. If it is excluded, the count is **32**, which is T2's ≈32.
- **CME caveat.** NQ trades on CME, not NYSE. No CME holiday calendar was fetched. It is UNVERIFIED whether CME equity futures had no RTH session on each of the 15 matched dates.
- The two long holes match T2's notes. 2021-09-10..09-24 is 11 weekdays. 2025-12-15..12-31 is 12 weekdays, excluding 12-25 and including 12-24.

**Does P1's wording hold?** As an approximation, yes. The exact corrected wording for Summary item 6, :178 and P1 is: *"33 weekdays in 2021-03-07..2026-07-20 have no RTH bar and are not NYSE-published holidays. The count is 32 if 2025-01-09 (Carter closure, UNVERIFIED) is excluded. 48 weekdays have no RTH bar in total."* The earlier "T2 marks its holiday calendar UNVERIFIED" is replaced: the NYSE dates are now sourced as above.

### C2. Holiday-adjusted Sharpe 1.1689 → 1.1907 (:81)

R1's script was re-run. Its output is byte-identical to the saved `R1-output.txt`. Lines 29 and 51 follow:
```
$ python3 $X/r1_indep.py > $X/r1_rerun.out; cmp $X/r1_rerun.out $S/out-C/R1-output.txt && echo IDENTICAL; sed -n "29p;51p" $X/r1_rerun.out
IDENTICAL
R0 all   T=1383 first 2021-03-29 last 2026-07-15 SRd(ddof1) 0.07363 SRd(ddof0) 0.07366 SRann 1.1689 skew g1 3.9492 G1 3.9535 kurt b2 50.0703 b2(sd1) 49.9980 tradeDays 792
nyse R0 removed 50 T=1333 SRd 0.07501 SRann 1.1907 skew 3.8702 kurt 48.2377; trade-exit dates on holidays: 2 PSR0 0.999056 ['2025-01-20', '2025-06-19']
```
R1's "nyse" holiday list is hardcoded in `r1_indep.py`. Compared with the fetched NYSE tables over R0's span, the two lists are identical:
```
$ python3 $X/holcmp.py $X $H
in R0 span: R1 list 52 | NYSE-published 52 | R1-only [] | published-only []
```
The claim at :81 holds. One clarification: "removed 50" is less than 52 because 2 of the holidays have trade exits (2025-01-20 and 2025-06-19), and the script keeps those days.

### C3. Intratrade drawdown −$48,657 (:137)

R1's extra script was re-run, and its output is byte-identical to the saved file:
```
$ (cd $X && python3 r1_extra.py > r1x_rerun.out); cmp $X/r1x_rerun.out $S/out-C/R1-extra-output.txt && echo IDENTICAL; sed -n 1p $X/r1x_rerun.out
IDENTICAL
MAE-envelope intratrade DD (approx, ignores commission in MAE) -48657.04 vs trade-close -45282.04
```
The claim holds. R1's own label applies: this is an approximation that ignores commission in the MAE.

### C4. "Full periods only: 16/21 and 8/10" and "Both of the last two halves are negative" (:139)

Net Profit is summed by exit date. A period is "full" if its whole calendar span lies between the first and last trade exits.
```
$ shasum -a 256 "$C"; python3 -I $X/periods.py "$C"
421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv
trades 1190 net 197327.60 first exit 2021-03-29 last exit 2026-07-15
 quarter 2021-Q1  2021-01-01..2021-03-31     +164.08  PARTIAL
 quarter 2021-Q2  2021-04-01..2021-06-30   +10239.56  full
 quarter 2021-Q3  2021-07-01..2021-09-30    -3472.08  full
 quarter 2021-Q4  2021-10-01..2021-12-31    +6626.28  full
 quarter 2022-Q1  2022-01-01..2022-03-31   +31429.64  full
 quarter 2022-Q2  2022-04-01..2022-06-30   +38456.28  full
 quarter 2022-Q3  2022-07-01..2022-09-30   +13466.48  full
 quarter 2022-Q4  2022-10-01..2022-12-31    -2317.60  full
 quarter 2023-Q1  2023-01-01..2023-03-31    +6606.48  full
 quarter 2023-Q2  2023-04-01..2023-06-30   +19434.24  full
 quarter 2023-Q3  2023-07-01..2023-09-30    +9398.12  full
 quarter 2023-Q4  2023-10-01..2023-12-31    +4390.16  full
 quarter 2024-Q1  2024-01-01..2024-03-31    -2182.60  full
 quarter 2024-Q2  2024-04-01..2024-06-30   +11346.48  full
 quarter 2024-Q3  2024-07-01..2024-09-30   +18066.28  full
 quarter 2024-Q4  2024-10-01..2024-12-31   +21373.12  full
 quarter 2025-Q1  2025-01-01..2025-03-31    +6664.44  full
 quarter 2025-Q2  2025-04-01..2025-06-30   +13144.04  full
 quarter 2025-Q3  2025-07-01..2025-09-30   -13106.68  full
 quarter 2025-Q4  2025-10-01..2025-12-31   +10752.72  full
 quarter 2026-Q1  2026-01-01..2026-03-31   -10905.16  full
 quarter 2026-Q2  2026-04-01..2026-06-30   +10169.04  full
 quarter 2026-Q3  2026-07-01..2026-09-30    -2415.72  PARTIAL
quarter: 17/23 positive (all) ; 16/21 positive (full only) ; last two (all) [((2026, 1), 10169.04), ((2026, 2), -2415.72)] ; last two full [((2026, 0), -10905.16), ((2026, 1), 10169.04)]
 half 2021-H1  2021-01-01..2021-06-30   +10403.64  PARTIAL
 half 2021-H2  2021-07-01..2021-12-31    +3154.20  full
 half 2022-H1  2022-01-01..2022-06-30   +69885.92  full
 half 2022-H2  2022-07-01..2022-12-31   +11148.88  full
 half 2023-H1  2023-01-01..2023-06-30   +26040.72  full
 half 2023-H2  2023-07-01..2023-12-31   +13788.28  full
 half 2024-H1  2024-01-01..2024-06-30    +9163.88  full
 half 2024-H2  2024-07-01..2024-12-31   +39439.40  full
 half 2025-H1  2025-01-01..2025-06-30   +19808.48  full
 half 2025-H2  2025-07-01..2025-12-31    -2353.96  full
 half 2026-H1  2026-01-01..2026-06-30     -736.12  full
 half 2026-H2  2026-07-01..2026-12-31    -2415.72  PARTIAL
half: 9/12 positive (all) ; 8/10 positive (full only) ; last two (all) [((2026, 0), -736.12), ((2026, 1), -2415.72)] ; last two full [((2025, 1), -2353.96), ((2026, 0), -736.12)]
```
- 17/23 and 9/12 (all periods) hold.
- 16/21 and 8/10 (full periods only) hold.
- "Both of the last two halves are negative" holds under either reading:
  - All halves: 2026-H1 −736.12 and 2026-H2 −2,415.72. 2026-H2 is partial and covers 07-01..07-15 only.
  - Full halves only: 2025-H2 −2,353.96 and 2026-H1 −736.12.

### C5. Quantpedia count (:136)

```
$ Q=$S/research-C/L3/quantpedia/in-sample-vs-out-of-sample-analysis-of-trading-strategies_.txt; shasum -a 256 $Q; sed -n 24p $Q | grep -o -E "Out of those,.{1,6}417.{1,6}were maintained|Further, 62 of them were excluded|we are left with 355 strategies"
97d7bd8a84a58fd9cbc3ec97682b48d7ef3b14e7df35051f2cbf48a450f1764f  SP/research-C/L3/quantpedia/in-sample-vs-out-of-sample-analysis-of-trading-strategies_.txt
Out of those,  417  were maintained
Further, 62 of them were excluded
we are left with 355 strategies
```
At :136, replace "mean IS Sharpe 1.574 across 417 strategies" with "mean IS Sharpe 1.574 across the **355** strategies analysed". Quantpedia maintained 417 strategies and excluded 62 of them. The 1.574 figure itself was not re-checked against the source's table in this correction (UNVERIFIED here).

### C6. DSR variance convention

V is the cross-trial variance of the daily SRs of R0–R3, at N=4. The report's 0.6163 (and the 0.62 in P3) uses the **sample variance (ddof=1)**. With the **population variance (ddof=0)** the result is **0.7494**. The brief cited 0.7495; the value observed here is 0.7494 from R1's script with the exact inputs. `dsr.py` uses the 5-dp printed inputs and gives 0.6162 and 0.7493.
```
$ diff $X/r1_indep.py $X/r1_indep_pop.py; python3 $X/r1_indep_pop.py | grep "DSR N=4 V(R0-R3)"; grep "DSR N=4 V(R0-R3)" $X/r1_rerun.out; python3 -I $X/dsr.py
233c233
<     v03 = np.var([srd[(k, "all")] for k in ("R0", "R1", "R2", "R3")], ddof=1)
---
>     v03 = np.var([srd[(k, "all")] for k in ("R0", "R1", "R2", "R3")], ddof=0)
DSR N=4 V(R0-R3) SR0_d 0.05770 SR0_ann 0.9160 DSR 0.7494
DSR N=4 V(R0-R3) SR0_d 0.06663 SR0_ann 1.0577 DSR 0.6163
sample ddof=1      V=0.00401048 SR0_d=0.06663 SR0_ann=1.0577 DSR=0.6162
population ddof=0  V=0.00300786 SR0_d=0.05770 SR0_ann=0.9160 DSR=0.7493
```
Under either convention the DSR is below 0.95 at N=4, so P3's "misses" reading is unchanged.

### C7. P1 and P9 sourcing

- **P1** has no literature source. It is a project-specific proposal based on the project's own data checks (T2 and C1 above).
- **P9** (PF without the top 1–2% of trades > 1.0) has no literature source. It is a project-specific proposal by Claude.
- Amear may adopt or drop either item.

### C8. R-1104-3 wording (:17, :170, :211)

```
$ cd /Volumes/Sensidine/Praxis.build; sed -n "753p;755p" DECISIONS.md | cut -c1-230; grep -n -o -E "R-1104-3.s judged version has breakers on|R-1104-3\*\* names the judged go/no-go version as High fill resolution with breakers on" docs/reports/2026-11-04-proof-of-concept-standard.md
- Amear's words: *"Yeah"*. Brief's framing: *"Yeah"* = High fill resolution with circuit breakers on as the judged go/no-go version, confirming R-VN3-6. The row does not record the question he answered.
- Condition, Amear's words: *"if the high fill resolution costs $700 for the data, I'm not going to pay that right now until there's proof of concept."*
17:R-1104-3's judged version has breakers on
170:R-1104-3's judged version has breakers on
211:R-1104-3** names the judged go/no-go version as High fill resolution with breakers on
```
`DECISIONS.md:753` records Amear's words only as *"Yeah"*. The reading "High fill resolution with circuit breakers on as the judged go/no-go version" is marked there as the brief's framing, and the row does not record the question he answered. His quoted words at `:755` mention high fill resolution and the $700 data cost. They do not mention breakers. Corrected wording:
- **:211:** *"R-1104-3 records Amear's reply as 'Yeah'. The ledger's framing, not his words, reads it as High fill resolution with breakers on as the judged version. His quoted condition concerns only the high-fill-resolution data cost: 'if the high fill resolution costs $700 …'."*
- **:17 and :170:** "R-1104-3's judged version has breakers on" is the ledger's framing of R-1104-3, not Amear's words.

### Correction scope

- Changed by this correction: the readings at :17, :81 (confirmed), :136, :137 (confirmed), :139 (confirmed), :170, :178, :211, P1, P3 (convention stated) and P9.
- Not changed: the `Result: PASS` at :351. It is a producer claim and not a grade, and this correction does not grade itself.
- Files staged: none. This correction appends to this file only.

### C9. Evidence supplement (internal adversarial check of C1–C8, same date)

An adversarial worker re-computed C1–C8 with its own code and got the same numbers, but returned FAIL on S1 with 7 gaps. Each gap is addressed below, in the same order. C1–C8 are left as written. Where C9 differs from them, C9 wins.

1. **Lines 1–353 unchanged:**
```
$ cd /Volumes/Sensidine/Praxis.build; head -353 docs/reports/2026-11-04-proof-of-concept-standard.md | shasum -a 256
cc800a7cdf212401443ac4e9bb968617f1f873f3b74b0ecc6d282bc69f5affd0  -
```
2. **HTTP status codes and Wayback capture timestamps.** The status codes in C1 were seen during the session but never saved to a file. The block below is a re-fetch with the same curl flags into `SP/corr-C2/`, and it is the evidence for the statuses: http=200 for all five NYSE pages and **http=403** for the ICE URL. The four Wayback re-fetches are not byte-identical to the files used in C1, but they resolve to the same capture timestamps. Those timestamps are pasted from the original files in the second block, and the 2022 capture's Juneteenth row is in the third.
```
$ for u in "https://web.archive.org/web/20210601000000/https://www.nyse.com/markets/hours-calendars|r2021" "https://web.archive.org/web/20221201000000/https://www.nyse.com/markets/hours-calendars|r2022" "https://web.archive.org/web/20240601000000/https://www.nyse.com/markets/hours-calendars|r2024" "https://web.archive.org/web/20250201000000/https://www.nyse.com/markets/hours-calendars|r2025" "https://www.nyse.com/markets/hours-calendars|rnow" "https://ir.theice.com/press/news-details/2024/NYSE-to-Close-Markets-on-January-9-2025-to-Honor-the-Passing-of-Former-President-Jimmy-Carter/default.aspx|rice"; do curl -sSL --max-time 20 -A "Mozilla/5.0" -o $S/corr-C2/${u##*|}.html -w "${u##*|} http=%{http_code} bytes=%{size_download} final=%{url_effective}\n" "${u%%|*}"; done; for y in 2021 2022 2024 2025 now; do cmp -s $S/corr-C/nyse-$y.html $S/corr-C2/r$y.html && echo "nyse-$y.html re-fetch IDENTICAL" || echo "nyse-$y.html re-fetch DIFFERS"; done
r2021 http=200 bytes=103663 final=https://web.archive.org/web/20210531122307/https://www.nyse.com/markets/hours-calendars
r2022 http=200 bytes=107289 final=https://web.archive.org/web/20221204100459/https://www.nyse.com/markets/hours-calendars
r2024 http=200 bytes=145253 final=https://web.archive.org/web/20240529214655/https://www.nyse.com/markets/hours-calendars
r2025 http=200 bytes=148720 final=https://web.archive.org/web/20250202023059/https://www.nyse.com/markets/hours-calendars
rnow http=200 bytes=134492 final=https://www.nyse.com/markets/hours-calendars
rice http=403 bytes=5911 final=https://ir.theice.com/press/news-details/2024/NYSE-to-Close-Markets-on-January-9-2025-to-Honor-the-Passing-of-Former-President-Jimmy-Carter/default.aspx
nyse-2021.html re-fetch DIFFERS
nyse-2022.html re-fetch DIFFERS
nyse-2024.html re-fetch DIFFERS
nyse-2025.html re-fetch DIFFERS
nyse-now.html re-fetch IDENTICAL
```
```
$ for y in 2021 2022 2024 2025; do print -n "nyse-$y.html "; grep -o -m1 "web.archive.org/web/[0-9]\{14\}" SP/corr-C/nyse-$y.html | head -1; done
nyse-2021.html web.archive.org/web/20210531122307
nyse-2022.html web.archive.org/web/20221204100459
nyse-2024.html web.archive.org/web/20240529214655
nyse-2025.html web.archive.org/web/20250202023059
```
```
$ python3 -I $X/hol.py $S/corr-C/nyse-2022.html | grep -E "^(==|Holiday|Juneteenth)"
== SP/corr-C/nyse-2022.html rows 19
Holiday | 2022 | 2023 | 2024
Juneteenth National Independence Day | Monday, June 20 (Juneteenth holiday observed) | Monday, June 19 | Wednesday, June 19
```
3. **`python3 -I` statement.** C1's opening paragraph says every untrusted page was parsed with `python3 -I`. That was false for the C2 block, which ran `holcmp.py` without `-I`. The same comparison re-run with `-I` gives identical output:
```
$ python3 -I $X/holcmp.py $X $H
in R0 span: R1 list 52 | NYSE-published 52 | R1-only [] | published-only []
```
4. **T2 citations.**
   - T2 states the end-stamped convention at line 268.
   - T2 uses the 09:31–16:00 RTH window at line 251, not 268.
   - T2's ≈32 count and its two long holes are at line 309. My count agrees with T2 on the two long holes: 11 weekdays and 12 weekdays.
```
$ sed -n "268p;298p;309p" $S/out-C/T2-notes.md | cut -c1-260; grep -n "093100\|09:31" $S/out-C/T2-notes.md $S/scripts-C/t2.py | head -5 | cut -c1-200
**Timestamp convention** — INFERRED (strong): end-stamped ET. Basis (t2b output): 18:01 bars 1354 vs 18:00 bars 1; 17:00 bars 1302 vs 17:01–17:59 48 total (daily halt 17:00–18:00 ET); holiday-halt days end at 13:00 ET (=12:00 CT), early-close days end 13
## CORRECTION to counter-condition 5 (roll days) — whole RTH days missing
Excluding exchange holidays (Good Fridays, Christmas/New Year observed, 2025-01-09 Carter closure — calendar from prior knowledge, UNVERIFIED), ≈32 ordinary trading days are absent: the quarterly-roll Thursdays 2021-06-10, 2021-12-09, 2022-03-10, 2022-06-0
SP/out-C/T2-notes.md:161:bars stamped 09:30 1354, 09:31 1355, 16:00 1306, 16:01 1305
SP/out-C/T2-notes.md:251:== 20230405 count bars 09:31-16:00: 273
SP/out-C/T2-notes.md:299:Item 5 above ("no roll-sized jump") is superseded: t2b's jump list showed 
```
5. **R1's hardcoded list and the "keeps those days" rule.** `r1_indep.py:114` defines the "nyse" list in code. Line 137 drops a holiday only if it has no trade P&L (`d not in pnl`). That is why 50 days were removed rather than 52.
```
$ grep -n -E "^def holidays|kind == .nyse.|d not in pnl" $X/r1_indep.py
103:def holidays(y, kind):
114:    if kind == "nyse":
137:        if d.weekday() < 5 and not (hol and d in hol and d not in pnl):
```
6. **"The brief cited 0.7495" is withdrawn.** It came from the correction brief, not from a file. The observed values are **0.6163 (ddof=1)** and **0.7494 (ddof=0)**, as pasted in C6.
7. **Link between 1.574 and the 355 strategies.** Tab. 1 is headed "Comparison of Sharpe Ratios of backtested strategies" (line 32). Line 29 computes Sharpe ratios "for each included strategy", and line 24 says 355 were left for analysis. That 1.574 is the mean over those 355 is **INFERRED** from these lines; the source does not state it outright. The corrected :136 should read "mean IS Sharpe 1.574 in Quantpedia's Tab. 1, which covers the 355 strategies analysed (INFERRED)".
```
$ Q=$S/research-C/L3/quantpedia/in-sample-vs-out-of-sample-analysis-of-trading-strategies_.txt; grep -n -E "Sharpe|Tab|355|1\.574" $Q | cut -c1-200 | head -12
18:The last research paper that we would like to mention is that of  Falck, Rej, and Thesmar (2021) , which examines the hypothesis of ex-ante characteristics empirically predicting the out-of-sample
24:From all 868  strategies  at the moment of analysis (at the beginning of  May 2023 ), we have in-house backtested  671  out of them. Out of those,  417  were maintained and updated on a mont
25:The main analyzed core interest is the  Sharpe Ratio , which we conclude is the most suitable measure to compare in- vs. out-of-sample results in our data sample. Our  database covers all main as
29:We calculated CAR p.a. and Volatility p.a. , which division gave us Sharpe Ratio s for in-sample and out-of-sample for each included strategy.
31:Now, let’s move on. As a measure of average, we have chosen the arithmetic mean. The  median  is the value separating the higher half from the lower half of a data sample and is not skewed by a
32:Tab. 1 Comparison of Sharpe Ratios of backtested strategies
33:Sharpe Ratio (of)
37:1.574
48:As per Tab. 1, Sharpe Ratio for out-of-sample results is worse and deteriorated by  33% (on average) or 44% (median strategy) . These results are totally in line and consistent with findings in th
49:Following is the figure depicting the distribution (histogram) of Sharpe Ratio s both in- and out-of-sample:
50:As we can see, the distribution of results follows “quasi-normal distribution”, where you can mainly expect your strategy to have a Sharpe ratio in interval (-1, 3) . And it is both for out-of-
57:Undoubtedly,  Sharpe Ratio s  worsen during a lifetime after forming various trading strategies based on beforehand not-know market anomalies. According to our analysis, it is reasonable to expec
```
