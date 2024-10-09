import pandas as pd

# Load your data
file_path = '../data/HINDALCO_1D.xlsx'
df = pd.read_excel(file_path)

# Calculate the short-term (20-day) and long-term (50-day) SMAs
df['SMA_20'] = df['close'].rolling(window=20).mean()
df['SMA_50'] = df['close'].rolling(window=50).mean()

# Generate buy/sell signals
df['Signal'] = 0
df.loc[df['SMA_20'] > df['SMA_50'], 'Signal'] = 1  # Buy signal
df.loc[df['SMA_20'] < df['SMA_50'], 'Signal'] = -1  # Sell signal

# Shift signals
df['Position'] = df['Signal'].shift()

# Calculate daily returns and strategy returns
df['Returns'] = df['close'].pct_change()
df['Strategy_Returns'] = df['Returns'] * df['Position']

# Cumulative returns for strategy and buy-and-hold
df['Cumulative_Strategy_Returns'] = (1 + df['Strategy_Returns']).cumprod()
df['Cumulative_Buy_Hold_Returns'] = (1 + df['Returns']).cumprod()

# Save or view the results
df.to_csv('strategy_output.csv')
