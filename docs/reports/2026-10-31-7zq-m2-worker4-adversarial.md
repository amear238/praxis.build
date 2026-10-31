# 7zq M2 worker 4 — ADVERSARIAL report on PraxisLastHalfHourMomentum (A), hand-test checklist (B), decisions addendum (C)

## Task
Try to break three things. A: `ninjascript/PraxisLastHalfHourMomentum.cs`, which claims to implement Baltussen, Da, Lammers & Martens (2021) η(r_ROD). B: `docs/reports/2026-10-31-7zq-m2-handtest-checklist.md`. C: `docs/reports/2026-10-31-7zq-m2-decisions-addendum.md`. They are tested against brief criteria 1–9 (S1, S2, S6, S8, F3).

## Mode
ADVERSARIAL. A, B and C were not edited. Nothing was compiled, because there is no NT8 on this Mac. Grades: OBSERVED (output pasted) / INFERRED / CANNOT-DETERMINE-STATICALLY.

## Process log
1. Read A (`cat -n`), B and C in full.
2. Hashed the paper PDF: `623ba824…acec57`, which matches the brief. Grepped the pdftotext for Eq. 2, Eq. 12, the data filters, Table 1, Table 6, Table A1 and Table B1. Mapped each to its PDF page by counting form feeds.
3. Inventory checks: duplicate types, `file`, `xxd`, CR count, non-ASCII lines, the rule→line map, and the F3 sentence count.
4. Checked B's sources: voice notes :22–54, DECISION_LOG rows 449 (22:17:00Z), 466 (00:46:43Z) and 365, the cost model, and the a20 time-zone result.
5. Scanned the import file `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt` (read-only) with scratch scripts kept outside the repo, `…/scratchpad/m2w4/scan.awk` and `count.py`. The scan looked for missing 15:30 and 15:59 bars, weekend stray bars, and partial RTH sessions in 2021-03-08 → 2026-07-17.

## Findings

### 1. MAJOR — C misdescribes what A does when there is no 15:30 bar (criteria 8, 9 / S2)
C says the build never trades without a 15:30 bar. The file says the opposite. A uses the **first** bar in [15:30, 15:59).
```
C:110  4. **Missing 15:30 bar.** The design makes no trade on any session without a 15:30-stamped bar: early close, or a data gap on a normal
C:111     day. There is no fallback to the nearest bar. Is that what you want? (Shortlist Q1.3, which proposed skipping early-close sessions.)
C:59   ... one trade per regular session, no trade without a 15:30 bar; input Contracts only; ...      (draft MANIFEST row)
A:49   //   * Signal: once per session, on the FIRST bar with SignalMod <= mod < FlatMod (normally the 15:30 bar),
A:75   //   D1. Missing 15:30 bar (no trades that minute): the next bar before 15:59 is used as the signal bar,
A:187  bool inSignalWindow = SignalMod <= mod && mod < FlatMod;
```
C says it did not read A and grades this INFERRED, pending the adversarial check (C:6-7). This is that check, and the claim is false. Two things follow:
- The NEEDS AMEAR question would put a false premise to Amear.
- The draft MANIFEST row, a permanent record, would describe the file wrongly.

Real-world exposure is small. In the import file, every weekday session with any bar in the window has a 15:30 bar. D1 fires only on weekend stray bars (see 4):
```
weekday sessions with a window bar: 1305
weekday sessions with a 15:30 bar: 1305
```
**Minimal fix:** rewrite C:110-111 and the C:59 row to match A:75-76 (D1). Example: "the first bar in [15:30, 15:59) is used; in the 2021-03-08→2026-07-17 import every weekday session that has such a bar has a 15:30 bar (OBSERVED)." Whether to fall back or require `mod == SignalMod` exactly stays Amear's call.

### 2. MAJOR — unlisted paper mismatch: P(c,t−1) after CME partial sessions on NYSE holidays (criteria 2, 3)
A sets the previous close to `Close[1]` on the first bar of a session (A:161). That is the last bar of the prior NT8 session, whatever time it carries. The data has 47 weekday sessions with RTH bars but no 15:30 bar. Only 9 are true early closes (13:15). 37 are CME 13:00 halts on **NYSE holidays** (MLK, Presidents, Memorial, Juneteenth, July 4, Labor, Thanksgiving). One is a data gap on a regular Wednesday (2023-04-05, last bar 14:03). OBSERVED:
```
weekday partial RTH sessions (RTH bars, no 15:30): 47
['20210531@1300', '20210705@1300', '20210906@1300', '20211125@1300', '20211126@1315', '20220117@1300', ... '20230405@1403', ...
 '20240115@1300', ... '20241129@1315', '20241224@1315', ... '20260619@1300', '20260703@1300']
```
The paper filters its data by "(ii) removing all non-business days, (iii) removing all days in which the exchange closed earlier" (pdftotext L315–317, PDF p. 5 = p. 381, OBSERVED). On the paper's cash-market calendar, MLK is not a business day. So the day after MLK takes Friday's 16:00 close as P(c,t−1). That reading (filter the days first, then compute returns) is INFERRED.

If the NT8 template carries the MLK partial session, A instead takes the 13:00 price of a session in which the cash market was closed. Whether it does is CANNOT-DETERMINE-STATICALLY. If it does, the sign of r_ROD rests on a different denominator on up to ~37 days (≈2.8% of trades), plus 9 days after early closes and 1 after the data gap.

D3 (A:78-80) covers only "Day after an early-close session" and calls it SPEC-SILENT. For the 37 holiday cases, filter (ii) is not silent. C Q3 (C:107-109) has the same narrow framing. This is an omission from the deviation list, which is exactly what criterion 2 tests.

**Minimal fix:** widen D3, or add a D7, with these counts. In C's NEEDS AMEAR, offer the third option: "use the most recent 16:00-stamped close". In code that would mean capturing `prevSessionClose` only on a bar with `mod == 960`. Amear decides. Add a B readback: the Data Box `Close[1]` used on 2024-01-16 (the day after MLK 2024).

### 3. MINOR — B's trade-count point estimate is ~30 too high (criterion 7)
B:35-37 estimates ≈1,334, using about 50 full holidays and about 15 early closes. The data caps it lower. Only 1,305 weekday sessions have a 15:30 bar (OBSERVED, above). After the first session, that leaves **≤1,304** trades. The model is off because no-trade weekdays are 1,400 − 1,305 = 95, not about 65. Weekday count, OBSERVED:
```
weekdays 1400 years 5.361 x252 1351
```
1,304 sits only 4 above B's lower bound of 1,300. Commission then ≈ 1,304 × 2.96 = $3,860, slippage ≈ $26,080, and NT "Total slippage" ≈ 52.16. **Fix:** state ≈1,304 as an OBSERVED ceiling from the import file, with a range of about 1,280–1,304.

### 4. MINOR — 18 weekend stray bars fall in the signal window; A and B say nothing about them (criteria 3, 7)
```
weekend dates with a window bar: 18 [('20210508', 'Sat'), ('20211219', 'Sun'), ... ('20251102', 'Sun')]
20210508 ['20210508 155500;17131.5;17131.5;17131.5;17131.5;1']
D4_missing_1559_with_window_bar=18: 20220904(no1600) ... (all 18 are these weekend dates)
```
If NT8's RTH template drops bars outside its sessions, these have no effect (INFERRED). If it does not, each one becomes a phantom signal with no 15:59 or 16:00 bar after it. That would mean an overnight or weekend hold through the D4 path. **Fix:** add a B readback, "any trade dated Sat/Sun? (count + first date)". An optional code guard on `Time[0].DayOfWeek` is Amear's call.

### 5. MINOR — C asserts a governing flat time that F2 says does not exist (criterion 8 / S6, S8)
```
C:84-85  ... untouched. The governing flat time stays 16:00 ET, and the 15:00 disposition is not addressed.
SPEC_RUBRIC.md:31  **Criterion.** One governing rule, written down, resolving: breaker #4 ... Deviation B flattens at 16:00 ET.
DECISION_LOG.md:365 ... "the expected flat-by-16:00 Eastern session close" is not an established requirement — it is one of the three candidates F2 was frozen to adjudicate.
```
The wording is inherited from M1 (decisions-scope.md:51, audited PASS). It still treats 16:00 ET as the governing rule, which is F2's open question. **Fix:** "the backtest realises Deviation B's 16:00 ET flat, one of F2's unresolved candidates; no governing rule exists or is named here."

### 6. MINOR — the previous close depends on an unconfirmed template end time (criteria 3, 7)
A:46-47 says Close[1] is "its 16:00 bar on a regular day". DECISION_LOG:365 records an open item: Amear's reading of the template showed `8:30 AM – 4:00 PM` Central, which is 17:00 ET. Against that, voice-notes :23 (REPORTED BY AMEAR) says "the 16:00 bar is followed by 9:31". B:17-18 checks the template **name** only, not the stamp of the session's last bar. If the session really ends at 17:00 ET, every `prevSessionClose` is the 17:00 price. The 15:30 and 15:59 constants still hold, because they are clock-based. The base file has the same dependency. **Fix:** add a B step: "Data Box: last RTH bar of 2026-07-16 is stamped 16:00 ☐". Fix 2 (a `mod == 960` capture) would also remove the dependency.

### 7. MINOR — two rare paths can submit two exits on one bar (criteria 3, 4)
(a) If the 15:59 bar is missing, `LHFlat1559` is sent on the 16:00 bar (A:177-182). On that same bar the session-close backstop could also fire, since a 16:00:00 stamp is ≥ 16:00 − 30 s. (b) If the first bar of a session has `mod >= 959` and a stale position, `LHStaleFlat` (A:164-173) and `LHFlat1559` (A:177-182) are both submitted on that bar. How NT8 managed orders handle a double exit, including a possible overfill or reversal, is CANNOT-DETERMINE-STATICALLY. D4 names the safety nets but not this collision. On weekdays in the import file it happens 0 times (OBSERVED in finding 4's scan: all 18 missing-15:59 cases are weekend dates). **Fix:** `return` after a stale exit in the first-bar block, and note the collision in D4.

## Positive controls for "no finding"
- **Look-ahead (crit. 1):** `Close[` appears only at A:161 (`Close[1]`, prior bar) and A:195 (`Close[0]` of the closed signal bar under OnBarClose, A:123). No negative index and no `Open[0]` read before the fill. The map grep below fires on both lines. The fill goes to the next bar's Open ≈ P(15:30) (INFERRED).
- **Sign rule, r = 0 (crit. 2):** A:196-199, `if (r > 0) EnterLong else EnterShort`, matches Eq. 12 "otherwise" (pdftotext L665-670, PDF p. 9 = p. 385).
- **Page cites (crit. 2, 6):** form-feed map: Eq. 2 / filters PDF p. 5 (=381), Table 1 p. 7 (=383), Eq. 12 p. 9 (=385), costs p. 10 (=386), Table 6 p. 11 (=387), Table A1 PDF p. 19. All match A:26-34. Table 6 Panel A η(r_ROD) SR **1.73** ✓. The "No NQ-alone P&L" claim holds: Table B1's NQ row is a regression ("results of regressing the last half-hour return").
- **Duplicate types (crit. 5):** `grep -n "enum \|class \|struct " ninjascript/*.cs` fired on 10 declarations. `PraxisLastHalfHourMomentum` appears once; the other names are distinct, and the nested `DayRecord`/`ParsedSignal` are private nested types. No CS0101.
- **API (crit. 5):** `EnterLong(int,string)`, `ExitLong(string,string)`, `ExitOnSessionCloseSeconds=30`, `TimeInForce.Day`, `BarsRequiredToTrade=20`, `[Range]`, `public int Contracts` all mirror the base (base :109-112, :227, :288, :303-305), which compiled clean per REPORTED voice :33. No using is missing relative to the base (INFERRED).
- **Encoding (crit. 5):** `file` shows UTF-8 for both. CR count is 0 in A and in the base. `xxd` byte 0 is `23` (`#`), so no BOM. Non-ASCII appears on 6 lines, all comments (A:18, 106, 107, 137, 176, 202). The base has 57 such lines.
- **Rule→line map (crit. 6):** `grep -n` returned 106, 107, 157, 161, 167, 172, 180, 182, 187, 195, 197, 199. All 11 entries in A:88-98 match.
- **F3 sentence (crit. 6):** `grep -c -F` gives A=1, B=1, C=1. Control: the shortlist gives 0, so the grep can miss.
- **Overclaim (crit. 9):** grepping compiled/tested/verified gives A:19 "WRITTEN, NOT COMPILED, NOT TESTED", A:87 "verified with grep -n" (true, re-run above), and C:17, which is a quoted log line. B:3 says "Nothing here was compiled or run". B's "NT8 8.1.7.2" has a source (DECISION_LOG:410).
- **B vs sources (crit. 7):** I read every cited voice line (:32, :33, :40, :47, :48, :52-54) and DECISION_LOG:449 ("Time in force DAY"). All match. The "confirm the template" line is the first item in §2 (B:17). Cost arithmetic re-run: 3948.64 / 3848 / 3996 / 26680 / 53.36. The cost model shows tick $5 and $1.48/side.
- **C S4 chain (crit. 8):** `grep -n "00:46:43" DECISION_LOG.md` gives rows 462/465/466, identical to C:16-18. Row 466 carries "third file: **"Build the top-ranked one (Recommended)"**", and it is in HEAD (`git show HEAD:DECISION_LOG.md | grep -c` = 1).
- **MANIFEST columns (crit. 8):** `head -5 MANIFEST.md` shows 5 columns. The awk field count for C:59-68 is 7 on every row (5 cells + 2 edges). C (c) names Block 2, F1, F2, F3, F4 and leaves O1 unanswered. C (e) lists 10 questions and answers none (but see 5).
- **Same-bar entry + exit, double entry (crit. 4):** the exit block always `return`s (A:183). Entry needs Flat (A:192). `signalDoneToday` is set before any entry (A:190) and reset only on the first bar of a session (A:157). On a regular session the first bar (09:31, mod 571) is outside the window.
- **BarsRequiredToTrade=20 (crit. 3):** the first session gets `prevSessionClose = 0` (A:161), so no order is attempted before bar 20.
- **TZ/DST (crit. 3):** NT8 time zone REPORTED "UTC-05:00 Eastern Time US and Canada" (a20-results:19, N1 provisional). Bar-time check PASS (voice :22-27).

## Verification evidence
The pasted outputs are inline above, under each finding and control.

## Files staged
`docs/reports/2026-10-31-7zq-m2-worker4-adversarial.md` only.

## Result
BROKEN on two MAJORs (1, 2); five MINORs (3–7).

VERDICT: BROKEN
