# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './questions/translate.ui',
# licensing of './questions/translate.ui' applies.
#
# Created: Wed Oct 16 12:21:00 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 283)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_1.setMaximumSize(QtCore.QSize(103, 21))
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.gridLayout.addWidget(self.textBrowser_1, 0, 1, 1, 1)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        self.commandLinkButton_2.setMaximumSize(QtCore.QSize(25, 16777215))
        self.commandLinkButton_2.setText("")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.gridLayout.addWidget(self.commandLinkButton_2, 1, 0, 1, 1)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_5.setMaximumSize(QtCore.QSize(103, 21))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout.addWidget(self.textBrowser_5, 4, 1, 1, 1)
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        self.commandLinkButton_4.setMaximumSize(QtCore.QSize(25, 16777215))
        self.commandLinkButton_4.setText("")
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.gridLayout.addWidget(self.commandLinkButton_4, 3, 0, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_4.setMaximumSize(QtCore.QSize(103, 21))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.textBrowser_4, 3, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 2, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 2, 1, 1)
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        self.commandLinkButton_3.setMaximumSize(QtCore.QSize(25, 16777215))
        self.commandLinkButton_3.setText("")
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.gridLayout.addWidget(self.commandLinkButton_3, 2, 0, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_3.setMaximumSize(QtCore.QSize(103, 21))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.commandLinkButton_1 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_1.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_1.setSizePolicy(sizePolicy)
        self.commandLinkButton_1.setMaximumSize(QtCore.QSize(25, 16777215))
        self.commandLinkButton_1.setText("")
        self.commandLinkButton_1.setObjectName("commandLinkButton_1")
        self.gridLayout.addWidget(self.commandLinkButton_1, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 2, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(103, 21))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 1, 1, 1, 1)
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        self.commandLinkButton_5.setMaximumSize(QtCore.QSize(25, 16777215))
        self.commandLinkButton_5.setText("")
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.gridLayout.addWidget(self.commandLinkButton_5, 4, 0, 1, 1)
        self.check = QtWidgets.QPushButton(Dialog)
        self.check.setGeometry(QtCore.QRect(280, 240, 112, 32))
        self.check.setObjectName("check")
        self.show = QtWidgets.QPushButton(Dialog)
        self.show.setGeometry(QtCore.QRect(170, 240, 112, 32))
        self.show.setObjectName("show")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.check.setText(QtWidgets.QApplication.translate("Dialog", "Check", None, -1))
        self.show.setText(QtWidgets.QApplication.translate("Dialog", "Show", None, -1))

