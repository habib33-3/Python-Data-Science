import pandas as pd

df = pd.read_csv("../../Files/movie_scores.csv")
print(df)
print(df.isnull())
print(df.notnull())
print(df["pre_movie_score"].notnull())
print(df[df["pre_movie_score"].notnull()])
print(df[df["pre_movie_score"].isnull()])
print(df[(df["pre_movie_score"].isnull()) & (df["first_name"].notnull())])
