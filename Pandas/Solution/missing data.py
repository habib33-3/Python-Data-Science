# TASK: Is there any missing data? If so, which column has the most missing data?

import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")
print(df.head())

print(df.isnull().sum())
print("yes")
max_null = df["company"].isnull().sum()
print("company column has most missing missing data")
print(f"Count of missing data : {max_null}")
