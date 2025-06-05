from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(-(x**2))


Iq, err = integrate.quad(f, -5, 5, epsabs=1.0e-7, epsrel=1.0e-7)
print(Iq)
print(err)
er = []
for N in range(1, 50):
    x = np.linspace(-5, 5, N)
    fs = np.exp(-(x**2))

    I = integrate.simpson(fs, x=x)
    error = I - Iq
    er.append(error)

plt.plot(er)
plt.show()
