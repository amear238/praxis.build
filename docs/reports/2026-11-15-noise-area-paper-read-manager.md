# Noise-Area paper read: does the source paper specify a hard stop? (manager)

**Unit:** `2026-11-15-noise-area-paper-read`. **Mode:** read-only research. No retest, no strategy change, no decision, no commit.
**HEAD:** `d9fc5f0` (= origin/main, pasted in block M1 below).

## Task

The trader's typed Q6 ruling (DECISION_LOG.md row 2026-11-15T14:37:18Z, :994) asks that the original paper be checked for a hard stop before any retest: "Report what the paper actually says, with the exact wording, before any retest. If a source spec has no stop, don't decide anything: bring it back to me." The run was cleared by his answer "Run it now" (row 2026-11-15T16:23:34Z, :1003) and dispatched by the master (row :1004). The paper is Carlo Zarattini, Andrew Aziz and Andrea Barbon, "Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)", Swiss Finance Institute Research Paper No. 24-97. The rows are pasted in block M1.

## Rubric criteria addressed

From `specs/SPEC_RUBRIC.md` (the lines are pasted in block M1): S1 (pasted output for every claim), S2 (no claim above its evidence), S4 (deviations from the plan), S5 (no inferred approval), S6 (cross-block check), S8 (no question of the trader's answered for him), S13 (the standing sentence, once).

## Workers dispatched (id, mode, outcome)

| id | mode | scope | outcome (report line) |
|---|---|---|---|
| worker 1 | BUILD | fetch, extract, grep, quote, project wording, mismatches | wrote report lines 1-549; stopped at its turn limit after writing (verdict NO; block E10) |
| worker 2 | ADVERSARIAL | independent re-fetch and re-hash, re-grep, quote-by-quote check, omission hunt | 22 of 22 quote blocks exact; 8 defects below verdict level (block E10, worker 2 :472-:486) |
| worker 3 | BUILD (fix) | append corrections D1-D8 to worker 1 | Addendum from worker 1 :550; lines 1-549 unchanged (blocks M3, E6) |
| worker 4 | ADVERSARIAL | check the worker 3 addendum | Result: FAIL, 2 defects (S2) (block E10) |
| worker 5 | BUILD (fix) | append corrections F1-F3 | Addendum 2 from worker 1 :955 |
| worker 6 | ADVERSARIAL | check Addendum 2 | 38 of 38 quote checks pass; Result: FAIL, 3 defects (1 S2, 2 S1) (block E10) |
| worker 7 | BUILD (fix) | append corrections G1-G3 | Addendum 3 from worker 1 :1063; checked by the manager's re-run (block M4), not by a further adversary |

## Process log

1. I read the rubric and checked the baseline: HEAD, the authorising rows, the target files and the tools (block M1).
2. I dispatched worker 1. The SSRN pages returned 403 bot-challenge pages. The St. Gallen university repository returned the PDF.
3. I re-ran the hash and the key greps myself on worker 1's copy (block M2).
4. I dispatched worker 2 in adversarial mode, giving it the artifact and the criteria but not worker 1's reasoning. It downloaded the file again itself: same bytes (block E1).
5. I ran negative tests: the report gate and the quote checker both trip (block M3).
6. Each adversary found defects. I sent each set to a fix worker, and each fix worker appended to the worker 1 report without changing earlier lines (workers 3, 5, 7). I sent each of the first two fixes to a fresh adversary (workers 4, 6). Worker 7's three small corrections were re-run by me (block M4).
7. Final evidence run (blocks E0-E12), then staging into a temp index (block M5).

## Verification evidence

Pasted output only. M blocks were captured during the run. E blocks come from the final evidence run (`evidence.sh` in the session scratchpad, read-only).

**M1. Baseline (manager, start of run):**
```
$ date -u && git rev-parse HEAD origin/main && git diff --cached --stat && echo "---default-index-end" && grep -nE '^\| *S(1|2|4|5|8|13) ' specs/SPEC_RUBRIC.md && ls docs/reports/2026-11-15-noise-area* ; command -v pdftotext pdfinfo curl python3 mutool qpdf
Sun 15 Nov 2026 16:24:31 UTC
d9fc5f08f25842180966dc04220082314689d29e
d9fc5f08f25842180966dc04220082314689d29e
 docs/reports/evidence/2026-10-28-mffu-davi-reply.png | Bin 0 -> 254350 bytes
 1 file changed, 0 insertions(+), 0 deletions(-)
---default-index-end
133:| S1 | Every claim in a report has pasted command output, not a description of output. |
134:| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
136:| S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after. |
137:| S5 | No approval is inferred from a verbal or in-session exchange. The ledger append is the authorisation. |
140:| S8 | No question that belongs to [trader] is answered on his behalf. |   (name masked by the manager)
145:| S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed." Reports with no such figure carry it too, ... [cut here by the manager for width]
(eval):1: no matches found: docs/reports/2026-11-15-noise-area*
/opt/homebrew/bin/pdftotext
/opt/homebrew/bin/pdfinfo
/usr/bin/curl
/opt/homebrew/bin/python3
/opt/homebrew/bin/qpdf
$ grep -n '2026-11-15T14:37:18Z\|2026-11-15T16:23:34Z' DECISION_LOG.md | cut -c1-600   (excerpts; each row cut by the manager at the first clause)
994:- [2026-11-15T14:37:18Z] WHO: [trader] | WHAT: **[trader]'s typed Q6 ruling in the master session** ... Verbatim: "Retest depends on the original source spec. For each of the five, go back to where the strategy was found and check what it specified. ...
1003:- [2026-11-15T16:23:34Z] WHO: [trader] | WHAT: **[trader]'s answers to the master's two questions at session start (AskUserQuestion, new session), verbatim option labels.** Q1, "May the paper read run now, without waiting for 205?": **"Run it now"** ...
1004:- [2026-11-15T16:23:34Z+] WHO: praxis-master | WHAT: **Dispatch of unit `2026-11-15-noise-area-paper-read`.** One praxis-manager, background. Read-only research: ...
   (names in rows 994 and 1003 masked as [trader] by the manager)
$ grep -n '^| S6 ' specs/SPEC_RUBRIC.md   (captured 16:39:46Z)
138:| S6 | Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own. |
```

**M2. Manager re-check of worker 1's copy:**
```
Sun 15 Nov 2026 16:32:05 UTC
 1901828 paper.pdf
41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad  paper.pdf
2168e040467e94d1b36ab83fe9c1fcd2
CreationDate:    Mon Feb  3 13:01:20 2025 EST
Pages:           43
HTTP/2 302 
HTTP/2 200 
content-disposition: inline; filename="ssrn-4824172 (2).pdf"; filename*=UTF-8''ssrn-4824172%20%282%29.pdf
--- p9
15:caused by short-term market fluctuations, trading is restricted to semi-hourly intervals,
16:specifically at HH:00 and HH:30. This timing mechanism ensures that decisions are
20:Positions are unwound either at market Close or if there is a crossover to the opposite
23:dence of demand/supply imbalance. Stop losses can also be triggered only on semi-hourly
--- p13
12:VWAP as a trailing stop for intraday trend exposures2 . Once a position is established,
13:as soon as the price crosses either the curent band or the VWAP, the position is closed.
17:                 Long TrailingStopt,HH:M M = max(U Bt,HH:M M , V W APt,HH:M M )
19:                 Short TrailingStopt,HH:M M = min(LBt,HH:M M , V W APt,HH:M M )
35:       VWAP is computed only using market hours data. For more details see our previous publication [5].
--- full-text counts
hard stop: 0
stop order: 0
stop-loss: 0
maximum loss: 0
fixed stop: 0
continuous: 0
```

**M3. Negative tests: the report-contract gate and the quote checker trip, plus the pre-append worker 1 hashes:**
```
Sun 15 Nov 2026 16:39:16 UTC
== N1 report-contract gate, latest report is worker2 (no Verification evidence section)
docs/reports/2026-11-15-noise-area-paper-read-worker2.md
BLOCKED: '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker2.md' has no Verification evidence section.
gate exit=2
== N2 qcheck on unmutated worker1 report, block02
block02 Q2 artline256 nlines=5 EXACT=['p9:20-24'] RSTRIP_ONLY=- NORM=['p9']
== N2 qcheck on copy with Q2 mutated (only -> at any time)
block02 Q2 artline256 nlines=5 EXACT=- RSTRIP_ONLY=- NORM=FAIL
259c259
< dence of demand/supply imbalance. Stop losses can also be triggered only on semi-hourly
---
> dence of demand/supply imbalance. Stop losses can also be triggered at any time on semi-hourly
   (diff output cut by the manager to the quote line; three other changed lines, 149, 220 and 442, carry the same substitution)
--- pre-append hashes, before worker 3 was dispatched
Sun 15 Nov 2026 16:39:46 UTC
c0a36f0caa52377f9d43b21e637da7c16ea5ca427e4e86c5e737cb5f2772a351  docs/reports/2026-11-15-noise-area-paper-read-worker1.md
a188308bd8bda361bc5433abaa4a3fab9fbe22bf01c06b79887827ccdb2333c7  docs/reports/2026-11-15-noise-area-paper-read-worker2.md
     550 docs/reports/2026-11-15-noise-area-paper-read-worker1.md
4fad7a367ee5c779815bc78c71e6e6f290f0f9752fb02896ed2924fa1c484250  -      <- head -n 549 worker1 | shasum -a 256
```

**M4. Manager re-run of the worker 7 Addendum 3 claims:**
```
--- after worker 5 (head -n 954 must equal the value worker 5 reported as its pre-append hash, 49ca77f0...)
Sun 15 Nov 2026 16:56:09 UTC
2e8327578e7a5eab740ddb3d83cd8342be828fef82bdc0e986ca5fd0778860e4  docs/reports/2026-11-15-noise-area-paper-read-worker1.md
49ca77f0aebcd10dcfb468bf4d5e126464d53b363401380ef75d47cebb97c283  -
--- after worker 7 (head -n 1062 must equal worker 7's reported pre-append value c2498486...)
Sun 15 Nov 2026 17:02:44 UTC
    1122 /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md
b7fb9269f5ac5e226cffc963bbbc7c16295ec23b7c4682bf89b2b9414390471e  /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md
c2498486b3812527cc7b924895a605a6ac7f62a045ac21e44fa227ae4b8ffe4c  -
--- G1-G3 re-run
Sun 15 Nov 2026 17:02:52 UTC
905:page-02.txt:25:       500. Unlike the academic literature that typically limits trading to the last 30 min-
907:page-04.txt:32:studies, our model does not limit the trading to the last 30-minutes of the trading session;
DECISIONS.md
docs/reports/2026-07-16-4uu-noise-area-strategy.md
docs/specs/2026-07-15-block2-backtesting-scope-proposal.md
docs/specs/2026-07-16-b2-noise-area-ruleset.md
check-ignore exit=1
29:       which have been discussed in our previous papers, we introduce the use of dy-
30:       namic trailing stops to mitigate downside risks while allowing for unlimited upside
0      <- email-shaped lines in worker 1 :1063-:1122
name exit=1
```

**E0-E12. Final evidence run.** This was run on the draft of this file before the blocks were inserted, so the two manager-report line numbers in E7 are draft positions. Block M5 gives the final positions:
```
== E0 date
Sun 15 Nov 2026 17:06:05 UTC
== E1 PDF identity (both independent downloads)
 1901828 /tmp/praxis-npr/dl/w1/paper.pdf
 1901828 /tmp/praxis-npr/dl/w2/paper.pdf
 3803656 total
41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad  /tmp/praxis-npr/dl/w1/paper.pdf
41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad  /tmp/praxis-npr/dl/w2/paper.pdf
cmp: identical
   1 content-disposition: inline; filename="ssrn-4824172 (2).pdf"; filename*=UTF-8''ssrn-4824172%20%282%29.pdf
   1 HTTP/2 200 
   1 HTTP/2 302 
   2 HTTP/2 403 
   1 location: https://alexandria.unisg.ch/server/api/core/bitstreams/a99aba00-f967-49b3-aceb-f544dc386e0b/content
== E2 key paper lines (worker 2 extraction, page:line)
-- p02:22-31
                                                       Abstract
       This paper investigates the profitability of a simple, yet effective intraday momen-
       tum strategy applied to SPY, one of the most liquid ETFs that tracks the S&P
       500. Unlike the academic literature that typically limits trading to the last 30 min-
       utes of the trading session, our model initiates trend-following positions as soon
       as there is an indication of abnormal demand/supply imbalance in the intraday
       price action. Building on trading techniques commonly used by active day traders,
       which have been discussed in our previous papers, we introduce the use of dy-
       namic trailing stops to mitigate downside risks while allowing for unlimited upside
       potential. From 2007 to early 2024, the resulting intraday momentum portfolio
-- p09:5-7
Figure 2: The time-varying boundary areas on SPY for 31 January 2022 (a) and 29 April 2022 (b) and
the resulting trades based on our base-model. Please note that all positions are closed at the market
Close (16:00).
-- p09:12-17
As discussed earlier, if the market breaches the boundaries of the Noise Area, our strat-
egy initiates positions in accordance with the prevailing intraday move—going long if the
price is above the Noise Area and short if it is below. To mitigate the risk of overtrading
caused by short-term market fluctuations, trading is restricted to semi-hourly intervals,
specifically at HH:00 and HH:30. This timing mechanism ensures that decisions are
based on more stable price movements rather than transient spikes.
-- p09:20-24
Positions are unwound either at market Close or if there is a crossover to the opposite
boundary of the Noise Area. In the event of such a crossover, the existing position is
closed, and a new one is initiated in the opposite direction to align with the latest evi-
dence of demand/supply imbalance. Stop losses can also be triggered only on semi-hourly
intervals.
-- p09:31-32
market movements. All positions are closed at market Close, adhering to the strategy’s
protocol to limit exposure to overnight market changes.
-- p13:11-19
ance. Building upon insights from our previous publication, we have chosen to integrate
VWAP as a trailing stop for intraday trend exposures2 . Once a position is established,
as soon as the price crosses either the curent band or the VWAP, the position is closed.
Mathematically, the trailing stops for long and short postions are defined as:


                 Long TrailingStopt,HH:M M = max(U Bt,HH:M M , V W APt,HH:M M )

                 Short TrailingStopt,HH:M M = min(LBt,HH:M M , V W APt,HH:M M )
-- p13:35-35
       VWAP is computed only using market hours data. For more details see our previous publication [5].
-- p30:1-7
Frequently Asked Questions (FAQs)
Following the publication of this paper, we received hundreds of insightful questions
from readers. While we are unable to address every inquiry—particularly those requiring
significant extensions of our research or the disclosure of specific trading rules that we
utilize to enhance strategy efficiency—we have compiled answers to the most common
questions. This section will be updated regularly to include new Q&As that may arise
in the future.
-- p34:3-5
Yes, but please note that this is a simplified model that can be further enhanced with
a few small adjustments. The goal of our papers is not to provide ready-to-use trading
strategies, but rather to introduce traders and readers to potential trading edges.
== E3 zero-hit terms across all 43 pages (one-line grep)
hard stop: 0
stop order: 0
stop-loss: 0
maximum loss: 0
fixed: 0
continuous: 0
intrabar: 0
every 30 minutes: 0
== E4 quote checker on worker 1 Q1-Q12 (worker 2 script, worker 2 text)
block01 Q1 EXACT=['p9:12-17'] NORM=['p9']
block02 Q2 EXACT=['p9:20-24'] NORM=['p9']
block03 Q3 EXACT=['p9:27-32'] NORM=['p9']
block04 Q3 EXACT=['p9:5-7'] NORM=['p9']
block05 Q4 EXACT=['p10:1-3'] NORM=['p10']
block06 Q5 EXACT=['p11:6-9'] NORM=['p11']
block07 Q5 EXACT=['p11:12-17'] NORM=FAIL
block08 Q5 EXACT=['p12:7-8'] NORM=['p12']
block09 Q5 EXACT=['p12:1-3'] NORM=['p12']
block10 Q6 EXACT=['p12:11-22'] NORM=['p12']
block11 Q7 EXACT=['p12:25-26'] NORM=FAIL
block12 Q7 EXACT=['p13:11-19'] NORM=['p13']
block13 Q7 EXACT=['p13:23-27'] NORM=['p13']
block14 Q7 EXACT=['p13:35-35'] NORM=['p13']
block15 Q7 EXACT=- NORM=['p13']
block16 Q8 EXACT=['p14:7-17'] NORM=['p14']
block17 Q8 EXACT=['p15:17-18'] NORM=['p15']
block18 Q8 EXACT=['p15:34-36'] NORM=['p15']
block19 Q9 EXACT=['p16:24-36'] NORM=['p16']
block20 Q10 EXACT=['p17:8-12'] NORM=['p17']
block21 Q11 EXACT=['p34:7-11'] NORM=['p34']
block22 Q12 EXACT=['p40:1-3'] NORM=['p40']
== E5 project wording, HEAD d9fc5f0
-- docs/specs/2026-07-16-b2-noise-area-ruleset.md:38
- **Positions per session:** **NOT capped at one.** A position is held until the close or until price crosses to the **opposite** boundary, at which point it is closed **and reversed** into a new position that direction (p. 9). Realized average trade frequency is **1.3 trades/day** (base opp-band stop) rising to **1.8 trades/day** with the VWAP stop (Table 4, p. 16). Stops, too, are evaluated only at the semi-hourly 
-- docs/specs/2026-07-16-b2-noise-area-ruleset.md:59
- **Base stop:** trailing stop at the **opposite** Noise-Area boundary (long stops at Lower/Upper as it trails; base model = "Stop @ Opp. Band", Table 1). Evaluated only at semi-hourly stamps.
-- docs/specs/2026-07-16-b2-noise-area-ruleset.md:61
  `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.
-- docs/reports/2026-07-16-4uu-noise-area-strategy.md:28
| Long stop `Max(curUpper, curVwap)`; Short `Min(curLower, curVwap)`; evaluated only at checkpoint | Trailing stop = band-or-VWAP (whichever tighter), at the stamp | §4 p.9,13 |
-- docs/reports/2026-11-14-r3-recheck-manager.md:9
| Noise-Area baseline (BandOrVWAP) | band/VWAP level, checked at HH:00/HH:30 bar closes, market exit | NO | −$542.40 | 10 | −$705.10 | 5 |
-- docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:129 (first 200 chars)
**Answer:** The strategy under test is the **Zarattini–Aziz–Barbon NQ "Noise-Area" intraday breakout** (clock-anchored, rules-based, one bracket/session). It is **NOT exportable from TradingView** — n
-- DECISION_LOG.md:994 ruling sentence (working tree, fixed-string -o)
The project's research summary says it uses a trailing stop at the band or VWAP, checked at set times, which would mean no fixed maximum loss.
== E6 report files
docs/reports/2026-11-15-noise-area-paper-read-worker1.md lines=1122 s13=1 b7fb9269f5ac5e22
docs/reports/2026-11-15-noise-area-paper-read-worker2.md lines=488 s13=1 a188308bd8bda361
docs/reports/2026-11-15-noise-area-paper-read-worker4.md lines=550 s13=1 b6e7ba4b5d2d4199
docs/reports/2026-11-15-noise-area-paper-read-worker6.md lines=202 s13=1 cdf27cd8776c25cd
-- worker1 lines 1-549 sha256 (worker 3 append-only proof; pre-append value 4fad7a36...)
4fad7a367ee5c779815bc78c71e6e6f290f0f9752fb02896ed2924fa1c484250  -
== E7 privacy sweep on this unit's reports
email grep exit=1 (1 = none)
docs/reports/2026-11-15-noise-area-paper-read-worker6.md:46:- Section 955-1063: 0 at-sign characters. The email regex gives exit 1 (no match). A grep for the names [trader], [trader-surname], Zarattini, Aziz and Barbon gives exit 1. The section names no person. The capitalised word pairs it contains are all titles, paths or paper text ("Asset Under").
worker-report name grep exit=0 (1 = none)   (names in the E7 lines above and below masked by the manager)
117:- **A name in this file.** The brief asks for both "no personal names other than the three paper authors" and a final section titled "For [trader]". I followed the specific heading instruction. The heading is the only place the trader's name appears (block E7 grep). The worker reports contain no names.
134:## For [trader]
== E8 negative test: report-contract gate on a scratch copy
BLOCKED: '/var/folders/6g/9y7c60hs3yv9bmk1w1lwbt4c0000gn/T/tmp.PuS1Sdi9P8/docs/reports/bad.md' has no Verification evidence section.
gate on report without Verification evidence: exit=2
gate on manager report copy: exit=0
== E9 tree unchanged outside this unit
 M .claude/settings.json
 M AUDIT_LOG.md
 M DECISIONS.md
 M DECISION_LOG.md
 M DISPATCH_LOG.md
 M HANDOFF.md
 M ISSUE_REGISTER.md
 M MANIFEST.md
 M STATUS.md
 M docs/reports/2026-10-28-f4-davi-reply-filing.md
 M docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md
A  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
 M docs/specs/2026-11-05-walk-forward-spec.md
 M docs/specs/2026-11-06-walk-forward-values.md
 M scripts/dispatch-log-writeahead.sh
untracked count: 115
== E10 worker report result lines and quote-check totals
docs/reports/2026-11-15-noise-area-paper-read-worker1.md:431:**Hard stop (a fixed maximum loss per trade, known at entry, such as a resting stop order at a set 
docs/reports/2026-11-15-noise-area-paper-read-worker1.md:546:## Result
docs/reports/2026-11-15-noise-area-paper-read-worker2.md:327:**Hard stop (a fixed maximum loss per trade known at entry, e.g. a resting stop order at a set pric
docs/reports/2026-11-15-noise-area-paper-read-worker2.md:472:## Result
docs/reports/2026-11-15-noise-area-paper-read-worker2.md:486:No privacy defect, no S8 defect, S13 satisfied. Result for the adversarial task: **BREAKS FOUND (8 
docs/reports/2026-11-15-noise-area-paper-read-worker4.md:237:TOTAL 202 PASS 199
docs/reports/2026-11-15-noise-area-paper-read-worker4.md:278:TOTAL 33 PASS 33
docs/reports/2026-11-15-noise-area-paper-read-worker4.md:540:## Result: FAIL
docs/reports/2026-11-15-noise-area-paper-read-worker6.md:94:TOTAL 38/38 PASS
docs/reports/2026-11-15-noise-area-paper-read-worker6.md:196:## Result: FAIL
550:## Addendum (worker 3, corrections)
955:## Addendum 2 (worker 5, corrections to the worker 3 addendum)
1063:## Addendum 3 (worker 7, corrections to Addendum 2)
== E11 default index (must be unchanged from session start)
 docs/reports/evidence/2026-10-28-mffu-davi-reply.png | Bin 0 -> 254350 bytes
 1 file changed, 0 insertions(+), 0 deletions(-)
== E12 Redemtion/ is untracked and ignored
.gitignore:7:Redemtion/	Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf
       0
```

## What the paper says (verbatim; page:line from the text extract, blocks E2 and E4)

- **Exit, base model (§3 Strategy Description, p. 9:20-24):** "Positions are unwound either at market Close or if there is a crossover to the opposite boundary of the Noise Area. In the event of such a crossover, the existing position is closed, and a new one is initiated in the opposite direction to align with the latest evi- dence of demand/supply imbalance. Stop losses can also be triggered only on semi-hourly intervals."
- **When trading is allowed (p. 9:15-16):** "trading is restricted to semi-hourly intervals, specifically at HH:00 and HH:30."
- **Session close (p. 9:31-32):** "All positions are closed at market Close, adhering to the strategy’s protocol to limit exposure to overnight market changes." The Figure 2 caption (p. 9:6-7) says the same thing: "all positions are closed at the market Close (16:00)."
- **Refined stop, the one the rest of the paper uses (p. 13:12-19; §4 p. 17:8-12 says the later tests use it):** "VWAP as a trailing stop for intraday trend exposures2 . Once a position is established, as soon as the price crosses either the curent [sic] band or the VWAP, the position is closed." The formulas are `Long TrailingStop = max(UB, VWAP)` and `Short TrailingStop = min(LB, VWAP)`, both indexed by time of day t,HH:MM.
- **Abstract (p. 2:29-31):** "we introduce the use of dy- namic trailing stops to mitigate downside risks while allowing for unlimited upside potential."
- **Rules not disclosed (FAQ preface, p. 30:3-5):** the authors say they cannot answer every question, "particularly those requiring significant extensions of our research or the disclosure of specific trading rules that we utilize to enhance strategy efficiency".
- **Simplified model (FAQ Q11, p. 34:3-5):** "this is a simplified model that can be further enhanced with a few small adjustments."
- **Zero-hit terms** across all 43 pages: "hard stop", "stop order", "stop-loss", "maximum loss", "fixed", "continuous", "intrabar" and "every 30 minutes" (block E3). "Max Loss Trade" in Table 4 (p. 16) is a backtest result column, not a rule (worker 1 :386-:401, :439).

## Answer (from the quotes only)

**Hard stop: NO.** The paper's stated exits are three: the market close, the opposite-boundary crossover, and a trailing stop at band or VWAP. All of these levels are set at times of day or move with the price. No passage sets a stop price or a loss amount at entry, and the terms in block E3 have 0 hits. The paper does not *state* a hard stop. The authors also say some trading rules are not disclosed (p. 30) and call the model "simplified" (p. 34). This NO therefore covers only the rules the paper prints. It is not evidence about rules the authors say they withhold. This is a statement about the text (S2). It is not a finding about how the strategy behaves.

**Continuous or set times:** For the base model, set times are stated in so many words: "Stop losses can also be triggered only on semi-hourly intervals" (p. 9:23-24). For the refined band-or-VWAP stop the answer is **UNCLEAR**. The text says "as soon as the price crosses" (p. 13:13) and does not restate the interval. The p. 9 sentence is not labelled base-only. The two worked exits fall on the half-hour grid ("at 14:00", "at 13:00"). Workers 1 and 2 reached this reading independently (worker 1 :442-:449; worker 2 :332-:340).

## The project's wording beside it (verbatim, file:line at HEAD `d9fc5f0`, block E5; more lines in worker 1 :451-:500 and the addenda)

- `docs/specs/2026-07-16-b2-noise-area-ruleset.md:59`: "Base stop: trailing stop at the opposite Noise-Area boundary ... Evaluated only at semi-hourly stamps."
- `docs/specs/2026-07-16-b2-noise-area-ruleset.md:61`: "... Position closes as soon as price crosses the current band or the VWAP." (VWAP "anchored at the 09:30 open", citing footnote 2.)
- `docs/specs/2026-07-16-b2-noise-area-ruleset.md:38`: "Stops, too, are evaluated only at the semi-hourly stamps (p. 9)."
- `docs/reports/2026-07-16-4uu-noise-area-strategy.md:28`: "Long stop `Max(curUpper, curVwap)`; Short `Min(curLower, curVwap)`; evaluated only at checkpoint | Trailing stop = band-or-VWAP (whichever tighter), at the stamp".
- `docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:129`: "... (clock-anchored, rules-based, one bracket/session)."
- **"The project's research summary":** no file contains the ruling's phrase word for word. The closest candidate is `docs/reports/2026-11-14-r3-recheck-manager.md:9`: "band/VWAP level, checked at HH:00/HH:30 bar closes, market exit | NO" (block E5). Worker 2 found it and worker 4 confirmed it. Other candidates are listed in worker 1 :490-:500 and the Addendum D4 (:616 onward). Which file the ruling meant is **UNVERIFIED**, and I have not chosen one.

## Mismatches between paper and project wording (none judged for trading)

These are worker 1's list (:503-:531) as corrected by the addenda.
1. `compass_artifact...md:42` (an untracked file under `Redemtion/`) says "exit is a hard stop + trailing or time-stop at session end". The paper states no hard stop.
2. One position or trade per session: scope proposal :129 "one bracket/session", the Shortlist RTF :34 and the April plan :255. The paper closes and reverses on a crossover. Spec :38 and 4uu :6 agree with the paper.
3. "VWAP-based" trailing stop (RTF :34 "e.g.", ROUND_2 :93). The paper's stop is band **or** VWAP. VWAP-only is a separate FAQ variant (p. 40).
4. Check times: the bullet on "top/bottom of an hour" was **withdrawn** (Addendum D2, worker 1 :587). Still standing: `compass...md:41` lists decision times 09:30-11:30 only, but the paper trades to 16:00.
5. Timing of the refined stop: spec :38, :59 and 4uu :28 say it is checked only at the stamps. The paper says "as soon as" (p. 13) and gives no interval. Spec :61 copies "as soon as". DECISIONS.md :2844 had already recorded the :59 vs :61 tension.
6. Spec :61 cites footnote 2 for "anchored at the 09:30 open". The footnote says "VWAP is computed only using market hours data. For more details see our previous publication [5]." It says nothing about the anchor (corrected in Addendum D3).
7. Spec :64 cites the Fig. 4 caption for the 16:00 close. That caption does not mention it. Fig. 2 and p. 9 do.
8. Spec :59 "(long stops at Lower/Upper as it trails ...)". This pairing does not appear in the paper (a wording ambiguity).
9. "Whichever is tighter" (spec :60, 4uu :28) is project wording. The paper uses max/min.
10. Out of scope, reported only: spec :95 says the noise multiplier has "no paper analog". The paper's §4.4 does introduce a "Volatility Multiplier".
11. The ruling's premise, "a trailing stop at the band or VWAP, checked at set times, which would mean no fixed maximum loss": the paper supports "band or VWAP" and "no fixed maximum loss stated". "Checked at set times" is explicit only for the base model (see Answer).

## Adversarial findings

- **Worker 2 on worker 1 lines 1-549:** 8 defects, all below verdict level. Among them: a wrong quote preamble, mismatch 4a not being a mismatch, a footnote quoted as "only" one sentence, a missed candidate for the research summary, four omitted passages (p. 30, p. 34, p. 25, p. 40), and overstated or unpasted counts. All were fixed by the worker 3 Addendum.
- **Worker 4 on the Addendum:** 2 defects. A file under the ignored `Redemtion/` folder was labelled "clean at HEAD", and a count of 2 should have been 3. Both were fixed by Addendum 2. It also observed that the p. 2 entry sentence was never quoted, which Addendum 2 fixed.
- **Worker 6 on Addendum 2:** 3 defects: a "0 hits" overstatement and two claims without pasted evidence. All were fixed by Addendum 3, and my re-run is in block M4.
- **Neither verdict ever changed.** Every adversary reached NO on the hard stop and the same timing reading (block E10).
- **Not done:** no worker opened the authors' linked code (p. 30), the SSRN page could not be reached (403), and the SSRN id 4824172 is supported only by the repository's stored filename (block E1).

## S4 and scope disclosures

- **Extra workers.** The brief named two workers. I also ran fix workers 3, 5 and 7 and adversaries 4 and 6 under my standing stress-test contract. The extra workers produced two extra reports (worker 4, worker 6) and three appended sections on the worker 1 report. Nothing earlier in that report was changed. I recorded the pre-append hash of lines 1-549 (block M3) and re-checked it after all three appends (block E6). For lines 1-954 and 1-1062, the pre-append values come from the worker 5 and worker 7 returns. My re-hash after each append matches the value that worker gave (block M4). The only file that was "rewritten" was the worker 1 report's final line: the standing sentence was moved down so that it appears once (block E6, s13=1). No DECISIONS.md entry covers this extension. The master should decide whether it needs one. I did not write one, because this unit decides nothing.
- **A name in this file.** The brief asks for both "no personal names other than the three paper authors" and a final section titled "For the trader". I followed the specific heading instruction. In this file the trader's name appears only in that heading and in this sentence about the heading. Names in pasted output are masked. Block M5 lists the line numbers that match the name grep in the final files. **Open defect, not fixed:** worker 6's report line 46 names the trader once. It lists the names its own privacy grep searched for. The reports are append-only, so I did not edit that line. The master should decide whether to mask it. The other worker reports have no hit (block M5).
- **Untrusted download handling.** The download directories are `/tmp/praxis-npr/dl/w1/` and `/dl/w2/`. The PDF is not in the repo.

## S6 cross-block check

No deviation is approved or proposed. No spec, strategy, code, DECISIONS.md or DECISION_LOG.md line was changed. The staged diff is limited to added report files and added MANIFEST rows (block M5, `--stat`). The read cites Block 2 documents (the b2 ruleset, the 4uu report, the scope proposal) and the 2026-11-14 R3 recheck report, all without editing them. Nothing here touches F3 or F4, and bead 205 was not touched.

## Files staged

The temp index is `/tmp/praxis-npr/idx`, built from `d9fc5f0`. The real index is unchanged: block M1 shows the "before" state and block E11 the "after". Staged: this report, the worker 1, 2, 4 and 6 reports, and MANIFEST.md (HEAD content plus 5 rows). The same 5 rows were appended to the working-tree MANIFEST.md.
```
$ date -u
Sun 15 Nov 2026 17:06:56 UTC
$ GIT_INDEX_FILE=/tmp/praxis-npr/idx git diff --cached --stat d9fc5f0
 MANIFEST.md                                              |    5 +
 docs/reports/2026-11-15-noise-area-paper-read-manager.md |  431 ++++++++++++++++++++++++++++++++++++++++++++++++++++
 docs/reports/2026-11-15-noise-area-paper-read-worker1.md | 1122 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 docs/reports/2026-11-15-noise-area-paper-read-worker2.md |  488 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 docs/reports/2026-11-15-noise-area-paper-read-worker4.md |  550 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 docs/reports/2026-11-15-noise-area-paper-read-worker6.md |  202 ++++++++++++++++++++++++
 6 files changed, 2798 insertions(+)
$ GIT_INDEX_FILE=/tmp/praxis-npr/idx git diff --cached d9fc5f0 -- . ':(exclude)docs/reports/2026-11-15-noise-area-paper-read-manager.md' | shasum -a 256
57f5e839aad754215d74598bcc2d3fdd187d7454b4eb59bb1fe81b913ba8a320  -
$ GIT_INDEX_FILE=/tmp/praxis-npr/idx git diff --cached --name-status d9fc5f0
M	MANIFEST.md
A	docs/reports/2026-11-15-noise-area-paper-read-manager.md
A	docs/reports/2026-11-15-noise-area-paper-read-worker1.md
A	docs/reports/2026-11-15-noise-area-paper-read-worker2.md
A	docs/reports/2026-11-15-noise-area-paper-read-worker4.md
A	docs/reports/2026-11-15-noise-area-paper-read-worker6.md
$ git diff --cached --name-status   (default index, after)
A	docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ for f in <this unit's 5 reports>; grep -n -i -E '<trader first name>|<trader surname>' f | cut -d: -f1   (line numbers only)
2026-11-15-noise-area-paper-read-manager.md: 378 427 
2026-11-15-noise-area-paper-read-worker1.md: 
2026-11-15-noise-area-paper-read-worker2.md: 
2026-11-15-noise-area-paper-read-worker4.md: 
2026-11-15-noise-area-paper-read-worker6.md: 46 
$ staged blobs vs working tree (git hash-object vs index entry)
SAME docs/reports/2026-11-15-noise-area-paper-read-manager.md
SAME docs/reports/2026-11-15-noise-area-paper-read-worker1.md
SAME docs/reports/2026-11-15-noise-area-paper-read-worker2.md
SAME docs/reports/2026-11-15-noise-area-paper-read-worker4.md
SAME docs/reports/2026-11-15-noise-area-paper-read-worker6.md
```
The sha256 of the whole staged diff includes this file, so it cannot be printed inside this file. The hash above covers the staged diff without this file. The full-diff sha256 goes to the master with this report's return.

Result: PASS (the paper read is complete: primary copy obtained, quotes verified by an independent adversary, verdict NO on a stated hard stop; nothing decided)

## For the trader

The paper does not give a hard stop. It never sets a fixed "most you can lose" amount when a trade opens. In its words, positions are closed "at market Close or if there is a crossover to the opposite boundary of the Noise Area." Its improved version closes a trade "as soon as the price crosses either the curent [sic] band or the VWAP" (the day's average traded price). Both of those levels move during the day. On timing, it says "Stop losses can also be triggered only on semi-hourly intervals," but it does not repeat this for the improved version. The authors also say they do not disclose "specific trading rules that we utilize to enhance strategy efficiency," so this answer covers only the rules they printed. Nothing has been retested or decided. What to do next is your call.

## Cure 1 (2026-11-15, after audit FAIL 1)

Authority: DECISION_LOG.md row 2026-11-15T17:18:43Z (WHO: praxis-master), which records audit FAIL 1 and orders this cure. This section is appended; the only edits above it are the three redacted lines in C1 and the removal of the former last line described under "S13 placement". The commands in this section were run in one bash script, and their outputs are pasted as produced. The two greps under "S13 placement" are the exception; they were run after the append.
```
$ R=docs/reports/2026-11-15-noise-area-paper-read
$ date -u
Sun 15 Nov 2026 17:25:21 UTC
$ grep -n '2026-11-15T17:18:43Z' DECISION_LOG.md | cut -c1-120
1007:- [2026-11-15T17:18:43Z] WHO: praxis-master | WHAT: **Audit FAIL 1 for unit `2026-11-15-noise-area-paper-read`** (p
```

### C1. Name redaction (audit finding 2, S4)

Before first commit, the trader's first name and surname were replaced with "the trader" at manager :378, manager :427 and worker 6 :46. The reason: the brief said no personal names other than the three paper authors. This is the same kind of pre-first-commit redaction as DECISION_LOG row 2026-11-15T14:38:00Z item (i). At worker 6 :46 the wording became "the names of the trader (first name and surname), Zarattini, Aziz and Barbon" (" of" and the parenthetical were added for grammar). In the commands below, the name pattern is written `A[m]ear|B[a]ni`. Only line numbers and counts are printed, and the before side of each diff is masked to `[first name]` and `[surname]`.

a) Before: line numbers matching the name pattern in the five reports, from the temp index (the pre-cure staged blobs):
```
$ for f in manager worker1 worker2 worker4 worker6; do printf '%s ' $f; GIT_INDEX_FILE=/tmp/praxis-npr/idx git show :$R-$f.md | grep -n -E 'A[m]ear|B[a]ni' | cut -d: -f1 | tr '\n' ' '; echo; done
manager 378 427 
worker1 
worker2 
worker4 
worker6 46 
```
b) Masked before-vs-after diffs. `/tmp/praxis-npr/cure1/before/` holds the pre-cure copies, which are identical to the temp index blobs. For the manager the diff is limited to lines 1-430, the lines that existed before this section:
```
$ diff <(sed -E 's/A[m]ear/[first name]/g; s/B[a]ni/[surname]/g' /tmp/praxis-npr/cure1/before/worker6.md) $R-worker6.md
46c46
< - Section 955-1063: 0 at-sign characters. The email regex gives exit 1 (no match). A grep for the names [first name], [surname], Zarattini, Aziz and Barbon gives exit 1. The section names no person. The capitalised word pairs it contains are all titles, paths or paper text ("Asset Under").
---
> - Section 955-1063: 0 at-sign characters. The email regex gives exit 1 (no match). A grep for the names of the trader (first name and surname), Zarattini, Aziz and Barbon gives exit 1. The section names no person. The capitalised word pairs it contains are all titles, paths or paper text ("Asset Under").
$ diff <(sed -E 's/A[m]ear/[first name]/g; s/B[a]ni/[surname]/g' /tmp/praxis-npr/cure1/before/manager.md | sed -n '1,430p') <(sed -n '1,430p' $R-manager.md)
378c378
< - **A name in this file.** The brief asks for both "no personal names other than the three paper authors" and a final section titled "For [first name]". I followed the specific heading instruction. In this file the trader's name appears only in that heading and in this sentence about the heading. Names in pasted output are masked. Block M5 lists the line numbers that match the name grep in the final files. **Open defect, not fixed:** worker 6's report line 46 names the trader once. It lists the names its own privacy grep searched for. The reports are append-only, so I did not edit that line. The master should decide whether to mask it. The other worker reports have no hit (block M5).
---
> - **A name in this file.** The brief asks for both "no personal names other than the three paper authors" and a final section titled "For the trader". I followed the specific heading instruction. In this file the trader's name appears only in that heading and in this sentence about the heading. Names in pasted output are masked. Block M5 lists the line numbers that match the name grep in the final files. **Open defect, not fixed:** worker 6's report line 46 names the trader once. It lists the names its own privacy grep searched for. The reports are append-only, so I did not edit that line. The master should decide whether to mask it. The other worker reports have no hit (block M5).
427c427
< ## For [first name]
---
> ## For the trader
```
The hunks are 46c46 only (worker 6), and 378c378 and 427c427 only (manager).

c) After: name-pattern counts in the five reports, case-sensitive and then case-insensitive whole-word:
```
$ grep -c -E 'A[m]ear|B[a]ni' $R-manager.md $R-worker1.md $R-worker2.md $R-worker4.md $R-worker6.md
docs/reports/2026-11-15-noise-area-paper-read-manager.md:0
docs/reports/2026-11-15-noise-area-paper-read-worker1.md:0
docs/reports/2026-11-15-noise-area-paper-read-worker2.md:0
docs/reports/2026-11-15-noise-area-paper-read-worker4.md:0
docs/reports/2026-11-15-noise-area-paper-read-worker6.md:0
$ grep -c -i -w -E 'a[m]ear|b[a]ni' $R-manager.md $R-worker1.md $R-worker2.md $R-worker4.md $R-worker6.md
docs/reports/2026-11-15-noise-area-paper-read-manager.md:0
docs/reports/2026-11-15-noise-area-paper-read-worker1.md:0
docs/reports/2026-11-15-noise-area-paper-read-worker2.md:0
docs/reports/2026-11-15-noise-area-paper-read-worker4.md:0
docs/reports/2026-11-15-noise-area-paper-read-worker6.md:0
```
d) Line counts. Worker 6 has the same line count before and after. The pre-cure manager had 431 lines. Its lines 1-430 differ only at 378 and 427 (diff b); line 431 is covered under "S13 placement".
```
$ wc -l /tmp/praxis-npr/cure1/before/worker6.md $R-worker6.md /tmp/praxis-npr/cure1/before/manager.md
     202 /tmp/praxis-npr/cure1/before/worker6.md
     202 docs/reports/2026-11-15-noise-area-paper-read-worker6.md
     431 /tmp/praxis-npr/cure1/before/manager.md
     835 total
```
e) At-sign counts, before and after, for manager and worker 6. The at-sign is written as the bash octal escape `$'\100'` so that this file gains no at-sign:
```
$ grep -c $'\100' /tmp/praxis-npr/cure1/before/manager.md $R-manager.md /tmp/praxis-npr/cure1/before/worker6.md $R-worker6.md
/tmp/praxis-npr/cure1/before/manager.md:1
docs/reports/2026-11-15-noise-area-paper-read-manager.md:1
/tmp/praxis-npr/cure1/before/worker6.md:0
docs/reports/2026-11-15-noise-area-paper-read-worker6.md:0
```
The counts are unchanged.

Disclosure: line 378 still describes the pre-cure state, and C1 supersedes it in three places. These are its statements about where the name appears, its "Open defect, not fixed" note about worker 6 :46, and its pointer to "Block M5". The file has no block headed M5. The grep below was run before this section was appended, because the section's own pasted output would match the pattern too:
```
$ grep -n -E '\*\*M[0-9]\.' $R-manager.md
40:**M1. Baseline (manager, start of run):**
70:**M2. Manager re-check of worker 1's copy:**
101:**M3. Negative tests: the report-contract gate and the quote checker trip, plus the pre-append worker 1 hashes:**
125:**M4. Manager re-run of the worker 7 Addendum 3 claims:**
```

### C2. Correction for line 372 (audit finding 1, S1/S2)

Line 372 says: "Every adversary reached NO on the hard stop and the same timing reading (block E10)." That sentence is WITHDRAWN. Line 372 is not edited. This correction sits beside it (append-only). Restatement, verbatim: "Workers 1 and 2 each stated NO on a stated hard stop and the same timing reading; workers 4 and 6 checked the addenda and did not state an answer."

Worker 1 (its NO, then its timing reading):
```
$ sed -n '431p' $R-worker1.md
**Hard stop (a fixed maximum loss per trade, known at entry, such as a resting stop order at a set price): NO.** The paper does not specify one.
$ sed -n '442,449p' $R-worker1.md
**Continuous or set times?** For the **base model**, stops are checked at **set times**. The paper says so outright: "Stop losses can also be triggered only on semi-hourly intervals." (Q2, p. 9). Trading generally is "restricted to semi-hourly intervals, specifically at HH:00 and HH:30" (Q1).

For the **refined band-or-VWAP stop** (Q7, p. 13), the check timing is **not restated**:
- The text says "as soon as the price crosses either the curent band or the VWAP, the position is closed." It does not name a checking frequency.
- The p. 9 sentence comes before the refinement is introduced. Its wording does not limit it to the base model, but the paper never explicitly says it applies to the refined stop either.
- The paper's worked exits fall on hour stamps: closed "at 14:00" (Q6) and "at 13:00" (Q7). Those times are consistent with half-hour checks, but they do not prove them.

So: set times are explicit for the base model. For the refined model the text is consistent with set times but not explicit. Separately, the authors say they run "a slightly modified version" live and update signals "at high frequency" (Q11). That describes their live trading, not the rule in the paper.
```
Worker 2 (its NO, then its timing reading):
```
$ sed -n '327p' $R-worker2.md
**Hard stop (a fixed maximum loss per trade known at entry, e.g. a resting stop order at a set price): NO.** This is my own reading and it agrees with the artifact.
$ sed -n '332,340p' $R-worker2.md
**Continuous or set times?**
- **Base model: set times, stated explicitly.** "Stop losses can also be triggered only on semi-hourly intervals." (p9:23-24), next to "trading is restricted to semi-hourly intervals, specifically at HH:00 and HH:30" (p9:15-16).
- **Refined band-or-VWAP stop: UNCLEAR from the text.**
  - The p. 9 sentence is a general strategy statement. It is not labelled base-only, and nothing later revokes it.
  - p. 13 says "as soon as the price crosses ..." and names no frequency.
  - The two worked exits fall on stamps: "closed at 14:00" (p12:13-14) and "close the long exposure at 13:00" (p13:24).
  - The FAQ preface says some trading rules are not disclosed (O1).

  The text is consistent with set-time checking and does not state it for the refined stop. This agrees with the artifact's reading. I add O1 as a further reason the paper alone cannot settle it.
```
Workers 4 and 6, full output:
```
$ grep -n -E 'hard stop|NO\b|UNCLEAR|Answer' $R-worker4.md $R-worker6.md
docs/reports/2026-11-15-noise-area-paper-read-worker4.md:369:| Noise-Area baseline (BandOrVWAP) | band/VWAP level, checked at HH:00/HH:30 bar closes, market exit | NO | −$542.40 | 10 | −$705.10 | 5 |
docs/reports/2026-11-15-noise-area-paper-read-worker4.md:544:2. **S2/S1, D6 (artifact line 806).** "Across line breaks there are two more occurrences ... Neither describes an exit rule." There are three. The Figure 2 caption at p. 9 lines 6-7 ("closed at the market / Close (16:00)") is missed, and it does describe an exit rule. The D6 correction of the earlier statement (2) is therefore itself incomplete. Q3 already quotes the caption, so the Answer is unaffected.
docs/reports/2026-11-15-noise-area-paper-read-worker6.md:41:- (b) "The Figure 2 caption's 16:00 close is already in Q3 and the answer": Q3 (lines 263-275) contains the caption, and the Answer has line 434 "The market Close at 16:00 (Q2, Q3)". CONFIRMED. "as soon as there is an indication ... names no check frequency": p2:25-28 contains no interval. CONFIRMED.
docs/reports/2026-11-15-noise-area-paper-read-worker6.md:188:--- Answer line
```
The brief expected 3 hits. The grep returned 4: worker 4 :369 and :544, and worker 6 :41 and :188. None of them is the worker's own stated answer:
- Worker 4 :369 is output of a command worker 4 ran on another report. Line 368 is the command, `git show d9fc5f0:docs/reports/2026-11-14-r3-recheck-manager.md | sed -n 9p`:
```
$ sed -n '368,369p' $R-worker4.md
$ cd /Volumes/Sensidine/Praxis.build && git show d9fc5f0:docs/reports/2026-11-14-r3-recheck-manager.md | sed -n 9p; git status --short -- docs/reports/2026-11-14-r3-recheck-manager.md; echo '(status output ends)'
| Noise-Area baseline (BandOrVWAP) | band/VWAP level, checked at HH:00/HH:30 bar closes, market exit | NO | −$542.40 | 10 | −$705.10 | 5 |
```
- Worker 4 :544 is item 2 of worker 4's defect list against the artifact it reviewed. "the Answer is unaffected" refers to that artifact's Answer:
```
$ sed -n '540,542p;544p' $R-worker4.md
## Result: FAIL

Defects:
2. **S2/S1, D6 (artifact line 806).** "Across line breaks there are two more occurrences ... Neither describes an exit rule." There are three. The Figure 2 caption at p. 9 lines 6-7 ("closed at the market / Close (16:00)") is missed, and it does describe an exit rule. The D6 correction of the earlier statement (2) is therefore itself incomplete. Q3 already quotes the caption, so the Answer is unaffected.
```
- Worker 6 :41 is worker 6 confirming that the artifact's own Answer has line 434 (full line in the grep output above).
- Worker 6 :188 is a header inside pasted output:
```
$ sed -n '188,189p' $R-worker6.md
--- Answer line
434:  - The market Close at 16:00 (Q2, Q3).
```
The two timing readings agree in substance. Both say the base model's set times are stated ("set times are explicit for the base model", worker 1; "Base model: set times, stated explicitly", worker 2). Both say the refined band-or-VWAP stop's timing is not stated: worker 1 says "consistent with set times but not explicit", and worker 2 says "UNCLEAR from the text" and "does not state it for the refined stop".

### C3. Correction for worker 2 :461 (audit finding 3, check (a))

Worker 2's report is not edited. The line:
```
$ sed -n '461p' $R-worker2.md
- Artifact line 71, "A6 is the authors' firm's web page". The paper links the authors' code to concretumgroup.com (p30:10-11 "We shared the Matlab and Python versions of the code in www.concretumgroup./com/coding"; p33:22). The first author's affiliation is "Concretum Research" (p2:7; p27:27). The artifact pastes none of this. "Firm's web page" is a reasonable inference, but the evidence is not in the artifact (S1).
```
Page and line checks on worker 1's downloaded copy:
```
$ shasum -a 256 /tmp/praxis-npr/dl/w1/paper.pdf
41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad  /tmp/praxis-npr/dl/w1/paper.pdf
$ pdftotext -layout /tmp/praxis-npr/dl/w1/paper.pdf /tmp/praxis-npr/cure1/layout.txt; rm -rf /tmp/praxis-npr/cure1/pages; mkdir -p /tmp/praxis-npr/cure1/pages; awk 'BEGIN{RS="\f"} {f=sprintf("/tmp/praxis-npr/cure1/pages/p%02d.txt",NR); printf "%s", $0 > f; close(f)}' /tmp/praxis-npr/cure1/layout.txt; ls /tmp/praxis-npr/cure1/pages | wc -l
      43
$ grep -n 'Concretum Research' /tmp/praxis-npr/cure1/pages/*.txt
/tmp/praxis-npr/cure1/pages/p01.txt:1:Concretum Research Lugano
/tmp/praxis-npr/cure1/pages/p02.txt:7:1 Concretum Research, Piazza Molino Nuovo 8, 6900 Lugano, Switzerland
/tmp/praxis-npr/cure1/pages/p27.txt:27:             Carlo later established Concretum Research, assisting institu-
/tmp/praxis-npr/cure1/pages/p27.txt:44:             at Concretum Research, and lead developer for the R-Candles
$ cat -n /tmp/praxis-npr/cure1/pages/p02.txt | sed -n '5,10p'
     5	                          Carlo Zarattini1 , Andrew Aziz2,3 , Andrea Barbon4
     6	
     7	1 Concretum Research, Piazza Molino Nuovo 8, 6900 Lugano, Switzerland
     8	2 Peak Capital Trading, 744 West Hastings Street, Vancouver, BC, Canada V6C 1A5
     9	3 Bear Bull Traders, 744 West Hastings Street, Vancouver, BC, Canada V6C 1A5
    10	4 University of St.Gallen, Dufourstrasse 50, 9000 St. Gallen, Switzerland
$ cat -n /tmp/praxis-npr/cure1/pages/p27.txt | sed -n '21,31p'
    21	             Carlo Zarattini, originally from Italy, currently resides in
    22	             Lugano, Switzerland. After completing his mathematics de-
    23	             gree in Padova, he pursued a dual master’s in quantitative
    24	             finance at Imperial College London and USI Lugano. He for-
    25	             merly served as a quantitative analyst at BlackRock, where
    26	             he developed volatility and trend-following trading strategies.
    27	             Carlo later established Concretum Research, assisting institu-
    28	             tional clients with both high and medium-frequency quantita-
    29	             tive strategies in stocks, futures, and options. Additionally, he
    30	             founded R-Candles.com, the first backtester for discretionary
    31	             technical traders.
$ pdftotext -layout -f 2 -l 2 /tmp/praxis-npr/dl/w1/paper.pdf - | grep -n 'Concretum Research'
7:1 Concretum Research, Piazza Molino Nuovo 8, 6900 Lugano, Switzerland
$ pdftotext -layout -f 27 -l 27 /tmp/praxis-npr/dl/w1/paper.pdf - | grep -n 'Concretum Research'
27:             Carlo later established Concretum Research, assisting institu-
44:             at Concretum Research, and lead developer for the R-Candles
$ grep -n 'Concretum Research' /tmp/praxis-npr/cure1/layout.txt
1:Concretum Research Lugano
16:1 Concretum Research, Piazza Molino Nuovo 8, 6900 Lugano, Switzerland
1033:             Carlo later established Concretum Research, assisting institu-
1050:             at Concretum Research, and lead developer for the R-Candles
$ grep -n $'\f' /tmp/praxis-npr/cure1/layout.txt | head -2 | cut -c1-40 | cat -v
10:^L                                 Bea
59:^L1    Introduction
$ pdftotext -f 2 -l 2 /tmp/praxis-npr/dl/w1/paper.pdf - | grep -n 'Concretum Research'
5:1 Concretum Research, Piazza Molino Nuovo 8, 6900 Lugano, Switzerland
```
Correct references, from the output above:
- Under `pdftotext -layout`, page-relative: p1:1, p2:7, p27:27 and p27:44. The split-page grep and pdftotext's own `-f/-l` page selection agree on p2:7, p27:27 and p27:44.
- Worker 2's "p2:7" and "p27:27" are correct page-relative references under `pdftotext -layout`. p27:27 is now checked: it is the author biography line "Carlo later established Concretum Research".
- The audit's "p2:16" is the whole-file line number of the same p. 2 line. Page 2 starts at whole-file line 10 (the line that begins with the form feed, shown as `^L`), so p2:7 is file line 10 + 7 - 1 = 16. The whole-file numbers are 1, 16, 1033 and 1050.
- One more p. 27 occurrence is not cited by worker 2: p27:44 (whole-file 1050), "at Concretum Research, and lead developer for the R-Candles". Worker 2 also did not cite p1:1, the cover line "Concretum Research Lugano".
- Without `-layout`, pdftotext numbers the p. 2 line as 5.

### S13 placement

The standalone S13 line that was line 431 is moved to the end of the file so that it still appears exactly once as a standalone line. These two greps were run after this section was appended, and their output was then written in place of two placeholder lines. The line count did not change:
```
$ S13='Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
$ grep -nxF "$S13" $R-manager.md
652:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
$ grep -cxF "$S13" $R-manager.md
1
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
