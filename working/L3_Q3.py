import numpy as np
import matplotlib.pyplot as plt

theta = np.array(np.linspace(0, 2 * np.pi, 100))


def draw_circle(x0, y0, R, color):
    x = R * np.cos(theta) + x0
    y = R * np.sin(theta) + y0

    ax.fill(x, y, color=color)


fig = plt.figure()
ax = fig.add_subplot()
for i in range(100, 110):
    draw_circle(i, i, 0.5, "red")


plt.show()
