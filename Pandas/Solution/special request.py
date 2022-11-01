# TASK: What are the names and emails of people who made exactly 5 "Special Requests"?

import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")
print(df.columns)

special = df[df["total_of_special_requests"] == 5][["name", "email"]]
print(special)
