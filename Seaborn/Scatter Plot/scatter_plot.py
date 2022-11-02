import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../../Files/dm_office_sales.csv")
print(df.head())

plt.figure(figsize=(12, 4))
sns.scatterplot(x="salary", y="sales", data=df, hue="level of education", palette="Dark2", size="work experience")

plt.savefig("Files/Scatter_plot.png")

plt.show()
