import numpy as np

# Set dimensions of the universe
Nx = 20
Ny = 20
# Set initial cells
c1 = (1, 2)
c2 = (2, 3)
c3 = (2, 2)
c4 = [10, 5]
c5 = [10, 6]
c6 = [11, 6]

field = np.zeros((Nx, Ny))
field[c1, c2] = 1
field[c3, c4] = 1


for row in field:
    for el in row:
        if el == 1:
            index = np.where(field == el)
            print(index[1])

# print(field)
