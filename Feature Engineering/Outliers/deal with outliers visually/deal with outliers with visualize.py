import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("../../../Files/Ames_Housing_Data.csv")
print(df.head())

correlation_with_salesPrice = df.corr()["SalePrice"].sort_values()
print(f"Correlation with sales price={correlation_with_salesPrice}")

plt.figure(1)
sns.scatterplot(x="Overall Qual", y="SalePrice", data=df)
plt.savefig("Correlation with sales price and overall quality.png")

plt.figure(2)
sns.scatterplot(x="Gr Liv Area", y="SalePrice", data=df)
plt.savefig("Correlation with sales price and Gr Liv area.")

outliers = df[(df["Gr Liv Area"] > 4000) & (df["SalePrice"] < 400000)]
print(f"Outliers={outliers}")

drop_index = outliers.index
df = df.drop(drop_index, axis=0)

df.to_csv("ames_without_outliers.csv")
# plt.show()
