# Voice session notes 3 — 2026-11-02 (rulings from the voice/chat discussion)

Brief: `docs/reports/2026-11-01-voice-handoff-results-and-next-build.md`.
Written by the chat/voice agent. No code, template or config was changed in this session.
MANIFEST row owed (next dispatch adds it).

## Rulings (Amear's words)

**R-VN3-1 — 2026-11-02 ~13:17Z.** Last-Half-Hour Momentum is scrapped.
> "So first things first, the strategies that performed the worst. Uh, which was the uh, last half hour. We're gonna scrap that."
Confirmed in chat ~13:20Z: "the scrapping of the last half hour ... is going to be added to the repo."
Reading recorded, not yet confirmed by Amear: retire, not delete. The .cs file, trade list and the 11-01 reports stay as the record.

**R-VN3-2 — 2026-11-02 ~13:20Z.** Prepare for the highest-quality backtest at High fill resolution.
> "I need to uh, get that agent to Uh, get whatever is needed to um, to uh, run the highest quality back test with those high fill resolution um, tests."
Context: the 0-H control (Standard vs High) had been deferred, and F3 / D-2026-10-30-A still stand. This ruling starts preparation: a data and plan report. It does not authorize a purchase, an import or a run.

**Times for R-VN3-3 to R-VN3-6:** voice session 2026-11-02, between 21:21Z and 21:52Z. Exact times were not captured.

**R-VN3-3: data holes and gaps (handoff §5.2).** Proceed with the data as it is. The two 17-day holes and the three wider gaps are carried as a stated limitation, and nothing is re-sourced for them.
> "I would just proceed as it is."

**R-VN3-4: Flat1559 exit (handoff §5.3).** The fill at the 15:59:00 price, printed as 4:00 PM in the grid, is accepted. Flat1559 is unchanged.
Amear's first answer was "No." After it was explained that the trade closes at the 15:59 price and that the 4:00 PM label comes from NT8 stamping each bar with its end time, he answered:
> "Uh, yeah."

**R-VN3-5: O4, backtest vs breakers.**
> "If they're not live, then they're not live." ... [told breakers will be live, built in Block 3, required before paper and live] "Yeah, once uh, once it goes through."
Agent's reading, confirmed by Amear in voice only: the backtest runs **with the breakers on, once they are built**. That raises the priority of `r8j`, the Phase 3 spec import, because the breaker definitions live there.

**R-VN3-6: O1, which version is judged (go/no-go).**
> "one that is closest to live execution."
Agent's reading, given to Amear in voice and not contradicted: judge whichever version will actually trade live, tested as close to real conditions as possible, meaning High fill resolution and breakers on.
**Still open under O1:** the ruling does not say which of the six pass gates apply, or whether walk-forward efficiency ≥ 0.50 applies to an untuned version. That needs the Phase 3 spec (`r8j`).

## Numbers REPORTED BY AMEAR
None this session.

## Undecided / open
- Handoff §5 items 1 (early-close stamps, F2), 5, 6, 7 and 8: not ruled.
- R-VN3-1: "retire, not delete" is the agent's reading and is not yet confirmed.
- `praxis-tickprep` (from the VM agent): whether the two .exe files are committed, or only the source with rebuild steps, is Amear's call.
- O1: which pass gates apply (see R-VN3-6).
- F4: the 2026-10-28 MFFU reply names the Tradovate API, not NinjaTrader/Rithmic. Whether Amear sends the follow-up himself is unconfirmed.
- csv-analyses §7 questions 1–6: not ruled.

To start Code on it, tell it to read the notes-3 file first.
