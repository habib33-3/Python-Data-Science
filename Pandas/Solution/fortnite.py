# TASK: How many arrivals took place between the 1st and the 15th of the month (inclusive of 1 and 15) ?
# Bonus: Can you do this in one line of pandas code?

import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")
print(df.columns)

print(df["arrival_date_day_of_month"].apply(lambda day: day in range(1, 16)).sum())
