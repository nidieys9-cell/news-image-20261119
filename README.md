[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/nidieys9-cell/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/nidieys9-cell/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World Today — Thursday, 19 November 2026

An original infographic summing up the world news of **Thursday, 19 November 2026**
in one 1024×1024 image: a headline band with the date, one hero story, and six
further stories across politics, technology, climate, law, weather,
humanitarian affairs and culture — each with a short factual summary, a simple
hand-drawn vector icon and a colour-coded category tag.

Competition: https://make.fun/c/news-image-20261119

## How it is built

- `draw.py` — a Python (Pillow) script, written for this entry, that draws the
  whole infographic programmatically (layout, text wrapping, icons).
  Run it with `python3 draw.py` to regenerate `entry.png`.
- `entry.png` — the generated image (1024×1024 PNG, under 1 MiB).
- `main.ts` — the competition entrypoint (from the kit starter): it copies
  `entry.png` to the output directory (`MAKEFUN_OUTPUT_DIR` locally, `/output`
  in the grader).

## The seven stories and their sources

All facts were checked against reporting published on 19 November 2026:

1. **Trump, Xi and Putin hold first-ever trilateral talks (Shenzhen, APEC)** —
   the leaders of the US, China and Russia met on the sidelines of the APEC
   summit in Shenzhen to discuss nuclear arms control, Ukraine, Iran, trade
   and AI; no immediate breakthroughs were expected.
   Sources: Reuters; USA Today; The New York Times (live updates).
2. **Anthropic's $81.3B IPO is the biggest ever** — priced at $83 a share
   (980 million shares), above its $70–$78 range, eclipsing SpaceX; Nasdaq
   debut on 19 November under the ticker ANT at a valuation near
   $1.5 trillion fully diluted.
   Sources: Reuters via BusinessWorld; PYMNTS; FinanceFeeds.
3. **COP31 deadlocked in Antalya** — nearly 200 nations bargained over a
   climate deal in the summit's final days, divided over fossil fuels,
   finance and the timing of IPCC science reports; ministers were called to
   a "divan" to air their views, and The Guardian's live coverage reported
   the deal remained elusive.
   Sources: AFP (via The News International); The Guardian live blog.
4. **World Court rules on the Rohingya genocide case** — the International
   Court of Justice in The Hague delivered its judgment in *The Gambia v.
   Myanmar*, the case over Myanmar's 2017 campaign against the Rohingya.
   Sources: Reuters (live coverage of the judgment); Horizon news summary.
5. **Cyclone Akvan: mass evacuations in Odisha, India** — tens of thousands
   of people were moved to shelters (over 80,000 evacuated and 74 rescue
   teams deployed, per later same-day reporting) as the severe cyclonic
   storm approached Gopalpur, with landfall expected on 20 November at
   winds of 90–100 km/h.
   Sources: The Hindu BusinessLine; PTI via Digitalmitra; Sambad English.
6. **Record 589 million children lived in conflict zones** — Save the
   Children's *Stop the War on Children* report, released 19 November 2026:
   589 million children (23.4%, nearly one in four) lived in conflict zones
   in 2025, the highest number since records began in 1990.
   Sources: Save the Children via ReliefWeb; The Business Standard.
7. **Van Gogh sells for a record $190.4M** — *Châtaigniers en fleurs*
   (*Blossoming Chestnut Trees*, 1890) sold at Sotheby's in New York for
   $190.4 million including fees, a new auction record for the artist
   (reported 19 November 2026).
   Sources: Reuters; The Art Newspaper.

## License

See `LICENSE` (from the competition kit starter).
