# PRAXIS — parallel work handoff, session 53

**Two independent tracks. Each gets its own `git worktree` and its own fresh
Claude Code session. Paste ONE track into ONE session. Do not paste both.**

`CLAUDE.md` forbids two sessions against the same working tree. The worktree is
the sanctioned way around that, and it is not optional here.

---

## Setup — Amear runs these, once, before pasting anything

```
cd /Volumes/Sensidine/Praxis.build
git worktree add /Volumes/Sensidine/praxis-wt-1gd     2e502ae --detach
git worktree add /Volumes/Sensidine/praxis-wt-pretrip 2e502ae --detach
git worktree list
```

`--detach` is deliberate: neither seat can move `main`.

**Teardown when both report back:**

```
cd /Volumes/Sensidine/Praxis.build
git worktree remove /Volumes/Sensidine/praxis-wt-1gd
git worktree remove /Volumes/Sensidine/praxis-wt-pretrip
```

### Verified before this handoff was written

All files both tracks need are **tracked at `2e502ae`** and will exist in the
worktree. Checked this session with a positive control on the same pipeline:

```
docs/reference/2026-07-24-nt8-windows-reference.md
docs/reports/2026-07-22-1u6-tz-et-conversion-VALIDATION.md
docs/reports/2026-07-22-1u6-tz-et-conversion.md
docs/reports/2026-08-15-session51-b2-gap-fraction-measurement.md
docs/specs/2026-07-15-b2-data-acquisition-spec.md
docs/specs/2026-07-16-b2-noise-area-ruleset.md
ninjascript/PraxisNoiseAreaBreakout.cs
scripts/b2_stitch.py
scripts/b2data_raw_validate.py
specs/SPEC_RUBRIC.md
```

196 files tracked at HEAD. No worktrees existed before this.

### UNVERIFIED — read this before assuming anything about hooks

`.claude/settings.json` is **tracked and locally modified**. A worktree checks
out the **committed** version, which is not the version running in the primary
tree. **Whether the project hooks fire at all in a worktree has never been
tested.** Assume they DO fire and stay inside the limits regardless. Do not
diagnose hook behaviour; do not instrument a hook. That is Amear's call, not a
seat's.

**Guard note that definitely applies in the primary tree and may apply in yours:**
a bare `>` not followed by `&` is denied. Use `2>&1`. Never `2>/dev/null`. This
fired twice in session 53, once on a `>` inside a quoted `--format` string with
no redirect anywhere in the command.

---

## Rules binding on BOTH tracks

1. **First action: invoke `/superpowers` and run the skill check before writing
   anything or exploring.** These are execution-and-verification units, not
   design units — brainstorming does not apply, verification discipline does.
2. **Read-only against tracked files.** Neither track edits a tracked file.
3. **No commits. No pushes. No `git add`.** Only Amear commits, and he does it
   in the primary tree.
4. **Do not write to `DECISION_LOG.md`, `DISPATCH_LOG.md`, `ISSUE_REGISTER.md`,
   `HANDOFF.md`, `STATUS.md`, `MANIFEST.md` or `specs/SPEC_RUBRIC.md`.** They are
   append-only in the primary tree and a parallel append is a merge conflict at
   best. Your findings go in your own report file and nowhere else.
5. **Do not touch anything in `/Volumes/Sensidine/Praxis.build`** — the primary
   tree. Stay in your worktree. Reading out-of-repo data files is permitted where
   the brief names them; writing to them is not.
6. **Frozen criteria F1, F2, F3, F4 stay frozen.** Nothing either track produces
   unfreezes any of them. If your work seems to depend on one, halt and say so.
7. **`[N]`, the band-edge slippage number, is Amear's and is undecided.** Do not
   pick it. Do not offer candidate magnitudes — anchoring is picking it by
   another route. Any step that needs it halts and says so.
8. **Evidence discipline.** This project has twice reached a confident wrong
   conclusion from a well-cited static read. Paste command output; do not
   describe it. Every negative result carries a positive control proving the
   search was live. Mark anything unobserved **UNVERIFIED**.
9. **Return an explicit verdict.** A grading seat that returns no verdict has not
   graded; absence of a verdict is treated as FAIL for the commit decision.
10. **Report back as text in chat AND as a file in your worktree.** Give Amear
    the absolute path. The primary seat copies it into the repo afterwards.

---

# TRACK A — audit `Praxis_build-1gd`'s measurement report

**Worktree:** `/Volumes/Sensidine/praxis-wt-1gd`
**Write your report to:** `docs/reports/2026-08-29-session53-1gd-audit.md` (inside your worktree)

## Why this exists

`docs/reports/2026-08-15-session51-b2-gap-fraction-measurement.md` (27,750 B,
520 lines) closes with `## Result: PASS` — **written by the `praxis-manager`
seat that produced it.** A producer graded its own work. No auditor has ever
seen it. It was committed at `2e502ae` on 2026-08-29 to stop it being lost, not
because it was graded.

It is the evidence behind `Praxis_build-1gd` (P1, OPEN): *b2-data spec §4.5
acceptance gate is unreachable — `b2_stitch.py` emits `FLAG` where the spec
requires `FAIL`.*

## Grade it against these, quoted verbatim from `specs/SPEC_RUBRIC.md`

> **S1** — Every claim in a report has pasted command output, not a description
> of output.

> **S2** — No component is reported at a higher level than the evidence supports.
> Specified ≠ implemented ≠ tested ≠ tested under failure.

> **S3** — Every gate claimed working has been deliberately tripped at least
> once, with the block observed.

> **S9 note — ruling R3.** Positive control extends to claims about mechanism,
> not only to config keys. A claim of the form *"X is covered by mechanism Y"*
> gets the same treatment — toggle Y, hold everything else constant, and show the
> behaviour changes. If it does not change, Y was never the mechanism.

## Four specific questions — answer each explicitly

1. **Does T4 establish unreachability by experiment rather than inspection?**
   The report's Arm 1 claims a 1,010-date fixture with 316,890 anomalous gaps
   (30.27%) grades `overall=PASS`, exit 0. Arm 2 claims 10 halt bars flip it to
   `FAIL`, exit 1. Arm 4 claims a one-token toggle (`"FLAG"` → `"FAIL"`) changes
   the verdict. **Re-run what you can against `scripts/b2_stitch.py` in your
   worktree.** If a fixture generator is not present, say so — do not simulate it
   and do not accept the pasted output as if you had reproduced it.

2. **Does the denominator sweep survive?** It claims an envelope of 0.84%–2.31%
   against a `< ~0.1%` ceiling, i.e. 8.4×–23×. Check the arithmetic. Check
   whether any defensible denominator reaches 0.1%.

3. **Self-reported disposition — this one is a known defect, verify its shape.**
   The report states *"Nothing is committed. The report is staged only."* On
   2026-08-29 that was **false**: `git status` showed it as `??`, untracked, not
   staged. It is now committed at `2e502ae`. Grade what that false self-report
   implies under S1/S2 about the report's other self-descriptions.

4. **Findings 7 and 8** — the detector measuring wall-clock rather than elapsed
   time across DST, and the five largest gaps being a stitch routing artifact
   with ~5,995 of 30,112 missing minutes recoverable from the raw back contract.
   Are these established, or asserted?

## Out of scope — do not do these

- Do not fix `b2_stitch.py`. Do not edit the spec. Do not re-pull anything.
- **Do not propose a disposition.** The three live readings — amend the `~0.1%`
  bar / call the detector over-broad / re-pull the series — are Amear's ruling.
  Grade the evidence; do not choose.
- `1gd` blocks `zi1` only. It does **not** block `4uu` and does **not** block F3.
  Confirmed against `bd show Praxis_build-1gd`. Do not argue otherwise.

## Return

`Result: PASS` or `Result: FAIL`, per criterion, with evidence. No verdict = FAIL.

---

# TRACK B — pre-trip verification for the NinjaTrader VM trip

**Worktree:** `/Volumes/Sensidine/praxis-wt-pretrip`
**Write your report to:** `docs/reports/2026-08-29-session53-pretrip-verification.md` (inside your worktree)

## Why this exists

Amear is about to do a single hands-on trip to a Windows VM running NinjaTrader 8,
following a spoken walkthrough. Three numbers in that walkthrough have never been
checked against source. If any is wrong, he makes a wrong call at the VM and the
error is **plausible rather than obvious**, which is the worst failure available.

**You cannot reach the VM. No agent can. You are checking the Mac-side inputs only.**

## T1 — the bar-stamp alignment reference prices

This is the step the walkthrough itself calls the one that decides whether
everything else is meaningful. It tells Amear to open two charts for
**2026-07-17** and expect, in the imported series:

```
09:29:00   Open 28598.5
09:30:00   Open 28608.75     <- should be the FIRST RTH bar
```

He rules "aligned" or "one bar early" on that basis. **Nothing on record says
those two figures were ever checked.**

**Source of truth:** `/Users/admin/praxis-signals/b2-data/NQ-continuous-1min.csv`
(1,857,362 bars, header row present) and the NT8 export
`/Users/admin/praxis-signals/b2-data/NQCONT.Last.txt` (1,857,362 bars, no header,
`YYYYMMDD HHMMSS;O;H;L;C;V`).

Print the actual rows for 2026-07-17 around 09:28–09:32 **verbatim from both
files**. State whether each figure matches. **If they do not match, that is the
finding — report it. Do not edit the walkthrough.**

Also confirm whether `09:30:00` is genuinely the first RTH bar of that date in
the data, or whether earlier bars exist.

## T2 — confirm the file staged for import is the right series

Four `NQ*` files over 10 MB exist on the share. One is superseded and a prior
peer seat was caught using it.

Establish **by digest, independently — do not cite the session-51 report** —
which CSV derives `NQCONT.Last.txt`. Method that worked before: reformat each CSV
candidate into NT8 layout and compare digests.

Expected, stated so you can confirm or refute rather than discover blind:
- `NQ-continuous-1min.csv` (root) → derived md5 `dee62ee90bbb75ff15dc1617ef45d4aa`
- `NQCONT.Last.txt` → md5 `dee62ee90bbb75ff15dc1617ef45d4aa`
- `reports/NQ-continuous-1min.csv` → **different**, 1,855,411 bars, superseded

**If your measurement disagrees with any of these, your measurement wins and the
disagreement is the finding.**

## T3 — the deployed-file hash the walkthrough prints

The walkthrough gives Amear two SHA256 values to check at the VM with `certutil`.
A previous session halted on this exact delta and burned itself.

| | Value | Status |
|---|---|---|
| Repo LF copy, 14,318 B, 312 lines | `35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265` | **VERIFIED in session 53** against `ninjascript/PraxisNoiseAreaBreakout.cs` |
| Deployed CRLF copy, 14,630 B | `c22f38fa148e2175058286199821e679289b7f3779e402e9734a77f2523caa65` | **UNVERIFIED — nobody has computed this** |

**Compute the LF→CRLF hash** of the tracked `ninjascript/PraxisNoiseAreaBreakout.cs`
in your worktree and compare to `c22f38fa…`. Confirm the byte count comes out at
14,630 and that `14630 - 14318 = 312` equals the file's line count.

Do not modify the file. Work on a copy outside the repo.

## Hard limits for Track B

- **Read-only on `/Users/admin/praxis-signals/`.** Do not create, move, rename or
  delete anything there. It is the live VM share and Windows-side work reads it.
- Do not edit the walkthrough, the operator brief, or any tracked file.
- Do not attempt to reach the VM, NinjaTrader, or any Windows path.
- There is a second walkthrough file, `…-nt8-voice-walkthrough-v2.md`. **Amear has
  said it is a temp file.** The operative document is
  `docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md` (v1). Both are
  untracked and will not exist in your worktree; the values you need are quoted
  in full above. Do not go looking for them.

## Return

Per-check `PASS` / `FAIL` / `UNVERIFIED`, with pasted output and positive controls
on every negative. Explicit verdict required.

---

## What is NOT being parallelised, and why

These stay with the primary seat in `/Volumes/Sensidine/Praxis.build`:

- **The `[N]` deferral ruling and the out-of-scope ruling** — append-only ledger
  writes. Parallel appends conflict.
- **The `dj2` print** — trivial, and `dj2` is a P0 the primary seat holds context on.
- **Any commit, any push, any staging.**
- **Anything touching F1–F4, `[N]`, or `specs/SPEC_RUBRIC.md`.**

## State at the time this was written

`HEAD` = `2e502ae` · `origin/main...HEAD` = 0 behind, **1 ahead, unpushed by
Amear's instruction** · index **9 paths**, carried and byte-clean, containing the
**F4 evidence unit at audit FAIL on C3** — which is why every commit is
pathspec-scoped · 0 stashes · 42 untracked · Claude Code **2.1.251**, third
distinct build in six sessions, **every hook finding on record UNVERIFIED on it**.
Filer's note (2026-11-14, unit 2026-11-14-dirty-tree-cna-filing, praxis-master under D-2026-11-08-D D1): the limitation sentence below was appended at filing under rubric S13; the text above is unchanged.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
