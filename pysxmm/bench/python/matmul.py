import numpy as np
m = 8
n = 10
k = 5
a = np.arange(m*n, dtype=np.float64).reshape((m,n))
b = np.arange(n*k, dtype=np.float64).reshape((n,k))
matmuls = 10000000

def run():
    print 'Start'
    for i in xrange(matmuls):
        c = np.dot(a,b)
    print 'Done'
