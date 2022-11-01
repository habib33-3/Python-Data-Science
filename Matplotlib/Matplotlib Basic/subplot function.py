import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 10, 11)
b = a ** 4

x = np.arange(0, 10)
y = 2 * x

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(4, 10), dpi=200)

axes[0][0].plot(x, y)
axes[0][0].set_title("First")
axes[0][0].set_xlabel("x axis")
axes[0][0].set_ylabel("y axis")

axes[1][0].plot(x, y)
axes[1][0].set_title("Second")
axes[1][0].set_xlabel("x axis")
axes[1][0].set_ylabel("y axis")

axes[0][1].plot(a, b)
axes[0][1].set_title("Third")
axes[0][1].set_xlabel("x axis")
axes[0][1].set_ylabel("y axis")

axes[1][1].plot(a, b)
axes[1][1].set_title("Fourth")
axes[1][1].set_xlabel("x axis")
axes[1][1].set_ylabel("y axis")

fig.suptitle("Graphs", fontsize=18)

# plt.tight_layout()

fig.subplots_adjust(wspace=0.9, hspace=0.6)

plt.savefig("files/subplots_function.png")

plt.show()
