import os, sys

pygsl_litedir = os.path.dirname("__name__")
gsldist_path = os.path.join(pygsl_litedir, "gsl_dist")
sys.path.insert(0, gsldist_path)
from swig_extension import SWIG_Extension
from gsl_Extension import gsl_Extension


def generate_extensions(macros, swig_flags):
    """
    Define all the extensions which will be built. Note that for SWIG
    extensions this also involves running SWIG if the wrappers are
    out of date.
    """
    exts = []
    pygsl_lite_errno = gsl_Extension(
        "errno",
        ["src/init/errorno.c"],
        gsl_min_version=(1,),
        define_macros=macros,
        python_min_version=(2, 1),
    )
    exts.append(pygsl_lite_errno)
    pygsl_lite_init = gsl_Extension(
        "init",
        ["src/init/initmodule.c"],
        gsl_min_version=(1,),
        define_macros=macros,
        python_min_version=(2, 1),
    )
    exts.append(pygsl_lite_init)
    pygsl_lite_init = gsl_Extension(
        "inittest",
        ["src/init/inittestmodule.c"],
        gsl_min_version=(1,),
        define_macros=macros,
        python_min_version=(2, 1),
    )
    exts.append(pygsl_lite_init)

    exts.append(
        SWIG_Extension(
            "gslwrap",
            ["src/gslwrap/gsl_gslwrap.i"],
            swig_include_dirs=["src/gslwrap/"],
            define_macros=macros,
            python_min_version=(2, 1),
        )
    )

    exts.append(
        SWIG_Extension(
            "odeiv2",
            ["src/callback/gsl_odeiv2.i"],
            include_dirs=["src/callback"],
            swig_include_dirs=["src/callback"],
            swig_flags=swig_flags,
            define_macros=macros,
            python_min_version=(2, 1),
        )
    )

    exts.append(
        SWIG_Extension(
            "_block",
            ["src/block/gsl_block.i"],
            swig_include_dirs=["src/block"],
            define_macros=macros,
            swig_flags=swig_flags,
            python_min_version=(2, 1),
        )
    )

    pygsl_lite__callback = SWIG_Extension(
        "_callback",
        ["src/callback/gsl_callback.i"],
        include_dirs=["src/callback"],
        swig_include_dirs=["src/callback"],
        swig_flags=swig_flags,
        define_macros=macros,
        python_min_version=(2, 1),
    )
    exts.append(pygsl_lite__callback)

    errortest = gsl_Extension(
        "errortest",
        ["src/errortestmodule.c"],
        gsl_min_version=(1,),
        define_macros=macros,
        python_min_version=(2, 0),
    )
    exts.append(errortest)
    return exts
