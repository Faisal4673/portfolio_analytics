import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta as dt

def get_data(ticker, months=24, _interval="1d"):
    # downloads stock data, from today - months, to today. Auto_adjust makes it so it returns adj close. Returns adj close price for given period
    stock_data = yf.download(ticker, start=(date.today() - dt(days=months*31)),  end=date.today(), interval=_interval, auto_adjust=False)
    return stock_data["Adj Close"]

def get_beta_alpha(ticker, market="^RUA", months=24, interval="1d"):
    #Gets the returns of the data (day to day pct change). Uses russel3000 as default market. Merges according to date. Adds suffix
    returns = get_data(ticker, months, interval).pct_change().dropna()
    market_returns = get_data(market, months, interval).pct_change().dropna()
    merge_data = pd.merge(returns, market_returns, left_index=True, right_index=True)
    y = merge_data[ticker]
    x = merge_data[market]
    # Not sure what this is, something about setting up the shape of the regression
    X = np.vstack([x, np.ones(len(x))]).T
    beta, alpha = np.linalg.lstsq(X, y, rcond=None)[0]
    return beta, alpha

def get_correlation(ticker1, ticker2, months=24, interval="1d"):
    data1 = get_data(ticker1, months, interval)
    data2 = get_data(ticker2, months, interval)
    merged = pd.merge(data1.pct_change().dropna(), data2.pct_change().dropna(), left_index=True, right_index=True)
    return merged.corr().iloc[0, 1]



