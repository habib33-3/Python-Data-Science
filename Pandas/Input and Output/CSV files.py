import pandas as pd

df1 = pd.read_csv("../../Files/example.csv", index_col=0)
print(df1)
df1.to_csv("newfile.csv")
