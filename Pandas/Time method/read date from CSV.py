import pandas as pd

sales = pd.read_csv("../../Files/RetailSales_BeerWineLiquor.csv")
print(sales)

sales["DATE"] = pd.to_datetime(sales["DATE"])
print(sales)
print(sales["DATE"][0].year)


