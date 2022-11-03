import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

np.random.seed(1)
ages = np.random.randint(0, 100, 200)
print(ages)

ages = pd.DataFrame(data=ages, columns=["age"])
print(ages)

Figure1 = plt.figure()
sns.rugplot(data=ages, x="age")

Figure2 = plt.figure()
sns.displot(data=ages, x="age", rug=True, bins=20, kde=True)

Figure3 = plt.figure()
sns.kdeplot(data=ages, x="age", fill=True)

Figure1.savefig("Files/kde example(rugplot).png")
Figure2.savefig("Files/kde example(displot).png")
Figure3.savefig("Files/kde example(kde).png")

plt.show()
