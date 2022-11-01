# TASK: What are the top 3 most common area code in the phone numbers? (Area code is first 3 digits)


import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")
print(df.columns)

area_code = df["phone-number"].apply(lambda num: num[:3])
area_code_count = area_code.value_counts()[:3]
print(area_code_count)

