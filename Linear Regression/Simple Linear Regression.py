import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../Files/Advertising.csv")

print(df.head(10))
print()

df["Total_spent"] = df["TV"] + df["radio"] + df["newspaper"]

print(df.head(10))
print()
print()

figure1 = plt.figure()
sns.regplot(data=df, x=df["Total_spent"], y=df["sales"])

plt.savefig("regPlot.png")

X = df["Total_spent"]
Y = df["sales"]
BetaCoefficient = np.polyfit(X, Y, deg=1)
print(BetaCoefficient)
print()
print()

potential_spent = np.linspace(0, 500, 100)

predicted_sales = BetaCoefficient[0] * potential_spent + BetaCoefficient[1]

fig2 = plt.figure()
sns.scatterplot(data=df, x="Total_spent", y="sales")
plt.plot(potential_spent, predicted_sales, color="red")

spend = 200
predicted_sales = BetaCoefficient[0] * spend + BetaCoefficient[1]
print(predicted_sales)
plt.show()
