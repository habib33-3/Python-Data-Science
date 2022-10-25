import numpy as np

np.random.seed(1)
x = np.random.randint(1, 100, 11)
print(f"Original array = {x}")

print(f"Sine  = {np.sin(x)}")
print(f"Cosine  = {np.cos(x)}")
print(f"Tangent  = {np.tan(x)}")
