# TASK: What is the name of the person who paid the highest ADR (average daily rate)? How much was their ADR?

import pandas as pd

df = pd.read_csv("../../Files/hotel_booking_data.csv")
print(df.head())
print(df.info())
MaxADR = df.iloc[df["adr"].idxmax()]
print(MaxADR)
