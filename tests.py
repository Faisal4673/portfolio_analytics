import yfinance as yf
import pandas as pd
import numpy as np

# https://jakevdp.github.io/PythonDataScienceHandbook/

np.random.seed(0)

a = np.random.randint(10, size=(5, 1))
b = np.ones((5, 1), int)




c = np.concat([a, b])

print(c)