/* -*- C -*- */
%{
#include <gsl/gsl_errno.h>
#include <gsl/gsl_rng.h>
#include <pygsl_lite/rng.h>
#include <pygsl_lite/rng_helpers.h>
%}

%include swig_init_pygsl.h
%init{
    swig_import_pygsl_rng();
}
%typemap(in) gsl_rng * IN {
     $1= (gsl_rng*) PyGSL_gsl_rng_from_pyobject($input);
     if($1 == NULL)
	  goto fail;
}
