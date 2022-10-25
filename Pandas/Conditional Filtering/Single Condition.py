import pandas as pd

df = pd.read_csv("../../Files/tips.csv")
print(df.head())

print(df[df['total_bill'] > 30])
print(df[df['sex'] == "Male"])
