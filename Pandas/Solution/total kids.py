# TASK: What are the names of the people who had booked the most number children and babies for their stay?
# (Don't worry if they canceled, only consider number of people reported at the time of their reservation)

import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")
print(df.columns)

df["total_kids"] = df["babies"] + df["children"]

max_kids = df.sort_values("total_kids", ascending=False)[["name", "total_kids", "babies", "children"]][:3]

print(max_kids)
