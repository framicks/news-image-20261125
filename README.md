# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/framicks/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/framicks/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Wednesday, 25 November 2026, packed into a single broadsheet page. The front page leads with the US Army's planned detonation of 68 barrels of degraded lead azide at the Iowa Army Ammunition Plant on Wednesday morning — too unstable to move, with residents told to leave and a lead-dust plume that may drift more than 100 miles. The rest of the page carries five more stories from the same day's news cycle: Japan's services inflation jumping to 4.2%, its fastest since 1990; Australia's consumer prices rising to 4.9%, hotter than forecast; Shanghai's party leadership pledging loyalty to Beijing as a graft probe fells Politburo member Chen Jining; Game 2 of the World Chess Championship in Geneva, with defending champion Gukesh holding White and the score level at half a point each; and US GDP and inflation data due later in the day. Six stories, one crowded news day, set out as a classic newspaper front page in `front-page.png`.

## Stories

1. Army to detonate 9,500 lb of unstable explosive in Iowa (25 Nov, 9 a.m. CT)
2. Japan services inflation hits 36-year high at 4.2% (data released 25 Nov)
3. Australia inflation jumps to 4.9%, hotter than forecast (data released 25 Nov)
4. Shanghai pledges loyalty as graft probe fells party chief (probe announced Tue 24 Nov; loyalty pledge Wed 25 Nov)
5. Chess title fight: Game 2 today in Geneva, scores level ½–½ (25 Nov, 3 p.m. CET)
6. US GDP and inflation data due today (25 Nov, 13:30 GMT)

## Run it

```sh
python3 main.py
```

This copies `front-page.png` (a real PNG, 1024×1024, under 1 MiB) to `/output/entry.png`. Set `MAKEFUN_OUTPUT_DIR` to pick a different destination. Running it twice produces byte-identical output, since the image is shipped in the repository and only copied, never redrawn. The script also re-reads the file it wrote and checks its sha256 against the shipped image before reporting success.

## Verification

You can check the output yourself in a minute. Run `python3 main.py` twice with `MAKEFUN_OUTPUT_DIR` pointed at two different folders, then compare the two `entry.png` files with `sha256sum` — both hashes should match each other and the shipped `front-page.png`, since the script only copies the image and never redraws it. The PNG itself should stay 1024×1024 pixels and under 1 MiB, which you can confirm with `file` or `identify`. If either run prints an error instead, the source image is missing, its first eight bytes are not a PNG signature, or its dimensions are not 1024×1024, and the script exits with code 1.

## Sources

Headlines were checked against reporting dated 25 November 2026: Reuters and the Des Moines Register on the Iowa lead-azide detonation set for 9 a.m. Wednesday; Reuters and the Bank of Japan on Japan's services producer prices rising 4.2% in October; the Australian Bureau of Statistics, Reuters and the Wall Street Journal on Australia's October CPI at 4.9%; Reuters on Shanghai's loyalty pledge after the Chen Jining probe (announced Tuesday 24 November by Xinhua); FIDE and World Chess on Game 2 of the Gukesh–Sindarov title match in Geneva; and Reuters on the US GDP and PCE data due at 13:30 GMT. Where an event itself fell on Tuesday 24 November, the story list above says so; nothing is presented as happening on a day it did not.

---

<sub>Entered on [make.fun](https://make.fun/?ref=jjs4n5n8&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
