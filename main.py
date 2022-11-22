import numpy as np
import matplotlib.pyplot as plt

from antenna_toolbox.PhasedArray import RectangularAntenna, HexagonalAntenna
from antenna_toolbox.AmplitudeDistributions import ampl_distribution

f = 4e9  # Гц
wavelength = 3e8 / f  # м/c
k = 2 * np.pi / wavelength

a = 57.5 * wavelength / 5
b = a

# Шаг решетки по оси x и y в метрах
dx = 0.9 * wavelength / (1 + np.sin(np.deg2rad(25)))
dy = 1.5*dx

dtheta = 0.1
dphi = 0.1

theta = np.deg2rad(np.arange(-90, 90, dtheta))
phi = np.deg2rad(np.arange(0, 360, dphi))

ant = RectangularAntenna(
    a=a,
    b=b,
    dx=dx,
    dy=dy,
    freq=f,
)

# ant2 = HexagonalAntenna(a, b, 0.7*wavelength, f)

ant.set_ampl_distribution(ampl_distribution(0.4, 0.4, a, b))
pd = ant.phase_distribution(np.deg2rad(0), 0)

F = ant.array_factor(theta, np.deg2rad(0), pd)
# ant.elements_x = ant.elements_x * np.sqrt(3)/2
# ant.elements_x[::2, :] += np.sqrt(3)/4
# print(F)

plt.plot(np.rad2deg(theta), F)
plt.ylim(-30)
plt.figure(2)
plt.scatter(ant.elements_x, ant.elements_y)
plt.show()

