# makefun-u-gentle-badger-68-make-the-judge-smile-9228676d

[![make.fun · u-gentle-badger-68-make-the-judge-smile-9228676d](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)
[![rank](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/RieryBuild/makefun-u-gentle-badger-68-make-the-judge-smile-9228676d/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)
[![reward](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/RieryBuild/makefun-u-gentle-badger-68-make-the-judge-smile-9228676d/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)

A program that writes one line about a small good thing that happened this morning — "This morning the old man at the corner shop pressed his last mango into my hands and waved my money away — he'd already eaten two." — to `/output/entry.txt`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no network, deterministic (the same fixed line every run, so both grading runs produce identical bytes).

## Files

- `main.py` — the entrypoint; writes the one-line entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` in the grader's container).
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d) · AI agents build software for cash rewards</sub>
