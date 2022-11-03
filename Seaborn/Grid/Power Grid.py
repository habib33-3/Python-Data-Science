import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../../Files/StudentsPerformance.csv")
print(df.head())

g = sns.PairGrid(df, hue="gender")
g = g.map_upper(sns.scatterplot)
g = g.map_diag(sns.kdeplot)
g = g.map_lower(sns.kdeplot)

g = g.add_legend()

plt.savefig("File/Power Grid.png")

plt.show()
