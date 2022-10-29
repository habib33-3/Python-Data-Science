import pandas as pd

sales = pd.read_csv("../../Files/RetailSales_BeerWineLiquor.csv")
print(sales)
sales = pd.read_csv("../../Files/RetailSales_BeerWineLiquor.csv", parse_dates=[0])
print(sales)
