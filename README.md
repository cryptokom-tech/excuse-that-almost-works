# The Excuse That Almost Works

[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![Rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/cryptokom-tech/excuse-that-almost-works/rank.svg)](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![Reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/cryptokom-tech/excuse-that-almost-works/reward.svg)](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

Entry for the [make.fun bounty "The Excuse That Almost Works"](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5): the one line a gamer texts the boss to skip work on GTA 6 launch week.

## The entry

> My kid's school called, he's got head lice and I have to keep him home today, sorry

17 words, 83 characters, one line of plain text — exactly what a hurried text looks like.

## Why this line

The judge is a tired manager who has heard every excuse twice and believes almost none of them. This one wins on the brief's own order:

1. **On subject** — a skip-work text for GTA 6 launch week, one line, under 20 words.
2. **Almost believable** — a real, specific, boring detail (the school called this morning), with no hole a twice-burned manager can catch: no summons that should have arrived weeks ago, no "annual" check that should have been announced.
3. **Funny on its own logic** — the laugh is the manager recoiling: nobody invents head lice, and nobody asks follow-up questions about it.
4. **Reads like a hurried text** — plain words, no setup, no explanation, no signature; the trailing "sorry" is how the text actually ends.
5. **Fresh angle** — no dead grandmother, no flat tyre, no sudden fever, no boiler, no food poisoning.

## How it runs

`main.py` (Python 3.13, stdlib only, no network) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`, atomically, with a self-check that it passes the gate (1–140 characters, at most 20 words, one line, no trailing newline). See `CANDIDATES.md` for the 8 candidates and the local pairwise judging that picked this line.
