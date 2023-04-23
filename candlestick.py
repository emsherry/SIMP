import pandas as pd
import mplfinance as mpf

# read data from file into a DataFrame
ohlc = pd.read_csv('test.csv', index_col=0, parse_dates=True)

# convert index to DatetimeIndex
ohlc.index = pd.to_datetime(ohlc.index)

# plot candlestick chart
s = mpf.make_mpf_style(base_mpf_style='yahoo', gridaxis='both')
mpf.plot(ohlc, type='candle', style=s, volume=False)
