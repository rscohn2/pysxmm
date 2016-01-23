import numpy as np
cimport numpy as np

cdef np.ndarray a
cdef np.ndarray b
cdef np.ndarray c

def setup(size=10):
    global a,b
    m = size
    n = size
    k = size
    a = np.arange(m*n, dtype=np.float64).reshape((m,n))
    b = np.arange(n*k, dtype=np.float64).reshape((n,k))

def run(count):
    cdef int i
    for i in range(count):
        c = np.dot(a,b)
