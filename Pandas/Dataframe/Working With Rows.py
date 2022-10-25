import pandas as pd

df = pd.read_csv("Files/tips.csv")
df = df.set_index('Payment ID')

print(df)

# df=df.reset_index()
# print(df)

print(df.iloc[0])  # if index is used; single row
print(df.iloc[0:])  # if index is used; multiple rows

print(df.loc['Sun2251'])  # label or name based index;single row
print(df.loc[['Sun2251', 'Sat1709']])  # label or name based index; multiple rows
print(df.loc['Sun2251': 'Sat1709'])  # label or name based index; multiple rows
