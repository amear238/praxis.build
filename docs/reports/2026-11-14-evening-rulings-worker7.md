# Evening rulings D-2026-11-13-D / -E — adversarial pass (worker 7)

## Task
Adversarial review of /tmp/praxis-rl/entries.md (160 lines; D-2026-11-13-D at :2-:92, D-2026-11-13-E at :94-:160) against the source handoff `docs/reports/2026-11-13-hermes-handoff-strategy-search.md`, DECISIONS.md at HEAD 9ff8a48, and DECISION_LOG.md:942-:944. First, re-check the six defects the prior pass raised. Then a fresh pass over items a-f.

## Mode
ADVERSARIAL. Read-only. Nothing was fixed or edited. The only file written is this report. Nothing was staged in the real index, and nothing was committed.

## Criterion
S1 (pasted evidence), S2/S8 (no credit to Amear beyond his quoted words, no answer to a question that is his, evidence levels stated), S6 (cross-block), S13 (fills line), plus the mechanics of the temp index and blob.

## Process log
1. Read entries.md in full (`cat -n`), handoff :1-:20 and :36-:113, and DECISION_LOG :942-:944 (`sed -n Np`).
2. Printed the cited DECISIONS.md lines at HEAD (`git show HEAD:DECISIONS.md | sed -n`).
3. Spot-checked 20+ other file:line citations at HEAD or in the working copy.
4. Ran a bash script for the byte checks on blocks and quotes, the S13 count, the rep-name count, and the mechanics.
5. Checked rubric F3's line range, whether D7 fired, a phrase sweep, the divergence of the working copy from HEAD, and whether the referenced reports exist.

## Prior defects: re-check

| # | Prior defect | Current text (quoted from entries.md) | Verdict |
|---|---|---|---|
| 1 | D's Status credited all of rulings (1)-(5) to Amear; "approval" over-read | :4 "The numbered rulings (1)-(5) are the channel's wording of those words (handoff :41-:45) ... Any sentence in that wording that goes beyond his quoted words is the channel's, not his. Examples: ruling 4's "it does not change Noise-Area's status", ruling 5's "The VM agent stays Hermes over SSH", and ruling 1's "every brief since April". ... That the approval also covers filing these rulings is the master's reading, stated in the REPORTED BY field of DECISION_LOG.md:944 ("which Amear pasted into this session and then approved here"), not his words." | CURED |
| 2 | D7 cited at :1942-:1943 | :76 "D7 (DECISIONS.md:1943-:1944) "The Noise-Area baseline continues through the VM tests for the record, but a GO on MFFU is not expected from it."" HEAD :1943 holds "forward to P0. The Noise-Area baseline continues through the VM" and :1944 holds "tests for the record, but a GO on MFFU is not expected from it." The quote joins the two lines with one space. | CURED |
| 3 | OppBand entry-time claim wrong | :74 "the first and last five OppBand entries listed in that report (three-strategy results :174-:183) enter between 10:01 and 11:31, none near 08:30". HEAD :174-:183 entry times are 10:01, 10:01, 10:01, 10:01, 11:31, 11:01, 11:01, 10:01, 11:31, 11:01. | CURED |
| 4 | E cited :1556-:1558 for the Block 2 gate values | :149 "(the six gates at WF spec :153-:159; which arm is judged on which gates, DECISIONS.md:1556-:1558 (R2, R3) and :1746-:1750 (A7, A8))". HEAD :1556-:1558 is R2/R3, :1746-:1747 is A7, and :1748-:1750 is A8. | CURED |
| 5 | E stated that DL :942 item (3) "carries" the skip list and commission rule | :98 "It does not name the skip list or the commission rule. That it carries them, because they sit in step 4 (handoff :67-:69), is the filer's reading (INFERRED)." | CURED |
| 6 | Timer stated as "already paused" with no evidence level | :61 "The 4-hour build timer is stated as paused in the master's plan in DECISION_LOG.md:942 ("The 4-hour build timer stays paused."). That is REPORTED BY the master, and this unit did not observe the timer." :90 "the master reports the build timer paused" | CURED |

## Verification evidence (pasted command output)

### Cited DECISIONS.md lines at HEAD
```
$ H(){ git show HEAD:DECISIONS.md | sed -n "$1p"; }; for r in 1010 1015 1063 1087 1419 1551,1558 1735,1751 1940,1944 2076 2176; do ...; done
--- DEC:1010
- **Item 2 — in-VM automation.** The "Oct 28 ruling" is ruling (1) of `docs/reports/2026-10-28-voice-session-notes.md:7` (untracked file), "The in-VM automation approach is dropped. No more Cowork or in-VM Claude Code executor work.", taken onto the ledger at DECISION_LOG `2026-10-30T21:36:00Z` (WHO: amear). (filer's identification) DECISIONS.md has no entry for it. In his words it is "lifted COMPLETELY once two tests pass; until then it stands." How far "COMPLETELY" reaches beyond that ruling is not stated (NEEDS AMEAR 6). The two tests:
--- DEC:1015
  - **State:** the repo holds no specification of test 2a or 2b and no record of either being run. Nothing is downloaded, installed or run by this entry.
--- DEC:1063
Rulings 1. Bridge install (NEEDS AMEAR 2): ... 2. Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — by new DECISIONS entry amending the cost model. ...
--- DEC:1087
| 4 — test 2a reference | "test 2a reference = 1,190 trades / $197,327.60 on NQCONTROW SEP25, exact match" | ...
--- DEC:1419
- T7 (spec :192): before every batch. Pass: the tab's commission template, backtest type, fill resolution and slippage read back as set ($2.96 acceptance, $4.68 walk-forward).
--- DEC:1551,1558
R1  RTH = 09:30–16:00 ET (answers §4 item 1, B1). Arms (a) and (b)
    anchor at the 09:30 ET cash open. VM step 0 reads the live
    "CME US Index Futures RTH" template hours (T7 readback). If the
    live template starts 08:30 ET, the 2026-11-01 baselines are
    suspect and are re-run at 09:30 ET before either arm counts.
R2  GO requires arm (a) to pass. Arm (b) can only add confidence or
    block a GO; it can never carry a GO on its own (§4 item 3).
R3  Gate 6 (WFE) applies to arm (b) only (§4 item 3).
--- DEC:1735,1751
A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80%
    of the ruled limit, i.e. below the lower of 3.2% of the MFFU
    account size and 80% of MFFU's trailing drawdown limit. This
    amends D-2026-11-05-A item 3 with a safety buffer for model error.
    Evaluated against every tier row; tier pick stays Q9. Closes the
    notes-4 DD equity-base item.
...
A7  R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not
    applicable). Arm (b) on gates 1-6 plus PBO < 0.05.
A8  O1 is discharged by R2 + R3 + A7. Gate 6 formula (Pardo WFE):
    annualised OOS net profit / annualised IS net profit of the
    selected parameter set, pooled across all windows; pass >= 0.50.
A9  File the 2026-11-08 strategy filter audit as an input to F2.
--- DEC:1940,1944
D7  If D6 fails at every tier at 1 MNQ: do not design breaker values
    to fit the drawdown ceiling (that is curve-fitting). Report it, and
    pull R6's research (higher-win-rate, steadier-equity strategies)
    forward to P0. The Noise-Area baseline continues through the VM
    tests for the record, but a GO on MFFU is not expected from it.
--- DEC:2076
## 2026-11-10 — D-2026-11-10-C: VM agent = Hermes over SSH (settlement 3 changed; master under D1)
--- DEC:2176
## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.0 (ARM64) installed in the VM. Record only. Filed WHO: amear, REPORTED BY the Claude.ai channel.
```
(The :1063 and :1735-:1751 lines are trimmed with "..." in this paste only. The full output was shown in session.)

### Block and quote byte checks, S13, rep-name, mechanics (script output, verbatim)
```
BLOCK entries:11 == handoff:9 IDENTICAL
BLOCK entries:17,19 == handoff:13,15 IDENTICAL
BLOCK entries:25,29 == handoff:41,45 IDENTICAL
BLOCK entries:103,105 == handoff:67,69 IDENTICAL
BLOCK entries:111,128 == handoff:71,88 IDENTICAL
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [the restriction of it being peer-reviewed is no longer a criteria that's needed]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [Have the loop run within Claude Code]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [changed the parameters so that it only trades from 9:30 a.m. onwards]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [the back tests from November the first had the open via 8:30 a.m.]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [I didn't lift it. ... that still exists.]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [Those rules are for you, not for me.]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [I just manually put it in there.]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [I didn't lift it.]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [all builds]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [(PROPOSED; Amear can change it)]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [(PROPOSED)]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [dispatched by Hermes over SSH as on 2026-11-13]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [in Claude Code on the Mac]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [published, peer-reviewed evidence on NQ after 2018]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [walk-forward runs on existing strategies]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [it does not change Noise-Area's status]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [The VM agent stays Hermes over SSH]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [every brief since April]
PRESENT in 2026-11-13-hermes-handoff-strategy-search.md: [the three Noise-Area arms and Last-Half-Hour Momentum]
PRESENT in tmp.DvTCfIwF5Z: [go from here and give me a handoff for hermes to resume at 4am tomorrow oncethe run here is over. include fore it to kiill this session and that i have approved]
PRESENT in tmp.DvTCfIwF5Z: [Amear approves Hermes killing it]
PRESENT in tmp.DvTCfIwF5Z: [which Amear pasted into this session and then approved here]
PRESENT in tmp.DvTCfIwF5Z: [The 4-hour build timer stays paused.]
PRESENT in tmp.DvTCfIwF5Z: [The contender bar and the overfitting guard (handoff :71-:88) are PROPOSED BY the channel, not Amear's rulings; under D-2026-11-08-D D1 the master adopts them, and Amear can change them.]
PRESENT in tmp.DvTCfIwF5Z: [(b) the five 2026-11-13 evening rulings appended to DECISIONS.md, filed as WHO: amear, with the contender bar and overfitting guard filed as PROPOSED BY the Claude.ai channel]
PRESENT in tmp.DvTCfIwF5Z: [start the strategy search loop (step 4)]
PRESENT in tmp.DvTCfIwF5Z: [go from here]
--- S13 line count per entry
D (lines 1-93): 1  E (94-160): 1  total: 2  last line is it: yes  line92: yes
rep-name count entries.md: 0
--- mechanics
     160
diff HEAD vs blob head 2365:        0 lines
    2365
blob tail == entries
wt last160 == entries
wt minus last160 == wt.before (head -n 2457)
byte-prefix check ok
name-status:
M	DECISIONS.md
numstat:
160	0	DECISIONS.md
canonical hash:
51078141d3cb6dc759fe7dddfa77e89b0fc858cea3b1c6625729da21f953b387  -
hash-object blob: 8b5a22a0c6a681b1c5e607231ae5ab32f8fcb738
ls-files: 100644 8b5a22a0c6a681b1c5e607231ae5ab32f8fcb738 0	DECISIONS.md
git grep D/E at HEAD:        0
tail -c1 of blob / entries hex:
0a
0a
```
(The tmp.* file holds `sed -n 942,944p DECISION_LOG.md`.)

### Spot-checks (excerpts of the output)
```
--- docs/reports/2026-11-01-three-strategy-results.md:41
... 07-10 = `PraxisNoiseAreaBreakout` (1190 rows), 07-57 = `PraxisNoiseAreaBreakout_OppBand` (810), 07-59 = `PraxisNoiseAreaBreakout_Flat1559` (1190), 08-00 = `PraxisLastHalfHourMomentum` (1304). ...
--- vm-queue-results:5
Source: the VM Claude Code session's own report, pasted to this channel by Amear at 14:37 ET (REPORTED BY Amear; ...
--- vm-queue-results:11
Setup: Strategy Analyzer tab "PRAXIS baseline NQCONTROW 0930", PraxisNoiseAreaBreakout, NQCONTROW SEP25, 1-minute, 2021-03-08 to 2026-07-17, CME US Index Futures RTH 0930 ET, commission PRAXIS $2.96 round trip, slippage 2, Standard fill resolution, 1 NQ.
--- vm-queue-results:13-15
| T1 | BandOrVWAP | 1,173 | ... | Exact match |
| T2 | OppBand | 1,112 | ... | -61 trades, ...
--- vm-queue-results:29
3. **`run-queue.ps1` was not used:** it needs the `claude` command, which is not installed on the VM. ...
--- vm-queue-results:42
3. **Later, not today:** Analyzer tabs for `PraxisNoiseAreaBreakout_Flat1559` and `PraxisLastHalfHourMomentum`, ...
--- d6:31,32
| Rapid 50K, Rapid EOD 50K, Pro 50K, Builder 50K | $1,600 | FAIL all | FAIL all |
| Builder 50K add-on | $1,200 | FAIL all | FAIL all |
--- d6:222,224   ... four-measure (values spec 6): FAIL ...
--- strategy-filter-audit:4   ... Every outcome below is **PROPOSED** pending Amear's approval. ...
--- strategy-filter-audit:57,58   | A4 | Post-2018 / algo-impact survival | ... / | A5 | Source tiering (peer-reviewed or institutional; no course sellers) | ...
--- briefs/2026-11-04...:11   3. **Sources.** Vendor documentation, exchange documentation, peer-reviewed papers, and public GitHub repositories count. ...
--- .gitignore:7   Redemtion/
--- WF spec :3   # Walk-forward test specification — NQ Noise-Area, arms (a) and (b)
--- WF spec :31   ... "3. Max-DD gate base: the lower of 4% of the MFFU account size ..."
--- WF spec :153-:159   Block 2 header + 6 gates (PF ≥ 1.30, Sharpe ≥ 1.0, DD ≤ 4%, ≥ 250 OOS trades, ≥ 60% windows, WFE ≥ 0.50)
--- values :82   - 252 / 63 / 63 sessions — RULED ...   values :124   3. Max drawdown ≤ 4% of equity
--- WT voice-handoff:62   Why it happened: every research run screened ideas by published, peer-reviewed evidence on NQ after 2018. ...
--- rubric (HEAD) F3 heading at :19; :31 **Blocks.** `4uu`. Everything downstream of `4uu`.  (inside F3; F4 starts :33)
--- rubric :23-:24  The Block 2 spec requires Order Fill Resolution = High with a / 1-tick resolution series, 1-tick slippage, $2.96 round-trip.
--- D7 fired: HEAD:HANDOFF.md:487 **D6 result → D7 FIRED** ...; HEAD:STATUS.md:156 ... `f10603a` (D6 drawdown check; D7 fired) ...
--- phrase sweep "peer-reviewed evidence on NQ after 2018": only voice-handoff, hermes-handoff, evening-rulings-worker1, -worker3 (no brief)
--- Redemtion comeback plan .rtf:53 "Source exclusiv[ely from peer-reviewed ...]"; Phase2 prompts .md:47, :48 "no peer-reviewed NQ evidence post-2018"
--- o78 :208-:219  -----CME US Index Futures RTH / TimeZone ['Eastern Standard Time'] / ('Monday', '830', 'Monday', '1600') ...
--- claude-ai-2 :61  ... when sessions start at the 08:31-stamped bar ...
--- HEAD DECISIONS: :247 D-2026-10-30-A CONDITIONAL, void clause live; :368 D-2026-11-02-A LastHalfHourMomentum RETIRED; D-2026-11-12-B only a mention at :2315, no heading
--- working copy vs HEAD: "DECISIONS.md differ: char 414862, line 2280"; WT :2280 is "## 2026-11-12 — D-2026-11-12-B ..."
--- HEAD DECISION_LOG (921 lines) is a prefix of the WT DECISION_LOG (947)
--- docs/reports/2026-11-14-evening-rulings-manager.md: wt=no head=no
```

## Per-item table

| Item | Check | Result |
|---|---|---|
| prior 1-6 | all six defects cured (quotes above) | PASS |
| a | handoff :9 and :13-:15 quotes and every inline Amear quote byte-present; the blocks for :41-:45, :67-:69 and :71-:88 are byte-identical | PASS |
| b | :1010, :1551-:1555, :1735-:1740, :2076, :1015, :1063, :1087, :1419, :1556-:1558, :1746-:1750, :1751, :1943-:1944 and :2176 all match HEAD and the claims made about them. More than 20 other citations were spot-checked and match (D6 below). | PASS |
| c | DL inline quotes byte-present in :942-:944 | PASS |
| d | E is PROPOSED BY the channel, adopted under D1, changeable by Amear, and NOT his ruling. F3 FROZEN and not claimed cleared. "downstream of 4uu" is left to Amear. Residual MINOR S2 items D1-D3 below. | PASS (with MINOR) |
| e | one S13 line per entry, each the entry's last line; rep-name count 0 | PASS |
| f | blob prefix diff empty; blob tail = entries; WT tail = entries; WT minus 160 = wt.before; `M	DECISIONS.md`; `160	0	DECISIONS.md`; hash-object = ls-files (8b5a22a0...); git grep count 0 | PASS |

## Defects (numbered)

1. MINOR (S2, evidence level). Ruling 3 finding, entries :68: "The same file also says, at :29, that the `claude` command "is not installed on the VM", which conflicts with its own :5." The entry states a conflict as fact. A missing `claude` CLI on the PATH (the command `run-queue.ps1` needs) does not rule out a Claude Code session started another way, so this is a tension, not a proven conflict. It should carry the filer's-reading label or be worded "may conflict".
2. MINOR (S2/S8). Ruling 5, entries :78, ends with this sentence, which has no label: "Ruling 5 binds every agent this repo dispatches." It is the filer's scope reading. It goes beyond Amear's "Those rules are for you, not for me" and beyond the channel's "No agent runs Claude Code inside the VM". It comes straight after an S8 open question, so it reads as settling scope. It also leaves unnamed a tension in its own citations: :1010's rule is "The in-VM automation approach is dropped", while D-2026-11-10-C (:2076) makes Hermes, an agent, the VM agent. Whether Hermes-over-SSH bridge work counts as "in-VM automation" is not raised.
3. MINOR (S1/S2). Ruling 5, entries :78: "The record has no lift ... the filer's greps found none since." No command or output is given, and the unit report is not named. Compare ruling 1 (:53), which says "commands and output are in the unit report". No evidence level is stated.
4. MINOR (completeness, ruling 4 bearing). Entries :70-:71 cite vm-queue :11 only for the tab name, then say "the record holds no readback of the template's hours". The same line :11 names the trading-hours template as "CME US Index Futures RTH 0930 ET", a different template from R1's "CME US Index Futures RTH". The o78 rescued copy shows that one at `830`-`1600`. This bears directly on R1's literal "live template" condition and on the reading "R1's clause reads as triggered" (:72), but the entry does not record it.
5. MINOR (cosmetic). Entries :4 says "(handoff :41-:45), as DECISION_LOG.md:944 lists them". :944 says "as the handoff lists them at :40-:45". The block quoted is :41-:45, which is correct. Only the attribution of the range to :944 is slightly off.
6. MINOR (uncited). Entries :82 says "D7 pulled R6 forward to P0." D7 is conditional ("If D6 fails at every tier"). The fact that it fired is on record (HEAD:HANDOFF.md:487 "D6 result → D7 FIRED"; HEAD:STATUS.md:156), but the entry gives no citation.
7. MINOR, a precondition for the commit. Entries :80 and :154 say "Graded in full in `docs/reports/2026-11-14-evening-rulings-manager.md`". That file does not exist in the working copy or at HEAD (wt=no head=no), and the temp index holds only DECISIONS.md. If it is not filed by commit time, the S6 reference dangles. This becomes BLOCKING if the commit lands while the file is still missing.

Out of scope, reported and not fixed: the working-copy DECISIONS.md is not HEAD plus appended lines. It diverges from HEAD at line 2280 (WT :2280 is the D-2026-11-12-B heading, where HEAD has its 2026-11-13 entries). So DECISION_LOG :942's "92 appended lines" is inaccurate as a description, and after this commit the working copy and HEAD will still differ in entry order. The entry's own claim "Lines 1-2279 are the same in HEAD and the working copy" is correct. Separately, HEAD DECISIONS.md :394 and :467 cite F3 as `specs/SPEC_RUBRIC.md:45-57`, but F3 sits at rubric :19-:31 at HEAD. That is a stale citation in earlier entries, not in this artifact.

UNVERIFIED: the bead lists and counts in ruling 2 (36 UNCLEAR, 20 harness or guard). `bd` was not run, because the brief makes beads read-only and I did not confirm that `bd list` makes no writes.

## Canonical hash
`51078141d3cb6dc759fe7dddfa77e89b0fc858cea3b1c6625729da21f953b387`

## Files staged
None. The real index is untouched. Only this report was written, and it is untracked.

## Result: PASS
No BLOCKING defect was found. All six prior defects are cured, and the seven MINOR items are listed above. Defect 7 becomes BLOCKING if the referenced manager report is not filed by commit time.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
