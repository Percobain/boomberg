"""Is it in WLS? Search the investible universe by name or ticker.

Usage: python scripts/wls.py "quality power" reliance "LULU UW"
If a stock is NOT here, TMSG will reject it with an "Index Membership" error.
Caveat: the list is a Sep 03 2026 snapshot; confirm on the Terminal before trading.
"""
import sys
from pathlib import Path

import pandas as pd

UNIVERSE = Path(__file__).resolve().parent.parent / "data/processed/wls_universe.csv"


def main(queries):
    df = pd.read_csv(UNIVERSE)
    for q in queries:
        ql = q.lower()
        hits = df[df.name.str.lower().str.contains(ql, regex=False, na=False)
                  | df.ticker.str.lower().str.contains(ql, regex=False, na=False)]
        print(f"\n== {q!r}: {'NOT IN WLS' if hits.empty else f'{len(hits)} match(es)'}")
        if not hits.empty:
            print(hits.head(15).to_string(index=False))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
