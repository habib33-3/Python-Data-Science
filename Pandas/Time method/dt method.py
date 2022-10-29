import pandas as pd

sales = pd.read_csv("../../Files/RetailSales_BeerWineLiquor.csv", parse_dates=[0])
print(sales)
print(sales["DATE"].dt.year)
