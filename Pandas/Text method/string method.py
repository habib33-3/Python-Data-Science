import pandas as pd

names = pd.Series(["andrew", "bobo", "claire", "5"])

print(names)
print(names.str.upper())
print(names.str.isdigit())
