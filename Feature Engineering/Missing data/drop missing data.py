import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open("../../Files/Ames_Housing_Feature_Description.txt", "r") as f:
    print(f.read())

df = pd.read_csv("../File/ames_without_outliers.csv")
print(df.head())

df = df.drop("PID", axis=1)


def percent_missing(dataframe):
    percent_nan = 100 * dataframe.isnull().sum() / len(dataframe)
    percent_nan = percent_nan[percent_nan > 0].sort_values()

    return percent_nan


percentage_missing = percent_missing(df)
print(percentage_missing)

less_than1percentage = percentage_missing[percentage_missing < 1]
print(f"less than 1%= \n{less_than1percentage}")

print(df[df["Electrical"].isnull()]["Garage Area"])  # electrical is missing but garage area is not
print(df["Bsmt Half Bath"].isnull())

df = df.dropna(axis=0, subset=["Electrical", "Garage Cars"])
percentage_missing = percent_missing(df)

plt.figure(num=2, dpi=100)
sns.barplot(x=percentage_missing.index, y=percentage_missing)
plt.xticks(rotation=90)
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig("missing data bar-plot after drop.png")

df.to_csv("after_drop.csv")

plt.show()
