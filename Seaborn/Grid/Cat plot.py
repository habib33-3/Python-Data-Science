import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../../Files/StudentsPerformance.csv")
print(df.head())

sns.catplot(data=df, x="gender", y="math score", kind="box", col="lunch", row="test preparation course")

plt.savefig("File/Cat Plot.png")

plt.show()
