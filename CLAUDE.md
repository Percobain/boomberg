@AGENTS.md

# boomberg — Bloomberg Trading Challenge workspace

Read `strategy/STATUS.md` first, then `strategy/RULES_AND_CHECKLIST.md`.

- Ranking metric is **Relative P&L vs the WLS index** (~61% US, India ~1.7%). Always frame ideas against the benchmark, not absolute returns.
- Hard rules: long-only, ≤ $200k per stock, cash ≥ 0, WLS members only. Run `python scripts/wls.py` before suggesting any ticker; use the exact Bloomberg ticker.
- `data/raw/` is read-only. Regenerate `data/processed/` with `scripts/build_universe.py`.
- Never invent prices, fills or P&L. Mark unknowns as unconfirmed and add them to the journal's open questions.
- When the user pastes team chat: log it in `journal/YYYY-MM-DD.md`, update `research/watchlist.csv`, `portfolio/*.csv`, and `strategy/STATUS.md` as needed.
- Keep the repo private (handbook is not for redistribution).
