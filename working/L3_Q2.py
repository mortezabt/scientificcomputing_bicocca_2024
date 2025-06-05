import numpy as np
import matplotlib.pyplot as plt

distance = np.array([0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.06, 39.48])
period = np.array([0.24, 0.62, 1.00, 1.88, 11.86, 29.46, 84.01, 164.8, 248.09])
names = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
    "Pluto",
]


fig = plt.figure()
ax = fig.add_subplot(111)
ax.loglog(distance, period, "o", label="period")
for i, (xi, yi) in enumerate(zip(distance, period)):
    ax.text(xi, yi, names[i], fontsize=8, ha="right", va="bottom")
ax.set_xlabel("Distance [A.U.]")
ax.set_ylabel("Period [Years]")
ax.set_title("Period vs Distance")
plt.show()
