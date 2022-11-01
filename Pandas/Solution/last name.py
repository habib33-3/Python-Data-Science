# TASK: What are the top 5 most common last name in the dataset?
# Bonus: Can you figure this out in one line of pandas code?
# (For simplicity treat the a title such as MD as a last name,
# for example Caroline Conley MD can be said to have the last name MD)


import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")
print(df.columns)

print(df["name"].apply(lambda name: name.split()[-1]).value_counts()[:5])
