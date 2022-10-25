import pandas as pd

df = pd.read_csv("../../Files/tips.csv")
print(df)


print(df.columns)
print(df.index)
print(df.head())  # return couple of top rows
print(df.tail())  # return couple of bottom rows
print(df.describe().transpose())
