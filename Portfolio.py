from stock import Stock
import pandas as pd
import numpy as np

class Portfolio:
    def __init__(self, stock_dict):
        self.stock_dict = {Stock(stock): weight for stock, weight in stock_dict.items()}
        self.ticker_dict ={stock.ticker: weight for stock, weight, in self.stock_dict.items()}
        self.corr_matrix = pd.concat([stock.returns for stock in self.stock_dict], axis=1, join="outer").corr()
        self.betas = pd.Series({stock.ticker: stock.beta() for stock in self.stock_dict})
        self.avg_beta = sum([stock.beta()* weight for stock, weight, in self.stock_dict.items()])
        self.avg_corr = self._compute_avg_corr()
        self.returns = pd.DataFrame((pd.concat([stock.returns * weight for stock, weight in self.stock_dict.items()], axis=1, join="inner")).sum(axis=1), columns=["PORTFOLIO RETURNS"])
        self.volatility = (self.returns.std() * np.sqrt(252))["PORTFOLIO RETURNS"]


    
    def _compute_avg_corr(self):
        weight_series = [self.stock_dict[stock] for stock in self.stock_dict]
        weight_array = np.outer(weight_series, weight_series)
        mask = ~np.eye(len(weight_series), dtype=bool)
        corr_vals = self.corr_matrix.values[mask]
        w_vals = weight_array[mask]
        valid = ~np.isnan(corr_vals)
        return (corr_vals[valid] * w_vals[valid]).sum() / w_vals[valid].sum()
        

    






matrix_dict = {
    "GOOG": 0.0852,
    "AMZN": 0.0578,
    "AMGN": 0.0285,
    "AAPL": 0.0648,
    "AMAT": 0.0345,
    "BK":   0.0233,
    "CMCSA": 0.0307,
    "META": 0.0428,
    "FDX":  0.0316,
    "FGXXX": 0.0051,
    "GNRC": 0.0523,
    "GS":   0.0439,
    "INTU": 0.0100,
    "JPM":  0.0373,
    "LOW":  0.0316,
    "MSFT": 0.0705,
    "MS":   0.0444,
    "NKE":  0.0148,
    "PNC":  0.0371,
    "PYPL": 0.0265,
    "PEP":  0.0368,
    "QCOM": 0.0333,
    "TXN":  0.0209,
    "TMO":  0.0157,
    "TSN":  0.0310,
    "USB":  0.0300,
    "WFC":  0.0315,
    "MDT":  0.0280,
}

test_dict = {
    "GOOG": 0.5,
    "AMZN": 0.5,}

matrix_etf = Portfolio(test_dict)

print(matrix_etf.betas)
