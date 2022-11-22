import numpy as np
import numpy.typing as npt


def ampl_distribution(tx: float, ty: float, a: float, b: float):
    def wrapped(x: npt.NDArray, y: npt.NDArray):
        return (tx + (1 - tx) * np.cos(np.pi * x / a)) * (
                ty + (1 - ty) * np.cos(np.pi * y / b)
        )
    return wrapped
