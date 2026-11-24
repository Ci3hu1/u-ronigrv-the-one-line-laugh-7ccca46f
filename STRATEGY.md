# Strategy — The One-Line Laugh

## The joke

One everyday truth, one surprise turn at the end. The setup is universal
(Wi-Fi down, five minutes of forced offline life); the turn is the last
clause — "it turns out they're nice" — which reframes the family as
people the writer had been avoiding by habit, not by dislike. The laugh
comes from recognition: everyone has used the internet as a reason not
to talk to the people in the next room.

## Why this shape

- **One sentence, 98 characters.** Well inside the 200-character gate,
  economical: every word earns its place, nothing explains the joke.
- **Surprise at the end.** The punchline lands on the final clause, as
  the judge's brief rewards.
- **Everyday truth.** Wi-Fi outages and awkward family small talk are
  both instantly recognisable.
- **Fresh angle.** The joke is about the writer's own avoidance, not a
  generic "internet bad" gag.

## Tried and dropped

- A version ending on "...and I still don't know their names" — sharper
  but meaner, and it contradicts the warm turn the brief rewards.
- A longer setup naming the router brand — extra words, no extra laugh.

## Entry

- `main.py` (pure stdlib) writes the line to `/output/entry.txt`.
- `tests/test_entry.py` checks the 1–200 gate, single-sentence shape,
  and byte-exact output.
