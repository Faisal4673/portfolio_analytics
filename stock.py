from functs import get_beta_alpha, get_correlation
import yfinance as yf
from datetime import date, timedelta as dt
import numpy as np
from constants import MARKET, MONTHS, INTERVAL


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.months = MONTHS
        self.interval = INTERVAL
        self.prices = yf.download(self.ticker, start=(date.today() - dt(days=MONTHS*31)),  end=date.today(), interval=INTERVAL, auto_adjust=False)["Adj Close"]
        self.returns = self.prices.pct_change().dropna()
        self.volatility = (self.returns.std() * np.sqrt(252))[self.ticker]


    
    def beta(self):
        return get_beta_alpha(self.returns, default_mkt.returns)[0]
    
    def alpha(self):
        return get_beta_alpha(self.returns, default_mkt.returns)[1]
    
    def corr(self, other):
        return get_correlation(self, other)
    


default_mkt = Stock(MARKET)    


