import pandas as pd

df = pd.read_excel("../../Files/my_excel_file.xlsx")
print(df)

wb = pd.ExcelFile("../../Files/my_excel_file.xlsx")
print(wb.sheet_names)

excel_sheet_dict = pd.read_excel("../../Files/my_excel_file.xlsx", sheet_name=None)
print(excel_sheet_dict.keys())
print(excel_sheet_dict)
print()
ndf = excel_sheet_dict["First_Sheet"]
print(ndf)

ndf.to_excel("new.xlsx")
