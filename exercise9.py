import numpy as np

M = np.eye(5, dtype = "int")

M[3:, 0:2] = 2

M[0:2, 3:] = 3

print(M)
