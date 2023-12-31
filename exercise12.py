import numpy as np

M = np.array([3, 2, 1, 4]).reshape(2, 2)
print(M)

M_inv = np.linalg.inv(M)
print(M_inv)

print(np.matmul(M_inv, M))
