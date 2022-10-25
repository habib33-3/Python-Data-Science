import numpy as np

np.random.seed(1)
x = np.random.randint(1, 100, 11)
print(f"Original array = {x}")

print(x + x)
print(x - x)
print(x * x)
print(x / 2)
print(x / 0)
print(x % 9)
