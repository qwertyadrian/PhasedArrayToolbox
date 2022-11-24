# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/ui_files/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(825, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.parametr = QtWidgets.QWidget()
        self.parametr.setObjectName("parametr")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.parametr)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.f0_value = QtWidgets.QLineEdit(self.parametr)
        self.f0_value.setObjectName("f0_value")
        self.gridLayout.addWidget(self.f0_value, 2, 1, 1, 1)
        self.grid_label = QtWidgets.QLabel(self.parametr)
        self.grid_label.setObjectName("grid_label")
        self.gridLayout.addWidget(self.grid_label, 4, 0, 1, 1)
        self.theta_max_label = QtWidgets.QLabel(self.parametr)
        self.theta_max_label.setObjectName("theta_max_label")
        self.gridLayout.addWidget(self.theta_max_label, 0, 0, 1, 1)
        self.delta_f_label = QtWidgets.QLabel(self.parametr)
        self.delta_f_label.setObjectName("delta_f_label")
        self.gridLayout.addWidget(self.delta_f_label, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dist_x_value = QtWidgets.QComboBox(self.parametr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dist_x_value.sizePolicy().hasHeightForWidth())
        self.dist_x_value.setSizePolicy(sizePolicy)
        self.dist_x_value.setObjectName("dist_x_value")
        self.dist_x_value.addItem("")
        self.dist_x_value.addItem("")
        self.dist_x_value.addItem("")
        self.dist_x_value.addItem("")
        self.dist_x_value.addItem("")
        self.dist_x_value.addItem("")
        self.horizontalLayout_3.addWidget(self.dist_x_value)
        self.dist_y_value = QtWidgets.QComboBox(self.parametr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dist_y_value.sizePolicy().hasHeightForWidth())
        self.dist_y_value.setSizePolicy(sizePolicy)
        self.dist_y_value.setObjectName("dist_y_value")
        self.dist_y_value.addItem("")
        self.dist_y_value.addItem("")
        self.dist_y_value.addItem("")
        self.dist_y_value.addItem("")
        self.dist_y_value.addItem("")
        self.dist_y_value.addItem("")
        self.horizontalLayout_3.addWidget(self.dist_y_value)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.theta_0_value = QtWidgets.QDoubleSpinBox(self.parametr)
        self.theta_0_value.setMinimum(-90.0)
        self.theta_0_value.setMaximum(90.0)
        self.theta_0_value.setObjectName("theta_0_value")
        self.horizontalLayout_4.addWidget(self.theta_0_value)
        self.phi_0_value = QtWidgets.QDoubleSpinBox(self.parametr)
        self.phi_0_value.setMaximum(360.0)
        self.phi_0_value.setObjectName("phi_0_value")
        self.horizontalLayout_4.addWidget(self.phi_0_value)
        self.gridLayout.addLayout(self.horizontalLayout_4, 7, 1, 1, 1)
        self.theta_max_value = QtWidgets.QDoubleSpinBox(self.parametr)
        self.theta_max_value.setDecimals(1)
        self.theta_max_value.setMaximum(90.0)
        self.theta_max_value.setObjectName("theta_max_value")
        self.gridLayout.addWidget(self.theta_max_value, 0, 1, 1, 1)
        self.thetaphi_label = QtWidgets.QLabel(self.parametr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thetaphi_label.sizePolicy().hasHeightForWidth())
        self.thetaphi_label.setSizePolicy(sizePolicy)
        self.thetaphi_label.setObjectName("thetaphi_label")
        self.gridLayout.addWidget(self.thetaphi_label, 7, 0, 1, 1)
        self.f0_label = QtWidgets.QLabel(self.parametr)
        self.f0_label.setObjectName("f0_label")
        self.gridLayout.addWidget(self.f0_label, 2, 0, 1, 1)
        self.delta_f_value = QtWidgets.QLineEdit(self.parametr)
        self.delta_f_value.setObjectName("delta_f_value")
        self.gridLayout.addWidget(self.delta_f_value, 3, 1, 1, 1)
        self.grid_value = QtWidgets.QComboBox(self.parametr)
        self.grid_value.setObjectName("grid_value")
        self.grid_value.addItem("")
        self.grid_value.addItem("")
        self.gridLayout.addWidget(self.grid_value, 4, 1, 1, 1)
        self.size_value = QtWidgets.QLineEdit(self.parametr)
        self.size_value.setObjectName("size_value")
        self.gridLayout.addWidget(self.size_value, 8, 1, 1, 1)
        self.size_label = QtWidgets.QLabel(self.parametr)
        self.size_label.setObjectName("size_label")
        self.gridLayout.addWidget(self.size_label, 8, 0, 1, 1)
        self.sector_label = QtWidgets.QLabel(self.parametr)
        self.sector_label.setObjectName("sector_label")
        self.gridLayout.addWidget(self.sector_label, 1, 0, 1, 1)
        self.dist_label = QtWidgets.QLabel(self.parametr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dist_label.sizePolicy().hasHeightForWidth())
        self.dist_label.setSizePolicy(sizePolicy)
        self.dist_label.setObjectName("dist_label")
        self.gridLayout.addWidget(self.dist_label, 6, 0, 1, 1)
        self.sector_value = QtWidgets.QComboBox(self.parametr)
        self.sector_value.setObjectName("sector_value")
        self.sector_value.addItem("")
        self.sector_value.addItem("")
        self.gridLayout.addWidget(self.sector_value, 1, 1, 1, 1)
        self.f_label = QtWidgets.QLabel(self.parametr)
        self.f_label.setObjectName("f_label")
        self.gridLayout.addWidget(self.f_label, 9, 0, 1, 1)
        self.f_value = QtWidgets.QLineEdit(self.parametr)
        self.f_value.setObjectName("f_value")
        self.gridLayout.addWidget(self.f_value, 9, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.parametr, "")
        self.distribution = QtWidgets.QWidget()
        self.distribution.setObjectName("distribution")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.distribution)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget.addTab(self.distribution, "")
        self.contour = QtWidgets.QWidget()
        self.contour.setObjectName("contour")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.contour)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.contour)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.tabWidget.addTab(self.contour, "")
        self.DN = QtWidgets.QWidget()
        self.DN.setObjectName("DN")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.DN)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.DN)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3.addWidget(self.widget_2)
        self.tabWidget.addTab(self.DN, "")
        self.amplt_dist = QtWidgets.QWidget()
        self.amplt_dist.setObjectName("amplt_dist")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.amplt_dist)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.amplt_dist)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4.addWidget(self.widget_3)
        self.tabWidget.addTab(self.amplt_dist, "")
        self.man = QtWidgets.QWidget()
        self.man.setObjectName("man")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.man)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_14 = QtWidgets.QLabel(self.man)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/root/img/equation3.svg"))
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.man)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.man)
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap(":/root/img/equation6.svg"))
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 6, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.man)
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap(":/root/img/equation2.svg"))
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.man)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.man)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/root/img/equation4.svg"))
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.man)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.man)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.man)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/root/img/equation5.svg"))
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 5, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.man)
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(":/root/img/equation1.svg"))
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.man)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 6, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.man)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.man)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 1, 1, 1)
        self.tabWidget.addTab(self.man, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.calc_value = QtWidgets.QPushButton(self.centralwidget)
        self.calc_value.setMinimumSize(QtCore.QSize(100, 0))
        self.calc_value.setMaximumSize(QtCore.QSize(100, 16777215))
        self.calc_value.setObjectName("calc_value")
        self.verticalLayout.addWidget(self.calc_value, 0, QtCore.Qt.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расчёт ФАР"))
        self.grid_label.setText(_translate("MainWindow", "Сетка расположения элементов:"))
        self.theta_max_label.setText(_translate("MainWindow", "Максимальный угол отклонения луча, град:"))
        self.delta_f_label.setText(_translate("MainWindow", "Полоса рабочих частот, Гц:"))
        self.dist_x_value.setItemText(0, _translate("MainWindow", " 1"))
        self.dist_x_value.setItemText(1, _translate("MainWindow", " 2"))
        self.dist_x_value.setItemText(2, _translate("MainWindow", " 3"))
        self.dist_x_value.setItemText(3, _translate("MainWindow", " 4"))
        self.dist_x_value.setItemText(4, _translate("MainWindow", " 5"))
        self.dist_x_value.setItemText(5, _translate("MainWindow", " 6"))
        self.dist_y_value.setItemText(0, _translate("MainWindow", " 1"))
        self.dist_y_value.setItemText(1, _translate("MainWindow", " 2"))
        self.dist_y_value.setItemText(2, _translate("MainWindow", " 3"))
        self.dist_y_value.setItemText(3, _translate("MainWindow", " 4"))
        self.dist_y_value.setItemText(4, _translate("MainWindow", " 5"))
        self.dist_y_value.setItemText(5, _translate("MainWindow", " 6"))
        self.thetaphi_label.setText(_translate("MainWindow", "Направление сканирования theta, phi\n"
"в градусах:"))
        self.f0_label.setText(_translate("MainWindow", "Средняя частота рабочего диапазона, Гц:"))
        self.grid_value.setItemText(0, _translate("MainWindow", "Прямоугольная"))
        self.grid_value.setItemText(1, _translate("MainWindow", "Гексагональная"))
        self.size_label.setText(_translate("MainWindow", "Размер антенны, м:"))
        self.sector_label.setText(_translate("MainWindow", "Сектор электрического сканирования луча:"))
        self.dist_label.setText(_translate("MainWindow", "Распределение поля в плоскостях x, y:"))
        self.sector_value.setItemText(0, _translate("MainWindow", "Симметричный"))
        self.sector_value.setItemText(1, _translate("MainWindow", "Конический"))
        self.f_label.setText(_translate("MainWindow", "Частота сигнала, Гц:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parametr), _translate("MainWindow", "Параметры"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.distribution), _translate("MainWindow", "Распределение"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contour), _translate("MainWindow", "Контур"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DN), _translate("MainWindow", "ДН"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.amplt_dist), _translate("MainWindow", "Амп. распределение"))
        self.label_10.setText(_translate("MainWindow", "5."))
        self.label_17.setText(_translate("MainWindow", "4."))
        self.label_9.setText(_translate("MainWindow", "1."))
        self.label_16.setText(_translate("MainWindow", "2."))
        self.label_11.setText(_translate("MainWindow", "6."))
        self.label_15.setText(_translate("MainWindow", "3."))
        self.label_21.setText(_translate("MainWindow", "Амплитудные распределения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.man), _translate("MainWindow", "Справка"))
        self.calc_value.setText(_translate("MainWindow", "Расчёт"))
from app.resources import resources
