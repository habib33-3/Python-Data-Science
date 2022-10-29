import pandas as pd

sales = pd.read_csv("../../Files/RetailSales_BeerWineLiquor.csv", parse_dates=[0])
print(sales)

sales = sales.set_index("DATE")
print(sales)

print(sales.resample(rule="A").mean())
