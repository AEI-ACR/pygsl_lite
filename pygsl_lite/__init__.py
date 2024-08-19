# Adapted by Sergei Ossokine from `pygsl`
# Original
# author: Achim Gaedke
# created: May 2001
# file: pygsl_lite/__init__.py
# $Id$
"""Wrapper for the GNU Scientific Library.

This module provides the following submodules:

    * interpolation
    * math
    * odeiv
    * roots


Homepage: https://github.com/pygsl_lite/pygsl_lite


"""

import sys

# Central Module used by errors. Make sure it loads. Should not depend on init
import pygsl_lite.errno

# Central Module used by C callbacks. So a good idea to import it here to be
# sure that  it exists from the very beginning!
# Should not depend on :mod:`pygsl_lite.iniit`
import pygsl_lite.errors

_init_import_errm ="""
Did you try to import pygsl_lite in the build directory?

Well, that does not work out of the box. If you want to do that, please
use
      python setup.py build_ext -i
to add the necessary extension module in the local pygsl_lite/ directory!

Please read the README first! Any further questions or missing information
please report on https://github.com/pygsl_lite/pygsl_lite!
"""


__test = 0
try:
    import pygsl_lite.init
    __test = 1
finally:
    if __test == 0:
        sys.stderr.write(_init_import_errm)

try:
    from ._version import version as version
except ModuleNotFoundError:
    version = ""



# And register all the errors
pygsl_lite.init.register_exceptions(*(pygsl_lite.errors.get_exceptions()))
pygsl_lite.init.register_warnings(*(pygsl_lite.errors.get_warnings()))


if sys.version_info[0] < 3:
    from exceptions import Warning

# The gsl version which was used when this module was compiled.
compiled_gsl_version = pygsl_lite.init.compiled_gsl_version

# The gsl version which is used  now
run_gsl_version = pygsl_lite.init.run_gsl_version

# The compile date
compile_date = pygsl_lite.init.compile_date

from . import _numobj
from . import errno


__all__=['interpolation','linalg',
         'math','odeiv', 'roots',
         'spline']




get_typecode_numpy = lambda x: x.dtype
get_typecode_default = lambda x: x.typecode()

if _numobj.nummodule == "numpy":
    get_typecode = get_typecode_numpy
else:
    get_typecode = get_typecode_default



try:
    Int =  _numobj.Int
except  AttributeError:
    # For numpy
    Int = _numobj.int64

try:
    Float = _numobj.Float
except  AttributeError:
    # For numpy
    Float = _numobj.float64

try:
    Complex = _numobj.Complex
except  AttributeError:
    # For numpy
    Complex = _numobj.complex128

try:
    ArrayType = _numobj.ArrayType
except AttributeError:
    # For numpy 1.0
    ArrayType = _numobj.ndarray

def array_typed_copy(array, code = None):
    """
    Return a new copy for the array
    """
    if code == None:
        code = get_typecode(array)
    return array.astype(code)

#import pygsl_lite._mlab
def get_debug_level():
    """Get the debug level

    See :func:`pygsl_lite.set_debug_level` for details.
    """
    return pygsl_lite.init.get_debug_level()

def set_debug_level(level):
    """Allows to set the debug level if implemented in the init function.

    Args:
         level:   A level of 0 deactivates all messages. The higher the
                  level gets the more messages are printed.

    Silently ignores this function if the functionality was not compiled into
    pygsl_lite during build time.

    These messages are compiled into the modules written in C. The level is
    stored as a c variable in the module level for each module. This can be
    useful to find the reason why PyGSL crashes during execution.
    """
    try:
        pygsl_lite.init.set_debug_level(level)
    except pygsl_lite.errors.gsl_NotImplementedError:
        #print "Switchable debug information was not compiled in!"
        pass

#
add_c_traceback_frames = init.add_c_traceback_frames

def import_all():
    """Import all functions of all

    PyGSL does not import all modules on statup. If you need it
    e.g for autocompletion call this function!
    """
    for i in __all__:
        name = "pygsl_lite." + i
        try:
            __import__(name, globals(), locals(), [])
        except ImportError:
            sys.stderr.write("Import of %s failed!" % (name,))

def _zeros_default(dimensions, array):
    """Generate zeros of the same type as the array
    """
    return _zeros(dimensions, array.typecode())

def _zeros_numpy(dimensions, array):
    """ Generate zeros of the same type as the array
    """
    return _zeros(dimensions, array.dtype)

if pygsl_lite._numobj.nummodule == "numpy":
    zeros = _zeros_numpy
else:
    zeros = _zeros_default
_zeros = pygsl_lite._numobj.zeros

if compiled_gsl_version != run_gsl_version:
    txt = """This pygsl_lite module was compiled for GSL version %s but it
is used with version %s!"""
    raise Warning(txt % (compiled_gsl_version, run_gsl_version))
