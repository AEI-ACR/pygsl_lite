"""
Simple Mathematical functions

fcmp(a, b, epsilon) -> -1, 0, 1
"""
import pygsl_lite._gslwrap
log1p = pygsl_lite._gslwrap.gsl_log1p
expm1 = pygsl_lite._gslwrap.gsl_expm1
hypot = pygsl_lite._gslwrap.gsl_hypot
acosh = pygsl_lite._gslwrap.gsl_acosh
asinh = pygsl_lite._gslwrap.gsl_asinh
atanh = pygsl_lite._gslwrap.gsl_atanh
ldexp = pygsl_lite._gslwrap.gsl_ldexp
frexp = pygsl_lite._gslwrap.gsl_frexp
fcmp  = pygsl_lite._gslwrap.gsl_fcmp
