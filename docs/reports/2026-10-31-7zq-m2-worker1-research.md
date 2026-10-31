# 7zq M2 worker 1 — research process log

## Task
Find three published, NQ-applicable intraday strategies (not Noise-Area, not cross-sectional), then score, rank and spec them. Deliverable: `docs/reports/2026-10-31-7zq-m2-shortlist.md`.

## Mode
BUILD (research). Unit `Praxis_build-7zq`, phase M2, worker 1. Date 2026-10-31.

## Criterion
The brief's deliverables: three specs with sources and sha256 hashes, rule steps, verbatim page-cited results, the NQ 1-min mapping, open questions, a 0–3 score table on (a)–(e), a ranking, "Pick = #1", a NEEDS AMEAR section, and S1 evidence (curl status lines, shasum lines, greps).

## Process log
`$B` = `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/m2-research`. Every download went into its own fresh subdirectory. Helper scripts (`oa.py`, `pg.py`) were kept in the parent scratchpad, outside every download directory, and run with `python3 -I`. `pg.py` counts `\f` form feeds before a regex match to get the PDF page.

### Turn 1: search (DuckDuckGo failed, arXiv worked)
```
202 text/html; charset=UTF-8 14328      (DDG gao — 202 = bot interstitial, no result links)
202 text/html; charset=UTF-8 14334      (DDG baltussen)
202 text/html; charset=UTF-8 14352      (DDG orb)
200 application/atom+xml; charset=utf-8 10152   (arXiv all:"intraday momentum")
    <id>http://arxiv.org/abs/2605.04004v3</id>
    <title>Structural Limits of OHLCV-Based Intraday Momentum Signals in MNQ Futures: A Systematic Falsification Study</title>
```
**Failed:** DuckDuckGo returned 202 with no results.

### Turns 2–3: Bing (failed, junk results)
```
200 text/html; charset=utf-8 123038 / 122472 / 119826
== bing-balt  <cite>https://biologyinsights.com › are- ...   (irrelevant)
== bing-orb   <cite>https://www.zhihu.com / github.com / reddit.com
```
**Failed:** no PDF links.

### Turn 4: OpenAlex (worked)
```
q1 200 application/json 33863 ... q5 200 application/json 44843
- 2018 Market intraday momentum | Journal of Financial Economics | https://doi.org/10.1016/j.jfineco.2018.05.009
     https://doi.org/10.2139/ssrn.2440866
- 2021 Hedging demand and market intraday momentum | Journal of Financial Economics | https://doi.org/10.1016/j.jfineco.2021.04.029
     https://pure.eur.nl/en/publications/21e7c79f-78ae-4e12-a1ab-e34686d78908
- 2023 Can Day Trading Really Be Profitable? | SSRN Electronic Journal | https://doi.org/10.2139/ssrn.4416622
- 2019 Assessing the Profitability of Timely Opening Range Breakout on Index Futures Markets | IEEE Access | https://doi.org/10.1109/access.2019.2899177
     https://ieeexplore.ieee.org/ielx7/6287639/8600701/08641124.pdf
```

### Turn 5: landing pages and the IEEE PDF
```
eur 200 text/html;charset=UTF-8 44484
zhou 404 text/html 1245                         (apps.olin.wustl.edu/faculty/zhou/ — FAILED)
ieee 200 application/pdf 8930514
arxiv 200 text/html; charset=utf-8 41419
concretum 200 text/html; charset=UTF-8 63351    (no ORB/PDF links found)
href="/files/58145484/1_s2.0_S0304405X21001598_main.pdf"
.../ieee-orb/paper.pdf: PDF document, version 1.5, 6 pages
```
arXiv 2605.04004 metadata (OBSERVED): `citation_author "Mesfin, Mathias"`, `citation_date "2026/05/05"`. The abstract includes "the Opening Range Breakout long (T = 0.88, year-unstable)".

### Turn 6: Erasmus PDF (failed)
```
balt 403 text/html; charset=UTF-8 5620
.../baltussen-jfe2021/paper.pdf: HTML document text, ASCII text, ...   (a 403 page saved as .pdf; NOT the paper)
978242daf5e438d2490bed6e9ef787e386b0f8d2b572cedc30edaa8f96f8dfff  .../baltussen-jfe2021/paper.pdf   (HTML error page)
058bd5e8b4a21eb312b2447f7ff04c9aacc764c6530580c45a120bcb8f89e46a  .../ieee-orb/paper.pdf
```

### Turn 7: Semantic Scholar API and Zhi Da's site
```
"title": "Market intraday momentum", ... "openAccessPdf": {"url": "https://doi.org/10.2139/ssrn.2440866", "status": "GREEN" ...
"abstract": "Based on high frequency data of the S&P 500 ETF from 1993-2013, we document an intraday momentum pattern: the first half-hour return on the market predicts the last half-hour return. ..."
 <- 10.1016/j.jfineco.2018.05.009 200
"title": "Hedging demand and market intraday momentum", ... "openAccessPdf": {"url": "https://www.sciencedirect.com/science/article/pii/S0304405X21001598", "status": "BRONZE" ...
 <- 10.1016/j.jfineco.2021.04.029 200
"title": "Can Day Trading Really Be Profitable? Evidence of Sustainable Long-term Profits from Opening Range Breakout (ORB) Day Trading Strategy vs. Benchmark in the US Stock Market", ... "authors": [... "Carlo Zarattini"}, {... "Andrew R. Aziz"}], "abstract": "... the day trading portfolio produced an annualized alpha of 33% (net of commissions). ... The resulting portfolio would have earned an outstanding return of 1,484% during the same period of 2016 to 2023, ..."
 <- 10.2139/ssrn.4416622 200
zda 200 text/html; charset=UTF-8 27555
href="intramom.pdf">Hedging Demand and Market Intraday Momentum
```

### Turn 8: Baltussen full text (worked); arXiv ORB search
```
balt-nd 200 application/pdf 2397917
.../baltussen-nd/intramom.pdf: PDF document, version 1.7, 23 pages
623ba82490acd01546f568cf582de5a9b45dfbd97731cd548cb119d7a0acec57  .../baltussen-nd/intramom.pdf
arxiv-orb 200 application/atom+xml; charset=utf-8 45323   (only 2605.04004 relevant)
olin-search 404 text/html; charset=UTF-8 105878   (Zhou Olin page guess — FAILED)
```

### Turn 9: scholar.archive.org (failed), text extraction
```
sa-gao 200 text/html; charset=UTF-8 4428    (no PDF hits)
sa-orb 200 text/html; charset=UTF-8 4428    (no PDF hits)
Assessing the Profitability of Timely Opening
Range Breakout on Index Futures Markets
YI-CHENG TSAI1,2 , MU-EN WU 3 , JIA-HAO SYU1,4 , CHIN-LAUNG LEI2 ,
CHUNG-SHU WU5 , JAN-MING HO1,6 , AND CHUAN-JU WANG 6
```

### Turns 10–13: Baltussen key greps (`grep -n`/`sed -n` on intramom.txt) and page map
```
459:  NASDAQ 100 futures∗                           NQ              9:30 - 16:00 ...
343: ... rROD,t =           − 1,     (2)   [+ "the return of buying at previous day's close and selling 30 min- utes before today's close"]
346:tions of the S&P E-Mini between 09:30 and 16:00, as these
 ... If the predictor return is positive, we will earn the last half-hour return, rLH , otherwise we will earn −rLH .
 ... removing all days in which the exchange closed earlier (such as Memorial Day), and (iv) removing all days in which the total traded vol- ume is less than 100 contracts.
794:   Note that we do not consider transaction costs. Given ...
     η (rROD )             6.86               3.96            1.73           0.55
   Always Long              0.44                4.20           0.11           0.53
  η (rONF H , rROD )        5.47               3.42            1.60           0.61
1375:  NASDAQ 100 futures∗                       NQ              1996-04-12            2020-05-01           6017           09:30–16:00               USA
1518:  NQ                7.45∗ ∗ ∗        2.01      1.83∗ ∗ ∗    6.95∗ ∗ ∗       5.14∗ ∗ ∗            11.54∗ ∗ ∗        4.31         3.58∗ ∗ ∗      6.36∗ ∗ ∗       4.10       3.76∗ ∗ ∗
pdfpage=7 line=459 :: 'NASDAQ 100 futures'
pdfpage=19 line=1375 :: 'NASDAQ 100 futures'
pdfpage=11 line=807 :: 'Table 6'
pdfpage=9 line=661 :: 'we examine a market-timing strategy'
pdfpage=5 line=343 :: 'rROD,t ='
pdfpage=10 line=794 :: 'we do not consider transaction costs'
pdfpage=21 line=1518 :: 'NQ                7.45'
```
The page footers seen in the `sed` output were 381 (after PDF page 5), 385, 386 and 387. So journal page = PDF page + 376 for pages 5–11. Not verified for PDF pages 19 and 21.

A zsh error happened in turn 9: an unquoted `======` was parsed as a command (`(eval):1: ===== not found`). I re-ran the step with quoted separators.

### Turns 14–15: TORB key greps
```
216:the observed period is the probe time tp , where tb < tp < te .
            Pt 0 ,d > max(Ptb ,d , · · · , Ptp ,d ) ⇒ Buy,        (3)
            Pt 0 ,d < min(Ptb ,d , · · · , Ptp ,d ) ⇒ Sell,       (4)
there is a trading signal on a day, the position closes at te on that day.
404: and E-mini NASDAQ are all with short probe times (4, 1, and 1 minutes, respectively)
428: best strategy in the full time period on the NASDAQ earns ... the annual return 5.58% is much less than the annual return 17.51% of the best TORB strategy on the same market.
373: 3 Here we follow Schulmeister's estimation to assume an overall transac- tion cost of 0.01% (per trade) [5].
172: the close price in the one-minute interval t on day d.
234: NASDAQ 100 (from 2001/1/2 to 2013/12/2)
272: FIGURE 4. E-mini NASDAQ PMMV and PMVR. ... for PMVR, including 8:30 (the opening time of the underlying market) and
pdfpage=4 line=216 / pdfpage=8 line=404 / pdfpage=9 line=428 / pdfpage=7 line=376 :: '32067' / pdfpage=3 line=193 :: '32063'
```
The tables are images: pdftotext emitted only their captions, and the bodies were blank. Wayback availability API: `429 Too Many Requests` for all three SSRN URLs. **Failed.**

### Turns 16–17: arXiv MNQ paper (secondary) and Google Scholar
```
arxivpdf 200 application/pdf 834734
.../arxiv-2605.04004-pdf/paper.pdf: PDF document, version 1.4, 8 pages
d0bd26e424a0c81bbca149e35566a3b9929a3cd207934e07638a99e78ca4ca80  .../arxiv-2605.04004-pdf/paper.pdf
gs 200 text/html; charset=UTF-8 157308   (captcha count 0)
<a href="https://papers.ssrn.com/sol3/Delivery.cfm?abstractid=2440866" ...><span class="gs_ctg2">[PDF]</span>   (SSRN only — not retried)
197: high or low of the first session bars; ... The opening range (OR) is defined as
198: 09:30–09:55 ET — the first six five-minute bars.
24: but fail elsewhere: the Opening Range Breakout long at a 15-bar hold (net +2.82 points, T = 0.88 on net returns)
```

### Turns 18–20: GitHub replication of Zarattini & Aziz ORB (secondary)
```
gh 200 application/json; charset=utf-8 14119
      "full_name": "giovannibrusco/zarattini-2023-orb-qqq",
readme 200 text/plain; charset=utf-8 13751
.../gh-brusco-readme/README.md: Unicode text, UTF-8 text, with very long lines (317)
4f0ff1e00fdc3318f600a3c9441518544f3bfb567640ef8d865ab724d195480f  .../gh-brusco-readme/README.md
31:| 🎯 **Replication** | Closely reproduced — **1,775 trades** (paper: 1,795), Sharpe **1.06** (paper: 1.12), max DD **22%** (paper: 22%) ...
75:QQQ 5-minute bars, **Jan 2016 → Feb 2023**, $25,000 starting capital.
79:    A["🕤 09:30–09:35 ET<br/>first 5-min QQQ bar"] -->|bullish bar| C{"🔀 NQ 09:25 bar<br/>also bullish?<br/><i>(filtered variant only)</i>"}
81:    A -->|doji| X["🚫 No trade"]
82:    C -->|yes| E["🟢 LONG at 09:35 open<br/>stop = 09:30 bar low"]
86:    E --> G["🎯 Exit: stop (−1R) · target (+10R)<br/>· or flat at session close"]
90:**Sizing & costs** — position size = `min(1% equity / $R, 4 × equity / entry)`
```
The second GitHub hit (`jlmn-code/bot_intradia_orb`) is a "stocks in play" ORB. That is cross-sectional and excluded; not used.

### Turns 21–24: wrote the shortlist, fixed IEEE page cites (abstract = p. 32061), wrote this log, staged.

## Verification evidence
The pasted command output is in each step above. Summary of downloads used as sources:

| Slug | URL | HTTP | `file` | sha256 | Used as |
|---|---|---|---|---|---|
| baltussen-nd | https://www3.nd.edu/~zda/intramom.pdf | 200 application/pdf | PDF 1.7, 23 pp | 623ba824…ec57 | #1 primary, full text |
| ieee-orb | https://ieeexplore.ieee.org/ielx7/6287639/8600701/08641124.pdf | 200 application/pdf | PDF 1.5 | 058bd5e8…e46a | #2 primary, full text (tables are images) |
| gh-brusco-readme | https://raw.githubusercontent.com/giovannibrusco/zarattini-2023-orb-qqq/HEAD/README.md | 200 text/plain | UTF-8 text | 4f0ff1e0…480f | #3 secondary (rules UNVERIFIED-from-secondary) |
| arxiv-2605.04004-pdf | https://arxiv.org/pdf/2605.04004v3 | 200 application/pdf | PDF 1.4, 8 pp | d0bd26e4…ca80 | secondary negative evidence on MNQ ORB |
| baltussen-jfe2021 | https://pure.eur.nl/files/58145484/… | **403** | HTML | 978242da…dfff | REJECTED (not the paper) |

Abstract-only sources (from the Semantic Scholar API, no file saved): Gao, Han, Li, Zhou 2018 and Zarattini & Aziz 2023.

Failures: DuckDuckGo 202 ×3; Bing junk; Zhou WUSTL 404 ×2; Erasmus 403 (HTML); scholar.archive.org no hits; Wayback 429 ×3. SSRN was never requested directly; the Scholar `[PDF]` link was SSRN and was not followed.

## Files staged
- `docs/reports/2026-10-31-7zq-m2-shortlist.md`
- `docs/reports/2026-10-31-7zq-m2-worker1-research.md`

## Turns used
About 25 of the 40-turn cap.

## Result: PASS
The shortlist was delivered with scores (#1 = 15, #2 = 12, #3 = 10) and Pick = #1. Remaining gaps are labelled in the shortlist: #3's rules are UNVERIFIED-from-secondary, Gao 2018 is abstract-only, the TORB tables are images, and Baltussen appendix pages are cited as PDF pages only.
