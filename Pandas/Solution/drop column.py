# TASK: Drop the "company" column from the dataset.

import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")
print(df.head())

df = df.drop("company", axis=1)
