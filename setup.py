#!/usr/bin/env python3
#
# 2023  Sergei Ossokine
# file: pygsl_lite/setup.py
# $Id$
# setup script for building and installing pygsl_lite. Adapted from `pygsl`.
# Original credits
# author: Achim Gaedke, Pierre Schnizer
# created: May 2001
# modified: over the years, 2017

# Use SWIG to generate the appropriate wrapper files. This is only necessary
# if you modified any interface file as the wrapper files are included in the
# distribution
USE_SWIG = 1

# Some modules have been reimplemented. These modules will be installed in
# pygsl_lite.testing...
# Set to one if you want them built
BUILD_TESTING = 1



## Which gsl error handler to install?
# set the error handler to off: only the integer return value will be available
# This is the safest version. But then information useful to the user could be
# lost.

# Use the store version of the error handler: when GSL calls the error handler
# the information passed (which file, at which line, which reason) are stored
# at a static location. This information is then used for functions which
# return a status. When a non success status is turned in a python exception
# the stored information is used to add this to the exception.
# If more than one thread is running it could happen that the wrong information
# is returned. Only the type of exception is then correct.
GSL_ERROR_HANDLER = 1

#####
# PyGSL comes with a lot of debug information. This can be either disabled
# setting DEBUG_LEVEL to 0 at compile time, swtiched on and off at run time
# using pygsl_lite.set_debug_level(level) setting DEBUG_LEVEL to 0 or set to some
# value during compile time using a level bigger than 1 (the heigher the value
# is the more verbose the output gets. Please note that pygsl_lite needs to be
# completly rebuild if you hcange this parameter
# No debug information
# DEBUG_LEVEL = 0
# dynamic debug information
DEBUG_LEVEL = 1
# Compile time set debug level
# DEBUG_LEVEL = 10
#####


import sys

# Add the gsldist path
import os

pygsl_litedir = os.path.dirname("__name__")


# Make sure that we use the new one ...
gsldist_path = os.path.join(pygsl_litedir, "gsl_dist")
sys.path.insert(0, gsldist_path)
sys.path.insert(0,pygsl_litedir)

from setuptools import setup

from gsl_packages import generate_extensions



swig_flags = ["-builtin", "-O", "-Wall"]

macros = [("SWIG_COBJECT_TYPES", 1), ("DEBUG", DEBUG_LEVEL)]

if GSL_ERROR_HANDLER == 0:
    # If the macro below is not set the error handler will be set to off.
    pass
elif GSL_ERROR_HANDLER == 1:
    macros += [
        ("PyGSL_SET_GSL_ERROR_HANDLER", 1),
    ]
else:
    raise ValueError("Expected a value of 0|1 but got '%s'" % (GSL_ERROR_HANDLER))

macros = macros + []


# Get all the extensions
exts = generate_extensions(macros,swig_flags)


# Now define the actual setup.
proj_name = "pygsl_lite"
setup(
    name=proj_name,
    package_dir={"pygsl_lite": "pygsl_lite", "pygsl_lite.gsl_dist": "gsl_dist"},
    packages=["pygsl_lite", "pygsl_lite.gsl_dist"],
    ext_package="pygsl_lite",
    ext_modules=exts,
)
