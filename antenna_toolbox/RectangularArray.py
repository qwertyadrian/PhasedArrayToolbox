from collections.abc import Iterable
import numpy as np
import numpy.typing as npt
import typing


class RectangularAntenna:
    def __init__(self, a: float, b: float, dx: float, dy: float, freq: float):
        """

        :param a: Размер антенны по оси X
        :param b: Размер антенны по оси Y
        :param dx: Шаг решетки по оси X
        :param dy: Шаг решетки по оси Y
        :param freq: Резонансная частота
        """
        self.a = a
        self.b = b
        self.dx = dx
        self.dy = dy
        self.frequency = freq

        self._x = dx * np.linspace(
            -self.Nx / 2, self.Nx / 2, self.Nx
        )
        self._y = dy * np.linspace(
            -self.Ny / 2, self.Ny / 2, self.Ny
        )

        self.elements_y, self.elements_x = np.meshgrid(self._y, self._x)

        self.ampl_distribution = None

    def phase_distribution(self, theta: float, phi: float) -> npt.NDArray:
        """

        :param theta: Угол сканирования в градусах в плоскости theta
        :param phi: Угол сканирования в градусах в плоскости phi
        :return: Фазовое распределение
        """
        return -self.k * (
                self.elements_x * np.cos(phi) + self.elements_y * np.sin(phi)
        ) * np.sin(theta)

    def array_factor(
            self,
            theta: float,
            phi: float,
            pd: npt.NDArray,
            normalize: bool = True,
            log: bool = True,
    ):
        """Функция, вычисляющая диаграмму направленности в точке (theta, phi)

        :param theta: Угол сканирования в плоскости theta
        :param phi: Угол сканирования в плоскости phi
        :param pd: Фазовое распределение в антенне
        :param normalize: Нормализовать диаграмму направленности
        :param log: Масштаб в децибелах
        :return:
        """
        F = np.abs(self._af(theta, phi, pd))
        if normalize:
            F_max = np.max(np.abs(self._af(theta, phi, pd)))
            F_norm = F / F_max
            if log:
                return 20 * np.log10(F_norm)
            else:
                return F_norm
        else:
            return F

    def _af(self, theta, phi, pd):
        if isinstance(theta, Iterable) and isinstance(phi, Iterable):
            F = np.zeros((theta.size, phi.size), dtype=complex)
            for i, th in enumerate(theta):
                for j, ph in enumerate(phi):
                    F[i, j] = self.__F(th, ph, pd)
            return F
        elif isinstance(theta, Iterable) and not isinstance(phi, Iterable):
            F = np.zeros(theta.size, dtype=complex)
            for i, th in enumerate(theta):
                F[i] = self.__F(th, phi, pd)
            return F
        elif not isinstance(theta, Iterable) and isinstance(phi, Iterable):
            F = np.zeros(theta.size, dtype=complex)
            for j, ph in enumerate(phi):
                F[j] = self.__F(theta, ph, pd)
            return F
        else:
            return self.__F(theta, phi, pd)

    def __F(self, theta, phi, pd):
        return np.sum(
            np.sum(
                self.ampl_distribution * np.exp(1j * pd) * np.exp(
                    1j * self.k * (
                            self.elements_x * np.cos(phi) +
                            self.elements_y * np.sin(phi)
                    ) * np.sin(theta)
                ),
                axis=0,
            )
        )

    def set_ampl_distribution(
            self,
            dist: typing.Callable[[npt.NDArray, npt.NDArray], npt.NDArray],
    ):
        """Метод, задающий амплитудное распределение

        :param dist: Функция амплитудного распределения, принимающая координаты
        элементов по оси X и Y
        """
        self.ampl_distribution = dist(self.elements_x, self.elements_y)

    @property
    def Nx(self) -> int:
        """Число элементов по оси X

        :rtype: float
        """
        return int(self.a // self.dx)

    @property
    def Ny(self) -> int:
        """Число элементов по оси Y

        :rtype: float
        """
        return int(self.b // self.dy)

    @property
    def wavelength(self):
        """Длина волны"""
        return 3e8 / self.frequency

    @property
    def k(self):
        """Волновое число"""
        return 2 * np.pi / self.wavelength
