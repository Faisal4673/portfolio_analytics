import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date, timedelta as dt



def get_beta_alpha(stock_returns, market_returns):
    #Gets the returns of the data (day to day pct change). Uses russel3000 as default market. Merges according to date. Adds suffix
    merge_data = pd.merge(stock_returns, market_returns, left_index=True, right_index=True)
    y = merge_data.iloc[:, 0]
    x = merge_data.iloc[:, 1]
    # Not sure what this is, something about setting up the shape of the regression
    X = np.vstack([x, np.ones(len(x))]).T
    beta, alpha = np.linalg.lstsq(X, y, rcond=None)[0]
    return beta, alpha

def get_correlation(stock1, stock2):
    
    merged = pd.merge(stock1.returns, stock2.returns, left_index=True, right_index=True)
    return merged.corr().iloc[0, 1]



