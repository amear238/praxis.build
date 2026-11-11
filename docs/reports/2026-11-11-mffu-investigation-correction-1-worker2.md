# 2026-11-11 MFFU investigation Correction 1 — worker 2

## Task
Unit `2026-11-11-mffu-investigation-correction-1`, worker 2. This is a re-dispatch with reduced scope. Mode: BUILD. Authority: DECISION_LOG 2026-11-11T17:32:05Z, decided by master under D-2026-11-08-D D1. The target is `/tmp/mffu-orig.md`, a pristine copy of `docs/reports/2026-11-11-mffu-connection-investigation.md`; it was read only and never edited. The job was to produce items C2.1-C2.4 as text to paste into the target's `## Correction 1`. That text is at `/tmp/mffu-corr/w2.md`.

## Rubric criteria
S1, S2 (graded claims; every grade backed by pasted command output).

## Process log
1. Wrote both skeleton files first. Read the target's lines 15-30, 88-96, 108-122 and 194-206 with `nl -ba`. Checked that fetch dirs `/tmp/mffu-fetch-41`..`46` did not exist yet. Each was created new and was empty (`ls -A` printed `[]`).
2. Fetch 41 got MFFU article 10082979 (HTTP 200, server-rendered). Fetch 42 got the ninjatrader.com home page. `/usr/bin/grep` replaced the default grep, which is ugrep and rejected the `{0,160}` pattern ("exceeds complexity limits").
3. Graded each step of 10082979 against the article text, and checked the "for evaluations" qualifier and the funded-account question. Wrote C2.1 and C2.2.
4. Pasted the fee-check report lines, the cost-model lines and the `git show --stat` for `a587a27`. Fetches 43 (MFFU help search "commissions"), 44 (ninjatrader.com/pricing) and 45 (MFFU Tradovate login article) looked for a platform or routing fee.
5. Line 203 says `a587a27` "applied $24.68", so I opened the archived 0710am trade list from that commit. Its Commission column is $2.96 on all 1,190 trades. DECISIONS.md:1126 shows that $4.68 arrived with cost model v1.2.0, and line 203 names v1.1.0. Wrote C2.3 and C2.4.
6. Moved my explanatory notes out of the pasted output blocks and put them in a labelled note. Ran the rep-name and S13 checks.

Five fetches used (41-45); fetch 46 was not created. I did not decide the broker route. I make no claim about rubric F4.

## Verification evidence

Fetch log (verbatim):
```text
2026-11-11T17:43:58Z
200 119667 https://help.myfundedfutures.com/en/articles/10082979-ninjatrader-login-instructions
2026-11-11T17:43:58Z
200 135645 https://ninjatrader.com/
2026-11-11T17:45:07Z
200 76567 https://help.myfundedfutures.com/en/?q=commissions
2026-11-11T17:45:07Z
200 102298 https://ninjatrader.com/pricing/
2026-11-11T17:45:08Z
200 120020 https://help.myfundedfutures.com/en/articles/8445591-tradovate-login-instructions
```

Key outputs (full pastes are in `/tmp/mffu-corr/w2.md`):
```text
=== 41 counts (tag-stripped article 10082979)
evaluation:        0
simulation:        3
rithmic:        0
$ grep -ci acqui /tmp/mffu-fetch-42/page.html
0
$ commission column values (distinct, count)   [docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv, from a587a27]
1190 $2.96
   1 commission col=15
```

Summary of grades (details in w2.md):
- Lines 112, 114, 115, 116, 117, 118: OBSERVED. Line 114 drops the "first time logging in" condition. Line 116's gloss "(NinjaTrader's native connection)" is INFERRED. Line 117 drops "click My NinjaTrader" and "Apply, OK".
- Line 19, "Simulation for evaluations": the article does not support it. The article never mentions evaluations ("evaluation" appears 0 times). It sets Simulation for every reader and says nothing about funded accounts.
- Lines 19/199 "exclusively Tradovate": REPORTED BY Hermes, UNVERIFIED. Line 119 "acquired": UNVERIFIED. The shared d/b/a ("NinjaTrader Clearing, LLC d/b/a NinjaTrader, Kraken Derivatives US, and Tradovate") is OBSERVED.
- Lines 199, 93, 198 become INFERRED. Line 24 is split (derived from MFFU's table: OBSERVED; "Tradovate rate" and "no re-run": INFERRED). Line 203 is CONTRADICTED. Lines 202 and 204 are at best INFERRED.
- Platform or routing fee for MFFU's NinjaTrader connection: NOT FOUND.

Rep-name and S13 checks:
```text
$ grep -ci "$N" /tmp/mffu-corr/w2.md
0
$ grep -c 'Fills are opt' /tmp/mffu-corr/w2.md
0
```
(The rep-name count for this report file is in the final check below.)

## Files staged
None. The brief says no git add and no index change. Two files were written, both left unstaged: this report and `/tmp/mffu-corr/w2.md`. Fetch dirs: `/tmp/mffu-fetch-41` to `/tmp/mffu-fetch-45`.

## Result
PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
