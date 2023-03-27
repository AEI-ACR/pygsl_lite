/*
 * This module must not depend on any other as it is needed during the startup
 * of pygsl_lite.
 */
#include <Python.h>
#include <gsl/gsl_errno.h>
#include <pygsl_lite/errorno.h>
#include <pygsl_lite/transition.h>
#include <pygsl_lite/error_helpers.h>

static int 
add_errno(PyObject * dict, int num, const char * name)
{
     PyObject * item;

     FUNC_MESS_BEGIN();
     item = PyLong_FromLong(num);
     if(item == NULL){
	  fprintf(stderr, "Failed to generate PyInt with value %d for errno %s\n",
		  num, name);
	  return -1;
     }
     if(PyDict_SetItemString(dict, name, item) == -1){
	  fprintf(stderr, "Failed to add PyInt %p with value %d to dict %p for errno %s\n",
		  (void *) item, num, (void *) dict, name);
	  return -1;
     }
     FUNC_MESS_END();
     return 0;
}   
#define ADD_ERRNO(ERRNO, ERRNOSTR)  if(add_errno(dict, ERRNO, ERRNOSTR) != 0) goto fail

static PyMethodDef errornoMethods[] = {
  {NULL, NULL, 0, NULL} /*sentinel */
};

static const char pygsl_lite_errno_doc[] = "The error numbers as provided by GSL.\n"
  "Typically the error numbers are converted to exceptions. These exceptions\n"
  "are listed in :py:mod:`pygsl_lite.errors`. Some functions (e.g. iterators or steppers)\n"
  "use return values to show that progress can be made (e.g. :c:data:`GSL_CONTINUE`). \n\n"
  "See also `<gsl/gsl_errno.h>`\n";

#ifdef PyGSL_PY3K
static PyModuleDef errnomodule = {
    PyModuleDef_HEAD_INIT,
    "pygsl_lite.errno",
    pygsl_lite_errno_doc,
    -1,
    errornoMethods,
    NULL,
    NULL,
    NULL,
    NULL
};
#endif 

#ifdef __cplusplus
extern "C"
#endif

#ifdef PyGSL_PY3K
PyMODINIT_FUNC
PyInit_errno(void)
#define RETVAL m
#else /* PyGSL_PY3K */
DL_EXPORT(void) initerrno(void)
#define RETVAL
#endif /* PyGSL_PY3K */
{
	PyObject *dict=NULL, *m=NULL;

	FUNC_MESS_BEGIN();
#ifdef PyGSL_PY3K
	m = PyModule_Create(&errnomodule);
#else /* PyGSL_PY3K */
	m = Py_InitModule("pygsl_lite.errno", errornoMethods);
#endif /* PyGSL_PY3K */
     
	if(m == NULL)
		return RETVAL;
	assert(m);

	dict = PyModule_GetDict(m);
	if(!dict)
		goto fail;

     ADD_ERRNO(GSL_SUCCESS , "GSL_SUCCESS");
     ADD_ERRNO(GSL_FAILURE , "GSL_FAILURE" );
     ADD_ERRNO(GSL_CONTINUE, "GSL_CONTINUE");
     ADD_ERRNO(GSL_EDOM    , "GSL_EDOM"    );
     ADD_ERRNO(GSL_ERANGE  , "GSL_ERANGE"  );
     ADD_ERRNO(GSL_EFAULT  , "GSL_EFAULT"  );
     ADD_ERRNO(GSL_EINVAL  , "GSL_EINVAL"  );
     ADD_ERRNO(GSL_EFAILED , "GSL_EFAILED" );
     ADD_ERRNO(GSL_EFACTOR , "GSL_EFACTOR" );
     ADD_ERRNO(GSL_ESANITY , "GSL_ESANITY" );
     ADD_ERRNO(GSL_ENOMEM  , "GSL_ENOMEM"  );
     ADD_ERRNO(GSL_EBADFUNC, "GSL_EBADFUNC");
     ADD_ERRNO(GSL_ERUNAWAY, "GSL_ERUNAWAY");
     ADD_ERRNO(GSL_EMAXITER, "GSL_EMAXITER");
     ADD_ERRNO(GSL_EZERODIV, "GSL_EZERODIV");
     ADD_ERRNO(GSL_EBADTOL , "GSL_EBADTOL" );
     ADD_ERRNO(GSL_ETOL    , "GSL_ETOL"    );
     ADD_ERRNO(GSL_EUNDRFLW, "GSL_EUNDRFLW");
     ADD_ERRNO(GSL_EOVRFLW , "GSL_EOVRFLW" );
     ADD_ERRNO(GSL_ELOSS   , "GSL_ELOSS"   );
     ADD_ERRNO(GSL_EROUND  , "GSL_EROUND"  );
     ADD_ERRNO(GSL_EBADLEN , "GSL_EBADLEN" );
     ADD_ERRNO(GSL_ENOTSQR , "GSL_ENOTSQR" );
     ADD_ERRNO(GSL_ESING   , "GSL_ESING"   );
     ADD_ERRNO(GSL_EDIVERGE, "GSL_EDIVERGE");
     ADD_ERRNO(GSL_EUNSUP  , "GSL_EUNSUP"  );
     ADD_ERRNO(GSL_EUNIMPL , "GSL_EUNIMPL" );
     ADD_ERRNO(GSL_ECACHE  , "GSL_ECACHE"  );
     ADD_ERRNO(GSL_ETABLE  , "GSL_ETABLE"  );
     ADD_ERRNO(GSL_ENOPROG , "GSL_ENOPROG" );
     ADD_ERRNO(GSL_ENOPROGJ, "GSL_ENOPROGJ");
     ADD_ERRNO(GSL_ETOLF   , "GSL_ETOLF"   );
     ADD_ERRNO(GSL_ETOLX   , "GSL_ETOLX"   );
     ADD_ERRNO(GSL_ETOLG   , "GSL_ETOLG"   );
     ADD_ERRNO(GSL_EOF     , "GSL_EOF"     );
     ADD_ERRNO(PyGSL_ESTRIDE, "PyGSL_ESTRIDE");
     ADD_ERRNO(PyGSL_EUNIMPL, "PyGSL_EUNIMPL");
     ADD_ERRNO(PyGSL_EINIT  , "PyGSL_EINIT");
     

	FUNC_MESS_END();

     return RETVAL;
 fail:
     fprintf(stderr, "Initialisation of module errorno failed!\n");
     return RETVAL;
}
