from stock import Stock
import pandas as pd
import numpy as np


class Portfolio:
    def __init__(self, stock_dict):
        self.stock_dict = {Stock(stock): weight for stock, weight in stock_dict.items()}
        self.ticker_dict = {stock.ticker: weight for stock, weight in self.stock_dict.items()}
        self.corr_matrix = pd.concat([stock.returns for stock in self.stock_dict], axis=1, join="outer").corr()
        self.betas = pd.Series({stock.ticker: stock.beta() for stock in self.stock_dict})
        self.avg_beta = sum([stock.beta() * weight for stock, weight in self.stock_dict.items()])
        self.avg_corr = self._compute_avg_corr()
        self.returns = pd.DataFrame(
            pd.concat([stock.returns * weight for stock, weight in self.stock_dict.items()], axis=1, join="inner").sum(axis=1),
            columns=["PORTFOLIO RETURNS"],
        )
        self.volatility = (self.returns.std() * np.sqrt(252))["PORTFOLIO RETURNS"]
        self.capm_return = sum([stock.capm_return * weight for stock, weight in self.stock_dict.items()])

    def _compute_avg_corr(self):
        # Weighted average of the off-diagonal correlations (each pair weighted
        # by the product of the two holdings' weights). The diagonal of 1.0s is
        # masked out so a stock's correlation with itself doesn't skew the mean.
        weight_series = [self.stock_dict[stock] for stock in self.stock_dict]
        weight_array = np.outer(weight_series, weight_series)
        mask = ~np.eye(len(weight_series), dtype=bool)
        corr_vals = self.corr_matrix.values[mask]
        w_vals = weight_array[mask]
        valid = ~np.isnan(corr_vals)
        return (corr_vals[valid] * w_vals[valid]).sum() / w_vals[valid].sum()
