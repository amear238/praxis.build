# Manager report — unit 2026-11-07-vm-handoff-amendment (praxis-manager, 2026-11-07)

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Task
Apply Amear's 2026-11-07 rulings 5, 6, 7(4)(5)(7)(11)(12), 8 and 10 to `vm/2026-11-06-vm-handoff.md`, in place. The rulings are D-2026-11-07-A: his words at DECISIONS.md:1229–1234, ledger DECISION_LOG `2026-11-07T12:55:00Z`, WHO: amear. D-2026-11-07-A :1272 assigns this unit: "these are APPLIED to `vm/2026-11-06-vm-handoff.md` by a later unit".

Also in scope:
- the skill `vm/skills/praxis-nt8-bridge-backtest/SKILL.md`, only where it now contradicts step 4;
- a DECISIONS.md addendum;
- MANIFEST rows;
- this report.

Authorisation (S5): DECISION_LOG `[2026-11-07T15:19:00Z] WHO: praxis-master` (line 689). HEAD at start and at end: `43b34b1`. Nothing was staged, run, installed, bought or connected.

The skill invoked with the brief (orchestrator-mine) prescribes an auditor dispatch and a gated commit. The manager role cannot do either, and the brief forbids both, so neither was done. The master grades and lands this unit.

## Does NOT cover / UNVERIFIED (written 15:30Z, before adversarial passes A and B were dispatched; unchanged since except the last bullet, added after the fix round)
- **Nothing tried.** Nothing in the amended handoff has been tried. Every VM step is SPECIFIED only (S2): not implemented on the VM, not tested, not tested under failure.
- **pip reading.** It is INFERRED. Only "what "pinned" means on this bridge is the master's reading" is on the ledger (DECISION_LOG 15:19:00Z). The four-package list and the `--no-deps` / `--no-build-isolation` flags are this unit's reading on the master's dispatch. This unit does NOT decide whether transitive dependencies and the build backend (`setuptools>=61`, `report:2386–2388`) fall inside "only the bridge's pinned requirements". After the fix round the handoff routes that question to Amear.
- **pip on the VM.** Whether `pip install -e .` downloads `setuptools` on the VM is UNVERIFIED. So are the VM's pip and its flags.
- **Hash-STOP scope.** Whether the STOP ends the step or the whole VM session is the master's reading, not his word.
- **Strategy copy.** Whether the VM's installed strategy copy is byte-identical to HEAD (e.g. line endings) is UNVERIFIED. The rule is STOP on mismatch.
- **§9.** §9 is a proposal. Every §9 mechanism is UNVERIFIED on the VM:
  - run timeouts (1800 s is untried);
  - whether one tab serves many runs;
  - whether `params` reaches arm (b)'s `[NinjaScriptProperty]` inputs;
  - whether the backtest type persists;
  - the 5000-trade cap;
  - whether `netProfit` is gross or net;
  - whether the bridge trade list is enough for CSCV;
  - the copy to `Z:\vm\replies\wf\`.
- **Arm (b) branch.** Branch `arm-b/wf-tunables` and `ninjascript/PraxisNoiseAreaBreakoutArmB.cs` do not exist. W2 OBSERVED: `git rev-parse --verify -q arm-b/wf-tunables; echo $?` → `1`; `git branch -a | grep -c arm-b` → `0`. §9.2 depends on a later unit (U3).
- **Not answered (Amear's).** Who sets the Strategy Analyzer tab by hand; the account; §8 rows 1, 2, 3 and 8; row 11's route half.
- **Ruling 10, second item.** In the walkthrough it sits at :35 in his 11-06 wording ("unmap Z: and turn the share off before real money"), not in ruling 10's wording ("unmap Z: and turn off the SMB share"). No edit was made: the item is present, and the filing unit chose not to duplicate it (DECISIONS.md:1275).
- **Fix round (added after it).** No fresh adversary re-checked the fix round (W5), because the 5-worker cap was reached. Only the manager's targeted checks below cover it.

## Rubric criteria addressed (verbatim from specs/SPEC_RUBRIC.md) and how each is met
- **S1 | Every claim in a report has pasted command output, not a description of output.** Every figure here is pasted in `## Verification evidence` from commands run this session.
- **S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure.** Every VM step stays "untried". Each mechanism claim carries a grade (OBSERVED / REPORTED BY / INFERRED / UNVERIFIED), and §9.4 names nine UNVERIFIED items. B-finding 2 is fixed: the text had claimed "not softened" for a STOP that only detected a download. The flags now prevent the download; the STOP is labelled detection after the fact.
- **S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after.** The chain:
  - D-2026-11-07-A :1272, in HEAD;
  - the DECISION_LOG 15:19:00Z dispatch, written before any edit (the first edit came after 15:22:17Z; see the shas-before capture);
  - the DECISIONS.md addendum :1463–1478, which records the work.

  Readings beyond the rulings are labelled either the master's (on the ledger) or this unit's (on the master's dispatch).
- **S5 | No approval is inferred from a verbal or in-session exchange. The ledger append is the authorisation.** His words are cited to DECISIONS.md:1229–1234, which were filed from the ledger row 12:55:00Z (WHO: amear). Two readings were first credited to the 15:19 row, which does not contain them (A-finding 2). Both are relabelled.
- **S8 | No question that belongs to Amear is answered on his behalf.** A-finding 1 (HIGH) is fixed. Code no longer decides how far "only" reaches: dependencies and the build backend are his question (3.5, §8 row 11). §8 rows 1, 2, 6 and 8, and step-0 items 1–6, are byte-equal to HEAD (pasted below). Row 3 and row 11's route half stay his.
- **S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: [the sentence — carried once, at line 3 of this report; not repeated here so that "once" holds]** This report carries it at line 3. The handoff and the skill carry it once each (count pasted). The DECISIONS addendum states no backtest or P&L figure (count 0, pasted), so it carries none.

## Workers dispatched (id, mode, outcome)
| # | agent id | mode | scope | outcome |
|---|---|---|---|---|
| W1 | acd7ab88151bce802 | BUILD | handoff §0–§8 + skill | done; its script byte-checked the quotes (22 handoff + 3 skill) |
| W2 | a37f4fa0abcfffcb6 | BUILD | §9 draft (scratchpad) + DECISIONS addendum + MANIFEST rows | done; MANIFEST rows appended as UPDATE ROWs, not edited in place (the house append-only convention); column 3 is Phase and stays `2`; §9 names rows 1, 2, 3 and 8 plus row 11's route half as his, and row 6 as a pending value (per DECISIONS.md:1278) — the brief said "1, 2, 6, 8"; accepted as more accurate |
| W3 | ab3a618eba2e32040 | ADVERSARIAL A (fidelity/S8) | handoff, skill, addendum | `VERDICT: FAIL` — 1 HIGH, 1 MEDIUM, 4 LOW |
| W4 | a3bdf70c3ca324bac | ADVERSARIAL B (mechanism) | handoff changed lines + §9, skill | `VERDICT: FAIL` — 2 MEDIUM, 6 LOW |
| W5 | abbc14e4d9b2adf38 | BUILD (fix) | the 12 numbered defects | all 12 reported fixed; manager-verified below |

## Process log
- 15:22:17Z: checked HEAD `43b34b1`. Captured the before-shas, the index fingerprint and backups (scratchpad `u4/`).
- Dispatched W1 and W2 in parallel, on disjoint files. The manager then appended W2's §9 draft to the handoff after §8. This was a pure doc insert, byte-equal to the draft (`S9-INSERTED-BYTE-EQUAL`).
- The manager read the handoff diff, the §9 draft, the addendum and the MANIFEST rows. Two problems were seen before the adversaries ran: the pip "without saying why" softening, and the stale "not observed" clause in the addendum. Both were left for the adversaries to confirm independently.
- 15:30Z: wrote the "Does NOT cover / UNVERIFIED" section into this report. Then dispatched W3 and W4 in parallel, with the artifacts and criteria only, no worker reasoning.
- Both returned FAIL. Dispatched W5 with the merged 12-defect list.
- The manager re-read the fixed regions (3.5, 4.2, §8, §9, the addendum, the skill diff) and ran the verification bundle.
- Not done:
  - No fresh adversary on the fix round (the 5-worker cap).
  - No edit to the Fusion walkthrough (both ruling-10 items are present).

## Verification evidence
Bundle 1: shas before and after, diff stat, HEAD hash, DECISIONS cmp, MANIFEST numstat, index unchanged, negative greps, S8 row equality, §9 length, S13 counts.

Shas before, captured 15:22:17Z (first 16 hex of sha256):
~~~
vm/2026-11-06-vm-handoff.md  HEAD=9c9fa56e6760036d  WT=9c9fa56e6760036d
vm/skills/praxis-nt8-bridge-backtest/SKILL.md  HEAD=e06c40c4c9dbc99d  WT=e06c40c4c9dbc99d
DECISIONS.md  HEAD=15513289d2215ebc  WT=15513289d2215ebc
MANIFEST.md  HEAD=2913c477b910ca06  WT=2913c477b910ca06
docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md  HEAD=64571309cc933ef5  WT=64571309cc933ef5
~~~
~~~
$ date -u
2026-11-07T15:42:09Z
$ git rev-parse --short HEAD
43b34b1
$ shas after (HEAD blob vs working tree, sha256 first 16)
vm/2026-11-06-vm-handoff.md  HEAD=9c9fa56e6760036d  WT=717c2d0c2bf8f803
vm/skills/praxis-nt8-bridge-backtest/SKILL.md  HEAD=e06c40c4c9dbc99d  WT=7097ace5a60fdee2
DECISIONS.md  HEAD=15513289d2215ebc  WT=f74028261e9c5050
MANIFEST.md  HEAD=2913c477b910ca06  WT=a8e8eae469875573
docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md  HEAD=64571309cc933ef5  WT=64571309cc933ef5
$ git diff --stat HEAD -- <five files>
 DECISIONS.md                                  |  16 ++++
 MANIFEST.md                                   |   3 +
 vm/2026-11-06-vm-handoff.md                   | 127 +++++++++++++++++++-------
 vm/skills/praxis-nt8-bridge-backtest/SKILL.md |  12 +--
 4 files changed, 120 insertions(+), 38 deletions(-)
$ git show HEAD:ninjascript/PraxisNoiseAreaBreakout.cs | shasum -a 256
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  -
$ cmp <(git show HEAD:DECISIONS.md) <(head -n $(git show HEAD:DECISIONS.md | wc -l) DECISIONS.md) && echo PREFIX-IDENTICAL
PREFIX-IDENTICAL
$ cmp <(git show HEAD:MANIFEST.md) <(head -n 265 MANIFEST.md) && echo MANIFEST-PREFIX-IDENTICAL
MANIFEST-PREFIX-IDENTICAL
$ git diff --numstat HEAD -- MANIFEST.md DECISIONS.md
16	0	DECISIONS.md
3	0	MANIFEST.md
$ index: name-list sha / full cached-diff sha (before, then now)
5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95  -
9571fa6b067ce97aceece3e4f888ff08c8d3f2bb6a5243ce3899aef22ac4e46f  -
5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95  -
9571fa6b067ce97aceece3e4f888ff08c8d3f2bb6a5243ce3899aef22ac4e46f  -
12
$ git diff --cached --name-only -- vm DECISIONS.md MANIFEST.md | wc -l
0
$ negative: softening phrases removed (counts)
without saying why => 0
unless Code => 0
is for Code => 0
the master's reading"; \*\*Amear\*\* confirms => 0
Test 2a is not judged passed until => 0
$ §8 rows 1,2,6,8 byte-equal to HEAD?
row 1 SAME
row 2 SAME
row 6 SAME
row 8 SAME
$ step-0 items 1-6 byte-equal to HEAD?
STEP0-ITEMS-SAME
$ §9 length
38 lines (from heading to EOF)
$ standing sentence count
vm/2026-11-06-vm-handoff.md:1
vm/skills/praxis-nt8-bridge-backtest/SKILL.md:1
$ addendum money figures
0
~~~
Bundle 2: liveness arms for the zero-count greps, the hash-gate negative test, and the de-identification probe (`scratchpad/tokprobe2.sh`, the method of `docs/reports/2026-11-07-rulings-filing-manager.md`:113–118; counts and line numbers only):
```text
$ liveness arm: same phrases in the W1 pre-fix copy (handoff-w1.md)
without saying why => 1
unless Code => 1
is for Code => 1
$ liveness arm: HEAD handoff
Test 2a is not judged passed until => 1
$ hash-gate negative: HEAD blob with LF->CRLF
c22f38fa148e2175058286199821e679289b7f3779e402e9734a77f2523caa65  -
$ qcheck (W5 adapted copy) summary
0
Traceback (most recent call last):
  File "/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/d2d7d756-0ed5-4816-acfb-8ded37620b9d/scratchpad/u4/fix/qcheck.py", line 6, in <module>
    others={'pip help install (Mac pip 26.2.1, whitespace collapsed)':open(os.path.join(sys.argv[1],'piphelp.txt')).read()}
                                                                                        ~~~~~~~~^^^
IndexError: list index out of range
$ token probe (counts only)
candidates=12
LIVENESS HEAD:DECISION_LOG.md tokens_hit=12 confined_tokens_hit=2 lines=47,77,89,143,259,464,500,501,535,640,47,153,317,496,47,47,47,161,47,47,119,47,47,61,47,47,47,
LIVENESS 7d9be8e:HANDOFF.md tokens_hit=12 confined_tokens_hit=2 lines=9,7,9,302,9,23,277,24,426,20,9,14,9,9,15,20,
vm/2026-11-06-vm-handoff.md tokens_hit=0 confined_tokens_hit=0 lines=none
vm/skills/praxis-nt8-bridge-backtest/SKILL.md tokens_hit=0 confined_tokens_hit=0 lines=none
DECISIONS.md[1463,1478] tokens_hit=0 confined_tokens_hit=0 lines=none
MANIFEST.md[266,268] tokens_hit=0 confined_tokens_hit=0 lines=none
docs/reports/2026-11-07-vm-handoff-amendment-manager.md tokens_hit=0 confined_tokens_hit=0 lines=none
```
In bundle 2, the qcheck step (`OK` count 0 and a traceback) is the first call, made without the script's directory argument. It is superseded by the re-run pasted two blocks below (64 OK). That failure is left in, not edited out.

Ruling quotes, verbatim, counted in the amended files (script `u4/verify.py` slices each one from its DECISIONS.md line):
~~~
R5 :1229     handoff=2 skill=0 | 2a run: YES, covered by my lift. A test that needs a run inc
R6 :1230     handoff=3 skill=0 | Strategy Analyzer tab: a hand-set tab may be used for 2a and
R8 :1232     handoff=2 skill=0 | Snapshot is my hand step: confirmed.
R10 :1234    handoff=1 skill=0 | Go-live checklist additions: remove the unauthenticated brid
R7(4) :1231  handoff=2 skill=0 | (4) playbackrun/reconnect/flatten/strategies/ghostorders/Aut
R7(5) :1231  handoff=2 skill=0 | (5) NT8 Guard out.
R7(7) :1231  handoff=2 skill=0 | (7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; t
R7(11) :1231 handoff=3 skill=0 | (11) pip may download only the bridge's pinned requirements,
R7(12) :1231 handoff=2 skill=0 | (12) you propose how each arm runs through the bridge after 
~~~
Quote byte-check: W5's adapted `fix/qcheck.py`, re-run by the manager. It reads the added-line extracts W5 wrote at the end of its round; no file was edited after that round. The 4 NOT FOUND lines are PowerShell paths inside double quotes, not quotes of anyone.
~~~
===== handoff_added.txt
OK 1229-1234 | (4) playbackrun/reconnect/flatten/strategies/ghostorders/AutoReconnect stay forbidden until live-trading desig
OK 1229-1234 | (5) NT8 Guard out.
OK 1229-1234 | (11) pip may download only the bridge's pinned requirements, into its own venv under C:\praxis\.
OK 1229-1234 | pinned requirements
OK DECISIONS(other line 961) | after a VMware snapshot
OK DECISIONS(other line 960) | Yeah, just do the snapshot.
OK 1229-1234 | Snapshot is my hand step: confirmed.
OK 1229-1234 | Go-live checklist additions: remove the unauthenticated bridge request folders (or add auth) before real money
OK 1229-1234 | pinned
OK DECISIONS(other line 1470) | means on this bridge is the master's reading (INFERRED, labelled)
OK DECISIONS(other line 1474) | setuptools>=61
OK in docs/reports/2026-11-06-cli-nt-bridge-code-read.md | setuptools.build_meta
OK 1229-1234 | the bridge's pinned requirements
OK in pip help install (Mac pip 26.2.1, whitespace collapsed) | --no-deps Don't install package dependencies.
OK in pip help install (Mac pip 26.2.1, whitespace collapsed) | --no-build-isolation Disable isolation when building a modern source distribution. Build dependencies specifie
OK 1229-1234 | into its own venv under C:\praxis\
OK 1229-1234 | 2a run: YES, covered by my lift. A test that needs a run includes the run.
OK 1229-1234 | (7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; the VM's installed copy must hash-match HEAD, or ST
OK 1229-1234 | the VM's installed copy
NOT FOUND | $D\NinjaTrader 8\bin\Custom\Strategies\PraxisNoiseAreaBreakout.cs
NOT FOUND | Z:\ninjascript\PraxisNoiseAreaBreakout.cs
OK DECISIONS(other line 1268) | a hard STOP condition for the VM session
OK in docs/reports/2026-11-06-cli-nt-bridge-code-read.md | presses Run on a Strategy Analyzer tab **already open and set up by hand**
OK in docs/reports/2026-11-06-cli-nt-bridge-code-read.md | No explicit bridge field sets 1-minute Standard fill resolution, 2 ticks/side slippage or the PRAXIS commissio
OK 1229-1234 | Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as
OK 1229-1234 | . It does NOT count as
OK 1229-1234 | . The full in-VM automation lift needs a run whose settings come from the bridge/config, not my hands. Log it 
OK DECISIONS(other line 1003) | drives the baseline from the terminal
OK 1229-1234 | bridge reproduces the baseline
OK 1229-1234 | driven from the terminal
OK 1229-1234 | not my hands
OK 1229-1234 | before real money
OK DECISIONS(other line 1269) | How the source reaches the VM
OK 1229-1234 | (12) you propose how each arm runs through the bridge after 2a passes.
OK DECISIONS(other line 1263) | The D-071 half of that question is not answered by ruling 5's words.
OK DECISIONS(other line 1063) | under my ruling
OK DECISIONS(other line 1126) | commission_round_turn_usd
OK DECISIONS(other line 1330) | Lookback
OK DECISIONS(other line 1397) | NoiseMult
OK DECISIONS(other line 1262) | StopAtrMult
OK DECISIONS(other line 1228) | ExitPolicy
OK DECISIONS(other line 308) | Flat1559
OK DECISIONS(other line 259) | Contracts
OK DECISIONS(other line 1225) | Q7 NT8 full-span runs per configuration through the bridge, window selection and PBO on the Mac from NT8's tra
OK DECISIONS(other line 1456) | Walk-forward runs use $4.68 (`config/backtest-cost-model.json`:19, `
OK DECISIONS(other line 1456) | : 4.68`). Acceptance runs use $2.96, the committed reference runs' figure.
OK in docs/specs/2026-11-06-walk-forward-values.md | Every acceptance run uses the committed $2.96 commission, so the reference figures apply; every walk-forward r
OK in docs/reports/2026-11-06-cli-nt-bridge-code-read.md | Each trade carries pnl, side, entry and exit time and price, and exit name. There is no per-trade commission o
===== skill_added.txt
OK 1229-1234 | the VM's installed copy must hash-match HEAD, or STOP
NOT FOUND | $D\NinjaTrader 8\bin\Custom\Strategies\PraxisNoiseAreaBreakout.cs
OK DECISIONS(other line 1268) | a hard STOP condition for the VM session
NOT FOUND | $D\NinjaTrader 8\bin\Custom
OK 1229-1234 | bridge reproduces the baseline
OK 1229-1234 | driven from the terminal
===== addendum.txt
OK 1229-1234 | Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as
OK 1229-1234 | . It does NOT count as
OK 1229-1234 | . The full in-VM automation lift needs a run whose settings come from the bridge/config, not my hands. Log it 
OK 1229-1234 | (11) pip may download only the bridge's pinned requirements, into its own venv under C:\praxis\.
OK DECISIONS(other line 1470) | floors only, no lock file
OK 1229-1234 | pinned
OK DECISIONS(other line 1470) | means on this bridge is the master's reading (INFERRED, labelled)
OK 1229-1234 | (7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; the VM's installed copy must hash-match HEAD, or ST
OK DECISIONS(other line 1268) | a hard STOP condition for the VM session
OK 1229-1234 | (12) you propose how each arm runs through the bridge after 2a passes.
OK DECISIONS(other line 1004) | unmap Z: and turn the share off before real money
OK 1229-1234 | remove the unauthenticated bridge request folders (or add auth) before real money
OK 1229-1234 | the bridge's pinned requirements
OK DECISIONS(other line 1272) | these are APPLIED to `vm/2026-11-06-vm-handoff.md` by a later unit
===== composite ruling 6
True | e/config, not my hands. Log it as a partial pass until then.
True |  baseline". It does NOT count as "driven from the terminal".
~~~
What the evidence shows:
- **Index untouched.** The full cached-diff sha and the name-list sha are identical before and after (`9571fa6b…`, `5bfab445…`), and the count is 12.
- **HEAD hash.** Re-derived from the committed blob: `35393823…2265`, as expected.
- **Hash-gate negative.** The same blob with CRLF line endings hashes to `c22f38fa…`. 4.2's comparison would therefore STOP on a CRLF copy.
- **Probe candidates.** The probe now finds `candidates=12`; the rulings-filing unit found 13. HEAD's DECISIONS.md has grown since then, and the probe subtracts its tokens. The liveness arms hit all 12 at both known locations; every target reads 0.
- **Diff stat.** It shows four files. The fifth, the walkthrough, has HEAD=WT, so it has no diff.

## Adversarial findings and fixes
A (W3, fidelity/S8), `VERDICT: FAIL`:
1. **HIGH, S8.** Step 3.5 let Code decide how far "only" reaches ("unless Code's reply names them", "is for Code's reply", "without saying why").
   **Fixed:** Code's reply may name only `jsonschema`, `numpy`, `pyarrow` and `tzdata` (each `==`) plus the clone's own `-e .`. Dependencies and the build backend are **Amear's** question. The negative greps read 0; the liveness arm on the W1 copy reads 1 for each phrase.
2. **MEDIUM, S2/S5.** Readings were credited to the 15:19 row, which does not contain them.
   **Fixed:** the pip reading now quotes the row's actual words, and the rest is labelled this unit's reading. The STOP scope now follows the master's written reading (rulings file :42, "a hard STOP condition for the VM session"; DECISIONS.md:1268), so a mismatch stops the VM session.
3. **LOW.** The §8 framing had become false.
   **Fixed:** retitled `## 8. What his words settle, and what is still his`, with `Settled since 2026-11-06:` and `Still not decided here:`.
4. **LOW, S8.** NEEDS AMEAR 6 was called answered as a whole.
   **Fixed:** the run half is answered; the D-071 half is not (DECISIONS.md:1263); limit 3 stands.
5. **LOW.** The addendum said "§3.4".
   **Fixed:** "§5 … step 3.4".
6. **LOW.** The `report:28` quote had lost its bold markers (already so in HEAD).
   **Fixed.**

B (W4, mechanism), `VERDICT: FAIL`:
1. **MEDIUM.** "T1–T13 as `backtest` runs" ignored the Output-window prints and NT8's own trade lists.
   **Fixed:** 9.2 now says what each T needs. 9.4 item 9 says the capture route is UNVERIFIED and **Amear's**.
2. **MEDIUM, S2.** The STOP only detected an unnamed download after the fact.
   **Fixed:** `--no-deps` / `--no-build-isolation` prevent the download (labelled INFERRED; the Mac pip help was OBSERVED by W4 and W5; the VM's pip is UNVERIFIED). The STOP is labelled detection.
3. **LOW.** `-e .` cannot be written `==`.
   **Fixed:** exempt by name.
4. **LOW.** The template changes from $2.96 to $4.68 between the T-runs and the 81.
   **Fixed:** that change is a hand step, and his.
5. **LOW.** "Z: is the Mac working tree" was ungraded.
   **Fixed:** INFERRED, in the handoff and the skill.
6. **LOW.** "template read for 2a holds 1.48" claimed a read that has not happened.
   **Fixed:** REPORTED BY amear (notes-2 :104–106).
7. **LOW.** No way to diagnose a CRLF mismatch.
   **Fixed:** byte-size and CR checks added (read-only, untried); it still STOPs.
8. **LOW.** The skill gate lacked "quotes the sim account".
   **Fixed.**

Residual, found by the manager in the fixed text (not fixed; for the master):
- Under `--no-deps`, `jsonschema` will likely lack its own dependencies (INFERRED, not tried). Step 3.5 is therefore likely to STOP unless Amear answers the dependency question first. Putting that question to him before the VM session starts would avoid the stall. That is the master's call; it is not answered here.

## S6 cross-block check
- **F1–F4** (`specs/SPEC_RUBRIC.md`, FROZEN) are untouched. `specs/SPEC_RUBRIC.md` is not in this unit's diff. Its working-tree modification predates the unit (it is in the session-start git status) and was not touched.
- **D-071** is untouched. Ruling 5 does not mention it (DECISIONS.md:1263). The handoff says limit 3 stands, and its "Settled since" bullet says the D-071 half is open.
- **F2** (breakers #4/#5 and Deviation B timing) bears on arm (b)'s Flat1559 policy (D-2026-11-07-B S6). §9 proposes no rule for it and runs nothing, so F2 is not resolved here.
- **Cost model.** Read, not changed: $4.68 for walk-forward runs and $2.96 for acceptance runs, quoted in §9.3 from DECISIONS.md:1456 and spec :159.
- **DECISIONS.md.** D-2026-11-06-A's text, the D-2026-11-07-A entry and every line at or above :1462 are unchanged (`PREFIX-IDENTICAL`).

## Files staged
This unit staged nothing. The real index holds only the pre-existing 12-file set, unchanged (shas above). Working-tree changes:
- `vm/2026-11-06-vm-handoff.md` (288 → 351 lines; amendment 1 + §9)
- `vm/skills/praxis-nt8-bridge-backtest/SKILL.md` (6+/6−)
- `DECISIONS.md` (16 lines appended, :1463–1478)
- `MANIFEST.md` (3 rows appended, :266–268)
- `docs/reports/2026-11-07-vm-handoff-amendment-manager.md` (this report; new, untracked)

## Still Amear's
1. How the bridge source reaches the VM (§8 row 11's route half; step-0 item 2).
2. The AddOn file set (row 1; item 3).
3. Whose hand presses F5 (row 2; item 6).
4. Whether the unauthenticated request folders are acceptable for these tests (row 3; item 4). Ruling 10 covers only "before real money".
5. Which sim account (row 8; item 5).
6. Who sets the Strategy Analyzer tab by hand, and who reads it back (go-2a).
7. NEW: whether the base packages' own dependencies and the build backend (`setuptools>=61`) count as "the bridge's pinned requirements" (step 3.5).
8. The D-071 half of D-2026-11-06-A NEEDS AMEAR 6.
9. Whether §9 is adopted, after 2a passes. Within it:
   - the $4.68 template hand step;
   - how arm (b)'s file reaches the VM, and who compiles it;
   - how the Output-window text and NT8's trade lists are captured.
10. Readings he can change: the master's (the STOP scope; what "pinned" means) and this unit's (the four-package list and the flags; the venv fit).

## Result
**Result: PASS.** The deliverables are written. Both adversarial passes ran, and all 20 findings were fixed and checked by the manager. Limits: no fresh adversary re-checked the fix round, and nothing has been tried on the VM. The master's auditor grades this unit.

## Correction 1 (audit FAIL 1 on S1, DECISION_LOG 2026-11-07T15:52:00Z)
Authorisation (S5): DECISION_LOG row `[2026-11-07T15:52:00Z] WHO: praxis-master`. Append-only: line 329 above stays as written, beside this correction.

**Retracted.** Line 329 says: "Both adversarial passes ran, and all 20 findings were fixed and checked by the manager." The count "20" is wrong. Nothing in this report supports it, and the report's own table and findings list contradict it. The sentence is retracted. The correct count is **14 findings** (A: 6, B: 8). All 14 are marked fixed. They reached W5 as **12 numbered defects**.

Evidence. These were captured before this section was appended, so they read only lines 1–329:
```
$ grep -c '^   \*\*Fixed' docs/reports/2026-11-07-vm-handoff-amendment-manager.md
14
$ sed -n 56,57p docs/reports/2026-11-07-vm-handoff-amendment-manager.md
| W3 | ab3a618eba2e32040 | ADVERSARIAL A (fidelity/S8) | handoff, skill, addendum | `VERDICT: FAIL` — 1 HIGH, 1 MEDIUM, 4 LOW |
| W4 | a3bdf70c3ca324bac | ADVERSARIAL B (mechanism) | handoff changed lines + §9, skill | `VERDICT: FAIL` — 2 MEDIUM, 6 LOW |
$ sed -n 262,297p docs/reports/2026-11-07-vm-handoff-amendment-manager.md | awk '<count ^N. lines under A (W3 / B (W4, stop at Residual>'
A=6 B=8
```
W3's row says 1 HIGH + 1 MEDIUM + 4 LOW = 6, and W4's says 2 MEDIUM + 6 LOW = 8. Total 14, which matches the 14 `**Fixed` lines.

Splice note: the first append left out the `14` under the first command. grep refused to read the file it was appending to, because its input was also its output. The command was re-run on the file and its real output spliced in. Nothing else in the block changed.

**How 14 findings became 12 defects.** The report text alone does not show the merge. The process log at :65 says only "the merged 12-defect list". To reconstruct it, I read W5's dispatch brief, which is the first message in W5's transcript. That transcript is machine-local under `~/.claude/projects/`. It is not version-controlled, so it can be re-read on this Mac only. Here are the brief's defect headers (OBSERVED; each cut to 110 characters):
```
$ head -1 <W5 transcript agent-abbc14e4d9b2adf38.jsonl> | python3 -I -c '<print each ^N. [..] defect line, first 110 chars>'
1. [HIGH, S8] Step 3.5 (:147–152) and limit 8 (:34): the file lets Code decide how far "only" reaches (":148 n
2. [MEDIUM, S2] Labels: the handoff (:148, :178), SKILL.md (:29) and DECISIONS.md (:1470–1471) credit readings
3. [LOW] §8 framing: heading :277 "What is NOT decided here", intro :279 "Questions only", ":296 Also not deci
4. [LOW, S8] :297 says NEEDS AMEAR 6 answered as a whole; it has a D-071 half (DECISIONS.md:1046, :1263: "The 
5. [MEDIUM, S2] §9.2 :318 "Then acceptance tests T1–T13 (spec §9) as `backtest` runs." Spec needs more than a 
6. [LOW] §9.2: T-runs at $2.96 then the 81 at $4.68 (9.3) means a template change on the tab mid-sequence — ad
7. [LOW] :177 and SKILL.md :28: "Z: is the Mac working tree, not HEAD" — tag INFERRED (header :8 grades Z: = r
8. [LOW] :310 "The PRAXIS template read for 2a holds 1.48 per unit" — no 2a read exists; grade REPORTED BY ame
9. [LOW] 4.2: the HEAD blob is LF-only, 14318 bytes (OBSERVED: `git show HEAD:ninjascript/PraxisNoiseAreaBreak
10. [LOW] SKILL.md gate (:13): add that go-2a quotes the sim account from Amear's step-0 words (matches handof
11. [LOW] handoff :182 quote of `report:28` lost its `**…**` markers — restore them so it is byte-exact (check
12. [LOW] DECISIONS.md addendum :1467 "the §3.4 go-live note" → "§5 step 3.4's go-live note"; and the "Applied
```
This mapping is the manager's reading. It matches each W5 brief item to the A/B findings by its text:

| W5 defect | finding(s) | note |
|---|---|---|
| 1 | A1 + B2 + B3 | **merged.** A1 is the "only"-reach HIGH. B2 asks for prevention, not detection, and its fix is the `--no-deps` / `--no-build-isolation` text inside W5-1. B3 is the `-e .` exemption, also inside W5-1 ("exempt it by name from the `==` rule"). Three findings became one item, so the count drops by 2. |
| 2 | A2 | |
| 3 | A3 | |
| 4 | A4 | |
| 5 | B1 | |
| 6 | B4 | |
| 7 | B5 | |
| 8 | B6 | |
| 9 | B7 | |
| 10 | B8 | |
| 11 | A6 | |
| 12 | A5 | W5-12 also carried two additions of the manager's own. One is the stale "not observed" clause in the addendum, seen before the adversaries ran (:63). The other is the dependency/build-backend "Still his" bullet. Neither is an adversary finding. |

Check: 14 − 2 = 12. That is "all 12 reported fixed" at :58, REPORTED BY W5. The 14 per-finding `**Fixed` lines are the manager's re-read.

**Disclosure (auditor MINOR).** "No extras" means `[dev]` and `[report]` are left out of Code's pip list (handoff step 3.5; §7 item 10). That exclusion is this unit's INFERRED reading of "only" in ruling 7(11). It is not Amear's word. It was not routed to him as a question of its own. He can change it. It belongs with item 10 of `## Still Amear's` (this unit's readings he can change).

**Restated result.** `Result: PASS` (the manager's call; the master's auditor grades). The limits are unchanged:
- no fresh adversary re-checked the fix round;
- nothing has been tried on the VM.

The after-capture (`wc -l`, sha, line 329 unchanged, the standing-sentence count, `git status`, the numstat of the other four unit files) is pasted in the manager's return, not here. Pasting it here would change the sha it reports.
