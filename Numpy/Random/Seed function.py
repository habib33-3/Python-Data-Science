import numpy as np

print("Seed helps to create a set of random numbers")

np.random.seed(1)
print(np.random.randint(0, 30, 7))

np.random.seed(2)
print(np.random.randint(0, 30, 7))

np.random.seed(1)
print(np.random.randint(0, 30, 7))
