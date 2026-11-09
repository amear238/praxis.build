Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

# R6 step 1 — MFFU rule read and announcement-strategy research design (unit `2026-11-09-r6-step1`, bead `Praxis_build-ckh`)

## For Amear (plain English)

MFFU's current rules allow the pre-announcement trade as R6 describes it: buy in the evening, sell five minutes before the 08:30 release. That stays inside one MFFU session, which runs 6 PM to 4:10 PM. The flat time is 4:10 PM; 16:59 appears nowhere. The announcement-day hold through the release is blocked on Rapid and Pro funded accounts: MFFU requires being flat two minutes either side of CPI, jobs, FOMC and FOMC-minutes releases. MFFU's own pages disagree about Builder. A split version that steps out around each release is specified instead. Two problems surface before any backtest. First, these events give about 30 trades a year, so the walk-forward's 250-trade gate cannot be met. Second, gaps between events often exceed MFFU's 7-day inactivity limit. Both are recorded as open items. Nothing was bought, built or run.

## Task

Amear D-2026-11-08-A R6 (DECISIONS.md :1572-1579), pulled to P0 by D-2026-11-08-D D7 (fired at `f10603a`). Part A: read MFFU's current rules (T1 news, trading-day boundary, flat time, consistency/EOD trailing) before any build. Part B: a research design for Pre-Announcement Drift (evening entry, exit before the release) and the Macroeconomic Announcement-Day Premium. Design only. Worktree, no commit.

## Rubric criteria addressed

S1 (pasted output in E1-E10), S2 (OBSERVED/INFERRED/UNVERIFIED on every item; design level WRITTEN), S4 (one gap, see Decisions item 1), S6 (design §7 and the S6 section below), S8 (D2 list; no Amear question answered), S13 (one line per file, counted in E10). F2, F3 and O4 are named as cross-block dependencies only; none is changed.

## Workers dispatched (id, mode, outcome)

| id | mode | task | outcome |
|---|---|---|---|
| W1 | BUILD | MFFU page capture, six evidence .txt files, quote catalogue K1-K30 | returned; 77 help articles + 4 plan pages, all HTTP 200 except /faq 404 |
| W2 | BUILD | papers + calendars | **NO RESULT**: hit the 40-turn cap with no report; split into W2a/W2b |
| W3 | BUILD | repo and data facts (read-only) | returned; corrected the brief: D-2026-11-08-A R3 is the WFE ruling, and Overnight Drift was accepted in Phase 2 Round 3 (D6) |
| W2a | BUILD | paper abstracts | returned; three abstracts, "Ai 2024" candidates |
| W2b | BUILD | free event calendars and counts | returned; BLS 403; Fed + ALFRED free |
| W4 | ADVERSARIAL | find current MFFU text contradicting the Part A readings | `GRADE: CONTRADICTED` (scope of the T1 restriction); see Adversarial findings |
| W5 | ADVERSARIAL | attack the design file, first version | `GRADE: DEFECTS FOUND`, 8 MAJOR / 7 MINOR; all 15 addressed in the second version (below) |

## Process log

1. `git worktree add /Volumes/Sensidine/Praxis.build-r6 …` failed: `fatal: could not create leading directories of '/Volumes/Sensidine/Praxis.build-r6/.git': Permission denied`. The volume root is `drwxrwxr-x root wheel`, and `id` shows user `admin` is not in `wheel` (E1). The branch `r6/announcement-research` was created at `f10603a`. The worktree was then added at `/Users/admin/Praxis.build-r6` (Decisions item 1).
2. W1, W2 and W3 ran in parallel. W2 died at its turn cap, so its scope was split into W2a and W2b, which ran in parallel with adversary W4.
3. The manager re-ran the MFFU quote greps (E2), fetched the T1 calendar image and the contradiction pages into evidence (E3), viewed the image (E4), re-ran W2b's count (E7), and re-fetched the abstracts (E6).
4. The manager computed event counts, the bar presence check and the inactivity gaps with its own script `/tmp/r6-mgr/bin/ev.py` (E8).
5. Design v1 was written and attacked by W5 (15 defects). Design v2 was rewritten to address each one; the defect-by-defect disposition is in Adversarial findings. v2 was not re-attacked by a fresh adversary (turn budget), and that is a limitation of this result.

## Part A — MFFU current rules (answers)

All quotes are OBSERVED in `docs/reports/evidence/2026-11-09-r6-mffu-*.txt` (fetch headers in E2) or in the PNG (E4).

1. **T1 news rule — OBSERVED, with a scope conflict inside MFFU's text.**
   - T1 = "FOMC Meetings, FOMC Minutes, Employment Report, CPI" (news.txt:38).
   - "All positions must be flattened at least two minutes prior to the scheduled T1 News event. For example, if news is at 8:30, positions must be closed by 8:28:00 or earlier, and may only be reopened after 8:32:00" (news.txt:28).
   - Restricted: Rapid Sim Funded and Pro Sim Funded. Unrestricted: all evaluations and Builder Plans (news.txt:30-35). Live: "Yes, you can trade news" (trading-day.txt:87). Studio: "Is news trading allowed? Yes." (plans.txt:954-955).
   - **Conflict (W4, re-verified E3/E4):**
     - The 2026 calendar image says "strictly prohibited on sim funded accounts 2 minutes before and after the event", with no plan named.
     - Builder guides say "T1 news trading is allowed during the Evaluation and Sim Funded stages" (adversarial.txt:332).
     - Rapid EOD 25K says "News trading is not allowed on this Sim Funded account" (adversarial.txt:150).
     - "Standard Trading Protocols" says flat 2 minutes around "any data release" (news.txt:20-21; adversarial.txt:32-33).
   - Penalty: only the general fair-play text, "Termination" and "Profit Confiscation" (news.txt:95-96). No news-specific penalty is stated (UNVERIFIED).
2. **Trading-day boundary — UNVERIFIED as worded by R6; the session window is OBSERVED.**
   - "Trades may be placed beginning at 6:00 PM EST when the Globex session opens and can remain open until the New York session closes at 4:10 PM EST." (trading-day.txt:10).
   - Plain answer: an evening entry after 18:00 ET belongs to the MFFU session that ends at 16:10 ET on the release day, so it is in the same session as an 08:30 release that day. MFFU never says "trading day" for this.
   - The Rapid FAQ says "Holding overnight will breach the account" but glosses it in the same answer as "All positions must be closed before the daily session close" (plans-site.txt:24). That gloss supports the reading (INFERRED). No text addresses an evening entry explicitly, so the grade stays UNVERIFIED.
3. **Flat-by time — OBSERVED: 4:10 PM ET ("EST" in MFFU's text).**
   - "any open positions will be automatically closed at 4:10 PM EST on regular (non-holiday) trading days" (trading-day.txt:12).
   - 16:59 is not in any fetched page (W1 and W4 both report zero hits; W4's liveness: `4:10` matched on several pages). The 16:59 figure came from the external D8 document (strategy-filter audit :171).
   - Holidays: no auto-liquidation; the trader must close (trading-day.txt:20-22).
4. **Consistency and EOD trailing drawdown — OBSERVED.**
   - "The consistency rule at MyFundedFutures is 30% on our Rapid EOD plans and 50% for Rapid Intraday and Pro plans. (Pro Plan One day pass has no consistency rule)" (consistency.txt:13); exceeding it "does not breach" (:22).
   - EOD trailing "does not move intraday – only at the close of each trading session" (drawdown.txt:153); it locks at +$100 (drawdown.txt:158). Rapid Sim Funded trails intraday (drawdown.txt:38).
   - Few-days-a-month bearing: "If a trader does not place a trade for 7 consecutive calendar days, the account could be closed. This includes simulated funded accounts." (consistency.txt:46). The article ties this to the one-time-payment model "Effective August 25, 2026" (:42). The Builder table lists "7 Calendar Days" (plans-site.txt:1086). Live has none (trading-day.txt:1111).

**Per strategy:**
- **Pre-Announcement Drift as R6 describes it** (evening entry, exit before the release): ALLOWED by MFFU's current text on every account. Residual risk: the word "overnight" (OPEN-1).
- **Announcement-Day Premium as a hold through the release:** **BLOCKED BY MFFU RULE on Rapid Sim Funded and Pro Sim Funded**: "Restricted Accounts: Trading on T1 News events is prohibited for the following: Rapid Sim Funded / Pro Sim Funded" (news.txt:30-32) and "All positions must be flattened at least two minutes prior to the scheduled T1 News event." (news.txt:28). On Builder Sim Funded MFFU's text conflicts, and the design treats it as blocked [D1]. The design specifies a compliant split variant (2S).

## Verification evidence (pasted output only)

**E1 — worktree path.**
```
fatal: could not create leading directories of '/Volumes/Sensidine/Praxis.build-r6/.git': Permission denied
drwxrwxr-x@ 18 root   wheel   576 Aug 24 10:32 /Volumes/Sensidine
uid=501(admin) gid=20(staff) groups=20(staff),12(everyone),61(localaccounts),79(_appserverusr),80(admin),...
Preparing worktree (checking out 'r6/announcement-research')
HEAD is now at f10603a docs: D6 drawdown viability check ...
```

**E2 — MFFU evidence headers and key quotes (manager re-run of W1's capture).** Fetch headers (excerpt):
```
2026-11-09-r6-mffu-news.txt  1:URL: https://help.myfundedfutures.com/en/articles/8230009-news-trading-policy
                              2:FETCHED_UTC: Mon Nov  9 09:06:22 UTC 2026   3:HTTP: 200
2026-11-09-r6-mffu-trading-day.txt 1:URL: https://help.myfundedfutures.com/en/articles/9558251-permitted-times-to-trade
                              2:FETCHED_UTC: Mon Nov  9 09:06:22 UTC 2026   3:HTTP: 200
2026-11-09-r6-mffu-consistency.txt 1:URL: https://help.myfundedfutures.com/en/articles/11994562-consistency-rule-at-my-fundedfutures
                              2:FETCHED_UTC: Mon Nov  9 09:06:23 UTC 2026   3:HTTP: 200
2026-11-09-r6-mffu-drawdown.txt 1:URL: https://help.myfundedfutures.com/en/articles/8348565-end-of-day-eod-drawdown-explained
                              2:FETCHED_UTC: Mon Nov  9 09:06:22 UTC 2026   3:HTTP: 200
2026-11-09-r6-mffu-plans.txt  1:URL: https://help.myfundedfutures.com/en/articles/17573707-comprehensive-look-into-redesigned-pro-plan
                              2:FETCHED_UTC: Mon Nov  9 09:06:26 UTC 2026   3:HTTP: 200
2026-11-09-r6-mffu-plans-site.txt 1:URL: https://myfundedfutures.com/plans/rapid
                              2:FETCHED_UTC: Mon Nov  9 09:07:41 UTC 2026   3:HTTP: 200
```
(Each file holds 2-4 pages, each with its own URL/FETCHED_UTC/HTTP/RAW_SHA256 block. This block was condensed from the grep output to two lines per file; every line shown is verbatim.) Key quotes, `/usr/bin/grep -n` output:
```
2026-11-09-r6-mffu-news.txt:28:All positions must be flattened at least two minutes prior to the scheduled ⁠T1 News event. For example, if news is at 8:30, positions must be closed by 8:28:00 or earlier, and may only be reopened after 8:32:00
2026-11-09-r6-mffu-news.txt:30:Restricted Accounts: Trading on T1 News events is prohibited for the following:
2026-11-09-r6-mffu-news.txt:31:Rapid Sim Funded
2026-11-09-r6-mffu-news.txt:32:Pro Sim Funded
2026-11-09-r6-mffu-news.txt:34:All evaluations
2026-11-09-r6-mffu-news.txt:35:Builder Plans
2026-11-09-r6-mffu-news.txt:38:For All Traders: FOMC Meetings, FOMC Minutes, Employment Report, CPI
2026-11-09-r6-mffu-trading-day.txt:10:Trades may be placed beginning at 6:00 PM EST when the Globex session opens and can remain open until the New York session closes at 4:10 PM EST.
2026-11-09-r6-mffu-trading-day.txt:12:At MyFundedFutures, any open positions will be automatically closed at 4:10 PM EST on regular (non-holiday) trading days. Holiday trading hours will be communicated to traders including closure of open positions.
2026-11-09-r6-mffu-trading-day.txt:1108:Q: Can I hold positions overnight?
2026-11-09-r6-mffu-trading-day.txt:1109:No. All positions must be closed before the end of the trading session. Any open positions at session close will be automatically closed by the platform.
2026-11-09-r6-mffu-trading-day.txt:1111:If you do not place a trade within 7 consecutive calendar days on your sim funded account, the account will be closed due to inactivity. There is no inactivity rule on the live account.
2026-11-09-r6-mffu-consistency.txt:13:The consistency rule at MyFundedFutures is 30% on our Rapid EOD plans and 50% for Rapid Intraday and Pro plans. (Pro Plan One day pass has no consistency rule)
2026-11-09-r6-mffu-consistency.txt:46:If a trader does not place a trade for 7 consecutive calendar days, the account could be closed. This includes simulated funded accounts.
2026-11-09-r6-mffu-plans-site.txt:24:A: No. Rapid is intended for intraday futures trading. All positions must be closed before the daily session close. Holding overnight will breach the account.
2026-11-09-r6-mffu-drawdown.txt:153:It does not move intraday – only at the close of each trading session.
```

**E3 — contradiction pages fetched by the manager into `2026-11-09-r6-mffu-adversarial.txt`.**
```
IMG fetched Mon Nov  9 09:18:32 UTC 2026
HTTP 200 7101784
...t1-calendar-2026.png: PNG image data, 3840 x 2160, 8-bit/color RGB, non-interlaced
3ab6c6d941be8c7cd15dd3dd8db0395920eb7b07fde8e819a8c3754b558ce5d4  (original, before downscale)
8230009-news-trading-policy 200
16727601-rapid-eod-25k-a-comprehensive-look 200
17035331 200
17036130-builder-plan-25k-a-comprehensive-look 200
9698984-2-price-limit-rule 200
1249126                                                            (bytes after `sips -Z 1600`)
52b35494335027234e7bf0578686b323c1f2c16e2807312e86f2eaa8f78a7ac5  (committed PNG)
32:Ensuring no open positions or orders are active in the order book 2 minutes before and after any data release.
33:These protocols apply to all news releases.
150:News trading is not allowed on this Sim Funded account. ​
199:URL: https://help.myfundedfutures.com/en/articles/17035331-builder-plan-150k-comprehensive-guide
332:T1 news trading is allowed during the Evaluation and Sim Funded stages. You may open and hold positions through any scheduled T1 news event without limitation.
484:News trading is fully unrestricted during the evaluation and sim funded stage. You may open and hold positions through any scheduled news event without limitation.
544:Equity Products ES, MES, NQ, MNQ, RTY, M2K, YM, and MYM overnight price limits have increased to 5%, which is 2% below the CME limit of 7%. Consequently, trading is suspended at MyFunded Futures.
```
The image URL is a signed Intercom CDN link (`downloads.intercomcdn.com/i/o/q04ao2hz/1920835709/…`), taken from W4's `img/urls.txt`. "09:18:32" is the `date -u` printed immediately before the curl.

**E4 — T1 calendar image, read by the manager with the Read tool (transcription of the banner and footer).** "Trading during these news events is strictly prohibited on sim funded accounts 2 minutes before and after the event. For example, if the news is at 2:00, all trades open prior to 1:58 should be liquidated. New trades should be opened until 2:02." (sic) … "ALL LISTED TIMES ARE EASTERN STANDARD TIME (EST) TIME ZONE." The 2026 rows show Employment Report and CPI at 8:30 AM, and FOMC Meeting and FOMC Minutes at 2:00 PM. Examples: Jul 02 Employment 8:30 AM, Jul 14 CPI 8:30 AM, Jul 29 FOMC Meeting 2:00 PM. There is no FOMC Meeting row in October, while the Fed page lists 2026-10-28 (E7).

**E5 — data file and bar structure (W3's block, labelled as W3's; sha and line count re-run by W5 with matching output).**
```
-rw-r--r--@ 1 admin  staff  95900139 Jul 23 13:02 /Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt
307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454  (matches expected)
 1857362
20210307 180100;16120.5;16167;16120.5;16154.75;17
20260720 112700;29005.5;29020.75;29003.5;29016;308
| 2022-06-14 | 180100 / 235900 / 359 | 2022-06-15 | 000000 / 093000 / 571 |
| 2024-06-11 | 180100 / 235900 / 359 | 2024-06-12 | 000000 / 093000 / 571 |
| 2026-06-09 | 180100 / 235900 / 359 | 2026-06-10 | 000000 / 093000 / 571 |
20240612 083000;21511.5;21555.5;21507;21522.5;909
20240612 083100;21541.5;21702.25;21522.5;21665.5;6624
20240612 140000;21763.5;21764.5;21757.25;21761.25;423
20240612 140100;21762;21763.5;21692;21729;6321
```
Manager re-run: `/usr/bin/grep -c -E '^[0-9]{8} 083[01]00;' <file>` → `2712`. W5 pasted the thin 18:05 bar: `20240611 180500;…;29`.

**E6 — paper abstracts (manager re-fetch).**
```
FETCH 2026-11-09T09:27:41Z 200 https://ideas.repec.org/a/eee/jfinec/v145y2022i3p909-936.html
We find large overnight returns with no abnormal variance before nonfarm payrolls, ISM, and GDP announcements, similar to the pre-FOMC returns.
FETCH 2026-11-09T09:27:42Z 200 https://ideas.repec.org/a/cup/jfinqa/v48y2013i02p343-375_00.html
The average announcement-day excess return from 1958 to 2009 is 11.4 basis points (bp) versus 1.
FETCH 2026-11-09T09:27:42Z 200 https://ideas.repec.org/a/eee/jfinec/v113y2014i2p171-201.html
In addition to significantly higher average returns for risky assets on announcement days, return patterns are much easier to reconcile with standard asset pricing theories, both cross-sectionally and over time.
crossref 200
Macroeconomic Announcement Premium | [[2024, 5, 22]]
During the period 1961–2023, roughly 44 days per year with macroeconomic announcements account for more than 71% of the aggregate equity market risk compensation.
```
(The Savor–Wilson 2013 line is cut at "1." by the extraction regex. W2a's full abstract text, labelled as W2a's, continues "1.1 bp for all the other days, suggesting that over 60% of the cumulative annual equity risk premium is earned on announcement days.") DOIs, as W2a reported them from Crossref: Hu et al. 10.1016/j.jfineco.2021.09.015; Savor–Wilson 2013 10.1017/s002210901300015x; 2014 10.1016/j.jfineco.2014.04.005; Ai–Bansal–Guo 10.1093/acrefore/9780190625979.013.912.

**E7 — calendars (manager re-run of W2b's script on W2b's fetched files; W2b's fetch log is W2b's).**
```
year FOMC CPI(ALFRED) EMP(ALFRED) union
2021 7 10 9 26
2022 8 13 12 33
2023 8 13 12 33
2024 8 13 14 34
2025 8 11 11 30
2026 4 7 7 18
total 43 67 65 174
   1 For release at 10:00 a.m. EDT
  35 For release at 2:00 p.m. EDT
  12 For release at 2:00 p.m. EST
20260128 20260318 20260429 20260617 20260729 20260916 20261028
```
W2b's reported statuses (W2b's): fomccalendars.htm 200; alfred.stlouisfed.org/release?rid=10 and rid=50 200; bls.gov/schedule/news_release/cpi.htm **403** ("Access Denied").

**E8 — event counts, bar presence, inactivity gaps, early-close event days (manager script `/tmp/r6-mgr/bin/ev.py`, using `scripts/wf/sessions.py` build_calendar read-only).**
```
OOS span 2022-03-17 2026-06-05
FOMC in_range 43 on_session 42 prev_evening_1805_bar 42 exit_bar 135500 42 in_OOS 33 per_OOS_window min/med/max 1 2 2
CPI in_range 67 on_session 63 prev_evening_1805_bar 61 exit_bar 082500 63 in_OOS 50 per_OOS_window min/med/max 2 3 4
EMP in_range 65 on_session 61 prev_evening_1805_bar 61 exit_bar 082500 61 in_OOS 49 per_OOS_window min/med/max 2 3 4
union in_range 174 union in_OOS(on session) 131 max gap days 37 gaps>7 90 of 173
per-year union {2021: 26, 2022: 33, 2023: 33, 2024: 34, 2025: 30, 2026: 18}
event days whose data ends before 16:00: [('2021-04-02', '091500'), ('2023-04-07', '091500'), ('2026-04-03', '091500')]
```

**E9 — line pointers used in the design (manager re-run).**
```
docs/specs/2026-11-06-walk-forward-values.md:125:  4. ≥ 250 aggregate OOS trades
docs/specs/2026-11-06-walk-forward-values.md:126:  5. ≥ 60% of walk-forward windows profitable
docs/specs/2026-11-05-phase3-build-specification.md:100:4. Session time gate — clock hits 11:30 ET → close positions, disable until next session
docs/specs/2026-11-05-phase3-build-specification.md:101:5. Afternoon session window — clock enters 3:00–6:00 PM ET → disable everything
DECISIONS.md:1576:    - Macroeconomic Announcement-Day Premium (Savor–Wilson; Ai 2024).
```

**E10 — S13 count, file list, staged diff (taken after the last edit):** see Files staged.

## Adversarial findings

**W4 (against Part A), `GRADE: CONTRADICTED`.**
- R1, T1 scope: contradicted. The image banner covers all Sim Funded accounts, the Builder pages allow T1 in Sim Funded, and the "any data release" protocol line also applies. Re-verified by the manager (E3, E4). Part A item 1 now reports the conflict, and the design's constraint (i) takes the strictest reading [D1].
- R2, overnight: narrowed. No nightly cut-off and no 17:00 CT reset were found. "Overnight" is undefined, and the Simulated Trader Agreement is not public (UNVERIFIED).
- R3: not contradicted.
- R4: narrowed. Pro One-Day has no consistency rule. Inactivity applies to one-time-payment accounts from 2026-08-25. W4 also cited a Pro "Consistent Trading Policy" that the design does not yet test (noted, OPEN under OPEN-5's F4 channel).

**W5 (against design v1), `GRADE: DEFECTS FOUND`.** Disposition in v2:
1. 1F held through a same-day 08:30 CPI. Fixed: earlier-release override (§1).
2. Rule (ii) adopted but not applied. Fixed: (ii) is scoped to 08:30-and-later US releases, and 1F/2S carry OPEN-4.
3. FOMC exit not rule-based. Fixed: variants 1N/1C/1F, each with one exit.
4. Report empty. Fixed: E1-E9 now carry the output.
5. "BLOCKED" overstated. Fixed: blocked on Rapid/Pro Sim Funded with quotes; Builder conflict stated; strictest reading labelled [D1].
6. No early-close rule. Fixed: skip rule plus E8 list.
7. Unlabelled acceptance measures. Fixed: labelled [D1], with D6 Decisions 4/5 cited.
8. Intraday trailing measure wrong. Fixed: peak on unrealised highs, worst-case bar order.
9. "Overnight" quote truncated. Fixed: full gloss quoted, OPEN-1 downgraded to residual.
10. Missed MFFU conditions. Fixed: 2% price limit, low-volume rule (OPEN-5), Builder Soft DLL and hedging added.
11. EST/EDT. Fixed: Time zone [D1].
12. FOMC Minutes source. Fixed: §3 row (dates listed on the Fed page, not yet extracted).
13. Wrong bar checked. Fixed: E8 re-run on the 18:05 bar (42/61/61, unchanged).
14. Pointer :1567-1580. Fixed to :1566-1582. The image time is kept as the `date -u` before the curl (E3).
15. D1 label wording. Kept the master's brief wording; the :1908 wording is noted in the design header.

## S6 cross-block check

Design §7 names every touched block: OPEN-1 (MFFU "overnight", F4 channel); OPEN-2 (F2 FROZEN; breakers #4 and #5 vs 1F/2A/2S, with 1N/1C clear of both); OPEN-3 (A7 gate 4 ≥ 250 OOS trades cannot be met: 1N ≤ 49, all PAD-E ≤ 131 OOS events, E8); OPEN-4 (non-T1 releases); OPEN-5 (MFFU low-volume rule); F3 (standing limitation carried); O4 (first pass without breakers [D1]); A14/hedging (standalone first pass [D1]); A5 (MFFU session as the day [D1]); R-1104-3 (nothing bought). Nothing in F1-F4 or O1-O4 is modified.

## Decisions taken under D-2026-11-08-D D1 (each: decided by manager under D-2026-11-08-D D1, changeable by Amear)

1. Worktree at `/Users/admin/Praxis.build-r6` instead of `/Volumes/Sensidine/Praxis.build-r6`, because the filesystem denied the brief's path (E1). Branch and base are as briefed. **S4 gap:** this deviation has no DECISIONS.md entry. This unit edits no ledger, so the master is to file one.
2. Strictest-reading constraint set (i)-(iv), and the MFFU "EST" read as US Eastern local time.
3. Builder Sim Funded is treated as T1-restricted despite the Builder guides.
4. Variants 1N (core), 1C (CPI extension, not in the abstract) and 1F; ISM/GDP excluded (no free source verified).
5. "Ai 2024" taken as Ai, Bansal & Guo (2024, Oxford Research Encyclopedia).
6. Split variant 2S as the deployable ADP form; 2A as a benchmark only.
7. Qualification measures in design §5 (OOS-span net, VS4 judged per tier row, intraday trailing on unrealised highs, inactivity judged standalone then overlay, no keep-alive trades).
8. First pass: Python event simulator, no breakers, each variant standalone; 20:00 entry and 4-tick sensitivity rows.
9. Event confirmation by the T+1 volume/range spike, with doubled ALFRED dates resolved the same way.

## D2 items

None. No purchase was needed: FOMC (Fed) and CPI/NFP (ALFRED) dates are free. BLS refused curl, ISM/GDP history was not sourced, and both were excluded rather than bought.

## Files staged

Created (10): the report, the design, and eight evidence files under docs/reports/evidence/ (six W1 text captures, the manager's adversarial.txt, the T1 PNG). Changed (1): MANIFEST.md, 10 rows appended at the end, no existing line changed. All staged in the worktree index; nothing committed.

`git -C /Users/admin/Praxis.build-r6 status --porcelain` (after the last edit):
```
M  MANIFEST.md
A  docs/reports/2026-11-09-r6-step1-manager.md
A  docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-news.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-plans.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-t1-calendar-2026.png
A  docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt
A  docs/specs/2026-11-09-r6-announcement-research-design.md
```

`wc -l` of each file (after the last edit):
```
     316 MANIFEST.md
     314 docs/reports/2026-11-09-r6-step1-manager.md
     123 docs/specs/2026-11-09-r6-announcement-research-design.md
     573 docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt
     155 docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt
     515 docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt
     117 docs/reports/evidence/2026-11-09-r6-mffu-news.txt
    1291 docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt
     964 docs/reports/evidence/2026-11-09-r6-mffu-plans.txt
    1117 docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt
    4660 docs/reports/evidence/2026-11-09-r6-mffu-t1-calendar-2026.png
   10145 total
```

`git -C /Users/admin/Praxis.build-r6 diff --cached --stat` (after the last edit, staged):
```
 MANIFEST.md                                        |   10 +
 docs/reports/2026-11-09-r6-step1-manager.md        |  314 +++++
 .../evidence/2026-11-09-r6-mffu-adversarial.txt    |  573 +++++++++
 .../evidence/2026-11-09-r6-mffu-consistency.txt    |  155 +++
 .../evidence/2026-11-09-r6-mffu-drawdown.txt       |  515 ++++++++
 docs/reports/evidence/2026-11-09-r6-mffu-news.txt  |  117 ++
 .../evidence/2026-11-09-r6-mffu-plans-site.txt     | 1291 ++++++++++++++++++++
 docs/reports/evidence/2026-11-09-r6-mffu-plans.txt |  964 +++++++++++++++
 .../2026-11-09-r6-mffu-t1-calendar-2026.png        |  Bin 0 -> 1249126 bytes
 .../evidence/2026-11-09-r6-mffu-trading-day.txt    | 1117 +++++++++++++++++
 .../2026-11-09-r6-announcement-research-design.md  |  123 ++
 11 files changed, 5179 insertions(+)
```

S13 count, `grep -c` of the standing limitation sentence, and the count of lines in this report holding any of the three words the brief bars (`grep -ciE` over the three, case-insensitive; pattern held in a shell variable so it is not written here):
```
report: 1
design: 1
barred-word lines in report: 0
```

## Result

Result: PASS at level WRITTEN. Part A's four questions are answered from MFFU text fetched in this unit: three OBSERVED, and the evening-entry/trading-day question UNVERIFIED (ambiguous), stated plainly. The announcement-day hold is BLOCKED on Rapid/Pro Sim Funded, with quotes. The design is written with S6 conflicts named, and two adversaries were run. Limits on this PASS: the design's second version was not re-attacked by a fresh adversary; one S4 gap (the worktree-path deviation has no DECISIONS.md entry) is routed to the master; OPEN-1..OPEN-5 remain open. Nothing is implemented or tested.

## Correction 1 (unit 2026-11-09-r6-step1-correction-1)

Bead `Praxis_build-ckh`. Cause: the independent audit of this report found one MAJOR defect under S2 (line 7 and line 65 said MFFU allows the evening entry, unqualified, while item 2 grades that question UNVERIFIED) and four MINOR defects M1-M4. Lines 1-314 above are not edited; this section supersedes the statements listed in C2. Rubric criteria addressed: S2 (MAJOR, M2, M3), S4 (M1), S1 (M3 grep pasted; M4 disclosure of evidence inputs outside the diff), S13 (count kept at one per file, C7). Workers dispatched for this correction: one ADVERSARIAL praxis-worker after the final evidence (its grade line is in C8). Lessons for the master are in C6, not in agent memory.

### C1. For Amear (plain English) — supersedes line 7

The evening trade passes MFFU's news rule on every account. You buy in the evening and sell five minutes before the 08:30 release, so you are already flat when the two-minute news window starts. The trade also stays inside one MFFU session, which runs 6 PM to 4:10 PM. What is not settled is whether MFFU counts an evening buy as "holding overnight". MFFU's pages do not say. One Rapid page says "Holding overnight will breach the account." A written answer from MFFU is needed before any funded use. The flat time is 4:10 PM ET. The 16:59 time appears in none of the MFFU pages saved in this unit. Holding through the release is blocked on Rapid and Pro sim-funded accounts: MFFU requires being flat two minutes either side of CPI, jobs, FOMC and FOMC-minutes releases. MFFU's own pages disagree about Builder. A split version that steps out around each release is specified instead. Two problems show up before any backtest. First, these events give about 30 trades a year, so the walk-forward's 250-trade gate cannot be met. Second, gaps between events often run past MFFU's 7-day inactivity limit. Both are recorded as open items. Nothing was bought, built or run.

### C2. Superseded statements (quoted exactly; each quote is prefixed "> ")

1. Line 7, whole line:
> MFFU's current rules allow the pre-announcement trade as R6 describes it: buy in the evening, sell five minutes before the 08:30 release. That stays inside one MFFU session, which runs 6 PM to 4:10 PM. The flat time is 4:10 PM; 16:59 appears nowhere. The announcement-day hold through the release is blocked on Rapid and Pro funded accounts: MFFU requires being flat two minutes either side of CPI, jobs, FOMC and FOMC-minutes releases. MFFU's own pages disagree about Builder. A split version that steps out around each release is specified instead. Two problems surface before any backtest. First, these events give about 30 trades a year, so the walk-forward's 250-trade gate cannot be met. Second, gaps between events often exceed MFFU's 7-day inactivity limit. Both are recorded as open items. Nothing was bought, built or run.

   Corrected text: the C1 paragraph above.

2. Line 65, whole line:
> - **Pre-Announcement Drift as R6 describes it** (evening entry, exit before the release): ALLOWED by MFFU's current text on every account. Residual risk: the word "overnight" (OPEN-1).

   Corrected text:
> - **Pre-Announcement Drift as R6 describes it** (evening entry, exit before the release): ALLOWED by the T1 news rule on every account; whether the evening entry counts as holding overnight is UNVERIFIED (OPEN-1). A written MFFU answer is needed before any funded use (design line 110).

3. Line 15, the S4 part only:
> S4 (one gap, see Decisions item 1)

   Corrected text:
> S4 (no gap: the worktree path departs from the master's brief, not from R7, which names no path, so no DECISIONS.md entry is needed; master ruling DECISION_LOG 2026-11-09T09:40:00Z, decided by master under D-2026-11-08-D D1, changeable by Amear)

4. Line 240, the "S4 gap" sentence and the sentence that depends on it:
> **S4 gap:** this deviation has no DECISIONS.md entry. This unit edits no ledger, so the master is to file one.

   Corrected text:
> Not an S4 gap. The path departs from the master's brief, not from R7 (R7 names no path), so no DECISIONS.md entry is needed. Master ruling, DECISION_LOG 2026-11-09T09:40:00Z: decided by master under D-2026-11-08-D D1, changeable by Amear.

   The rest of line 240 (the path, the reason, "Branch and base are as briefed") stands. The ruling as it sits in the main working tree's DECISION_LOG.md (that file is not in this worktree's diff), `/usr/bin/grep -n -o` output:
```
753:Decided by master under D-2026-11-08-D D1** (changeable by Amear): (1) the worktree path is a departure from the master's brief, not from R7 (R7 names no path), so no DECISIONS.md entry is needed
```

5. Line 57, whole line:
>    - 16:59 is not in any fetched page (W1 and W4 both report zero hits; W4's liveness: `4:10` matched on several pages). The 16:59 figure came from the external D8 document (strategy-filter audit :171).

   Corrected text:
> - 16:59 (and 4:59) has zero hits in the seven committed capture files `docs/reports/evidence/2026-11-09-r6-mffu-*.txt`, which hold 27 page blocks (C3). Control: `4:10` hits 8 lines in the same files, all in trading-day.txt (C3). REPORTED BY workers W1 and W4, not re-run on the committed files: zero hits across the 77 help articles and 4 plan pages they read, and W4's own `4:10` control. The 16:59 figure came from the external D8 document (strategy-filter audit :171).

6. Line 314, the Result line:
> Result: PASS at level WRITTEN. Part A's four questions are answered from MFFU text fetched in this unit: three OBSERVED, and the evening-entry/trading-day question UNVERIFIED (ambiguous), stated plainly. The announcement-day hold is BLOCKED on Rapid/Pro Sim Funded, with quotes. The design is written with S6 conflicts named, and two adversaries were run. Limits on this PASS: the design's second version was not re-attacked by a fresh adversary; one S4 gap (the worktree-path deviation has no DECISIONS.md entry) is routed to the master; OPEN-1..OPEN-5 remain open. Nothing is implemented or tested.

   Corrected text: the Result line at the end of this correction. Its "one S4 gap ... routed to the master" clause is withdrawn per item 4.

Read in the light of C1 (not edited, not superseded in wording): line 226's "OPEN-1 downgraded to residual" describes the v1-to-v2 change only. After this correction OPEN-1 is an UNVERIFIED question that gates funded use, not a residual. Lines 51-54 (item 2, graded UNVERIFIED) already state this and stand.

### C3. M3 grep on the committed captures

The brief's command (the shell `grep` here is a wrapper function, so the same count is repeated with `/usr/bin/grep`):
```
$ grep -c '16:59\|4:59' docs/reports/evidence/2026-11-09-r6-mffu-*.txt
docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-news.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-plans.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt:0
exit=1
$ grep -c '4:10' docs/reports/evidence/2026-11-09-r6-mffu-*.txt
docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-plans.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-news.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt:8
exit=0
```
`/usr/bin/grep -c '16:59\|4:59'` on the same files gave 0 for each of the seven, and `/usr/bin/grep -c '^URL:'` (page blocks per file) gave:
```
docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt:5
docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt:4
docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt:5
docs/reports/evidence/2026-11-09-r6-mffu-news.txt:2
docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt:4
docs/reports/evidence/2026-11-09-r6-mffu-plans.txt:3
docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt:4
```
Total 27 page blocks committed, against the 77 + 4 pages W1 reports reading (line 21). The zero-hit claim is OBSERVED for the 27 committed pages only.

### C4. M4 disclosure — evidence inputs outside the diff

No file is added by this correction. These E-blocks rest on inputs that are not in the staged diff, so they cannot be reproduced from the diff alone:
- E3: W4's image URL list, `/tmp/r6-w4/img/urls.txt`, is no longer present (`ls` below). The original, pre-downscale PNG (sha `3ab6c6d9…`) is not committed; only the downscaled PNG is. The raw HTML of the five contradiction pages is in `/tmp/r6-mgr/raw/` (`8230009.html`, `16727601.html`, `17035331.html`, `17036130.html`, `9698984.html`); their extracted text is in the committed adversarial.txt.
- E5: W3's block (W3 scratch `/tmp/r6-w3/n.py`) and W5's matching re-run (in W5's return, not in a file); the data file `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt`, outside the repo.
- E6: the manager's re-fetched pages in `/tmp/r6-mgr/raw/` (`v145y2022i3p909-936.html`, `v48y2013i02p343-375_00.html`, `v113y2014i2p171-201.html`, `ai.json`); W2a's full abstract text and DOIs (W2a's return; scratch `/tmp/r6-w2a/`).
- E7: W2b's script in `/tmp/r6-w2b/bin/` (`count.py`, `txt.py`) run on W2b's fetched files in `/tmp/r6-w2b/raw/`; W2b's fetch statuses are W2b's.
- E8: the manager's script `/tmp/r6-mgr/bin/ev.py`, which reads `/tmp/r6-w2b/raw/fomc_st_dates.txt`, `alfrel10.dates`, `alfrel50.dates`, the data file above, and `scripts/wf/sessions.py` (in the tree at `f10603a`, not changed by this unit).
- E1 is session command output with no file behind it. E2, E4 and E9 rest only on files in the tree at `f10603a` or in the staged diff.

```
ls: /tmp/r6-w4/img/urls.txt: No such file or directory
-rw-r--r--@ 1 admin  staff  95900139 Jul 23 13:02 /Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt
-rw-r--r--@ 1 admin  wheel      2365 Nov  9 04:27 /tmp/r6-mgr/bin/ev.py
-rw-r--r--@ 1 admin  wheel     36024 Nov  9 04:27 /tmp/r6-mgr/raw/ai.json
-rw-r--r--@ 1 admin  wheel      1182 Nov  9 04:17 /tmp/r6-w2b/bin/count.py
-rw-r--r--@ 1 admin  wheel       737 Nov  9 04:17 /tmp/r6-w2b/raw/alfrel10.dates
-rw-r--r--@ 1 admin  wheel       715 Nov  9 04:17 /tmp/r6-w2b/raw/alfrel50.dates
-rw-r--r--@ 1 admin  wheel       432 Nov  9 04:16 /tmp/r6-w2b/raw/fomc_st_dates.txt
scripts/wf/sessions.py
sessions_py_unchanged_in_index
```
`/tmp` is not durable. If these files are cleared, E3 and E5-E8 stand as pasted output only.

### C5. Design check (step 2)

`/usr/bin/grep -n -i 'allow'` and `/usr/bin/grep -n -i 'overnight'` on the design, before the edit (cut to 220 characters):
```
14:| T1 news rule | T1 = "FOMC Meetings, FOMC Minutes, Employment Report, CPI" (news.txt:38). Flat from 2 minutes before to 2 minutes after (news.txt:27-28). The policy text restricts "Rapid Sim Funded" and "Pro Sim Fund
28:- **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWED by the T1 rule on every account (exit at T−5). Inside one MFFU session (18:00 → 16:10). Residual risk: the word "overnight" is 
29:- **Strategy 2, Announcement-Day Premium, holding through the release:** **BLOCKED BY MFFU RULE on Rapid Sim Funded and Pro Sim Funded.** Quotes: "Restricted Accounts: Trading on T1 News events is prohibited for the f
52:- Low-volume hours: "Profiting from isolated, stale or unrealistic fills … during low-volume hours is not allowed" (news.txt:86). The 18:05 bar can be thin (volume 29 on 2024-06-11, E5). The first pass reports a 20:00
---
15:| Evening entry vs trading day | "Trades may be placed beginning at 6:00 PM EST when the Globex session opens and can remain open until the New York session closes at 4:10 PM EST" (trading-day.txt:10). An entry after 
25:- (iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED).
28:- **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWED by the T1 rule on every account (exit at T−5). Inside one MFFU session (18:00 → 16:10). Residual risk: the word "overnight" is 
33:**Source (paper's claim).** Hu, Pan, Wang & Zhu, "Premium for heightened uncertainty: Explaining pre-announcement market returns", JFE 145(3):909-936 (2022), DOI 10.1016/j.jfineco.2021.09.015. Abstract (IDEAS/RePEc, E
51:- 2% price-limit rule, Sim Funded and Live: "overnight price limits have increased to 5% … Consequently, trading is suspended" (adversarial.txt:544). The backtest flags every event night whose move from the prior sett
110:| OPEN-1 | MFFU terms (F4 channel, owner Amear) | "Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an
```
One line fixed in place: line 28. It said the evening entry is ALLOWED with only a "residual risk" that "overnight" is not defined, and it carried no UNVERIFIED grade and no need for a written answer. It now carries both. No line was added or removed. `diff` of the staged design before the edit against the file after it, and `wc -l`:
```
     123 docs/specs/2026-11-09-r6-announcement-research-design.md
28c28
< - **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWED by the T1 rule on every account (exit at T−5). Inside one MFFU session (18:00 → 16:10). Residual risk: the word "overnight" is not defined by MFFU in so many words (OPEN-1).
---
> - **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWED by the T1 rule on every account (exit at T−5). Inside one MFFU session (18:00 → 16:10). Whether MFFU counts the evening entry as holding overnight is UNVERIFIED: MFFU's pages do not say, and a Rapid page says "Holding overnight will breach the account." (plans-site.txt:24). A written MFFU answer is needed before any funded use (OPEN-1).
diff_exit=1
24:A: No. Rapid is intended for intraday futures trading. All positions must be closed before the daily session close. Holding overnight will breach the account.
288:No. Rapid is intended for intraday futures trading. All positions must be closed before the daily session close. Holding overnight will breach the account.
```
(The last two lines are `/usr/bin/grep -n` of the quoted sentence in plans-site.txt, confirming the citation.)

Left as they are: line 15 (graded UNVERIFIED for "same trading day"); line 25 (the design's own constraint (iv), labelled INFERRED, not a claim about what MFFU allows); line 110 (OPEN-1, which already says "A written MFFU answer is needed before any funded use"). Not edited, outside step 2's scope: design line 16, "No 16:59 rule on any page fetched.", has the same width as report line 57. Its support is what corrected line 57 states in C2 item 5: OBSERVED for the 27 committed pages, REPORTED BY W1 and W4 for the rest.

### C6. Notes for the master

- The design blob changed (line 28), so the tree sha and canonical sha in the master's 09:40Z row no longer hold for the staged index; the master re-measures.
- Lesson: a plain-English headline must carry the weakest grade of any item it summarises. Line 7 summarised item 2 (UNVERIFIED) as "allow".
- Lesson: "not in any fetched page" must say which pages. The committed captures (27 page blocks) are fewer than the pages workers read (81).

### C7. Final evidence (taken after the last edit)

BEFORE the edit, on the staged report blob (run at the start of this correction):
```
$ git -C /Users/admin/Praxis.build-r6 show :docs/reports/2026-11-09-r6-step1-manager.md | openssl dgst -sha256
SHA2-256(stdin)= 849fa486f677159b30bcba49d2437f1332bd8305daded2587663f6277a47856a
```
AFTER the last edit and re-stage (`zsh /tmp/r6-c1/fe.sh`; each command is echoed before its output):
```
$ date -u
Mon Nov  9 09:41:49 UTC 2026
$ git -C /Users/admin/Praxis.build-r6 status --porcelain
M  MANIFEST.md
A  docs/reports/2026-11-09-r6-step1-manager.md
A  docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-news.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-plans.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-t1-calendar-2026.png
A  docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt
A  docs/specs/2026-11-09-r6-announcement-research-design.md
$ git -C /Users/admin/Praxis.build-r6 diff --stat   (work tree vs index; empty = nothing unstaged)
$ git -C /Users/admin/Praxis.build-r6 diff --cached --stat
 MANIFEST.md                                        |   10 +
 docs/reports/2026-11-09-r6-step1-manager.md        |  461 +++++++
 .../evidence/2026-11-09-r6-mffu-adversarial.txt    |  573 +++++++++
 .../evidence/2026-11-09-r6-mffu-consistency.txt    |  155 +++
 .../evidence/2026-11-09-r6-mffu-drawdown.txt       |  515 ++++++++
 docs/reports/evidence/2026-11-09-r6-mffu-news.txt  |  117 ++
 .../evidence/2026-11-09-r6-mffu-plans-site.txt     | 1291 ++++++++++++++++++++
 docs/reports/evidence/2026-11-09-r6-mffu-plans.txt |  964 +++++++++++++++
 .../2026-11-09-r6-mffu-t1-calendar-2026.png        |  Bin 0 -> 1249126 bytes
 .../evidence/2026-11-09-r6-mffu-trading-day.txt    | 1117 +++++++++++++++++
 .../2026-11-09-r6-announcement-research-design.md  |  123 ++
 11 files changed, 5326 insertions(+)
$ wc -l <every staged file except the report>
     316 MANIFEST.md
     123 docs/specs/2026-11-09-r6-announcement-research-design.md
     573 docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt
     155 docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt
     515 docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt
     117 docs/reports/evidence/2026-11-09-r6-mffu-news.txt
    1291 docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt
     964 docs/reports/evidence/2026-11-09-r6-mffu-plans.txt
    1117 docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt
    4660 docs/reports/evidence/2026-11-09-r6-mffu-t1-calendar-2026.png
    9831 total
$ git -C /Users/admin/Praxis.build-r6 show :MANIFEST.md | head -n 306 | cmp - <(git -C /Users/admin/Praxis.build-r6 show f10603a:MANIFEST.md) && echo HEAD306_IDENTICAL
HEAD306_IDENTICAL
$ git show :docs/specs/2026-11-09-r6-announcement-research-design.md | diff /tmp/r6-c1/design.pre - | cut -c1-90   (design.pre = the design blob staged before this correction)
28c28
< - **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWE
---
> - **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWE
diff_exit=1
$ grep -cF '<the standing limitation sentence>' on the staged report blob and the staged design blob
report: 1
design: 1
$ grep -ciE '<the three barred words, held in a variable>' on the staged report blob
barred-word lines in report: 0
$ grep -cw '<the placeholder token, bracketed>' on the staged report blob
placeholder lines in report: 0
$ git show :docs/reports/2026-11-09-r6-step1-manager.md | head -n 314 | openssl dgst -sha256   (lines 1-314 after the edit; staged blob)
SHA2-256(stdin)= 849fa486f677159b30bcba49d2437f1332bd8305daded2587663f6277a47856a
$ head -n 314 docs/reports/2026-11-09-r6-step1-manager.md | openssl dgst -sha256   (work tree)
SHA2-256(stdin)= 849fa486f677159b30bcba49d2437f1332bd8305daded2587663f6277a47856a
```
The two lines-1-314 hashes AFTER equal the BEFORE hash, so lines 1-314 are byte-identical.

The report's own line count and diff-stat line are not self-measured; the earlier Files staged section (:254–310) is SUPERSEDED for the report's own figures and for the total; the master and auditor measure them.

Values in the earlier Files staged section, against this capture: unchanged are the status list (same 11 paths, same codes), MANIFEST.md 316, the design 123, all seven evidence .txt counts, the PNG (4660 by `wc -l`, Bin 1249126 bytes), every diff-stat line except the report's, the S13 counts (report 1, design 1) and barred-word lines 0. Changed: the report's own figures (line count and diff-stat line) and both totals (`wc -l` total and the diff-stat total line). The design's line count is unchanged, but its content changed at line 28 (C5), so its blob differs from the one the earlier section measured.

### C8. Adversaries on Correction 1, and amendments (appended; supersedes all of C1 and C7, and parts of C4, C5, C6 and line 318)

**Adversary 1** (praxis-worker, ADVERSARIAL, foreground; given the staged report through C7, the staged design, the audit's MAJOR and M1-M4, S2, and the Result line then planned). Its grade line:
```
GRADE: DEFECTS FOUND (1 MAJOR, 5 MINOR)
```
Its clean checks, REPORTED BY adversary 1: lines 1-314 hash equal to the BEFORE hash; the four whole-line quotes in C2 byte-equal to the originals (`cmp`); design diff `28c28`, 123 lines; C3 counts and the 27 page blocks reproduce; C7 reproduces except the report's own diff-stat line; the `ev.py` inputs match C4; the DECISION_LOG :753 grep reproduces.

Findings and disposition:
1. MAJOR (S2). The ADP variants 2A and 2S also enter at the 18:05 bar on E−1, so the overnight question applies to them. The design and the report still called them allowed, compliant or deployable with no OPEN-1 caveat: design lines 29 and 64, report lines 66 and 245, MANIFEST.md line 308. C5's grep searched only `allow` and `overnight`. Fixed: design lines 29 and 64 in place (A4); report lines 66 and 245 superseded (A1, A2). Not fixed: MANIFEST.md line 308 ("2S (split, MFFU-compliant)"), because this unit is barred from any MANIFEST change; routed to the master.
2. MINOR (S1/S2). C4 checked the wrong path for W4's URL list. Fixed by A3.
3. MINOR (M4). C4 did not name `/tmp/r6-mgr/bin/x.py`, the manager's HTML-to-text extractor that produced the page text in the committed adversarial.txt. Fixed by A3.
4. MINOR (S2). Design line 16 still says "No 16:59 rule on any page fetched." and is graded OBSERVED. Not edited: this unit's design scope is the evening-entry statements only. Listed as a limit in the Result line; its support is as C2 item 5 states.
5. MINOR (S2). C1 said "MFFU's news rule", dropping "T1". The 1F variant holds through 10:00 non-T1 releases (OPEN-4). Fixed by C1a.
6. MINOR (S2). The Result line then planned (given to adversary 1 in its brief, not written to the report) said the adversary checked "the correction scope only", omitted design line 16 and the 2A/2S wording, and said PASS while finding 1 stood. Fixed in the Result line below, which is no longer PASS (adversary 2, finding 1).

**C1a. For Amear (plain English) — supersedes C1 and line 7.**

The evening trade passes MFFU's T1 news rule on every account. You buy in the evening and sell five minutes before the 08:30 release, so you are already flat when the two-minute T1 window starts. The trade also stays inside one MFFU session, which runs 6 PM to 4:10 PM. What is not settled is whether MFFU counts an evening buy as "holding overnight". MFFU's pages do not say. One Rapid page says "Holding overnight will breach the account." The same question applies to every version in the design that buys in the evening. A written answer from MFFU is needed before any funded use. The flat time is 4:10 PM ET. The 16:59 time appears in none of the MFFU pages saved in this unit. Holding through the release is blocked on Rapid and Pro sim-funded accounts: MFFU requires being flat two minutes either side of CPI, jobs, FOMC and FOMC-minutes releases. MFFU's own pages disagree about Builder. A split version that steps out around each release is specified instead. Two problems show up before any backtest. First, these events give about 30 trades a year, so the walk-forward's 250-trade gate cannot be met. Second, gaps between events often run past MFFU's 7-day inactivity limit. Both are recorded as open items. Nothing was bought, built or run.

**A1. Line 66, last sentence**, quoted exactly:
> The design specifies a compliant split variant (2S).

Corrected text:
> The design specifies a split variant (2S) that is compliant with the T1 news rule; its evening entry carries the same UNVERIFIED overnight question (OPEN-1).

**A2. Line 245, whole line**, quoted exactly:
> 6. Split variant 2S as the deployable ADP form; 2A as a benchmark only.

Corrected text:
> 6. Split variant 2S as the proposed deployable ADP form, subject to OPEN-1 (the UNVERIFIED overnight question); 2A as a benchmark only.

**A3. C4, first E3 sentence** (line 405), quoted exactly:
> W4's image URL list, `/tmp/r6-w4/img/urls.txt`, is no longer present (`ls` below).

Corrected text:
> W4's image URL list is at `/tmp/r6-w4/raw/img/urls.txt` (present; the `ls` in C4 checked a wrong path). A byte-identical copy (same sha) of the original pre-downscale PNG, fetched earlier by W4 (file time 04:14 local, 09:14Z), is at `/tmp/r6-w4/raw/img/t1_1.png`; the manager's own 09:18:32Z fetch is not kept, and neither is committed. E3's page text was produced by the manager's extractor `/tmp/r6-mgr/bin/x.py` from the raw HTML in `/tmp/r6-mgr/raw/`.

```
$ ls -l /tmp/r6-w4/raw/img/urls.txt /tmp/r6-w4/raw/img/t1_1.png /tmp/r6-mgr/bin/x.py
-rw-r--r--@ 1 admin  wheel      751 Nov  9 04:18 /tmp/r6-mgr/bin/x.py
-rw-r--r--@ 1 admin  wheel  7101784 Nov  9 04:14 /tmp/r6-w4/raw/img/t1_1.png
-rw-r--r--@ 1 admin  wheel      576 Nov  9 04:14 /tmp/r6-w4/raw/img/urls.txt
$ shasum -a 256 /tmp/r6-w4/raw/img/t1_1.png
3ab6c6d941be8c7cd15dd3dd8db0395920eb7b07fde8e819a8c3754b558ce5d4  /tmp/r6-w4/raw/img/t1_1.png
$ /usr/bin/grep -c 'downloads.intercomcdn.com/i/o/q04ao2hz/1920835709/' /tmp/r6-w4/raw/img/urls.txt
1
```
Adversary 1 also reports (REPORTED BY adversary 1, not re-run here) that `x.py` re-run on `9698984.html` matches the committed block apart from blank lines, and that the raw sha matches the block's `RAW_SHA256`.

**A4. C5, "One line fixed in place: line 28"** (line 442) is superseded: three design lines are now fixed in place, 28, 29 and 64. No line was added or removed. The wider grep after the edit, and the full diff, are in C9.

**A5. Line 318, the workers sentence**, quoted exactly:
> Workers dispatched for this correction: one ADVERSARIAL praxis-worker after the final evidence (its grade line is in C8).

Corrected text:
> Workers dispatched for this correction: two ADVERSARIAL praxis-workers, both foreground. Adversary 1 checked the staged report through C7; adversary 2 checked this C8/C9 as a draft before it was appended. Both grade lines are in C8.

**A6. C6, line 459**, the words "The design blob changed (line 28)" are superseded by "The design blob changed (lines 28, 29 and 64)". The rest of that line stands.

**Adversary 2** (praxis-worker, ADVERSARIAL, foreground; given the staged report through C7, this C8 as a draft to be appended verbatim, the staged design, the same criteria, and the Result line then planned). Its grade line:
```
GRADE: DEFECTS FOUND (1 MAJOR, 5 MINOR)
```
Its clean checks, REPORTED BY adversary 2: a synonym search of the report with this draft appended and of the whole design (allow, permit, complian, deploy, meets, satisf, pass, clear, legal, eligible, accept, conform, safe, ok, qualif, fits) found every evening-entry hit superseded or carrying the residual, except MANIFEST.md:308; the A1-A3 quotes and lines 66, 245, 405 and 442 are byte-correct; the design diff is lines 28, 29 and 64 only, 123 lines; `fe.sh` and the A3 commands reproduce.

Findings and disposition:
1. MAJOR (S2). MANIFEST.md line 308, inside this unit's staged diff, still calls 2S "MFFU-compliant" with no OPEN-1 caveat, so a PASS cannot stand. Not fixable here: this unit is barred from any MANIFEST change. The Result is therefore FAIL, and the item is routed to the master. A one-row in-place edit would fix it (for example "2S (split, T1-compliant; evening entry UNVERIFIED overnight, OPEN-1)"); MANIFEST would stay at 316 lines with rows 1-306 untouched. That wording is a suggestion, not applied.
2. MINOR (S2). The planned Result line said the two adversaries "re-ran the evidence blocks". Neither re-ran E5-E8. Fixed in the Result line below.
3. MINOR (S1/S2). Line 318's worker count, C6's "(line 28)" and this section's heading were stale. Fixed by A5, A6 and the heading.
4. MINOR (S1/M4). A3 gave the PNG copy the wrong provenance. Fixed in A3.
5. MINOR (S1). The heading "taken after the last edit" is the brief's wording. The paste of the capture is the only edit after it, and it changes only the report's own figures, which are not self-measured (C9). After the append the manager checks that no fill marker is left (`/usr/bin/grep -c '@[@]'` on the staged report); that figure goes in the return to the master, not here, because writing it would change the file.
6. MINOR (S2, weak). Design line 89 quotes R5's requirement ("survives every MFFU condition") and line 95's flat-by measure rests on the design's INFERRED reading (iv). Neither says MFFU allows the evening entry, so neither is edited (outside this unit's design scope). A pass of the §5 measures would not settle OPEN-1. Listed in the Result's limits.

No third adversary was run on the text after these fixes.

Lessons for the master (in the report, not in agent memory): a correction's over-claim search must include synonyms (`compliant`, `deployable`) and every variant that shares the evening entry, not only the sentence the audit quoted. Draft the correction, adversary-test the draft, then append it once; an append-only report turns every post-adversary fix into another appended layer.

### C9. Final evidence (taken after the last edit) — supersedes C7

AFTER the last edit and re-stage (`zsh /tmp/r6-c1/fe.sh`; each command is echoed before its output):
```
$ date -u
Mon Nov  9 09:55:28 UTC 2026
$ git -C /Users/admin/Praxis.build-r6 status --porcelain
M  MANIFEST.md
A  docs/reports/2026-11-09-r6-step1-manager.md
A  docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-news.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-plans.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-t1-calendar-2026.png
A  docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt
A  docs/specs/2026-11-09-r6-announcement-research-design.md
$ git -C /Users/admin/Praxis.build-r6 diff --stat   (work tree vs index; empty = nothing unstaged)
$ git -C /Users/admin/Praxis.build-r6 diff --cached --stat
 MANIFEST.md                                        |   10 +
 docs/reports/2026-11-09-r6-step1-manager.md        |  536 ++++++++
 .../evidence/2026-11-09-r6-mffu-adversarial.txt    |  573 +++++++++
 .../evidence/2026-11-09-r6-mffu-consistency.txt    |  155 +++
 .../evidence/2026-11-09-r6-mffu-drawdown.txt       |  515 ++++++++
 docs/reports/evidence/2026-11-09-r6-mffu-news.txt  |  117 ++
 .../evidence/2026-11-09-r6-mffu-plans-site.txt     | 1291 ++++++++++++++++++++
 docs/reports/evidence/2026-11-09-r6-mffu-plans.txt |  964 +++++++++++++++
 .../2026-11-09-r6-mffu-t1-calendar-2026.png        |  Bin 0 -> 1249126 bytes
 .../evidence/2026-11-09-r6-mffu-trading-day.txt    | 1117 +++++++++++++++++
 .../2026-11-09-r6-announcement-research-design.md  |  123 ++
 11 files changed, 5401 insertions(+)
$ wc -l <every staged file except the report>
     316 MANIFEST.md
     123 docs/specs/2026-11-09-r6-announcement-research-design.md
     573 docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt
     155 docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt
     515 docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt
     117 docs/reports/evidence/2026-11-09-r6-mffu-news.txt
    1291 docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt
     964 docs/reports/evidence/2026-11-09-r6-mffu-plans.txt
    1117 docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt
    4660 docs/reports/evidence/2026-11-09-r6-mffu-t1-calendar-2026.png
    9831 total
$ git -C /Users/admin/Praxis.build-r6 show :MANIFEST.md | head -n 306 | cmp - <(git -C /Users/admin/Praxis.build-r6 show f10603a:MANIFEST.md) && echo HEAD306_IDENTICAL
HEAD306_IDENTICAL
$ git show :docs/specs/2026-11-09-r6-announcement-research-design.md | diff /tmp/r6-c1/design.pre -   (design.pre = the design blob staged before this correction)
28,29c28,29
< - **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWED by the T1 rule on every account (exit at T−5). Inside one MFFU session (18:00 → 16:10). Residual risk: the word "overnight" is not defined by MFFU in so many words (OPEN-1).
< - **Strategy 2, Announcement-Day Premium, holding through the release:** **BLOCKED BY MFFU RULE on Rapid Sim Funded and Pro Sim Funded.** Quotes: "Restricted Accounts: Trading on T1 News events is prohibited for the following: Rapid Sim Funded / Pro Sim Funded" (news.txt:30-32) and "All positions must be flattened at least two minutes prior to the scheduled T1 News event." (news.txt:28). On Builder Sim Funded, MFFU's text conflicts (image banner vs Builder guides) → treated as blocked under (i) [D1]. Allowed in evaluations, Studio and Live per MFFU's text. The deployable form is the split variant 2S (§2), which is a design change, not the papers' strategy [D1].
---
> - **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWED by the T1 rule on every account (exit at T−5). Inside one MFFU session (18:00 → 16:10). Whether MFFU counts the evening entry as holding overnight is UNVERIFIED: MFFU's pages do not say, and a Rapid page says "Holding overnight will breach the account." (plans-site.txt:24). A written MFFU answer is needed before any funded use (OPEN-1).
> - **Strategy 2, Announcement-Day Premium, holding through the release:** **BLOCKED BY MFFU RULE on Rapid Sim Funded and Pro Sim Funded.** Quotes: "Restricted Accounts: Trading on T1 News events is prohibited for the following: Rapid Sim Funded / Pro Sim Funded" (news.txt:30-32) and "All positions must be flattened at least two minutes prior to the scheduled T1 News event." (news.txt:28). On Builder Sim Funded, MFFU's text conflicts (image banner vs Builder guides) → treated as blocked under (i) [D1]. Allowed by the T1 rule in evaluations, Studio and Live per MFFU's text; its evening entry carries the same UNVERIFIED overnight question as Strategy 1 (OPEN-1). The proposed deployable form, subject to OPEN-1, is the split variant 2S (§2), which is a design change, not the papers' strategy [D1].
64c64
< **2S — split hold, MFFU-compliant [D1; not the papers' strategy].**
---
> **2S — split hold, compliant with the T1 rule; its evening entry carries the UNVERIFIED overnight question (OPEN-1) [D1; not the papers' strategy].**
diff_exit=1
$ git show :docs/specs/2026-11-09-r6-announcement-research-design.md | /usr/bin/grep -n -i 'allow\|overnight\|compliant\|deployable\|permitted' | cut -c1-160
14:| T1 news rule | T1 = "FOMC Meetings, FOMC Minutes, Employment Report, CPI" (news.txt:38). Flat from 2 minutes before to 2 minutes after (news.txt:27-28). Th
15:| Evening entry vs trading day | "Trades may be placed beginning at 6:00 PM EST when the Globex session opens and can remain open until the New York session 
25:- (iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED).
28:- **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWED by the T1 rule on every account (exit at T−5). Inside one MFFU sess
29:- **Strategy 2, Announcement-Day Premium, holding through the release:** **BLOCKED BY MFFU RULE on Rapid Sim Funded and Pro Sim Funded.** Quotes: "Restricted
33:**Source (paper's claim).** Hu, Pan, Wang & Zhu, "Premium for heightened uncertainty: Explaining pre-announcement market returns", JFE 145(3):909-936 (2022),
51:- 2% price-limit rule, Sim Funded and Live: "overnight price limits have increased to 5% … Consequently, trading is suspended" (adversarial.txt:544). The bac
52:- Low-volume hours: "Profiting from isolated, stale or unrealistic fills … during low-volume hours is not allowed" (news.txt:86). The 18:05 bar can be thin (
62:**2A — as published (hold through the release).** Long 1 MNQ from the close of the 18:05 ET bar on E−1 to the close of the 16:05 ET bar on E. BLOCKED BY MFFU
64:**2S — split hold, compliant with the T1 rule; its evening entry carries the UNVERIFIED overnight question (OPEN-1) [D1; not the papers' strategy].**
110:| OPEN-1 | MFFU terms (F4 channel, owner Amear) | "Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an
$ grep -cF '<the standing limitation sentence>' on the staged report blob and the staged design blob
report: 1
design: 1
$ grep -ciE '<the three barred words, held in a variable>' on the staged report blob
barred-word lines in report: 0
$ grep -cw '<the placeholder token, bracketed>' on the staged report blob
placeholder lines in report: 0
$ git show :docs/reports/2026-11-09-r6-step1-manager.md | head -n 314 | openssl dgst -sha256   (lines 1-314 after the edit; staged blob)
SHA2-256(stdin)= 849fa486f677159b30bcba49d2437f1332bd8305daded2587663f6277a47856a
$ head -n 314 docs/reports/2026-11-09-r6-step1-manager.md | openssl dgst -sha256   (work tree)
SHA2-256(stdin)= 849fa486f677159b30bcba49d2437f1332bd8305daded2587663f6277a47856a
```
The two lines-1-314 hashes equal the BEFORE hash in C7 (`849fa486…856a`), so lines 1-314 are byte-identical.

The report's own line count and diff-stat line are not self-measured; the earlier Files staged section (:254–310) is SUPERSEDED for the report's own figures and for the total; the master and auditor measure them.

Against the earlier Files staged section: unchanged are the status list (same 11 paths, same codes), MANIFEST.md 316, the design 123, the seven evidence .txt counts, the PNG (4660 by `wc -l`; Bin 1249126 bytes), every diff-stat line except the report's, the S13 counts (report 1, design 1) and barred-word lines 0. Changed: the report's own figures and both totals. The design's line count is unchanged, but its content changed at lines 28, 29 and 64, so its blob differs from the one the earlier section measured.

Result: FAIL at level WRITTEN. One over-claim of the audited kind remains in the staged diff: MANIFEST.md line 308 calls 2S "MFFU-compliant" without the OPEN-1 caveat, and this unit is barred from changing MANIFEST.md, so the fix is routed to the master (C8, adversary 2 finding 1). Everything else the correction brief asked for is done. Correction 1 supersedes report lines 7, 15 (S4 part), 57, 65, 66 (last sentence), 240 (S4 sentences), 245 and 314, and parts of its own C1, C4, C5, C6 and line 318; it fixes design lines 28, 29 and 64 in place (123 lines kept). The evening entry with exit before the release passes MFFU's T1 news rule on every account; whether an evening entry counts as holding overnight is UNVERIFIED (OPEN-1) for every variant that enters in the evening (1N, 1C, 1F, 2A, 2S), and a written MFFU answer is needed before any funded use. The announcement-day hold is BLOCKED on Rapid/Pro Sim Funded, with quotes. No S4 gap (master ruling 2026-11-09T09:40:00Z). The 16:59 zero-hit claim is OBSERVED for the 27 committed page blocks only. Other limits: design line 16 still says "any page fetched" (not edited, outside this correction's design scope); design lines 89 and 95 do not carry OPEN-1; E3 and E5-E8 rest partly on /tmp and worker files outside the diff (C4, A3); this correction's two adversaries searched the whole staged report and design for the evening-entry over-claim and re-ran C3, the C4/A3 listings and the final-evidence capture, but not E5-E8; no third adversary checked the text after adversary 2's fixes; the design's second version was never re-attacked as a whole by a fresh adversary; OPEN-1 to OPEN-5 remain open. Nothing is implemented or tested.

## Correction 2 (unit 2026-11-09-r6-step1-correction-1b)

Bead `Praxis_build-ckh`. Scope: the edits routed by Correction 1's Result line (:704) and the master's brief for this unit, all in place, no line added or removed in MANIFEST.md or the design. Rubric: S2 (no over-claim; the evening-entry overnight question stays UNVERIFIED, OPEN-1), S1 (pasted output). No worker or adversary was dispatched (master's brief item 6); the master sends this to an independent audit.

Baseline hash of report lines 1-704, taken before this append:
```
$ head -n 704 docs/reports/2026-11-09-r6-step1-manager.md | openssl dgst -sha256
SHA2-256(stdin)= 7ad0a27b562389b7c9145c920a7260f537d5f7c4db693eb7cb86132c0bcc080e
```

### Edit 1. MANIFEST.md line 308 (the design's row)

Old text: "2S (split, MFFU-compliant)". New text: "2S (split; passes the T1 rule; evening-entry overnight question UNVERIFIED, OPEN-1)". Nothing else on the row changed. Rows 307-316 were checked for the same kind of over-claim:
```
$ /usr/bin/grep -niE "compliant|allowed|allow|permitted" MANIFEST.md | awk -F: '$1>=307' | cut -c1-140
310:| /docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt | Evidence | 2 | 2026-11-09 | MFFU help articles 9558251 (permitted times to
```
Line 308 now carries the OPEN-1 caveat. Line 310's "permitted times to trade" is the title of MFFU help article 9558251, not a claim about a variant. Line 307 says the announcement-day hold is BLOCKED and claims nothing is allowed. No other row was edited. Diff of the previously staged MANIFEST.md blob (869cfb7, as Correction 1 left it) against the newly staged blob (3f72380 = `git rev-parse :MANIFEST.md`); `-` is the old line, `+` the new:
```
$ git diff -U0 869cfb7 3f72380
diff --git a/869cfb7 b/3f72380
index 869cfb7..3f72380 100644
--- a/869cfb7
+++ b/3f72380
@@ -308 +308 @@
-| /docs/specs/2026-11-09-r6-announcement-research-design.md | Spec | 2 | 2026-11-09 | R6 research design, PROPOSED, level WRITTEN: Pre-Announcement Drift evening-entry variants 1N/1C/1F and Announcement-Day Premium 2A (benchmark, blocked in Sim Funded) / 2S (split, MFFU-compliant); free event calendars; costs v1.2.0; R5 qualification and A4 per-tier drawdown test; S6 conflicts OPEN-1..5 (incl. gate 4 unreachable, inactivity). |
+| /docs/specs/2026-11-09-r6-announcement-research-design.md | Spec | 2 | 2026-11-09 | R6 research design, PROPOSED, level WRITTEN: Pre-Announcement Drift evening-entry variants 1N/1C/1F and Announcement-Day Premium 2A (benchmark, blocked in Sim Funded) / 2S (split; passes the T1 rule; evening-entry overnight question UNVERIFIED, OPEN-1); free event calendars; costs v1.2.0; R5 qualification and A4 per-tier drawdown test; S6 conflicts OPEN-1..5 (incl. gate 4 unreachable, inactivity). |
```

### Edit 2a and 2b. Design lines 16 and 89

Line 16 (Flat-by time): "No 16:59 rule on any page fetched." is narrowed to the 27 committed page blocks (OBSERVED) plus the workers' wider count (REPORTED BY workers, not re-run). The page count used is "77 help articles and 4 plan pages", as this report states it at :21 and :358; the brief's shorthand was "77 pages". The same line's grade cell was changed from "OBSERVED" to "OBSERVED, except the workers' 77 + 4 page count (REPORTED)", so the line is not graded above its weakest part.

Line 89 (§5, the R5 requirement line): one sentence appended to the line's text, placed before "Measures [D1 unless a source is cited]:" so the list that follows still reads under that phrase. §5 now says once that an evening-entry variant (1N, 1C, 1F, 2A, 2S) cannot qualify for any funded-account tier row until OPEN-1 is answered in writing by MFFU. Line 95 (flat-by measure) was not edited; the line 89 statement covers every §5 measure, including it.

Diff of the previously staged design blob (edf71be, as Correction 1 left it) against the newly staged blob (124f763 = `git rev-parse :docs/specs/2026-11-09-r6-announcement-research-design.md`); `-` is the old line, `+` the new:
```
$ git diff -U0 edf71be 124f763
diff --git a/edf71be b/124f763
index edf71be..124f763 100644
--- a/edf71be
+++ b/124f763
@@ -16 +16 @@ Grades: OBSERVED (text or output captured in this unit), INFERRED (reasoning fro
-| Flat-by time | "automatically closed at 4:10 PM EST on regular (non-holiday) trading days" (trading-day.txt:12). No 16:59 rule on any page fetched. Holidays: "auto-liquidation will not occur at the half-time market close … Failure to close the positions before the market closes will result in breaching" (trading-day.txt:20-22). | OBSERVED |
+| Flat-by time | "automatically closed at 4:10 PM EST on regular (non-holiday) trading days" (trading-day.txt:12). No 16:59 rule in the 27 page blocks of the committed captures (zero hits, OBSERVED, report Correction 1 C3); workers W1 and W4 reported zero hits over the 77 help articles and 4 plan pages they read (REPORTED BY workers, not re-run). Holidays: "auto-liquidation will not occur at the half-time market close … Failure to close the positions before the market closes will result in breaching" (trading-day.txt:20-22). | OBSERVED, except the workers' 77 + 4 page count (REPORTED) |
@@ -89 +89 @@ The backtest unit confirms each event by a volume/range spike on the T+1 bar and
-R5 requires: fully rule-based; net positive after costs; survives every MFFU condition, including the EOD trailing drawdown and the consistency rule. Measures [D1 unless a source is cited]:
+R5 requires: fully rule-based; net positive after costs; survives every MFFU condition, including the EOD trailing drawdown and the consistency rule. An evening-entry variant (1N, 1C, 1F, 2A, 2S) cannot qualify for any funded-account tier row until OPEN-1 is answered in writing by MFFU; passing the measures below does not settle OPEN-1. Measures [D1 unless a source is cited]:
```
Re-run of the C3 counts this line now cites (taken in this unit, on the committed captures):
```
$ /usr/bin/grep -c '16:59\|4:59' docs/reports/evidence/2026-11-09-r6-mffu-*.txt
docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-news.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-plans.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt:0
exit=1
$ /usr/bin/grep -c '4:10' docs/reports/evidence/2026-11-09-r6-mffu-*.txt
docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-news.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-plans.txt:0
docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt:8
exit=0
$ /usr/bin/grep -c '^URL:' docs/reports/evidence/2026-11-09-r6-mffu-*.txt
docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt:5
docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt:4
docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt:5
docs/reports/evidence/2026-11-09-r6-mffu-news.txt:2
docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt:4
docs/reports/evidence/2026-11-09-r6-mffu-plans.txt:3
docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt:4
exit=0
```
Page blocks 5+4+5+2+4+3+4 = 27; zero 16:59/4:59 hits; the `4:10` control fires (8 in trading-day.txt).

### Edit 2c. Grep of the whole design for the permission words

The brief's pattern (case-sensitive):
```
$ /usr/bin/grep -nE "compliant|allowed|ALLOWED|allow|permitted" docs/specs/2026-11-09-r6-announcement-research-design.md
14:| T1 news rule | T1 = "FOMC Meetings, FOMC Minutes, Employment Report, CPI" (news.txt:38). Flat from 2 minutes before to 2 minutes after (news.txt:27-28). The policy text restricts "Rapid Sim Funded" and "Pro Sim Funded" and leaves "All evaluations" and "Builder Plans" unrestricted (news.txt:30-35). Conflicts: the 2026 T1 image banner says "strictly prohibited on sim funded accounts" without naming plans, while its caption says "to be avoided on all news-restricted accounts" (news.txt:50) and Builder guides say T1 holds are allowed in Sim Funded (adversarial.txt:332, :484); a "Standard Trading Protocols" line says flat 2 minutes around "any data release" (news.txt:20-21). | OBSERVED text; Rapid/Pro Sim Funded scope OBSERVED and unambiguous; Builder Sim Funded scope UNVERIFIED (MFFU text conflicts) |
28:- **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWED by the T1 rule on every account (exit at T−5). Inside one MFFU session (18:00 → 16:10). Whether MFFU counts the evening entry as holding overnight is UNVERIFIED: MFFU's pages do not say, and a Rapid page says "Holding overnight will breach the account." (plans-site.txt:24). A written MFFU answer is needed before any funded use (OPEN-1).
52:- Low-volume hours: "Profiting from isolated, stale or unrealistic fills … during low-volume hours is not allowed" (news.txt:86). The 18:05 bar can be thin (volume 29 on 2024-06-11, E5). The first pass reports a 20:00 ET entry and a 4-ticks/side slippage row beside the judged 18:05 / 2-tick figures [D1]. Whether MFFU would treat an ordinary market order at 18:05 as "stale fill" profit is UNVERIFIED (OPEN-5).
64:**2S — split hold, compliant with the T1 rule; its evening entry carries the UNVERIFIED overnight question (OPEN-1) [D1; not the papers' strategy].**
exit=0
```
The brief's pattern does not match "Allowed" (capital A, lower-case rest). Control, case-insensitive, with "deployable" added, first 60 characters per hit:
```
$ /usr/bin/grep -niE "compliant|allow|permitted|deployable" docs/specs/2026-11-09-r6-announcement-research-design.md | cut -c1-60
14:| T1 news rule | T1 = "FOMC Meetings, FOMC Minutes, Emplo
28:- **Strategy 1, Pre-Announcement Drift, evening entry, ex
29:- **Strategy 2, Announcement-Day Premium, holding through
52:- Low-volume hours: "Profiting from isolated, stale or un
62:**2A — as published (hold through the release).** Long 1 
64:**2S — split hold, compliant with the T1 rule; its evenin
exit=0
```
Disposition per hit:
- :14 — "allowed" is in MFFU's Builder guides (T1 holds in Sim Funded), quoted as a conflict; not a claim about an evening-entry variant.
- :28 — Strategy 1 (1N/1C/1F), evening entry: carries OPEN-1 on the line ("Whether MFFU counts the evening entry as holding overnight is UNVERIFIED … (OPEN-1)").
- :29 — Strategy 2 (2A/2S), "Allowed by the T1 rule in evaluations, Studio and Live": carries OPEN-1 on the line ("its evening entry carries the same UNVERIFIED overnight question as Strategy 1 (OPEN-1)"; "subject to OPEN-1").
- :52 — "is not allowed" is MFFU's low-volume rule, quoted; the open question is OPEN-5, stated on the line.
- :62 — 2A "never deployable on a Sim Funded account"; a restriction, not a permission.
- :64 — 2S, "compliant with the T1 rule": carries OPEN-1 on the line.
No hit about an evening-entry variant lacks the OPEN-1 caveat on its own line.

### What Correction 2 supersedes

Correction 2 supersedes Correction 1's Result line (:704). Limits that line listed and that are now fixed:
1. MANIFEST.md line 308 called 2S "MFFU-compliant" without the OPEN-1 caveat (the stated reason for that FAIL): fixed, Edit 1.
2. "design line 16 still says 'any page fetched'": fixed, Edit 2a.
3. "design lines 89 and 95 do not carry OPEN-1": fixed by one statement on line 89 that covers all of §5, including line 95's measure (Edit 2b).
Limits from :704 that still stand: E3 and E5-E8 rest partly on /tmp and worker files outside the diff (C4, A3); Correction 1's two adversaries did not re-run E5-E8; no third adversary checked the text after adversary 2's fixes; the design's second version was never re-attacked as a whole by a fresh adversary; OPEN-1 to OPEN-5 remain open; nothing is implemented or tested. Added by this correction: no adversary checked Correction 2 (master's brief item 6). Report lines 1-704, including the earlier statements that Correction 1 superseded, are not edited.

### Final evidence (taken after the last edit)

Taken after the Correction 2 text above was appended and the report re-staged. Only this evidence block and the Result line follow it.
```
$ head -n 704 docs/reports/2026-11-09-r6-step1-manager.md | openssl dgst -sha256
SHA2-256(stdin)= 7ad0a27b562389b7c9145c920a7260f537d5f7c4db693eb7cb86132c0bcc080e
$ git -C /Users/admin/Praxis.build-r6 status --porcelain
M  MANIFEST.md
A  docs/reports/2026-11-09-r6-step1-manager.md
A  docs/reports/evidence/2026-11-09-r6-mffu-adversarial.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-drawdown.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-news.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-plans-site.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-plans.txt
A  docs/reports/evidence/2026-11-09-r6-mffu-t1-calendar-2026.png
A  docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt
A  docs/specs/2026-11-09-r6-announcement-research-design.md
$ git -C /Users/admin/Praxis.build-r6 diff --cached --stat
 MANIFEST.md                                        |   10 +
 docs/reports/2026-11-09-r6-step1-manager.md        |  824 +++++++++++++
 .../evidence/2026-11-09-r6-mffu-adversarial.txt    |  573 +++++++++
 .../evidence/2026-11-09-r6-mffu-consistency.txt    |  155 +++
 .../evidence/2026-11-09-r6-mffu-drawdown.txt       |  515 ++++++++
 docs/reports/evidence/2026-11-09-r6-mffu-news.txt  |  117 ++
 .../evidence/2026-11-09-r6-mffu-plans-site.txt     | 1291 ++++++++++++++++++++
 docs/reports/evidence/2026-11-09-r6-mffu-plans.txt |  964 +++++++++++++++
 .../2026-11-09-r6-mffu-t1-calendar-2026.png        |  Bin 0 -> 1249126 bytes
 .../evidence/2026-11-09-r6-mffu-trading-day.txt    | 1117 +++++++++++++++++
 .../2026-11-09-r6-announcement-research-design.md  |  123 ++
 11 files changed, 5689 insertions(+)
$ wc -l MANIFEST.md docs/specs/2026-11-09-r6-announcement-research-design.md
     316 MANIFEST.md
     123 docs/specs/2026-11-09-r6-announcement-research-design.md
     439 total
$ git -C /Users/admin/Praxis.build-r6 show :MANIFEST.md | head -n 306 | cmp - <(git -C /Users/admin/Praxis.build-r6 show f10603a:MANIFEST.md) && echo HEAD306_IDENTICAL
HEAD306_IDENTICAL
$ git -C /Users/admin/Praxis.build-r6 show :MANIFEST.md | sed -n 308p
| /docs/specs/2026-11-09-r6-announcement-research-design.md | Spec | 2 | 2026-11-09 | R6 research design, PROPOSED, level WRITTEN: Pre-Announcement Drift evening-entry variants 1N/1C/1F and Announcement-Day Premium 2A (benchmark, blocked in Sim Funded) / 2S (split; passes the T1 rule; evening-entry overnight question UNVERIFIED, OPEN-1); free event calendars; costs v1.2.0; R5 qualification and A4 per-tier drawdown test; S6 conflicts OPEN-1..5 (incl. gate 4 unreachable, inactivity). |
$ S=$(sed -n 6p docs/specs/2026-11-09-r6-announcement-research-design.md | sed 's/^Standing limitation: //')   # the standing limitation sentence, held in a variable
$ grep -cF "$S" docs/reports/2026-11-09-r6-step1-manager.md; grep -cF "$S" docs/specs/2026-11-09-r6-announcement-research-design.md   # working files
1
1
$ git show :docs/reports/2026-11-09-r6-step1-manager.md | grep -cF "$S"; git show :docs/specs/2026-11-09-r6-announcement-research-design.md | grep -cF "$S"   # staged blobs
1
1
```

The baseline hash of lines 1-704 (top of Correction 2) and the hash above are equal: 1-704 unchanged. HEAD306_IDENTICAL: MANIFEST.md rows 1-306 equal the base f10603a. The report's standing-limitation count (1) is taken after the Correction 2 append; this evidence block and the Result line do not contain the sentence. The report's own line count and diff-stat line are not self-measured; the master and auditor measure them.

Result: PASS at level WRITTEN. MANIFEST.md line 308 and design lines 16 and 89 are corrected in place (316 and 123 lines kept, rows 1-306 identical to f10603a); no line of the design or MANIFEST rows 307-316 states or implies that an evening-entry variant (1N, 1C, 1F, 2A, 2S) is MFFU-compliant or allowed without the OPEN-1 caveat on that line; §5 states once that none can qualify for a funded-account tier row until MFFU answers OPEN-1 in writing. The evening-entry overnight question stays UNVERIFIED (OPEN-1). Limits that still stand are listed under "What Correction 2 supersedes"; no adversary checked Correction 2, and the independent audit grades it. Nothing is implemented or tested.
