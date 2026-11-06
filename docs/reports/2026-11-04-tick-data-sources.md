# Tick data for NQ, 2021-03-08 → 2026-07-17 — sources, cost, format, NT8 path (Brief A)

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Unit:** `2026-11-04-tick-data-sources` · **Date:** 2026-11-04 · **Author:** praxis-manager (workers W1–W4, adversaries W5–W6) · **Brief:** `docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md`, sha256 `4c115d0382c571487ce2c249c34aa533d8330ba9454c283c7bdeee3312059980`, Brief A only.
**Status:** research only. Nothing bought, no account created, no data file downloaded, nothing imported or run, no code changed. Not audited.
**Grades:** OBSERVED = read on a vendor, exchange or help-guide page this session (2026-11-04, via `curl`), excerpt pasted in §9 under the E-number cited. INFERRED = reasoning, basis stated. UNVERIFIED = not reached or not stated. REPORTED = taken from an earlier repo report, not re-read on the web here.

## 1. Summary

1. Of the 14 rows in §2 (13 without Kinetick EOD, which has no tick data), **2 have a published price, read this session, that reaches the whole window**: Kibot $580 or $1,100 one-time packages that list NQ from 2009-09-28 [E8, E9] (end date not shown; reaching 2026-07-17 is INFERRED from "daily updates" [E9]), and Massive (ex-Polygon) $199/month, with downloaded data deleted within 30 days after the plan ends [E30, E30b]. Portara's $695 also reaches it (REPORTED, declined by Amear 2026-11-03). IQFeed has a published price but reaches only 180 days back, about 2.3 months of the window [E20, E21]. Databento's rate is only a calculator default ($71.40/GB, INFERRED weak) [E6].
2. FirstRate's NQ page lists **bars only** (1-minute and up). No FirstRate NQ tick product was found (OBSERVED page; "not sold" is INFERRED) [E13, E14].
3. **Native NT8 routes** (Kinetick paid, IQFeed, NinjaTrader's own feed, Rithmic) all need a new NT8 connection. D-071, as Amear restated it, allows only the Simulated Data Feed [E40]. That is flagged in §3.3 and not acted on.
4. Tick depth for Kinetick, NinjaTrader's own data and Rithmic was **not found** on any page reachable by curl (UNVERIFIED). IQFeed's service list says "180 calendar days of tick history" without naming an asset class (OBSERVED [E20]); that it covers CME futures and rolls daily is INFERRED.
5. Q2: NT8's help guide documents one fill-resolution setting and one date range per backtest; mixing is **not documented** (UNVERIFIED). Separate runs per range is INFERRED.
6. Q4: **No quantitative source** compares tick vs 1-second vs 1-minute fills (UNVERIFIED). For stamp-anchored market orders, finer data is INFERRED not to change the fill price.
7. Barchart (bot challenge), CME DataMine pricing (login, and a 403 anti-scraping block), and TickData pricing could not be reached. Their prices are UNVERIFIED.
8. No source is recommended. §5 sorts sources by Amear's three stated criteria only; every purchase, licence and connection question is in §8.

## 2. Vendor table

Column key: **Cov** = NQ tick coverage of 2021-03-08 → 2026-07-17 · **P/C** = per-contract / continuous · **T/BA** = trades only or bid/ask · **TS** = timestamp precision and zone · **Fmt** = file format · **Price** = exact as published · **Lic** = licence terms on own use · **NT8 path** = native / TickPrep-ready / needs new code · **Adj** = vendor back-adjustment documented.

TickPrep's input is per-contract NT tick text, `yyyyMMdd HHmmss[ fffffff];price;volume`, with `--tz-in Eastern|UTC` (`tools/tickprep/TickPrep.cs:5,16,18`, read 2026-11-04) [E0].

| Source | Cov | P/C | T/BA | TS | Fmt | Price | Lic | NT8 path | Adj | Grade · E |
|---|---|---|---|---|---|---|---|---|---|---|
| **Databento** GLBX.MDP3 `trades` | Dataset from June 2010 (OBS); NQ dates not read (catalog is JS) | Both; continuous is unadjusted; continuous via API only (OBS) | `trades` = every trade plus aggressor side; quotes in other schemas (OBS) | ns, UNIX epoch (OBS) | DBN, CSV, JSON (OBS) | Usage-based $/GB, no subscription for history (OBS). "from $0.50 /GB" is a dataset floor (OBS). `trades` default in calculator code $71.40/GB (INFERRED weak). NQ cost for window UNVERIFIED | UNVERIFIED (licence guide not fetched) | New code: CSV → NT tick text per contract, then TickPrep `--tz-in UTC` (INFERRED) | Roll rules c/n/v documented; "We don't create a synthetic time series by back-adjusting" (OBS) | E1–E7 |
| **Kibot** | NQ from 2009-09-28 in Top-10 tick package (OBS); end date UNVERIFIED | Both sold (OBS) | Both: tick, tick + bid/ask (OBS) | 1 s, US Eastern default; ms variant "not officially supported" (OBS) | CSV `Date,Time,Price,Size`; NinjaTrader output option on the custom-order form only (package page: 0 mentions); NT tick layout `yyyyMMdd HHmmss;Price;Volume` (OBS) | One-time. Top-10 continuous: tick $580, tick + bid/ask $800. Top-10 with every contract month: tick $1,100, tick + bid/ask $1,700 (OBS). NQ-only price is server-side: UNVERIFIED. Nearest example: "ES + NQ … Tick + bid/ask, last 3 years $465.00" (OBS, not this window) | "internal use only", no resale/redistribution (OBS) | Per-contract NT tick files at 1 s fit TickPrep's format without conversion (INFERRED). Same-second trades share a stamp | Calendar roll, "no back-adjustment"; NQ rolls 5 trading days before expiry (OBS) | E8–E12, E36 |
| **FirstRate Data** | No NQ tick product found; NQ page lists "Intraday Bars" 2-Jan-2008 → 3-Nov-2026 (OBS). "Not sold" = INFERRED | Bars: both; 3 adjustment types (OBS) | n/a | n/a | CSV zipped (OBS) | NQ bar price not in static HTML (UNVERIFIED). The brief's "FirstRate $75–225" is in gitignored `Redemtion/` files, labelled "FirstRate Data NQ 1-min" (REPORTED, §6, §10 V3) | No resale/redistribution (OBS) | n/a for tick | Bars: unadjusted / absolute / ratio (OBS) | E13–E15 |
| **TickData.com / TickWrite** | Futures from 2003, dataset-wide (OBS); NQ not confirmed (product page body didn't render) | As-traded per contract + continuous via TickWrite (OBS) | Trades; top-of-book quotes from 2010-01-04 in separate files (OBS) | ms from 2011-07-01; exchange time zone, Central for CME (INFERRED) (OBS) | Comma-delimited text (OBS) | Not found on any page read (UNVERIFIED) | UNVERIFIED | Conversion + Central→Eastern/UTC step; TickPrep takes only Eastern or UTC (INFERRED) | Roll table exists; NQ row not read (OBS/UNVER) | E16–E19 |
| **Portara / CQG** | 2014 → present (REPORTED) | Per contract (REPORTED) | Trades only (REPORTED) | 7-digit fractional seconds; Eastern on request (REPORTED) | NinjaTrader format (REPORTED) | **$695 flat**; per-year $125, $500 minimum (REPORTED, `docs/reports/2026-11-02-vm-high-res-plan.md:45`). Declined by Amear 2026-11-03 | Not in repo | TickPrep plan written (REPORTED) | TickPrep does it | Repo E39 |
| **IQFeed / DTN** | "180 calendar days of tick history" (OBS; asset class not named, futures and rolling INFERRED); reaches about 2026-05-08 from today (INFERRED arithmetic) | UNVERIFIED | Bid/ask attached to each last tick (OBS, NT8 table) | "microsecond timestamps (if available …)" (OBS); zone UNVERIFIED | Feed/API, no files (INFERRED) | Subscription: startup "$50", core "$108.15/month", US futures "$24.87/month", CME E-mini fee "$78.58", "as of December 1st, 2025" (OBS). First month if all four apply: $261.60 (Claude's arithmetic, INFERRED) | Exchange fees "NON-REFUNDABLE once the data has been entitled" (OBS); cancellation and minimum term not found (UNVERIFIED). One-time backfill of the window: not possible, depth caps it at 180 days (INFERRED from E20) | Native NT8 connection — **needs a new connection (D-071, §3.3)** | Vendor silent; NT8 merges and back-adjusts locally (OBS) | E20–E22, E26 |
| **Kinetick** (paid) | Paid tier has "Historical tick, minute and daily data" (OBS); depth in days UNVERIFIED | UNVERIFIED | Bid/ask attached to last tick (OBS, NT8 table) | UNVERIFIED | NT connection | Base service "$81.11 per month" (/Subscribe) vs "$78.75/month" (/CME): pages conflict. CME E-mini "$78.75"; Globex Non-Pro Level I "$2.10 per month" (OBS) | Non-Pro needs an NT user account and a futures brokerage account (OBS) | Native — **new connection (D-071)** | Vendor silent | E23–E25 |
| **Kinetick EOD (free)** | End-of-day only (OBS) | — | — | — | — | Free | — | Native (already listed, not connected, Amear K1 ruling 2026-10-20) | — | E23 |
| **NinjaTrader own data** (NT / Continuum-CQG connection) | Historical tick "YES" in NT8 table (OBS); depth **not stated** anywhere read. The repo's "about 1 year of ticks" stays UNVERIFIED | Per contract download; NT merges locally (OBS) | Bid/ask tick "YES" (OBS) | "Native" real-time stamp; historical precision UNVERIFIED | NT repository | Plans $0, $99/month, $1,499 lifetime; real-time data needs a funded account (OBS); no depth difference stated | Export terms UNVERIFIED | Native — **new connection (D-071)** | "Merge back adjusted : NinjaTrader automatically merges and back adjusts" (OBS) | E26–E29 |
| **Rithmic** via NT8 (MFFU or Rithmic paper) | Historical tick "YES" in NT8 table (OBS); **days served UNVERIFIED** (no help-guide page; rithmic.com and NT Connection Guides didn't render) | UNVERIFIED | Bid/ask tick "YES" (OBS) | "Native" | NT repository | UNVERIFIED (prop-firm terms not read) | UNVERIFIED | Native — **new connection (D-071)** | NT8 local merge | E26 |
| **Barchart OnDemand** | UNVERIFIED (every page HTTP 202, empty bot-challenge body) | UNVERIFIED | UNVERIFIED | UNVERIFIED | REST API exists (official GitHub client, OBS) | UNVERIFIED | UNVERIFIED | New code, if ticks exist (INFERRED) | UNVERIFIED | E31 |
| **Massive (ex-Polygon.io) futures** | Futures trades "date back to April 3, 2017" (OBS); NQ by name not shown, INFERRED from CME coverage | Per contract (ticker e.g. "ESZ4"); continuous not seen (OBS / UNVER) | Trades; top-of-book quotes "available" on Developer/Advanced (OBS) | UTC, ns since epoch (OBS) | REST JSON (OBS); flat-file format didn't render (UNVER) | Monthly: Starter $29 (no trades), Developer $79 ("5 years"), Advanced $199 ("All history"), Business CME $999 (OBS). 20% off annual (OBS) | "solely for your own personal, non-business and non-commercial use"; Advanced needs non-professional status (OBS). Licence ends with the plan; delete within 30 days (OBS, E30b). Fit to MFFU use = Amear's | New code: REST paging + JSON → NT tick text, then TickPrep `--tz-in UTC` (INFERRED) | Not documented; per-contract so unadjusted (INFERRED) | E30 |
| **CME DataMine** (T&S, Top of Book, Depth) | T&S: CME electronic "6/26/1992 → Present" (OBS); Top of Book misses 3 in-window dates (OBS); NQ per-product filter not read | Per contract (OBS) | T&S trades only; Top of Book adds bid/ask (OBS) | T&S to the second, Central, before 2025-03-11; ns UTC after (OBS). The wiki also says v2 starts 2022-08-22 (OBS, **contradiction**) | Headerless CSV; ToB fixed-width ASCII, CSV from 2025-04-14 (OBS) | Behind CME login (UNVERIFIED) | UNVERIFIED (cmegroup.com 403) | New code: CSV → NT text, sort by sequence number, CT→ET (INFERRED) | None; raw exchange record (INFERRED) | E32–E34 |
| **Open / academic** (HF, Kaggle, GitHub, Zenodo, WRDS) | No NQ tick set found on HF, Kaggle, GitHub (OBS for those queries); Kaggle NQ sets are 1-minute bars. Zenodo 403, WRDS needs login (UNVERIFIED) | — | — | — | — | — | Kaggle 1-min NQ set "Apache 2.0" (OBS) | — | — | E35 |

## 3. Answers 1–4

### 3.1 Cheapest route to a partial tick set (e.g. the most recent 12 months)

"Most recent 12 months" of this backtest window is taken as 2025-07-17 → 2026-07-17 (INFERRED reading).

| Source | Sells partial? | What partial costs | Grade |
|---|---|---|---|
| Kibot | Yes: custom order takes a typed start date [E11] | Server-side price, not published for NQ (UNVERIFIED). Nearest example: ES + NQ tick + bid/ask, last 3 years, $465.00 [E10] | Partial OBS; price UNVERIFIED |
| Databento | Any start/end range, billed by bytes [E4, E5] | $/GB × size; NQ size not published (UNVERIFIED) | INFERRED |
| Portara | Per year, $125, $500 minimum, counted back from today | 2025-07 → 2026-07 needs 2 years back from today (INFERRED arithmetic on the REPORTED rate), so the $500 minimum applies (REPORTED rate, `vm-high-res-plan.md:45`) | REPORTED |
| IQFeed | 180 calendar days only [E20] (asset class not named; futures and rolling INFERRED) | Reaches about 2026-05-08. Covers only ~2.3 months of the window's last 12 (Claude's arithmetic). First month $261.60 if all four fees apply (INFERRED). Each day of delay removes a day; after about 2027-01-13 IQFeed reaches no part of the window (INFERRED arithmetic) | OBS / INFERRED |
| Massive | Developer $79/month, "5 years"; Advanced $199/month, all history [E30] | Developer from 2026-11-04 back 5 years reaches about 2021-11 (INFERRED; rolling or fixed is UNVERIFIED) | OBS / INFERRED |
| CME DataMine | Query, price and order by user [E34] | Price behind login (UNVERIFIED) | OBS / UNVERIFIED |
| TickData, Barchart, Kinetick, NT, Rithmic | Not found | UNVERIFIED | UNVERIFIED |

No source with a published price sells *only* a 12-month NQ tick slice at a published price. The lowest published figures that reach any part of the last 12 months are Massive Developer ($79/month; downloaded data must be deleted within 30 days after the plan ends, OBSERVED [E30b]) and IQFeed ($261.60 first month, 180 days only). Both are subscriptions, and both need new code (Massive) or a new NT8 connection (IQFeed).

### 3.2 Can NT8 run High fill resolution with ticks for part of the window and Standard for the rest?

**The NT8 help guide does not say (UNVERIFIED).** What it does say [E27, E28]:
- "Order fill resolution — Sets the order fill resolution to be used for the backtest." There is one value per run, with one "Start date" and one "End date" (OBSERVED).
- "NinjaTrader will only start the backtest after we have loaded historical data for both the strategy and the order fill resolution." (OBSERVED)
- What NT8 does when the High series has no ticks for part of the range is **not documented** (UNVERIFIED). Testing it would need a run, which is outside this unit.

INFERRED: as documented, it is per run. "High for part, Standard for the rest" means two runs on two date ranges, combined by hand. A walk-forward split that way would break any indicator warm-up across the joint; that is a design question, not answered here.

### 3.3 Free collection going forward: depth stored, and D-071

Facts [E26, E29]:
- Backfill depth on connect: **UNVERIFIED** for Rithmic sim/paper and for Kinetick. IQFeed: 180 days [E20].
- NT8 history requests are in "calendar days format" (OBSERVED [E29]). That NT8 stores what was requested, capped by what the provider serves, is INFERRED. The cap is UNVERIFIED.
- Forward recording: "Record live data as historical" (Tools → Options → **Market Data**) stores incoming real-time ticks only while "a Chart or Market Analyzer (must have an indicator column added) window open". NT warns it "is intended for connections which DO NOT provide historical data" (OBSERVED). Default off: INFERRED from the wording.

**D-071 flag (not acted on, not ruled on).** Amear restated D-071 on 2026-10-20 [E40]: *"the Simulated Data Feed is the one allowed connection. No orders, no other connection."* Opening an NT8 connection to Rithmic (sim, paper or MFFU), Kinetick paid, IQFeed or NinjaTrader's own feed would be a connection other than the Simulated Data Feed. That is a reading of the words, not a ruling. **Whether any such connection may be opened is Amear's call (§8).** The Simulated Data Feed is, by its name, generated data, so recording it would not produce real NQ ticks (INFERRED from the name only; not tested).

### 3.4 Is 1-second or volume-bar data a cheaper intermediate?

**No quantitative source was found** comparing fill error at tick vs 1-second vs 1-minute (UNVERIFIED; not a claim that none exists). The repo's 08-07 research (UNGRADED) already covers the 1-minute ambiguity figure and is not repeated here.

What was found:
- NT8's fill page says High takes "a secondary bar series" and gives "a 1 Tick Data Series" as the most granular (OBSERVED) [E27]. **Whether "Second" can be selected as the High series is not stated** (UNVERIFIED; a look at the VM dropdown would settle it).
- The NT8 provider table lists historical data types Tick, Minute, Daily and their Bid/Ask variants only (OBSERVED) [E26]. INFERRED: NT8 builds 1-second and volume bars from stored ticks, so an NT8 "1-second intermediate" still needs tick files, which removes the saving.
- 1-second NQ bars are sold by Databento (`ohlcv-1s`, OBSERVED; price UNVERIFIED) and Massive (`second_aggregates` "available" on Futures Developer, OBSERVED; other plans not excerpted) [E7, E30]. FirstRate's NQ page lists 1-minute as finest (OBSERVED) [E13].
- CME's wiki says T&S is second-stamped before 2025-03-11, but also that CSV v2 from 2022-08-22 carries nanosecond datetimes (OBSERVED, contradictory [E33]). Which applies to NQ files from 2022-08-22 to 2025-03-10 is UNVERIFIED.

INFERRED reasoning, labelled, not a finding: the project facts say entries are market orders on the 1-minute bar at HH:00/HH:30 and flat by 16:00. A market order sent on bar close fills on the next bar's first trade. Tick, 1-second and 1-minute data share that first trade, so finer data should not change the fill price before slippage. **This rests on two points.** (a) UNVERIFIED: that NT8 High fills market orders at the secondary series' next open. (b) OBSERVED for current code: Baseline, OppBand and Flat1559 place no resting stop or target. Every exit is a market order at the HH:00/HH:30 stamp under `Calculate.OnBarClose`, or the session flatten (`ninjascript/PraxisNoiseAreaBreakout*.cs`; §10 V2). UNVERIFIED for the judged version: R-1104-3 names "breakers on", the breakers are not built, and if they become resting orders, finer data would matter. Volume bars are not time-anchored, so they cannot line up with HH:00/HH:30 stamps (INFERRED).

## 4. D-071 — see §3.3 (flag only)

## 5. Shortlist sorted by the stated criteria (cost, coverage, import effort)

This is a sort, not a recommendation. Cost is the lowest **published** figure that reaches the whole window. Import effort: **native** = an NT8 connection backfills it (needs a new connection, D-071) · **TickPrep-ready** = per-contract NT tick text, TickPrep's documented input · **new code** = a converter must be written first (a code change, so Amear's call).

**Full window, 2021-03-08 → 2026-07-17, published price found.** One-time and subscription prices are sorted separately. Comparing them needs a use period, and choosing one is Amear's call.

*One-time (data kept):*

| Order | Source | Cost (exact) | Coverage | Import effort | Caveats |
|---|---|---|---|---|---|
| 1 | Kibot Top-10 continuous tick | $580 one-time; "files you download are yours to keep" (OBS, E9) | NQ from 2009-09-28 (OBS); continuous, unadjusted, 1-second stamps | **New code**: the continuous file must be split per contract at Kibot's roll dates before TickPrep (INFERRED) | NQ-only price is server-side (UNVERIFIED); it may be lower |
| 2 | Portara | $695 flat (REPORTED) | 2014 → present, per contract, fractional seconds (REPORTED) | TickPrep-ready; plan already written (REPORTED) | Declined by Amear 2026-11-03 |
| 3 | Kibot Top-10 with every contract month | $1,100 tick; $1,700 tick + bid/ask (OBS) | As row 1, plus per contract (OBS) | TickPrep-ready **if** the package can be delivered in Kibot's NinjaTrader format. That option is OBSERVED only on the custom-order form [E36], which is priced server-side; the package page doesn't mention it. Otherwise a CSV → NT converter is needed (new code) | 1-second stamps |

*Subscription (licence ends with the plan):*

| Order | Source | Cost (exact) | Coverage | Import effort | Caveats |
|---|---|---|---|---|---|
| 1 | Massive Advanced | $199/month while the data is used. Delete "within thirty (30) days" after the licence ends (OBS, E30b). Below Kibot's $580 continuous file only for ≤ 2 months of use (3 × $199 = $597), and below Kibot's $1,100 per-contract package only for ≤ 5 months (6 × $199 = $1,194) (Claude's arithmetic, INFERRED) | 2017 → present, per contract, ns UTC, trades (OBS) | New code (REST JSON paging + converter, then TickPrep `--tz-in UTC`) | Licence "personal, non-business" (Amear's question); non-professional status required |

**Full window, no published price (cannot be sorted on cost):** Databento (calculator default $71.40/GB × unknown size), TickData.com, CME DataMine, Barchart. Their coverage and effort are in §2.

**Partial only:** IQFeed (180 days, $261.60 first month INFERRED, native, D-071). Massive Developer ($79/month, ~5 years, new code). Kinetick, NinjaTrader and Rithmic: depth UNVERIFIED, native, D-071.

**Not a tick source for NQ:** FirstRate (bars only, INFERRED). Open datasets (none found).

## 6. Leads not confirmed

No forum page was used. These are leads from vendor-page structure or the repo, not confirmed:
- Repo claim (`vm-high-res-plan.md:27`): "NT's servers keep about 1 year of ticks". No NT page read states any retention figure.
- The brief's "FirstRate $75–225": in no git-tracked file (the brief itself is untracked as of 2026-11-04). It is in gitignored `Redemtion/` working-tree files (PRAXIS_PHASE_3_OUTPUT_SUMMARY.md:104,160; compass_artifact…md:152,582). One labels it "FirstRate Data NQ 1-min | One-time", so it was a 1-minute-bar price, not tick (REPORTED; §10 V3). Not confirmed on firstratedata.com.
- The same compass file (line 105) says "tick samples available" for FirstRate (REPORTED, unconfirmed; no FirstRate NQ tick page was found [E13, E14]).
- Databento's exact `trades` $/GB is probably served by `pricing_engine_get_unit_price` (named in its JS bundle). Not called: it is a server call behind the portal.
- Kibot's NQ-only price is served by `POST /api/quote`. Not called.
- IQFeed: the trial footnote's "tick data retreival is limited to 8 days during regular equity market hours" may or may not apply to paid users.
- IQFeed cancellation and minimum-term policy: on the online-billing page, not fetched.
- Barchart getHistory may have a tick type for futures.
- NT8 builds Second and Volume bars from tick data (inferred from the provider table only).
- Hugging Face `EdisonFU2025/Domestic_Futures_ticks` (MIT): content not read; probably not NQ.
- CME DataMine per-product start date for NQ: filter link not followed.

## 7. What could not be reached

| URL | Result (2026-11-04) |
|---|---|
| https://databento.com/pricing, https://databento.com/catalog/cme/GLBX.MDP3 | HTTP 200, JS shell, no content |
| https://www.kibot.com/custom-order.html | Price computed server-side (`POST /api/quote`) |
| https://firstratedata.com/i/futures/NQ | Purchase price not in static HTML |
| https://www.tickdata.com/product/historical-futures-data/ | HTTP 200, product body didn't render |
| https://www.barchart.com/ondemand and 6 other Barchart URLs | HTTP 202, empty bot-challenge body |
| https://datamine.cmegroup.com/ | TLS handshake failure |
| https://www.cmegroup.com/market-data/datamine-historical-data.html | HTTP 403, anti-scraping notice; no further cmegroup.com fetches |
| https://zenodo.org/api/records?q=… | HTTP 403 |
| https://www.rithmic.com/ ; NT Connection Guides (support.ninjatrader.com) | HTTP 200, JS shell |
| https://kinetick.com/NinjaTrader | HTTP 429 |
| https://massive.com/docs/flat-files/futures/trades | HTTP 200, JS shell |
| WRDS | Needs institutional login (not attempted) |

## 8. NEEDS AMEAR (questions only; none answered here)

1. **Connections (D-071):** may any NT8 connection other than the Simulated Data Feed be opened (Rithmic sim/paper/MFFU, Kinetick paid, IQFeed, NinjaTrader feed) to collect or backfill ticks? Today's wording says no other connection.
2. **Purchase:** any tick purchase or subscription (Kibot, Massive, Databento, IQFeed, Kinetick, TickData, DataMine). R-1104-3 holds this until proof of concept, which is not yet defined.
3. **Licences:** do Kibot's "internal use only", FirstRate's no-redistribution, or Massive's "personal, non-business and non-commercial use" fit trading an MFFU funded account?
4. **Quotes and sign-ups:** may agents request a vendor quote that needs an account, email or API key (Databento portal estimate, Kibot quote endpoint, CME DataMine login, Kibot free sample)? Each would turn an UNVERIFIED price into an OBSERVED one.
5. **Code:** routes marked "new code" (Massive, Databento, DataMine, TickData) need a converter to NT tick text. That is a code change.
6. **Scraping terms:** CME's 403 notice says scraping cmegroup.com is prohibited. The DataMine facts came from CME's Atlassian-hosted wiki instead. Is that acceptable for future work?
7. **VM look:** may an agent (or Amear) check whether "Second" is offered as the High fill series in the Strategy Analyzer dropdown, with no run? That settles part of Q4.

## 9. Evidence catalogue (verbatim excerpts, read 2026-11-04)

Each line is pasted from the stripped page text that a worker saved in the session scratchpad (raw HTML kept beside it). The HTML strip removed markup: the IQFeed line E20 has `<strong>` tags in the raw page, and the Massive pricing JSON (E30) is backslash-escaped in the raw page. E26 (a `<span>` around "DO NOT") and the E30 trades-page tier line (split by `<span>` tags) also match only after stripping. The manager re-checked E20 and E30 (§10 V1); the adversary re-found 48 excerpt substrings (§11).

**E0 — TickPrep input (repo).**
> "// Tick files:  NinjaTrader tick format: yyyyMMdd HHmmss[ fffffff];price;volume" — tools/tickprep/TickPrep.cs:18
> "//   measure <minuteFile> <contracts.csv> <outDir> [--tz-in Eastern|UTC]" — TickPrep.cs:5
> "// contracts.csv: name,path   (one line per contract, any order; '#' lines ignored)" — TickPrep.cs:16

**E1 — Databento coverage.**
> "Databento provides full coverage of all futures and options on futures beginning in June 2010." — https://databento.com/docs/venues-and-datasets/glbx-mdp3, HTTP 200
> "Nanosecond-resolution timestamps have been introduced by CME on 2015-11-20." — same URL

**E2 — Databento continuous / back-adjustment.**
> "The continuous contract prices returned are the original, unadjusted prices. We don't create a synthetic time series by back-adjusting the prices to remove jumps during rollovers." — https://databento.com/docs/standards-and-conventions/symbology, HTTP 200
> "It is not currently possible to select continuous contracts through our web portal." — same URL
> "c Refers to the offset from the closest expiration or front month." / "n Will rank the expirations by the open interest at the previous day's close." / "v Will rank the expirations by the previous day's trading volume." — same URL

**E3 — Databento `trades` schema.**
> "Trades provides every trade event. This is a subset of MBO ." — https://databento.com/docs/schemas-and-data-formats/trades, HTTP 200
> "The side that initiates the trade. Can be A sk for a sell aggressor in a trade, B id for a buy aggressor in a trade, or N one where no side is specified." — same URL
> "ts_event ... The matching-engine-received timestamp expressed as the number of nanoseconds since the UNIX epoch." — same URL

**E4 — Databento formats and billing.**
> "Choose between CSV, JSON, and our highly-compressible binary encoding, DBN." — https://databento.com/datasets/GLBX.MDP3, HTTP 200
> "Historical data is priced in $/GB. Every month, you pay only for the historical data that you've used. There is no monthly subscription fee for usage-based historical data." — https://databento.com/docs/faqs/usage-pricing-and-data-credits, HTTP 200
> "Databento meters data by its uncompressed size in binary encoding." — same URL
> "Historical from $0.50 /GB" (CME Globex MDP 3.0 card) — https://databento.com/futures, HTTP 200
> "All new users receive $125 in free credits upon signup." — usage-pricing FAQ above

**E5 — Databento arbitrary range.**
> "start= '2023-01-09T00:00' , end= '2023-01-09T20:00'" — https://databento.com/datasets/GLBX.MDP3 (API example)

**E6 — Databento calculator default (INFERRED weak as a current rate).**
> `I8e=mo({name:"pricing",initialState:{dataType:"historical",datasetId:"GLBX.MDP3",schema:"trades",unitPrice:71.4,activeInstruments:5,monthlyUsage:10,licenses:[],licensesFee:20,totalFee:714},` — https://databento.com/assets/index-DqfktovK.js, HTTP 200
> `updatePricingSchema:(t,e)=>{const{schema:n,unitPrice:r}=e.payload;t.schema=n,t.unitPrice=r,` — same file (the live value replaces the default from a server response)

**E7 — Databento 1-second bars.**
> "schema ID's suffix: -1s for 1-second, -1m for 1-minute … If no trade occurs within the interval, no record is printed." — https://databento.com/docs/schemas-and-data-formats/ohlcv, HTTP 200

**E8 — Kibot NQ in Top-10 tick package** (manager re-ran, §10 V3).
> " Listed instruments (10) / Symbol / Name / Exchange / Start / ES / E-mini S&P 500 / CME / 2009-09-30 / NQ / E-mini Nasdaq-100 / CME / 2009-09-28" (lines 40–52 joined with " / ") — https://www.kibot.com/historical-data/top-10-continuous-futures-contracts-tick-data.html, HTTP 200
> "It's $580.00 one-time, with no per-symbol fees and no subscription." — same URL

**E9 — Kibot package prices.**
> "Top 10 Futures Continuous Contracts ... Tick data $580.00 2009 + / Tick + bid/ask $800.00 2009 +" — https://www.kibot.com/buy.html, HTTP 200
> "Top 10 futures including every individual contract month. ... Tick data $1,100.00 2009 + / Tick + bid/ask $1,700.00 2009 +" — same URL
> "Prices shown are one-time and per universe. A one-time purchase gives you the full history immediately, with 45 days of unlimited downloads and daily updates, then free quarterly updates at 3, 6, and 9 months. Download access lasts one year from your last purchase, and files you download are yours to keep." — same URL

**E10 — Kibot nearest NQ example and server-side pricing.**
> "ES + NQ E-mini futures Tick + bid/ask, last 3 years $465.00" — https://www.kibot.com/custom-order.html, HTTP 200
> "Live-quotes the user's selections via POST /api/quote (debounced)," — https://www.kibot.com/js/custom-order.js, HTTP 200 (line 3)

**E11 — Kibot partial window.**
> "The start date defaults to full history : once you enter symbols and pick an interval, the box shows the first date on file for them. Type over it for a shorter window, or use the buttons below." — https://www.kibot.com/custom-order.html

**E12 — Kibot format, time, licence, roll.**
> "Tick with bid/ask ... Date,Time,Price,Bid,Ask,Size" / "Tick without bid/ask ... Date,Time,Price,Size" — https://www.kibot.com/file-format/data-format-reference.html, HTTP 200
> "Timestamps: Eastern Time (ET) by default, EST (UTC-5) or EDT (UTC-4) depending on the date; the time zone can be changed to suit your needs" — same URL
> "An experimental millisecond-timestamp variant exists for stocks, ETFs and futures; it is not officially supported." — https://www.kibot.com/file-format/millisecond-tick-data.html, HTTP 200
> "The Data is for the Licensee's own internal use only." / "The Licensee warrants that he will not resell or redistribute the Data or the Software." — https://www.kibot.com/license.html, HTTP 200
> "Kibot builds continuous contracts using calendar-based unadjusted rollover. ... There is no back-adjustment" — https://www.kibot.com/futures/continuous-futures.html, HTTP 200
> "Equity index futures (ES, NQ, YM, RTY, EMD, NKD) all roll 5 trading days before expiration." — https://www.kibot.com/futures/rollover-rules.html, HTTP 200

**E36 — Kibot NinjaTrader output option.**
> `<option value="kibot">Kibot CSV (default)</option>` / `<option value="ninjatrader">NinjaTrader</option>` — https://www.kibot.com/custom-order.html, HTTP 200
> "NinjaTrader tick yyyyMMdd HHmmss;Price;Volume Example: 20250915 103015;4520.50;3" — https://www.kibot.com/file-format/data-format-reference.html
> "Conversion to NinjaTrader or TradeStation format is available from any source resolution; it is a format change, not an aggregation." — same URL

**E13 — FirstRate NQ page (bars only).**
> "Datasets / Intraday Bars ... Start Date / End Date ... Intraday Bars / 2-Jan-2008 / 3-Nov-2026" — https://firstratedata.com/i/futures/NQ, HTTP 200
> "This dataset contains continuous data series and individual futures contracts in 1-minute, 5-minute, 30-minute, 1-hour, and 1-day timeframes." — same URL
> "Unadjusted - actual historic traded prices with no adjustments" / "Absolute-Adjusted - …" / "Ratio-Adjusted - …" — same URL
> "The files are in comma-separated (csv) format, zipped and available for immediate download" — same URL

**E14 — FirstRate tick page (stocks/ETFs).**
> "Tickers : / 5000 stocks and ETF tickers. All Russell 3000 stocks (including S&P 500 stocks) plus 2000 most liquid ETFs." — https://firstratedata.com/tick-data, HTTP 200
> "This bundle contains 1-minute, 5-minute, 30-minute, 1-hour, and 1-day historical intraday data for the 130 most actively traded futures contracts." — https://firstratedata.com/b/29/futures-most-active, HTTP 200

**E15 — FirstRate licence.**
> "(i) not to resell or otherwise redistribute the Data as part of a commercial agreement with other third-parties." — https://firstratedata.com/about/license, HTTP 200

**E16–E19 — TickData.com futures FAQ** (https://www.tickdata.com/futures-faq/, HTTP 200).
> E16 "Beginning on Jul-1-2003, our futures dataset contains full session data for all contracts that trade overnight and post-settlement, with intraday volume for all electronically-executed trades."
> E17 "We deliver all of our data (both as-traded and time series) in comma-delimited text files." / "Can I create continuous files of multiple futures contracts? / YES."
> E18 "We have futures quote data available for all symbols starting Jan-4-2010. Quote data is top of book (Level 1 or BBO) … Trade and quote data are not interlaced and are delivered in separate files."
> E19 "From Jul-1-2011 forward, all futures data contains a millisecond time stamp (e.g. HH:MM:SS.000)." / "All of our data is delivered in the time zone of the instrument’s exchange." / "The table below details recommended “Contract” and “Roll Method” settings for each futures symbol."

**E20 — IQFeed tick depth.**
> "180 calendar days of tick history (includes pre-post market) with microsecond timestamps (if available from the exchange feed) ***" — https://www.iqfeed.net/index.cfm?displayaction=data&section=services, HTTP 200
> "*** Trial users are restricted to 4 calendar days of intraday (Tick/Minute) historical data during their trial and tick data retreival is limited to 8 days during regular equity market hours" — same URL

**E21 — IQFeed fees** (https://www.iqfeed.net/index.cfm?displayaction=data&section=fees, HTTP 200).
> "Startup Fee:\n $50 \n IQFeed Core Service: \n $108.15/month*"
> "IQFeed RT US Futures and Futures Options \n $24.87/month*"
> "CME E-mini … Emini Nasdaq 100 …" then "$78.58" "$78.58" (columns "Non-Professional" / "Professionals")
> "All Prices are as of December 1st, 2025"

**E22 — IQFeed terms.**
> "All Exchange Fees are NON-REFUNDABLE once the data has been entitled on your account." — fees URL above

**E23 — Kinetick prices and tiers.**
> "The Kinetick base service costs $81.11 per month and includes the following standard features:" … "Historical tick, minute and daily data" — https://kinetick.com/Subscribe, HTTP 200
> "CME E-mini - $78.75" — same URL
> "Kinetick’s base service includes the following for only $78.75/month:" — https://kinetick.com/CME, HTTP 200
> "Globex Non-Pro Level I Data\n CME Globex - $2.10 per month" — same URL
> "The Kinetick - End Of Day (Free) connection provides FREE end of day data for stocks, futures and forex." — https://ninjatrader.com/support/helpGuides/nt8/connecting_to_kinetick.htm, HTTP 200

**E24 — Kinetick Non-Pro eligibility.**
> "An active NinjaTrader user account. Create your free user account here .\n A brokerage account that will support futures trading on NinjaTrader." — https://kinetick.com/CME

**E25 — NT help guide on Kinetick pricing (older text).**
> "Real-time data service starts as low as $60 per month" — connecting_to_kinetick.htm above

**E26 — NT8 Data by Provider** (https://ninjatrader.com/support/helpGuides/nt8/data_by_provider.htm, HTTP 200).
> "NinjaTrader, LLC is not a market data provider. Historical data is provided by our connectivity providers that offer historical data as part of their service."
> "Rithmic | YES| YES| YES| YES| YES| YES| YES| Native| F| NO| YES| YES| Extended Trading Hours| YES" (cells joined with "|" by the strip step; column 2 = Historical Tick Data)
> "NinjaTrader | YES| YES| YES| YES| YES| YES| YES| Native| F, I| NO| YES| YES| Extended Trading Hours| YES"
> Kinetick row: Historical Tick Data "YES (subscription only)"; footnote "*Historical bid/ask comes from associated value at each historical last tick value."
> "if you enable the option 'Record live data as historical' in the Control Center > Tools > Options > Market Data Category then NinjaTrader will store real-time incoming tick data to your local PC if you have a Chart or Market Analyzer (must have an indicator column added) window open."
> "Warning : Recording live data uses more PC resources and is intended for connections which DO NOT provide historical data."

**E27 — NT8 historical fill page** (https://ninjatrader.com/support/helpGuides/nt8/understanding_historical_fill_.htm, HTTP 200).
> "Selecting order fill resolution of \" High \" will allow you to set a secondary bar series to be used as the price data to fill your orders"
> "NinjaTrader will only start the backtest after we have loaded historical data for both the strategy and the order fill resolution."
> "You could choose to always use the most granular order fill resolution such as a  1 Tick Data Series ."
> "Order fill resolution cannot be used with Multi Time Frame/Multi Instrument strategies, or when Tick Replay is used."

**E28 — NT8 backtest settings** (https://ninjatrader.com/support/helpGuides/nt8/backtest_a_strategy.htm, HTTP 200).
> "Order fill resolution\n Sets the order fill resolution to be used for the backtest."
> "Start date\n Sets the start date for the test period\n End date\n Sets the end date for the test period"

**E29 — NT8 loading, merge, plans.**
> "Critical : All NinjaTrader historical data requests are handled using calendar days format" — https://ninjatrader.com/support/helpGuides/nt8/loading_historical_data.htm, HTTP 200
> "Merge back adjusted : NinjaTrader automatically merges and back adjusts historical data" — https://ninjatrader.com/support/helpGuides/nt8/options_marketdata.htm, HTTP 200
> "Record live data as historical\n Enables or disables the storage of incoming real-time Chart data to your local PC for future historical data requests. If you are connected to a provider that supports historical data, disable this feature." — same URL
> "The Free plan has no monthly fee … The Monthly plan is $99/month … The Lifetime plan is a one-time payment of $1,499" — https://ninjatrader.com/pricing/, HTTP 200
> "To activate your plan benefits—including real-time market data, trading access, and add-ons—your account must first be funded." — same URL

**E30 — Massive (ex-Polygon.io).**
> curl on https://polygon.io/pricing → `200 https://massive.com/pricing`
> "Futures Basic Free Not included Futures Starter $29/mo Not included Futures Developer $79/mo 5 years Futures Advanced $199/mo All history Futures Business CME $999/mo All history" — https://massive.com/docs/rest/futures/trades-quotes/trades, HTTP 200
> "Plan History Records date back to April 3, 2017" — same URL
> "The futures contract identifier, including the base symbol and contract expiration (e.g., GCJ5 for the April 2025 gold contract)." — same URL
> "Timestamps in our futures API responses are returned in Coordinated Universal Time (UTC). Trade, quote, and aggregate ( window_start ) timestamps are Unix timestamps expressed in nanoseconds since the epoch" — https://polygon.io/docs/futures, HTTP 200
> `"historical_data":"7+ Years Historical Data" ... "trades":"available" ... "name":"Futures Advanced" ... "license_type":"personal","monthly_price":{"amount":19900 ... "qualifications":["non_professional"]` — massive.com/pricing embedded JSON (unescaped), HTTP 200
> `"name":"Futures Developer"` … `"quotes_top_of_book":"available" ... "second_aggregates":"available" ... "trades":"available"` — same
> "solely for your own personal, non-business and non-commercial use. Personal use includes your own research, analysis and investment activities" — https://massive.com/legal/market-data-terms-of-service, HTTP 200
> **E30b** "Canceling a subscription does not end your license before the end of the period you have paid for." / "When your license to any Information ends, you must stop using it and delete it promptly, and in any event within thirty (30) days, including downloaded files, stored copies and caches." — https://massive.com/legal/market-data-terms-of-service, HTTP 200
> Note: the pricing JSON says Advanced is "7+ Years"; the trades page says "All history" and "April 3, 2017". Both cover 2021-03-08.

**E31 — Barchart.**
> https://www.barchart.com/ondemand → HTTP 202, 0 bytes (plain UA); 202, 1997 bytes (browser UA), no text after stripping
> "barchart/barchart-ondemand-client-python | Simple Python client for Barchart OnDemand REST APIs | Organization" — https://api.github.com/search/repositories?q=barchart+ondemand, HTTP 200

**E32–E34 — CME DataMine** (CME Group Client Systems Wiki, Confluence REST, HTTP 200; cmegroup.com itself returned 403).
> 403 body: "This IP address is blocked due to suspected web scraping activity associated with it on this CMEgroup.com page. Use of scripts, software, spiders, robots, avatars, agents, tools or other scraping mechanisms is strictly prohibited by CME Group's website Data Terms of Use." — https://www.cmegroup.com/market-data/datamine-historical-data.html, HTTP 403
> E32 "CME Electronic Pit 6/26/1992 1/4/1982 Present Present" / "Are bids and asks included in Time and Sales files? No." / "E Instrument_Symbol String Globex Contract / Instrument Code ESH5" / "Please note the Time and Sales data files do not include column headers." — https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457223239/Time+and+Sales
> E33 "CME/CBOT T&S data is in CT. Files from 03/11/2025 onwards are in UTC." / "Time and Sales records have timestamps to the nanosecond for data after 3/11/2025. Data before then is timestamped to the second." / "Time and Sales CSV format v2 (beginning 08/22/2022) … Datetime of transaction to the nanosecond, in ISO 8601 format (UTC)" / "A user should always sort by sequence number and not timestamp when using these files." — same page
> E34 "Top of Book data is available on four exchanges in ASCII format from as early as 1999. A new CSV format is available starting on Monday, April 14, 2025. The following 3 dates are unavailable: 06-14-2024 01-09-2024 03-10-2023" — wiki content 457418968 / "Through the DataMine Self-Service Center, users can query, price, order, receive, and manage historical data subscriptions. … To access the CME DataMine self-service platform, please register for a CME Group Login." — wiki content 457088998

**E35 — Open datasets.**
> Zenodo `records?q=…`: HTTP 403, "Access to this resource has been restricted due to unusual traffic from"
> Hugging Face `datasets?search=nq%20futures` → `[]`
> Kaggle: `"subtitleNullable":"Regular-session NQ bars, Dec 2022 to Dec 2025, for a funded-challenge study"` … licence "Apache 2.0" — https://www.kaggle.com/api/v1/datasets/list?search=nq%20futures%20tick, HTTP 200
> GitHub `q=NQ+futures+tick+data`: total_count 4, none hosts a dataset; e.g. "Candlestick Charts with real tick data from R:\Futures Data\NQ - Tick Chart" — https://api.github.com/repos/apointandaline/nq-futures/readme

**E39 — Portara (repo, REPORTED).**
> "| **Price** | **$695 flat, 2014 → present.** Per year is $125 with a $500 minimum, counted back from today, so reaching March 2021 costs 6 × $125 = **$750**. Flat is cheaper. | REPORTED (Portara pricing pages) |" — docs/reports/2026-11-02-vm-high-res-plan.md:45
> "- **No backfill.** NT's servers keep about 1 year of ticks, and a custom name like `NQCONTROW` returns "Unknown instrument". The ticks must be imported. REPORTED (NT forum / help guide); the server limit is UNVERIFIED here." — same file :27

**E40 — D-071 as restated by Amear** (manager grep, §10 V4).
> "DECISION_LOG.md:427:- [2026-10-20T16:37:30Z] WHO: amear | WHAT: **K5/K8 RE-RULED on the corrected framing: KEEP AS FOUND.** Simulated Data Feed is connected and Simulation (the demo server) is not. **D-071 is restated by Amear: the Simulated Data Feed is the one allowed connection. No orders, no other connection.**"

## 10. Verification evidence (manager re-runs, pasted output)

**V0 — brief hash** (`shasum -a 256 docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md`):
```
4c115d0382c571487ce2c249c34aa533d8330ba9454c283c7bdeee3312059980  docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md
```

**V1 — worker excerpts re-found in saved raw/stripped pages** (manager `/usr/bin/grep -o` on w1–w3 pages):
```
== Tick data \$580.00
 Tick data $580.00 2009 +
== Tick data \$1,100.00
 Tick data $1,100.00 2009 +
== last 3 years \$465
 ES + NQ E-mini futures Tick + bid/ask, last 3 years $465.00
== from \$0.50
 from $0.50 /GB
== internal use only
 The Data is for the Licensee's own internal use only.
== 108.15/month
w2-pages/iq_fees.txt
== Record live data as historical
w2-pages/nt_dbp.txt
== Records date back to April 3, 2017
w3-pages/m_trades.html
== non-business and non-commercial
w3-pages/m_terms.txt
		<li> <strong>180 calendar days of tick</strong> history (includes pre-post market) with microsecond times
res_advanced\":{\"display\":\"$$199\",\"amount\":19900},\"stocks_starter_legacy\":{\
_data\":\"7+ Years Historical Data\",\"
Futures Advanced $199/mo Futures Business CME $999/mo Fu
inute) historical data during their trial and tick data retreival is limited to 8 days during regular equity market hours
```
Massive terms (E30b), `/usr/bin/grep -o` on `w3-pages/m_terms.txt`:
```
Canceling a subscription does not end your license before the end of the period you have paid for.
When your license to any Information ends, you must stop using it and delete it promptly, and in any event within thirty (30) days, including downloaded files, stored copies and caches.
```

**V2 — current strategies place no resting stop or target** (§3.4 caveat b):
```
$ /usr/bin/grep -c -E "SetStopLoss|SetProfitTarget|SetTrailStop|StopMarket|StopLimit|LimitOrder" ninjascript/PraxisNoiseAreaBreakout.cs ninjascript/PraxisNoiseAreaBreakout_OppBand.cs ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
ninjascript/PraxisNoiseAreaBreakout.cs:0
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:0
$ /usr/bin/grep -n -E "Calculate = |ExitLong\(|EnterLong\(" ninjascript/PraxisNoiseAreaBreakout.cs
211:					ExitLong("XL", "");
227:				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
288:				ExitLong("FlatEOD", "");
```
(The `Calculate = ` pattern did not match in this run because of the spacing in the file. The adversary's run found `105: Calculate = Calculate.OnBarClose;`, §11.)

**V3 — FirstRate "$75–225" location** (`/usr/bin/grep -rn -F '$75–225' --include='*.md' .`, lines cut to 200 chars):
```
./docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md:18:   - Project doc "PHASE 3 — BUILD SPECIFICATION" (pass gates; FirstRate $75–225)
./Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-0085-4b1e-a813-4f4221d90a63_text_markdown.md:152:| Pre-2024 history backstop (if WFO needs it) | FirstRate Data NQ 1-min | One-time
./Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-0085-4b1e-a813-4f4221d90a63_text_markdown.md:582:- One-off historical-data backstop purchase (FirstRate Data $75–225) — amortize
./Redemtion/Intitialization-April 2026/PRAXIS_PHASE_3_OUTPUT_SUMMARY.md:104:- Historical data sourcing: purchase from FirstRate Data ($75–225 one-time) for walk-forward validation + collect forward
./Redemtion/Intitialization-April 2026/PRAXIS_PHASE_3_OUTPUT_SUMMARY.md:160:| Block 2 (Backtesting) | $75–225 one-time + $50–100 MFFU eval + $12/mo CME data | FirstRate Data + Rithmic connection |
.gitignore:7:Redemtion/	Redemtion/
```
An earlier manager search for this figure returned nothing because the shell `grep` wrapper skips gitignored paths. The adversary caught it (§11, M3).

**V4 — D-071 restatement** (`/usr/bin/grep -n "D-071" DECISION_LOG.md`, the relevant line, cut):
```
DECISION_LOG.md:427:- [2026-10-20T16:37:30Z] WHO: amear | WHAT: **K5/K8 RE-RULED on the corrected framing: KEEP AS FOUND.** Simulated Data Feed is connected and Simulation (the demo server) is not. **D-071 is restated by Amear: the Simulated Data Feed is the one allowed connection. No orders, no other connection.**
```
A grep of `DECISIONS.md` for "D-071" returned no line. D-071 sits in the migration-side ledger, restated in this repo's DECISION_LOG as above.

**V5 — Kibot Top-10 tick page lists NQ** (`sed -n 40,52p w1-pages/kb-top10tick.txt`):
```
 Listed instruments (10)
 Symbol
 Name
 Exchange
 Start
 ES
 E-mini S&P 500
 CME
 2009-09-30
 NQ
 E-mini Nasdaq-100
 CME
 2009-09-28
```

**V6 — repo state** (`git diff --cached --name-only | wc -l`; `git status --porcelain | wc -l`; `git rev-parse --short HEAD`), taken before this report was written:
```
      12
     103
87d506f
```
The 12 staged paths are the old unrelated set (D-2026-11-04-A R-1104-1). This unit staged nothing. Observer effect: this report adds one untracked file, so `git status --porcelain` reads 104 after it lands.

## 11. Adversarial findings

**W5 (adversarial, on the first full draft): `Result: FAIL`, 2 blocking + 13 minor.** It re-found 48 excerpt substrings in the raw pages with meaning intact. A live re-fetch of Kibot buy.html, the Massive trades page and the IQFeed fees page showed every quoted price unchanged. Its A4 grep of the strategies, pasted from its file:
```
105: Calculate = Calculate.OnBarClose;
108: IsExitOnSessionCloseStrategy = true;   // backstop; explicit 16:00 flat is primary
211: ExitLong("XL", "");   219: ExitShort("XS", "");
227: EnterLong(Contracts, "L");   229: EnterShort(Contracts, "S");
288: ExitLong("FlatEOD", "");   290: ExitShort("FlatEOD", "");
```
- **B1:** Massive "one month if one is enough" was refuted by Massive's own terms (delete within 30 days; E30b). **Fixed:** §5 split into one-time and subscription sorts; Massive's licence cell, §3.1 and §1 updated.
- **B2:** §1 line 1 counted IQFeed as reaching the whole window. **Fixed:** the count is 2 read this session (Kibot, Massive) plus Portara (REPORTED); the table has 14 rows.
- **M1–M13 fixed** with W5's replacement text: IQFeed's asset class not named; IQFeed reaches nothing after ~2027-01-13; FirstRate's figure is in gitignored `Redemtion/` files and labelled 1-minute; Kibot's NT option is on the custom-order form only; the DataMine timestamp contradiction is kept open; caveat (b) is now OBSERVED for current code (V2); the broken §4.3 reference; NT8 storage is INFERRED; Massive's 1-second flag is excerpted for Developer only; the Portara 2-year count is INFERRED; the IQFeed one-time backfill is answered; markup splits are disclosed.
- **W5 S8 sweep:** no sentence decides for Amear.

**W6 (adversarial re-check of the fixed draft): `Result: FAIL`, 1 blocking + 5 minor.** It confirmed B1, B2, M2, M4, M5 and M7–M13 resolved, and M1, M3 and M6 partly resolved. It found 3 × $199 = $597, 2027-01-13, the "2 have a published price" count and the 14 rows correct. Every cited E-number exists, and E30b matches `m_terms.txt` exactly.
- **D1 (blocking):** §10 and §11 were cited but not yet written, so the V2 fact had no pasted output. **Fixed:** this §10 and §11, with V2 pasted.
- **D2–D6 fixed** with W6's replacement text: "Rolling" graded INFERRED; Massive also compared with Kibot's $1,100 package (≤ 5 months); Kibot's end date marked INFERRED in §1; the brief is untracked, not git-tracked; the FirstRate "tick samples available" lead added to §6.
- **Not re-attacked after the W6 fixes.** D2–D6 are W6's exact replacement text; D1 is this section. A third adversarial pass was not run (turn budget).

## 12. Manager record

**Task.** Brief A of `docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md`. Enumerate NQ tick sources for 2021-03-08 → 2026-07-17, with cost, format and NT8 path. Answer Q1–Q4, give a ranked shortlist by stated criteria, and list leads not confirmed. Research only.

**Rubric criteria addressed** (`specs/SPEC_RUBRIC.md`): S1 (`:107`), S2 (`:108`), S8 (`:114`), as quoted in the dispatch.

**Workers dispatched.**

| Id | Mode | Scope | Outcome |
|---|---|---|---|
| W1 | BUILD | Databento, Kibot, FirstRate, TickData | Returned; findings with excerpts; 31 tool calls |
| W2 | BUILD | IQFeed, Kinetick, NT data, Rithmic; Q2, Q3 | Returned; 32 tool calls |
| W3 | BUILD | Barchart, Massive/Polygon, CME DataMine, open data; Q4 | Returned; 32 tool calls |
| W4 | BUILD | Gap-fill: Kibot NQ price rule, Databento $/GB, Kibot NT format | Returned; G1 UNVERIFIED (server-side), G2 $71.40 default (INFERRED weak), G3 OBSERVED/INFERRED |
| W5 | ADVERSARIAL | Full draft vs raw pages, live re-fetch, strategy code | FAIL 2B/13M, all fixed |
| W6 | ADVERSARIAL | Re-check of fixes | FAIL 1B/5M, all fixed; not re-attacked |

**Process log.** Read the brief (hash V0), the rubric lines, D-071 (V4), D-2026-11-04-A, and the Portara and fill-resolution repo reports. Dispatched W1–W3 in parallel, each with its own pages directory. Read all three findings files in full. Spot-checked excerpts against the raw pages (V1). Resolved a W1/W4 conflict on Kibot Top-10 membership from the page (V5). Dispatched W4 for price gaps. Drafted in the scratchpad. W5 attack, fixes by exact-match script, W6 re-check, fixes. Wrote this report last.

**S6 cross-block check.** No F-block spec changed. F1 (`specs/SPEC_RUBRIC.md:17-28`), F2 (`:30-43`), F3 (`:45-57`) and F4 (`:59-70`) are untouched; line ranges are as cited in D-2026-11-04-A and not re-read this unit. F3 and D-2026-10-30-A's void clause stand. This report authorises no purchase, import or run. No code, template, config or ledger was edited.

**Files staged.** None. This unit staged nothing (V6). Written: this report (untracked). Scratch: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/research-A/` (pages, findings w1–w6, drafts).

**Result: PASS** — manager stress-test only: every W5/W6 finding fixed with its own replacement text. No third re-attack after the W6 fixes. Not audited; the master's audit decides.

## Correction 1 (2026-11-04, after audit FAIL 1)

Append-only: no line above was edited. Where a line above conflicts with this section, this section governs. Pages were fetched live on 2026-11-04 into `scratchpad/corr-A/` (full path in §12's scratch note, `.../scratchpad/corr-A/`). They were stripped with `python3 -I .../scratchpad/corrA-strip.py <html> <txt>`. The script sits outside `corr-A/`. It removes `<script>`/`<style>`, turns tags into newlines and unescapes entities. Pages only: no data file, no account, no purchase.

**Fetch** (`curl -sSL --max-time 20 -A "Mozilla/5.0" -o $D/<id>.html -w "<id> %{http_code} %{url_effective} %{size_download}\n" <url>`):
```
kb10c 200 https://www.kibot.com/historical-data/top-10-futures-contracts-tick-data.html 212073
mpr 200 https://massive.com/pricing 233821
mfut 200 https://massive.com/futures 291989
mprod 404 https://massive.com/docs/rest/futures/reference/products 309682
mcon 404 https://massive.com/docs/rest/futures/reference/contracts 309684
```
Second fetch, same flags, `-w "<id> %{http_code} %{size_download}\n"`, URLs taken from https://massive.com/sitemap.xml (`msite 200 36306`):
```
mblog 200 298934
mkb1 200 354613
mkb2 200 287979
```
(`mkb1` = https://massive.com/knowledge-base/article/does-massive-have-continuous-futures-contracts; `mblog` = https://massive.com/blog/futures-data-has-arrived.)

### C-M1 (S1): Massive annual discount, §2 Massive row, "20% off annual (OBS)"

New excerpt **E30c**. `/usr/bin/grep -n -o -i -E ".{0,40}save 20%.{0,40}|.{0,40}20% .{0,40}" mpr.html`:
```
1:class="text-sm font-bold text-gray-500">Save 20% with the annual plan</span></div></div>
2:class="text-sm font-bold text-gray-500">Save 20% with the annual plan</span></div></div>
```
Stripped text, `/usr/bin/grep -n -F "Save 20%" mpr.txt`:
```
76:Save 20% with the annual plan
94:Save 20% with the annual plan
```
> **E30c** "Save 20% with the annual plan" (appears twice): https://massive.com/pricing, HTTP 200.

Grade stays OBSERVED, now with an excerpt. Which tiers the 20% applies to is not stated next to the string (UNVERIFIED). No annual price is computed here.

### C-M2 (S2/S1): Kibot's $1,100 per-contract package and NQ

E8 is the **continuous** package page. E9 gives the $1,100 price but no instrument list. Neither shows NQ for the per-contract package, so the OBSERVED grade on §1 item 1 and §5 row 3 was not supported by them. New excerpt **E8b**, from https://www.kibot.com/historical-data/top-10-futures-contracts-tick-data.html, HTTP 200. `/usr/bin/grep -n -E "NQ|Nasdaq|April 2010|individual contract|\$1,100|2009-09-28" kb10c.txt | head -20`. Selected output lines; the omitted lines are 66, 102, 118 and 162 (other symbols' `2009-09-28` starts) and 207–220 (NQ contract rows):
```
17:Top 10 futures including every individual contract month.
18:Kibot's Top 10 Futures Continuous and Individual Contracts tick dataset covers 1,000+ symbols, with continuous series since September 2009 and individual contracts from April 2010, delivered in one consistent CSV schema. Expired contracts are included. It's $1,100.00 one-time, with no per-symbol fees and no subscription. Download a free sample before you buy.
19:$1,100.00
20:Continuous series since September 2009, individual contracts from April 2010
21:Add to cart, $1,100.00
203:NQ
204:E-mini Nasdaq-100
206:2009-09-28
```
In-window NQ contracts listed on the same page, `/usr/bin/grep -n -A3 -E "^NQ(H21|M21|U26)$" kb10c.txt | tr '\n' '|'`:
```
215:NQU26|216-E-mini Nasdaq-100 (U26)|217-CME|218-2025-10-27|--|2621:NQH21|2622-E-mini Nasdaq-100 (H21)|2623-CME|2624-2020-03-06|--|2689:NQM21|2690-E-mini Nasdaq-100 (M21)|2691-CME|2692-2020-09-02|
```
`/usr/bin/grep -c -E "^NQ[FGHJKMNQUVXZ][0-9]{2}$" kb10c.txt` → `73` NQ contract rows.

**Corrected statement.** Kibot's $1,100 per-contract tick package lists NQ, E-mini Nasdaq-100, CME, from 2009-09-28, and individual NQ contracts including NQH21, NQM21 and NQU26 (OBSERVED [E8b]). Per that page, **per-contract history begins April 2010**. That still covers 2021-03 → 2026-07. No end date is shown, so reaching 2026-07-17 stays INFERRED, as before. Read §1 item 1 and §5 row 3 as citing **[E8b]**, not [E8, E9], for the per-contract package. E9 still supports the price and the "daily updates" wording. One strip artefact is disclosed and not used: the NQH10 row shows no start date in the stripped text (`NQH10|E-mini Nasdaq-100 (H10)|CME|NQH11|E-mini Nasdaq-100 (H11)|CME|2010-05-24|`).

### C-M3 (S2): Massive "reaches the whole window" in §1

§2 graded Massive's NQ coverage INFERRED. §1 item 1 said it reaches the whole window with no grade. Searching for NQ on the pricing and futures pages, `/usr/bin/grep -c -E "\bNQ[HMUZ][0-9]" mkb1.txt mfut.txt mpr.txt mblog.txt`:
```
.../corr-A/mkb1.txt:10
.../corr-A/mfut.txt:0
.../corr-A/mpr.txt:0
.../corr-A/mblog.txt:0
```
`mkb1` names NQ in a recent-roll table. Caption (`sed -n 292,304p mkb1.txt | tr '\n' ' '`): "This table shows, for three recent expiries, the session in which the later contract's daily volume first passed the expiring contract's: Product Expiring contract Its last trade date Later contract …". The NQ row (`sed -n 305,318p mkb1.txt | tr '\n' '|'`):
```
15 June 2026|3|MGC|MGCQ6|27 August 2026|MGCZ6|29 July 2026|29|NQ|NQU6|18 September 2026|NQZ6|14 September 2026|4|
```
> **E30d** "NQ | NQU6 | 18 September 2026 | NQZ6 | 14 September 2026 | 4" (row of the roll table) — https://massive.com/knowledge-base/article/does-massive-have-continuous-futures-contracts, HTTP 200.

E30d shows only that Massive serves 2026 NQ contracts. No Massive page read gives an NQ start date. **Corrected §1 item 1, Massive clause:** "Massive (ex-Polygon) $199/month. Futures trades date back to April 3, 2017 dataset-wide (OBSERVED [E30]). NQ is served as a product, with 2026 contracts named (OBSERVED [E30d]). That NQ history reaches 2021-03-08 is **INFERRED**: no page read names an NQ start date. Downloaded data must be deleted within 30 days after the plan ends [E30b]." The same grade applies to the §2 Massive Cov cell ("NQ by name not shown" is now superseded by E30d; the reach is still INFERRED) and to §5's subscription row ("2017 → present … (OBS)" is dataset-wide; NQ reach is INFERRED). So §1's count of "2 … that reaches the whole window" is: Kibot, NQ named from before the window (OBSERVED [E8, E8b]), end date INFERRED; and Massive, whole-window NQ reach INFERRED.

### C-M4 (S1): what was confirmed live in this correction

Re-fetched live on 2026-11-04 for this correction: **E30c** (new), **E8b** (new), **E30d** (new). E8b also re-confirms the $1,100.00 price (E9) and NQ 2009-09-28 (E8 / V5). No other §9 excerpt was re-fetched here. Their basis is unchanged from §9–§11: read 2026-11-04 by W1–W4 and re-checked by W5/W6.

**Correction record.** The manager did this correction directly (narrow, budget ~15 turns). No worker or adversary was dispatched, so these corrections have **not been adversarially re-checked**. The master's audit decides. Nothing staged, no `git add`, no other file touched. Research-only rules held.
