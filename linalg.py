import numpy as np

a = [[1, 0, 0], [1, 1, 0]]
b = [[1, 1], [0, 1], [0, 0]]

c = np.dot(a, b)

d = [[1, -1], [2, 0]]

print(np.dot(-1, d))