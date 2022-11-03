import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../../Files/StudentsPerformance.csv")
print(df.head())

sns.pairplot(data=df, hue="gender")

plt.savefig("File/Pair plot.png")

plt.show()
