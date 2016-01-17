from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(name = 'pysxmm',
      version = '1.0',
      requires = ['numpy'],
      packages = ['bench.python'],
      ext_modules=cythonize(Extension('bench/cython', ['bench/cython/matmul.pyx']))
      )
