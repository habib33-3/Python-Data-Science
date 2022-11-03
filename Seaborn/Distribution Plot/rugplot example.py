import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../../Files/dm_office_sales.csv")
print(df.head())

sns.rugplot(x="salary", data=df, height=0.5)

plt.savefig("Files/rugplot example.png")

plt.show()
