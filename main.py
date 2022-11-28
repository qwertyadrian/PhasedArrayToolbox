import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from antenna_toolbox.PhasedArray import (
    RectangularAntenna,
    HexagonalAntenna,
    HexagonalRoundAntenna,
    RectangularRoundAntenna,
)
import antenna_toolbox.AmplitudeDistributions as ad

f = 4e9  # Гц
wavelength = 3e8 / f  # м/c
k = 2 * np.pi / wavelength

a = 57.5 * wavelength / 5
b = a

# Шаг решетки по оси x и y в метрах
dx = 0.9 * wavelength / (1 + np.sin(np.deg2rad(25)))
dy = dx

dtheta = 0.1
dphi = 0.1

theta = np.deg2rad(np.arange(-90, 90, dtheta))
phi = np.deg2rad(np.arange(0, 360, dphi))


# ant = RectangularAntenna(
#     a=a,
#     b=b,
#     dx=dx,
#     dy=dy,
#     freq=f,
# )

# ant = HexagonalAntenna(
#     a=a,
#     b=b,
#     ddelta=dx,
#     freq=f,
# )

ant = RectangularRoundAntenna(
    diameter=0.5,
    dx=dx,
    dy=dy,
    freq=f,
)

# ant = HexagonalRoundAntenna(
#     diameter=0.5,
#     ddelta=dx,
#     freq=f,
# )

ant.set_ampl_distribution(ad.ampl_distribution_round(delta=0.4, n=4, a=0.25))
pd = ant.phase_distribution(np.deg2rad(0), 0)

F = ant.array_factor(theta, np.deg2rad(90), pd)

# plt.subplot(2, 1, 1)
# plt.plot(np.rad2deg(theta), ant.array_factor(theta, np.deg2rad(0), pd))
# plt.ylim(-30)
# 
# plt.subplot(2, 1, 2)
# plt.plot(np.rad2deg(theta), ant.array_factor(theta, np.deg2rad(90), pd))
# plt.ylim(-30)
# plt.figure(2)
# plt.scatter(ant.elements_x, ant.elements_y)
# 
# fig_4, ax_4 = plt.subplots(subplot_kw={"projection": "3d"})
# 
# if len(ant.ampl_distribution.shape) == 2:
#     surf = ax_4.plot_surface(
#         ant.elements_x,
#         ant.elements_y,
#         ant.ampl_distribution,
#         rcount=ant.elements_x.size,
#         ccount=ant.elements_y.size,
#         cmap=plt.get_cmap("rainbow"),
#         linewidth=0,
#         antialiased=False,
#     )
# else:
#     surf = ax_4.plot_trisurf(
#         ant.elements_x,
#         ant.elements_y,
#         ant.ampl_distribution,
#         cmap=plt.get_cmap("rainbow"),
#         linewidth=0,
#         antialiased=False,
#     )
# 
# fig_4.colorbar(surf, ticks=np.arange(0, 1.15, 0.05))
# 
# ax_4.scatter(ant.elements_x, ant.elements_y, 0)
# ax_4.set_xlabel("$x$, м")
# ax_4.set_ylabel("$Y$, м")
# ax_4.set_zlabel("$A$, В/м")


fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# ax.plot(theta, ant.array_factor(theta, np.deg2rad(0), pd))
# ax.set_rmin(-30)
# ax.set_rticks(np.arange(-30,1,5))  # Less radial ticks
# ax.set_rlabel_position(135)  # Move radial labels away from plotted line
# ax.grid(True)

# x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(theta, ant.array_factor(theta, np.deg2rad(0), pd))


def animate(i):
    
    theta0 = 45 * np.sin(2*np.pi*i/100)
    pd = ant.phase_distribution(np.deg2rad(theta0), 0)
    line.set_ydata(ant.array_factor(theta, np.deg2rad(0), pd))  # update the data.
    return line,

ax.set_rmin(-30)
ax.set_rticks(np.arange(-30,1,5))  # Less radial ticks
ax.set_rlabel_position(135)  # Move radial labels away from plotted line
ax.grid(True)

ani = animation.FuncAnimation(
    fig, animate, interval=1, blit=True, save_count=50, frames=100)

ani.save("DN_polar.gif", fps=144)

plt.show()
