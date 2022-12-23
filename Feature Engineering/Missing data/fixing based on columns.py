import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open("../../Files/Ames_Housing_Feature_Description.txt", "r") as f:
    print(f.read())

df = pd.read_csv("after_fill.csv")
print(df.head())


def percent_missing(dataframe):
    percent_nan = 100 * dataframe.isnull().sum() / len(dataframe)
    percent_nan = percent_nan[percent_nan > 0].sort_values()

    return percent_nan


gar_str_cols = ["Garage Type", "Garage Finish", "Garage Qual", "Garage Cond"]
df[gar_str_cols] = df[gar_str_cols].fillna("None")
df["Garage Yr Blt"] = df["Garage Yr Blt"].fillna(0)

percentage_missing = percent_missing(df)

plt.figure(dpi=100)
sns.barplot(x=percentage_missing.index, y=percentage_missing)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("missing data bar-plot after fixing using feature.png")

df = df.drop(["Pool QC", "Misc Feature", "Alley", "Fence"], axis=1)
df["Fireplace Qu"] = df["Fireplace Qu"].fillna("None")

percentage_missing_drop_column = percent_missing(df)

plt.figure(dpi=100)
sns.barplot(x=percentage_missing_drop_column.index, y=percentage_missing_drop_column)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("missing data bar-plot after drop column.png")

df.to_csv("after_fixing.csv")
plt.show()
