# Adversarial check — MFFU "Davi" reply transcript vs screenshot

## Task
Find discrepancies between `docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md` and the image `docs/reports/evidence/2026-10-28-mffu-davi-reply.png`.

## Mode
ADVERSARIAL. Read-only on the repo apart from this report. The evidence png was not modified. All crops were made from a scratch copy.

## Criterion
Every visible line is present, in order, with exact spelling, capitalization, punctuation, spacing and typos (nothing corrected, added or omitted). Nothing that is not visible in the image may be asserted as fact.

## Process log

Scratch dir: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/e2d12a7c-ea8d-4471-9c36-a46d92b1a310/scratchpad/adv/`

1. `cp <evidence png> $D/src.png`. sha256 of the copy is `15af5410…2992`, which matches the transcript's claim. Size is 2866x930.
2. Grid of 30 strips: `sips -c 100 1000 --cropOffset $y $x src.png --out s_${y}_${x}.png` for y ∈ {1,90,180,270,360,450,540,630,720,810} and x ∈ {1,950,1866}.
   - Pitfall: my first pass used offset `0`. sips silently ignores an offset of 0 and falls back to a centre crop, so the `x=0` tiles showed the wrong region. Every tile was redone with offset 1.
3. Extra full-column crops: `sips -c 930 1000 --cropOffset 1 1866` (right column) and `sips -c 300 1000 --cropOffset 630 950` (bottom middle).
4. Zoom crops, each upscaled with `sips -Z`:

   | Target | Crop (h w) | Offset (y x) |
   |---|---|---|
   | email | 30 470 | 135 420 |
   | preview part 1 | 34 600 | 40 125 |
   | preview part 2 | 34 560 | 40 720 |
   | preview end | 34 300 | 40 1170 |
   | Hello | 34 300 | 200 125 |
   | Hi ! | 34 300 | 325 125 |
   | I'll | 34 360 | 265 560 |
   | URL part 1 | 34 460 | 593 1095 |
   | URL part 2 | 34 460 | 593 1540 |
   | URL digits | 34 200 | 593 1450 |
   | Davi avatar | 70 120 | 128 45 |
   | signature | 34 330 | 685 125 |
   | to me | 30 120 | 166 125 |

5. Pixel sampling: 4x4 crops, converted with `sips -s format bmp`, averaged with a small stdlib Python script run under `python3 -I`.
6. Mechanical checks: grep and xxd on the transcript, listed under Verification evidence.

## Line-by-line results (fenced transcript lines 15–39)

| T-line | Image text (read from crops) | Result |
|---|---|---|
| 15 | `amear Bani-Ahmad` (bold, lowercase a) | MATCH |
| 16 | `Hi Frank — thanks for confirming, that's helpful. Two follow-ups so I can be sure I'm building within the rules rather than assuming. 1. Does this specific is f` (no ellipsis, nothing after `f`) | MATCH |
| 17 | blank: divider and gap | MATCH |
| 18 | `Davi from MyFundedFutures <eda.daniel.david@myfundedfutures.intercom-mail.com>`. Checked every character on the 4x zoom. | MATCH |
| 19 | `to me` followed by a filled down-triangle | MATCH |
| 20 | blank (see Observation B) | MATCH (structural) |
| 21 | `Hello amear,i hope this mail meets you well.` | MATCH |
| 23 | `Thank you for contacting MyFundedFutures Support! I'll be happy to assist you today.` | MATCH |
| 25 | `Hi ! Thank you so much for reaching out to MyFundedFutures Support. My name is Michael and I am here to help you with any support you may need today.` (space before `!` confirmed on zoom) | MATCH |
| 27 | `You can use custom Tradovate API access with your MyFundedFutures Tradovate evaluation and funded accounts for fully automated order execution.` | MATCH |
| 28 | `• Automated trading solutions using an API are supported, allowing you to integrate your trading bot or automated strategy via the Tradovate API. This enables your custom software to submit orders, manage positions, and retrieve market data directly from your account.` (spans all three column tiles) | MATCH |
| 29 | `• Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.` | MATCH |
| 30 | `• High-frequency trading is not allowed, and automated tools must not exploit favorable fills in the simulated environment.` (spelled `favorable`, US) | MATCH |
| 31 | `• For live accounts, automated trading must comply with CME guidelines.` | MATCH |
| 33 | `You are responsible for the performance and reliability of your automated system. For more details, see: https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices`. Article number `8444599` confirmed on the digit zoom. | MATCH |
| 35 | `Best regards,` | MATCH |
| 36 | `Davi-MyFundedFutures Support` (hyphen with no spaces) | MATCH |
| 38 | `Davi` (bold) | MATCH |
| 39 | `MyFundedFutures` | MATCH |
| — | Below line 39, and the whole right column (x 1866–2866): no further text. The header row has no timestamp or icons. | MATCH (no omission) |

Blank lines 22, 24, 26, 32, 34 and 37 match the paragraph gaps in the image.

## Prose outside the fence

- Metadata at lines 3–5: verified. The Desktop source is 254350 bytes. Its sha256 is `15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992`, identical to the copy. The filename bytes before `PM` are `e2 80 af`.
- Glyph notes at lines 44–52 (em dash, hyphens, straight apostrophes, `amear,i`, `Hi !`, the bold elements, the blue underlined URL): all consistent with the zooms. The em-dash bytes in the file are `e2 80 94`.
- Line 56 (round avatar with a coloured illustration): MATCH.
- **Line 57: DISCREPANCY 1.**
  - Transcript says: "a grey generic-person avatar".
  - Image shows: a pale grey circle (sampled RGB ≈ 245,245,245) holding a **green** person silhouette (head and body both sample at RGB 137,211,178).
  - The person figure is visibly green, not grey. The description misstates a visible element.
  - Severity: low. It is a non-text element and outside the fence.
- Line 58 (dropdown ▾): MATCH. Line 59 (divider): MATCH.
- Line 60 (light vertical strip): MATCH. Sampled RGB is 248,250,253 against a white body of 255,255,255.
- **Line 12: DISCREPANCY 2 (assertion beyond the image).**
  - Transcript says: "it ends mid-word at `is f`".
  - Image shows: only that the visible text stops at `f` and is followed by whitespace.
  - Whether the next hidden character is a letter cannot be seen in the image, so "mid-word" is an inference stated as fact. It is a highly plausible one, since `f` alone is not a word. The claims "truncated" and "no ellipsis" are fine: no ellipsis is visible.
  - Severity: low.
- "Not visible" list at lines 64–71: no claims beyond the image found. The "Frank" item is framed as an example of something not visible.

### Observation B (not counted)
The gap between `to me` and `Hello` is about 41 px. That is smaller than the body's paragraph gaps (about 60 px) and slightly larger than the intro-to-bullet spacing (about 37 px), which gets no blank line. Rendering it as a blank line is a reasonable header/body separation. I record it but do not count it as a discrepancy.

## Verification evidence (pasted output)

```
$ grep -n 'amear,i' / 'Hi !' / '8444599-…' / email / 'favorable\|favourable' / 'Davi-MyFundedFutures Support' / 'is f$'
21:Hello amear,i hope this mail meets you well.
47:- `Hello amear,i` has no space after the comma and a lowercase `a` and `i`, exactly as shown.
25:Hi ! Thank you so much for reaching out to MyFundedFutures Support. My name is Michael and I am here to help you with any support you may need today.
48:- `Hi !` has a space before `!`, exactly as shown.
33:You are responsible for the performance and reliability of your automated system. For more details, see: https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices
18:Davi from MyFundedFutures <eda.daniel.david@myfundedfutures.intercom-mail.com>
30:• High-frequency trading is not allowed, and automated tools must not exploit favorable fills in the simulated environment.
36:Davi-MyFundedFutures Support
16:Hi Frank — thanks for confirming, that's helpful. Two follow-ups so I can be sure I'm building within the rules rather than assuming. 1. Does this specific is f
--- non-ASCII bytes in fence (lines 15-39):
2:Hi Frank — thanks for confirming, that's helpful. Two follow-ups so I can be s
14:• Automated trading solutions using an API are supported, allowing you to int
15:• Algo trading is permitted on all plans, including evaluation, simulated-fun
16:• High-frequency trading is not allowed, and automated tools must not exploit
17:• For live accounts, automated trading must comply with CME guidelines.
--- trailing spaces / double spaces in fence:
none
--- em dash bytes:
00000000: 4672 616e 6b20 e280 9420 7468 616e 6b73  Frank ... thanks
--- pixel samples:
head(y=155,x=78) avg RGB= [137, 211, 178]
body(y=172,x=78) avg RGB= [137, 211, 178]
circle_inside_y158x66 avg RGB= [245, 245, 245]
leftstrip avg RGB= [248, 250, 253]
bodybg avg RGB= [255, 255, 255]
--- source file:
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
00000020: e280 af50 4d2e 706e 670a                 ...PM.png.
```

## Files staged
None. This report file is unstaged, as instructed.

## Result
The fenced verbatim transcription is clean: all 19 text lines match, in order, with no omissions or additions. The two discrepancies are both in the surrounding prose and both low severity.

VERDICT: DISCREPANCIES FOUND (2)
