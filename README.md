# pysxmm
Python small matrix multiply

# installing numpy in my home directory
    python setup.py install --user

# running cython
python -c 'import bench.cython; bench.cython.run()'

# running python
python -c 'import bench.python; bench.python.run()'

# base environment checkout numpy and install in virtualenv
virtualenv ~/venvs/base
source ~/venvs/base/bin/activate
python setup.py install

# nogil numpy won't release gil while doing blas
virtualenv ~/venvs/nogil
source ~/venvs/nogil/bin/activate
git checkout fast
python setup.py install
