import pandas as pd

df = pd.read_csv("../../Files/tips.csv")
print(df)

df["sex"] = df["sex"].replace(["Male", "Female"], ["M", "F"])
print(df)
