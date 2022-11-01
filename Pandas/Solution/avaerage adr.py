# TASK: The adr is the average daily rate for a person's stay at the hotel.
# What is the mean adr across all the hotel stays in the dataset?

import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")
print(df.head(10))

avg_adr = df["adr"].mean()

print(avg_adr)
