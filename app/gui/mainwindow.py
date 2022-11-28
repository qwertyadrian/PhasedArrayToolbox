from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDoubleValidator

from .window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Максимальный угол отклонения луча, град.
        self.theta_max = None
        # Сектор электрического сканирования (0-Симметричный, 1-Конический)
        self.sector = None
        # Средняя частота рабочего диапозона, Гц
        self.f0 = None
        # Полоса рабочих частот, Гц
        self.delta_f = None
        # Сетка расположения элементов (0-Прямоугольная, 1-Гексагональная)
        self.grid = None
        # Тип распределений поля в плоскостях x, y
        self.dist_type = dict(x=None, y=None)
        # Направление сканирования, град.
        self.direction = dict(theta0=None, phi0=None)
        # Размер антенны, м (для прямоугольной-сторона квадрата, для круглой диаметр)
        self.size = None
        # Частота сигнала, Гц
        self.f = None
        self.dist = {
            "x": {"t": None, "n": None},
            "y": {"t": None, "n": None},
            "r": {"d": None, "n": None},
        }

        # Проверка вводимых значений
        self.double_validator = QDoubleValidator(0, 1e12, 8)

        self.f0_value.setValidator(self.double_validator)
        self.delta_f_value.setValidator(self.double_validator)
        self.size_value.setValidator(self.double_validator)
        self.f_value.setValidator(self.double_validator)

        self.dist_x_value.currentIndexChanged.connect(self.set_dist_x)
        self.dist_y_value.currentIndexChanged.connect(self.set_dist_y)
        self.calc_value.clicked.connect(self.calculate)

    def set_dist_x(self, i):
        if i == 5:
            self.dist_y_value.setEnabled(False)
        else:
            self.dist_y_value.setEnabled(True)
        print(i)

    def set_dist_y(self, i):
        if i == 5:
            self.dist_x_value.setEnabled(False)
        else:
            self.dist_x_value.setEnabled(True)
        print(i)

    def calculate(self):

        self.theta_max = self.theta_max_value.value()
        self.sector = self.sector_value.currentIndex()
        self.grid = self.grid_value.currentIndex()
        self.dist_type.update(
            dict(
                x=self.dist_x_value.currentIndex(),
                y=self.dist_y_value.currentIndex(),
            )
        )
        self.direction.update(
            dict(
                theta0=self.theta_0_value.value(),
                phi0=self.phi_0_value.value(),
            )
        )

        self.f0 = float(self.f0_value.text().replace(",", "."))
        self.delta_f = float(self.delta_f_value.text().replace(",", "."))
        self.size = float(self.size_value.text().replace(",", "."))
        self.f = float(self.f_value.text().replace(",", "."))
