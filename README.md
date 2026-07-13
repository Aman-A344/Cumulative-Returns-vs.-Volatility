# Financial Analysis: Cumulative Returns vs. Volatility

A Python-based data visualization tool that analyzes and compares the historical performance of **Apple (AAPL)**, **Microsoft (MSFT)**, and the **S&P 500 ETF (SPY)** over a 5-year period. 

The script generates a dual-plot visualization comparing the cumulative growth of a \$1 investment against the 30-day annualized rolling volatility of the broader market (SPY).

---

## Features

* **True Cumulative Returns:** Utilizes standard close-to-close daily percentage returns (`.pct_change()`) to accurately track the compounding growth of assets, factoring in overnight price gaps.
* **Annualized Rolling Volatility:** Calculates the 30-day rolling standard deviation of SPY returns, scaled to an annualized metric ($\sigma \times \sqrt{252}$).
* **Clean Visualizations:** Uses `matplotlib` subplots paired with a clean `seaborn` aesthetic to display both data points on a cohesive time-series chart.

---

## Methodology

### 1. Cumulative Returns
Instead of basic price tracking or isolating intraday (Open-to-Close) fluctuations, the script measures day-over-day holding performance:
$$\text{Daily Return} = \frac{\text{Close}_t - \text{Close}_{t-1}}{\text{Close}_{t-1}}$$

These daily fractions are then compounded sequentially to show the growth of an initial \$1 investment:
$$\text{Cumulative Return} = \prod (1 + \text{Daily Return})$$

### 2. Annualized Volatility
Volatility represents market risk. By taking the standard deviation of daily returns over a rolling 30-day window and multiplying it by the square root of the number of trading days in a year (252), we get a standardized annual risk metric.

---

## Installation & Setup
Make sure you have Python installed. You will need to install the following dependencies:

```bash
pip install yfinance matplotlib seaborn pandas
