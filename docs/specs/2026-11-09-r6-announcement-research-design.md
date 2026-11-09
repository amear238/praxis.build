# R6 announcement research design — Pre-Announcement Drift (evening entry) and Announcement-Day Premium

Status: PROPOSED. Level: WRITTEN (specified only; nothing implemented, nothing run, nothing tested).
Unit: `2026-11-09-r6-step1`, bead `Praxis_build-ckh`. Authority: Amear D-2026-11-08-A R5, R6, R7 (DECISIONS.md :1566-1582), A4 and A5 (:1735-1743), D-2026-11-08-D D1/D2/D7. Pasted evidence for every figure below: `docs/reports/2026-11-09-r6-step1-manager.md` (sections E1-E8); MFFU text: `docs/reports/evidence/2026-11-09-r6-mffu-*.txt` and `…-t1-calendar-2026.png`.

Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

Grades: OBSERVED (text or output captured in this unit), INFERRED (reasoning from observed text), UNVERIFIED (not found, not loaded, or ambiguous). "[D1]" = decided by manager under D-2026-11-08-D D1, changeable by Amear (wording per the master's brief; DECISIONS.md :1908 words it "decided by master under …").

## 0. Gate from Part A (MFFU's current rules, fetched 2026-11-09 09:06-09:18Z)

| Item | Plain answer | Grade |
|---|---|---|
| T1 news rule | T1 = "FOMC Meetings, FOMC Minutes, Employment Report, CPI" (news.txt:38). Flat from 2 minutes before to 2 minutes after (news.txt:27-28). The policy text restricts "Rapid Sim Funded" and "Pro Sim Funded" and leaves "All evaluations" and "Builder Plans" unrestricted (news.txt:30-35). Conflicts: the 2026 T1 image banner says "strictly prohibited on sim funded accounts" without naming plans, while its caption says "to be avoided on all news-restricted accounts" (news.txt:50) and Builder guides say T1 holds are allowed in Sim Funded (adversarial.txt:332, :484); a "Standard Trading Protocols" line says flat 2 minutes around "any data release" (news.txt:20-21). | OBSERVED text; Rapid/Pro Sim Funded scope OBSERVED and unambiguous; Builder Sim Funded scope UNVERIFIED (MFFU text conflicts) |
| Evening entry vs trading day | "Trades may be placed beginning at 6:00 PM EST when the Globex session opens and can remain open until the New York session closes at 4:10 PM EST" (trading-day.txt:10). An entry after 18:00 sits inside the session that ends at 16:10 on the release day. The Rapid FAQ glosses "overnight" in the same answer: "All positions must be closed before the daily session close. Holding overnight will breach the account." (plans-site.txt:24); Builder: "All positions must be closed before the end of the trading session." (trading-day.txt:1109). MFFU never says "trading day" for an evening entry. | session window OBSERVED; "same trading day" UNVERIFIED (no explicit text; the FAQ's own gloss supports it, INFERRED) |
| Flat-by time | "automatically closed at 4:10 PM EST on regular (non-holiday) trading days" (trading-day.txt:12). No 16:59 rule in the 27 page blocks of the committed captures (zero hits, OBSERVED, report Correction 1 C3); workers W1 and W4 reported zero hits over the 77 help articles and 4 plan pages they read (REPORTED BY workers, not re-run). Holidays: "auto-liquidation will not occur at the half-time market close … Failure to close the positions before the market closes will result in breaching" (trading-day.txt:20-22). | OBSERVED, except the workers' 77 + 4 page count (REPORTED) |
| Consistency / drawdown / inactivity | Consistency 30% Rapid EOD, 50% Rapid and Pro; "does not breach the account" (consistency.txt:13-22); Builder 50% per payout cycle in Sim Funded (plans.txt:464). EOD trailing moves "only at the close of each trading session", locks at +$100 (drawdown.txt:152-158); Rapid Sim Funded trails intraday on equity highs "including unrealized" (drawdown.txt:38). Inactivity: "does not place a trade for 7 consecutive calendar days, the account could be closed. This includes simulated funded accounts." (consistency.txt:46). | OBSERVED |

**Time zone [D1].** MFFU writes "EST" year-round, including "ALL LISTED TIMES ARE EASTERN STANDARD TIME (EST)" on a calendar whose July and August events are at 8:30 AM. This design reads MFFU's "EST" as US Eastern local time (EST in winter, EDT in summer). INFERRED: the data's release-minute spike on 2024-06-12 (EDT) sits on the 08:31 and 14:01 bars (E5), and the Fed statements read "2:00 p.m. EDT" in summer (E7).

**Constraint set used by this design [D1] (the design's own constraints, stricter than some MFFU pages):**
- (i) Flat from T−5 min to T+3 min around every T1 release, on every account and stage.
- (ii) The "any data release" line (news.txt:20) is applied to US scheduled releases at 08:30 ET or later. PAD-E core variants exit at 08:25 and so clear every release from 08:30 on. Variants 1F and 2S hold through 10:00-14:00 and need a non-T1 release list that this unit did not source → OPEN-4.
- (iii) Every position opened at or after 18:00 ET is closed before 16:10 ET in the same MFFU session, and before any early close.
- (iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED).

**Per strategy, as R6 describes it:**
- **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWED by the T1 rule on every account (exit at T−5). Inside one MFFU session (18:00 → 16:10). Whether MFFU counts the evening entry as holding overnight is UNVERIFIED: MFFU's pages do not say, and a Rapid page says "Holding overnight will breach the account." (plans-site.txt:24). A written MFFU answer is needed before any funded use (OPEN-1).
- **Strategy 2, Announcement-Day Premium, holding through the release:** **BLOCKED BY MFFU RULE on Rapid Sim Funded and Pro Sim Funded.** Quotes: "Restricted Accounts: Trading on T1 News events is prohibited for the following: Rapid Sim Funded / Pro Sim Funded" (news.txt:30-32) and "All positions must be flattened at least two minutes prior to the scheduled T1 News event." (news.txt:28). On Builder Sim Funded, MFFU's text conflicts (image banner vs Builder guides) → treated as blocked under (i) [D1]. Allowed by the T1 rule in evaluations, Studio and Live per MFFU's text; its evening entry carries the same UNVERIFIED overnight question as Strategy 1 (OPEN-1). The proposed deployable form, subject to OPEN-1, is the split variant 2S (§2), which is a design change, not the papers' strategy [D1].

## 1. Strategy 1 — Pre-Announcement Drift, evening-entry variant (PAD-E)

**Source (paper's claim).** Hu, Pan, Wang & Zhu, "Premium for heightened uncertainty: Explaining pre-announcement market returns", JFE 145(3):909-936 (2022), DOI 10.1016/j.jfineco.2021.09.015. Abstract (IDEAS/RePEc, E6): "We find large overnight returns with no abnormal variance before nonfarm payrolls, ISM, and GDP announcements, similar to the pre-FOMC returns." OBSERVED-abstract for the event set and the word "overnight". UNVERIFIED (paywalled full text not read): magnitude, sample period, instrument, the exact clock window, and whether the return still accrues in the minutes before the release.

**Variants and event sets [D1].**
- 1N (core): Employment Situation (NFP), release 08:30 ET. In the abstract; free dates.
- 1C (extension, labelled NOT IN THE ABSTRACT): CPI, 08:30 ET.
- 1F: FOMC statement, 14:00 ET ("similar to the pre-FOMC returns").
- Excluded for now: ISM (10:00) and GDP (08:30) — no free historical date source verified in this unit (not bought).

**Rules (1-minute bars, end-stamped; US Eastern local time).**
- Entry: on calendar day E−1 (the evening before release day E; Sunday for a Monday release), buy 1 MNQ at market on the close of the bar stamped 18:05 ET. Fill modelled at the next bar's open.
- Exit: sell at market on the close of the bar stamped T−5 min on day E (08:25 for 08:30 releases; 13:55 for FOMC). Fill at the next bar's open, about T−5 to T−4, which is at least 2 minutes before the T−2:00 cut-off.
- Earlier-release override: if any T1 release (or, for 1F, any release listed under OPEN-4) falls between entry and the target exit, exit instead at the close of the bar stamped (that release's time − 5 min) and do not re-enter. Example: on a CPI + FOMC day, 1F exits at 08:25.
- Skip rules: no trade if the 18:05 bar on E−1 or the exit bar on E is missing, if a data hole lies between them, or if E's session is an early close (data or exchange) that ends before the target exit (E8 lists the three Good Friday NFP days, data ending 09:15: 1N exits at 08:25 and is unaffected; any later exit is skipped).
- Direction long only; no stop, no target, no optimisation in the first pass. Size 1 MNQ (1 NQ shown alongside, as D6).

**Bars exist for this geometry (E5, E8).** Sampled evenings carry 359 bars 18:01-23:59 and 571 bars 00:00-09:30. For in-range events on data sessions, the 18:05 bar on E−1 is present for FOMC 42/42, CPI 61/63, NFP 61/61; the exit bar (08:25 / 13:55) is present for all of them.

**MFFU conditions specific to an evening hold.**
- 2% price-limit rule, Sim Funded and Live: "overnight price limits have increased to 5% … Consequently, trading is suspended" (adversarial.txt:544). The backtest flags every event night whose move from the prior settlement reaches 3% (INFERRED proxy) and reports them; a suspension would block the exit.
- Low-volume hours: "Profiting from isolated, stale or unrealistic fills … during low-volume hours is not allowed" (news.txt:86). The 18:05 bar can be thin (volume 29 on 2024-06-11, E5). The first pass reports a 20:00 ET entry and a 4-ticks/side slippage row beside the judged 18:05 / 2-tick figures [D1]. Whether MFFU would treat an ordinary market order at 18:05 as "stale fill" profit is UNVERIFIED (OPEN-5).

## 2. Strategy 2 — Macroeconomic Announcement-Day Premium (ADP)

**Sources (papers' claims; E6).**
- Savor & Wilson (2013), JFQA 48:343-375: "Stock market average returns and Sharpe ratios are significantly higher on days when important macroeconomic news about inflation, unemployment, or interest rates is scheduled for announcement. The average announcement-day excess return from 1958 to 2009 is 11.4 basis points (bp) versus 1.1 bp for all the other days …" OBSERVED-abstract.
- Savor & Wilson (2014), JFE 113(2):171-201, "Asset pricing: A tale of two days": higher average returns for risky assets on announcement days (OBSERVED-abstract); event list and sample UNVERIFIED.
- "Ai 2024" is not pinned in the repo (DECISIONS.md :1576). Taken as Ai, Bansal & Guo, "Macroeconomic Announcement Premium", Oxford Research Encyclopedia of Economics and Finance (2024-05-22) — the only 2024 item with that title [D1]. Abstract: "During the period 1961–2023, roughly 44 days per year with macroeconomic announcements account for more than 71% of the aggregate equity market risk compensation." OBSERVED-abstract. The strategy-filter audit's "post-2018 evidence intact through 2022" is UNVERIFIED.
- No abstract splits the day's return into before- and after-release parts (UNVERIFIED which part carries it).

**2A — as published (hold through the release).** Long 1 MNQ from the close of the 18:05 ET bar on E−1 to the close of the 16:05 ET bar on E. BLOCKED BY MFFU RULE on Rapid and Pro Sim Funded (§0). Run only as a research benchmark, never deployable on a Sim Funded account.

**2S — split hold, compliant with the T1 rule; its evening entry carries the UNVERIFIED overnight question (OPEN-1) [D1; not the papers' strategy].**
- Entry: long 1 MNQ at the close of the 18:05 ET bar on E−1.
- For every T1 release at time T on day E (CPI/NFP 08:30, FOMC statement or FOMC Minutes 14:00): exit at the close of the bar stamped T−5; re-enter long at the close of the bar stamped T+3 (fills at T−4 and T+4, outside T±2).
- Exit: close of the bar stamped 16:05 ET on E.
- Skip the whole post-release leg on any early-close day (E8) and on any day with an OPEN-4 release until that list exists.
- 2S drops the release minutes, where announcement risk resolves; whether any premium survives that is what 2S tests (INFERRED to be material).

## 3. Event calendar — free sources (E7)

| Event | Free source | Dates | Times |
|---|---|---|---|
| FOMC statement | federalreserve.gov/monetarypolicy/fomccalendars.htm + statement pages | full range | "For release at 2:00 p.m. EDT/EST" on 47 statement pages; 2025-08-22 (10:00 a.m., Longer-Run Goals) excluded |
| FOMC Minutes | same calendar page ("Minutes … (Released <date>)") | listed, not yet extracted | 14:00 ET on the MFFU 2026 image only; earlier years INFERRED |
| CPI | alfred.stlouisfed.org/release?rid=10 | full range (posting dates; doubled months 2022-02, 2023-02, 2024-02) | BLS pages returned 403; 08:30 OBSERVED only for 2026 (MFFU image) |
| Employment Situation | alfred.stlouisfed.org/release?rid=50 | full range (doubled 2024-01, 2024-08) | as CPI |

The backtest unit confirms each event by a volume/range spike on the T+1 bar and drops and lists any event without one; doubled ALFRED dates are resolved the same way [D1]. Nothing needs buying; no D2 item.

## 4. Data, costs, sizing

- Data: `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt`, sha256 `307c5e8a…e454` (match), 1,857,362 lines, first `20210307 180100`, last `20260720 112700`. End-stamped bars (DECISIONS.md :257, INFERRED there). Eastern local wall clock INFERRED (NT8 match; 17:00/18:01 row structure). Holes 2021-09-09→09-27 and 2025-12-14→2026-01-01 are used as is (R-VN3-3).
- Costs (config/backtest-cost-model.json v1.2.0): MNQ $1.90 round turn + 2 ticks/side × $0.50 = $2.00 → $3.90 per MNQ round turn; NQ $4.68 + $20.00 = $24.68. 2S costs two round turns per event ($7.80 MNQ).

## 5. Qualification test (R5) and D6-style check

R5 requires: fully rule-based; net positive after costs; survives every MFFU condition, including the EOD trailing drawdown and the consistency rule. An evening-entry variant (1N, 1C, 1F, 2A, 2S) cannot qualify for any funded-account tier row until OPEN-1 is answered in writing by MFFU; passing the measures below does not settle OPEN-1. Measures [D1 unless a source is cited]:
- Net after §4 costs, over the full range and, separately, the 17-window OOS span [D1].
- Drawdown vs A4 (DECISIONS.md :1735-1737): worst drawdown at 1 MNQ per walk-forward window, WIN and VS4 both shown (as D6), judged on VS4 (as D6 Decision 5). Result per tier row, against that row's ceiling (Studio $160/$320/$640; 25K $800; 50K $1,600; Builder 50K add-on $1,200; 100K $2,400; 150K $3,600 — the D6 table). A strategy qualifies for a tier row if every window is strictly below that row's ceiling [D1, as D6 Decision 4].
- Rapid Sim Funded (intraday trailing) row: running peak = highest equity including unrealised gains (bar highs for a long), trough on bar lows, with the within-bar order assumed worst case (high before low) [D1].
- Consistency: largest single-session profit ÷ total profit per evaluation path and per payout cycle, against 30% (Rapid EOD) and 50% (Rapid, Pro, Builder Sim Funded); report the days needed (it does not breach).
- News windows: zero position-minutes inside any T±2 window of a T1 release (FOMC Minutes included).
- Flat-by: zero positions at 16:10 ET or across 16:10-18:00; none open at an early close.
- Inactivity (7 calendar days): of 173 gaps between consecutive event dates in range, 90 exceed 7 days and the longest is 37 (E8). A standalone event strategy therefore fails the inactivity rule on Sim Funded accounts. It is judged as failing standalone and is then evaluated only as an overlay on an account that trades on other days; no invented "keep-alive" trades [D1].
- Builder Soft DLL ("The Soft DLL ($1,750 on the Builder 100K) is a soft pause, not a breach.", plans.txt:532) is reported per Builder row as days that would have paused, not as a breach.
- Hedging and same-instrument overlap with the Noise-Area baseline: see A14 in §7.

## 6. How it would be backtested later, and dependencies

- Engine (proposal [D1]; the master files a DECISIONS.md entry before the backtest unit, S4): a Mac-side Python event simulator on the 1-minute file (signals on bar close, fills at the next bar's open, equivalent to Standard resolution), then an NT8 replication of any variant that qualifies, for parity (O4). No VM time in the first pass.
- Trade counts (E8): events on data sessions in range — FOMC 42, CPI 63, NFP 61. Inside the OOS span 2022-03-17 → 2026-06-05: FOMC 33, CPI 50, NFP 49; union 131 distinct dates (ALFRED doubling inflates CPI/NFP by a few). Per OOS window: FOMC 1-2, CPI 2-4, NFP 2-4. Per year about 8 FOMC + 12 CPI + 12 NFP, union 30-34 dates.
- Enough for the walk-forward? Not against the existing gates: gate 4 needs "≥ 250 aggregate OOS trades" (values spec :125); 1N gives at most 49 and all three PAD-E variants together at most 131. 2S's split must not be counted twice to reach 250. Gate 5 ("≥ 60% of walk-forward windows profitable", :126) on 2-8 events per window is noise-dominated (INFERRED). → OPEN-3.

## 7. Cross-block conflicts (S6)

| # | Block / spec | Conflict | State |
|---|---|---|---|
| OPEN-1 | MFFU terms (F4 channel, owner Amear) | "Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use. | OPEN |
| OPEN-2 | F2 (FROZEN); breakers #4 and #5 (Phase 3 spec :100-101); R8/A6 proposal unit | #4 "clock hits 11:30 ET → close positions, disable until next session": 1F (to 13:55) and 2S/2A (to 16:05) hold past 11:30. #5 "clock enters 3:00–6:00 PM ET → disable everything": 2S/2A hold 15:00-16:05. Entries at 18:05 are after #5 ends; whether #4's "next session" starts at 18:00 is undefined. 1N/1C (18:05→08:25) touch neither window. | OPEN (F2 changes state only when Amear approves the breaker proposal, A6) |
| OPEN-3 | Walk-forward gates (A7: arm (a) gates 1-5) | No event strategy on this data reaches gate 4's 250 OOS trades; whether gates 4 and 5 apply to R6 strategies needs a ruling. Agents do not write acceptance bars. | OPEN (Amear) |
| OPEN-4 | MFFU "any data release" line | Non-T1 releases (e.g. 10:00 ET) inside 1F and 2S holds; no free release list was sourced in this unit. | OPEN (backtest unit to source a free list, or 1F/2S stay provisional) |
| OPEN-5 | MFFU low-volume / stale-fill rule | Whether an 18:05 market entry is caught by it. | OPEN (F4 channel) |
| F3 | Fill resolution (FROZEN) | 1-minute bars, Standard resolution, next-bar-open market fills; the standing limitation applies. Exits are placed at T−5, away from the release bar. | Carried as the standing limitation |
| O4 | Backtest-vs-live parity (OPEN) | First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2. | First pass [D1]; parity OPEN with O4 |
| A14 | Same-instrument conflict and MFFU hedging rule vs the Noise-Area baseline | 1N/1C exit 08:25, before the baseline's 09:30 anchor: no overlap. 1F, 2A, 2S overlap the baseline's RTH window on NQ. First pass runs each variant standalone; a priority rule belongs to the overlay unit. | Standalone [D1]; overlay OPEN |
| A5 | R6 "trading day" = MFFU's definition | MFFU session 18:00 → 16:10 is the day for consistency, drawdown and inactivity counts. | Applied [D1] |
| R-1104-3 | Nothing bought | All sources free; ISM/GDP excluded rather than bought. | Applied |

## 8. What this design does not claim

No backtest, no result and no P&L figure exists for any variant. The papers' effects are their claims, read from abstracts. The MFFU readings are as fetched on 2026-11-09, and MFFU's own pages conflict on news scope.
