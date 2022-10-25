import numpy as np

x = np.arange(0, 17)
print(f"original array: {x}")

sliced_array = x[0:5]

print(f"Sliced array: {sliced_array}")

sliced_array[:] = 77
print(f"reassigned sliced array = {sliced_array}")
print(f"updated version of original array = {x}")
