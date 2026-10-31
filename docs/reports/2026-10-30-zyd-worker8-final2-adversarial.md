# Praxis_build-zyd — worker8 final adversarial (after fix pass 3)

## Task
Attack D-2026-10-30-A (DECISIONS.md), the `config/backtest-cost-model.json` diff and the MANIFEST rows after :132. Criteria: bead zyd acceptance (a)(b)(c), rubric F3 `specs/SPEC_RUBRIC.md:45-57`, S2, S4/S5, S6, S8. Focus: the fix-pass-3 edits.

## Mode
ADVERSARIAL, read-only. The only write is this report. Nothing staged.

## Attacks with pasted output

### A1. Mechanical checks (all pass)
```
$ python3 -I -m json.tool config/backtest-cost-model.json >/dev/null && echo OK
OK
cost_model {... 'slippage_ticks_per_side': 2, 'slippage_usd_per_side': 10.0, 'slippage_round_turn_ticks': 4, 'slippage_round_turn_usd': 20.0, 'fill_resolution': 'Standard', 'total_cost_per_round_turn_usd': 22.96, 'total_cost_per_round_turn_ticks': 4.592}
python3: round(2.96+2*2*5,2), round(2.96/5+4,3) -> 22.96 4.592
$ git diff DECISIONS.md MANIFEST.md | /usr/bin/grep -c '^-[^-]'
0
void clause, entry vs DECISION_LOG 2026-08-29T00:10:00Z (python, .encode() compare): IDENTICAL
21:36:30Z copy vs 00:10:00Z: IDENTICAL
MANIFEST paths: 17 OK; MISSING only /docs/reports/2026-10-30-zyd-f3-artifact.md (excluded by brief)
webp sha256 8787483dcb41fbc0d52c023faeb32ff3606075a8fa518126749b1a4da90eac55 (matches row)
voice notes: git ls-files --error-unmatch -> "did not match any file(s) known to git" (row's "untracked" is true)
code sha256 35393823e9bc...2242752265; :105 OnBarClose, :108 IsExitOnSessionCloseStrategy = true, :189, :196-198, :200, :211/:219/:227/:229/:288/:290 all match
order grep: only Enter*/Exit* at 211/219/227/229/288/290 (+comments 224/225); no Set*/Submit*/Limit/Stop* order call
import file: 1857362 lines; head 20210307 180100; tail 20260720 112700 (matches (a))
```
The citations also check out: rubric `:55-56` (Unblocks when), O4 `:94-99`, SHM `:47-50`, F4 `:45` / `:151`, Q5/Q6/Q9 at DECISIONS `:185/:186/:189`, 3gm `:710`, `:737-773`, `:1164-1173`, `:1185-1207`, and `:949` ("DECISION_LOG:442 locks `[N]` as **band-edge** slippage …"; line 442 = row 21:36:30Z). The worker verdict lines in MANIFEST also match: w2 `:230`, w4 `:93`, w6 `:87` are all BREAK FOUND, and w4 grades M1/M2 "RESOLVED (… residue)".

### A2. The contrary hypothesis at `:784`, against its own source context
```
$ sed -n '775,786p' docs/reports/2026-10-30-3gm-fidelity-check.md   (excerpt)
## D4 — Run 1 (48 trades) vs run 2 (41 trades): NOT resolved
...
Ranked hypotheses, all INFERRED:
...
2. **Exit on session close** or **Time in force** differed. ... A position carried overnight changes the next day's `Position.MarketPosition` at checkpoints, which changes whether entries fire.
...
5. **Order fill resolution** High vs Standard. This could change how same-bar exit+reverse pairs and the 16:00 orders resolve.
```
Hypothesis 5 is offered as a cause of a different **trade count** (48 vs 41). Hypothesis 2 sets out the mechanism: a changed position state "changes whether entries fire". In this code, entries depend on position state, because `Position.MarketPosition` is read at 201/226/228 (3gm positive control, rows 22:16/22:40).

Entry (c), as it now reads:
> "… so Standard's intrabar High-vs-Low ordering assumption would not decide whether or when an entry or exit order is sent. … Contrary hypothesis on record, not resolved: 3gm D4 hypothesis 5 (`:784`, INFERRED) holds that Order fill resolution High vs Standard could change how same-bar exit+reverse pairs and the 16:00 orders resolve. So the fill-resolution choice may still bias how NT8 fills those two cases"

The config note has the same narrowing: "…does not decide whether or when an order is sent, is INFERRED; 3gm D4 hypothesis 5 (INFERRED) holds that fill resolution could still change how same-bar exit+reverse pairs and the 16:00 orders resolve."

Worker6's F-1 fix text asked for the linkage "and through them later entries". It also asked for "(c) holds only for the checkpoint decision itself, not for how those two order pairs execute". Neither made it into the entry.

### A3. Void-clause paragraph against row 21:36:30Z and the S8 list
```
row 442 (21:36:30Z): **Void-clause status (REPORTED BY AMEAR, not observed by the master):** ... never exercised; ... The clause is NOT triggered; it is also NOT retired, since no run has set High.
row 347 (00:10:00Z): ... whether NT8 silently falls back to Standard when `Order Fill Resolution = High` is set ... "If the VM measurement shows NT8 errors or demands a secondary series ..."
```
Entry:
> "The clause's trigger is "the VM measurement", which has not been run (REPORTED: no run has set High, 21:36:30Z); … Whether a High run is the trigger is Amear's."

The re-attribution to the REPORTED BY AMEAR block is accurate (worker6 F-3, first half, resolved). The second half is not resolved, though. "Has not been run" is true only if "the VM measurement" means "a High run", and the entry's own last sentence leaves that to Amear. Runs 1–4 were VM Analyzer runs, and none errored or asked for a secondary series. Under the other reading the measurement has been run. The ledger never says "the VM measurement has not been run". It says "no run has set High".

### A4. NEEDS AMEAR 2, "first ledger writing", checked against the ledger
```
$ grep -n "\[N\]" DECISION_LOG.md | awk -F: '$1<442'  -> lines 347 353 373 379 389 441
row 441 [2026-10-30T21:36:00Z] **WHO: amear** ... (3) F3 `[N]` = **2 ticks per side** — recorded in its own row below.
```
Entry NEEDS AMEAR 2 says: "its first ledger writing is the `2026-10-30T21:36:30Z` row". In fact row 21:36:00Z (WHO: amear) writes `[N]` = 2 thirty seconds earlier.

### A5. Residual bullet 3 attribution
Entry: "same-bar exit+reverse resolution; early-close days (both CANNOT-DETERMINE-STATICALLY, INFERRED) — fill resolution may bear on this (3gm `:784`, INFERRED)." `:784` (pasted in A2) names same-bar exit+reverse pairs and the 16:00 orders. It does not mention early-close days.

### A6. Other checks, no break
- The Status line reads "the commit is Amear's". It matches 21:36:30Z HOW ("the commit is Amear's") and 22:40 ("Commit is Amear's"). It does not claim the entry is committed.
- Addresses: "not a grade", and F3 satisfaction is left to NEEDS AMEAR 2. No S8 breach.
- NEEDS AMEAR 6 matches its source. 21:36:30Z says "band-edge slippage = 2 ticks per side ($10/side …; ≈ $22.96 per round trip)", and 3gm `:949` reserves the scope question for Amear.
- Scope-of-change bullets match the diff: `amended` added, 4 note/ref keys changed, no key removed, and `applies_to` / commission / instrument / `bead` / `created` unchanged (python key dump).
- "Amear's own framing (00:10:00Z) was stop-cluster adverse selection" matches row 347 ("at exactly the price level where other participants' stops rest"). "The master's note … INFERRED from source, pending 3gm" matches row 442.
- The S6 consumers are all named: applies_to (3 items, verbatim in substance), D-2026-07-04-B, SHM-4/Q9, O4, the Python MC, and F4 `:151`.
- No label upgrade found in the MANIFEST Purpose cells. The 3gm row's "re-audit PASS … strike one" matches 22:40. "Run 3 ruled INVALID" matches 22:22 (amear).

## Findings

**F-1 MAJOR (S2 + bead (c) honesty; DECISIONS.md (c) and config `fill_resolution_note`).** The contrary hypothesis is narrowed so that it no longer contests the headline. In its source, `:784` is a candidate cause of a different trade count. Its sibling `:780` gives the path: a changed position "changes whether entries fire". The entry reports it only as "may still bias how NT8 fills those two cases". It keeps, unqualified, the claim that the fill-resolution assumption "would not decide whether or when an entry or exit order is sent". The (c) heading, "does not decide which orders this strategy sends", says the same thing. The graded source's own hypothesis disputes that claim: through the post-reversal and post-16:00 position state, it could decide whether later entries are sent. So the entry does not honestly state how far (c) gets. It concedes a fill-price residual and leaves out the order-selection residual its source raises. The config note repeats the narrowing. Worker6's F-1 fix text ("and through them later entries"; "(c) holds only for the checkpoint decision itself") was not carried in. The label stays INFERRED and the R3 control is named, so this is MAJOR, not BLOCKING.

**F-2 MINOR (S8 / internal contradiction, void clause).** "The clause's trigger is 'the VM measurement', which has not been run" decides the trigger's meaning (measurement = a High run), and the next sentence reserves that same question for Amear ("Whether a High run is the trigger is Amear's"). The parenthetical "(REPORTED: no run has set High)" supports "no High run". It does not support "the VM measurement has not been run". This is a residue of worker6 F-3. Rated MINOR because the deferral sentence is present.

**F-3 MINOR (S4, NEEDS AMEAR 2).** "Its first ledger writing is the 21:36:30Z row" is false. Row 21:36:00Z (WHO: amear, line 441) records "`[N]` = **2 ticks per side**" first. The timing question to Amear is unaffected, since both rows come after runs 1–3.

**F-4 MINOR (S2 citation scope, residual bullet 3).** "Early-close days … fill resolution may bear on this (3gm `:784`)". `:784` does not mention early-close days.

**F-5 MINOR (S2 omission).** (b) and the config give dollar figures ($10/side, $22.96 RT) for a backtest run on NQCONT. Neither carries 3gm's caveat that NQCONT's $20 point value is UNVERIFIED (`:949` "Its dollar effect also depends on the UNVERIFIED NQCONT point value"; D3 condition 4). These are cost-model numbers, so this is not a label upgrade, but a consumer reading $22.96 as the backtest's realised cost is not warned.

**F-6 MINOR (S8-adjacent).** "Unblocks: review and closure of Praxis_build-zyd". Closure needs (c) met, and the entry itself asks (NEEDS AMEAR 5) whether (c) can "stand as INFERRED". "Unblocks … review" would be accurate. "Closure" assumes the answer.

## NOT CHECKED
- The full text of the 3gm D2(c) section for the "next bar may be the next day's 09:31" wording. Checked only through the master's 22:22 row summary.
- Whether `D-2026-07-04-B` itself mentions slippage. Only the heading at DECISIONS `:43` was located.
- MANIFEST tier column ("2") semantics and the column conventions of earlier rows.
- Worker7's fix-3 report. Edits were graded against sources, not against worker7's claims.
- The bead's (c) wording against any later bead update. `bd show` shows Updated 2026-07-25.

## Result / VERDICT
One MAJOR (F-1) and five MINORs (F-2 to F-6). All mechanical checks pass.

VERDICT: BREAK FOUND
