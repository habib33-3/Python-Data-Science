import numpy as np

np.random.seed(1)
x = np.random.randint(1, 60, 25).reshape(5, 5)
print(f"Original Matrix = \n{x}")

print(f"Sum of a axis = {x.sum(axis=0)}")
print(f"Mean of a axis = {x.mean(axis=0)}")
print(f"Variance of a axis = {x.var(axis=0)}")
print(f"Standard Deviation of a axis = {x.std(axis=0)}")
