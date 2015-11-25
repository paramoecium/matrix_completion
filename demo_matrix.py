import numpy as np

N = 16
rank = 2
iMax = 5
X = np.dot( np.random.random_integers(iMax, size=(N, rank)), np.random.random_integers(iMax, size=(rank, N)) )
print np.linalg.matrix_rank(X)
