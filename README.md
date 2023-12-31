# NoiseFlow


[![Actions Status](https://github.com/shakeflow/noiseflow/actions/workflows/workflow.yml/badge.svg)](https://github.com/shakeflow/noiseflow/actions)
[![coverage](https://codecov.io/gh/shakeflow/noiseflow/branch/main/graph/badge.svg)](https://codecov.io/gh/shakeflow/noiseflow)
[![docs](https://img.shields.io/badge/docs-stable-blue.svg)](https://shakeflow.github.io/noiseflow/)
[![supported versions](https://img.shields.io/pypi/pyversions/noiseflow.svg?label=python_versions)](https://pypi.python.org/pypi/noiseflow)
[![docs](https://badge.fury.io/py/noiseflow.svg)](https://badge.fury.io/py/noiseflow)


## Prerequisites

NoiseFlow now supports `Clang` and `GCC` compiler in MacOS and Linux system separately, and all installation processes are under the `conda` environment, and we recommend to use miniconda. Make sure to install the following pre-packages before installing noiseflow:


If you use `Clang` in Mac, please install `OpenMP` via `brew` as following:

```bash
brew install openmp
```

And use `pip` and `conda` to install the following packages:

```bash
pip install joblib

conda install -c conda-forge numpy scipy matplotlib
conda install -c conda-forge obspy
conda install -c conda-forge fftw (动态库)
conda install -c conda-forge pybind11 (头文件)
conda install -c conda-forge xtensor xsimd xtl xtensor-blas xtensor-python (可能是静态库)
conda install -c conda-forge xtensor-fftw  #(usually failed at most time)
```

The `xtensor-fftw` and `KFR` need to be installed from source, first download them:


```bash
git clone https://github.com/OUCyf/noiseflow.git
cd noiseflow
git submodule init
git submodule update
```



Note the `xtensor-fftw` do not support M1 chip, and if it is failed to install via conda, you can install it from source into conda environment as `$CONDA_PREFIX`

```bash
cd ./external/xtensor-fftw
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX
make install
```



The `KFR` package is C++ DSP framework, should be installed in `./extern/kfr` from source

```bash
cd ./external/kfr
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX
make install
```




## Installation

Now you can install `NoiseFlow`. If you use `MacOS`, please make sure to use Clang as the complier

```bash
export CXX=clang++
# unset CXX
python setup.py install
```

If you use `Linux`, please use GCC as the compiler

```bash
export CXX=g++-13
python setup.py install
```


If you use `HPC` with `module` tool, you can use both Clang and GCC, for example using NOTS in Rice University.

```bash
# use gcc
module load GCC/13.1.0
export CXX=g++
python setup.py install
INCLUDE_CMAKE_EXTENSION=1 pip install .

# use clang
module load GCCcore/11.2.0
module load Clang/13.0.1
export CXX=clang++
python setup.py install
```

```bash
conda install -c conda-forge stockwell

NOISEFLOW_USE_CPP=1 pip install --no-binary :all: noiseflow --no-cache-dir

git submodule add https://gitclone.com/github.com/kfrlib/kfr.git extern/kfr
```
w


## License
Noiseflow is dual-licensed, available under both commercial and apache license.

If you want to use noiseflow in a commercial product or a closed-source project, you need to purchase a Commercial License.



`stockwell`: 'numpy>=1.18', scipy, fftw, ['cp36-*', 'cp37-*', 'cp38-*', 'cp39-*', 'cp310-*']



## INSTALL (NOETS)
- conda:



```bash
brew install fftw
conda install -c conda-forge fftw(没用)
conda install -c conda-forge pybind11 (头文件)
conda install -c conda-forge xtensor xsimd xtl xtensor-blas xtensor-python (可能是静态库)
```




```bash
cd ./external/xtensor-fftw
mkdir build && cd build

myenv = $(conda env list | grep ' \* ' | awk '{print $1}')
conda_prefix = $(conda info --base)
export CMAKE_PREFIX_PATH="${conda_prefix}/envs/${myenv}"


cmake .. -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX -DCMAKE_PREFIX_PATH=$CONDA_PREFIX
make install
```


### [build-system]
cmake = '^3.18.0'
fftw = '^3.3.10'
pybind11 = '^2.10.4'
xtensor = '^0.24.6'
xsimd = '8.0.5' # when the version is larger than 8.0.5, it will got error in compiling stage.
xtl = '^0.7.5'
xtensor_blas = '^0.20.0'
xtensor_python = '^0.26.1'
xtensor_fftw = '^0.2.6' # not show in conda env
kfr = '^5.0.2' # not show in conda env

### [optional-for-mac]
libomp = '^16.0.6' # via brew
