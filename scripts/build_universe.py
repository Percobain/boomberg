"""Clean the raw WLS export into data/processed/wls_universe.csv.

Usage: python scripts/build_universe.py
Re-run whenever a newer WLS export is dropped into data/raw/ (update RAW below).
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw/WLS as of Sep 03 2026 arshia.xlsx"
OUT = ROOT / "data/processed/wls_universe.csv"

# Bloomberg exchange suffix -> country. "?" marks codes worth double-checking on the Terminal.
SUFFIX_COUNTRY = {
    "UW": "United States", "UN": "United States", "UQ": "United States", "UR": "United States",
    "UF": "United States", "UA": "United States",
    "JT": "Japan", "TT": "Taiwan", "LN": "United Kingdom", "CT": "Canada", "HK": "Hong Kong",
    "KP": "South Korea", "KQ": "South Korea", "FP": "France", "SE": "Switzerland", "GY": "Germany",
    "IS": "India", "IB": "India", "AT": "Australia", "C1": "China", "C2": "China",
    "NA": "Netherlands", "SQ": "Spain", "SS": "Sweden", "IM": "Italy", "BS": "Brazil",
    "SP": "Singapore", "AB": "Saudi Arabia", "DC": "Denmark", "SJ": "South Africa", "IT": "Israel",
    "BB": "Belgium", "MF": "Mexico", "FH": "Finland", "TB": "Thailand", "NO": "Norway",
    "MK": "Malaysia", "PW": "Poland", "IJ": "Indonesia", "AV": "Austria", "TI": "Turkey",
    "ID": "Ireland", "DH": "UAE", "DB": "UAE", "CC": "Chile", "KK": "Kuwait", "GA": "Greece",
    "QD": "Qatar", "PM": "Philippines", "PL": "Portugal", "NZ": "New Zealand", "HB": "Hungary",
    "CK": "Czech Republic", "PE": "Peru",
    "CX": "? verify", "EC": "? verify", "SF": "? verify",
}


def main():
    df = pd.read_excel(RAW, sheet_name="Worksheet")
    df.columns = [c.strip().lower() for c in df.columns]
    for c in ("weight", "shares", "price"):
        df[c] = pd.to_numeric(df[c], errors="coerce")  # a couple of rows have "--"
    df["suffix"] = df["ticker"].str.split().str[1]
    df["country"] = df["suffix"].map(SUFFIX_COUNTRY).fillna("? verify")
    df = df.rename(columns={"weight": "weight_pct", "price": "price_sep03_local"})
    df = df[["ticker", "name", "country", "suffix", "weight_pct", "shares", "price_sep03_local"]]
    df.sort_values("weight_pct", ascending=False).to_csv(OUT, index=False)

    by_country = df.groupby("country")["weight_pct"].sum().sort_values(ascending=False)
    by_country.round(3).to_csv(ROOT / "data/processed/wls_country_weights.csv", header=["weight_pct"])
    print(f"{len(df)} stocks, total weight {df.weight_pct.sum():.2f}% -> {OUT.relative_to(ROOT)}")
    print(by_country.head(10).round(2).to_string())


if __name__ == "__main__":
    main()
