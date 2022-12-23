import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def create_age(mu=50, sigma=13, num_samples=100, seed=42):
    np.random.seed(seed)

    sample_ages = np.random.normal(loc=mu, scale=sigma, size=num_samples)
    sample_ages = np.round(sample_ages, decimals=0)

    return sample_ages


sample = create_age()

print(sample)

plt.figure(1)
sns.boxplot(sample)
plt.savefig("boxplot 1")

ser = pd.Series(sample)
print(ser.describe())

q75, q25 = np.percentile(sample, [75, 25])
iqr = q75 - q25

lower_limit = q25 - 1.5 * iqr
print(f"lower limit={lower_limit}")

plt.show()
