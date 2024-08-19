import pygsl_lite.errno as errno
import pygsl_lite.odeiv2 as odeiv2
import numpy as np


def ode_system_gradient(t: float, y: np.ndarray, args) -> np.ndarray:
    mu = args[0]
    f = [y[1], -y[0] - mu * y[1] * (y[0] * y[0] - 1)]
    return np.array(f)


def ode_system_jacobian(t: float, y: np.ndarray, args):
    mu = args[0]

    dfdy = np.zeros((2, 2))
    dfdy[0, 0] = 0
    dfdy[0, 1] = 1
    dfdy[1, 0] = -2.0 * mu * y[0] * y[1] - 1.0
    dfdy[1, 1] = -mu * (y[0] * y[0] - 1.0)

    dfdt = np.zeros((2,))
    return dfdy, dfdt


def test_ode_basic():
    mu = 10
    dimension = 2
    sys = odeiv2.system(
        ode_system_gradient,
        ode_system_jacobian,
        dimension,
        [mu],
    )

    s = odeiv2.pygsl_lite_odeiv2_step(odeiv2.step_rk8pd, dimension)
    c = odeiv2.pygsl_lite_odeiv2_control(1e-6, 1e-6, 1, 0, None)
    e = odeiv2.pygsl_lite_odeiv2_evolve(dimension)

    t = 0.0
    t1 = 1000.0
    y = [1.0, 0.0]
    h = 1e-4

    all_ts = []
    all_y = []

    while t < t1:
        # Take a step
        status, t, h, y = e.apply(c, s, sys, t, t1, h, y)
        if status != errno.GSL_SUCCESS:
            print("break status", status)
            break

        # error from the test control
        e.get_yerr()

        # Append the last step
        all_y.append(y)
        all_ts.append(t)

    assert all_y
    assert all_ts
