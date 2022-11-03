import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../../Files/StudentsPerformance.csv")
print(df.head())

fig1 = plt.figure(1, (10, 6))
sns.jointplot(data=df, x="math score", y="reading score", kind="scatter", hue="gender")

fig1.savefig("File/Joint Plot.png")

plt.show()
