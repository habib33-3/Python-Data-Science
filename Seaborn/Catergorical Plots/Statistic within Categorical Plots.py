import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("../../Files/dm_office_sales.csv")
print(df.head())

print(df["division"].value_counts())

figure1 = plt.figure(figsize=(10, 4))
sns.countplot(data=df, x="level of education", hue="division")

figure2 = plt.figure(figsize=(10, 4))
sns.barplot(data=df, x="level of education", y="salary", estimator=np.mean, errorbar="sd", hue="division")

figure1.savefig("Files/count_plot.png")
figure2.savefig("Files/bar_plot.png")

plt.show()
