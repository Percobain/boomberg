# Where we stand — updated 2026-10-22

**Team:** berg bloom (K J Somaiya) — *assumed ours, confirm*
**Latest leaderboard seen:** Global rank **1373**, Rel P&L **−$1,926**, Abs P&L **−$2,444**.
Same-college rival Titanium Bros: rank 1903, Rel −$10,004.
**Trading days left:** ~17 (last day Fri 13 Nov).

## Holdings (see `portfolio/positions.csv`)
| Stock | Status | $ |
|---|---|---|
| Quality Power (QPOWER IS) | bought | ? |
| Reliance (RELIANCE IS) | planned / unconfirmed | ~50k? |
| Emami (HMN IS) | planned / unconfirmed | ~50k? |
| Whirlpool of India (WHIRL IS) | planned / unconfirmed | ~50k? |

## Biggest risks right now
1. **We don't know our own book.** Amounts, fills and cash aren't recorded. → Pull TMSG history and fill `positions.csv` + `trades.csv`.
2. **100% India vs a ~61% US benchmark.** All four picks are Indian small/mid/large caps in INR. Nifty falling + INR weakness = Rel P&L hit twice. Decide deliberately if that's the strategy.
3. **Idle cash.** If most of the $1M is uninvested, we only beat the index when it falls. Decide on a core allocation.
4. **Small sizes can't move rank.** $50k positions at ±5% = ±$2.5k. Leaders are typically far apart; positions up to $200k exist for a reason.
5. **Wrong-ticker risk.** RELIANCE IS ≠ RS UN; WHIRL IS ≠ WHR UN. Always run `scripts/wls.py`.

## Next actions
- [ ] Pull actual trades from TMSG → `portfolio/`.
- [ ] Agree overall strategy (core index-like sleeve + conviction bets?) → write in `strategy/PLAN.md`.
- [ ] 5-line thesis for each holding in `research/stocks/`.
- [ ] Start `tracking/daily_pnl.csv` today.
