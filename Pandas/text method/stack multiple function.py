import pandas as pd

messy_names = pd.Series(["andrew    ", "bo;bo", "   claire"])

print(messy_names)
print(messy_names.str.replace(";", ""))
print(messy_names.str.replace(";", "").str.strip())
print(messy_names.str.replace(";", "").str.strip().str.capitalize())
