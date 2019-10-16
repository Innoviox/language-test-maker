# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './questions/translate.ui',
# licensing of './questions/translate.ui' applies.
#
# Created: Wed Oct 16 10:21:00 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 10, 351, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.word1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.word1.setObjectName("word1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.word1)
        self.word1LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.word1LineEdit.setObjectName("word1LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.word1LineEdit)
        self.word2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.word2.setObjectName("word2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.word2)
        self.word2LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.word2LineEdit.setObjectName("word2LineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.word2LineEdit)
        self.word3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.word3.setObjectName("word3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.word3)
        self.word3LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.word3LineEdit.setObjectName("word3LineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.word3LineEdit)
        self.word4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.word4.setObjectName("word4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.word4)
        self.word4LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.word4LineEdit.setObjectName("word4LineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.word4LineEdit)
        self.word5Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.word5Label.setObjectName("word5Label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.word5Label)
        self.word5LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.word5LineEdit.setObjectName("word5LineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.word5LineEdit)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.word1.setText(QtWidgets.QApplication.translate("Dialog", "Word 1", None, -1))
        self.word2.setText(QtWidgets.QApplication.translate("Dialog", "Word 2", None, -1))
        self.word3.setText(QtWidgets.QApplication.translate("Dialog", "Word 3", None, -1))
        self.word4.setText(QtWidgets.QApplication.translate("Dialog", "Word 4", None, -1))
        self.word5Label.setText(QtWidgets.QApplication.translate("Dialog", "Word 5", None, -1))

