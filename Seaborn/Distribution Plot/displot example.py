import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../../Files/dm_office_sales.csv")
print(df.head())

sns.set(style="darkgrid")
sns.displot(data=df, x="salary", bins=20, kde=True, rug=True)

plt.savefig("Files/displot example.png")

plt.show()
