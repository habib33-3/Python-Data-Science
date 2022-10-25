import numpy as np

x = np.arange(2, 19)

print(f"original array: {x}")

x[0:3] = 37
print(f"reassigned array : {x}")
