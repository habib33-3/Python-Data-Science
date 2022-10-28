import pandas as pd

df = pd.read_csv("../../Files/tips.csv")
print(df)

my_map = {"Female": "F", "Male": "M"}
df["sex"]=df["sex"].map(my_map)
print(df)
