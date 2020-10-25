# Simple Moving Average

import pandas as pd
import plotly as py
from plotly import subplots
import plotly.graph_objs as go

df = pd.read_csv('EURUSDDaily.csv')
df.columns = ['date', 'close', 'open', 'high', 'low', 'change']
df.date = pd.to_datetime(df.date, format="%m/%d/%Y")
df = df.set_index(df.date)
df = df[['close', 'open', 'high', 'low', 'change']]
df = df.drop_duplicates(keep=False)

# Moving Average

ma = df.close.rolling(center=False, window=30).mean()

trace0 = go.Ohlc(x=df.index, open=df.open, high=df.high, low=df.low, close=df.close, name='Currency Quote')
trace1 = go.Scatter(x=df.index, y=ma)
trace2 = go.Bar(x=df.index, y=df.change)

data = [trace0, trace1, trace2]

fig = subplots.make_subplots(rows=2, cols = 1, shared_xaxes=True)
fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 2, 1)

# print to HTMl

py.offline.plot(fig,filename='MA1.html')

print(df.head())
