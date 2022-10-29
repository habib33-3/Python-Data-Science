import pandas as pd

style_date = "12--Dec--2000"
print(pd.to_datetime(style_date, format="%d--%b--%Y"))

custom_date = "12th of Nov 2002"
print(pd.to_datetime(custom_date))
