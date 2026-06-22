import ast
from Portfolio import Portfolio



def main():
    raw = input("Enter your portfolio as a dictionary with yfinance tickers as keys and weights as values (e.g., {'GOOG': 0.5, 'AMZN': 0.5}): ")
    portfolio = Portfolio(ast.literal_eval(raw))
    print("REPORT:")
    print("Portfolio Betas:")
    print(portfolio.betas)
    print("Average Beta:")
    print(portfolio.avg_beta)
    print("Correlation Matrix:")
    print(portfolio.corr_matrix)
    print("Average Correlation:")
    print(portfolio.avg_corr)
    print("Portfolio Returns:")
    print(portfolio.returns)
    print("Portfolio Volatility:")
    print(portfolio.volatility)
    print("Portfolio CAPM Return:")
    print(portfolio.capm_return)


if __name__ == "__main__":    
    main()