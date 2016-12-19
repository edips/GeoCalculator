# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculatorUi.ui'
#
# Created: Mon Jan  6 00:27:51 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_hesap(object):
    def setupUi(self, hesap):
        hesap.setObjectName("hesap")
        hesap.resize(157, 135)
        self.label = QtGui.QLabel(hesap)
        self.label.setGeometry(QtCore.QRect(10, 10, 21, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(hesap)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(hesap)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 21, 16))
        self.label_3.setObjectName("label_3")
        self.sum = QtGui.QPushButton(hesap)
        self.sum.setGeometry(QtCore.QRect(30, 70, 111, 24))
        self.sum.setObjectName("sum")
        self.a = QtGui.QLineEdit(hesap)
        self.a.setGeometry(QtCore.QRect(30, 10, 113, 23))
        self.a.setObjectName("a")
        self.b = QtGui.QLineEdit(hesap)
        self.b.setGeometry(QtCore.QRect(30, 40, 113, 23))
        self.b.setObjectName("b")
        self.c = QtGui.QLineEdit(hesap)
        self.c.setGeometry(QtCore.QRect(30, 100, 113, 23))
        self.c.setObjectName("c")

        self.retranslateUi(hesap)
        QtCore.QMetaObject.connectSlotsByName(hesap)

    def retranslateUi(self, hesap):
        hesap.setWindowTitle(QtGui.QApplication.translate("hesap", "addition", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("hesap", "a", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("hesap", "b", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("hesap", "c", None, QtGui.QApplication.UnicodeUTF8))
        self.sum.setText(QtGui.QApplication.translate("hesap", "calculate", None, QtGui.QApplication.UnicodeUTF8))

