###################################################################  
#   Optimization Parameters
################################################################### 
cmake_minimum_required(VERSION 3.18)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "-Wall -g -fPIC -O3")
set(CMAKE_PREFIX_PATH $ENV{CONDA_PREFIX}) # set conda env path, so that cmake can find some libraries in conda env



###################################################################  
#   Project Info & Compiler Detection
###################################################################  
project(noiseflow_share VERSION 0.1.0 LANGUAGES CXX)
message("Check C++ compiler: ${CMAKE_CXX_COMPILER_ID}")
if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    if (MINGW)
        message("Using MinGW-w64")
        set(COMPILER "MinGW-w64")
    else()
        message("Using GCC")
        set(COMPILER "GCC")
    endif()
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
    message("Using Clang")
    set(COMPILER "Clang")
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "AppleClang")
    message("Using AppleClang")
    set(COMPILER "AppleClang")
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
    message("Using MSVC")
    set(COMPILER "MSVC")
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Intel")
    message("Using Intel Compiler")
    set(COMPILER "Intel")
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "IntelLLVM")
    message("Using Intel oneAPI Compiler")
    set(COMPILER "Intel oneAPI")
else()
    message(FATAL_ERROR "Unrecognized compiler: ${CMAKE_CXX_COMPILER_ID}")
endif()



###################################################################  
#   Find Libraries
###################################################################  
### Numpy
find_package(Python REQUIRED COMPONENTS Interpreter Development NumPy)


### OpenMP, check if the LLVM_OPENMP environment variable is set (clang doesn't bring openmp, you need to install it by conda, and find_package can't find it sometimes, you need to set the PATH as below.
if(DEFINED ENV{LLVM_OPENMP} AND "$ENV{LLVM_OPENMP}" STREQUAL "1")
    message(STATUS "Searching for OpenMP in conda path")
    set(CONDA_PREFIX $ENV{CONDA_PREFIX})
    set(OpenMP_CXX_FLAGS "-Xpreprocessor -fopenmp -I${CONDA_PREFIX}/include")
    set(OpenMP_CXX_LIB_NAMES "omp")
    set(OpenMP_omp_LIBRARY "${CONDA_PREFIX}/lib")
    find_package(OpenMP REQUIRED)
else()
    message(STATUS "Searching for OpenMP in default path")
    find_package(OpenMP REQUIRED)
endif()


### pybind11 xtensor xtl xtensor-blas xtensor-python
find_package(pybind11 REQUIRED CONFIG)
find_package(xtensor REQUIRED)
find_package(xtl REQUIRED)
find_package(xtensor-blas REQUIRED)
find_package(xtensor-python REQUIRED)


### xtensor-fftw
set(FFTW_USE_FLOAT ON CACHE BOOL "Use float precision") # set fftw to use float precision
set(FFTW_USE_DOUBLE ON CACHE BOOL "Use double precision") # set fftw to use double precision
set(FFTW_USE_LONG_DOUBLE OFF CACHE BOOL "Use long double precision") # set fftw to not use long double precision
include_directories("./extern/xtensor-fftw/include")


### FFTW using FindFFTW.cmake (note this command will seach some default path to find fftw, for example the conda env path)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/extern/xtensor-fftw/cmake/Modules/findFFTW") # use FindFFTW.cmake to find fftw
find_package(FFTW REQUIRED COMPONENTS ${REQUIRE_FLOAT_LIB} ${REQUIRE_DOUBLE_LIB} ${REQUIRE_LONG_DOUBLE_LIB})
if(FFTW_FOUND)
    message(STATUS "FFTW Found!")
endif()


### KFR 
include_directories("./extern/kfr/include")



###################################################################  
#   Target -- Python Package Module
################################################################### 
pybind11_add_module(cc_share ${CMAKE_SOURCE_DIR}/noiseflow/cc/src/pybind11.cpp)
target_include_directories(cc_share PRIVATE ${CMAKE_SOURCE_DIR}/noiseflow/cc/src ${CMAKE_SOURCE_DIR}/noiseflow/cc/include)
target_link_libraries(cc_share PUBLIC ${BLAS_LIBRARIES} ${LAPACK_LIBRARIES} ${FFTW_LIBRARIES} pybind11::module xtensor xtensor::optimize xtensor-blas xtensor-python Python::NumPy OpenMP::OpenMP_CXX) 


pybind11_add_module(signal_share ${CMAKE_SOURCE_DIR}/noiseflow/signal/src/pybind11.cpp)
target_include_directories(signal_share PRIVATE ${CMAKE_SOURCE_DIR}/noiseflow/signal/src ${CMAKE_SOURCE_DIR}/noiseflow/signal/include)
target_link_libraries(signal_share PUBLIC ${BLAS_LIBRARIES} ${LAPACK_LIBRARIES} ${FFTW_LIBRARIES} pybind11::module xtensor xtensor::optimize xtensor-blas xtensor-python Python::NumPy OpenMP::OpenMP_CXX)
