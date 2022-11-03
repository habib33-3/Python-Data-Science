import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../../Files/StudentsPerformance.csv")
print(df.head())

fig1 = plt.figure(1, (10, 4))
sns.boxplot(data=df, y="reading score", x="parental level of education", hue="test preparation course")

fig2 = plt.figure(2, (10, 4))
sns.violinplot(data=df, x="reading score", y="parental level of education", split=True,
               inner="stick")

fig3 = plt.figure(3, (10, 4))
sns.swarmplot(data=df, x="math score", size=2, hue="test preparation course", dodge=True)

fig4 = plt.figure(4, (10, 4))
sns.boxenplot(data=df, x="math score", y="test preparation course", hue="gender")

fig1.savefig("Files/BoxPlot.png")
fig2.savefig("Files/ViolinPlot.png")
fig3.savefig("Files/SwarmPlot.png")
fig4.savefig("Files/BoxenPlot.png")

plt.show()
