import numpy as np
import numpy.typing as npt


def ampl_distribution(t: float, a: float):
    def wrapped(x: npt.NDArray, y: npt.NDArray):
        return (t + (1 - t) * np.cos(np.pi * x / a)) * (
                t + (1 - t) * np.cos(np.pi * y / a)
        )
    return wrapped
