# Where we stand — updated 2026-10-22

**Team:** berg bloom (K J Somaiya) — *assumed ours, confirm*
**Latest leaderboard seen:** Global rank **1373**, Rel P&L **−$1,926**, Abs P&L **−$2,444**.
Same-college rival Titanium Bros: rank 1903, Rel −$10,004.
**Trading days left:** ~17 (last day Fri 13 Nov).

## Holdings (see `portfolio/positions.csv`)
| Stock | Status | $ |
|---|---|---|
| Reliance (RELIANCE IS) | open | 50,000 |
| Quality Power (QPOWER IS) | open | 30,000 |
| Emami (HMN IS) | open | 30,000 |
| Whirlpool of India (WHIRL IS) | open | 30,000 |
| **Invested** | | **140,000** |
| **Cash** | | **~860,000 (86%)** |

Amounts are what Arshia allocated (chat 22-Oct 00:02); exact fills/dates still to pull from TMSG.
If the leaderboard Abs P&L (−$2,444) reflects these holdings, that's ≈ −1.7% on $140k.

## Biggest risks right now
1. **Fills not recorded.** Sizes known, but exact debits, prices and dates aren't. → Pull TMSG history into `portfolio/`.
2. **100% India vs a ~61% US benchmark.** All four picks are Indian small/mid/large caps in INR. Nifty falling + INR weakness = Rel P&L hit twice. Decide deliberately if that's the strategy.
3. **86% idle cash.** With ~$860k uninvested, we only beat the index when it falls. Decide on a core allocation.
4. **Small sizes can't move rank.** $50k positions at ±5% = ±$2.5k. Leaders are typically far apart; positions up to $200k exist for a reason.
5. **Wrong-ticker risk.** RELIANCE IS ≠ RS UN; WHIRL IS ≠ WHR UN. Always run `scripts/wls.py`.

## Next actions
- [ ] Pull exact fills/dates from TMSG → `portfolio/`.
- [ ] Decide what to do with the ~$860k cash → proposal in `strategy/PLAN.md` (team to approve).
- [x] Strategy drafted: `strategy/PLAN.md` (US core + Taiwan overweight + small HK/KR/JP).
- [ ] 5-line thesis for each holding in `research/stocks/`.
- [ ] Start `tracking/daily_pnl.csv` today.
