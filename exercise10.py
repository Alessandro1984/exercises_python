import numpy as np

d = np.arange(1, 11, 1)
D = np.tile(d, 10).reshape(10, 10)

print(D)

print(D.sum(axis = 0))

print(D.mean(axis = 1))
