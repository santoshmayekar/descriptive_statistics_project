# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

def calculate_statistics():
    mean = np.mean(sale_price)
    median = np.median(sale_price)
    mode1 = sale_price.mode()
    mode=mode1[0]
    return mean,median,mode
