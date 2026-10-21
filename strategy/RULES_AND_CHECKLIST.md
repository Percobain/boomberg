# Rules cheat-sheet + anti-fumble checklist

Source: `docs/rules/2026 Traders Handbook.pdf` (text copy: `docs/rules/handbook.txt`).

## Hard rules (TMSG enforces these)
| Rule | Detail | TMSG error if broken |
|---|---|---|
| Capital | $1,000,000 USD | — |
| Long only, no leverage | Strategy dropdown must be **Long** | "Max # Sell ideas is 0" |
| Max per stock | 20% = **$200,000** per company | "Maximum Position Size as a Percentage" |
| Cash ≥ 0 | Can't spend more than you have | "Minimum Cash Balance is 0" |
| Universe | Only **WLS Index** members (~10.8k stocks) | "Index Membership" |
| Who trades | Only the **captain** enters trades in `TMSG <GO>` | — |
| Execution | ~**20 min** to execute; fills are approx (max whole shares for the $ amount) | — |

## How we are ranked
**Relative P&L vs the WLS Index** (the `Rel P&L` column in TMSG). Making money is not enough — we must beat the index.

What the WLS benchmark actually is (Sep-03 snapshot, `data/processed/wls_country_weights.csv`):
- **United States ≈ 61%**, Japan ≈ 5.8%, Taiwan ≈ 3.2%, UK ≈ 3.1%, Canada ≈ 3.0% … **India ≈ 1.7%**.
- So an India-heavy portfolio is a huge active bet on India **and on INR vs USD**. If Nifty falls or the rupee weakens while US large-caps rise, Rel P&L gets hit twice.
- **Uninvested cash is also a bet** — it earns 0 while the index moves. If the index rises, idle cash loses Rel P&L.

## Key dates (2026)
| Date | Event |
|---|---|
| Mon 12 Oct | Challenge begins (tracker workbook uses 13 Oct as baseline) |
| Mon 19 Oct | Week 1 leaderboard |
| Mon 26 Oct | Week 2 leaderboard |
| Mon 2 Nov | Week 3 leaderboard |
| Mon 9 Nov | Week 4 leaderboard |
| **Fri 13 Nov** | **Last trading day** |
| Fri 20 Nov | Winners announced |

## PRE-TRADE CHECKLIST (do every time — this is how we don't fumble)
1. `python scripts/wls.py "<name>"` → confirm the **exact** ticker (e.g. `RELIANCE IS` not `RS UN`; `WHIRL IS` not `WHR UN`).
2. Thesis written in `research/stocks/<TICKER>.md` (even 5 lines): why it beats the **index** in the time left, and the exit/stop.
3. Size ≤ $200k and ≤ available cash. Think about what it does to country/sector exposure (`python scripts/check_portfolio.py`).
4. Team agreed (who/when noted in the journal). Captain enters it in TMSG; strategy = **Long**.
5. Within the hour: log it in `portfolio/trades.csv` + update `portfolio/positions.csv` with **actual fill** from `TMSG > 4) NETWORKS > Show History`.
6. Check the trade actually executed (20-min lag) — mark `verified_in_tmsg=yes`.

## DAILY ROUTINE (~10 min)
- Add a row to `tracking/daily_pnl.csv` (Abs, Rel P&L from TMSG, cash).
- Journal note `journal/YYYY-MM-DD.md`: what moved, any news on holdings, decisions.
- Every Monday: add leaderboard snapshot to `tracking/leaderboard.csv`.

## Useful Terminal functions
`N` news · `BI` industry research · `EQS` screening · `FA` financials · `ANR` analyst recs · `MODL` estimates · `GP` charts · `W` worksheets · `PORT` portfolio analytics (compare vs benchmark!) · `TMSG` trading · `GRAB` screenshot for helpdesk.
Helpdesk: bbgtradecomp@bloomberg.net
