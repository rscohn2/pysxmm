import numpy as np
cimport numpy as np
cdef int m = 20
cdef int n = 20
cdef int k = 20
cdef np.ndarray a = np.arange(m*n, dtype=np.float64).reshape((m,n))
cdef np.ndarray b = np.arange(n*k, dtype=np.float64).reshape((n,k))
cdef int matmuls = 10000000
d = np.dot

def run():
    print 'Start'
    cdef int i
    for i in range(matmuls):
        c = d(a,b)
    print 'Done'
