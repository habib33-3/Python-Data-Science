# TASK: What percentage of hotel stays were classified as "repeat guests"?
# (Do not base this off the name of the person, but instead of the is_repeated_guest column)

import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")
print(df.columns)
total = sum(df["is_repeated_guest"] == 1)
perc = round(100 * (total / len(df)), 2)
print(perc)
