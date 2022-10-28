import pandas as pd

df = pd.read_csv("../../Files/mpg.csv")
print(df)

print(df["model_year"].value_counts())
print(df.groupby("model_year").mean())
print(df.groupby(["model_year", "cylinders"]).mean(numeric_only=True))
print(df.groupby(["model_year", "cylinders"]).mean(numeric_only=True)["mpg"])
print(df.groupby("model_year").describe().transpose())
year_cyl = df.groupby(["model_year", "cylinders"]).mean(numeric_only=True)
print(year_cyl)
print(year_cyl.index.levels)
print(year_cyl.loc[70])
print(year_cyl.loc[(70,4)])
