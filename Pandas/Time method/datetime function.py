from datetime import datetime

import pandas as pd

my_year = 2022
my_month = 1
my_day = 1
my_hour = 2
my_min = 30
my_sec = 15

my_date = datetime(my_year, my_month, my_day)

print(my_date)

my_date = datetime(my_year, my_month, my_day, my_hour, my_min, my_sec)
print(my_date)

my_ser = pd.Series(["Nov 3, 1990", "2000-01-01", None])
print(my_ser)

t = pd.to_datetime(my_ser)
print(t)
print(t[0].year)

obvious_euro_date = "31-12-1990"
print(pd.to_datetime(obvious_euro_date, dayfirst=True))

euro_date = "10-12-2000"
print(pd.to_datetime(euro_date, dayfirst=True))


