import numpy as np


""" A"""
lst0 = list(range(15))
k = 0
for i in range(5):
    for j in range(3):
        lst0[k] = (i + 1) + j * 5
        k += 1

array = np.array(lst0).reshape(5, 3)
print(array)

new_array = array[[1, 3], :]
print(new_array)


""" B """

# Type in arbitrary array dimension
Nx = 8
Ny = 12

array_mid = np.zeros((Nx, Ny))
array_mid[:,[0, -1]] = 1
array_mid[[0, -1],:] = 1
print(array_mid)
