# 2026-11-12 — fgd-doc-alignment — worker 2 (ADVERSARIAL, narrow re-check)

## Task

Unit `2026-11-12-fgd-doc-alignment`, mode ADVERSARIAL, narrow re-check of three wording cures applied after `docs/reports/2026-11-12-fgd-doc-alignment-worker1.md` (section "## Findings", line 550 as filed and at re-run; Correction-1 re-run evidence). Working directory `/Volumes/Sensidine/Praxis.build`, branch `main`, HEAD `006a08b`. Files under check:

- `docs/specs/2026-11-10-live-signal-topology.md` (body 1–114, note appended)
- `docs/specs/2026-07-16-b2-noise-area-ruleset.md` (body 1–111, note appended)
- `docs/specs/2026-11-10-f2-session-flat-proposal.md` (body 1–81, note appended)

Checks in scope: (a) Finding 2 cure, topology aligned reading for :41; (b) Finding 3 cure, topology aligned reading for :78; (c) Finding 4 cure, proposal aligned reading for :79; (d) Finding 1, proposal note line 95 encoding and rubric citation; (e) body byte-identity, zero removed lines, numstat, shasum; (f) the cures add no design choice and no claim above SPECIFIED ONLY.

This worker staged and committed nothing, and wrote no file apart from this report (the last part is a self-report). At re-run HEAD is still `006a08b` and the index holds 1 entry, one PNG under `docs/reports/evidence/` (counts in the re-run block), and 0 entries under `docs/specs`, this report or DECISIONS.md (Correction-1 re-run evidence).

## Checks run

### C1 — numstat, shasum, removed-line count, UTF-8 (body-identity part of this call failed; re-run in C2)

The body-identity loop in this call failed because zsh does not word-split `$x` (re-run 2026-11-12 by correction-1: with `x="a 1"`, `set -- $x` gives 1 argument in zsh and 2 in bash; Correction-1 re-run evidence); that part of the output is not evidence and is replaced by C2. The numstat, shasum, removed-line and UTF-8 parts are valid.

Command:

```bash
cd /Volumes/Sensidine/Praxis.build && T=docs/specs/2026-11-10-live-signal-topology.md; B=docs/specs/2026-07-16-b2-noise-area-ruleset.md; P=docs/specs/2026-11-10-f2-session-flat-proposal.md; echo "== numstat"; git diff --numstat HEAD -- $T $B $P; echo "== shasum"; shasum $T $B $P; echo "== removed lines count"; for f in $T $B $P; do echo "$f: $(git diff HEAD -- $f | grep -c '^-[^-]')"; done; echo "== body identity"; for x in "$T 114" "$B 111" "$P 81"; do set -- $x; a=$(head -n $2 $1 | shasum | cut -c1-40); b=$(git show HEAD:$1 | head -n $2 | shasum | cut -c1-40); h=$(git show HEAD:$1 | wc -l | tr -d ' '); echo "$1 work=$a head=$b HEADlines=$h"; done; echo "== utf8"; for f in $T $B $P; do iconv -f UTF-8 -t UTF-8 $f >/dev/null && echo "$f valid UTF-8"; done
```

Output:

```text
== numstat
59	0	docs/specs/2026-07-16-b2-noise-area-ruleset.md
30	0	docs/specs/2026-11-10-f2-session-flat-proposal.md
86	0	docs/specs/2026-11-10-live-signal-topology.md
== shasum
5865a1121cd1b55783f217c4f341e20b7cfc03d5  docs/specs/2026-11-10-live-signal-topology.md
b68c098f4aa1d3273ad179474299d662f1e0c243  docs/specs/2026-07-16-b2-noise-area-ruleset.md
24598c3d73d8dd3a3961a7083aa8e42a68012362  docs/specs/2026-11-10-f2-session-flat-proposal.md
== removed lines count
docs/specs/2026-11-10-live-signal-topology.md: 0
docs/specs/2026-07-16-b2-noise-area-ruleset.md: 0
docs/specs/2026-11-10-f2-session-flat-proposal.md: 0
== body identity
head: illegal line count -- docs/specs/2026-11-10-live-signal-topology.md 114
head: option requires an argument -- n
usage: head [-n lines | -c bytes] [file ...]
fatal: path 'docs/specs/2026-11-10-live-signal-topology.md 114' does not exist in 'HEAD'
fatal: path 'docs/specs/2026-11-10-live-signal-topology.md 114' does not exist in 'HEAD'
docs/specs/2026-11-10-live-signal-topology.md 114 work=da39a3ee5e6b4b0d3255bfef95601890afd80709 head=da39a3ee5e6b4b0d3255bfef95601890afd80709 HEADlines=0
head: illegal line count -- docs/specs/2026-07-16-b2-noise-area-ruleset.md 111
head: option requires an argument -- n
usage: head [-n lines | -c bytes] [file ...]
fatal: path 'docs/specs/2026-07-16-b2-noise-area-ruleset.md 111' does not exist in 'HEAD'
fatal: path 'docs/specs/2026-07-16-b2-noise-area-ruleset.md 111' does not exist in 'HEAD'
docs/specs/2026-07-16-b2-noise-area-ruleset.md 111 work=da39a3ee5e6b4b0d3255bfef95601890afd80709 head=da39a3ee5e6b4b0d3255bfef95601890afd80709 HEADlines=0
head: illegal line count -- docs/specs/2026-11-10-f2-session-flat-proposal.md 81
head: option requires an argument -- n
usage: head [-n lines | -c bytes] [file ...]
fatal: path 'docs/specs/2026-11-10-f2-session-flat-proposal.md 81' does not exist in 'HEAD'
fatal: path 'docs/specs/2026-11-10-f2-session-flat-proposal.md 81' does not exist in 'HEAD'
docs/specs/2026-11-10-f2-session-flat-proposal.md 81 work=da39a3ee5e6b4b0d3255bfef95601890afd80709 head=da39a3ee5e6b4b0d3255bfef95601890afd80709 HEADlines=0
== utf8
docs/specs/2026-11-10-live-signal-topology.md valid UTF-8
docs/specs/2026-07-16-b2-noise-area-ruleset.md valid UTF-8
docs/specs/2026-11-10-f2-session-flat-proposal.md valid UTF-8
```

### C2 — body byte-identity to HEAD (re-run)

Command:

```bash
cd /Volumes/Sensidine/Praxis.build && chk(){ a=$(head -n $2 $1 | shasum | cut -c1-40); b=$(git show HEAD:$1 | head -n $2 | shasum | cut -c1-40); h=$(git show HEAD:$1 | wc -l | tr -d ' '); w=$(wc -l < $1 | tr -d ' '); echo "$1 body1-$2 work=$a head=$b HEADlines=$h worklines=$w"; }; chk docs/specs/2026-11-10-live-signal-topology.md 114; chk docs/specs/2026-07-16-b2-noise-area-ruleset.md 111; chk docs/specs/2026-11-10-f2-session-flat-proposal.md 81; echo "== HEAD whole-file sha vs work prefix"; for f in docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/specs/2026-11-10-f2-session-flat-proposal.md; do n=$(git show HEAD:$f | wc -c | tr -d ' '); echo "$f HEADbytes=$n headsha=$(git show HEAD:$f | shasum | cut -c1-40) workprefix=$(head -c $n $f | shasum | cut -c1-40)"; done
```

Output:

```text
docs/specs/2026-11-10-live-signal-topology.md body1-114 work=41aa15cee88544e5e9b4d673d7e04543198f9295 head=41aa15cee88544e5e9b4d673d7e04543198f9295 HEADlines=114 worklines=200
docs/specs/2026-07-16-b2-noise-area-ruleset.md body1-111 work=5ee985f56965b1ab13aef55dba866c8e215de9d8 head=5ee985f56965b1ab13aef55dba866c8e215de9d8 HEADlines=111 worklines=170
docs/specs/2026-11-10-f2-session-flat-proposal.md body1-81 work=df9fd167a69eaedff53c1bd8a6aa0454c1bcb394 head=df9fd167a69eaedff53c1bd8a6aa0454c1bcb394 HEADlines=81 worklines=111
== HEAD whole-file sha vs work prefix
docs/specs/2026-11-10-live-signal-topology.md HEADbytes=24094 headsha=41aa15cee88544e5e9b4d673d7e04543198f9295 workprefix=41aa15cee88544e5e9b4d673d7e04543198f9295
docs/specs/2026-07-16-b2-noise-area-ruleset.md HEADbytes=11354 headsha=5ee985f56965b1ab13aef55dba866c8e215de9d8 workprefix=5ee985f56965b1ab13aef55dba866c8e215de9d8
docs/specs/2026-11-10-f2-session-flat-proposal.md HEADbytes=12061 headsha=df9fd167a69eaedff53c1bd8a6aa0454c1bcb394 workprefix=df9fd167a69eaedff53c1bd8a6aa0454c1bcb394
```

Each HEAD blob is exactly the body line count (114, 111, 81), and each working file's leading bytes equal the whole HEAD blob. The change in each file is a pure append.

### C3 — topology source lines :41, :78, :105 and the whole topology note (:115–200)

Command:

```bash
cd /Volumes/Sensidine/Praxis.build && echo "== topology :41 :78 :105"; sed -n '41p;78p;105p' docs/specs/2026-11-10-live-signal-topology.md; echo "== topology note 115-200"; sed -n '115,200p' docs/specs/2026-11-10-live-signal-topology.md
```

Output:

````text
== topology :41 :78 :105
Path: NT8 emitter (computes signal) → HTTP POST → n8n webhook → **[breaker gates, Redis, default closed]** → Write Signal File → outbox → sweep daemon → drop dir → `PraxisSignalConsumer` → **[consumer-side checks #4, #5, #7, #8, #9]** → `SubmitBracket` → Rithmic → account.
Option 3 has the fewest unbuilt parts, because NT8 already holds account P&L, position and clock. The decision rule puts the Phase 3 placement first unless the evidence shows the signal cannot pass through n8n, and it does not show that today. So option 1 is recommended, and option 3 is the fallback **only if** OPEN-T1 finds the VM cannot reach the webhook. If the fallback is taken, what changes: all nine checks move into the strategy before its order calls; Redis default-closed becomes a strategy default (no entries until every check has been confirmed this session); #9 needs an outside health source the strategy can read.
| OPEN-T8 | How R8's lockout on Amear's own interaction 15:00–18:00 is enforced, since manual orders never pass n8n (B3). | Block 3 design under D1; it binds Amear's own conduct, so he may overrule it. |
== topology note 115-200

## Amendment note — 2026-11-12 (D-2026-11-12-A alignment)

> ***Added 2026-11-12; not part of the text above.*** Body lines 1–114 above are unchanged. Unit `2026-11-12-fgd-doc-alignment` (bead `Praxis_build-fgd`, part A), decided by master under D-2026-11-08-D D1, changeable by Amear. This note carries out D-2026-11-12-A (DECISIONS.md:2205) and Amendment 1 at the end of `docs/specs/2026-11-05-phase3-build-specification.md` (amended #4 at its line :212, amended #5 at :224). It makes no new design choice and writes no DECISIONS.md entry; where an aligned reading would need a choice that D-2026-11-12-A and Rule F2-1 do not make, the item is listed as OPEN below with both readings. Each old line below is copied by script from this file at HEAD, byte-identical.

**Level.** Unchanged: the nine breakers, #4 and #5 included, remain SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure. This note changes how lines are read; it builds nothing.

**Governing text.** Amended #4, copied by script from `docs/specs/2026-11-05-phase3-build-specification.md`:212:

> 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not), and refuse new system entries until the next session opens at 18:00 ET.

Amended #5, copied by script from `docs/specs/2026-11-05-phase3-build-specification.md`:224:

> 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry and manual changes to the system by the operator. The system's own trading is not disabled by this breaker; the system's no-entry period 16:00–18:00 ET is enforced by breaker #4.

### :41 — path line (follow-up F-1)

```text
Path: NT8 emitter (computes signal) → HTTP POST → n8n webhook → **[breaker gates, Redis, default closed]** → Write Signal File → outbox → sweep daemon → drop dir → `PraxisSignalConsumer` → **[consumer-side checks #4, #5, #7, #8, #9]** → `SubmitBracket` → Rithmic → account.
```

Aligned reading: the consumer-side checks on this path are #4, #7, #8 and #9. #5 has no check on the signal path: amended #5 does not disable the system's own trading, and the system's no-entry period 16:00–18:00 ET is enforced by #4. This is the case the #5 row (:62) already states for adoption of the F2 proposal ("the n8n/consumer window check is then removed"): D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232), and proposal :40 states that, if adopted, the system window check is removed.

### :48 — consumer-side checks (F-1)

```text
**What changes from the Block 1 architecture.** The emitter is NT8, not TradingView (CLAUDE.md "Signal flow: TradingView alert → webhook → …"). Deviation G's public-ingress question stops being on the anchor strategy's live path, because the emitter posts from inside the local network. Breakers #4, #5, #8 and #9 gain a consumer-side check (section 3), because n8n cannot measure relay delay after its own write, and cannot vouch for itself when it is down.
```

Aligned reading: breakers #4, #8 and #9 gain a consumer-side check; #5 does not (see :41). The reason given for #4, #8 and #9 is unchanged.

### :54 — breaker names (F-2)

```text
Names are exactly as the Phase 3 import lists them (`docs/specs/2026-11-05-phase3-build-specification.md`:97–105, at HEAD) [E1]. Every row's current level is SPECIFIED: no breaker exists in code or workflow (1.13). "Upstream" means the check runs, and can stop the order, before `SubmitBracket` calls `EnterLong` / `EnterShort`.
```

Aligned reading: the names in the table are the import's body names at :97–105, and they stay as written. Since Amendment 1, the body lines :100–101 of the import are superseded and #4 and #5 carry the amended names: #4 "Session flat gate" (body name "Session time gate"); #5 "Session window (operator lockout)" (body name "Afternoon session window"). Read the #4 and #5 rows (:61, :62) under the amended names and the amended text.

### :61 — breaker #4 row (F-2)

```text
| 4 | Session time gate | Two checks: an n8n gate node before Write Signal File (ET clock; entries refused after the flat time until the next session), and an ET clock check in the consumer before `SubmitBracket`, so a file written just before the cut-off, or dropped straight into the drop dir (bypass B1), is still refused after it. Its "close positions" action: the emitter's own time exit posted as a FLATTEN signal, plus the FLATTEN command from n8n at the gate time. | The n8n check runs before the file write; the consumer check is the last step before `EnterLong` / `EnterShort` and bounds the relay delay that n8n cannot see after its own write. | ET wall clock; the flat time and the next-session start (both are F2's; see `docs/specs/2026-11-10-f2-session-flat-proposal.md`, PROPOSED). | SPECIFIED | F2 (FROZEN); FLATTEN path (unbuilt); the deterministic fallback script for when n8n is down (Phase 3 :109; unbuilt). |
```

Aligned reading: name "Session flat gate". The flat time is 16:00:00 ET, or the exchange's early close on an early-close day if earlier, and the next session starts at 18:00 ET (amended #4); they are no longer PROPOSED. "F2 (FROZEN)" in the "Depends on" column reads: rubric F2 is PASSED@e3323a8. The two checks (n8n gate before Write Signal File, consumer ET clock check before `SubmitBracket`) and the FLATTEN close action stay as written, and now also carry the system's no-entry period 16:00–18:00 ET that amended #5 hands to #4. Amended #4 also names "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)"; this row does not place either action on the path, and this note does not place them (OPEN-A1 below).

### :62 — breaker #5 row (F-1, F-2)

```text
| 5 | Afternoon session window | As the Phase 3 text stands: an n8n gate node before Write Signal File plus the same consumer clock check as #4, refusing every system entry (including Noise-Area reversals) in the window. Under the F2 proposal (`docs/specs/2026-11-10-f2-session-flat-proposal.md`, PROPOSED, not adopted) #5 becomes an operator lockout only, and the system no-entry period 16:00–18:00 moves into #4; the n8n/consumer window check is then removed. | As the text stands, the n8n check runs before the file write and the consumer check before `SubmitBracket`; nothing in the window becomes an order. | ET wall clock; the window. | SPECIFIED | F2. R8 splits #5 into a disable of the system's own trading (redone) and a lockout on Amear's own interaction (KEPT). **The lockout half cannot sit on this path**: a manual order typed into NT8 or the broker platform never passes n8n (bypass B3, section 5). |
```

Aligned reading: name "Session window (operator lockout)". The row's own conditional ("Under the F2 proposal … the n8n/consumer window check is then removed") is now in effect: there is no n8n gate node and no consumer clock check for #5, and nothing on the signal path enforces #5. System entries 15:00–16:00 ET are allowed, subject to breakers #1, #2, #3, #6, #7, #8 and #9 (proposal :30, copied into Amendment 1); from 16:00 to 18:00 ET they are refused by #4. The row's "As the Phase 3 text stands" readings describe the superseded import text. The row's last sentence stands: the lockout cannot sit on this path (bypass B3); how it is enforced is OPEN-T8 (:105), not decided here. "Depends on: F2" reads: rubric F2 is PASSED@e3323a8.

### :74 — option 1, unbuilt components (F-1)

```text
| **1 (recommended)** | NT8 emitter strategy posts to the local n8n webhook | n8n + Redis before the file write; #7/#8/#9 also in the consumer | emitter strategy; VM → n8n reach (OPEN-T1); EXIT/FLATTEN instruction types; consumer clock check for #4/#5; n8n gate nodes; Redis gate keys; PostgreSQL trip log; account-state and fill feed into Redis; FLATTEN command in the consumer; consumer checks for #8/#9 (and #7 at plan size); n8n health stamp; fallback script | Yes |
```

Aligned reading: "consumer clock check for #4/#5" reads "consumer clock check for #4". Option 2 (:75, "Same as 1") reads the same way.

### :78 — fallback option 3 (F-1; found by this unit, not in the cited list)

```text
Option 3 has the fewest unbuilt parts, because NT8 already holds account P&L, position and clock. The decision rule puts the Phase 3 placement first unless the evidence shows the signal cannot pass through n8n, and it does not show that today. So option 1 is recommended, and option 3 is the fallback **only if** OPEN-T1 finds the VM cannot reach the webhook. If the fallback is taken, what changes: all nine checks move into the strategy before its order calls; Redis default-closed becomes a strategy default (no entries until every check has been confirmed this session); #9 needs an outside health source the strategy can read.
```

Aligned reading: if the fallback is taken, the system checks that move into the strategy are those of #1–#4 and #6–#9; #5 has no system check to move; where its operator lockout sits, including whether the strategy could carry it, is OPEN-T8 (:105), not decided here.

### :86 — bypass B1 (F-1)

```text
| B1 | A JSON file written straight into the drop dir `/Users/admin/praxis-signals`, into `incoming/`, or into the n8n outbox, by anything that can write as `admin`, or through any share that exposes the drop dir to the VM. D-2026-11-10-A (DECISIONS.md:2041) already reads it this way ("a file written straight into the drop dir would not pass those gates (inference from that text, not tested)"). | No. The consumer cannot tell a file that came through n8n from one that did not. | (a) The consumer-side checks #4, #5, #7, #8 and #9 still apply to such a file; #1, #2, #3 and #6 do not, because they run only in n8n. (b) n8n signs each gate-passed file (HMAC over the payload) and the consumer refuses unsigned files. That needs a key in n8n and in the VM: **waits for Amear (D2(d))**. (c) The `praxispush` user and drop-dir move (D-2026-11-10-A) narrow who can write. | (b) Amear, D2(d). (c) the deferral is decided (D-2026-11-10-A, DECISIONS.md:2039, "DEFERRED, not dropped"); provisioning stays with Amear (D2(d), :2043), so B1 stays open as an accepted risk until then. |
```

Aligned reading: under (a), the consumer-side checks #4, #7, #8 and #9 still apply to such a file; #5 has none. The rest of the row is unchanged.

### OPEN

| ID | Open item | The two readings |
|---|---|---|
| OPEN-A1 | Where amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)" sit on the live path. D-2026-11-12-A adopts the text; it places neither action. | (a) Both are part of the FLATTEN command the consumer executes at the flat time (the consumer cancels its own working entries and reports flat or not flat). (b) The confirmation is a separate n8n-side check on account state, which needs the account-state feed of OPEN-T3. Not chosen here. |

**F1 bearing (not a grade).** Rubric F1 (PASSED@b4c3291) asks that this document address "every one of the nine breakers by name". The table at :58–66 still names all nine by the import's body names; this note adds the amended names of #4 and #5. Amended #5 no longer sits on the signal path at all (its system half moved into #4; its lockout is off-path, B3). Whether F1 needs re-grading is the master's call; this note does not grade it.
````

### C4 — DECISIONS.md around :2232 (all DECISIONS.md line numbers in C4–C6 and in Findings are working tree; its lines 1–2278 are identical to HEAD, Correction-1 re-run evidence), proposal :30 :40 :79, the whole proposal note (:82–111), rubric HEAD :93–94

Command:

```bash
cd /Volumes/Sensidine/Praxis.build && echo "== DECISIONS.md 2228-2236"; sed -n '2228,2236p' DECISIONS.md; echo "== proposal :30 :40 :79"; sed -n '30p;40p;79p' docs/specs/2026-11-10-f2-session-flat-proposal.md; echo "== proposal note 82-111"; sed -n '82,111p' docs/specs/2026-11-10-f2-session-flat-proposal.md; echo "== rubric HEAD 93-94"; git show HEAD:specs/SPEC_RUBRIC.md | sed -n 93,94p
```

Output:

````text
== DECISIONS.md 2228-2236
```text
**On a full trading day, at 15:00 ET an open system position stays open.** Nothing closes it at 15:00. (On an early-close day whose close is at or before 15:00, Rule F2-1 has already flattened it and no system position is open at 15:00.) It is managed by its own strategy's exits (for the Noise-Area: the band / VWAP trailing stop and reverse rule) and by the always-on breakers #1, #6 and #7, and its closing order is sent no later than 16:00:00 ET by Rule F2-1 (the strategy's own flat, backed by breaker #4), flat before 16:10 ET. New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9. Between 15:00 and 18:00 ET Amear's own manual interaction is locked out (R8 KEEP, breaker #5 below).
```

**The amended breaker text.** The proposal's replacement text for breakers #4 and #5 is adopted as the amended breaker spec. Copied by script from proposal :36 and :38:

```text
> 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not), and refuse new system entries until the next session opens at 18:00 ET.

== proposal :30 :40 :79
**On a full trading day, at 15:00 ET an open system position stays open.** Nothing closes it at 15:00. (On an early-close day whose close is at or before 15:00, Rule F2-1 has already flattened it and no system position is open at 15:00.) It is managed by its own strategy's exits (for the Noise-Area: the band / VWAP trailing stop and reverse rule) and by the always-on breakers #1, #6 and #7, and its closing order is sent no later than 16:00:00 ET by Rule F2-1 (the strategy's own flat, backed by breaker #4), flat before 16:10 ET. New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9. Between 15:00 and 18:00 ET Amear's own manual interaction is locked out (R8 KEEP, breaker #5 below).
Placement of both on the live path is in `docs/specs/2026-11-10-live-signal-topology.md`, section 3. That table places #5 as the Phase 3 text stands (a system entry block in the window) and states what changes under this proposal: if adopted, the system window check is removed and only the operator lockout remains. That document notes that #5's operator lockout cannot sit on the signal path, because manual orders never pass n8n (its bypass B3, OPEN-T8).
| OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec. |
== proposal note 82-111

## Amendment note — 2026-11-12 (D-2026-11-12-A alignment)

> ***Added 2026-11-12; not part of the text above.*** Body lines 1–81 above are unchanged. Unit `2026-11-12-fgd-doc-alignment` (bead `Praxis_build-fgd`, part A), decided by master under D-2026-11-08-D D1, changeable by Amear. This note carries out D-2026-11-12-A (DECISIONS.md:2205) and Amendment 1 at the end of `docs/specs/2026-11-05-phase3-build-specification.md` (amended #4 at its line :212, amended #5 at :224). It makes no new design choice and writes no DECISIONS.md entry; where an aligned reading would need a choice that D-2026-11-12-A and Rule F2-1 do not make, the item is listed as OPEN below with both readings. Each old line below is copied by script from this file at HEAD, byte-identical.

**Level.** Unchanged: the nine breakers, #4 and #5 included, remain SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure. This note changes how lines are read; it builds nothing.

### :8 — rubric line citation (follow-up F-7)

```text
This file is a proposal only. It writes no DECISIONS.md entry, edits no breaker spec, and changes no rubric state. F2 unblocks when "A DECISIONS.md entry names the governing rule and the 15:00 disposition, and breaker specs #4 and #5 are amended to match" (`specs/SPEC_RUBRIC.md`:43–44). Under A6, "F2's state changes when Amear approves the proposed values" (DECISIONS.md:1744–1745).
```

Aligned reading: the F2 unblock clause quoted here is at `specs/SPEC_RUBRIC.md`:93–94 at HEAD `006a08b`, inside the section "### F2 — Session-flat time vs. breakers #4 and #5" (:81), which now sits under "## PASSED — closed criteria". It was at :30–31 at `e3323a8` (D-2026-11-12-A); the rubric change at `c29d08b` moved F2 into PASSED. The quoted words are unchanged. The second citation on this line, DECISIONS.md:1744–1745 (A6), is unchanged. The line's "changes no rubric state" is true of this file; rubric F2's state was moved at `c29d08b`, not by this file.

### :79 — OPEN-F2-5 (follow-up F-9)

```text
| OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec. |
```

Aligned reading: OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits. Each step its "What would decide it" column names now has a record: Amear's approval of Rule F2-1 (D-2026-11-11-A, V2, DECISIONS.md:2108); a DECISIONS.md entry (D-2026-11-12-A, DECISIONS.md:2205); the amended #4/#5 text in the breaker spec (Amendment 1 of the Phase 3 spec). Rubric F2 is PASSED@e3323a8. Limits carried from D-2026-11-12-A, not changed here: Amear's approval was given on the words of a summary; the #4/#5 text is the master's adoption under D1, not Amear's words, changeable by Amear; whether his approval reaches that text, and whether A6 is triggered, are not graded.

Read with :3, which states this file's status when it was filed:

```text
Status: PROPOSED. F2 stays FROZEN until Amear approves (A6, DECISIONS.md:1744)
```

That status is historical: Rule F2-1 is adopted (D-2026-11-12-A) and rubric F2 is PASSED@e3323a8. The rest of this file is unchanged; OPEN-F2-1 to OPEN-F2-4 (:75–78) stay open.
== rubric HEAD 93-94
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
````

### C5 — DECISIONS.md:2232 exact, :2108, the limits inside D-2026-11-12-A, proposal line 95 encoding and citation, rubric HEAD headings

Command:

```bash
cd /Volumes/Sensidine/Praxis.build && echo "== DECISIONS 2232 numbered"; sed -n '2232p' DECISIONS.md | cat -n | sed 's/^ *1/2232/'; echo "== DECISIONS 2108"; sed -n '2108p' DECISIONS.md; echo "== D-2026-11-12-A block 2205-2280 grep for limits"; sed -n '2205,2290p' DECISIONS.md | grep -n -i -E 'summary|A6|D1|not graded|changeable|SPECIFIED' ; echo "== proposal line 95 bytes check"; sed -n '95p' docs/specs/2026-11-10-f2-session-flat-proposal.md | iconv -f UTF-8 -t UTF-8 >/dev/null && echo "line95 valid UTF-8"; sed -n '95p' docs/specs/2026-11-10-f2-session-flat-proposal.md | grep -o 'specs/SPEC_RUBRIC.md`:93–94'; sed -n '95p' docs/specs/2026-11-10-f2-session-flat-proposal.md | LC_ALL=C grep -c $'\xef\xbf\xbd'; echo "== rubric HEAD :81 and PASSED heading"; git show HEAD:specs/SPEC_RUBRIC.md | grep -n -E '^## |^### F2'
```

Output (grep line numbers in the "limits" block are relative to line 2205, so relative 1 = DECISIONS.md:2205, 45 = :2249, 59 = :2263, 68 = :2272):

```text
== DECISIONS 2232 numbered
2232	**The amended breaker text.** The proposal's replacement text for breakers #4 and #5 is adopted as the amended breaker spec. Copied by script from proposal :36 and :38:
== DECISIONS 2108
**V2 — Rule F2-1: APPROVED (A6).** (return-handoff :45–48.) The words put to Amear were the channel's summary, return-handoff :46: "flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00; no new system entries 16:00–18:00 ET." Amear: "Uh, yeah, you have my approval." (return-handoff :47). It is filed as closing the A6 hold, that is, Amear's approval, the first of the three parts OPEN-F2-5 names at `docs/specs/2026-11-10-f2-session-flat-proposal.md`:79 (its resolution cell, copied by script: "Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec."), on the words put to him at return-handoff :46. The amended #4/#5 text does not exist, and OPEN-F2-5 is not closed by this entry. Whether his approval reaches the elements (a)–(f) listed below, which were not put to him in those words, is not graded here. That file is called the proposal below. Rule F2-1 as the proposal writes it, copied by script from proposal :20:
== D-2026-11-12-A block 2205-2280 grep for limits
1:## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to match Rule F2-1 (rubric F2; master under D-2026-11-08-D D1)
3:**Status:** Decided by master under D-2026-11-08-D D1, changeable by Amear. Not Amear's ruling. A spec amendment only: nothing is built.
4:**Authority:** DECISION_LOG.md:854 (row 2026-11-12T05:29:00Z, WHO: praxis-master, unit `2026-11-12-f2-breaker-amendment`, Unit F2B); at filing that row sits in the working copy, after the 851 lines of DECISION_LOG.md at HEAD `9905804`. Rule F2-1's approval: D-2026-11-11-A, V2 (DECISIONS.md:2108–2116). D1: `specs/SPEC_RUBRIC.md`:437–442. Every quotation in this entry is copied by script, byte-identical to the cited line or to the stated part of it. The row's item (1), copied by script from DECISION_LOG.md:854:
45:**Why this is the master's decision, changeable by Amear.** Amear's approval (D-2026-11-11-A, V2) was given on the words put to him, "flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00; no new system entries 16:00–18:00 ET." (as copied at DECISIONS.md:2108). That entry records, copied by script from DECISIONS.md:2108: "The amended #4/#5 text does not exist" and "Whether his approval reaches the elements (a)–(f) listed below, which were not put to him in those words, is not graded here." Its element (f), copied by script from DECISIONS.md:2116: "(f) the proposed replacement text for breakers #4 and #5 (proposal :36, :38)." So his approval reached Rule F2-1 as summarised, and whether it reaches element (f) is ungraded. This entry does not read his approval as reaching (f). The adoption of the #4/#5 text is the master's, under D1, and Amear may change it. The master's reading (not graded by anyone else): the adopted text keeps the three parts of the summary — #4 flattens by 16:00 ET and refuses new system entries until 18:00 ET; #5 no longer disables the system's own trading, so a position open at 15:00 may stay open until 16:00.
54:    permissions. Everything else is D1.
59:**Level.** The nine breakers, #4 and #5 included, remain SPECIFIED ONLY: zero implemented, zero tested, zero tested under failure (Phase 3 import status note, :11). This entry changes text, not level.
68:This entry names the governing rule (Rule F2-1) and the 15:00 disposition, and records the amendment of #4 and #5. It does not grade the clause and does not change F2's state. The F2 state move is a later, separate unit after this unit is audited and committed; DECISION_LOG.md:854 item (4), copied by script: "(4) the rubric F2 state move is a later, separate unit after this one is audited and committed (F1 precedent `b4c3291` → `d30ab4d`)." A6 ties F2's state change to Amear's approval (DECISIONS.md:1744–1745); whether A6 is triggered is not graded here. Citation note, not an edit: the proposal :8 cites the unblock clause as (`specs/SPEC_RUBRIC.md`:43–44); the clause is at :30–31.
76:## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine authorised, first pass only (Mac-side Python event simulator on the 1-minute file; master under D-2026-11-08-D D1)
78:**Status:** Decided by master under D-2026-11-08-D D1, changeable by Amear. Not Amear's ruling. An authorisation entry only: at filing no R6 step 2 code, run or result exists.
79:**Authority chain.** Amear's ruling D-2026-11-08-A R6 (DECISIONS.md:1572–1579: research and backtest on the existing 1-minute data only, nothing bought), pulled forward to P0 by Amear's D-2026-11-08-D D7 (DECISIONS.md:1940–1944) after D6 failed (HANDOFF.md:289 at `c29d08b`: "D6 result → D7 FIRED"). D1: `specs/SPEC_RUBRIC.md`:441–445. R6 step 1 design: `bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`, on branch `r6/announcement-research` in the worktree `/Users/admin/Praxis.build-r6`, not on `main` (cited below as "design :N"). The master's closures of R6 OPEN-3 and OPEN-4 (H01, H03): DECISION_LOG.md:765 (row 2026-11-09T17:32:00Z). This run's master row: DECISION_LOG.md:861 (row 2026-11-12T09:03:23Z, items (c) and (d)); at filing that row sits in the working copy, after the 859 lines of DECISION_LOG.md at HEAD `c29d08b`. Bead `Praxis_build-ckh`. Fenced quotations below are whole lines copied by script from the cited source; short quotations in running text are parts of the cited line.
== proposal line 95 bytes check
line95 valid UTF-8
specs/SPEC_RUBRIC.md`:93–94
0
== rubric HEAD :81 and PASSED heading
17:## FROZEN — nothing downstream may proceed until these clear
46:## PASSED — closed criteria
81:### F2 — Session-flat time vs. breakers #4 and #5
99:## OPEN — gradeable now
123:## Standing criteria — graded on every dispatch
256:## Process rulings — binding on the orchestrator
434:## Autonomy — D1–D5, 2026-11-08 human ruling (D-2026-11-08-D; DECISION_LOG 2026-11-08T19:57:00Z, WHO: amear)
```

### C6 — OPEN-F2-5 inside D-2026-11-12-A, rubric at `e3323a8` :30–31, prior worker's findings

Command:

```bash
cd /Volumes/Sensidine/Praxis.build && echo "== OPEN-F2-5 in D-2026-11-12-A (2205-2279)"; sed -n '2205,2279p' DECISIONS.md | grep -n 'OPEN-F2-5'; echo "== e3323a8 rubric 30-31"; git show e3323a8:specs/SPEC_RUBRIC.md | sed -n 30,31p; echo "== worker1 findings"; grep -n '^## ' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md; awk '/^## Findings/{f=1} f' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | head -60
```

Output:

```text
== OPEN-F2-5 in D-2026-11-12-A (2205-2279)
== e3323a8 rubric 30-31
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
== worker1 findings
3:## Task
9:## Checks run (command + full output)
541:## Attack-by-attack result
550:## Findings
## Findings

1. **MAJOR (observed at first read; cured in the working tree at mtime 2026-11-12T08:12:44, while this review ran).** Proposal note line 95, the F-7 citation. At first read it was `` `specs/SPEC_RUBRIC.md`: `` + bytes `80 93` + `94`: invalid UTF-8, with "93" and the en-dash lead byte missing (C3a). F-7's whole purpose is this line number, so the follow-up was misstated, and the public file would have rendered replacement characters. The current file reads `:93–94` and is valid UTF-8 (C3b). Fix already applied by someone else. Suggestion: before staging, re-run `python3 -I -c 'open("docs/specs/2026-11-10-f2-session-flat-proposal.md","rb").read().decode("utf-8")'`, then cmp line 95 against the MANIFEST row 448 text. I did not make this edit, and I do not know who did.
2. **MINOR — topology :136 (aligned reading for :41).** "...('the n8n/consumer window check is then removed'); D-2026-11-12-A adopts that text." Read naturally, "that text" is the topology :62 row text. D-2026-11-12-A adopts something else, "The proposal's replacement text for breakers #4 and #5" (DECISIONS.md:2232). The same entry also says the topology document is not edited (:2274). Removing the check follows from the adopted #5 text, through proposal :40. Fix: "D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232); proposal :40 states that, if adopted, the system window check is removed."
3. **MINOR — topology :184 (aligned reading for :78).** "its operator lockout cannot sit in the strategy either (B3, OPEN-T8)." B3 (:88) says "Nothing on this path can gate a human order", and "this path" is option 1's. OPEN-T8 (:105) leaves the enforcement open ("Block 3 design under D1"), and D-2026-11-12-A does not decide it (:2274). Ruling out a strategy-resident lockout narrows OPEN-T8 without a source. Fix: "#5 has no system check to move; where its operator lockout sits, including whether the strategy could carry it, is OPEN-T8 (:105)."
4. **MINOR — proposal :103 (F-9).** The note opens "OPEN-F2-5 is closed." without qualification. The item's decider is "Amear's approval under A6; then ... the amended #4/#5 text". D-2026-11-12-A records that "whether A6 is triggered is not graded here" (DECISIONS.md:2272). It also records that whether his approval reaches element (f), the #4/#5 text, is ungraded (:2249). The note carries both limits in the same paragraph, so this is not a false claim, but the lead sentence states the result at a higher level than its own caveats. Fix: "OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits:"
5. **MINOR (process) — the artifact changed during adversarial review.** Topology and ruleset mtime 2026-11-12T08:10:48; proposal 08:12:44 (C3b). My first reads came before at least the proposal edit (C3a and C3b differ). I re-ran every check at 08:15:12 (C1c). The grade binds only to sha1 prefixes topology `5aea715d2ff4`, ruleset `b68c098f4aa1`, proposal `e1d2d72895b3`. Fix: the manager should confirm the staged blobs match these hashes, or send any later edit for a fresh check.

Standing MAJOR findings on the current files: 0. MAJOR observed and since cured: 1. MINOR: 4.

The verdict below holds only for the hashes in Finding 5. If the staged blobs differ, it does not hold.

Verdict: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
```

The `OPEN-F2-5` grep inside D-2026-11-12-A printed nothing: that entry does not name OPEN-F2-5.

### C7 — level words in all added lines; location of the three cured sentences; absence of the pre-cure wording

Command:

```bash
cd /Volumes/Sensidine/Praxis.build && for f in docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/specs/2026-11-10-f2-session-flat-proposal.md; do echo "== $f added lines matching level words"; git diff HEAD -- $f | grep '^+[^+]' | grep -n -i -E 'implemented|tested|is built|are built|enforced by|works|verified|IMPLEMENTED|TESTED' ; done; echo "== cured sentences, exact"; grep -n 'adopts the proposal' docs/specs/2026-11-10-live-signal-topology.md; grep -n 'including whether the strategy could carry it' docs/specs/2026-11-10-live-signal-topology.md; grep -n 'within D-2026-11-12-A' docs/specs/2026-11-10-f2-session-flat-proposal.md; grep -n -c 'cannot sit in the strategy either' docs/specs/2026-11-10-live-signal-topology.md; grep -n -c 'D-2026-11-12-A adopts that text' docs/specs/2026-11-10-live-signal-topology.md
```

Output:

```text
== docs/specs/2026-11-10-live-signal-topology.md added lines matching level words
3:+**Level.** Unchanged: the nine breakers, #4 and #5 included, remain SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure. This note changes how lines are read; it builds nothing.
7:+> 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry and manual changes to the system by the operator. The system's own trading is not disabled by this breaker; the system's no-entry period 16:00–18:00 ET is enforced by breaker #4.
12:+Aligned reading: the consumer-side checks on this path are #4, #7, #8 and #9. #5 has no check on the signal path: amended #5 does not disable the system's own trading, and the system's no-entry period 16:00–18:00 ET is enforced by #4. This is the case the #5 row (:62) already states for adoption of the F2 proposal ("the n8n/consumer window check is then removed"): D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232), and proposal :40 states that, if adopted, the system window check is removed.
45:+| B1 | A JSON file written straight into the drop dir `/Users/admin/praxis-signals`, into `incoming/`, or into the n8n outbox, by anything that can write as `admin`, or through any share that exposes the drop dir to the VM. D-2026-11-10-A (DECISIONS.md:2041) already reads it this way ("a file written straight into the drop dir would not pass those gates (inference from that text, not tested)"). | No. The consumer cannot tell a file that came through n8n from one that did not. | (a) The consumer-side checks #4, #5, #7, #8 and #9 still apply to such a file; #1, #2, #3 and #6 do not, because they run only in n8n. (b) n8n signs each gate-passed file (HMAC over the payload) and the consumer refuses unsigned files. That needs a key in n8n and in the VM: **waits for Amear (D2(d))**. (c) The `praxispush` user and drop-dir move (D-2026-11-10-A) narrow who can write. | (b) Amear, D2(d). (c) the deferral is decided (D-2026-11-10-A, DECISIONS.md:2039, "DEFERRED, not dropped"); provisioning stays with Amear (D2(d), :2043), so B1 stays open as an accepted risk until then. |
== docs/specs/2026-07-16-b2-noise-area-ruleset.md added lines matching level words
3:+**Level.** Unchanged: the nine breakers, #4 and #5 included, remain SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure. This note changes how lines are read; it builds nothing.
15:+| D8 | Flat time | **16:00** — no 11:30 stop in paper | b2-q1 report notes a **"flat-by-11:30-ET baseline"** | ❌ **CONFLICT** — 11:30 is a **PRAXIS window choice** (09:30–11:30 active hours), NOT the paper. The paper's edge is measured on full-day holds to 16:00; truncating at 11:30 is untested by the paper and changes expectancy |
== docs/specs/2026-11-10-f2-session-flat-proposal.md added lines matching level words
3:+**Level.** Unchanged: the nine breakers, #4 and #5 included, remain SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure. This note changes how lines are read; it builds nothing.
== cured sentences, exact
136:Aligned reading: the consumer-side checks on this path are #4, #7, #8 and #9. #5 has no check on the signal path: amended #5 does not disable the system's own trading, and the system's no-entry period 16:00–18:00 ET is enforced by #4. This is the case the #5 row (:62) already states for adoption of the F2 proposal ("the n8n/consumer window check is then removed"): D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232), and proposal :40 states that, if adopted, the system window check is removed.
184:Aligned reading: if the fallback is taken, the system checks that move into the strategy are those of #1–#4 and #6–#9; #5 has no system check to move; where its operator lockout sits, including whether the strategy could carry it, is OPEN-T8 (:105), not decided here.
103:Aligned reading: OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits. Each step its "What would decide it" column names now has a record: Amear's approval of Rule F2-1 (D-2026-11-11-A, V2, DECISIONS.md:2108); a DECISIONS.md entry (D-2026-11-12-A, DECISIONS.md:2205); the amended #4/#5 text in the breaker spec (Amendment 1 of the Phase 3 spec). Rubric F2 is PASSED@e3323a8. Limits carried from D-2026-11-12-A, not changed here: Amear's approval was given on the words of a summary; the #4/#5 text is the master's adoption under D1, not Amear's words, changeable by Amear; whether his approval reaches that text, and whether A6 is triggered, are not graded.
0
0
```

## Findings

**(a) Finding 2 (topology :136, aligned reading for :41): CURED.** The sentence now reads "D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232), and proposal :40 states that, if adopted, the system window check is removed." DECISIONS.md:2232 (C5) reads "The proposal's replacement text for breakers #4 and #5 is adopted as the amended breaker spec." Proposal :40 (C4) reads "if adopted, the system window check is removed and only the operator lockout remains." The object of adoption is now stated exactly, and the old wording "D-2026-11-12-A adopts that text" has 0 matches (C7). Attack tried: proposal :40's "if adopted" refers to "this proposal", but D-2026-11-12-A adopts only the #4/#5 replacement text, and OPEN-F2-1 to OPEN-F2-4 (proposal :75–78, Correction-1 re-run evidence) stay open. That does not break the sentence. The removal of the system window check follows from the adopted #5 text itself, "The system's own trading is not disabled by this breaker" (topology note, copied from Phase 3 :224; that :224 holds those words is in Correction-1 re-run evidence). That is the part of the proposal that was adopted. No break.

**(b) Finding 3 (topology :184, aligned reading for :78): CURED.** The sentence now reads "#5 has no system check to move; where its operator lockout sits, including whether the strategy could carry it, is OPEN-T8 (:105), not decided here." OPEN-T8 (:105, C3) leaves enforcement to "Block 3 design under D1". The old wording that ruled out a strategy-resident lockout, "cannot sit in the strategy either", has 0 matches (C7). The cure narrows nothing: the list of moved checks (#1–#4 and #6–#9) follows from amended #5 not disabling system trading. No break.

**(c) Finding 4 (proposal :103, aligned reading for :79): CURED.** The lead sentence now reads "OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits." I checked each limit the paragraph lists against D-2026-11-12-A (C5):
- "approval was given on the words of a summary" matches :2249 ("given on the words put to him").
- "the #4/#5 text is the master's adoption under D1 ... changeable by Amear" matches :2207 and :2249 ("The adoption of the #4/#5 text is the master's, under D1, and Amear may change it").
- "whether his approval reaches that text ... not graded" matches :2249 ("whether it reaches element (f) is ungraded").
- "whether A6 is triggered ... not graded" matches :2272 ("whether A6 is triggered is not graded here").

Observation, not a break: D-2026-11-12-A never names OPEN-F2-5 (C6 grep is empty). So "closed" is the note's own reading of the three records, not a statement copied from the decision. The lead sentence frames it as closure "on the records below", and each of the three records exists. Finding 4 graded that as not a false claim; the check here is whether the lead is qualified. It is.

**(d) Finding 1 (proposal line 95): CONFIRMED CURED.** Line 95 is valid UTF-8, contains `` specs/SPEC_RUBRIC.md`:93–94 `` and has 0 U+FFFD bytes (C5). `git show HEAD:specs/SPEC_RUBRIC.md | sed -n 93,94p` returns the unblock clause, and the quoted words match the words cited at :8 (C4). The note's other claims check out:
- The section heading is at :81 under "## PASSED — closed criteria" at :46 (C5).
- At `e3323a8` the clause sits at :30–31 (C6).

**(e) Body identity: PASS.**
- Each HEAD blob equals the working file's leading bytes: topology 114 lines / 24094 bytes, ruleset 111 / 11354, proposal 81 / 12061 (C2).
- `git diff HEAD` shows 0 removed lines in each file (C1).
- `git diff --numstat HEAD`: topology `86 0`, ruleset `59 0`, proposal `30 0`.
- shasum (sha1): topology `5865a1121cd1b55783f217c4f341e20b7cfc03d5`, ruleset `b68c098f4aa1d3273ad179474299d662f1e0c243`, proposal `24598c3d73d8dd3a3961a7083aa8e42a68012362`.

Compared with worker 1's Finding 5 hashes, topology (`5aea715d2ff4`) and proposal (`e1d2d72895b3`) changed and ruleset (`b68c098f4aa1`) did not. That fits cures that touched only the topology and proposal notes. Worker 1's PASS bound only to its hashes, so this re-check is the grade for the current blobs.

**(f) No new design choice, no claim above SPECIFIED ONLY: PASS.** In C7, every added line that contains a level word is one of three kinds:
- the "SPECIFIED ONLY — zero implemented, zero tested" level statement;
- a text-level "enforced by #4" that copies amended #5's own wording (Phase 3 :224, "is enforced by breaker #4"; Correction-1 re-run evidence);
- an old HEAD line copied into a fence (B1 "not tested", topology HEAD :86; ruleset D8 "untested", ruleset HEAD :79; each HEAD line occurs twice in its working file, body and note fence: Correction-1 re-run evidence).

The three cured sentences add citations (a), replace a narrowing claim with a pointer to OPEN-T8 (b), and add a qualifier (c). None adds a placement, an enforcement mechanism or a level.

Scope limit: I held no copy of the pre-cure working-tree note text, so I could not diff old against new note text line by line. For (f) I checked the current text of the three cured sentences, confirmed the pre-cure wording is gone (0 matches, C7), and scanned all added lines.

Findings count: 0 breaks. 1 observation: D-2026-11-12-A does not itself name OPEN-F2-5, so "closed" is the note's reading, qualified as required.

Verdict: PASS

## Correction-1 re-run evidence (2026-11-12)

Re-run 2026-11-12 by correction-1. Script `/tmp/fgdc1/ev-worker2.sh`; its output is pasted verbatim below. Each command is shown as `$ cmd`, then its full output, then `(exit N)`.

```text
$ git rev-parse --short HEAD; git branch --show-current
006a08b
main
(exit 0)
$ git log -1 --format='%h %s' | cut -c1-60
006a08b ledgers: flush DECISION_LOG 2026-11-12T09:03Z throug
(exit 0)
$ git diff --cached --name-only | wc -l; git diff --cached --name-only -- docs/specs docs/reports/2026-11-12-fgd-doc-alignment-worker2.md DECISIONS.md | wc -l; git diff --cached --name-only | grep -c '^docs/reports/evidence/.*\.png$'
       1
       0
1
(exit 0)
$ zsh -c 'x="a 1"; set -- $x; echo $#'
1
(exit 0)
$ bash -c 'x="a 1"; set -- $x; echo $#'
2
(exit 0)
$ shasum docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/specs/2026-11-10-f2-session-flat-proposal.md
5865a1121cd1b55783f217c4f341e20b7cfc03d5  docs/specs/2026-11-10-live-signal-topology.md
b68c098f4aa1d3273ad179474299d662f1e0c243  docs/specs/2026-07-16-b2-noise-area-ruleset.md
24598c3d73d8dd3a3961a7083aa8e42a68012362  docs/specs/2026-11-10-f2-session-flat-proposal.md
(exit 0)
$ git show HEAD:DECISIONS.md | wc -l; wc -l < DECISIONS.md
    2278
    2370
(exit 0)
$ cmp <(git show HEAD:DECISIONS.md | sed -n '1,2278p') <(sed -n '1,2278p' DECISIONS.md) && echo "DECISIONS.md lines 1-2278 identical HEAD vs working tree"
DECISIONS.md lines 1-2278 identical HEAD vs working tree
(exit 0)
$ git diff --numstat HEAD -- docs/specs/2026-11-05-phase3-build-specification.md | wc -l
       0
(exit 0)
$ sed -n 224p docs/specs/2026-11-05-phase3-build-specification.md | cut -c1-60
> 5. Session window (operator lockout) — clock is in 3:00–6:
(exit 0)
$ grep -n -o -F "The system's own trading is not disabled by this breaker" docs/specs/2026-11-05-phase3-build-specification.md
224:The system's own trading is not disabled by this breaker
(exit 0)
$ grep -n -o -F "is enforced by breaker #4" docs/specs/2026-11-05-phase3-build-specification.md
224:is enforced by breaker #4
(exit 0)
$ sed -n '75,78p' docs/specs/2026-11-10-f2-session-flat-proposal.md | cut -c1-40
| OPEN-F2-1 | Backtest flat on the 15:59
| OPEN-F2-2 | R6 variants that hold to 1
| OPEN-F2-3 | Early-close stamps 12:15 v
| OPEN-F2-4 | Whether R8's #8 numbering 
(exit 0)
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n 86p | grep -o 'not tested'
not tested
(exit 0)
$ grep -c -x -F "$(git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n 86p)" docs/specs/2026-11-10-live-signal-topology.md
2
(exit 0)
$ git show HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md | sed -n 79p | grep -o 'untested'
untested
(exit 0)
$ grep -c -x -F "$(git show HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md | sed -n 79p)" docs/specs/2026-07-16-b2-noise-area-ruleset.md
2
(exit 0)
$ grep -n '^## Findings' /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker1.md
/tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md:550:## Findings
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md:550:## Findings
(exit 0)
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
