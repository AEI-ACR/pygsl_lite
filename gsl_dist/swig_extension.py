#!/usr/bin/env python
"""Currently no control when SWIG will be run.
"""
from gsl_Extension import gsl_Extension, gsl_Location
from distutils.util import spawn
from distutils.dep_util import newer_group
from distutils.file_util import copy_file

import os.path
import sys
import re
import string
remove_underscore=re.compile("_*(.*)")

gsl_include_dir = gsl_Location.get_gsl_prefix() + '/include'
swig_flags_default = ['-python', '-keyword', '-shadow', '-Itypemaps',
              # faster wrappers ... requires python 2.5 or greater
              #'-builtin',
              #'-cpperraswarn',
              '-I' + gsl_include_dir]
swig_flags = ['-python', '-builtin', '-modern', '-keyword', '-O', '-Itypemaps', #'-cpperraswarn',
              '-I' + gsl_include_dir]


class SWIG_Extension(gsl_Extension):
    def __init__(self, name, sources,
                 include_dirs=None,
                 define_macros=None,
                 undef_macros=None,
                 library_dirs=None,
                 libraries=None,
                 runtime_library_dirs=None,
                 extra_objects=None,
                 extra_compile_args=None,
                 extra_link_args=None,
                 export_symbols=None,
                 gsl_prefix=None,
                 gsl_min_version=None,
                 python_min_version=None,
                 swig_include_dirs=[],
                 swig_dependencies=[],
                 swig_flags=[],
                 c_dir="swig_src",
                 py_dir="pygsl_lite"
                 ):



        # Make the target of the swig wrapper out of the name and the c_dir
        target = name + "_wrap.c"

        # In the old makefile the leading underscore was not taken into account.
        # I will stick to that.

        m = remove_underscore.match(target)
        if len(m.groups()) >= 1:
            target = m.groups()[0]
        if c_dir:
            target = c_dir + "/" + target

        self._run_swig(sources, swig_dependencies, target, swig_include_dirs, swig_flags, py_dir, c_dir, name)

        # SWIG generates two files. A py proxy file and a .so. The so appends a _ to the module name.
        gsl_Extension.__init__(self, '_' + name, [target,],
                               include_dirs,
                               define_macros,
                               undef_macros,
                               library_dirs,
                               libraries,
                               runtime_library_dirs,
                               extra_objects,
                               extra_compile_args,
                               extra_link_args,
                               export_symbols,
                               gsl_prefix,
                               gsl_min_version,
                               python_min_version)
        return

    def _run_swig(self, sources, swig_dependencies, target, swig_include_dirs, swig_flags, py_dir, c_dir, name):
        """
        If the SWIG sources need to be regenerated, do so.
        """
        if newer_group(sources + swig_dependencies, target):
            includes = [f'-I{i}' for i in swig_include_dirs]
            t_swig_flags = swig_flags_default + swig_flags
            cmd = [gsl_Location.get_swig(),] + t_swig_flags + includes
            cmd.extend(['-o', target] + sources)
            sys.stderr.write(" ".join(cmd) + "\n")
            spawn(cmd, 1, 1)
            src = f"{name}.py"
            if c_dir:
                src = os.path.join(c_dir,src)
            dst = "."
            if py_dir:
                dst = py_dir
            copy_file(src, dst)

class SWIG_Extension_Nop(SWIG_Extension):
    """
    Do not build swig
    """
    def _run_swig(self, sources, swig_dependencies, target, swig_include_dirs, py_dir, c_dir, name):
        pass
