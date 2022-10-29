import pandas as pd

df = pd.read_csv("../../Files/Sales_Funnel_CRM.csv")
print(df)

licenses = df[["Company", "Product", "Licenses"]]
print(licenses)
print(pd.pivot(data=licenses, index="Company", columns="Product", values="Licenses"))

print(pd.pivot_table(df, index="Company", aggfunc="sum", values=["Licenses", "Sale Price"]))

print(pd.pivot_table(df, index=["Account Manager", "Contact"], values=["Sale Price"], aggfunc="sum"))
print(
    pd.pivot_table(df, index=["Account Manager", "Contact"], values=["Sale Price"], columns=["Product"], aggfunc="sum",
                   fill_value=0))
