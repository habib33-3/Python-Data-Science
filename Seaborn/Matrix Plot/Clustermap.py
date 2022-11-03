import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../../Files/country_table.csv")
df = df.set_index("Countries")
print(df)

plt.figure(1, (10, 8))
sns.clustermap(data=df.drop("Life expectancy", axis=1), linewidths=0.5, annot=True, col_cluster=False)

plt.savefig("File/ClusterMap.png")

plt.show()
