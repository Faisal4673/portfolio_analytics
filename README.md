# Portfolio Analytics

A small Python library for computing risk and return analytics on an equity
portfolio. Given a set of tickers and their portfolio weights, it pulls
historical price data from Yahoo Finance (via `yfinance`) and reports
portfolio-level statistics.

## Metrics

- **Beta** — per-stock and weighted-average beta against the Russell 3000 (`^RUA`),
  estimated by regressing each stock's daily returns on the market's.
- **Correlation** — the full correlation matrix plus a weighted-average pairwise
  correlation across holdings (diagonal excluded).
- **Returns & volatility** — the weighted portfolio return series and its
  annualized volatility (daily standard deviation scaled by √252).
- **CAPM expected return** — the weighted-average CAPM required return, using a
  configurable risk-free rate.

## Usage

```bash
python main.py
```

Then enter your portfolio as a dictionary of `{ticker: weight}`, e.g.:

```
{'GOOG': 0.5, 'AMZN': 0.5}
```

The script prints betas, average beta, the correlation matrix, average
correlation, the portfolio return series, volatility, and CAPM expected return.

## Configuration

Defaults live in `constants.py`:

| Setting | Default | Meaning |
| --- | --- | --- |
| `MONTHS` | `60` | Lookback window for price history |
| `INTERVAL` | `"1d"` | Sampling interval |
| `MARKET` | `"^RUA"` | Benchmark used for beta / CAPM (Russell 3000) |
| `RISK_FREE_RATE` | `0.045` | Annual risk-free rate for CAPM |

## Project layout

| File | Responsibility |
| --- | --- |
| `portfolio.py` | `Portfolio` — aggregates holdings into portfolio-level metrics |
| `stock.py` | `Stock` — price history, returns, beta, alpha, and CAPM per ticker |
| `functs.py` | Regression (beta/alpha) and correlation helpers |
| `constants.py` | Configuration constants |
| `main.py` | Command-line entry point |

## Notes

All market data comes from `yfinance`. This is a personal project built to
learn quantitative portfolio analytics in Python.
