import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#Gather info on AAPL MSFT and SPY over past 5 years
Data = yf.download(['AAPL', 'MSFT', 'SPY'], start='2021-01-01', end='2026-01-01')

#Calculate Cumulative Returns for each
returns = Data['Close'].pct_change()
Cum_returns = (1 + returns).cumprod()

#Calculate 30 day annualized rolling volatility for SPY
volatility = returns['SPY'].rolling(30).std() * (252 ** 0.5)

#Initialize a 2x1 subplot figure layout
fig, axes = plt.subplots(2, 1, figsize=(12, 8))
fig.suptitle('Cumulative Returns vs Volatility over 5yrs', fontsize='14', fontweight='bold')

#Top Graph = cumulative returns for each Ticker
Cum_returns.plot(ax=axes[0], color=['red', 'green', 'purple'])
axes[0].legend(loc='upper left')
axes[0].set(title ='Cumulative Returns (AAPL, MSFT, SPY)', ylabel = 'Growth of $1')

#Bottom Graph = 30 day annualized rolling volatility for SPY
axes[1].plot(volatility, color='purple', label='SPY Volatility')
axes[1].legend(loc='upper left')
axes[1].set(title = '30 Day Annualized Rolling Volatility (SPY)', xlabel = 'Date', ylabel = 'vVlatility')

plt.tight_layout()
plt.show()
