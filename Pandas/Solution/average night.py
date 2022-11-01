# TASK: What is the average (mean) number of nights for a stay across the entire data set?
# Feel free to round this to 2 decimal points.

import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")

df['total_night'] = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]
avg_night = round(df["total_night"].mean(), 2)
print(df.columns)

print(avg_night)
