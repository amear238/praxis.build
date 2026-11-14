# Adversarial review: D-2026-11-13-D and D-2026-11-13-E (worker 3)

## Task
An adversarial check of /tmp/praxis-rl/entries.md (two new DECISIONS.md entries, 160 lines). It is checked against the source handoff `docs/reports/2026-11-13-hermes-handoff-strategy-search.md`, against DECISION_LOG.md:942-:944, against every cited line, and against the temp-index staging mechanics. Nothing was fixed.

## Mode
ADVERSARIAL

## Criterion
S1, S2, S4, S5, S6, S8 and S13 (specs/SPEC_RUBRIC.md), plus brief items 1-8.

## Defects

1. **BLOCKING (S2/S8): D-2026-11-13-D credits Amear with more than his words, and more than the authorisation row lists.** D's Status line says: "Rulings (1)-(5) are Amear's, in the wording the channel gives them. ... The bold labels and the DECISIONS.md line citations inside it are the channel's." That makes every other sentence in the rulings block (handoff :41-:45) his. Some of those sentences are in none of his quotes (handoff :9, :13-:15). They are also not in the authorisation row's own list of the rulings (DECISION_LOG.md:944: "(4) the trade-count gap is explained by the 09:30 vs 08:30 open, with its bearing on R1's re-run clause recorded; (5) the 2026-10-28 rule (DECISIONS.md :1010) still binds agents"):
   - ruling 4: "Record the bearing; it does not change Noise-Area's status." This is a strategy-status statement credited to Amear.
   - ruling 5: "The VM agent stays Hermes over SSH (D-2026-11-10-C, :2076)."
   - ruling 1: "This changes the research standard every brief since April has used (...)" and "Indicator-based strategies are now in scope."
   The entry also contradicts itself. Under Ruling 1 it treats the "every brief since April" sentence as "the channel's description", but the Status line credits the block to Amear. A reader cannot tell which sentences in the block are Amear's. The approval behind it (DECISION_LOG.md:942, "go from here ... include fore it to kiill this session and that i have approved") is read by that same row as "Amear approves Hermes killing it". Reading it as approval of the handoff's ruling text is the master's reading (DL :944 "then approved here"). It is not Amear's words. The entry states it as "Amear's approval", with no evidence level.
2. **MINOR (S1, citation): D7 line range is off by one.** Under Ruling 4, D cites "D7 (DECISIONS.md:1942-:1943)" for "The Noise-Area baseline continues through the VM tests for the record, but a GO on MFFU is not expected from it." At HEAD that text is at :1943-:1944. Line :1942 is "pull R6's research (higher-win-rate, steadier-equity strategies)". The Ruling 1 cite, :1940-:1944, is correct.
3. **MINOR (S1, factual): the OppBand entry times are misstated.** D says "the first and last five OppBand entries listed in that report (three-strategy results :174-:181) are at 10:01". At HEAD, #5 (:178) enters at 11:31, #806 and #807 (:179-:180) at 11:01, #809 (:182) at 11:31 and #810 (:183) at 11:01. The last five run to :183, not :181. The conclusion D draws, that no entry is near 08:30, still holds. The stated fact and the line range do not.
4. **MINOR (S1, citation): :1556-:1558 does not support the gates it is cited for.** E cites "DECISIONS.md:1556-:1558" for the Block 2 gates (OOS PF >= 1.30, >= 250 OOS trades, Sharpe, PBO). At HEAD those lines are R2 (arm (a) carries GO) and R3 (gate 6 WFE applies to arm (b)). They contain no PF, trade-count or Sharpe figure. The figures are at WF spec :153-:159, and PBO < 0.05 is at :1747. Both are also cited, so the claim is supported, but not by :1556-:1558.
5. **MINOR (S5/S2): the authorisation for the skip list and the commission rule is stretched.** E says DL :942's "same row's item (3), 'start the strategy search loop (step 4)', carries the skip list and the commission rule". Item (3) of DL :942 is "the master writes a Hermes resume handoff ... It tells Hermes to ... start the strategy search loop (step 4)". It names neither the skip list nor the commission rule. Saying item (3) carries them is the filer's inference, stated as fact. E does mark the two as channel text adopted under D1, so the label itself is sound.
6. **MINOR (S2 evidence level):** D says "The 4-hour build timer was already paused when this entry was written". The only evidence is DL :942's "The 4-hour build timer stays paused." That is a master statement, so it is REPORTED, not OBSERVED. The entry gives no evidence level.

Not defects (checked and holding): F3 is stated FROZEN and is not claimed cleared, in both entries. "Downstream of `4uu`" is left open for Amear. 2a's reference and the VM Claude Code session's re-use are left to Amear. E is labelled PROPOSED BY the channel, adopted by master under D1, changeable by Amear, and "NOT Amear's ruling". The bead counts under "UNCLEAR, 36 beads ... 20 agent-harness" were not re-counted: UNVERIFIED by me.

## Process log
- Read entries.md (all 160 lines), the handoff (all 113 lines) and DECISION_LOG.md:942-:944.
- Ran a Python script for exact-substring checks (items 1, 2, 4 and 6).
- Checked every DECISIONS.md citation against `git show HEAD:DECISIONS.md`.
- Spot-checked more than 8 other file:line citations at HEAD: 25 lines across 9 files.
- Ran the item 7 mechanics.
- Checked D-2026-10-30-A, D-2026-11-02-A and D-2026-11-08-D D4 headings, F3 at rubric :17-:31, and `bd show Praxis_build-ckh` (read only).

## Verification evidence (pasted)

Items 1, 2, 4 and 6 (python -I exact substring; footer counts):
```
handoff :9-:9 len=594 in_entries=True count=1
handoff :13-:15 len=601 in_entries=True count=1
handoff :41-:45 len=1089 in_entries=True count=1
handoff :67-:69 len=721 in_entries=True count=1
handoff :71-:88 len=1377 in_entries=True count=1
  quote@:9 in_entries=True: "Just rewrite the handoff. I'm going to give it to the Hermes"
  quote@:13 in_entries=True: 'yesterday I basically changed the parameters so that it only'
  quote@:14 in_entries=True: 'I just manually put it in there.'
  quote@:14 in_entries=True: "I didn't lift it. ... that still exists."
  quote@:14 in_entries=True: 'Or if I determine that I will bypass the rules. Those rules '
  quote@:15 in_entries=True: "The other session did stop. It's just, oh, I just didn't act"
  inline in handoff=True: the restriction of it being peer-reviewed is no longer a criteria that's needed
  inline in handoff=True: Have the loop run within Claude Code
  inline in handoff=True: I didn't lift it. ... that still exists.
  inline in handoff=True: Those rules are for you, not for me.
DL present=True count=1: go from here and give me a handoff for hermes to resume at 4am tomorro
DL present=True count=1: The 4-hour build timer stays paused.
DL present=True count=1: The contender bar and the overfitting guard (handoff :71-:88) are PROP
DL present=True count=1: (b) the five 2026-11-13 evening rulings appended to DECISIONS.md, file
DL present=True count=1: start the strategy search loop (step 4)
D footer count 1 ends with footer True
E footer count 1 ends with footer True
rep-name count: 0
     160 /tmp/praxis-rl/entries.md
```
Handoff :11 is "(transcribed, so the wording may be slightly off)", matching D's note.

Item 3, DECISIONS.md at HEAD (`git show HEAD:DECISIONS.md | sed -n 'Np'`, cut to 700 characters):
```
--- 1010
- **Item 2 — in-VM automation.** The "Oct 28 ruling" is ruling (1) of ... In his words it is "lifted COMPLETELY once two tests pass; until then it stands." ...
--- 1015
  - **State:** the repo holds no specification of test 2a or 2b and no record of either being run. ...
--- 1063
Rulings 1. ... 2. Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — ...
--- 1087
| 4 — test 2a reference | "test 2a reference = 1,190 trades / $197,327.60 on NQCONTROW SEP25, exact match" | ...
--- 1419
- T7 (spec :192): before every batch. Pass: the tab's commission template, backtest type, fill resolution and slippage read back as set ($2.96 acceptance, $4.68 walk-forward).
--- 1551,1558
R1  RTH = 09:30–16:00 ET (answers §4 item 1, B1). Arms (a) and (b)
    anchor at the 09:30 ET cash open. VM step 0 reads the live
    "CME US Index Futures RTH" template hours (T7 readback). If the
    live template starts 08:30 ET, the 2026-11-01 baselines are
    suspect and are re-run at 09:30 ET before either arm counts.
R2  GO requires arm (a) to pass. Arm (b) can only add confidence or
    block a GO; it can never carry a GO on its own (§4 item 3).
R3  Gate 6 (WFE) applies to arm (b) only (§4 item 3).
--- 1735,1740
A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80%
    of the ruled limit, i.e. below the lower of 3.2% of the MFFU
    account size and 80% of MFFU's trailing drawdown limit. ...
    Evaluated against every tier row; tier pick stays Q9. ...
--- 1746,1751
A7  R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not
    applicable). Arm (b) on gates 1-6 plus PBO < 0.05.
A8  ...
A9  File the 2026-11-08 strategy filter audit as an input to F2.
--- 2076
## 2026-11-10 — D-2026-11-10-C: VM agent = Hermes over SSH (settlement 3 changed; master under D1)
--- 2176
## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; ...
--- wt vs head 1-2279
SAME
```
Defect 2 evidence:
```
  1942	    pull R6's research (higher-win-rate, steadier-equity strategies)
  1943	    forward to P0. The Noise-Area baseline continues through the VM
  1944	    tests for the record, but a GO on MFFU is not expected from it.
```
Non-DECISIONS spot checks at HEAD (25 lines, 9 files):
```
vm-queue :5   Source: the VM Claude Code session's own report, pasted to this channel by Amear at 14:37 ET (REPORTED BY Amear; ...
vm-queue :15  | T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615 | -$38,905.64 | Exact match |
vm-queue :16  | T2 | OppBand | 1,112 | $188,618.48 | 1.2861 | -$37,906.24 | ...
vm-queue :29  3. **`run-queue.ps1` was not used:** it needs the `claude` command, which is not installed on the VM. ...
vm-queue :42  3. **Later, not today:** Analyzer tabs for `PraxisNoiseAreaBreakout_Flat1559` and `PraxisLastHalfHourMomentum`, ...
filter :4     **Status:** recommendation only. Every outcome below is **PROPOSED** pending Amear's approval. ...
filter :57    | A4 | Post-2018 / algo-impact survival | ...
filter :58    | A5 | Source tiering (peer-reviewed or institutional; no course sellers) | ...
D6 :31        | Rapid 50K, Rapid EOD 50K, Pro 50K, Builder 50K | $1,600 | FAIL all | FAIL all |
D6 :32        | Builder 50K add-on | $1,200 | FAIL all | FAIL all |
D6 :222       ... | four-measure (values spec 6): FAIL  fails=[16, 17]
WF spec :3    # Walk-forward test specification — NQ Noise-Area, arms (a) and (b)
WF spec :31   - *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. ..."*
WF spec :154  - OOS profit factor ≥ 1.30   (:155 Sharpe ≥ 1.0, :157 ≥ 250 aggregate OOS trades)
values :82    - 252 / 63 / 63 sessions — RULED ...
values :124     3. Max drawdown ≤ 4% of equity
3-strat :41   ... 07-10 = `PraxisNoiseAreaBreakout` (1190 rows), 07-57 = `..._OppBand` (810), 07-59 = `..._Flat1559` (1190), 08-00 = `PraxisLastHalfHourMomentum` (1304). ...
3-strat :178  | first 5 | 5 | Short | 2021-04-14 11:31 -> 16:00 | ...
3-strat :179  | last 5 | 806 | Short | 2026-07-01 11:01 -> 16:00 | ...
3-strat :182  | last 5 | 809 | Long | 2026-07-14 11:31 -> 16:00 | ...
3-strat :183  | last 5 | 810 | Short | 2026-07-15 11:01 -> 16:00 | ...
brief :11     3. **Sources.** Vendor documentation, exchange documentation, peer-reviewed papers, and public GitHub repositories count. ...
voice :62     Why it happened: every research run screened ideas by published, peer-reviewed evidence on NQ after 2018. ...  (header: "Written by praxis-master")
o78 :210-212  -----CME US Index Futures RTH ... ('Monday', '830', 'Monday', '1600') ...
rh2 :61       ... when sessions start at the 08:31-stamped bar. ...
.gitignore:7  Redemtion/
```
Other checks:
```
peer-review grep: 0
12-B at HEAD: HEAD:DECISIONS.md:2315 mention only ("parked D-2026-11-12-B"); no entry heading
rubric :17 ## FROZEN ...  :23-24 "The Block 2 spec requires Order Fill Resolution = High with a / 1-tick resolution series, 1-tick slippage, $2.96 round-trip."  :31 **Blocks.** `4uu`. Everything downstream of `4uu`.
247:## 2026-10-30 — D-2026-10-30-A: F3 backtest fill resolution (CONDITIONAL, void clause live) + ... 2 ticks/side ...
368:## 2026-11-02 — D-2026-11-02-A: R-VN3-1 — `PraxisLastHalfHourMomentum` RETIRED ...
1919: D4  Loop: a Hermes timer starts a fresh Code session every four hours.
bd show ckh: "2026-11-12 PARKED (absolute park rule, audit-fail-x2) ... A human resumes"
```
Item 7 mechanics:
```
a) head-2365 diff:
EMPTY
b) blob tail vs entries:
EQUAL
c) wt tail160 vs entries:
EQUAL
    2617
    2457
d) wt 2280-2371 vs before:
EQUAL
wt[1..2457]==before EQUAL
wt[2372..2457]==HEAD[2280..2365] EQUAL
e) name-status:
M	DECISIONS.md
f) numstat:
160	0	DECISIONS.md
g) canonical hash:
5bec276bb584840d96d0beb3e8c274e5896cb028631076290af40476dc291100  -
h) hash-object vs index:
5b51a4dfc61c261b6d3c5e0e7bd8f033efd0e416
100644 5b51a4dfc61c261b6d3c5e0e7bd8f033efd0e416 0	DECISIONS.md
i) HEAD grep D/E:
       0
```

## Per-item table

| # | Item | Result |
|---|---|---|
| 1 | Amear quotes byte-identical | PASS |
| 2 | Rulings, bar/guard and skip/commission blocks byte-identical | PASS |
| 3 | DECISIONS and other citations | FAIL (defects 2, 3, 4; all MINOR) |
| 4 | DECISION_LOG inline quotes byte-present in :942-:944 | PASS |
| 5 | Labels, S2, S8 | FAIL (defect 1 BLOCKING; defect 6 MINOR). F3 FROZEN and the 4uu question left open: PASS |
| 6 | S13 footer once per entry; rep-name count 0 | PASS |
| 7 | Mechanics | PASS |
| 8 | Other: S4 chain, S5, S6 coverage | FAIL (defect 5 MINOR). S4 chain and S6 coverage (WF spec, values, D7, ckh, fgd, F3, F4): PASS |

## Files staged
None. Only this report was written. The real index, the temp index and tracked files were not touched.

Result: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
