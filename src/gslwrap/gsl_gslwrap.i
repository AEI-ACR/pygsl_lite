/* -*- C -*- */
/*
 * Author: Fabian Jakobs
 * Modified by : Pierre Schnizer January 2003, 2025
 *
 * Changes:
 *   22. May 2003: Changed to use the pygsl_lite library. Warning! Do not import
 * Numeric/arrayobject.h before pygsl_lite_block_helpers.h.  pygsl_lite_block_helpers.h
 * defines the PY_ARRAY_UNIQUE_SYMBOL.
 *
 * 2025: swig 4.3 compatible
 */
%module gslwrap
%feature ("autodoc", "3");
%include pygsl_compat.i
%include swig_init_pygsl.h

%{
#include <gsl/gsl_types.h>
#include <stdio.h>
#include <pygsl_lite/error_helpers.h>
#include <pygsl_lite/utils.h>
#include <typemaps/swig_init_pygsl.h>

static PyObject *module = NULL;

static const char _pygsl_lite_gsl_unimpl_feature[] =  "Feature not implemented in your version of GSL";
#define _PyGSL_ERROR_UNIMPL pygsl_lite_error(_pygsl_lite_gsl_unimpl_feature, __FILE__, __LINE__, GSL_EUNIMPL)
#define PyGSL_ERROR_UNIMPL      do{_PyGSL_ERROR_UNIMPL; PyGSL_ERROR_FLAG(GSL_EUNIMPL); return GSL_EUNIMPL; }while(0);
#define PyGSL_ERROR_UNIMPL_NULL do{_PyGSL_ERROR_UNIMPL; PyGSL_ERROR_FLAG(GSL_EUNIMPL); return GSL_EUNIMPL; }while(0);
%}

%init {
  swig_init_pygsl_lite();
}

typedef int size_t;

%include typemaps.i
%include gsl/gsl_types.h
%include gsl_error_typemap.i
%include gsl_block_typemaps.i
%include gsl_complex_typemap.i


%immutable;
%include gsl_math.i
%typemap (out) int = gsl_error_flag_drop;
%include interpolation.i



/* %include error.i */
/* %include complex.i */
/* %include matrix.i */
/* %include vector.i */
