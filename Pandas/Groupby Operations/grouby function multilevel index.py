import pandas as pd

df = pd.read_csv("../../Files/mpg.csv")
print(df)

year_cyl = df.groupby(["model_year", "cylinders"]).mean(numeric_only=True)
print(year_cyl)

print("Model year = 70")
print(year_cyl.xs(key=70, level="model_year"))
print()
print("cylinders=4")
print(year_cyl.xs(key=4, level="cylinders"))
print()
print(year_cyl.swaplevel())
print()
print(year_cyl.sort_index(level="model_year", ascending=False))

print()
print(df.agg(["std", "mean"]))
print(df.agg(["std", "mean"]))
print(df.agg({"mpg": ["max", "mean"], "weight": ["mean", "std"]}))
