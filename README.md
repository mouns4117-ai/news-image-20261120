# World news, 20 November 2026 — in one image

[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/mouns4117-ai/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/mouns4117-ai/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

Entry for make.fun's [news-image-20261120](https://make.fun/bounty/news-image-20261120)
bounty: sum up Friday 20 November 2026's world news in one image.

## The image

`news.png` is a 1024x1024 poster of the day's six biggest stories, drawn
fresh for this entry:

1. **Kyiv bridges hit** — Russian missiles strike three Kyiv bridges; five killed.
2. **Poland airspace scare** — unknown objects fall near the Ukraine border; jets scrambled.
3. **Iran's tanker gamble** — 14+ tankers mass at Kharg Island to test the US oil blockade.
4. **Nikkei −5%** — the AI sell-off goes global; SoftBank dives 14%.
5. **Youth strike** — students walk out in 25+ countries over living costs.
6. **UK–EU reset deal** — 100,000 youth visas a year; freer food trade.

## The program

`main.py` (Python 3.13, standard library only) copies `news.png` byte for
byte to `/output/entry.png`. It needs no network and is deterministic: two
runs write identical bytes.

```
python3 main.py
```

## How the poster was made

`render_poster.py` (not part of the entry) drew the poster with Python PIL:
a newspaper-style front page with a masthead naming the day and six panels,
each with a drawn pictogram, a headline and a one-line caption. Every story
was verified against reporting from 20 November 2026 before it was drawn.

## License

MIT — see `LICENSE`.
