# Noise-Area paper read: does the paper specify a hard stop? (worker 1)

**Unit:** `2026-11-15-noise-area-paper-read`, worker 1. **Mode:** BUILD (read-only research). **Repo HEAD:** `d9fc5f0`.
**Run window (from `date -u` in the steps below):** 2026-11-15 16:25:02Z to 16:28:43Z.
Nothing staged, nothing committed. This file is the only repo file written.

## Task

Get a primary copy of Zarattini, Aziz and Barbon, "Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)", Swiss Finance Institute Research Paper No. 24-97. Quote word for word what it says about entries, exits and limiting loss. Answer from those quotes alone: does it specify a hard stop (a fixed maximum loss per trade, known at entry)? Are exits checked continuously or only at set times? Then put the project's own wording beside the paper's and list where they differ. This report makes no judgment on trading and recommends nothing.

## Local search

Search for a local copy or citation of the paper. No local copy of the PDF exists. The only PDF under the repo is an unrelated research file.

```
$ find . -path ./.git -prune -o -iname "*.pdf" -print | head
./Redemtion/Research Results/Architecting a Minimal-Intervention Trading System_ An Integrated Framework Combining n8n Orchestration, Direct Broker APIs, and Compliant Browser Monitoring.pdf

$ find . -path ./.git -prune -o \( -iname "*zarattini*" -o -iname "*beat*market*" -o -iname "*noise*area*" -o -iname "*4824172*" \) -print
./ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
./ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
./ninjascript/PraxisNoiseAreaBreakout.cs
./Redemtion/Intitialization-April 2026/Systematic, Higher-Frequency NQ Strategies to Pair with the Noise-Area Breakout .rtf
./docs/specs/2026-07-16-b2-noise-area-ruleset.md
./docs/reports/2026-07-16-4uu-noise-area-strategy.md

$ ls -d Redemtion "Research Results" "Research Prompts"
ls: Research Prompts: No such file or directory
ls: Research Results: No such file or directory
Redemtion
```
(The folders "Research Results" and "Research Prompts" exist only under `Redemtion/`.)

Citations: `grep -rIl -i -E "Zarattini|Beat the Market|4824172|Barbon"` matched **60 files**. Excerpts from the earlier sourcing record:

```
docs/specs/2026-07-16-b2-noise-area-ruleset.md:5:**Source paper:** Zarattini, C., Aziz, A., Barbon, A., *"Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY),"* Swiss Finance Institute Research Paper No. 24-97. First version 10 May 2024; **this version 3 Feb 2025**. SSRN ab
docs/specs/2026-07-16-b2-noise-area-ruleset.md:6:**Version obtained:** Full open-access PDF, 43 pp., 3 Feb 2025 revision, via University of St. Gallen Alexandria repository (see source log `docs/reports/2026-07-16-b2-ruleset-source.md`). SSRN page itself was 403-blocked; ...
docs/reports/2026-07-16-b2-ruleset-source.md:14:| 3 | `https://alexandria.unisg.ch/bitstreams/a99aba00-f967-49b3-aceb-f544dc386e0b/download` | WebFetch 405, but **`curl` downloaded the full 43-page PDF (1.9 MB, PDF v1.5)** — this is the authoritative full text. |
```
The 2026-07-16 record gave the St. Gallen URL. I fetched it fresh this session (below). I relied on no earlier copy.

## Fetch attempts (pasted output)

The download directory `/tmp/praxis-npr/dl/w1/` was new and empty (`ls -A | wc -l` gave `0`). Each request used a generic desktop Chrome User-Agent and no other identifying headers.

```
Sun 15 Nov 2026 16:25:26 UTC
== A1 SSRN abstract
403 https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4824172 text/html; charset=UTF-8 5771
== A2 SSRN Delivery
403 https://papers.ssrn.com/sol3/Delivery.cfm?abstractid=4824172&mirid=1 text/html; charset=UTF-8 5834
== A3 SSRN Delivery variant
403 https://papers.ssrn.com/sol3/Delivery.cfm/4824172.pdf?abstractid=4824172&mirid=1 text/html; charset=UTF-8 5892
== A4 unisg alexandria
200 https://alexandria.unisg.ch/server/api/core/bitstreams/a99aba00-f967-49b3-aceb-f544dc386e0b/content application/pdf;charset=UTF-8 1901828
```
All three SSRN bodies are a bot-challenge page:
```
a3.bin:<title>Just a moment...
a1.html:<title>Just a moment...
a2.bin:<title>Just a moment...
```
```
Sun 15 Nov 2026 16:25:38 UTC
== A5 alexandria item search (handle lookup)
200 https://alexandria.unisg.ch/server/api/core/bitstreams/a99aba00-f967-49b3-aceb-f544dc386e0b application/hal+json;charset=UTF-8 1613
== A6 concretum
200 https://concretumgroup.com/beat-the-market-an-effective-intraday-momentum-strategy-for-sp500-etf-spy/ text/html; charset=UTF-8 126779
```
A6 is the authors' firm's web page. It is SECONDARY and I did not use it for any finding.

## Primary copy identity

- **Source URL (requested):** `https://alexandria.unisg.ch/bitstreams/a99aba00-f967-49b3-aceb-f544dc386e0b/download`. It redirected with a 302 to `https://alexandria.unisg.ch/server/api/core/bitstreams/a99aba00-f967-49b3-aceb-f544dc386e0b/content`. This is the University of St. Gallen institutional repository, where the third author is affiliated.
- **Local path:** `/tmp/praxis-npr/dl/w1/paper.pdf` (byte-identical copy of `a4.bin`).
- **Bytes:** 1901828. **SHA-256:** `41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad`.

```
$ file a4.bin; wc -c a4.bin; shasum -a 256 a4.bin
a4.bin: PDF document, version 1.5
 1901828 a4.bin
41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad  a4.bin
$ shasum -a 256 paper.pdf
41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad  paper.pdf
$ pdfinfo a4.bin
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
```
(The Title, Subject, Keywords and Author fields in pdfinfo are empty.)

The server headers and the repository's own checksum record agree with the file:
```
a4.headers: content-disposition: inline; filename="ssrn-4824172 (2).pdf"; filename*=UTF-8''ssrn-4824172%20%282%29.pdf
a4.headers: last-modified: Mon, 10 Mar 2025 13:19:49 GMT
a4.headers: etag: "2168e040467e94d1b36ab83fe9c1fcd2"
a5.json:   {'name': 'ssrn-4824172 (2).pdf', 'sizeBytes': 1901828, 'checkSum': {'checkSumAlgorithm': 'MD5', 'value': '2168e040467e94d1b36ab83fe9c1fcd2'}, 'bundleName': 'ORIGINAL'}
$ md5 -q paper.pdf
2168e040467e94d1b36ab83fe9c1fcd2
```

The title, authors and version match. This is extracted text from page 2 (lines 1-5 and 16-17; the author contact lines are left out):
```
                                 Beat the Market
            An Effective Intraday Momentum Strategy
                     for S&P500 ETF (SPY)

                          Carlo Zarattini1 , Andrew Aziz2,3 , Andrea Barbon4
                                              First Version: May 10, 2024
                                             This Version: February 3, 2025
```
**Series number:** The text extract does not contain the string "24-97". `grep -n -i -E "ssrn|4824172|24-97|swiss finance" paper.txt` returned only affiliation and reference-list lines. The cover (page 1) prints the series number as glyph images. I rendered it (`pdftoppm -f 1 -l 1 -r 60 -png`, to `/tmp/praxis-npr/w1-img/p1-01.png`) and read the image. It shows "Swiss Finance Institute Research Paper Series N°24-97", the full title and the three authors. This is a visual reading of a rendered image, not pasteable text.

**SSRN id 4824172:** SSRN itself returned 403 to every request (A1 to A3), so I could not confirm the id from SSRN. Two pieces of indirect evidence support it: the repository's stored filename `ssrn-4824172 (2).pdf` (in both the headers and the bitstream JSON), and the fact that the PDF matches the title, authors and SFI number. So the id is **supported indirectly but NOT confirmed from SSRN**.

**PDF page numbers:** Printed page numbers equal PDF page numbers. The last line on PDF pages 5, 9 and 20 reads `5`, `9` and `20`, and PDF page 43 reads `43`.

## Extraction and grep output

```
$ pdftotext -layout paper.pdf /tmp/praxis-npr/w1-text/paper.txt     # plus one file per page: page-01.txt .. page-43.txt
    1643 paper.txt
$ grep -c <formfeed> paper.txt
43
$ shasum -a 256 paper.txt
5bed406569325f0aa45b92fcf7c09567db20cef2a6414536070db0d982c0b79a  /tmp/praxis-npr/w1-text/paper.txt
```
Section headings (`grep -n -E "^ {0,6}[0-9](\.[0-9])? +[A-Z]"`): `page-06:9: 3 Strategy Description`, `page-17:7: 4 Further Investigations`, `page-21:26: 4.4 Volatility Multiplier`, `page-26:1: 5 Conclusion`. **So pages 6 to 16 are all §3 "Strategy Description".**

**Stop / trailing / exit / maximum loss** (`/usr/bin/grep -n -i -E "stop|trailing|exit|maximum loss|max(imum)? (draw|loss)" page-*.txt`):
```
page-02.txt:30:       namic trailing stops to mitigate downside risks while allowing for unlimited upside
page-09.txt:23:dence of demand/supply imbalance. Stop losses can also be triggered only on semi-hourly
page-11.txt:8:matic shifts in market character. A trailing stop set at the opposite side of the Noise
page-11.txt:20:Table 1: Summary statistics of intraday momentum strategy with stop loss at opposite band and SPY
page-11.txt:25:   Strategy         Stop        Size            IRR     Vol                     MDD   Alpha   Beta
page-12.txt:1:Figure 4: SPY price action on 20 January 2022 illustrates our model strategy’s entry and exits. The
page-12.txt:2:base strategy uses the opposite band as a trailing stop. Following a sharp reversal in SPY in the last 2
page-12.txt:12:the Upper Boundary of the Noise Area as a trailing stop for our long positions, and vice
page-12.txt:15:improves the return from -2.19% to -0.31%. While a tighter stop loss can significantly
page-12.txt:20:This observation underscores the need to balance the protective benefits of a tighter stop
page-13.txt:1:                  (a) Stop = UpperBand                            (b) Stop = max(VWAP,UpperBand)
page-13.txt:5:Figure 5: Improvement in our strategy’s exit by incorporating tighter trailing stop losses. In Figure
page-13.txt:6:(a), the trailing stop is based on the upper band of the Noise Area, while in Figure (b), it is based on
page-13.txt:12:VWAP as a trailing stop for intraday trend exposures2 . Once a position is established,
page-13.txt:14:Mathematically, the trailing stops for long and short postions are defined as:
page-13.txt:17:                 Long TrailingStopt,HH:M M = max(U Bt,HH:M M , V W APt,HH:M M )
page-13.txt:19:                 Short TrailingStopt,HH:M M = min(LBt,HH:M M , V W APt,HH:M M )
page-13.txt:26:cacy as a dynamic stop loss mechanism that aligns closely with market momentum, thus
page-13.txt:30:To demonstrate the economic advantages of these trailing stop refinements, we have con-
page-14.txt:1: Figure 6: Comparison of equity curves of intraday momentum strategy with a) stop loss at opposite
page-14.txt:7: from 0.61 to 1.24, while the Hit Ratio decreased to 43% due to tighter stops. As exhibited
page-14.txt:9: turn sees a 5% improvement (from -10.3% to -4.8%). However, the tighter stop loss does
page-14.txt:20: Table 2: Summary statistics of intraday momentum strategy with a) stop loss at opposite band, b)
page-14.txt:25:Strategy          Stop                  Size                IRR     Vol                     MDD   Alpha   Beta
page-15.txt:1:  Table 3: Summary statistics of intraday momentum strategy with a) stop loss at opposite band, b)
page-15.txt:7:Strategy          Stop                  Size                 IRR    Vol                     MDD   Alpha   Beta
page-15.txt:42:  improves to 1.33, indicative of a more stable risk profile. The maximum drawdown is
page-16.txt:1:Figure 7: Comparison of equity curves of intraday momentum strategy with a) stop loss at opposite
page-16.txt:19:Table 4: Summary statistics at trade-level of intraday momentum strategy with a) stop loss at opposite
page-16.txt:24:                                                 Avg. Trade    Hit    Avg. PnL    Max Loss        Max Gain
page-16.txt:25:Strategy     Stop                Size   Trades
page-17.txt:11:momentum strategy that employs a trailing stop based on the current band and VWAP,
page-22.txt:17:Given the complexity of the decision between higher returns and better risk-adjusted
page-24.txt:32:trailing volume exceeding 300,000 shares.
page-26.txt:11:dynamic trailing stops, yields substantial returns over the period from 2007 to early 2024.
page-40.txt:1:Q22. How do the results change if we use only VWAP as a trailing stop?
page-40.txt:2:Switching to a VWAP-only trailing stop results in less restrictive exit conditions, leading
page-40.txt:13:       Strategy     Stop               Leverage               IRR    Vol                     MDD
page-43.txt:4:     Table A1: Summary statistics of intraday momentum strategy with a) stop loss at opposite band, b) current band with VWAP, c) as in (b) with the
page-43.txt:9:            Strategy         Stop                 Size            IRR       Vol                     MDD   Alpha   Beta    Skewness   Worst Day   Best Day
```

**Close / end of day / VWAP / boundary / band / noise area** (`/usr/bin/grep -n -i -E "close|closing|end of (the )?day|market close|4:00|16:00|VWAP|boundar|noise area|band" page-*.txt`). Excerpt for pages 6 to 17 (§3 and the opening of §4). For pages 18 and later, only the hits that mention the stop or exit are kept; all omitted hits are table rows or the Concretum Bands indicator FAQ. "end of day" and "market close" had **0 hits** as phrases. The only close-time wording is "market Close" (p. 9).
```
page-07.txt:26:      UpperBoundt,HH:M M = max(Opent,9:30 , Closet−1,16:00 ) × (1 + σt,9:30−HH:M M )
page-07.txt:30:      LowerBoundt,HH:M M = min(Opent,9:30 , Closet−1,16:00 ) × (1 − σt,9:30−HH:M M )
page-09.txt:6:the resulting trades based on our base-model. Please note that all positions are closed at the market
page-09.txt:7:Close (16:00).
page-09.txt:12:As discussed earlier, if the market breaches the boundaries of the Noise Area, our strat-
page-09.txt:14:price is above the Noise Area and short if it is below. To mitigate the risk of overtrading
page-09.txt:20:Positions are unwound either at market Close or if there is a crossover to the opposite
page-09.txt:21:boundary of the Noise Area. In the event of such a crossover, the existing position is
page-09.txt:22:closed, and a new one is initiated in the opposite direction to align with the latest evi-
page-09.txt:31:market movements. All positions are closed at market Close, adhering to the strategy’s
page-11.txt:16:south, dropping almost 2% in the last trading hours; SPY closes the day below the Lower
page-11.txt:17:Boundary of the Noise Area, resulting in a 2.19% loss for the active strategy. This sce-
page-12.txt:14:position being closed at 14:00, just as the market begins to weaken. This adjustment
page-13.txt:13:as soon as the price crosses either the curent band or the VWAP, the position is closed.
page-13.txt:24:ing VWAP allows us to close the long exposure at 13:00, ultimately achieving a break-even
page-13.txt:35:       VWAP is computed only using market hours data. For more details see our previous publication [5].
page-14.txt:29:Momentum          Curr.Band + VWAP     100%     380%        9.7%   7.7%     1.24    43%     12%   9.9%    -0.03
page-16.txt:32:Intra Mom.   Curr.Band + VWAP    100%   7,668       1.8       37%       0.09
page-17.txt:11:momentum strategy that employs a trailing stop based on the current band and VWAP,
page-40.txt:2:Switching to a VWAP-only trailing stop results in less restrictive exit conditions, leading
page-40.txt:4:of trades decreases significantly from 7,964 (for the VWAP + Current Band version) to
```

**Risk / sizing / leverage / check / interval / half-hour / HH:00 / HH:30 / every / continuous**, pages 1 to 17 (`/usr/bin/grep -n -i -E "risk|sizing|size|leverage|check|interval|30 minutes|half-hour|semi-hourly|30-minute|HH:00|HH:30|:00|:30|continuous|intra-?bar|every"`). Hits on the timing and sizing rules:
```
page-09.txt:14:price is above the Noise Area and short if it is below. To mitigate the risk of overtrading
page-09.txt:15:caused by short-term market fluctuations, trading is restricted to semi-hourly intervals,
page-09.txt:16:specifically at HH:00 and HH:30. This timing mechanism ensures that decisions are
page-09.txt:23:dence of demand/supply imbalance. Stop losses can also be triggered only on semi-hourly
page-09.txt:24:intervals.
page-09.txt:29:at 10:30, even though the price had moved outside the Noise Area a few minutes earlier.
page-10.txt:1:The strategy allocates exposure equal to 100% of the equity available at the beginning
page-12.txt:11:A straightforward method to mitigate the risk of sudden market reversals is by utilizing
page-14.txt:15: As a final refinement to our model, we have implemented a sizing methodology that
page-15.txt:18:  trade with half of the capital; conversely, if it is 1%, we would utilize a leverage of 2.
page-15.txt:36:  policies, the leverage for the active strategy is capped at 4x.
```
"check" or "checked", "continuous", "intrabar" and "every" had **0 hits on pages 1 to 17**. On pages 18 to 43 the same pattern gave one "every" hit (page-30 line 3, the FAQ preface: "address every inquiry") and no "check" hit.

**Order / limit / fixed / per trade** (`/usr/bin/grep -n -i -E "order|limit|fixed|percent|% of|per trade"`). No hit describes a resting stop order or a fixed loss limit. The only order-type wording is the slippage study on page 25 ("send market orders on SPY") and the live-trading FAQ on page 34 ("send orders to Interactive Brokers"):
```
page-09.txt:32:protocol to limit exposure to overnight market changes.
page-25.txt:5:funded with $100,000, we instruct an algorithm to send market orders on SPY for $100,000
page-34.txt:10:and then automatically send orders to Interactive Brokers via IBML, a specialized Mat-
page-40.txt:3:to a slight increase in the average holding period per trade. Consequently, the number
```
**ATR / profit target** (`/usr/bin/grep -n -E "ATR|[Aa]verage [Tt]rue|profit target|take.profit|target"`). There are 0 ATR hits. The only "target" hits are the volatility-target sizing rule (page 14 line 17, page 15 lines 17 and 22).

## Verbatim quotes (section, page)

These are copied character for character from `page-NN.txt`, with the original line breaks kept. Words split by a line-end hyphen in the PDF are rejoined only in the reading line under each quote: "strat-/egy" to "strategy", "evi-/dence" to "evidence", "dra-/matic" to "dramatic", "sce-/nario" to "scenario", "imbal-/ance" to "imbalance", "re-/mains" to "remains", "effi-/cacy" to "efficacy", "con-/ducted" to "conducted". The typos "curent" and "postions" are the paper's own (sic).

**Q1. Entry and when trading is allowed: §3 Strategy Description, p. 9, lines 12-17**
```
As discussed earlier, if the market breaches the boundaries of the Noise Area, our strat-
egy initiates positions in accordance with the prevailing intraday move—going long if the
price is above the Noise Area and short if it is below. To mitigate the risk of overtrading
caused by short-term market fluctuations, trading is restricted to semi-hourly intervals,
specifically at HH:00 and HH:30. This timing mechanism ensures that decisions are
based on more stable price movements rather than transient spikes.
```

**Q2. Base exit rule and when stops are checked: §3, p. 9, lines 20-24**
```
Positions are unwound either at market Close or if there is a crossover to the opposite
boundary of the Noise Area. In the event of such a crossover, the existing position is
closed, and a new one is initiated in the opposite direction to align with the latest evi-
dence of demand/supply imbalance. Stop losses can also be triggered only on semi-hourly
intervals.
```

**Q3. Session close and stamp timing: §3, p. 9, lines 27-32, and the Figure 2 caption, lines 5-7**
```
Figures 2 illustrates the Noise Areas and the resulting trades on 2 days with clear trends
that occurred in 2022. As shown by the dashed grid on the charts, trades are executed
at 10:30, even though the price had moved outside the Noise Area a few minutes earlier.
This delay in response reduces the risk that trading decisions are triggered by fleeting
market movements. All positions are closed at market Close, adhering to the strategy’s
protocol to limit exposure to overnight market changes.
```
```
Figure 2: The time-varying boundary areas on SPY for 31 January 2022 (a) and 29 April 2022 (b) and
the resulting trades based on our base-model. Please note that all positions are closed at the market
Close (16:00).
```

**Q4. Base-model sizing: §3, p. 10, lines 1-3**
```
The strategy allocates exposure equal to 100% of the equity available at the beginning
of each trading day. We calculate the number of shares that can be traded using the
equation:
```
(The equation that follows is `Shares_t = AUM_{t−1} / Open_{t,9:30}`. It is rendered over several lines in the extract, p. 10, lines 6-8.)

**Q5. Weakness of the base stop: §3, p. 11, lines 6-9 and 12-17, continuing on p. 12, lines 7-8**
```
By design, the active intraday strategy is vulnerable to sudden market reversals, which
can be triggered by news releases or other fundamental catalysts that can provoke dra-
matic shifts in market character. A trailing stop set at the opposite side of the Noise
Area exacerbates this vulnerability, as the portfolio can suffer dramatically on such days.
```
```
January 20, 2022 serves as a poignant example of the weaknesses inherent in our base
model. As shown in Figure 4, the market strongly rallies in the first 30 minutes, triggering
a long exposure. For some 4 hours, the price remains above the Noise Area, indicating
continued abnormal buying pressure. However, around 14:00, the market begins to turn
south, dropping almost 2% in the last trading hours; SPY closes the day below the Lower
Boundary of the Noise Area, resulting in a 2.19% loss for the active strategy. This sce-
```
```
nario highlights the need for adjustments in our base model to mitigate losses during
abrupt market reversals.
```
Figure 4 caption, p. 12, lines 1-3:
```
Figure 4: SPY price action on 20 January 2022 illustrates our model strategy’s entry and exits. The
base strategy uses the opposite band as a trailing stop. Following a sharp reversal in SPY in the last 2
hours of trading, the base model realizes a loss of more than 2%.
```

**Q6. Tighter stop at the current band: §3, p. 12, lines 11-22**
```
A straightforward method to mitigate the risk of sudden market reversals is by utilizing
the Upper Boundary of the Noise Area as a trailing stop for our long positions, and vice
versa for short positions. As we demonstrate in Figure 5(a), this approach leads to the
position being closed at 14:00, just as the market begins to weaken. This adjustment
improves the return from -2.19% to -0.31%. While a tighter stop loss can significantly
reduce downside risks, it is important to note that it may also substantially increase the
number of trades due to false signals, and consequently, the associated transaction costs.


This observation underscores the need to balance the protective benefits of a tighter stop
loss against the potential for increased operational costs, ensuring that the strategy re-
mains economically viable while providing adequate risk management.
```

**Q7. The paper's band-or-VWAP trailing stop: §3, p. 12, lines 25-26, continuing on p. 13, lines 11-19, 23-27 and footnote 2 (line 35)**
```
Moreover, as documented in a previous paper [5], Volume Weighted Average Price (VWAP)
can serve as a powerful intraday indicator to identify shifts in the demand-supply imbal-
```
```
ance. Building upon insights from our previous publication, we have chosen to integrate
VWAP as a trailing stop for intraday trend exposures2 . Once a position is established,
as soon as the price crosses either the curent band or the VWAP, the position is closed.
Mathematically, the trailing stops for long and short postions are defined as:


                 Long TrailingStopt,HH:M M = max(U Bt,HH:M M , V W APt,HH:M M )

                 Short TrailingStopt,HH:M M = min(LBt,HH:M M , V W APt,HH:M M )
```
```
Figure 5(b) illustrates the revised approach in the case study of January 20, 2022. Includ-
ing VWAP allows us to close the long exposure at 13:00, ultimately achieving a break-even
trade. This adjustment represents a significant improvement, showcasing VWAP’s effi-
cacy as a dynamic stop loss mechanism that aligns closely with market momentum, thus
enhancing the strategy’s risk management capabilities.
```
```
       VWAP is computed only using market hours data. For more details see our previous publication [5].
```
Figure 5 caption, p. 13, lines 1 and 5-7:
```
                  (a) Stop = UpperBand                            (b) Stop = max(VWAP,UpperBand)
Figure 5: Improvement in our strategy’s exit by incorporating tighter trailing stop losses. In Figure
(a), the trailing stop is based on the upper band of the Noise Area, while in Figure (b), it is based on
the maximum between the VWAP and the upper band.
```

**Q8. Effect of the tighter stop, and dynamic sizing: §3, p. 14, lines 7-17, then p. 15, lines 17-18 and 34-36**
```
 from 0.61 to 1.24, while the Hit Ratio decreased to 43% due to tighter stops. As exhibited
 in Table A1, the skewness shifts to positive (from -1.24 to 1.29) and the worst daily re-
 turn sees a 5% improvement (from -10.3% to -4.8%). However, the tighter stop loss does
 result in a significant increase in the total number of trades, rising from 5,494 to 7,668
 over the 17-year period (see Table 4). These results highlight the enhanced risk-return
 profile achieved by the strategic modifications, albeit with an increase in trading activity.


 As a final refinement to our model, we have implemented a sizing methodology that
 dynamically adjusts the traded exposure based on daily market volatility. Instead of
 maintaining constant full notional exposure, this method targets a daily market volatility
```
```
  of 2% (σtarget = 2%). Practically, if the recent daily volatility of SPY is 4%, we would
  trade with half of the capital; conversely, if it is 1%, we would utilize a leverage of 2.
```
```
  This adjustment results in a more stable risk profile for the active portfolio, making it
  less dependent on overall market volatility regimes. In line with mainstream brokerage
  policies, the leverage for the active strategy is capped at 4x.
```

**Q9. Realised worst trades (outcomes, not a rule): §3, Table 4, p. 16, lines 24-36**
```
                                                 Avg. Trade    Hit    Avg. PnL    Max Loss        Max Gain
Strategy     Stop                Size   Trades
                                                   x Day      Ratio    x Share     Trade           Trade

                                                                                    -8.6%           6.0%
Intra Mom.   Opp.Band            100%   5,494       1.3       53%       0.10
                                                                                 (13-Nov-2008)   (13-Oct-2008)
                                                                                    -4.0%           4.6%
Intra Mom.   Curr.Band + VWAP    100%   7,668       1.8       37%       0.09
                                                                                 (18-Mar-2020)   (15-Oct-2008)
                                                                                    -2.9%           9.1%
Intra Mom.   Curr.Band + VWAP    Dyn.   7,668       1.8       37%       0.09
                                                                                 (31-Jul-2013)   (10-Oct-2018)
```
p. 10, lines 31-33: "...the most con-/cerning aspects are the worst daily return of -10.33% and the negative skewness of the/intraday momentum portfolio..." (the slashes mark the PDF line breaks).

**Q10. Which version the rest of the paper uses: §4 Further Investigations, p. 17, lines 8-12**
```
In this section, we outline the more in-depth statistical analysis we have conducted in or-
der to assess how the profitability of the intraday momentum strategy changes in different
market scenarios. Unless otherwise specified, all tests are conducted using the intraday
momentum strategy that employs a trailing stop based on the current band and VWAP,
and adjusts investment size according to recent market volatility.
```

**Q11. The authors' live practice, separate from the backtest rule: FAQ Q11, p. 34, lines 7-11**
```
We do trade a slightly modified version of this strategy in our accounts, leveraging the
functionalities of the Interactive Brokers API. While there are many ways to automate
a trading strategy, in our portfolios, we update signals at high frequency using IQFeed
and then automatically send orders to Interactive Brokers via IBML, a specialized Mat-
lab trading package designed for both financial institutions and individual quant traders.
```

**Q12. VWAP-only variant: FAQ Q22, p. 40, lines 1-3**
```
Q22. How do the results change if we use only VWAP as a trailing stop?
Switching to a VWAP-only trailing stop results in less restrictive exit conditions, leading
to a slight increase in the average holding period per trade. Consequently, the number
```

## Answer

**Hard stop (a fixed maximum loss per trade, known at entry, such as a resting stop order at a set price): NO.** The paper does not specify one.

- The exit rules the paper states are these:
  - The market Close at 16:00 (Q2, Q3).
  - In the base model, a crossover to the opposite boundary, which closes the position and reverses it (Q2).
  - In the refined model, a trailing stop at `max(UB, VWAP)` for longs and `min(LB, VWAP)` for shorts (Q7). This is the model the paper uses from §4 on (Q10).
- The stop is a level that changes over time. The boundaries are indexed by time of day, `HH:MM` (Q7 formula; p. 8 says the bands widen through the day), and VWAP moves with price. Nothing in the quoted text sets a stop price or a loss amount when the trade is entered.
- The grep found no "fixed" stop, no "maximum loss" rule, no ATR stop, no profit target, and no stop-order wording (see the order and limit grep). The only order wording is "market orders" in the slippage study (p. 25).
- "Max Loss Trade" in Table 4 (Q9) is a realised result of the backtest, not a limit. It ranges from -8.6% to -2.9% depending on the variant.
- How far this "NO" reaches: it means the paper does not *state* a hard stop. I base it on reading all of §3 (pp. 6-16) and grepping the full 43-page text extract. Text that appears only inside figure images would not be in the extract. I did not run or check the authors' linked code (p. 30, Q1).

**Continuous or set times?** For the **base model**, stops are checked at **set times**. The paper says so outright: "Stop losses can also be triggered only on semi-hourly intervals." (Q2, p. 9). Trading generally is "restricted to semi-hourly intervals, specifically at HH:00 and HH:30" (Q1).

For the **refined band-or-VWAP stop** (Q7, p. 13), the check timing is **not restated**:
- The text says "as soon as the price crosses either the curent band or the VWAP, the position is closed." It does not name a checking frequency.
- The p. 9 sentence comes before the refinement is introduced. Its wording does not limit it to the base model, but the paper never explicitly says it applies to the refined stop either.
- The paper's worked exits fall on hour stamps: closed "at 14:00" (Q6) and "at 13:00" (Q7). Those times are consistent with half-hour checks, but they do not prove them.

So: set times are explicit for the base model. For the refined model the text is consistent with set times but not explicit. Separately, the authors say they run "a slightly modified version" live and update signals "at high frequency" (Q11). That describes their live trading, not the rule in the paper.

## Project wording (file:line, verbatim)

Line numbers are from the working tree. `git status --short` showed the spec, the 4uu report and the scope proposal clean at HEAD `d9fc5f0`. `DECISIONS.md` is modified in the working tree (` M`), and `docs/reports/2026-11-15-voice-notes-open-questions.md` is untracked (`??`).

**`docs/specs/2026-07-16-b2-noise-area-ruleset.md`** (`sed -n`):
```
36: - **Entry condition:** at a **semi-hourly checkpoint only** — `HH:00` and `HH:30` — if price is **above** the Upper Boundary → **go long**; if **below** the Lower Boundary → **go short**. Checking only at the half-hour (not tick-by-tick) is deliberate, to avoid acting on transient spikes; the paper shows a breach a few minutes before 10:30 is not acted on until the 10:30 stamp (Fig. 2, p. 9).
38: - **Positions per session:** **NOT capped at one.** A position is held until the close or until price crosses to the **opposite** boundary, at which point it is closed **and reversed** into a new position that direction (p. 9). Realized average trade frequency is **1.3 trades/day** (base opp-band stop) rising to **1.8 trades/day** with the VWAP stop (Table 4, p. 16). Stops, too, are evaluated only at the semi-hourly stamps (p. 9).
50: | Stop-ATR | **not used** — there is no ATR-based stop anywhere in the paper | — |
57: ## 4. Exit policy + session-flat — PAPER-VERIFIED (§3, pp. 9–14)
59: - **Base stop:** trailing stop at the **opposite** Noise-Area boundary (long stops at Lower/Upper as it trails; base model = "Stop @ Opp. Band", Table 1). Evaluated only at semi-hourly stamps.
60: - **Improved stop (paper's preferred model):** trailing stop at **band-or-VWAP**, whichever is tighter to price:
61:   `Long TrailingStop = max(UpperBound, VWAP)` ; `Short TrailingStop = min(LowerBound, VWAP)` (§3 p. 13). VWAP is computed **from market-hours data only, anchored at the 09:30 open** (footnote 2, p. 13). Position closes as soon as price crosses the current band **or** the VWAP.
62: - **Reversal:** a cross to the opposite boundary closes and reverses (see §2).
63: - **Profit target:** none.
64: - **Session flat:** **all positions closed at the market Close = 16:00 ET** (cash close), never held overnight (Fig. 2 caption p. 9; Fig. 4 p. 12). The paper has **no intraday time-stop** — the only time-based exit is 16:00.
95: | **noise multiplier** | **no paper analog** (`k = 1.0`) | Input `NoiseMult` (default **1.0** to match paper): `UB = ref·(1 + k·σ)`. Any k≠1 is a PRAXIS extension, not validated by 24-97. |
99: Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; ... Entry via `EnterLongStopMarket`/`EnterShortStopMarket` at the boundary is a reasonable NT8 realization of "act at the next HH:00/HH:30 stamp if price is outside the band," but note the paper acts on the **stamp**, not on an intrabar stop-touch — a stop-market order can fill mid-bar and diverge slightly; reconcile in b2-signal-repro.
```
(Line 99 is shortened at "..." only. The omitted text is about the reference price and the flat time, not the stop.)

**`docs/reports/2026-07-16-4uu-noise-area-strategy.md`** (grep -n; the last column of the table is headed "Spec § / paper page", so "§4" there means the spec's own §4):
```
6:**Trader locks (DECISION_LOG 2026-07-16, session 16):** 16:00 ET flat; reverse-on-opposite-cross; pure paper replication with FIXED params (Lookback=14, band=1×σ, no ATR stop); ExitMode is the only knob.
25:| `isCheckpoint = (min==0 || min==30) && OpenMod<mod<CloseMod` | Act only at HH:00 / HH:30 stamps | §2 p.9 |
28:| Long stop `Max(curUpper, curVwap)`; Short `Min(curLower, curVwap)`; evaluated only at checkpoint | Trailing stop = band-or-VWAP (whichever tighter), at the stamp | §4 p.9,13 |
29:| `ExitMode==OppBand` → stop = band only | Base "Stop @ Opp. Band" variant | §4 p.9 / Table 1 |
30:| `mod >= CloseMod → FlattenAll(); return` | 16:00 ET cash-close flat, no new entry at/after close | §4 p.9,12; trader lock |
```

**`docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:129`** (start of the line, `sed -n 129p`):
```
**Answer:** The strategy under test is the **Zarattini–Aziz–Barbon NQ "Noise-Area" intraday breakout** (clock-anchored, rules-based, one bracket/session). ... optimize {lookback, noise mult, stop-ATR mult, exit policy}). ...
```

**The research summary** that the trader's Q6 ruling refers to. The ruling text itself, `DECISIONS.md:2839` (excerpt):
```
... Before anything else, confirm from the original paper (Zarattini, Aziz and Barbon, "Beat the Market", Swiss Finance Institute 24-97) whether the Noise-Area strategy has a hard stop. The project's research summary says it uses a trailing stop at the band or VWAP, checked at set times, which would mean no fixed maximum loss. ...
```
No file contains the exact phrase "trailing stop at the band or VWAP, checked at set times". `grep -rn -i -E "set times|interval-checked|checked at (fixed|set|the half)"` found only `DECISIONS.md:2822`, `DECISIONS.md:2839`, `DECISIONS.md:2844`, `DECISION_LOG.md:994` and the voice notes file. The candidate source passages are:
```
docs/reports/2026-11-15-voice-notes-open-questions.md:92:The agent answered yes and noted the source paper (Zarattini, Aziz and Barbon) appears to use an interval-checked trailing exit at band/VWAP and no hard stop, so a hard stop is a new variable. ...
DECISIONS.md:2822:  (same sentence, filed copy)
Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf:34: ... When price breaches the upper (lower) boundary at the top/bottom of an hour, a long (short) position is opened. The position uses dynamic trailing stops (e.g., VWAP-based) and is flat at the cash close. One position per session; sized to a 2% daily volatility target capped at 4\'d7 notional. The setup is binary \'97 either price has closed beyond the band at the half-hourly check or it has not.\
Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf:45: ... exits are programmatic (trailing stop, EOD flat, or band reversion).\
Redemtion/Intitialization-April 2026/PRAXIS INITIALIZATION PLAN- April2026.md:255:**What it is:** At each half-hour or hour, two boundaries ("noise band") are drawn around the day's open. When price breaches the boundary, a position opens. Trailing stop, flat at close. One trade per session. ...
Redemtion/Research Results/ROUND_2_RESEARCH_PROMPTS_Agent_2_and_3.md:93:- **Implications for Strategy #1 (Noise-Area Breakout).** Strategy #1 uses dynamic trailing stops (VWAP-based) and EOD-flat exits. ...
Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-0085-4b1e-a813-4f4221d90a63_text_markdown.md:41:- Decision is made **at fixed wall-clock times** (09:30, 10:00, 10:30, 11:00, 11:30 ET) on bar close, not intra-bar.
Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-0085-4b1e-a813-4f4221d90a63_text_markdown.md:42:- Entry can be a stop-market or stop-limit at the noise boundary; exit is a hard stop + trailing or time-stop at session end.
```
Which of these the ruling meant by "the project's research summary" is **UNVERIFIED**.

## Mismatches

Each item sets paper text against project text. None is a judgment about trading.

1. **Hard stop.** `compass_artifact_wf-ee42...md:42` says "exit is a hard stop + trailing or time-stop at session end". The paper states no hard stop (Q2, Q3, Q7; Answer).
2. **Positions per session.** Three project texts say one position or one trade per session:
   - `scope-proposal:129` "one bracket/session"
   - `Verified Trading-Strategy Shortlist ... .rtf:34` "One position per session"
   - `PRAXIS INITIALIZATION PLAN- April2026.md:255` "One trade per session"

   The paper closes and reverses on an opposite-boundary crossover (Q2). Table 4 reports 1.3 to 1.8 trades per day (Q9). "Bracket" also implies a resting stop-and-target order pair. The paper names no target and no resting stop order (grep output above). Spec `:38` and 4uu `:6` agree with the paper on reversal.
3. **What the trailing stop is.**
   - `Verified ... .rtf:34` says "dynamic trailing stops (e.g., VWAP-based)".
   - `ROUND_2_RESEARCH_PROMPTS...md:93` says "dynamic trailing stops (VWAP-based)".
   - The paper's preferred stop is `max(UB, VWAP)` / `min(LB, VWAP)`, that is, band **or** VWAP (Q7). VWAP-only is a separate FAQ variant (Q12).
   - The spec already flags the RTF wording as partial at its `:77` (D6).
4. **Check times.**
   - `Verified ... .rtf:34` says "at the top/bottom of an hour". The paper says HH:00 **and HH:30** (Q1). The same RTF line also says "at the half-hourly check".
   - `compass...md:41` lists 09:30 to 11:30 ET only. The paper trades to the 16:00 close (Q1, Q3).
5. **Check timing of the refined stop.** Spec `:38`, spec `:59`, 4uu `:28` and the voice-notes `:92` wording ("interval-checked trailing exit at band/VWAP") say or imply that stops are evaluated only at the semi-hourly stamps.
   - The paper says this explicitly in the base-model description (Q2, p. 9).
   - For the band-or-VWAP stop the paper says "as soon as the price crosses" (Q7, p. 13) and does not restate the interval. Spec `:61` copies "as soon as" without the qualifier, while 4uu `:28` attaches "at the stamp" to the band-or-VWAP stop.
   - The paper text does not settle which reading holds for the refined stop (see Answer).
6. **VWAP anchor.** Spec `:61` cites footnote 2, p. 13 for "from market-hours data only, anchored at the 09:30 open". The footnote text is only "VWAP is computed only using market hours data." The words "anchored at the 09:30 open" are not in the footnote.
7. **Citation for the session flat.** Spec `:64` cites "Fig. 4 p. 12" for the 16:00 close. The Fig. 4 caption text (p. 12, lines 1-3) does not mention 16:00 or the close. The 16:00 close is stated in the Fig. 2 caption and the body text on p. 9 (Q3).
8. **Base-stop wording.** Spec `:59` has the parenthesis "(long stops at Lower/Upper as it trails ...)". The paper's base model is a crossover to the **opposite** boundary (Q2). For a long position the paper names the Lower Boundary in the p. 11 example (Q5). The spec's "Lower/Upper" pairing does not appear in the paper. This is a wording ambiguity, not a direct contradiction.
9. **Gloss on "whichever is tighter".** Spec `:60` and 4uu `:28` say "whichever is tighter to price". The paper says `max(...)` / `min(...)` and "crosses either the curent band or the VWAP" (Q7). For a long, max of the two is the higher level, so the gloss matches the formula, but the words are the project's, not the paper's.
10. **Outside the exit and stop scope, reported only.** Spec `:95` says the noise multiplier has "**no paper analog**", and spec `:84` says the paper has neither a noise multiplier nor a stop-ATR. The paper's §4.4 "Volatility Multiplier" (p. 21, lines 26-43) introduces VM as a multiplier on band width: `UpperBound = max(Open, Close_{t-1,16:00}) × (1 + VM × σ)`. The no-ATR statements (spec `:50`, 4uu `:6`) match the paper: 0 ATR hits.
11. **The trader's ruling premise compared with the paper.** `DECISIONS.md:2839` says "a trailing stop at the band or VWAP, checked at set times, which would mean no fixed maximum loss". The paper's text supports "trailing stop at band or VWAP" (Q7) and "no fixed maximum loss" (Answer). "Checked at set times" is explicit only for the base model (Q2). See item 5.

## Secondary sources (labelled)

- SECONDARY, fetched but not used: `https://concretumgroup.com/beat-the-market-an-effective-intraday-momentum-strategy-for-sp500-etf-spy/` (A6, 200, 126779 bytes, kept as `/tmp/praxis-npr/dl/w1/a6.html`). No finding rests on it.
- SECONDARY, not fetched: the authors' Matlab and Python code linked in FAQ Q1 (p. 30), and the TradingView "Concretum Bands" indicator (p. 30, Q3).
- SECONDARY, project texts: every project file quoted under "Project wording". None is presented as the paper's words.
- I used no recalled knowledge of the paper. Every paper claim above rests on the extracted text or, for the series number, the rendered page-1 image.

## Files

- Downloaded, untrusted, outside the repo: `/tmp/praxis-npr/dl/w1/` (a1 to a6 bodies and headers, `paper.pdf`).
- Extracted text: `/tmp/praxis-npr/w1-text/paper.txt` and `page-01.txt` to `page-43.txt`. Page-1 render: `/tmp/praxis-npr/w1-img/p1-01.png`. Scripts directory: `/tmp/praxis-npr/scripts-w1/` (holds only a form-feed helper byte).
- Repo: this report only. Nothing staged.

## Result

**PASS.** I obtained a primary copy: the SFI 24-97 cover and the "This Version: February 3, 2025" PDF from the University of St. Gallen repository, 1901828 bytes, sha256 `41d635d1...07ad`, MD5 equal to the repository's stored checksum. On a hard stop, the paper's answer is **NO**. On check timing, set times are explicit for the base model and not restated for the band-or-VWAP stop. I listed eleven mismatches and made no trading judgment.

## Addendum (worker 3, corrections)

Appended by worker 3 of unit `2026-11-15-noise-area-paper-read`. Lines 1 to 549 above are unchanged (hash proof is in the worker-3 return, not here, because this text is part of the file being hashed). The standing sentence that was line 550 was removed only so that it appears once, as the last line. Each item below was found by an adversarial check; I re-checked each one against my own extraction before writing it. Paper text comes from my own per-page `pdftotext -layout` extraction in `/tmp/praxis-npr/w3-text/` (page-NN.txt, via `-f N -l N`). Two kinds of masking apply to pasted output: any line containing an email address is withheld, and personal names other than the paper's three authors are replaced by `[name withheld]` / `[names withheld]`.

**Source identity (re-hashed this step):**
```
Sun 15 Nov 2026 16:43:27 UTC
41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad  /tmp/praxis-npr/dl/w1/paper.pdf
Pages:           43
      43
```

### D1. Quote preamble (line 242): CONFIRMED

Correction: the quotes in "Verbatim quotes" are raw extracted lines and are **not rejoined**. There is no reading line under any quote. "con-/ducted" is not inside any quote: the only such split is p. 13 lines 30-31 ("we have con-" / "ducted a comprehensive historical backtest"), which Q7 does not include. The preamble also left out four splits that are inside quotes: "Includ-/ing" (Q7), "re-/turn" (Q8), "or-/der" (Q10) and "Mat-/lab" (Q11). Separately, the inline p. 10 quote under Q9 keeps "con-/cerning" with a slash. The true list of line-end splits inside the Q1 to Q12 block quotes, scripted over the exact page:line ranges each quote heading names:
```
Sun 15 Nov 2026 16:43:27 UTC
Q1 page-09.txt:12:As discussed earlier, if the market breaches the boundaries of the Noise Area, our strat-
Q2 page-09.txt:22:closed, and a new one is initiated in the opposite direction to align with the latest evi-
Q5 page-11.txt:7:can be triggered by news releases or other fundamental catalysts that can provoke dra-
Q5 page-11.txt:17:Boundary of the Noise Area, resulting in a 2.19% loss for the active strategy. This sce-
Q6 page-12.txt:21:loss against the potential for increased operational costs, ensuring that the strategy re-
Q7 page-12.txt:26:can serve as a powerful intraday indicator to identify shifts in the demand-supply imbal-
Q7 page-13.txt:23:Figure 5(b) illustrates the revised approach in the case study of January 20, 2022. Includ-
Q7 page-13.txt:25:trade. This adjustment represents a significant improvement, showcasing VWAP’s effi-
Q8 page-14.txt:8: in Table A1, the skewness shifts to positive (from -1.24 to 1.29) and the worst daily re-
Q10 page-17.txt:8:In this section, we outline the more in-depth statistical analysis we have conducted in or-
Q11 page-34.txt:10:and then automatically send orders to Interactive Brokers via IBML, a specialized Mat-
$ /usr/bin/grep -n -E "con-[[:space:]]*$" page-*.txt
page-10.txt:23:These operational parameters ensure that our backtesting reflects realistic trading con-
page-10.txt:31:overall slight underperformance compared to the passive SPY exposure, the most con-
page-13.txt:30:To demonstrate the economic advantages of these trailing stop refinements, we have con-
page-27.txt:6:             100 best-selling authors in ”Business and Finance” for 7 con-
page-38.txt:5:significant relationship between VIX and short trade profitability. This is visually con-
```
That is 11 splits: strat-/egy, evi-/dence, dra-/matic, sce-/nario, re-/mains, imbal-/ance, Includ-/ing, effi-/cacy, re-/turn, or-/der, Mat-/lab.

### D2. Mismatch 4, first bullet: CONFIRMED, WITHDRAWN as a mismatch

The RTF line itself says "At each clock half-hour or hour" and "the half-hourly check". Read with those, "top/bottom of an hour" means HH:00 and HH:30, which matches the paper (Q1). Mismatch 4 now consists only of its second bullet (the compass file :41 lists times to 11:30 ET only).
```
Sun 15 Nov 2026 16:43:27 UTC
$ sed -n 34p "<RTF>" | /usr/bin/grep -o -E (the three timing clauses)
At each clock half-hour or hour, two boundaries ("noise band") are drawn around the day's open.
 When price breaches the upper (lower) boundary at the top/bottom of an hour, a long (short) position is opened.
 The setup is binary \'97 either price has closed beyond the band at the half-hourly check or it has not.
$ sed -n 34p "<RTF>"   (full line)
**1. Mechanical description.** At each clock half-hour or hour, two boundaries ("noise band") are drawn around the day's open. The boundaries are computed as *open \'d7 (1 \'b1 average return-from-open over a 14-day lookback at that minute-of-day)*, with overnight gap adjustments. When price breaches the upper (lower) boundary at the top/bottom of an hour, a long (short) position is opened. The position uses dynamic trailing stops (e.g., VWAP-based) and is flat at the cash close. One position per session; sized to a 2% daily volatility target capped at 4\'d7 notional. The setup is binary \'97 either price has closed beyond the band at the half-hourly check or it has not.\
$ git status --short -- "<RTF>"   (empty = clean at HEAD)
```

### D3. Mismatch 6 and the spec :99 elision: CONFIRMED

Footnote 2 is two sentences, not one. It also says "For more details see our previous publication [5]." Spec `:99` repeats "VWAP anchored at 09:30, market-hours only". So the earlier note under the spec excerpt ("The omitted text is about the reference price and the flat time, not the stop") is **withdrawn as incomplete**: the elided text also contains the VWAP anchor, and VWAP is part of the stop. The finding of mismatch 6 stands: "anchored at the 09:30 open" is not in the footnote, and "anchor" has 0 hits anywhere in the 43 pages.
```
Sun 15 Nov 2026 16:43:27 UTC
$ sed -n 34,35p page-13.txt
34:   2
35:       VWAP is computed only using market hours data. For more details see our previous publication [5].
$ /usr/bin/grep -n -i anchor page-*.txt ; echo exit=$?
exit=1
$ sed -n 99p docs/specs/2026-07-16-b2-noise-area-ruleset.md
Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = max/min(Open_{9:30}, PrevClose)`; VWAP anchored at 09:30, market-hours only; **flat at 16:00** (or the trader-chosen 11:30 — see D8). Entry via `EnterLongStopMarket`/`EnterShortStopMarket` at the boundary is a reasonable NT8 realization of "act at the next HH:00/HH:30 stamp if price is outside the band," but note the paper acts on the **stamp**, not on an intrabar stop-touch — a stop-market order can fill mid-bar and diverge slightly; reconcile in b2-signal-repro.
$ git status --short -- docs/specs/2026-07-16-b2-noise-area-ruleset.md   (empty = clean)
```

### D4. Missed candidates for "the project's research summary": CONFIRMED

Two project texts that use the words "checked at HH:00/HH:30" and "at HH:00/HH:30 checkpoints" for the band/VWAP exit were missing from the candidate list. `docs/specs/2026-11-06-walk-forward-values.md` is modified in the working tree compared with HEAD `d9fc5f0`, but its line 63 is identical at HEAD (the `-F -x` match below). Which file the ruling meant by "the project's research summary" stays **UNVERIFIED**. I do not choose one.
```
Sun 15 Nov 2026 16:43:27 UTC
$ git show d9fc5f0:docs/reports/2026-11-14-r3-recheck-manager.md | sed -n 9p
| Noise-Area baseline (BandOrVWAP) | band/VWAP level, checked at HH:00/HH:30 bar closes, market exit | NO | −$542.40 | 10 | −$705.10 | 5 |
$ git status --short -- docs/reports/2026-11-14-r3-recheck-manager.md   (empty = clean)
$ sed -n 63p docs/specs/2026-11-06-walk-forward-values.md
- **BandOrVWAP** — OBSERVED (code): the base file's logic: at HH:00/HH:30 checkpoints, a long exits when `Close <= max(UpperBound, VWAP)`, a short when `Close >= min(LowerBound, VWAP)` (`PraxisNoiseAreaBreakout.cs:205-220`); flat on the 16:00-stamped bar (`:189-193`).
$ git diff --stat d9fc5f0 -- docs/specs/2026-11-06-walk-forward-values.md
 docs/specs/2026-11-06-walk-forward-values.md | 42 ++++++++++++++--------------
 1 file changed, 21 insertions(+), 21 deletions(-)
$ git show d9fc5f0:<same file> | /usr/bin/grep -n -F -x -- "<working-tree line 63>" | cut -c1-12
63:- **BandO
```
Wider search (the brief's command; each line cut to 260 characters for width, names masked; `head -40` caps it, so the r3-recheck manager report is not in the first 40 lines):
```
Sun 15 Nov 2026 16:43:27 UTC
$ /usr/bin/grep -rn -i -E 'checked at HH|HH:00/HH:30.*(stop|exit)|band/VWAP|band-or-VWAP|BandOrVWAP' docs/ Redemtion/ *.md --exclude-dir=.git | head -40 | cut -c1-260
docs/specs/2026-07-16-b2-noise-area-ruleset.md:60:- **Improved stop (paper's preferred model):** trailing stop at **band-or-VWAP**, whichever is tighter to price:
docs/specs/2026-07-16-b2-noise-area-ruleset.md:96:| **stop-ATR mult** | **no paper analog** | Paper uses band/VWAP stops, not ATR. If Block-2 insists on an ATR stop it is a **new, untested variant** — flag for trader (§7). Faithful port = disable ATR, use the 
docs/specs/2026-07-16-b2-noise-area-ruleset.md:97:| **exit policy** | discrete: {opp-band ; max/min(band,VWAP) ; +vol-target} | Enum input `ExitMode` ∈ {OppBand, BandOrVWAP}. Paper's preferred = **BandOrVWAP**. |
docs/specs/2026-07-16-b2-noise-area-ruleset.md:99:Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = max/min(Open_{9:30}, PrevClose)`; VWAP anchored at 09:30, market-hours only; **flat at 16:00** (or the trader-chose
docs/specs/2026-07-16-b2-noise-area-ruleset.md:108:- **T4: exit mode** — OppBand vs BandOrVWAP (paper prefers the latter).
docs/specs/2026-07-16-b2-noise-area-ruleset.md:153:Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = max/min(Open_{9:30}, PrevClose)`; VWAP anchored at 09:30, market-hours only; **flat at 16:00** (or the trader-chos
docs/specs/2026-11-06-walk-forward-values.md:17:- **Ruling 4 of 2026-11-06** (DECISIONS.md D-2026-11-06-B, from DECISION_LOG `2026-11-06T20:08:28Z`, WHO: [name withheld]), verbatim: "4. Walk-forward arm (b) and spec NEEDS [name withheld], under "We're not here to fuck around" — s
docs/specs/2026-11-06-walk-forward-values.md:41:- Rules: `Lookback = 14` (`:74`), `BandSigmaMult = 1.0` (`:76`), `ExitMode = PraxisNoiseExitMode.BandOrVWAP` (`:118`), `Contracts = 1` (`:119`) — OBSERVED (code). Nothing optimised — RULED (D-2026-11-05-A item 1:
docs/specs/2026-11-06-walk-forward-values.md:52:| Exit policy | BandOrVWAP (OBSERVED, code `:118`) | {BandOrVWAP, OppBand, Flat1559} | RULED — ruling 4 of 2026-11-06: "exit policies BandOrVWAP / OppBand / Flat1559" |
docs/specs/2026-11-06-walk-forward-values.md:63:- **BandOrVWAP** — OBSERVED (code): the base file's logic: at HH:00/HH:30 checkpoints, a long exits when `Close <= max(UpperBound, VWAP)`, a short when `Close >= min(LowerBound, VWAP)` (`PraxisNoiseAreaBreakout.c
docs/specs/2026-11-06-walk-forward-values.md:65:- **Flat1559** — RULED (Q5: "Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar, as in _Flat1559.cs."): BandOrVWAP exits, with the flatten decided on the close of the 15:59-stamped bar (`mod >= 959`; `
docs/specs/2026-11-06-walk-forward-values.md:77:- **Precedence** — SETTLED: on every bar, (1) the session flat, (2) the stop, (3) the checkpoint exits and entries. The session flat is the session's last bar — 16:00, or 12:00 / 12:15 / 14:03 on early-close days
docs/specs/2026-11-06-walk-forward-values.md:97:- **Tie-break** — SETTLED: equal S to 1e-9 → the configuration nearest the anchor, as the sum of grid-step distances on lookback (anchor 14) and k (anchor 1.0), plus exit-policy distance 0 for BandOrVWAP, else 1.
docs/specs/2026-11-06-walk-forward-values.md:145:- **New enum** — SETTLED: the new file declares `PraxisNoiseArmBExitPolicy { BandOrVWAP, OppBand, Flat1559 }`. Reason (OBSERVED in code; compile result INFERRED): `PraxisNoiseExitMode` is declared once in the ba
docs/specs/2026-11-06-walk-forward-values.md:153:| `ExitPolicy` | `PraxisNoiseArmBExitPolicy` | BandOrVWAP | `ExitMode` (`:300`) |
docs/specs/2026-11-06-walk-forward-values.md:164:| T1 | 14 | 1.0 | 0 | BandOrVWAP | 1 | input value 0, T1–T3 only |
docs/specs/2026-11-06-walk-forward-values.md:167:| T4 | 14 | 1.0 | 1.5 | BandOrVWAP | 1 | also T12a and T13a's twin |
docs/specs/2026-11-06-walk-forward-values.md:168:| T5a | 18 | 1.0 | 1.5 | BandOrVWAP | 1 | differs from T4 in Lookback only |
docs/specs/2026-11-06-walk-forward-values.md:169:| T5b | 14 | 1.2 | 1.5 | BandOrVWAP | 1 | differs from T4 in k only |
docs/specs/2026-11-06-walk-forward-values.md:170:| T5c | 14 | 1.0 | 2.25 | BandOrVWAP | 1 | differs from T4 in m only |
docs/specs/2026-11-06-walk-forward-values.md:172:| T5e | 14 | 1.0 | 1.5 | BandOrVWAP | 1 | T4's inputs again, run straight after T5d |
docs/specs/2026-11-06-walk-forward-values.md:176:| T13a | 14 | 1.0 | 1.5 | BandOrVWAP | 2 | |
docs/specs/2026-11-06-walk-forward-values.md:181:  - T1: ArmB at (14, 1.0, 0, BandOrVWAP) gives the base file's trade list row for row (entry/exit time, price, side, quantity, exit name) and its totals, 1,190 trades / $197,327.60 (results report `:73`, `:402`)
docs/specs/2026-11-06-walk-forward-values.md:188:    - **Does NOT catch:** a stop at the wrong distance or on the wrong ATR (T8); the stop under OppBand or Flat1559 (T4 is BandOrVWAP only; T8 runs every policy); a dead m (T5c, T8); a broken stop that trips now
docs/specs/2026-11-06-walk-forward-values.md:190:    - **Does NOT catch:** a property that is printed right but not used where it matters (the readback prints the property, not its uses); a wrong use that still changes the trades (e.g. Lookback 18 used as 17: 
docs/specs/2026-11-06-walk-forward-values.md:195:  - T8 (stop exits against the oracle; T6 checks only the values the strategy prints, not where it exits). Runs: every stop-on acceptance run and the 81. Stop exits carry the signal name `XStop`. **Session-flat 
docs/specs/2026-11-06-walk-forward-values.md:203:  - T12 (ExitPolicy under the stop, the test whose absence parked version 1). Runs: T12a = T4's run (14, 1.0, 1.5, BandOrVWAP), T12b = T5d's run (14, 1.0, 1.5, OppBand), T12c (14, 1.0, 1.5, Flat1559). **Exit nam
docs/specs/2026-11-06-walk-forward-values.md:206:    - (iii) Policy-rule oracle, for non-stop exits. For each trade, the script walks the checkpoints after the entry's decision checkpoint, up to and including the exit decision bar d (T8's definition). A checkp
docs/specs/2026-11-06-walk-forward-values.md:210:    - (vii) Power. The script applies the OppBand rule to T12a's trades and the BandOrVWAP rule to T12b's. Each must give at least one trade whose c* differs from the run's own rule; otherwise T12 is not passed.
docs/specs/2026-11-06-walk-forward-values.md:222:| ExitPolicy | T5(ii) (T5d = T4, whatever the fixed policy); T12(i) unconditionally; T12(ii) (Flat1559's `FlatEOD` vs the 16:00 `Exit on session close`); T12(iii) on the runs whose policy differs from the fixed 
docs/specs/2026-11-06-walk-forward-values.md:234:- (d) **Enum numeric order.** `ExitPolicy` is {BandOrVWAP = 0, OppBand = 1, Flat1559 = 2}; the base enum is {OppBand = 0, BandOrVWAP = 1} (:626). The bridge must send `ExitPolicy` by name. How the bridge convert
docs/specs/2026-11-06-walk-forward-values.md:247:| Q5 | "Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar, as in _Flat1559.cs." | §3 |
docs/specs/2026-11-06-walk-forward-values.md:290:| 31 | Enum | `PraxisNoiseArmBExitPolicy { BandOrVWAP, OppBand, Flat1559 }` | Base enum plus a `bool` for the 15:59 flatten | §9 |
docs/reports/2026-11-13-strategy-review-index-worker5.md:87:1. `docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md` (committed in 9ff8a48). VM bridge queue T1-T3 (bridge-driven Strategy Analyzer runs). Source `:5`: "the VM Claude Code session
docs/reports/2026-11-13-strategy-review-index-worker5.md:302:docs/reports/2026-11-13-research-filing-worker2.md:405:15:| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615 | -$38,9
docs/reports/2026-11-13-strategy-review-index-worker5.md:303:docs/reports/2026-11-13-research-filing-worker2.md:407:17:| T3 | BandOrVWAP | 1,173 | $176,392.92 | 1.26 | -$38,905
docs/reports/2026-11-13-strategy-review-index-worker5.md:306:docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:15:| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615
docs/reports/2026-11-13-strategy-review-index-worker5.md:307:docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:17:| T3 | BandOrVWAP | 1,173 | $176,392.92 | 1.26 |
docs/reports/2026-11-14-evening-rulings-worker3.md:113:vm-queue :15  | T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615 | -$38,905.64 | Exact match |
docs/reports/2026-10-31-a9d-walkthrough-future-row.md:168:| Exit mode (files base/1/2 only) | BandOrVWAP for base and file 2; **OppBand** for file 1 (its default) |
$ (same command without head) | wc -l
     653
```

### D5. Omitted paper passages: CONFIRMED

FAQ preface: the authors say they do not disclose "specific trading rules that we utilize to enhance strategy efficiency". FAQ Q11: they call it "a simplified model". §4.6 (heading p. 24 line 15): the slippage study sends market orders "a few milliseconds before the start of minute HH:MM" and measures slippage "relative to the Open price of minute HH:MM". FAQ Q22 gives 7,964 trades for "VWAP + Current Band", while Table 4 (p. 16) and the p. 14 text give 7,668. The paper does not reconcile the two counts. The Q22 table says it covers "May 2007 to December 2024" (p. 40 line 10); p. 14 says Table 4 covers "the 17-year period".
```
Sun 15 Nov 2026 16:43:29 UTC
--- p30:1-7 (FAQ preface)
1:Frequently Asked Questions (FAQs)
2:Following the publication of this paper, we received hundreds of insightful questions
3:from readers. While we are unable to address every inquiry—particularly those requiring
4:significant extensions of our research or the disclosure of specific trading rules that we
5:utilize to enhance strategy efficiency—we have compiled answers to the most common
6:questions. This section will be updated regularly to include new Q&As that may arise
7:in the future.
--- p34:1-5 (FAQ Q11)
1:Q11. Is it possible to automate this strategy in a personal trading account?
2:How?
3:Yes, but please note that this is a simplified model that can be further enhanced with
4:a few small adjustments. The goal of our papers is not to provide ready-to-use trading
5:strategies, but rather to introduce traders and readers to potential trading edges.
--- p24:15 (section heading)
15:4.6    The Impact of Commissions (and Slippage)
--- p25:5-8 and 20-22 (§4.6)
5:funded with $100,000, we instruct an algorithm to send market orders on SPY for $100,000
6:just a few milliseconds before the start of minute HH:MM. The algorithm randomly
7:takes long or short positions. The goal of the study is to evaluate the magnitude of the
8:slippage relative to the Open price of minute HH:MM. Mathematically, we evaluate the
20:orders without significantly impacting the market. For simplicity and consistency with
21:our real-trading analysis, we have chosen to apply a standard slippage rate of $0.001 in
22:our backtest.
--- p40:3-5 (FAQ Q22) and p40:10
3:to a slight increase in the average holding period per trade. Consequently, the number
4:of trades decreases significantly from 7,964 (for the VWAP + Current Band version) to
5:6,728 (for the VWAP-only version). This reduction in trade frequency may enhance cost
10:performance from May 2007 to December 2024.
--- p16:32 (Table 4) and p14:10-11
32:Intra Mom.   Curr.Band + VWAP    100%   7,668       1.8       37%       0.09
10: result in a significant increase in the total number of trades, rising from 5,494 to 7,668
11: over the 17-year period (see Table 4). These results highlight the enhanced risk-return
```
One more search across all 43 pages for exits, loss limits and stop-check timing:
```
Sun 15 Nov 2026 16:43:29 UTC
$ /usr/bin/grep -n -i -E "stop|exit|unwound|loss limit|max(imum)? loss|drawdown limit|risk limit|liquidat|time.?stop|holding period|semi-hourly|intraday check|tick|high frequency|minute-by-minute|each minute|every minute" page-*.txt | cut -c1-200
page-02.txt:30:       namic trailing stops to mitigate downside risks while allowing for unlimited upside
page-03.txt:23:3- to 12-month holding periods and the profitability of these portfolios is not explained
page-04.txt:31:intraday trends caused by sticky demand/supply imbalances. Unlike the aforementioned
page-09.txt:15:caused by short-term market fluctuations, trading is restricted to semi-hourly intervals,
page-09.txt:20:Positions are unwound either at market Close or if there is a crossover to the opposite
page-09.txt:23:dence of demand/supply imbalance. Stop losses can also be triggered only on semi-hourly
page-11.txt:8:matic shifts in market character. A trailing stop set at the opposite side of the Noise
page-11.txt:20:Table 1: Summary statistics of intraday momentum strategy with stop loss at opposite band and SPY
page-11.txt:25:   Strategy         Stop        Size            IRR     Vol                     MDD   Alpha   Beta
page-12.txt:1:Figure 4: SPY price action on 20 January 2022 illustrates our model strategy’s entry and exits. The
page-12.txt:2:base strategy uses the opposite band as a trailing stop. Following a sharp reversal in SPY in the last 2
page-12.txt:12:the Upper Boundary of the Noise Area as a trailing stop for our long positions, and vice
page-12.txt:15:improves the return from -2.19% to -0.31%. While a tighter stop loss can significantly
page-12.txt:20:This observation underscores the need to balance the protective benefits of a tighter stop
page-13.txt:1:                  (a) Stop = UpperBand                            (b) Stop = max(VWAP,UpperBand)
page-13.txt:5:Figure 5: Improvement in our strategy’s exit by incorporating tighter trailing stop losses. In Figure
page-13.txt:6:(a), the trailing stop is based on the upper band of the Noise Area, while in Figure (b), it is based on
page-13.txt:12:VWAP as a trailing stop for intraday trend exposures2 . Once a position is established,
page-13.txt:14:Mathematically, the trailing stops for long and short postions are defined as:
page-13.txt:17:                 Long TrailingStopt,HH:M M = max(U Bt,HH:M M , V W APt,HH:M M )
page-13.txt:19:                 Short TrailingStopt,HH:M M = min(LBt,HH:M M , V W APt,HH:M M )
page-13.txt:26:cacy as a dynamic stop loss mechanism that aligns closely with market momentum, thus
page-13.txt:30:To demonstrate the economic advantages of these trailing stop refinements, we have con-
page-14.txt:1: Figure 6: Comparison of equity curves of intraday momentum strategy with a) stop loss at opposite
page-14.txt:7: from 0.61 to 1.24, while the Hit Ratio decreased to 43% due to tighter stops. As exhibited
page-14.txt:9: turn sees a 5% improvement (from -10.3% to -4.8%). However, the tighter stop loss does
page-14.txt:20: Table 2: Summary statistics of intraday momentum strategy with a) stop loss at opposite band, b)
page-14.txt:25:Strategy          Stop                  Size                IRR     Vol                     MDD   Alpha   Beta
page-15.txt:1:  Table 3: Summary statistics of intraday momentum strategy with a) stop loss at opposite band, b)
page-15.txt:7:Strategy          Stop                  Size                 IRR    Vol                     MDD   Alpha   Beta
page-16.txt:1:Figure 7: Comparison of equity curves of intraday momentum strategy with a) stop loss at opposite
page-16.txt:19:Table 4: Summary statistics at trade-level of intraday momentum strategy with a) stop loss at opposite
page-16.txt:24:                                                 Avg. Trade    Hit    Avg. PnL    Max Loss        Max Gain
page-16.txt:25:Strategy     Stop                Size   Trades
page-17.txt:11:momentum strategy that employs a trailing stop based on the current band and VWAP,
page-22.txt:17:Given the complexity of the decision between higher returns and better risk-adjusted
page-26.txt:11:dynamic trailing stops, yields substantial returns over the period from 2007 to early 2024.
page-30.txt:12:ity multiplier, slippage assumption, and even ticker) to create tailored versions of the
page-30.txt:38:applicable to any ticker but is designed specifically for intraday time frames. We have
page-34.txt:9:a trading strategy, in our portfolios, we update signals at high frequency using IQFeed
page-40.txt:1:Q22. How do the results change if we use only VWAP as a trailing stop?
page-40.txt:2:Switching to a VWAP-only trailing stop results in less restrictive exit conditions, leading
page-40.txt:3:to a slight increase in the average holding period per trade. Consequently, the number
page-40.txt:13:       Strategy     Stop               Leverage               IRR    Vol                     MDD
page-43.txt:4:     Table A1: Summary statistics of intraday momentum strategy with a) stop loss at opposite band, b) current band with VWAP, c) as in (b) with the
page-43.txt:9:            Strategy         Stop                 Size            IRR       Vol                     MDD   Alpha   Beta    Skewness   Worst Day   Best Day
--- p02:29-31 (abstract) and p26:10-11 (conclusion)
29:       which have been discussed in our previous papers, we introduce the use of dy-
30:       namic trailing stops to mitigate downside risks while allowing for unlimited upside
31:       potential. From 2007 to early 2024, the resulting intraday momentum portfolio
10:tions of abnormal demand/supply imbalance in intraday price action and incorporating
11:dynamic trailing stops, yields substantial returns over the period from 2007 to early 2024.
--- FAQ question titles
page-30.txt:9:Q1. Can you share the code used to backtest the strategy?
page-30.txt:24:Q2. Where do you source your data? Can you share the database?
page-30.txt:33:Q3. How can I incorporate the Noise Area into my intraday charts?
page-31.txt:1:Q4. Do you have a monthly performance table for the strategy?
page-31.txt:29:Q5. Do the long and short legs of the strategy contribute equally? Can you
page-31.txt:39:Q6. How does the lookback period for sigma affect the results?
page-32.txt:1:Q7. How did the strategy perform during the worst 10 quarters for the S&P
page-32.txt:27:Q8. Can we consider the strategy a hedge for a passive long market expo-
page-33.txt:13:Q9. What software did you use for the historical backtest?
page-33.txt:18:Q10. I have tried to replicate the backtest, but my results differ. Can you
page-34.txt:1:Q11. Is it possible to automate this strategy in a personal trading account?
page-34.txt:19:Q12. Does the strategy work with other ETFs or stocks?
page-35.txt:1:Q13. Does the strategy work also in futures markets?
page-35.txt:53:Q14. To me, the strategy seems over-optimized!
page-36.txt:22:Q15. The slippage model you used seems inaccurate. How do the results
page-37.txt:25:Q16. If the strategy is so profitable, why share it with the public?
page-37.txt:36:Q17. The results are great, can you manage my account using this strategy?
page-37.txt:43:Q18. Does the Intraday Momentum strategy exhibit intraday seasonalities?
page-38.txt:1:Q19. Does the profitability of short trades increase when market volatility
page-39.txt:1:Q20. How does total profitability change if we only trade when the VIX is
page-39.txt:12:Q21. Should we open short trades only when the market is trading below
page-40.txt:1:Q22. How do the results change if we use only VWAP as a trailing stop?
page-40.txt:23:Q23. How does the average trade profitability change over the years?
page-41.txt:1:Q24. How has the strategy performed since the paper was published?
page-42.txt:26:Q25. I have a question that is not part of the above FAQs!
```
What it found beyond Q1 to Q12 and the passages above: the abstract (p. 2 lines 29-31) says "dynamic trailing stops to mitigate downside risks while allowing for unlimited upside potential", and the conclusion (p. 26 lines 10-11) says "dynamic trailing stops". Neither names a fixed loss or a check time. The p. 4 line 31 hit ("sticky") and the p. 3 line 23 hit ("holding periods" in the literature review) are not about this strategy's exits. No FAQ title is about a loss limit or a stop-check time; Q22 (VWAP-only stop) is already covered by Q12.

### D6. Line 190 statements: CONFIRMED, BOTH WITHDRAWN

Withdrawn: (1) "all omitted hits are table rows or the Concretum Bands indicator FAQ". The omitted hits for pages 18 and later include prose: p18:33, p19:23, p19:26, p21:33, p23:23, p31:41, p36:2, p37:48-49 and p40:5, plus the VM formulas on p21:41 and 43 and the reference on p28:16. (2) the statement that "end of day" and "market close" had 0 hits and that the only close-time wording is "market Close" (p. 9). With `-i`, "market close" hits p9:20 and p9:31 even line by line. Across line breaks there are two more occurrences, "end / of day" (p10:11-12, about equity at the end of day t − 1) and "until market / close" (p37:48-49, FAQ Q18 on intraday seasonality). Neither describes an exit rule.
```
Sun 15 Nov 2026 16:43:29 UTC
$ /usr/bin/grep -n -i -E "close|closing|end of (the )?day|market close|4:00|16:00|VWAP|boundar|noise area|band" page-1[89].txt page-[234]?.txt | cut -c1-190
page-18.txt:33:      daily range, and the Close is above the 85th percentile, suggesting a strong bullish
page-19.txt:23:      and Close are within the top 75th percentile of the daily range (or the reverse for
page-19.txt:26:    • Strong/Weak Closure: Identifies days where the closing price is above the 90th
page-21.txt:33:the Noise Area, making the model either more conservative (for values above 1) or more
page-21.txt:41:   UpperBoundt,HH:MM = max Opent,9:30 , Closet−1,16:00 × (1 + VM × σt,9:30−HH:MM )
page-21.txt:43:   LowerBoundt,HH:MM = min Opent,9:30 , Closet−1,16:00 × (1 − VM × σt,9:30−HH:MM )
page-23.txt:23:tory variable) as of the previous day’s close. We anticipate that a higher RSI indicates
page-28.txt:16: [5] C. Zarattini and A. Aziz. Volume weighted average price (vwap) the holy grail for
page-30.txt:33:Q3. How can I incorporate the Noise Area into my intraday charts?
page-30.txt:34:If you’re using TradingView, you can easily add the Noise Area to your charts by uti-
page-30.txt:35:lizing the free indicator called Concretum Bands. You can access the TradingView
page-30.txt:36:indicator from https://bit.ly/CBands6 . In the spirit of transparency, the PineScript
page-30.txt:47:      https://www.tradingview.com/script/CUpWCZhe-Concretum-Bands/
page-31.txt:41:period used to compute the Noise Area. Empirical evidence shows that the highest Total
page-36.txt:2:boundaries of the Noise Area. The two main parameters that define the Noise Area are:
page-37.txt:48:trends tend to pause during lunchtime, they resume strongly from 14:00 until market
page-37.txt:49:close. This suggests that although the intraday trend strategy is effective for most of the
page-40.txt:1:Q22. How do the results change if we use only VWAP as a trailing stop?
page-40.txt:2:Switching to a VWAP-only trailing stop results in less restrictive exit conditions, leading
page-40.txt:4:of trades decreases significantly from 7,964 (for the VWAP + Current Band version) to
page-40.txt:5:6,728 (for the VWAP-only version). This reduction in trade frequency may enhance cost
page-40.txt:16:       Intra Mom.   Opp.Band             1x            169    5.8    10.7    0.58    54.0    21
page-40.txt:17:       Intra Mom.   Curr.Band + VWAP     1x             393    9.5    7.6    1.23    44.0    12
page-40.txt:18:       Intra Mom.   Curr.Band + VWAP   Dynamic         2382   19.9   14.3    1.35    44.0    25
page-40.txt:19:       Intra Mom.   VWAP               Dynamic         1846   18.3   15.5    1.17    46.0    27
page-43.txt:4:     Table A1: Summary statistics of intraday momentum strategy with a) stop loss at opposite band, b) current band with VWAP, c) as in (b) with the
page-43.txt:12:            Momentum         Opp.Band            100%     178%     6.2%    10.9%    0.61    54%     21%    7.1%   -0.05    -1.24      -10.3%      6.1%
page-43.txt:13:            Momentum         Curr.Band + VWAP    100%     380%    9.7%      7.7%    1.24    43%     12%    9.9%   -0.03    1.29        -4.8%       5.1%
page-43.txt:14:            Momentum         Curr.Band + VWAP    Dyn.    1,985%   19.6%    14.3%    1.33    43%     25%   19.6%   -0.07    1.22        -4.5%       9.1%
$ /usr/bin/grep -n -i -E "end of (the )?day|market close" page-*.txt   (single-line)
page-09.txt:20:Positions are unwound either at market Close or if there is a crossover to the opposite
page-09.txt:31:market movements. All positions are closed at market Close, adhering to the strategy’s
--- split occurrences
11:where AU Mt−1 represents the equity (or Asset Under Management) available at the end
12:of day t − 1.
48:trends tend to pause during lunchtime, they resume strongly from 14:00 until market
49:close. This suggests that although the intraday trend strategy is effective for most of the
```

### D7. Unsupported claims: (a) and (b) now supported with evidence, (c) figure replaced, (d) relabelled

(a) Line 75 "where the third author is affiliated": **supported**. On p. 2 the third author is Andrea Barbon with superscript 4, and affiliation 4 is the University of St.Gallen. Page 1 names "University of St.Gallen and Swiss Finance Institute". The p. 2 lines 13-14 are withheld below because they contain email addresses.
```
Sun 15 Nov 2026 16:43:29 UTC
--- p01, non-blank lines
1:Concretum Research Lugano
5:Peak Capital Trading and Bear Bull Traders, Canada
9:University of St.Gallen and Swiss Finance Institute
10:
--- p02:5-10
5:                          Carlo Zarattini1 , Andrew Aziz2,3 , Andrea Barbon4
6:
7:1 Concretum Research, Piazza Molino Nuovo 8, 6900 Lugano, Switzerland
8:2 Peak Capital Trading, 744 West Hastings Street, Vancouver, BC, Canada V6C 1A5
9:3 Bear Bull Traders, 744 West Hastings Street, Vancouver, BC, Canada V6C 1A5
10:4 University of St.Gallen, Dufourstrasse 50, 9000 St. Gallen, Switzerland
```
(b) Line 71 "the authors' firm's web page": **narrowed**. Affiliation 1 (Carlo Zarattini) is "Concretum Research", and the paper hosts its code at concretumgroup.com (FAQ Q1). That concretumgroup.com is Concretum Research's own site is INFERRED from the name. The paper does not say so in the extracted text. Corrected wording: "A6 is a page on concretumgroup.com, the site the paper names for its code".
```
Sun 15 Nov 2026 16:43:29 UTC
--- p02:7
7:1 Concretum Research, Piazza Molino Nuovo 8, 6900 Lugano, Switzerland
--- p30:9-11 and 43-45
9:Q1. Can you share the code used to backtest the strategy?
10:Yes! We shared the Matlab and Python versions of the code in www.concretumgroup.
11:com/coding. Users can easily change the backtest parameters (look-back window, volatil-
43:      https://www.concretumgroup.com/backtesting-riding-intraday-trends-in-us-markets-using-matlab/
44:  5
45:      https://www.concretumgroup.com/python-backtesting-beat-the-market-an-effective-intraday-momentum-strategy-for-the-sp500-etf-spy/
```
(c) Line 34 "matched **60 files**": **replaced**. The re-run gives 76. Only two matching files are newer than 16:25Z, and both are this unit's own reports. 76 − 2 = 74, which still does not reproduce 60. Why the original count was 60 is UNVERIFIED. Eleven other matching files have an mtime earlier today (listed; I did not check who wrote them), so the count depends on when the original search ran, and I do not know that time.
```
Sun 15 Nov 2026 16:43:29 UTC
$ /usr/bin/grep -rIl -i -E "Zarattini|Beat the Market|4824172|Barbon" --exclude-dir=.git . | wc -l
      76
--- matching files with mtime after 2026-11-15T16:25:00Z
2026-11-15T16:31:21Z ./docs/reports/2026-11-15-noise-area-paper-read-worker1.md
2026-11-15T16:38:49Z ./docs/reports/2026-11-15-noise-area-paper-read-worker2.md
--- matching files with mtime on 2026-11-15 up to 16:25:00Z
2026-11-15T14:42:50Z ./docs/reports/2026-11-15-voice-notes-open-questions.md
2026-11-15T14:58:31Z ./docs/reports/2026-11-15-rulings-filing-worker2.md
2026-11-15T15:12:16Z ./docs/reports/2026-11-15-rulings-filing-worker4.md
2026-11-15T15:28:55Z ./docs/reports/2026-11-15-rulings-filing-worker6.md
2026-11-15T15:33:12Z ./docs/reports/2026-11-15-rulings-filing-worker7.md
2026-11-15T15:42:34Z ./docs/reports/2026-11-15-rulings-filing-worker8.md
2026-11-15T15:43:31Z ./MANIFEST.md
2026-11-15T15:55:31Z ./DECISIONS.md
2026-11-15T16:04:55Z ./STATUS.md
2026-11-15T16:17:20Z ./HANDOFF.md
2026-11-15T16:23:53Z ./DECISION_LOG.md
```
(d) Lines 231-237: the four-line block was an **unlabelled excerpt**, not the full output. The full run has 23 hits. Order wording beyond p. 25 line 5 and p. 34 line 10 also appears at p25:20 ("large orders"), p25:29 ("order methodologies") and p36:36 (FAQ Q15, I-Star slippage model, "their order"). None of the 23 hits describes a resting stop order or a fixed loss limit. Names in the p. 5 literature-review hits are masked. The final `grep -c` prints 0 and exits 1 because no hit line contains an at-sign.
```
Sun 15 Nov 2026 16:43:32 UTC
$ /usr/bin/grep -n -i -E "order|limit|fixed|percent|% of|per trade" page-*.txt
page-02.txt:25:       500. Unlike the academic literature that typically limits trading to the last 30 min-
page-02.txt:30:       namic trailing stops to mitigate downside risks while allowing for unlimited upside
page-04.txt:32:studies, our model does not limit the trading to the last 30-minutes of the trading session;
page-05.txt:16:for under-reaction, based on investors’ limited attention to news, is proposed by [name withheld]
page-05.txt:17:[names withheld] [15]. Such behavior may stem from limited cognitive abilities or be
page-09.txt:32:protocol to limit exposure to overnight market changes.
page-10.txt:1:The strategy allocates exposure equal to 100% of the equity available at the beginning
page-18.txt:32:   • Trend Days: Identifies days when the Open is below the 15th percentile of the
page-18.txt:33:      daily range, and the Close is above the 85th percentile, suggesting a strong bullish
page-19.txt:23:      and Close are within the top 75th percentile of the daily range (or the reverse for
page-19.txt:27:      percentile (strong closure) or below the 10th percentile (weak closure) of the daily
page-20.txt:11:statistical reliability due to a limited number of observations (85 occurrences).
page-20.txt:16:However, in order to exploit higher expected returns, active day traders might consider
page-24.txt:31:approximately 20% of the days, we benefit from lower commission fees due to a 1-month
page-25.txt:5:funded with $100,000, we instruct an algorithm to send market orders on SPY for $100,000
page-25.txt:20:orders without significantly impacting the market. For simplicity and consistency with
page-25.txt:29:ity. Given the available diversity in commission structures and order methodologies, we
page-34.txt:10:and then automatically send orders to Interactive Brokers via IBML, a specialized Mat-
page-36.txt:36:their order and the overall participation in market volumes. Mathematically, we can
page-37.txt:32:trading limits. Academic research has shown that momentum-based strategies tend to
page-39.txt:6:regression results: limiting short trades to high volatility environments does not benefit
page-40.txt:3:to a slight increase in the average holding period per trade. Consequently, the number
page-40.txt:29:Thanks to the overall appreciation of SPY over the years, the same percentage move in
$ ... | wc -l
      23
$ ... | /usr/bin/grep -c <at-sign>
0
exit=1
```

### D8. Line 437 paraphrase: CONFIRMED

Line 437's "p. 8 says the bands widen through the day" drops the hedge. The paper says "Typically, the average intraday movement from the Open tends to increase over time, peaking at 16:00." Corrected wording: "p. 8 says the average intraday movement from the Open typically increases over the day, peaking at 16:00".
```
Sun 15 Nov 2026 16:43:32 UTC
10:A distinctive feature of this model is that the noise boundaries are dynamic and vary
11:throughout the trading day. This variation means, for example, that the market move-
12:ment required to indicate a demand/supply imbalance is different in the first 30 minutes
13:of trading compared to the first 6 hours. Typically, the average intraday movement from
14:the Open tends to increase over time, peaking at 16:00. As demonstrated in the simplified
```

### Effect on the answer

(a) Hard stop: **unchanged**. None of the passages added here states a fixed maximum loss known at entry. The new passages add the abstract's "dynamic trailing stops ... unlimited upside potential" (p. 2), the authors' statement that they do not disclose "specific trading rules that we utilize to enhance strategy efficiency" (p. 30), and "this is a simplified model" (p. 34). The last two mean the paper's "NO" covers only the rules the paper states. It does not cover rules the authors say they do not disclose.

(b) Timing: **unchanged**. Set times are explicit for the base model ("Stop losses can also be triggered only on semi-hourly intervals", p. 9). They are not restated for the band-or-VWAP stop ("as soon as the price crosses", p. 13). §4.6 adds that the slippage study's market orders are timed to "the start of minute HH:MM" and measured against that minute's Open (p. 25). That passage concerns execution in the slippage study and does not name a stop-check frequency. The two new project candidates under D4 say "checked at HH:00/HH:30" and "at HH:00/HH:30 checkpoints". Those are project wording, and one of them is described as code ("OBSERVED (code)"). Neither is paper text.

This addendum makes no trading recommendation and decides nothing. Those belong to the trader.

## Addendum 2 (worker 5, corrections to the worker 3 addendum)

This addendum corrects three items in the worker 3 addendum. Lines 1-954 above are unchanged. Paper text is the pdftotext -layout extract of the paper PDF (sha256 below).

### F1. Line 598 "(empty = clean at HEAD)": CONFIRMED, LABEL WITHDRAWN

The Verified Trading-Strategy Shortlist RTF is not tracked in git. `.gitignore` line 7 ignores all of `Redemtion/`, and `git ls-files` lists 0 files under it. The RTF has no version at HEAD `d9fc5f0`, so an empty `git status --short` says nothing about HEAD. The correct label for line 598 is: "(empty because the path is ignored; Redemtion/ files are working-tree only and have no HEAD version)". The RTF quotes in D2 and in the Mismatches section are working-tree content only. The grep for the label finds 4 lines. Only line 598 names a Redemtion/ path. Line 453 names docs/ files, and the paths on lines 613 and 623 are tracked (`git ls-files` below), so those labels are not affected by this item.
```
Sun 15 Nov 2026 16:54:30 UTC
$ git rev-parse --short HEAD
d9fc5f0
$ git cat-file -e d9fc5f0:"<RTF>"; echo $?
fatal: path 'Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf' exists on disk, but not in 'd9fc5f0'
128
$ git ls-files -- "<RTF>" | wc -l
0
$ git check-ignore -v -- "<RTF>"; echo exit=$?
.gitignore:7:Redemtion/	Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf
exit=0
$ sed -n 7p .gitignore
Redemtion/
$ git ls-files -- Redemtion/ | wc -l
0
$ /usr/bin/grep -n 'clean at HEAD\|clean = \|empty = clean' docs/reports/2026-11-15-noise-area-paper-read-worker1.md | cut -c1-120
453:Line numbers are from the working tree. `git status --short` showed the spec, the 4uu report and the scope proposal 
598:$ git status --short -- "<RTF>"   (empty = clean at HEAD)
613:$ git status --short -- docs/specs/2026-07-16-b2-noise-area-ruleset.md   (empty = clean)
623:$ git status --short -- docs/reports/2026-11-14-r3-recheck-manager.md   (empty = clean)
$ git ls-files -- docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/reports/2026-11-14-r3-recheck-manager.md
docs/reports/2026-11-14-r3-recheck-manager.md
docs/specs/2026-07-16-b2-noise-area-ruleset.md
```

### F2. D6 "two more occurrences ... Neither describes an exit rule": CONFIRMED, CORRECTED

Across line breaks there are **three** occurrences, not two. The third is the Figure 2 caption, p. 9 lines 6-7, "closed at the market / Close (16:00)". It **does** describe an exit rule: "Please note that all positions are closed at the market Close (16:00)." This caption is already quoted as Q3. Corrected D6 wording: "Across line breaks there are three more occurrences: "market / Close" (p9:6-7, the Figure 2 caption, which states the 16:00 exit, Q3), "end / of day" (p10:11-12, about equity at the end of day t − 1) and "until market / close" (p37:48-49, FAQ Q18 on intraday seasonality). Only the p. 9 caption describes an exit rule."
```
Sun 15 Nov 2026 16:54:30 UTC
$ sed -n 5,7p page-09.txt | cat -n   (numbers 1-3 = lines 5-7)
     1	Figure 2: The time-varying boundary areas on SPY for 31 January 2022 (a) and 29 April 2022 (b) and
     2	the resulting trades based on our base-model. Please note that all positions are closed at the market
     3	Close (16:00).
$ sed -n 11,12p page-10.txt
where AU Mt−1 represents the equity (or Asset Under Management) available at the end
of day t − 1.
$ sed -n 48,49p page-37.txt
trends tend to pause during lunchtime, they resume strongly from 14:00 until market
close. This suggests that although the intraday trend strategy is effective for most of the
$ (python3 -I, regex "end\s+of\s+(the\s+)?day|market\s+close", re.I, over page-*.txt; print matches containing a newline)
page-09.txt 6 'market\nClose'
page-10.txt 11 'end\nof day'
page-37.txt 48 'market\nclose'
```

### F3. Abstract passages: PARTLY CONFIRMED

- The entry-timing sentence is an omission (0 hits in this file before this addendum). The full sentence, p. 2 lines 25-28, raw lines:
  - 25: "500. Unlike the academic literature that typically limits trading to the last 30 min-"
  - 26: "utes of the trading session, our model initiates trend-following positions as soon"
  - 27: "as there is an indication of abnormal demand/supply imbalance in the intraday"
  - 28: "price action. Building on trading techniques commonly used by active day traders,"
  - The sentence begins after "500." on line 25 and ends at "price action." on line 28.
- The stop passage, p. 2 lines 28-31, raw lines 29-31: "which have been discussed in our previous papers, we introduce the use of dy-" / "namic trailing stops to mitigate downside risks while allowing for unlimited upside" / "potential. From 2007 to early 2024, the resulting intraday momentum portfolio". This passage is **not** an omission. It is already quoted in this file (raw p2:29-30 at lines 770-771, and assembled at line 802, see the grep below).
- The abstract does not name a check frequency. The only time figure in the sentence ("the last 30 minutes of the trading session") describes the academic literature, not this model. "as soon as there is an indication" names no interval. The single-line grep for "as soon as there" returns nothing because the phrase breaks across lines 26-27. The second grep shows both halves.
```
Sun 15 Nov 2026 16:54:31 UTC
$ shasum -a 256 /tmp/praxis-npr/dl/w1/paper.pdf
41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad  /tmp/praxis-npr/dl/w1/paper.pdf
$ sed -n 22,31p page-02.txt | cat -n   (numbers 1-10 = lines 22-31)
     1	                                                       Abstract
     2	       This paper investigates the profitability of a simple, yet effective intraday momen-
     3	       tum strategy applied to SPY, one of the most liquid ETFs that tracks the S&P
     4	       500. Unlike the academic literature that typically limits trading to the last 30 min-
     5	       utes of the trading session, our model initiates trend-following positions as soon
     6	       as there is an indication of abnormal demand/supply imbalance in the intraday
     7	       price action. Building on trading techniques commonly used by active day traders,
     8	       which have been discussed in our previous papers, we introduce the use of dy-
     9	       namic trailing stops to mitigate downside risks while allowing for unlimited upside
    10	       potential. From 2007 to early 2024, the resulting intraday momentum portfolio
$ /usr/bin/grep -n -i 'as soon as there' page-*.txt
$ /usr/bin/grep -c -i 'as soon as there is an indication\|indication of abnormal' /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md
0
$ /usr/bin/grep -n 'namic trailing stops' /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md | cut -c1-90
148:page-02.txt:30:       namic trailing stops to mitigate downside risks while allowing f
182:page-26.txt:11:dynamic trailing stops, yields substantial returns over the period from
494:Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Inde
497:Redemtion/Research Results/ROUND_2_RESEARCH_PROMPTS_Agent_2_and_3.md:93:- **Implicatio
515:   - `Verified ... .rtf:34` says "dynamic trailing stops (e.g., VWAP-based)".
516:   - `ROUND_2_RESEARCH_PROMPTS...md:93` says "dynamic trailing stops (VWAP-based)".
597:**1. Mechanical description.** At each clock half-hour or hour, two boundaries ("noise
723:page-02.txt:30:       namic trailing stops to mitigate downside risks while allowing f
759:page-26.txt:11:dynamic trailing stops, yields substantial returns over the period from
771:30:       namic trailing stops to mitigate downside risks while allowing for unlimited
774:11:dynamic trailing stops, yields substantial returns over the period from 2007 to ear
802:What it found beyond Q1 to Q12 and the passages above: the abstract (p. 2 lines 29-31)
906:page-02.txt:30:       namic trailing stops to mitigate downside risks while allowing f
949:(a) Hard stop: **unchanged**. None of the passages added here states a fixed maximum l
$ /usr/bin/grep -n -E 'as soon$|^ *as there is an indication' page-02.txt
26:       utes of the trading session, our model initiates trend-following positions as soon
27:       as there is an indication of abnormal demand/supply imbalance in the intraday
```

### Effect on the answer (from the quotes only)

(a) Hard stop: **unchanged**. The abstract's "dynamic trailing stops ... unlimited upside potential" was already considered. None of F1-F3 adds a fixed maximum loss known at entry. (b) Timing: **unchanged**. The Figure 2 caption's 16:00 close is already in Q3 and the answer. The abstract's "as soon as there is an indication" is about entry and names no check frequency. F1 changes only the provenance label of the RTF quotes, not their text.

This addendum makes no trading recommendation, proposes no retest and decides nothing. Those belong to the trader.

## Addendum 3 (worker 7, corrections to Addendum 2)

This addendum corrects three items in Addendum 2. Lines 1-1062 above are unchanged. The standing sentence that was line 1063 is moved to the end of the file. Commands were run from the repo root under /bin/bash. Timestamps are from `date -u` in each step.

### G1. Line 1011 "is an omission (0 hits in this file before this addendum)": OVERSTATED, RESTATED

The 0-hit count is true for the two phrases searched ("as soon as there is an indication", "indication of abnormal"). It is not true that the sentence was absent. Line 905, inside the worker 3 grep listing, already carried raw p2:25, the first raw line of the sentence. Line 907 carried p4:32, the body-text version of the same contrast ("last 30-minutes", hyphenated). The brief's pattern `last 30 min` does not match line 907 because of the hyphen. The second command below shows it with the hyphenated pattern.

Restated: the full p. 2 entry-timing sentence was not quoted or discussed before Addendum 2. Its first raw line (p2:25) appeared once before, inside grep output at line 905.

```
Sun 15 Nov 2026 17:01:31 UTC
$ head -n 954 docs/reports/2026-11-15-noise-area-paper-read-worker1.md | /usr/bin/grep -n 'academic literature\|last 30 min'
905:page-02.txt:25:       500. Unlike the academic literature that typically limits trading to the last 30 min-
Sun 15 Nov 2026 17:01:38 UTC
$ sed -n '907p' docs/reports/2026-11-15-noise-area-paper-read-worker1.md
page-04.txt:32:studies, our model does not limit the trading to the last 30-minutes of the trading session;
$ head -n 954 docs/reports/2026-11-15-noise-area-paper-read-worker1.md | /usr/bin/grep -n 'last 30-minutes'
907:page-04.txt:32:studies, our model does not limit the trading to the last 30-minutes of the trading session;
$ head -n 954 docs/reports/2026-11-15-noise-area-paper-read-worker1.md | /usr/bin/grep -c 'as soon as there is an indication\|indication of abnormal'
0
```

### G2. Line 961 "Line 453 names docs/ files": REASON REPLACED WITH EVIDENCE

Being under docs/ is not a reason. The evidence is below. All four paths named on line 453 are tracked (`git ls-files` lists all four). None is ignored (`git check-ignore` prints nothing, exit=1). `git status --short` shows only ` M DECISIONS.md`, so the spec, the 4uu report and the scope proposal match HEAD `d9fc5f0`. That is what line 453 says, so its labels stand. The fifth path on line 453 (the untracked voice-notes report) is outside this item and was not re-checked here.

```
Sun 15 Nov 2026 17:01:31 UTC
$ git rev-parse --short HEAD
d9fc5f0
$ git ls-files -- docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/reports/2026-07-16-4uu-noise-area-strategy.md docs/specs/2026-07-15-block2-backtesting-scope-proposal.md DECISIONS.md
DECISIONS.md
docs/reports/2026-07-16-4uu-noise-area-strategy.md
docs/specs/2026-07-15-block2-backtesting-scope-proposal.md
docs/specs/2026-07-16-b2-noise-area-ruleset.md
$ git check-ignore -v -- docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/reports/2026-07-16-4uu-noise-area-strategy.md docs/specs/2026-07-15-block2-backtesting-scope-proposal.md DECISIONS.md; echo exit=$?
exit=1
$ git status --short -- docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/reports/2026-07-16-4uu-noise-area-strategy.md docs/specs/2026-07-15-block2-backtesting-scope-proposal.md DECISIONS.md
 M DECISIONS.md
```

### G3. Line 1017 "lines 770-771": CITATION CONFIRMED, EVIDENCE ADDED

The `namic trailing stops` grep in Addendum 2 shows only line 771 (raw p2:30). The citation also names line 770. The output below shows line 770 carries raw p2:29 and line 771 carries raw p2:30. The citation "raw p2:29-30 at lines 770-771" is correct. Addendum 2 lacked the evidence for line 770.

```
Sun 15 Nov 2026 17:01:31 UTC
$ sed -n '770,771p' docs/reports/2026-11-15-noise-area-paper-read-worker1.md
29:       which have been discussed in our previous papers, we introduce the use of dy-
30:       namic trailing stops to mitigate downside risks while allowing for unlimited upside
```

### Effect on the answer (from the pasted text only)

None of G1-G3 changes the hard-stop answer or the timing answer. The pasted lines contain no fixed maximum loss known at entry and no stop-check interval. G1 changes how the sentence's earlier appearance is described, G2 changes the evidence behind a label, and G3 adds evidence for a citation.

This addendum makes no trading recommendation and decides nothing. Those belong to the trader.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
