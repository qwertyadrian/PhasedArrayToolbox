from PyQt5.QtWidgets import QWidget
from .widget1 import Ui_Form as Ui_Form1
from .widget2 import Ui_Form as Ui_Form2
from .widget3 import Ui_Form as Ui_Form3


class ParameterT(QWidget, Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ParameterN(QWidget, Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ParametersDeltaN(QWidget, Ui_Form3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


