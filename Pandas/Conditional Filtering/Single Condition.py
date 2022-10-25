import pandas as pd

df = pd.read_csv("../../Files/tips.csv")
print(df.head())

bool_series = df['total_bill'] > 30

print(df[bool_series])
