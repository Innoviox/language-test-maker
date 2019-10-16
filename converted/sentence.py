# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './questions/sentence.ui',
# licensing of './questions/sentence.ui' applies.
#
# Created: Wed Oct 16 13:50:28 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.check = QtWidgets.QPushButton(Dialog)
        self.check.setGeometry(QtCore.QRect(210, 200, 112, 32))
        self.check.setObjectName("check")
        self.show = QtWidgets.QPushButton(Dialog)
        self.show.setGeometry(QtCore.QRect(90, 200, 112, 32))
        self.show.setObjectName("show")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(102, 170, 211, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(175, 130, 58, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.check.setText(QtWidgets.QApplication.translate("Dialog", "Check", None, -1))
        self.show.setText(QtWidgets.QApplication.translate("Dialog", "Show", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "TextLabel", None, -1))

