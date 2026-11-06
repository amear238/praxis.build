# 2026-11-05 — MFFU fee check (unit `2026-11-05-mffu-fee-check`)

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Summary
- MFFU's own help-centre article "Futures Instrument List" (dated August 24, 2026) can be read. HTTP 200, 181974 bytes, fetched twice on its own, and the extracted text is identical both times.
- MFFU gives one figure per instrument, in a column headed "Total Cost Round Trip": **NQ $4.68, MNQ $1.90**. MFFU does not split it into commission, exchange, clearing, NFA or platform fees.
- **$5.76 is NOT supported for NQ by MFFU's page.** On that page $5.76 belongs to **YM (E-mini Dow)**, not NQ. That is a likely source of the voice agent's figure, but this is INFERRED: the voice agent cited Tradeify and FundedNext.
- Against the current $2.96: MFFU's $4.68 is +$1.72 per round turn. Over 1,190 trades that is −$2,046.80, which takes the R0 net from $197,327.60 to $195,280.80 (−1.037%). Arithmetic only, no backtest.
- Neither branch of Amear's typed instruction fires: $5.76 is not confirmed, and the page *can* be read. Whether $4.68 is adopted is NEEDS AMEAR 1. Nothing was edited.
- None of the evaluation or sim pages read says whether per-trade costs come out of the sim balance. The Live Funded page says costs are deducted from the live balance.

## Task
This is the brief from the master, the DECISION_LOG rows at 2026-11-05T23:51:21Z (R-VN4-6) and 23:50:09Z (typed cost-model instruction). Steps 1–4: read MFFU's fee page, compute round-turn costs for NQ and MNQ, compare them with $2.96 at 1,190 trades, and handle the unreadable-page case.

## Rubric criteria addressed
S1, S2 and S8 are quoted verbatim in the brief. S6 is the cross-block check (`specs/SPEC_RUBRIC.md:112`), covered below.

## Workers dispatched
| id | mode | outcome |
|---|---|---|
| (manager, first fetch) | — | 21 MFFU URLs fetched into `scratchpad/research-D/` |
| a879277f0cd54f008 | ADVERSARIAL | VERDICT: NOT REFUTED. Independent re-fetch into `scratchpad/research-ADV/`. Found the YM $5.76 row. |

## Process log
1. Read the current model and its provenance first. `config/backtest-cost-model.json` gives `"commission_round_turn_usd": 2.96`. DECISIONS.md:185 says `Q5 cost model: $2.96 round-turn commission`. DECISIONS.md:276 (D-2026-10-30-A) says `Commission ($2.96 RT) … unchanged`.
2. Fetched the sitemaps. The help sitemap has 90 URLs and none of them is a dedicated fee or commission article. Then fetched 12 candidate articles.
3. Found the fee table in 9735811 and extracted it. The adversarial worker re-fetched it on its own and searched for contradicting text.
4. The re-fetch was byte-different from mine at the same size (`differ: char 2982, line 1`), but the extracted text was IDENTICAL (diff below).

## What was read (fetched 2026-11-05T23:54:37Z; adversary 23:56:04Z)
```
f1 200 410349 https://myfundedfutures.com/
f2 200 14313 https://myfundedfutures.com/sitemap.xml
f3 404 0 https://myfundedfutures.com/sitemap_index.xml
f4 200 106684 https://help.myfundedfutures.com/en/
f6 404 7483 https://myfundedfutures.com/faq
f8 200 14927 https://help.myfundedfutures.com/sitemap.xml
200 181974 9735811-futures-instrument-list
200 117288 8528339-understanding-evaluation-parameters-at-myfundedfutures
200 178456 12109396-comprehensive-faq-live-accounts-at-myfunded-futures
200 111367 10101257-understanding-live-funded-account-at-myfunded-futures
200 119638 10082979-ninjatrader-login-instructions
200 111610 8528335-overview-of-supported-platforms-at-mffu
200 152110 17573707-comprehensive-look-into-redesigned-pro-plan
200 153481 15072271-flex-plan-50-000-a-comprehensive-guide
200 131178 16158363-rapid-eod-50k-a-comprehensive-look
200 138176 17005296-builder-plan-100k-comprehensive-guide
200 101697 12398151-does-myfundedfutures-charge-activation-fees
200 114563 16498635-moving-from-evaluation-to-sim-funded-account
```
Excerpts from `https://help.myfundedfutures.com/en/articles/9735811-futures-instrument-list`, pasted from the parser output:
```
Futures Instrument List Includes Contract Specifications, Commissions, and Trading Fees August 24, 2026
CME Instrument Name | Code | Trading Hours | Tick Size | Tick Value | Total Cost Round Trip |
49-E-mini NASDAQ 100 50: | NQ 51- | Sunday - Friday 17:00 - 16:00 CT 52-Daily Break: 16:00 - 17:00 CT 53- | 0.25 54- | $5 55- | $4.68 56- |
65-E-mini S&P 500 66: | ES ... 69- | 0.25 70- | $12.50 71- | $4.68 72- |
119-Micro E-mini Nasdaq-100 120: | MNQ ... 123- | 0.25 124- | $0.50 125- | $1.90 126- |
255-E-mini Dow Jones 256: | YM ... 259- | 1.00 260- | $5.00 261- | $5.76 262- |
261: | $5.76          <- the only $5.76 on the page
```
Two oddities are recorded as they appear on the page and not corrected: NQ's tick value is printed as `$5` and ES's tick value as `$12.50`.

Adversary excerpts:
```
NQ row:  E-mini NASDAQ 100 | NQ | ... | 0.25 | $5 | $4.68
MNQ row: Micro E-mini Nasdaq-100 | MNQ | ... | 0.25 | $0.50 | $1.90
page ends: $2.92 / To get funded to trade the instruments, start here.Did this answer your question?
help-centre search "5.76": s_576.html 200 72057 -> only "Futures Instrument ListYM ... 1.00 $5.00 $5.76"
```
Live Funded (10101257):
```
These costs include: CME Professional Data Subscription Round-Trip Commissions and Fees Platform License or Subscription All costs will be deducted directly from your Live Funded Account balance .
```
Live FAQ (12109396). This is a monthly data fee, not a per-trade cost:
```
Your exchange fee will be automatically deducted on the first trading day of the month.
```

## Fee table (MFFU's figures only)
| Item | NQ | MNQ | Source |
|---|---|---|---|
| Total Cost Round Trip | **$4.68** | **$1.90** | 9735811, as pasted above |
| Commission per side | not published | not published | the page has no split. The adversary found no "per side", "round turn", "rithmic", "tradovate", "ninjatrader", "varies" or "subject to change" in the raw HTML |
| Exchange / clearing / NFA | not published separately | not published separately | the same |
| Per-trade platform/data fee | none published | none published | data and platform fees appear only as Live-account costs (10101257, 12109396) |
| Deducted from eval/sim balance? | **not stated on any page read** | **not stated** | no match for commission, deduct, per side, NFA or clearing on the eval, sim, plan or home pages (adversary) |

The fee table is SPECIFIED by MFFU's published page. Whether a sim account actually charges $4.68 per round trip has not been OBSERVED. That would need a fill statement, which would need a login, and logging in is out of scope.

## Arithmetic
The R0 net has commission included at $2.96 on every trade. `docs/reports/2026-11-01-csv-analyses.md:348` reads `qty={1: 1190} … commission/trade={'2.96': 1190}` and `:344` reads `R0 baseline NAB: trades=1190 net=197327.60`.
Script: `scratchpad/fee_math.py`, run with `python3 -I`. Output:
```
current model RT commission=2.96  baseline R0 net=197327.60 at n=1190
MFFU NQ $4.68 (page): delta/RT=+1.72  delta total=-2046.80  new net=195280.80  pct of net=-1.037%  total RT cost incl 20.00 slip=24.68
voice $5.76 (reported): delta/RT=+2.80  delta total=-3332.00  new net=193995.60  pct of net=-1.689%  total RT cost incl 20.00 slip=25.76
MNQ $1.90 per side-equivalent=0.95; NQ $4.68 per side=2.34
4.68 vs 5.76 gap=1.08 x 1190 = 1285.20
```
The per-side figures are Claude's halving. MFFU does not publish per-side figures.

## Confirmed / range / not supported
- **$5.76 for NQ: NOT SUPPORTED by MFFU's page.** MFFU's NQ figure is $4.68. $5.76 is MFFU's YM figure.
- **MFFU NQ $4.68: READ on MFFU's page (SPECIFIED)**, and identical on two separate fetches. It is a single figure, not a range.
- If Amear wants a range, the two figures on the table are $4.68 (MFFU, read) and $5.76 (voice agent, REPORTED). They are $1.08 apart per round trip, or $1,285.20 over 1,190 trades. Whether to use a range at all is Amear's call (NEEDS AMEAR 2).

## Leads not confirmed
- The voice agent's $5.76, from Tradeify and a FundedNext example: REPORTED and not fetched in this unit.
- What MFFU's $4.68 includes (commission only, or all-in with exchange, clearing and NFA): not stated on the page. The subtitle "Commissions, and Trading Fees" suggests all-in. That is INFERRED.
- Whether costs differ by platform (Rithmic vs Tradovate) or by plan: the page does not say. Not checked: blog pages, articles 11802648/11802669, anything behind login.

## Adversarial findings
The adversary returned NOT REFUTED and added one material finding: $5.76 is on the YM row (I checked this against my own download, `261: | $5.76` above). It also flagged a scope limit: "no MFFU page read" is supported, but "no MFFU page anywhere" is not. I made no correction to the claim. The report keeps the narrower wording.

## Verification evidence (second fetch vs first)
```
EXTRACTED TEXT IDENTICAL
3e6820e087332ad8ade8   (instr.txt, sha256 prefix)
3e6820e087332ad8ade8   (instr_adv.txt, sha256 prefix)
...research-D/a_9735811.html ...research-ADV/article.html differ: char 2982, line 1
```
**Negative test** (does the instruction's gate block?): the "amend" branch of the 23:50:09Z instruction needs $5.76 to be confirmed. Its value is not on MFFU's NQ row, so the gate does not open and no DECISIONS entry was drafted. The "keep $2.96" branch needs the page to be unreadable, and the page returned 200. So that branch does not fire either.

## S6 cross-block check
Nothing was changed, so no deviation was approved. If $4.68 were adopted, the blocks it would touch are the ones in `config/backtest-cost-model.json` `applies_to`: the P&L distributions (NT8 WFA and Python MC), the SHM distributions and thresholds (D-2026-07-04-B), and R-multiple conversion (Q6). It would also touch `total_cost_per_round_turn_usd` (22.96 → 24.68) and `_ticks` (4.592 → 4.936, which is Claude's arithmetic 24.68/5, not run). None of these was tested here.

## Files staged
None. This report is untracked and not `git add`ed, per the brief. No repo file other than this report was written.

## NEEDS AMEAR
1. MFFU's page reads NQ $4.68 round trip, not $5.76, and your typed instruction covers only "confirmed" and "unreadable". Does R-VN4-6 ("Apply the best figure you can find") mean $4.68 goes into a new DECISIONS entry?
2. Single figure ($4.68) or a range ($4.68–$5.76)?
3. MFFU publishes no per-side split and does not say whether sim accounts deduct costs. Should this be checked against an account fill statement, which would need a login?

## Result: PASS
Steps 1–4 are answered: the page was read, the arithmetic was run, the $5.76 status is stated, and step 4 does not apply because the page was readable. The only adoption question goes to Amear.

## Correction 1 (2026-11-06, after audit FAIL 1 on S1)
The audit (DECISION_LOG 2026-11-06T00:01:58Z) failed S1 on lines 84 and 87 (BLOCKING), and on 27 and 54–61 (MINOR). It failed S2 on line 62 (MINOR). Nothing above this heading was edited. Every paste below is this correction's own live re-fetch, done by the manager, not the adversary. Fetched 2026-11-06T00:02:56Z into `scratchpad/corr-D/` (untrusted, never executed). Text was stripped with `scratchpad/corr-tools/strip.py`, run as `python3 -I` from `corr-tools/`. All greps are `/usr/bin/grep` (the shell `grep` is a wrapper).

**C1. Fetch log** (`curl -sSL --max-time 20 -A "Mozilla/5.0" -o corr-D/<name>.html -w '%{http_code}' <url>`; columns: name, HTTP, bytes, URL), then the stripped line counts:
```
instr 200 181974 https://help.myfundedfutures.com/en/articles/9735811-futures-instrument-list
eval 200 117288 https://help.myfundedfutures.com/en/articles/8528339-understanding-evaluation-parameters-at-myfundedfutures
sim 200 114563 https://help.myfundedfutures.com/en/articles/16498635-moving-from-evaluation-to-sim-funded-account
pro 200 152110 https://help.myfundedfutures.com/en/articles/17573707-comprehensive-look-into-redesigned-pro-plan
flex 200 153481 https://help.myfundedfutures.com/en/articles/15072271-flex-plan-50-000-a-comprehensive-guide
rapid 200 131178 https://help.myfundedfutures.com/en/articles/16158363-rapid-eod-50k-a-comprehensive-look
builder 200 138176 https://help.myfundedfutures.com/en/articles/17005296-builder-plan-100k-comprehensive-guide
home 200 410349 https://myfundedfutures.com/
helphome 200 106684 https://help.myfundedfutures.com/en/
hsitemap 200 14927 https://help.myfundedfutures.com/sitemap.xml
2026-11-06T00:02:56Z
instr.txt 335 lines
eval.txt 54 lines
sim.txt 51 lines
pro.txt 209 lines
flex.txt 175 lines
rapid.txt 116 lines
builder.txt 132 lines
home.txt 227 lines
helphome.txt 51 lines
```
Liveness controls. These show each text file holds the page, so an exit 1 below is a real absence and not an empty file (`/usr/bin/grep -c -i -E 'myfundedfutures|mffu' <f>.txt`; for sim, `-c -i 'funded'`; for instr, `-c -F '4.68'`):
```
instr 2
eval 6
sim 0
pro 4
flex 2
rapid 1
builder 1
home 16
helphome 5
instr 4.68: 3
sim control funded: 23
```

**C2. Supersedes line 84** (the 9735811 negative search, which was the adversary's and had nothing pasted):
```
$ /usr/bin/grep -n -i -E per side|round turn|rithmic|tradovate|ninjatrader|varies|subject to change instr.txt
(exit 1)
$ /usr/bin/grep -c -i -E per side|round turn|rithmic|tradovate|ninjatrader|varies|subject to change instr.html
0
(exit 1)
```
(The runner echoes the pattern without its quotes. It was passed as one quoted argument.) None of the terms is in the text (335 lines) or in the raw HTML (181974 bytes). Line 84's claim holds.

**C3. Supersedes line 87** (the eval, sim, plan and home negative search):
```
=== :87 eval ===
$ /usr/bin/grep -n -i -E commission|deduct|per side|nfa|clearing eval.txt
(exit 1)
=== :87 sim ===
$ /usr/bin/grep -n -i -E commission|deduct|per side|nfa|clearing sim.txt
(exit 1)
=== :87 pro ===
$ /usr/bin/grep -n -i -E commission|deduct|per side|nfa|clearing pro.txt
(exit 1)
=== :87 flex ===
$ /usr/bin/grep -n -i -E commission|deduct|per side|nfa|clearing flex.txt
(exit 1)
=== :87 rapid ===
$ /usr/bin/grep -n -i -E commission|deduct|per side|nfa|clearing rapid.txt
89:Clearing the $2,100 buffer for your first payout, then reaching $500 in net profit since your last payout to unlock each payout after that, under the 90/10 split.
=== :87 builder ===
$ /usr/bin/grep -n -i -E commission|deduct|per side|nfa|clearing builder.txt
(exit 1)
=== :87 home ===
$ /usr/bin/grep -n -i -E commission|deduct|per side|nfa|clearing home.txt
215:Disclaimer: MyFundedFutures provides the information on this website for general informational and educational purposes only. It does not constitute investment, trading, tax, legal, or financial advice, and does not constitute an offer to buy or a solicitation to sell any financial product or de
=== :87 helphome ===
$ /usr/bin/grep -n -i -E commission|deduct|per side|nfa|clearing helphome.txt
(exit 1)
```
(The `home` line above is cut at 300 characters by the runner's `cut -c1-300`.) This is the matching span:
```
$ /usr/bin/grep -n -i -o -E ".{0,80}(commission|deduct|per side|nfa|clearing).{0,80}" home.txt
215:Futures is not a broker-dealer, investment adviser, introducing broker, futures commission merchant (FCM), or money manager. You should consult your own advisors before e
```
**Line 87's wording "no match" is wrong, and is corrected here.** There are two matches. Neither is about per-trade costs. rapid:89 is "Clearing" a payout buffer. home:215 is a "futures commission merchant (FCM)" disclaimer. The other six pages have no match. The finding behind summary line 11 and NEEDS AMEAR 3 holds, now on this evidence: none of these pages says whether per-trade costs come out of the eval or sim balance.

**C4. Supersedes line 27** (the sitemap):
```
$ /usr/bin/grep -o "<loc>[^<]*</loc>" hsitemap.html | wc -l
      90
$ /usr/bin/grep -o "<loc>[^<]*</loc>" hsitemap.html | /usr/bin/grep -i -E "fee|commission|cost"
<loc>https://help.myfundedfutures.com/en/articles/12398151-does-myfundedfutures-charge-activation-fees</loc>
(exit 0)
```
The count of 90 holds. **Line 27's "none of them is a dedicated fee or commission article" is too broad, and is corrected here.** One URL names fees: 12398151, on activation fees, which was fetched (line 49). It does not contain per-trade cost terms:
```
actfee 200 101697
      36 actfee.txt
$ /usr/bin/grep -n -i -E "commission|round trip|per side|nfa|clearing|deduct" actfee.txt
(exit 1)
```
Corrected wording: none of the 90 is a per-trade fee or commission article.

**C5. Supersedes lines 52–61** (the edited excerpt). This is a raw, unedited excerpt of the NQ, MNQ and YM rows. It is this correction's parser output (`strip.py`) on the instr fetch above (181974 bytes, the same size as line 39):
```
$ sed -n "56,63p;117,124p;236,243p" instr.txt
E-mini NASDAQ 100
NQ
Sunday - Friday 17:00 - 16:00 CT
Daily Break: 16:00 - 17:00 CT
0.25
$5
$4.68
E-mini Russell 2000
Micro E-mini Nasdaq-100
MNQ
Sunday - Friday 17:00 - 16:00 CT
Daily Break: 16:00 - 17:00 CT
0.25
$0.50
$1.90
Micro E-mini Russell 2000
E-mini Dow Jones
YM
Sunday - Friday 17:00 - 16:00 CT
Daily Break: 16:00 - 17:00 CT
1.00
$5.00
$5.76
Micro E-mini dow Jones
```
The line ranges are 8 lines each, so each range's last line is the name of the next instrument. Lines 54–61 were a hand-edited excerpt (with `...` cuts and an added note), so they are not pasted output. This block replaces them as the evidence for NQ $4.68, MNQ $1.90 and YM $5.76.

**C6. Supersedes line 62** (S2): NQ's `$5` and ES's `$12.50` are the correct tick values (0.25 × $20 and 0.25 × $50). They are not oddities, and "oddities" is withdrawn.

Scope of this correction: no sign-up, no login, nothing staged. No repo file other than this report was touched. The figures and NEEDS AMEAR 1–3 are unchanged.
