import numpy as np
import timeit

def setup(size=10):
    global a,b
    m = size
    n = size
    k = size
    a = np.arange(m*n, dtype=np.float64).reshape((m,n))
    b = np.arange(n*k, dtype=np.float64).reshape((n,k))

def run(count=10000000):
    for i in xrange(count):
        c = np.dot(a,b)
