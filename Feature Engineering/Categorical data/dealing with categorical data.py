import pandas as pd

with open("../../Files/Ames_Housing_Feature_Description.txt", "r") as f:
    print(f.read())

df = pd.read_csv("../File/no_missing_data.csv")

df["MS SubClass"] = df["MS SubClass"].apply(str)

my_object_df = df.select_dtypes(include="object")
my_numeric_df = df.select_dtypes(exclude="object")

df_object_dummies = pd.get_dummies(my_object_df, drop_first=True)
final_df = pd.concat([my_numeric_df, df_object_dummies], axis=1)

print(final_df)

final_df.to_csv("final.csv")
