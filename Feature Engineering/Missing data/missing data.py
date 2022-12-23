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

plt.figure(num=1, dpi=100)
sns.barplot(x=percentage_missing.index, y=percentage_missing)
plt.xticks(rotation=90)
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig("missing data bar-plot.png")

plt.show()
