import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 11, 11)

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, x, label="X vs X")
ax.plot(x, x ** 2, label="X vs X^2")

plt.savefig("files/add_legend.png")

ax.legend(loc=0)

plt.show()
