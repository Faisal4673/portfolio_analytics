from functs import get_data, get_beta_alpha, get_correlation


class Stock:
    def __init__(self, ticker, months=24, interval="1d"):
        self.ticker = ticker
        self.months = months
        self.interval = interval


    def data(self, months=24, interval="1d"):
        return get_data(self.ticker, months, interval)
    
    def beta(self, market="^RUA", months=24, interval="1d"):
        return get_beta_alpha(self.ticker, market, months, interval)[0]
    
    def alpha(self, market="^RUA", months=24, interval="1d"):
        return get_beta_alpha(self.ticker, market, months, interval)[1]
    
    def corr(self, other, months=24):
        return get_correlation(self.ticker, other.ticker, months)
    
