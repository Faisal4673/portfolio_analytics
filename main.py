from stock import Stock

def main():
    ticker = input("Input Ticker")
    stock = Stock(ticker)
    print("Beta: ", stock.beta(), "Alpha: ", stock.alpha())

main()