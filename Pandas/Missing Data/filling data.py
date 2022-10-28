import pandas as pd

df = pd.read_csv("../../Files/movie_scores.csv")
print(df)

print(df.fillna("new value"))
df["pre_movie_score"] = df["pre_movie_score"].fillna(0)
print(df)
df["post_movie_score"] = df["post_movie_score"].fillna(df["post_movie_score"].mean())
print(df)
