import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 10, 11)
b = a ** 4

print(a)
print(b)

x = np.arange(0, 10)
y = 2 * x

print(x)
print(y)

fig = plt.figure()
axes1 = fig.add_axes([0, 0, 1, 1])  # first 2 digits represent coordinates,rest are height and width
axes1.plot(a, b)
axes1.set_title("large figure")
axes1.set_xlabel("x axis")
axes1.set_ylabel("y axis")

axes2 = fig.add_axes([0.2, 0.5, 0.25, 0.25])
axes2.plot(x, y)
axes2.set_title("small figure")
axes2.set_xlabel("x axis")
axes2.set_ylabel("y axis")

plt.savefig("files/figure_object.png")

plt.show()
