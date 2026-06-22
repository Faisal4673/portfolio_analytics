import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date, timedelta as dt



def get_beta_alpha(stock_returns, market_returns):
    # Regress the stock's returns on the market's returns (aligned by date).
    # The slope is beta (market sensitivity); the intercept is alpha.
    merge_data = pd.merge(stock_returns, market_returns, left_index=True, right_index=True)
    y = merge_data.iloc[:, 0]
    x = merge_data.iloc[:, 1]
    # Build the design matrix [x, 1] and solve the least-squares fit y = beta*x + alpha.
    X = np.vstack([x, np.ones(len(x))]).T
    beta, alpha = np.linalg.lstsq(X, y, rcond=None)[0]
    return beta, alpha

def get_correlation(stock1, stock2):
    
    merged = pd.merge(stock1.returns, stock2.returns, left_index=True, right_index=True)
    return merged.corr().iloc[0, 1]



