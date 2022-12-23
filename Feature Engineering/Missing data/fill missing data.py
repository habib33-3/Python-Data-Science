import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open("../../Files/Ames_Housing_Feature_Description.txt", "r") as f:
    print(f.read())

df = pd.read_csv("after_drop.csv")
print(df.head())


def percent_missing(dataframe):
    percent_nan = 100 * dataframe.isnull().sum() / len(dataframe)
    percent_nan = percent_nan[percent_nan > 0].sort_values()

    return percent_nan


print(df[df["Bsmt Full Bath"].isnull()])

# BSMT numeric columns --> fill na 0

bsmt_num_cols = ["BsmtFin SF 1", "BsmtFin SF 2", "Bsmt Unf SF", "Total Bsmt SF", "Bsmt Full Bath", "Bsmt Half Bath"]
df[bsmt_num_cols] = df[bsmt_num_cols].fillna(0)

# BSMT String Column

bsmt_string_col = ["Bsmt Qual", "Bsmt Cond", "Bsmt Exposure", "BsmtFin Type 1", "BsmtFin Type 2"]
df[bsmt_string_col] = df[bsmt_string_col].fillna("None")

df["Mas Vnr Type"] = df["Mas Vnr Type"].fillna("None")
df["Mas Vnr Area"] = df["Mas Vnr Area"].fillna(0)

percentage_missing = percent_missing(df)

plt.figure(num=3, dpi=100)
sns.barplot(x=percentage_missing.index, y=percentage_missing)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("missing data bar-plot after filling.png")

print(df[df["Bsmt Full Bath"].isnull()])

df.to_csv("after_fill.csv")

plt.show()
