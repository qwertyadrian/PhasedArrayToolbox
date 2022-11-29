import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# from matplotlib.backends.backend_qtagg import (
#     FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
# from matplotlib.figure import Figure

from antenna_toolbox.PhasedArray import (
    RectangularAntenna,
    HexagonalAntenna,
    HexagonalRoundAntenna,
    RectangularRoundAntenna,
)
import antenna_toolbox.AmplitudeDistributions as ad


def graph(
    theta_max,
    sector,
    grid,
    dist_type,
    direction,
    f0,
    delta_f,
    size,
    f,
    dist,
):
    # Длина волны в метрах
    wavelength = 3e8 / f
    # Волновое число
    k = 2 * np.pi / wavelength

    dtheta = 0.1
    dphi = 0.1

    theta = np.deg2rad(np.arange(-90, 90, dtheta))
    phi = np.deg2rad(np.arange(0, 360, dphi))

    if grid == 0:
        dx = 0.9 * 3e8 / (f0 + delta_f / 2) / (1 + np.sin(np.deg2rad(theta_max)))
        dy = dx
    else:
        ddelta = (
            0.9
            * 2
            / np.sqrt(3)
            * 3e8
            / (f0 + delta_f / 2)
            / (1 + np.sin(np.deg2rad(theta_max)))
        )

    if sector == 0 and grid == 0:
        ant = RectangularAntenna(
            a=size,
            b=size,
            dx=dx,
            dy=dy,
            freq=f0,
        )
    elif sector == 0 and grid == 1:
        ant = HexagonalAntenna(
            a=size,
            b=size,
            ddelta=ddelta,
            freq=f0,
        )
    elif sector == 1 and grid == 0:
        ant = RectangularRoundAntenna(
            diameter=size,
            dx=dx,
            dy=dy,
            freq=f0,
        )
    else:
        ant = HexagonalRoundAntenna(
            diameter=size,
            ddelta=ddelta,
            freq=f0,
        )
    direction = {k: np.deg2rad(v) for k, v in direction.items()}

    if 5 in dist_type.values():
        ant.set_ampl_distribution(ad.ampl_distribution_round(**dist["r"], a=size))
    else:
        ant.set_ampl_distribution(
            choice_distribution(dist_type["x"], dist["x"], size),
            choice_distribution(dist_type["y"], dist["y"], size),
        )
    pd = ant.phase_distribution(**direction)

    #     F = ant.array_factor(theta, np.deg2rad(90), pd)

    plt.subplot(2, 1, 1)
    plt.plot(np.rad2deg(theta), ant.array_factor(theta, np.deg2rad(0), pd))
    plt.ylim(-30)

    plt.subplot(2, 1, 2)
    plt.plot(np.rad2deg(theta), ant.array_factor(theta, np.deg2rad(90), pd))
    plt.ylim(-30)

    plt.figure(2)
    plt.scatter(ant.elements_x, ant.elements_y)

    fig_4, ax_4 = plt.subplots(subplot_kw={"projection": "3d"})

    if len(ant.ampl_distribution.shape) == 2:
        surf = ax_4.plot_surface(
            ant.elements_x,
            ant.elements_y,
            ant.ampl_distribution,
            rcount=ant.elements_x.size,
            ccount=ant.elements_y.size,
            cmap=plt.get_cmap("rainbow"),
            linewidth=0,
            antialiased=False,
        )
    else:
        surf = ax_4.plot_trisurf(
            ant.elements_x,
            ant.elements_y,
            ant.ampl_distribution,
            cmap=plt.get_cmap("rainbow"),
            linewidth=0,
            antialiased=False,
        )

    fig_4.colorbar(surf, ticks=np.arange(0, 1.15, 0.05))

    ax_4.scatter(ant.elements_x, ant.elements_y, 0)
    ax_4.set_xlabel("$x$, м")
    ax_4.set_ylabel("$Y$, м")
    ax_4.set_zlabel("$A$, В/м")

    #     fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    # ax.plot(theta, ant.array_factor(theta, np.deg2rad(0), pd))
    # ax.set_rmin(-30)
    # ax.set_rticks(np.arange(-30,1,5))  # Less radial ticks
    # ax.set_rlabel_position(135)  # Move radial labels away from plotted line
    # ax.grid(True)

    # x = np.arange(0, 2*np.pi, 0.01)
    #     line, = ax.plot(theta, ant.array_factor(theta, np.deg2rad(0), pd))
    #
    #
    #     def animate(i):
    #
    #     #     theta0 = 45 * np.sin(2*np.pi*i/100)
    #
    #         pd = ant.phase_distribution(np.deg2rad(i), 0)
    #         line.set_ydata(ant.array_factor(theta, np.deg2rad(0), pd))  # update the data.
    #         #plt.savefig(f"result/Dn{i+50}.pdf")
    #         return line,
    #
    #
    #     ax.set_rmin(-30)
    #     ax.set_rticks(np.arange(-30,1,5))  # Less radial ticks
    #     ax.set_rlabel_position(135)  # Move radial labels away from plotted line
    #     ax.grid(True)
    #
    #     ani = animation.FuncAnimation(
    #         fig, animate, interval=1, blit=True, save_count=50, frames=np.arange(-50,50))

    plt.show()


def choice_distribution(index: int, dist: dict, size: float):
    if index == 0:
        return ad.ampl_dist_uniform()
    elif index == 1:
        return ad.ampl_dist_squared(t=dist["t"], a=size)
    elif index == 2:
        return ad.ampl_dist_cos(t=dist["t"], a=size)
    elif index == 3:
        return ad.ampl_dist_cos_pedestal(t=dist["t"], a=size)
    else:
        return ad.ampl_dist_cos_degree_n(n=dist["n"], a=size)
