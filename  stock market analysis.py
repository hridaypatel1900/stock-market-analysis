import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
from plotly.subplots import make_subplots

today = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=50000)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

input_string = input("stock_name")
data = yf.download((input_string),
                   start=start_date,
                   end=end_date,
                   progress=False)
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)

# Set up subplots with one subplot
fig = make_subplots(rows=1, cols=1)

# Plot the initial candlestick chart
candlestick_trace = go.Candlestick(x=data["Date"],
                                   open=data["Open"],
                                   high=data["High"],
                                   low=data["Low"],
                                   close=data["Close"])

fig.add_trace(candlestick_trace)

# Update layout
fig.update_layout(title="Stock Price Analysis",
                  xaxis_rangeslider_visible=False)

# Display the initial figure
fig.show()