import pandas as pd

df = pd.read_csv("../../Files/tips.csv")
print(df)


def last_four(num):
    return int(str(num)[-4:])


df["last_four"] = df['CC Number'].apply(last_four)
print(df)


def yelp(price):
    if price < 10:
        return '$'
    elif 10 <= price <= 30:
        return '$$'
    else:
        return '$$$'


df['yelp'] = df["total_bill"].apply(yelp)
print(df)