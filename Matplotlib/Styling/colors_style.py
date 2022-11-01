import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 11, 11)

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])
l = ax.plot(x, x, color="#650dbd", lw=3, ls="--")
l[0].set_dashes([5, 2, 10, 2])
ax.plot(x, x + 3, color="#956dbd", lw=1, ls=":")
ax.plot(x, x + 5, color="#956dbd", lw=1, marker="o", ls="--", ms=10)

plt.savefig("files/color_style.png")

plt.show()
