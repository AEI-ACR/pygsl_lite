/* -*- C -*- */
/**
 * Author : Fabian Jakobs	
 */

/* Raffi Enficiaud 12.2025: this file cannot be named math.i as there is already a file
   with that name in swig, and it is included before this one otherwise.
 */
%{
#include <gsl/gsl_math.h>
%}

%ignore gsl_function_struct;
%ignore gsl_function_fdf_struct;
%ignore gsl_function_vec_struct;

#pragma SWIG nowarn=305
%include gsl/gsl_math.h
%include gsl/gsl_nan.h
%include gsl/gsl_sys.h
#pragma SWIG nowarn=+305
