import pandas as pd
import numpy as np

df = pd.read_csv("../../Files/tips.csv")
print(df)


print(df['total_bill'])

col = ['total_bill', 'tip']
print(df[col])

df["tip_percentage"] = np.round(100 * df['tip'] / df['total_bill'],2)
df['price_per_person'] = np.round(df['total_bill'] / df['size'])

print(df.head())


