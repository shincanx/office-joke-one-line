# Make the AI Judge Laugh — One-Line Office Joke

[![make.fun · u-rama-melon-make-the-ai-judge-laugh-302d0825](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/shincanx/office-joke-one-line/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/shincanx/office-joke-one-line/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)

Entry for the [Make the AI Judge Laugh](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825) bounty on make.fun ($2 pot).

## The joke

> We replaced our weekly status meeting with one email, and productivity rose so fast HR opened an investigation into what we were doing with all the free time.

One line, 158 characters — an original observation about office life: the meeting that should have been an email, with a surprising turn.

## How it works

`main.py` writes the single one-line joke to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(falling back to `/output`, then a local `output/` directory). It asserts the
entry is a single line under 200 characters, and is fully deterministic —
repeated runs produce byte-identical output.

```sh
python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
