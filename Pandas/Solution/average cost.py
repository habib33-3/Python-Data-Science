# TASK: What is the average total cost for a stay in the dataset?
# Not average daily cost, but total stay cost.
# (You will need to calculate total cost your self by using ADR and week day and weeknight stays).
# Feel free to round this to 2 decimal points.


import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")

df['total_night'] = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]

df["total_cost"] = df["adr"] * df["total_night"]

avg_cost = round(df["total_cost"].mean(), 2)

print(avg_cost)
