/***************************************************************************
 * Copyright (c) Fu Yin                                                     *
 *                                                                          *
 * Distributed under the terms of the Apache-2.0 License.                   *
 *                                                                          *
 * The full license is in the file LICENSE, distributed with this software. *
 ****************************************************************************/

#ifndef UTILS_HPP
#define UTILS_HPP

#ifdef _OPENMP
#include <omp.h>
#endif

#include <iostream>
#include <string>
#include <vector>
#include <chrono>
#include <exception>

#include <kfr/base.hpp>
#include <kfr/dsp.hpp>

#include <xtensor/xarray.hpp>
#include <xtensor/xtensor.hpp>
#include <xtensor/xbuilder.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xmath.hpp>
#include <xtensor/xcomplex.hpp>
#include <xtensor/xmanipulation.hpp>
#include <xtensor/xadapt.hpp>
#include <xtensor/xsort.hpp>
#include <xtensor/xoperation.hpp>
#include <xtensor/xindex_view.hpp>
#include <xtensor-blas/xlinalg.hpp>
#include <xtensor-python/pyarray.hpp>
#include <xtensor-python/pytensor.hpp>



#endif