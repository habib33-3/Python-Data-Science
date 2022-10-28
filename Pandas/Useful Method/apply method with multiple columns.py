import numpy as np
import pandas as pd

df = pd.read_csv("../../Files/tips.csv")
print(df.head(10))


def quality(total_bill, tip):
    if tip / total_bill > 0.25:
        return "Generous"
    else:
        return "Other"


df["quality"] = df[["total_bill", "tip"]].apply(lambda df: quality(df["total_bill"], df["tip"]), axis=1)

print(df.head(10))

df["quality"] = np.vectorize(quality)(df["total_bill"], df["tip"])  # faster and easy
print(df.head())
