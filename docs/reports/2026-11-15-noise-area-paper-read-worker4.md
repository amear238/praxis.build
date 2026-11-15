# Noise-Area paper read: adversarial check of the worker-3 addendum (worker 4)

## Task

Unit `2026-11-15-noise-area-paper-read`, worker 4. Mode: ADVERSARIAL, read-only. Artifact under test: the section `## Addendum (worker 3, corrections)` in `docs/reports/2026-11-15-noise-area-paper-read-worker1.md`, lines 550-955. Lines 1-549 are out of scope except where the addendum makes a claim about them. Criteria (specs/SPEC_RUBRIC.md): S1, S2, S8, S13. Nothing was staged, committed or modified except this report. Paper text comes from my own extraction (`pdftotext -layout -f N -l N`) in `/tmp/praxis-npr/w4-text/`. Scripts are in `/tmp/praxis-npr/scripts-w4/` and run only as `python3 -I -B`. Every grep uses `/usr/bin/grep`. This report was assembled by a bash builder script: each `$` line below was executed when the report was built, and the output under it is pasted unedited apart from name masking. Masking: personal names other than the paper's three authors are replaced by `[name withheld]` / `[names withheld]`. No line here contains an email address.

## Artifact hash
```
$ date -u
Sun 15 Nov 2026 16:52:56 UTC
$ shasum -a 256 '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md' /tmp/praxis-npr/dl/w1/paper.pdf
03e36d4fd1fb16498a904162cc3a6baa95778f1541ae4bbd4b102cd3225e7551  /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md
41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad  /tmp/praxis-npr/dl/w1/paper.pdf
$ pdfinfo /tmp/praxis-npr/dl/w1/paper.pdf | /usr/bin/grep Pages; pdftotext -v 2>&1 | head -1
Pages:           43
pdftotext version 26.04.0
$ cd /tmp/praxis-npr/w4-text && ls page-*.txt | wc -l; for f in page-*.txt; do cmp -s $f ../w3-text/$f || echo DIFF $f; done; echo 'cmp vs w3-text done (no DIFF line = all 43 identical)'
      43
cmp vs w3-text done (no DIFF line = all 43 identical)
```

## Quote verification (paper)

Scripted check: every `page-NN.txt:L:text` line and every bare `L:text` line under a `--- pNN:...` header in addendum lines 550-955 is compared byte for byte with my extracted line. Where the addendum's command used `cut -c1-200` or `-c1-190`, the comparison uses the same cut. Expected FAILs: L630 is the walk-forward spec line under `-F -x` (project file, not paper; the script mis-maps it). L908-909 are the two lines where the addendum masked literature-review names (disclosed in its preamble). In the output below my SRC side is masked the same way.
```
$ date -u
Sun 15 Nov 2026 16:52:57 UTC
$ python3 -I -B /tmp/praxis-npr/scripts-w4/check_quotes.py '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md' /tmp/praxis-npr/w4-text
addendum L567  p9:12     PASS
addendum L568  p9:22     PASS
addendum L569  p11:7     PASS
addendum L570  p11:17    PASS
addendum L571  p12:21    PASS
addendum L572  p12:26    PASS
addendum L573  p13:23    PASS
addendum L574  p13:25    PASS
addendum L575  p14:8     PASS
addendum L576  p17:8     PASS
addendum L577  p34:10    PASS
addendum L579  p10:23    PASS
addendum L580  p10:31    PASS
addendum L581  p13:30    PASS
addendum L582  p27:6     PASS
addendum L583  p38:5     PASS
addendum L607  p13:34    PASS
addendum L608  p13:35    PASS
addendum L630  p13:63    FAIL
   SHOWN: '- **BandO'
   SRC  : None
addendum L686  p30:1     PASS
addendum L687  p30:2     PASS
addendum L688  p30:3     PASS
addendum L689  p30:4     PASS
addendum L690  p30:5     PASS
addendum L691  p30:6     PASS
addendum L692  p30:7     PASS
addendum L694  p34:1     PASS
addendum L695  p34:2     PASS
addendum L696  p34:3     PASS
addendum L697  p34:4     PASS
addendum L698  p34:5     PASS
addendum L700  p24:15    PASS
addendum L702  p25:5     PASS
addendum L703  p25:6     PASS
addendum L704  p25:7     PASS
addendum L705  p25:8     PASS
addendum L706  p25:20    PASS
addendum L707  p25:21    PASS
addendum L708  p25:22    PASS
addendum L710  p40:3     PASS
addendum L711  p40:4     PASS
addendum L712  p40:5     PASS
addendum L713  p40:10    PASS
addendum L715  p16:32    PASS
addendum L716  p14:10    PASS
addendum L717  p14:11    PASS
addendum L723  p2:30     PASS
addendum L724  p3:23     PASS
addendum L725  p4:31     PASS
addendum L726  p9:15     PASS
addendum L727  p9:20     PASS
addendum L728  p9:23     PASS
addendum L729  p11:8     PASS
addendum L730  p11:20    PASS
addendum L731  p11:25    PASS
addendum L732  p12:1     PASS
addendum L733  p12:2     PASS
addendum L734  p12:12    PASS
addendum L735  p12:15    PASS
addendum L736  p12:20    PASS
addendum L737  p13:1     PASS
addendum L738  p13:5     PASS
addendum L739  p13:6     PASS
addendum L740  p13:12    PASS
addendum L741  p13:14    PASS
addendum L742  p13:17    PASS
addendum L743  p13:19    PASS
addendum L744  p13:26    PASS
addendum L745  p13:30    PASS
addendum L746  p14:1     PASS
addendum L747  p14:7     PASS
addendum L748  p14:9     PASS
addendum L749  p14:20    PASS
addendum L750  p14:25    PASS
addendum L751  p15:1     PASS
addendum L752  p15:7     PASS
addendum L753  p16:1     PASS
addendum L754  p16:19    PASS
addendum L755  p16:24    PASS
addendum L756  p16:25    PASS
addendum L757  p17:11    PASS
addendum L758  p22:17    PASS
addendum L759  p26:11    PASS
addendum L760  p30:12    PASS
addendum L761  p30:38    PASS
addendum L762  p34:9     PASS
addendum L763  p40:1     PASS
addendum L764  p40:2     PASS
addendum L765  p40:3     PASS
addendum L766  p40:13    PASS
addendum L767  p43:4     PASS
addendum L768  p43:9     PASS
addendum L770  p2:29     PASS
addendum L771  p2:30     PASS
addendum L772  p2:31     PASS
addendum L773  p26:10    PASS
addendum L774  p26:11    PASS
addendum L776  p30:9     PASS
addendum L777  p30:24    PASS
addendum L778  p30:33    PASS
addendum L779  p31:1     PASS
addendum L780  p31:29    PASS
addendum L781  p31:39    PASS
addendum L782  p32:1     PASS
addendum L783  p32:27    PASS
addendum L784  p33:13    PASS
addendum L785  p33:18    PASS
addendum L786  p34:1     PASS
addendum L787  p34:19    PASS
addendum L788  p35:1     PASS
addendum L789  p35:53    PASS
addendum L790  p36:22    PASS
addendum L791  p37:25    PASS
addendum L792  p37:36    PASS
addendum L793  p37:43    PASS
addendum L794  p38:1     PASS
addendum L795  p39:1     PASS
addendum L796  p39:12    PASS
addendum L797  p40:1     PASS
addendum L798  p40:23    PASS
addendum L799  p41:1     PASS
addendum L800  p42:26    PASS
addendum L810  p18:33    PASS
addendum L811  p19:23    PASS
addendum L812  p19:26    PASS
addendum L813  p21:33    PASS
addendum L814  p21:41    PASS
addendum L815  p21:43    PASS
addendum L816  p23:23    PASS
addendum L817  p28:16    PASS
addendum L818  p30:33    PASS
addendum L819  p30:34    PASS
addendum L820  p30:35    PASS
addendum L821  p30:36    PASS
addendum L822  p30:47    PASS
addendum L823  p31:41    PASS
addendum L824  p36:2     PASS
addendum L825  p37:48    PASS
addendum L826  p37:49    PASS
addendum L827  p40:1     PASS
addendum L828  p40:2     PASS
addendum L829  p40:4     PASS
addendum L830  p40:5     PASS
addendum L831  p40:16    PASS
addendum L832  p40:17    PASS
addendum L833  p40:18    PASS
addendum L834  p40:19    PASS
addendum L835  p43:4     PASS
addendum L836  p43:12    PASS
addendum L837  p43:13    PASS
addendum L838  p43:14    PASS
addendum L840  p9:20     PASS
addendum L841  p9:31     PASS
addendum L843  p10:11    PASS
addendum L844  p10:12    PASS
addendum L845  p37:48    PASS
addendum L846  p37:49    PASS
addendum L855  p1:1      PASS
addendum L856  p1:5      PASS
addendum L857  p1:9      PASS
addendum L858  p1:10     PASS
addendum L860  p2:5      PASS
addendum L861  p2:6      PASS
addendum L862  p2:7      PASS
addendum L863  p2:8      PASS
addendum L864  p2:9      PASS
addendum L865  p2:10     PASS
addendum L871  p2:7      PASS
addendum L873  p30:9     PASS
addendum L874  p30:10    PASS
addendum L875  p30:11    PASS
addendum L876  p30:43    PASS
addendum L877  p30:44    PASS
addendum L878  p30:45    PASS
addendum L905  p2:25     PASS
addendum L906  p2:30     PASS
addendum L907  p4:32     PASS
addendum L908  p5:16     FAIL
   SHOWN: 'page-05.txt:16:for under-reaction, based on investors’ limited attention to news, is proposed by [name withheld]'
   SRC  : 'page-05.txt:16:for under-reaction, based on investors’ limited attention to news, is proposed by [name withheld]'
addendum L909  p5:17     FAIL
   SHOWN: 'page-05.txt:17:[names withheld] [15]. Such behavior may stem from limited cognitive abilities or be'
   SRC  : 'page-05.txt:17:[names withheld] [15]. Such behavior may stem from limited cognitive abilities or be'
addendum L910  p9:32     PASS
addendum L911  p10:1     PASS
addendum L912  p18:32    PASS
addendum L913  p18:33    PASS
addendum L914  p19:23    PASS
addendum L915  p19:27    PASS
addendum L916  p20:11    PASS
addendum L917  p20:16    PASS
addendum L918  p24:31    PASS
addendum L919  p25:5     PASS
addendum L920  p25:20    PASS
addendum L921  p25:29    PASS
addendum L922  p34:10    PASS
addendum L923  p36:36    PASS
addendum L924  p37:32    PASS
addendum L925  p39:6     PASS
addendum L926  p40:3     PASS
addendum L927  p40:29    PASS
addendum L940  p8:10     PASS
addendum L941  p8:11     PASS
addendum L942  p8:12     PASS
addendum L943  p8:13     PASS
addendum L944  p8:14     PASS
TOTAL 202 PASS 199
```

Prose quotes (whitespace-normalised page text; the p. 2 abstract also checked after rejoining the 'dy-/namic' split):
```
$ date -u
Sun 15 Nov 2026 16:52:57 UTC
$ python3 -I -B /tmp/praxis-npr/scripts-w4/check_inline.py /tmp/praxis-npr/w4-text
PASS p2 "dynamic trailing stops to mitigate downside risks while allowing for unlimited upside potential  [checked after rejoining 'dy-/namic']"
PASS p30 'specific trading rules that we utilize to enhance strategy efficiency'
PASS p34 'a simplified model'
PASS p25 'a few milliseconds before the start of minute HH:MM'
PASS p25 'relative to the Open price of minute HH:MM'
PASS p25 'the start of minute HH:MM'
PASS p40 'VWAP + Current Band'
PASS p40 'May 2007 to December 2024'
PASS p14 'the 17-year period'
PASS p13 'For more details see our previous publication [5].'
PASS p1 'University of St.Gallen and Swiss Finance Institute'
PASS p2 'Concretum Research'
PASS p30 'concretumgroup.'
PASS p26 'dynamic trailing stops'
PASS p25 'large orders'
PASS p25 'order methodologies'
PASS p36 'their order'
PASS p25 'send market orders on SPY'
PASS p34 'send orders to Interactive Brokers'
PASS p8 'Typically, the average intraday movement from the Open tends to increase over time, peaking at 16:00.'
PASS p9 'Stop losses can also be triggered only on semi-hourly intervals'
PASS p13 'as soon as the price crosses'
PASS p9 'market Close'
PASS p10 'end of day t − 1'
PASS p37 'until market close'
PASS p30 'address every inquiry'
PASS p13 'we have con- ducted a comprehensive historical backtest'
PASS p10 'the most con- cerning aspects'
PASS p14 '7,668'
PASS p40 '7,964'
PASS p40 '6,728'
PASS p16 '7,668'
PASS p2 'Andrea Barbon4'
TOTAL 33 PASS 33
```

D1 split list, scripted over each Q heading's page:line ranges, plus the 'con-' grep and the reading-line check:
```
$ date -u
Sun 15 Nov 2026 16:52:57 UTC
$ python3 -I -B /tmp/praxis-npr/scripts-w4/splits.py /tmp/praxis-npr/w4-text '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md'
Q1 p9:12 'he Noise Area, our strat-' | next starts: 'egy'
Q2 p9:22 'lign with the latest evi-' | next starts: 'dence'
Q5 p11:7 'sts that can provoke dra-' | next starts: 'matic'
Q5 p11:17 'ctive strategy. This sce-' | next starts: ''
Q6 p12:21 'ing that the strategy re-' | next starts: 'mains'
Q7 p12:26 ' the demand-supply imbal-' | next starts: ''
Q7 p13:23 'January 20, 2022. Includ-' | next starts: 'ing'
Q7 p13:25 ', showcasing VWAP’s effi-' | next starts: 'cacy'
Q8 p14:8 ') and the worst daily re-' | next starts: 'turn'
Q10 p17:8 ' we have conducted in or-' | next starts: 'der'
Q11 p34:10 ' IBML, a specialized Mat-' | next starts: 'lab'
split count over heading ranges: 11
Figure 2 caption at p9:5
artifact lines 244-428: in-block lines ending letter-hyphen: 11
$ cd /tmp/praxis-npr/w4-text && /usr/bin/grep -n -E 'con-[[:space:]]*$' page-*.txt
page-10.txt:23:These operational parameters ensure that our backtesting reflects realistic trading con-
page-10.txt:31:overall slight underperformance compared to the passive SPY exposure, the most con-
page-13.txt:30:To demonstrate the economic advantages of these trailing stop refinements, we have con-
page-27.txt:6:             100 best-selling authors in ”Business and Finance” for 7 con-
page-38.txt:5:significant relationship between VIX and short trade profitability. This is visually con-
$ cd /tmp/praxis-npr/w4-text && for x in 10:24 10:32 13:31 38:6; do p=${x%%:*}; n=${x##*:}; printf 'p%s:%s ' $p $n; sed -n "${n}p" page-$p.txt | cut -c1-50; done
p10:24 ditions and provides a credible estimation of the 
p10:32 cerning aspects are the worst daily return of -10.
p13:31 ducted a comprehensive historical backtest, the re
p38:6 firmed by the flat black line representing the fit
$ awk 'NR>=244&&NR<=428{ if(/^```/){inb=!inb; next} if(!inb && $0!="" && $0 !~ /^\*\*Q/) print NR": "substr($0,1,120)}' '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md'
284: (The equation that follows is `Shares_t = AUM_{t−1} / Open_{t,9:30}`. It is rendered over several lines in the extract
305: Figure 4 caption, p. 12, lines 1-3:
354: Figure 5 caption, p. 13, lines 1 and 5-7:
402: p. 10, lines 31-33: "...the most con-/cerning aspects are the worst daily return of -10.33% and the negative skewness of
$ sed -n 242p '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md'
These are copied character for character from `page-NN.txt`, with the original line breaks kept. Words split by a line-end hyphen in the PDF are rejoined only in the reading line under each quote: "strat-/egy" to "strategy", "evi-/dence" to "evidence", "dra-/matic" to "dramatic", "sce-/nario" to "scenario", "imbal-/ance" to "imbalance", "re-/mains" to "remains", "effi-/cacy" to "efficacy", "con-/ducted" to "conducted". The typos "curent" and "postions" are the paper's own (sic).
```

D3 footnote and 'anchor':
```
$ date -u
Sun 15 Nov 2026 16:52:57 UTC
$ sed -n '32,40p' /tmp/praxis-npr/w4-text/page-13.txt | cat -v -n
     1	6 and Table 2. The improvements are substantial: the average annual return increases
     2	to 9.7%, while annual volatility decreases to 7.7%. The Sharpe Ratio doubles, improving
     3	   2
     4	       VWAP is computed only using market hours data. For more details see our previous publication [5].
     5	
     6	
     7	
     8	
     9	                                                    13
$ cd /tmp/praxis-npr/w4-text && /usr/bin/grep -n -i anchor page-*.txt; echo exit=$?
exit=1
$ python3 -I -B /tmp/praxis-npr/scripts-w4/joined.py /tmp/praxis-npr/w4-text 'anchor' 'an- ?chor'; echo joined-anchor-end
joined-anchor-end
```

## Project-line verification

These checks cover the RTF `:34` (D2), the compass `:41` (D2), spec `:99` (D3), the r3-recheck manager report `:9` at HEAD `d9fc5f0` (D4), walk-forward values `:63` (D4), and the D4 claim that both candidates were missing from lines 1-549. Finding: the addendum labels the RTF `git status` check "(empty = clean at HEAD)". The output below shows the RTF is not in `d9fc5f0` and not in the index, and `.gitignore:7` ignores it. An empty status line here therefore means the file is ignored. It does not mean the file is clean at HEAD. The quoted content of line 34 itself matches the working-tree file.
```
$ date -u
Sun 15 Nov 2026 16:52:57 UTC
$ cd /Volumes/Sensidine/Praxis.build && sed -n 34p 'Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf' | /usr/bin/grep -o -E 'At each clock half-hour or hour[^.]*\.|When price breaches[^.]*\.|The setup is binary[^.]*\.'
At each clock half-hour or hour, two boundaries ("noise band") are drawn around the day's open.
When price breaches the upper (lower) boundary at the top/bottom of an hour, a long (short) position is opened.
The setup is binary \'97 either price has closed beyond the band at the half-hourly check or it has not.
$ cd /Volumes/Sensidine/Praxis.build && git status --short -- 'Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf'; echo '(status output ends)'
(status output ends)
$ cd /Volumes/Sensidine/Praxis.build && git show 'd9fc5f0:Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf' | sed -n 34p
fatal: path 'Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf' exists on disk, but not in 'd9fc5f0'
$ cd /Volumes/Sensidine/Praxis.build && git ls-files -- 'Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf' | wc -l; git ls-tree -r --name-only d9fc5f0 -- Redemtion/ | wc -l
       0
       0
$ cd /Volumes/Sensidine/Praxis.build && git check-ignore -v -- 'Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf'; echo check-ignore-exit=$?
.gitignore:7:Redemtion/	Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf
check-ignore-exit=0
$ cd /Volumes/Sensidine/Praxis.build && sed -n 41p 'Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-0085-4b1e-a813-4f4221d90a63_text_markdown.md'
- Decision is made **at fixed wall-clock times** (09:30, 10:00, 10:30, 11:00, 11:30 ET) on bar close, not intra-bar.
$ cd /Volumes/Sensidine/Praxis.build && sed -n 99p docs/specs/2026-07-16-b2-noise-area-ruleset.md | shasum -a 256; git show d9fc5f0:docs/specs/2026-07-16-b2-noise-area-ruleset.md | sed -n 99p | shasum -a 256; git status --short -- docs/specs/2026-07-16-b2-noise-area-ruleset.md; echo '(status output ends)'
64338b8e0ef66a87c457d6b25d44d6165fb1c65b192899d6a27f72ffd6670cf6  -
64338b8e0ef66a87c457d6b25d44d6165fb1c65b192899d6a27f72ffd6670cf6  -
(status output ends)
$ cd /Volumes/Sensidine/Praxis.build && sed -n 99p docs/specs/2026-07-16-b2-noise-area-ruleset.md | cut -c1-200
Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = max/min(Open_{9:30}, PrevClose)`; VWAP anchored at 09:30, market-hours only; **flat at 16:00** (or the tr
$ cd /Volumes/Sensidine/Praxis.build && git show d9fc5f0:docs/reports/2026-11-14-r3-recheck-manager.md | sed -n 9p; git status --short -- docs/reports/2026-11-14-r3-recheck-manager.md; echo '(status output ends)'
| Noise-Area baseline (BandOrVWAP) | band/VWAP level, checked at HH:00/HH:30 bar closes, market exit | NO | −$542.40 | 10 | −$705.10 | 5 |
(status output ends)
$ cd /Volumes/Sensidine/Praxis.build && W=docs/specs/2026-11-06-walk-forward-values.md; sed -n 63p $W | cut -c1-120; git show d9fc5f0:$W | sed -n 63p | cmp - <(sed -n 63p $W) && echo 'line 63 identical, working tree vs d9fc5f0'; git diff --stat d9fc5f0 -- $W
- **BandOrVWAP** — OBSERVED (code): the base file's logic: at HH:00/HH:30 checkpoints, a long exits when `Close <= max(U
line 63 identical, working tree vs d9fc5f0
 docs/specs/2026-11-06-walk-forward-values.md | 42 ++++++++++++++--------------
 1 file changed, 21 insertions(+), 21 deletions(-)
$ cd /Volumes/Sensidine/Praxis.build && sed -n '1,549p' '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md' | /usr/bin/grep -c -E 'r3-recheck-manager|walk-forward-values'
0
```

## Figure re-runs

I re-ran: the citation file count 76 and the mtime split (2 after 16:25Z, 11 earlier today); the 653-line count (today 690, because the addendum itself added 37 matching lines: 690 - 37 = 653); the head -40 block (only difference is name masking; the r3-recheck manager is absent); the 23-hit order/limit run and its at-sign count 0 / exit 1; the D5 and D6 greps (no differences); and the trade counts 7,964 / 7,668. My count of 76 ran at the time shown, before this report existed.

Note on the two diffs below: each shown pair differs only in a personal name. The report masks both sides, so the pair prints identically here.
```
$ date -u
Sun 15 Nov 2026 16:52:57 UTC
$ cd /Volumes/Sensidine/Praxis.build && /usr/bin/grep -rIl -i -E 'Zarattini|Beat the Market|4824172|Barbon' --exclude-dir=.git . | wc -l
      76
$ cd /Volumes/Sensidine/Praxis.build && hi=$(date -j -u -f '%Y-%m-%dT%H:%M:%S' 2026-11-15T16:25:00 +%s); lo=$(date -j -u -f '%Y-%m-%dT%H:%M:%S' 2026-11-15T00:00:00 +%s); /usr/bin/grep -rIl -i -E 'Zarattini|Beat the Market|4824172|Barbon' --exclude-dir=.git . | while IFS= read -r f; do m=$(stat -f %m "$f"); [ $m -ge $lo ] && echo "$(date -u -r $m +%Y-%m-%dT%H:%M:%SZ) $( [ $m -ge $hi ] && echo AFTER-16:25Z || echo before-16:25Z) $f"; done | sort
2026-11-15T14:42:50Z before-16:25Z ./docs/reports/2026-11-15-voice-notes-open-questions.md
2026-11-15T14:58:31Z before-16:25Z ./docs/reports/2026-11-15-rulings-filing-worker2.md
2026-11-15T15:12:16Z before-16:25Z ./docs/reports/2026-11-15-rulings-filing-worker4.md
2026-11-15T15:28:55Z before-16:25Z ./docs/reports/2026-11-15-rulings-filing-worker6.md
2026-11-15T15:33:12Z before-16:25Z ./docs/reports/2026-11-15-rulings-filing-worker7.md
2026-11-15T15:42:34Z before-16:25Z ./docs/reports/2026-11-15-rulings-filing-worker8.md
2026-11-15T15:43:31Z before-16:25Z ./MANIFEST.md
2026-11-15T15:55:31Z before-16:25Z ./DECISIONS.md
2026-11-15T16:04:55Z before-16:25Z ./STATUS.md
2026-11-15T16:17:20Z before-16:25Z ./HANDOFF.md
2026-11-15T16:23:53Z before-16:25Z ./DECISION_LOG.md
2026-11-15T16:38:49Z AFTER-16:25Z ./docs/reports/2026-11-15-noise-area-paper-read-worker2.md
2026-11-15T16:43:57Z AFTER-16:25Z ./docs/reports/2026-11-15-noise-area-paper-read-worker1.md
$ cd /Volumes/Sensidine/Praxis.build && /usr/bin/grep -rn -i -E 'checked at HH|HH:00/HH:30.*(stop|exit)|band/VWAP|band-or-VWAP|BandOrVWAP' docs/ Redemtion/ *.md --exclude-dir=.git | wc -l; echo 'hits inside the addendum (lines 550-955):'; sed -n '550,955p' '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md' | /usr/bin/grep -c -i -E 'checked at HH|HH:00/HH:30.*(stop|exit)|band/VWAP|band-or-VWAP|BandOrVWAP'
     690
hits inside the addendum (lines 550-955):
37
$ cd /Volumes/Sensidine/Praxis.build && /usr/bin/grep -rn -i -E 'checked at HH|HH:00/HH:30.*(stop|exit)|band/VWAP|band-or-VWAP|BandOrVWAP' docs/ Redemtion/ *.md --exclude-dir=.git | head -40 | cut -c1-260 > /tmp/praxis-npr/scripts-w4/my-head40.txt; s=$(/usr/bin/grep -n "^\$ /usr/bin/grep -rn -i -E 'checked at HH" '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md' | cut -d: -f1); e=$(/usr/bin/grep -n '^\$ (same command without head)' '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md' | cut -d: -f1); echo "pasted block = lines $((s+1))-$((e-1))"; sed -n "$((s+1)),$((e-1))p" '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md' | diff - /tmp/praxis-npr/scripts-w4/my-head40.txt | cut -c1-150; echo 'r3-recheck-manager lines in head -40:'; /usr/bin/grep -c r3-recheck-manager /tmp/praxis-npr/scripts-w4/my-head40.txt
pasted block = lines 636-675
7c7
< docs/specs/2026-11-06-walk-forward-values.md:17:- **Ruling 4 of 2026-11-06** (DECISIONS.md D-2026-11-06-B, from DECISION_LOG `2026-11-06T20:08:28Z`,
---
> docs/specs/2026-11-06-walk-forward-values.md:17:- **Ruling 4 of 2026-11-06** (DECISIONS.md D-2026-11-06-B, from DECISION_LOG `2026-11-06T20:08:28Z`,
r3-recheck-manager lines in head -40:
0
$ cd /tmp/praxis-npr/w4-text && /usr/bin/grep -n -i -E 'order|limit|fixed|percent|% of|per trade' page-*.txt | wc -l; /usr/bin/grep -n -i -E 'order|limit|fixed|percent|% of|per trade' page-*.txt | diff <(sed -n '905,927p' '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md') - ; /usr/bin/grep -n -i -E 'order|limit|fixed|percent|% of|per trade' page-*.txt | /usr/bin/grep -c $'\x40'; echo at-sign-count-exit=$?
      23
4,5c4,5
< page-05.txt:16:for under-reaction, based on investors’ limited attention to news, is proposed by [name withheld]
< page-05.txt:17:[names withheld] [15]. Such behavior may stem from limited cognitive abilities or be
---
> page-05.txt:16:for under-reaction, based on investors’ limited attention to news, is proposed by [name withheld]
> page-05.txt:17:[names withheld] [15]. Such behavior may stem from limited cognitive abilities or be
0
at-sign-count-exit=1
$ cd /tmp/praxis-npr/w4-text && /usr/bin/grep -n -i -E 'stop|exit|unwound|loss limit|max(imum)? loss|drawdown limit|risk limit|liquidat|time.?stop|holding period|semi-hourly|intraday check|tick|high frequency|minute-by-minute|each minute|every minute' page-*.txt | cut -c1-200 | diff <(sed -n '723,768p' '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md') - ; echo D5-grep-diff-exit=$?
D5-grep-diff-exit=0
$ cd /tmp/praxis-npr/w4-text && /usr/bin/grep -n -i -E 'close|closing|end of (the )?day|market close|4:00|16:00|VWAP|boundar|noise area|band' page-1[89].txt page-[234]?.txt | cut -c1-190 | diff <(sed -n '810,838p' '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md') - ; echo D6-grep-diff-exit=$?
D6-grep-diff-exit=0
$ cd /tmp/praxis-npr/w4-text && /usr/bin/grep -n -E '7,964|7,668|5,494|6,728' page-*.txt | cut -c1-110
page-14.txt:10: result in a significant increase in the total number of trades, rising from 5,494 to 7,668
page-16.txt:29:Intra Mom.   Opp.Band            100%   5,494       1.3       53%       0.10
page-16.txt:32:Intra Mom.   Curr.Band + VWAP    100%   7,668       1.8       37%       0.09
page-16.txt:35:Intra Mom.   Curr.Band + VWAP    Dyn.   7,668       1.8       37%       0.09
page-40.txt:4:of trades decreases significantly from 7,964 (for the VWAP + Current Band version) to
page-40.txt:5:6,728 (for the VWAP-only version). This reduction in trade frequency may enhance cost
$ sed -n '8,10p' /tmp/praxis-npr/w4-text/page-40.txt
volatility increases by 1.2%. This results in a Sharpe ratio drop from 1.35 to 1.17, indi-
cating a clear deterioration in risk-adjusted returns. The table summarizes the strategy’s
performance from May 2007 to December 2024.
```

## Omission hunt

I searched all 43 pages, joined into one line per page with line-end splits rejoined, for exit, stop, loss-limit, check-timing, order-type, flatten and drawdown wording. Pages 9-16 were also searched line by line, with the Q heading ranges and the quoted caption blocks excluded.

- **D6 count is wrong.** D6 says that across line breaks there are "two more occurrences" of "end of day" / "market close" (p10:11-12, p37:48-49), and that "Neither describes an exit rule". The joined search finds a third: the Figure 2 caption, p. 9 lines 6-7, "all positions are closed at the market / Close (16:00)". That one *is* an exit rule. Q3 already quotes it, so no paper text is lost. The count and the D6 correction are still incomplete.
- **Not quoted anywhere in the file (entry timing, not exit):** abstract p. 2 lines 25-27, "our model initiates trend-following positions as soon as there is an indication of abnormal demand/supply imbalance". The body restricts entries to semi-hourly checks (p9:15). This passage matters to the addendum's Effect (b), which cites p. 13's "as soon as the price crosses" as evidence that check timing is not restated for the band-or-VWAP stop. The abstract shows this paper uses "as soon as" for entries even though entries are checked on a fixed schedule. So "as soon as" is not evidence of continuous checking. Effect (b) does not claim that it is; it says only "not restated", which is true. I record this as an observation, not a defect.
- No other unquoted passage on exits, loss limits, stop-check timing, stop orders or a maximum loss per trade was found. The remaining hits outside pages 9-16 are table captions or headers (p11, p14, p15, p16, p43), the p17 one-line recap, and FAQ Q22 (p40, already Q12). The rest are unrelated: p03/p04 literature, p20/p37 "leverage", p21/p32 "triggered", and p22, where "complexity" matches "exit".
```
$ date -u
Sun 15 Nov 2026 16:53:01 UTC
$ python3 -I -B /tmp/praxis-npr/scripts-w4/joined.py /tmp/praxis-npr/w4-text 'end of (the )?day' 'market close' | cut -c1-200
p09 [market close] ...d on our base-model. Please note that all positions are closed at the market Close (16:00). As discussed earlier, if the market breaches the boundaries ...
p09 [market close] ...vements rather than transient spikes. Positions are unwound either at market Close or if there is a crossover to the opposite boundary of the Noise Area...
p09 [market close] ...e triggered by fleeting market movements. All positions are closed at market Close, adhering to the strategy’s protocol to limit exposure to overnight m...
p10 [end of (the )?day] ...−1 represents the equity (or Asset Under Management) available at the end of day t − 1. To assess the historical performance of our strategy, we simul...
p37 [market close] ...tend to pause during lunchtime, they resume strongly from 14:00 until market close. This suggests that although the intraday trend strategy is effective...
$ sed -n '5,7p' /tmp/praxis-npr/w4-text/page-09.txt
Figure 2: The time-varying boundary areas on SPY for 31 January 2022 (a) and 29 April 2022 (b) and
the resulting trades based on our base-model. Please note that all positions are closed at the market
Close (16:00).
$ python3 -I -B /tmp/praxis-npr/scripts-w4/joined.py /tmp/praxis-npr/w4-text 'stop' 'exit' 'loss(es)? (limit|cap)' 'max(imum)? (daily )?loss' 'risk (management|limit|control)' 'trigger' 'as soon as' 'immediately' 'intra-?bar' 'continuous' 'monitor' 'check' 'semi-hourly|half-hour|30-minute|every 30' 'stop[- ]?(loss )?order|limit order|market order|bracket' 'close (the|a|its|all) position|positions? (is|are) closed|unwound|flatten|liquidat' 'drawdown' 'leverage' | /usr/bin/grep -v -E '^p(09|1[0-6]) ' | cut -c1-200
p02 [stop] ...ssed in our previous papers, we introduce the use of dynamic trailing stops to mitigate downside risks while allowing for unlimited upside poten...
p02 [as soon as] ...of the trading session, our model initiates trend-following positions as soon as there is an indication of abnormal demand/supply imbalance in the int...
p03 [semi-hourly|half-hour|30-minute|every 30] ...demonstrates the potential of overnight returns to forecast the final half-hour returns of the S&P 500, highlighting significant intraday time-series.
p04 [semi-hourly|half-hour|30-minute|every 30] ...rementioned studies, our model does not limit the trading to the last 30-minutes of the trading session; empirically, we have seen that intraday tren.
p17 [stop] ...onducted using the intraday momentum strategy that employs a trailing stop based on the current band and VWAP, and adjusts investment size accor...
p20 [leverage] ...-of-the-Week Effect is a focal point for statistical arbitrageurs who leverage calendar seasonality to identify market inefficiencies. While this ap...
p21 [trigger] ...ility on Wednesday may be linked to significant intraday trends often triggered on Federal Open Market Committee (FOMC) days. 4.4 Volatility Multip...
p22 [exit] ...ff between the total return and risk-adjusted returns. Given the complexity of the decision between higher returns and better risk-adjusted perf...
p25 [stop[- ]?(loss )?order|limit order|market order|bracket] ...ntum strategy. funded with $100,000, we instruct an algorithm to send market orders on SPY for $100,000 just a few milliseconds before 
p26 [stop] ...imbalance in intraday price action and incorporating dynamic trailing stops, yields substantial returns over the period from 2007 to early 2024....
p32 [trigger] ...out further downward pressure, the intraday momentum model may not be triggered, making it ineffective as a 32 ...
p37 [leverage] ...stors can extract alpha from intraday time frames, where turnover and leverage often exceed their trading limits. Academic research has shown that m...
p40 [stop] ...Q22. How do the results change if we use only VWAP as a trailing stop? Switching to a VWAP-only trailing stop results in less restrictive e...
p40 [stop] ...e use only VWAP as a trailing stop? Switching to a VWAP-only trailing stop results in less restrictive exit conditions, leading to a slight incr...
p40 [stop] ...performance from May 2007 to December 2024. Total Sharpe Hit Strategy Stop Leverage IRR Vol MDD Return Ratio Ratio Intra Mom. Opp.Band 1x 169 5....
p40 [exit] ...p? Switching to a VWAP-only trailing stop results in less restrictive exit conditions, leading to a slight increase in the average holding perio...
p40 [leverage] ...rmance from May 2007 to December 2024. Total Sharpe Hit Strategy Stop Leverage IRR Vol MDD Return Ratio Ratio Intra Mom. Opp.Band 1x 169 5.8 10.7 0....
p43 [stop] ...es Table A1: Summary statistics of intraday momentum strategy with a) stop loss at opposite band, b) current band with VWAP, c) as in (b) with t...
p43 [stop] ...istically significant at 5% level or below. Total Sharpe Hit Strategy Stop Size IRR Vol MDD Alpha Beta Skewness Worst Day Best Day Return Ratio ...
$ cd /tmp/praxis-npr/w4-text && /usr/bin/grep -n -i -E 'stop|exit|unwound|closed|trigger|as soon as|semi-hourly|interval|loss|check|HH:M' page-09.txt page-1[0-6].txt | awk -F: '{p=$1; n=$2+0; q=0; if(p=="page-09.txt" && ((n>=5&&n<=7)||(n>=12&&n<=17)||(n>=20&&n<=24)||(n>=27&&n<=32))) q=1; if(p=="page-10.txt"&&((n>=1&&n<=3)||(n>=31&&n<=33))) q=1; if(p=="page-11.txt"&&((n>=6&&n<=9)||(n>=12&&n<=17))) q=1; if(p=="page-12.txt"&&((n>=1&&n<=3)||(n>=7&&n<=8)||(n>=11&&n<=22)||(n>=25&&n<=26))) q=1; if(p=="page-13.txt"&&(n==1||(n>=5&&n<=7)||(n>=11&&n<=19)||(n>=23&&n<=27)||n==35)) q=1; if(p=="page-14.txt"&&n>=7&&n<=17) q=1; if(p=="page-15.txt"&&((n>=17&&n<=18)||(n>=34&&n<=36))) q=1; if(p=="page-16.txt"&&n>=24&&n<=36) q=1; if(!q) print}' | cut -c1-160
page-11.txt:20:Table 1: Summary statistics of intraday momentum strategy with stop loss at opposite band and SPY
page-11.txt:25:   Strategy         Stop        Size            IRR     Vol                     MDD   Alpha   Beta
page-13.txt:30:To demonstrate the economic advantages of these trailing stop refinements, we have con-
page-14.txt:1: Figure 6: Comparison of equity curves of intraday momentum strategy with a) stop loss at opposite
page-14.txt:20: Table 2: Summary statistics of intraday momentum strategy with a) stop loss at opposite band, b)
page-14.txt:25:Strategy          Stop                  Size                IRR     Vol                     MDD   Alpha   Beta
page-15.txt:1:  Table 3: Summary statistics of intraday momentum strategy with a) stop loss at opposite band, b)
page-15.txt:7:Strategy          Stop                  Size                 IRR    Vol                     MDD   Alpha   Beta
page-16.txt:1:Figure 7: Comparison of equity curves of intraday momentum strategy with a) stop loss at opposite
page-16.txt:19:Table 4: Summary statistics at trade-level of intraday momentum strategy with a) stop loss at opposite
$ sed -n '25,27p' /tmp/praxis-npr/w4-text/page-02.txt; /usr/bin/grep -c -i -E 'as soon as there|initiates trend-following' '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md'
       500. Unlike the academic literature that typically limits trading to the last 30 min-
       utes of the trading session, our model initiates trend-following positions as soon
       as there is an indication of abnormal demand/supply imbalance in the intraday
0
```

## S2, S8, privacy

- Privacy: the addendum has 0 lines with an at-sign. The only capitalised two-word personal names in it are two of the three authors. The third author appears as "Andrew Aziz2,3" / "A. Aziz", which the two-word pattern does not catch. Withheld markers are present where other names occurred.
- S8: the only decision-shaped wording is the closing disclaimer and the D4 statement "I do not choose one". The other hits are paper text ("suggesting", "suggests", "Should we") or a quoted project ruling. I found no trading recommendation.
- S2 overstatements found: (1) the RTF label "clean at HEAD" (see Project-line verification); (2) the D6 "two more occurrences" count (see Omission hunt). Labelled inferences checked and found correctly hedged: D7(b) concretumgroup.com ownership (INFERRED), D4 file choice (UNVERIFIED), D7(c) cause of 60 (UNVERIFIED).
- Cosmetic: the D7(a) block header says "p01, non-blank lines", but it includes `10:`, whose line is a lone form feed (0x0c, the page break); the quote check shows the bytes match.
- S13: the standing sentence occurs exactly once and is the file's last line (output below).
```
$ date -u
Sun 15 Nov 2026 16:53:01 UTC
$ sed -n '550,955p' '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md' > /tmp/praxis-npr/scripts-w4/addendum.txt; A=/tmp/praxis-npr/scripts-w4/addendum.txt; echo at-sign-lines=$(/usr/bin/grep -c $'\x40' $A); echo email-shaped=$(/usr/bin/grep -c -E '[A-Za-z0-9._%+-]+[[:space:]]*(\x40|\[at\]|\(at\))[[:space:]]*[A-Za-z0-9.-]+\.[a-z]{2,}' $A); echo withheld-markers=$(/usr/bin/grep -c -E 'name[s]? withheld' $A)
at-sign-lines=0
email-shaped=0
withheld-markers=4
$ /usr/bin/grep -o -E '\b[A-Z][a-z]+ [A-Z][a-z]+\b' /tmp/praxis-npr/scripts-w4/addendum.txt | sort | uniq -c | sort -rn | tr '\n' ';'
  11 Noise Area;   5 Intra Mom;   5 Concretum Research;   3 Current Band;   2 West Hastings;   2 Swiss Finance;   2 Piazza Molino;   2 Peak Capital;   2 Interactive Brokers;   2 Concretum Bands;   2 Bear Bull;   1 Worst Day;   1 Weak Closure;   1 Upper Boundary;   1 Trend Days;   1 The Impact;   1 Strategy Analyzer;   1 Max Loss;   1 Max Gain;   1 Intraday Momentum;   1 In Figure;   1 If Block;   1 Hit Ratio;   1 Frequently Asked;   1 Claude Code;   1 Carlo Zarattini;   1 Best Day;   1 Asset Under;   1 Andrea Barbon;$ /usr/bin/grep -n -i -E 'recommend|should|suggest|advis|propose|go live|deploy|adopt|we must|must be|decid' /tmp/praxis-npr/scripts-w4/addendum.txt | cut -c1-160
97:docs/specs/2026-11-06-walk-forward-values.md:65:- **Flat1559** — RULED (Q5: "Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar, as in _Flat1559.c
247:page-39.txt:12:Q21. Should we open short trades only when the market is trading below
261:page-18.txt:33:      daily range, and the Close is above the 85th percentile, suggesting a strong bullish
277:page-37.txt:49:close. This suggests that although the intraday trend strategy is effective for most of the
297:49:close. This suggests that although the intraday trend strategy is effective for most of the
359:page-05.txt:16:for under-reaction, based on investors’ limited attention to news, is proposed by [name withheld]
364:page-18.txt:33:      daily range, and the Close is above the 85th percentile, suggesting a strong bullish
404:This addendum makes no trading recommendation and decides nothing. Those belong to the trader.
$ /usr/bin/grep -c -F -x -f /tmp/praxis-npr/scripts-w4/s13.txt '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md'; /usr/bin/grep -c -F -- 'Fills are optimistic' '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md'; tail -n 1 '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md' | cmp - /tmp/praxis-npr/scripts-w4/s13.txt && echo 'last line == standing sentence (s13.txt)'; wc -l < '/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md'
1
1
last line == standing sentence (s13.txt)
     955
```

## Verification evidence

- Artifact and paper hashes match the brief, and my 43-page extraction is byte-identical to worker 3's: see "Artifact hash".
- Paper quotes: 202 line-quotes checked. 199 are exact. 2 differ only by disclosed name masking (L908, L909). 1 is not a paper line (L630, a mis-mapping in my script). 33 of 33 prose quotes pass, as does the D1 count of 11 splits: see "Quote verification (paper)".
- Project lines: RTF `:34`, compass `:41`, spec `:99` (identical at HEAD), manager `:9` at HEAD, walk-forward `:63` (identical at HEAD) and the 42-line diff stat are reproduced. The RTF is ignored by git and not in HEAD: see "Project-line verification".
- Figures: 76, 11 + 2 mtimes, 653 (as 690 - 37), 23 hits / at-sign count 0 / exit 1, 7,964 vs 7,668; the D5 and D6 greps match: see "Figure re-runs".
- Omissions and S2, S8, privacy, S13: see the last two sections.

## Result: FAIL

Defects:
1. **S2, D2 (artifact line 598).** `git status --short -- "<RTF>"   (empty = clean at HEAD)`. The RTF is not in HEAD `d9fc5f0` ("exists on disk, but not in 'd9fc5f0'"), not in the index (ls-files count 0), and is ignored by `.gitignore:7: Redemtion/`. The empty output is evidence that the file is ignored, not that it is clean at HEAD. The quoted line-34 text is correct for the working-tree file. Its provenance label is not.
2. **S2/S1, D6 (artifact line 806).** "Across line breaks there are two more occurrences ... Neither describes an exit rule." There are three. The Figure 2 caption at p. 9 lines 6-7 ("closed at the market / Close (16:00)") is missed, and it does describe an exit rule. The D6 correction of the earlier statement (2) is therefore itself incomplete. Q3 already quotes the caption, so the Answer is unaffected.

Observations, not counted as defects: the p. 2 abstract "as soon as there is an indication" entry-timing passage is quoted nowhere in the file (Omission hunt), and the "non-blank lines" header includes a form-feed line.

This report makes no trading recommendation, decides nothing, and proposes no retest.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
