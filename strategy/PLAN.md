# Plan — deploy cash on Fri 23 Oct 2026

Research: `research/countries/2026-10-22_*.md` · Orders: `strategy/orders_2026-10-23.csv`
Check: `python scripts/check_portfolio.py strategy/orders_2026-10-23.csv` → **RULE CHECK: OK**

## Logic
1. We're ranked on **relative** return vs WLS (~61% US). Holding 86% cash + 14% India means any US rally leaves us behind. → **Put most of the cash in the largest US names** to close the gap.
2. To actually *beat* the index we need bets → **overweight Taiwan** (TSMC Q3 beat and strong Q4 guide, but the stock fell in the AI selloff) plus small **Korea/Japan** chip positions with **dated earnings inside the window (28–30 Oct)**.
3. **Hong Kong** is in a downtrend with no stimulus → small and defensive only (AIA + Tencent).
4. **India:** no new money (oil >$110, record FPI outflows, INR ~95). Hold Reliance and Emami; consider trimming Whirlpool of India and Quality Power.
5. Keep **~$100k cash** for adds after MSFT/GOOGL/hynix/Advantest results (28 Oct) and a buffer for FX and fills.

## Orders ($760k)
| Country | Stock | WLS ticker | $ |
|---|---|---|---|
| 🇺🇸 US $400k | NVIDIA | NVDA UW | 110,000 |
| | Microsoft | MSFT UW | 80,000 |
| | Alphabet | GOOGL UW | 80,000 |
| | Apple | AAPL UW | 70,000 |
| | Amazon | AMZN UW | 60,000 |
| 🇹🇼 Taiwan $200k | TSMC | 2330 TT | 120,000 |
| | MediaTek | 2454 TT | 40,000 |
| | Delta Electronics | 2308 TT | 40,000 |
| 🇭🇰 HK $60k | AIA | 1299 HK | 35,000 |
| | Tencent | 700 HK | 25,000 |
| 🇰🇷 Korea $50k | SK hynix | 000660 KP | 30,000 |
| | Samsung Electronics | 005930 KP | 20,000 |
| 🇯🇵 Japan $50k | Tokyo Electron | 8035 JT | 25,000 |
| | Advantest | 6857 JT | 25,000 |

## Resulting book (after orders)
| Country | Ours | WLS | Active |
|---|---|---|---|
| US | 40% | 61% | −21 |
| Taiwan | 20% | 3.2% | **+17** |
| India | 14% | 1.7% | **+12** |
| HK | 6% | 2.3% | +4 |
| Korea | 5% | 2.2% | +3 |
| Japan | 5% | 5.8% | −1 |
| Cash | 10% | 0 | |

## ⚠️ Risks
- **~41% in AI hardware/semis** (NVDA, TSMC, MediaTek, Delta, hynix, Samsung, TEL, Advantest). The SOX index fell ~11% in a week in October. This is the main bet: if the AI selloff continues, we lose relative return.
- **Currencies:** TWD, INR and JPY are all weak against a strong USD (DXY ~101.8).
- **Event cluster 28 Oct:** FOMC statement + MSFT/GOOGL + SK hynix + Advantest all on the same day.
- Prices in the WLS file are from 3 Sep. **Check live prices on the Terminal before entering.**

## Timing (IST; TMSG takes ~20 min to fill)
| Market | Hours IST | Enter |
|---|---|---|
| Japan / Korea | 05:30–12:00 | Morning |
| Taiwan | 06:30–11:00 | Morning |
| Hong Kong | 07:00–13:30 | Morning |
| US | 19:00–01:30 (until US DST ends 1 Nov) | Evening |
If an order goes in while that market is closed, check whether TMSG holds it for the next open.

## Next decision points
- **28–29 Oct:** after MSFT/GOOGL/AMZN, hynix/Samsung and Advantest results → use the ~$100k reserve to add to winners, cut losers.
- **29 Oct:** Fifth Plenum ends + FCC vote → if bad for HK, cut to AIA only.
- **3 Nov:** midterms.
- **~10 Nov:** Taiwan October revenue (TSMC) → decide to hold or take profit before 13 Nov.
