import numpy as np
from pygsl_lite import spline


def test_cubic_spline():
    t_old = np.linspace(-2 * np.pi, 2 * np.pi, 50)
    y_old = np.cos(t_old)
    n = len(t_old)
    intrp = spline.cspline(n)
    intrp.init(t_old, y_old)
    t_new = np.linspace(-2 * np.pi, 2 * np.pi, 200)
    y_interp = intrp.eval_e_vector(t_new)
    assert (
        np.abs(np.sum(y_interp) - 0.9878615069653094) < 1e-8
    ), "Interpolation test failed"
