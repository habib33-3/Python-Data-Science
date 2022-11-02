import matplotlib.pyplot as plt
import numpy as np

m = np.arange(0, 11)
c = 3 * 10 ** 8
E = m * c ** 2

plt.plot(E, m, color="red")
plt.title("E=mc^2")
plt.xlabel("Mass in Grams")
plt.ylabel("Energy in Joules")


plt.savefig("Files/e=mc^2.png")

plt.show()
