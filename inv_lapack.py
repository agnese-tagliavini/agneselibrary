import numpy as np
from numpy.linalg import lapack_lite

lapack_routine = lapack_lite.dgesv

# Looking one step deeper, we see that solve performs many sanity checks.  
# Stripping these, we have:

def faster_inverse(A):
    b = np.identity(A.shape[1], dtype=A.dtype)
    n_eq = A.shape[0]
    n_rhs = A.shape[1]
    pivots = np.zeros(n_eq, np.intc)
    identity  = np.eye(n_eq)
    results = lapack_lite.zgesv(n_eq, n_rhs, A, n_eq, pivots, b, n_eq, 0) 
    if results['info'] > 0:
        raise LinAlgError('Singular matrix') 
    return b

#def lapack_inverse(a):
#        b = np.copy(identity)
#        pivots = np.zeros(n_eq, np.intc)
#        results = lapack_lite.dgesv(n_eq, n_rhs, a, n_eq, pivots, b, n_eq, 0)
#        if results['info'] > 0:
#           raise LinAlgError('Singular matrix')
#        return b

#    return np.array([lapack_inverse(a) for a in A])
