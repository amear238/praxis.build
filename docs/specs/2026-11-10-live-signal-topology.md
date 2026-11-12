# Live signal topology and circuit-breaker placement (rubric F1)

Status: RECOMMENDATION. Decided by master under D-2026-11-08-D D1; changeable by Amear.
Unit: 2026-11-10-f1-f2-proposal (authorisation: DECISION_LOG.md row 2026-11-10T13:03:00Z, praxis-master, item (2)). Bead context: `Praxis_build-2nh`.
Evidence for every repo-based claim below is pasted in `docs/reports/2026-11-10-f1-f2-proposal-manager.md`, section "Verification evidence (command output)", under the tag given in square brackets (for example [E3]).

This document does not clear F1. F1 clears when this file is committed and the auditor confirms it addresses every one of the nine breakers by name (`specs/SPEC_RUBRIC.md`:28–29). It builds nothing, changes no code, no workflow and no account.

Level words, used exactly: SPECIFIED (written in a spec only), WRITTEN (code or config exists, not run), TESTED (run, behaviour observed), TESTED UNDER FAILURE (deliberately tripped, block observed), UNVERIFIED (not observed in this unit, or the records disagree). Specified is not implemented is not tested.

---

## 1. What exists on the signal path today

| # | Component | What the repo shows | Level | Evidence |
|---|---|---|---|---|
| 1.1 | Arm (a), replication: `ninjascript/PraxisNoiseAreaBreakout.cs` (and the `_Flat1559`, `_OppBand` exit variants on main) | A self-contained Strategy Analyzer backtest. Its header says it "is NOT the file-drop signal consumer … it carries no order pipeline, no JSON, no share watcher" (:25–27). It calls `EnterLong` / `EnterShort` / `ExitLong` / `ExitShort` itself (:211, :219, :227, :229, :288, :290). It emits no signal file and no webhook call. | Backtest: run in the Strategy Analyzer (the 2026-11-01 trade lists are committed, `a587a27`). As a live signal emitter: none exists. | [E3], [E4] |
| 1.2 | Arm (b), tunables: `ninjascript/PraxisNoiseAreaBreakoutArmB.cs` | On branch `arm-b/wf-tunables` only, commit `c16f85f`, whose message says "WRITTEN, not compiled, not run". Backtest strategy; no file emission. | WRITTEN | [E5] |
| 1.3 | Last-Half-Hour Momentum: `ninjascript/PraxisLastHalfHourMomentum.cs` | Header: "WRITTEN, NOT COMPILED, NOT TESTED"; backtest strategy: enters at 15:30 ET, "flat on the 15:59 bar" (`Description`, :141). Retired per the strategy filter audit (:110). | WRITTEN | [E6] |
| 1.4 | R6 Pre-Announcement Drift, evening entry | A PROPOSED research design on branch `r6/announcement-research` (`bf6fcc7`); no strategy code. | SPECIFIED | [E15] |
| 1.5 | TradingView as the emitter | The anchor strategy is "NOT TradingView-exportable"; "no Pine source anywhere in repo" (DECISION_LOG 2026-07-15T21:10Z). `git ls-files` shows no Pine file. | Not an emitter for the anchor strategy | [E2], [E7] |
| 1.6 | Any LIVE trading signal | Nothing in the repo computes the anchor signal outside the backtester, and nothing emits a live signal. The drop dir's processed-signals log was last written Jul 15 (the Block 1 test run); `incoming/` is empty. | No live emitter exists (this unit's reading of [E3]–[E8]; the VM was not observed, so whether any strategy is enabled on a live data connection in NT8 right now is UNVERIFIED) | [E8] |
| 1.7 | n8n workflow | Container `n8n-compose-n8n-1` is up. Workflow "PRAXIS — Signal Webhook (Block 0)" is `active: True`, last updated 2026-07-16. Nodes: webhook `praxis-signal` → Validate Signal Payload → Is Payload Valid → Write Signal File → Respond 200 / 500 (+ Telegram notifies). There is no Redis node, no PostgreSQL node and no breaker node. The workflow JSON is not in the repo (no `n8n/` directory). | Path: TESTED (Block 1 milestone, signed off 2026-07-15, test webhook posts). Breaker gates in n8n: none exist. | [E9], [E10], [E1] |
| 1.8 | Redis / PostgreSQL breaker state | Two Redis containers run on the host, both under other compose projects' names; the PRAXIS workflow has no Redis node (1.7), so no breaker state store is wired to the signal path. | SPECIFIED only (Phase 3 spec :107) | [E9], [E10] |
| 1.9 | Public ingress (Deviation G) | D-2026-07-09-D: n8n runs locally; how live TradingView signals reach it "is deferred to pre-live (Block 4–5)". A committed record says the workflow `EmMbN4sslwIx1ydn` was once published at a public address (HANDOFF.md:1539, commit `936d7e4`, Step 0.5; address not reproduced here). Whether the webhook is reachable from outside the host today was not observed here. | UNVERIFIED | [E11], [E29] |
| 1.10 | File drop and relay | n8n writes JSON into the outbox `/Users/admin/n8n-compose/local-files/outbox`; the sweep daemon (`build.praxis.signals-sweep-daemon`, loaded with a pid) moves it via `incoming/` into `/Users/admin/praxis-signals`. The drop dir is owned by `admin`; no `praxispush` user exists (D-2026-11-10-A). How the current VM reaches the drop dir: the records differ (D-2026-11-10-A, DECISIONS.md:2026–2045). | Relay: TESTED in Block 1 (Parallels era). On the current VM: UNVERIFIED. | [E12], [E13] |
| 1.11 | `ninjascript/PraxisSignalConsumer.cs` | FileSystemWatcher on `*.json` (:164–165); validates schema, `qty > MaxQty` reject (MaxQty default 5, :94, :527–528), geometry gate, signal_id dedup; parses `ts` (:537–538) but never compares its age with the clock (the only uses of `tsParsed` are :537–538); hard Sim-account wall (:39, :98–107, :638–641). | TESTED on Sim in Block 1 (B1-f T1–T4). MaxQty reject path as a breaker: UNVERIFIED (Phase 3 import :11 says untested as a breaker). | [E14] |
| 1.12 | Order submission | `SubmitBracket` in `PraxisSignalConsumer.cs`: `SetStopLoss` / `SetProfitTarget`, then `EnterLong(sig.Qty, …)` / `EnterShort(sig.Qty, …)` (:660, :662). This is the only place on the file-drop path that submits an order. The backtest strategies (1.1–1.3) submit their own orders inside NT8 when run. | TESTED on Sim (Block 1). Not run against any MFFU account. | [E14] |
| 1.13 | The nine circuit breakers | Phase 3 import status note: "zero implemented, zero tested, zero tested under failure" (:11). Re-run here: the only "breaker" hit in `ninjascript/` is a comment in `_Flat1559.cs`:31. | SPECIFIED | [E1] |

**Plainly: today no live trading signal is emitted by anything, and none of the nine breakers exists in code or workflow.** The Block 1 pipe (webhook → n8n → file → consumer → Sim bracket) is TESTED, but it is fed only by test posts, and it carries no breaker.

---

## 2. What emits the live trading signal going forward

**Recommendation (Decided by master under D-2026-11-08-D D1; changeable by Amear).**

The live trading signal is emitted by **a new NT8 signal-emitter strategy** (working name `PraxisNoiseAreaEmitter`, not built). It runs the same Noise-Area band logic as `PraxisNoiseAreaBreakout.cs`, on bar close, but it never calls `EnterLong`, `EnterShort`, `ExitLong`, `ExitShort` or any order method. Instead it sends each decision (entry, exit, reverse, session flat) as an HTTP POST to the existing local n8n webhook `praxis-signal`. n8n runs the breaker gates and only then writes the signal file. `PraxisSignalConsumer.cs` stays the **only** component that submits orders.

Path: NT8 emitter (computes signal) → HTTP POST → n8n webhook → **[breaker gates, Redis, default closed]** → Write Signal File → outbox → sweep daemon → drop dir → `PraxisSignalConsumer` → **[consumer-side checks #4, #5, #7, #8, #9]** → `SubmitBracket` → Rithmic → account.

**How the decision rule was applied.**
1. Every one of the nine breakers must sit upstream of order submission on the live path. Under this topology, every gate check runs before `SubmitBracket` (table, section 3). The flatten and close actions of #1, #4 and #6 are orders themselves; section 3 says where they come from.
2. Keep the Phase 3 placement (n8n gates before the file-write node, Redis, default state closed) unless repo evidence shows the live signal cannot pass through n8n. The repo shows the signal **cannot come from TradingView** (1.5) and that today it is **computed only inside NT8** (1.1). It does **not** show that an NT8-computed signal cannot be posted to n8n: nothing in the repo tests or rules out the VM reaching the Mac's n8n webhook. So the Phase 3 placement is kept, with the emitter moved from TradingView to NT8. Whether the VM can reach the webhook is OPEN-T1 below; if it cannot, the fallback in section 4 applies.
3. Fewest unbuilt components. Compared in section 4.

**What changes from the Block 1 architecture.** The emitter is NT8, not TradingView (CLAUDE.md "Signal flow: TradingView alert → webhook → …"). Deviation G's public-ingress question stops being on the anchor strategy's live path, because the emitter posts from inside the local network. Breakers #4, #5, #8 and #9 gain a consumer-side check (section 3), because n8n cannot measure relay delay after its own write, and cannot vouch for itself when it is down.

---

## 3. The nine breakers on that path

Names are exactly as the Phase 3 import lists them (`docs/specs/2026-11-05-phase3-build-specification.md`:97–105, at HEAD) [E1]. Every row's current level is SPECIFIED: no breaker exists in code or workflow (1.13). "Upstream" means the check runs, and can stop the order, before `SubmitBracket` calls `EnterLong` / `EnterShort`.

| # | Breaker (Phase 3 name) | Where it sits on the path | Why that is upstream of order submission | State it needs | Level now | Depends on |
|---|---|---|---|---|---|---|
| 1 | Daily loss limit | n8n gate node, before Write Signal File: Redis flag `gate:daily_loss` (closed when realised + unrealised P&L ≤ −threshold, or when the P&L reading is stale). Its "cancel all, flatten" action: n8n writes a FLATTEN command file that the consumer executes, plus resting stops on every live position (R-VN4-2: "Until the account is live … resting stops.", REPORTED BY the voice agent; the reading "resting stops once live" is the voice agent's, Phase 3 import :24–25) [E27]. | The gate stops every new entry signal before the file is written, so no file reaches the consumer and no order is submitted. The flatten is an order itself; it is a risk-reducing exit, not a new entry, and must never be blocked by a closed gate (OPEN-T2). | Realised + unrealised P&L for the session, in real time, from the NT8 account; the threshold. | SPECIFIED. No numeric threshold exists anywhere (`docs/reports/2026-11-09-d6-drawdown-check-manager.md`:39, :65). | An account-state feed from NT8 to Redis (unbuilt); EXIT and FLATTEN instruction types in the payload and the consumer (unbuilt; the consumer only knows BUY/SELL, :516–520, and only calls `EnterLong` / `EnterShort`, :660, :662 [E14]; under NT8's managed approach an `EnterShort` while long reverses into a short, `PraxisNoiseAreaBreakout.cs`:224, so an exit sent as SELL would open a position); a threshold value (R8 KEEP; value PROPOSED by a later unit; D2(c) once real money is at stake). |
| 2 | Max trades per day | n8n gate node, before Write Signal File: Redis counter of entries this session; gate closes when count = max. | Same as #1: the entry signal is dropped before the file write. | Count of entries submitted this session (from the consumer's journal or fills); the session boundary; the max value. | SPECIFIED | A fill/entry feed back to Redis (unbuilt); session boundary (F2 proposal, H02); value (R8 says "redone", PROPOSED). Deviation C reverse-and-re-enter counts as an entry (O4, bead `Praxis_build-yra`). |
| 3 | Consecutive loss (“two and done”) | n8n gate node, before Write Signal File: Redis counter of consecutive losing closed trades this session; closes at 2, "identical to max trades". | Same as #2. | Closed-trade results in order, this session. | SPECIFIED | Fill/P&L feed (unbuilt); session boundary; R8 says "redone". |
| 4 | Session time gate | Two checks: an n8n gate node before Write Signal File (ET clock; entries refused after the flat time until the next session), and an ET clock check in the consumer before `SubmitBracket`, so a file written just before the cut-off, or dropped straight into the drop dir (bypass B1), is still refused after it. Its "close positions" action: the emitter's own time exit posted as a FLATTEN signal, plus the FLATTEN command from n8n at the gate time. | The n8n check runs before the file write; the consumer check is the last step before `EnterLong` / `EnterShort` and bounds the relay delay that n8n cannot see after its own write. | ET wall clock; the flat time and the next-session start (both are F2's; see `docs/specs/2026-11-10-f2-session-flat-proposal.md`, PROPOSED). | SPECIFIED | F2 (FROZEN); FLATTEN path (unbuilt); the deterministic fallback script for when n8n is down (Phase 3 :109; unbuilt). |
| 5 | Afternoon session window | As the Phase 3 text stands: an n8n gate node before Write Signal File plus the same consumer clock check as #4, refusing every system entry (including Noise-Area reversals) in the window. Under the F2 proposal (`docs/specs/2026-11-10-f2-session-flat-proposal.md`, PROPOSED, not adopted) #5 becomes an operator lockout only, and the system no-entry period 16:00–18:00 moves into #4; the n8n/consumer window check is then removed. | As the text stands, the n8n check runs before the file write and the consumer check before `SubmitBracket`; nothing in the window becomes an order. | ET wall clock; the window. | SPECIFIED | F2. R8 splits #5 into a disable of the system's own trading (redone) and a lockout on Amear's own interaction (KEPT). **The lockout half cannot sit on this path**: a manual order typed into NT8 or the broker platform never passes n8n (bypass B3, section 5). |
| 6 | Trailing drawdown proximity | n8n gate node, before Write Signal File: Redis flag closed when account equity is within a margin of MFFU's EOD trailing drawdown level; "reduce size" means n8n rewrites `qty` downward before the write. | The check runs before the file write, so a halted or resized entry is decided before any order exists. | Account equity, the EOD trailing drawdown level for the account tier, the proximity margin. | SPECIFIED | Account-state feed (unbuilt); the margin value (none exists); tier values (A4; F4 FROZEN). D2(c) once real money is at stake. |
| 7 | Max position size | Two checks: n8n gate node before Write Signal File (qty vs plan), and the consumer's existing `qty > MaxQty` reject before `SubmitBracket`. | Both run before `EnterLong` / `EnterShort`. The consumer check is the last one before submission and also catches a file that skipped n8n. | The plan size (1 contract in the backtests); current open position (an entry plus an open position can exceed plan even when each signal's qty does not). | SPECIFIED. The consumer's MaxQty cap (default 5) is WRITTEN and resembles #7; it is not set to plan and has not been tested as a breaker. The consumer also sets `EntriesPerDirection = 10` (:82, "allow several concurrent signals"), so open position is not capped at plan today. | Plan size value; position read-back in the consumer (NT8 `Position`, available in-strategy). |
| 8 | Stale signal filter | Two checks: n8n gate node on receipt (payload `ts` vs clock), and a new consumer check before `SubmitBracket` (payload `ts` vs clock at the moment of submission). | The consumer check is the last step before submission and measures the whole delay, including the relay. n8n alone cannot see delay added after its own write. | Payload `ts` (already required and parsed, :537–538); a synchronised clock on the Mac and in the VM; X seconds. | SPECIFIED. The consumer parses `ts` but has no age check (1.11). | X value (none exists); VM clock sync (UNVERIFIED). R8 lists "#8 inter-trade interval under 5 minutes", which is not the Phase 3 import's #8 (OPEN-T6). |
| 9 | Heartbeat dead-man switch | In the consumer, before `SubmitBracket`: refuse new entries if the n8n-written health stamp is older than 5 minutes. Redis default-closed covers the case where n8n runs but cannot confirm state. | If n8n is dead, an n8n gate cannot run, so the check has to sit at the consumer, which is still upstream of submission. | A health stamp written by n8n (today the drop-dir `.heartbeat` is written by the sweep daemon, not by n8n [E12]); the clock. | SPECIFIED | An n8n health-stamp workflow (unbuilt); the consumer check (unbuilt); what "confirmed system health" covers (OPEN-T7). |

---

## 4. Options compared (fewest unbuilt components)

| Option | Emitter | Where the gates run | Unbuilt components | Keeps Phase 3 placement |
|---|---|---|---|---|
| **1 (recommended)** | NT8 emitter strategy posts to the local n8n webhook | n8n + Redis before the file write; #7/#8/#9 also in the consumer | emitter strategy; VM → n8n reach (OPEN-T1); EXIT/FLATTEN instruction types; consumer clock check for #4/#5; n8n gate nodes; Redis gate keys; PostgreSQL trip log; account-state and fill feed into Redis; FLATTEN command in the consumer; consumer checks for #8/#9 (and #7 at plan size); n8n health stamp; fallback script | Yes |
| 2 | A Mac-side program computes the band from a live data feed and posts to n8n | Same as 1 | everything in 1 except the NT8 emitter, plus a live NQ data feed on the Mac and a second implementation of the band logic (a data subscription may cost money, D2(a), waits for Amear) | Yes |
| 3 (fallback) | NT8 strategy computes the signal and gates itself | In NinjaScript, before its own `EnterLong` / `EnterShort` | gate code in the strategy; account-state read (available in NT8); trip log; heartbeat source; fallback script | No: there is no n8n gate and no Redis; the Block 1 pipe is unused |

Option 3 has the fewest unbuilt parts, because NT8 already holds account P&L, position and clock. The decision rule puts the Phase 3 placement first unless the evidence shows the signal cannot pass through n8n, and it does not show that today. So option 1 is recommended, and option 3 is the fallback **only if** OPEN-T1 finds the VM cannot reach the webhook. If the fallback is taken, what changes: all nine checks move into the strategy before its order calls; Redis default-closed becomes a strategy default (no entries until every check has been confirmed this session); #9 needs an outside health source the strategy can read.

---

## 5. Bypass routes: ways an order can reach submission without passing the gates

| # | Route | Does it pass the n8n gates? | What would close it | Who decides |
|---|---|---|---|---|
| B1 | A JSON file written straight into the drop dir `/Users/admin/praxis-signals`, into `incoming/`, or into the n8n outbox, by anything that can write as `admin`, or through any share that exposes the drop dir to the VM. D-2026-11-10-A (DECISIONS.md:2041) already reads it this way ("a file written straight into the drop dir would not pass those gates (inference from that text, not tested)"). | No. The consumer cannot tell a file that came through n8n from one that did not. | (a) The consumer-side checks #4, #5, #7, #8 and #9 still apply to such a file; #1, #2, #3 and #6 do not, because they run only in n8n. (b) n8n signs each gate-passed file (HMAC over the payload) and the consumer refuses unsigned files. That needs a key in n8n and in the VM: **waits for Amear (D2(d))**. (c) The `praxispush` user and drop-dir move (D-2026-11-10-A) narrow who can write. | (b) Amear, D2(d). (c) the deferral is decided (D-2026-11-10-A, DECISIONS.md:2039, "DEFERRED, not dropped"); provisioning stays with Amear (D2(d), :2043), so B1 stays open as an accepted risk until then. |
| B2 | Any NT8 strategy that places its own orders, enabled on a live data connection with an account: the backtest strategies in 1.1–1.3, or an emitter built wrongly. | No. These strategies call `EnterLong` / `EnterShort` directly, and they have no Sim wall. | The emitter carries no order calls (checkable by `grep`); a rule that backtest strategies are never enabled on an account connection. Enforcement in code is not designed here (OPEN-T5). | Build rule under D1; the live order path to a funded account **waits for Amear (D2(b))**. |
| B3 | Manual orders typed into NT8, Rithmic or the MFFU platform. | No, never. | Nothing on this path can gate a human order. R8's KEPT half of #5 (lockout on Amear's own interaction) needs a separate mechanism, not designed here (OPEN-T8). | Amear. |
| B4 | n8n down or Redis unreachable. | Not applicable: no file is written, so no entry order. | Default closed (Phase 3 :107). Open positions are then protected only by resting stops and the fallback script (Phase 3 :109), both unbuilt. | Build. |
| B5 | Anything that can POST to the webhook. | Yes, it passes the gates like any signal. Not a gate bypass; an injection risk if the webhook is reachable from outside (1.9, UNVERIFIED). | Webhook authentication (a credential: **waits for Amear (D2(d))**). | Amear, D2(d). |

---

## 6. OPEN items

| ID | What is undecided | What would decide it |
|---|---|---|
| OPEN-T1 | Can an NT8 strategy in the VM reach the Mac's n8n webhook over HTTP? | A read-only reachability test from the VM on its next session. If it cannot, option 3 applies (section 4). |
| OPEN-T2 | Closed gates must block new entries and never block exits or flattens, which needs the payload to say which a signal is (EXIT / FLATTEN types, unbuilt; today an exit can only be sent as BUY/SELL, which the consumer turns into an entry). Phase 3 says only "if any gate is closed, the workflow terminates before reaching the file-write node" (:107). | A gate-semantics spec for the breaker build (Block 3), splitting entry signals from risk-reducing signals. |
| OPEN-T3 | Where account state (P&L, equity, fills, open position) comes from, and how fresh it must be. | Block 3 design. Reads from NT8's account in the VM are the nearest source. |
| OPEN-T4 | Breaker values: #1 threshold, #2 max, #6 margin, #7 plan size, #8 X seconds. | A later PROPOSED values unit (R8, A6). Changing values while real money is at stake **waits for Amear (D2(c))**; today none is. |
| OPEN-T5 | How to stop a self-trading NT8 strategy from being enabled on an account connection (B2). | Block 3 design. |
| OPEN-T6 | R8's "#8 inter-trade interval under 5 minutes" (DECISIONS.md:1583–1589) does not match the Phase 3 import's #8 "Stale signal filter" (:104). The strategy filter audit numbers breakers from a different source table (its #8 "cascade detector", #9 a round-number block; audit :75, :78). Which numbering R8 uses is Amear's to say. | A reading by the master under D1 (not a D2 item), changeable by Amear; or Amear. This document uses the Phase 3 import's names and numbers. |
| OPEN-T7 | What "confirmed system health" in #9 covers (n8n alive only, or n8n plus Redis plus relay plus consumer). | Block 3 design. |
| OPEN-T8 | How R8's lockout on Amear's own interaction 15:00–18:00 is enforced, since manual orders never pass n8n (B3). | Block 3 design under D1; it binds Amear's own conduct, so he may overrule it. |
| OPEN-T9 | Any order path to a funded account. | **Waits for Amear (D2(b))**. D8(8): the final step of this build is a Block 4 paper pass on MFFU sim; Block 5 live is a separate sign-off. |

---

## 7. Cross-block touches (S6)

This topology touches: Block 1 (the emitter changes from TradingView to NT8; the TESTED pipe is reused; Deviation G's ingress question leaves the anchor's live path); Block 2 (the emitter must reproduce the backtest strategy's decisions, so O4 parity now also covers emitter-vs-backtest equality); Block 3 (all nine breakers, Redis, PostgreSQL, the fallback script); Block 4 (the paper pass on MFFU sim runs on this path, D8(8)); Block 5 (live, D2(b)); Deviation A (strategy logic in NinjaScript, kept; now also the emitter); Deviation C (reversals are entries for #2, bead `Praxis_build-yra`); Deviation G (D-2026-07-09-D); D-2026-11-10-A (bypass B1); rubric F2 (the flat time and session boundary for #4/#5); rubric F4 (MFFU automation, FROZEN); rubric O2 (`praxispush`); rubric O4 (parity); the SHM thresholds that F1 blocks (`specs/SPEC_RUBRIC.md`:30).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

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
