# TASK: What are the top 5 most common country codes in the dataset?

import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")
print(df.head())

count_CC = df["country"].value_counts()[:5]
print(count_CC)
