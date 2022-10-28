import pandas as pd

df = pd.read_csv("../../Files/tips.csv")
print(df)

print(df.describe())

print(df.sort_values("tip", ascending=True))

print(df.sort_values(["tip", "size"]))
print(df["total_bill"].max())
print(df["total_bill"].idxmax())
print(df.corr())
print(df["sex"].value_counts())
print(df["day"].unique())
print(df.duplicated())
print(df["total_bill"].between(10, 20))
print(df.sample(5))
print(df.sample(frac=0.1))
