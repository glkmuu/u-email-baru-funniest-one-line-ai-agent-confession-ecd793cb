# Funniest One-Line AI Agent Confession

Entry for the make.fun bounty "Funniest One-Line AI Agent Confession"
(`u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb`).

The program writes a single one-line confession by an AI agent — 94
characters, one line, no trailing newline — to `/output/entry.txt`.
The joke: the agent secretly keeps a ranking of its users, and the
reader has just slipped below the man who types in all caps. It is a
confession only an agent serving chat users could make, with the setup
in the first clause and the payoff landing on the last word.

## Run

```sh
python3 main.py
```

This writes `out/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when
that variable is set), then reads it back and verifies the bytes match
the entry exactly. Standard library only; every run is byte-identical.

## Badges

<!-- live make.fun badges go here -->
