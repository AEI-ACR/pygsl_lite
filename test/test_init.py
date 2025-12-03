import pygsl_lite
import pygsl_lite.init


def test_init_set_debug_level():
    pygsl_lite.init.set_debug_level(1)
    pygsl_lite.init.set_debug_level(0)


def test_set_debug_level():
    pygsl_lite.set_debug_level(1)
    pygsl_lite.set_debug_level(0)
