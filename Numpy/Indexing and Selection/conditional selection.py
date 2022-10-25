import numpy as np

np.random.seed(1)
x = np.random.randint(1, 111, 10)
print(f"original array = \n {x}")
print(x > 50)
print(x[x > 60])
