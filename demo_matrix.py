import numpy as np
from pcp import pcp
from util import *
n = 500
r = 0.05*n
k = 0.05*(n**2)
M = np.empty([n, n])
with Timer('Creating matrix ...'):
    L0 = np.dot( np.random.normal(0.0, 1.0/n, size=(n, r)), np.random.normal(0.0, 1.0/n, size=(r, n)) )
    P_omg = np.zeros(L0.size)
    P_omg[np.random.choice(L0.size, k, False)] = 1
    S0 = np.random.choice([1, -1], size=(n, n))*np.random.randint(2, size=(n, n))
    M = L0 + S0
print "rank(L0) =", np.linalg.matrix_rank(L0)
print "||S0||_0 =", np.count_nonzero(S0)
with Timer('Principal Component Pursuit ...'):
    L, S, (u, s, v) = pcp(M, maxiter=50, verbose=True, svd_method="exact")

