import pandas as pd

tech_finance = ["GOOG,APPL,AMZN", "JPM,BAC,GS"]

tickers = pd.Series(tech_finance)

print(tickers)
print(tickers.str.split(","))
print(tickers.str.split(",").str[0])
print(tickers.str.split(",", expand=True))
