from scipy import integrate, signal
import numpy as np
import matplotlib.pyplot as plt


def fdata(x, L):
    A = L / 10.0
    return (
        2 * np.sin(2 * np.pi * x / L)
        + x * (L - x) ** 2 / L**3 * np.cos(x)
        + 5 * x * (L - x) / L**2
        + A / 2
        + 0.1 * A * np.sin(13 * np.pi * x / L)
    )


N = 2048
L = 50.0
x = np.linspace(0, L, N, endpoint=False)
orig = fdata(x, L)
noisy = orig + 0.5 * np.random.randn(N)
plt.figure()
plt.plot(x, noisy)
plt.plot(x, orig)


gau = signal.windows.gaussian(50, 8, sym=True)
# plt.plot(gau)

con = signal.convolve(noisy, gau)
con = 6 * con / 100
plt.figure()
plt.plot(con)
plt.show()
