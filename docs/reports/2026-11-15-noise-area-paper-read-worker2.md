# Noise-Area paper read: adversarial check of worker 1 (worker 2)

**Unit:** `2026-11-15-noise-area-paper-read`, worker 2. **Mode:** ADVERSARIAL, read-only. **Repo HEAD:** `d9fc5f0`.
**Run window (from `date -u` in the steps below):** 2026-11-15 16:32:04Z to 16:36:11Z.
**Artifact under test:** `docs/reports/2026-11-15-noise-area-paper-read-worker1.md` (550 lines).
**Criteria:** `specs/SPEC_RUBRIC.md` S1, S2, S8, S13.
Nothing staged, nothing committed, no git index touched. This file is the only repo file written. All downloads are in `/tmp/praxis-npr/dl/w2/`, scripts in `/tmp/praxis-npr/scripts-w2/`, my text extraction in `/tmp/praxis-npr/w2-text/`, page-1 render in `/tmp/praxis-npr/w2-img/`. Python was run as `python3 -I -B` only, with paths passed as arguments.

Privacy masking in this report: email addresses and social handles in the paper (p. 2 line 13-14, p. 33, p. 34, p. 35) are not reproduced. Pasted project lines that contain an at-sign show it as `<AT>`. A name inside a pasted ruling record is shown as `[name masked]`. Lines naming cited researchers other than the three authors are not reproduced.

## Task

Try to break worker 1's claims: re-download the paper, re-extract it, re-run the greps, check every quote character by character, hunt for omitted exit/loss/timing passages, re-check the two verdicts, verify the project-side citations and the eleven mismatches, and check for S2 overstatements and privacy leaks. No retest, no decision, no trading judgment.

## Independent fetch (pasted)

Download directory was new and empty. Generic desktop Chrome User-Agent, no other identifying headers.

```
       0                                   <- ls -A /tmp/praxis-npr/dl/w2 | wc -l
Sun 15 Nov 2026 16:32:13 UTC
== B1 unisg
200 https://alexandria.unisg.ch/server/api/core/bitstreams/a99aba00-f967-49b3-aceb-f544dc386e0b/content application/pdf;charset=UTF-8 1901828
== B2 ssrn abstract
403 https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4824172 text/html; charset=UTF-8 5771
== B3 ssrn delivery
403 https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4824172_code5302207.pdf?abstractid=4824172&mirid=1 text/html; charset=UTF-8 5970
HTTP/2 302
location: https://alexandria.unisg.ch/server/api/core/bitstreams/a99aba00-f967-49b3-aceb-f544dc386e0b/content
HTTP/2 200
last-modified: Mon, 10 Mar 2025 13:19:49 GMT
etag: "2168e040467e94d1b36ab83fe9c1fcd2"
content-disposition: inline; filename="ssrn-4824172 (2).pdf"; filename*=UTF-8''ssrn-4824172%20%282%29.pdf
b3.bin:<title>Just a moment...
b2.html:<title>Just a moment...
00000000: 3c21 444f 43                             <!DOC
```
Both SSRN URLs returned 403 with a bot-challenge page, as worker 1 reported. The SSRN id 4824172 is therefore not confirmed from SSRN by me either.

Repository bitstream record, fetched independently (16:35:25Z):
```
200 application/hal+json;charset=UTF-8 1613
{'name': 'ssrn-4824172 (2).pdf', 'sizeBytes': 1901828, 'checkSum': {'checkSumAlgorithm': 'MD5', 'value': '2168e040467e94d1b36ab83fe9c1fcd2'}, 'bundleName': 'ORIGINAL'}
```

## Hash comparison (pasted)

```
Sun 15 Nov 2026 16:32:19 UTC
paper.pdf: PDF document, version 1.5
 1901828 paper.pdf
41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad  paper.pdf
2168e040467e94d1b36ab83fe9c1fcd2
Title:
Subject:
Keywords:
Author:
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.25
CreationDate:    Mon Feb  3 13:01:20 2025 EST
ModDate:         Mon Feb  3 13:01:20 2025 EST
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           43
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       1901828 bytes
Optimized:       no
PDF version:     1.5
cmp: identical (exit 0)
41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad  /tmp/praxis-npr/dl/w1/paper.pdf
sha256 MATCHES artifact claim
```
**Size, SHA-256, MD5 (= repository checksum and ETag), page count and `cmp` against worker 1's copy all match the artifact.**

Cover and title check from my copy (16:33:44Z). Page 1 has no text for the title or series, only the affiliations:
```
--- p1 text:
Concretum Research Lugano
Peak Capital Trading and Bear Bull Traders, Canada
University of St.Gallen and Swiss Finance Institute
--- p2 lines 1-5,16-17:
                                 Beat the Market
            An Effective Intraday Momentum Strategy
                     for S&P500 ETF (SPY)

                          Carlo Zarattini1 , Andrew Aziz2,3 , Andrea Barbon4
                                              First Version: May 10, 2024
                                             This Version: February 3, 2025
--- p2 line 10 (affiliation 4):
4 University of St.Gallen, Dufourstrasse 50, 9000 St. Gallen, Switzerland
--- p2 line 7:
1 Concretum Research, Piazza Molino Nuovo 8, 6900 Lugano, Switzerland
```
I rendered page 1 myself (`pdftoppm -f 1 -l 1 -r 60 -png` to `/tmp/praxis-npr/w2-img/p1-01.png`) and read the image: it shows "Swiss Finance Institute Research Paper Series N°24-97", the title, and the three authors with the affiliations above. This is a visual reading of an image, not pasteable text. It agrees with the artifact.

## Extraction and greps (pasted)

```
Sun 15 Nov 2026 16:32:24 UTC
    1643 paper.txt
5bed406569325f0aa45b92fcf7c09567db20cef2a6414536070db0d982c0b79a  paper.txt
      43
page-03.txt:1:1    Introduction
page-06.txt:1:2    Data
page-06.txt:9:3    Strategy Description
page-17.txt:7:4       Further Investigations
page-17.txt:15:4.1     Market Volatility Regimes
page-18.txt:8:4.2    Daily Patterns
page-20.txt:20:4.3    Day-of-the-Week Effect
page-21.txt:26:4.4    Volatility Multiplier
page-23.txt:1:4.5     Gamma Imbalance
page-24.txt:15:4.6    The Impact of Commissions (and Slippage)
page-26.txt:1:5    Conclusion
page-05 last nonblank:                                              5
page-09 last nonblank:                                                  9
page-20 last nonblank:                                             20
page-43 last nonblank: 43
```
(The heading grep also matched the four affiliation lines on page 2; they are left out here.) My `paper.txt` SHA-256 equals the one worker 1 reported (`5bed4065...b79a`). §3 runs from p. 6 to p. 16, as claimed. The FAQ section starts on p. 30 ("Frequently Asked Questions (FAQs)").

Requested terms, case-insensitive, fixed-string, per page (16:32:32Z; `pNN:line:`):
```
=== 'stop'           [37 hits; same list as the artifact's lines 148-187: p02:30, p09:23, p11:8,20,25, p12:2,12,15,20, p13:1,5,6,12,14,17,19,26,30, p14:1,7,9,20,25, p15:1,7, p16:1,19,25, p17:11, p26:11, p40:1,2,13, p43:4,9]
=== 'stop-loss'      (0 hits)
=== 'stop loss'
p09:23:dence of demand/supply imbalance. Stop losses can also be triggered only on semi-hourly
p11:20, p12:15, p13:5, p13:26, p14:1, p14:9, p14:20, p15:1, p16:1, p16:19, p43:4   (table/figure captions and the p12-p14 text quoted below)
=== 'trailing'       p02:30 p11:8 p12:2 p12:12 p13:5 p13:6 p13:12 p13:14 p13:17 p13:19 p13:30 p17:11 p24:32 p26:11 p40:1 p40:2
=== 'exit'
p12:1:Figure 4: SPY price action on 20 January 2022 illustrates our model strategy's entry and exits. The
p13:5:Figure 5: Improvement in our strategy's exit by incorporating tighter trailing stop losses. In Figure
p22:17:Given the complexity of the decision between higher returns and better risk-adjusted
p40:2:Switching to a VWAP-only trailing stop results in less restrictive exit conditions, leading
=== 'unwound'
p09:20:Positions are unwound either at market Close or if there is a crossover to the opposite
=== 'maximum loss'   (0 hits)
=== 'max loss'
p16:24:                                                 Avg. Trade    Hit    Avg. PnL    Max Loss        Max Gain
=== 'end of day'     (0 hits on one line)
=== 'check'          (0 hits)
=== 'checked'        (0 hits)
=== 'interval'
p03:30:research focusing on daily, weekly, or monthly intervals. However, with the rise of high-
p03:32:in applying momentum strategies to shorter time frames, such as intraday intervals for
p06:22:day time interval over the previous days. We define the Noise Area as the space between
p09:15:caused by short-term market fluctuations, trading is restricted to semi-hourly intervals,
p09:24:intervals.
p21:31:recorded during the same intraday time interval over the previous 14 days. We now intro-
=== 'semi-hourly'
p09:15:caused by short-term market fluctuations, trading is restricted to semi-hourly intervals,
p09:23:dence of demand/supply imbalance. Stop losses can also be triggered only on semi-hourly
=== 'every 30 minutes' (0 hits)
=== 'half-hour'
p03:34:to forecast the final half-hour returns of the S&P 500, highlighting significant intraday
=== 'HH:00'
p09:16:specifically at HH:00 and HH:30. This timing mechanism ensures that decisions are
=== 'HH:30'
p09:16:specifically at HH:00 and HH:30. This timing mechanism ensures that decisions are
=== 'fixed'          (0 hits)
=== 'target'
p14:17: maintaining constant full notional exposure, this method targets a daily market volatility
p15:17:  of 2% (σtarget = 2%). Practically, if the recent daily volatility of SPY is 4%, we would
p15:22:                                     AU Mt−1 × min(4, σtarget /σSP Y,t )
=== 'limit'
p02:25 (limits trading to the last 30 min-), p02:30 (unlimited upside), p04:32, p05:16, p05:17, p20:11, p37:32 (trading limits), p39:6
p09:32:protocol to limit exposure to overnight market changes.
=== 'order'
p20:16:However, in order to exploit higher expected returns, active day traders might consider
p25:5:funded with $100,000, we instruct an algorithm to send market orders on SPY for $100,000
p25:20:orders without significantly impacting the market. For simplicity and consistency with
p25:29:ity. Given the available diversity in commission structures and order methodologies, we
p34:10:and then automatically send orders to Interactive Brokers via IBML, a specialized Mat-
p36:36:their order and the overall participation in market volumes. Mathematically, we can
```
(The 'stop', 'stop loss' and 'limit' blocks are condensed to page:line lists; the full raw output was on screen and the hits are identical to the artifact's lines 148-187 for 'stop'.)

Per-page counts for the remaining terms (16:32:38Z):
```
=== 'close' (count per page)      06:2 07:2 09:5 11:1 12:1 13:3 18:1 19:1 21:2 23:1 37:1
=== 'VWAP' (count per page)       04:1 12:1 13:7 14:3 15:3 16:4 17:1 28:1 40:7 43:3
=== 'boundar' (count per page)    06:1 07:6 08:4 09:3 11:1 12:1 36:1
=== 'noise area' (count per page) 06:3 07:4 09:5 11:2 12:1 13:1 21:1 30:2 31:1 36:1
=== 'risk' (count per page)       02:1 03:1 09:2 12:3 13:1 14:1 15:2 17:2 18:1 20:1 22:3 23:1 37:1 40:1
=== 'sizing' (count per page)     14:1
=== 'leverage' (count per page)   15:2 20:1 37:1 40:1
=== 'band' count per page         11:2 12:1 13:3 14:5 15:5 16:5 17:1 30:2 40:4 43:4
```
No "continuous", "intrabar", "check", "checked", "fixed", "maximum loss", "stop-loss" or "every 30 minutes" anywhere in the 43 pages. "every" has one hit (p30:3, FAQ preface).

## Quote-by-quote verification

Script `/tmp/praxis-npr/scripts-w2/qcheck.py` reads every fenced block in the artifact's "Verbatim quotes" section and tests it against MY per-page text: EXACT = the block's lines equal a run of consecutive raw lines (no stripping at all); NORM = present after joining line-end hyphens and collapsing whitespace.

```
Sun 15 Nov 2026 16:33:28 UTC
block01 Q1 artline246 nlines=6 EXACT=['p9:12-17'] RSTRIP_ONLY=- NORM=['p9']
block02 Q2 artline256 nlines=5 EXACT=['p9:20-24'] RSTRIP_ONLY=- NORM=['p9']
block03 Q3 artline265 nlines=6 EXACT=['p9:27-32'] RSTRIP_ONLY=- NORM=['p9']
block04 Q3 artline273 nlines=3 EXACT=['p9:5-7'] RSTRIP_ONLY=- NORM=['p9']
block05 Q4 artline280 nlines=3 EXACT=['p10:1-3'] RSTRIP_ONLY=- NORM=['p10']
block06 Q5 artline288 nlines=4 EXACT=['p11:6-9'] RSTRIP_ONLY=- NORM=['p11']
block07 Q5 artline294 nlines=6 EXACT=['p11:12-17'] RSTRIP_ONLY=- NORM=FAIL
block08 Q5 artline302 nlines=2 EXACT=['p12:7-8'] RSTRIP_ONLY=- NORM=['p12']
block09 Q5 artline307 nlines=3 EXACT=['p12:1-3'] RSTRIP_ONLY=- NORM=['p12']
block10 Q6 artline314 nlines=12 EXACT=['p12:11-22'] RSTRIP_ONLY=- NORM=['p12']
block11 Q7 artline330 nlines=2 EXACT=['p12:25-26'] RSTRIP_ONLY=- NORM=FAIL
block12 Q7 artline334 nlines=9 EXACT=['p13:11-19'] RSTRIP_ONLY=- NORM=['p13']
block13 Q7 artline345 nlines=5 EXACT=['p13:23-27'] RSTRIP_ONLY=- NORM=['p13']
block14 Q7 artline352 nlines=1 EXACT=['p13:35-35'] RSTRIP_ONLY=- NORM=['p13']
block15 Q7 artline356 nlines=4 EXACT=- RSTRIP_ONLY=- NORM=['p13']
block16 Q8 artline364 nlines=11 EXACT=['p14:7-17'] RSTRIP_ONLY=- NORM=['p14']
block17 Q8 artline377 nlines=2 EXACT=['p15:17-18'] RSTRIP_ONLY=- NORM=['p15']
block18 Q8 artline381 nlines=3 EXACT=['p15:34-36'] RSTRIP_ONLY=- NORM=['p15']
block19 Q9 artline388 nlines=13 EXACT=['p16:24-36'] RSTRIP_ONLY=- NORM=['p16']
block20 Q10 artline406 nlines=5 EXACT=['p17:8-12'] RSTRIP_ONLY=- NORM=['p17']
block21 Q11 artline415 nlines=5 EXACT=['p34:7-11'] RSTRIP_ONLY=- NORM=['p34']
block22 Q12 artline424 nlines=3 EXACT=['p40:1-3'] RSTRIP_ONLY=- NORM=['p40']
```
The two NORM=FAIL rows are an artefact of my normaliser, not a quote error: both blocks end on a split word ("This sce-", "imbal-"), which in the page continues on the next line, so the joined text reads "scenario"/"imbalance" and the dangling "sce-" no longer appears. Both pass EXACT. Block 15 (Figure 5 caption) is a declared splice of line 1 and lines 5-7; it cannot match EXACT by construction and passes NORM. Raw lines for the two most load-bearing quotes, from my copy (p. 9 and p. 13, `cat -n`):
```
    20	Positions are unwound either at market Close or if there is a crossover to the opposite
    21	boundary of the Noise Area. In the event of such a crossover, the existing position is
    22	closed, and a new one is initiated in the opposite direction to align with the latest evi-
    23	dence of demand/supply imbalance. Stop losses can also be triggered only on semi-hourly
    24	intervals.
...
    12	VWAP as a trailing stop for intraday trend exposures2 . Once a position is established,
    13	as soon as the price crosses either the curent band or the VWAP, the position is closed.
    14	Mathematically, the trailing stops for long and short postions are defined as:
...
    34	   2
    35	       VWAP is computed only using market hours data. For more details see our previous publication [5].
```

| Quote | Claimed place | Found (my copy) | Text | Page/section |
|---|---|---|---|---|
| Q1 | §3 p9 12-17 | p9:12-17 | PASS | PASS |
| Q2 | §3 p9 20-24 | p9:20-24 | PASS | PASS |
| Q3 | §3 p9 27-32; Fig 2 cap 5-7 | p9:27-32; p9:5-7 | PASS | PASS |
| Q4 | §3 p10 1-3 (+ formula 6-8) | p10:1-3 | PASS | PASS |
| Q5 | §3 p11 6-9, 12-17; p12 7-8; Fig 4 cap p12 1-3 | same | PASS | PASS |
| Q6 | §3 p12 11-22 | p12:11-22 | PASS | PASS |
| Q7 | §3 p12 25-26; p13 11-19, 23-27, fn 35; Fig 5 cap 1, 5-7 | same | PASS | PASS |
| Q8 | §3 p14 7-17; p15 17-18, 34-36 | same | PASS | PASS |
| Q9 | §3 Table 4 p16 24-36; inline p10 31-33 | same | PASS | PASS |
| Q10 | §4 p17 8-12 | p17:8-12 | PASS | PASS |
| Q11 | FAQ Q11 p34 7-11 | p34:7-11 | PASS | PASS |
| Q12 | FAQ Q22 p40 1-3 | p40:1-3 | PASS | PASS |

All 22 blocks are character-exact, including the paper's typos "curent" and "postions". Q9's inline quote matches p10:31-33 as rendered in the artifact. **But the preamble to the quotes is wrong** (see defect 1):
```
Sun 15 Nov 2026 16:35:25 UTC
--- line-end hyphens inside Verbatim section (art lines 240-428):
246: ...the Noise Area, our strat-
258: ...align with the latest evi-
289: ...ysts that can provoke dra-
299: ...active strategy. This sce-
324: ...ring that the strategy re-
331: ...n the demand-supply imbal-
345: ... January 20, 2022. Includ-
347: ... showcasing VWAP's effi-
365: ...9) and the worst daily re-
406: ...s we have conducted in or-
418: ...a IBML, a specialized Mat-
--- 'con-' occurrences in verbatim section:
--- lines starting with a reading/rejoined line in section (e.g. 'Reading:'):
3:These are copied character for character ... rejoined only in the reading line under each quote: ... "con-/ducted" to "conducted". ...
```
The preamble says split words are "rejoined only in the reading line under each quote", but no quote has a reading line under it. Its list names "con-/ducted", which occurs in no quote (it is p13:30-31, outside Q7's lines), and leaves out four splits that do occur: "Includ-/ing" (Q7), "re-/turn" (Q8), "or-/der" (Q10), "Mat-/lab" (Q11). The quotes themselves are unaffected.

## Omissions found

Passages that bear on exits, loss limits, check timing or order type, and that the artifact does not quote. None of them changes the hard-stop answer. Item O1 changes how far the paper can be read as a complete rulebook.

O1. **FAQ preface, p. 30 lines 1-7: the authors say they withhold some trading rules.** (16:33:44Z)
```
Frequently Asked Questions (FAQs)
Following the publication of this paper, we received hundreds of insightful questions
from readers. While we are unable to address every inquiry—particularly those requiring
significant extensions of our research or the disclosure of specific trading rules that we
utilize to enhance strategy efficiency—we have compiled answers to the most common
questions. This section will be updated regularly to include new Q&As that may arise
in the future.
```
The artifact's only mention of this page is a grep hit on the word "every" (its line 229). It does not quote the "disclosure of specific trading rules" sentence.

O2. **FAQ Q11, p. 34 lines 3-5, the lines before the artifact's Q11 quote:**
```
Yes, but please note that this is a simplified model that can be further enhanced with
a few small adjustments. The goal of our papers is not to provide ready-to-use trading
strategies, but rather to introduce traders and readers to potential trading edges.
```

O3. **§4.6, p. 25 lines 5-8 and 20-22: how executions are modelled.** The artifact quotes only line 5, as a grep hit:
```
     5	funded with $100,000, we instruct an algorithm to send market orders on SPY for $100,000
     6	just a few milliseconds before the start of minute HH:MM. The algorithm randomly
     7	takes long or short positions. The goal of the study is to evaluate the magnitude of the
     8	slippage relative to the Open price of minute HH:MM. Mathematically, we evaluate the
    ...
    20	orders without significantly impacting the market. For simplicity and consistency with
    21	our real-trading analysis, we have chosen to apply a standard slippage rate of $0.001 in
    22	our backtest.
```
The study is of randomly placed market orders. Slippage is measured against the open of minute HH:MM, and its result is applied to all backtest fills. This is the only text on order type and fill pricing in the paper. It names market orders, not resting stop orders. I am not inferring the strategy's own order type from it.

O4. **Trade count is inconsistent inside the paper.** FAQ Q22, p. 40 lines 3-5, the sentence the artifact's Q12 cuts at "Consequently, the number":
```
of trades decreases significantly from 7,964 (for the VWAP + Current Band version) to
6,728 (for the VWAP-only version). This reduction in trade frequency may enhance cost
```
Table 4 on p. 16 gives 7,668 for "Curr.Band + VWAP" (`Intra Mom.   Curr.Band + VWAP    100%   7,668       1.8 ...`). The artifact uses 7,668 (Q8) and does not note the 7,964. This is not an exit rule. I report it so that the "1.8 trades per day" figure is not treated as settled by the paper alone.

O5. **p. 8 lines 10-14, about band width, is paraphrased without quotation.** The artifact's line 437 says "p. 8 says the bands widen through the day". The text says "Typically, the average intraday movement from the Open tends to increase over time, peaking at 16:00" (p8:13-14). The paraphrase drops "Typically".

Searched and found nothing further: the whole FAQ (Q1-Q25, pp. 30-42) has no answer on stop orders, maximum loss or intraday checking frequency. FAQ Q13 (p. 35) says only "We applied the same rules to 33 different futures markets" and gives no exit detail. Footnote 1 (p. 10) points to §4.6. There is no "check", "continuous", "intrabar", "fixed", "maximum loss" or "every 30 minutes" anywhere (grep above).

## Verdict re-check (hard stop; timing)

**Hard stop (a fixed maximum loss per trade known at entry, e.g. a resting stop order at a set price): NO.** This is my own reading and it agrees with the artifact.
- The exits the paper states are three. The market Close: "Positions are unwound either at market Close or if there is a crossover to the opposite boundary of the Noise Area" (p9:20-21). The opposite-boundary crossover in the same sentence. And the refined stop: "Long TrailingStopt,HH:M M = max(U Bt,HH:M M , V W APt,HH:M M )" with "as soon as the price crosses either the curent band or the VWAP, the position is closed" (p13:13-19).
- The stop levels are indexed by time `t,HH:MM` and include VWAP, so they move after entry. No passage sets a price or loss amount at entry. "fixed", "maximum loss" and "stop-loss" have 0 hits. The only order-type text is the market-order slippage study (O3).
- "Max Loss Trade" (p16:24) is a backtest outcome column: -8.6%, -4.0% and -2.9% by variant.

**Continuous or set times?**
- **Base model: set times, stated explicitly.** "Stop losses can also be triggered only on semi-hourly intervals." (p9:23-24), next to "trading is restricted to semi-hourly intervals, specifically at HH:00 and HH:30" (p9:15-16).
- **Refined band-or-VWAP stop: UNCLEAR from the text.**
  - The p. 9 sentence is a general strategy statement. It is not labelled base-only, and nothing later revokes it.
  - p. 13 says "as soon as the price crosses ..." and names no frequency.
  - The two worked exits fall on stamps: "closed at 14:00" (p12:13-14) and "close the long exposure at 13:00" (p13:24).
  - The FAQ preface says some trading rules are not disclosed (O1).

  The text is consistent with set-time checking and does not state it for the refined stop. This agrees with the artifact's reading. I add O1 as a further reason the paper alone cannot settle it.

## Project-side verification

Cited lines printed with `sed -n` (16:33:54Z, HEAD `d9fc5f0`). Each cited line matches the artifact's quote. The artifact's `...` elisions on :99 and scope :129 are disclosed.
```
docs/specs/2026-07-16-b2-noise-area-ruleset.md:36: - **Entry condition:** at a **semi-hourly checkpoint only** — `HH:00` and `HH:30` — ... (Fig. 2, p. 9).
docs/specs/2026-07-16-b2-noise-area-ruleset.md:38: ... Stops, too, are evaluated only at the semi-hourly stamps (p. 9).
docs/specs/2026-07-16-b2-noise-area-ruleset.md:50: | Stop-ATR | **not used** — there is no ATR-based stop anywhere in the paper | — |
docs/specs/2026-07-16-b2-noise-area-ruleset.md:57: ## 4. Exit policy + session-flat — PAPER-VERIFIED (§3, pp. 9–14)
docs/specs/2026-07-16-b2-noise-area-ruleset.md:59: - **Base stop:** trailing stop at the **opposite** Noise-Area boundary (long stops at Lower/Upper as it trails; base model = "Stop <AT> Opp. Band", Table 1). Evaluated only at semi-hourly stamps.
docs/specs/2026-07-16-b2-noise-area-ruleset.md:60: - **Improved stop (paper's preferred model):** trailing stop at **band-or-VWAP**, whichever is tighter to price:
docs/specs/2026-07-16-b2-noise-area-ruleset.md:61:   `Long TrailingStop = max(UpperBound, VWAP)` ; ... VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.
docs/specs/2026-07-16-b2-noise-area-ruleset.md:64: - **Session flat:** **all positions closed at the market Close = 16:00 ET** (cash close), never held overnight (Fig. 2 caption p. 9; Fig. 4 p. 12). ...
docs/specs/2026-07-16-b2-noise-area-ruleset.md:77: | D6 | Exit stop | opposite band, or `max/min(band, VWAP)` (pp. 9,13) | RTF: "VWAP trailing stop" | ⚠️ Partial — ...
docs/specs/2026-07-16-b2-noise-area-ruleset.md:84: ... (c) a tunable "noise multiplier" and "stop-ATR" (D1, §3 — the paper has neither).
docs/specs/2026-07-16-b2-noise-area-ruleset.md:95: | **noise multiplier** | **no paper analog** (`k = 1.0`) | ...
docs/specs/2026-07-16-b2-noise-area-ruleset.md:99: Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = max/min(Open_{9:30}, PrevClose)`; VWAP anchored at 09:30, market-hours only; **flat at 16:00** (or the trader-chosen 11:30 — see D8). Entry via ...
docs/reports/2026-07-16-4uu-noise-area-strategy.md:6: **Trader locks (DECISION_LOG 2026-07-16, session 16):** 16:00 ET flat; reverse-on-opposite-cross; pure paper replication with FIXED params (Lookback=14, band=1×σ, no ATR stop); ExitMode is the only knob.
docs/reports/2026-07-16-4uu-noise-area-strategy.md:25: | `isCheckpoint = (min==0 || min==30) && OpenMod<mod<CloseMod` | Act only at HH:00 / HH:30 stamps | §2 p.9 |
docs/reports/2026-07-16-4uu-noise-area-strategy.md:28: | Long stop `Max(curUpper, curVwap)`; Short `Min(curLower, curVwap)`; evaluated only at checkpoint | Trailing stop = band-or-VWAP (whichever tighter), at the stamp | §4 p.9,13 |
docs/reports/2026-07-16-4uu-noise-area-strategy.md:29: | `ExitMode==OppBand` → stop = band only | Base "Stop <AT> Opp. Band" variant | §4 p.9 / Table 1 |
docs/reports/2026-07-16-4uu-noise-area-strategy.md:30: | `mod >= CloseMod → FlattenAll(); return` | 16:00 ET cash-close flat, no new entry at/after close | §4 p.9,12; trader lock |
scope:129: **Answer:** The strategy under test is the **Zarattini–Aziz–Barbon NQ "Noise-Area" intraday breakout** (clock-anchored, rules-based, one bracket/session). ...
14:| Code block (PraxisNoiseAreaBreakout.cs) | Implements | Spec § / paper page |      <- 4uu table header, confirms "§4" = spec §4
```
DECISIONS / DECISION_LOG / voice notes (16:34:04Z):
```
--- DECISIONS.md:2822
The agent answered yes and noted the source paper (Zarattini, Aziz and Barbon) appears to use an interval-checked trailing exit at band/VWAP and no hard stop, so a hard stop is a new variable. ...
--- DECISIONS.md:2839
... Before anything else, confirm from the original paper (Zarattini, Aziz and Barbon, "Beat the Market", Swiss Finance Institute 24-97) whether the Noise-Area strategy has a hard stop. The project's research summary says it uses a trailing stop at the band or VWAP, checked at set times, which would mean no fixed maximum loss. Report what the paper actually says, with the exact wording, before any retest. If a source spec has no stop, don't decide anything: bring it back to me.
--- DECISIONS.md:2844
- D1, the exit. ... The tested Noise-Area exits are checked at HH:00/HH:30 bar closes (`docs/reports/2026-11-14-r3-recheck-manager.md` :9-:11 at HEAD), and the ruleset records the paper's trailing stop as "Evaluated only at semi-hourly stamps" (... :59 at HEAD). ... The ruleset can be read two ways on whether the exit is interval-checked (only at the :48 stamps, per :59, or as soon as price crosses, per :61); ...
--- DECISION_LOG.md:994
- [2026-11-15T14:37:18Z] WHO: [name masked] | WHAT: **[name masked]'s typed Q6 ruling in the master session** ... Verbatim: "... The project's research summary says it uses a trailing stop at the band or VWAP, checked at set times, which would mean no fixed maximum loss. ..."
--- voice:92
The agent answered yes and noted the source paper (Zarattini, Aziz and Barbon) appears to use an interval-checked trailing exit at band/VWAP and no hard stop, so a hard stop is a new variable. ...
 M DECISIONS.md
 M DECISION_LOG.md
?? docs/reports/2026-11-15-voice-notes-open-questions.md
```
Redemtion files (16:34:23Z):
```
--- VTS:34
**1. Mechanical description.** At each clock half-hour or hour, two boundaries ("noise band") are drawn around the day's open. ... When price breaches the upper (lower) boundary at the top/bottom of an hour, a long (short) position is opened. The position uses dynamic trailing stops (e.g., VWAP-based) and is flat at the cash close. One position per session; ... either price has closed beyond the band at the half-hourly check or it has not.\
--- VTS:45
... exits are programmatic (trailing stop, EOD flat, or band reversion).\
--- PLAN:255
**What it is:** At each half-hour or hour, two boundaries ("noise band") are drawn around the day's open. When price breaches the boundary, a position opens. Trailing stop, flat at close. One trade per session. ...
--- ROUND2:93
- **Implications for Strategy #1 (Noise-Area Breakout).** Strategy #1 uses dynamic trailing stops (VWAP-based) and EOD-flat exits. ...
--- compass:41
- Decision is made **at fixed wall-clock times** (09:30, 10:00, 10:30, 11:00, 11:30 ET) on bar close, not intra-bar.
--- compass:42
- Entry can be a stop-market or stop-limit at the noise boundary; exit is a hard stop + trailing or time-stop at session end.
```
Every Redemtion line the artifact quotes matches.

**A better candidate for "the project's research summary" was missed.** The ruling's phrase is "a trailing stop at the band or VWAP, checked at set times, which would mean no fixed maximum loss". The 2026-11-14 R3 recheck manager report, filed in HEAD commit `d9fc5f0` and cited by `DECISIONS.md:2844`, says almost exactly that (16:34:12Z):
```
| strategy | stop rule as coded/written | max loss known before entry? | largest loss | ...
| Noise-Area baseline (BandOrVWAP) | band/VWAP level, checked at HH:00/HH:30 bar closes, market exit | NO | −$542.40 | 10 | −$705.10 | 5 |
```
(`docs/reports/2026-11-14-r3-recheck-manager.md:9`). Another close match is `docs/specs/2026-11-06-walk-forward-values.md:63`: "BandOrVWAP — OBSERVED (code): ... at HH:00/HH:30 checkpoints, a long exits when `Close <= max(UpperBound, VWAP)` ...". Neither file is in the artifact's candidate list (its lines 490-500). The artifact's search pattern `set times|interval-checked|checked at (fixed|set|the half)` cannot match "checked at HH:00". The artifact keeps the attribution UNVERIFIED, so this is an omission and not an overclaim. I also do not assert which file the ruling meant: UNVERIFIED.

Citation-count claim (artifact line 34, "matched 60 files"), 16:34:59Z and 16:35:08Z:
```
75     <- /usr/bin/grep -rIl ... --exclude-dir=.git
89     <- /usr/bin/grep -rIl ... (including .git)
NEWER: ./docs/reports/2026-11-15-noise-area-paper-read-worker1.md
74     <- files older than 16:25Z
/bin/zsh
grep is a shell function from /Users/admin/.claude/shell-snapshots/snapshot-zsh-...sh
61     <- zsh shell-function grep (includes the artifact itself)
53     <- git grep -l
```
The "60" reproduces only with the zsh `grep` shell function, which skips some files. `/usr/bin/grep` finds 74 files that existed before the artifact's run. The artifact gives the count without pasted output and without naming the tool.

## Mismatch-list check

| # | Artifact claim | Check against quotes above | Verdict |
|---|---|---|---|
| 1 | compass:42 says "hard stop"; paper states none | compass:42 matches; paper has 0 "fixed"/"maximum loss" | ACCURATE |
| 2 | scope:129, VTS:34, PLAN:255 say one per session; paper reverses; 1.3-1.8 trades/day | lines match; p9:20-22; Table 4 1.3/1.8 | ACCURATE. The 1.8 rests on Table 4's 7,668, which FAQ Q22 contradicts with 7,964 (O4). "'Bracket' also implies a resting stop-and-target order pair" is the artifact's own reading of a project word |
| 3 | VTS:34 / ROUND2:93 say VWAP-based; paper is band-or-VWAP | lines match. VTS:34 says "e.g., VWAP-based", which offers VWAP as an example, not as the only stop | MOSTLY ACCURATE; weak as a "mismatch" for VTS:34 |
| 4 | VTS:34 "at the top/bottom of an hour" vs paper HH:00 and HH:30 | "Top/bottom of the hour" is ordinary wording for :00 and :30, and VTS:34 itself opens "At each clock half-hour or hour" and ends "at the half-hourly check" | **FIRST BULLET INACCURATE**: the line agrees with the paper. Second bullet (compass:41 lists 09:30-11:30 only; paper trades to 16:00) ACCURATE |
| 5 | refined-stop check timing: project says "stamps", paper says "as soon as" | spec :38/:59, 4uu :28, voice :92 match; p13:13 | ACCURATE. `DECISIONS.md:2844` had already recorded the same :59 vs :61 tension; the artifact does not note that |
| 6 | spec :61 "anchored at the 09:30 open" not in footnote 2; "The footnote text is only 'VWAP is computed only using market hours data.'" | footnote p13:35 has a second sentence, "For more details see our previous publication [5]." | MAIN POINT ACCURATE, **QUOTE INCOMPLETE** ("only" is false). The same anchor wording recurs at spec :99, inside the text the artifact elided as "not about the stop" |
| 7 | spec :64 cites Fig. 4 p. 12 for 16:00; caption has no 16:00 | p12:1-3 confirmed | ACCURATE |
| 8 | spec :59 "Lower/Upper" pairing not in paper | p11:16-17 names Lower Boundary for a long | ACCURATE, flagged as ambiguity |
| 9 | "whichever is tighter" is project wording | p13:17-19 max/min | ACCURATE |
| 10 | spec :95/:84 "no paper analog" vs §4.4 VM | p21:26-43 confirmed (below) | ACCURATE |
| 11 | ruling premise vs paper | DECISIONS:2839 matches; p9:23-24, p13:13 | ACCURATE |

p. 21 check for item 10 (16:34:46Z):
```
4.4    Volatility Multiplier
...
duce a parameter we term as the Volatility Multiplier (VM), which adjusts the width of
the Noise Area, making the model either more conservative (for values above 1) or more
...
   UpperBoundt,HH:MM = max Opent,9:30 , Closet−1,16:00 × (1 + VM × σt,9:30−HH:MM )
```

## S2 and privacy findings

Privacy (16:34:46Z and 16:34:59Z):
```
--- emails in artifact:
       0
--- at-sign count:
       2
461:59: - **Base stop:** ... base model = "Stop <AT> Opp. Band", Table 1
477:29:| `ExitMode==OppBand` → stop = band only | Base "Stop <AT> Opp. Band" variant | §4 p.9 / Table 1 |
0      <- count of artifact lines naming the trader or any cited researcher other than the three authors
```
There are no email addresses. The two at-signs are inside pasted project lines, not addresses. The capitalised-pair scan found no personal names other than the three authors. The trader is not named. **No privacy defect.**

S2 / S1 findings:
- Artifact line 75, "the University of St. Gallen institutional repository, where the third author is affiliated". This is true per p2:10 and the p. 1 text pasted above, but the artifact pastes neither the affiliation line nor any page-1 text. Its page-2 excerpt deliberately leaves out lines 7-14. It is an S1 gap: the claim is correct, but its evidence is not in the artifact.
- Artifact line 71, "A6 is the authors' firm's web page". The paper links the authors' code to concretumgroup.com (p30:10-11 "We shared the Matlab and Python versions of the code in www.concretumgroup./com/coding"; p33:22). The first author's affiliation is "Concretum Research" (p2:7; p27:27). The artifact pastes none of this. "Firm's web page" is a reasonable inference, but the evidence is not in the artifact (S1).
- Artifact line 190: "For pages 18 and later ... all omitted hits are table rows or the Concretum Bands indicator FAQ." This is false (16:35:32Z). Omitted prose hits include p18:33, p19:23, p19:26, p21:33/41/43 (§4.4 formula), p23:23, p28:16 (reference), p31:41, p36:2, p37:48-49 ("they resume strongly from 14:00 until market / close"), p40:5. None of these changes the exit reading. The sentence still overstates the filter (S2).
- Artifact line 190: "'end of day' and 'market close' had 0 hits as phrases. The only close-time wording is 'market Close' (p. 9)." Both phrases occur split across a line: "at the end / of day t − 1" (p10:11-12, about AUM) and "until market / close" (p37:48-49, FAQ Q18). The "0 hits" applies only to single-line grep, and "the only" overstates (S2, low materiality).
- Artifact lines 231-237: the "order / limit / fixed" block shows 4 lines as the grep output. The pattern returns more lines (p20:16, p25:20, p25:29, p36:36 and the 'limit' hits listed above), and the block does not say it is an excerpt (S1, low materiality).
- S8: the artifact answers only the question the ruling posed (what the paper says). It keeps the ruling's source UNVERIFIED, makes no trading judgment and recommends nothing. **No S8 defect found.**
- S13 (16:36:11Z): the standing sentence appears exactly once, as the last line.
```
1
[tail -n 1 output: the standing sentence, verbatim; not repeated here so that this report contains it exactly once]
```

## Result

**Hard-stop verdict, own reading: NO** (agrees with the artifact). **Timing:** set times explicit for the base model (p9:23-24). **UNCLEAR** for the band-or-VWAP stop (p13:13 "as soon as"; worked exits at 13:00/14:00; FAQ preface withholds some rules). This agrees with the artifact. **Hash: match** (1901828 bytes, sha256 `41d635d1...07ad`, MD5 = repository checksum, `cmp` identical to worker 1's copy). **All 22 quote blocks (Q1-Q12) are character-exact on the claimed page and lines.**

Defects found in the artifact. None of them reverses either verdict.
1. **Quote preamble misdescribes the quotes** (artifact line 242). It promises a rejoined "reading line under each quote", and none exists. Its rejoin list names "con-/ducted", which is in no quote, and omits "Includ-/ing", "re-/turn", "or-/der" and "Mat-/lab", which are.
2. **Mismatch 4, first bullet, is not a mismatch.** VTS:34 "top/bottom of an hour" means :00/:30, and the same line says "At each clock half-hour or hour" and "the half-hourly check".
3. **Mismatch 6 misquotes footnote 2 as "only"** one sentence. The footnote also says "For more details see our previous publication [5]." The spec :99 elision (artifact line 470, "not the stop") hides the same "VWAP anchored at 09:30" wording.
4. **Missed candidate for "the project's research summary".** `docs/reports/2026-11-14-r3-recheck-manager.md:9` ("band/VWAP level, checked at HH:00/HH:30 bar closes, market exit | NO") is the closest match, and `docs/specs/2026-11-06-walk-forward-values.md:63` is another. Neither is listed, and the search pattern could not find them. (Attribution stays UNVERIFIED.)
5. **Omitted relevant passages:** the FAQ preface on withheld "specific trading rules" (p30:3-5), the "simplified model" caveat (p34:3-5), the market-order / minute-open fill model (p25:5-8, 20-22), and the 7,964 vs 7,668 trade-count conflict (p40:4 vs p16).
6. **S2 overstatement at artifact line 190:** "all omitted hits are table rows or the Concretum Bands indicator FAQ" is false. "'end of day' and 'market close' had 0 hits" and "the only close-time wording" ignore line-split occurrences (p10:11-12, p37:48-49).
7. **S1 gaps:** the St. Gallen affiliation (line 75), "authors' firm's web page" (line 71), "matched 60 files" (line 34; `/usr/bin/grep` gives 74 pre-existing files, and 60 reproduces only with the zsh grep function), and the order/limit grep block (lines 231-237) are stated without pasted supporting output, or as an unlabelled excerpt. The affiliation and firm claims are true per my pasted text.
8. Minor: "p. 8 says the bands widen through the day" (line 437) drops the paper's "Typically" (p8:13).

No privacy defect, no S8 defect, S13 satisfied. Result for the adversarial task: **BREAKS FOUND (8 defects, all below verdict level).**

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
