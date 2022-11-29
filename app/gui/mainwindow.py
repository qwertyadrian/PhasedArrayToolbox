from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QDoubleValidator

from .window import Ui_MainWindow
from .widgets import ParameterT, ParameterN, ParametersDeltaN


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Максимальный угол отклонения луча, град.
        self.theta_max = None
        # Сектор электрического сканирования (0-Симметричный, 1-Конический)
        self.sector = None
        # Средняя частота рабочего диапазона, Гц
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

        # Инициализация виджетов
        self.t_x_widget = ParameterT()
        self.t_y_widget = ParameterT()
        self.n_x_widget = ParameterN()
        self.n_y_widget = ParameterN()
        self.delta_n_widget = ParametersDeltaN()

        # Проверка вводимых значений
        self.double_validator = QDoubleValidator(0, 1e12, 8)
        # Создание текстовых меток
        self.dist_x_label = QLabel("Параметры распределения поля в плоскости X:")
        self.dist_y_label = QLabel("Параметры распределения поля в плоскости Y:")
        self.dist_r_label = QLabel("Параметры распределения поля в круглом раскрыве:")
        self.dist_r_label.hide()
        # Вставляем виджеты в компоновщик
        self.dist_layout.addWidget(self.dist_x_label, 0, 0, Qt.AlignHCenter)
        self.dist_layout.addWidget(self.dist_y_label, 0, 1, Qt.AlignHCenter)
        self.dist_layout.addWidget(self.dist_r_label, 0, 0, Qt.AlignHCenter)
        self.dist_layout.addWidget(self.t_x_widget, 1, 0)
        self.dist_layout.addWidget(self.n_x_widget, 1, 0)
        self.dist_layout.addWidget(self.delta_n_widget, 1, 0)
        self.dist_layout.addWidget(self.t_y_widget, 1, 1)
        self.dist_layout.addWidget(self.n_y_widget, 1, 1)
        # Добавляем вертикальные пробелы
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.dist_layout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.dist_layout.addItem(spacerItem1, 2, 1, 1, 1)

        # Применяем валидаторы к полям ввода значений
        self.f0_value.setValidator(self.double_validator)
        self.delta_f_value.setValidator(self.double_validator)
        self.size_value.setValidator(self.double_validator)
        self.f_value.setValidator(self.double_validator)

        self.dist_x_value.currentIndexChanged.connect(self.set_dist_x)
        self.dist_y_value.currentIndexChanged.connect(self.set_dist_y)
        self.calc_value.clicked.connect(self.calculate)

    def set_dist_x(self, i):
        if i == 5:
            # TODO: убрать код условия в отдельную функцию?
            self.dist_y_value.setEnabled(False)
            self.sector_value.setCurrentIndex(1)
            self.sector_value.setEnabled(False)
            self.dist_x_label.hide()
            self.dist_y_label.hide()
            self.dist_r_label.show()
            self.t_x_widget.hide()
            self.n_x_widget.hide()
            self.t_y_widget.hide()
            self.n_y_widget.hide()
            self.delta_n_widget.show()
        else:
            if i == 0:
                self.t_x_widget.hide()
                self.delta_n_widget.hide()
                self.n_x_widget.hide()
            elif i == 4:
                self.t_x_widget.hide()
                self.delta_n_widget.hide()
                self.n_x_widget.show()
            else:
                self.n_x_widget.hide()
                self.delta_n_widget.hide()
                self.t_x_widget.show()
            self.dist_x_label.show()
            self.dist_y_label.show()
            self.dist_r_label.hide()
            self.dist_y_value.setEnabled(True)
            self.sector_value.setEnabled(True)

    def set_dist_y(self, i):
        if i == 5:
            # TODO: убрать код условия в отдельную функцию?
            self.dist_x_value.setEnabled(False)
            self.sector_value.setCurrentIndex(1)
            self.sector_value.setEnabled(False)
            self.dist_x_label.hide()
            self.dist_y_label.hide()
            self.dist_r_label.show()
            self.t_x_widget.hide()
            self.n_x_widget.hide()
            self.t_y_widget.hide()
            self.n_y_widget.hide()
            self.delta_n_widget.show()
        else:
            if i == 0:
                self.t_y_widget.hide()
                self.delta_n_widget.hide()
                self.n_y_widget.hide()
            elif i == 4:
                self.t_y_widget.hide()
                self.delta_n_widget.hide()
                self.n_y_widget.show()
            else:
                self.n_y_widget.hide()
                self.delta_n_widget.hide()
                self.t_y_widget.show()
            self.dist_x_label.show()
            self.dist_y_label.show()
            self.dist_r_label.hide()
            self.dist_x_value.setEnabled(True)
            self.sector_value.setEnabled(True)

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
