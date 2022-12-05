from tempfile import NamedTemporaryFile

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.colorbar import Colorbar

from antenna_toolbox.PhasedArray import (
    RectangularAntenna,
    HexagonalAntenna,
    HexagonalRoundAntenna,
    RectangularRoundAntenna,
)
import antenna_toolbox.AmplitudeDistributions as ad


plt.rcParams["font.size"] = "14"


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
    calc_animation=False,
):
    """Функция вычисляющая ДН и амплитудное распределение

    :param theta_max: Максимальный угол отклонения луча
    :param sector: Тип сектора (симметричный или конический)
    :param grid: Сетка расположения элементов (гексагональная или прямоугольная)
    :param dist_type: Тип распределения
    :param direction: Направление сканирования
    :param f0: Центральная частота
    :param delta_f: Полоса рабочих частот
    :param size: Размер антенны (сторона квадрата или диаметр раскрыва)
    :param f: Рабочая частота
    :param dist: Параметры распределения
    :param calc_animation: Нужно ли считать анимацию
    :return: Холсты с графиками
    """
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
            freq=f,
        )
    elif sector == 0 and grid == 1:
        ant = HexagonalAntenna(
            a=size,
            b=size,
            ddelta=ddelta,
            freq=f,
        )
    elif sector == 1 and grid == 0:
        ant = RectangularRoundAntenna(
            diameter=size,
            dx=dx,
            dy=dy,
            freq=f,
        )
    else:
        ant = HexagonalRoundAntenna(
            diameter=size,
            ddelta=ddelta,
            freq=f,
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

    # Расчет контурного графика
    th = np.deg2rad(np.arange(91))
    ph = np.deg2rad(np.arange(0, 362, 2))

    contour_map_canvas = FigureCanvas(Figure())
    ax1, ax2 = contour_map_canvas.figure.subplots(1, 2, width_ratios=(0.95, 0.05))
    cs = ax1.contourf(
        np.rad2deg(ph),
        np.rad2deg(th),
        ant.array_factor(th, ph, pd),
        levels=np.arange(-30, 0.05, 1),
        cmap=plt.get_cmap("Spectral_r"),
    )
    ax1.set_ylim(0, 90)
    ax1.set_ylabel(r"$\theta \degree$")
    ax1.set_xlabel(r"$\varphi \degree$")
    ax1.grid()
    Colorbar(ax2, ticks=np.arange(-30, 1, 2), mappable=cs)

    # График ДН
    th = np.deg2rad(np.arange(-180, 180, 0.1))

    dn_canvas = FigureCanvas(Figure())
    if not (direction["theta"] or direction["phi"]):
        dn_canvas.figure.subplots_adjust(hspace=0.5)
        ax1, ax2 = dn_canvas.figure.subplots(2, 1)
        ax1.plot(np.rad2deg(th), ant.array_factor(th, 0, pd))
        ax1.set_ylim(-30, 0)
        ax1.grid(color="k", linewidth=1)
        ax1.minorticks_on()
        ax1.grid(which="minor", ls=":")
        ax1.set_xlabel(r"$\theta \degree$")
        ax1.set_ylabel(r"$F(\theta, \varphi=0\degree)$, дБ")

        ax2.plot(np.rad2deg(th), ant.array_factor(th, np.pi / 2, pd))
        ax2.set_ylim(-30, 0)
        ax2.grid(color="k", linewidth=1)
        ax2.minorticks_on()
        ax2.grid(which="minor", ls=":")
        ax2.set_xlabel(r"$\theta \degree$")
        ax2.set_ylabel(r"$F(\theta, \varphi=90\degree)$, дБ")
    else:
        ax1 = dn_canvas.figure.subplots()
        ax1.plot(np.rad2deg(th), ant.array_factor(th, direction["phi"], pd))
        ax1.set_ylim(-30, 0)
        ax1.grid(color="k", linewidth=1)
        ax1.minorticks_on()
        ax1.grid(which="minor", ls=":")
        ax1.set_xlabel(r"$\theta \degree$")
        ax1.set_ylabel(
            rf"$F(\theta, \varphi={np.rad2deg(direction['phi'])}\degree)$, дБ"
        )

    # Расчет амплитудного распределения и сетки расположения излучателей
    dist_canvas = FigureCanvas(Figure())
    if not all(dist_type.values()):
        ax1 = dist_canvas.figure.subplots(subplot_kw={"projection": "3d"})
    else:
        ax1, ax2 = dist_canvas.figure.subplots(1, 2, width_ratios=(0.95, 0.05))
        ax1 = dist_canvas.figure.subplots(subplot_kw={"projection": "3d"})
    if len(ant.ampl_distribution.shape) == 2:
        surf = ax1.plot_surface(
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
        surf = ax1.plot_trisurf(
            ant.elements_x,
            ant.elements_y,
            ant.ampl_distribution,
            cmap=plt.get_cmap("rainbow"),
            linewidth=0,
            antialiased=False,
        )
    ax1.scatter(ant.elements_x, ant.elements_y, 0)
    ax1.set_xlabel(r"$x$, м")
    ax1.set_ylabel(r"$Y$, м")
    ax1.set_zlabel(r"$E$, В/м")
    if all(dist_type.values()):
        Colorbar(ax2, ticks=np.arange(0, 1.1, 0.1), mappable=surf)

    grid_canvas = FigureCanvas(Figure())
    ax1 = grid_canvas.figure.subplots()
    ax1.scatter(ant.elements_x, ant.elements_y, marker="s")
    ax1.grid()
    ax1.set_xlim(-ant.Nx * ant.dx / 2 - 2 * ant.dx, ant.Nx * ant.dx / 2 + 2 * ant.dx)
    ax1.set_xlim(-ant.Ny * ant.dy / 2 - 2 * ant.dy, ant.Ny * ant.dy / 2 + 2 * ant.dy)

    ani_file = None
    if calc_animation:
        th = np.deg2rad(np.arange(-90, 90, 0.25))

        scan_fig = Figure(figsize=(6.4 * 1.2, 4.8 * 1.2))
        scan_fig.subplots_adjust(top=0.935, bottom=0.055, left=0, right=1)
        # scan_fig.tight_layout()
        scan_canvas = FigureCanvas(scan_fig)
        ax1 = scan_canvas.figure.subplots(subplot_kw={"projection": "polar"})
        (line_,) = ax1.plot(th, ant.array_factor(th, 0, pd))
        line1_ = ax1.axvline(0, color="red")
        ax1.set_rmin(-30)
        ax1.set_rticks(np.arange(-30, 1, 5))  # Less radial ticks
        ax1.set_thetagrids(np.arange(-90, 100, 10))
        ax1.set_thetamin(-90)
        ax1.set_thetamax(90)
        ax1.set_rlabel_position(135)  # Move radial labels away from plotted line
        ax1.grid(True)
        ax1.set_theta_zero_location("N")

        def animate(i, lines, theta, antenna):
            theta0 = np.pi / 2 * np.sin(2 * np.pi * i / 150)
            pd = antenna.phase_distribution(theta0, 0)
            lines[0].set_ydata(ant.array_factor(theta, 0, pd))  # update the data.
            lines[1].set_xdata(theta0)
            return lines

        def progress(current_frame: int, total_frames: int):
            print(f"Saving animation: {current_frame+1} of {total_frames}")

        ani = animation.FuncAnimation(
            scan_fig,
            animate,
            interval=100,
            fargs=((line_, line1_), th, ant),
            frames=150,
        )
        ani_file = NamedTemporaryFile(delete=False, suffix=".gif")
        ani.save(ani_file.name, progress_callback=progress)

    return contour_map_canvas, dn_canvas, dist_canvas, grid_canvas, ani_file


def choice_distribution(index: int, dist: dict, size: float) -> callable:
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
