# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(499, 113)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.delta_value = QtWidgets.QDoubleSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delta_value.sizePolicy().hasHeightForWidth())
        self.delta_value.setSizePolicy(sizePolicy)
        self.delta_value.setMaximum(1.0)
        self.delta_value.setSingleStep(0.1)
        self.delta_value.setObjectName("delta_value")
        self.gridLayout.addWidget(self.delta_value, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.n_value = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_value.sizePolicy().hasHeightForWidth())
        self.n_value.setSizePolicy(sizePolicy)
        self.n_value.setObjectName("n_value")
        self.gridLayout.addWidget(self.n_value, 1, 1, 1, 1)
        self.delta_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delta_label.sizePolicy().hasHeightForWidth())
        self.delta_label.setSizePolicy(sizePolicy)
        self.delta_label.setText("")
        self.delta_label.setPixmap(QtGui.QPixmap(":/root/img/delta.svg"))
        self.delta_label.setObjectName("delta_label")
        self.gridLayout.addWidget(self.delta_label, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "n"))
from resources import resources
