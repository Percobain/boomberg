"""Rule check + benchmark-relative exposure for portfolio/positions.csv.

Usage: python scripts/check_portfolio.py [strategy/orders_YYYY-MM-DD.csv]
Pass an orders file to check the book AS IF those buys were filled.
Checks: WLS membership, <= $200k per name (20%), cash >= 0, long-only.
Then shows our country weights vs the WLS benchmark, because we are ranked on
RELATIVE P&L: every % we hold away from the index's mix is an active bet.
"""
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CAPITAL = 1_000_000
MAX_POSITION = 200_000


def main():
    uni = pd.read_csv(ROOT / "data/processed/wls_universe.csv")
    pos = pd.read_csv(ROOT / "portfolio/positions.csv")
    held = pos[pos.status.isin(["open", "pending"])].copy()
    if len(sys.argv) > 1:
        orders = pd.read_csv(ROOT / sys.argv[1]).rename(columns={"amount_usd": "invested_usd"})
        held = pd.concat([held, orders.assign(status="proposed")], ignore_index=True)
        print(f"(including proposed orders from {sys.argv[1]})")
    held["invested_usd"] = pd.to_numeric(held.invested_usd, errors="coerce")
    held = held.groupby("ticker", as_index=False).agg(invested_usd=("invested_usd", "sum"))

    problems = []
    for _, p in held.iterrows():
        if p.ticker not in set(uni.ticker):
            problems.append(f"{p.ticker}: not in WLS snapshot")
        if pd.isna(p.invested_usd):
            problems.append(f"{p.ticker}: invested_usd unknown - fill in from TMSG")
        elif p.invested_usd > MAX_POSITION:
            problems.append(f"{p.ticker}: ${p.invested_usd:,.0f} > ${MAX_POSITION:,} cap")
        elif p.invested_usd < 0:
            problems.append(f"{p.ticker}: negative amount (long-only!)")

    invested = held.invested_usd.sum()
    cash = CAPITAL - invested
    if cash < 0:
        problems.append(f"cash would be negative: ${cash:,.0f}")

    print(f"Positions: {len(held)} | invested ${invested:,.0f} | cash ${cash:,.0f} "
          f"({cash / CAPITAL:.0%} uninvested - cash earns 0 while the index moves)")
    print("\nRULE CHECK:", "OK" if not problems else "")
    for p in problems:
        print("  !!", p)

    held = held.merge(uni[["ticker", "country"]], on="ticker", how="left")
    ours = (held.groupby("country").invested_usd.sum() / CAPITAL * 100).rename("ours_pct")
    bench = pd.read_csv(ROOT / "data/processed/wls_country_weights.csv", index_col=0).weight_pct
    cmp = pd.concat([ours, bench.rename("wls_pct")], axis=1).fillna(0)
    cmp["active_pct"] = cmp.ours_pct - cmp.wls_pct
    cmp = cmp[(cmp.ours_pct > 0) | (cmp.wls_pct > 1)].sort_values("active_pct")
    print("\nCOUNTRY EXPOSURE vs BENCHMARK (cash counted as 0%):")
    print(cmp.round(2).to_string())


if __name__ == "__main__":
    main()
