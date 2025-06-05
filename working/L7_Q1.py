# import multiprocessing, pathos.multiprocessing
# import numpy as np
# import time
# print(multiprocessing.cpu_count())

# CPUS = 20
# parmap = pathos.multiprocessing.ProcessingPool(CPUS)


# a = np.random.normal(100, 1000, int(1e7))
# b = np.random.normal(10,100, int(1e7))

# def addition(x,y):

#     return  x * y 
# s = time.time()
# my = list(parmap.imap(addition, a,b))
# e = time.time()

# print(e - s)


import multiprocessing
import pathos.multiprocessing
import numpy as np
import time

def addition(x,y):
    # x, y = pair  # Unpack the pair
    return x * y

if __name__ == "__main__":
    print("Available CPUs:", multiprocessing.cpu_count())

    # Number of CPUs to use
    CPUS = 20
    parmap = pathos.multiprocessing.ProcessingPool(CPUS).imap

    # Generate random data
    a = np.random.normal(100, 1000, int(1e7))
    b = np.random.normal(10, 100, int(1e7))

    # Prepare the data as a list of pairs
    data = zip(a, b)  # Use zip directly to save memory

    # Measure execution time
    s = time.time()
    result = list(parmap(addition, a,b))  # Pass the zipped data
    e = time.time()

    print(f"Time taken: {e - s:.2f} seconds")
