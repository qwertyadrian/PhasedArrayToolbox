import numpy as np
import numpy.typing as npt


def ampl_distribution_round(delta: float, n: int, a: float, E0: float = 1.0):
    def wrapped(x: npt.NDArray, y: npt.NDArray):
        return E0 * ((1 - delta) + delta * (1 - (x**2 + y**2) / a**2) ** n)

    return wrapped


def ampl_dist_uniform(E0: float = 1.0):
    def wrapped(x: npt.NDArray):
        return E0 * np.ones_like(x)

    return wrapped


def ampl_dist_squared(t: float, a: float, E0: float = 1.0):
    def wrapped(x: npt.NDArray):
        return E0 * (1 - (1 - t) * (2 * x / a) ** 2)

    return wrapped


def ampl_dist_cos(t: float, a: float, E0: float = 1.0):
    def wrapped(x: npt.NDArray):
        return E0 * (t + (1 - t) * np.cos(np.pi * x / a))

    return wrapped


def ampl_dist_cos_pedestal(t: float, a: float, E0: float = 1.0):
    def wrapped(x: npt.NDArray):
        return E0 * ((1 + t) / 2 + (1 - t) / 2 * np.cos(2 * np.pi * x / a))

    return wrapped


def ampl_dist_cos_degree_n(n: int, a: float, E0: float = 1.0):
    def wrapped(x: npt.NDArray):
        return E0 * np.cos(np.pi * x / a) ** n

    return wrapped
