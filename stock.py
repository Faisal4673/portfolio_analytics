from functs import get_beta_alpha, get_correlation
import yfinance as yf
from datetime import date, timedelta as dt
import numpy as np
from constants import MARKET, MONTHS, INTERVAL, RISK_FREE_RATE



# The market benchmark, built lazily as a Stock with ticker MARKET.
default_mkt = None


class Stock:
    def __init__(self, ticker):
        global default_mkt
        self.ticker = ticker
        self.months = MONTHS
        self.interval = INTERVAL
        self.prices = yf.download(self.ticker, start=(date.today() - dt(days=MONTHS*31)),  end=date.today(), interval=INTERVAL, auto_adjust=False)["Adj Close"]
        self.returns = self.prices.pct_change().dropna()
        self.volatility = (self.returns.std() * np.sqrt(252))[self.ticker]
        if default_mkt is None:
            default_mkt = self if ticker == MARKET else Stock(MARKET)
        market_annual_return = (default_mkt.returns.mean() * 252)[MARKET]
        self.capm_return = RISK_FREE_RATE + self.beta() * (market_annual_return - RISK_FREE_RATE)


    
    def beta(self):
        return get_beta_alpha(self.returns, default_mkt.returns)[0]
    
    def alpha(self):
        return get_beta_alpha(self.returns, default_mkt.returns)[1]
    
    def corr(self, other):
        return get_correlation(self, other)
    


  


