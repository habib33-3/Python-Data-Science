import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10)
y = 2 * x
print(x)
print(y)

plt.plot(x, y)
plt.title("Graph")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.savefig("files/plot_function.png")  # always use plt.savefig() function before plt.show() or plt.close()
plt.show()
