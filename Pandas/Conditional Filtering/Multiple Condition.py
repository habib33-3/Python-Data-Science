import pandas as pd

df = pd.read_csv("../../Files/tips.csv")
print(df)

print(df[(df['total_bill'] > 30) & (df['sex'] == "Male")])  # AND operation;both are true
print(df[(df['total_bill'] > 30) | (df['sex'] == "Male")])  # OR operation;one of them is true

print(df[df['day'].isin(['Sat', 'Sun'])])
