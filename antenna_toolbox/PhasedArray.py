from abc import ABC
from collections.abc import Iterable
import numpy as np
import numpy.typing as npt
import typing


class AntennaBase(ABC):
    elements_x: npt.NDArray
    elements_y: npt.NDArray
    ampl_distribution: npt.NDArray
    frequency: float
    a: float
    b: float
    dx: float
    dy: float

    def phase_distribution(self, theta: float, phi: float) -> npt.NDArray:
        """

        :param theta: Угол сканирования в градусах в плоскости theta
        :param phi: Угол сканирования в градусах в плоскости phi
        :return: Фазовое распределение
        """
        return (
            -self.k
            * (self.elements_x * np.cos(phi) + self.elements_y * np.sin(phi))
            * np.sin(theta)
        )

    def array_factor(
        self,
        theta: typing.Union[float, npt.NDArray],
        phi: typing.Union[float, npt.NDArray],
        pd: npt.NDArray,
        normalize: bool = True,
        log: bool = True,
    ) -> typing.Union[float, npt.NDArray]:
        """Функция, вычисляющая диаграмму направленности в точке (theta, phi)

        :param theta: Угол сканирования в плоскости theta
        :param phi: Угол сканирования в плоскости phi
        :param pd: Фазовое распределение в антенне
        :param normalize: Нормализовать диаграмму направленности
        :param log: Масштаб в децибелах
        :return: Значение или массив значений ДН
        """
        F = np.abs(self._af(theta, phi, pd))
        if normalize:
            F_max = np.max(F)
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
                self.ampl_distribution
                * np.exp(1j * pd)
                * np.exp(
                    1j
                    * self.k
                    * (self.elements_x * np.cos(phi) + self.elements_y * np.sin(phi))
                    * np.sin(theta)
                ),
                axis=0,
            )
        )

    def set_ampl_distribution(
        self,
        dist_x: typing.Callable[[npt.NDArray], npt.NDArray],
        dist_y: typing.Callable[[npt.NDArray], npt.NDArray],
    ):
        """Метод, задающий амплитудное распределение

        :param dist_x: Функция амплитудного распределения, принимающая координаты
        элементов по оси X
        :param dist_y: Функция амплитудного распределения, принимающая координаты
        элементов по оси Y
        """
        self.ampl_distribution = dist_x(self.elements_x) * dist_y(self.elements_y)

    @property
    def Nx(self) -> int:
        """Число элементов по оси X

        :rtype: int
        """
        return int(self.a // self.dx)

    @property
    def Ny(self) -> int:
        """Число элементов по оси Y

        :rtype: int
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


class RectangularAntenna(AntennaBase):
    """Класс антенны с прямоугольной сеткой и прямоугольным раскрывом"""

    def __init__(self, a: float, b: float, dx: float, dy: float, freq: float):
        """

        :param a: Размер антенны по оси X
        :param b: Размер антенны по оси Y
        :param dx: Шаг решетки по оси X
        :param dy: Шаг решетки по оси Y
        :param freq: Рабочая частота
        """
        self.a = a
        self.b = b
        self.dx = dx
        self.dy = dy
        self.frequency = freq

        self._x = dx * np.linspace(-self.Nx / 2, self.Nx / 2, self.Nx)
        self._y = dy * np.linspace(-self.Ny / 2, self.Ny / 2, self.Ny)

        self.elements_x, self.elements_y = np.meshgrid(self._x, self._y)

        self.ampl_distribution = np.array([])


class HexagonalAntenna(RectangularAntenna):
    """Класс антенны с гексагональной сеткой и прямоугольным раскрывом"""

    def __init__(self, a: float, b: float, ddelta: float, freq: float):
        """

        :param a: Размер антенны по оси X
        :param b: Размер антенны по оси Y
        :param ddelta: Расстояние между элементами
        :param freq: Рабочая частота
        """

        ratio = np.sqrt(3) / 2
        dx = ddelta
        dy = ratio * ddelta

        self.ddelta = ddelta

        super().__init__(a, b, dx, dy, freq)

        self.elements_x[::2, :] += self.ddelta / 2


class RectangularRoundAntenna(AntennaBase):
    """Класс антенны с прямоугольной сеткой и круглым раскрывом"""

    def __init__(
        self, diameter: float, dx: float, dy: float, freq: float, ddelta: float = 0
    ):
        """

        :param diameter: Диаметр раскрыва антенны
        :param dx: Шаг сетки по оси X
        :param dy: Шаг сетки по оси Y
        :param freq: Рабочая частота
        :param ddelta: Расстояние между соседними элементами в решетке
        """
        self.dx = dx
        self.dy = dy
        self.diameter = diameter
        self.ddelta = ddelta
        self.frequency = freq

        N = max(self.Nx, self.Ny) + 1
        self._x = self.dx * np.linspace(-N / 2, N / 2, N)
        self._y = self.dy * np.linspace(-N / 2, N / 2, N)

        elements_x, elements_y = np.meshgrid(self._x, self._y)
        elements_x[::2, :] += self.ddelta / 2

        self.elements_x = np.array([])
        self.elements_y = np.array([])

        for i, j in zip(elements_x.flatten(), elements_y.flatten()):
            if np.sqrt(i**2 + j**2) <= self.diameter / 2:
                self.elements_x = np.append(self.elements_x, i)
                self.elements_y = np.append(self.elements_y, j)

    def set_ampl_distribution(self, *args):
        if len(args) == 1:
            (dist,) = args
            self.ampl_distribution = dist(self.elements_x, self.elements_y)
        elif len(args) == 2:
            dist_x, dist_y = args
            self.ampl_distribution = dist_x(self.elements_x) * dist_y(self.elements_y)

    @property
    def Nx(self) -> int:
        """Число элементов по оси X

        :rtype: int
        """
        return int(np.ceil(self.diameter / (4 * self.dx)) * 4)

    @property
    def Ny(self) -> int:
        """Число элементов по оси Y

        :rtype: int
        """
        return int(np.ceil(self.diameter / (4 * self.dy)) * 4)


class HexagonalRoundAntenna(RectangularRoundAntenna):
    """Класс антенны с гексагональной сеткой и круглым раскрывом"""

    def __init__(self, diameter: float, ddelta: float, freq: float):
        """

        :param diameter: Диаметр раксрыва
        :param ddelta: Расстояние между элементами
        :param freq: Рабочая частота
        """
        ratio = np.sqrt(3) / 2

        super().__init__(
            diameter, dx=ddelta, dy=ratio * ddelta, freq=freq, ddelta=ddelta
        )

    @property
    def Nx(self) -> int:
        """Число элементов по оси X

        :rtype: int
        """
        return int(np.ceil(self.diameter / (4 * self.ddelta)) * 4)
