import pandas as pd

with open("../../Files/Ames_Housing_Feature_Description.txt", "r") as f:
    print(f.read())

df = pd.read_csv("after_fixing.csv")
print(df.head())

print(df["Lot Frontage"])

print(df.groupby("Neighborhood")["Lot Frontage"].mean())

df["Lot Frontage"] = df.groupby("Neighborhood")["Lot Frontage"].transform(lambda value: value.fillna(value.mean()))

df["Lot Frontage"] = df["Lot Frontage"].fillna(0)

print(df.isnull().sum())

df.to_csv("no_missing_data.csv")
