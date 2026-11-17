# PRAXIS — handoff for a fresh planning session

**Paste this whole file into a new chat. First action there: invoke `/superpowers`
and run the brainstorming skill BEFORE writing any plan.**

---

## What you are planning

**Not** the NinjaTrader clicking. That is a separate document and a human does it.

You are planning **how PRAXIS clears frozen criterion F3 and gets one useful trip
to the Windows VM out of it.** The deliverable is a written plan, not code.

---

## The project in one paragraph

PRAXIS is an automated NQ futures trading system. Signal flow: TradingView →
n8n → NinjaTrader 8 → Rithmic → MFFU (a prop firm). Repo lives at
`/Volumes/Sensidine/Praxis.build`. It is currently in **Block 2 — Backtesting**.
No trading code has moved in roughly ten sessions; the work has all been
supervision and process. `HEAD` = `c41a969`, 9 paths staged, nothing committed
since 2026-08-09.

The human is **Amear**. He is the only actor who can commit (a hook denies the
agent any command containing `>`, which the mandatory commit trailer contains),
the only one who edits `specs/SPEC_RUBRIC.md`, and the only one who rules on
frozen criteria. **Do not answer a question that belongs to him.**

---

## Read these first, in this order

1. `specs/SPEC_RUBRIC.md` — **in full.** It is the governing document. F1–F4 are
   FROZEN; S1–S12 are graded on every dispatch.
2. `docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md` — 339 lines.
   **Untracked, ungraded, in no commit.** It is the single most useful artifact
   for this plan and it is easy to miss for exactly that reason.
3. `/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md` — the operator brief,
   16,603 bytes, dated 2026-08-15. **Outside the repo.** Supersedes v2.
4. `DECISION_LOG.md`, rows dated `2026-08-29` — this session's rulings.

---

## F3, stated precisely

> **F3 — Backtest fill resolution vs. acquired data granularity**
> **Criterion.** The fill resolution the Strategy Analyzer will actually run at,
> and the slippage assumption applied at the band edge, stated in writing before
> the backtest runs.
> **Unblocks when.** The assumption is committed and the backtest report carries
> it as a stated limitation.
> **Blocks.** `4uu`. Everything downstream of `4uu`.

### What is settled, and verified at source

The Block 2 spec pins `Order Fill Resolution = High` with a **1-tick resolution
series**. Deviation F delivered **1-minute bars only**. So the spec describes a
run that cannot happen.

**But the intrabar problem is structurally absent from this strategy**, and this
was verified by reading `ninjascript/PraxisNoiseAreaBreakout.cs` directly:

- `:105` — `Calculate = Calculate.OnBarClose;`
- `:196-198` — `isCheckpoint = (Minute == 0 || Minute == 30) …` then
  `if (!isCheckpoint || !haveBand) return;` — a hard gate, and **every order call
  in the file sits below it**
- `:227` / `:229` — `EnterLong` / `EnterShort`, **plain market orders**
- exits `:211` / `:219` also below the gate; `:288` / `:290` are EOD-flat
- grep for `StopMarket` / `SetStopLoss` / `SetProfitTarget` → **zero matches**,
  with `EnterLong` / `EnterShort` matching as the positive control

**There are no resting intrabar orders.** The strategy transacts only at `HH:00`,
`HH:30` and EOD flat. Intrabar path ordering cannot affect its fills.

⚠️ **A previous session got this wrong twice** — asserting the edge "lives at a
band touch" without reading the implementation. The correction is recorded in the
research report's closing section. Do not re-derive the error.

### What is NOT settled

- **NT8's actual behaviour when `High` is set and no tick data exists.** The
  research marks this **UNVERIFIED**: does it silently coarsen, warn, or demand a
  secondary series? Nobody has watched it.
- **The slippage number.** Called `[N]` throughout the ledger. **Amear's, and
  only Amear's.** He has not supplied it. Do not pick it, and do not offer a menu
  of candidate magnitudes — anchoring is picking it by another route.

---

## The two candidate paths — the plan should choose between them or better them

**Path A — conditional commitment (Amear's standing ruling, `DECISION_LOG`
`2026-08-29T00:10:00Z`):**

> We accept Standard resolution on 1-minute bars. Band-edge slippage widened to
> `[N]`. Fills are optimistic and the report states so. If the VM measurement
> shows NT8 errors or demands a secondary series rather than falling back
> silently, this row is void and the assumption is re-decided cold.

**Path B — the R3 control experiment** (proposed by the research report's
addendum, not yet ruled on): run the backtest **twice, identical in every
respect, `Standard` vs `High`**. Under checkpoint-only evaluation the two runs
should produce identical trade lists. This is rubric ruling R3 in its prescribed
form — *toggle the mechanism, hold everything else constant.* If they agree, fill
resolution is **proven** inert rather than argued inert, and F3 collapses to a
single written slippage assumption. Same single VM trip.

**Path B looks strictly better** — A still commits a prediction, merely hedged.
But **the `00:10:00Z` ruling is Amear's and only he amends it.** Surface the
comparison; do not switch paths unilaterally.

---

## Also open, and it is not obviously downstream

`Praxis_build-1gd` (**P1, OPEN**) — *"b2-data §4.5 acceptance gate is
unreachable: `b2_stitch.py` emits `FLAG` where spec requires `FAIL`."* Filed out
of session 51. Its measurement report is at
`docs/reports/2026-08-15-session51-b2-gap-fraction-measurement.md` (27,750 bytes,
**untracked, unaudited, unread**).

A peer channel argued this must be ruled before F3 proceeds, on the grounds that
"the same gate machinery would grade F3's artifact." **The dependency graph does
not support that**: `1gd` and `4uu` are siblings, both feeding `zi1`, and
`b2_stitch.py` validates the stitched CSV — it does not grade a written slippage
assumption. Include `1gd` in the plan as its own item, not as an F3 blocker.

---

## Hard constraints on the plan

1. **F3 is FROZEN.** Do not plan work that assumes it is cleared. Name the
   unblocking artifact explicitly wherever it matters.
2. **`[N]` is unfilled.** Any plan step that needs it must halt and say so.
3. **No commits.** Only Amear commits.
4. **Evidence discipline.** This project has been wrong twice on well-cited
   static reads — a misread nesting default and a stale binary. Both had
   impeccable form. Mark anything unobserved as **UNVERIFIED** rather than
   asserting it.
5. **The VM is human-only.** No subagent can reach NinjaTrader.
6. **One session per working tree.** Do not run a second Claude session against
   this repo; use a `git worktree`.

---

## Environment facts, observed 2026-08-29

- Claude Code **`2.1.251`**. One binary, PATH lists `~/.local/bin` twice. Third
  distinct build in five sessions — **every hook finding on record is
  `UNVERIFIED` on this build.**
- `scripts/master-bash-guard.sh` denies any command containing `>` not followed
  by `&`. **`2>/dev/null` will be blocked.** Use `2>&1` instead.
- `DISPATCH_LOG.md` currently shows **2 SubagentStart rows against 13 stop
  events**, 11 unmatched. Cause unknown, deliberately undiagnosed. Do not rely on
  hook rows to verify worker caps this session without instrumenting first.

---

## What good looks like

A plan that gets **one** trip to the VM to produce: the bar-stamp alignment
verdict, a compile, and whatever fill-resolution evidence the chosen path needs —
without pretending F3 is cleared, and without anyone picking `[N]` except Amear.
