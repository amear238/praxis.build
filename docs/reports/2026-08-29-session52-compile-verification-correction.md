# Part 5 compile — ambiguous status, resolved

**Correction to `2026-08-29-session52-nt8-voice-walkthrough-v2.md` Part 5.
Append-only; the walkthrough is not edited.**

Grades: **VERIFIED** = confirmed against `docs/reference/2026-07-24-nt8-windows-
reference.md`, which was built from 20 screenshots of this exact install.
**INFERRED** = reasoning from verified facts. **UNVERIFIED** = not known.

---

## The headline: NinjaScript Output is not where compile results appear

**VERIFIED — reference §3, "Where compile errors surface":**

> An **error-list panel at the bottom** of the Editor: each row = **filename**,
> **description**, **line/column**. Open-file errors render lighter; other-file
> errors darker. […] Offending code gets a **red wavy underline**. […] Compile
> messages also echo to the Control Center **Log** tab.

**Three places. NinjaScript Output is not one of them.**

**NinjaScript Output is a separate window** — VERIFIED, it is its own entry in the
Control Center `New` menu (§0), listed alongside `NinjaScript Editor`, and its own
button on the Editor toolbar (§1b: *Print · Print Preview · NinjaScript Output ·
Find · Compile · Open in Visual Studio*).

**What it is for:** displaying `Print()` output from *running* scripts. Not build
diagnostics.

**So a blank NinjaScript Output before, during and after a compile is exactly what
should happen.** It is not a symptom. It carries no information about your compile
in either direction. **This was my documentation defect** — Part 5 told you to read
error rows without saying which panel, and you reasonably opened the one with
"NinjaScript" in the name.

---

## Was it the render fault?

**INFERRED: probably not — and there is a direct test, so do not infer.**

The discriminator: `UCEERR_RENDERTHREADFAILURE` is a failure to **paint**. Dialogs
come up blank or don't open. **Your compile spinner painted and animated
correctly**, which is the renderer working normally on that surface.

**But test it rather than reason about it** — re-run the Part 0 check:
**Control Center → `Log` tab → search `UCEERR_RENDERTHREADFAILURE`.** Present or
absent, that is an observation instead of my inference.

---

## F5 not registering — almost certainly not NinjaTrader

**INFERRED, high confidence:** on a Mac keyboard the top row defaults to media
functions. **F5 is being consumed by macOS before Parallels ever sees it**, so
Windows receives no keypress at all. Nothing to do with NT8 or the VM's health.

Fixes, any one of them:

- Hold **`Fn` + `F5`**
- macOS **System Settings → Keyboard → "Use F1, F2, etc. keys as standard function
  keys"**
- Parallels **Devices → Keyboard** profile for function keys
- **Or just keep using the toolbar Compile button — you already did the right
  thing.** VERIFIED (§3): the toolbar Compile button and F5 are equivalent paths.

**Do not read the F5 failure as evidence about the compile.** Unrelated fault.

---

## The important subtlety: a clean compile is silent

**INFERRED, and it changes how to read what you saw.** Reference §3 documents only
where *errors* surface. It describes no success message, no toast, no "build
succeeded" banner.

**So "spinner ran, spinner vanished, nothing appeared anywhere" is the expected
signature of a compile that worked.** Ambiguous to look at, which is precisely why
it needs a positive confirmation rather than an absence of complaint.

---

# What to check, in order

## 1. The error panel at the BOTTOM of the Editor — not the Output window

Look at the bottom edge of the NinjaScript Editor for a list panel with **filename
/ description / line-column** columns. **Empty or absent = no errors reported.**

Also scan the open file for **red wavy underlines**.

## 2. Control Center → `Log` tab

**VERIFIED:** compile messages echo here. Check entries at the timestamp of your
compile. This is the authoritative text record.

## 3. ⭐ The decisive check — the compiled assembly's timestamp

**This is the one that actually settles it, because it is a measurement rather than
a panel reading.**

NT8 compiles all custom NinjaScript into a DLL under:

```
%USERPROFILE%\Documents\NinjaTrader 8\bin\Custom\
```

List that folder with timestamps:

```
dir "%USERPROFILE%\Documents\NinjaTrader 8\bin\Custom\*.dll"
```

- **A `.dll` with a modified time matching your compile, to the minute → the
  compile SUCCEEDED.** A failed compile does not write a new assembly.
- **Timestamp is hours or days old → the compile FAILED**, silently, and the error
  reporting is broken too. That would be a genuine finding.

**UNVERIFIED:** the exact DLL filename (I believe `NinjaTrader.Custom.dll`, but
have not confirmed it against this install). **List the folder and read the names
and times rather than looking for a specific file** — that is robust to me being
wrong.

**Read me the filename and the timestamp.**

## 4. Functional check — with a caveat that matters

Open `New > Strategy Analyzer` and confirm `PraxisNoiseAreaBreakout` appears under
category **"02. Praxis (tunable)"** (VERIFIED §4).

**⚠️ But this proves less than it looks.** Reference §0 records both strategies as
**already installed and confirmed live on 2026-07-24**. So presence in that list
may be left over from an earlier successful compile and says nothing about
*today's*. **Check 3 is the one that isolates today's run.**

---

# Optional — a real positive control for the error channel

**Your call; it creates and deletes one throwaway file.**

Everything above tests whether the compile *succeeded*. None of it tests whether
**this install can still report a failure**. If the error channel is broken, a
clean-looking compile is uninformative no matter what the DLL says.

The standing rule here is S3 — *every gate claimed working has been deliberately
tripped at least once, with the block observed.*

1. Editor → NinjaScript Wizard → create a **new throwaway indicator**, any name.
2. Type deliberate garbage into it — a line like `int x = ;`
3. Compile.
4. **The bottom error panel should populate**, and the Log tab should carry it.
5. Delete the throwaway file, recompile, confirm clean.

**If a deliberate syntax error produces no visible error anywhere — that is a
finding**, and it means every compile on this machine has been unverifiable.

**This does not touch `PraxisNoiseAreaBreakout.cs`.** The hard rule against
modifying `.cs` files is about the strategy; this creates a separate scratch file.
But it does write into your NT8 folder, so it is your decision, not mine.

---

## Report back

1. Error panel at the Editor's bottom — populated or empty?
2. Log tab — compile entries at that timestamp? Any `UCEERR_RENDERTHREADFAILURE`?
3. **`bin\Custom\` DLL filename and modified time.** ← the one that decides it
4. Whether you ran the negative control, and what it showed.

Until item 3 comes back, **Part 5 is `NOT-RUN`, not `PASS`.** An absence of error
messages from a panel that never shows error messages is not evidence of anything.
