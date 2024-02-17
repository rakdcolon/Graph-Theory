import numpy as np
from numpy.linalg import matrix_power

m = 3

A = np.zeros((m,m))

for r in range(0,m):
    for c in range(0,m):
        if r is c: continue
        A[r][c] = 1.0/(m-1)

print(A)
print()

k = 20
print(matrix_power(A,k))

b = np.ones((m,1))

print(np.linalg.solve(A, b))


