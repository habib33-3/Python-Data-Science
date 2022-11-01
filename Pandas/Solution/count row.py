# TASK: How many rows are there?


import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")
print(df.head())
print(len(df))
