import numpy as np

x = np.array([[2, 4, 6, 3], [4, 6, 8, 3], [7, 5, 3, 2]])

print(f"original Array = \n{x}")

y = x[:2, 1:]

print(f"sliced array = \n{y}")
