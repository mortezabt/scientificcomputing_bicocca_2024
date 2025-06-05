import numpy as np



file = np.loadtxt(
    r"L2\sample.txt"
)
file_mod = file[:, 1]
print(file_mod)
hist, bin_edges = np.histogram(file_mod)

print("Bin Counts:", hist)
print("Bin Edges:", bin_edges)

for i in range(len(bin_edges) - 1):
    ave = np.mean([bin_edges[i], bin_edges[i + 1]])

    count = hist[i]

    print(f"For average {ave}, count is {count}")
