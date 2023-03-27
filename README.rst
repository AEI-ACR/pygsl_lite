PyGSL_Lite
============

This package provides a very minimal wrapper for ``GSL``, based on the `pygsl library <https://github.com/pygsl/pygsl>`_ .
This is done to drastically reduce complexity. In particular,  the following features are supported as they provide performance
advantages useful for physics simulations.

- ODE integration
- Cubic spline interpolation
- 1D root finding

Due to the much reduced scope, this package can eschew a lot of
complexity in wrapping all of ``GSL``. Furthermore, only latest ``GSL`` versions(>=2.7) are supported.
As a result, the installation process is significantly streamlined.


**For a complete GSL experience, it is recommended to use**  `pygsl <https://github.com/pygsl/pygsl>`_

**All credit for GSL functionality is due to original pygsl authors/maintainers**. See `thanks <https://github.com/pygsl/pygsl/#thanks>`_  , `maintainers <https://github.com/pygsl/pygsl#maintainers>`_  and in `CREDITS.rst. <https://github.com/pygsl/pygsl/blob/main/CREDITS.rst>`_


Installation instructions
-------------------------
Installation requires ``gsl>=2.7`` and optionally ``swig>=4.0``, if one wants to rebuild the wrappers.
Only ``python>=3.8`` is supported.

If installing from source, run

.. code-block:: sh

   pip install .


The ``pygsl`` documentation can be found at `here <https://github.com/pygsl/pygsl/>`_
