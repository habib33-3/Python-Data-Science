import numpy as np

np.random.seed(1)
x = np.random.randint(1, 100, 11)
print(f"Original array = {x}")

print(x ** x)
print(np.sqrt(x))
print(np.log(x))
